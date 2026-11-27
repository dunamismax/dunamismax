<div align="center">

# Stephen Sawyer

### I build the software. I run the servers.

Full-stack developer and hands-on sysadmin. Web apps in **SvelteKit**, poker AI in **Python**,
iPhone apps in **Swift**, all running on Ubuntu infrastructure I operate myself.

[![Website](https://img.shields.io/badge/dunamismax.com-0d1117?style=for-the-badge&logo=svelte&logoColor=58a6ff)](https://dunamismax.com)
[![Portfolio](https://img.shields.io/badge/Portfolio-0d1117?style=for-the-badge&logo=bookstack&logoColor=58a6ff)](https://dunamismax.com/projects)
[![Contact](https://img.shields.io/badge/Contact-0d1117?style=for-the-badge&logo=tuta&logoColor=58a6ff)](https://dunamismax.com/contact)
[![Codeberg](https://img.shields.io/badge/Codeberg-0d1117?style=for-the-badge&logo=codeberg&logoColor=58a6ff)](https://codeberg.org/dunamismax)

![SvelteKit](https://img.shields.io/badge/SvelteKit-FF3E00?style=flat-square&logo=svelte&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL_18-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Drizzle](https://img.shields.io/badge/Drizzle-C5F74F?style=flat-square&logo=drizzle&logoColor=black)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)
![pnpm](https://img.shields.io/badge/pnpm-F69220?style=flat-square&logo=pnpm&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Swift](https://img.shields.io/badge/Swift-F05138?style=flat-square&logo=swift&logoColor=white)
![Caddy](https://img.shields.io/badge/Caddy-1F88C0?style=flat-square&logo=caddy&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=flat-square&logo=ubuntu&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

</div>

---

## Right now

- **Running a poker site.** [RiverMind Poker](https://rivermindpoker.com) deals no-limit hold'em
  against labelled bots, for play money, while a CFR training pipeline builds stronger ones.
- **Shipping on one stack.** Every deployed web app runs on SvelteKit 3, Svelte 5, TypeScript and
  Tailwind CSS 4 on Node 26, behind Caddy, with PostgreSQL 18 and Drizzle wherever there is data to
  keep. Every repository pins the same exact Node, pnpm and dependency versions.
- **Keeping twelve sites up** on a single Ubuntu server, with monitoring, encrypted backups and
  restore drills.

## Games & play

| | Project | Stack | |
| :-: | --- | --- | :-: |
| ♠️ | **[RiverMind Poker](https://github.com/dunamismax/rivermind-poker)**<br>No-limit Texas hold'em at 2 to 9 seats in the browser. A fuzz-tested engine, the bots and the table server are TypeScript inside one SvelteKit service, streaming hands over WebSockets; Monte Carlo CFR in Python trains the bots. [Play it](https://rivermindpoker.com) | SvelteKit · TypeScript · PostgreSQL · Python | `live` |

## Websites & publishing

| | Project | Stack | |
| :-: | --- | --- | :-: |
| 📜 | **[vincentsawyer.org](https://vincentsawyer.org)**<br>The website and permanent archive of my father's ministry: sermons, Bible studies, and pastoral training courses, with original files preserved byte-for-byte. | SvelteKit · PostgreSQL · Drizzle | `live` |
| ✒️ | **[Grace & Footnotes](https://graceandfootnotes.com)**<br>My Christian writing site, with scheduled publishing, RSS, study dates and downloads. Every page reads fully without JavaScript. | SvelteKit · PostgreSQL · Drizzle | `live` |
| 🧭 | **[dunamismax.com](https://github.com/dunamismax/dunamismax.com)**<br>Portfolio and blog. Prerendered pages, a read-only public database role, immutable releases, and no browser JavaScript. | SvelteKit · PostgreSQL · Tailwind CSS | `live` |
| 🏥 | **[Imaging Services website](https://dunamismax.com/projects#imaging-services)**<br>A thirteen-page replacement for a company WordPress site, hosted as a review demo before launch. Private source. | SvelteKit · PostgreSQL · Drizzle | `demo` |

## Apps in development

Both run on their own domains as development previews, kept out of search engines until they are ready.

| | Project | Stack | |
| :-: | --- | --- | :-: |
| 🛠️ | **[Field Cadence](https://dunamismax.com/projects#field-cadence)**<br>Field-service software for x-ray and imaging dealers: every machine by serial number, computed due dates, nightly proposed schedules, and an offline-capable technician app. Private source. | SvelteKit · Better Auth · PostgreSQL · SwiftUI | `preview` |
| 📖 | **[Day by Word](https://github.com/dunamismax/daybyword)**<br>A Bible reading companion for iPhone, iPad and the web: pick a plan, see today's reading, keep an honest record, and get a welcoming way back after missed days. | Swift · SwiftUI · SvelteKit · PostgreSQL | `preview` |

## Infrastructure & tools

| | Project | Stack | |
| :-: | --- | --- | :-: |
| 🖥️ | **[Company remote support](https://xrayservice.net)**<br>Self-hosted RustDesk server and relay for my whole company, with a support site that hands customers a preconfigured Windows client, built weekly and verified against upstream digests and Authenticode signatures. | RustDesk · Docker · SvelteKit · Caddy | `in service` |
| 📈 | **[Dunamis Status](https://status.dunamismax.com)**<br>Operations dashboard for site health, services, backups, incidents, deployments and repository status. A five-minute collector writes; the public app only reads. [Source](https://github.com/dunamismax/status.dunamismax) | SvelteKit · PostgreSQL · systemd | `live` |
| 🔐 | **[Backup & recovery](https://dunamismax.com/projects#backups)**<br>Daily age-encrypted snapshots of every database, each site's exact release and the server's configuration, kept off the server, plus an encrypted off-site copy of the large media. Every run restores the databases into an isolated cluster and boots the recovered sites against them. | Bash · Python · PostgreSQL · age · restic | `scheduled` |
| 🌐 | **[Dynamic DNS automation](https://dunamismax.com/projects#dns-automation)**<br>A TypeScript updater on a five-minute timer keeps selected Cloudflare DNS records pointed at the server's public address, with drift checks and a dry-run mode. | TypeScript · Node · systemd | `scheduled` |
| 🃏 | **[MTG Card Bot](https://github.com/dunamismax/mtg-card-bot)**<br>Discord bot for Magic: The Gathering card lookups, prices, legality and rulings through Scryfall, with typo-tolerant matching and slash-command autocomplete. | Python · discord.py · httpx | `in service` |
| 📘 | **[C From The Ground Up](https://github.com/dunamismax/c-from-the-ground-up)**<br>A free, progressive C course: 38 runnable lessons from Hello World to sockets, threads and an ncurses text adventure, then debugging, undefined behavior and testing. [cfromthegroundup.com](https://cfromthegroundup.com) | C · POSIX · ncurses · SvelteKit | `published` |

## One server, everything on it

```text
Cloudflare DNS ── DNS-only records, no proxy
  │
  ▼
Caddy ── HTTPS via Let's Encrypt, security headers, rate limits, static files
  │
  ├── SvelteKit apps on Node 26, one systemd unit each ──▶ PostgreSQL 18, one least-privilege role per job
  ├── Python Discord bot
  └── RustDesk server + relay in Docker

systemd timers ── monitoring · DDNS · installer builds · daily age-encrypted backups
Ubuntu 26.04 LTS on Hyper-V · Tailscale · UFW · fail2ban · SSH over the tailnet only
```

## How I work

- **One stack, used deliberately.** SvelteKit, TypeScript and PostgreSQL for the web. Python or Swift
  only when the project actually needs a model, a bot or a native app.
- **Pages that work without JavaScript.** Server-rendered, semantic HTML first; scripts only where a
  feature needs them.
- **Least privilege by default.** Separate service accounts and database roles for readers, publishers,
  collectors and migrations. Secrets never live in a repository or a build.
- **Releases that only move forward.** Immutable releases, atomic symlink switches and a shared deploy
  lock. Each release first runs as a candidate against the real database, under the service's own
  account and sandbox, and takes traffic only if it passes. There is no rollback: a bad release is
  fixed in a new commit.
- **One written standard.** Every web project follows the same platform contract: pnpm, one Node
  version, exact dependency pins, the host's PostgreSQL. A conformance check is the definition of done.
- **Plans in writing.** Each project keeps its build plan and decision records next to the code, and says
  exactly what is finished and what is not.

<div align="center">

**[Full tech stack →](TECH_STACK.md)**

<sub>Code on <a href="https://github.com/dunamismax">GitHub</a>, mirrored to <a href="https://codeberg.org/dunamismax">Codeberg</a> · <a href="https://dunamismax.com/feed.xml">RSS</a></sub>

</div>
