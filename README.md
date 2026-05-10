# Stephen Sawyer

Engineer working in Rust, Python, PostgreSQL, and vanilla TypeScript. Open source, privacy, and security advocate. Fifteen years in IT, building software that has to keep working after the demo is over.

> Small languages, small tools, no frameworks. Software you can read at 2 AM and own end-to-end.

- Website: [dunamismax.com](https://dunamismax.com)
- zwire: [zwire.cc](https://zwire.cc)
- ciphers: [ciphers.cc](https://ciphers.cc)
- GitHub: [@dunamismax](https://github.com/dunamismax)
- Codeberg: [@dunamismax](https://codeberg.org/dunamismax)

## What I Build

I build systems software, scripts, and small web apps that are durable, inspectable, and owned by the person who runs them. The goal is software with explicit data, explicit ownership, explicit failure modes, and no hidden framework architecture.

My toolkit is intentionally narrow:

- **Rust** for the systems core: protocol code, network services, parsers, file formats, anything that has to be precise about memory and time. Memory safety is a product requirement, not a perk.
- **Python** (3.12+) for APIs, control planes, scripting, automation, and backends. FastAPI + asyncpg + raw SQL. Modern tooling: `uv` for environments and packaging, `ruff` for lint and format, `mypy` where it earns its place.
- **PostgreSQL** as the default data platform: relational state, JSONB documents, search, queues, audit logs, permissions, reporting, geospatial data, and vector search before adding specialized infrastructure.
- **Vanilla HTML, CSS, and TypeScript** for websites and browser frontends. No frameworks, no build-time magic, no SPA tax when a server-rendered page works.
- **Caddy on Ubuntu** for TLS, static assets, reverse proxying, and boring deployment.

## Current Focus

### [zwire](https://zwire.cc)

zwire is a self-hosted, end-to-end encrypted file transfer service written in Rust, with a Python control plane on PostgreSQL, and published at [zwire.cc](https://zwire.cc).

The target shape is a public web portal and CLI where two people use one short human-readable code or share link and a file lands on the other side: no plaintext on the wire, no raw codes stored in PostgreSQL, and a self-hosted relay that only sees ciphertext. It is shaped after Magic Wormhole, with a PAKE handshake for code-to-key derivation and authenticated encryption for every byte after the handshake.

The repo lives at [github.com/dunamismax/zwire](https://github.com/dunamismax/zwire).

### [ciphers](https://ciphers.cc)

ciphers is an interactive cryptography playground for the browser, published at [ciphers.cc](https://ciphers.cc).

It is a framework-free, local-only educational site for learning cryptography by transforming it: Caesar, Vigenere, Enigma, AES rounds, Diffie-Hellman, RSA toys, hashing, Merkle trees, and cryptanalysis tools with every algorithm implemented in readable TypeScript. No backend, no analytics, no third-party JavaScript at runtime.

The repo lives at [github.com/dunamismax/ciphers](https://github.com/dunamismax/ciphers).

## Selected Work

- [zwire](https://zwire.cc) — End-to-end encrypted file transfer by short human code. Rust relay and protocol, Python control plane, PostgreSQL, PAKE, AEAD.
- [ciphers](https://ciphers.cc) — Interactive browser cryptography playground. Vanilla HTML, CSS, and TypeScript.
- [dunamismax.com](https://github.com/dunamismax/dunamismax.com) — This site. Static HTML, CSS, TypeScript, Python build tooling, Caddy.

## Principles

- **Small languages, no frameworks.** Rust, Python, and vanilla web. Anything that depends on a framework to stay coherent is too clever for what I want to build.
- **Memory safety on the network edge.** Code that handles untrusted bytes from the internet runs in a memory-safe language by default.
- **Explicit over magical.** Explicit ownership, explicit lifetimes, explicit errors, explicit data flow. If you can't trace the value through the system, the system is broken.
- **PostgreSQL first.** Durable application state belongs in PostgreSQL by default: relational data, JSONB documents, search, queues, audit logs, permissions, reporting, geospatial data, and vector search. Add Redis, Kafka, Elasticsearch, ClickHouse, or a dedicated vector database only when the workload proves Postgres is the wrong tool.
- **Self-hostable over rented.** Software should run on hardware you control with data you can inspect and move.
- **Privacy and security as product requirements**, not decorations.
- **Open source when it helps people inspect, adapt, and own their tools.**
- **Boring infrastructure**, clear operations, and code you can read at 2 AM.

## License

Repository content is [GPL-3.0](LICENSE) unless an individual project specifies otherwise.
