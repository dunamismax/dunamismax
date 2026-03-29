# Tech Stacks

**Opinionated stack guidance for the repos in this workspace.**

This folder is a routing document. Read this file first, then read the stack document(s) that match your project.

> **Last reviewed:** 2026-03-29

## How To Use This Folder

### For AI agents and coding assistants

If you are an LLM, coding agent, or sub-agent reading this file as context for a build task:

1. **Read this README first.** It contains shared rules, the database operating model, and the routing table.
2. **Use the [routing section](#routing) to determine which stack doc(s) to read.**
3. **Read only the docs the routing table assigns.** Do not load unrelated stack documents.

### For humans

Same idea. Pick your lane, read that doc, build the thing.

These docs describe the default stack direction for current work. Older repos, reference repos, and intentionally off-stack repos can diverge. When a repo is marked as an exception below, follow that repo's own README and in-repo docs.

---

## Routing

### Stack docs

| Shape | Read | File |
| --- | --- | --- |
| Python script, automation, CLI tool, API, or full-stack app | **Python** | `python-tech-stack.md` |
| Go service, CLI, API, daemon, or orchestrator | **Go** | `go-tech-stack.md` |
| Existing repo with an intentional exception or legacy stack | **Repo README first** | repo-specific |

Rust does not have its own stack doc. In this workspace it is maintenance-only for existing Rust repos unless a project has a clearly documented reason to require it.

### Concrete lane map

| Repo | Lane | Notes |
| --- | --- | --- |
| bore | Go + Python frontend | Go runtime with Python/FastAPI operator surface |
| wirescope | Go + Python frontend | Go runtime with Python/FastAPI browser companion; no Rust lane |
| flowhook | Python | Core toolchain and optional FastAPI dashboard are Python |
| patchworks | Python | Pure Python repo; Rust mapping is obsolete |
| toolworks | Python / shell | Script-by-script repo; default to Python unless a tool says otherwise |
| scrybase | Python | Target stack is pure Python; existing Go code is rewrite/spec context |
| mtg-card-bot | Python | Python app |
| dunamismax.com | Python | FastAPI site |
| cargo-compatible | Rust (maintenance) | Existing Rust repo |
| cargo-async-doctor | Rust (maintenance) | Existing Rust repo |
| rust-async-field-guide | Rust docs/examples (maintenance) | Existing Rust repo |
| gitpulse | Repo-specific exception | Go backend with a Python/FastAPI + Jinja2 + htmx UI and a deliberate local-first data model; follow repo README |
| go-web-server | Repo-specific reference | Go + Echo + Templ + HTMX + PostgreSQL starter; follow repo README |
| c-from-the-ground-up | C reference/docs | No stack doc |
| hello-world-from-hell | C novelty repo | No stack doc |
| openclaw-backup | Ops/shell + Python | No stack doc |

### Frontend direction

Default direction for new browser surfaces and active rewrites:

- **FastAPI + Jinja2 + htmx + Alpine.js** for new frontends
- No separate frontend build step for new product work. No Node/Bun/TypeScript frontend toolchain by default.
- No Django. FastAPI is the only Python web framework in this stack.

Existing repos can diverge when they predate this standard or exist as references. Current exceptions include `gitpulse` and `go-web-server`.

---

## Shared Rules

These apply to every stack. You do not need to re-read them in the individual stack documents.

- Always use the latest stable release of every tool in the stack.
- Prefer official toolchains and standard libraries first.
- Prefer one obvious build entrypoint per repo.
- Prefer process boundaries over language-FFI tangles.
- Prefer single-binary or small-surface deploys over sprawling control planes.
- Prefer Go or Python for new work. Treat Rust as maintenance-only unless the repo already exists in Rust or the requirement is exceptional.
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
- embedded metadata/state inside a CLI, daemon, or utility
- offline-first tools where shipping one file matters more than networked concurrency
- caches, snapshots, manifests, or sidecar state
- products that are specifically about SQLite itself
- very small utilities or one-off internal tools where PostgreSQL would be pure ceremony

If you pick SQLite, do it on purpose and say why in the repo docs.

## SQLite Operating Model

When a repo does use SQLite, every repo must follow these rules.

### Minimum version

SQLite **3.37.0** or later. This is the floor for `STRICT` tables (3.37.0), which this workspace uses by default. `RETURNING` landed in 3.35.0, and built-in math functions require the `SQLITE_ENABLE_MATH_FUNCTIONS` compile-time option (not version-gated). In practice, `modernc.org/sqlite` ships recent enough builds, but if you are linking against a system SQLite, verify both the version and compile options.

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

- Open one long-lived connection for writes. Open a small pool (2–4) for reads.
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
| Database (Go apps and tools) | PostgreSQL by default; SQLite only for deliberately local-first, embedded, or tiny utilities |
| Database (Python web) | PostgreSQL by default; SQLite only for deliberately local-first, single-user, or tiny self-hosted apps |
| Data model | Relational |
| Query / schema layer | Raw SQL first; keep helper layers thin |
| Migrations | SQL files for Go; Alembic for Python |
| Observability | Structured logs, Prometheus metrics, OpenTelemetry where tracing is worth it |
| Packaging | Single-purpose binaries (Go) or uv-managed Python apps |
| CI quality bar | Formatter, linter, type checker, tests, vulnerability scan |
| Frontend (default for new browser surfaces) | FastAPI + Jinja2 + htmx + Alpine.js (server-rendered, no SPA) |
| Cross-language integration | Process boundary first, stable protocols second |

---

## Update Policy

- Update this folder whenever a new stable release of any tool in the stack materially changes the advice.
- Always default to the latest stable version of Python, Go, and all other tools.
- Re-check guidance when major releases land.
