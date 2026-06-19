// SPDX-License-Identifier: MIT
// @ts-check
import path from 'node:path';
import { defineConfig, passthroughImageService } from 'astro/config';
import { unified } from '@astrojs/markdown-remark';
import starlight from '@astrojs/starlight';

// Deployed as a GitHub project page, so the site lives under a /base/ subpath.
const SITE = 'https://ahembree.github.io';
const BASE = '/guidesnotincluded';

// The crawler writes cross-page links as relative `.md` paths (e.g.
// `pipes-and-pumps.md`), which are convenient for editing/GitHub but which
// Starlight does not resolve in page bodies. Rewrite them to real routed URLs
// at build time so the prose links work without altering the content.
function remarkRelativeMdLinks() {
  return (/** @type {any} */ tree, /** @type {any} */ file) => {
    // Slugs are relative to the archive folder (its name is stripped by the
    // loader's generateId), so resolve relative `.md` links against the same root.
    const docsRoot = path.resolve(
      file.cwd ?? process.cwd(),
      'src/content/docs/guidesnotincluded_archive'
    );
    const fileDir = file.path ? path.dirname(file.path) : docsRoot;
    const rewrite = (/** @type {string} */ url) => {
      // Leave external, protocol-relative, root-absolute, and pure-anchor links.
      if (/^([a-z][a-z0-9+.-]*:|\/\/|\/|#)/i.test(url)) return url;
      const m = url.match(/^(.*?)\.md(#.*)?$/i);
      if (!m) return url;
      const hash = m[2] ?? '';
      const absNoExt = path.resolve(fileDir, m[1]);
      let slug = path.relative(docsRoot, absNoExt).split(path.sep).join('/');
      if (slug === 'index' || slug === '') return `${BASE}/${hash}`;
      if (slug.endsWith('/index')) slug = slug.slice(0, -'/index'.length);
      return `${BASE}/${slug}/${hash}`;
    };
    const visit = (/** @type {any} */ node) => {
      if ((node.type === 'link' || node.type === 'definition') && typeof node.url === 'string') {
        node.url = rewrite(node.url);
      }
      if (Array.isArray(node.children)) node.children.forEach(visit);
    };
    visit(tree);
  };
}

export default defineConfig({
  site: SITE,
  base: BASE,
  // The archive's images are already web-optimised AVIF from the original Wix
  // site; serve them as-is instead of re-encoding ~460 files on every build.
  image: { service: passthroughImageService() },
  // Astro 6.4 moved extra remark/rehype plugins under `processor`. `unified()`
  // from @astrojs/markdown-remark keeps the default pipeline (GFM, Smartypants)
  // and Starlight's own markdown plugins, adding ours on top.
  markdown: { processor: unified({ remarkPlugins: [remarkRelativeMdLinks] }) },
  integrations: [
    starlight({
      title: 'Guides Not Included',
      description:
        'An archived copy of guidesnotincluded.com — Oxygen Not Included builds, ' +
        'guides, and resources. Restored from the Internet Archive.',
      tagline: 'An Oxygen Not Included guides archive',
      lastUpdated: false,
      pagination: false,
      customCss: ['./src/styles/custom.css'],
      social: [
        {
          icon: 'github',
          label: 'GitHub',
          href: 'https://github.com/ahembree/guidesnotincluded',
        },
      ],
      // Restore the per-page social/JSON-LD meta (was overrides/main.html) and
      // the site-wide CC BY-NC-SA / Klei copyright line (was mkdocs `copyright`).
      components: {
        Head: './src/components/Head.astro',
        Footer: './src/components/Footer.astro',
      },
      // Mirrors the hand-curated MkDocs `nav:`. guides.md and home.md are
      // intentionally left out (empty / duplicate of the homepage) but still build.
      sidebar: [
        { label: 'Home', link: '/' },
        {
          label: 'Start here',
          items: [
            { label: 'The very early game', slug: 'the-very-early-game' },
            { label: 'The early game', slug: 'the-early-game' },
            {
              label: "Complete beginner's guide",
              slug: 'complete-beginners-completely-incomplete-guide-to-oxygen-not-included',
            },
            { label: "Things I wish I'd known", slug: 'things-i-wish-id-known-when-i-started' },
            { label: 'Builds overview', slug: 'builds' },
            { label: 'Base game vs Spaced Out', slug: 'base-game-versus-spaced-out-dlc' },
          ],
        },
        {
          label: 'Duplicants',
          items: [
            { label: 'Choosing duplicants', slug: 'choosing-duplicants' },
            { label: 'How many dupes?', slug: 'how-many-dupes-should-you-have' },
            { label: 'Atmo suits', slug: 'atmo-suit-basics' },
          ],
        },
        {
          label: 'Core mechanics',
          items: [
            { label: 'Pipes and pumps', slug: 'pipes-and-pumps' },
            { label: 'Liquid lock basics', slug: 'liquid-lock-basics' },
            { label: 'Liquid lock (build)', slug: 'liquid-lock' },
          ],
        },
        {
          label: 'Oxygen (SPOMs)',
          items: [
            { label: 'What is a SPOM?', slug: 'to-know-the-spom-is-to-love-the-spom' },
            { label: 'SPOM — 1 kg/s', slug: 'spom-1kg-s' },
            { label: 'SPOM — Full Rodriguez', slug: 'spom-3kg-s' },
          ],
        },
        {
          label: 'Water & germs',
          items: [
            { label: 'Getting more water', slug: 'getting-more-water' },
            { label: 'Decontaminating germy water', slug: 'decontaminating-germy-water-francis' },
            { label: 'Recycling toilet water', slug: 'recycling-toilet-water' },
            { label: 'Dealing with slimelung', slug: 'dealing-with-slimelung' },
          ],
        },
        {
          label: 'Cooling & heat',
          items: [
            { label: 'Heat transfer basics', slug: 'heat-transfer-basics' },
            { label: 'Anti-entropy thermo-nullifier (AETN)', slug: 'anti-entropy-thermo-nullifier' },
            { label: 'AETN cooling loop', slug: 'anti-entropy-thermo-nullifier-cooling' },
            { label: 'Aquatuner + steam turbine loop', slug: 'aquatuner-steam-turbine-cooling-loo' },
            { label: 'Thermo aquatuner cooling loop', slug: 'thermo-aquatuner-steam-turbine-cooling-loop' },
          ],
        },
        {
          label: 'Power & automation',
          items: [
            { label: 'Getting started with automation', slug: 'getting-started-with-automation' },
            { label: 'Carbon skimmer automation', slug: 'carbon-skimmer-automation-jahws' },
            { label: 'Taming a hydrogen vent', slug: 'hydrogen-vent-taming' },
          ],
        },
        {
          label: 'Resources & industry',
          items: [
            { label: 'Getting steel', slug: 'getting-steel' },
            { label: 'Oil, petroleum & plastic', slug: 'getting-oil-petroleum-and-plastic' },
            { label: 'Oil well with liquid lock', slug: 'oil-well-with-liquid-lock' },
            { label: 'Taming metal volcanoes', slug: 'taming-metal-volcanos' },
            { label: 'Mini industry', slug: 'mini-industry' },
          ],
        },
        {
          label: 'Ranching',
          items: [
            { label: 'Ranching basics', slug: 'ranching-basics' },
            { label: 'Drecko ranching (plastic)', slug: 'low-tech-plastic-drecko-ranching' },
          ],
        },
        {
          label: 'Space & Spaced Out (DLC)',
          items: [
            { label: 'Getting to space', slug: 'getting-to-space-dlc' },
            { label: 'Spaced Out research', slug: 'spaced-out-research-guide' },
            { label: 'Dealing with meteor showers', slug: 'dealing-with-meteor-showers' },
            { label: 'Liquid hydrogen & oxygen', slug: 'liquid-hydrogen-oxygen-small' },
          ],
        },
        {
          label: 'Drafts & duplicates',
          items: [
            { label: 'The early game (draft)', slug: 'copy-of-the-early-game' },
            { label: 'Getting to space (draft)', slug: 'copy-of-getting-more-water' },
            { label: 'Work in progress', slug: 'copy-of-wip' },
          ],
        },
        {
          label: 'About this archive',
          items: [
            { label: 'Attribution & licensing', slug: 'attribution' },
            { label: 'Guide feedback', slug: 'guide-feedback' },
          ],
        },
      ],
    }),
  ],
});
