# Contributing

Use the [recipe defect or install problem templates](https://github.com/Kinprove/genealogy-research-recipes/issues/new/choose)
to report a problem. For a security or privacy concern, follow
[SECURITY.md](SECURITY.md) instead of posting the details publicly. Use invented
or redacted examples in issues, pull requests and test fixtures.

## Local checks

From the repository root, use Python 3.11 or newer for both offline test suites:

```sh
python3 -B tests/run_all.py
python3 scripts/recipe_catalog.py --check
```

The runner exits non-zero if either suite fails or collects no tests. The npm
artifact check skips without npm outside CI; CI requires npm.

The tests use Python's standard library. The root suite also exercises the native
JavaScript adapter, so have Node.js available. For Markdown lint, use Node.js 22
or newer. Run the offline link/anchor tests and the same pinned linter as CI:

```sh
npm ci --prefix tests/markdown-links --ignore-scripts
npm test --prefix tests/markdown-links
npx --yes markdownlint-cli2@0.23.0 "**/*.md"
```

The configuration is [`.markdownlint-cli2.jsonc`](.markdownlint-cli2.jsonc).
Lint is check-only: do not add `--fix` or reformat generated recipe bytes. For
exported recipe content, fix its source or generator and regenerate. Existing
public recipes accept reviewed corrections in place, preserving their headers
and prior public corrections; see [MAINTAINERS.md](MAINTAINERS.md).

CI additionally validates the Claude plugin and runs integration checks against
pinned Hermes and OpenClaw runtimes, plus secret scans of working files and Git
history. Those jobs and their exact setup live in
[`.github/workflows/ci.yml`](.github/workflows/ci.yml).

## Recipe changes

Keep a correction focused: identify the file and passage, explain the resulting
behavior, and cite the evidence supporting the change. Separate a source's claim
from your inference, and keep dates, access limits and uncertainty visible. Update
the corresponding `sources/<slug>.md` when its evidence or attribution changes.

Follow [MAINTAINERS.md](MAINTAINERS.md) for recipe headers, source-check dates,
source/claim ledgers, new-recipe exports and privacy declarations. Give provenance
reports a stable locator such as `recipe-slug#S12` or `recipe-slug#C-claim-id`, the
defect class, exact passage, observed access status and observation date. An
outbound action needs its privacy
checkpoint, capability declaration and reviewed inventory entry. An existing
inventory entry or a passing test does not itself establish permission.

The marked routing region in `skills/genealogy-research-recipes/SKILL.md` and
capability region in `README.md` are generated. After changing recipe headers,
regenerate them instead of hand-editing those regions:

```sh
python3 scripts/recipe_catalog.py --write
python3 scripts/recipe_catalog.py --check
```

Shared instructions outside those markers can be edited directly. Do not move a
source-check date forward without rechecking the source.

## Pull requests

Open a focused pull request against `main`, link the issue it resolves, explain
the change, and state which checks you ran and their results. Add a regression
check when a behavioral defect needs one. Leave unrelated files and release
versions alone; coordinate releases with the maintainers. Include no private
research data or credentials in the diff or commit history.

## Preparing a release

Start from a clean checkout with all intended changes committed. Fetch tags so
the date check can use the preceding version's tag as well as the release history:

```sh
git fetch origin --tags
python3 scripts/bump_version.py 1.13.0 2026-11-07
```

Replace the example version and date with the intended release. The date is the
first public availability day in UTC, as defined in
[the release history](skills/genealogy-research-recipes/CHANGELOG.md).
The command updates all five host manifests, the skill's version/date, the test's
expected version and a new history row including its MIT anniversary. It refuses
staged, unstaged or untracked changes, a version that does not increase, invalid
versions/dates, future dates and dates before the preceding release. Ignored
build outputs do not make a checkout dirty.

Review the diff and run the checks above before committing and opening a release
pull request. If the public availability day changes before merge, correct the
skill stamp and the new history row together, then rerun the checks. Date checks
use UTC; when Git tags are absent (for example in a source archive or shallow
CI checkout), the history still enforces release-date ordering.

The bump command prepares files only. Tagging, host updates and live publication
are separate release actions; use [MAINTAINERS.md](MAINTAINERS.md) for ClawHub
validation and publication.
