# Maintainer notes

## Recipe headers and generated routing

Every file in `skills/genealogy-research-recipes/recipes/`, including the citation
and research-log references, starts with a YAML 1.2 header. Each line is a key
and a JSON-encoded value: quote strings and use JSON arrays/objects. This YAML
subset is deliberately strict so every supported host can validate it with
Python's standard library. Multiline YAML, implicit dates and duplicate keys
are rejected. The schema is enforced by
[`scripts/recipe_catalog.py`](scripts/recipe_catalog.py).

| Field | Contract |
| --- | --- |
| `id`, `title`, `summary` | Filename stem, exact first heading without the `Recipe:` prefix, and routing summary. |
| `kind` | `judgment`, `platform` (procedures for named tools/sites), or `records` (record types and custody). |
| `scope` | `platforms` and nonempty `tasks` string lists. |
| `triggers` | Nonempty list of task phrases; additional phrases appear in full router entries. |
| `privacy` | `none`, `living-person`, `genetic-self`, or `genetic-third-party`. This describes the gated data, not permission. |
| `gates` | `privacy-transfer` for any extension, data-transfer or contact action; otherwise empty. |
| `guardrails` | Nonempty list of `{id, text}` objects; IDs are globally unique. Full router entries copy the first rule verbatim, apart from wrapping; topic pointers defer to the header. |
| `handoff` | Recipe IDs to consult next; all must exist. Local recipe links and code filenames are also checked. |
| `checked`, `checked_basis` | ISO date and an exact dated excerpt from the source sidecar, or both `null` when no dated check is recorded. |
| `capabilities` | String lists for `browse`, `local_script`, `extensions`, `data_transfer`, and `contact`. Described actions, not automatically executed tools. |
| `router` | `tier` (`full` or `pointer`), topic `group`, and globally unique integer `order`. Full entries precede pointers. |

Use `text` for guardrails because existing rules include both prohibitions and
positive obligations; a `never` key would invert a rule such as “preserve the
original locator.” Keep the rule consistent with the body when changing it.
The generator removes the second hand-maintained routing copy; it does not
replace review of the recipe's claims.

`checked` is a dated source check, not a claim that every procedure was tested
in a live account. The migration conservatively uses the oldest explicit check
found in each source sidecar. Publication dates and archive-capture dates do
not count as checks. Source limitations, including summary-only and historical
checks, still apply. Platform checks expire after **90 days**, against the UTC
date, and fail CI; recheck the relevant documentation and update its evidence
before updating the header. Do not roll dates forward merely to pass the check.

The reviewed `tests/privacy_gate_inventory.json` remains independent. Its
actions must be declared in the header (`contact` for contact steps,
`data_transfer` for the other checkpoint kinds). A new outbound step needs its
checkpoint and inventory entry as well as its capability declaration. The
privacy gate applies even to an action absent from this inventory or header.

After editing headers, regenerate and validate:

```sh
python3 scripts/recipe_catalog.py --write
python3 scripts/recipe_catalog.py --check
python3 -B -m unittest discover -s tests -p 'test_*.py'
```

Only the marked regions in `SKILL.md` and `README.md` are generated. Edit shared
instructions outside them directly. Do not hand-edit generated entries or the
capability table. Tests reject a dangling recipe, duplicate rule ID, missing
privacy declaration, expired platform check or generated-output drift.

The Markdown CI job also checks relative links in every tracked Markdown file,
including heading fragments, images and reference links. Run it locally with:

```sh
npm ci --ignore-scripts
npm run test:markdown-links
```

The check resolves paths offline and uses `github-slugger` for heading IDs,
including Unicode and duplicate headings. Code examples and front matter are
excluded. Non-Markdown resources are checked for existence; their format-specific
fragments (such as PDF page numbers) are left alone. The npm development
dependencies are only for these checks; installed plugins do not need them.

For a **new** recipe, prepare its reviewed body and a complete header object
as JSON, plus its source sidecar and any privacy-inventory entries, then use:

```sh
python3 scripts/recipe_catalog.py --export-body /path/to/reviewed-body.md --metadata /path/to/header.json
```

This export emits the header and regenerates both consumers after validating
the candidate with the entire catalog. It refuses to overwrite a public recipe.
An upstream draft exporter may produce the body first; pass that body through
this step before committing it here. Existing public recipes are edited in
place, preserving their headers and public corrections.

## Locked maintainer and CI tools

Use Node 24.16 or newer (Node 24 or 26) and install the tools from the repository
root:

```sh
npm ci --prefix ci-tools --ignore-scripts
```

`ci-tools/package-lock.json` locks OpenClaw, Claude Code, markdownlint-cli2 and
ClawHub, including their transitive dependencies. Keep lifecycle scripts disabled.
The CI plugin checks, Markdown lint and ClawHub validation work without them;
optional native features of OpenClaw are outside these checks. Claude Code ships
`cli-wrapper.cjs` specifically for installs with scripts disabled: it launches
the locked platform binary directly, without the postinstall copy needed by
`.bin/claude`:

```sh
node ci-tools/node_modules/@anthropic-ai/claude-code/cli-wrapper.cjs plugin validate . --strict
ci-tools/node_modules/.bin/markdownlint-cli2 "**/*.md"
```

ClawHub validation selects the installed OpenClaw SDK explicitly; its default
would resolve the latest release. The OpenClaw runtime check installs the packed
plugin artifact so development tools are not copied into its temporary profile.

When changing a tool version, update `ci-tools/package.json`, regenerate the lock
with `npm install --prefix ci-tools --package-lock-only --ignore-scripts`, then
repeat the clean install and runtime checks. Commit both files. These tools are
development dependencies and are excluded from the published plugin artifact.

## Publishing to ClawHub

Use a clean checkout of the reviewed commit, with all host manifest versions
synchronized. Publish under the ClawHub `kinprove` owner using an account with
access to that owner. The `@kinprove/` package scope must match it. Install the
locked tools above first, and run these commands from the repository root.

```sh
ci-tools/node_modules/.bin/clawhub package validate . --openclaw ci-tools/node_modules/openclaw --out ../clawhub-validation --json
ci-tools/node_modules/.bin/clawhub package publish . --family code-plugin --owner kinprove --dry-run --json
```

Check that the dry-run reports `code-plugin`, the intended version and the exact
reviewed commit before making a separately authorized live publication. Keep
`--family code-plugin`: Claude manifests coexist in this repository, so automatic
family detection can choose a Claude bundle instead of the native OpenClaw package.
The npm artifact deliberately includes native OpenClaw code and the complete
skill/resources/license tree, not the other hosts' adapters or development files.

A successful dry-run is not a public release. Authenticate securely, publish the
same clean commit with the same flags (without `--dry-run`), and verify its
ClawHub publication/security-check status before announcing availability. Do not
publish to npm merely because this package uses an npm-style scoped name.

## Reproducible installs and audits

To make a direct Hermes repository install reproducible, add
`--ref <full-commit-sha>` to the install command. Public catalog inclusion does not
mean a package is maintained by the host or has received a full security audit.

The native adapters expose bundled instructions, not automatic access to your
DNA accounts or records. They do not make service calls, install an MCP server,
store credentials, send telemetry, or start background jobs. Individual recipes
can describe optional services and commands; executing those still requires the
host's appropriate tools, permissions and any service-specific credentials.

## Running the tests

Run both unit-test suites (the repository's `tests/` and the skill's own `tests/`) with:

```sh
python3 tests/run_all.py
```

It exits non-zero when a test fails or a suite collects no tests. The npm package test
skips when `npm` is not installed, except in CI.
