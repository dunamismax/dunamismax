# BUILD

This is the profile README repo and tech-stacks host for dunamismax.

It has no build system. Its deliverables are:

- `README.md` -- the GitHub profile README, visible at github.com/dunamismax
- `tech-stacks/` -- opinionated reference stack docs for Bun + TypeScript + Astro + Alpine.js web apps, C, Zig, Go, Go backends, Go-rendered web apps, and unified Go + Zig + C systems

Maintenance work here falls into three phases: keeping the profile README accurate, keeping the tech-stack docs current, and keeping the portfolio curation honest.

---

## Phase 1: Profile README Maintenance

- [ ] Verify every repo linked in "Start Here" is public and the description matches what the repo actually does today
- [ ] Verify every repo linked in "Building Now" is still active and the description is current
- [ ] Verify every repo linked in "Reference, Learning, and Smaller Builds" still exists and the one-line description is accurate
- [ ] Confirm the tech-stacks link at the bottom resolves correctly
- [ ] Confirm the "Working Style" section still reflects actual language usage across the portfolio
- [ ] Remove any repo links that have been deleted, renamed, or made private
- [ ] Add newly public repos to the appropriate section if they meet the bar

## Phase 2: Tech Stack Alignment

- [ ] Re-check the Go toolchain version in all four Go stack docs against the current stable release at go.dev/dl
- [ ] Re-check the Zig toolchain version in `zig-tech-stack.md` and `unified-go-zig-c-tech-stack.md` against the current stable release at ziglang.org/download
- [ ] Re-check the Bun, Astro, Alpine.js, Biome, and Vitest guidance in the web stack doc against current stable docs
- [ ] Re-check the C stack for any changes to Clang, GCC, CMake, or Meson that materially affect the guidance
- [ ] Confirm `sqlc`, `pgx`, `goose`, `chi`, `golangci-lint`, and `govulncheck` references are still the correct packages and still actively maintained
- [ ] Confirm `templ`, `htmx`, `air`, and `scs` references in the Go-rendered web doc are current
- [ ] Confirm `buf`, `connectrpc`, and `opentelemetry` references in the backend doc are current
- [ ] Update the "Last reviewed" date in each tech-stack file after verifying it
- [ ] Verify that the repo examples cited in each stack doc still exist and still match the described stack
  - `go-tech-stack.md` cites: wirescope, riftline, vaultd, gitpulse, repokeeper, podforge
  - `zig-tech-stack.md` cites: lockbox, dunamis
  - `c-tech-stack.md` cites: dunamis, vaultd
  - `unified-go-zig-c-tech-stack.md` cites: dunamis, vaultd
- [ ] Update `tech-stacks/README.md` "Last reviewed" date after any stack doc changes
- [ ] Confirm the "How To Choose" table in `tech-stacks/README.md` still maps correctly to the actual stack docs

## Phase 3: Portfolio Curation

- [ ] Confirm the "Start Here" section contains the six strongest entry points into the work -- reorder or swap if a newer repo is a better first impression
- [ ] Confirm the "Building Now" section reflects repos that are genuinely in active development, not stalled experiments
- [ ] Remove any repo from "Building Now" that has gone quiet for more than one release cycle and move it to a lower section or drop it
- [ ] Confirm no significant repo is missing entirely from the README
- [ ] Confirm the one-paragraph bio at the top still reflects the actual focus areas (networking, cryptography, observability, developer tooling, trading infrastructure, OS work)
- [ ] Confirm the repo section headers still make structural sense given the current portfolio shape
