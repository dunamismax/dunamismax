# Unified Go + Zig + C Tech Stack

Last reviewed: 2026-03-23

## Purpose

Use this stack when one product genuinely benefits from all three languages.

This is the right model for the kind of work already visible in this workspace:

- `dunamis`: Zig kernel core, C firmware boundary, Go host tooling
- `vaultd`: C custody core with a Go control surface
- future products that combine systems engines, operator surfaces, crypto, and self-hosted deployment

Do not use this stack for vanity. Use it when each language has a clear job.

## Division Of Labor

| Concern | Default language |
| --- | --- |
| Web UI, APIs, services, admin CLI, migrations, auth, persistence, observability | Go |
| Native engines, packet and protocol machinery, terminal apps, systems libraries, cross-compiled tools | Zig |
| Firmware edge, freestanding code, stable ABI shims, custody code, platform interop leafs | C |

## Architectural Rule

The default architecture is:

- Go owns the control plane
- Zig owns the systems engine
- C owns the narrowest low-level boundary

If a concern does not obviously belong to Zig or C, it belongs in Go.

## Interop Rule Order

Prefer cross-language integration in this order:

1. process boundary
2. stable file or socket protocol
3. narrow C ABI
4. only then a very small `cgo` bridge

That means:

- Go should usually talk to Zig or C components over Unix sockets, pipes, stdio, or a tightly defined RPC boundary
- Zig can own the native build and compile the C edge
- C stays leaf-like and avoids dragging the rest of the system into FFI debt

## The Default Unified Stack

| Area | Default |
| --- | --- |
| Root build spine | `zig build` |
| Go toolchain | Go 1.26.1 |
| Zig toolchain | Zig 0.15.2 stable |
| C toolchain | Clang by default, GCC as a portability check, `zig cc` for cross builds |
| Service transport | Go `net/http` or `chi` |
| Data store | PostgreSQL, owned by Go |
| Query layer | `pgx` + `sqlc` |
| Migrations | `goose` |
| Contracts | protobuf managed by Buf when typed RPC is required |
| Logs and metrics | emitted in Go as the primary operational surface |
| Tracing | OpenTelemetry at the Go boundary when worth it |
| Release shape | a small set of explicit binaries and artifacts, not a hidden polyglot maze |

## Recommended Repo Shape

```text
project/
  build.zig
  build.zig.zon
  cmd/
  internal/
  zig/
  c/
  proto/
  sql/
  migrations/
  out/
  README.md
```

Suggested responsibilities:

- `cmd/` and `internal/` for Go control-plane code
- `zig/` for systems engines, shared native libs, or TUIs
- `c/` for firmware or ABI-boundary code
- `proto/` only when the system actually benefits from typed contracts
- `sql/` and `migrations/` as Go-owned data boundaries

## Boundary Guidance

### Go <-> Zig

- prefer a process boundary for long-running engines and daemons
- use a narrow C ABI only for leaf functionality that truly benefits from in-process calls
- do not let Go business logic leak into native glue layers

### Zig <-> C

- use Zig as the build and integration spine
- keep C exposed through small headers and narrow contracts
- wrap imported C APIs in Zig-owned modules before they touch the rest of the codebase

### Go <-> C

- use `cgo` only for very small, well-audited surfaces
- never let `cgo` become the default integration model for broad subsystems

## Data And State Guidance

- PostgreSQL belongs on the Go side by default.
- SQL, migrations, auth, audit logs, and admin workflows belong on the Go side by default.
- Zig and C components should treat persistent state as an explicit dependency, not something they casually own.

This keeps the systems code focused and the operations story understandable.

## Observability Guidance

Go should be the main operator surface:

- structured logs
- metrics
- health endpoints
- tracing when needed
- admin CLI or HTTP endpoints

Zig and C components should emit simple, structured, parseable outputs rather than each inventing separate observability stacks.

## Security Guidance

- keep secret custody in the narrowest possible native layer
- keep policy, audit, and orchestration in Go
- review every cross-language boundary as if it were a network boundary
- keep ABI surfaces tiny and documented

## When This Stack Is The Right Call

Use the unified stack when:

- there is a real native core that earns Zig
- there is a real boundary or custody layer that earns C
- there is a real service, UI, or operational surface that earns Go

If any one of those jobs is fake, collapse the architecture and remove the language.

## Avoid By Default

- shared-state polyglot architectures
- broad `cgo` integration
- three different build systems fighting each other
- separate logging and config systems per language
- storing product logic in ABI glue code

## Primary Sources

- [Go downloads](https://go.dev/dl/)
- [Zig downloads](https://ziglang.org/download/)
- [Zig docs](https://ziglang.org/documentation/master/)
- [Clang docs](https://clang.llvm.org/docs/)
- [CMake docs](https://cmake.org/cmake/help/latest/)
- [`pgx` docs](https://pkg.go.dev/github.com/jackc/pgx/v5)
- [`sqlc` docs](https://docs.sqlc.dev/)
- [`goose` docs](https://pressly.github.io/goose/)
- [Buf docs](https://buf.build/docs/)
- [OpenTelemetry for Go](https://opentelemetry.io/docs/languages/go/)
