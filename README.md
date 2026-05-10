# Stephen Sawyer

Systems-leaning engineer working in C, Zig, Python, and vanilla TypeScript. Open source, privacy, and security advocate. Fifteen years in IT, building software that has to keep working after the demo is over.

> Small languages, small tools, no frameworks. Software you can read at 2 AM and own end-to-end.

- Website: [dunamismax.com](https://dunamismax.com)
- GitHub: [@dunamismax](https://github.com/dunamismax)
- Codeberg: [@dunamismax](https://codeberg.org/dunamismax)

## What I Build

I build systems software, scripts, and small web apps that are durable, inspectable, and owned by the person who runs them. The goal is software with explicit data, explicit ownership, explicit failure modes, and no hidden framework architecture.

My toolkit is intentionally narrow:

- **C** (C23 preferred, C17 for portability) for the systems core: parsers, file formats, on-disk data, anything that has to be precise about memory and time.
- **Zig** for the build system, cross-compilation, codegen, helper tooling, and test harnesses. `zig cc` is how the C compiles; CMake stays out of the project.
- **Python** for scripting, automation, APIs, and backends — anywhere a clean, fast script or a small service is the right shape.
- **Vanilla HTML, CSS, and TypeScript** for websites and browser frontends. No frameworks, no build-time magic, no SPA tax when a server-rendered page works.

## Current Focus

### [zarc](https://github.com/dunamismax/zarc)

zarc is a local-first, content-addressed backup system written in C and built with Zig.

A zarc repository is a normal directory of explicit files, binary formats, and content-addressed objects — designed to remain understandable with ordinary tools. The early releases focus on a small archive core (store file bytes as hashed objects, record snapshots as explicit metadata, restore data from an inspectable repository) so the full backup system grows from boring, testable ground instead of framework architecture.

The build is Zig-only: `zig build`, `zig build test`, `zig build sanitize`, `zig build release`. C is compiled through `zig cc`. The project policy is allocator-clean code, fixed-width binary formats, fuzzable parsers, and recovery behavior that's easy to inspect at 2 AM.

It's my pinnacle current project and the work that defines how I write everything else now.

## Selected Work

- [zarc](https://github.com/dunamismax/zarc) — Local-first, content-addressed backup system. C, built with Zig.

## Principles

- **Small languages, no frameworks.** C, Zig, Python, and vanilla web. Anything that depends on a framework to stay coherent is too clever for what I want to build.
- **Explicit over magical.** Explicit ownership, explicit lifetimes, explicit errors, explicit allocation, explicit data flow. If you can't trace the value through the system, the system is broken.
- **Self-hostable over rented.** Software should run on hardware you control with data you can inspect and move.
- **Privacy and security as product requirements**, not decorations.
- **Open source when it helps people inspect, adapt, and own their tools.**
- **Boring infrastructure**, clear operations, and code you can read at 2 AM.

## License

Repository content is [GPL-3.0](LICENSE) unless an individual project specifies otherwise.
