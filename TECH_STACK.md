# Rust / PostgreSQL / Python Tech Stack

Default stack for new work. Rust is the center. PostgreSQL is the data layer.
Python is for automation, scripting, prototypes, data work, and glue.

## Core

- Rust stable, edition 2024 where available
- Cargo workspaces for multi-crate projects
- Tokio for async systems when async is justified
- `tracing` for logs and diagnostics
- `serde` / `serde_json` / `toml` for structured data
- PostgreSQL as the primary database
- Python 3.13+ managed with `uv`
- Ruff for Python linting and formatting
- pytest for Python tests
- Bash, zsh, and PowerShell for operations
- macOS for local work, Ubuntu LTS for servers
- systemd, Caddy, SSH deploys, and reproducible runbooks

## Rust Systems Layer

- CLI tools and terminal apps
- Network services and protocol implementations
- QUIC/TLS where the product needs secure transport
- Cryptography-adjacent tooling with reviewed libraries
- Market-data, trading, and low-latency experiments
- Benchmarks before performance claims
- Small crates with explicit ownership boundaries
- `cargo fmt`, `cargo clippy`, `cargo test`, and release builds as the normal gate

## PostgreSQL Data Platform

- Source of truth for durable application state
- Explicit SQL migrations
- Relational schema first, JSONB when the data is genuinely document-shaped
- Full-text and trigram search when useful
- Audit tables and event history for important workflows
- Job tables with `FOR UPDATE SKIP LOCKED` where a queue can stay in Postgres
- Backups with `pg_dump` and tested restores

## Python Automation Layer

- `uv init`, `uv sync`, and project-local virtual environments
- `pyproject.toml` as the package/tooling contract
- Ruff for lint and format
- pytest for tests
- Pyright when static typing meaningfully reduces risk
- `httpx`, `pydantic`, and small focused libraries when they earn their place
- Scripts that can run from a clean checkout without manual dependency drift

## Operations

- One Ubuntu LTS VM until scale proves otherwise
- Caddy for TLS and reverse proxy
- systemd units for long-running services
- GitHub Actions for CI and SSH-based deploys
- Shell and PowerShell scripts for repeatable IT workflows
- Logs and health checks before dashboards
- Prometheus/Grafana only when operational scale earns them
