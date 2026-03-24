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

## Current Repos

These are the active repos right now. Some ship today. Some are still early build lanes. `podforge` is transitional and stays out of the main list.

### Browser-first products

- [CallRift](https://github.com/dunamismax/callrift) — self-hosted incident command with public status pages and a responder console. Domains: `callrift.com`, `callrift.dev`, `callrift.org`
- [DebugPath](https://github.com/dunamismax/debugpath) — self-hosted request-path debugger and investigation studio. Domain: `debugpath.dev`
- [ElChess](https://github.com/dunamismax/elchess) — open-source multiplayer chess platform for real play, analysis, puzzles, and tournaments. Domain: `elchess.org`
- [MyLifeRPG](https://github.com/dunamismax/myliferpg) — gamified habit engine with mood correlation, adaptive difficulty, and an RPG layer. Domain: `myliferpg.app`
- [Scrybase](https://github.com/dunamismax/scrybase) — local-first Commander intelligence for decks, collection tracking, and real pod meta. Domains: `scrybase.app`, `scrybase.net`
- [0xvane](https://github.com/dunamismax/0xvane) — local-first algorithmic trading workbench for signals, risk control, execution, and operator state. Domains: `0xvane.com`, `0xvane.dev`

### Infrastructure and observability

- [bore](https://github.com/dunamismax/bore) — privacy-first file transfer with a payload-blind relay and a real browser surface.
- [wirescope](https://github.com/dunamismax/wirescope) — terminal-first network observability with durable metadata and raw PCAP retention.
- [riftline](https://github.com/dunamismax/riftline) — self-hosted secure ingress tunnel for private services.

### Security and custody

- [lockbox](https://github.com/dunamismax/lockbox) — Zig-first file crypto toolkit built around `seal`, `unseal`, `inspect`, and `keygen`.
- [vaultd](https://github.com/dunamismax/vaultd) — small local HSM-style daemon with a C core and a Go control plane.

### Developer tooling

- [repokeeper](https://github.com/dunamismax/repokeeper) — self-hosted repo health daemon for doc verification, remote validation, and drift detection.
- [gitpulse](https://github.com/dunamismax/gitpulse) — local-first git activity analytics with separate ledgers for live work, commits, and pushes.

### Systems

- [dunamis](https://github.com/dunamismax/dunamis) — operating-system umbrella repo; **Basalt** is the kernel.

`podforge` remains the legacy transitional repo for Commander session and pod tracking until Scrybase reaches parity for that lane.

[tech-stacks](./tech-stacks/README.md) — opinionated reference docs for the web lane, Go, Zig, C, and the unified stack.
