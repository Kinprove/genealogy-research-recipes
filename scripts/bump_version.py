#!/usr/bin/env python3
"""Prepare a release in a clean checkout; never commit, tag or publish it."""

import argparse
import datetime as dt
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JSON_MANIFESTS = ("package.json", "plugin.json", "openclaw.plugin.json", ".claude-plugin/plugin.json")
SKILL = "skills/genealogy-research-recipes/SKILL.md"
CHANGELOG = "skills/genealogy-research-recipes/CHANGELOG.md"
VERSION = re.compile(r"(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)")
STAMP = re.compile(r"^This copy is version (\S+), released (\d{4}-\d{2}-\d{2})\.$", re.MULTILINE)
HISTORY_ROW = re.compile(r"^\| (\S+) \| (\d{4}-\d{2}-\d{2}) \| (\d{4}-\d{2}-\d{2}) \|$", re.MULTILINE)


def version_key(version):
    if not isinstance(version, str) or not VERSION.fullmatch(version):
        raise ValueError(f"invalid version {version!r}; expected X.Y.Z without leading zeroes")
    return tuple(map(int, version.split(".")))


def release_day(value):
    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", value):
        raise ValueError("release date must be YYYY-MM-DD")
    try:
        return dt.date.fromisoformat(value)
    except ValueError as error:
        raise ValueError(f"invalid release date {value!r}: {error}") from error


def validate_release_date(day, earliest=None, today=None):
    today = today or dt.datetime.now(dt.timezone.utc).date()
    if day > today:
        raise ValueError(f"release date {day} is after today ({today}, UTC)")
    if earliest is not None and day < earliest:
        raise ValueError(f"release date {day} is before the previous release ({earliest})")


def previous_tag_date(root, version):
    """UTC creation day of the greatest lower version tag reachable from HEAD.

    Lightweight tags use their commit date; annotated tags use their tagger date.
    Source archives and shallow checkouts without tags have no tag bound.
    """
    try:
        result = subprocess.run(
            ["git", "for-each-ref", "--merged=HEAD", "--format=%(refname:strip=2) %(creatordate:iso-strict)", "refs/tags"],
            cwd=root, text=True, capture_output=True, check=False,
        )
    except FileNotFoundError:
        return None
    if result.returncode:
        return None
    current = version_key(version)
    candidates = []
    for line in result.stdout.splitlines():
        tag, _, timestamp = line.partition(" ")
        name = tag.removeprefix("v")
        if VERSION.fullmatch(name) and version_key(name) < current:
            day = dt.datetime.fromisoformat(timestamp).astimezone(dt.timezone.utc).date()
            candidates.append((version_key(name), day))
    return max(candidates)[1] if candidates else None


def replace_once(text, pattern, replacement, name):
    if len(re.findall(pattern, text, re.MULTILINE)) != 1:
        raise ValueError(f"{name}: expected exactly one release field")
    return re.sub(pattern, replacement, text, flags=re.MULTILINE)


def prepare_release(root, version, released):
    """Validate and render every change before writing any file."""
    target = version_key(version)
    day = release_day(released)
    validate_release_date(day)
    status = subprocess.run(
        ["git", "status", "--porcelain", "--untracked-files=normal"],
        cwd=root, text=True, capture_output=True, check=True,
    )
    if status.stdout:
        raise ValueError("working tree is dirty; commit or remove changes before preparing a release")

    files = (*JSON_MANIFESTS, "plugin.yaml", SKILL, "tests/test_manifest_versions.py", CHANGELOG)
    texts = {name: (root / name).read_text(encoding="utf-8") for name in files}
    stamps = STAMP.findall(texts[SKILL])
    if len(stamps) != 1:
        raise ValueError("SKILL.md must have exactly one version and release date")
    old_version, old_released = stamps[0]
    if target <= version_key(old_version):
        raise ValueError(f"version must increase from {old_version}")
    bounds = [release_day(old_released)]
    tag_day = previous_tag_date(root, version)
    if tag_day is not None:
        bounds.append(tag_day)
    validate_release_date(day, max(bounds))

    changes = {}
    for name in JSON_MANIFESTS:
        if json.loads(texts[name]).get("version") != old_version:
            raise ValueError(f"{name}: version disagrees with SKILL.md")
        changes[name] = replace_once(
            texts[name], r'^(\s*"version"\s*:\s*)"' + re.escape(old_version) + r'"',
            lambda m: m[1] + json.dumps(version), name,
        )
    changes["plugin.yaml"] = replace_once(
        texts["plugin.yaml"], r"^version:\s*" + re.escape(old_version) + r"[ \t]*$",
        f"version: {version}", "plugin.yaml",
    )
    changes[SKILL] = STAMP.sub(f"This copy is version {version}, released {released}.", texts[SKILL])
    changes["tests/test_manifest_versions.py"] = replace_once(
        texts["tests/test_manifest_versions.py"], r'^EXPECTED_VERSION = "' + re.escape(old_version) + r'"$',
        f'EXPECTED_VERSION = "{version}"', "tests/test_manifest_versions.py",
    )
    rows = list(HISTORY_ROW.finditer(texts[CHANGELOG]))
    if not rows or rows[0].group(1, 2) != (old_version, old_released):
        raise ValueError("CHANGELOG.md must start with the current SKILL.md release")
    # A 29 February release reaches its second anniversary on 28 February.
    try:
        mit = day.replace(year=day.year + 2)
    except ValueError:
        mit = day.replace(year=day.year + 2, day=28)
    row = f"| {version} | {released} | {mit} |\n"
    offset = rows[0].start()
    changes[CHANGELOG] = texts[CHANGELOG][:offset] + row + texts[CHANGELOG][offset:]
    return changes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("version", help="new X.Y.Z version")
    parser.add_argument("date", help="first public availability date, YYYY-MM-DD (UTC)")
    args = parser.parse_args()
    try:
        changes = prepare_release(ROOT, args.version, args.date)
        for name, content in changes.items():
            (ROOT / name).write_text(content, encoding="utf-8")
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        parser.exit(1, f"bump_version: {error}\n")
    print(f"Prepared {args.version} ({args.date}) in {len(changes)} files. Review and run the release checks.")


if __name__ == "__main__":
    main()
