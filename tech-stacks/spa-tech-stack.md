# SPA Tech Stack

Last reviewed: 2026-03-24

## Best Fit

Use this stack when the project is mostly:

- a dashboard, operator UI, or admin console
- a product frontend with real client-side state and interaction
- any browser-facing surface that needs routing, forms, and dynamic behavior
- a standalone SPA that talks to a Go backend over HTTP

This is the default web lane for browser-facing frontends. For repos with a Go or Rust backend, start with the backend doc and use this doc as a supplement for frontend-specific decisions. See the [routing table](./README.md#routing) to determine which docs apply to your repo.

When paired with a Go backend, the SPA lives in `web/` inside the Go repo. Go owns auth, business logic, and persistence. The SPA owns presentation and browser interaction.

## Opinionated Default

| Area | Default |
| --- | --- |
| Runtime / package manager | Bun |
| Language | TypeScript (strict mode) |
| Build tool / dev server | Vite |
| UI framework | React |
| Routing | TanStack Router |
| Server-state / data fetching | TanStack Query (when needed) |
| Forms | TanStack Form (when needed) |
| Validation | Zod |
| UI components | shadcn/ui + Radix UI |
| Styling | Tailwind CSS (via shadcn defaults) |
| Lint + format | Biome |
| Unit / component tests | Vitest |
| E2E tests | Playwright (when needed) |
| Durable state (SPA-only products) | Backend-owned (SQLite behind a Go API) or external API — the SPA never owns persistence directly |

## Golden Path

1. Start with `bun create vite` using the React + TypeScript template.
2. Enable strict mode in `tsconfig.json` from the start.
3. Add TanStack Router for type-safe file-based routing.
4. Add shadcn/ui and configure Tailwind CSS through its setup.
5. Add Biome for lint and format. One config, one tool.
6. Add Vitest for tests.
7. Add TanStack Query only when the product has server state to manage.
8. Add TanStack Form only when form complexity earns it.
9. Add Playwright only when browser interaction flows genuinely need E2E coverage.
10. Keep the component tree shallow and the state surface small.

## Default Repo Shape (SPA-Only)

```text
project/
  src/
    components/
    routes/
    lib/
    main.tsx
  public/
  tests/
  index.html
  vite.config.ts
  tsconfig.json
  biome.json
  package.json
  README.md
```

Use `src/components/` for reusable UI, `src/routes/` for route components (TanStack Router file-based routing), `src/lib/` for shared utilities and API clients.

## Repo Shape When Paired With Go

When the SPA lives inside a Go backend repo:

```text
project/
  cmd/
  internal/
  migrations/
  web/
    src/
      components/
      routes/
      lib/
      main.tsx
    public/
    tests/
    index.html
    vite.config.ts
    tsconfig.json
    biome.json
    package.json
  go.mod
  README.md
```

The Go binary serves the built SPA assets from `web/dist/` (or a reverse proxy does). The SPA build is a Vite build inside `web/`. Go and the SPA share nothing at build time — they are two independent build targets that happen to live in one repo.

## Routing Guidance

TanStack Router is the default. It provides:

- fully type-safe route definitions and params
- file-based routing that maps `src/routes/` to URL paths
- type-safe search params and loader data
- code splitting per route out of the box

Keep route components focused on layout and data orchestration. Push business logic into `src/lib/`. Push UI primitives into `src/components/`.

Do not use React Router. TanStack Router gives you type safety that React Router does not, and the file-based convention keeps routing decisions visible in the file tree.

## Data Fetching Guidance

TanStack Query manages server state. The rules:

- every API call that reads server data goes through a query
- mutations use `useMutation` with proper cache invalidation
- keep client state minimal and local — `useState` and `useReducer` are fine for UI state
- do not add a global state management library unless the product genuinely has complex cross-cutting client state that TanStack Query does not cover
- colocate query keys and fetch functions in `src/lib/` so they are reusable across routes

Avoid fetching in `useEffect`. TanStack Query handles caching, deduplication, background refetching, and error/loading states. Let it.

## Component Architecture Guidance

shadcn/ui provides composable, copy-pasted component primitives built on Radix UI. The rules:

- install shadcn/ui components into `src/components/ui/` — they are your code, not a black-box library
- use Radix primitives for accessibility (focus management, keyboard navigation, ARIA)
- keep component trees shallow — if nesting goes past three or four levels, flatten
- prefer composition over configuration — small components that compose beat large components with many props
- do not build a component library abstraction on top of shadcn/ui — use the components directly

## Styling Guidance

Tailwind CSS utility classes via shadcn/ui defaults. The rules:

- use Tailwind utilities for layout, spacing, color, and typography
- use `cn()` (from shadcn/ui) for conditional class merging
- do not add CSS-in-JS libraries
- do not add a second styling system
- keep custom CSS to a minimum — if Tailwind cannot express it, think twice before writing it

## Build And Deploy Guidance

Vite builds the SPA into static assets (`dist/`). Deployment options:

- **Go backend:** embed the `dist/` directory and serve it with `http.FileServer` or equivalent. Add a catch-all route that serves `index.html` for any path the SPA router handles.
- **CDN or static host:** upload `dist/` and configure a catch-all fallback to `index.html`.
- **Reverse proxy:** Nginx, Caddy, or similar. Serve static files from `dist/`, catch-all to `index.html`.

SPA routing requires the catch-all fallback. Without it, direct navigation to any route other than `/` will 404.

Keep the build fast. Vite already handles code splitting, tree shaking, and asset hashing. Do not add extra build steps unless they solve a real problem.

## Go Backend Pairing Guidance

When the SPA talks to a Go backend:

- keep the boundary same-origin HTTP — the SPA and API live behind the same origin
- Go owns auth, business logic, persistence, jobs, and operational concerns
- the SPA owns presentation, routing, and browser interaction
- the Go binary serves the SPA as static assets, or a reverse proxy does
- API routes are plain JSON over HTTP — no GraphQL, no RPC unless the product genuinely needs it
- keep auth simple — session cookies or JWT, managed by Go, consumed by the SPA
- CORS is unnecessary when the SPA and API share an origin

The SPA is a build artifact that Go serves. It is not a separate service with its own deploy pipeline unless the product has clearly earned that complexity.

## Validation Guidance

Zod is the default validation library. Use it for:

- API response validation at the boundary
- form input validation
- search param parsing
- any runtime type checking where TypeScript's compile-time types are not enough

Keep Zod schemas in `src/lib/` and reuse them across routes and components. Do not scatter inline schemas through the component tree.

## Testing Guidance

### Unit and component tests

Vitest is the default. The rules:

- test utility functions, hooks, and non-trivial logic in `src/lib/`
- test component behavior, not implementation details
- use `@testing-library/react` for component tests
- colocate test files next to the code they test or keep them in `tests/`
- run tests with `bun run test`

### E2E tests

Playwright is the default, but only when needed. Add E2E tests when:

- the product has critical user flows that span multiple routes
- form submission, auth flows, or payment paths need browser-level verification
- the cost of a regression in that flow justifies the maintenance cost of the test

Do not add Playwright for every page. Unit and component tests cover most things faster and cheaper.

## TypeScript Guidance

Strict mode is mandatory. In `tsconfig.json`:

```json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true
  }
}
```

Do not weaken strict mode to make code compile faster. Fix the types.

Prefer explicit types at module boundaries (function signatures, API responses, exported interfaces). Let inference handle the rest.

Use Zod schemas as the source of truth for runtime types. Derive TypeScript types from Zod schemas with `z.infer<>` instead of maintaining parallel type definitions.

## Biome Guidance

Biome handles both linting and formatting in one tool. The rules:

- configure once in `biome.json`
- run `bun run lint` for linting and `bun run format` for formatting
- do not add ESLint or Prettier alongside Biome — one tool, not three
- use Biome's recommended rules as the baseline and only override with good reason

## Security Baseline

- validate all API responses at the boundary with Zod
- do not trust server data shapes without validation
- sanitize user input before rendering — React handles most XSS by default, but be careful with `dangerouslySetInnerHTML`
- keep auth tokens in httpOnly cookies managed by Go, not in localStorage
- use Content-Security-Policy headers served by Go or the reverse proxy

## When To Choose This Stack

Choose the SPA stack when:

- the product has a browser-facing surface with real interaction
- users navigate between views, fill forms, see live-updating data
- the browser owns meaningful client state beyond what a static page provides
- the product is a dashboard, operator UI, admin console, or product frontend

## When Not To Choose This Stack

- if the product is a static content site with no interaction, serve static HTML — but this workspace does not have a separate static-site stack doc for that
- if the browser surface is a simple status page or docs site, a plain HTML file is fine
- if there is no browser surface, do not add one

## Avoid By Default

- Next.js, Remix, or any SSR framework unless the product genuinely needs server rendering
- Astro, Alpine.js, or islands architecture
- GraphQL
- State management libraries beyond TanStack Query (no Redux, Zustand, Jotai, or MobX unless the product has genuinely complex cross-cutting client state)
- CSS-in-JS (styled-components, Emotion, etc.)
- Heavy component libraries (Material UI, Ant Design, Chakra) — shadcn/ui + Radix covers the need
- Multiple styling systems
- ESLint + Prettier when Biome does both
- Separate deploy pipelines for the SPA when it can be served as static assets from the Go binary
