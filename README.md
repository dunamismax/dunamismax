# Stephen Sawyer

I build self-hostable, local-first software for network ops, database tooling, operator workflows, and terminal-first products.

Python and Go still carry most backend work. Browser frontends now default to TypeScript + Bun + Astro. Vue is optional and has to earn its place. Terminal frontends default to OpenTUI + TypeScript + Bun. When the product shape justifies it, I want both.

Backend is chosen by fit:

- Python for APIs, automation, scripting, data work, and general backend services
- Go for networking, daemons, systems work, performance-sensitive services, and concurrency-heavy runtime paths
- Rust stays in the maintenance lane where it already earns its keep

[dunamismax.com](https://dunamismax.com)

---

## Security and networking

- [wirescope](https://github.com/dunamismax/wirescope) - Terminal-first network observability with live capture, historical search, DNS context, alerts, and PCAP export. `v1.0.0`
- [bore](https://github.com/dunamismax/bore) - Encrypted peer-to-peer file transfer over QUIC with automatic relay fallback. `v1.0.1`
- [flowhook](https://github.com/dunamismax/flowhook) - mitmproxy addon suite for capture, replay, mutation, auth analysis, endpoint cataloging, and export. `v1.0.1`

## Operator tools

- [patchworks](https://github.com/dunamismax/patchworks) - SQLite diff and migration workbench with schema diff, row diff, merge workflows, snapshots, and a local web UI. `v1.0.0`
- [gitpulse](https://github.com/dunamismax/gitpulse) - Local-first git activity analytics with separate ledgers for working tree, commit history, and push history. `v0.2.0`
- [toolworks](https://github.com/dunamismax/toolworks) - Small automation, CLI helpers, and working experiments. Active repo.

## Apps

- [scrybase](https://github.com/dunamismax/scrybase) - Local-first Commander workbench for deck building, collection tracking, pod history, and matchup notes. `v2.0.0`
- [mtg-card-bot](https://github.com/dunamismax/mtg-card-bot) - Discord bot for fast Magic card lookups with live pricing, legality, rulings, and embed-first responses. `3.0.0`

## Maintained Rust

- [cargo-compatible](https://github.com/dunamismax/cargo-compatible) - Check whether a resolved dependency graph fits a target Rust version, then fix blockers with a lockfile-first workflow. `v1.0.1`
- [cargo-async-doctor](https://github.com/dunamismax/cargo-async-doctor) - Catch high-signal async Rust hazards and point to the fix. `v1.0.1`
- [rust-async-field-guide](https://github.com/dunamismax/rust-async-field-guide) ([read it](https://dunamismax.github.io/rust-async-field-guide/)) - Examples-first guide to async Rust failure modes, debugging, and fixes. `v1.0.0`

## Learning and reference

- [c-from-the-ground-up](https://github.com/dunamismax/c-from-the-ground-up) ([read it](https://dunamismax.github.io/c-from-the-ground-up/)) - Progressive C workbook from basics to systems programming. `v1.0.0`
- [go-web-server](https://github.com/dunamismax/go-web-server) - Go starter for server-rendered apps with Echo, Templ, HTMX, PostgreSQL, SQLC, and Mage. `4.0.0`
- [hello-world-from-hell](https://github.com/dunamismax/hello-world-from-hell) - Deliberately cursed C. Useless in the best way. `v3.0.0`
- [tech-stacks](./tech-stacks/README.md) - Build defaults for Python and Go backends, Astro-first web frontends with optional Vue, and OpenTUI terminal products.

---

## License

[MIT](LICENSE)
