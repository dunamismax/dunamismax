# Stephen Sawyer

**Systems software, self-hostable products, and practical build reference docs.**

Front door for my public work: an active index of the projects, products, and reference material I want people to hit first.

**Home:** [dunamismax.com](https://dunamismax.com) · [repo](https://github.com/dunamismax/dunamismax.com)

## Start Here

- [bore](https://github.com/dunamismax/bore) — move files between machines with a short code and end-to-end encryption. The relay never sees your data.
- [repokeeper](https://github.com/dunamismax/repokeeper) — run the verification commands your docs claim work, validate your remotes, and store the results. One binary, no cloud.
- [scrybase](https://github.com/dunamismax/scrybase) — Commander workbench that connects what you play, what you own, who you play against, and what actually wins.
- [wirescope](https://github.com/dunamismax/wirescope) — live network inspection for operators who need proof, not dashboards. Top talkers, DNS context, connection tables, and raw PCAP on disk.

## Rust Crates

- [cargo-compatible](https://github.com/dunamismax/cargo-compatible) — check whether your resolved dependency graph fits a target Rust version. Lockfile-first fixes before manifest changes.
- [cargo-async-doctor](https://github.com/dunamismax/cargo-async-doctor) — catch async Rust bugs that compile fine and pass Clippy but deadlock at 2 AM. Three high-signal checks with real fixes.
- [patchworks](https://github.com/dunamismax/patchworks) — open two SQLite databases and see exactly what changed: schema, rows, and the SQL to reconcile them.

## Notes and Reference

- [rust-async-field-guide](https://github.com/dunamismax/rust-async-field-guide) — learn async Rust by breaking things first. Twelve chapters of real footguns, reproductions, and verified fixes.
- [tech-stacks](./tech-stacks/README.md) — opinionated reference docs for how I build.

## Working Style

Most of the work here is **Go** and **Rust**, with **TypeScript** for browser-facing products.

- local-first when possible
- relational data by default
- small operational surfaces
- honest docs over hype
