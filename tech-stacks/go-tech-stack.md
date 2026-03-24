# Go Tech Stack

Last reviewed: 2026-03-24

## Best Fit

Use this stack when the project is mostly:

- services and daemons
- CLIs and operator tooling
- orchestration and control planes
- APIs and network-facing systems software
- durable application logic
- integrations, automation, and operational products

If the browser surface is the product, pair Go with the [SPA](./spa-tech-stack.md) stack.

If the project also has a Rust runtime, shared core, or safety-critical subsystem, also read the [Go + Rust](./go-rust-tech-stack.md) stack.

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
| Database | SQLite |
| SQLite driver | `database/sql` + `modernc.org/sqlite` |
| Query layer | Plain SQL first; `sqlc` only when query surface genuinely justifies codegen |
| Migrations | SQL files first; tiny in-repo runner second; `goose` only when the repo truly needs it |
| Config | Environment variables and flags first, `koanf` only when multiple sources really matter |
| CLI | `flag` for small tools, `cobra` for large multi-command CLIs |
| Task runner | `mage` |
| Observability | `pprof`, `trace`, Prometheus metrics, OpenTelemetry when tracing is justified |
| RPC schemas | Buf + Protobuf + Connect only when network boundaries justify it |

## SQLite Driver Decision

Use `modernc.org/sqlite`. Always.

It is a pure Go implementation. No CGO. No system library dependency. Clean single-binary story. Cross-compilation works without toolchain surgery. The performance difference from `mattn/go-sqlite3` is negligible for the workloads in this workspace.

Do not use `mattn/go-sqlite3` unless a specific repo has a verified, documented reason to require CGO-linked system SQLite.

Follow the [SQLite Operating Model](./README.md#sqlite-operating-model) in the tech-stacks README for pragma configuration, connection discipline, and migration patterns.

## Golden Path

1. Start with one binary and divide the code by capability, not architecture cosplay.
2. Use the standard library unless a small package clearly removes pain.
3. Start with SQLite when the product needs state.
4. Use plain SQL first.
5. Add `sqlc` only when the query surface or team workflow really earns it.
6. Add structured logs and Prometheus metrics on day one for long-running services.
7. Keep the deploy shape obvious.
8. Pair Go with the SPA stack when the browser is a first-class product surface.

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

- SQLite by default
- Relational data by default
- Plain SQL first
- `sqlc` only when backend complexity actually justifies it

That means:

- use SQLite for local-first tools, single-node services, operator software, early products, and repos where easy setup matters more than networked concurrency
- use database constraints, transactions, indexes, and explicit query shape instead of hiding truth in repository folklore
- keep schema truth in readable SQL migration files
- do not reach for a heavyweight Go ORM as the center of the data layer
- do not add extra infrastructure before the single-file store is genuinely the bottleneck

## Web Pairing Guidance

When the product has a browser-facing frontend, the SPA stack owns it. See `spa-tech-stack.md`.

- the SPA (React + Vite) owns routes, presentation, and browser interaction
- Go owns auth, business logic, persistence, jobs, and operational concerns
- the SPA is served as static assets by the Go binary or a reverse proxy
- keep the boundary same-origin HTTP — no separate deploy pipeline unless the product has clearly earned it
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

## When To Choose Go Over Rust Or Web

Choose Go when:

- the hard part is coordination, control, state, or operator workflow
- operators need an API, CLI, or administrative surface
- you need straightforward concurrency and deployment
- the code is mostly application logic, not native engine work

Choose the SPA stack when the browser is the first-class product surface.

Choose Rust when the project is mostly a native tool, a shared-core systems product, or a boundary that benefits from stronger safety guarantees than Go alone.

## Avoid By Default

- Heavyweight ORMs as the center of the data layer
- Reflection-driven web frameworks
- Giant DI containers
- Multi-service decomposition before one binary is clearly failing
- Adding Redis, Kafka, or extra infrastructure before SQLite and a straightforward worker loop have been exhausted
- Splitting a small product into separate deploy pipelines when one binary serving the SPA as static assets is enough
- `mattn/go-sqlite3` when `modernc.org/sqlite` works fine
