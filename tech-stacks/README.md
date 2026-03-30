# Tech Stacks

**Opinionated stack guidance for active work across Stephen Sawyer's repos.**

This folder is a routing document. Read this file first, then read the stack document or documents that match the project shape.

> **Last reviewed:** 2026-03-30

## The Current Contract

This workspace now has **three language lanes** and **two primary frontend modes**.

### Language lanes

- **Python** for backend services, APIs, automation, scripting, data work, and general application logic
- **Go** for networking, daemons, systems work, performance-sensitive services, and concurrency-heavy runtimes
- **TypeScript** for product frontends, both web and terminal

### Frontend modes

- **Web frontend:** TypeScript + Bun + Astro + Vue
- **Terminal frontend:** OpenTUI + TypeScript + Bun

### Product default

Pick the backend by fit: **Python or Go**.

Then apply the frontend rule:

- If the product has a browser surface, the default frontend is **Astro + Vue on Bun**.
- If the product also benefits from a serious terminal operator surface, add **OpenTUI + TypeScript + Bun** as a second frontend.
- If a TUI does not fit, ship the **web frontend only**.

The preferred shape, when it is justified, is **one backend plus dual frontends**: web and TUI.

---

## How To Use This Folder

### For AI agents and coding assistants

If you are an LLM, coding agent, or sub-agent reading this file as context for build work:

1. Read this README first.
2. Use the [routing section](#routing) to determine which stack doc or docs to read.
3. Read only the docs the routing table assigns.
4. Do not assume Python is the default backend. Choose Python or Go based on the actual product shape.

### For humans

Same idea. Pick the lane, read the docs, build the thing.

These docs describe the current default direction for new work and major rewrites. Existing repos can diverge when the repo docs say so.

---

## Routing

### Stack docs

| Shape | Read | File |
| --- | --- | --- |
| Python backend, automation, API, data tool, or service | **Python** | `python-tech-stack.md` |
| Go service, daemon, networking tool, performance-sensitive backend, or systems runtime | **Go** | `go-tech-stack.md` |
| Browser-facing product surface, site, dashboard, or app frontend | **Web frontend** | `web-frontend-tech-stack.md` |
| Terminal UI, operator console, or terminal-first app frontend | **OpenTUI** | `opentui-tech-stack.md` |
| Product with both browser and terminal frontends | **Web frontend + OpenTUI + chosen backend doc** | `web-frontend-tech-stack.md` + `opentui-tech-stack.md` + backend doc |
| Existing repo with an intentional exception or legacy stack | **Repo README first** | repo-specific |

Rust does not have its own stack doc. In this workspace it is maintenance-only for existing Rust repos unless a repo has a clearly documented reason to stay there.

### Recommended lane map for active repos

This table is routing guidance for future work, not a claim that every repo already implements the target stack today.

| Repo | Recommended lane now | Notes |
| --- | --- | --- |
| bore | Go backend | Add Astro + Vue only if a browser surface becomes first-class |
| wirescope | Go backend + Astro + Vue web + OpenTUI optional | Strong dual-frontend candidate for operator workflows |
| flowhook | Python backend/tooling | Add Astro + Vue only if browser workflows earn it |
| patchworks | Python backend + Astro + Vue web | Core product stays Python; browser UI follows the new web lane |
| toolworks | Python / Go / shell | Choose per tool; Python by default, Go when systems or networking shape justifies it |
| scrybase | Python backend + Astro + Vue web + OpenTUI optional | Dual frontend can make sense if the terminal lane improves the workflow |
| mtg-card-bot | Python backend/bot | No separate frontend by default |
| dunamismax.com | Astro + Vue web | Public-facing site follows the new web lane |
| gitpulse | Repo-specific exception | Follow repo README and in-repo docs |
| go-web-server | Repo-specific reference | Go web reference repo; not the default browser lane for new work |
| cargo-compatible | Rust maintenance | Existing Rust repo |
| cargo-async-doctor | Rust maintenance | Existing Rust repo |
| rust-async-field-guide | Rust docs/examples maintenance | Existing Rust repo |
| c-from-the-ground-up | C reference/docs | No stack doc |
| hello-world-from-hell | C novelty repo | No stack doc |
| openclaw-backup | Ops/shell + Python | No stack doc |

### Frontend direction

Default direction for new product surfaces and active rewrites:

- **TypeScript + Bun + Astro + Vue** for browser frontends
- **OpenTUI + TypeScript + Bun** for terminal frontends
- **Web frontend first** when the product needs a browser surface
- **Dual frontends** when a terminal operator workflow is materially useful
- **Web only** when a TUI would be forced, redundant, or ceremonial

For the web lane, do not default to a client-heavy SPA. Astro owns pages, delivery, and server-first rendering. Vue owns interactive components and stateful UI where interactivity is actually needed.

---

## Shared Rules

These apply to every stack. You do not need to re-read them in every individual stack document.

- Always use the latest stable release of every tool in the stack.
- Prefer official toolchains and standard libraries first.
- Prefer one obvious build entrypoint per repo.
- Prefer process boundaries over language-FFI tangles.
- Prefer single-binary or small-surface deploys over sprawling control planes.
- Prefer Python, Go, or TypeScript based on product shape. There is no universal backend default.
- Add third-party dependencies only when they clearly beat the standard option on correctness, leverage, or operating cost.

---

## Database Operating Model

PostgreSQL is the default database for new application work in this workspace.

That means:

- **PostgreSQL first** for web apps, APIs, services, daemons, multi-user tools, and anything with real deployment ambitions
- **SQLite only when earned** for local-first single-user tools, embedded state, caches, snapshots, SQLite-native products, and very small one-off utilities

If you are starting a new repo and you are not sure which database to pick, choose PostgreSQL.

### PostgreSQL default

Use PostgreSQL by default when the product needs any of the following:

- networked or multi-user access
- concurrent writes as a normal operating condition
- service-style deployment
- richer operational reporting or background jobs
- a Python or Go application that is meant to grow beyond one local machine or one operator session

### SQLite exceptions

SQLite is still the right tool when the repo is intentionally one of these shapes:

- local-first, single-user desktop-ish or operator software
- embedded metadata or state inside a CLI, daemon, or utility
- offline-first tools where shipping one file matters more than networked concurrency
- caches, snapshots, manifests, or sidecar state
- products that are specifically about SQLite itself
- very small utilities or one-off internal tools where PostgreSQL would be pure ceremony

If you pick SQLite, do it on purpose and say why in the repo docs.

## SQLite Operating Model

When a repo does use SQLite, every repo must follow these rules.

### Minimum version

SQLite **3.37.0** or later. This is the floor for `STRICT` tables, which this workspace uses by default. `RETURNING` landed in 3.35.0, and built-in math functions require the `SQLITE_ENABLE_MATH_FUNCTIONS` compile-time option. In practice, `modernc.org/sqlite` ships recent enough builds, but if you are linking against a system SQLite, verify both the version and compile options.

### Default pragmas

Apply these at connection open, before any other queries:

```sql
PRAGMA journal_mode = WAL;
PRAGMA busy_timeout = 5000;
PRAGMA synchronous = NORMAL;
PRAGMA foreign_keys = ON;
PRAGMA cache_size = -20000;
```

### Connection discipline

- Open one long-lived connection for writes. Open a small pool, usually 2 to 4, for reads.
- Do not open a new connection per request.
- In Go, use `sql.Open` once at startup and keep the `*sql.DB` alive for the process lifetime.

### Migration discipline

- Keep migrations as plain `.sql` files in a `migrations/` directory.
- Name them with a sequential prefix: `001_initial.sql`, `002_add_users.sql`.
- Run them at startup in order.
- Never hand-edit a production database outside a migration.

### Backup discipline

- Use `.backup` or `VACUUM INTO` for safe hot backups.
- For Go apps, expose a backup command or admin endpoint.

---

## Default Meta-Choices Across Repos

| Concern | Default |
| --- | --- |
| Backend | Python or Go by fit |
| Browser frontend | TypeScript + Bun + Astro + Vue |
| Terminal frontend | OpenTUI + TypeScript + Bun |
| Database | PostgreSQL by default; SQLite only for deliberately local-first, embedded, SQLite-native, or tiny utilities |
| Data model | Relational |
| Query / schema layer | Raw SQL first; keep helper layers thin |
| Migrations | SQL files for Go; Alembic for Python |
| Observability | Structured logs, Prometheus metrics, OpenTelemetry where tracing is worth it |
| Packaging | Single-purpose binaries, Bun-managed frontend apps, or uv-managed Python apps |
| CI quality bar | Formatter, linter, type checker, tests, vulnerability scan |
| Cross-language integration | Process boundary first, stable protocols second |

---

## Update Policy

- Update this folder whenever a new stable release of any tool in the stack materially changes the advice.
- Always default to the latest stable version of Python, Go, Bun, Astro, Vue, OpenTUI, and all other tools in scope.
- Re-check guidance when major releases land.
