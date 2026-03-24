# Tech Stacks

Last reviewed: 2026-03-23

This folder is the opinionated reference set for the software that shows up across this workspace:

- Static web for blogs, docs, marketing, and content-heavy sites
- SPA web for rich, interactive, client-first browser apps
- SSR web for Go-backed server-rendered apps with auth, sessions, and durable state
- Go for services, daemons, CLIs, operator software, and durable application logic
- Zig for systems tools, native engines, protocol machinery, and low-level control
- C for boundary-layer, firmware, ABI, and custody code
- A unified stack when one product genuinely needs all four lanes at once

These are not "all possible tools" lists. They are boring-default stack decisions for self-hostable systems software, networking, observability, crypto, local-first tooling, operator-facing products, and browser surfaces that should stay fast, sane, and pleasant to build.

## How To Choose

| If the project is mostly... | Start here |
| --- | --- |
| Blogs, docs, marketing, portfolio, or content-heavy sites | [Static Web](./web-static-tech-stack.md) |
| Rich interactive browser apps where the client experience is the product | [SPA Web](./web-spa-tech-stack.md) |
| Go-backed apps with auth, sessions, API routes, and server rendering | [SSR Web](./web-ssr-tech-stack.md) |
| Boundary-layer systems code, firmware edges, ABI shims, hot loops, or tiny native tools | [C Tech Stack](./c-tech-stack.md) |
| Native tooling, protocol engines, terminal apps, packet logic, or systems libraries | [Zig Tech Stack](./zig-tech-stack.md) |
| Services, daemons, CLIs, orchestration, or operational software | [Go Tech Stack](./go-tech-stack.md) |
| One product where the browser surface, Go control plane, Zig engine, and C boundary all belong in the same architecture | [Unified Go + Zig + C + Web Tech Stack](./unified-go-zig-c-web-tech-stack.md) |

## Shared Rules

- Always use the latest stable release of every tool in the stack.
- Prefer official toolchains and standard libraries first.
- Prefer one obvious build entrypoint per repo.
- Prefer process boundaries over language-FFI tangles.
- Prefer single-binary or small-surface deploys over sprawling control planes.
- Prefer server-first rendering and HTML/CSS that still make sense before JavaScript runs.
- Hydrate the smallest possible surface when client state is genuinely required.
- Add third-party dependencies only when they clearly beat the standard option on correctness, leverage, or operating cost.

## SQLite Operating Model

SQLite is the default database across this workspace. Every repo that uses SQLite should follow these shared operational rules.

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

## Update Policy

- Update this folder whenever a new stable release of any tool in the stack materially changes the advice.
- Always default to the latest stable version of Go, Zig, Bun, Astro, and all other tools.
- Re-check guidance when major releases land.
