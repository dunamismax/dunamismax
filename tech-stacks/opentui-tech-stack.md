# OpenTUI + TypeScript + Bun Tech Stack

Last reviewed: 2026-03-31

## Best Fit

Use this stack when the product needs:

- a real terminal UI with layout, focus, input, and component state
- a terminal-first operator console, workbench, or dashboard
- an interactive CLI that has outgrown flags and line prompts
- a serious local operator surface where terminal ergonomics are part of the product

This is the default **terminal frontend lane** in the workspace.

It is usually paired with a backend in Python or Go. When the product also needs a browser surface, pair this lane with [Astro](./web-frontend-tech-stack.md) as a sibling frontend. Add Vue only when the browser UI earns it.

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
| Backend pairing | Python or Go, chosen by product shape |
| Browser pairing | Astro on Bun when the product also needs the web, with Vue only when earned |

## What Matters About OpenTUI

From the official site and docs today:

- OpenTUI is a native terminal UI core written in Zig with TypeScript bindings
- the native core exposes a C ABI
- `@opentui/core` provides the imperative renderer and core primitives
- React and Solid bindings exist, but they are optional layers
- OpenTUI is currently Bun-exclusive, with Deno and Node support still in progress

That makes this a good fit for terminal products that need a real UI model without dragging a browser into the loop.

## Golden Path

1. Start with Bun.
2. Add `@opentui/core` first.
3. Build the first version with the imperative API.
4. Keep state local and explicit.
5. Reach for React or Solid only when the component tree clearly earns a reconciler.
6. Keep the backend boundary boring: local process, HTTP, or a small RPC surface.
7. If the product also needs a browser, add Astro as a sibling frontend instead of trying to force one UI stack to do both jobs. Add Vue only when the browser UI earns it.

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

- prefer OpenTUI constructs and primitives over wrapping everything immediately
- treat layout as product logic
- keep keyboard handling visible and test the important paths
- design for resize, focus, and partial redraw from the start
- if the app is mostly forms, lists, panes, search, and shortcuts, this stack is in its lane
- if the app mostly prints output and exits, a plain Go or Python CLI is probably the better answer

## Quality Bar

Every OpenTUI repo should pass:

```bash
bun install
bunx biome check .
bunx tsc --noEmit
bun test
```

If the repo has a smoke entrypoint, also run it once in a real terminal before shipping.

## Integration Guidance

Use this stack for the terminal UX, not for everything by default.

- Pair it with **Go** when the hard part is networking, daemon behavior, systems integration, or concurrency.
- Pair it with **Python** when the hard part is automation, APIs, data work, or service logic.
- Pair it with **Astro** when the product also needs a browser frontend. Add Vue only when the browser UI earns it.
- Leave **Rust** in the maintenance lane unless the repo is already Rust-native.

Cross-language boundaries should stay simple and observable.

## Dual Frontend Guidance

This workspace now explicitly allows the product to have both:

- a web frontend for browser access, sharing, and wider reach
- a terminal frontend for operators, power users, or workflows that are better in a terminal

Use dual frontends when they improve the product. Do not add a TUI just because it sounds cool.

## When Not To Use This Stack

- the tool is a straightforward CLI with flags, subcommands, and text output
- the primary interface is a browser, not a terminal
- the product needs a single static binary more than it needs a rich TUI
- the team does not want Bun in the toolchain
- the UI complexity is low enough that plain stdout wins

## Avoid By Default

- pulling in React or Solid on day one without a real state-management problem
- recreating browser UI habits inside the terminal
- hiding keybindings or focus rules in clever abstractions
- mixing the TUI layer directly into backend business logic
- building a second frontend that does not improve the operator workflow
