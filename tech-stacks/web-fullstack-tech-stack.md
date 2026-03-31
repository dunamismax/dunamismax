# Web Full-Stack Tech Stack

Last reviewed: 2026-03-31

## Best Fit

Use this stack for:

- browser-first products with real backend logic, persistence, auth, and deployment needs
- ambitious web apps, dashboards, operator consoles, and productized internal tools
- portfolio pieces and public demos that should still look and feel like real production systems
- greenfield products where TypeScript across the entire application meaningfully reduces friction
- web projects that want one modern stack from page shell to API to database boundary

This is the default **full-stack TypeScript web lane** when the product is genuinely web-first and Bun is the right backend runtime.

If the work is only a frontend surface, use [web-frontend-tech-stack.md](./web-frontend-tech-stack.md) instead.

If the backend logic is better served by Python or Go, use those lanes and pair them with the standard Astro frontend. Add Vue only when the UI earns it.

## The Stack

The stack is:

- **TypeScript** for application code across frontend, backend, and shared contracts
- **Bun** for runtime, package management, scripts, and tests
- **Astro** for page composition, server-first delivery, and site structure
- **Vue** only when the product has substantial interactive UI that Astro alone should not carry
- **Plain CSS** for styling, with modern CSS features and design tokens
- **Elysia** for the Bun-native HTTP API and backend service layer
- **Zod** for shared validation, request parsing, and contract definitions
- **PostgreSQL** as the system of record
- **Raw SQL first** with the `postgres` driver, with thin query helpers only when earned
- **Docker Compose** for local orchestration and single-host deployment shape
- **Caddy** for TLS termination, reverse proxying, compression, and edge-facing delivery

The goal is one coherent stack that stays fast, explicit, and deployable without collapsing into framework soup.

## Why This Stack

This stack optimizes for a few things that matter in real work:

- one language across the whole product
- one package manager and script runner
- server-first page delivery instead of defaulting to a client-heavy SPA
- fast local iteration with Bun
- a backend that still feels lightweight and direct
- relational data as the source of truth
- a deployment shape that is boring enough to trust

Astro keeps the web surface fast and page-oriented.
Astro can stand alone.
Vue gives interactivity where it is actually needed.
Elysia keeps the backend close to the metal without forcing low-level boilerplate everywhere.
PostgreSQL holds the truth.
Caddy and Docker keep the operational story clean.

## Opinionated Default

| Area | Default |
| --- | --- |
| Language | TypeScript |
| Runtime, package manager, scripts, tests | Bun |
| Repo shape | Bun workspace monorepo |
| Frontend framework | Astro |
| Interactive UI layer | None by default; Vue 3 only when the UI clearly earns it |
| Styling | Plain CSS first |
| Backend framework | Elysia |
| Validation and shared contracts | Zod |
| Database | PostgreSQL |
| PostgreSQL driver | `postgres` |
| Query style | Raw SQL first |
| Query builder upgrade path | Kysely only when the query surface clearly earns it |
| Migrations | SQL files with a small checked-in Bun runner |
| Auth | Server-side sessions with secure cookies |
| Local orchestration | Docker Compose |
| Reverse proxy and TLS | Caddy |
| Lint and format | Biome |
| Type checking | `tsc --noEmit` and `astro check` |
| Unit and integration tests | `bun test` |
| Browser E2E | Playwright |
| Dev entrypoint | `bun run dev` |
| Verify entrypoint | `bun run verify` |

## Default Product Shape

```text
project/
  apps/
    web/
      src/
        components/
        layouts/
        pages/
        lib/
        styles/
      public/
      astro.config.*
      package.json
      tsconfig.json
    api/
      src/
        routes/
        middleware/
        services/
        db/
        lib/
        index.ts
      package.json
      tsconfig.json
  packages/
    contracts/
      src/
      package.json
      tsconfig.json
    ui/
      src/
      package.json
      tsconfig.json
  db/
    migrations/
    seeds/
  ops/
    docker/
  Caddyfile
  compose.yaml
  biome.json
  package.json
  bun.lock
  tsconfig.base.json
  README.md
```

Not every repo needs `packages/ui/` on day one, but `packages/contracts/` is usually worth it because shared schemas and types remove duplication fast.

## Golden Path

1. Start as a Bun workspace with `apps/web`, `apps/api`, and `packages/contracts`.
2. Let Astro own pages, routing, layouts, and server-first rendering.
3. Start with Astro alone unless the product already has clear, substantial interactive complexity.
4. Use Vue only for the parts that are actually interactive and substantial enough to justify the extra layer.
5. Keep styling hand-written and token-driven with plain CSS.
6. Put auth, business logic, data access, webhooks, and background entrypoints in the Bun API.
7. Keep PostgreSQL as the source of truth and keep schema changes in SQL migration files.
8. Put Caddy in front from day one so local and production routing stay close.
9. Keep the product on one origin when practical.
10. Make JavaScript earn itself. Do not ship a SPA or a pure Vue app by reflex.
11. Add more services only when one web app, one API, and PostgreSQL are clearly failing.

## Frontend Guidance

Use Astro for:

- routing
- page rendering
- SSR and content delivery
- layout composition
- public marketing pages, docs pages, and application shell pages
- server-side data fetching for page load

Use Vue for:

- authenticated app surfaces
- form-heavy workflows
- stateful widgets
- filters, inspectors, editors, and dashboards
- modal and drawer flows
- client-side interaction that would be awkward in plain HTML

Do not move page ownership into Vue by default. Astro should still own the page. Astro-alone is a valid end state.

### Styling Guidance

Default styling rules:

- hand-written CSS first
- CSS variables for color, spacing, type, radius, motion, and elevation tokens
- modern CSS features are encouraged when browser support is solid
- keep global tokens and resets explicit
- use component-scoped styles when they improve clarity
- reach for a component library only when the repo clearly earns it
- do not default to Tailwind just because the ecosystem expects it

The frontend should look intentional, not library-shaped.

## Backend Guidance

Use the Bun API for:

- auth and session handling
- application business logic
- JSON APIs
- webhooks
- background work entrypoints
- realtime endpoints when the product actually needs them
- integration boundaries with third-party services

Prefer one API service per product.
Keep the surface boring: HTTP, JSON, explicit request and response schemas, and predictable route structure.

Elysia is the default because it fits Bun well, keeps TypeScript ergonomics strong, and does not force unnecessary ceremony.

### Contracts and Type Sharing

Shared contracts should live in `packages/contracts/`.

Use that package for:

- Zod schemas for requests and responses
- shared enums and value objects
- form payload validation
- DTOs that intentionally cross the frontend/backend boundary
- shared utility types that are actually part of the contract

Rules:

- infer types from schemas instead of hand-maintaining duplicates
- do not expose raw database row shapes directly to the UI
- keep backend internals private even if the language is shared
- treat the contract package as a boundary, not a dumping ground

## Data Guidance

PostgreSQL is the default database for this lane.

Use PostgreSQL because these projects are expected to be real web applications, not static brochures wearing a JSON file as a fake backend.

Default data rules:

- PostgreSQL first
- relational schema first
- constraints first
- transactions where they matter
- indexes added deliberately
- SQL migrations checked into the repo
- raw SQL first with `postgres`
- Kysely only when the query surface is large enough to justify typed composition

Do not start with an ORM that hides the actual query plan and schema truth.

If the product needs jobs, start with PostgreSQL-backed job state or a simple jobs table before adding Redis or heavier queue infrastructure.

## Auth and Session Guidance

Default auth posture:

- server-side sessions
- secure, HttpOnly cookies
- SameSite set deliberately for the actual product shape
- passwordless or passkey flows when the product earns them
- JWTs only when a specific integration boundary truly requires them

Do not default to token-sprawl when ordinary web sessions are the simpler and safer answer.

## Docker and Caddy Guidance

Use Docker Compose for local development and for straightforward single-host deployment.

Default services:

- `caddy`
- `web`
- `api`
- `postgres`
- optional `worker` only when background work actually justifies a separate process

Use Caddy for:

- automatic HTTPS
- reverse proxying
- compression
- caching headers where appropriate
- websocket and streaming upgrades
- one clean public entrypoint in front of the product

Keep the Caddyfile in the repo.
Keep Compose simple.
Do not invent a platform before the product needs one.

## Dev And Deployment Shape

Default local flow:

1. start PostgreSQL with Docker Compose
2. run the Bun workspace in dev mode
3. route browser traffic through Caddy when testing integrated behavior
4. keep local and production hostnames, ports, and path routing structurally similar

Default production shape:

- Caddy at the edge
- one Astro web service
- one Bun API service
- one PostgreSQL instance
- optional worker process only when background work is real

For most of these projects, that is enough.

## Quality Bar

Every repo using this stack should have a root-level `bun run verify` that covers the actual quality gates.

The baseline should include:

```bash
bun install
bunx biome check .
bun run typecheck
bun test
bun --cwd apps/web run build
bun --cwd apps/api run build
```

When the browser experience matters, also run Playwright.

A good `bun run verify` usually wraps:

- formatting and lint checks
- TypeScript checks
- Astro checks
- unit and integration tests
- build validation for both web and API
- Playwright for important browser flows

## When Not To Use This Stack

- the project is mostly a content site, docs site, or portfolio with little backend logic
- the backend problem is better served by Python or Go
- the repo is a small tool where a full web stack would be theater
- the product has no meaningful persistence or auth surface
- the deployment target cannot justify Bun as the backend runtime
- the repo is an existing documented exception

## Avoid By Default

- client-heavy SPA architecture as the starting point
- Tailwind as an automatic default
- React or Next.js muscle memory imported without a reason
- heavy ORMs that hide SQL truth
- split frontend and backend repos for one small product
- Redis, Kafka, or extra infrastructure before PostgreSQL and a straightforward worker model are exhausted
- JWT-first auth when normal web sessions would be simpler
- microservice decomposition before one app and one API have actually hit a wall
- hiding deployment behind platform magic when Docker and Caddy already solve the problem
