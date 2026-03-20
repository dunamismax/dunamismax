# Stephen Sawyer

<div align="center">
  <strong>Rust. Local-first. Ships.</strong>
  <br />
  <br />
  I build native desktop apps, terminal workbenches, Cargo tools, and SQLite-native software in Rust.
  <br />
  Most of my work sits at the intersection of observability, developer workflows, diffing, local analytics, and systems that stay understandable.
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
  <img alt="Tokio" src="https://img.shields.io/badge/Tokio-DC2626?style=for-the-badge" />
  <img alt="SQLx" src="https://img.shields.io/badge/SQLx-0F172A?style=for-the-badge" />
  <img alt="Tauri v2" src="https://img.shields.io/badge/Tauri-v2-24C8D8?style=for-the-badge&amp;logo=tauri&amp;logoColor=white" />
  <img alt="Axum" src="https://img.shields.io/badge/Axum-111827?style=for-the-badge" />
  <img alt="HTMX" src="https://img.shields.io/badge/HTMX-3366CC?style=for-the-badge&amp;logo=htmx&amp;logoColor=white" />
  <img alt="Ratatui" src="https://img.shields.io/badge/Ratatui-166534?style=for-the-badge" />
  <img alt="egui" src="https://img.shields.io/badge/egui-334155?style=for-the-badge" />
  <img alt="Bevy" src="https://img.shields.io/badge/Bevy-1A1A1A?style=for-the-badge" />
  <img alt="tracing" src="https://img.shields.io/badge/tracing-B45309?style=for-the-badge" />
</p>

## Start Here

If you only open five repositories, open these.
These are my primary build focus right now and the clearest picture of how I think about software.

### 1. [GitPulse](https://github.com/dunamismax/gitpulse)

Local-first git activity analytics for one repo or many. Tracks live working-tree changes, staged work, commits, pushes, sessions, streaks, goals, and achievements, then serves the history back through a responsive local dashboard backed by SQLite.

### 2. [TraceScope](https://github.com/dunamismax/tracescope)

Native Rust viewer for Tokio `console-subscriber` telemetry. Connect to live gRPC streams, inspect tasks, spans, resources, and warnings, then persist snapshots to SQLite for later analysis.

### 3. [Patchworks](https://github.com/dunamismax/patchworks)

SQLite diff studio for inspecting schemas, comparing rows, snapshotting live databases, and generating SQL intended to move one database toward another.

### 4. [cargo-doctor-build](https://github.com/dunamismax/cargo-doctor-build)

Stable-Rust build profiler for Cargo workflows. Captures machine-readable snapshots, renders standalone HTML reports, and compares runs to surface regressions, hot spots, and slow units without scraping Cargo timings HTML.

### 5. [cargo-capability](https://github.com/dunamismax/cargo-capability)

Cargo subcommand that heuristically inventories sensitive capabilities in Rust workspaces, explains where they came from, and enforces lightweight CI policy around unexpected behavior.

## What I Optimize For

- Local-first software over service-heavy architectures by default
- SQLite as an application substrate, not just an implementation detail
- Native desktop apps and TUIs when they make the product clearer and faster
- Cargo and workspace tooling that solves real maintainer pain
- Diffs, timelines, telemetry, and search as first-class features
- Shared Rust domain cores with thin interface layers on top
- Repos that ship with tests, CI, benchmarks, and explicit quality gates

## More Rust Projects

### Local-First Apps And Systems

**[Caseboard](https://github.com/dunamismax/caseboard)**  
Investigation desktop app for sources, claims, evidence links, tags, snapshots, search, and time-oriented case timelines.

### Cargo And Workspace Tooling

**[cargo-compatible](https://github.com/dunamismax/cargo-compatible)**  
Cargo subcommand for finding the highest dependency graph that still fits a chosen Rust version or MSRV, with candidate lockfile resolution and conservative manifest suggestions.

**[cargo-license-verify](https://github.com/dunamismax/cargo-license-verify)**  
Cargo subcommand for verifying manifest license metadata, packaged license evidence, SPDX headers, and dependency licensing against CI policy.

**[Cargo Scout](https://github.com/dunamismax/cargoscout)**  
Ratatui instrument panel for Cargo dependency graphs, shortest-path "why is this here?" tracing, feature visibility, and RustSec advisory surfacing.

### Playable Systems And Rust Experiments

**[Sand Sorcerer](https://github.com/dunamismax/sand-sorcerer)**  
Bevy action-puzzler / roguelite where combat is driven by reactive material-grid chain reactions across a short handcrafted ruined-temple run.

**[Deepblue](https://github.com/dunamismax/deepblue)**  
Truecolor terminal aquarium with procedural fish genomes, boids-inspired motion, breeding, feeding, bubbles, plants, and a full day/night cycle.

## Preferred Stack

- **Application shells:** Tauri v2, Axum, HTMX, Ratatui, egui, and Bevy when the project wants a real-time engine
- **Runtime and services:** Tokio, `tracing`, `reqwest`, and `tower-http`
- **Data and persistence:** SQLite by default, SQLx for explicit schemas and checked queries, plus `serde`, `serde_json`, and `toml`
- **CLI and errors:** `clap`, `thiserror`, `anyhow`, and layered config when the product needs it
- **Quality toolbox:** `rustfmt`, `clippy`, `cargo-nextest`, `cargo-deny`, Criterion, and Proptest

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
