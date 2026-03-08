# Hi, I'm Stephen 👋

📍 **Florida** · ⚙️ **Self-hosted systems builder** · 🐍 **Python + Rust** · 🧱 **Alias:** `dunamismax`

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Rust](https://img.shields.io/badge/-Rust-000000?style=flat-square&logo=rust&logoColor=white)
![Django](https://img.shields.io/badge/-Django-092E20?style=flat-square&logo=django&logoColor=white)
![FastAPI](https://img.shields.io/badge/-FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![uv](https://img.shields.io/badge/-uv-6E56CF?style=flat-square&logo=python&logoColor=white)
![Cargo](https://img.shields.io/badge/-Cargo-8C4A2F?style=flat-square&logo=rust&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/-Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![CLI](https://img.shields.io/badge/-CLI-000000?style=flat-square&logo=gnu-bash&logoColor=white)
![Self-Hosted](https://img.shields.io/badge/-Self--Hosted-2E8B57?style=flat-square&logo=serverfault&logoColor=white)

> I build software that still makes sense at 2am: self-hosted when possible, local-first where it matters, explicit about its tradeoffs, and verified before it gets trusted.

## What I build

Most of my work right now lives in two lanes:

- **Python** for operational products, automation, web apps, CLIs, and repo tooling
- **Rust** for cargo-native developer tools, policy engines, and build / ABI introspection

I care about software that is durable, understandable, and useful to the person actually operating it.

## Building now

### 🚨 ChangeLedger

**[ChangeLedger](https://github.com/dunamismax/changeledger)** is my flagship Python project: an operational memory and change intelligence platform for IT, platform, and ops teams.

It is intentionally built as **one Python-first product in one repo**.

- API, CLI, TUI, worker, connectors, docs site, and shared domain models live together
- The repo is organized for operation, not theater
- Current module lanes include:
  - **KEV Commander**
  - **Identity & SaaS Drift Watch**
  - **Incident Timeline & Recovery Proof**

## Active Rust work

- **[cargo-trust](https://github.com/dunamismax/cargo-trust)** — dependency admission control for Rust with explainable `allow`, `review`, and `block` decisions
- **[explain-build](https://github.com/dunamismax/explain-build)** — a cargo subcommand that captures `build`, `check`, `test`, and `run` sessions, then explains what changed between them
- **[abi-audit](https://github.com/dunamismax/abi-audit)** — a Cargo-native CLI for auditing Rust FFI and ABI boundaries

## Active Python work

- **[pymodernize](https://github.com/dunamismax/pymodernize)** — deterministic Python modernization planning and low-risk fixers
- **[verify-patch](https://github.com/dunamismax/verify-patch)** — patch-aware verification for Python repos with repo-native checks and GitHub-friendly output
- **[scriptspace](https://github.com/dunamismax/scriptspace)** — a PEP 723 workspace manager for single-file Python scripts
- **[pyforge](https://github.com/dunamismax/pyforge)** — a growing home for durable Python utilities and reusable tooling
- **[rip](https://github.com/dunamismax/rip)** — a self-hosted FastAPI app for inspecting formats and downloading media through `yt-dlp`
- **[podwatch](https://github.com/dunamismax/podwatch)** — a focused Django app for recurring groups and their scheduled events
- **[questlog](https://github.com/dunamismax/questlog)** — a Django app for quests, habits, and daily check-ins without gamified bloat
- **[trade-desk-cli](https://github.com/dunamismax/trade-desk-cli)** — a human-directed Python trading CLI with typed models, verification, and explicit operator control
- **[scryfall-discord-bot](https://github.com/dunamismax/scryfall-discord-bot)** — a Python Discord bot for fast Scryfall lookups and rich card embeds
- **[scry-home](https://github.com/dunamismax/scry-home)** — my Python-only control plane repo for workstation automation, docs, and local ops workflows

## How I build

- **Ship small. Verify always.**
- **Prefer boring infrastructure over clever architecture.**
- **Keep software self-hostable when control and durability matter.**
- **Make CLI, API, and operator workflows first-class.**
- **Treat docs as part of the product.**
- **Optimize for maintenance reality, not launch-day aesthetics.**

## What I optimize for

- local-first and self-hosted workflows
- understandable repo layouts
- deterministic tooling over magical abstractions
- operator-facing software that reduces cognitive load
- systems that can scale without becoming impossible to reason about

## Tech I reach for most

- **Python** for product velocity, automation, and operational software
- **Rust** for sharp, trustworthy developer tooling
- **Django** and **FastAPI** for practical web surfaces
- **PostgreSQL** for durable state
- **Docker** for reproducible local environments

## Elsewhere

[GitHub](https://github.com/dunamismax) · [Codeberg](https://codeberg.org/dunamismax)
