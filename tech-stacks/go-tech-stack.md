# Go Tech Stack

Last reviewed: 2026-03-29

## Best Fit

Use this stack when the project is mostly:

- services and daemons
- CLIs and operator tooling
- orchestration and control planes
- APIs and network-facing systems software
- durable application logic
- integrations, automation, and operational products

If the product needs a browser surface, pair Go with a [Python/FastAPI](./python-tech-stack.md) frontend layer using Jinja2 + htmx. In this workspace, that is the default web pairing for new Go-backed products.

## Opinionated Default

| Area | Default |
| --- | --- |
| Toolchain | Go (latest stable) |
| Dependency management | Go modules |
| Workspace mode | `go work` only when actively developing multiple modules together |
| Formatting | `gofmt` |
| Linting | `golangci-lint` plus `go vet` |
| Vulnerability scan | `govulncheck` |
| Logging | `log/slog` |
| HTTP | `net/http` first |
| Router upgrade path | `chi` when route structure and middleware outgrow the stdlib |
| Database | PostgreSQL by default; SQLite only when the repo is deliberately local-first, embedded, or tiny |
| PostgreSQL driver | `pgx/v5` (`database/sql` stdlib or `pgxpool` when the repo actually needs it) |
| SQLite driver | `database/sql` + `modernc.org/sqlite` when SQLite is the deliberate choice |
| Query layer | Plain SQL first; `sqlc` only when query surface genuinely justifies codegen |
| Migrations | SQL files first; tiny in-repo runner second; `goose` only when the repo truly needs it |
| Config | Environment variables and flags first, `koanf` only when multiple sources really matter |
| CLI | `flag` for small tools, `cobra` for large multi-command CLIs |
| Task runner | `mage` |
| Observability | `pprof`, `trace`, Prometheus metrics, OpenTelemetry when tracing is justified |
| RPC schemas | Buf + Protobuf + Connect only when network boundaries justify it |

## Database Default

Use PostgreSQL by default.

For most new Go applications in this workspace, that means:

- `pgx/v5` as the driver layer
- plain SQL first
- `sqlc` when the query surface clearly earns code generation
- SQL migrations checked into the repo

Choose SQLite only when the repo is deliberately one of these shapes:

- local-first single-user operator software
- embedded metadata/state inside a CLI or daemon
- offline-first utilities where shipping one file matters more than networked access
- tiny internal tools where PostgreSQL would be pure ceremony

## SQLite Driver Decision

When a repo deliberately uses SQLite, use `modernc.org/sqlite`.

It is a pure Go implementation. No CGO. No system library dependency. Clean single-binary story. Cross-compilation works without toolchain surgery. The performance difference from `mattn/go-sqlite3` is negligible for the workloads in this workspace.

Do not use `mattn/go-sqlite3` unless a specific repo has a verified, documented reason to require CGO-linked system SQLite.

Follow the [SQLite Operating Model](./README.md#sqlite-operating-model) in the tech-stacks README for pragma configuration, connection discipline, and migration patterns.

## Golden Path

1. Start with one binary and divide the code by capability, not architecture cosplay.
2. Use the standard library unless a small package clearly removes pain.
3. Start with PostgreSQL when the product needs durable state.
4. Use SQLite only when the repo is intentionally local-first, embedded, or tiny.
5. Use plain SQL first.
6. Add `sqlc` only when the query surface or team workflow really earns it.
7. Add structured logs and Prometheus metrics on day one for long-running services.
8. Keep the deploy shape obvious.
9. Pair Go with the Python/FastAPI server-rendered frontend when the browser is a first-class product surface.

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
- Relational data by default
- Plain SQL first
- `sqlc` only when backend complexity actually justifies it
- SQLite only when the repo is deliberately local-first, embedded, or tiny

That means:

- use PostgreSQL for new services, APIs, web backends, networked tools, and any Go application that is meant to grow
- use SQLite only for local-first tools, single-user operator software, embedded state, caches, or deliberately small utilities
- use database constraints, transactions, indexes, and explicit query shape instead of hiding truth in repository folklore
- keep schema truth in readable SQL migration files
- do not reach for a heavyweight Go ORM as the center of the data layer
- do not add extra infrastructure before the actual product shape earns it

## Web Pairing Guidance

When the product has a browser-facing frontend, a Python/FastAPI layer owns it. See `python-tech-stack.md`.

- Python (FastAPI + Jinja2 + htmx) owns templates, presentation, and browser interaction
- Go owns auth, business logic, persistence, jobs, and operational concerns
- the Python frontend fetches data from Go's JSON API endpoints
- keep the boundary same-origin HTTP or localhost proxy
- let SQLite live on the Go side, where persistent state belongs

## Testing Baseline

- `go test ./...` is always the base path
- Use table-driven tests where they make the cases easier to read
- Use `httptest` for HTTP handlers
- Use fuzz tests for parsers, protocol inputs, and anything that ingests attacker-controlled data
- Keep integration tests explicit and easy to run locally

## Security Baseline

- `govulncheck` in CI
- Dependency updates on a regular cadence
- Explicit timeouts on outbound network calls
- No silent retry storms
- Authenticated admin surfaces
- Audit logging for security-relevant actions

## When To Choose Go Over Python Or Rust

Choose Go when:

- the hard part is coordination, control, state, or operator workflow
- operators need an API, CLI, or administrative surface
- you need straightforward concurrency and deployment
- the code is mostly application logic, not native engine work

Choose Python when the product is mostly automation, scripting, server-rendered web work, or a browser-first application that does not need Go's deployment and concurrency profile.

Choose Rust only when you are working in an existing Rust repo or when the requirement is explicit enough that Go no longer fits on correctness, safety, or systems constraints.

## Avoid By Default

- Heavyweight ORMs as the center of the data layer
- Reflection-driven web frameworks
- Giant DI containers
- Multi-service decomposition before one binary is clearly failing
- Adding Redis, Kafka, or extra infrastructure before SQLite and a straightforward worker loop have been exhausted
- Splitting a small product into extra deploy pipelines before one Go service or one Go service plus a small Python frontend actually needs it
- `mattn/go-sqlite3` when `modernc.org/sqlite` works fine
