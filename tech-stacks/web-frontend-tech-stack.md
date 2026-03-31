# Web Frontend Tech Stack

Last reviewed: 2026-03-31

## Best Fit

Use this stack for:

- browser-facing product surfaces
- documentation sites, portfolio sites, and marketing pages
- dashboards, consoles, and operator web apps
- product UIs that need a modern browser frontend without defaulting to a client-heavy SPA

This is the default **web frontend lane** in the workspace.

The stack is:

- **TypeScript** for application code
- **Bun** for runtime, package management, scripts, and tests
- **Astro** for page composition, server-first delivery, and site structure
- **Vue** only when the product has substantial interactive UI that Astro alone should not carry

Astro is the default. It can stand on its own. Vue is optional and must earn its place.

## Why This Stack

From the official docs today:

- Bun is an all-in-one toolkit for JavaScript and TypeScript apps, shipping runtime, package manager, test runner, and bundler in one binary.
- Astro is server-first, fast by default, and built around islands architecture with zero JavaScript by default.
- Vue 3 is a progressive, component-based UI framework that scales from small interactive widgets to larger application surfaces when that extra layer is actually warranted.

That gives this workspace a web stack that stays fast, explicit, and modern without defaulting to an SPA or a pure Vue app for everything.

## Opinionated Default

| Area | Default |
| --- | --- |
| Runtime and package manager | Bun |
| Language | TypeScript |
| Web framework | Astro |
| Interactive UI layer | None by default; Vue 3 only when the UI clearly earns it |
| Styling | Plain CSS first; utility or component libraries only when the repo clearly earns them |
| Lint and format | Biome |
| Type checking | `astro check` |
| Unit tests | `bun test` |
| Browser E2E | Playwright |
| Dev entrypoint | `bun run dev` |
| Build entrypoint | `bun run build` |
| Preview entrypoint | `bun run preview` |

## Default Shape

```text
project/
  src/
    components/
    layouts/
    pages/
    lib/
    styles/
  public/
  tests/
  astro.config.*
  package.json
  bun.lock
  tsconfig.json
  biome.json
  README.md
```

If the repo has enough interactive UI to deserve separation, keep Vue components under `src/components/` and keep Astro pages and layouts responsible for routing, composition, and data handoff. If it does not, skip Vue.

## Golden Path

1. Start with Astro on Bun.
2. Ship Astro alone first when it can carry the job.
3. Add the Vue integration only when the product has sustained interactivity, stateful workflows, or UI complexity that Astro alone should not absorb.
4. Keep pages and layouts in Astro.
5. Use Vue for interactive islands, forms, filters, editors, drawers, and stateful widgets when those patterns are substantial enough to justify it.
6. Keep client-side JavaScript earned, not automatic.
7. Keep the frontend boundary clean against the backend, whether that backend is Python or Go.
8. If the product also needs a terminal operator workflow, add OpenTUI as a second frontend rather than forcing the browser to do everything.

## Astro Guidance

Use Astro for:

- route structure
- page rendering
- content-heavy surfaces
- server-first and multi-page app delivery
- static generation or on-demand rendering as the product requires

Do not treat Astro as a thin wrapper around a client-heavy app by default. Let Astro do the page work.
Astro-alone is a valid finish line.

## Vue Guidance

Use Vue for:

- interactive controls
- form-heavy workflows
- search and filtering
- editors and inspectors
- stateful widgets inside Astro pages
- richer app behavior where plain HTML would become awkward

Do not add Vue just because the repo has a browser. Prefer Vue Single-File Components when the interaction is substantial enough to justify them.

## Backend Pairing Guidance

This frontend lane is deliberately backend-agnostic.

- Pair with **Python** when the backend is about APIs, automation, data work, or general service logic.
- Pair with **Go** when the backend is about networking, daemons, systems behavior, concurrency, or performance-sensitive services.

Do not pretend one backend is the default for every project. Pick the one that fits.

## Dual Frontend Guidance

When the product shape justifies it, the preferred setup is:

- one backend in Python or Go
- one web frontend in Astro, with Vue only where needed
- one terminal frontend in OpenTUI + TypeScript + Bun

If the TUI does not improve the product, do not add it.

## Quality Bar

Every web frontend repo should pass:

```bash
bun install
bunx biome check .
bunx astro check
bun test
```

When the repo has browser flows that matter, also run Playwright.

## When Not To Use This Stack

- the product does not have a browser surface
- the UI is trivial enough that static HTML or a tiny embedded admin page is enough
- the product is terminal-first and the browser is not part of the actual workflow
- the repo is an existing, documented exception

## Avoid By Default

- client-heavy SPA architecture as the starting point
- shipping large amounts of JavaScript to pages that do not need it
- reaching for pure Vue by reflex when Astro already fits
- moving page composition into Vue when Astro should own it
- making frontend stack choices that force the backend into the wrong language
