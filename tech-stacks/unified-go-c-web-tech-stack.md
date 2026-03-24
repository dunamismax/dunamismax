# Unified Go + C + Web Tech Stack

Last reviewed: 2026-03-24

## Purpose

Use this stack when one product genuinely benefits from all three lanes:

- Web for the browser surface
- Go for the control plane and durable application logic
- C for the narrowest low-level boundary

Do not use this stack for vanity. Use it when each lane has a clear job and deleting one of them would make the product worse.

This is the right model for work shaped like:

- `dunamis`: C kernel core, C firmware boundary, Go host tooling, and a future web-facing operator surface if the product earns one
- future products that combine systems engines, operator surfaces, crypto, self-hosted deployment, and a browser-facing UI

## Division Of Labor

| Concern | Default lane |
| --- | --- |
| Browser UI, docs, dashboards, account pages, operator frontend | Web |
| APIs, services, auth, persistence, admin CLI, jobs, metrics, audit, release plumbing | Go |
| Firmware edge, freestanding code, stable ABI shims, custody code, platform interop leafs, kernel internals | C |

## Architectural Rule

The default architecture is:

- Web owns presentation and browser-only interaction
- Go owns the control plane and the boundary the browser talks to
- C owns the narrowest low-level boundary and systems core

If a concern does not obviously belong to C, it belongs in Go. If it only exists because a human is in a browser, it belongs in the web lane.

## Interop Rule Order

Prefer cross-language integration in this order:

1. Browser talks to Go over same-origin HTTP
2. Go talks to C components over process boundaries
3. Stable file or socket protocols
4. Narrow C ABI
5. Only then a very small `cgo` bridge

That keeps the browser simple, the Go control plane obvious, and the native code leaf-like.

## The Default Unified Stack

| Area | Default |
| --- | --- |
| Web toolchain | Bun |
| Web framework | Astro |
| Web interaction layer | Alpine.js 3 |
| Go toolchain | Go (latest stable) |
| Go SQLite driver | `database/sql` + `modernc.org/sqlite` |
| C toolchain | Clang by default, GCC as a portability check |
| Cross compilation | Clang cross-target flags or platform-specific cross toolchains |
| Control-plane transport | Go `net/http` or `chi` |
| Typed contracts | Buf-managed Protobuf only when contracts justify it |
| Browser auth/session boundary | Terminate at the Go edge |
| Logs and metrics | Emitted in Go as the primary operational surface |
| Tracing | OpenTelemetry at the Go boundary when worth it |
| Release shape | A small set of explicit binaries and assets, not a hidden polyglot maze |

## Recommended Repo Shape

```text
project/
  web/
  cmd/
  internal/
  c/
  proto/
  sql/
  migrations/
  out/
  README.md
```

Suggested responsibilities:

- `web/` for the Astro frontend, browser assets, and web-owned presentation
- `cmd/` and `internal/` for Go control-plane code
- `c/` for firmware, ABI-boundary code, or systems core
- `proto/` only when the system actually benefits from typed contracts
- `sql/` and `migrations/` for explicit SQL owned by the application layer

## Boundary Guidance

### Web ↔ Go

- Let Web own routes, HTML, assets, and browser-only interaction
- Let Go own auth, business logic, jobs, and heavy service logic
- Keep the boundary same-origin and boring
- Do not leak backend topology into frontend build choices unless the product genuinely needs it

### Go ↔ C

- Prefer a process boundary for long-running native components
- Use `cgo` only for very small, well-audited surfaces
- Never let `cgo` become the default integration model for broad subsystems
- Keep C exposed through small headers and narrow contracts

## Data And State Guidance

The unified stack data doctrine is:

- Relational by default
- SQLite by default
- Plain SQL first
- Thin helpers only when the repo clearly benefits from them

That means:

- let the web lane stay fast and local-first with SQLite when it can
- let Go own persistence, jobs, auth, audit, and operational state
- keep C focused on boundaries and systems core, not casual ownership of application data
- keep schema truth in visible SQL files
- follow the [SQLite Operating Model](./README.md#sqlite-operating-model) for pragma configuration and connection discipline

## Observability Guidance

Go should be the main operator surface:

- structured logs
- metrics
- health endpoints
- tracing when needed
- admin CLI or HTTP endpoints

The web lane should report user-visible failures cleanly. C components should emit simple, structured, parseable outputs instead of each inventing separate observability stacks.

## Security Guidance

- Keep secret custody in the narrowest possible native layer
- Keep policy, audit, auth, and orchestration in Go
- Keep browser state shallow and first-party
- Review every cross-language boundary as if it were a network boundary
- Keep ABI surfaces tiny and documented

## When This Stack Is The Right Call

Use the unified stack when:

- there is a real browser-facing product or operator surface
- there is a real service or control plane that earns Go
- there is a real boundary, custody layer, or systems core that earns C

If any one of those jobs is fake, collapse the architecture and remove the lane.

## Avoid By Default

- Shared-state polyglot architectures
- Broad `cgo` integration
- Three different build systems fighting each other without a clear top-level entrypoint
- Separate logging, auth, and config systems per lane
- Storing product logic in ABI glue code
- Turning the web app into a second control plane
- Introducing extra persistence layers before a clean SQLite path has actually failed
