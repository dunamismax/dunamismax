# Go / C / PostgreSQL Tech Stack

The single stack I use across every project I own. One language, one
database, one VM—plus C for systems. Everything below is the default;
anything outside it has to earn its place.

## Core

- Go 1.26+
- C (clang/gcc, C11/C17)
- Standard library first
- `justfile` for every repo
- PostgreSQL 18
- Ubuntu LTS
- systemd
- Caddy 2.9+
- HTMX 2.0+
- Vanilla CSS or Tailwind v4

## Go Application Layer

- `net/http` for routing and handlers
- `html/template` for server-rendered HTML
- `sqlc` for typed SQL generation
- `pgx` for PostgreSQL access
- Forward-only SQL migrations (goose or golang-migrate)
- PostgreSQL-backed job tables with `FOR UPDATE SKIP LOCKED`
- Structured logging (slog)
- Zero-dependency binaries where practical

## C Systems Layer

- Clang / GCC
- Make or `just` for builds
- Focus on first-principles systems and performance
- Minimal dependencies

## PostgreSQL Data Platform

- Source of truth for all state
- `pgcrypto`, `pg_trgm`, `pg_stat_statements`, `btree_gin`
- JSONB for raw payloads and flexible documents
- Full-text search and trigram search
- Materialized views for summaries and pairing
- Time-ordered UUIDs (uuidv7)
- Explicit constraints and foreign keys

## Operations

- Single Ubuntu VM
- systemd for process management
- Caddy for TLS and reverse proxy
- GitHub Actions for CI and SSH-based deploy
- Automated `pg_dump` to offsite storage
- Regular restore drills
- Prometheus/Grafana for monitoring only when scale earns it
