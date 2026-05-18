# Stephen Sawyer

Rust-first engineer and IT operator focused on high-performance systems,
crypto infrastructure, cryptography, encryption, PostgreSQL-backed products,
and Python automation.

> Build fast systems you can inspect, operate, and own.

- Website: [dunamismax.com](https://dunamismax.com)
- GitHub: [@dunamismax](https://github.com/dunamismax)
- Codeberg: [@dunamismax](https://codeberg.org/dunamismax)

## Focus

I am going deep on Rust for performance-sensitive software: market data,
trading infrastructure, local-first tools, secure networking, protocol work,
and systems that need predictable behavior under pressure.

The supporting stack is deliberately small:

- **Rust** for production systems, CLIs, network services, protocol work,
  cryptography-adjacent tooling, and performance-critical paths.
- **PostgreSQL** as the primary data layer for durable state, audit trails,
  analytics, queues, search, and operational reporting.
- **Python** for scripting, prototypes, data work, automation, bots, and glue.
  New Python work uses `uv`, Ruff, project-local virtual environments, and
  checked-in `pyproject.toml` configuration.
- **Shell and PowerShell** for IT operations, deployment scripts, diagnostics,
  and cross-platform admin work on macOS, Ubuntu, and Windows.

## Projects

- [FileFerry](https://github.com/dunamismax/fileferry) — Rust encrypted backup
  CLI with client-side encryption, local and S3-compatible repositories,
  policy-driven retention, and scriptable restore workflows.
- [mtg-card-bot](https://github.com/dunamismax/mtg-card-bot) — Python Discord
  bot for Magic: The Gathering card lookup, built with `uv`, Ruff, pytest,
  `discord.py`, and live Scryfall data.
- [Callrift](https://github.com/dunamismax/callrift) — Username-first
  communications platform for encrypted messages, WebRTC voice, groups,
  developer servers, and technical communities, being rewritten around Rust,
  Axum, Leptos, PostgreSQL, and coturn.
- [Pod Tracker](https://github.com/dunamismax/pod-tracker) — PostgreSQL-first
  Commander playgroup OS for events, RSVPs, pod generation, deck tracking,
  game logging, and meta dashboards, being rewritten around Rust, Axum,
  Leptos, sqlx, and SSE.
- [status.dunamismax](https://github.com/dunamismax/status.dunamismax) —
  Rust status and operations dashboard for public site health, host services,
  deploy history, and project progress across my self-hosted systems.
- [Toolworks](https://github.com/dunamismax/toolworks) — Python automation,
  operational scripts, and durable CLI helpers.
- [LangIndex](https://github.com/dunamismax/langindex) — Open-source reference
  for programming languages and ecosystem tradeoffs.
- [dunamismax.com](https://github.com/dunamismax/dunamismax.com) — Personal
  site and portfolio.

## Principles

- **Rust first.** Prefer memory-safe, explicit, fast systems with small public
  APIs and measurable behavior.
- **PostgreSQL first.** Keep durable application state in one inspectable
  database until the workload proves it needs another component.
- **Python for leverage.** Automate the boring parts, prototype quickly, and
  keep scripts reproducible with `uv`, Ruff, and local project environments.
- **Security is architecture.** Cryptography, encryption, identity, key
  handling, logs, and retention shape the design from the start.
- **Self-hostable and inspectable.** The owner should be able to run it,
  recover it, audit it, and move it.
- **Boring operations.** Ubuntu, macOS, systemd, Caddy, SSH deploys,
  PostgreSQL backups, restore drills, and clear runbooks beat fragile magic.

## License

Repository content is [MIT](LICENSE) unless an individual project specifies
otherwise.
