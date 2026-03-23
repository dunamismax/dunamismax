# Bun + TypeScript + Astro + Alpine.js Web Tech Stack

Last reviewed: 2026-03-23

## Purpose

This is the default web stack in this workspace.

Use it for:

- websites
- docs and content-heavy product surfaces
- authenticated web frontends
- browser-facing apps that still want a calm architecture
- frontends paired with Go services or APIs

The point is simple: fast local loops, small client-side JavaScript, clean HTML, and deploys that do not turn the frontend into its own circus.

## Why This Stack

- Bun keeps installs, scripts, and local feedback fast.
- TypeScript catches stupid mistakes without needing framework ceremony.
- Astro keeps rendering server-first and lets the browser stay mostly quiet.
- Alpine.js covers the small interaction layer without dragging in a full client application.
- The whole stack pairs cleanly with Go backends while keeping the frontend pleasant to build.

## The Default Web Stack

| Area | Default |
| --- | --- |
| Toolchain | Bun |
| Language | TypeScript in strict mode |
| Page framework | Astro |
| Interaction layer | Alpine.js 3 |
| Component model | `.astro` layouts and components first |
| Styling | CSS variables plus hand-written CSS first |
| Content | Astro content collections when the repo is content-heavy |
| Lint + format | Biome |
| Type and Astro checks | `astro check` |
| Unit tests | Vitest |
| Browser tests | Playwright only for critical flows |
| Output mode | static by default, SSR only when required |
| Backend pairing | Go over same-origin HTTP when the product has a real service layer |

## Golden Path

1. Use Bun for install, scripts, and local commands.
2. Build pages, layouts, and components in Astro.
3. Fetch data on the server or at build time first.
4. Ship HTML and CSS that work before JavaScript wakes up.
5. Add Alpine only where the page needs small interaction.
6. Add a hydrated island only when the browser truly owns local state.
7. Keep deployment simple: static unless the product forces SSR.

## Default Project Shape

```text
project/
  public/
  src/
    components/
    content/
    layouts/
    lib/
      api/
      env.ts
    pages/
    styles/
      base.css
      tokens.css
  tests/
  astro.config.mjs
  biome.json
  package.json
  tsconfig.json
```

Notes:

- `src/pages/` owns routes.
- `src/layouts/` owns page shells.
- `src/components/` holds reusable Astro components.
- `src/lib/api/` is where backend calls and adapters live.
- `src/styles/` holds the global tokens and base rules.
- `public/` is only for files that must bypass the build pipeline.

## Rendering And Data Flow

Default order:

1. static generation
2. server rendering in Astro
3. client fetch after first paint

That means:

- fetch public or cacheable data in Astro page frontmatter
- fetch per-request or authenticated data in SSR mode
- keep forms and mutations server-owned when possible
- treat client fetch as a follow-up move, not the first instinct
- avoid a client cache/query layer until repeated pain proves it is needed

If the backend is Go, keep the boundary boring:

- Astro owns routes, HTML, assets, and presentation
- Go owns APIs, auth, jobs, SQL, and durable state
- use same-origin routing or a simple reverse proxy instead of clever frontend/backend choreography

## Interaction Ladder

### Plain Astro First

Use plain Astro for:

- content pages
- marketing pages
- docs
- dashboards that mostly render server data
- search and filtering that can live in the URL
- standard forms and post/redirect/get flows

### Alpine Next

Use Alpine when the page needs light interaction such as:

- menus, dialogs, tabs, disclosures, and accordions
- filter controls and sort toggles
- inline validation hints
- optimistic button state
- small multi-step forms
- simple live refresh wiring around existing HTML

Alpine should enhance server-rendered HTML, not replace it.

### Hydrated Islands Last

Use an island only when the browser genuinely owns the interaction model, for example:

- charts with rich client controls
- editors
- drag-and-drop surfaces
- maps
- large client-side data grids
- third-party widgets that already assume a client runtime

If Astro plus Alpine cannot carry a widget, isolate the heavy part. Do not hydrate the whole page. Do not turn the entire app into an accidental SPA.

## Styling Direction

Default order:

1. CSS variables in `tokens.css`
2. shared base rules in `base.css`
3. component-local styles in Astro components
4. Tailwind CSS only when the UI density clearly earns it

Avoid by default:

- CSS-in-JS
- design-token build machinery
- giant utility piles without a real design system
- animation libraries for normal interface work

## Testing And Quality Bar

Default scripts should cover:

- `bun run dev`
- `bun run build`
- `bun run check`
- `bun run test`
- `bun run format`

Recommended meaning:

- `bun run check` -> `biome check . && astro check`
- `bun run test` -> `vitest run`

Add Playwright only when the product has critical browser flows worth protecting, such as auth, checkout, editors, or complex mutations.

## Deployment Posture

Default order:

1. static hosting
2. one Astro SSR process
3. anything more complex only if the product earns it

Guidance:

- prefer static output for websites, docs, and cache-friendly product pages
- use SSR when auth, request-scoped data, previews, or private dashboards require it
- keep the frontend on the same origin as the backend when cookies or session flows matter
- avoid edge-function mazes unless there is a real latency or placement reason
- let the backend carry observability and business-state complexity; the frontend should stay thin

## Guardrails

- Do not start with a SPA router.
- Do not hydrate layouts, nav, or whole pages by default.
- Do not add a global client state library by reflex.
- Do not mirror all backend validation in the browser.
- Do not add GraphQL, tRPC, or websocket machinery just to feel modern.
- Do not split into frontend and backend deployment complexity if one simple reverse proxy solves it.
- Do not bring in React, Vue, or Svelte for the whole app when Astro and Alpine already cover the problem.

## When Not To Use This Stack

Do not use this stack when:

- the product is really a native desktop or mobile app
- the browser surface is basically a thin admin UI that wants to live inside one Go binary
- the product is an offline-first rich client with heavy long-lived browser state
- the core value is a canvas, editor, or app shell that behaves more like a desktop program than a website

In those cases, choose the stack that matches the actual runtime shape instead of forcing this one past its sweet spot.

## Primary Sources

- [Bun docs](https://bun.sh/docs)
- [TypeScript docs](https://www.typescriptlang.org/docs/)
- [Astro docs](https://docs.astro.build/)
- [Astro deployment guide](https://docs.astro.build/en/guides/deploy/)
- [Alpine.js docs](https://alpinejs.dev/start-here)
- [Biome docs](https://biomejs.dev/guides/getting-started/)
- [Vitest docs](https://vitest.dev/guide/)
- [Playwright docs](https://playwright.dev/docs/intro)
