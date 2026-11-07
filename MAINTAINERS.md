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
| `guardrails` | Nonempty list of `{id, text}` objects; IDs are globally unique. The router copies the first rule verbatim, apart from wrapping. |
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

## Publishing to ClawHub

Use a clean checkout of the reviewed commit, with all host manifest versions
synchronized. Publish under the ClawHub `kinprove` owner using an account with
access to that owner. The `@kinprove/` package scope must match it.

```sh
npx --yes clawhub@0.23.3 package validate . --out ../clawhub-validation --json
npx --yes clawhub@0.23.3 package publish . --family code-plugin --owner kinprove --dry-run --json
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
