# Stephen Sawyer

<div align="center">
  <strong>Rust. Local-first. Sharp tools.</strong>
  <br />
  <br />
  I build Cargo tools, native desktop apps, and local-first developer software in Rust.
  <br />
  Current focus: async diagnostics, observability, and SQLite-backed workflows.
  <br />
  <br />
  <a href="https://github.com/dunamismax">GitHub</a>
  ·
  <a href="https://codeberg.org/dunamismax">Codeberg</a>
</div>

<br />

<p align="center">
  <img alt="Rust" src="https://img.shields.io/badge/Rust-000000?style=for-the-badge&amp;logo=rust&amp;logoColor=white" />
  <img alt="Tokio" src="https://img.shields.io/badge/Tokio-DC2626?style=for-the-badge" />
  <img alt="SQLite" src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&amp;logo=sqlite&amp;logoColor=white" />
  <img alt="tracing" src="https://img.shields.io/badge/tracing-B45309?style=for-the-badge" />
  <img alt="Tauri v2" src="https://img.shields.io/badge/Tauri-v2-24C8D8?style=for-the-badge&amp;logo=tauri&amp;logoColor=white" />
</p>

## Flagship Project

### [GitPulse](https://github.com/dunamismax/gitpulse)

Local-first git analytics for working-tree activity, staged work, commits, pushes, sessions, streaks, goals, and dashboards.

GitPulse is the clearest expression of what I like building: software that stays local, surfaces real behavior, and turns noisy development activity into something inspectable and useful.

## Core Projects

### [TraceScope](https://github.com/dunamismax/tracescope)

Native Rust desktop viewer for Tokio `console-subscriber` telemetry with live task inspection, resource views, warnings, and SQLite-backed snapshots.

### [Patchworks](https://github.com/dunamismax/patchworks)

Native SQLite diff studio for schemas, rows, snapshots, and SQL export.

### [cargo-compatible](https://github.com/dunamismax/cargo-compatible)

Cargo subcommand for finding the highest dependency graph that still fits a target Rust version or MSRV.

### [CargoWatch](https://github.com/dunamismax/cargowatch)

Rust build monitor with managed runs, structured diagnostics, and SQLite-backed session history.

### [rust-async-field-guide](https://github.com/dunamismax/rust-async-field-guide)

Examples-first guide to practical async Rust: debugging, cancellation, observability, testing, and runtime-aware design.

### [cargo-async-doctor](https://github.com/dunamismax/cargo-async-doctor)

Cargo subcommand for detecting common async Rust hazards and explaining how to fix them.

## Selected Other Rust Work

- **[Deepblue](https://github.com/dunamismax/deepblue)** — truecolor terminal aquarium with procedural fish genomes, boids-inspired motion, and a full day/night cycle.
- **[Sand Sorcerer](https://github.com/dunamismax/sand-sorcerer)** — Bevy-built action-puzzler / roguelite vertical slice centered on reactive material-grid spellcasting.

## What I Optimize For

- Local-first software over service-heavy defaults
- Async systems that are observable and explainable
- SQLite as part of the product, not just storage
- Cargo tooling that solves real maintainer pain
- Tests, CI, benchmarks, and explicit quality gates
