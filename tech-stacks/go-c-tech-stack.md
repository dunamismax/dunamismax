# Go + C Tech Stack

Last reviewed: 2026-03-24

## Best Fit

Use this stack when the product genuinely needs both:

- **Go** for orchestration, control plane, CLI, persistence, and operator tooling
- **C** for a narrow boundary — custody code, capture paths, ABI surfaces, packet hot paths, platform interop

This is the right model for repos shaped like:

- `vaultd`: C crypto core + Go control plane
- `wirescope`: C capture + Go aggregation, persistence, and TUI

If the C boundary is fake, just use Go. If Go is fake, just use C. Both languages must earn their place.

If the product also needs a browser surface, read this doc for the backend/boundary and the relevant web doc (`web-ssr-tech-stack.md` or `web-static-tech-stack.md`) for the frontend. There is no single unified doc — compose the relevant docs instead.

## Division Of Labor

| Concern | Owner |
| --- | --- |
| APIs and services | Go |
| CLI and operator tooling | Go |
| Persistence (SQLite) | Go |
| Config, logging, metrics | Go |
| Auth, audit, admin | Go |
| Orchestration and lifecycle | Go |
| ABI shims | C |
| Custody code and secret handling | C |
| Capture paths and packet hot paths | C |
| Firmware edges and platform interop leaves | C |

If a concern does not obviously belong to C, it belongs in Go. C owns the narrowest possible boundary and nothing more.

## Interop Rule Order

Prefer cross-language integration in this order:

1. **Process boundaries** — separate binaries communicating over pipes, sockets, or files
2. **Stable file or socket protocols** — well-defined wire formats between processes
3. **Narrow C ABI** — small headers, explicit contracts, caller-controlled allocation
4. **Very small `cgo` bridge** — last resort, audited, tiny surface

Process boundaries are the default. They give you clean failure isolation, independent restart, and simpler debugging. Keep `cgo` tiny and treat it as a cost, not a feature.

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
| Go observability | `pprof`, `trace`, Prometheus metrics, OpenTelemetry when tracing is justified |
| C language baseline | C23, with C17 fallback when portability forces it |
| C primary compiler | Clang/LLVM |
| C secondary compiler | GCC |
| C build system | CMake + Ninja |
| C formatter | `clang-format` |
| C static analysis | `clang-tidy`, `scan-build`, GCC `-fanalyzer` |
| C runtime checking | AddressSanitizer, UndefinedBehaviorSanitizer, ThreadSanitizer |
| C tests | Plain C test binaries + CTest |
| C fuzzing | libFuzzer with sanitizers |
| C crypto | libsodium |
| Cross compilation | Clang cross-target flags or platform-specific cross toolchains |

## Recommended Repo Shape

```text
project/
  cmd/
  internal/
  c/            # or daemon/ — the C boundary component
  migrations/
  sql/
  README.md
  go.mod
  CMakeLists.txt
```

- `cmd/` for Go entrypoints
- `internal/` for Go application code
- `c/` (or `daemon/`) for the C boundary component — includes `include/`, `src/`, `tests/`, `fuzz/`
- `migrations/` for SQL schema changes
- `sql/` when the repo has enough queries to deserve explicit SQL files
- Top-level `CMakeLists.txt` for the C build, `go.mod` for Go

## Boundary Guidance (Go ↔ C)

- Prefer a **process boundary** for long-running native components. Go launches and supervises the C binary. Communication happens over pipes, sockets, or files.
- Use `cgo` only for **very small, well-audited surfaces**. A handful of functions, not an entire subsystem.
- Never let `cgo` become the default integration model. Every `cgo` call is a context switch with non-trivial overhead and a debugging surface that is worse than either pure Go or pure C.
- Keep C exposed through **small headers and narrow contracts**. Caller-controlled allocation. Explicit ownership.
- Review every cross-language call site as if it were a network boundary.
- If the C component is long-running, give it its own binary and let Go manage its lifecycle.

## Data And State Guidance

Go owns persistence. The data doctrine is:

- Relational by default
- SQLite by default
- Plain SQL first
- Thin helpers only when the repo clearly benefits

That means:

- Go owns the database, schema, migrations, jobs, audit, and operational state
- C does not casually own application data
- C reads and writes only the bytes it must — custody secrets, capture buffers, ABI payloads
- Schema truth lives in visible SQL files under `migrations/`
- Follow the [SQLite Operating Model](./README.md#sqlite-operating-model) for pragma configuration, connection discipline, and migration patterns

## Observability Guidance

Go is the main operator surface:

- Structured logs via `log/slog`
- Prometheus metrics
- Health endpoints
- Tracing when justified
- Admin CLI or HTTP endpoints for diagnostics

C components emit simple, structured, parseable output. Logs go to stdout/stderr in a format Go can consume. C does not run its own metrics server or health endpoint — Go aggregates and exposes everything.

## Security Guidance

- **Secret custody in the narrowest C layer.** Libsodium for memory-hard primitives and secure-memory facilities. `explicit_bzero` or equivalent for secret-bearing buffers.
- **Policy, audit, auth, and orchestration in Go.** The Go layer decides who gets access and what gets logged. The C layer does the dangerous thing and nothing else.
- **Review every cross-language boundary as if it were a network boundary.** Validate inputs. Check return values. Do not trust the other side to handle errors for you.
- **Keep the C attack surface tiny.** Fewer functions exposed, fewer ways in.
- `govulncheck` for Go. Sanitizer jobs and `clang-tidy` for C. Both in CI.

## Testing Baseline

### Go side

- `go test ./...` as the base path
- Table-driven tests where they help readability
- `httptest` for HTTP handlers
- Fuzz tests for parsers and protocol inputs

### C side

- Unit tests as plain executables
- Sanitizer jobs mandatory in CI
- Fuzz targets for parsers, decoders, and packet handling
- Compile every target with both Clang and GCC in CI

### Integration

- End-to-end tests that exercise the Go ↔ C boundary through the actual integration path (process boundary, socket protocol, or `cgo` bridge)
- Do not test the boundary only in unit isolation

## When To Use This Stack

Use Go + C when:

- the product needs Go for coordination, state, operator surface, and deployment story
- **and** the product needs C for an auditable boundary that Go cannot cleanly own — custody code, capture paths, ABI shims, firmware edges, platform interop
- **and** both languages genuinely earn their place

## When Not To Use This Stack

- If the C boundary is fake or aspirational, just use Go. Read `go-tech-stack.md`.
- If Go is fake and the product is really a C tool, just use C. Read `c-tech-stack.md`.
- Do not use this stack because it feels serious. Use it because the product has two genuinely different problems that map to two genuinely different tools.

## Avoid By Default

- Broad `cgo` integration across the codebase
- Shared-state polyglot architectures where both sides fight over the same memory
- Separate logging, auth, and config systems per language
- Storing product logic in ABI glue code
- Letting the C side grow into a second application with its own persistence and operator surface
- Three build systems fighting each other — keep it to `go build` + CMake/Ninja with a clear top-level entrypoint
- Introducing extra infrastructure before a clean SQLite path has actually failed
