# Stephen Sawyer

Systems developer focused on encryption, networking, privacy, and performance.

I build tools in **Go**, **Zig**, and **C**, backed by **PostgreSQL** and **SQLite**. Python for data work and scripting. Everything is local-first. Every tool earns its place by solving a real problem.

---

## Stack

| Role | Languages |
|---|---|
| Primary | Go, Zig, SQL |
| Supporting | C, Python |

Core interests: encrypted communications, network protocols, privacy tooling, database internals, and high-performance systems.

---

## Projects

### Go

[bore](https://github.com/dunamismax/bore) / Privacy-first encrypted file transfer. No accounts, no cloud. End-to-end encrypted with Noise protocol and ChaCha20-Poly1305. Peer-to-peer with relay fallback.

[dbvault](https://github.com/dunamismax/dbvault) / SQLite backup and integrity toolkit. WAL-safe online backups, manifest-driven tracking, integrity verification, and rotation policies.

[repokeeper](https://github.com/dunamismax/repokeeper) / Self-hosted git repo health monitoring daemon. Watches remotes, detects drift, validates documentation in sandboxed environments, stores results in SQLite.

[gitpulse](https://github.com/dunamismax/gitpulse) / Local-first git activity analytics. Tracks commits, sessions, and streaks across repositories. CLI and web dashboard.

[patchworks](https://github.com/dunamismax/patchworks) / SQLite database diffing, schema comparison, and SQL migration generation. CLI tool for inspecting what changed between two database states.

[tracescope](https://github.com/dunamismax/tracescope) / Go runtime observability tool. Visualizes goroutine counts, GC pauses, memory stats, and pprof data with snapshot recording to SQLite.

[podforge](https://github.com/dunamismax/podforge) / Local-first MTG Commander game-night tracker. Players, decks, pods, sessions, match history. SQLite-backed, zero cloud dependency.

### Go / Python / SQL

[0xvane](https://github.com/dunamismax/0xvane) / Local-first algorithmic trading workbench. Research, backtesting, paper trading, live execution, and risk management. Go engine, Python research scripts, PostgreSQL data layer.

### Zig

[rtop](https://github.com/dunamismax/rtop) / Ground-up terminal system monitor. Full process table, CPU/memory/swap meters, tree view, sort, search, and filter. An htop replacement built from scratch.

### C

[sqlite-vfs-encrypt](https://github.com/dunamismax/sqlite-vfs-encrypt) / Transparent AES-256-GCM encryption for SQLite at the VFS layer. Every page encrypted before disk write, decrypted on read. Uses libsodium. Zero application changes required.
