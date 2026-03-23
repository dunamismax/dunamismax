# Unified Go + Zig + C + Web Tech Stack

Last reviewed: 2026-03-23

## Purpose

Use this stack when one product genuinely benefits from all four lanes:

- Web for the browser surface
- Go for the control plane and durable application logic
- Zig for the native engine
- C for the narrowest low-level boundary

Do not use this stack for vanity. Use it when each lane has a clear job and deleting one of them would make the product worse.

This is the right model for work shaped like:

- `dunamis`: Zig kernel core, C firmware boundary, Go host tooling, and a future web-facing operator surface if the product earns one
- future products that combine systems engines, operator surfaces, crypto, self-hosted deployment, and a browser-facing UI

## Division Of Labor

| Concern | Default lane |
| --- | --- |
| Browser UI, docs, dashboards, account pages, operator frontend | Web |
| APIs, services, auth, persistence, admin CLI, jobs, metrics, audit, release plumbing | Go |
| Native engines, packet and protocol machinery, terminal apps, systems libraries, cross-compiled tools | Zig |
| Firmware edge, freestanding code, stable ABI shims, custody code, platform interop leafs | C |

## Architectural Rule

The default architecture is:

- Web owns presentation and browser-only interaction
- Go owns the control plane and the boundary the browser talks to
- Zig owns the systems engine
- C owns the narrowest low-level boundary

If a concern does not obviously belong to Zig or C, it belongs in Go. If it only exists because a human is in a browser, it belongs in the web lane.

## Interop Rule Order

Prefer cross-language integration in this order:

1. browser talks to Go over same-origin HTTP
2. Go talks to Zig or C components over process boundaries
3. stable file or socket protocols
4. narrow C ABI
5. only then a very small `cgo` bridge

That keeps the browser simple, the Go control plane obvious, and the native code leaf-like.

## The Default Unified Stack

| Area | Default |
| --- | --- |
| Web toolchain | Bun |
| Web framework | Astro |
| Web interaction layer | Alpine.js 3 |
| Web data default | SQLite + Drizzle |
| Go toolchain | Go 1.26.1 |
| Go data default | SQLite first |
| PostgreSQL path | only when the product clearly earns it |
| Heavier backend query path | plain SQL or `sqlc` when justified |
| Zig toolchain | Zig 0.15.2 stable |
| C toolchain | Clang by default, GCC as a portability check, `zig cc` for cross builds |
| Control-plane transport | Go `net/http` or `chi` |
| Typed contracts | Buf-managed Protobuf only when contracts justify it |
| Browser auth/session boundary | terminate at the Go edge |
| Logs and metrics | emitted in Go as the primary operational surface |
| Tracing | OpenTelemetry at the Go boundary when worth it |
| Release shape | a small set of explicit binaries and assets, not a hidden polyglot maze |

## Recommended Repo Shape

```text
project/
  web/
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

- `web/` for the Astro frontend, Drizzle schema, and browser assets
- `cmd/` and `internal/` for Go control-plane code
- `zig/` for systems engines, shared native libs, or TUIs
- `c/` for firmware or ABI-boundary code
- `proto/` only when the system actually benefits from typed contracts
- `sql/` and `migrations/` only when the Go side has earned an explicit heavier data boundary

## Boundary Guidance

### Web <-> Go

- let Web own routes, HTML, assets, and browser-only interaction
- let Go own auth, business logic, jobs, and heavy service logic
- keep the boundary same-origin and boring
- do not leak backend topology into frontend build choices unless the product genuinely needs it

### Go <-> Zig

- prefer a process boundary for long-running engines and daemons
- use a narrow C ABI only for leaf functionality that truly benefits from in-process calls
- do not let Go business logic leak into native glue layers

### Zig <-> C

- use Zig as the build and integration spine for native pieces
- keep C exposed through small headers and narrow contracts
- wrap imported C APIs in Zig-owned modules before they touch the rest of the codebase

### Go <-> C

- use `cgo` only for very small, well-audited surfaces
- never let `cgo` become the default integration model for broad subsystems

## Data And State Guidance

The unified stack data doctrine is:

- **relational by default**
- **SQLite by default**
- **Drizzle for web-heavy apps**
- **PostgreSQL only when the product clearly earns it**
- **plain SQL or `sqlc` only when backend complexity actually justifies it**

That means:

- let the web lane stay fast and local-first with SQLite when it can
- let Go take over heavier persistence, job coordination, auth, audit, and operational state when the product grows into that shape
- move to PostgreSQL because the product needs it, not because the stack doc said so years ago
- keep Zig and C focused on engines and boundaries, not casual ownership of application data

This keeps the systems code focused and the operations story understandable.

## Observability Guidance

Go should be the main operator surface:

- structured logs
- metrics
- health endpoints
- tracing when needed
- admin CLI or HTTP endpoints

The web lane should report user-visible failures cleanly. Zig and C components should emit simple, structured, parseable outputs instead of each inventing separate observability stacks.

## Security Guidance

- keep secret custody in the narrowest possible native layer
- keep policy, audit, auth, and orchestration in Go
- keep browser state shallow and first-party
- review every cross-language boundary as if it were a network boundary
- keep ABI surfaces tiny and documented

## When This Stack Is The Right Call

Use the unified stack when:

- there is a real browser-facing product or operator surface
- there is a real service or control plane that earns Go
- there is a real native core that earns Zig
- there is a real boundary or custody layer that earns C

If any one of those jobs is fake, collapse the architecture and remove the lane.

## Avoid By Default

- shared-state polyglot architectures
- broad `cgo` integration
- three different build systems fighting each other without a clear top-level entrypoint
- separate logging, auth, and config systems per lane
- storing product logic in ABI glue code
- turning the web app into a second control plane
- jumping to PostgreSQL, MongoDB, or extra infrastructure before the product has actually outgrown SQLite

## Primary Sources

- [Bun docs](https://bun.sh/docs)
- [TypeScript docs](https://www.typescriptlang.org/docs/)
- [Astro docs](https://docs.astro.build/)
- [Alpine.js docs](https://alpinejs.dev/start-here)
- [SQLite docs](https://www.sqlite.org/docs.html)
- [Drizzle docs](https://orm.drizzle.team/docs/overview)
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