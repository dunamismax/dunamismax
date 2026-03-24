# Go Tech Stack

Last reviewed: 2026-03-23

## Best Fit

Use this stack when the project is mostly:

- services and daemons
- CLIs and operator tooling
- orchestration and control planes
- APIs and network-facing systems software
- durable application logic
- integrations, automation, and operational products

For this workspace, that maps to `wirescope`, `riftline`, `vaultd`, `gitpulse`, `repokeeper`, and `podforge`.

If the browser surface is the product, start with the [Web Tech Stack](./web-tech-stack.md). If the browser is only an operator surface and one binary matters more than frontend specialization, Go can still own the HTML.

## Opinionated Default

| Area | Default | Why |
| --- | --- | --- |
| Toolchain | Go 1.26.1 | Current stable toolchain, excellent stdlib, strong tooling |
| Dependency management | Go modules | Native, boring, and reliable |
| Workspace mode | `go work` only when actively developing multiple modules together | Useful, but not mandatory ceremony |
| Formatting | `gofmt` | Canonical formatting |
| Linting | `golangci-lint` plus `go vet` | Broad static checks with low operating cost |
| Vulnerability scan | `govulncheck` | Official vulnerability tooling |
| Logging | `log/slog` | Standard structured logging |
| HTTP | `net/http` first | The stdlib is strong and keeps dependency count down |
| Router upgrade path | `chi` when route structure and middleware outgrow the stdlib | Small, idiomatic, not framework-heavy |
| Database default | SQLite | Fastest path to a real local app with minimal setup |
| SQLite path | `database/sql` + `modernc.org/sqlite` first | Pure Go, simple local setup, clean single-binary story |
| Native SQLite path | `database/sql` + `github.com/mattn/go-sqlite3` when CGO is acceptable | Useful when binding against system SQLite is intentional |
| Query layer | plain SQL first; `sqlc` only when query surface or team size clearly justify codegen | Keeps early repos light without giving up a typed path later |
| Migrations | SQL files first; tiny in-repo runner second; `goose` only when the repo truly needs a migration tool | Avoid ceremony before it helps |
| Config | environment variables and flags first, `koanf` only when multiple sources really matter | Avoid configuration theater |
| CLI | `flag` for small tools, `cobra` for large multi-command CLIs | Keep small tools small |
| Task runner | `mage` | Lets Go repos stay Go-native |
| Observability | `pprof`, `trace`, Prometheus metrics, OpenTelemetry when tracing is justified | Use the built-ins first |
| Browser surface when Go owns it | `templ` + `htmx` + server-rendered HTML | Good for operator UIs and one-binary apps |
| Sessions when Go owns the browser surface | `scs` | Boring web sessions |
| Validation when Go owns forms | `go-playground/validator` or explicit hand-written checks | Keep validation visible |
| Dev reload for browser-facing Go apps | `air` | Simple local loop |
| RPC schemas | Buf + Protobuf + Connect only when network boundaries justify it | Strong contracts without framework sprawl |

## Golden Path

1. Start with one binary and divide the code by capability, not architecture cosplay.
2. Use the standard library unless a small package clearly removes pain.
3. Start with SQLite when the product needs state.
4. Use plain SQL first.
5. Add `sqlc` only when the query surface or team workflow really earns it.
6. Add structured logs and Prometheus metrics on day one for long-running services.
7. Keep the deploy shape obvious.
8. Pair Go with the web lane when the browser is a first-class product surface.
9. Let Go render HTML directly only when that materially simplifies the product.

## Default Repo Shape

```text
project/
  cmd/
  internal/
  migrations/
  sql/
  static/
  views/
  README.md
  go.mod
```

Use `cmd/` for entrypoints, `internal/` for app code, `migrations/` for schema changes, and `sql/` when the repo has enough queries to deserve explicit SQL files.

`static/` and `views/` only belong here when Go owns the browser surface.

## HTTP Guidance

- Default to `net/http`.
- Use `http.Server` with explicit timeouts.
- Use middleware sparingly and visibly.
- Reach for `chi` only when route grouping and middleware composition become materially easier with it.
- Avoid reflection-heavy frameworks unless the project has a genuinely unusual requirement.

## Data Guidance

The Go data doctrine is:

- **SQLite by default**
- **relational data by default**
- **plain SQL first**
- **`sqlc` only when backend complexity actually justifies it**

That means:

- use SQLite for local-first tools, single-node services, operator software, early products, and repos where easy setup matters more than networked concurrency
- use database constraints, transactions, indexes, and explicit query shape instead of hiding truth in repository folklore
- keep schema truth in readable SQL migration files
- do not reach for a heavyweight Go ORM as the center of the data layer
- do not add extra infrastructure before the single-file store is genuinely the bottleneck

## Web Pairing Guidance

When the product has a real browser-facing frontend:

- let the [Web Tech Stack](./web-tech-stack.md) own routes, HTML shells, assets, and presentation
- let Go own auth, business logic, jobs, and heavy service logic
- let SQLite live on the side that actually owns the durable state
- keep the boundary boring: same-origin HTTP or one reverse proxy in front
- do not couple frontend deploy complexity to backend service boundaries unless the product actually needs it

## When Go Should Own The Browser Surface

Let Go render HTML directly when:

- one binary is a hard requirement
- the browser surface is an operator UI, admin console, dashboard, or internal tool
- server-rendered HTML already covers nearly all interaction
- authored JavaScript should stay near zero

The default shape there is `templ` for server-rendered components, `htmx` for partial updates, normal forms for mutations, SSE for live status, and `scs` for sessions. Do not turn a clean Go app into a JavaScript platform by accident.

## Testing Baseline

- `go test ./...` is always the base path
- use table-driven tests where they make the cases easier to read
- use `httptest` for HTTP handlers
- use fuzz tests for parsers, protocol inputs, and anything that ingests attacker-controlled data
- keep integration tests explicit and easy to run locally

## Security Baseline

- `govulncheck` in CI
- dependency updates on a regular cadence
- explicit timeouts on outbound network calls
- no silent retry storms
- authenticated admin surfaces
- audit logging for security-relevant actions

## When To Choose Go Over Web, Zig, Or C

Choose Go when:

- the hard part is coordination, control, state, or operator workflow
- operators need an API, CLI, or administrative surface
- you need straightforward concurrency and deployment
- the code is mostly application logic, not native engine work

Choose the [Web Tech Stack](./web-tech-stack.md) when the browser is the first-class product surface.

Choose Zig when the project is mostly native systems logic and performance-sensitive machinery.

Choose C when the project is mostly ABI, firmware, or the narrowest possible low-level surface.

## Avoid By Default

- heavyweight ORMs as the center of the data layer
- reflection-driven web frameworks
- giant DI containers
- multi-service decomposition before one binary is clearly failing
- adding Redis, Kafka, or extra infrastructure before SQLite and a straightforward worker loop have been exhausted
- splitting a small product into frontend and backend theater when one binary or one boring boundary is enough

## Primary Sources

- [Go downloads](https://go.dev/dl/)
- [Go release history](https://go.dev/doc/devel/release)
- [`slog` blog post](https://go.dev/blog/slog)
- [`net/http` ServeMux docs](https://pkg.go.dev/net/http#ServeMux)
- [`govulncheck` tutorial](https://go.dev/doc/tutorial/govulncheck)
- [SQLite docs](https://www.sqlite.org/docs.html)
- [SQLite SQL language reference](https://www.sqlite.org/lang.html)
- [`sqlc` docs](https://docs.sqlc.dev/)
- [`chi` docs](https://go-chi.io/)
- [`templ` guide](https://templ.guide/)
- [`htmx` docs](https://htmx.org/docs/)
- [`scs` package docs](https://pkg.go.dev/github.com/alexedwards/scs/v2)
- [`go-playground/validator` docs](https://pkg.go.dev/github.com/go-playground/validator/v10)
- [`air` repository](https://github.com/air-verse/air)
- [`goose` docs](https://pressly.github.io/goose/)
- [OpenTelemetry for Go](https://opentelemetry.io/docs/languages/go/)
- [Prometheus Go app guide](https://prometheus.io/docs/guides/go-application/)
- [Buf docs](https://buf.build/docs/)
- [Connect RPC docs](https://connectrpc.com/docs/)
- [`golangci-lint` docs](https://golangci-lint.run/)
