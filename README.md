# Stephen Sawyer

I build self-hostable systems software in **Go, Zig, and C**.

The through-lines are networking, cryptography, observability, developer tooling, trading infrastructure, and operating-system work. When state matters, I use **PostgreSQL** and write **raw SQL**. I like local-first tools, clean operator workflows, and software that still makes sense when something breaks at 2am.

---

## Start Here

If you want the strongest entry points into my work, start with these:

- [bore](https://github.com/dunamismax/bore) — privacy-first file transfer with relay-assisted rendezvous, end-to-end encryption, and a clean CLI workflow.
- [ztop](https://github.com/dunamismax/ztop) — Zig terminal system monitor focused on speed, legibility, and systems-level control.
- [lockbox](https://github.com/dunamismax/lockbox) — Zig-first file crypto toolkit built around `seal`, `unseal`, `inspect`, and `keygen`.
- [wirescope](https://github.com/dunamismax/wirescope) — terminal-first network observability with live capture, replay, and PostgreSQL-backed metadata.
- [riftline](https://github.com/dunamismax/riftline) — self-hosted secure ingress tunnel for exposing private services through a public relay.
- [dunamis](https://github.com/dunamismax/dunamis) — operating-system umbrella repo; **Basalt** is the kernel, with Zig for the kernel core, C at the firmware boundary, and Go for host tooling.

## Building Now

These are the other repos I think are most worth watching:

- [netweave](https://github.com/dunamismax/netweave) — userspace network stack in Zig, built as a layered library with demos.
- [vaultd](https://github.com/dunamismax/vaultd) — small local HSM-style daemon with a C core and a Go control surface.
- [gitpulse](https://github.com/dunamismax/gitpulse) — local-first repository analytics and operational insight with Go, PostgreSQL, and a terminal/web operator surface.
- [0xvane](https://github.com/dunamismax/0xvane) — local-first algorithmic trading workbench for signals, risk control, paper/live execution, and PostgreSQL-backed state.
- [repokeeper](https://github.com/dunamismax/repokeeper) — self-hosted repo health daemon for remote validation, drift detection, and doc verification.
- [podforge](https://github.com/dunamismax/podforge) — local-first Commander / MTG session and results engine with a Go/PostgreSQL core.

## Reference, Learning, and Smaller Builds

- [c-from-the-ground-up](https://github.com/dunamismax/c-from-the-ground-up) — practical C systems workbook from fundamentals through networking, crypto, and memory work.
- [go-web-server](https://github.com/dunamismax/go-web-server) — a boring-default Go starter for server-rendered apps with PostgreSQL and SQLC.
- [mtg-card-bot](https://github.com/dunamismax/mtg-card-bot) — Discord bot for fast Magic: The Gathering lookups.
- [hello-world-from-hell](https://github.com/dunamismax/hello-world-from-hell) — intentionally cursed C nonsense, which is sometimes its own kind of documentation.

## Tech Stacks

- [tech-stacks](./tech-stacks/README.md) — opinionated reference stack docs for C, Zig, Go, Go backends, Go full-stack apps, and unified Go + Zig + C systems.

## Working Style

- **Go** for services, daemons, CLIs, and orchestration.
- **Zig** for systems code, native tooling, protocol machinery, and low-level control.
- **C** for tight boundary-layer work: boot code, secure-memory custody, packet hot paths, and auditable interfaces.
- **PostgreSQL** when persistent state matters.
- **Raw SQL** over ORM theater.
- Build the boring core first. Earn complexity later.

---

I care about software that is inspectable, self-hostable, and durable.
