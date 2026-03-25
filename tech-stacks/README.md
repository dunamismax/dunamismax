# Tech Stacks

**Opinionated stack guidance for the repos in this workspace.**

This folder is a routing document. Read this file first, then read the stack document(s) that match your project.

> **Last reviewed:** 2026-03-25

## How To Use This Folder

### For AI agents and coding assistants

If you are an LLM, coding agent, or sub-agent reading this file as context for a build task:

1. **Read this README first.** It contains shared rules, the SQLite operating model, and the routing table.
2. **Use the [routing section](#routing) to determine which stack doc(s) to read.**
3. **Read only the docs the routing table assigns.** Do not load unrelated stack documents.

### For humans

Same idea. Pick your lane, read that doc, build the thing.

---

## Routing

### Stack docs

| Shape | Read | File |
| --- | --- | --- |
| Python script, automation, CLI tool, API, or full-stack app | **Python** | `python-tech-stack.md` |
| Go service, CLI, API, daemon, or orchestrator | **Go** | `go-tech-stack.md` |

Rust repos (patchworks, cargo-compatible, cargo-async-doctor, rust-async-field-guide) follow standard Rust tooling conventions. Rust does not have its own stack doc — it is used only when the project specifically requires it.

### Concrete lane map

| Repo | Lane |
| --- | --- |
| toolworks | Python |
| bore | Go + Python (FastAPI/htmx frontend) |
| repokeeper | Go + Python (FastAPI/htmx frontend) |
| scrybase | Go + Python (FastAPI/htmx frontend) |
| wirescope | Go + Rust + Python (FastAPI/htmx frontend) |
| dunamismax.com | Python (FastAPI) |
| patchworks | Rust |
| cargo-compatible | Rust |
| cargo-async-doctor | Rust |
| rust-async-field-guide | Rust (reference/docs) |
| openclaw-backup | Ops/shell (no stack doc) |

### Frontend direction

All web surfaces use Python-driven server-rendered pages:

- **FastAPI + Jinja2 + htmx + Alpine.js** for all frontends
- No separate frontend build step. No Node/Bun/TypeScript toolchain.
- No Django. FastAPI is the only Python web framework in this stack.

---

## Shared Rules

These apply to every stack. You do not need to re-read them in the individual stack documents.

- Always use the latest stable release of every tool in the stack.
- Prefer official toolchains and standard libraries first.
- Prefer one obvious build entrypoint per repo.
- Prefer process boundaries over language-FFI tangles.
- Prefer single-binary or small-surface deploys over sprawling control planes.
- Add third-party dependencies only when they clearly beat the standard option on correctness, leverage, or operating cost.

---

## SQLite Operating Model

SQLite is the default database for local-first tools and Go services. Every repo that uses SQLite must follow these rules.

### Minimum version

SQLite **3.37.0** or later. This is the floor for `STRICT` tables (3.37.0), which this workspace uses by default. `RETURNING` landed in 3.35.0, and built-in math functions require the `SQLITE_ENABLE_MATH_FUNCTIONS` compile-time option (not version-gated). In practice, `modernc.org/sqlite` ships recent enough builds — but if you are linking against a system SQLite, verify both the version and compile options.

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

### When to use PostgreSQL instead

Use PostgreSQL when the product needs:

- multiple write-heavy processes that cannot share one writer
- networked multi-node access
- operational reporting that needs concurrent heavy reads alongside writes
- a Python web app (Django/FastAPI default to PostgreSQL)

SQLite is the default for Go CLI tools, daemons, and local-first products. PostgreSQL is the default for Python web applications.

---

## Default Meta-Choices Across Repos

| Concern | Default |
| --- | --- |
| Database (Go tools) | SQLite |
| Database (Python web) | PostgreSQL |
| Data model | Relational |
| Query / schema layer | Raw SQL first; keep helper layers thin |
| Migrations | SQL files for Go; Alembic for Python |
| Observability | Structured logs, Prometheus metrics, OpenTelemetry where tracing is worth it |
| Packaging | Single-purpose binaries (Go) or uv-managed Python apps |
| CI quality bar | Formatter, linter, type checker, tests, vulnerability scan |
| Frontend | FastAPI + Jinja2 + htmx + Alpine.js (server-rendered, no SPA) |
| Cross-language integration | Process boundary first, stable protocols second |

---

## Update Policy

- Update this folder whenever a new stable release of any tool in the stack materially changes the advice.
- Always default to the latest stable version of Python, Go, and all other tools.
- Re-check guidance when major releases land.
