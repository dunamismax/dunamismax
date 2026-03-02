<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&height=200&color=0:020617,25:0f172a,50:7c2d12,75:ea580c,100:fb923c&text=Stephen%20Sawyer&fontColor=e2e8f0&fontSize=50&fontAlignY=38&desc=🦀%20dunamismax&descAlignY=56&descSize=18&animation=fadeIn" alt="Header" />

<p align="center">
  <strong>Full-Stack Engineer · <a href="https://github.com/openclaw/openclaw">OpenClaw</a> Contributor · Self-Hosting Evangelist</strong><br />
  Building self-hostable, operator-first systems. TypeScript, React, Bun, and whatever else the job demands.
</p>

<p align="center">
  <a href="https://github.com/openclaw/openclaw/pull/32217"><img src="https://img.shields.io/badge/🦀_OpenClaw-Contributor-ea580c?style=flat&labelColor=0f172a" alt="OpenClaw Contributor" /></a>&nbsp;
  <a href="https://github.com/dunamismax"><img src="https://img.shields.io/github/followers/dunamismax?style=flat&label=Followers&color=fb923c&labelColor=0f172a" alt="Followers" /></a>&nbsp;
  <a href="https://codeberg.org/dunamismax"><img src="https://img.shields.io/badge/Codeberg-Mirror-2185D0?style=flat&logo=codeberg&logoColor=white" alt="Codeberg" /></a>&nbsp;
  <img src="https://komarev.com/ghpvc/?username=dunamismax&label=Views&color=ea580c&style=flat" alt="Profile views" />
</p>

---

## Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=typescript,react,bun,vite,tailwind,postgres,python,docker,linux,git&perline=10" alt="Tech stack" />
</p>

```
Runtime        Bun
Language       TypeScript (strict)
Framework      Vite + React Router 7 (framework mode, SPA-first)
UI             React 19 · Tailwind CSS v4 · shadcn/ui
Mobile         React Native + Expo
Data           PostgreSQL · Drizzle ORM
API            Hono
Auth           Better Auth
Validation     Zod
Quality        Biome (lint + format)
```

---

## Projects

### Full-Stack Applications

<table>
  <tr>
    <td width="50%">
      <h3><a href="https://github.com/dunamismax/reactiveweb">reactiveweb</a></h3>
      <p>Full-stack web platform with session auth, RBAC, Hono API, and dark-themed UI. The canonical template for the stack.</p>
      <p><sub>Bun · React 19 · React Router 7 · Hono · Postgres · Drizzle · Tailwind v4 · shadcn/ui</sub></p>
    </td>
    <td width="50%">
      <h3><a href="https://github.com/dunamismax/poddashboard">poddashboard</a></h3>
      <p>Pod management and event dashboard with credentials auth, role-based permissions, and session-authenticated API.</p>
      <p><sub>Bun · React 19 · React Router 7 · Hono · Postgres · Drizzle · TanStack Query</sub></p>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <h3><a href="https://github.com/dunamismax/mylife-rpg">mylife-rpg</a></h3>
      <p>Gamified productivity system. Quests, habits, XP, leveling, stat progression, and achievements — powered by a testable domain-driven RPG engine.</p>
      <p><sub>Bun · React 19 · React Router 7 · Postgres · Drizzle · TanStack Query · shadcn/ui</sub></p>
    </td>
    <td width="50%">
      <h3><a href="https://github.com/dunamismax/open-video-downloader">open-video-downloader</a></h3>
      <p>Self-hosted video downloader for 1700+ sites. Paste a URL, pick a format, download. Real-time progress via WebSocket. Powered by yt-dlp + ffmpeg.</p>
      <p><sub>Bun · React 19 · Hono · WebSocket · TanStack Query · Tailwind v4</sub></p>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <h3><a href="https://github.com/dunamismax/elchess">elchess</a></h3>
      <p>Self-hostable chess platform. Interactive board with legal move highlighting, full game state detection, move history, and material tracking.</p>
      <p><sub>Bun · React 19 · React Router 7 · Vite · chess.js · Tailwind v4</sub></p>
    </td>
    <td width="50%">
      <h3><a href="https://github.com/dunamismax/CallRift">CallRift</a></h3>
      <p>Mobile SIP/VoIP client with contact management, call history, and real-time messaging. Native performance, cross-platform.</p>
      <p><sub>React Native · Expo SDK 55 · React 19 · Zustand · Fastify · Drizzle</sub></p>
    </td>
  </tr>
</table>

### Developer Tools & Automation

<table>
  <tr>
    <td width="50%">
      <h3><a href="https://github.com/dunamismax/repo-monitor">repo-monitor</a></h3>
      <p>Real-time dashboard for monitoring AI agent activity across git repos. Detects Claude, Cursor, Aider, and Codex. SSE streaming, inline diffs, keyboard-driven UI.</p>
      <p><sub>Bun · React 19 · React Router 7 · SSE · Tailwind v4</sub></p>
    </td>
    <td width="50%">
      <h3><a href="https://github.com/dunamismax/scryai-typescript">scryai-typescript</a></h3>
      <p>Operations CLI and agent identity repo. Workstation bootstrap, project orchestration, dual-remote sync, cross-repo health checks, and OpenClaw config.</p>
      <p><sub>Bun · TypeScript · Biome</sub></p>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <h3><a href="https://github.com/dunamismax/scry-trader">scry-trader</a></h3>
      <p>Automated trading system with Interactive Brokers integration and Claude-powered market analysis. Real-time data, strategy execution, risk management.</p>
      <p><sub>Python · IBKR API · Claude · asyncio</sub></p>
    </td>
    <td width="50%">
      <h3><a href="https://github.com/dunamismax/mtg-card-bot">mtg-card-bot</a></h3>
      <p>Discord bot for Magic: The Gathering card lookups via Scryfall. Bracket syntax, random pulls, rules lookup, rich embeds with prices and legality.</p>
      <p><sub>Python 3.12+ · discord.py · httpx · Scryfall API</sub></p>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <h3><a href="https://github.com/dunamismax/configs">configs</a></h3>
      <p>Dotfiles and workstation config. Shell profiles, SSH config, Ghostty terminal, VS Code Insiders settings — organized by OS.</p>
      <p><sub>Zsh · Bash · SSH · Ghostty</sub></p>
    </td>
    <td width="50%"></td>
  </tr>
</table>

---

## Principles

- **Ship small, verify always.** Lint, typecheck, build, test — every change, no exceptions.
- **Self-hostable by default.** If you can't run it yourself, you don't own it.
- **Boring infrastructure.** Postgres over the database of the week. Deterministic tooling over novelty.
- **Operator-first design.** Systems should survive being handed to a stranger with only the README.
- **Right tool for the job.** TypeScript is the default, not the religion. Python, Rust, Go — whatever actually fits.
- **Mirror everything.** All repos on [GitHub](https://github.com/dunamismax) + [Codeberg](https://codeberg.org/dunamismax). Platform risk is not existential. 🦀

---

## Activity

<p align="center">
  <img height="160" src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=dunamismax&theme=github_dark" alt="GitHub stats" />
  <img height="160" src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=dunamismax&theme=github_dark" alt="Top languages" />
</p>

<p align="center">
  <img src="https://streak-stats.demolab.com/?user=dunamismax&theme=transparent&hide_border=true&ring=ea580c&fire=fb923c&currStreakLabel=fb923c&sideNums=cbd5e1&currStreakNum=e2e8f0&dates=94a3b8" alt="Contribution streak" />
</p>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=dunamismax&bg_color=0d111700&color=fb923c&line=ea580c&point=e2e8f0&area=true&hide_border=true" alt="Activity graph" />
</p>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&section=footer&height=120&color=0:020617,25:0f172a,50:7c2d12,75:ea580c,100:fb923c" alt="Footer" />
