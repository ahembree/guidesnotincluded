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
    seen_assets: dict[str, str] = field(default_factory=dict)  # src -> local filename


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
def _clean_title(text: str) -> str:
    # Drop the repetitive Wix site-name suffix ("Page | Guides Not Included").
    text = re.sub(r"\s*[|–—-]\s*(Guides Not Included|guidesnotincluded\.com)\s*$",
                  "", text.strip(), flags=re.IGNORECASE)
    return text.strip()


def extract_title(soup: BeautifulSoup, fallback: str) -> str:
    for selector in ("meta[property='og:title']", "meta[name='title']"):
        tag = soup.select_one(selector)
        if tag and tag.get("content"):
            return _clean_title(tag["content"]) or fallback
    if soup.title and soup.title.string:
        return _clean_title(soup.title.string) or fallback
    h1 = soup.find("h1")
    if h1 and h1.get_text(strip=True):
        return _clean_title(h1.get_text(strip=True)) or fallback
    return fallback


# Wix renders each page's content inside a <main id="PAGES_CONTAINER">
# landmark, with the site chrome in sibling <header id="SITE_HEADER"> /
# <footer id="SITE_FOOTER">. readability discards the build screenshots that
# ARE the point of these guides, so for Wix pages we extract that landmark
# directly -- it keeps both the prose and the images and excludes the chrome.
WIX_MAIN_SELECTORS = ("main#PAGES_CONTAINER", "main", "#SITE_PAGES")
_CHROME_TAGS = ["script", "style", "noscript", "iframe", "header", "footer", "nav"]
# Labels of the Wix prev/home/next page-pager that gets baked into the content.
_PAGER_WORDS = {"previous", "prev", "home", "next"}


def strip_wix_pager(node) -> None:
    """Remove the Wix "Previous / Home / Next" page-pager that Wix bakes into
    the page body as a handful of one-word blocks.

    To avoid deleting a legitimate lone word ("Home", "Next"), only strip when
    at least two distinct pager labels are present -- i.e. it really is a pager.
    """
    blocks = []
    for b in node.find_all(["p", "div", "section", "nav", "li"]):
        if b.parent is None:
            continue
        words = b.get_text(" ", strip=True).lower().split()
        if words and len(words) <= 3 and set(words) <= _PAGER_WORDS:
            blocks.append(b)
    labels = set()
    for b in blocks:
        labels.update(b.get_text(" ", strip=True).lower().split())
    if len(labels) >= 2:
        for b in blocks:
            if b.parent is not None:  # may already be gone with an ancestor
                b.decompose()


def unwrap_self_links(soup, page_url: str) -> None:
    """Replace <a> tags that point at this very page with their text.

    Wix in-page anchor menus lose their ``#fragment`` in the archive, so every
    "Contents" entry ends up linking to the page root. Unwrapping turns that
    broken navigation back into a plain (non-clickable) list of section names.
    """
    here = normalize_key(page_url)
    for a in soup.find_all("a"):
        href = a.get("href")
        if not href:
            continue
        m = re.match(r"^https?://web\.archive\.org/web/\d+(?:[a-z]{2}_)?/(.*)$", href)
        if m:
            href = m.group(1)
        href = href.split("#", 1)[0]
        if href.startswith("http") and normalize_key(href) == here:
            a.unwrap()


def rewrite_internal_links(soup, current_relpath: str, url_map: dict[str, str]) -> None:
    """Repoint links that target other archived pages at their local Markdown
    files, using paths relative to the current page.

    Keeps navigation inside this documentation instead of the dead original
    domain. External links (YouTube, Reddit, Steam, …) and any in-site link
    whose target was not restored are left untouched. Provenance links live in
    the front matter / footer, which are added after this runs, so they keep
    pointing at the original site and the Wayback snapshot.
    """
    here_dir = os.path.dirname(current_relpath) or "."
    for a in soup.find_all("a"):
        href = a.get("href")
        if not href:
            continue
        m = re.match(r"^https?://web\.archive\.org/web/\d+(?:[a-z]{2}_)?/(.*)$", href)
        if m:
            href = m.group(1)
        if not href.startswith("http"):
            continue
        base, sep, frag = href.partition("#")
        target = url_map.get(normalize_key(base))
        if not target:
            continue
        rel = os.path.relpath(target, here_dir)
        a["href"] = rel + (sep + frag if frag else "")


def extract_main_html(html: str) -> str:
    """Best-effort extraction of the primary content region.

    Order matters: try the Wix page-content landmark first (it preserves the
    images and excludes the header/footer), then readability for generic prose
    pages, then the whole <body> minus obvious chrome.
    """
    soup = BeautifulSoup(html, "lxml")
    for selector in WIX_MAIN_SELECTORS:
        node = soup.select_one(selector)
        if node is None:
            continue
        for tag in node.select(", ".join(_CHROME_TAGS)):
            tag.decompose()
        if len(node.get_text(strip=True)) >= 200:
            strip_wix_pager(node)
            return str(node)

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
    soup2 = BeautifulSoup(html, "lxml")
    for tag in soup2(_CHROME_TAGS):
        tag.decompose()
    for el in soup2.select("#SCROLL_TO_TOP, #SCROLL_TO_BOTTOM, #SITE_HEADER, #SITE_FOOTER"):
        el.decompose()
    body = soup2.body or soup2
    return str(body)


def clean_archive_links(markdown: str) -> str:
    """Strip Wayback wrappers that may survive in links and collapse blanks."""
    markdown = re.sub(
        r"\(https?://web\.archive\.org/web/\d+(?:[a-z]{2}_)?/(https?://[^)]+)\)",
        r"(\1)",
        markdown,
    )
    # Wix pads its layout with zero-width-space "empty paragraphs"; drop them.
    markdown = markdown.replace("​", "").replace("﻿", "")
    markdown = re.sub(r"[ \t]+\n", "\n", markdown)
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    return markdown.strip() + "\n"


def _norm_heading(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


# The site-wide tagline banner Wix renders as a heading at the top of every page.
_SITE_TAGLINE_N = _norm_heading(
    "The Complete Beginner's Completely Incomplete Guide to Oxygen Not Included"
)


def tidy_body(markdown: str) -> str:
    """Drop residual Wix banner noise that survives into the Markdown body:
    the site-wide tagline heading and meaningless "Anchor N" marker lines.
    """
    out = []
    for line in markdown.split("\n"):
        s = line.strip()
        m = re.match(r"^#{1,6}\s+(.*)$", s)
        if m and _norm_heading(m.group(1)) == _SITE_TAGLINE_N:
            continue
        if re.fullmatch(r"anchor\s*\d+", s, flags=re.IGNORECASE):
            continue
        out.append(line)
    text = re.sub(r"\n{3,}", "\n\n", "\n".join(out))
    return text.strip() + "\n"


# --------------------------------------------------------------------------- #
# Asset handling
# --------------------------------------------------------------------------- #
_CT_EXT = {
    "image/avif": ".avif", "image/webp": ".webp", "image/jpeg": ".jpg",
    "image/png": ".png", "image/gif": ".gif", "image/svg+xml": ".svg",
    "image/bmp": ".bmp", "image/x-icon": ".ico",
}


def sniff_image_ext(data: bytes) -> str | None:
    """Return a file extension based on the image's *magic bytes*.

    This is the only reliable signal: Wix's ``enc_avif`` URLs are served as
    PNG/JPEG/AVIF depending on the (capturing browser's) Accept header, so the
    URL and even the archived Content-Type can disagree with the actual bytes.
    """
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return ".png"
    if data[:3] == b"\xff\xd8\xff":
        return ".jpg"
    if data[:6] in (b"GIF87a", b"GIF89a"):
        return ".gif"
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return ".webp"
    if data[:2] == b"BM":
        return ".bmp"
    if data[:4] == b"\x00\x00\x01\x00":
        return ".ico"
    if len(data) >= 12 and data[4:8] == b"ftyp":  # ISO-BMFF (AVIF/HEIF)
        brand = data[8:12]
        if brand in (b"heic", b"heix", b"mif1", b"msf1"):
            return ".heic"
        return ".avif"
    head = data[:512].lstrip().lower()
    if head[:5] == b"<?xml" or head[:4] == b"<svg":
        return ".svg"
    return None


def asset_stem(src: str) -> str:
    """Format-independent local name for a source URL (``name-<digest>``)."""
    base = unquote(os.path.basename(urlsplit(src).path)) or "image"
    name = os.path.splitext(base)[0]
    digest = hashlib.sha1(src.encode()).hexdigest()[:10]
    name = re.sub(r"[^A-Za-z0-9._-]+", "-", name)[:48].strip("-") or "image"
    return f"{name}-{digest}"


def asset_filename(src: str, ext: str) -> str:
    return f"{asset_stem(src)}{ext}"


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
        try:
            fname = stats.seen_assets.get(src)
            if fname is None:  # first time we see this source URL this run
                stem = asset_stem(src)
                # Reuse an already-downloaded file (makes re-runs idempotent
                # and skips the network round-trip).
                existing = next((p for p in assets_dir.iterdir()
                                 if p.name.startswith(stem + ".")), None)
                if existing is not None:
                    fname = existing.name
                else:
                    wb = to_wayback_resource(src, page_original, timestamp)
                    if not wb:
                        continue
                    r = http_get(s, wb, tries=3, timeout=60)
                    data = r.content
                    ct = (r.headers.get("Content-Type") or "").split(";")[0].strip().lower()
                    url_ext = os.path.splitext(urlsplit(src).path)[1].lower()
                    if not re.fullmatch(r"\.[a-z0-9]{1,5}", url_ext):
                        url_ext = ""
                    ext = sniff_image_ext(data) or _CT_EXT.get(ct) or url_ext or ".img"
                    fname = asset_filename(src, ext)
                    (assets_dir / fname).write_bytes(data)
                    stats.assets += 1
                stats.seen_assets[src] = fname
            img["src"] = rel_prefix + fname
            img["loading"] = "lazy"
            for attr in ("srcset", "data-src", "data-srcset", "sizes"):
                if img.has_attr(attr):
                    del img[attr]
            # Wix wraps each image in a lightbox <a> pointing at the (now dead)
            # full-size original; unwrap it so the image just renders.
            parent = img.parent
            if parent is not None and parent.name == "a":
                parent.replace_with(img)
        except Exception as exc:  # noqa: BLE001
            stats.errors.append(f"asset {src}: {exc}")
            # Drop the image rather than leave a broken remote/dead reference.
            img.decompose()


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
    url_map: dict[str, str] | None = None,
) -> str:
    r = http_get(s, cap.raw_url)
    html = r.text

    full_soup = BeautifulSoup(html, "lxml")
    title = extract_title(full_soup, fallback=rel_md_path)

    main_html = extract_main_html(html)
    main_soup = BeautifulSoup(main_html, "lxml")
    unwrap_self_links(main_soup, cap.original)
    if url_map:
        rewrite_internal_links(main_soup, rel_md_path, url_map)

    if download_imgs:
        download_assets(s, main_soup, cap.original, cap.timestamp, docs_dir, rel_md_path, stats)

    markdown = md(str(main_soup), heading_style="ATX", strip=["script", "style"])
    markdown = clean_archive_links(markdown)
    markdown = tidy_body(markdown)

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
    if re.match(r"^\s*#\s", body):
        pass  # already opens with an H1
    elif re.match(r"^\s*#{2,6}\s+", body):
        # Promote the page's own leading title heading to H1 instead of
        # prepending a duplicate synthetic title.
        body = re.sub(r"^\s*#{2,6}\s+", "# ", body, count=1)
    else:
        body = f"# {title}\n\n{body}"

    # Per-page attribution footer (CC BY-NC-SA: credit the source, link the
    # licence, and indicate that the page was reformatted from the archive).
    attr_link = "../" * rel_md_path.count("/") + "attribution.md"
    attribution = (
        "\n\n---\n\n"
        f"*Archived from [{cap.original}]({cap.original}) "
        f"([Wayback Machine snapshot]({cap.raw_url})). "
        "Original work © Some Random Finn / guidesnotincluded.com, licensed "
        "[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). "
        "Reformatted from HTML to Markdown for this non-commercial community "
        f"archive — see [Attribution & licensing]({attr_link}).*\n"
    )
    return front_matter + body.rstrip() + attribution


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
            content = convert_capture(s, cap, rel, docs_dir, not args.no_assets, stats, rel_paths)
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
