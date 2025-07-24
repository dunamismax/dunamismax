<p align="center">
  <img src="https://github.com/dunamismax/images/blob/main/Vanilla-JS-Logo.png" alt="flare-router Creator" width="200" />
</p>

<p align="center">
  <a href="https://github.com/dunamismax">
    <img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&size=24&pause=1000&color=FF6B35&center=true&vCenter=true&width=1000&lines=flare-router+Creator+%2B+3.4kB+Bundle;Lightning-Fast+SPA+Navigation;Zero+Configuration+Setup;Intelligent+Link+Prefetching;Static+Sites+Feel+Like+SPAs;Full-Stack+JavaScript+Developer;Vanilla+JavaScript+%2B+Node.js+Expert;Modern+Monorepo+Architectures;Production-Ready+Web+Applications;Fastify+%2B+MongoDB+Backend;VineJS+Validation+%2B+Security;pnpm+Workspaces+%2B+ES+Modules;Zero+Framework+Dependencies;Maximum+Performance+Control;Enterprise+Grade+Architecture" alt="Typing SVG" />
  </a>
</p>

<p align="center">
  <a href="https://github.com/dunamismax/flare-router"><img src="https://img.shields.io/badge/flare_router-3.4kB-FF6B35.svg" alt="flare-router"></a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript"><img src="https://img.shields.io/badge/Vanilla_JS-ES2020+-F7DF1E.svg?logo=javascript" alt="Vanilla JavaScript"></a>
  <a href="https://nodejs.org/"><img src="https://img.shields.io/badge/Node.js-18+-339933.svg?logo=node.js" alt="Node.js Version"></a>
  <a href="https://fastify.dev/"><img src="https://img.shields.io/badge/Fastify-4.29+-000000.svg?logo=fastify" alt="Fastify Version"></a>
  <a href="https://www.mongodb.com/"><img src="https://img.shields.io/badge/MongoDB-6.18+-47A248.svg?logo=mongodb" alt="MongoDB Version"></a>
  <a href="https://pnpm.io/"><img src="https://img.shields.io/badge/Package_Manager-pnpm-F69220.svg?logo=pnpm" alt="pnpm"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="MIT License"></a>
</p>

---

## About

**Creator of flare-router** and **full-stack JavaScript developer** specializing in **ultra-lightweight solutions** and **production-ready monorepo architectures**. I build high-performance web applications with 3.4kB routers that transform static sites into SPAs, vanilla frontends with intelligent prefetching, and modern backends - all deployable with minimal overhead and maximum performance control.

**Philosophy**: Modern web development doesn't need heavy frameworks. My projects showcase pure JavaScript patterns that prioritize speed, simplicity, and developer control.

---

## Featured Projects

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

### **[Full-Stack Vanilla JavaScript Monorepo](https://github.com/dunamismax/javascript)**

<p align="center">
  <a href="https://github.com/dunamismax/javascript">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=dunamismax&repo=javascript&theme=dark&show_owner=true" alt="javascript-monorepo" />
  </a>
</p>

**Production-ready JavaScript monorepo** featuring vanilla HTML, CSS, and JavaScript frontend with Node.js, Fastify, and MongoDB backend. Built with shared utilities, modern tooling, and complete production deployment configurations. Showcases flare-router integration for SPA-like navigation across real applications.

**Tech Stack:** Vanilla JS + Node.js + Fastify + MongoDB + flare-router + VineJS Validation  
**Architecture:** pnpm Workspaces • Shared Packages • ES Modules • Zero Framework Overhead  
**Applications:** Todo List with Analytics + Weather Dashboard with OpenWeatherMap API  
**Developer Experience:** esbuild Bundling • Hot Reload • 4-Step Setup • systemd + Caddy Deploy

---

<p align="center">
  <img src="https://github.com/dunamismax/images/blob/main/JavaScript-logo.png" alt="JavaScript" width="100" />
</p>

## Quick Start

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

### Full-Stack JavaScript Monorepo

```bash
# Clone and get running in 4 steps
git clone https://github.com/dunamismax/javascript.git
cd javascript && pnpm install

# Configure environment
cp apps/todo-list/.env.example apps/todo-list/.env
cp apps/weather/.env.example apps/weather/.env
# Edit .env files with your MongoDB URI and OpenWeatherMap API key

# Build and start (includes flare-router)
pnpm build && pnpm dev

# Access: Todo List at http://localhost:3001, Weather at http://localhost:3000
```

## Technical Stack

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=js,nodejs,mongodb,html,css,vite,git,linux" />
  </a>
</p>

**Router Stack**: Vanilla JavaScript ES Modules • IntersectionObserver API • Fetch API • History API • esbuild  
**Frontend Stack**: flare-router • CSS Design System • Intelligent Prefetching • State Preservation  
**Backend Stack**: Node.js 18+ • Fastify • MongoDB Native Driver • VineJS Validation • REST APIs  
**DevOps Stack**: pnpm Workspaces • ESLint • Prettier • Linux • systemd • Caddy • GitHub Actions

**Architecture Philosophy**:

- **Ultra-Lightweight Solutions**: 3.4kB router that transforms static sites into blazingly fast SPAs
- **Zero Framework Dependencies**: Pure JavaScript solutions with maximum performance control
- **Intelligent Performance**: Smart prefetching, SPA-like navigation, modern browser APIs
- **Production Ready**: Environment management, security best practices, deployment automation
- **Framework Agnostic**: Drop-in solutions that work with any website architecture
- **Developer Experience**: Zero config setup, comprehensive tooling, modern workflows

---

## GitHub Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=dunamismax&show_icons=true&theme=dark&count_private=true" alt="GitHub Stats" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=dunamismax&layout=compact&theme=dark" alt="Top Languages" />
</p>

---

<p align="center">
  <img src="https://github.com/dunamismax/images/blob/main/js-evolution-wallpaper.jpg" alt="JavaScript Evolution" width="450" />
</p>

## Key Features

**flare-router Features:**

- **3.4kB Bundle Size** - Ultra-lightweight router with zero configuration setup
- **Intelligent Prefetching** - IntersectionObserver-based link prefetching for instant navigation
- **SPA-like Navigation** - Transform static sites into blazingly fast single-page experiences
- **Framework Agnostic** - Drop-in solution compatible with any website architecture
- **State Preservation** - Long-lived JavaScript behaviors between navigations

**Full-Stack Applications:**

- **Todo List with Analytics** - Full CRUD operations, MongoDB backend, real-time analytics dashboard
- **Weather Dashboard** - OpenWeatherMap integration, server-side proxy, responsive design
- **Lightning-Fast Navigation**: flare-router for instant page transitions without full reloads
- **Enterprise Security**: VineJS validation, XSS protection, OWASP-compliant headers

---

## Support My Work

If you find **flare-router** and these **production-ready JavaScript monorepos** useful for building **blazingly fast applications**, consider supporting continued development:

<p align="center">
  <a href="https://buymeacoffee.com/dunamismax" target="_blank">
    <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" />
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
  <strong>flare-router • Production-Ready JavaScript Monorepos</strong><br>
  <sub>3.4kB Router • Lightning-Fast SPA Navigation • Full-Stack Vanilla JavaScript • Fastify • MongoDB • VineJS • pnpm Workspaces • Zero Framework Dependencies • Ultra-Lightweight Solutions</sub>
</p>

<p align="center">
  <img src="https://github.com/dunamismax/images/blob/main/js-coffee-particles.jpg" alt="JavaScript Coffee" width="450" />
</p>
