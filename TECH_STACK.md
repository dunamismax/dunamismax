# Tech Stack

This is the stack behind my current projects, reviewed against their source
repositories and deployed services on 2026-10-17. PHP and MySQL are central to
my websites, but the support site, remote-support service, and Discord bot use
different tools for different jobs.

## Where the tools run

| Project | Application and data | Delivery and operations |
| --- | --- | --- |
| dunamismax.com | Bespoke PHP 8.5, MySQL 8.4, semantic HTML, hand-written CSS | Caddy and a dedicated PHP-FPM pool; no JavaScript |
| Dunamis Status | Bespoke PHP 8.5 and MySQL 8.4 | Caddy and PHP-FPM for the read-only website; a separate PHP CLI collector runs on a systemd timer |
| Grace & Footnotes | Bespoke PHP 8.5, MySQL 8.4, HTML, CSS, and one local theme script | Caddy, PHP-FPM, CLI publishing, and RSS |
| Imaging Services replacement | Bespoke PHP 8.5, MySQL 8.4, HTML, CSS, a self-hosted Inter font, and one local theme script | Caddy and PHP-FPM on a hosted demo; the main domain still serves the existing site |
| xrayservice.net and RustDesk | Static HTML/CSS support page; third-party RustDesk server and relay in Docker | Caddy, scheduled Windows installer builds with digest and signature checks, PHP CLI Cloudflare DNS updates, and systemd timers |
| MTG Card Bot | Python 3.13, `discord.py`, `httpx`, and the Scryfall API | `uv` for dependencies and a systemd service on Ubuntu |
| Server backup and recovery | Shell scripts, MySQL dumps, and `age` encryption | Scheduled snapshots, integrity checks, and documented restore steps |

The hosted services share an Ubuntu 26.04 LTS VM. Cloudflare provides DNS;
Caddy serves the websites and sends PHP requests to site-specific PHP-FPM
pools. MySQL runs locally for the PHP applications that need persistent data.
The static support page needs neither PHP-FPM nor MySQL to serve a visitor.

## Application and data practices

- The PHP websites use small, bespoke applications with server-rendered HTML,
  PDO prepared statements, explicit database schemas or migrations, and no
  framework, ORM, Composer dependency, or frontend build step.
- The portfolio and Grace & Footnotes publish through protected CLI tools.
  Their public database accounts can only read. Dunamis Status similarly
  separates its scheduled writer from the read-only public website.
- The Imaging Services replacement is a hosted demo under review. Its
  database-backed application does not imply that the company's main site
  has been cut over.
- The MTG Card Bot is a Python project with its own dependencies and quality
  checks: `uv`, Ruff, Pyright, and pytest. The Cloudflare DNS updater and the
  status collector are PHP CLI jobs, not Python services.
- The PHP repositories use `php -l` and project-specific tests. Deployment
  scripts are checked with shell syntax tools and ShellCheck where applicable.

## Front end

- The PHP sites render semantic HTML on the server; the support landing page
  is static HTML. All use responsive, hand-written CSS. The portfolio, status
  site, and support landing page send no JavaScript.
- Grace & Footnotes and the Imaging Services demo each send one small, local
  script for a light/dark theme choice. Their content remains usable without
  JavaScript.
- Most sites use system fonts; the Imaging Services demo serves Inter locally.
  None of these sites needs an external font service or frontend asset build.

## Operations and recovery

- I use Caddy for HTTPS and static files, dedicated PHP-FPM pools for the PHP
  sites, Docker for RustDesk, and systemd services and timers for the bot,
  monitoring, DNS updates, installer builds, and backups.
- Server access uses Tailscale, key-only SSH, UFW, and fail2ban. Cloudflare
  DNS is maintained by a scheduled PHP updater with an explicit allowlist.
- Application secrets stay outside web roots and source repositories.
  Site-specific service identities and database grants keep public reading
  separate from publishing, collection, and host administration.
- Website releases use versioned directories and a `current` symlink, with
  deployment checks and a documented rollback path. Git pushes alone do not
  deploy the PHP sites.
- Backup jobs capture databases, configuration, and service data. The host
  backup encrypts sensitive material with `age`; restore procedures and
  verification commands are documented. A successful backup job or checksum
  is not, by itself, proof of a complete server recovery.
- Bash handles deployment and server automation. PowerShell maintains the
  Windows host networking used by the remote-support service.
