# Stephen Sawyer

Systems-leaning engineer working in C, Zig, PostgreSQL, Python, and vanilla TypeScript. Open source, privacy, and security advocate. Fifteen years in IT, building software that has to keep working after the demo is over.

> Small languages, small tools, no frameworks. Software you can read at 2 AM and own end-to-end.

- Website: [dunamismax.com](https://dunamismax.com)
- GitHub: [@dunamismax](https://github.com/dunamismax)
- Codeberg: [@dunamismax](https://codeberg.org/dunamismax)

## What I Build

I build systems software, scripts, and small web apps that are durable, inspectable, and owned by the person who runs them. The goal is software with explicit data, explicit ownership, explicit failure modes, and no hidden framework architecture.

My toolkit is intentionally narrow:

- **C** (C23 preferred, C17 for portability) for the systems core: parsers, file formats, on-disk data, anything that has to be precise about memory and time.
- **Zig** for the build system, cross-compilation, codegen, helper tooling, and test harnesses. `zig cc` is how the C compiles; CMake stays out of the project.
- **PostgreSQL** as the default data platform: relational state, JSONB documents, search, queues, audit logs, permissions, reporting, geospatial data, and vector search before adding specialized infrastructure.
- **Python** for scripting, automation, APIs, and backends — anywhere a clean, fast script or a small service is the right shape.
- **Vanilla HTML, CSS, and TypeScript** for websites and browser frontends. No frameworks, no build-time magic, no SPA tax when a server-rendered page works.

## Current Focus

### [zarc](https://github.com/dunamismax/zarc)

zarc is a local-first, content-addressed backup system written in C and built with Zig.

A zarc repository is a normal directory of explicit files, binary formats, and content-addressed objects — designed to remain understandable with ordinary tools. The v1.0.0 core can initialize a repository, archive a directory as content-addressed objects, record snapshots as strict binary metadata, list and show snapshots, restore files, verify repository health, and dump raw object bytes.

The build is Zig-only: `zig build`, `zig build test`, `zig build sanitize`, `zig build release`. C is compiled through `zig cc`. The project policy is allocator-clean code, fixed-width binary formats, fuzzable parsers, and recovery behavior that's easy to inspect at 2 AM.

It's my current flagship systems project and the work that defines how I write everything else now.

### [zwire](https://github.com/dunamismax/zwire)

zwire is an end-to-end encrypted file transfer tool written in C and built with Zig.

The target shape is two machines, one short human-readable code, and a file lands on the other side: no accounts, no daemon, no plaintext on the wire, and an optional self-hostable relay that only sees ciphertext. It is shaped after Magic Wormhole, with a PAKE handshake for code-to-key derivation and authenticated encryption for every byte after the handshake.

The project is in phase 0. The repo currently holds the README, build manual, and license while the implementation lands against a protocol-first plan.

### [ciphers](https://github.com/dunamismax/ciphers)

ciphers is an interactive cryptography playground for the browser.

It is a framework-free, local-only educational site for learning cryptography by transforming it: Caesar, Vigenere, Enigma, AES rounds, Diffie-Hellman, RSA toys, hashing, Merkle trees, and cryptanalysis tools with every algorithm implemented in readable TypeScript. No backend, no analytics, no third-party JavaScript at runtime.

The project is in phase 0. The repo currently holds the README, build manual, and license while the interactive site is built out.

## Selected Work

- [zarc](https://github.com/dunamismax/zarc) — Local-first, content-addressed backup system. C, built with Zig.
- [zwire](https://github.com/dunamismax/zwire) — End-to-end encrypted file transfer by short human code. C, Zig, PAKE, AEAD.
- [ciphers](https://github.com/dunamismax/ciphers) — Interactive browser cryptography playground. Vanilla HTML, CSS, and TypeScript.
- [dunamismax.com](https://github.com/dunamismax/dunamismax.com) — This site. Static HTML, CSS, TypeScript, Python build tooling, Caddy.

## Principles

- **Small languages, no frameworks.** C, Zig, Python, and vanilla web. Anything that depends on a framework to stay coherent is too clever for what I want to build.
- **Explicit over magical.** Explicit ownership, explicit lifetimes, explicit errors, explicit allocation, explicit data flow. If you can't trace the value through the system, the system is broken.
- **PostgreSQL first.** Durable application state belongs in PostgreSQL by default: relational data, JSONB documents, search, queues, audit logs, permissions, reporting, geospatial data, and vector search. Add Redis, Kafka, Elasticsearch, ClickHouse, or a dedicated vector database only when the workload proves Postgres is the wrong tool.
- **Self-hostable over rented.** Software should run on hardware you control with data you can inspect and move.
- **Privacy and security as product requirements**, not decorations.
- **Open source when it helps people inspect, adapt, and own their tools.**
- **Boring infrastructure**, clear operations, and code you can read at 2 AM.

## License

Repository content is [GPL-3.0](LICENSE) unless an individual project specifies otherwise.
