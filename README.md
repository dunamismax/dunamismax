# Stephen Sawyer

<div align="center">
  <strong>Rust. Local-first. Ships.</strong>
  <br />
  <br />
  Builder of native desktop apps, terminal workbenches, and small systems that stay understandable.
  <br />
  Most of my work lives at the intersection of observability, research workflows, diffing, and SQLite-backed local software.
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
</p>

<p align="center">
  <img alt="Axum" src="https://img.shields.io/badge/Axum-111827?style=for-the-badge" />
  <img alt="HTMX" src="https://img.shields.io/badge/HTMX-3366CC?style=for-the-badge&amp;logo=htmx&amp;logoColor=white" />
  <img alt="Ratatui" src="https://img.shields.io/badge/Ratatui-166534?style=for-the-badge" />
  <img alt="egui" src="https://img.shields.io/badge/egui-334155?style=for-the-badge" />
  <img alt="tracing" src="https://img.shields.io/badge/tracing-B45309?style=for-the-badge" />
</p>

## Build Bias

- Local-first software over service-heavy architectures by default
- SQLite as an application substrate, not just an implementation detail
- Native desktop apps and TUIs when they make the tool clearer and faster
- Diffs, timelines, search, and observability as first-class features
- Shared Rust domain cores with thin interface layers on top

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

### Developer Tooling and Data Utilities

**[Patchworks](https://github.com/dunamismax/patchworks)**
Native SQLite diff studio: inspect schemas, compare rows, snapshot live databases, and generate SQL intended to move one database toward another.

**[Cargo Scout](https://github.com/dunamismax/cargoscout)**
Ratatui instrument panel for Cargo dependency graphs, shortest-path "why is this here?" tracing, feature visibility, and RustSec advisory surfacing.

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
