# Runbook: restoring guidesnotincluded.com from the Internet Archive

This procedure crawls the Wayback Machine, converts each archived page to
Markdown, and serves the result as a MkDocs site on GitHub Pages.

## 0. Prerequisites: network access to the Internet Archive

The crawler must reach `web.archive.org`. On **Claude Code on the web**, the
environment's egress proxy blocks it by default (`403 host_not_allowed`).

To fix it, edit the environment (cloud icon → environment selector → hover →
settings gear) and set **Network access** to:

- **Full** — any domain (simplest), **or**
- **Custom** — add `web.archive.org` and `archive.org`, and tick
  *"Also include default list of common package managers"* so pip/npm/GitHub
  still work.

Saving rebuilds the environment cache. **The new policy only applies to a new
session**, so start a fresh session afterward. Git state on this branch
persists across sessions, so all the tooling here carries over.

Verify access:

```bash
curl -sI "https://web.archive.org/web/2024id_/https://www.guidesnotincluded.com/" | head -1
# Expect: HTTP/2 200  (not 403 host_not_allowed)
```

## 1. Install dependencies

```bash
pip install -r scripts/requirements.txt   # crawler
pip install -r requirements.txt           # site build (mkdocs-material)
```

## 2. Inspect the inventory first (optional but recommended)

```bash
python3 scripts/crawl_archive.py --domain guidesnotincluded.com --list-only \
  --inventory-out inventory.json
```

This prints every page the crawler found (latest 200/HTML capture of each URL)
and where it will be written, without downloading anything. Review it to confirm
the page set looks right.

## 3. Do a small trial run

```bash
python3 scripts/crawl_archive.py --domain guidesnotincluded.com --limit 3
mkdocs serve   # open http://127.0.0.1:8000 and check the conversion quality
```

guidesnotincluded.com was a **Wix** site, so the raw archived HTML can be
noisy. Check that the trial pages extract cleanly. If chrome (nav/menus) leaks
in or content is missing, tune `extract_main_html()` in
`scripts/crawl_archive.py` (e.g. add Wix-specific content selectors) before the
full run.

## 4. Full crawl

```bash
python3 scripts/crawl_archive.py --domain guidesnotincluded.com
```

Useful flags:

| Flag | Effect |
| --- | --- |
| `--limit N` | Only convert the first N pages. |
| `--no-assets` | Skip downloading images. |
| `--no-subdomains` | Match only the exact domain (no `www.` etc.). |
| `--sleep S` | Seconds between requests (default 0.5; be polite). |
| `--docs-dir DIR` | Output directory (default `docs`). |

## 5. Review, then build

```bash
mkdocs serve            # local preview
mkdocs build            # produce ./site (gitignored)
```

Optionally pin an explicit `nav:` in `mkdocs.yml` to control page ordering;
by default the nav is generated from the `docs/` tree.

## 6. Commit and deploy

```bash
git add docs mkdocs.yml requirements.txt scripts .github
git commit -m "Restore guidesnotincluded.com content from the Internet Archive"
git push -u origin <branch>
```

Merging to `main` triggers `.github/workflows/deploy.yml`, which builds the site
and deploys to GitHub Pages.

### One-time GitHub Pages setup

In the repository: **Settings → Pages → Build and deployment → Source =
GitHub Actions**. After the first successful deploy the site is available at:

```
https://ahembree.github.io/guidesnotincluded/
```
