# Stephen Sawyer

I build websites and run the systems behind them. My work spans bespoke PHP
and MySQL applications, Python automation, company remote support, and the
Ubuntu infrastructure that keeps those services available.

[Website](https://dunamismax.com) ·
[Portfolio](https://dunamismax.com/projects) ·
[Contact](https://dunamismax.com/contact) ·
[Codeberg](https://codeberg.org/dunamismax)

## Selected work

### Infrastructure and support

- **[Company remote support](https://xrayservice.net)** — I self-host RustDesk's
  server and relay for company-wide remote support. The support site
  offers a preconfigured Windows client; scheduled jobs verify installer
  updates and back up the self-hosted service.
- **[Dunamis Status](https://status.dunamismax.com)** — A PHP/MySQL dashboard for
  website health, services, incidents, deployments, and repository status. A
  scheduled collector writes snapshots; the public site reads them with a
  separate, read-only database account. [Source](https://github.com/dunamismax/status.dunamismax)
- **[Server backup and recovery](https://dunamismax.com/projects#backups)** —
  Daily server and application backups, age-encrypted sensitive data, and
  documented rebuild procedures. The operational repository stays private.

### Websites

- **[dunamismax.com](https://dunamismax.com)** — This portfolio and blog,
  built with PHP, MySQL, semantic HTML, and hand-written CSS. It runs without
  JavaScript or a frontend build step. [Source](https://github.com/dunamismax/dunamismax.com)
- **[Grace & Footnotes](https://graceandfootnotes.com)** — My Christian writing
  site, with PHP/MySQL publishing, scheduled posts, RSS, and downloadable
  resources. I build and host it on my own server.
- **[Imaging Services website](https://dunamismax.com/projects#imaging-services)** —
  A twelve-page PHP/MySQL replacement for an existing WordPress site. It is
  hosted as a demo for review; the company's main website has not been cut
  over. The source is private.

### Automation

- **[MTG Card Bot](https://github.com/dunamismax/mtg-card-bot)** — A running
  Python Discord bot for Magic: The Gathering card search, pricing, legality,
  and rulings through Scryfall.
- **[Dynamic DNS automation](https://dunamismax.com/projects#dns-automation)** —
  A scheduled PHP CLI tool that updates an explicit allowlist of Cloudflare
  DNS records, with a dry-run mode for reviewing changes.

## How I work

I favor server-rendered pages, readable code, prepared SQL, and small,
purposeful dependencies. Shipping includes deployment, monitoring, backups,
and recovery documentation. I separate public read access from private
operating tools and describe demos as demos.

My working stack is PHP, MySQL, Python, HTML, CSS, Ubuntu, Caddy, Docker, and
systemd. See [Tech Stack](TECH_STACK.md) for the details.
