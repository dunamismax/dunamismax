# Stephen Sawyer

Systems software, self-hostable products, and reference docs for people who build things.

**Home:** [dunamismax.com](https://dunamismax.com)

---

## Products

- [bore](https://github.com/dunamismax/bore) — peer-to-peer encrypted file transfer. Direct connections first, relay fallback when NAT wins. No accounts, no cloud, no trust required.
- [wirescope](https://github.com/dunamismax/wirescope) — terminal-first network observability. Live capture, top talkers, DNS context, connection tables, PCAP on disk. Go core with Rust capture backend.
- [repokeeper](https://github.com/dunamismax/repokeeper) — self-hosted repo health daemon. Validates remotes, detects drift, runs the verification commands your docs claim work, and stores the results. One binary, no cloud.
- [patchworks](https://github.com/dunamismax/patchworks) — git-style diffs for SQLite databases. Schema, rows, and the SQL to reconcile them. Native desktop app and headless CLI.

## Rust Crates

- [cargo-compatible](https://github.com/dunamismax/cargo-compatible) — check whether your resolved dependency graph fits a target Rust version. Lockfile-first, fixes before manifest changes.
- [cargo-async-doctor](https://github.com/dunamismax/cargo-async-doctor) — catch async Rust bugs that compile fine and pass Clippy but deadlock at 2 AM.

## Labs

- [scrybase](https://github.com/dunamismax/scrybase) — Commander intelligence workbench. Decks, collection, pod tracking, matchup journal, Scryfall integration, and real meta from your actual games.

## Toolbox

- [toolworks](https://github.com/dunamismax/toolworks) — automation, CLI helpers, and working experiments. A curated workshop for scripts and small tools that earn their keep.

## Reference

- [rust-async-field-guide](https://github.com/dunamismax/rust-async-field-guide) ([read it](https://dunamismax.github.io/rust-async-field-guide/)) — learn async Rust by breaking things first. Twelve chapters of real footguns, reproductions, and verified fixes.
- [tech-stacks](./tech-stacks/README.md) — opinionated stack docs for how I build.

---

**Python** and **Go** for most things. **Rust** where it earns its keep. **TypeScript** for browser surfaces. SQLite by default. Local-first when possible. Honest docs over hype.
