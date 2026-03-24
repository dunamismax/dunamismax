# SPA Web Tech Stack

Last reviewed: 2026-03-23

## Best Fit

Use this stack when the project is mostly:

- rich interactive browser applications where the client experience is the product
- editors, canvases, or drag-and-drop surfaces
- data-heavy dashboards with complex client-side state
- real-time collaborative interfaces
- apps where the browser holds meaningful session state between navigations

For this workspace, no current repo is a pure SPA, but specific islands or future products could earn this treatment.

## Opinionated Default

| Area | Default |
| --- | --- |
| Toolchain | Bun |
| Language | TypeScript in strict mode |
| Framework | Astro with client-side islands for heavy interaction |
| Interaction layer | Alpine.js for light interaction; a framework island for heavy components |
| Island framework | Preact or Solid when an island needs a real component model |
| Styling | CSS variables plus hand-written CSS first; Tailwind when UI density earns it |
| Client state | Keep it local. Use signals, stores, or context within the island boundary |
| Data fetching | Fetch API. No client query cache library unless repeated pain proves it necessary |
| Lint + format | Biome |
| Unit tests | Vitest |
| Browser tests | Playwright for critical interactive flows |
| Output mode | Static shell with client-side hydration for interactive regions |

## Golden Path

1. Start with Astro as the shell. Let Astro own routing, page structure, and static content.
2. Identify the interactive boundary. Only the part of the page that needs rich client-side state becomes an island.
3. Choose the lightest possible island runtime. Alpine covers most interaction. Preact or Solid only when the component model genuinely helps.
4. Keep client state inside the island. Do not let island state leak into Astro's static rendering.
5. Fetch data from the Go API over same-origin HTTP. Keep the fetch logic explicit and visible.
6. Ship the smallest possible JavaScript bundle. Measure it. Set a budget and enforce it.
7. Keep the shell functional without JavaScript. Navigation, content, and layout should work even if the island fails to load.

## Architecture

The SPA stack is still Astro-first. The difference from the static stack is that specific regions of the page are hydrated islands with their own component model, state, and lifecycle.

```text
Astro page shell (static or SSR)
  └── Island (Preact / Solid / Alpine)
        └── Client state, interaction, data fetching
```

The page shell is Astro. The island is the SPA. This avoids turning the entire application into a client-side routing mess while still delivering a rich interactive experience where it matters.

## When To Use A Full SPA Router

Almost never. If the product genuinely needs client-side route transitions with preserved state (an editor with multiple tabs, a dashboard with deep navigation), use a framework-level router inside the island boundary.

Do not use a client-side router for navigation between content pages. That is Astro's job.

## Client State Rules

- Keep state local to the island.
- Use signals or lightweight stores (Preact signals, Solid signals, Alpine `$store`).
- Do not add Redux, Zustand, or Jotai unless the island's state complexity genuinely requires it.
- Do not cache server data on the client unless you have measured the cost of re-fetching and it is unacceptable.
- Treat the server as the source of truth. The client is a view.

## Data Layer

The SPA stack does not own persistence. Data lives in the Go backend and SQLite.

- Fetch data from the Go API over same-origin HTTP.
- Use `fetch()` directly. Do not add a query abstraction layer by default.
- Mutations go through the API. Optimistic UI is allowed but must reconcile with server truth.
- Do not add GraphQL, tRPC, or WebSocket data sync unless the product earns it.

## Performance Budget

| Metric | Target |
| --- | --- |
| First Contentful Paint | < 1.0s |
| Largest Contentful Paint | < 1.5s |
| Total Blocking Time | < 100ms |
| Cumulative Layout Shift | < 0.05 |
| Island JavaScript budget | < 50KB per island (gzipped) |
| Lighthouse Performance | > 90 |
| Lighthouse Accessibility | 100 |

## Styling Direction

Same as the static stack:

1. CSS variables in `tokens.css`
2. Shared base rules in `base.css`
3. Component-local styles (CSS modules, scoped styles, or Astro component styles)
4. Tailwind when UI density earns it

## Testing And Quality Bar

Default scripts:

- `bun run dev`
- `bun run build`
- `bun run check` → `biome check . && astro check`
- `bun run test` → `vitest run`
- `bun run format` → `biome format . --write`

Additional for SPA islands:

- Vitest for unit testing island components
- Playwright for critical interactive flows (editor save, drag-and-drop, multi-step mutations)

## Guardrails

- Do not turn the whole app into a SPA. Astro owns the shell and routing.
- Do not add a global client state library by reflex.
- Do not add a client-side query cache by reflex.
- Do not hydrate the layout, navigation, or footer.
- Keep JavaScript budgets explicit and enforced.
- The shell must work without JavaScript. Islands enhance; they do not gate.
- Do not import React unless there is a specific third-party component that requires it.

## When Not To Use This Stack

Do not use this stack when:

- the product is a content site with no rich interaction (use [Static Web](./web-static-tech-stack.md))
- the product is a server-rendered app with forms, auth, and CRUD (use [SSR Web](./web-ssr-tech-stack.md))
- the "SPA" is really just a few Alpine toggles on an otherwise static page (use Static Web with Alpine)
- the product is a native desktop or mobile app
