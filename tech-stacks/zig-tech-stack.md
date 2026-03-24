# Zig Tech Stack

Last reviewed: 2026-03-24

## Best Fit

Use Zig when the project needs:

- high-performance system components with deterministic memory management and no hidden allocators
- C interop without the overhead of a runtime, garbage collector, or borrow checker ceremony
- eBPF/BPF CO-RE helpers, kernel-adjacent tooling, or probe infrastructure
- capture-path hot loops, protocol parsers, or binary format handlers where C would traditionally own the boundary
- compact, auditable binaries for embedded or resource-constrained targets

Zig is not a replacement for Go or Rust in this workspace. It fills a specific niche: the boundary where C would otherwise be the answer, but you want better tooling, safer defaults, and a real build system.

## When To Reach For Zig

| Scenario | Zig fits? |
| --- | --- |
| BPF CO-RE skeletons and eBPF helper utilities | Yes |
| High-throughput capture probes or packet processors | Yes |
| C library wrappers with zero overhead | Yes |
| Protocol-level binary parsers that need C ABI compatibility | Yes |
| Small system utilities or single-purpose tools | Yes |
| Application-level services, APIs, or daemons | No — use Go |
| Safety-critical subsystems with complex ownership | No — use Rust |
| Browser-facing products | No — use the SPA stack |
| Desktop tools or cargo plugins | No — use Rust |

## Opinionated Default

| Area | Default |
| --- | --- |
| Toolchain | `zig` (latest stable release) |
| Build system | `build.zig` (Zig's built-in build system) |
| Testing | `zig test` with built-in test runner |
| C interop | `@cImport` for header inclusion, Zig's C backend for ABI compatibility |
| Allocator | Explicit allocator passing; `GeneralPurposeAllocator` for debugging, `FixedBufferAllocator` or arena for hot paths |
| Error handling | Zig error unions; no exceptions, no panics in library code |
| Logging | `std.log` |

## Architecture Principles

- **Zig owns the narrow, hot boundary.** Product logic stays in Go or Rust. Zig components handle capture, protocol framing, BPF interaction, or C interop — nothing more.
- **Process boundaries preferred.** Zig components should be standalone binaries or libraries consumed across a process boundary. Avoid deep in-process FFI unless the component is truly tiny.
- **Explicit allocation everywhere.** No hidden allocators. Every allocation is visible and auditable.
- **C ABI is the integration surface.** When Zig code needs to interop with Go or Rust, expose a C ABI. Keep the exported function set minimal.

## Default Repo Shape

### Standalone Zig component

```text
component/
  src/
    main.zig
  build.zig
  README.md
```

### Zig component inside a Go + Rust repo

```text
project/
  cmd/
  internal/
  rust/
  zig/
    src/
    build.zig
  README.md
  go.mod
```

The `zig/` directory sits alongside `rust/` and follows the same integration pattern: process boundary by default, narrow C ABI when in-process is justified.

## Testing Baseline

- `zig test` for unit tests (built-in, no framework needed)
- `zig build test` for the full test suite via the build system
- integration tests through the process boundary (Go or Rust drives the Zig binary and checks output)
- benchmarks via `std.time` or external measurement when performance is the justification for using Zig

## Security Baseline

- no undefined behavior by default (Zig's safety checks are on in debug, explicitly opted out in release)
- explicit bounds checking
- no hidden control flow
- `zig build` with ReleaseSafe for production unless profiling justifies ReleaseFast

## When Not To Use Zig

- If Go or Rust already handles the boundary well, do not introduce Zig for novelty.
- If the component needs complex ownership semantics, use Rust.
- If the component needs a garbage collector or goroutines, use Go.
- If the component is application logic, use Go.
- Do not use Zig because it is interesting. Use it because the alternative is writing C.

## Avoid By Default

- using Zig for application-level logic that belongs in Go
- replacing Rust's ownership model with manual Zig memory management in safety-critical paths
- building web servers or HTTP APIs in Zig
- introducing Zig into a repo without a clear boundary and build integration story
- mixing Zig and Rust in the same subsystem without a process boundary between them
