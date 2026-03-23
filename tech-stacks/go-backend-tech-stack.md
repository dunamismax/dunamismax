# Go Backend Tech Stack

Last reviewed: 2026-03-23

## Purpose

This is the backend-specific version of the Go stack for:

- APIs
- daemons
- service backends
- workers
- control planes
- internal operator systems

Use this when the browser UI is not the center of the project.

If the project does have a real browser frontend, the default pairing is [Bun + TypeScript + Astro + Alpine.js](./bun-typescript-astro-alpine-tech-stack.md) on the web side and Go on the backend side.

## The Default Backend Stack

| Area | Default |
| --- | --- |
| Language | Go 1.26.1 |
| Process model | modular monolith first |
| Transport | JSON over HTTP by default |
| HTTP layer | `net/http` plus explicit middleware, upgrade to `chi` if needed |
| Config | env vars, flags, optional `koanf` when config sources multiply |
| Logging | `log/slog` |
| Metrics | Prometheus |
| Tracing | OpenTelemetry only when trace data is worth the cost |
| Profiling | `pprof` and `trace` |
| Database | PostgreSQL |
| Driver | `pgxpool` |
| Query layer | `sqlc` over raw SQL |
| Migrations | `goose` |
| Background jobs | same binary worker loop first, PostgreSQL-backed job table before extra infra |
| Contracts | JSON first, Buf + Protobuf + Connect or gRPC when typed RPC is justified |
| Release shape | one deployable binary per service |

## Architecture Default

Start with one backend binary and divide the code by capability, not by technical layer theatre.

Good first split:

- `internal/httpapi`
- `internal/app`
- `internal/store`
- `internal/jobs`
- `internal/obs`

That is usually enough until scale or team shape proves otherwise.

## API Style Guidance

Default external API:

- JSON over HTTP
- stable route names
- explicit request validation
- explicit error envelopes

Default internal RPC when needed:

- Buf-managed Protobuf schemas
- Connect or gRPC for typed service-to-service calls

Do not introduce typed RPC just because it feels more serious. Use it when contract stability, generated clients, or inter-service evolution really justify it.

## Frontend Pairing Guidance

When a browser UI exists:

- let Astro own routes, HTML, assets, and presentation
- let Go own auth, business logic, SQL, jobs, and durable state
- keep the boundary boring: same-origin HTTP or one reverse proxy in front
- avoid coupling frontend deploy complexity to backend service boundaries unless there is a real product need

## Database Guidance

- PostgreSQL is the default source of truth.
- `sqlc` is the default query path.
- migrations live in-repo and ship with the service.
- use transactions deliberately and visibly.
- prefer database constraints over hand-wavy application promises.
- use `LISTEN/NOTIFY`, `SKIP LOCKED`, and regular SQL before adding queue infrastructure.

## Worker And Async Guidance

Default order of escalation:

1. synchronous request path
2. background goroutine in the same service when safe
3. PostgreSQL-backed jobs and worker polling
4. only then consider extra broker infrastructure

This keeps the operational model small and fits the kinds of self-hosted systems in this workspace.

## Observability Baseline

- structured logs with request or job correlation fields
- `/metrics` for Prometheus
- health and readiness endpoints
- `pprof` on an admin-only path
- tracing only for distributed flows or latency investigations that merit it

## Security Baseline

- timeouts on every server and outbound client
- authenticated admin surfaces
- audit logs for destructive or privileged actions
- `govulncheck` and linting in CI
- keep secrets in environment or platform secret stores, not in config files checked into repos

## Deployment Default

- ship a single Linux binary
- run under `systemd` or a small container image
- keep migrations as a first-class release step
- expose metrics and health explicitly
- avoid multi-container operational choreography unless there is a real need

## Avoid By Default

- service meshes for small systems
- generic repository abstractions over `sqlc`
- asynchronous infrastructure before PostgreSQL has been pushed hard enough
- adding a second database because one query is inconvenient
- framework-driven code generation as the backbone of the app

## Primary Sources

- [Go downloads](https://go.dev/dl/)
- [`net/http` docs](https://pkg.go.dev/net/http#ServeMux)
- [`pgx` docs](https://pkg.go.dev/github.com/jackc/pgx/v5)
- [`sqlc` docs](https://docs.sqlc.dev/)
- [`goose` docs](https://pressly.github.io/goose/)
- [OpenTelemetry for Go](https://opentelemetry.io/docs/languages/go/)
- [Prometheus Go app guide](https://prometheus.io/docs/guides/go-application/)
- [Buf docs](https://buf.build/docs/)
- [Connect RPC docs](https://connectrpc.com/docs/)
