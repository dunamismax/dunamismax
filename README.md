# Stephen Sawyer

I build self-hostable systems software.

**Home:** [dunamismax.com](https://dunamismax.com)

Most of it lives in **Go, Zig, and C**, with **Bun + Astro + Alpine.js** on the browser-facing side. I bias toward local-first products, operator-friendly workflows, relational data, **SQLite as the default store**, and **raw SQL as the default interface to state**.

Defaults, not dogma:

- **Go** for services, daemons, CLIs, and orchestration
- **Zig** for native tooling, protocol machinery, and systems work
- **C** for tight boundary-layer code
- **Bun + Astro + Alpine.js** for browser surfaces
- **SQLite first and unapologetically**
- **Raw SQL first**
- **Relational by default**

---

## Selected Work

### Products

- [callrift](https://github.com/dunamismax/callrift) — self-hosted incident command platform with public status pages, a responder console, and an optional audio bridge.
- [elchess](https://github.com/dunamismax/elchess) — open-source multiplayer chess platform with real-time play, Glicko-2 ratings, Stockfish WASM analysis, puzzles, and tournaments.
- [scrybase](https://github.com/dunamismax/scrybase) — local-first Commander intelligence for decks, collection tracking, pod results, and real meta analysis.
- [myliferpg](https://github.com/dunamismax/myliferpg) — gamified habit engine with mood-habit correlation, adaptive difficulty, and an RPG layer that fades into analytics.
- [0xvane](https://github.com/dunamismax/0xvane) — local-first algorithmic trading workbench for signals, risk control, execution, and operator state.

### Networking and infrastructure

- [bore](https://github.com/dunamismax/bore) — privacy-first file transfer with a payload-blind relay, end-to-end encryption, and a real browser surface.
- [wirescope](https://github.com/dunamismax/wirescope) — terminal-first network observability with durable metadata, raw PCAP retention, and a read-only browser companion.
- [riftline](https://github.com/dunamismax/riftline) — self-hosted secure ingress tunnel for exposing private services through a public relay.
- [debugpath](https://github.com/dunamismax/debugpath) — self-hosted request-path debugger and investigation studio for capturing, replaying, diffing, and exporting HTTP traffic.

### Security and custody

- [lockbox](https://github.com/dunamismax/lockbox) — Zig-first file crypto toolkit built around `seal`, `unseal`, `inspect`, and `keygen`.
- [vaultd](https://github.com/dunamismax/vaultd) — small local HSM-style daemon with a C core and a Go control surface.

### Developer tooling

- [repokeeper](https://github.com/dunamismax/repokeeper) — self-hosted repo health daemon for doc verification, remote validation, and drift detection.
- [gitpulse](https://github.com/dunamismax/gitpulse) — local-first git activity analytics with separate ledgers for live work, commits, and pushes.

### Systems work

- [dunamis](https://github.com/dunamismax/dunamis) — operating-system umbrella repo; **Basalt** is the kernel, with Zig for the kernel core, C at the firmware boundary, and Go for host tooling.

---

[tech-stacks](./tech-stacks/README.md) — opinionated reference docs for the web lane, Go, Zig, C, and the unified stack.
