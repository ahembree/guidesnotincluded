# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A restoration of **guidesnotincluded.com** — an *Oxygen Not Included* guides
site (built on Wix) that is now offline and survives only on the Internet
Archive. The repo crawls the Wayback Machine, converts each page to Markdown,
and serves the result as a MkDocs Material site on GitHub Pages.

The content in `docs/` is generated, not hand-written: it is the output of
`scripts/crawl_archive.py`. Treat the crawler as the source of truth for how
content is produced; edit content by re-running/improving the crawler unless
making a small manual fix.

## Licensing & attribution — STRICT (CC BY-NC-SA 4.0)

The restored guide text is the work of **Some Random Finn**
(guidesnotincluded.com), published by the author under **CC BY-NC-SA 4.0**
(Attribution-NonCommercial-ShareAlike). The repo owner requires **strict**
adherence. Treat these as hard constraints — never weaken them, and when in
doubt err toward *more* attribution, never less:

- **Attribution (BY) — never strip it.** Every crawled page carries an
  attribution footer emitted by `convert_capture` in `scripts/crawl_archive.py`
  (credits the author, links the original URL + Wayback snapshot, links the
  licence, and states the page was reformatted). The site also renders a
  `copyright` footer (`mkdocs.yml`). Do **not** remove, gate, or empty either,
  and if you change the crawler/conversion the per-page footer must still be
  emitted on **every** page. Preserve the in-page build credits too (Francis
  John, Jahws, Mullematsch, the ONI community).
- **NonCommercial (NC).** Never add ads, profit-driven analytics, affiliate
  links, sponsorships, paywalls, donation prompts, or any monetisation, and keep
  hosting non-commercial. (The original author is explicitly ad-free — see
  `docs/guide-feedback.md`.)
- **ShareAlike (SA).** This archive is redistributed under CC BY-NC-SA 4.0. Do
  not relicense it or any adaptation under other terms; new or derived content
  stays CC BY-NC-SA 4.0.
- **Indicate changes.** Modifications (HTML→Markdown, link rewriting to relative
  paths, image localisation, Wix-chrome removal) must be disclosed — the
  per-page footer already says the page was reformatted; keep that true.
- **Images are NOT under this licence.** Per the author they come from the ONI
  Wiki, the author's gameplay, and **Klei Entertainment**; game imagery is
  © Klei (fan-content use). Do not claim CC over images; honour takedown
  requests.

Canonical references: `LICENSE` (repo) and `docs/attribution.md` (on-site,
linked from every page footer). If a task would reduce or remove attribution,
add monetisation, or relicense, **stop and flag it** rather than proceeding.

## The two pipelines

1. **Crawl** (`scripts/crawl_archive.py`): Wayback CDX API → pick the *latest*
   HTTP-200/HTML capture per page → fetch raw HTML → extract main content →
   Markdown → write into `docs/`. Needs network access to `web.archive.org`.
2. **Build/deploy** (`mkdocs.yml` + `.github/workflows/deploy.yml`): MkDocs
   Material builds `docs/` → GitHub Actions deploys to Pages on push to `main`.

## Commands

```bash
# Crawler deps vs. site-build deps are intentionally separate.
pip install -r scripts/requirements.txt    # for the crawler
pip install -r requirements.txt            # for mkdocs build/serve

# Inspect what would be crawled (no downloads):
python3 scripts/crawl_archive.py --domain guidesnotincluded.com --list-only --inventory-out inventory.json

# Trial run, then full run:
python3 scripts/crawl_archive.py --domain guidesnotincluded.com --limit 3
python3 scripts/crawl_archive.py --domain guidesnotincluded.com

# Preview / build the site:
mkdocs serve        # http://127.0.0.1:8000
mkdocs build        # outputs ./site (gitignored)
```

Crawler flags worth knowing: `--limit N`, `--no-assets`, `--no-subdomains`,
`--sleep S`, `--docs-dir DIR`. There is no test suite; the crawler's offline
logic is validated ad hoc (see the smoke-test pattern in git history).

## Network access is the usual blocker

`web.archive.org` is blocked by default on Claude Code on the web
(`403 host_not_allowed`). It requires the environment's **Network access = Full**
(or Custom + `web.archive.org`/`archive.org`). **The change only applies to a
new session** — a running container keeps its original egress policy. Always
verify before crawling:

```bash
curl -sI "https://web.archive.org/web/2024id_/https://www.guidesnotincluded.com/" | head -1
# Expect HTTP 200, not 403
```

See `RUNBOOK.md` for the end-to-end procedure.

## Crawler internals (the non-obvious parts)

- **Capture mode matters.** Pages are fetched via the `id_` suffix
  (`/web/<ts>id_/<url>`) = raw, toolbar-free HTML. Images use the `im_` suffix.
  Don't use the default replay URL; it injects the Wayback banner.
- **Latest-per-page de-duplication** is done in Python via `normalize_key()`,
  which folds `www`/non-`www` and trailing slashes together and keeps the
  capture with the greatest timestamp. CDX `collapse=digest` only drops
  byte-identical re-captures.
- **URL → file path** (`url_to_relpath`) strips `.html`/`.php` suffixes and
  slugifies. `resolve_index_collisions()` then promotes a page to
  `<dir>/index.md` when other pages nest beneath it, so MkDocs treats it as a
  section landing page (works with the `navigation.indexes` theme feature).
- **Content extraction** (`extract_main_html`) tries the Wix
  `<main id="PAGES_CONTAINER">` landmark first (keeps the prose **and** the
  build screenshots, excludes header/footer), then `readability-lxml`, then
  `<body>` minus chrome. readability alone dropped every image, which is fatal
  for these screenshot-heavy guides — this is the first place to tune if
  conversions come out poorly.
- **Images: name by content, not URL.** `download_assets` sniffs the magic
  bytes (`sniff_image_ext`) to pick the extension, because Wix `enc_avif` URLs
  are served as AVIF/PNG/JPEG depending on the capturing browser's `Accept`
  header — the URL lies about the format. Re-runs reuse already-downloaded
  assets, so they don't re-fetch.
- **Link & chrome cleanup** happens during conversion: `rewrite_internal_links`
  repoints links to other archived pages at relative `.md` paths (external and
  provenance links stay absolute); `unwrap_self_links`, `strip_wix_pager`, and
  `tidy_body` remove the dead in-page TOC links, the prev/home/next pager, the
  site-tagline banner, and "Anchor N" markers.
- Every output file gets YAML front matter (`source_url`, `archived`,
  `archive_snapshot`) **and** the per-page attribution footer required for
  licence compliance (see *Licensing & attribution* above — do not remove it).

## Conventions / gotchas

- CI runs `mkdocs build` **without** `--strict` on purpose: archived content
  carries dead links from the original site and shouldn't block deploys.
- `mkdocs.yml` pins an explicit grouped `nav:` (12 topic sections). Pages live
  flat in `docs/`; the `nav:` only controls grouping/labels, so it must be
  updated by hand when pages are added or removed. `guides.md` (empty in the
  archive) and `home.md` (a duplicate of the homepage) are intentionally left
  out of the `nav:` but are still built and reachable by direct link.
- GitHub Pages must be set to **Source = GitHub Actions** (one-time, in repo
  Settings). Deployed URL: `https://ahembree.github.io/guidesnotincluded/`.
- `docs/index.md` may be a placeholder until the crawl runs; the crawl
  overwrites it with the archived home page.
