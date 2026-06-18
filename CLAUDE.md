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
- **Content extraction** (`extract_main_html`) tries `readability-lxml` first
  and falls back to `<body>` minus chrome (`script/style/nav/header/footer`).
  guidesnotincluded.com was **Wix**, which produces noisy HTML — this function
  is the first place to tune if conversions come out poorly.
- Every output file gets YAML front matter recording `source_url`, `archived`
  date, and `archive_snapshot` for provenance.

## Conventions / gotchas

- CI runs `mkdocs build` **without** `--strict` on purpose: archived content
  carries dead links from the original site and shouldn't block deploys.
- `mkdocs.yml` has no explicit `nav:`; navigation is generated from the `docs/`
  tree. Pin a `nav:` only if you need to control ordering.
- GitHub Pages must be set to **Source = GitHub Actions** (one-time, in repo
  Settings). Deployed URL: `https://ahembree.github.io/guidesnotincluded/`.
- `docs/index.md` may be a placeholder until the crawl runs; the crawl
  overwrites it with the archived home page.
