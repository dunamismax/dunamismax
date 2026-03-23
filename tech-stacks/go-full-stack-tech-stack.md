# Go Full-Stack Tech Stack

Last reviewed: 2026-03-23

## Purpose

This is the Go-rendered web stack for the cases where one Go binary should own the browser surface.

It is **not** the default frontend or website stack in this workspace anymore. For most websites, frontends, and browser-facing web apps, use [Bun + TypeScript + Astro + Alpine.js](./bun-typescript-astro-alpine-tech-stack.md).

Use this stack when you want:

- Go as the main language
- a browser UI that lives in the same runtime as the backend
- minimal authored JavaScript
- server-rendered HTML
- PostgreSQL-backed state
- deploys that still feel like normal Go software

This is still a good fit for small operator surfaces and products where one binary matters more than frontend specialization.

## The Go-Rendered Stack

| Area | Default |
| --- | --- |
| Language | Go 1.26.1 |
| HTTP layer | `net/http` first, `chi` if routing structure needs it |
| HTML rendering | `templ` |
| Front-end interaction | `htmx` |
| CSS | hand-written CSS or Tailwind CSS v4 via the standalone CLI |
| Sessions | `scs` with PostgreSQL session storage |
| Validation | server-side validation with `go-playground/validator` |
| Durable state | PostgreSQL |
| Driver | `pgx/v5` |
| Query layer | `sqlc` |
| Migrations | `goose` |
| Live reload in development | `air` |
| Assets | static files plus SVGs, served directly by Go |
| Observability | `slog`, Prometheus, `pprof` |

## Golden Path

1. Render HTML on the server.
2. Use `templ` for components and layout composition.
3. Use `htmx` for progressive interaction instead of building a client app.
4. Keep validation and domain rules on the server.
5. Keep authored JavaScript at zero unless the product truly forces it.
6. Use PostgreSQL, `pgx`, and `sqlc` for state.

## Default App Shape

```text
project/
  cmd/web/
  internal/app/
  internal/httpui/
  internal/store/
  views/
  static/
  migrations/
  sql/
  go.mod
```

Suggested split:

- `cmd/web/` for the entrypoint
- `internal/httpui/` for handlers and page composition
- `views/` for `templ` components and pages
- `static/` for CSS, images, and non-generated assets
- `internal/store/` for `sqlc`-backed data access

## Front-End Philosophy

This stack is HTML-over-the-wire first.

That means:

- links and forms do most of the work
- `htmx` handles targeted partial updates
- SSE handles dashboards and low-friction live updates
- CSS carries the presentation system
- the server stays in control of state and rendering

This is the right fit for operator dashboards, internal tools, self-hosted products, and stateful web software where one deployable Go runtime matters more than having a dedicated frontend stack.

## CSS Guidance

Default order:

1. hand-written CSS if the design system is small
2. Tailwind CSS v4 standalone CLI if utility classes will clearly speed delivery

Do not introduce a Node-heavy front-end build chain unless the app has crossed a very real threshold that this stack cannot handle.

## Interaction Guidance

Use:

- normal forms for create and update flows
- `htmx` partial swaps for inline edits and dashboards
- SSE for live status pages and logs

Avoid:

- SPA routing as the default
- client-side state management libraries
- turning a Go app into a JavaScript platform by accident

## Auth And Session Guidance

- use cookie-backed sessions for first-party web apps
- keep auth checks on the server
- use CSRF protection on mutating browser flows
- make session storage PostgreSQL-backed when multi-instance or durability needs it

## When To Choose This Instead Of The Default Web Stack

Choose this Go-rendered stack over the Bun + Astro web stack when:

- one binary is a hard requirement
- the browser surface is an operator UI, not a frontend product lane of its own
- server-rendered HTML already covers nearly all interaction needs
- the team wants Go to own routing, templates, sessions, and deploy shape end to end

## Dev And Release Guidance

- use `air` for local reload
- compile assets in a simple, visible step
- ship one web binary plus static assets
- keep migrations in the same repo and release flow

## When Not To Use This Stack

Do not use this stack when:

- the product is truly an offline-first rich client that needs heavy browser-side logic
- the team is explicitly building a frontend/web app as a first-class product surface
- the real value is a native desktop or mobile app instead of a web surface
- Astro would give you a simpler, faster frontend split without hurting deployment

## Primary Sources

- [Go downloads](https://go.dev/dl/)
- [`templ` guide](https://templ.guide/)
- [`htmx` docs](https://htmx.org/docs/)
- [Tailwind CSS docs](https://tailwindcss.com/docs/)
- [`air` repository](https://github.com/air-verse/air)
- [`pgx` docs](https://pkg.go.dev/github.com/jackc/pgx/v5)
- [`sqlc` docs](https://docs.sqlc.dev/)
- [`goose` docs](https://pressly.github.io/goose/)
- [Prometheus Go app guide](https://prometheus.io/docs/guides/go-application/)
- [`golangci-lint` docs](https://golangci-lint.run/)
