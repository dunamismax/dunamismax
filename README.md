# Stephen Sawyer

I build self-hostable systems software: networking, cryptography, observability, trading infrastructure, and operating-system work.

**Stack:** Go, Zig, C, and PostgreSQL.
**Style:** raw SQL, local-first systems, clean operator workflows, durable software that still makes sense at 2am.

---

## Flagships

- [Riftline](https://github.com/dunamismax/riftline) — private ingress mesh for exposing internal services through a public relay without turning the whole thing into cloud theater.
- [Lockbox](https://github.com/dunamismax/lockbox) — Zig-first file crypto toolkit focused on `seal`, `unseal`, `inspect`, and `keygen`, with a tight UX and no cryptography cosplay.
- [Wirescope](https://github.com/dunamismax/wirescope) — terminal-first network observability with live capture, drill-down, and PostgreSQL-backed metadata instead of dashboard sludge.
- [Vaultd](https://github.com/dunamismax/vaultd) — small local HSM-style daemon with a C core, Unix socket control surface, and sharp operational boundaries.
- [Netweave](https://github.com/dunamismax/netweave) — userspace network stack in Zig, built as a layered library with demos instead of a monolithic moonshot.
- [Dunamis](https://github.com/dunamismax/dunamis) — operating-system umbrella repo; **Basalt** is the kernel, with Zig for kernel work, C at the firmware boundary, and Go for host tooling.

## Selected Repos

- [bore](https://github.com/dunamismax/bore) — secure file transfer with relay-assisted rendezvous and a clean CLI-first workflow.
- [gitpulse](https://github.com/dunamismax/gitpulse) — repository analytics and operational insight with Go, PostgreSQL, and a terminal/web operator surface.
- [0xvane](https://github.com/dunamismax/0xvane) — algorithmic trading workbench for signals, risk controls, paper/live execution paths, and PostgreSQL-backed state.
- [podforge](https://github.com/dunamismax/podforge) — local-first card and deck tooling with a Go/PostgreSQL core and operator-grade CLI direction.
- [rtop](https://github.com/dunamismax/rtop) — Zig terminal process monitor with fixture-driven verification and a systems-first design.
- [c-from-the-ground-up](https://github.com/dunamismax/c-from-the-ground-up) — practical C systems reference covering fundamentals through networking, crypto, and memory work.

## Working Philosophy

- Go for services, daemons, CLIs, and orchestration.
- Zig for systems code, native tooling, protocol machinery, and low-level control.
- C for auditable boundary-layer work: boot code, secure-memory custody, packet hot paths, and tight systems interfaces.
- PostgreSQL when state matters. Raw SQL always.
- Ship the boring core first. Earn complexity later.

---

If a repo is here, it is meant to become real software — not a parking lot for vague ideas.
