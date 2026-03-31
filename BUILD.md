# BUILD.md

Last reviewed: 2026-03-31

This file is the active execution manual for the current evolution of the `dunamismax` repo.

Future agents are expected to work through this file, keep it current, and check boxes as phases and steps are actually completed. Do not treat this as background reading. Treat it as the working plan.

If the repo truth changes, update this file first, then update the stable docs. Do not check aspirational items early.

## Repo role

This repo is best understood as a lightweight public identity and portfolio repo:

- root `README.md` is the public GitHub profile and project summary
- `tech-stacks/` holds Stephen's current stack guidance for new work and major rewrites
- CI is intentionally small and only verifies markdown presence and local links in the stable docs it knows about

## Fit boundaries

This repo should align with Stephen's current preferred stack and portfolio direction, but it should not fake a product shape it does not have.

What should stay true here:

- this remains a markdown-first profile and documentation repo
- the repo stays small, readable, and current-state oriented
- project links point outward to the actual repos where the real implementation work lives
- stack guidance stays honest about current defaults and exceptions

What should **not** happen here just because the preferred web lane is now Bun + TypeScript + Astro + Vue:

- do **not** turn this repo into an Astro app by reflex
- do **not** add Elysia, PostgreSQL, Docker, Caddy, or app scaffolding to this repo without a separately justified repo-shape change
- do **not** pretend the GitHub profile README repo is the same thing as a full portfolio web application
- do **not** duplicate deep project documentation that belongs in each project repo

If Stephen wants a richer browser portfolio experience, that work belongs in `dunamismax.com` or another dedicated web repo. This repo should then link to it cleanly.

## Current repo truth

As of 2026-03-31:

- the repo contains a public-facing `README.md`, a `LICENSE`, CI, and stack docs under `tech-stacks/`
- the public README already reflects Stephen's current language lanes and project focus areas
- the stack docs already establish Bun + Astro as the default web frontend lane and Bun + Astro + Elysia + PostgreSQL + Caddy as the default full-stack TypeScript web lane when the product is genuinely web-first
- there is no runtime, package manifest, application source tree, deployment config, or database layer in this repo
- this repo is a documentation and positioning surface, not an application runtime

## Target outcome

The target state for this repo is:

- `README.md` stays sharp, current, and aligned with Stephen's actual portfolio direction
- `tech-stacks/` remains the canonical routing layer for current build defaults
- selected projects emphasize Stephen's real current lanes without erasing valid legacy or maintenance exceptions
- this repo clearly distinguishes between profile documentation and actual product repos
- any future portfolio web app effort is linked cleanly instead of being awkwardly forced into this repo
- once this evolution work is genuinely complete, stable docs should stand on their own and this `BUILD.md` should be removed

## Future-agent operating rules

- Read `README.md`, `tech-stacks/README.md`, and the most relevant stack doc or docs before editing.
- Keep stable docs current-state oriented. Do not turn them into speculative roadmap documents.
- Use this `BUILD.md` as the live plan. If the plan becomes wrong, rewrite the plan before changing the repo around it.
- Check boxes only after verifying the work directly.
- When a phase is complete, tighten the stable docs so they reflect current truth without requiring this file for normal understanding.
- If the repo no longer needs a build-phase tracker, fold any remaining current-state guidance into stable docs and delete `BUILD.md`.

## Phased plan

### Phase 1 - Baseline and guardrails

Work items:

- [ ] Re-read `README.md`, `tech-stacks/README.md`, and the stack doc most relevant to the current portfolio direction before making further edits.
- [ ] Confirm the repo still fits the profile-docs shape and does not secretly need to become a different kind of repo.
- [ ] Record any new fit-boundary decisions in this file before changing public docs.
- [ ] Confirm there are no current README or stack-doc statements that imply this repo itself is a web app or full-stack product.

Acceptance criteria:

- [ ] The repo role is explicit and future agents can tell, in under a minute, what belongs here and what does not.
- [ ] The plan clearly states that this repo aligns with the modern stack direction without pretending to be an implementation of that stack.

### Phase 2 - Public portfolio narrative tightening

Work items:

- [ ] Audit the root `README.md` for project ordering, wording, and emphasis against Stephen's actual current focus.
- [ ] Make sure the top section leads with current build lanes and public portfolio direction, not stale historical framing.
- [ ] Revisit the selected-project list and confirm the set still represents the strongest current signal.
- [ ] Tighten wording where the profile can better highlight web-first Bun/Astro work, Go systems work, Python automation work, and justified exceptions.
- [ ] Remove or rewrite any line that overstates maturity, activity, or stack uniformity.

Acceptance criteria:

- [ ] The root README reads as current truth, not aspiration.
- [ ] The project list and focus areas match Stephen's actual direction and public priorities.
- [ ] The README distinguishes active lanes from maintenance lanes cleanly.

### Phase 3 - Stack-doc coherence and routing hygiene

Work items:

- [ ] Re-audit `tech-stacks/README.md` against the individual stack docs for routing consistency.
- [ ] Verify `web-fullstack-tech-stack.md` and `web-frontend-tech-stack.md` still match Stephen's preferred browser-product direction.
- [ ] Confirm the recommended lane map stays honest about repo-specific exceptions and does not force weak rewrites.
- [ ] Tighten any stack-doc wording that drifts into hype, ambiguity, or contradictory defaults.
- [ ] Verify relative links across root docs and stack docs after any edits.

Acceptance criteria:

- [ ] A future agent can choose the correct lane quickly from `tech-stacks/README.md`.
- [ ] The docs clearly separate browser frontend work from true full-stack TypeScript web work.
- [ ] Exceptions are documented as intentional exceptions, not accidents or forgotten drift.

### Phase 4 - Optional portfolio structure expansion only if earned

Work items:

- [ ] Decide whether the repo now needs one additional stable supporting doc, such as a tightly curated project index or portfolio-routing doc.
- [ ] Add a new stable doc only if it reduces ambiguity that the root README should not carry alone.
- [ ] Keep any added doc current-state oriented and link it cleanly from the root README.
- [ ] Do not add placeholder folders, app scaffolding, or speculative content.

Acceptance criteria:

- [ ] Any added documentation earns its maintenance cost.
- [ ] The repo remains small and obviously useful.
- [ ] Nothing in the repo suggests a fake product surface or fake implementation roadmap.

### Phase 5 - Verification, ship, and retirement decision

Work items:

- [ ] Run the smallest useful verification for doc integrity and local links after edits.
- [ ] Review the diff for current-state wording and removal of stale framing.
- [ ] Commit the repo changes with a clean docs-focused commit message.
- [ ] Push to `origin` on the active branch.
- [ ] Decide whether this repo is still in an active evolution phase that justifies keeping `BUILD.md`.
- [ ] If the answer is no, fold any remaining current-state guidance into stable docs and remove this file in the final cleanup pass.

Acceptance criteria:

- [ ] The repo is committed, pushed, and consistent.
- [ ] Stable docs are sufficient for normal readers.
- [ ] `BUILD.md` exists only while it still adds real execution value.

## Notes for future agents

Use judgment, but be honest about fit.

This repo should reflect Stephen's current portfolio direction, including the stronger push toward Bun + TypeScript web products where that lane is the right fit. The honest alignment mechanism here is curation, positioning, and stack guidance, not pretending this repo itself needs a full-stack rewrite.

If you find yourself about to add an app framework here, stop and justify the repo-shape change explicitly first.
