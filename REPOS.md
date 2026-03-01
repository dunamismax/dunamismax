# Repository Index

> Complete index of Stephen Sawyer's (`dunamismax`) repositories.
> All repos live under `~/github/` and most are mirrored across GitHub and Codeberg.
> Last updated: 2026-03-01.

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
- Use `bun run scry:sync:remotes` in the scryai repo to verify and fix remotes across all projects.

---

## Repositories

### reactiveweb

| | |
|---|---|
| **Type** | Full-stack web application |
| **Stack** | Bun, React 19, React Router 7, Hono, Tailwind CSS v4, PostgreSQL, Drizzle ORM, Zod, Biome |
| **GitHub** | [dunamismax/reactiveweb](https://github.com/dunamismax/reactiveweb) |
| **Codeberg** | [dunamismax/reactiveweb](https://codeberg.org/dunamismax/reactiveweb) |

Full-stack web app platform with authentication, RBAC, Hono API backend, and dark-themed UI with shadcn/ui patterns.

---

### open-video-downloader

| | |
|---|---|
| **Type** | Self-hosted web application |
| **Stack** | Bun, React 19, React Router 7, Hono, WebSocket, Tailwind CSS v4, Zod, Biome |
| **GitHub** | [dunamismax/open-video-downloader](https://github.com/dunamismax/open-video-downloader) |

Self-hosted web app for downloading videos from 1700+ sites. Paste a URL, pick a format, download. Powered by yt-dlp and ffmpeg. Real-time progress via WebSocket.

---

### repo-monitor

| | |
|---|---|
| **Type** | Developer tool |
| **Stack** | Bun, React 19, React Router 7, SSE, Tailwind CSS v4, Biome |
| **GitHub** | [dunamismax/repo-monitor](https://github.com/dunamismax/repo-monitor) |

Real-time dashboard for monitoring AI agent activity across git repositories. Detects Claude, Cursor, Aider, and Codex. Keyboard navigation, diff preview, activity firehose.

---

### poddashboard

| | |
|---|---|
| **Type** | Full-stack web application |
| **Stack** | Bun, React 19, React Router 7, Tailwind CSS v4, PostgreSQL, Drizzle ORM, Zod, Biome |
| **GitHub** | [dunamismax/poddashboard](https://github.com/dunamismax/poddashboard) |
| **Codeberg** | [dunamismax/poddashboard](https://codeberg.org/dunamismax/poddashboard) |

Pod management and event dashboard with credentials auth, role-based permissions, and session-authenticated API endpoints.

---

### mylife-rpg

| | |
|---|---|
| **Type** | Full-stack web application |
| **Stack** | Bun, React 19, React Router 7, Tailwind CSS v4, PostgreSQL, Drizzle ORM, Zod, Biome |
| **GitHub** | [dunamismax/mylife-rpg](https://github.com/dunamismax/mylife-rpg) |
| **Codeberg** | [dunamismax/mylife-rpg](https://codeberg.org/dunamismax/mylife-rpg) |

Gamified productivity system. Quests, habits, XP/leveling, stat progression, and achievements. Domain-driven RPG engine with testable rules.

---

### scryai

| | |
|---|---|
| **Type** | Operations CLI / identity hub |
| **Stack** | Bun, TypeScript, Biome |
| **GitHub** | [dunamismax/scryai](https://github.com/dunamismax/scryai) |
| **Codeberg** | [dunamismax/scryai](https://codeberg.org/dunamismax/scryai) |

Operations CLI and identity hub for **scry**. Workstation bootstrap, project orchestration, SSH key management, dual-remote sync, and cross-repo health checks.

---

### mtg-card-bot

| | |
|---|---|
| **Type** | Discord bot |
| **Stack** | Python 3.12+, discord.py, httpx, uv |
| **GitHub** | [dunamismax/mtg-card-bot](https://github.com/dunamismax/mtg-card-bot) |
| **Codeberg** | [dunamismax/mtg-card-bot](https://codeberg.org/dunamismax/mtg-card-bot) |

Discord bot for Magic: The Gathering card lookups via Scryfall. Bracket syntax, random pulls, rules lookup, rich embeds with prices and legality. Per-user cooldowns and rate limiting.

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

### configs

| | |
|---|---|
| **Type** | Dotfiles / system configuration |
| **Stack** | Shell (bash/zsh), SSH config, terminal config |
| **GitHub** | [dunamismax/configs](https://github.com/dunamismax/configs) |
| **Codeberg** | [dunamismax/configs](https://codeberg.org/dunamismax/configs) |

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

---

## By Language

| Language | Repos |
|---|---|
| **TypeScript / React** | reactiveweb, open-video-downloader, repo-monitor, poddashboard, mylife-rpg |
| **TypeScript (CLI)** | scryai |
| **Python** | mtg-card-bot |
| **Shell / Config** | configs |
| **Markdown / Docs** | dunamismax, images, Sawyer-Visual-Media, work |

## By Category

| Category | Repos |
|---|---|
| **Full-stack apps** | reactiveweb, poddashboard, mylife-rpg |
| **Developer tools** | open-video-downloader, repo-monitor |
| **Bots / automation** | mtg-card-bot |
| **Infrastructure / ops** | scryai, configs |
| **Business / docs** | Sawyer-Visual-Media, work |
| **Profile / assets** | dunamismax, images |
