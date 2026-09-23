# Tech Stack

My default stack for new work. PHP is the center, MySQL is the data layer,
and the front end stays vanilla. Python handles scripting and automation.
Everything runs on an Ubuntu server I administer myself.

| Layer | Choice | Responsibility |
| --- | --- | --- |
| DNS and optional edge proxy | Cloudflare | Domain routing, edge TLS, optional protection |
| Server | Ubuntu LTS | Hosts the application, database, and files |
| Web server | Caddy | Origin HTTPS, static assets, FastCGI to PHP-FPM |
| Application | PHP 8.5, object-oriented and bespoke | Routing, rendering, application logic |
| Database | MySQL 8 | Published writing, drafts, durable records |
| Documents | Semantic HTML | Complete, accessible, server-rendered pages |
| Styling | Vanilla CSS | Responsive layout, light/dark themes, print styles |
| Enhancement | Vanilla JavaScript | Small, local, deferred, and only when a feature needs it |

```text
Reader → Cloudflare DNS → Ubuntu → Caddy → PHP-FPM → PHP → MySQL
                                        ↳ static CSS and assets as files
```

## The rule

A site sends zero JavaScript unless a concrete feature needs it. No framework,
ORM, CMS, Composer dependency, npm project, frontend build step, external font,
analytics script, CDN, or hosted content service. Add a dependency only when a
concrete need justifies its lifetime cost. Application code, data, files, and
backups stay on infrastructure I control.

## PHP application layer

- `public/index.php` front controller as the only web entry point, with a
  small `bootstrap.php` autoloader
- Readable classes in `app/`, plain-PHP templates in `views/` that escape
  every value they print
- Prepared statements through PDO; no ORM
- Correct status codes, content types, canonical URLs, and security headers
- CLI tools in `bin/` for schema, publishing, and checks
- `php -l` on every file and dependency-free tests in `tests/run.php`; no
  PHPUnit
- Local development with `php -S` and a small `dev/router.php`

## MySQL data layer

- One database per site on 127.0.0.1
- Explicit schema in `database/schema.sql`
- Least-privilege accounts: the website reads, a separate writer publishes
- Drafts and future-dated records filtered by one shared visibility rule
- Scheduled `mysqldump` backups with checksums and restore checks

## Front end

- Semantic, accessible HTML rendered on the server
- Hand-written, responsive CSS with system fonts and
  `prefers-color-scheme` themes
- Pages work fully without JavaScript; any enhancement is local and deferred

## Operations

- Ubuntu LTS on a single server until scale proves otherwise
- Caddy for HTTPS, static files, and FastCGI
- One system user and one PHP-FPM pool per site, on a private Unix socket
  with `clear_env`
- Secrets in root-owned environment files outside the repo and web root
- Versioned releases in `/srv/www/<domain>/releases/<commit>` behind a
  `current` symlink, so rollback is one symlink swap
- systemd services and timers for backups and scheduled jobs
- Idempotent root scripts that back up what they change, validate config
  before reloading, and print verification and rollback steps
- Key-only SSH kept off the public internet, fail2ban, and unattended
  security updates
- Logs and health checks before dashboards

## Scripting and automation

- Python 3.13+ with `uv`, project-local virtual environments, and a checked-in
  `pyproject.toml`
- Ruff for lint and format, pytest for tests, Pyright when typing reduces risk
- Small, focused libraries such as `httpx` only when they earn their place
- Bash and zsh for deploy and server glue; PowerShell for Windows
  administration
- macOS for local work
