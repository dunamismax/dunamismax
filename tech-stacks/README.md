# Tech Stacks

Last reviewed: 2026-03-23

This folder is the opinionated reference set for the software that shows up across this workspace:

- Web for websites, docs, frontends, and browser-facing products
- Go for services, daemons, CLIs, operator software, and durable application logic
- Zig for systems tools, native engines, protocol machinery, and low-level control
- C for boundary-layer, firmware, ABI, and custody code
- a unified stack when one product genuinely needs all four lanes at once

These are not "all possible tools" lists. They are boring-default stack decisions for self-hostable systems software, networking, observability, crypto, local-first tooling, operator-facing products, and browser surfaces that should stay fast, sane, and pleasant to build.

The data doctrine in this folder is now explicit:

- **SQLite is the default database**
- **raw SQL is the default query language**
- **relational data is the default model**
- higher-level query layers are exceptions that must earn their place

## How To Choose

| If the project is mostly... | Start here |
| --- | --- |
| Websites, docs, product frontends, or browser-facing web apps | [Web Tech Stack](./web-tech-stack.md) |
| Boundary-layer systems code, firmware edges, ABI shims, hot loops, or tiny native tools | [C Tech Stack](./c-tech-stack.md) |
| Native tooling, protocol engines, terminal apps, packet logic, or systems libraries | [Zig Tech Stack](./zig-tech-stack.md) |
| Services, daemons, CLIs, orchestration, or operational software | [Go Tech Stack](./go-tech-stack.md) |
| One product where the browser surface, Go control plane, Zig engine, and C boundary all belong in the same architecture | [Unified Go + Zig + C + Web Tech Stack](./unified-go-zig-c-web-tech-stack.md) |

## Shared Rules

- Prefer official toolchains and standard libraries first.
- Prefer one obvious build entrypoint per repo.
- Prefer **SQLite by default**.
- Prefer **raw SQL by default**.
- Prefer **relational data by default**.
- Prefer tiny SQL migration files over framework-heavy migration machinery.
- Prefer process boundaries over language-FFI tangles.
- Prefer single-binary or small-surface deploys over sprawling control planes.
- Prefer server-first rendering and HTML/CSS that still make sense before JavaScript runs.
- Hydrate the smallest possible surface when client state is genuinely required.
- Add third-party dependencies only when they clearly beat the standard option on correctness, leverage, or operating cost.

## What "Best" Means In These Files

In this folder, "best" means the tool is some combination of:

- current and actively maintained
- official or de facto standard
- well documented
- boring to operate
- easy to audit
- aligned with Go, Zig, C, and the default web lane instead of fighting them
- fast enough to keep local loops, agent workflows, and solo development pleasant

That means some fashionable tools are intentionally absent. If the stack decision increases hidden state, runtime magic, framework theater, JavaScript sprawl, database theater, or operational drag, it probably did not make the cut.

## Default Meta-Choices Across Repos

| Concern | Default |
| --- | --- |
| Database | SQLite |
| Data model | Relational |
| Query / schema layer | Raw SQL first; Drizzle or `sqlc` only when they clearly reduce real pain |
| Migrations | SQL files first; tiny runners second; heavier tooling only when the repo has earned it |
| Observability | Structured logs, Prometheus metrics, OpenTelemetry where tracing is worth it |
| Packaging | Single-purpose binaries first |
| CI quality bar | formatter, linter, tests, vulnerability scan, and release smoke path |
| Frontend/web lane | Bun + Astro first, TypeScript where it helps, Alpine for light interaction, islands only when the browser really owns the state |
| Cross-language integration | Process boundary first, C ABI second, broad `cgo` usage last |

## Update Policy

- Update this folder whenever a new stable Go or Zig release materially changes the advice.
- Re-check Bun, Astro, Alpine.js, Biome, Vitest, and SQLite guidance when their stable releases materially change the default web lane.
- Re-check C toolchain guidance on new stable Clang, GCC, CMake, or Meson releases.
- Re-check Go guidance when the standard library meaningfully grows and removes the need for external packages.

## Primary Research Anchors

- [Bun docs](https://bun.sh/docs)
- [TypeScript docs](https://www.typescriptlang.org/docs/)
- [Astro docs](https://docs.astro.build/)
- [Alpine.js docs](https://alpinejs.dev/start-here)
- [Biome docs](https://biomejs.dev/guides/getting-started/)
- [Vitest docs](https://vitest.dev/guide/)
- [Playwright docs](https://playwright.dev/docs/intro)
- [SQLite docs](https://www.sqlite.org/docs.html)
- [SQLite SQL language reference](https://www.sqlite.org/lang.html)
- [SQLite pragma reference](https://www.sqlite.org/pragma.html)
- [Drizzle docs](https://orm.drizzle.team/docs/overview)
- [Go downloads and release history](https://go.dev/dl/)
- [Go release notes index](https://go.dev/doc/devel/release)
- [Go `slog` announcement](https://go.dev/blog/slog)
- [Go `net/http` ServeMux docs](https://pkg.go.dev/net/http#ServeMux)
- [Go `govulncheck` tutorial](https://go.dev/doc/tutorial/govulncheck)
- [Zig downloads](https://ziglang.org/download/)
- [Zig language and standard library docs](https://ziglang.org/documentation/master/)
- [CMake docs](https://cmake.org/cmake/help/latest/)
- [Meson docs](https://mesonbuild.com/)
- [Ninja manual](https://ninja-build.org/manual.html)
- [Clang docs](https://clang.llvm.org/docs/)
- [GCC docs](https://gcc.gnu.org/onlinedocs/)
- [OpenSSL docs](https://docs.openssl.org/3.5/)
- [libsodium docs](https://doc.libsodium.org/)
- [`sqlc` docs](https://docs.sqlc.dev/)
- [`chi` docs](https://go-chi.io/)
- [`templ` guide](https://templ.guide/)
- [`htmx` docs](https://htmx.org/docs/)
- [`goose` docs](https://pressly.github.io/goose/)
- [OpenTelemetry for Go](https://opentelemetry.io/docs/languages/go/)
- [Prometheus Go app guide](https://prometheus.io/docs/guides/go-application/)
- [Buf docs](https://buf.build/docs/)
- [Connect RPC docs](https://connectrpc.com/docs/)
- [`golangci-lint` docs](https://golangci-lint.run/)
