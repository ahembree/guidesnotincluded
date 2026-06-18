#!/usr/bin/env python3
"""Crawl the Wayback Machine for an archived site and convert it to Markdown.

This tool was built to resurrect https://guidesnotincluded.com (an Oxygen Not
Included guides site) from the Internet Archive and host the content as a
MkDocs site in this repository.

What it does
------------
1. Queries the Wayback CDX API for every captured URL under the target domain.
2. Keeps the *latest* successful (HTTP 200, text/html) capture of each page.
3. Downloads the raw archived HTML (``id_`` capture mode = no Wayback toolbar).
4. Extracts the main content + title and converts it to Markdown.
5. Optionally downloads referenced images into ``docs/assets`` and rewrites
   the image links to local relative paths.
6. Writes Markdown files into the MkDocs ``docs/`` tree, mirroring the site's
   URL structure, with YAML front matter recording the archive provenance.

Requirements: see ``scripts/requirements.txt``.

NOTE: ``web.archive.org`` must be reachable. On Claude Code on the web this
means the environment's Network access must be **Full** (or **Custom** with
``web.archive.org`` + ``archive.org`` allowed). See RUNBOOK.md.

Usage
-----
    python3 scripts/crawl_archive.py --domain guidesnotincluded.com
    python3 scripts/crawl_archive.py --domain guidesnotincluded.com --limit 3 --no-assets
    python3 scripts/crawl_archive.py --list-only   # just print the page inventory
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urljoin, urlparse, urlsplit, unquote

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from readability import Document

WAYBACK = "https://web.archive.org"
CDX_API = f"{WAYBACK}/cdx/search/cdx"
USER_AGENT = "guidesnotincluded-archive-crawler/1.0 (+https://github.com/ahembree/guidesnotincluded)"

# Skip these file extensions when treating a capture as a "page".
NON_PAGE_EXT = {
    ".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".ico", ".bmp",
    ".css", ".js", ".json", ".xml", ".txt", ".pdf", ".zip", ".gz",
    ".woff", ".woff2", ".ttf", ".eot", ".map", ".mp4", ".webm", ".mp3",
}


@dataclass
class Capture:
    """One archived page we intend to convert."""

    original: str       # original (live-site) URL, e.g. https://www.guidesnotincluded.com/guides
    timestamp: str      # Wayback timestamp, e.g. 20230115120000
    statuscode: str
    mimetype: str

    @property
    def raw_url(self) -> str:
        """Raw (toolbar-free) capture URL."""
        return f"{WAYBACK}/web/{self.timestamp}id_/{self.original}"


@dataclass
class CrawlStats:
    pages: int = 0
    assets: int = 0
    errors: list[str] = field(default_factory=list)


def log(msg: str) -> None:
    print(msg, flush=True)


def session_with_retries() -> requests.Session:
    s = requests.Session()
    s.headers.update({"User-Agent": USER_AGENT})
    return s


def http_get(s: requests.Session, url: str, *, tries: int = 4, timeout: int = 60) -> requests.Response:
    """GET with exponential backoff. Raises on final failure."""
    delay = 2
    last_exc: Exception | None = None
    for attempt in range(1, tries + 1):
        try:
            r = s.get(url, timeout=timeout)
            r.raise_for_status()
            return r
        except Exception as exc:  # noqa: BLE001 - we retry everything
            last_exc = exc
            if attempt < tries:
                log(f"  ! GET failed ({exc}); retry {attempt}/{tries - 1} in {delay}s")
                time.sleep(delay)
                delay *= 2
    raise RuntimeError(f"GET {url} failed after {tries} tries: {last_exc}")


# --------------------------------------------------------------------------- #
# CDX inventory
# --------------------------------------------------------------------------- #
def normalize_key(original: str) -> str:
    """Canonical key for de-duplicating www/non-www and trailing slashes."""
    p = urlsplit(original)
    host = p.netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    path = p.path.rstrip("/") or "/"
    query = f"?{p.query}" if p.query else ""
    return f"{host}{path}{query}"


def is_page(original: str) -> bool:
    path = urlsplit(original).path.lower()
    ext = os.path.splitext(path)[1]
    return ext not in NON_PAGE_EXT


def fetch_inventory(s: requests.Session, domain: str, *, include_subdomains: bool = True) -> list[Capture]:
    """Return the latest 200/text-html capture for each unique page URL."""
    params = {
        "url": f"{domain}",
        "matchType": "domain" if include_subdomains else "prefix",
        "output": "json",
        "fl": "original,timestamp,statuscode,mimetype",
        "filter": ["statuscode:200", "mimetype:text/html"],
        "collapse": "digest",  # drop identical re-captures; we still dedupe in Python
    }
    log(f"Querying CDX API for {domain} (matchType={params['matchType']}) ...")
    r = s.get(CDX_API, params=params, timeout=120)
    r.raise_for_status()
    rows = r.json()
    if not rows:
        return []
    header, *data = rows
    idx = {name: i for i, name in enumerate(header)}

    latest: dict[str, Capture] = {}
    for row in data:
        original = row[idx["original"]]
        if not is_page(original):
            continue
        ts = row[idx["timestamp"]]
        cap = Capture(
            original=original,
            timestamp=ts,
            statuscode=row[idx["statuscode"]],
            mimetype=row[idx["mimetype"]],
        )
        key = normalize_key(original)
        prev = latest.get(key)
        # Keep the most recent capture. Prefer a www/https original when tied.
        if prev is None or ts > prev.timestamp:
            latest[key] = cap
    return sorted(latest.values(), key=lambda c: normalize_key(c.original))


# --------------------------------------------------------------------------- #
# URL -> file path mapping
# --------------------------------------------------------------------------- #
def slugify(text: str) -> str:
    text = unquote(text)
    text = text.strip().strip("/")
    text = re.sub(r"[^A-Za-z0-9._/-]+", "-", text)
    text = re.sub(r"-{2,}", "-", text).strip("-/")
    return text.lower()


def url_to_relpath(original: str) -> str:
    """Map a page URL to a docs-relative .md path (without the docs/ prefix)."""
    p = urlsplit(original)
    path = p.path
    segments = [seg for seg in path.split("/") if seg]
    # carry a query string into the filename so distinct pages don't collide
    suffix = ""
    if p.query:
        suffix = "-" + hashlib.sha1(p.query.encode()).hexdigest()[:8]

    if not segments:
        return "index.md"

    # strip a trailing .html / .htm / .php etc. from the last segment
    last = segments[-1]
    last = re.sub(r"\.(html?|php|aspx?)$", "", last, flags=re.IGNORECASE)
    segments[-1] = last

    rel = "/".join(slugify(s) for s in segments)
    return f"{rel}{suffix}.md"


def resolve_index_collisions(paths: dict[str, str]) -> dict[str, str]:
    """If a page path also needs to be a directory (because other pages nest
    under it), convert it to ``<dir>/index.md`` so MkDocs treats it as the
    section landing page.
    """
    dirs = set()
    for rel in paths.values():
        parent = os.path.dirname(rel)
        while parent:
            dirs.add(parent)
            parent = os.path.dirname(parent)

    resolved = {}
    for key, rel in paths.items():
        stem = rel[:-3]  # drop .md
        if stem in dirs:
            resolved[key] = f"{stem}/index.md"
        else:
            resolved[key] = rel
    return resolved


# --------------------------------------------------------------------------- #
# HTML -> Markdown
# --------------------------------------------------------------------------- #
def extract_title(soup: BeautifulSoup, fallback: str) -> str:
    for selector in ("meta[property='og:title']", "meta[name='title']"):
        tag = soup.select_one(selector)
        if tag and tag.get("content"):
            return tag["content"].strip()
    if soup.title and soup.title.string:
        return soup.title.string.strip()
    h1 = soup.find("h1")
    if h1 and h1.get_text(strip=True):
        return h1.get_text(strip=True)
    return fallback


def extract_main_html(html: str) -> str:
    """Best-effort extraction of the primary content region."""
    # readability gives a clean <article>-like summary for prose pages.
    try:
        doc = Document(html)
        summary = doc.summary(html_partial=True)
        text_len = len(BeautifulSoup(summary, "lxml").get_text(strip=True))
        if text_len >= 200:
            return summary
    except Exception:  # noqa: BLE001
        pass

    # Fallback: whole <body> minus obvious chrome.
    soup = BeautifulSoup(html, "lxml")
    for tag in soup(["script", "style", "noscript", "iframe", "header", "footer", "nav"]):
        tag.decompose()
    body = soup.body or soup
    return str(body)


def clean_archive_links(markdown: str) -> str:
    """Strip Wayback wrappers that may survive in links and collapse blanks."""
    markdown = re.sub(
        r"\(https?://web\.archive\.org/web/\d+(?:[a-z]{2}_)?/(https?://[^)]+)\)",
        r"(\1)",
        markdown,
    )
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    return markdown.strip() + "\n"


# --------------------------------------------------------------------------- #
# Asset handling
# --------------------------------------------------------------------------- #
def asset_filename(src: str) -> str:
    p = urlsplit(src)
    base = os.path.basename(p.path) or "image"
    base = unquote(base)
    name, ext = os.path.splitext(base)
    if not ext or len(ext) > 6:
        ext = ".img"
    digest = hashlib.sha1(src.encode()).hexdigest()[:10]
    name = re.sub(r"[^A-Za-z0-9._-]+", "-", name)[:48].strip("-") or "image"
    return f"{name}-{digest}{ext}"


def to_wayback_resource(src: str, page_original: str, timestamp: str) -> str | None:
    """Build a Wayback URL that will serve the *raw* asset bytes."""
    src = src.strip()
    if not src or src.startswith("data:"):
        return None
    # Already a Wayback URL? force im_ raw mode.
    m = re.match(r"^https?://web\.archive\.org/web/\d+(?:[a-z]{2}_)?/(.*)$", src)
    if m:
        src = m.group(1)
    absolute = urljoin(page_original, src)
    if not absolute.startswith("http"):
        return None
    return f"{WAYBACK}/web/{timestamp}im_/{absolute}"


def download_assets(
    s: requests.Session,
    soup: BeautifulSoup,
    page_original: str,
    timestamp: str,
    docs_dir: Path,
    rel_md_path: str,
    stats: CrawlStats,
) -> None:
    """Download <img> sources and rewrite them to local relative paths."""
    assets_dir = docs_dir / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)
    # path from this markdown file back to docs/assets
    depth = rel_md_path.count("/")
    rel_prefix = "../" * depth + "assets/"

    for img in soup.find_all("img"):
        src = img.get("src") or img.get("data-src")
        if not src:
            continue
        wb = to_wayback_resource(src, page_original, timestamp)
        if not wb:
            continue
        fname = asset_filename(src)
        dest = assets_dir / fname
        try:
            if not dest.exists():
                r = http_get(s, wb, tries=3, timeout=60)
                dest.write_bytes(r.content)
                stats.assets += 1
            img["src"] = rel_prefix + fname
            for attr in ("srcset", "data-src", "data-srcset"):
                if img.has_attr(attr):
                    del img[attr]
        except Exception as exc:  # noqa: BLE001
            stats.errors.append(f"asset {src}: {exc}")


# --------------------------------------------------------------------------- #
# Conversion driver
# --------------------------------------------------------------------------- #
def convert_capture(
    s: requests.Session,
    cap: Capture,
    rel_md_path: str,
    docs_dir: Path,
    download_imgs: bool,
    stats: CrawlStats,
) -> str:
    r = http_get(s, cap.raw_url)
    html = r.text

    full_soup = BeautifulSoup(html, "lxml")
    title = extract_title(full_soup, fallback=rel_md_path)

    main_html = extract_main_html(html)
    main_soup = BeautifulSoup(main_html, "lxml")

    if download_imgs:
        download_assets(s, main_soup, cap.original, cap.timestamp, docs_dir, rel_md_path, stats)

    markdown = md(str(main_soup), heading_style="ATX", strip=["script", "style"])
    markdown = clean_archive_links(markdown)

    archive_date = (
        f"{cap.timestamp[0:4]}-{cap.timestamp[4:6]}-{cap.timestamp[6:8]}"
        if len(cap.timestamp) >= 8 else cap.timestamp
    )
    front_matter = (
        "---\n"
        f"title: {json.dumps(title)}\n"
        f"source_url: {cap.original}\n"
        f"archived: {archive_date}\n"
        f"archive_snapshot: {cap.raw_url}\n"
        "---\n\n"
    )
    body = markdown
    if not re.match(r"^\s*#\s", body):
        body = f"# {title}\n\n{body}"
    return front_matter + body


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #
def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--domain", default="guidesnotincluded.com", help="Target domain (default: %(default)s)")
    ap.add_argument("--docs-dir", default="docs", help="MkDocs docs/ output directory (default: %(default)s)")
    ap.add_argument("--limit", type=int, default=0, help="Only convert the first N pages (0 = all)")
    ap.add_argument("--no-assets", action="store_true", help="Do not download images")
    ap.add_argument("--no-subdomains", action="store_true", help="Match only the exact domain prefix")
    ap.add_argument("--list-only", action="store_true", help="Print the page inventory and exit")
    ap.add_argument("--sleep", type=float, default=0.5, help="Seconds to sleep between pages (politeness)")
    ap.add_argument("--inventory-out", default="", help="Optional path to write the inventory as JSON")
    args = ap.parse_args(argv)

    s = session_with_retries()
    docs_dir = Path(args.docs_dir)

    try:
        captures = fetch_inventory(s, args.domain, include_subdomains=not args.no_subdomains)
    except Exception as exc:  # noqa: BLE001
        log(f"ERROR: could not fetch CDX inventory: {exc}")
        if "host_not_allowed" in str(exc) or "403" in str(exc):
            log("       web.archive.org is blocked. Set Network access to Full. See RUNBOOK.md.")
        return 2

    log(f"Found {len(captures)} unique pages.")

    # compute output paths + resolve section-index collisions
    rel_paths = {normalize_key(c.original): url_to_relpath(c.original) for c in captures}
    rel_paths = resolve_index_collisions(rel_paths)

    if args.inventory_out:
        inv = [
            {"original": c.original, "timestamp": c.timestamp, "path": rel_paths[normalize_key(c.original)]}
            for c in captures
        ]
        Path(args.inventory_out).write_text(json.dumps(inv, indent=2), encoding="utf-8")
        log(f"Wrote inventory to {args.inventory_out}")

    if args.list_only:
        for c in captures:
            log(f"  {c.timestamp}  {c.original}  ->  {docs_dir}/{rel_paths[normalize_key(c.original)]}")
        return 0

    if args.limit:
        captures = captures[: args.limit]

    stats = CrawlStats()
    for i, cap in enumerate(captures, 1):
        rel = rel_paths[normalize_key(cap.original)]
        out_path = docs_dir / rel
        log(f"[{i}/{len(captures)}] {cap.original} -> {out_path}")
        try:
            content = convert_capture(s, cap, rel, docs_dir, not args.no_assets, stats)
            write_file(out_path, content)
            stats.pages += 1
        except Exception as exc:  # noqa: BLE001
            stats.errors.append(f"page {cap.original}: {exc}")
            log(f"  ! failed: {exc}")
        if args.sleep:
            time.sleep(args.sleep)

    log("")
    log(f"Done. Pages: {stats.pages}, assets: {stats.assets}, errors: {len(stats.errors)}")
    for err in stats.errors:
        log(f"  - {err}")
    return 0 if stats.pages else 1


if __name__ == "__main__":
    sys.exit(main())
