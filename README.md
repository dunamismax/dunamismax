# Stephen Sawyer

Software developer building useful, durable, privacy- and security-focused things.

I work across Rust, Go, C, and Lua. Most of my public work is local-first software, developer tools, systems utilities, and security-conscious infrastructure — but I also build games and experiments that are fun, weird, or genuinely useful.

Everything is local-first. Everything is honest about what it can and can't do.

GitHub: <https://github.com/dunamismax>
Codeberg: <https://codeberg.org/dunamismax>

---

## Flagship projects

- [bore](https://github.com/dunamismax/bore) — privacy-first encrypted file transfer. No accounts, no cloud, end-to-end encrypted, direct peer-to-peer with relay fallback. Monorepo: Rust client with Go relay server, NAT traversal library, and admin dashboard.

## Developer tools

- [cargo-compatible](https://github.com/dunamismax/cargo-compatible) — Cargo subcommand for auditing dependency graphs against any Rust version. Lockfile-first MSRV compatibility. Rust.
- [GitPulse](https://github.com/dunamismax/gitpulse) — local-first git activity analytics. Tracks commits, sessions, and streaks across CLI, web dashboard, and desktop app. Rust.
- [repokeeper](https://github.com/dunamismax/repokeeper) — self-hosted repo health daemon with built-in doc verification. Watches repos, validates remotes, detects drift, runs doc-extracted commands in sandboxed temp dirs. Go.

## Data and infrastructure

- [Patchworks](https://github.com/dunamismax/patchworks) — git-style diffs for SQLite databases. Native desktop inspection, comparison, and SQL migration generation. Rust.
- [TraceScope](https://github.com/dunamismax/tracescope) — native desktop viewer for live Tokio console-subscriber telemetry with SQLite snapshot recording. Rust.
- [dbvault](https://github.com/dunamismax/dbvault) — SQLite backup and integrity toolkit. WAL-safe backups, integrity verification, rotation, and audit trail. Go.
- [sqlite-vfs-encrypt](https://github.com/dunamismax/sqlite-vfs-encrypt) — transparent AES-256 encryption for SQLite databases at the VFS layer. One `.c`/`.h`, zero application changes. C.
- [rtop](https://github.com/dunamismax/rtop) — ground-up Rust rewrite of htop. Linux and macOS as co-equal first-class platforms. Rust.

## Games and creative

- [Sand Sorcerer](https://github.com/dunamismax/sand-sorcerer) — Bevy action-puzzler / roguelite with reactive material simulation. Rust.
- [Deepblue](https://github.com/dunamismax/deepblue) — truecolor terminal aquarium with procedural fish, boids, and ecosystem simulation. Rust.
- [deepblue.lua](https://github.com/dunamismax/deepblue.lua) — Love2D port of Deepblue. Same simulation, real pixel rendering. Lua.
- [podforge](https://github.com/dunamismax/podforge) — local-first Commander night tracker for pods, decks, sessions, and playgroup stats. Go.
