# Stephen Sawyer

Engineer working in Go, C, and PostgreSQL. Open source, privacy, and security advocate. Fifteen years in IT, building software that has to keep working after the demo is over.

> One language, one database, one VM. Software you can read at 2 AM and own end-to-end.

- Website: [dunamismax.com](https://dunamismax.com)
- GitHub: [@dunamismax](https://github.com/dunamismax)
- Codeberg: [@dunamismax](https://codeberg.org/dunamismax)

## What I Build

I build server-rendered web apps, backend services, and systems tooling that are durable, inspectable, and owned by the person who runs them. The goal is software with explicit data, explicit ownership, explicit failure modes, and one well-known runtime end to end.

My toolkit is intentionally narrow:

- **Go** for the application layer: web apps, APIs, workers, scheduled jobs, and CLIs.
- **C** for systems programming, performance-critical components, and ground-up learning.
- **PostgreSQL** as the single data platform: relational state, JSONB documents, full-text search, queues, audit logs, permissions, reporting, geospatial, and vector search before reaching for anything else.
- **Server-rendered HTML** with HTMX and restrained CSS. No SPA tax when a server-rendered page works.
- **One Ubuntu VM** with Caddy in front for TLS and reverse proxy, Go services under systemd, and PostgreSQL on the same box. Boring, debuggable, and easy to recover.

The full stack, with versions and the supporting libraries, is in [TECH_STACK.md](TECH_STACK.md).

## Current Focus

I am consolidating onto a single Go, C, and PostgreSQL stack and rewriting older projects on top of it. New projects are intentionally small, self-hostable, and PostgreSQL-first from the first migration.

## Live Projects

- [pod-tracker](https://github.com/dunamismax/pod-tracker) — Self-hosted Commander playgroup operating system. Go, PostgreSQL, server-rendered HTML, HTMX, sqlc, Caddy, and systemd.
- [mtg-card-bot](https://github.com/dunamismax/mtg-card-bot) — Magic: The Gathering card lookup Discord bot. Staying on Python.
- [go-web-server](https://github.com/dunamismax/go-web-server) — Go, PostgreSQL, sqlc, Echo, and embedded frontend starter with real auth and browser smoke tests.
- [c-from-the-ground-up](https://github.com/dunamismax/c-from-the-ground-up) — Learning and building systems from first principles in C.
- [hello-world-from-hell](https://github.com/dunamismax/hello-world-from-hell) — Cursed, performance-obsessed C for the sake of it.
- [dunamismax.com](https://github.com/dunamismax/dunamismax.com) — This profile's website. Public copy now reflects the Go, C, and PostgreSQL direction; the site implementation will be rewritten onto that stack.

## Principles

- **One language, one database.** Go and PostgreSQL by default, with C for systems and performance. Reach for something else only when the workload proves these are the wrong tools.
- **PostgreSQL first.** Durable application state belongs in PostgreSQL: relational data, JSONB documents, search, queues, audit logs, permissions, reporting, geospatial, and vector search. Add Redis, Kafka, Elasticsearch, ClickHouse, or a dedicated vector database only when the workload proves Postgres is the wrong tool.
- **Server-rendered by default.** HTML templates, HTMX, and restrained CSS cover most product surfaces without an SPA, a bundler, or a JavaScript framework.
- **Explicit over magical.** Explicit schemas, explicit migrations, explicit SQL with sqlc or a similarly transparent workflow, explicit errors. If you cannot trace the value through the system, the system is broken.
- **Self-hostable over rented.** Software should run on hardware you control with data you can inspect and move.
- **Privacy and security as product requirements**, not decorations.
- **Open source when it helps people inspect, adapt, and own their tools.**
- **Boring infrastructure.** One VM, one Go service, one database, one reverse proxy, one redeploy script.

## License

Repository content is [GPL-3.0](LICENSE) unless an individual project specifies otherwise.
