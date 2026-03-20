# Stephen Sawyer

<div align="center">
  <strong>Rust. Local-first. Ships.</strong>
  <br />
  <br />
  Builder of native desktop apps, terminal workbenches, web backends, and interactive Rust software that stays understandable.
  <br />
  <br />
  Most of my work lives at the intersection of observability, research workflows, Cargo/workspace tooling, diffing, and SQLite-backed local software, with a side channel of visual, real-time, and playable Rust experiments.
  <br />
  <br />
  <a href="https://github.com/dunamismax">GitHub</a>
  ·
  <a href="https://codeberg.org/dunamismax">Codeberg</a>
</div>

<br />

<p align="center">
  <img alt="Rust" src="https://img.shields.io/badge/Rust-000000?style=for-the-badge&amp;logo=rust&amp;logoColor=white" />
  <img alt="SQLite" src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&amp;logo=sqlite&amp;logoColor=white" />
  <img alt="Tauri v2" src="https://img.shields.io/badge/Tauri-v2-24C8D8?style=for-the-badge&amp;logo=tauri&amp;logoColor=white" />
  <img alt="Tokio" src="https://img.shields.io/badge/Tokio-DC2626?style=for-the-badge" />
  <img alt="SQLx" src="https://img.shields.io/badge/SQLx-0F172A?style=for-the-badge" />
  <img alt="Axum" src="https://img.shields.io/badge/Axum-111827?style=for-the-badge" />
  <img alt="HTMX" src="https://img.shields.io/badge/HTMX-3366CC?style=for-the-badge&amp;logo=htmx&amp;logoColor=white" />
  <img alt="Ratatui" src="https://img.shields.io/badge/Ratatui-166534?style=for-the-badge" />
  <img alt="egui" src="https://img.shields.io/badge/egui-334155?style=for-the-badge" />
  <img alt="Bevy" src="https://img.shields.io/badge/Bevy-1A1A1A?style=for-the-badge" />
  <img alt="wgpu" src="https://img.shields.io/badge/wgpu-0F766E?style=for-the-badge" />
  <img alt="tracing" src="https://img.shields.io/badge/tracing-B45309?style=for-the-badge" />
</p>

## Build Bias

- Local-first software over service-heavy architectures by default
- SQLite as an application substrate, not just an implementation detail
- Native desktop apps and TUIs when they make the tool clearer and faster
- Web backends and server-rendered interfaces when they keep the product simpler
- Diffs, timelines, search, and observability as first-class features
- Shared Rust domain cores with thin interface layers on top

## Preferred Stack

- **Application shells:** Tauri v2 for native desktop/mobile shells, Axum for APIs and server-rendered apps, HTMX + plain HTML/CSS for low-complexity web interaction, Ratatui for terminal interfaces, egui for native tools, and Bevy when the project wants a real-time engine.
- **Runtime and services:** Tokio for async execution, `tracing` for instrumentation, `reqwest` for outbound HTTP, and `tower-http` for practical Axum middleware.
- **Data and persistence:** SQLite by default for local-first software, SQLx + SQLx migrations for explicit schemas and checked queries, plus `serde`, `serde_json`, and `toml` for app boundaries and configuration.
- **CLI, config, and errors:** `clap` for developer-facing tools, `config` for layered settings, `thiserror` for library/domain errors, and `anyhow` at the application boundary.
- **Quality and validation:** `rustfmt`, `clippy`, `cargo-nextest`, `cargo-deny`, Criterion, and Proptest as the default quality/performance/testing toolbox.

## Portfolio Map

### Observability and System Visibility

**[TraceScope](https://github.com/dunamismax/tracescope)**
Native Rust viewer for Tokio `console-subscriber` telemetry. Connect to live gRPC streams, inspect tasks, spans, resources, and warnings, then persist snapshots to SQLite for later analysis.

**[HostLens](https://github.com/dunamismax/hostlens)**
macOS host-visibility recorder. Collects launch agents, ports, installed apps, recent files, and persistence points, then stores and diffs the machine over time.

**[ChangeRadar](https://github.com/dunamismax/changeradar)**
Local-first change watcher for web pages and local files. Normalizes content, scores diffs, stores history in SQLite, and raises desktop notifications when something materially changes.

### Research and Investigation

**[Caseboard](https://github.com/dunamismax/caseboard)**
Local-first investigation desktop app for sources, claims, evidence links, tags, snapshots, search, and time-oriented case timelines.

**[SourceDeck](https://github.com/dunamismax/sourcedeck)**
Terminal-native research workbench that ingests CSV, JSON, NDJSON, plain text, and SQLite query results into a searchable, taggable local vault.

**[Atlas Local](https://github.com/dunamismax/atlaslocal)**
Local dataset mapper that turns CSV and JSON into timeline reports with schema inference, field mapping, diagnostics, and Markdown/HTML export.

### Cargo and Workspace Tooling

**[Cargo Scout](https://github.com/dunamismax/cargoscout)**
Ratatui instrument panel for Cargo dependency graphs, shortest-path "why is this here?" tracing, feature visibility, and RustSec advisory surfacing.

**[cargo-capability](https://github.com/dunamismax/cargo-capability)**
Cargo subcommand that heuristically inventories sensitive capabilities in Rust workspaces, explains where they came from, and enforces simple CI policy.

**[cargo-compatible](https://github.com/dunamismax/cargo-compatible)**
Cargo subcommand for finding the highest dependency graph that still fits a chosen Rust version or MSRV, with candidate lockfile resolution and conservative manifest suggestions.

**[cargo-doctor-build](https://github.com/dunamismax/cargo-doctor-build)**
Stable-Rust build profiler for Cargo workflows. Captures machine-readable snapshots, renders HTML reports, and compares runs to surface regressions and slow units.

**[cargo-license-verify](https://github.com/dunamismax/cargo-license-verify)**
Cargo subcommand for verifying manifest license metadata, packaged license evidence, SPDX headers, and dependency licensing against CI policy.

### Data and Diff Utilities

**[Patchworks](https://github.com/dunamismax/patchworks)**
Native SQLite diff studio: inspect schemas, compare rows, snapshot live databases, and generate SQL intended to move one database toward another.

### Playable Systems and Games

**[Caseboard Noir](https://github.com/dunamismax/caseboard-noir)**
Local-first detective game built with Tauri, Axum, and SQLite. Read source documents, link claims to evidence, reveal the timeline, and file a final accusation.

**[Dependency Dungeon](https://github.com/dunamismax/dependency-dungeon)**
Ratatui roguelike about surviving a cursed dependency graph, complete with deterministic floors, cargo-themed enemies, and a Lockfile Lich boss.

**[Sand Sorcerer](https://github.com/dunamismax/sand-sorcerer)**
Bevy action-puzzler / roguelite where combat is driven by reactive material-grid chain reactions across a short handcrafted ruined-temple run.

### Visual, Audio, and Simulation Labs

**[Deepblue](https://github.com/dunamismax/deepblue)**
Truecolor terminal aquarium with procedural fish genomes, boids-inspired motion, breeding, feeding, bubbles, plants, and a day/night cycle.

**[Falling-Sand Lab](https://github.com/dunamismax/falling-sand-lab)**
Native `egui` cellular sandbox with seven reactive materials, instant presets, snapshot save/load, and a clean local desktop loop.

**[Fractal Forge](https://github.com/dunamismax/fractal-forge)**
GPU-powered fractal explorer with Mandelbrot, Julia, Burning Ship, and Tricorn modes, progressive rendering, palette cycling, and PNG export.

**[Signal Garden](https://github.com/dunamismax/signal-garden)**
Desktop particle-and-trail instrument built with `wgpu` and `egui`, tuned around curated presets, live control-surface tweaking, and screensaver mode.

**[Sonic Prism](https://github.com/dunamismax/sonic-prism)**
Microphone-driven audio visualizer that runs FFT analysis in Rust and renders multiple reactive GPU views through a native desktop shell.

**[Void Museum](https://github.com/dunamismax/void-museum)**
Desktop ray-marching gallery for impossible geometry and fractal objects, with orbit/fly camera modes plus PNG and GIF export.

## Beyond Rust

- **[go-web-server](https://github.com/dunamismax/go-web-server)**: Go starter with Echo, Templ, HTMX, PostgreSQL, SQLC, and Mage.
- **[c-from-the-ground-up](https://github.com/dunamismax/c-from-the-ground-up)**: Project-based C workbook for learning systems fundamentals and what abstractions cost.
- **[scryfall-discord-bot](https://github.com/dunamismax/scryfall-discord-bot)**: Discord bot for Magic: The Gathering card lookups via Scryfall.

<details>
  <summary>Archived TypeScript-first projects</summary>
  <br />
  <a href="https://github.com/dunamismax/roleback">Roleback</a>
  ·
  <a href="https://github.com/dunamismax/fieldlog">FieldLog</a>
  ·
  <a href="https://github.com/dunamismax/dispatch">Dispatch</a>
  ·
  <a href="https://github.com/dunamismax/chute">Chute</a>
  ·
  <a href="https://github.com/dunamismax/rip">rip</a>
  ·
  <a href="https://github.com/dunamismax/opsledger">OpsLedger</a>
  ·
  <a href="https://github.com/dunamismax/podwatch">PodWatch</a>
  ·
  <a href="https://github.com/dunamismax/questlog">QuestLog</a>
  ·
  <a href="https://github.com/dunamismax/arbor">Arbor</a>
  ·
  <a href="https://github.com/dunamismax/tsforge">tsforge</a>
</details>
