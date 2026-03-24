# Tech Stacks

Last reviewed: 2026-03-23

## How To Use This Folder

This is a routing document. Read this file first, then read **only the one stack document** that matches your project. Do not read all the stack documents — each one is self-contained and designed to be the single reference for its lane.

### For AI agents and coding assistants

If you are an LLM, coding agent, or sub-agent reading this file as context for a build task:

1. **Read this README first.** It contains shared rules and the SQLite operating model that apply to every stack.
2. **Use the decision table below to pick exactly one stack document.**
3. **Read only that one document.** It has everything you need for that project type — defaults, golden path, repo shape, guardrails, and anti-patterns.
4. **Do not load the other stack documents.** They are for different project types and will waste your context window.
5. **If the project spans multiple lanes** (e.g., a Go backend with an Astro frontend), read the Go doc and the relevant web doc — that is two documents, not five. If the project also has a C boundary layer, add `go-c-tech-stack.md` for the Go ↔ C boundary rules.

### For humans

Same idea. Pick your lane, read that doc, build the thing.

---

## Decision Table

Pick the **first row that matches** your project:

| Your project looks like... | Read this | File |
| --- | --- | --- |
| A blog, docs site, portfolio, marketing page, or content-heavy static site | **Static Web** | `web-static-tech-stack.md` |
| A Go-backed web app with auth, sessions, API routes, forms, and server rendering | **SSR Web** | `web-ssr-tech-stack.md` |
| A service, daemon, CLI, API, orchestrator, or operational tool | **Go** | `go-tech-stack.md` |
| Boundary-layer code, firmware, ABI shim, custody code, kernel internals, or tiny native utility | **C** | `c-tech-stack.md` |
| A product that needs Go orchestration + a narrow C boundary layer (no browser surface in scope) | **Go + C** | `go-c-tech-stack.md` |

### Common combinations

Most repos in this workspace are **Go + SSR Web** (a Go backend serving an Astro frontend). For that shape:

- Read `go-tech-stack.md` for the backend
- Read `web-ssr-tech-stack.md` for the frontend
- The SSR doc covers the Go ↔ Astro boundary

If the repo needs **Go + C without a browser surface**, read `go-c-tech-stack.md`. It covers the division of labor, interop rules, and boundary guidance for that pair.

If the repo needs **Go + C and also has a browser surface**, read `go-c-tech-stack.md` for the backend/boundary and the relevant web doc (`web-ssr-tech-stack.md` or `web-static-tech-stack.md`) for the frontend. There is no single unified doc for all three — compose the relevant docs instead.

If the repo is purely a Go service with no browser surface, read only `go-tech-stack.md`.

If the repo is purely a static site with no backend, read only `web-static-tech-stack.md`.

---

## Shared Rules

These apply to every stack. You do not need to re-read them in the individual stack documents.

- Always use the latest stable release of every tool in the stack.
- Prefer official toolchains and standard libraries first.
- Prefer one obvious build entrypoint per repo.
- Prefer process boundaries over language-FFI tangles.
- Prefer single-binary or small-surface deploys over sprawling control planes.
- Prefer server-first rendering and HTML/CSS that still make sense before JavaScript runs.
- Hydrate the smallest possible surface when client state is genuinely required.
- Add third-party dependencies only when they clearly beat the standard option on correctness, leverage, or operating cost.

---

## SQLite Operating Model

SQLite is the default database across this workspace. Every repo that uses SQLite must follow these rules. Individual stack documents reference this section instead of repeating it.

### Minimum version

SQLite 3.35.0 or later. This is the floor for `RETURNING`, `STRICT` tables, and built-in math functions. In practice, `modernc.org/sqlite` and `bun:sqlite` both ship recent enough versions that this is not a concern — but if you are linking against a system SQLite, verify the version.

### Default pragmas

Apply these at connection open, before any other queries:

```sql
PRAGMA journal_mode = WAL;
PRAGMA busy_timeout = 5000;
PRAGMA synchronous = NORMAL;
PRAGMA foreign_keys = ON;
PRAGMA cache_size = -20000;
```

**WAL mode** is mandatory for any app that serves concurrent reads or runs a web server. It allows readers and one writer to operate simultaneously without blocking each other.

**busy_timeout** prevents immediate `SQLITE_BUSY` errors under light write contention. 5 seconds is a reasonable default; tune down for latency-sensitive paths.

**synchronous = NORMAL** is safe under WAL mode and avoids the performance cost of `FULL` syncs on every commit. Do not set `synchronous = OFF` unless you genuinely accept data loss on crash.

**foreign_keys = ON** is off by default in SQLite. Always enable it. There is no good reason to leave referential integrity disabled.

**cache_size = -20000** sets a 20MB page cache. Adjust per workload, but the 2MB default is too small for most apps.

### Connection discipline

- Open one long-lived connection for writes. Open a small pool (2–4) for reads.
- Do not open a new connection per request. SQLite connections are cheap to keep open and expensive to re-negotiate WAL state on.
- In Go, use `sql.Open` once at startup and keep the `*sql.DB` alive for the process lifetime.
- In Bun, use `new Database()` once and reuse the handle.

### Migration discipline

- Keep migrations as plain `.sql` files in a `migrations/` directory.
- Name them with a sequential prefix: `001_initial.sql`, `002_add_users.sql`.
- Run them at startup in order. A small in-repo runner is fine. Do not add a migration framework unless the repo has earned it.
- Never hand-edit a production database outside a migration. If you need a fix, write a migration.

### Backup discipline

- Use `.backup` or `VACUUM INTO` for safe hot backups. Do not copy the database file while connections are open.
- For Go apps, expose a backup command or admin endpoint.

### When SQLite is not enough

Move to PostgreSQL when the product clearly earns it through:

- multiple write-heavy processes that cannot share one writer
- networked multi-node access
- operational reporting that needs concurrent heavy reads alongside writes
- deployment shape that requires a shared database server

Do not move to PostgreSQL because it "feels more serious." SQLite handles more than most people think.

---

## Default Meta-Choices Across Repos

| Concern | Default |
| --- | --- |
| Database | SQLite |
| Data model | Relational |
| Query / schema layer | Raw SQL first; keep helper layers thin and only add them when they clearly reduce real pain |
| Migrations | SQL files first; tiny runners second; heavier tooling only when the repo has earned it |
| Observability | Structured logs, Prometheus metrics, OpenTelemetry where tracing is worth it |
| Packaging | Single-purpose binaries first |
| CI quality bar | Formatter, linter, tests, vulnerability scan, and release smoke path |
| Frontend/web lane | Bun + Astro first, TypeScript where it helps, Alpine for light interaction, islands only when the browser really owns the state |
| Cross-language integration | Process boundary first, C ABI second, broad `cgo` usage last |

---

## Update Policy

- Update this folder whenever a new stable release of any tool in the stack materially changes the advice.
- Always default to the latest stable version of Go, Bun, Astro, and all other tools.
- Re-check guidance when major releases land.
