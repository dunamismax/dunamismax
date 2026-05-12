# Stephen Sawyer

Engineer working in Java, PostgreSQL, and server-rendered web apps. Open source, privacy, and security advocate. Fifteen years in IT, building software that has to keep working after the demo is over.

> One language, one database, one VM. Software you can read at 2 AM and own end-to-end.

- Website: [dunamismax.com](https://dunamismax.com)
- GitHub: [@dunamismax](https://github.com/dunamismax)
- Codeberg: [@dunamismax](https://codeberg.org/dunamismax)

## Current Focus

[callrift](https://github.com/dunamismax/callrift) is my primary build focus: an open-source, username-first communications platform for encrypted messages, WebRTC voice, group spaces, and technical communities without phone numbers as identity.

The live alpha is at [callrift.dev](https://callrift.dev).

## What I Build

I build server-rendered web apps and backend services that are durable, inspectable, and owned by the person who runs them. The goal is software with explicit data, explicit ownership, explicit failure modes, and one well-known runtime end to end.

My default stack is intentionally narrow:

- **Java 25 LTS** with Spring Boot 4, Maven, Java records, JDK toolchains, and virtual threads for web apps, APIs, services, scheduled jobs, and CLIs.
- **PostgreSQL 18** as the single data platform: relational state, JSONB documents, full-text search, audit trails, reporting, queues, and extensions only when the product earns them.
- **Server-rendered HTML** with Thymeleaf, HTMX, Tailwind CSS, vanilla JavaScript, and Alpine.js only when page-local state justifies it.
- **One Ubuntu LTS VM** with Caddy in front, a Spring Boot fat jar under systemd, PostgreSQL on the same box, GitHub Actions deploys over SSH, Flyway migrations, and `pg_dump` backups.

The full stack, with versions and supporting libraries, is in [TECH_STACK.md](TECH_STACK.md).

## Highlighted Projects

- [callrift](https://github.com/dunamismax/callrift) — Primary focus. Encrypted voice, messages, groups, and technical communities without phone numbers.
- [pod-tracker](https://github.com/dunamismax/pod-tracker) — Magic: The Gathering Commander pod, deck, collection, and game-night tracker.
- [c-from-the-ground-up](https://github.com/dunamismax/c-from-the-ground-up) — Progressive C learning workbook from basics to systems programming.
- [mtg-card-bot](https://github.com/dunamismax/mtg-card-bot) — Magic: The Gathering card lookup Discord bot powered by Scryfall.
- [go-web-server](https://github.com/dunamismax/go-web-server) — Go, PostgreSQL, SQLC, Echo, and embedded Astro/Vue starter.
- [hello-world-from-hell](https://github.com/dunamismax/hello-world-from-hell) — Deliberately overbuilt C "Hello World" joke repo with real build discipline.

## Principles

- **One language, one database.** Java and PostgreSQL by default. Reach for something else only when the workload proves these are the wrong tools.
- **PostgreSQL first.** Durable application state belongs in PostgreSQL: relational data, JSONB documents, search, queues, audit logs, permissions, reporting, geospatial, and vector search. Add Redis, Kafka, Elasticsearch, ClickHouse, or a dedicated vector database only when the workload proves Postgres is the wrong tool.
- **Server-rendered by default.** Thymeleaf, HTMX, and Tailwind cover most product surfaces without an SPA, a bundler, or a JavaScript framework.
- **Explicit over magical.** Explicit schemas, explicit migrations with Flyway, explicit SQL with jOOQ, explicit errors. If you cannot trace the value through the system, the system is broken.
- **Self-hostable over rented.** Software should run on hardware you control with data you can inspect and move.
- **Privacy and security as product requirements**, not decorations.
- **Open source when it helps people inspect, adapt, and own their tools.**
- **Boring infrastructure.** One VM, one fat jar, one database, one reverse proxy, one redeploy path.

## License

Repository content is [GPL-3.0](LICENSE) unless an individual project specifies otherwise.
