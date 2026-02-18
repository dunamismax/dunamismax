# Repository Index

> Complete index of Stephen Sawyer's (`dunamismax`) repositories, their purpose, stack, and source control strategy.
> All repos live under `/home/sawyer/github/` and are mirrored across GitHub and Codeberg.
> Last updated: 2026-02-17.

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
| **PHP / Laravel** | poddashboard, mylife-rpg, codex-web, imaging-services-website |
| **TypeScript** | scryai |
| **Python** | mtg-card-bot |
| **Shell / Config** | configs |
| **Markdown** | dunamismax |

## By Category

| Category | Repos |
|---|---|
| **Full-stack apps** | poddashboard, mylife-rpg, codex-web, imaging-services-website, scryai |
| **Bots / automation** | mtg-card-bot |
| **Infrastructure / config** | configs, scryai (infra layer) |
| **Profile / docs** | dunamismax |
