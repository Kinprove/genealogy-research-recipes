#!/usr/bin/env python3
"""Check release identity and ClawHub CLI output; never upload or authenticate."""

import argparse
import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME = "@kinprove/genealogy-research-recipes"
REPOSITORY = "Kinprove/genealogy-research-recipes"


def require_fields(actual, expected, label):
    if not isinstance(actual, dict):
        raise ValueError(f"{label}: expected a JSON object")
    for key, value in expected.items():
        if actual.get(key) != value:
            raise ValueError(f"{label}.{key}: expected {value!r}, got {actual.get(key)!r}")


def release_version(ref, package):
    require_fields(package, {"name": NAME}, "package")
    version = package.get("version")
    if not isinstance(version, str) or not re.fullmatch(r"(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)", version):
        raise ValueError("package.version must be X.Y.Z without leading zeroes")
    if ref != f"refs/tags/v{version}":
        raise ValueError(f"dispatch at refs/tags/v{version}, not {ref!r}")
    return version


def verify_preview(data, version, commit, tag):
    require_fields(data, {
        "name": NAME,
        "family": "code-plugin",
        "version": version,
        "commit": commit,
        "source": f"github:{REPOSITORY}@{tag}",
    }, "publish")


def verify_publication(data, version, commit, tag):
    verify_preview(data, version, commit, tag)
    require_fields(data, {"publicationStatus": "published", "status": "published"}, "publish")


def verify_inspection(data, version, commit, tag):
    require_fields(data, {}, "inspect")
    require_fields(data.get("package"), {"name": NAME}, "inspect.package")
    require_fields(data.get("owner"), {"handle": "kinprove"}, "inspect.owner")
    release = data.get("version")
    require_fields(release, {"version": version}, "inspect.version")
    verification = release.get("verification")
    require_fields(verification, {
        "sourceRepo": REPOSITORY, "sourceCommit": commit, "sourceTag": tag,
    }, "inspect.version.verification")
    # Trusted publishing currently leaves this false. Report it, never upgrade it.
    return verification.get("hasProvenance")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("context", "preview", "published", "inspect"))
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.path.read_text(encoding="utf-8"))
        package = data if args.mode == "context" else json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
        ref = os.environ["GITHUB_REF"]
        version = release_version(ref, package)
        if args.mode == "context":
            print(version)
            return
        commit = os.environ["GITHUB_SHA"]
        tag = ref  # ClawHub records the full tag ref of a trusted publish
        if args.mode == "preview":
            verify_preview(data, version, commit, tag)
        elif args.mode == "published":
            verify_publication(data, version, commit, tag)
        else:
            provenance = verify_inspection(data, version, commit, tag)
            print(f"Registry hasProvenance: {json.dumps(provenance)} (reported separately from trusted publishing; see #230).")
        print(f"{args.mode} verified: {NAME}@{version} ({commit})")
    except (OSError, ValueError, KeyError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
