# Repository Index

> Complete index of Stephen Sawyer's (`dunamismax`) repositories, their purpose, stack, and source control strategy.
> All repos live under `/home/sawyer/github/` and are mirrored across GitHub and Codeberg.
> Last updated: 2026-02-16.

---

## Source Control Strategy

### Dual-Remote Mirroring (GitHub + Codeberg)

Every repository uses a single `origin` remote with dual push URLs:

```
origin  git@github.com:dunamismax/<repo>.git   (fetch)
origin  git@github.com:dunamismax/<repo>.git   (push)
origin  git@codeberg.org:dunamismax/<repo>.git  (push)
```

One `git push` publishes to both hosts. This is an intentional resilience pattern — platform risk is not existential when source control is redundant across providers.

**Rules:**

- All remotes use **SSH**, never HTTPS.
- Fetch comes from GitHub. Push goes to both GitHub and Codeberg.
- New repos get dual push URLs wired immediately after clone or init.
- Force push to a secondary mirror is only allowed for initial bootstrap, with explicit approval.
- SSH host config and dedicated identities are maintained in `~/.ssh/config` for both providers.

### Why

- **Sovereignty**: If GitHub goes down or changes policy, Codeberg has the full history.
- **Simplicity**: No sync scripts, no cron jobs. The git push URL list handles it natively.
- **Zero friction**: The workflow is identical to single-remote — `git push` just does more.

---

## Repositories

### scryai

| | |
|---|---|
| **Path** | `scryai` |
| **Type** | Monorepo — infrastructure, apps, and agent operating docs |
| **Stack** | TypeScript, Qwik + Qwik City, Bun, Vite, Tailwind CSS v4, PostgreSQL (pgvector, pgcrypto), postgres.js, Better Auth, pg-boss, MinIO, Caddy |
| **GitHub** | [dunamismax/scryai](https://github.com/dunamismax/scryai) |
| **Codeberg** | [dunamismax/scryai](https://codeberg.org/dunamismax/scryai) |

Canonical root repo for **scry** (AI engineering partner). Contains shared infrastructure (Docker Compose with PostgreSQL, MinIO, Caddy), monorepo apps under `apps/`, root automation scripts, and the identity/operations contracts (`SOUL.md`, `AGENTS.md`). Current app: `bedrock-web` (full-stack template, migrating from React Router to Qwik).

---

### TALLstack

| | |
|---|---|
| **Path** | `TALLstack` |
| **Type** | Application template |
| **Stack** | PHP 8.2+, Laravel 12, Livewire 4, Fortify, Flux UI, Tailwind CSS 4, Spatie Permission, Pest 4 |
| **GitHub** | [dunamismax/TALLstack](https://github.com/dunamismax/TALLstack) |
| **Codeberg** | [dunamismax/TALLstack](https://codeberg.org/dunamismax/TALLstack) |

Production-ready Laravel + Livewire admin dashboard template. Fortify-backed auth with 2FA, password reset, and email verification. Spatie RBAC with role/permission management. Versioned admin API (`/api/v1/admin`) with session authentication. Monitoring via Laravel Telescope, Pulse, and Pail. Larastan static analysis.

---

### poddashboard

| | |
|---|---|
| **Path** | `poddashboard` |
| **Type** | Application |
| **Stack** | PHP 8.2+, Laravel 12, Livewire 4, Fortify, Flux UI, Spatie Permission, Pest |
| **GitHub** | [dunamismax/poddashboard](https://github.com/dunamismax/poddashboard) |
| **Codeberg** | [dunamismax/poddashboard](https://codeberg.org/dunamismax/poddashboard) |

Lean pod/event management app with passwordless OTP sign-in and session-authenticated API endpoints. Telescope and Pulse monitoring. PHPStan static analysis.

---

### mylife-rpg

| | |
|---|---|
| **Path** | `mylife-rpg` |
| **Type** | Application |
| **Stack** | PHP 8.2+, Laravel 12, Livewire 4, Fortify, Flux UI, Spatie Permission, Pest |
| **GitHub** | [dunamismax/mylife-rpg](https://github.com/dunamismax/mylife-rpg) |
| **Codeberg** | [dunamismax/mylife-rpg](https://codeberg.org/dunamismax/mylife-rpg) |

Gamified productivity engine. Quests, habits, XP/leveling, achievements, and stat progression. Fortify authentication with RBAC. Telescope and Pulse monitoring.

---

### codex-web

| | |
|---|---|
| **Path** | `codex-web` |
| **Type** | Application |
| **Stack** | PHP 8.2+, Laravel, Livewire, Flux UI, Tailwind CSS v4 |
| **GitHub** | [dunamismax/codex-web](https://github.com/dunamismax/codex-web) |
| **Codeberg** | [dunamismax/codex-web](https://codeberg.org/dunamismax/codex-web) |

Browser console for Codex CLI sessions. Real-time streaming chat via `wire:stream` and SSE. Session continuation with thread IDs. Configurable runtime controls (model, reasoning, sandbox, approval policy). Server-side workspace path boundary validation.

---

### BereanAI

| | |
|---|---|
| **Path** | `BereanAI` |
| **Type** | Application |
| **Stack** | TypeScript, Node.js 22, TanStack Start, TanStack Router, Tailwind CSS, Auth.js, PostgreSQL, Docker Compose |
| **GitHub** | [dunamismax/BereanAI](https://github.com/dunamismax/BereanAI) |
| **Codeberg** | [dunamismax/BereanAI](https://codeberg.org/dunamismax/BereanAI) |

Self-hosted Christian AI research workspace. Selectable specialist agents with OpenAI/Anthropic fallback. ESV-aware local context search. Auth.js with PostgreSQL sessions. OpenTelemetry + SigNoz observability. Rate limiting and security hardening.

---

### mtg-card-bot

| | |
|---|---|
| **Path** | `mtg-card-bot` |
| **Type** | Bot / automation |
| **Stack** | Python 3.12+, discord.py, httpx, uv |
| **GitHub** | [dunamismax/mtg-card-bot](https://github.com/dunamismax/mtg-card-bot) |
| **Codeberg** | [dunamismax/mtg-card-bot](https://codeberg.org/dunamismax/mtg-card-bot) |

Discord bot for Magic: The Gathering card lookups via Scryfall. Prefix commands and bracket syntax (`[[Card Name]]`). Random card with filters, rules lookup, multi-card queries. Rich embeds with prices, legality, and imagery. Per-user cooldowns and duplicate suppression.

---

### c-from-the-ground-up

| | |
|---|---|
| **Path** | `c-from-the-ground-up` |
| **Type** | Educational curriculum |
| **Stack** | C11, GCC/Clang, Make, ncurses, POSIX threads |
| **GitHub** | [dunamismax/c-from-the-ground-up](https://github.com/dunamismax/c-from-the-ground-up) |
| **Codeberg** | [dunamismax/c-from-the-ground-up](https://codeberg.org/dunamismax/c-from-the-ground-up) |

Complete, open-source C programming curriculum. 35 progressive lessons across 5 parts (beginner to expert). Code-first learning with lessons embedded in code comments. Projects: calculators, text editors, network apps, multithreaded tools. Memory safety focus. Capstone: text adventure game.

---

### hello-world-from-hell

| | |
|---|---|
| **Path** | `hello-world-from-hell` |
| **Type** | Novelty / systems programming showcase |
| **Stack** | C17 (GNU extensions), SIMD (AVX2/NEON), POSIX threads |
| **GitHub** | [dunamismax/hello-world-from-hell](https://github.com/dunamismax/hello-world-from-hell) |
| **Codeberg** | [dunamismax/hello-world-from-hell](https://codeberg.org/dunamismax/hello-world-from-hell) |

The most cursed Hello World ever written in C. 11 randomized execution modes including trigraph witchcraft, 30+ macros, and Duff's device. SIMD vectorization, threading, atomic operations. Cross-platform (x86_64, ARM64). 17/17 tests passing with benchmarks.

---

### xray-chrome

| | |
|---|---|
| **Path** | `xray-chrome` |
| **Type** | Enterprise tooling |
| **Stack** | PowerShell, Windows enterprise policies |
| **GitHub** | [dunamismax/xray-chrome](https://github.com/dunamismax/xray-chrome) |
| **Codeberg** | [dunamismax/xray-chrome](https://codeberg.org/dunamismax/xray-chrome) |

PowerShell scripts to lock down Chrome on dedicated medical X-ray workstations. Restricts browsing to localhost only. Prevents automatic updates for medical software compatibility. Enterprise policy management via ADMX templates. Complete reversal script included. Windows 10/11.

---

### imagingservices

| | |
|---|---|
| **Path** | `imagingservices` |
| **Type** | Support tooling / knowledge base |
| **Stack** | Python, Shell scripts, Markdown |
| **GitHub** | [dunamismax/imagingservices](https://github.com/dunamismax/imagingservices) |
| **Codeberg** | [dunamismax/imagingservices](https://codeberg.org/dunamismax/imagingservices) |

AI support repo for day-to-day imaging software support work. Manual search scripts (SymSync, Ultra, Opal, mOpal). PDF extraction pipeline for searchable manual text. Agent policy docs and knowledge base of product manual extracts.

---

### imaging-services-website

| | |
|---|---|
| **Path** | `imaging-services-website` |
| **Type** | Website |
| **Stack** | PHP 8.2+, Laravel 12, Livewire 4, Tailwind CSS, Pest |
| **GitHub** | [dunamismax/imaging-services-website](https://github.com/dunamismax/imaging-services-website) |
| **Codeberg** | [dunamismax/imaging-services-website](https://codeberg.org/dunamismax/imaging-services-website) |

Imaging Services department website built with Laravel and Livewire.

---

### configs

| | |
|---|---|
| **Path** | `configs` |
| **Type** | Dotfiles / system configuration |
| **Stack** | Shell (bash/zsh), SSH config, terminal config |
| **GitHub** | [dunamismax/configs](https://github.com/dunamismax/configs) |
| **Codeberg** | [dunamismax/configs](https://codeberg.org/dunamismax/configs) |

Personal dotfiles and system configuration. Shell profiles (`.zshrc`, `.bash_profile`, `.profile`, `.zprofile`), SSH config, Ghostty terminal config, Ubuntu-WSL settings.

---

### dunamismax

| | |
|---|---|
| **Path** | `dunamismax` |
| **Type** | GitHub profile README |
| **Stack** | Markdown, GitHub widgets |
| **GitHub** | [dunamismax/dunamismax](https://github.com/dunamismax/dunamismax) |
| **Codeberg** | [dunamismax/dunamismax](https://codeberg.org/dunamismax/dunamismax) |

GitHub profile page. Professional summary, featured project badges, contribution stats, and tech arsenal display.

---

## By Language

| Language | Repos |
|---|---|
| **PHP / Laravel** | TALLstack, poddashboard, mylife-rpg, codex-web, imaging-services-website |
| **TypeScript** | scryai, BereanAI |
| **Python** | mtg-card-bot, imagingservices |
| **C** | c-from-the-ground-up, hello-world-from-hell |
| **PowerShell** | xray-chrome |
| **Shell / Config** | configs |
| **Markdown** | dunamismax |

## By Category

| Category | Repos |
|---|---|
| **Full-stack apps** | TALLstack, poddashboard, mylife-rpg, codex-web, BereanAI, imaging-services-website, scryai |
| **Bots / automation** | mtg-card-bot |
| **Educational** | c-from-the-ground-up, hello-world-from-hell |
| **Enterprise / IT** | xray-chrome, imagingservices |
| **Infrastructure / config** | configs, scryai (infra layer) |
| **Profile / docs** | dunamismax |
