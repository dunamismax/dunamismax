<div align="center">

# Stephen Sawyer

### I build the software. I run the servers.

Full-stack developer and hands-on sysadmin. Web apps in **SvelteKit**, game servers in **Go**,
poker AI in **Python**, iPhone apps in **Swift**, all running on Ubuntu infrastructure I operate myself.

[![Website](https://img.shields.io/badge/dunamismax.com-0d1117?style=for-the-badge&logo=svelte&logoColor=58a6ff)](https://dunamismax.com)
[![Portfolio](https://img.shields.io/badge/Portfolio-0d1117?style=for-the-badge&logo=bookstack&logoColor=58a6ff)](https://dunamismax.com/projects)
[![Contact](https://img.shields.io/badge/Contact-0d1117?style=for-the-badge&logo=tuta&logoColor=58a6ff)](https://dunamismax.com/contact)
[![Codeberg](https://img.shields.io/badge/Codeberg-0d1117?style=for-the-badge&logo=codeberg&logoColor=58a6ff)](https://codeberg.org/dunamismax)

![SvelteKit](https://img.shields.io/badge/SvelteKit-FF3E00?style=flat-square&logo=svelte&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL_18-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Drizzle](https://img.shields.io/badge/Drizzle-C5F74F?style=flat-square&logo=drizzle&logoColor=black)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Swift](https://img.shields.io/badge/Swift-F05138?style=flat-square&logo=swift&logoColor=white)
![Caddy](https://img.shields.io/badge/Caddy-1F88C0?style=flat-square&logo=caddy&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=flat-square&logo=ubuntu&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

</div>

---

## Right now

- **Building an MMO server.** [Lorehallow](https://lorehallow.com) is a pixel-art fantasy MMO with an
  authoritative Go server. The networking core is in progress, and an early browser prototype is open at
  [play.lorehallow.com](https://play.lorehallow.com).
- **Running a poker site.** [RiverMind Poker](https://rivermindpoker.com) deals no-limit hold'em
  against labelled bots, for play money, while a CFR training pipeline builds stronger ones.
- **Shipping on one stack.** Every web app is moving to SvelteKit 3, Svelte 5, TypeScript, Tailwind CSS 4,
  PostgreSQL 18 and Drizzle on Node, behind Caddy. Four are in production on it today.
- **Keeping eight public sites up** on a single Ubuntu server, with monitoring, encrypted backups and
  restore drills.

## Games & play

| | Project | Stack | |
| :-: | --- | --- | :-: |
| ⚔️ | **[Lorehallow](https://github.com/dunamismax/lorehallow)**<br>A small online world with zones, quests, grouping, and other people already there when you log in. One goroutine per zone, a versioned Protocol Buffers protocol, and a scale target of thousands of players that nothing claims until it's measured. [lorehallow.com](https://lorehallow.com) | Go · Protobuf · TypeScript · SvelteKit | `pre-alpha` |
| ♠️ | **[RiverMind Poker](https://github.com/dunamismax/rivermind-poker)**<br>No-limit Texas hold'em at 2 to 9 seats in the browser. A fuzz-tested engine and FastAPI table server stream hands over WebSockets to a SvelteKit client; Monte Carlo CFR trains the bots. [Play it](https://rivermindpoker.com) | Python · FastAPI · SvelteKit · PostgreSQL | `live` |
| 🗺️ | **[Azeroth Trail](https://github.com/dunamismax/azerothtrail)**<br>A WoW leveling guide that answers "what should I do at my level?" for every Paladin and Druid spec, with a build-time verifier against its sources and Web Push server-status alerts. [azerothtrail.com](https://azerothtrail.com) | Astro · TypeScript · Node · Web Push | `live` |

## Websites & publishing

| | Project | Stack | |
| :-: | --- | --- | :-: |
| 📜 | **[vincentsawyer.org](https://vincentsawyer.org)**<br>The website and permanent archive of my father's ministry: sermons, Bible studies, and pastoral training courses, with original files preserved byte-for-byte. | SvelteKit · PostgreSQL · Drizzle | `live` |
| ✒️ | **[Grace & Footnotes](https://graceandfootnotes.com)**<br>My Christian writing site, with scheduled publishing, RSS, study dates and downloads. Zero browser JavaScript. | SvelteKit · PostgreSQL · Drizzle | `live` |
| 🧭 | **[dunamismax.com](https://github.com/dunamismax/dunamismax.com)**<br>Portfolio and blog. Prerendered pages, a read-only public database role, immutable releases, and no browser JavaScript. | SvelteKit · PostgreSQL · Tailwind CSS | `live` |
| 🏥 | **[Imaging Services website](https://dunamismax.com/projects#imaging-services)**<br>A thirteen-page replacement for a company WordPress site, hosted as a review demo before launch. Private source. | Astro → SvelteKit · PostgreSQL | `demo` |

## Apps in development

| | Project | Stack | |
| :-: | --- | --- | :-: |
| 🛠️ | **[Field Cadence](https://dunamismax.com/projects#field-cadence)**<br>Field-service software for x-ray and imaging dealers: every machine by serial number, computed due dates, nightly proposed schedules, and an offline-capable technician app. Private source. | SvelteKit · Better Auth · PostgreSQL · SwiftUI | `building` |
| 📖 | **[Day by Word](https://github.com/dunamismax/daybyword)**<br>A Bible reading companion for iPhone, iPad and the web: pick a plan, see today's reading, keep an honest record, and get a welcoming way back after missed days. | Swift · SwiftUI · SvelteKit · PostgreSQL | `building` |

## Infrastructure & tools

| | Project | Stack | |
| :-: | --- | --- | :-: |
| 🖥️ | **[Company remote support](https://xrayservice.net)**<br>Self-hosted RustDesk server and relay for my whole company, with a support site that hands customers a preconfigured Windows client, built weekly and verified against upstream digests and Authenticode signatures. | RustDesk · Docker · Astro · Caddy | `in service` |
| 📈 | **[Dunamis Status](https://status.dunamismax.com)**<br>Operations dashboard for site health, services, backups, incidents, deployments and repository status. A five-minute collector writes; the public app only reads. [Source](https://github.com/dunamismax/status.dunamismax) | SvelteKit · PostgreSQL · systemd | `live` |
| 🔐 | **[Backup & recovery](https://dunamismax.com/projects#backups)**<br>Nightly database and configuration backups, age-encrypted and kept off the server, with restore drills in an isolated PostgreSQL cluster. | Bash · PostgreSQL · age | `scheduled` |
| 🃏 | **[MTG Card Bot](https://github.com/dunamismax/mtg-card-bot)**<br>Discord bot for Magic: The Gathering card lookups, prices, legality and rulings through Scryfall, with typo-tolerant matching and slash-command autocomplete. | Python · discord.py · httpx | `in service` |
| 📘 | **[C From The Ground Up](https://github.com/dunamismax/c-from-the-ground-up)**<br>A progressive C workbook from Hello World to sockets, threads and an ncurses text adventure. [Read it online](https://dunamismax.github.io/c-from-the-ground-up/) | C · POSIX · ncurses · mdBook | `published` |

## One server, everything on it

```text
Cloudflare DNS ── DNS-only records, no proxy
  │
  ▼
Caddy ── HTTPS via Let's Encrypt, security headers, static files
  │
  ├── SvelteKit apps on Node 24 ──▶ PostgreSQL 18, one least-privilege role per job
  ├── static Astro sites ── Azeroth Trail, the support site
  ├── Go game server · FastAPI poker server · Discord bot
  └── RustDesk server + relay in Docker

systemd timers ── monitoring · DDNS · installer builds · nightly age-encrypted backups
Ubuntu 26.04 LTS on Hyper-V · Tailscale · UFW · fail2ban · key-only SSH
```

## How I work

- **One stack, used deliberately.** SvelteKit, TypeScript and PostgreSQL for the web. Go, Python or Swift
  only when the project actually needs a game server, a model or a native app.
- **Pages that work without JavaScript.** Server-rendered, semantic HTML first; scripts only where a
  feature needs them.
- **Least privilege by default.** Separate service accounts and database roles for readers, publishers,
  collectors and migrations. Secrets never live in a repository or a build.
- **Releases you can roll back.** Immutable commit-named releases, atomic symlink switches, a shared deploy
  lock, and a rollback check before anything is called done.
- **Plans in writing.** Each project keeps its build plan and decision records next to the code, and says
  exactly what is finished and what is not.

<div align="center">

**[Full tech stack →](TECH_STACK.md)**

<sub>Code on <a href="https://github.com/dunamismax">GitHub</a>, mirrored to <a href="https://codeberg.org/dunamismax">Codeberg</a> · <a href="https://dunamismax.com/feed.xml">RSS</a></sub>

</div>
