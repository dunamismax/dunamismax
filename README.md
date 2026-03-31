# Stephen Sawyer

I build self-hostable, local-first software with boring infrastructure, explicit data models, and fast feedback loops.

My stack is getting simpler and more opinionated:

- TypeScript + Bun + Astro + Vue for web apps
- Go and Golang-first systems work for networking, daemons, and operator tools
- Python for scripting, automation, APIs, and glue code
- PostgreSQL by default when the product needs a real database
- OpenTUI when a terminal surface genuinely earns its place

Website: [dunamismax.com](https://dunamismax.com)

## Current focus

- full-stack web apps on Bun + TypeScript
- Go services and networking-heavy tools
- Python scripting and automation
- products that run cleanly on your own hardware

## Selected projects

### Full-stack apps and operator products

- [debugpath](https://github.com/dunamismax/debugpath) - Browser-first debug artifact workspace for incident timelines, artifact search, correlation, notes, and shareable debug bundles. In active build.
- [elchess](https://github.com/dunamismax/elchess) - Real-time multiplayer chess platform focused on fast play, durable game history, ratings, and post-game review. In active build.
- [myliferpg](https://github.com/dunamismax/myliferpg) - Planning-first personal operating system that unifies habits, routines, tasks, goals, quests, and progress tracking. In active build.
- [scrybase](https://github.com/dunamismax/scrybase) - Commander workbench for decks, collection tracking, pod history, and matchup notes.
- [gitpulse](https://github.com/dunamismax/gitpulse) - Local-first git activity analytics with a web dashboard and terminal workflow.
- [patchworks](https://github.com/dunamismax/patchworks) - SQLite diff and migration workbench for schema review, row diffs, snapshots, and merge workflows.
- [flowhook](https://github.com/dunamismax/flowhook) - HTTP capture, replay, mutation, auth analysis, endpoint cataloging, and export on top of mitmproxy.

### Go, networking, and systems

- [wirescope](https://github.com/dunamismax/wirescope) - Network observability with live capture, historical search, DNS context, alerts, and PCAP export.
- [bore](https://github.com/dunamismax/bore) - Encrypted peer-to-peer file transfer over QUIC with automatic relay fallback.
- [go-web-server](https://github.com/dunamismax/go-web-server) - Go starter for modern web apps with PostgreSQL, SQLC, Mage, and an Astro + Vue frontend.

### Python and automation

- [toolworks](https://github.com/dunamismax/toolworks) - Automation, CLI helpers, and scripts that earn their keep.
- [mtg-card-bot](https://github.com/dunamismax/mtg-card-bot) - Discord bot for fast Magic card lookups with live pricing, legality, and rulings.

### Rust, still in the maintenance lane

- [cargo-compatible](https://github.com/dunamismax/cargo-compatible) - Check whether a resolved dependency graph fits a target Rust version and fix blockers safely.
- [cargo-async-doctor](https://github.com/dunamismax/cargo-async-doctor) - Catch high-signal async Rust hazards and point to the fix.
- [rust-async-field-guide](https://github.com/dunamismax/rust-async-field-guide) - Examples-first guide to async Rust failure modes, debugging, and fixes.

## Build defaults

- [tech-stacks](./tech-stacks/README.md) - Current defaults for Bun + TypeScript web apps, Go backends, Python scripting, and OpenTUI terminal products.

## License

[MIT](LICENSE)
