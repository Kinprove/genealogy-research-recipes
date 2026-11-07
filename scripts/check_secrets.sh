#!/usr/bin/env bash
# Run from the checkout to scan. Use the exported config without claiming a
# comparison with the private source, which is unavailable in public CI.
set -euo pipefail

if [ ! -f .gitleaks.toml ]; then
  echo "::error::.gitleaks.toml is missing — copy it from the canonical source during the export round."
  exit 1
fi

# gitleaks v8.30.1 — the same immutable image for both scan modes.
image=ghcr.io/gitleaks/gitleaks:v8.30.1@sha256:c00b6bd0aeb3071cbcb79009cb16a60dd9e0a7c60e2be9ab65d25e6bc8abbb7f
docker run --rm -v "${PWD}:/scan:ro" "$image" \
  dir --config /scan/.gitleaks.toml --exit-code 1 --redact /scan
docker run --rm -v "${PWD}:/scan:ro" "$image" \
  git --config /scan/.gitleaks.toml --exit-code 1 --redact --log-opts=--all /scan
