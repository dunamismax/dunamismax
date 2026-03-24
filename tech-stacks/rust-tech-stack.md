# Rust Tech Stack

Last reviewed: 2026-03-24

## Best Fit

Use this stack when the project is mostly:

- a native desktop or mobile tool with a Rust backend
- a cargo plugin, CLI, terminal app, or developer tool
- a shared cross-platform core with thin platform shells
- a local-first app with strong invariants and explicit boundaries
- a Rust-first web app or service where the browser stays thin
- a real-time, GPU, or interactive native application

For this workspace, that maps to `patchworks`, `cargo-compatible`, `cargo-async-doctor`, `tracescope`, `rust-async-field-guide`, and future Rust-first products.

If the browser is the real product surface and needs a full SPA, pair Rust with the [SPA](./spa-tech-stack.md) stack. If the browser is thin HTML over the wire, stay in this document.

## Architecture Principles

> **Rust-first core.** Keep business logic, state, validation, and domain rules in Rust.
>
> **Thin frontends.** Use the UI as a presentation layer with minimal business logic.
>
> **Shared core, platform shells.** Reuse core crates across platforms while isolating platform integrations.
>
> **Clear boundaries.** Separate domain, infrastructure, transport, and UI concerns.

## Opinionated Default

| Area | Default |
| --- | --- |
| Toolchain | `rustup` + latest stable Rust |
| Language server | `rust-analyzer` |
| Formatting | `rustfmt` |
| Linting | `clippy` |
| Test runner | `cargo test`, `cargo-nextest` once the suite grows |
| Dependency / advisory audit | `cargo-deny` |
| Async runtime | Tokio |
| Web framework | Axum |
| Browser strategy | HTMX + plain HTML/CSS |
| Desktop / mobile | Tauri v2 |
| Terminal UI | Ratatui |
| Native GUI | egui |
| HTTP client | reqwest |
| HTTP middleware | tower-http |
| Database | SQLite |
| Query layer | SQLx |
| Migrations | SQLx migrations |
| Serialization | serde + serde_json |
| Config | `config` + `toml` + env vars |
| CLI | clap |
| Errors | `thiserror` in libraries, `anyhow` at app boundaries |
| Observability | `tracing` |
| Benchmarks | criterion |
| Property testing | proptest |
| Interactive / game engine | Bevy |
| Graphics / compute | wgpu |

Follow the [SQLite Operating Model](./README.md#sqlite-operating-model) in the tech-stacks README for pragma configuration, migration discipline, and backup rules.

## Golden Path

1. Start with a Cargo workspace when the repo has more than one meaningful crate.
2. Keep domain logic in a Rust core crate with no UI assumptions.
3. Keep frontends thin: Tauri shell, Ratatui shell, egui shell, or Axum + HTMX shell.
4. Default to Tokio for async work and `tracing` for instrumentation.
5. Default to SQLite + SQLx when the product needs durable state.
6. Keep migrations in checked-in SQL files and run them explicitly.
7. Expose a CLI or deterministic local run path early, even for GUI apps.
8. Add benchmarks and property tests where invariants or performance actually matter.

## Default Workspace Shapes

### Cargo Tool Or CLI

```text
project/
  src/
  tests/
  Cargo.toml
  README.md
```

### Multi-Crate Product

```text
project/
  crates/
    app/
    core/
    ui/
  migrations/
  tests/
  Cargo.toml
  README.md
```

Use `core/` for domain logic and invariants, `app/` for orchestration and runtime wiring, and `ui/` for egui, Tauri, or other presentation concerns.

## Web Guidance

For Rust web products, the default is:

- Axum for HTTP and routing
- HTMX for browser interactivity
- plain HTML/CSS for rendering
- minimal JavaScript

This is the right default when you want server-owned state, simple browser behavior, and low frontend complexity.

If the product truly needs rich client-side state, route-level caching, and SPA behavior, pair Rust with the [SPA](./spa-tech-stack.md) stack instead of forcing HTMX to impersonate a frontend framework.

## UI Guidance

- Use Tauri v2 when you need desktop or mobile shells around a Rust core.
- Use Ratatui for terminal dashboards, operators tools, and internal UIs.
- Use egui for native tools, inspectors, viewers, and editors where shipping fast matters more than pixel-perfect native widgets.
- Use Bevy only when the product is genuinely interactive, simulation-heavy, or game-like.
- Use wgpu directly when rendering or compute is core to the product and an engine would be the wrong abstraction.

## Data Guidance

The Rust data doctrine is:

- SQLite by default
- relational data by default
- SQLx for database access
- explicit migrations in-repo

That means:

- keep schema truth in SQL migration files
- prefer checked queries over runtime stringly-typed drift
- keep database access behind narrow application services
- do not reach for a heavyweight service mesh or distributed store before SQLite has actually failed the workload

## Testing Baseline

- `cargo test` is always the base path
- add `cargo-nextest` when the suite is large enough to justify it
- use property tests for invariants, parsers, and tricky state transitions
- use criterion for hot paths, query engines, diff engines, collectors, and protocol-heavy code
- keep example apps or fixtures runnable when the repo is educational or tooling-heavy

## Security Baseline

- `cargo-deny` in CI for advisories, licenses, duplicates, and banned crates
- explicit timeout and retry policy for outbound network calls
- avoid hidden global mutable state
- keep secret handling and config loading visible and testable
- prefer narrow process and crate boundaries over clever cross-layer shortcuts

## When To Choose This Stack

Choose Rust when:

- correctness, performance, and explicit invariants matter
- the project benefits from a strong shared core across multiple shells
- the repo is a developer tool, native utility, terminal app, or local-first desktop product
- you want a small deploy surface with strong internal boundaries

## Avoid By Default

- putting core business logic in the UI layer
- thick browser clients when HTMX or server-rendered HTML is enough
- mixing multiple UI paradigms in one repo without a clear reason
- overusing macros when plain Rust is clearer
- choosing distributed infrastructure before a local-first design has been exhausted
