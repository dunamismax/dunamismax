# Tech Stacks

Last reviewed: 2026-03-23

This folder is the opinionated reference set for the software that shows up across this workspace:

- Go services, daemons, CLIs, and operator surfaces like `wirescope`, `riftline`, `gitpulse`, `vaultd`, `repokeeper`, `podforge`, and `go-web-server`
- Zig systems tools and native engines like `ztop`, `lockbox`, `netweave`, and the Zig parts of `dunamis`
- C boundary-layer, firmware, ABI, and custody code like the low-level edges in `dunamis`, the C core in `vaultd`, and the learning path in `c-from-the-ground-up`

These are not "all possible tools" lists. They are boring-default stack decisions for self-hostable systems software, networking, observability, crypto, local-first tooling, and operator-facing products.

## How To Choose

| If the project is mostly... | Start here |
| --- | --- |
| Boundary-layer systems code, firmware edges, ABI shims, hot loops, or tiny native tools | [C Tech Stack](./c-tech-stack.md) |
| Native tooling, protocol engines, terminal apps, packet logic, or systems libraries | [Zig Tech Stack](./zig-tech-stack.md) |
| Services, daemons, CLIs, orchestration, or operational software | [Go Tech Stack](./go-tech-stack.md) |
| Browser-facing Go apps with HTML rendering and a web front end | [Go Full-Stack Tech Stack](./go-full-stack-tech-stack.md) |
| APIs, daemons, and service backends without a primary browser UI | [Go Backend Tech Stack](./go-backend-tech-stack.md) |
| One product where Go, Zig, and C all belong in the same architecture | [Unified Go + Zig + C Tech Stack](./unified-go-zig-c-tech-stack.md) |

## Shared Rules

- Prefer official toolchains and standard libraries first.
- Prefer one obvious build entrypoint per repo.
- Prefer PostgreSQL and raw SQL when durable state matters.
- Prefer process boundaries over language-FFI tangles.
- Prefer single-binary or small-surface deploys over sprawling control planes.
- Prefer explicit memory, explicit ownership, explicit failure modes, and inspectable logs.
- Add third-party dependencies only when they clearly beat the standard option on correctness, leverage, or operating cost.

## What "Best" Means In These Files

In this folder, "best" means the tool is some combination of:

- current and actively maintained
- official or de facto standard
- well documented
- boring to operate
- easy to audit
- aligned with Go, Zig, and C instead of fighting them

That means some fashionable tools are intentionally absent. If the stack decision increases hidden state, runtime magic, reflection debt, JavaScript sprawl, or operational drag, it probably did not make the cut.

## Default Meta-Choices Across Repos

| Concern | Default |
| --- | --- |
| Database | PostgreSQL |
| Query layer | Raw SQL, usually generated into typed code where that helps |
| Observability | Structured logs, Prometheus metrics, OpenTelemetry where tracing is worth it |
| Packaging | Single-purpose binaries first |
| CI quality bar | formatter, linter, tests, vulnerability scan, and release smoke path |
| Web UI style | Server-rendered HTML first, hypermedia over heavy client apps |
| Cross-language integration | Process boundary first, C ABI second, broad `cgo` usage last |

## Update Policy

- Update this folder whenever a new stable Go or Zig release materially changes the advice.
- Re-check C toolchain guidance on new stable Clang, GCC, CMake, or Meson releases.
- Re-check Go web guidance when the standard library meaningfully grows and removes the need for external packages.

## Primary Research Anchors

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
- [`pgx` package docs](https://pkg.go.dev/github.com/jackc/pgx/v5)
- [`chi` docs](https://go-chi.io/)
- [`templ` guide](https://templ.guide/)
- [`htmx` docs](https://htmx.org/docs/)
- [`goose` docs](https://pressly.github.io/goose/)
- [OpenTelemetry for Go](https://opentelemetry.io/docs/languages/go/)
- [Prometheus Go app guide](https://prometheus.io/docs/guides/go-application/)
- [Buf docs](https://buf.build/docs/)
- [Connect RPC docs](https://connectrpc.com/docs/)
- [`golangci-lint` docs](https://golangci-lint.run/)
