# C Tech Stack

Last reviewed: 2026-03-23

## Best Fit

Use this stack when the project is mostly:

- boundary-layer systems code
- firmware or freestanding work
- syscall and ABI shims
- auditable crypto custody code
- tiny native utilities
- packet hot paths that need direct control

For this workspace, this maps best to `c-from-the-ground-up`, the C edges inside `dunamis`, and the narrow C core patterns inside `vaultd`.

## Opinionated Default

| Area | Default | Why |
| --- | --- | --- |
| Language baseline | C23, with C17 fallback when portability forces it | C23 gives cleaner modern C without leaving mainstream compilers behind |
| Primary compiler | Clang/LLVM | Best diagnostics, best sanitizer ergonomics, best editor tooling via `clangd` |
| Secondary compiler | GCC | Portability cross-check and a second warning model |
| Build system | CMake + Ninja | Widest ecosystem support, good IDE support, easy CI use |
| Alternative build system | Meson | Simpler authoring when the project is a normal app or library |
| Cross compilation | `zig cc` | Excellent "just cross-compile it" option from a C codebase |
| Formatter | `clang-format` | Ubiquitous and boring |
| LSP / indexing | `clangd` | Best-in-class C editing experience |
| Static analysis | `clang-tidy`, `scan-build`, GCC `-fanalyzer` | C needs multiple lines of defense |
| Runtime checking | AddressSanitizer, UndefinedBehaviorSanitizer, ThreadSanitizer | Find memory, UB, and concurrency bugs early |
| Tests | plain C test binaries plus CTest | Fewer layers, easier to debug than clever test frameworks |
| Fuzzing | libFuzzer with sanitizers | Strong default for parsers, protocol code, and binary formats |
| Dependency strategy | system libs via `pkg-config`, otherwise vendor small dependencies | Keeps the build legible and reproducible |
| Crypto | libsodium by default | Safer and simpler than assembling crypto primitives yourself |
| TLS / ecosystem compatibility | OpenSSL only when you need TLS or broad compatibility | Use the boring industry implementation when the problem demands it |
| Terminal UI | `ncurses` or `ncursesw` | Mature and reliable for terminal apps |

## Golden Path

1. Compile every target with both Clang and GCC in CI.
2. Develop primarily with Clang plus sanitizers enabled.
3. Use CMake + Ninja unless the project is so small that a tiny `Makefile` is clearly enough.
4. Keep the public API small, header-driven, and easy to audit.
5. Prefer explicit ownership and caller-controlled allocation.
6. Use `zig cc` when you need painless cross-target builds.

## Default Build Flags

Use a strict warning baseline in development:

```sh
-std=c23 -Wall -Wextra -Wpedantic -Wconversion -Wshadow -Wstrict-prototypes -Wmissing-prototypes
```

Add these in dedicated debug or CI variants, not in release builds:

```sh
-fsanitize=address,undefined
```

Use `-fsanitize=thread` for concurrent code paths in separate runs.

## Default Repo Shape

```text
project/
  include/
  src/
  tests/
  fuzz/
  third_party/
  CMakeLists.txt
  README.md
```

Use `src/` for implementation, `include/` for public headers, `tests/` for direct executable tests, and `fuzz/` for parser or protocol fuzz targets.

## Dependency Rules

- Prefer libc, POSIX, and platform SDKs before adding external libraries.
- Use `pkg-config` for system dependencies.
- Vendor very small libraries if that makes the build easier to audit.
- Do not pull in dependency managers just to feel modern.
- If the project needs deep cross-compilation support, strongly consider building the C code through Zig's C frontend.

## Security Baseline

- Zero tolerance for unchecked allocation failures in security-sensitive paths.
- Zero tolerance for unclear ownership on secret-bearing buffers.
- Prefer libsodium for secret-key workflows and memory-hard primitives.
- Use `explicit_bzero`, libsodium secure-memory facilities, or equivalent platform-safe wiping where appropriate.
- Keep secret-handling code narrow and isolate it from UI and orchestration concerns.

## Testing Baseline

- Unit tests are normal executables.
- Integration tests are shell-driven or harness-driven binaries.
- Sanitizer jobs are mandatory in CI.
- Add fuzz targets for parsers, decoders, network packet handling, and file formats.

## When To Choose C Over Zig Or Go

Choose C when:

- the target is freestanding or firmware-adjacent
- the boundary must expose a stable C ABI
- you need the smallest and most auditable surface possible
- you are wrapping platform APIs or legacy libraries

Do not choose C just because the code is "performance sensitive." If the work is mostly systems logic and not boundary code, Zig is usually the better default now.

## Avoid By Default

- giant macro frameworks
- custom build systems when CMake or Meson would do
- homegrown crypto
- hidden global allocators
- complicated header-only meta-programming tricks
- broad dependency trees for tiny tools

## Primary Sources

- [Clang docs](https://clang.llvm.org/docs/)
- [GCC docs](https://gcc.gnu.org/onlinedocs/)
- [CMake docs](https://cmake.org/cmake/help/latest/)
- [Meson docs](https://mesonbuild.com/)
- [Ninja manual](https://ninja-build.org/manual.html)
- [libsodium docs](https://doc.libsodium.org/)
- [OpenSSL docs](https://docs.openssl.org/3.5/)
