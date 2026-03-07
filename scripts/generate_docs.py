#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "repos.json"
README_PATH = ROOT / "README.md"
README_CURRENT_START = "<!-- BEGIN GENERATED CURRENT PROJECTS -->"
README_CURRENT_END = "<!-- END GENERATED CURRENT PROJECTS -->"
README_OTHER_START = "<!-- BEGIN GENERATED OTHER WORK -->"
README_OTHER_END = "<!-- END GENERATED OTHER WORK -->"

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
    parser = argparse.ArgumentParser(description="Generate README.md from tracked repo metadata.")
    parser.add_argument("--check", action="store_true", help="Fail if generated docs are out of date.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repos = load_repos()

    readme = build_readme(repos, README_PATH.read_text())

    ok = True
    ok &= write_or_check(README_PATH, readme, args.check)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
