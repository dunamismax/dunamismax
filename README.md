<p align="center">
  <img src="https://raw.githubusercontent.com/dunamismax/gohub/main/docs/images/go-logo.png" alt="Go Developer Logo" width="400" />
</p>

<p align="center">
  <a href="https://github.com/dunamismax">
    <img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&size=24&pause=1000&color=00ADD8&center=true&vCenter=true&width=800&lines=Modern+Go+Developer;Echo+%2B+Templ+%2B+HTMX+Architecture;Enterprise-Grade+Security;Single+Binary+Deployment;Type-Safe+Database+Operations;Production-Ready+Monorepos" alt="Typing SVG" />
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
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="MIT License"></a>
</p>

---

## About

**Modern Go developer** specializing in production-ready web applications with **enterprise security**, **type-safe architecture**, and **single binary deployment**. I build high-performance monorepo applications using the modern Go stack that prioritize security, maintainability, and operational simplicity.

**Current Focus**: Building comprehensive Go monorepos showcasing modern web development - unified backend architecture, CSRF protection, XSS prevention, type-safe database operations, and comprehensive testing that achieve lightning-fast performance while maintaining zero external dependencies.

---

## Featured Projects

### **[GoHub](https://github.com/dunamismax/gohub)** - Enterprise Go Monorepo

<p align="center">
  <a href="https://github.com/dunamismax/gohub">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=dunamismax&repo=gohub&theme=dark&show_owner=true" alt="gohub" />
  </a>
</p>

**Production-ready monorepo** demonstrating modern Go development with unified backend architecture - web and TUI applications sharing data access, configuration, and business logic with enterprise-grade security.

**Tech Stack:** Go 1.24 + Echo + Bubble Tea + Templ + HTMX + sqlc + SQLite + Mage  
**Applications:** Web App with CSRF Protection • Interactive TUI Dashboard • Unified Database Layer  
**Features:** Enterprise Security • Type Safety • Single Binary • Comprehensive Testing • CI/CD Pipeline

### **[Go Web Server](https://github.com/dunamismax/go-web-server)** - Minimal Perfect Template

<p align="center">
  <a href="https://github.com/dunamismax/go-web-server">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=dunamismax&repo=go-web-server&theme=dark&show_owner=true" alt="go-web-server" />
  </a>
</p>

**Minimal, reusable template** for modern web development using the Modern Go Stack - radical simplicity and stability with single, self-contained binaries and zero external dependencies.

**Tech Stack:** Go 1.24 + Echo + Templ + HTMX + Pico.css + sqlc + SQLite + slog  
**Features:** Single Binary • Type Safety • Hot Reloading • Production Patterns • Embedded Assets

---

<p align="center">
  <img src="https://raw.githubusercontent.com/dunamismax/gohub/main/docs/images/gopher-mage.svg" alt="Gopher Mage" width="150" />
</p>

## Quick Start

```bash
# Enterprise Go Monorepo with Security & Testing
git clone https://github.com/dunamismax/gohub.git
cd gohub && mage setup

# Start Applications
mage dev:server    # Web App with CSRF protection (Port 8080)
mage dev:tui       # Interactive TUI dashboard

# Perfect Minimal Template
git clone https://github.com/dunamismax/go-web-server.git
cd go-web-server && go generate ./... && go run ./cmd/web
```

## Technical Expertise

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=go,sqlite,docker,linux,git,github,vscode,bash" />
  </a>
</p>

**Core Stack**: Go 1.24 • Echo • Templ • HTMX • sqlc • SQLite • Bubble Tea • Mage • slog

**Specializations**:

- **Enterprise Security**: CSRF protection, XSS prevention, input validation, secure headers
- **Type-Safe Architecture**: sqlc database queries, templ templates, comprehensive error handling
- **Modern Go Stack**: Echo framework, Bubble Tea TUIs, HTMX interactions, Pico.css styling
- **Production Operations**: Single binary deployment, structured logging, database migrations
- **Monorepo Design**: Unified backend, shared infrastructure, multiple application interfaces
- **Quality Assurance**: Comprehensive testing, CI/CD pipelines, vulnerability scanning
- **Performance Optimization**: Zero dependencies, embedded assets, fast startup times
- **Developer Experience**: Mage build system, hot reloading, professional tooling

---

## Architecture Philosophy

**Security First**: Enterprise-grade CSRF protection, XSS prevention, comprehensive input validation  
**Type Safety**: sqlc-generated database code, templ templates, compile-time error prevention  
**Unified Backend**: Shared data access, configuration, and business logic across applications  
**Single Binary**: Embedded assets, zero dependencies, trivial deployment and scaling  
**Production Ready**: Structured logging, database migrations, comprehensive test coverage  
**Developer Experience**: Modern tooling, quality gates, automated workflows

---

## Application Architecture

### Enterprise Security Features

- **CSRF Protection**: Secure cookie-based tokens with proper validation
- **XSS Prevention**: HTML escaping, content security policies, input sanitization
- **Input Validation**: Length limits, UTF-8 validation, dangerous content detection
- **Secure Headers**: CORS restrictions, security-focused middleware configuration

### Modern Go Stack Components

- **Web Framework**: Echo with comprehensive middleware and type-safe routing
- **TUI Framework**: Bubble Tea with rich terminal interactions and real-time updates
- **Database Layer**: sqlc type-safe queries with SQLite for zero-dependency deployment
- **Template Engine**: Templ for compile-time HTML validation and component architecture
- **Build System**: Mage for Go-native build automation and quality assurance

---

## GitHub Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=dunamismax&show_icons=true&theme=dark&count_private=true" alt="GitHub Stats" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=dunamismax&layout=compact&theme=dark" alt="Top Languages" />
</p>

---

## Support My Work

If you find these Modern Go Stack projects valuable for building secure, high-performance web applications with type safety and single binary deployment, consider supporting continued development:

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
  <strong>Building the Future with Modern Go Architecture</strong><br>
  <sub>Go 1.24 • Echo • Templ • HTMX • sqlc • SQLite • Bubble Tea • Enterprise Security • Single Binary</sub>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/dunamismax/gohub/main/docs/images/gopher-running-jumping.gif" alt="Gopher Running and Jumping" width="400" />
</p>
