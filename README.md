# Stephen Sawyer

I build terminal-first tools for networking, security, and infrastructure. Python and Go for almost everything, Rust when it earns it. Local-first, self-hosted, no accounts required.

[dunamismax.com](https://dunamismax.com)

---

## Security & Networking

- [apisentry](https://github.com/dunamismax/apisentry) - OWASP API Top 10 scanner. Tests auth, authorization, rate limiting, injection, and SSRF against live endpoints.
- [flowhook](https://github.com/dunamismax/flowhook) - mitmproxy addons for capturing, replaying, mutating, and cataloging HTTP traffic.
- [wirescope](https://github.com/dunamismax/wirescope) - Live packet capture with top talkers, DNS enrichment, connection tracking, and PCAP export. Runs in a terminal.
- [bore](https://github.com/dunamismax/bore) - Encrypted peer-to-peer file transfer. Direct when possible, relay when NAT gets in the way. Zero trust, zero accounts.

## Operator Tools

- [patchworks](https://github.com/dunamismax/patchworks) - Diff two SQLite databases like `git diff` diffs source code. Schema changes, row-level deltas, and the SQL to reconcile them.
- [repokeeper](https://github.com/dunamismax/repokeeper) - Repo health daemon. Watches remotes, detects drift, runs your verification commands, stores results.
- [toolworks](https://github.com/dunamismax/toolworks) - Scripts, CLI helpers, and small automation tools that do one thing well.

## Rust Projects

- [cargo-compatible](https://github.com/dunamismax/cargo-compatible) - Check if your resolved dependency graph actually compiles on a target Rust version.
- [cargo-async-doctor](https://github.com/dunamismax/cargo-async-doctor) - Find async bugs that compile clean and pass Clippy but deadlock at runtime.
- [rust-async-field-guide](https://github.com/dunamismax/rust-async-field-guide) ([read it](https://dunamismax.github.io/rust-async-field-guide/)) - Twelve chapters on async Rust footguns with reproductions and verified fixes.

## Labs

- [scrybase](https://github.com/dunamismax/scrybase) - MTG Commander workbench. Deck management, pod tracking, matchup journal, meta analysis, Scryfall integration.

## Reference

- [tech-stacks](./tech-stacks/README.md) - How I build things and why.

---

## License

[MIT](LICENSE)
