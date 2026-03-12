# Stephen Sawyer

Bun-first TypeScript builder for self-hosted products, control planes, and operator-facing software.

![Bun](https://img.shields.io/badge/Bun-1.3+-000000?style=flat-square&logo=bun&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-5.x-3178C6?style=flat-square&logo=typescript&logoColor=white)
![TanStack Start](https://img.shields.io/badge/TanStack-Start-FF4154?style=flat-square&logo=tanstack&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16+-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Drizzle ORM](https://img.shields.io/badge/Drizzle-ORM-C5F74F?style=flat-square&logo=drizzle&logoColor=111111)
![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-Wired-6B3FA0?style=flat-square&logo=opentelemetry&logoColor=white)

I spend most of my time building Bun monorepos with shared contracts across web, server, and CLI packages. The common thread is narrow products, explicit data flow, authentication that is part of the design, and observability wired in before the system gets complicated.

## Current stack

- Runtime, scripts, and workspaces: Bun
- Language: TypeScript
- App layer: TanStack Start, TanStack Router, TanStack Query
- Data: PostgreSQL + Drizzle ORM
- Validation and contracts: Zod
- Auth: Better Auth
- Tooling: Biome + Vitest
- Observability: OpenTelemetry

## What I optimize for

- Self-hosted and operator-facing software that a small team can actually own
- Clear contracts between packages instead of hidden framework magic
- Web apps, CLIs, and background workflows that share the same domain model
- Docs, tests, and telemetry as part of the feature, not cleanup work later

## Current repos

Most of my active work now lives in these Bun-first repositories:

<!-- BEGIN GENERATED FEATURED REPOS -->
- **[scry-home](https://github.com/dunamismax/scry-home)** - Control plane monorepo for local repo operations, encrypted backups, CAB packet scaffolding, and an operator dashboard.
- **[Roleback](https://github.com/dunamismax/Roleback)** - Self-hostable Discord server backup platform with a TanStack Start dashboard, bot runtime, Drizzle persistence, and observability.
- **[rip](https://github.com/dunamismax/rip)** - Authenticated self-hosted `yt-dlp` workspace with PostgreSQL-backed queues, Better Auth, and OpenTelemetry around download workflows.
- **[QuestLog](https://github.com/dunamismax/questlog)** - Personal execution journal for quests, habits, daily check-ins, and a lightweight XP loop.
- **[PodWatch](https://github.com/dunamismax/podwatch)** - Recurring-group scheduling app for pods, events, and timeline review inside a Bun monorepo.
- **[tsforge](https://github.com/dunamismax/tsforge)** - Email template conversion workbench that pairs a Bun CLI with a TanStack Start app and a TypeScript converter core.
<!-- END GENERATED FEATURED REPOS -->

## Also in the workshop

I still keep a hand in adjacent work when control is worth the cost:

- **[boring-go-web](https://github.com/dunamismax/boring-go-web)** - Practical Go starter with Echo, Templ, HTMX, PostgreSQL, SQLC, and the kind of auth and ops plumbing I want from day one.
- **[c-from-the-ground-up](https://github.com/dunamismax/c-from-the-ground-up)** - Project-based C workbook for staying close to systems fundamentals and understanding what abstractions cost.

## Open source

- Contributor to **[OpenClaw](https://github.com/openclaw/openclaw)**, a multi-surface personal assistant project with chat, browser, desktop, and mobile integrations.

## Elsewhere

[GitHub](https://github.com/dunamismax) · [Codeberg](https://codeberg.org/dunamismax)
