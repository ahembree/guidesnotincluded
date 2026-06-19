# Runbook: restoring guidesnotincluded.com from the Internet Archive

This procedure crawls the Wayback Machine, converts each archived page to
Markdown, and serves the result as an Astro + Starlight site on GitHub Pages.

> **This is a one-time procedure, and it has already been run.** The converted
> content is committed under `src/content/docs/guidesnotincluded_archive/`, so to
> run or deploy the site you only need `pnpm install` + `pnpm build` (see the
> README). Follow the steps below only to refresh the archive from the Wayback
> Machine.

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
pip install -r scripts/requirements.txt   # crawler (Python)
pnpm install                              # site build (Astro/Starlight; pnpm 11, Node 20+)
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
pnpm dev   # open http://localhost:4321/guidesnotincluded/ and check quality
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

The crawler writes pages and images into `src/content/docs/guidesnotincluded_archive/` (Starlight's
content collection). Useful flags:

| Flag | Effect |
|-|-|
| `--limit N` | Only convert the first N pages. |
| `--no-assets` | Skip downloading images. |
| `--no-subdomains` | Match only the exact domain (no `www.` etc.). |
| `--sleep S` | Seconds between requests (default 0.5; be polite). |
| `--docs-dir DIR` | Output directory (default `src/content/docs/guidesnotincluded_archive`). |

New pages are built automatically, but they only appear in the sidebar if you
add them to the `sidebar` array in `astro.config.mjs` (the nav is curated by
hand, mirroring the original site's grouping).

## 5. Review, then build

```bash
pnpm dev                 # local preview with hot reload
pnpm build               # produce ./dist (gitignored)
pnpm preview             # serve the production build locally
```

## 6. Commit and deploy

```bash
git add src public astro.config.mjs package.json pnpm-lock.yaml pnpm-workspace.yaml .npmrc scripts .github
git commit -m "Restore guidesnotincluded.com content from the Internet Archive"
git push -u origin <branch>
```

Merging to `main` triggers `.github/workflows/deploy.yml`, which builds the site
with `withastro/action` and deploys `./dist` to GitHub Pages.

### One-time GitHub Pages setup

In the repository: **Settings → Pages → Build and deployment → Source =
GitHub Actions**. After the first successful deploy the site is available at:

```
https://ahembree.github.io/guidesnotincluded/
```
