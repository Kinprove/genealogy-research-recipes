# Maintainer notes

## Source and claim provenance

The [provenance report](PROVENANCE.md) lists reviewed current-state claims and
remaining migration debt. The [migration decision](docs/provenance-ledger.md)
explains the evidence boundary and deferred private-export integration.

Every source sidecar has a `provenance-ledger` block before its final Credits
section. Inside the YAML fence, `schema: 1`, `sources:` and `claims:` are literal;
each list item is one JSON object. Duplicate keys and IDs are errors. Keep source
URLs byte-exact: case, query order, escaping and fragments matter. Existing IDs
stay stable, including gaps; numbered bibliographies use `N1`, unlabelled bullets
`B1`, and separately retained additions `H3-addition-1` in their ledgers.

To review a source, set `review` to `reviewed`, classify `kind` and `access`, and
record the actual retrieval date and an exact, dated `basis` from the bibliography.
Do not equate publication or archive-capture dates with retrieval. `unknown`
means no reviewed access record; preserve unknown rights as null. Separate bundled
URLs into distinct bibliography entries before giving them an access status.
`entry_sha256` binds the full parsed entry, including its limitations; use the
`source_entries()` and `digest()` functions in `scripts/provenance.py` after an
intentional edit. Updating a digest is not a source recheck.

To review a claim, retain its ID, set `review` to `reviewed`, classify its `kind`
and `stated_as`, and record a unique, exact paragraph `anchor` and its source IDs.
The paragraph's markers must match those IDs. `--write` generates each source's
reverse `claims` list in claim order; `--check` rejects drift. A non-read source requires an `observation`,
a dagger on its marker and visible attributed/limited-access wording. Partial
reads require a visible qualification. A factual claim cannot use a pending
source. Checks validate the representation; review must still establish that
the cited source supports each statement in the paragraph.

Only prose citations, dates and qualifications count. The pinned `markdown-it`
and `parse5` parsers extract rendered prose; code, comments, HTML attributes and
Markdown link destinations/titles (including reference definitions) cannot supply
evidence. Visible link labels remain available. Every supporting source needs
at least one nonempty citation context. Raw anchors and hashes remain exact;
sentence checks use offsets within the parsed prose, not within the raw anchor.

For `platform-ui`, `fee`, `portal-availability` and `custody`, record `checked`
and a separate `[S1 @YYYY-MM-DD]` marker for each supporting source. Fees and
portal availability expire after 90 days; platform UI and custody after 180.
History, methods and examples have no automatic expiry. These claim dates do
not replace the catalog header's independently enforced platform check.

New or changed factual/cited paragraphs need ledger entries. The detector catches
domains, currency, selected current-state phrases and custodian names; it cannot
discover every factual assertion. New source entries must also be reviewed.
The fixed `tests/provenance_legacy.json` fingerprints only the initial pending
records. Do not add exceptions or reset it to make an edit pass. Regeneration
prunes resolved exceptions but cannot enroll new ones:

```sh
npm ci --prefix tests/markdown-links --ignore-scripts
python3 scripts/provenance.py --write
python3 scripts/provenance.py --check
python3 -B -m unittest discover -s tests -p 'test_provenance.py'
```

`--import-legacy` is a one-time migration command and refuses an existing
inventory or ledger. Normal write/check commands validate the entire candidate
before changing files. No command fetches URLs, changes statuses, advances dates
or enrolls new exceptions. #95 closed on the structural scope recorded in the
migration decision's closeout: a legacy record is reviewed when an edit changes
it, not in a bulk pass.

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

Keep material source limitations beside the affected claim in the recipe as well
as in its source sidecar. Distinguish a search-result extract, an unread page, a
publisher's description and a source actually read. If another inspected source
supports the claim, cite that support explicitly. Review this at claim level:
keywords such as `403` or `search-result` can describe an earlier failed fetch
followed by a successful reading, and do not by themselves make a claim unverified.

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
npm ci --prefix tests/markdown-links --ignore-scripts
npm test --prefix tests/markdown-links
```

The check resolves paths offline and uses `github-slugger` for heading IDs,
including Unicode and duplicate headings. Code examples and front matter are
excluded. Non-Markdown resources are checked for existence; their format-specific
fragments (such as PDF page numbers) are left alone. The dependencies and lockfile
live in the private `tests/markdown-links` package; installed plugins and the
release version script do not need them.

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

Use relative Markdown links for bundled files in recipes and `SKILL.md`. A
GitHub blob URL selects a separate copy and needs network access; the offline
regression suite rejects these self-repository URLs regardless of their ref.

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

## Release distributions

`main` is the only hand-edited source. The `dist/claude-directory` and
`dist/hermes-catalog` branches are generated; never edit them by hand. Configure branch
protection so only the release distribution workflow can write to `dist/*`.

After publishing a GitHub release, `.github/workflows/dist.yml` builds all three targets
from the release tag's commit. Each changed branch tree gets one commit whose parent is
the previous distribution head; the first build creates a root commit. Identical trees
are skipped, a release older than the source of the current distribution head is
skipped for the branches (its ZIP is still uploaded), the release must already be
published, and pushes never force-update history. The workflow also attaches
`genealogy-research-recipes-<version>.zip` to the release for OpenAI. To retry, or to
rebuild the same release after changing the build rules, run the workflow manually with
the existing release tag as its `tag` input.

To inspect a release locally, use empty output directories:

```sh
python3 scripts/build_dist.py --target claude-directory --source <release-sha> --out dist/claude-directory
python3 scripts/build_dist.py --target hermes-catalog --source <release-sha> --out dist/hermes-catalog
python3 scripts/build_dist.py --target openai-plugin --source <release-sha> --out dist/openai-plugin
python3 scripts/build_dist.py --check-claude dist/claude-directory
python3 scripts/build_dist.py --check-links dist/claude-directory
python3 scripts/build_dist.py --check-links dist/hermes-catalog
python3 scripts/build_dist.py --check-links dist/openai-plugin/*.zip
```

The builder reads only `git archive <sha>`, ignoring working-tree changes and untracked
files. It fails on missing allowlisted inputs. Claude's tree omits scripts and the
`sources/` sidecars, renames each `NOTICE` to `NOTICE.md`, and points every link and path
mention of `sources/` at the same files on GitHub, pinned to the release SHA. Claude's
directory validation timed out on the full 9.4 MB tree and passed at 6.5 MB, so the
policy check refuses a Claude tree over 6 MiB. Hermes and OpenAI retain the offline
Beider helper; the OpenAI ZIP has sorted entries, fixed timestamps and fixed permissions.
The checks validate Claude's file policy and relative Markdown destinations inside each
built tree (or ZIP); the repository's Markdown suite separately checks heading anchors.

After a release, update the Hermes catalog pin to the full `dist/hermes-catalog` commit,
with the release version. Disclose that it is a generated branch built by the public
workflow from the named source release SHA. Upload the release ZIP to OpenAI manually;
attaching it to GitHub does not publish a directory listing. Anthropic's directory
submission must track `dist/claude-directory`; switching that submission and configuring
branch protection are separate owner actions.

## Running the tests

Run both unit-test suites (the repository's `tests/` and the skill's own `tests/`) with:

```sh
python3 tests/run_all.py
```

It exits non-zero when a test fails or a suite collects no tests. The npm package test
skips when `npm` is not installed, except in CI.
