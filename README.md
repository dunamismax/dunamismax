# Stephen Sawyer

I build websites, write automation, and run the systems behind them. My work
includes Astro and TypeScript applications, PostgreSQL publishing systems,
Python tools, and self-hosted Ubuntu infrastructure.

[Website](https://dunamismax.com) ·
[Portfolio](https://dunamismax.com/projects) ·
[Contact](https://dunamismax.com/contact) ·
[Codeberg](https://codeberg.org/dunamismax)

## Selected work

### Websites

- **[dunamismax.com](https://dunamismax.com)** — My portfolio and blog, built
  with Astro, strict TypeScript, and PostgreSQL. Static pages sit alongside
  database-backed publishing; the browser receives no JavaScript.
  [Source](https://github.com/dunamismax/dunamismax.com)
- **[Grace & Footnotes](https://graceandfootnotes.com)** — My Christian writing
  site, with scheduled publishing, RSS, and downloadable resources. I build
  and host its Astro and PostgreSQL application on my own server.
- **[Imaging Services website](https://dunamismax.com/projects#imaging-services)** —
  A twelve-page Astro and PostgreSQL replacement for an existing WordPress
  site. It is hosted as a demo for review; the company's main website has
  not been cut over. The source remains private.

### Infrastructure and automation

- **[Company remote support](https://xrayservice.net)** — I operate RustDesk's
  self-hosted server and relay for company-wide support. A static Astro site
  distributes a preconfigured Windows client, with scheduled installer
  verification and service backups.
- **[Dunamis Status](https://status.dunamismax.com)** — An Astro and PostgreSQL
  dashboard for website health, services, incidents, deployments, and
  repository status. A TypeScript collector records snapshots separately
  from the read-only public application.
  [Source](https://github.com/dunamismax/status.dunamismax)
- **[Server backup and recovery](https://dunamismax.com/projects#backups)** —
  Automated database and configuration backups, age-encrypted off-site
  snapshots, isolated PostgreSQL restore verification, and documented
  rebuild procedures. The operational repository stays private.
- **[MTG Card Bot](https://github.com/dunamismax/mtg-card-bot)** — A running
  Python Discord bot for Magic: The Gathering card search, pricing, legality,
  and rulings through Scryfall.
- **[Dynamic DNS automation](https://dunamismax.com/projects#dns-automation)** —
  A scheduled TypeScript tool that updates an explicit allowlist of
  Cloudflare DNS records, with a dry-run mode for reviewing changes.

## How I work

I favor semantic HTML, hand-written CSS, parameterized SQL, and small,
purposeful dependencies. I prerender stable pages and use server rendering
where content needs to change at request time. Reading works without
JavaScript; local scripts add small enhancements where useful.

Deployment, monitoring, backups, and recovery are part of the work. Public
applications use restricted service identities and database access; publishing
and administration stay separate.

See [Tech Stack](TECH_STACK.md) for the tools and practices behind these projects.
