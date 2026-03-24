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

For this workspace, this maps best to the C edges inside `dunamis` and the narrow C core patterns inside `vaultd`.

## Opinionated Default

| Area | Default |
| --- | --- |
| Language baseline | C23, with C17 fallback when portability forces it |
| Primary compiler | Clang/LLVM |
| Secondary compiler | GCC |
| Build system | CMake + Ninja |
| Alternative build system | Meson |
| Cross compilation | `zig cc` |
| Formatter | `clang-format` |
| LSP / indexing | `clangd` |
| Static analysis | `clang-tidy`, `scan-build`, GCC `-fanalyzer` |
| Runtime checking | AddressSanitizer, UndefinedBehaviorSanitizer, ThreadSanitizer |
| Tests | Plain C test binaries plus CTest |
| Fuzzing | libFuzzer with sanitizers |
| Dependency strategy | System libs via `pkg-config`, otherwise vendor small dependencies |
| Crypto | libsodium by default |
| TLS / ecosystem compatibility | OpenSSL only when you need TLS or broad compatibility |
| Terminal UI | `ncurses` or `ncursesw` |

## Golden Path

1. Compile every target with both Clang and GCC in CI.
2. Develop primarily with Clang plus sanitizers enabled.
3. Use CMake + Ninja unless the project is so small that a tiny `Makefile` is clearly enough.
4. Keep the public API small, header-driven, and easy to audit.
5. Prefer explicit ownership and caller-controlled allocation.
6. Use `zig cc` when you need painless cross-target builds.
7. Keep product persistence outside the C layer unless the C code is the only honest owner of the bytes.

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

## Data Boundary Guidance

- C is not the default owner of product persistence.
- If state must persist, prefer letting Go or the web lane own SQLite and handing C a narrow file, socket, or ABI contract.
- Keep database concerns out of C unless the whole point of the component is a tiny auditable storage leaf.

## When To Choose C Over Zig Or Go

Choose C when:

- the target is freestanding or firmware-adjacent
- the boundary must expose a stable C ABI
- you need the smallest and most auditable surface possible
- you are wrapping platform APIs or legacy libraries

Do not choose C just because the code is "performance sensitive." If the work is mostly systems logic and not boundary code, Zig is usually the better default now.

## Avoid By Default

- Giant macro frameworks
- Custom build systems when CMake or Meson would do
- Homegrown crypto
- Hidden global allocators
- Complicated header-only meta-programming tricks
- Broad dependency trees for tiny tools
