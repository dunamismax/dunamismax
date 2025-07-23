<p align="center">
  <img src="https://github.com/dunamismax/images/blob/main/sveltekit-wallpaper.png" alt="SvelteKit Developer Logo" width="600" />
</p>

<p align="center">
  <a href="https://github.com/dunamismax">
    <img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&size=24&pause=1000&color=ff3e00&center=true&vCenter=true&width=1000&lines=SvelteKit+%2B+Deno+Full-Stack+Developer;Svelte+5+Runes+%2B+Modern+Reactivity;Deno+2+Runtime+%2B+Hono+Framework;shadcn%2Fui+%2B+Tailwind+CSS+v4;Superforms+%2B+Zod+Validation;PostgreSQL+%2B+Drizzle+ORM;JWT+Authentication+%2B+Security;Full-Stack+Type+Safety;Docker+%2B+Self-Hosted+Deploy;Monorepo+%2B+Shared+Packages;4-Step+Development+Setup;Zero+Configuration+Required;Production-Ready+Templates;Hot+Module+Replacement;TypeScript+%2B+ESLint+Ready" alt="Typing SVG" />
  </a>
</p>

<p align="center">
  <a href="https://kit.svelte.dev/"><img src="https://img.shields.io/badge/SvelteKit-2.25.1+-ff3e00.svg?logo=svelte" alt="SvelteKit Version"></a>
  <a href="https://svelte.dev/"><img src="https://img.shields.io/badge/Svelte-5.0+-ff3e00.svg?logo=svelte" alt="Svelte Version"></a>
  <a href="https://deno.com/"><img src="https://img.shields.io/badge/Deno-2.4.0+-000000.svg?logo=deno" alt="Deno Version"></a>
  <a href="https://hono.dev/"><img src="https://img.shields.io/badge/Framework-Hono-E36002.svg" alt="Hono Framework"></a>
  <a href="https://www.shadcn-svelte.com/"><img src="https://img.shields.io/badge/UI-shadcn%2Fui-000000.svg" alt="shadcn/ui"></a>
  <a href="https://tailwindcss.com/"><img src="https://img.shields.io/badge/CSS-Tailwind_v4-06B6D4.svg?logo=tailwindcss" alt="Tailwind CSS"></a>
  <a href="https://www.postgresql.org/"><img src="https://img.shields.io/badge/Database-PostgreSQL-336791.svg?logo=postgresql" alt="PostgreSQL"></a>
</p>

---

## About

**Full-stack developer** specializing in **modern SvelteKit applications** with **Deno backends**. I create production-ready templates that combine the latest web technologies with pragmatic architecture, emphasizing developer experience, type safety, and rapid deployment.

**Philosophy**: Modern web development should be simple yet powerful. My projects showcase cutting-edge patterns - Svelte 5 runes, Deno 2 runtime, shadcn/ui components, full-stack TypeScript, and zero-configuration setups - all deployable with Docker in minutes.

---

## Featured Project

### **[SvelteKit + Deno Monorepo Template](https://github.com/dunamismax/svelte)**

<p align="center">
  <a href="https://github.com/dunamismax/svelte">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=dunamismax&repo=svelte&theme=dark&show_owner=true" alt="svelte-template" />
  </a>
</p>

**Complete full-stack template** combining SvelteKit frontend, Deno API backend, and shared packages in a monorepo architecture. Perfect for rapid development of modern web applications with type safety, performance, and developer experience in mind.

**Tech Stack:** SvelteKit 5 + Deno 2 + Hono + shadcn/ui + Tailwind v4 + PostgreSQL + Drizzle ORM  
**Architecture:** Monorepo • Shared Packages • Full-Stack Type Safety • Zero Configuration  
**Security:** JWT Authentication • Input Validation • SQL Injection Prevention • CORS Protection  
**Developer Experience:** Hot Reload • 4-Step Setup • Database Studio • Docker Support

**Key Features:**

- **Svelte 5 Runes**: Modern reactivity and component patterns
- **Deno 2 Runtime**: Secure, modern JavaScript/TypeScript execution
- **shadcn/ui Integration**: Beautiful, accessible UI components
- **PostgreSQL + Drizzle**: Real database with type-safe queries
- **Superforms + Zod**: Enhanced form handling with validation
- **Docker Ready**: Development and production deployment
- **Monorepo Structure**: Shared packages for maximum code reuse

---

<p align="center">
  <img src="https://github.com/dunamismax/images/blob/main/TS-logo.png" alt="TypeScript" width="200" />
</p>

## Quick Start

```bash
# Clone the complete SvelteKit + Deno template
git clone https://github.com/dunamismax/svelte.git
cd svelte

# 4-step setup - everything works out of the box
pnpm install                              # Install dependencies
docker-compose up -d                      # Start PostgreSQL database
pnpm --filter sveltekit-template db:push  # Run database migrations
pnpm dev                                  # Start development servers

# Open and develop
# Frontend: http://localhost:5173
# API: http://localhost:8000
# Database Studio: pnpm --filter sveltekit-template db:studio
```

## Development Workflow

The template includes comprehensive tooling for modern development:

```bash
# Development Commands
pnpm dev                              # Start all development servers
pnpm build                            # Build all applications
pnpm lint                             # Lint and format code
pnpm --filter api type-check          # TypeScript checking for Deno API
pnpm --filter sveltekit-template build # Build SvelteKit app

# Database Operations
docker-compose up -d                  # Start PostgreSQL database
pnpm --filter sveltekit-template db:push   # Update database schema
pnpm --filter sveltekit-template db:studio # Open Drizzle Studio

# Add shadcn/ui Components
pnpm dlx shadcn-svelte@latest add button card input dialog

# Production Deployment
docker-compose -f docker-compose.prod.yml up -d --build
```

## Technical Stack

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=svelte,typescript,deno,nodejs,postgres,docker,tailwind,vite" />
  </a>
</p>

**Frontend Stack**: SvelteKit 5 • Svelte 5 Runes • shadcn/ui • Tailwind CSS v4 • Superforms • Vite  
**Backend Stack**: Deno 2 • Hono Framework • JWT Auth • PostgreSQL • Drizzle ORM  
**DevOps Stack**: Docker • pnpm Workspaces • TypeScript • ESLint • Prettier

**Focus Areas**:

- **Modern Reactivity**: Svelte 5 runes for intuitive state management and component logic
- **Type Safety**: Full-stack TypeScript with shared validation schemas and database types
- **UI Excellence**: shadcn/ui components with Tailwind CSS v4 for beautiful, accessible interfaces
- **Backend Performance**: Deno 2 runtime with Hono framework for lightning-fast API responses
- **Database Integration**: PostgreSQL with Drizzle ORM for type-safe, real database operations
- **Developer Experience**: Hot reload, 4-step setup, comprehensive tooling, zero configuration
- **Production Ready**: Docker deployment, environment management, security best practices
- **Monorepo Architecture**: Shared packages for UI, validation, and database utilities

---

## GitHub Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=dunamismax&show_icons=true&theme=dark&count_private=true" alt="GitHub Stats" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=dunamismax&layout=compact&theme=dark" alt="Top Languages" />
</p>

---

## Support My Work

If you find this **SvelteKit + Deno template** useful for building **modern web applications** with **full-stack type safety** and **rapid deployment**, consider supporting continued development:

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
  <strong>Building Modern Web Applications with SvelteKit + Deno</strong><br>
  <sub>SvelteKit 5 • Deno 2 • shadcn/ui • Tailwind v4 • PostgreSQL • Full-Stack Type Safety • Zero Configuration</sub>
</p>

<p align="center">
  <img src="https://github.com/dunamismax/images/blob/main/svelte-white-hires-logo.jpeg" alt="Svelte Logo" width="400" />
</p>
