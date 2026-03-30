# OpenTUI + TypeScript + Bun Tech Stack

Last reviewed: 2026-03-30

## Best Fit

Use this stack when the product is mostly:

- a terminal-first application with real layout, focus, input, and component state
- an interactive CLI that wants a richer UX than flags and line prompts
- an operator console, dashboard, workbench, or local-first tool that belongs in the terminal
- a TUI where interface quality is part of the product, not an afterthought

OpenTUI is a native terminal UI core written in Zig with TypeScript bindings. Upstream also exposes a C ABI, but the default lane here is TypeScript on Bun.

## Opinionated Default

| Area | Default |
| --- | --- |
| Runtime and package manager | Bun |
| Language | TypeScript |
| TUI core | `@opentui/core` |
| Component model | Imperative core API first |
| Framework upgrade path | `@opentui/react` or `@opentui/solid` only when state and composition actually justify it |
| Lint and format | Biome |
| Type checking | `tsc --noEmit` |
| Testing | `bun test` |
| Build entrypoint | `bun run` |
| Browser companion | Python/FastAPI only if the product also needs a web surface |

## What Matters About OpenTUI

From the official docs and repo today:

- OpenTUI is built on a native Zig core with TypeScript bindings
- the project is Bun-first right now
- `@opentui/core` gives you the imperative renderer and core primitives
- React and Solid bindings exist, but they are optional layers
- the native core exposes a C ABI if a repo later needs another language at the boundary

That makes this a good fit for terminal products that need a real UI model without dragging a browser into the loop.

## Golden Path

1. Start with Bun.
2. Add `@opentui/core` first.
3. Build the first version with the imperative API.
4. Keep state local and explicit.
5. Reach for React or Solid only when the component tree is clearly earning a reconciler.
6. Keep the backend boundary boring. Local process, HTTP, or a small RPC surface.
7. If the product also needs a browser, keep that as a separate Python/FastAPI surface instead of forcing one UI stack to do both jobs.

## Default Repo Shape

```text
project/
  src/
    main.ts
    components/
    screens/
    state/
  tests/
  package.json
  bun.lock
  tsconfig.json
  biome.json
  README.md
```

Use `src/main.ts` as the obvious entrypoint. Keep screen layout, component primitives, and state transitions separate enough to stay readable, but do not invent framework cosplay.

## Component Guidance

- Prefer OpenTUI constructs and primitives over wrapping everything immediately.
- Treat layout as product logic. Terminal space is constrained, so be explicit.
- Keep keyboard handling visible and test the important paths.
- Design for resize, focus, and partial redraw from the start.
- If the app is mostly forms, lists, panes, search, and shortcuts, this stack is in its lane.
- If the app mostly prints output and exits, a plain Go or Python CLI is probably the better answer.

## Quality Bar

Every OpenTUI repo should pass:

```bash
bun install
bunx biome check .
bunx tsc --noEmit
bun test
```

If the repo has a small smoke entrypoint, also run it once in a real terminal before shipping.

## Integration Guidance

Use this stack for the terminal UX, not for everything by default.

- Pair it with **Go** when the hard part is networking, concurrency, daemon behavior, or systems integration.
- Pair it with **Python** when the hard part is automation, data work, APIs, or a server-rendered web companion.
- Leave **Rust** in its existing maintenance lane unless the repo is already Rust-native.

Cross-language boundaries should stay simple and observable.

## When Not To Use This Stack

- the tool is a straightforward CLI with flags, subcommands, and text output
- the primary interface is a browser, not a terminal
- the product needs a single static binary more than it needs a rich TUI
- the team does not want Bun in the toolchain
- the UI complexity is low enough that curses-style minimalism or plain stdout wins

## Avoid By Default

- pulling in React or Solid on day one without a real state-management problem
- recreating browser UI habits inside the terminal
- hiding keybindings or focus rules in clever abstractions
- mixing the TUI layer directly into backend business logic
- using this lane as an excuse to build a browser SPA later
