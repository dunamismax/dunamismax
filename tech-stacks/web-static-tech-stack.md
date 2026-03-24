# Static Web Tech Stack

Last reviewed: 2026-03-23

## Best Fit

Use this stack when the project is mostly:

- blogs and personal sites
- documentation sites
- marketing and product landing pages
- portfolios and project showcases
- content-heavy sites where pages rarely change per-request

For this workspace, this fits `dunamismax.com`.

## Opinionated Default

| Area | Default |
| --- | --- |
| Toolchain | Bun |
| Language | TypeScript in strict mode |
| Page framework | Astro in static output mode |
| Interaction layer | Alpine.js 3 |
| Component model | `.astro` layouts and components first |
| Styling | CSS variables plus hand-written CSS first |
| Content | Astro content collections for Markdown-driven pages |
| Lint + format | Biome |
| Type and Astro checks | `astro check` |
| Unit tests | Vitest |
| Browser tests | Playwright only when critical flows justify it |
| Output mode | Static (pre-built HTML) |

## Golden Path

1. Use Bun for installs, scripts, and the development loop.
2. Build pages, layouts, and components in Astro.
3. Write content in Markdown with frontmatter. Use Astro content collections.
4. Fetch data at build time. There is no server at runtime.
5. Ship HTML and CSS that work before JavaScript wakes up.
6. Add Alpine only where the page needs light interaction.
7. Self-host fonts and assets. No external CDN calls at runtime.
8. Keep the dependency count small enough to audit in five minutes.

## Default Project Shape

```text
project/
  public/
    fonts/
    og/
  src/
    components/
    content/
      blog/
      projects/
    layouts/
    lib/
    pages/
    styles/
      base.css
      tokens.css
  scripts/
  tests/
  astro.config.mjs
  biome.json
  package.json
  tsconfig.json
```

Notes:

- `src/pages/` owns routes.
- `src/layouts/` owns page shells.
- `src/content/` holds Markdown-driven content collections.
- `src/styles/` holds the global tokens and base rules.
- `public/` is for files that must bypass the build pipeline.
- No `src/db/` — static sites have no runtime data layer.

## Content Model

Blog posts, project entries, and other structured content live in Astro content collections as Markdown files with typed frontmatter. No CMS. No database. Content is files in the repo.

This means:

- adding a post is committing a Markdown file
- the content schema is TypeScript, version-controlled, and enforceable at build time
- there is no runtime dependency for content delivery

## Rendering Model

Every page is pre-built at `bun run build` time. There is no server process at runtime. The output is a directory of static HTML, CSS, and minimal JavaScript that any static host can serve.

That means:

- no request-scoped data
- no server-side auth
- no API routes
- no SSR middleware
- no session state

If a page later needs any of those, move that page (or the whole site) to the [SSR Web](./web-ssr-tech-stack.md) stack.

## Interaction Ladder

### Plain Astro first

Use plain Astro for everything that does not need client-side state. That covers the vast majority of static site pages: content, navigation, layouts, search-by-URL, and links.

### Alpine next

Use Alpine when the page needs light interaction: menus, dialogs, tabs, accordions, dark mode toggles, filter controls, or inline form validation.

Alpine should enhance server-rendered HTML, not replace it. If the interaction needs more than ~30 lines of Alpine, reconsider the approach.

### Hydrated islands last

Use an island only when the browser genuinely owns the interaction model: charts, editors, maps, or embedded third-party widgets. Do not hydrate layouts or whole pages.

## Styling Direction

1. CSS variables in `tokens.css`
2. Shared base rules in `base.css`
3. Component-local styles in Astro components
4. Tailwind only when the UI density clearly earns it

Avoid by default: CSS-in-JS, design-token build machinery, animation libraries for normal interface work.

## Performance Budget

| Metric | Target |
| --- | --- |
| First Contentful Paint | < 0.5s |
| Largest Contentful Paint | < 1.0s |
| Total Blocking Time | 0ms |
| Cumulative Layout Shift | 0 |
| Total page weight | < 100KB transferred |
| JavaScript shipped | < 10KB |
| Lighthouse Performance | 100 |
| Lighthouse Accessibility | 100 |

## Deployment

Static output goes to any static host. Pick the simplest option that serves files fast:

- Cloudflare Pages
- self-hosted Caddy or Nginx
- Vercel or Netlify

The output is just files. The choice is always reversible.

## Testing And Quality Bar

Default scripts:

- `bun run dev`
- `bun run build`
- `bun run check` → `biome check . && astro check`
- `bun run test` → `vitest run`
- `bun run format` → `biome format . --write`

## Guardrails

- Do not add SSR mode. If you need server rendering, use the SSR stack.
- Do not add a database. If you need runtime data, use the SSR stack.
- Do not add client-side routing or a SPA router.
- Do not add a CMS. Content is Markdown in the repo.
- Do not add third-party analytics, tracking pixels, or CDN font calls.
- Do not hydrate layouts or whole pages.
- Every page must work with JavaScript disabled.

## When Not To Use This Stack

Do not use this stack when:

- the site needs authentication or per-request data
- the site needs API routes or server-side mutations
- the product is an interactive application, not a content site
- the site needs a database

In those cases, use the [SSR Web](./web-ssr-tech-stack.md) or [SPA Web](./web-spa-tech-stack.md) stack instead.
