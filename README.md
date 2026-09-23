# Stephen Sawyer

PHP developer and Linux systems administrator. I build bespoke,
object-oriented PHP on MySQL with semantic HTML and hand-written CSS, script
the routine work in Python, and run the Ubuntu servers it all lives on.

[dunamismax.com](https://dunamismax.com) ·
[Contact](https://dunamismax.com/contact) ·
[Codeberg](https://codeberg.org/dunamismax) ·
[Status](https://status.dunamismax.com)

## What I do

- **Web.** Bespoke PHP 8.5: a small front controller, readable classes,
  prepared SQL, and templates that render complete, accessible HTML on the
  server. Styles are hand-written and responsive. Most pages send no
  JavaScript at all.
- **Data.** MySQL for published content and durable records, with explicit
  schemas and separate read-only and writer accounts.
- **Operations.** I administer the servers my sites run on: Ubuntu LTS, Caddy
  for HTTPS, a dedicated PHP-FPM pool and system user per site, MySQL on
  localhost, systemd services and timers, backups with restore checks, and
  SSH that stays off the public internet. Deploys are versioned releases
  with a one-command rollback.
- **Scripting.** Python for automation, bots, and data cleanup, managed with
  `uv`, Ruff, and pytest. Bash for deploy and server glue, and PowerShell
  where Windows administration calls for it.

## Stack

| Layer | Choice |
| --- | --- |
| Application | PHP 8.5, object-oriented and bespoke |
| Database | MySQL 8 |
| Front end | Semantic HTML, vanilla CSS, vanilla JavaScript only when a feature needs it |
| Web server | Caddy with PHP-FPM |
| Server | Ubuntu LTS, systemd |
| DNS | Cloudflare |
| Scripting | Python (`uv`, Ruff, pytest), Bash, PowerShell |

No framework, ORM, CMS, Composer dependency, npm project, build step,
external font, analytics, or CDN unless a concrete need justifies its
lifetime cost. More detail is in [TECH_STACK.md](TECH_STACK.md).

## Projects

- [dunamismax.com](https://github.com/dunamismax/dunamismax.com): my site
  and blog. Bespoke PHP and MySQL behind Caddy, with semantic HTML,
  hand-written CSS, and zero JavaScript.
  [Live](https://dunamismax.com)
- [status.dunamismax](https://github.com/dunamismax/status.dunamismax): a
  status and operations dashboard for site health, host services, deploy
  history, and project progress across my self-hosted systems. PHP and
  MySQL, no JavaScript. [Live](https://status.dunamismax.com)
- [mtg-card-bot](https://github.com/dunamismax/mtg-card-bot): a Discord bot
  for Magic: The Gathering card lookups with live Scryfall prices, legality,
  and rulings. Python, `discord.py`, and `httpx`.
- [Toolworks](https://github.com/dunamismax/toolworks): Python automation,
  CLI helpers, and operational scripts for repeatable IT workflows.
- [LangIndex](https://github.com/dunamismax/langindex): an open reference
  for programming languages, ecosystem tradeoffs, and practical language
  selection. [Live](https://langindex.dev)

## What I care about

- **Vanilla first.** Frameworks, package managers, and build steps all carry
  a lifetime cost. I'd rather read fifty lines of my own PHP than debug
  someone else's abstraction.
- **Security as architecture.** Prepared SQL, escaped output,
  least-privilege accounts, secrets kept out of the web root and out of Git,
  and trust boundaries decided before the first line of code.
- **Ownership.** Software that runs on hardware you control, with data you
  can inspect, back up, restore, and move.
- **Explicit data.** If you can't trace a value through the system, the
  system is too clever.
- **Operational discipline.** Iterate, but keep only the complexity that has
  earned its place.

Code lives on GitHub and mirrors to
[Codeberg](https://codeberg.org/dunamismax).

## License

Repository content is [MIT](LICENSE) unless an individual project says
otherwise.
