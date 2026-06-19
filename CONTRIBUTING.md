# Contributing

Thanks for helping improve this archive of **guidesnotincluded.com**! This is an
unofficial, **non-commercial** community restoration. Please read the
[Licensing](#licensing--read-this-first) section before you start — this project
has strict attribution and non-commercial rules, and contributions that break
them can't be merged.

## TL;DR

```bash
corepack enable                 # use the pnpm version pinned in package.json
pnpm install                    # install site-build deps (pnpm 11, Node 20+)
pnpm dev                        # http://localhost:4321/guidesnotincluded/
# ...make your change...
pnpm build                      # must pass before you open a PR
```

The guide content is already generated and committed — you do **not** need to run
the crawler to contribute. Just edit files and run the site.

## What lives where (and what to modify)

| Path | What it is | Licence |
|-|-|-|
| `src/content/docs/guidesnotincluded_archive/*.md` | The guide pages (the original author's content) | **CC BY-NC-SA 4.0** |
| `src/content/docs/guidesnotincluded_archive/assets/` | Images (game screenshots etc.) | © Klei / ONI Wiki / author — **not** CC |
| `astro.config.mjs` | Site config: sidebar nav, base path, image handling, relative-link plugin | MIT |
| `src/content.config.ts` | Content collection + front-matter schema | MIT |
| `src/components/Head.astro` | SEO / OpenGraph / JSON-LD + image lightbox | MIT |
| `src/components/Footer.astro` | Site-wide CC/Klei copyright line | MIT |
| `src/styles/custom.css` | Theme accent + lightbox styles | MIT |
| `scripts/crawl_archive.py` | One-time Wayback crawler (already run) | MIT |
| `pnpm-workspace.yaml` / `.npmrc` | Dependency supply-chain policy | MIT |

**The rule of thumb: everything inside `guidesnotincluded_archive/` is the
original author's CC-licensed work; everything else is project code under MIT.**

## Common contributions — exactly what to do

### Fix a typo or formatting in a guide

1. Edit the relevant `.md` file in
   `src/content/docs/guidesnotincluded_archive/`.
2. **Do not remove or alter the attribution footer** at the bottom of the page
   (the `*Archived from … CC BY-NC-SA 4.0 …*` block). It is required by the
   licence.
3. Cross-page links use relative `.md` paths (e.g. `[pumps](pipes-and-pumps.md)`);
   images use `![alt](assets/<file>)`. Keep that style — a build-time plugin
   rewrites `.md` links to real URLs.
4. `pnpm dev` to preview, `pnpm build` to confirm.

### Add or remove a guide page

1. Add/remove the `.md` file under `guidesnotincluded_archive/`. Every page needs
   YAML front matter with at least a `title`.
2. **Update the sidebar by hand** in `astro.config.mjs` → the `sidebar` array.
   Use the file name without `.md` as the `slug` (the archive folder name is
   stripped from URLs automatically), e.g.
   `{ label: 'My page', slug: 'my-page' }`.
3. `pnpm build` and check the page renders and is reachable from the nav.

### Change the look, layout, or behaviour (code)

- Theme/colours: `src/styles/custom.css`. Footer/head/SEO: the components in
  `src/components/`. Nav/config: `astro.config.mjs`.
- **Interactive components** (e.g. an ONI calculator) are welcome as Astro
  islands. Put them in `src/` as their own `.astro`/`.js`/`.ts` files — they are
  MIT code. A page can load a widget and stay CC; see
  [Licensing](#licensing--read-this-first).

### Add a dependency (supply-chain policy)

Dependencies are governed by `pnpm-workspace.yaml` + `.npmrc`. When you
`pnpm add` something:

- **pnpm only**, from the **official npm registry**. No `git:`, tarball, or other
  "exotic" specifiers.
- A **24-hour release-age cooldown** is enforced (`minimumReleaseAge`); pnpm will
  resolve to the newest version that's at least a day old. This is intentional —
  don't disable it.
- Build/lifecycle scripts are blocked by default (`strictDepBuilds`). If a new,
  trusted package genuinely needs one, vet it and add it to `allowBuilds` in
  `pnpm-workspace.yaml`; otherwise the install will fail loudly.
- Prefer few, well-known dependencies. Commit the updated `pnpm-lock.yaml`.

### Refresh the archived content (rarely needed)

The crawler already ran; its output is committed. Only re-run it to pull fresh
captures — see [RUNBOOK.md](RUNBOOK.md). It writes into
`src/content/docs/guidesnotincluded_archive/`.

## Licensing — read this first

This repository is **dual-licensed by file**, and contributions must respect it:

- **Guide content** (everything in `guidesnotincluded_archive/`, excluding images
  and code) is the work of **Some Random Finn**, licensed
  **[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)**. See
  the root [`LICENSE`](LICENSE).
- **Code** (everything else) is **[MIT](LICENSE-CODE)**.
- **Images** are © **Klei Entertainment** / the ONI Wiki / the author and are
  **not** under CC — used for non-commercial, fan-content/archival purposes only.

The full licence texts are bundled in the repo: [`LICENSE-CONTENT`](LICENSE-CONTENT)
(CC BY-NC-SA 4.0) and [`LICENSE-CODE`](LICENSE-CODE) (MIT), with a one-glance
summary in [`NOTICE`](NOTICE).

**By opening a pull request, you agree that:**

- your changes to **content** are contributed under **CC BY-NC-SA 4.0**, and your
  changes to **code** are contributed under **MIT** — matching the file you edit
  (inbound = outbound);
- you have the right to contribute what you submit.

You must, in every contribution:

- **Attribution (BY)** — never remove, empty, or hide the per-page attribution
  footer, the site-wide copyright footer (`src/components/Footer.astro`), or the
  JSON-LD author/licence in `src/components/Head.astro`. Preserve in-page build
  credits (Francis John, Jahws, Mullematsch, the ONI community).
- **NonCommercial (NC)** — do **not** add ads, analytics-for-profit, affiliate
  links, sponsorships, paywalls, donation prompts, or any monetisation, and keep
  hosting non-commercial.
- **ShareAlike (SA)** — any adaptation of the guide content stays CC BY-NC-SA 4.0.
  New original guide text you write is welcome but is also offered under
  CC BY-NC-SA 4.0; credit yourself in-page and open an issue first for anything
  large.
- **Don't blur the code/content line** — keep interactive code in its own files
  under `src/` (MIT). A `.md` page stays CC even when it loads a widget. If a
  component reproduces the author's words/tables/data, *that reproduced content*
  stays CC BY-NC-SA — so compute from game constants (Klei/ONI-wiki data) rather
  than transcribing the author's prose.
- **Images** — don't relicense game imagery or claim CC over it; honour takedown
  requests.

If a change would reduce attribution, add monetisation, or relicense anything,
**stop and open an issue first.**

## Opening a pull request

1. Branch off `main`.
2. Make your change; run `pnpm build` (CI runs the same Astro build — archived
   dead links don't fail it, but real build errors do).
3. Keep PRs focused; describe what changed and why.
4. Confirm the checklist below in your PR description.

### PR checklist

- [ ] `pnpm build` passes locally.
- [ ] Per-page attribution footers, the site copyright footer, and the JSON-LD
      author/licence are all intact.
- [ ] No ads / paid analytics / affiliate / sponsorship / paywall / donation
      added (NonCommercial).
- [ ] Content edits stay in `guidesnotincluded_archive/` (CC BY-NC-SA); code
      edits are MIT and live outside it.
- [ ] New deps: added with `pnpm`, official registry, no exotic specifiers,
      build scripts vetted/allow-listed, `pnpm-lock.yaml` committed.
- [ ] No game imagery relicensed; image sources respected.

## Reporting issues & takedowns

Open a GitHub issue for bugs, broken pages, or content problems. **Rights
holders** who want an image or page removed can also open an issue — see
[`src/content/docs/guidesnotincluded_archive/attribution.md`](src/content/docs/guidesnotincluded_archive/attribution.md).
