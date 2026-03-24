# SSR Web Tech Stack

Last reviewed: 2026-03-23

## Best Fit

Use this stack when the project is mostly:

- authenticated web applications with sessions, forms, and mutations
- operator dashboards and admin consoles backed by a Go service
- CRUD apps with server-owned state and relational data
- products where the browser surface talks to a Go API over same-origin HTTP
- apps that need per-request data, auth gates, or server-side redirects

For this workspace, this fits most of the product repos: Scrybase, 0xvane, bore, gitpulse, repokeeper, wirescope, and vaultd.

## Two Modes

The SSR stack has two shapes depending on who owns the HTML:

### Astro SSR mode

Astro runs in SSR mode (`output: 'server'`) and renders pages on each request. The Go service is the API backend. Astro owns routes, HTML, layouts, and presentation. Go owns auth, business logic, persistence, and heavy service work.

Use this when the browser surface is a first-class product with its own page structure, content, and design system.

### Go-owned HTML

Go renders HTML directly using `templ` for components and `htmx` for partial updates. There is no separate frontend build step. The browser surface lives inside the Go binary.

Use this when one binary is a hard requirement, the browser surface is an operator UI or admin console, and authored JavaScript should stay near zero.

## Astro SSR Default Stack

| Area | Default |
| --- | --- |
| Toolchain | Bun |
| Language | TypeScript in strict mode |
| Page framework | Astro in SSR mode |
| Interaction layer | Alpine.js 3 |
| Component model | `.astro` layouts and components first |
| Styling | CSS variables plus hand-written CSS first |
| Database | SQLite via the Go backend (not in the Astro layer) |
| Auth | Terminate at the Go edge. Astro reads auth state from the Go API |
| Lint + format | Biome |
| Unit tests | Vitest |
| Browser tests | Playwright when auth, forms, or multi-step flows justify it |

## Go-Owned HTML Default Stack

| Area | Default |
| --- | --- |
| Toolchain | Go (latest stable) |
| Templates | `templ` |
| Partial updates | `htmx` |
| Forms | Standard HTML forms with POST and server-side validation |
| Sessions | `scs` |
| Validation | `go-playground/validator` or explicit hand-written checks |
| Styling | Hand-written CSS embedded or served from the binary |
| Dev reload | `air` |

## Golden Path — Astro SSR

1. Use Bun for installs, scripts, and the development loop.
2. Set Astro to SSR mode in `astro.config.mjs`.
3. Build pages, layouts, and components in Astro.
4. Fetch per-request data in Astro page frontmatter from the Go API.
5. Keep forms and mutations server-owned when possible. POST to the Go API, redirect on success.
6. Add Alpine only where the page needs light interaction.
7. Keep the Go API on the same origin. One reverse proxy or Astro adapter handles the boundary.
8. Let Go own all persistence, auth, background jobs, and business logic.

## Golden Path — Go-Owned HTML

1. Use `templ` for all rendered components.
2. Use standard HTML forms for mutations.
3. Use `htmx` for partial page updates where full reloads feel sluggish.
4. Use `scs` for sessions.
5. Serve everything from one Go binary.
6. Keep client JavaScript at zero or near zero.
7. Use `air` for live reload during development.

## Architecture — Astro SSR

```text
browser
  │
  ▼
Astro SSR (routes, HTML, layouts, presentation)
  │ fetch() to same-origin Go API
  ▼
Go service (auth, business logic, API, persistence)
  │
  ▼
SQLite
```

## Architecture — Go-Owned HTML

```text
browser
  │
  ▼
Go net/http server (routes, templ rendering, htmx partials, static assets)
  │
  ▼
SQLite
```

## Data Layer

The SSR stack does not own the database. The Go backend owns SQLite, and the web layer reads and writes through the Go API.

In the Astro SSR mode:

- Astro pages fetch data from the Go API in page frontmatter
- Forms POST to the Go API
- No direct SQLite access from the Astro layer
- No ORM or query library in the frontend

In the Go-owned HTML mode:

- Go handles data access directly through `database/sql` and `modernc.org/sqlite`
- Templates receive data from Go handlers
- No JavaScript data layer

## Auth And Session Boundary

- Auth terminates at the Go edge in both modes.
- In Astro SSR mode, Astro reads auth state by calling the Go API (cookie forwarding or token header).
- In Go-owned HTML mode, `scs` manages sessions directly.
- Do not implement auth in the Astro layer. Do not store secrets in the frontend.

## Default Project Shape — Astro SSR

```text
project/
  web/
    public/
    src/
      components/
      layouts/
      lib/
        api/
      pages/
      styles/
    astro.config.mjs
    biome.json
    package.json
    tsconfig.json
  cmd/
  internal/
  migrations/
  go.mod
  README.md
```

## Default Project Shape — Go-Owned HTML

```text
project/
  cmd/
  internal/
  views/
  static/
  migrations/
  go.mod
  README.md
```

## Interaction Ladder

Same as the static stack:

1. Plain server-rendered HTML first
2. Alpine for light interaction
3. Hydrated islands only when the browser genuinely owns the interaction

In Go-owned HTML mode, `htmx` replaces Alpine for most interaction patterns. Use Alpine alongside `htmx` only when `htmx` cannot cover the interaction cleanly.

## Styling Direction

Astro SSR mode: same as the static stack. CSS variables, base rules, component-local styles.

Go-owned HTML mode: hand-written CSS served from the binary. Keep it simple. These are operator UIs, not design showcases.

## Testing And Quality Bar

Astro SSR scripts:

- `bun run dev`
- `bun run build`
- `bun run check` → `biome check . && astro check`
- `bun run test` → `vitest run`
- `bun run format` → `biome format . --write`

Go verification:

- `go test ./...`
- `go vet ./...`
- `go build ./cmd/<binary>`

Add Playwright when the app has auth flows, multi-step forms, or interactive mutations worth protecting.

## Guardrails

- Do not put auth logic in the Astro layer.
- Do not give the Astro layer direct database access.
- Do not add a client-side router. Pages are server-rendered routes.
- Do not add GraphQL, tRPC, or WebSocket data sync unless the product earns it.
- Do not turn the Go backend into a generic REST framework with automatic CRUD generation.
- Keep the same-origin boundary boring. One proxy, one origin, no CORS theater.
- In Go-owned HTML mode, do not add a JavaScript build step.

## Quality Bar: Smooth And Responsive

SSR apps should feel fast and fluid, not sluggish or page-reload-heavy. The quality bar:

- Use `htmx` or Alpine for partial updates instead of full-page reloads where it improves the experience
- Keep page transitions fast — server responses should be snappy and HTML should be lightweight
- Use optimistic UI patterns where appropriate (disable buttons on submit, show loading states)
- Minimize layout shift during navigation
- Use SSE or targeted polling for live status updates instead of forcing page refreshes
- The goal is an app that feels smooth and responsive to use, not one that feels like a 2005 form-submission loop

This is a quality expectation, not a separate architecture. SSR with good use of htmx and Alpine can deliver an experience that feels as fluid as a client-heavy app without the complexity cost.

## When Not To Use This Stack

Do not use this stack when:

- the site is a static content site with no per-request data (use [Static Web](./web-static-tech-stack.md))
- the product needs heavy client-side state management beyond what Alpine and htmx can handle cleanly (evaluate whether the interaction ladder can still cover it before reaching for heavier client frameworks)
- the browser surface does not need a Go backend at all
