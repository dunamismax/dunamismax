# Web Full-Stack Tech Stack

Last reviewed: 2026-04-04

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
- **Tailwind CSS v4** for styling, with design tokens via CSS custom properties
- **@vueuse/motion** for micro-interactions, page transitions, and animation
- **Elysia** for the Bun-native HTTP API and backend service layer
- **Zod** for shared validation, request parsing, and contract definitions
- **PostgreSQL** as the system of record
- **Raw SQL first** with the `postgres` driver, with thin query helpers only when earned
- **Valkey** for caching, session storage, rate limiting, pub/sub, and background job backing
- **BullMQ** for background job processing, backed by Valkey
- **Lucia** for session-based auth with **Arctic** for OAuth providers
- **MeiliSearch** for fast, typo-tolerant search with relevance tuning
- **D3** for data visualization, charts, maps, and heatmaps
- **Sharp** for server-side image processing, thumbnails, and format conversion
- **Resend** for transactional email with **@vue-email/components** for templates
- **Stripe** for subscription billing and payment processing
- **Sentry** for error tracking, performance monitoring, and session replay
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
Tailwind keeps styling fast, consistent, and token-driven without hand-writing thousands of lines of CSS.
Motion makes the UI feel alive without custom animation boilerplate.
Elysia keeps the backend close to the metal without forcing low-level boilerplate everywhere.
PostgreSQL holds the truth.
Valkey gives the fast layer: caching, sessions, pub/sub, rate limiting, and job queues.
BullMQ handles background work reliably without inventing a custom queue.
Lucia and Arctic keep auth secure and standard without rolling crypto from scratch.
MeiliSearch gives instant, typo-tolerant search without overloading PostgreSQL.
D3 powers the data visualizations that drive engagement and retention.
Sharp handles image processing so uploads are fast and storage-efficient.
Resend delivers transactional email without managing SMTP infrastructure.
Stripe handles money so you never touch card numbers.
Sentry catches errors before users report them.
Caddy and Docker keep the operational story clean.

## Opinionated Default

| Area | Default |
| --- | --- |
| Language | TypeScript |
| Runtime, package manager, scripts, tests | Bun |
| Repo shape | Bun workspace monorepo |
| Frontend framework | Astro |
| Interactive UI layer | None by default; Vue 3 only when the UI clearly earns it |
| Styling | Tailwind CSS v4 with design tokens via CSS custom properties |
| Animation | @vueuse/motion for Vue components; CSS transitions for simple cases |
| Backend framework | Elysia |
| Validation and shared contracts | Zod |
| Database | PostgreSQL |
| PostgreSQL driver | `postgres` |
| Query style | Raw SQL first |
| Query builder upgrade path | Kysely only when the query surface clearly earns it |
| Migrations | SQL files with a small checked-in Bun runner |
| Cache, sessions, rate limiting, pub/sub | Valkey |
| Background jobs | BullMQ backed by Valkey |
| Auth | Lucia (sessions) + Arctic (OAuth) + @node-rs/argon2 (password hashing) |
| Search | MeiliSearch |
| Data visualization | D3 |
| Image processing | Sharp |
| Email | Resend + @vue-email/components |
| Payments | Stripe |
| Monitoring | Sentry |
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
      tailwind.config.*
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
    worker/
      src/
        jobs/
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
    email/
      src/
        templates/
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

Not every repo needs `packages/ui/` or `packages/email/` on day one, but `packages/contracts/` is usually worth it because shared schemas and types remove duplication fast. The `apps/worker/` service is added when background jobs are real.

## Golden Path

1. Start as a Bun workspace with `apps/web`, `apps/api`, and `packages/contracts`.
2. Let Astro own pages, routing, layouts, and server-first rendering.
3. Start with Astro alone unless the product already has clear, substantial interactive complexity.
4. Use Vue only for the parts that are actually interactive and substantial enough to justify the extra layer.
5. Keep styling token-driven with Tailwind CSS v4 and a `tokens.css` design token file.
6. Put auth, business logic, data access, webhooks, and background entrypoints in the Bun API.
7. Use Lucia for auth and Arctic for OAuth — do not roll custom session or hashing logic.
8. Add Valkey and BullMQ when the product has background work, caching, or rate limiting needs.
9. Keep PostgreSQL as the source of truth and keep schema changes in SQL migration files.
10. Put Caddy in front from day one so local and production routing stay close.
11. Keep the product on one origin when practical.
12. Make JavaScript earn itself. Do not ship a SPA or a pure Vue app by reflex.
13. Add more services only when one web app, one API, and PostgreSQL are clearly failing.

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

- Tailwind CSS v4 as the styling layer
- design tokens defined as CSS custom properties and consumed by Tailwind's theme
- use Tailwind's `@theme` directive to map tokens into utility classes
- keep a `tokens.css` file as the single source of truth for color, spacing, type scale, radius, motion curves, and elevation
- use Tailwind utilities for layout, spacing, typography, and color
- use `@apply` sparingly and only in component-scoped styles where utility chains get unreadable
- use component-scoped `<style>` blocks in Vue SFCs when Tailwind utilities are insufficient
- reach for a component library only when the repo clearly earns it

Animation and motion rules:

- use @vueuse/motion for Vue component animations: enter/leave transitions, scroll-triggered reveals, interactive hover/tap states
- use CSS transitions and Tailwind's transition utilities for simple state changes (hover, focus, color shifts)
- define motion tokens (duration, easing curves) in `tokens.css` alongside other design tokens
- every interactive element should have a motion response — buttons, cards, modals, list items, page transitions
- keep animations subtle and fast (150-300ms for micro-interactions, 300-500ms for page transitions)
- respect `prefers-reduced-motion` — disable non-essential animation when the user requests it

The frontend should look intentional and feel alive.

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

If the product needs background jobs, use BullMQ backed by Valkey. Do not invent a custom PostgreSQL-based job queue.

## Auth and Session Guidance

Default auth posture:

- Lucia for session management: creation, validation, expiry, and secure cookie handling
- Arctic for OAuth provider integration (Google, Apple, GitHub) when the product earns social login
- @node-rs/argon2 for password hashing — never use bcrypt, sha256, or anything weaker
- secure, HttpOnly cookies with SameSite set deliberately for the actual product shape
- server-side sessions stored in PostgreSQL (default) or Valkey (when session lookup speed matters)
- passwordless or passkey flows when the product earns them
- JWTs only when a specific integration boundary truly requires them
- email verification flow on registration using Resend
- password reset flow with time-limited, single-use tokens

Do not default to token-sprawl when ordinary web sessions are the simpler and safer answer. Do not roll custom session or password hashing logic when Lucia and argon2 already solve it correctly.

## Cache, Pub/Sub, and Rate Limiting Guidance

Valkey is the default fast layer for this stack.

Use Valkey for:

- session storage when session lookup latency matters more than durability
- response caching for expensive or frequently-read queries (species data, leaderboards, frequency tables)
- rate limiting with sliding window counters per endpoint, per user, and per IP
- pub/sub for WebSocket fan-out when multiple server instances need to broadcast to connected clients
- sorted sets for leaderboards and ranking queries
- BullMQ job queue backing store

Default rate limiting rules:

- apply rate limits at the Elysia middleware layer using Valkey as the backing store
- use sliding window algorithm (not fixed window) for smoother limiting behavior
- auth endpoints (login, register, password reset): strict limits (5-10 requests per minute per IP)
- write endpoints (sighting reports, messages): moderate limits (30-60 per minute per user)
- read endpoints: generous limits (300+ per minute per user)
- return standard `429 Too Many Requests` with `Retry-After` header

Add Valkey to Docker Compose from day one. It is lightweight and earns its keep immediately through sessions and rate limiting alone.

## Background Jobs Guidance

BullMQ is the default job queue, backed by Valkey.

Use BullMQ for:

- alert dispatch (fan-out push notifications to matching users after sighting confirmation)
- external API sync (eBird data refresh, weather and tide data polling)
- leaderboard and stats recomputation (scheduled, not inline)
- email delivery (verification, password reset, event reminders, digests)
- image processing pipeline (resize, thumbnail, format conversion after upload)
- challenge progress evaluation
- any work that takes more than 100ms or touches external services

Default job rules:

- run workers in a separate `apps/worker/` process, not inside the API
- add a `worker` service to Docker Compose
- use named queues to separate job types (alerts, email, media, sync, stats)
- configure retries with exponential backoff for jobs that hit external services
- use scheduled/repeating jobs for periodic work (eBird sync, leaderboard refresh)
- log job failures to Sentry

## Search Guidance

MeiliSearch is the default search engine for this stack.

Use MeiliSearch for:

- fast, typo-tolerant search across species (common name, scientific name, family)
- user search (username, display name)
- hotspot and location search
- any search surface where autocomplete, fuzzy matching, or relevance ranking matters

Default search rules:

- run MeiliSearch as a Docker Compose service
- sync data from PostgreSQL to MeiliSearch via background jobs or application-level hooks
- PostgreSQL remains the source of truth — MeiliSearch is a read-optimized index
- use MeiliSearch's ranking rules to weight results (e.g., species frequency, recency, user trust)
- configure filterable and sortable attributes deliberately per index
- keep index updates near-real-time for user-facing data (species, sightings) via BullMQ sync jobs

Do not query MeiliSearch for data integrity operations. It is for search UX, not transactional reads.

## Data Visualization Guidance

D3 is the default visualization library for this stack.

Use D3 for:

- geographic visualizations (county/state fill maps, range maps, heatmaps)
- custom chart types that standard charting libraries handle poorly
- species accumulation curves, frequency charts, seasonal activity grids
- any visualization where you need full control over the SVG output

Default visualization rules:

- wrap D3 logic in Vue composables or components — do not scatter raw D3 DOM manipulation across the app
- use Vue's reactivity to drive D3 updates rather than D3's own data join when possible
- keep chart components in a dedicated `components/charts/` directory
- define a consistent color palette for charts in the design token system
- make all charts responsive and mobile-friendly
- provide accessible alternatives (data tables, ARIA labels) for screen readers

For simple bar/line/pie charts where D3 is overkill, a lightweight wrapper like Chart.js is acceptable, but D3 should be the first reach.

## Image Processing Guidance

Sharp is the default image processing library for this stack.

Use Sharp for:

- thumbnail generation on upload (e.g., 200x200 for avatars, 600x400 for feed cards)
- format conversion to WebP for optimized delivery
- EXIF data stripping for privacy
- size validation and rejection of oversized uploads
- progressive JPEG generation for large photos

Default media pipeline:

1. user uploads original file via API
2. API validates file type, size, and dimensions
3. BullMQ job picks up the upload and runs Sharp processing
4. Sharp generates: original (stored as-is), optimized full-size WebP, thumbnail WebP
5. processed files are written to the configured storage backend (local filesystem or S3-compatible)
6. database record is updated with URLs for each variant

Do not process images inline in the HTTP request. Always offload to a background job.

## Email Guidance

Resend is the default transactional email provider for this stack.

Use Resend for:

- email verification on registration
- password reset flows
- event reminders and RSVP confirmations
- rare bird alert digests (for users who prefer email over push)
- weekly stats summaries
- moderation notifications

Default email rules:

- build email templates with @vue-email/components in `packages/email/`
- render templates to HTML server-side before sending via Resend
- send email via BullMQ jobs, never inline in the HTTP request
- include plain text fallback for every HTML email
- use a consistent sender address and reply-to across the product
- track delivery status via Resend webhooks when delivery reliability is critical

## Payments Guidance

Stripe is the default payment provider for this stack.

Use Stripe for:

- subscription management (monthly and annual plans)
- Stripe Checkout for the payment flow — do not build a custom payment form
- Stripe Customer Portal for self-service billing management (plan changes, cancellation, invoice history)
- Stripe webhooks for server-side state sync (subscription created, renewed, cancelled, payment failed)

Default payments rules:

- store the Stripe customer ID and subscription ID on the user record
- use webhook events as the source of truth for subscription status, not client-side callbacks
- handle the `webhooks.ts` route with Stripe signature verification
- keep subscription tier logic in a shared permissions module so both frontend and backend can check entitlements
- never store card numbers, bank details, or sensitive payment data — Stripe handles PCI compliance

## Monitoring Guidance

Sentry is the default error tracking and performance monitoring tool for this stack.

Use Sentry for:

- unhandled exception capture in both the API and the frontend
- performance transaction tracing for slow API endpoints and page loads
- session replay for debugging user-reported frontend issues
- release tracking to correlate errors with deployments
- alert rules for error spikes and performance regressions

Default monitoring rules:

- initialize Sentry in both `apps/web/` and `apps/api/` entry points
- attach user context (user ID, role) to Sentry events when authenticated
- set sample rates deliberately: 100% for errors, 10-20% for performance transactions in production
- use Sentry's source maps upload for readable frontend stack traces
- configure alert rules for: new error types, error rate spikes, and p95 latency regressions
- do not log sensitive data (passwords, tokens, PII) to Sentry — scrub before sending

For uptime monitoring and a public status page, use Better Stack, Uptime Robot, or a similar external service pointed at health check endpoints.

## Docker and Caddy Guidance

Use Docker Compose for local development and for straightforward single-host deployment.

Default services:

- `caddy`
- `web`
- `api`
- `worker`
- `postgres`
- `valkey`
- `meilisearch`

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
- one BullMQ worker service
- one PostgreSQL instance
- one Valkey instance
- one MeiliSearch instance

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
bun --cwd apps/worker run build
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
- React or Next.js muscle memory imported without a reason
- heavy ORMs that hide SQL truth
- split frontend and backend repos for one small product
- Kafka or extra infrastructure beyond Valkey before the current stack is exhausted
- JWT-first auth when Lucia sessions are the simpler and safer answer
- microservice decomposition before one app and one API have actually hit a wall
- hiding deployment behind platform magic when Docker and Caddy already solve the problem
- Elasticsearch when MeiliSearch covers the search surface
- custom payment forms when Stripe Checkout exists
- inline image processing or email sending in HTTP request handlers — use BullMQ jobs
- rolling custom auth, session management, or password hashing when Lucia, Arctic, and argon2 exist
