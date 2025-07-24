<p align="center">
  <img src="https://github.com/dunamismax/images/blob/main/golang/go-logo.png" alt="Go and JavaScript Developer" width="400" />
</p>

<p align="center">
  <a href="https://github.com/dunamismax">
    <img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&size=24&pause=1000&color=00ADD8&center=true&vCenter=true&width=1200&lines=Go+%2B+JavaScript+Developer;The+Modern+Go+Stack+Creator;Echo+v4+Framework+with+Type-Safe+SQL;HTMX+2.x+Dynamic+UX+without+JavaScript+Overhead;SQLC+Generated+Queries+with+Pure+Go+SQLite;CSRF+Protection+and+Input+Sanitization;Single+Binary+Deployment+at+11MB;flare-router+3.4kB+Zero-Config+Router;Lightning-Fast+SPA+Navigation+Experience;Intelligent+Link+Prefetching+System;Static+Sites+Feel+Like+Blazing+SPAs;Zero+External+Dependencies+Architecture;Enterprise+Security+Middleware+Stack;Structured+Error+Handling+and+Logging;Hot+Reload+Development+with+Mage+Automation;Production-Ready+Go+Web+Applications" alt="Typing SVG" />
  </a>
</p>

<p align="center">
  <a href="https://golang.org/"><img src="https://img.shields.io/badge/Go-1.24+-00ADD8.svg?logo=go" alt="Go Version"></a>
  <a href="https://github.com/dunamismax/go-web-server"><img src="https://img.shields.io/badge/Echo-v4-00ADD8.svg?logo=go" alt="Echo Framework"></a>
  <a href="https://github.com/dunamismax/flare-router"><img src="https://img.shields.io/badge/flare_router-3.4kB-FF6B35.svg" alt="flare-router"></a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript"><img src="https://img.shields.io/badge/Vanilla_JS-ES2020+-F7DF1E.svg?logo=javascript" alt="Vanilla JavaScript"></a>
  <a href="https://templ.guide/"><img src="https://img.shields.io/badge/Templates-Templ-00ADD8.svg?logo=go" alt="Templ"></a>
  <a href="https://htmx.org/"><img src="https://img.shields.io/badge/Frontend-HTMX_2.x-3D72D7.svg?logo=htmx" alt="HTMX"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="MIT License"></a>
</p>

---

## About

**Go and JavaScript developer** specializing in **The Modern Go Stack** and **ultra-lightweight frontend solutions**. I build production-ready web applications using Echo v4, Templ, HTMX, and type-safe database operations with SQLC, plus 3.4kB JavaScript routers that transform static sites into lightning-fast SPAs. My projects emphasize enterprise-grade security, single binary deployments, and zero external dependencies.

**Philosophy**: Modern web development needs both robust backend architectures and ultra-lightweight frontend solutions. Go provides enterprise-grade reliability with compile-time safety, while vanilla JavaScript delivers unmatched performance control without framework bloat.

---

## Featured Projects

### **[The Modern Go Stack - Web Server Template](https://github.com/dunamismax/go-web-server)**

<p align="center">
  <a href="https://github.com/dunamismax/go-web-server">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=dunamismax&repo=go-web-server&theme=dark&show_owner=true" alt="go-web-server" />
  </a>
</p>

**Production-ready Go web application template** featuring the complete Modern Go Stack with Echo v4 framework, type-safe Templ templates, HTMX 2.x dynamic interactions, and comprehensive security middleware. Uses SQLC for type-safe database queries with a pure Go SQLite driver, creating self-contained 11MB binaries with zero CGO dependencies.

**Security Features:** Custom CSRF Protection • Input Sanitization Middleware • Security Headers Stack • Rate Limiting • Structured Error Handling  
**Database Layer:** SQLC Type-Safe Queries • Pure Go SQLite Driver • Database Migrations with Goose • Zero CGO Dependencies  
**Development Experience:** Hot Reload with Air • Mage Build Automation • Quality Checks Pipeline • Vulnerability Scanning  
**Production Ready:** Single Binary Deployment • Graceful Shutdown • Multi-Source Configuration • Request Tracing • Structured Logging

### **[flare-router](https://github.com/dunamismax/flare-router)**

<p align="center">
  <a href="https://github.com/dunamismax/flare-router">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=dunamismax&repo=flare-router&theme=dark&show_owner=true" alt="flare-router" />
  </a>
</p>

**Ultra-lightweight 3.4kB router** and intelligent prefetcher that transforms static sites into blazingly fast SPAs without framework overhead. Features zero-configuration setup, IntersectionObserver-based intelligent prefetching, and seamless client-side navigation while preserving JavaScript state between page transitions.

**Core Features:** 3.4kB Gzipped Bundle • Zero Configuration Setup • Intelligent Link Prefetching • SPA-like Navigation • State Preservation  
**Modern APIs:** IntersectionObserver • Fetch API • History API • DOM Manipulation • Event Handling System  
**Framework Agnostic:** Static Sites • Server-Rendered Apps • Jekyll • Hugo • Astro Compatible • Drop-in Solution  
**Developer Experience:** Progress Tracking • Event System • Programmatic Navigation • Debug Logging • Graceful Fallbacks

---

<p align="center">
  <img src="https://github.com/dunamismax/images/blob/main/golang/gopher-mage.svg" alt="Go Gopher" width="150" />
</p>

## Quick Start

### The Modern Go Stack - Production-Ready in 4 Steps

```bash
# Clone and setup Go web server template
git clone https://github.com/dunamismax/go-web-server.git
cd go-web-server && go mod tidy

# Install development tools and dependencies
mage setup

# Start development server with hot reload
mage dev

# Server starts at http://localhost:8080 with interactive user management demo
```

### flare-router - Lightning-Fast Navigation in 3 Steps

```bash
# 1. Install flare-router
npm install flare-router

# 2. Import and initialize with intelligent prefetching
import flare from 'flare-router';
const router = flare({ prefetch: 'visible', log: true });

# 3. That's it! Your static site now has SPA-like navigation
```

**Complete Implementation Example:**

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Lightning Fast Site</title>
  </head>
  <body>
    <nav>
      <a href="/">Home</a>
      <a href="/about">About</a>
      <a href="/products">Products</a>
      <a href="/contact">Contact</a>
    </nav>
    <main><!-- Your content loads instantly --></main>
    <script type="module">
      import flare from "flare-router";
      const router = flare({
        prefetch: "visible",
        log: true,
        pageTransitions: false,
      });
    </script>
  </body>
</html>
```

## Technical Stack

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=go,js,html,css,sqlite,docker,linux,git" />
  </a>
</p>

**Go Backend Stack**: Echo v4 Framework • Type-Safe Templ Templates • HTMX 2.x Dynamic UX • SQLC Generated Queries • Pure Go SQLite • Structured slog Logging  
**JavaScript Frontend Stack**: flare-router 3.4kB Bundle • Vanilla ES Modules • IntersectionObserver API • Fetch API • History API • Zero Dependencies  
**Security & Middleware**: Custom CSRF Protection • Input Sanitization • Security Headers • Rate Limiting • Request Tracing • Error Handling  
**Build & DevOps Stack**: Mage Build Automation • Air Hot Reload • Goose Database Migrations • Quality Checks • Vulnerability Scanning

**Architecture Philosophy**:

- **The Modern Go Stack**: Enterprise-grade web applications with Echo v4, type-safe Templ templates, HTMX dynamic interactions, and SQLC database queries
- **Single Binary Deployment**: Self-contained 11MB applications with embedded assets and zero external dependencies
- **Ultra-Lightweight Frontend**: 3.4kB zero-config router that transforms static sites into lightning-fast SPAs with intelligent prefetching
- **Type-Safe Development**: SQLC for compile-time SQL safety, Templ for type-safe HTML components, structured logging with context
- **Zero Configuration Philosophy**: Drop-in solutions with intelligent defaults that work immediately without complex setup
- **Security-First Design**: Enterprise security middleware stack with CSRF protection, input sanitization, and structured error handling
- **Developer Experience Focus**: Hot reload, build automation, comprehensive tooling, quality checks, and modern development workflows

---

## GitHub Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=dunamismax&show_icons=true&theme=dark&count_private=true" alt="GitHub Stats" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=dunamismax&layout=compact&theme=dark" alt="Top Languages" />
</p>

---

<p align="center">
  <img src="https://github.com/dunamismax/images/blob/main/golang/gopher-aviator.jpg" alt="Go Gopher" width="400" />
</p>

## Key Features

**The Modern Go Stack Enterprise Features:**

- **Single Binary Deployment** - Self-contained 11MB applications with embedded Pico.css, HTMX, Templ templates, and SQLite database
- **Enterprise Security Stack** - Custom CSRF protection, input sanitization, security headers, rate limiting, and structured error handling
- **Type-Safe Database Layer** - SQLC generates Go code from SQL queries with compile-time safety and zero reflection overhead
- **Hot Reload Development** - Air for instant server restart, Mage for build automation, comprehensive quality checks pipeline
- **Pure Go Architecture** - Zero CGO dependencies with modernc.org/sqlite driver, cross-platform compilation support
- **Production Monitoring** - Request tracing, structured logging with slog, graceful shutdown, multi-source configuration management

**flare-router Lightning Features:**

- **3.4kB Gzipped Bundle** - Ultra-lightweight router with zero configuration setup and immediate functionality
- **Intelligent Prefetching System** - IntersectionObserver-based link prefetching for instant page transitions and optimal performance
- **SPA-like Navigation Experience** - Transform static sites into blazingly fast single-page applications without framework overhead
- **Framework Agnostic Design** - Drop-in solution compatible with static sites, Jekyll, Hugo, Astro, and server-rendered applications
- **State Preservation Architecture** - Long-lived JavaScript behaviors and application state maintained between page navigations
- **Modern Browser APIs** - Built with IntersectionObserver, Fetch API, History API for optimal performance and compatibility

---

## Support My Work

If you find **The Modern Go Stack** and **flare-router** valuable for building **production-ready web applications** with enterprise security and lightning-fast performance, consider supporting continued development:

<p align="center">
  <a href="https://buymeacoffee.com/dunamismax" target="_blank">
    <img src="https://github.com/dunamismax/images/blob/main/golang/buy-coffee-go.gif" alt="Buy Me A Coffee" style="height: 150px !important;" />
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
  <strong>The Modern Go Stack • flare-router • Enterprise Web Applications</strong><br>
  <sub>Echo v4 • Templ • HTMX 2.x • SQLC • Pure Go SQLite • 3.4kB Router • Type-Safe SQL • Single Binary • Zero Dependencies • Lightning Performance</sub>
</p>

<p align="center">
  <img src="https://github.com/dunamismax/images/blob/main/golang/gopher-running-jumping.gif" alt="Go Gopher" width="600" />
</p>
