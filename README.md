# Stephen Sawyer

Rust-first engineer and IT operator building self-hostable systems that are
fast, inspectable, and boring to run.

- Website: [dunamismax.com](https://dunamismax.com)
- GitHub: [@dunamismax](https://github.com/dunamismax)
- Codeberg: [@dunamismax](https://codeberg.org/dunamismax)

## Focus

I work on performance-sensitive software, self-hostable product systems,
crypto infrastructure, secure networking, local-first tools, and automation for
real operations. My current primary product focus is LoveWard, a private,
safety-aware meditation, journaling, and daily practice PWA.

Current default stack:

- **Rust** for production systems, CLIs, network services, protocol work, and
  performance-critical paths.
- **Next.js, React, TypeScript, Tailwind CSS, shadcn/ui, and Radix** for
  web-native product interfaces when the product needs a mature PWA and app
  router surface.
- **PostgreSQL** for durable state, audit trails, queues, analytics, search,
  and reporting.
- **Drizzle, Better Auth, pgvector, Dexie, Stripe, Docker Compose, Caddy, and
  OpenAI-backed provider abstractions** for portable, private-by-default
  application backends.
- **Leptos, Axum, Tokio, and SQLx** for Rust web apps and operator surfaces.
- **Python** for automation, scripts, prototypes, bots, data work, and glue,
  managed with `uv`, Ruff, pytest, and checked-in `pyproject.toml` config.
- **Shell and PowerShell** for deployment, diagnostics, and cross-platform IT
  operations across macOS, Ubuntu, and Windows.

## Projects

- [LoveWard](https://github.com/dunamismax/loveward) — Self-hostable Next.js
  PWA for meditation, self-inquiry, private journaling, daily practice, and a
  safety-aware AI reflection guide.
- [FileFerry](https://github.com/dunamismax/fileferry) — Rust encrypted backup
  CLI with client-side encryption, local and S3-compatible repositories, and
  scriptable restores.
- [Callrift](https://github.com/dunamismax/callrift) — Username-first
  communications platform for encrypted messages, WebRTC voice, groups, and
  technical communities.
- [Pod Tracker](https://github.com/dunamismax/pod-tracker) — PostgreSQL-first
  Commander playgroup OS for events, RSVPs, pod generation, deck tracking, and
  meta dashboards.
- [status.dunamismax](https://github.com/dunamismax/status.dunamismax) — Rust
  status and operations dashboard for public site health, host services,
  deploy history, and project progress.
- [mtg-card-bot](https://github.com/dunamismax/mtg-card-bot) — Python Discord
  bot for Magic: The Gathering card lookup using live Scryfall data.
- [Toolworks](https://github.com/dunamismax/toolworks) — Python automation,
  operational scripts, and durable CLI helpers.
- [LangIndex](https://github.com/dunamismax/langindex) — Open-source reference
  for programming languages and ecosystem tradeoffs.
- [dunamismax.com](https://github.com/dunamismax/dunamismax.com) — Personal
  site and portfolio.

## Principles

- Rust first for systems work.
- PostgreSQL first for durable application state.
- Python where speed of iteration matters.
- Security, key handling, logs, retention, backups, and restores are part of
  the architecture.
- The owner should be able to run it, audit it, recover it, and move it.

## License

Repository content is [MIT](LICENSE) unless an individual project specifies
otherwise.
