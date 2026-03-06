#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "repos.json"
README_PATH = ROOT / "README.md"
REPOS_PATH = ROOT / "REPOS.md"

README_CURRENT_START = "<!-- BEGIN GENERATED CURRENT PROJECTS -->"
README_CURRENT_END = "<!-- END GENERATED CURRENT PROJECTS -->"
README_OTHER_START = "<!-- BEGIN GENERATED OTHER WORK -->"
README_OTHER_END = "<!-- END GENERATED OTHER WORK -->"

LANGUAGE_ORDER = [
    "TypeScript / React",
    "TypeScript (Mobile)",
    "TypeScript (CLI)",
    "Python",
    "Shell / Config",
    "Markdown / Docs",
]

CATEGORY_ORDER = [
    "Full-stack apps",
    "Self-hosted tools",
    "Mobile",
    "Developer tools",
    "Trading",
    "Bots / automation",
    "AI gateway deployments",
    "Infrastructure / ops",
    "Business / docs",
    "Profile / assets",
]

REPOS_PREFIX = """# Repository Index

> Complete index of Stephen Sawyer's (`dunamismax`) repositories.
> All repos live under `~/github/` and most are mirrored across GitHub and Codeberg.
> Generated from `data/repos.json` via `python3 scripts/generate_docs.py`.

---

## Source Control Strategy

### Dual-Remote Mirroring (GitHub + Codeberg)

Most repositories use a single `origin` remote with dual push URLs:

```
origin  git@github.com-dunamismax:dunamismax/<repo>.git   (fetch)
origin  git@github.com-dunamismax:dunamismax/<repo>.git   (push)
origin  git@codeberg.org-dunamismax:dunamismax/<repo>.git  (push)
```

One `git push` publishes to both hosts. This is an intentional resilience pattern — platform risk is not existential when source control is redundant across providers.

**Rules:**

- All remotes use **SSH**, never HTTPS.
- Fetch comes from GitHub. Push goes to both GitHub and Codeberg.
- New repos get dual push URLs wired immediately after clone or init.
- SSH host config and dedicated identities are maintained in `~/.ssh/config` for both providers.
- Use `bun run scry:sync:remotes` in the grimoire repo to verify and fix remotes across all projects.

---

## Repositories
"""


def load_repos() -> list[dict[str, object]]:
    return json.loads(DATA_PATH.read_text())


def sort_repos(repos: list[dict[str, object]], key: str) -> list[dict[str, object]]:
    return sorted(repos, key=lambda repo: int(repo[key]))


def format_readme_bullet(repo: dict[str, object]) -> str:
    emoji = repo["readme_emoji"]
    name = repo["display_name"]
    url = repo["github_url"]
    summary = repo["readme_summary"]
    prefix = f"{emoji} " if emoji else ""
    return f"- {prefix}**[{name}]({url})** — {summary}"


def replace_managed_block(text: str, start: str, end: str, body: str) -> str:
    start_marker = text.find(start)
    end_marker = text.find(end)
    if start_marker == -1 or end_marker == -1 or end_marker < start_marker:
        raise RuntimeError(f"Missing managed block markers: {start} / {end}")

    block_start = start_marker + len(start)
    return text[:block_start] + "\n" + body + "\n" + text[end_marker:]


def build_readme(repos: list[dict[str, object]], current_text: str) -> str:
    current_projects = sort_repos(
        [repo for repo in repos if repo["readme_section"] == "current_projects"],
        "readme_order",
    )
    other_work = sort_repos(
        [repo for repo in repos if repo["readme_section"] == "other_work"],
        "readme_order",
    )

    updated = replace_managed_block(
        current_text,
        README_CURRENT_START,
        README_CURRENT_END,
        "\n".join(format_readme_bullet(repo) for repo in current_projects),
    )
    return replace_managed_block(
        updated,
        README_OTHER_START,
        README_OTHER_END,
        "\n".join(format_readme_bullet(repo) for repo in other_work),
    )


def format_repo_section(repo: dict[str, object]) -> str:
    slug = repo["slug"]
    stack = ", ".join(repo["stack"])
    github_url = repo["github_url"]
    codeberg_url = repo["codeberg_url"]
    description = repo["description"]
    return "\n".join(
        [
            f"### {slug}",
            "",
            "| | |",
            "|---|---|",
            f"| **Type** | {repo['type']} |",
            f"| **Stack** | {stack} |",
            f"| **GitHub** | [dunamismax/{slug}]({github_url}) |",
            f"| **Codeberg** | [dunamismax/{slug}]({codeberg_url}) |",
            "",
            str(description),
        ]
    )


def render_bucket_table(
    repos: list[dict[str, object]],
    heading: str,
    column_name: str,
    bucket_key: str,
    ordered_buckets: list[str],
) -> str:
    grouped: dict[str, list[str]] = defaultdict(list)
    for repo in sort_repos(repos, "index_order"):
        grouped[str(repo[bucket_key])].append(str(repo["slug"]))

    lines = [
        f"## {heading}",
        "",
        f"| {column_name} | Repos |",
        "|---|---|",
    ]
    for bucket in ordered_buckets:
        names = ", ".join(grouped[bucket])
        lines.append(f"| **{bucket}** | {names} |")
    return "\n".join(lines)


def build_repos(repos: list[dict[str, object]]) -> str:
    sections = []
    for repo in sort_repos(repos, "index_order"):
        sections.append(format_repo_section(repo))

    language_table = render_bucket_table(
        repos,
        heading="By Language",
        column_name="Language",
        bucket_key="language_bucket",
        ordered_buckets=LANGUAGE_ORDER,
    )
    category_table = render_bucket_table(
        repos,
        heading="By Category",
        column_name="Category",
        bucket_key="category_bucket",
        ordered_buckets=CATEGORY_ORDER,
    )

    parts = [REPOS_PREFIX, "\n\n---\n\n".join(sections), language_table, category_table]
    return "\n\n".join(parts) + "\n"


def write_or_check(path: Path, expected: str, check: bool) -> bool:
    current = path.read_text()
    if current == expected:
        print(f"{path.name}: up to date")
        return True

    if check:
        print(f"{path.name}: needs regeneration", file=sys.stderr)
        return False

    path.write_text(expected)
    print(f"{path.name}: regenerated")
    return True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate README.md and REPOS.md from tracked repo metadata.")
    parser.add_argument("--check", action="store_true", help="Fail if generated docs are out of date.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repos = load_repos()

    readme = build_readme(repos, README_PATH.read_text())
    repos_doc = build_repos(repos)

    ok = True
    ok &= write_or_check(README_PATH, readme, args.check)
    ok &= write_or_check(REPOS_PATH, repos_doc, args.check)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
