# Go Tech Stack

Last reviewed: 2026-03-23

## Best Fit

Use this stack when the project is mostly:

- services and daemons
- CLIs and operator tooling
- orchestration and control planes
- APIs and network-facing systems software
- durable-state applications
- integrations, automation, and operational products

For this workspace, this maps to `wirescope`, `riftline`, `vaultd`, `gitpulse`, `repokeeper`, and `podforge`.

For websites, frontends, and browser-facing web apps, the default lane is [Bun + TypeScript + Astro + Alpine.js](./bun-typescript-astro-alpine-tech-stack.md). Use this Go stack for the service/runtime side, not as the default frontend choice.

## Opinionated Default

| Area | Default | Why |
| --- | --- | --- |
| Toolchain | Go 1.26.1 | Current stable toolchain, excellent stdlib, strong tooling |
| Dependency management | Go modules | Native, boring, and reliable |
| Workspace mode | `go work` only when actively developing multiple modules together | Useful, but do not force it into every repo |
| Formatting | `gofmt` | Canonical formatting |
| Linting | `golangci-lint` plus `go vet` | Broad static checks with low operational cost |
| Vulnerability scan | `govulncheck` | Official vulnerability tooling |
| Logging | `log/slog` | Standard structured logging |
| HTTP | `net/http` first | The standard library is strong and keeps dependency count down |
| Router upgrade path | `chi` when routing and middleware structure outgrow the stdlib | Small, idiomatic, and not framework-heavy |
| Database | PostgreSQL | Best fit for durable state in this workspace |
| DB driver | `pgx/v5` | Best-in-class PostgreSQL driver and toolkit in Go |
| SQL layer | `sqlc` | Typed code from raw SQL without ORM magic |
| Migrations | `goose` | Simple and durable |
| Config | environment variables and flags first, `koanf` when multiple sources really matter | Avoid configuration theater |
| CLI | `flag` for small tools, `cobra` for large multi-command CLIs | Keep small tools small |
| Task runner | `mage` | Lets Go repos stay Go-native |
| Observability | `pprof`, `trace`, Prometheus metrics, OpenTelemetry when tracing is justified | Use the built-ins first, add tracing deliberately |
| RPC schemas | Buf + Protobuf only when network boundaries justify it | Strong contracts without mandatory framework sprawl |

## Golden Path

1. Start with a modular monolith, not a microservice fleet.
2. Use the standard library unless a small package clearly removes pain.
3. Use PostgreSQL, `pgx`, and `sqlc` for anything with real state.
4. Keep the binary self-contained and operationally obvious.
5. Add Prometheus metrics and structured logs from day one.
6. Add OpenTelemetry only when trace data will actually be consumed.

## Default Repo Shape

```text
project/
  cmd/
  internal/
  migrations/
  sql/
  static/
  README.md
  go.mod
```

Use `cmd/` for entrypoints, `internal/` for app code, `migrations/` for schema changes, and `sql/` for the source SQL that feeds `sqlc`.

## HTTP Guidance

- Default to `net/http`.
- Use `http.Server` with explicit timeouts.
- Use middleware sparingly and visibly.
- Reach for `chi` only when route grouping and middleware composition become materially easier with it.
- Avoid reflection-heavy frameworks unless the project has a very unusual requirement.

## Data Guidance

- PostgreSQL is the default durable store.
- `pgxpool` is the default connection layer for services.
- `sqlc` is the default path for typed data access.
- Use raw SQL and database constraints instead of pushing correctness into application folklore.
- Prefer transactions, proper indexes, and explicit query shape over magical repository layers.

## Testing Baseline

- `go test ./...` is always the base path.
- Use table-driven tests where they make the cases easier to read.
- Use `httptest` for HTTP handlers.
- Use fuzz tests for parsers, protocol inputs, and anything that ingests attacker-controlled data.
- Keep integration tests explicit and easy to run locally.

## Security Baseline

- `govulncheck` in CI.
- dependency updates on a regular cadence
- explicit timeouts on outbound network calls
- no silent retry storms
- audit logging for security-relevant actions

## When To Choose Go Over Zig Or C

Choose Go when:

- the system has durable state
- operators need an API, CLI, or administrative surface
- you need straightforward concurrency and deployment
- the code is mostly coordination, control, or application logic

Choose Zig when the project is mostly native systems logic and performance-sensitive machinery.

Choose C when the project is mostly ABI, firmware, or the narrowest possible low-level surface.

## Avoid By Default

- ORMs as the center of the data layer
- reflection-driven web frameworks
- giant DI containers
- multi-service decomposition before one binary is clearly failing
- adding Redis, Kafka, or extra infrastructure before PostgreSQL and a worker loop have been exhausted

## Primary Sources

- [Go downloads](https://go.dev/dl/)
- [Go release history](https://go.dev/doc/devel/release)
- [`slog` blog post](https://go.dev/blog/slog)
- [`net/http` ServeMux docs](https://pkg.go.dev/net/http#ServeMux)
- [`govulncheck` tutorial](https://go.dev/doc/tutorial/govulncheck)
- [`pgx` docs](https://pkg.go.dev/github.com/jackc/pgx/v5)
- [`sqlc` docs](https://docs.sqlc.dev/)
- [`chi` docs](https://go-chi.io/)
- [`goose` docs](https://pressly.github.io/goose/)
- [OpenTelemetry for Go](https://opentelemetry.io/docs/languages/go/)
- [Prometheus Go app guide](https://prometheus.io/docs/guides/go-application/)
- [`golangci-lint` docs](https://golangci-lint.run/)
