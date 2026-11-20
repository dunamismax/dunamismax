<div align="center">

# Tech Stack

**SvelteKit 3 · Svelte 5 · TypeScript · Tailwind CSS 4 · PostgreSQL 18 + Drizzle ORM · Node · Caddy**

One web stack, used everywhere it fits. Go, Python and Swift where a project genuinely needs them.

<sub>Reviewed against project source, the production server and public HTTPS responses on <b>November 20, 2026</b>.</sub>

</div>

---

## The toolbox

| Area | Tools |
| --- | --- |
| **Web** | SvelteKit 3, Svelte 5, strict TypeScript 6, Tailwind CSS 4, Vite, adapter-node, Better Auth where accounts are needed, Astro for fully static sites |
| **Data** | PostgreSQL 18, Drizzle ORM over node-postgres with reviewed `drizzle-kit` migrations; SQLAlchemy and Alembic on the Python side |
| **Languages** | TypeScript · Go · Python · Swift · SQL · C · Bash |
| **Games & realtime** | Go game server, Protocol Buffers with Buf, WebSockets, FastAPI and uvicorn, NumPy and scikit-learn for poker AI training |
| **Apple** | Swift 6, SwiftUI, Xcode for iPhone and iPad clients that share HTTPS APIs with the web apps |
| **Python** | uv, Ruff, Pyright, pytest, discord.py, httpx |
| **Quality** | svelte-check, `tsc --noEmit`, Node's test runner and Vitest, Biome, golangci-lint, ShellCheck, isolated PostgreSQL fixtures in tests |
| **Hosting** | Ubuntu 26.04 LTS on Hyper-V, Caddy, Node 24, systemd services and timers, Docker for RustDesk |
| **Security** | Tailscale, UFW, fail2ban, key-only SSH, Lynis audits, strict CSP headers, dedicated service accounts, least-privilege database roles |
| **Recovery** | Nightly `pg_dump`, `age`-encrypted off-server snapshots, isolated restore drills for databases and application releases |
| **Workflow** | Git on `main`, GitHub with Codeberg mirrors, GitHub Actions, committed lockfiles and pinned runtimes, `BUILD.md` plans and decision records in each repo |
| **Workstation** | MacBook with Apple silicon, Ghostty, VS Code, Xcode, Homebrew, mise for runtime versions |

## Where it runs

| Project | Application & data | Delivery |
| --- | --- | --- |
| [dunamismax.com](https://dunamismax.com) | SvelteKit, Svelte 5, TypeScript, Tailwind CSS 4, PostgreSQL 18, Drizzle | Node via adapter-node behind Caddy. Prerendered pages, server-rendered blog and RSS, zero browser JavaScript |
| [Grace & Footnotes](https://graceandfootnotes.com) | SvelteKit, TypeScript, Tailwind CSS 4, PostgreSQL 18, Drizzle | Node behind Caddy, shell-only publishing on its own database role, scheduled posts, RSS |
| [vincentsawyer.org](https://vincentsawyer.org) | SvelteKit, TypeScript, Tailwind CSS 4, PostgreSQL 18, Drizzle | Node behind Caddy; a validated, checksummed content catalog |
| [Dunamis Status](https://status.dunamismax.com) | SvelteKit, TypeScript, PostgreSQL 18, Drizzle | Read-only public app; a separate TypeScript collector on a five-minute systemd timer |
| [RiverMind Poker](https://rivermindpoker.com) | Python, FastAPI, WebSockets, SQLAlchemy, Alembic, PostgreSQL; SvelteKit client | Python table server behind Caddy, built client served as static files |
| [Lorehallow](https://lorehallow.com) | Go server, Protocol Buffers; Astro website | Go binary as a systemd service; Caddy serves the static site. Website moves to SvelteKit when accounts arrive |
| [Azeroth Trail](https://azerothtrail.com) | Astro, TypeScript, Node status tracker, Web Push | Static pages from Caddy plus a small Node service |
| Imaging Services website | Astro, TypeScript, PostgreSQL 18, Drizzle; SvelteKit port approved | Hosted review demo behind Caddy and Node; not yet launched |
| [xrayservice.net](https://xrayservice.net) + RustDesk | Static Astro support site; RustDesk server and relay in Docker | Weekly verified Windows installer builds, TypeScript Cloudflare DDNS on a timer |
| [MTG Card Bot](https://github.com/dunamismax/mtg-card-bot) | Python 3.13, discord.py, httpx, Pillow, Scryfall API | `uv` with a lockfile, dedicated systemd service account |
| Field Cadence · Day by Word | SvelteKit, PostgreSQL, Drizzle; SwiftUI apps | In development, not deployed |

## How it fits together

```text
Cloudflare DNS ── DNS-only records, edited by hand, pointing at the server's public IP
      │
Caddy ── its own Let's Encrypt certificates, security headers, static files, reverse proxy
      │
      ├── Node 24 ── SvelteKit apps, each its own systemd unit and service account, loopback only
      ├── Go · Python ── game server, poker table server, Discord bot under systemd
      ├── Docker ── RustDesk server and relay
      └── PostgreSQL 18 ── loopback only; separate roles for web, publishing, collectors, migrations
```

There is no Cloudflare proxy, DNS challenge, Caddy DNS plugin or API token for Caddy. PHP-FPM and
MySQL are retired from active hosting; protected legacy material remains for recovery.

## Practices

**Application**

- Content sites are server-rendered semantic HTML. The portfolio, Grace & Footnotes, Dunamis Status,
  Lorehallow's site and the support page ship no browser JavaScript at all; Azeroth Trail's small script
  only filters and remembers, and every page reads fine without it.
- Parameterized queries through Drizzle, small connection pools, and migrations reviewed as SQL before
  they ever touch a real database, applied by a dedicated operator-only identity.
- Publishing sites read through views or roles that exclude drafts and future posts. Writers and readers
  never share credentials.
- Fonts are system fonts or self-hosted. No external CDNs, analytics or trackers.

**Deployment**

- Releases are built and tested as isolated candidates first: type checks, unit tests, a production
  build and, for the database-backed sites, a rehearsal against a disposable PostgreSQL cluster that
  covers outage and recovery.
- Releases are immutable, named by commit, and switched with an atomic `current` symlink under a shared
  deploy lock. The previous release stays ready for rollback, and public HTTPS is verified before a
  cutover counts as done.
- Shared services are never restarted for one site's release; Caddy only reloads after the full
  configuration validates.

**Operations**

- systemd runs applications, monitoring, DDNS, installer builds, disk cleanup and backups. Services run
  under dedicated identities with filesystem protections.
- RustDesk installers are checked against upstream SHA-256 digests, Authenticode signatures and pinned
  certificates before they are published.
- Backups capture every database, the exact deployed releases, configuration and service data. Restores
  are drilled in an isolated cluster; a passing timer alone is never treated as proof of recovery.
- Bash drives deployment and recovery tooling. PowerShell handles the Windows Hyper-V host's forwarding
  and firewall.

<div align="center">

**[← Back to profile](README.md)**

</div>
