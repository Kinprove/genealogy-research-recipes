#!/usr/bin/env bash
# Compare Git trees so deletions, renames and multi-commit pushes count.
set -eu
if git diff --quiet --no-renames "$1" "${2:-HEAD}" -- \
    __init__.py plugin.yaml plugin.yml plugin.json pyproject.toml 'requirements*.txt' uv.lock \
    scripts/build_dist.py tests/test_build_dist.py tests/check_hermes_runtime.py tests/test_hermes_plugin.py \
    skills/genealogy-research-recipes/scripts/ skills/genealogy-research-recipes/resources/ \
    .github/scripts/hermes-integration-changed.sh .github/workflows/{ci,dist,hermes}.yml; then
    echo false
else
    status=$?
    [[ $status == 1 ]] || exit "$status"
    echo true
fi
