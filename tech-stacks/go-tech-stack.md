# Go Tech Stack

Last reviewed: 2026-03-31

## Best Fit

Use this stack when the project is mostly:

- network services and daemons
- CLIs and operator tooling that benefit from a single binary
- systems work and infrastructure-facing software
- APIs and backends with meaningful concurrency demands
- long-running runtimes where deployment simplicity matters
- performance-sensitive services where Go's profile is a better fit than Python

Go is not the universal default backend either. Use it when the runtime shape, concurrency model, deployment target, or systems constraints clearly justify it.

If the product needs a browser surface, the default frontend pairing is now [TypeScript + Bun + Astro](./web-frontend-tech-stack.md). Add Vue only when the browser UI earns it. If the product also benefits from a real terminal operator surface, pair it with [OpenTUI](./opentui-tech-stack.md).

## Opinionated Default

| Area | Default |
| --- | --- |
| Toolchain | Latest stable Go |
| Dependency management | Go modules |
| Workspace mode | `go work` only when actively developing multiple modules together |
| Formatting | `gofmt` |
| Linting | `golangci-lint` plus `go vet` |
| Vulnerability scan | `govulncheck` |
| Logging | `log/slog` |
| HTTP | `net/http` first |
| Router upgrade path | `chi` when route structure and middleware outgrow the stdlib |
| Database | PostgreSQL by default; SQLite only when the repo is deliberately local-first, embedded, or tiny |
| PostgreSQL driver | `pgx/v5` via `database/sql` or `pgxpool` when the repo actually needs pooling semantics |
| SQLite driver | `database/sql` + `modernc.org/sqlite` when SQLite is the deliberate choice |
| Query layer | Plain SQL first; `sqlc` only when the query surface genuinely justifies codegen |
| Migrations | SQL files first; tiny in-repo runner second; `goose` only when the repo truly needs it |
| Config | Environment variables and flags first |
| CLI | `flag` for small tools, `cobra` for large multi-command CLIs |
| Task runner | `mage` |
| Browser frontend pairing | Astro on Bun, with Vue only when the UI earns it |
| Terminal frontend pairing | OpenTUI + TypeScript + Bun |

## Database Default

Use PostgreSQL by default.

For most new Go applications in this workspace, that means:

- `pgx/v5` as the driver layer
- plain SQL first
- `sqlc` when the query surface clearly earns code generation
- SQL migrations checked into the repo

Choose SQLite only when the repo is deliberately one of these shapes:

- local-first single-user operator software
- embedded metadata or state inside a CLI or daemon
- offline-first utilities where shipping one file matters more than networked access
- tiny internal tools where PostgreSQL would be pure ceremony

## SQLite Driver Decision

When a repo deliberately uses SQLite, use `modernc.org/sqlite`.

It is pure Go. No CGO. No system library dependency. Clean single-binary story. Cross-compilation works without toolchain surgery.

Do not use `mattn/go-sqlite3` unless a specific repo has a verified, documented reason to require CGO-linked system SQLite.

Follow the [SQLite Operating Model](./README.md#sqlite-operating-model) in the tech-stacks README for pragma configuration, connection discipline, and migration patterns.

## Golden Path

1. Start with one binary and divide the code by capability, not architecture theater.
2. Use the standard library unless a small package clearly removes pain.
3. Start with PostgreSQL when the product needs durable state.
4. Use SQLite only when the repo is intentionally local-first, embedded, or tiny.
5. Use plain SQL first.
6. Add `sqlc` only when the query surface or team workflow really earns it.
7. Add structured logs and Prometheus metrics on day one for long-running services.
8. Keep the deploy shape obvious.
9. Add Astro and OpenTUI as sibling frontends when the product needs them. Add Vue only where the browser UI earns it.

## Default Repo Shape

```text
project/
  cmd/
  internal/
  migrations/
  sql/
  README.md
  go.mod
```

Use `cmd/` for entrypoints, `internal/` for app code, `migrations/` for schema changes, and `sql/` when the repo has enough queries to deserve explicit SQL files.

## HTTP Guidance

- Default to `net/http`.
- Use `http.Server` with explicit timeouts.
- Use middleware sparingly and visibly.
- Reach for `chi` only when route grouping and middleware composition become materially easier with it.
- Avoid reflection-heavy frameworks unless the project has a genuinely unusual requirement.

## Data Guidance

The Go data doctrine is:

- PostgreSQL by default
- relational data by default
- plain SQL first
- `sqlc` only when backend complexity actually justifies it
- SQLite only when the repo is deliberately local-first, embedded, or tiny

That means:

- use PostgreSQL for new services, APIs, web backends, networked tools, and any Go application that is meant to grow
- use SQLite only for local-first tools, single-user operator software, embedded state, caches, or deliberately small utilities
- use database constraints, transactions, indexes, and explicit query shape instead of hiding truth in repo folklore
- keep schema truth in readable SQL migration files
- do not reach for a heavyweight Go ORM as the center of the data layer
- do not add extra infrastructure before the actual product shape earns it

## Frontend Pairing Guidance

When the product has a browser-facing frontend:

- Astro owns page composition, delivery, and server-first rendering
- Vue is optional and owns interactive components, stateful widgets, and richer browser behavior only when the browser UI actually needs that extra layer
- Go owns auth, business logic, persistence, jobs, APIs, and operational concerns
- keep the boundary boring: HTTP, JSON, server-rendered edges, or same-origin integration

When the product has a real terminal operator surface:

- OpenTUI owns layout, focus, keyboard flow, and terminal interaction
- Go owns the runtime, state transitions, persistence, and long-running work
- keep the frontend and backend boundary observable and testable

Dual frontends are a good fit for operational products when both browser and terminal workflows are genuinely useful.

## Testing Baseline

- `go test ./...` is always the base path
- use table-driven tests where they make the cases easier to read
- use `httptest` for HTTP handlers
- use fuzz tests for parsers, protocol inputs, and attacker-controlled inputs
- keep integration tests explicit and easy to run locally

## Security Baseline

- `govulncheck` in CI
- dependency updates on a regular cadence
- explicit timeouts on outbound network calls
- no silent retry storms
- authenticated admin surfaces
- audit logging for security-relevant actions

## When To Choose Go Over Python

Choose Go when:

- the hard part is networking, concurrency, systems behavior, or daemon lifecycle
- operators need a durable service, CLI, or control-plane runtime
- you need straightforward concurrency and deployment simplicity
- the code is mostly service logic, not scripting or data tooling

Choose Python when the product is mostly automation, scripting, backend integration work, or data-heavy service logic.

Choose OpenTUI + TypeScript + Bun when the hard part is the terminal UX itself.

Choose Rust only when you are already in a Rust repo or the requirement is explicit enough that Go no longer fits.

## Avoid By Default

- heavyweight ORMs as the center of the data layer
- reflection-driven web frameworks
- giant DI containers
- multi-service decomposition before one binary is clearly failing
- adding Redis, Kafka, or extra infrastructure before PostgreSQL or SQLite plus a straightforward worker loop have been exhausted
- splitting a small product into extra deploy pipelines before one Go backend and its frontends actually need it
- `mattn/go-sqlite3` when `modernc.org/sqlite` works fine
