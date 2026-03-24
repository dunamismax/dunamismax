# Go + Rust Tech Stack

Last reviewed: 2026-03-24

## Best Fit

Use this stack when the product genuinely needs both:

- **Go** for orchestration, control plane, CLI, persistence, APIs, and operator tooling
- **Rust** for a native runtime, shared systems core, protocol-heavy boundary, or safety-critical subsystem

This is the right model for repos shaped like:

- `wirescope`: Rust native capture/dissection lane + Go aggregation, persistence, and terminal/web surfaces
- `0xvane`: Go control plane with a Rust execution boundary for venue protocol, order-state, and hard risk logic

If the Rust boundary is fake, just use Go. If Go is fake, just use Rust. Both languages must earn their place.

If the product also needs a browser surface, read this doc for the backend/boundary and `spa-tech-stack.md` for the frontend. There is no single unified doc — compose the relevant docs instead.

## Division Of Labor

| Concern | Owner |
| --- | --- |
| APIs and services | Go |
| CLI and operator tooling | Go |
| Persistence (SQLite) | Go |
| Config, logging, metrics | Go |
| Auth, audit, admin | Go |
| Orchestration and lifecycle | Go |
| Native runtime core | Rust |
| Packet parsing, protocol handling, and binary formats | Rust |
| Secret custody and high-assurance leaf logic | Rust |
| Shared systems core reused across shells | Rust |

If a concern does not obviously belong to Rust, it belongs in Go. Rust owns the narrow subsystem or shared core that actually benefits from it.

## Interop Rule Order

Prefer cross-language integration in this order:

1. **Process boundaries** — separate binaries communicating over pipes, sockets, or files
2. **Stable file or socket protocols** — explicit wire formats between processes
3. **Well-defined RPC boundaries** — HTTP, Connect, gRPC, or other explicit transport only when earned
4. **Very small FFI bridges** — last resort, audited, tiny surface

Process boundaries are the default. They give you clean failure isolation, independent restart, and simpler debugging. Keep FFI tiny and treat it as a cost, not a feature.

## Default Stack

| Area | Default |
| --- | --- |
| Go toolchain | Go (latest stable) |
| Go dependency management | Go modules |
| Go SQLite driver | `database/sql` + `modernc.org/sqlite` |
| Go logging | `log/slog` |
| Go HTTP | `net/http` first, `chi` when route complexity earns it |
| Go CLI | `flag` for small tools, `cobra` for large multi-command CLIs |
| Go config | Environment variables and flags first |
| Go task runner | `mage` |
| Go formatting | `gofmt` |
| Go linting | `golangci-lint` + `go vet` |
| Go vulnerability scan | `govulncheck` |
| Rust toolchain | `rustup` + latest stable Rust |
| Rust workspace shape | Cargo workspace when more than one crate matters |
| Rust async runtime | Tokio |
| Rust logging / tracing | `tracing` |
| Rust serialization | `serde` + `serde_json` |
| Rust CLI | `clap` |
| Rust errors | `thiserror` + `anyhow` |
| Rust testing | `cargo test`, `cargo-nextest` when earned |
| Rust linting | `clippy` |
| Rust formatting | `rustfmt` |
| Rust advisory / license audit | `cargo-deny` |

## Recommended Repo Shape

```text
project/
  cmd/
  internal/
  rust/
    crates/
  migrations/
  sql/
  README.md
  go.mod
```

- `cmd/` for Go entrypoints
- `internal/` for Go application code
- `rust/` for the Rust runtime or shared core workspace
- `migrations/` for SQL schema changes
- `sql/` when the repo has enough queries to deserve explicit SQL files

If the Rust component is a standalone binary rather than a workspace, `rust/` may contain a single crate.

## Boundary Guidance (Go ↔ Rust)

- Prefer a **process boundary** for long-running native components. Go launches and supervises the Rust binary. Communication happens over pipes, sockets, or files.
- Use FFI only for **very small, well-audited surfaces**. A handful of functions, not an entire subsystem.
- Never let FFI become the default integration model. Every cross-language call adds build, debugging, and ownership complexity.
- Keep Rust exposed through **small interfaces and narrow contracts**. Explicit ownership. Explicit error handling. No hidden shared state.
- Review every cross-language boundary as if it were a network boundary.
- If the Rust component is long-running, give it its own binary and let Go manage its lifecycle.

## Data And State Guidance

Go owns persistence. The data doctrine is:

- relational by default
- SQLite by default
- plain SQL first
- thin helpers only when the repo clearly benefits

That means:

- Go owns the database, schema, migrations, jobs, audit, and operational state
- Rust does not casually own product persistence
- Rust reads and writes only the bytes it must for the boundary it owns
- schema truth lives in visible SQL files under `migrations/`
- follow the [SQLite Operating Model](./README.md#sqlite-operating-model) for pragma configuration, connection discipline, and migration patterns

## Observability Guidance

Go is the main operator surface:

- structured logs via `log/slog`
- Prometheus metrics
- health endpoints
- tracing when justified
- admin CLI or HTTP endpoints for diagnostics

Rust components should emit structured, parseable output and tracing that Go can aggregate or expose. Do not create two competing operator surfaces unless the product clearly earns that complexity.

## Security Guidance

- **Keep the dangerous leaf logic narrow.** Rust should own the boundary that benefits from stronger memory safety and explicit invariants.
- **Policy, audit, auth, and orchestration stay in Go.** The Go layer decides who gets access and what gets logged.
- **Review every cross-language boundary as if it were a network boundary.** Validate inputs. Check return values. Be explicit about ownership and timeouts.
- **Keep the Rust attack surface tight.** Fewer exported entrypoints, fewer ways in.
- `govulncheck` for Go and `cargo-deny` for Rust both belong in CI.

## Testing Baseline

### Go side

- `go test ./...` as the base path
- table-driven tests where they help readability
- `httptest` for HTTP handlers
- fuzz tests for parsers and protocol inputs

### Rust side

- `cargo test` as the base path
- property tests when invariants matter
- benchmarks for hot paths, parsers, collectors, and protocol-heavy code

### Integration

- end-to-end tests that exercise the Go ↔ Rust boundary through the actual integration path
- do not test the boundary only in unit isolation

## When To Use This Stack

Use Go + Rust when:

- the product needs Go for coordination, state, operator surface, and deployment story
- **and** the product needs Rust for a runtime core, native subsystem, or safety-critical boundary that Go should not own alone
- **and** both languages genuinely earn their place

## When Not To Use This Stack

- If the Rust boundary is fake or aspirational, just use Go. Read `go-tech-stack.md`.
- If Go is fake and the product is really a Rust tool, just use Rust. Read `rust-tech-stack.md`.
- Do not use this stack because it feels serious. Use it because the product has two genuinely different problems that map to two genuinely different tools.

## Avoid By Default

- broad FFI integration across the codebase
- shared-state polyglot architectures where both sides fight over the same memory
- separate logging, auth, and config systems per language
- storing product logic in glue code
- letting the Rust side grow into a second application with its own persistence and operator surface
- three build systems fighting each other
- introducing extra infrastructure before a clean SQLite path has actually failed
