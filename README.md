# Stephen Sawyer

I build self-hostable systems software in **Go, Zig, and C**, and I default to **Bun + Astro + Alpine.js** for browser-facing products.

The through-lines are networking, cryptography, observability, developer tooling, trading infrastructure, and operating-system work. When state matters, I default to **SQLite first**, move to **PostgreSQL only when the product clearly earns it**, keep data **relational by default**, use **Drizzle** for web-heavy apps, and reach for **`sqlc` or plain SQL** only when backend complexity justifies it. I like local-first tools, clean operator workflows, and software that still makes sense when something breaks at 2am.

---

## Portfolio

If you want the strongest entry points into my public work, start here, in order:

1. [bore](https://github.com/dunamismax/bore) — privacy-first file transfer with relay-assisted rendezvous, end-to-end encryption, and a clean CLI workflow.
2. [wirescope](https://github.com/dunamismax/wirescope) — terminal-first network observability with live capture, replay, and durable metadata.
3. [lockbox](https://github.com/dunamismax/lockbox) — Zig-first file crypto toolkit built around `seal`, `unseal`, `inspect`, and `keygen`.
4. [0xvane](https://github.com/dunamismax/0xvane) — local-first algorithmic trading workbench for signals, risk control, paper/live execution, and durable operator state.
5. [repokeeper](https://github.com/dunamismax/repokeeper) — self-hosted repo health daemon for remote validation, drift detection, and doc verification.
6. [riftline](https://github.com/dunamismax/riftline) — self-hosted secure ingress tunnel for exposing private services through a public relay.
7. [podforge](https://github.com/dunamismax/podforge) — local-first Commander / MTG session and results engine with a durable Go core.
8. [vaultd](https://github.com/dunamismax/vaultd) — small local HSM-style daemon with a C core and a Go control surface.
9. [gitpulse](https://github.com/dunamismax/gitpulse) — local-first repository analytics and operational insight with a terminal and browser operator surface.

## Long-Horizon Systems Work

- [dunamis](https://github.com/dunamismax/dunamis) — operating-system umbrella repo; **Basalt** is the kernel, with Zig for the kernel core, C at the firmware boundary, and Go for host tooling.

## Tech Stacks

- [tech-stacks](./tech-stacks/README.md) — opinionated reference stack docs for Web, C, Zig, Go, and unified Go + Zig + C + Web systems.

## Working Style

- **Go** for services, daemons, CLIs, and orchestration.
- **Bun + Astro + Alpine.js** for websites, frontends, and web apps.
- **TypeScript** in the browser where types help and framework ceremony does not.
- **Zig** for systems code, native tooling, protocol machinery, and low-level control.
- **C** for tight boundary-layer work: boot code, secure-memory custody, packet hot paths, and auditable interfaces.
- **SQLite by default**.
- **PostgreSQL when the product clearly earns it**.
- **Relational data by default**.
- **Drizzle for web-heavy apps**.
- **`sqlc` or plain SQL when backend complexity actually justifies it**.
- Build the boring core first. Earn complexity later.

---

I care about software that is inspectable, self-hostable, durable, and pleasant to build.