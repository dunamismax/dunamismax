#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "featured_repos.json"
README_PATH = ROOT / "README.md"
README_START = "<!-- BEGIN GENERATED FEATURED REPOS -->"
README_END = "<!-- END GENERATED FEATURED REPOS -->"
REQUIRED_KEYS = {"name", "url", "summary"}


def load_projects() -> list[dict[str, str]]:
    projects = json.loads(DATA_PATH.read_text())

    for index, project in enumerate(projects):
        missing = REQUIRED_KEYS - project.keys()
        if missing:
            missing_keys = ", ".join(sorted(missing))
            raise RuntimeError(f"Project #{index} is missing required keys: {missing_keys}")

    return projects


def format_project(project: dict[str, str]) -> str:
    return f"- **[{project['name']}]({project['url']})** - {project['summary']}"


def replace_managed_block(text: str, body: str) -> str:
    start_marker = text.find(README_START)
    end_marker = text.find(README_END)
    if start_marker == -1 or end_marker == -1 or end_marker < start_marker:
        raise RuntimeError("Missing README managed block markers")

    block_start = start_marker + len(README_START)
    return text[:block_start] + "\n" + body + "\n" + text[end_marker:]


def build_readme(projects: list[dict[str, str]], current_text: str) -> str:
    body = "\n".join(format_project(project) for project in projects)
    return replace_managed_block(current_text, body)


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
    parser = argparse.ArgumentParser(description="Generate README.md from featured repos.")
    parser.add_argument("--check", action="store_true", help="Fail if README.md is out of date.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    projects = load_projects()
    readme = build_readme(projects, README_PATH.read_text())

    ok = write_or_check(README_PATH, readme, args.check)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
