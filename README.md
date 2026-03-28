# Stephen Sawyer

I build terminal-first tools for networking, security, and infrastructure. Go and Python are the default. Rust is mostly maintenance work on existing crates and reference repos. Local-first, self-hosted, no accounts required.

[dunamismax.com](https://dunamismax.com)

---

## Security & Networking

- [wirescope](https://github.com/dunamismax/wirescope) - Live packet capture with top talkers, DNS enrichment, connection tracking, and PCAP export. Runs in a terminal. `v1.0.0`
- [bore](https://github.com/dunamismax/bore) - Encrypted peer-to-peer file transfer over QUIC. Direct when possible, relay when NAT gets in the way. `v1.0.0`
- [flowhook](https://github.com/dunamismax/flowhook) - mitmproxy addon suite for capturing, replaying, mutating, and documenting HTTP traffic. Endpoint catalog, auth analysis, HAR/Burp export. `v1.0.0`

## Operator Tools

- [patchworks](https://github.com/dunamismax/patchworks) - SQLite database diff tool. Schema and row-level comparison, SQL migration generation, three-way merge, snapshot management, local web UI. `v1.0.0`
- [gitpulse](https://github.com/dunamismax/gitpulse) - Local-first git activity analytics. Honest commit signals without uploading source code.
- [toolworks](https://github.com/dunamismax/toolworks) - Scripts, CLI helpers, and small automation tools that do one thing well.

## Maintained Rust Projects

- [cargo-compatible](https://github.com/dunamismax/cargo-compatible) - Check if your resolved dependency graph actually compiles on a target Rust version. `v1.0.0`
- [cargo-async-doctor](https://github.com/dunamismax/cargo-async-doctor) - Find async bugs that compile clean and pass Clippy but deadlock at runtime. `v1.0.0`
- [rust-async-field-guide](https://github.com/dunamismax/rust-async-field-guide) ([read it](https://dunamismax.github.io/rust-async-field-guide/)) - Twelve chapters on async Rust footguns with reproductions and verified fixes. `v1.0.0`

## Apps

- [scrybase](https://github.com/dunamismax/scrybase) - MTG Commander workbench. Deck lab, pod tracking, matchup journal, meta analytics, tuning loop, Scryfall integration. `v2.0.0`
- [mtg-card-bot](https://github.com/dunamismax/mtg-card-bot) - Discord bot for Magic: The Gathering card lookups with live prices, legality, rulings, and Scryfall-powered embeds.

## Learning Resources

- [c-from-the-ground-up](https://github.com/dunamismax/c-from-the-ground-up) ([read it](https://dunamismax.github.io/c-from-the-ground-up/)) - C learning workbook. Progressive lessons from basics to systems programming, with the explanation in the comments. `141 stars`
- [go-web-server](https://github.com/dunamismax/go-web-server) - Go starter for server-rendered apps with Echo, Templ, HTMX, PostgreSQL, SQLC, and Mage. `66 stars`
- [hello-world-from-hell](https://github.com/dunamismax/hello-world-from-hell) - "Hello World" done the wrong way on purpose. A novelty C repo for the unhinged.

## Reference

- [tech-stacks](./tech-stacks/README.md) - How I build things and why.

---

## License

[MIT](LICENSE)
