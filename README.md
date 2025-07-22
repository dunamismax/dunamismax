<p align="center">
  <img src="https://raw.githubusercontent.com/dunamismax/gohub/main/docs/images/go-logo.png" alt="Go Developer Logo" width="400" />
</p>

<p align="center">
  <a href="https://github.com/dunamismax">
    <img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&size=24&pause=1000&color=00ADD8&center=true&vCenter=true&width=900&lines=Modern+Go+Developer;Echo+%2B+Templ+%2B+HTMX+Architecture;Enterprise+Security+%26+Performance;Single+Binary+Deployment;Type-Safe+Database+Operations;Production-Ready+Monorepos;Radical+Simplicity+%26+Stability;CGO-Free+Pure+Go+Binaries;Unified+Backend+Infrastructure;CSRF+%2B+XSS+Protection;Structured+Logging+%26+Testing;Zero+External+Dependencies" alt="Typing SVG" />
  </a>
</p>

<p align="center">
  <a href="https://golang.org/"><img src="https://img.shields.io/badge/Go-1.24+-00ADD8.svg?logo=go" alt="Go Version"></a>
  <a href="https://echo.labstack.com/"><img src="https://img.shields.io/badge/Framework-Echo-00ADD8.svg?logo=go" alt="Echo Framework"></a>
  <a href="https://templ.guide/"><img src="https://img.shields.io/badge/Templates-Templ-00ADD8.svg?logo=go" alt="Templ"></a>
  <a href="https://htmx.org/"><img src="https://img.shields.io/badge/Frontend-HTMX-3D72D7.svg?logo=htmx" alt="HTMX"></a>
  <a href="https://sqlc.dev/"><img src="https://img.shields.io/badge/SQL-sqlc-00ADD8.svg?logo=go" alt="sqlc"></a>
  <a href="https://www.sqlite.org/"><img src="https://img.shields.io/badge/Database-SQLite-003B57.svg?logo=sqlite" alt="SQLite"></a>
  <a href="https://magefile.org/"><img src="https://img.shields.io/badge/Build-Mage-purple.svg?logo=go" alt="Mage"></a>
</p>

---

## About

**Go developer** specializing in **enterprise-grade web applications** with **radical simplicity**. I build high-performance monorepo systems using the modern Go stack, emphasizing security, type safety, and single binary deployment with zero external dependencies.

**Philosophy**: Pragmatic simplicity meets enterprise security. Every project showcases production-ready patterns - CSRF protection, XSS prevention, type-safe operations, structured logging, and comprehensive testing - all compiled into fast, self-contained binaries that deploy anywhere.

---

## Featured Projects

### **[GoHub](https://github.com/dunamismax/gohub)** - Enterprise Go Monorepo

<p align="center">
  <a href="https://github.com/dunamismax/gohub">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=dunamismax&repo=gohub&theme=dark&show_owner=true" alt="gohub" />
  </a>
</p>

**Enterprise-grade monorepo** showcasing unified backend architecture - web and TUI applications sharing platform services, data access, and configuration with comprehensive security and testing.

**Tech Stack:** Go 1.24 + Echo + Bubble Tea + Templ + HTMX + sqlc + SQLite + Mage
**Architecture:** Unified Backend • Shared Platform Services • Multiple Application Interfaces
**Security:** CSRF Protection • XSS Prevention • Input Validation • Vulnerability Scanning
**Operations:** Single Binary • Database Migrations • Structured Logging • CI/CD Pipeline

### **[Go Web Server](https://github.com/dunamismax/go-web-server)** - Minimal Perfect Template

<p align="center">
  <a href="https://github.com/dunamismax/go-web-server">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=dunamismax&repo=go-web-server&theme=dark&show_owner=true" alt="go-web-server" />
  </a>
</p>

**Perfect minimal template** for modern web development using the Modern Go Stack - radical simplicity and production stability with CGO-free, self-contained binaries.

**Tech Stack:** Go 1.24 + Echo + Templ + HTMX + Pico.css + sqlc + SQLite + slog
**Features:** Zero Dependencies • Type Safety • Hot Reloading • Embedded Assets
**Benefits:** 10-15MB Binary • Instant Startup • Production Patterns • Pure Go

---

## Quick Start

```bash
# Enterprise Monorepo (Security + Testing + TUI)
git clone https://github.com/dunamismax/gohub.git
cd gohub && mage setup && mage dev:server

# Minimal Template (Perfect Starting Point)
git clone https://github.com/dunamismax/go-web-server.git
cd go-web-server && make run

# Both create single binaries with embedded assets - zero dependencies!
```

<p align="center">
  <img src="https://raw.githubusercontent.com/dunamismax/gohub/main/docs/images/gopher-mage.svg" alt="Gopher Mage" width="150" />
</p>

## Modern Build System with Mage

**GoHub** showcases advanced **Go-based build automation** with [**Mage**](https://magefile.org/) - replacing Makefiles with pure Go for better maintainability and cross-platform support.

```bash
# Development Workflow
mage setup            # Install all tools and dependencies
mage generate:all     # Generate sqlc + templ code
mage dev:server       # Start web app with hot reload
mage dev:tui          # Launch interactive TUI dashboard

# Build & Quality
mage build:all        # Build both webapp and TUI binaries
mage test:all         # Run comprehensive test suite
mage quality:all      # Format, vet, and vulnerability scan

# Database Operations
mage database:up      # Run all database migrations
mage database:reset   # Reset database with fresh schema

# Production Ready
mage ci               # Complete CI pipeline (generate → quality → test → build)
mage clean            # Clean all build artifacts
```

**Why Mage?** Pure Go build scripts, better dependency management, cross-platform compatibility, and excellent IDE integration compared to traditional Makefiles.

## Technical Expertise

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=go,sqlite,docker,linux,git,github,vscode,bash" />
  </a>
</p>

**Core Stack**: Go 1.24 • Echo • Templ • HTMX • sqlc • SQLite • Bubble Tea • Mage • slog

**Architecture Specializations**:

- **Enterprise Security**: CSRF protection, XSS prevention, input validation, secure headers
- **Type-Safe Operations**: sqlc database queries, templ templates, comprehensive error handling
- **Modern Go Stack**: Echo framework, Bubble Tea TUIs, HTMX interactions, Pico.css styling
- **Production Excellence**: Single binary deployment, structured logging, database migrations
- **Monorepo Design**: Unified backend, shared platform services, multiple application interfaces
- **Quality Engineering**: Comprehensive testing, CI/CD pipelines, vulnerability scanning
- **Performance Focus**: Zero dependencies, embedded assets, sub-second startup times
- **Developer Experience**: Mage build automation, hot reloading, professional tooling

---

## GitHub Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=dunamismax&show_icons=true&theme=dark&count_private=true" alt="GitHub Stats" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=dunamismax&layout=compact&theme=dark" alt="Top Languages" />
</p>

---

## Support My Work

If you find these **Modern Go Stack projects** valuable for building **secure, high-performance web applications** with **enterprise security**, **type safety**, and **single binary deployment**, consider supporting continued development:

<p align="center">
  <a href="https://buymeacoffee.com/dunamismax" target="_blank">
    <img src="https://raw.githubusercontent.com/dunamismax/gohub/main/docs/images/buy-coffee-go.gif" alt="Buy Me A Coffee" style="height: 150px !important;" />
  </a>
</p>

---

## Connect With Me

<p align="center">
  <a href="https://twitter.com/dunamismax" target="_blank"><img src="https://img.shields.io/badge/Twitter-%231DA1F2.svg?&style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter"></a>
  <a href="https://bsky.app/profile/dunamismax.bsky.social" target="_blank"><img src="https://img.shields.io/badge/Bluesky-blue?style=for-the-badge&logo=bluesky&logoColor=white" alt="Bluesky"></a>
  <a href="https://reddit.com/user/dunamismax" target="_blank"><img src="https://img.shields.io/badge/Reddit-%23FF4500.svg?&style=for-the-badge&logo=reddit&logoColor=white" alt="Reddit"></a>
  <a href="https://discord.com/users/dunamismax" target="_blank"><img src="https://img.shields.io/badge/Discord-dunamismax-7289DA.svg?style=for-the-badge&logo=discord&logoColor=white" alt="Discord"></a>
  <a href="https://signal.me/#p/+dunamismax.66" target="_blank"><img src="https://img.shields.io/badge/Signal-dunamismax.66-3A76F0.svg?style=for-the-badge&logo=signal&logoColor=white" alt="Signal"></a>
</p>

---

<p align="center">
  <strong>Building Enterprise Applications with Modern Go Architecture</strong><br>
  <sub>Go 1.24 • Echo • Templ • HTMX • sqlc • SQLite • Bubble Tea • CSRF Protection • Zero Dependencies</sub>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/dunamismax/gohub/main/docs/images/gopher-running-jumping.gif" alt="Gopher Running and Jumping" width="400" />
</p>
