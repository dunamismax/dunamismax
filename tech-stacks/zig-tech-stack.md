# Zig Tech Stack

Last reviewed: 2026-03-23

## Best Fit

Use this stack when the project is mostly:

- native tooling
- protocol and packet machinery
- terminal interfaces
- systems libraries
- cross-compiled utilities
- kernel, runtime, or low-level platform work

For this workspace, this fits `lockbox` and the Zig core inside `dunamis`.

## Opinionated Default

| Area | Default | Why |
| --- | --- | --- |
| Toolchain | Zig 0.15.2 stable, track 0.16 when it becomes stable | Stay on stable for real projects, watch master for upcoming changes |
| Build system | `zig build` | Native, unified, and cross-target aware |
| Package management | `build.zig.zon` | Built-in dependency story, no external package manager needed |
| Formatting | `zig fmt` | Canonical formatting, no debate |
| Tests | `zig test` plus `std.testing` | First-class and fast |
| LSP | `zls` | Standard editor companion |
| C compilation | `zig cc` | Excellent C compiler frontend and cross-toolchain escape hatch |
| C interop | `@cImport`, `zig translate-c`, explicit wrappers | Good enough when used narrowly and deliberately |
| Logging | `std.log` or thin local wrappers | Keep logging explicit and low magic |
| Serialization | explicit binary formats, JSON when human readability matters | Good fit for systems tooling |
| Profiling | system profilers plus targeted instrumentation | Keeps the runtime simple |

## Golden Path

1. Use the stable Zig release for shipping work.
2. Keep `zig build`, `zig fmt`, and `zig test` as the core workflow.
3. Prefer the standard library first.
4. Add third-party packages only when they are clearly earned.
5. Keep allocator choice explicit in the API.
6. Use Zig as the native build spine whenever the repo has cross-target or mixed-language needs.
7. Let SQLite-owned business state live outside the Zig engine unless Zig is truly the right owner.

## Default Repo Shape

```text
project/
  src/
  tests/
  build.zig
  build.zig.zon
  README.md
```

If the repo exports a reusable library, keep `src/lib.zig` small and clean. If it is an app, make `src/main.zig` the obvious entrypoint and keep feature modules in `src/`.

## Dependency Rules

- Standard library first.
- Small dependency set second.
- Built-in package manager only.
- Avoid collecting immature framework dependencies.
- Prefer local modules for product-specific primitives instead of reaching for ecosystem sprawl.

## Memory And API Rules

- Make allocation explicit in public APIs.
- Do not hide allocator ownership.
- Return rich errors and use Zig's error handling directly.
- Use slices and clear ownership rules instead of clever abstractions.
- Use `ArenaAllocator` only where lifecycle boundaries are obvious.
- Use `GeneralPurposeAllocator` in development where extra checking helps.

## Testing And Safety Baseline

- `zig test` is the default unit and module test path.
- Add integration-style tests as normal executables under the build graph.
- Keep debug-safe code paths available early.
- Add focused property and fuzz-style testing for parsers, crypto framing, protocol edges, and packet work.

## Interop Rules

- Use C interop for platform SDKs, libc, and narrow leaf dependencies.
- Keep imported C APIs wrapped behind Zig-owned interfaces.
- If a Go service needs Zig functionality, prefer a process boundary or a very narrow leaf FFI surface.
- Avoid making Zig depend on large foreign runtime ecosystems.

## Web And State Guidance

Zig is excellent for engines, packet paths, CLIs, TUIs, and systems libraries. It is not the default choice here for browser-heavy product work or for stateful CRUD-style services with a lot of operator UI and persistence logic.

If persistent business state and web delivery dominate the project:

- keep the engine in Zig if it earns its place
- put the control plane and SQLite boundary in Go or the web lane
- keep raw SQL near the application owner instead of burying state in the engine

## When To Choose Zig Over C Or Go

Choose Zig when:

- you want low-level control without C's footguns as the default
- cross compilation matters
- explicit allocation and compile-time structure help the design
- the project is mostly systems logic, not just a thin ABI boundary

Choose C instead when the job is mostly firmware, legacy interop, or a tiny stable ABI surface.

Choose Go instead when the job is mostly services, persistence, orchestration, or web-facing operator workflows.

## Avoid By Default

- immature Zig web frameworks as the center of product architecture
- hidden allocators
- overusing `translate-c` output directly in business logic
- large dependency trees for simple tools
- turning `build.zig` into an unreadable metaprogram

## Primary Sources

- [Zig downloads](https://ziglang.org/download/)
- [Zig docs](https://ziglang.org/documentation/master/)
- [`zls` repository](https://github.com/zigtools/zls)
