<p align="center">
  <img src="https://github.com/dunamismax/images/blob/main/golang/go-logo.png" alt="Go and JavaScript Developer" width="400" />
</p>

<p align="center">
  <a href="https://github.com/dunamismax">
    <img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&size=24&pause=1000&color=00ADD8&center=true&vCenter=true&width=1000&lines=Go+%2B+JavaScript+Developer;The+Modern+Go+Stack+Creator;Echo+v4+%2B+Templ+%2B+HTMX+Expert;Production-Ready+Go+Applications;flare-router+3.4kB+JavaScript+Router;Type-Safe+SQL+with+SQLC;Pure+Go+SQLite+Applications;Lightning-Fast+SPA+Navigation;Zero+Configuration+Setup;Single+Binary+Deployment;Hot+Reload+%2B+Mage+Build;Structured+Logging+with+slog;Modern+Web+Architectures;Enterprise+Grade+Solutions" alt="Typing SVG" />
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

**Go and JavaScript developer** specializing in **The Modern Go Stack** and **ultra-lightweight frontend solutions**. I build production-ready applications using Echo v4, Templ, HTMX, and type-safe SQL, plus 3.4kB JavaScript routers that transform static sites into blazingly fast SPAs. My projects deliver single binary deployments with zero external dependencies and maximum performance control.

**Philosophy**: Modern web development needs both robust backend architectures and lightweight frontend solutions. Go provides enterprise-grade reliability while vanilla JavaScript delivers unmatched performance control.

---

## Featured Projects

### **[The Modern Go Stack - Web Server Template](https://github.com/dunamismax/go-web-server)**

<p align="center">
  <a href="https://github.com/dunamismax/go-web-server">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=dunamismax&repo=go-web-server&theme=dark&show_owner=true" alt="go-web-server" />
  </a>
</p>

**Production-ready Go web application template** featuring Echo v4, Templ, HTMX 2.x, and Pico.css with type-safe SQL using SQLC and pure Go SQLite driver. Creates single, self-contained binaries (~11MB) with zero external dependencies, structured logging with slog, and comprehensive development tooling.

**Tech Stack:** Echo v4 • Templ • HTMX 2.x • Pico.css v2 • SQLC • SQLite • Pure Go Driver  
**Architecture:** Type-Safe SQL • Structured Logging • Single Binary Deployment • Zero CGO Dependencies  
**Developer Experience:** Hot Reload with Air • Mage Build Automation • Database Migrations with Goose  
**Production Features:** Security Middleware • Rate Limiting • Graceful Shutdown • Multi-Source Configuration

### **[flare-router 🔥](https://github.com/dunamismax/flare-router)**

<p align="center">
  <a href="https://github.com/dunamismax/flare-router">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=dunamismax&repo=flare-router&theme=dark&show_owner=true" alt="flare-router" />
  </a>
</p>

**Lightning-fast 3.4kB router** and intelligent prefetcher that makes static sites feel like blazingly fast SPAs. Transform any multi-page website into a lightning-fast experience without framework overhead. Zero configuration, intelligent prefetching with IntersectionObserver, and seamless navigation.

**Key Features:** 3.4kB Bundle Size • Zero Configuration • Intelligent Link Prefetching • SPA-like Navigation • State Preservation  
**Architecture:** IntersectionObserver API • Fetch API • History API • Modern Browser APIs  
**Compatibility:** Framework Agnostic • Static Sites • Server-Rendered Apps • Astro Compatible  
**Developer Experience:** Drop-in Solution • Event Handling • Programmatic Navigation • Progress Tracking

---

<p align="center">
  <img src="https://github.com/dunamismax/images/blob/main/golang/gopher-mage.svg" alt="Go Gopher" width="150" />
</p>

## Quick Start

### The Modern Go Stack - Production-Ready in 4 Steps

```bash
# Clone and setup Go web server
git clone https://github.com/dunamismax/go-web-server.git
cd go-web-server && go mod tidy

# Install development tools and dependencies
mage setup

# Start development server with hot reload
mage dev

# Server starts at http://localhost:8080 with full CRUD demo
```

### flare-router - Get SPA Navigation in 3 Steps

```bash
# 1. Install flare-router
npm install flare-router

# 2. Import and initialize
import flare from 'flare-router';
const router = flare({ prefetch: 'visible', log: true });

# 3. That's it! Your static site now feels blazingly fast
```

**Example Implementation:**

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My Fast Site</title>
  </head>
  <body>
    <nav>
      <a href="/">Home</a>
      <a href="/about">About</a>
      <a href="/contact">Contact</a>
    </nav>
    <main><!-- Your content --></main>
    <script type="module">
      import flare from "flare-router";
      const router = flare({ prefetch: "visible", log: true });
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

**Go Backend Stack**: Echo v4 • Templ • HTMX 2.x • SQLC • SQLite • Pure Go Driver • slog Logging  
**JavaScript Frontend Stack**: flare-router • Vanilla ES Modules • IntersectionObserver API • Fetch API • History API  
**Build & DevOps Stack**: Mage Build Automation • Air Hot Reload • Goose Migrations • Docker • Linux • GitHub Actions  
**Development Stack**: Type-Safe SQL • Structured Logging • Single Binary Deployment • Zero Dependencies

**Architecture Philosophy**:

- **The Modern Go Stack**: Production-ready web applications with Echo v4, Templ, HTMX, and type-safe SQL
- **Single Binary Deployment**: Self-contained applications (~11MB) with zero external dependencies
- **Ultra-Lightweight Frontend**: 3.4kB JavaScript router that transforms static sites into blazingly fast SPAs
- **Type-Safe Development**: SQLC for database queries, Templ for HTML components, structured logging
- **Zero Configuration**: Drop-in solutions that work immediately with intelligent defaults
- **Developer Experience**: Hot reload, build automation, comprehensive tooling, modern workflows

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

**The Modern Go Stack:**

- **Single Binary Deployment** - Self-contained applications (~11MB) with zero external dependencies
- **Type-Safe SQL** - SQLC generates Go code from SQL queries with compile-time safety
- **Hot Reload Development** - Air for instant server restart, Mage for build automation
- **Production Security** - Rate limiting, CORS, secure headers, graceful shutdown middleware
- **Pure Go SQLite** - Zero CGO dependencies with modernc.org/sqlite driver

**flare-router Features:**

- **3.4kB Bundle Size** - Ultra-lightweight router with zero configuration setup
- **Intelligent Prefetching** - IntersectionObserver-based link prefetching for instant navigation
- **SPA-like Navigation** - Transform static sites into blazingly fast single-page experiences
- **Framework Agnostic** - Drop-in solution compatible with any website architecture
- **State Preservation** - Long-lived JavaScript behaviors between navigations

---

## Support My Work

If you find **The Modern Go Stack** and **flare-router** useful for building **production-ready applications**, consider supporting continued development:

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
  <strong>The Modern Go Stack • flare-router • Production-Ready Web Applications</strong><br>
  <sub>Echo v4 • Templ • HTMX 2.x • SQLC • SQLite • 3.4kB Router • Type-Safe SQL • Single Binary Deployment • Zero Dependencies • Ultra-Lightweight Solutions</sub>
</p>

<p align="center">
  <img src="https://github.com/dunamismax/images/blob/main/golang/gopher-running-jumping.gif" alt="Go Gopher" width="600" />
</p>
