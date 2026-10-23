# Tech Stack

My current websites use **Astro, strict TypeScript, and PostgreSQL**, served
through **Caddy on Ubuntu**. Python powers the Discord bot, Docker packages
RustDesk, and systemd runs services and scheduled jobs. Each project uses
the runtime that fits its job.

Reviewed against project source and active deployments on **October 23, 2026**.

## Where the tools run

| Project | Application and data | Delivery and operations |
| --- | --- | --- |
| [dunamismax.com](https://dunamismax.com) | Astro, TypeScript, PostgreSQL, semantic HTML, hand-written CSS | Prerendered pages and server-rendered publishing through Caddy and Node; no browser JavaScript |
| [Dunamis Status](https://status.dunamismax.com) | Astro, TypeScript, PostgreSQL | Read-only public Node application; separate TypeScript collector on a systemd timer; no browser JavaScript |
| [Grace & Footnotes](https://graceandfootnotes.com) | Astro, TypeScript, PostgreSQL, HTML, CSS | Caddy and Node, CLI publishing, scheduled posts, RSS, and a local theme script |
| Imaging Services replacement | Astro, TypeScript, PostgreSQL, HTML, CSS, self-hosted Inter, and a local theme script | Hosted demo through Caddy and Node; the company's main website has not been cut over |
| [xrayservice.net](https://xrayservice.net) and RustDesk | Static Astro support site; third-party RustDesk server and relay in Docker | Caddy serves built files; scheduled installer verification, TypeScript Cloudflare DDNS, and systemd timers |
| [MTG Card Bot](https://github.com/dunamismax/mtg-card-bot) | Python 3.13, `discord.py`, `httpx`, Pillow, and the Scryfall API | `uv` and `uv.lock`; a dedicated systemd service account on Ubuntu |
| Server backup and recovery | Bash, PostgreSQL dumps, application/configuration archives, and `age` encryption | Scheduled off-site snapshots, integrity checks, isolated database restore verification, and rebuild procedures |

The hosted services share an **Ubuntu 26.04 LTS VM on Hyper-V**. Cloudflare
provides DNS. Caddy serves static output or proxies to application-specific
Node services; Node and PostgreSQL listen on loopback. The support landing
page needs no running Node application or database to serve visitors.

The website toolchain currently uses Astro 7, TypeScript 6, Node 24, and
PostgreSQL 18. Repositories pin exact application runtime and dependency
versions. PHP-FPM and MySQL have been retired from active hosting; protected
legacy material remains available for recovery.

## Application and data practices

- Astro handles static generation and server rendering. Strict TypeScript
  covers application code, publishing tools, monitoring, and DNS automation.
- PostgreSQL access uses `pg`, parameterized queries, small connection pools,
  and explicit SQL schemas or migrations.
- Web readers, publishers, collectors, and migration operators use separate
  database roles. Publishing views exclude private drafts and future posts
  until their publication time.
- Node projects use exact dependency pins, committed npm lockfiles, and
  `npm ci`. Astro checks, TypeScript checks, project tests, and production
  builds verify changes; database integration tests use isolated fixtures.
- The bot keeps its Python workflow: `uv`, Ruff, Pyright, and pytest.
  Deployment scripts use shell syntax checks and ShellCheck where applicable.

## Front end

- Semantic HTML and responsive, hand-written CSS keep pages accessible and
  readable without a browser framework.
- Astro builds the websites, but a build step does not require shipping
  JavaScript to the browser. The portfolio, status site, and support landing
  page send none. Grace & Footnotes and the Imaging Services demo use small
  local theme scripts; reading remains usable without JavaScript.
- Most sites use system fonts; the Imaging Services demo serves Inter
  locally. Fonts do not depend on an external service.

## Operations and recovery

- Caddy handles HTTPS, static files, and reverse proxying. Docker runs
  RustDesk; systemd manages application services, monitoring, DDNS, installer
  verification, and backup schedules.
- Tailscale, key-only SSH, UFW, and fail2ban support server access controls.
  Dedicated service identities and systemd filesystem protections limit
  application access. Secrets stay outside repositories and public assets.
- Website deployments use immutable commit-based releases, atomic `current`
  symlinks, a shared deployment lock, verification checks, and documented
  rollback procedures. Publishing and deployment remain separate operations.
- RustDesk installers are checked against upstream digests and Windows
  signatures. The TypeScript DDNS job manages an explicit record allowlist
  and supports dry runs.
- Daily backups capture databases, active application releases, configuration,
  and service data. Sensitive off-site snapshots are encrypted with `age`.
  The host backup verifies PostgreSQL dumps by restoring them into an
  isolated cluster. Database restore verification and a complete replacement
  server rehearsal are distinct checks.
- Bash handles server deployment and recovery tooling. PowerShell manages
  the Windows Hyper-V host's forwarding and firewall configuration.

[Back to profile](README.md)
