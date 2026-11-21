<div align="center">

# Tech Stack

**SvelteKit 3 · Svelte 5 · TypeScript · Tailwind CSS 4 · PostgreSQL 18 + Drizzle ORM · Node 26 · pnpm · Caddy**

One web stack, used everywhere it fits. Go, Python and Swift where a project genuinely needs them.

<sub>Reviewed against project source, the production server and public HTTPS responses on <b>November 21, 2026</b>.</sub>

</div>

---

## The toolbox

| Area | Tools |
| --- | --- |
| **Web** | SvelteKit 3, Svelte 5, strict TypeScript 6, Tailwind CSS 4, Vite, adapter-node, Better Auth where accounts are needed |
| **Data** | PostgreSQL 18, Drizzle ORM over node-postgres (`pg`) with reviewed `drizzle-kit` migrations |
| **Languages** | TypeScript · Go · Python · Swift · SQL · C · Bash |
| **Games & realtime** | Go game server, Protocol Buffers with Buf, WebSockets, a TypeScript poker engine and table server checked against their Python originals, NumPy and scikit-learn for poker AI training |
| **Apple** | Swift 6, SwiftUI, Xcode for iPhone and iPad clients that share HTTPS APIs with the web apps |
| **Python** | uv, Ruff, Pyright, pytest, discord.py, httpx |
| **Quality** | svelte-check, `tsc --noEmit`, Node's test runner and Vitest, Playwright with axe-core, ESLint, Biome, golangci-lint, ShellCheck, isolated PostgreSQL fixtures in tests |
| **Hosting** | Ubuntu 26.04 LTS on Hyper-V, a custom Caddy build with rate limiting, Node 26, systemd services and timers, Docker for RustDesk only |
| **Security** | Tailscale, UFW, fail2ban, SSH over the tailnet only with passwords off, Lynis audits, strict CSP headers, sandboxed systemd units under dedicated service accounts, least-privilege database roles |
| **Recovery** | Daily `pg_dump` of every database, `age`-encrypted snapshots kept off the server, restic for large media, isolated restore drills for databases and application releases |
| **Workflow** | Git on `main`, GitHub with Codeberg mirrors, GitHub Actions, pnpm with committed lockfiles, one exact Node, pnpm and dependency version across every repository, `BUILD.md` plans and decision records in each repo |
| **Workstation** | MacBook with Apple silicon, Ghostty, VS Code, Xcode, Homebrew, mise for runtime versions |

## Where it runs

| Project | Application & data | Delivery |
| --- | --- | --- |
| [dunamismax.com](https://dunamismax.com) | SvelteKit, Svelte 5, TypeScript, Tailwind CSS 4, PostgreSQL 18, Drizzle | Node via adapter-node behind Caddy. Prerendered pages, server-rendered blog and RSS, zero browser JavaScript |
| [Grace & Footnotes](https://graceandfootnotes.com) | SvelteKit, TypeScript, Tailwind CSS 4, PostgreSQL 18, Drizzle | Node behind Caddy, shell-only publishing on its own database role, scheduled posts, RSS; one small theme script |
| [vincentsawyer.org](https://vincentsawyer.org) | SvelteKit, TypeScript, Tailwind CSS 4, PostgreSQL 18, Drizzle | Node behind Caddy; a validated, checksummed content catalog; sermon media backed up off-site on its own schedule |
| [Dunamis Status](https://status.dunamismax.com) | SvelteKit, TypeScript, Tailwind CSS 4, PostgreSQL 18, Drizzle | Read-only public app; a separate TypeScript collector on a five-minute systemd timer |
| [RiverMind Poker](https://rivermindpoker.com) | SvelteKit, TypeScript, Tailwind CSS 4, PostgreSQL 18, Drizzle; a TypeScript engine, bots and table server over WebSockets; Python with NumPy and scikit-learn for offline CFR training | One Node service behind Caddy serves the pages, the API and the tables; open tables are kept in PostgreSQL and survive a restart |
| [Lorehallow](https://lorehallow.com) | Go server, Protocol Buffers; script-free SvelteKit website; Phaser browser client | Go binary as a systemd service; SvelteKit on Node behind Caddy; Caddy serves the client build at play.lorehallow.com |
| [Azeroth Trail](https://azerothtrail.com) | SvelteKit, TypeScript, Tailwind CSS 4; PostgreSQL 18 and Drizzle for the server-status tracker; Web Push | Prerendered pages from Caddy; Node via adapter-node for the tracker API |
| [C From The Ground Up](https://cfromthegroundup.com) | 38 C lessons that compile as C17 and C23; SvelteKit course site with PostgreSQL 18, Drizzle and Better Auth for optional accounts | Node behind Caddy, lesson pages prerendered from the lesson sources; an mdBook mirror on GitHub Pages |
| Imaging Services website | SvelteKit, TypeScript, Tailwind CSS 4, PostgreSQL 18, Drizzle | Hosted review demo on Node behind Caddy, kept out of search engines; not yet launched |
| [xrayservice.net](https://xrayservice.net) + RustDesk | Prerendered SvelteKit support page with no database; RustDesk server and relay in Docker | Node behind Caddy; weekly verified Windows installer builds, TypeScript Cloudflare DDNS on a five-minute timer |
| Field Cadence | SvelteKit, TypeScript, Tailwind CSS 4, PostgreSQL 18, Drizzle, Better Auth; a SwiftUI iPhone app on the same API | Development preview at fieldcadence.app on Node behind Caddy, kept out of search engines; not open to customers |
| [Day by Word](https://github.com/dunamismax/daybyword) | Swift and SwiftUI app for iPhone and iPad; SvelteKit, PostgreSQL 18 and Drizzle for the web version | Development preview at daybyword.com on Node behind Caddy, kept out of search engines; the app is not yet released |
| [MTG Card Bot](https://github.com/dunamismax/mtg-card-bot) | Python 3.13, discord.py, httpx, Pillow, Scryfall API | `uv` with a lockfile, immutable releases, a sandboxed systemd service under its own account |
| Backup & recovery | Bash and Python tooling, `age`, restic, PostgreSQL | systemd timers; every daily run ends with a restore drill before it publishes the snapshot |

## How it fits together

```text
Cloudflare DNS ── DNS-only records, edited by hand, pointing at the server's public IP
      │
Caddy ── its own Let's Encrypt certificates, security headers, rate limits, static files, reverse proxy
      │
      ├── Node 26 ── SvelteKit apps, each its own systemd unit and service account, loopback only
      ├── Go · Python ── game server and Discord bot under systemd
      ├── Docker ── RustDesk server and relay
      └── PostgreSQL 18 ── loopback only; separate roles for web, publishing, collectors, migrations
```

There is no Cloudflare proxy, DNS challenge, Caddy DNS plugin or API token for Caddy. Caddy is a custom
build with one plugin, for rate limiting, rebuilt from pinned versions and checked daily against
upstream releases. No website runs in a container. PHP-FPM and MySQL are retired from active hosting;
protected legacy material remains for recovery.

## Practices

**Application**

- Content sites are server-rendered semantic HTML. The portfolio, Dunamis Status, Lorehallow's site and
  the support page ship no browser JavaScript at all. Grace & Footnotes ships one small theme script and
  Azeroth Trail a few that filter, remember and handle alerts; every page on both reads fine without them.
- Parameterized queries through Drizzle, small connection pools, and migrations reviewed as SQL before
  they ever touch a real database, applied by a dedicated operator-only identity.
- Publishing sites read through views or roles that exclude drafts and future posts. Writers and readers
  never share credentials.
- Fonts are system fonts or self-hosted. No external CDNs and no third-party trackers. The one
  analytics tool is a self-hosted, cookieless Umami for the C course site, installed and not yet
  switched on.

**Deployment**

- One written platform contract covers every web project: pnpm, one Node version, exact dependency
  pins shared across repositories, the host's PostgreSQL cluster, and a conformance script that each
  repository must pass.
- Releases are built and tested outside the shared deploy lock first: type checks, lint, unit tests, a
  production build and, where the site has one, a rehearsal against a disposable PostgreSQL cluster
  that covers outage and recovery.
- Releases are immutable and switched with an atomic `current` symlink under the deploy lock. Before
  the switch each release runs as a candidate on a spare port, from its final directory, as the
  service account, under the new unit file and against the real database, and public HTTPS is verified
  before a cutover counts as done.
- There is no rollback. Migrations are additive so the release that is still serving keeps working,
  and a release that misbehaves is fixed in a new commit and deployed forward.
- Shared services are never restarted for one site's release; Caddy only reloads after the full
  configuration validates.

**Operations**

- systemd runs applications, monitoring, DDNS, installer builds, disk cleanup and backups. Services run
  under dedicated identities with filesystem protections.
- RustDesk installers are checked against upstream SHA-256 digests, Authenticode signatures and pinned
  certificates before they are published.
- Backups capture every database, the exact deployed releases, configuration and service data; large
  media goes to a separate encrypted off-site repository. Restores are drilled in an isolated cluster,
  with the recovered sites booted against it; a passing timer alone is never treated as proof of
  recovery.
- Bash drives deployment and recovery tooling. PowerShell handles the Windows Hyper-V host's forwarding
  and firewall.

<div align="center">

**[← Back to profile](README.md)**

</div>
