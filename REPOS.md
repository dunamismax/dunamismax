# Repository Index

> Complete index of Stephen Sawyer's (`dunamismax`) repositories.
> All repos live under `~/github/` and most are mirrored across GitHub and Codeberg.
> Generated from `data/repos.json` via `python3 scripts/generate_docs.py`.

---

## Source Control Strategy

### Dual-Remote Mirroring (GitHub + Codeberg)

Most repositories use a single `origin` remote with dual push URLs:

```
origin  git@github.com-dunamismax:dunamismax/<repo>.git   (fetch)
origin  git@github.com-dunamismax:dunamismax/<repo>.git   (push)
origin  git@codeberg.org-dunamismax:dunamismax/<repo>.git  (push)
```

One `git push` publishes to both hosts. This is an intentional resilience pattern — platform risk is not existential when source control is redundant across providers.

**Rules:**

- All remotes use **SSH**, never HTTPS.
- Fetch comes from GitHub. Push goes to both GitHub and Codeberg.
- New repos get dual push URLs wired immediately after clone or init.
- SSH host config and dedicated identities are maintained in `~/.ssh/config` for both providers.
- Use `bun run scry:sync:remotes` in the grimoire repo to verify and fix remotes across all projects.

---

## Repositories


### homepage

| | |
|---|---|
| **Type** | Full-stack web application |
| **Stack** | Bun, React 19, React Router 7, Hono, Tailwind CSS v4, PostgreSQL, Drizzle ORM, Zod, Biome |
| **GitHub** | [dunamismax/homepage](https://github.com/dunamismax/homepage) |
| **Codeberg** | [dunamismax/homepage](https://codeberg.org/dunamismax/homepage) |

Full-stack web app platform with authentication, RBAC, Hono API backend, and dark-themed UI with shadcn/ui patterns.

---

### rip

| | |
|---|---|
| **Type** | Self-hosted web application |
| **Stack** | Bun, React 19, React Router 7, Hono, WebSocket, Tailwind CSS v4, Zod, Biome |
| **GitHub** | [dunamismax/rip](https://github.com/dunamismax/rip) |
| **Codeberg** | [dunamismax/rip](https://codeberg.org/dunamismax/rip) |

Self-hosted web app for downloading videos from 1700+ sites. Paste a URL, pick a format, download. Powered by yt-dlp and ffmpeg. Real-time progress via WebSocket.

---

### sentinel

| | |
|---|---|
| **Type** | Developer tool |
| **Stack** | Bun, React 19, React Router 7, SSE, Tailwind CSS v4, Biome |
| **GitHub** | [dunamismax/sentinel](https://github.com/dunamismax/sentinel) |
| **Codeberg** | [dunamismax/sentinel](https://codeberg.org/dunamismax/sentinel) |

Real-time dashboard for monitoring AI agent activity across git repositories. Detects Claude, Cursor, Aider, and Codex. Keyboard navigation, diff preview, activity firehose.

---

### podwatch

| | |
|---|---|
| **Type** | Full-stack web application |
| **Stack** | Bun, React 19, React Router 7, Tailwind CSS v4, PostgreSQL, Drizzle ORM, Zod, Biome |
| **GitHub** | [dunamismax/podwatch](https://github.com/dunamismax/podwatch) |
| **Codeberg** | [dunamismax/podwatch](https://codeberg.org/dunamismax/podwatch) |

Pod management and event dashboard with credentials auth, role-based permissions, and session-authenticated API endpoints.

---

### questlog

| | |
|---|---|
| **Type** | Full-stack web application |
| **Stack** | Bun, React 19, React Router 7, Tailwind CSS v4, PostgreSQL, Drizzle ORM, Zod, Biome |
| **GitHub** | [dunamismax/questlog](https://github.com/dunamismax/questlog) |
| **Codeberg** | [dunamismax/questlog](https://codeberg.org/dunamismax/questlog) |

Gamified productivity system. Quests, habits, XP/leveling, stat progression, and achievements. Domain-driven RPG engine with testable rules.

---

### elchess

| | |
|---|---|
| **Type** | Self-hosted web application |
| **Stack** | Bun, React 19, React Router 7, Vite, chess.js, Tailwind CSS v4, Biome |
| **GitHub** | [dunamismax/elchess](https://github.com/dunamismax/elchess) |
| **Codeberg** | [dunamismax/elchess](https://codeberg.org/dunamismax/elchess) |

Self-hostable chess platform. Interactive board with click-to-move, legal move highlighting, full game state detection, move history, captured pieces, and material tracking.

---

### CallRift

| | |
|---|---|
| **Type** | Mobile application |
| **Stack** | React Native, Expo SDK 55, React 19, Zustand, Fastify, Drizzle, SQLite, Biome |
| **GitHub** | [dunamismax/CallRift](https://github.com/dunamismax/CallRift) |
| **Codeberg** | [dunamismax/CallRift](https://codeberg.org/dunamismax/CallRift) |

Mobile SIP/VoIP client with contact management, call history search, real-time messaging, pull-to-refresh, persisted settings, and error boundaries. Cross-platform via Expo.

---

### grimoire

| | |
|---|---|
| **Type** | Operations CLI / identity hub |
| **Stack** | Bun, TypeScript, Biome |
| **GitHub** | [dunamismax/grimoire](https://github.com/dunamismax/grimoire) |
| **Codeberg** | [dunamismax/grimoire](https://codeberg.org/dunamismax/grimoire) |

Operations CLI and identity hub for Scry. Workstation bootstrap, project orchestration, SSH key management, dual-remote sync, OpenClaw config, and cross-repo health checks.

---

### augur

| | |
|---|---|
| **Type** | Trading system |
| **Stack** | Python 3.12+, ib-async, Anthropic Claude, Click, Rich, Pydantic, pandas |
| **GitHub** | [dunamismax/augur](https://github.com/dunamismax/augur) |
| **Codeberg** | [dunamismax/augur](https://codeberg.org/dunamismax/augur) |

AI-assisted, human-directed trading system. Claude analyzes and recommends, you confirm. IBKR integration for live portfolio, quotes, and order execution. Rule-based risk management, trade journaling, CLI-native interface.

---

### oracle

| | |
|---|---|
| **Type** | Discord bot |
| **Stack** | Python 3.12+, discord.py, httpx, uv |
| **GitHub** | [dunamismax/oracle](https://github.com/dunamismax/oracle) |
| **Codeberg** | [dunamismax/oracle](https://codeberg.org/dunamismax/oracle) |

Discord bot for Magic: The Gathering card lookups via Scryfall. Bracket syntax, random pulls, rules lookup, rich embeds with prices and legality. Per-user cooldowns and rate limiting.

---

### PodScry

| | |
|---|---|
| **Type** | Preconfigured AI gateway deployment |
| **Stack** | OpenClaw, Docker, Docker Compose, Markdown |
| **GitHub** | [dunamismax/PodScry](https://github.com/dunamismax/PodScry) |
| **Codeberg** | [dunamismax/PodScry](https://codeberg.org/dunamismax/PodScry) |

Pre-configured OpenClaw instance for Discord playgroups. MTG Commander knowledge base, Docker-ready deployment, and playgroup-focused defaults.

---

### Sawyer-Visual-Media

| | |
|---|---|
| **Type** | Business operations |
| **Stack** | Markdown, business documents |
| **GitHub** | [dunamismax/Sawyer-Visual-Media](https://github.com/dunamismax/Sawyer-Visual-Media) |
| **Codeberg** | [dunamismax/Sawyer-Visual-Media](https://codeberg.org/dunamismax/Sawyer-Visual-Media) |

Business repository for Sawyer Visual Media — professional aerial drone photography and videography. Marketing, operations, legal, finances, portfolio, and website.

---

### dotfiles

| | |
|---|---|
| **Type** | Dotfiles / system configuration |
| **Stack** | Shell (bash/zsh), SSH config, terminal config |
| **GitHub** | [dunamismax/dotfiles](https://github.com/dunamismax/dotfiles) |
| **Codeberg** | [dunamismax/dotfiles](https://codeberg.org/dunamismax/dotfiles) |

Personal workstation configuration backups. Shell profiles, SSH config, Ghostty terminal, VS Code Insiders settings.

---

### images

| | |
|---|---|
| **Type** | Static assets |
| **Stack** | PNG, JPG, SVG, GIF, MOV |
| **GitHub** | [dunamismax/images](https://github.com/dunamismax/images) |
| **Codeberg** | [dunamismax/images](https://codeberg.org/dunamismax/images) |

Central media library for reusable images, icons, screenshots, and visual assets across projects.

---

### work

| | |
|---|---|
| **Type** | Work documents |
| **Stack** | Documents, templates |
| **GitHub** | [dunamismax/work](https://github.com/dunamismax/work) |
| **Codeberg** | [dunamismax/work](https://codeberg.org/dunamismax/work) |

Work-related documents, email templates, employee handbook materials, marketing assets, and the imaging services website.

---

### dunamismax

| | |
|---|---|
| **Type** | GitHub profile README |
| **Stack** | Markdown, GitHub widgets |
| **GitHub** | [dunamismax/dunamismax](https://github.com/dunamismax/dunamismax) |
| **Codeberg** | [dunamismax/dunamismax](https://codeberg.org/dunamismax/dunamismax) |

GitHub profile page. Professional summary, featured projects, contribution stats, and tech stack display.

## By Language

| Language | Repos |
|---|---|
| **TypeScript / React** | homepage, rip, sentinel, podwatch, questlog, elchess |
| **TypeScript (Mobile)** | CallRift |
| **TypeScript (CLI)** | grimoire |
| **Python** | augur, oracle |
| **Shell / Config** | dotfiles |
| **Markdown / Docs** | PodScry, Sawyer-Visual-Media, images, work, dunamismax |

## By Category

| Category | Repos |
|---|---|
| **Full-stack apps** | homepage, podwatch, questlog, elchess |
| **Self-hosted tools** | rip |
| **Mobile** | CallRift |
| **Developer tools** | sentinel, grimoire |
| **Trading** | augur |
| **Bots / automation** | oracle |
| **AI gateway deployments** | PodScry |
| **Infrastructure / ops** | dotfiles |
| **Business / docs** | Sawyer-Visual-Media, work |
| **Profile / assets** | images, dunamismax |
