# Stephen Sawyer

I build self-hostable systems software.

**Home:** [dunamismax.com](https://dunamismax.com) — profile site, project index, and durable public landing page.

Most of it lives in **Go, Zig, and C**, with **Bun + Astro + Alpine.js** on the browser-facing side. I bias toward local-first products, operator-friendly workflows, relational data, and software that stays legible when something breaks at 2am.

Defaults, not dogma:

- **Go** for services, daemons, CLIs, and orchestration
- **Zig** for native tooling, protocol machinery, and systems work
- **C** for tight boundary-layer code
- **Bun + Astro + Alpine.js** for browser surfaces
- **SQLite first**, **PostgreSQL when the product clearly earns it**
- **Relational by default**

---

## Selected Work

### Networking and operator tooling

- [bore](https://github.com/dunamismax/bore) — privacy-first file transfer with a payload-blind relay, end-to-end encryption, and a real browser surface.
- [wirescope](https://github.com/dunamismax/wirescope) — terminal-first network observability with durable metadata, raw PCAP retention, and a read-only browser companion.
- [riftline](https://github.com/dunamismax/riftline) — self-hosted secure ingress tunnel for exposing private services through a public relay.
- [debugpath](https://github.com/dunamismax/debugpath) — self-hosted request-path debugger for capturing, replaying, diffing, and exporting HTTP traffic.
- [repokeeper](https://github.com/dunamismax/repokeeper) — self-hosted repo health daemon for doc verification, remote validation, and drift detection.
- [gitpulse](https://github.com/dunamismax/gitpulse) — local-first git activity analytics with separate ledgers for live work, commits, and pushes.

### Security and custody

- [lockbox](https://github.com/dunamismax/lockbox) — Zig-first file crypto toolkit built around `seal`, `unseal`, `inspect`, and `keygen`.
- [vaultd](https://github.com/dunamismax/vaultd) — small local HSM-style daemon with a C core and a Go control surface.

### Stateful local-first products

- [callrift](https://github.com/dunamismax/callrift) — self-hosted incident command platform with public status pages, an authenticated responder console, and an optional built-in audio bridge.
- [0xvane](https://github.com/dunamismax/0xvane) — local-first algorithmic trading workbench for signals, risk control, execution, and operator state.
- [scrybase](https://github.com/dunamismax/scrybase) — local-first Commander workbench for decks, collection intelligence, pod results, and real meta tracking.

### Long-horizon systems work

- [dunamis](https://github.com/dunamismax/dunamis) — operating-system umbrella repo; **Basalt** is the kernel, with Zig for the kernel core, C at the firmware boundary, and Go for host tooling.

## Stack references

- [tech-stacks](./tech-stacks/README.md) — opinionated reference docs for the web lane, Go, Zig, C, and the unified Go + Zig + C + Web stack.

---

I like boring infrastructure, explicit data flow, and products you can actually run yourself.
