# AGENTS.md

> Runtime operations source of truth for this repository.
> This file defines how scry should operate in `dunamismax`.

---

## First Rule

Read `SOUL.md` first, then this file, then inspect `README.md` and `REPOS.md` before editing.

---

## Repo Scope

- Repo: `dunamismax`
- Purpose: profile and portfolio documentation repo.
- Primary files:
  - `README.md` (public profile presentation)
  - `REPOS.md` (repository index, stack map, mirroring policy)

---

## Owner

- Name: Stephen
- Alias: `dunamismax`
- Home: `/Users/sawyer`
- Projects root: `/Users/sawyer/github`

---

## Operating Contract

- Treat docs as operational truth, not marketing fluff.
- Keep claims factual and aligned with current repos.
- Prefer precise, current stack descriptions over generic labels.
- When repo inventory changes, update `REPOS.md` in the same session.
- Keep dual-remote policy explicit and SSH-first.

---

## Workflow

`Wake -> Explore -> Plan -> Edit -> Verify -> Report`

- **Explore**: read existing sections and identify stale claims.
- **Plan**: minimal, high-signal edits.
- **Edit**: preserve readable Markdown structure and visual style.
- **Verify**: validate links and key factual claims against local repos.
- **Report**: summarize changes and any remaining drift.

---

## Command Policy

- Use shell-native checks and git inspection for verification.
- Do not introduce app/toolchain dependencies into this docs-only repo.
- Avoid destructive operations; ask first for high-blast-radius actions.

### Verification commands

```bash
# quick content sanity for local path/remote conventions
rg -n "/home/sawyer|git@github.com:|git@codeberg.org:" README.md REPOS.md

# inspect local repo inventory from workspace root
for d in /Users/sawyer/github/*; do
  [ -d "$d" ] || continue
  git -C "$d" rev-parse --is-inside-work-tree >/dev/null 2>&1 && basename "$d"
done

# review doc diff
git diff -- README.md REPOS.md AGENTS.md SOUL.md
```

---

## Git Remote Sync Policy

- Use `origin` as the working remote.
- `origin` fetch URL:
  - `git@github.com-dunamismax:dunamismax/dunamismax.git`
- `origin` push URLs:
  - `git@github.com-dunamismax:dunamismax/dunamismax.git`
  - `git@codeberg.org-dunamismax:dunamismax/dunamismax.git`
- `git push origin main` must publish to both.
- Never force-push `main` unless Stephen explicitly asks.

---

## Done Criteria

A task is done when all are true:

- Requested doc changes are implemented.
- Repo facts and stack claims are accurate.
- Mirroring policy wording matches actual SSH setup.
- Diff is clear and reviewable.

---

## Living Document Protocol

- Keep this file current-state only.
- Update immediately when repo purpose, structure, or workflow changes.

---

## Platform Baseline (Strict)

- Primary and only local development OS is **macOS**.
- Assume `zsh`, BSD userland, and macOS filesystem paths by default.
- Do not provide or prioritize Windows/PowerShell/WSL instructions.
- If cross-platform guidance is requested, keep macOS as source of truth and treat Windows as out of scope unless Stephen explicitly asks for it.
- Linux deployment targets may exist per repo requirements; this does not change local workstation assumptions.
