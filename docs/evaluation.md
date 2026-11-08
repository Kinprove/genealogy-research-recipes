# Evaluation

The recipes are tested in two tiers: offline checks that run in CI on every change, and a
behavioural tier that gives an agent synthetic research questions.

## Offline tier

The offline tier runs in the existing unittest CI job. It checks that every recipe is routed,
every local recipe link and fragment resolves (also in the real npm artifact), and every case's
guardrail ID exists in a recipe header with a quote still present in the body. Platform
documentation-check dates expire after 90 days; future dates fail too. The suite uses the
canonical header parser, schema, source-check evidence and generated-output checks from
[`scripts/recipe_catalog.py`](../scripts/recipe_catalog.py). Case-specific guardrails are added
to the existing headers and must quote the recipe body; the catalog's first routing rule
stays first. Every platform header requires a dated source check.

```sh
python3 -B -m unittest discover -s tests -p 'test_recipe_evals.py' -v
python3 skills/genealogy-research-recipes/evals/run_evals.py --static
python3 skills/genealogy-research-recipes/evals/run_evals.py --output eval-results
```

## Behavioural tier

The behavioural tier has [ten starting guardrail cases, a helper-consent variant and three ambiguity cases](../skills/genealogy-research-recipes/evals/cases/),
with synthetic materials only. It appends the literal `SKILL.md` as system instructions to
Claude Code, provides a read-only `read_file` tool over `recipes/`, and records successful
reads and line coverage, and checks the answer with regexes and an independent rubric call.
Routing and regex checks must pass three of three samples; at least two samples must pass
all rubric questions. A denied read, missing sample, invalid judge response or timeout cannot
pass. Task recipes must be read in full; judgment recipes may be read at their rules sections.
Recipes named in `read_sections` are mandatory supplements, except alternatives selected by
`any_of`. Cases bind required judgment sections to returned body-line spans: opening only a title or
Goal cannot satisfy them. Denied, unfinished and out-of-scope reads fail even after another
successful read. A subset replay checks the saved fixtures used by that subset.
`optional_read_sections` binds the rules of additional judgment recipes when opened; it does
not require those additional routes. Their rules still need complete coverage.
Questions in the rubric are bound to exact recipe sentences and their current body line numbers.
Clarification cases must stop at one focused question and a brief reason, waiting for the
user's answer before any source list or workflow.
The `.yaml` cases use JSON syntax, a YAML 1.2 subset; headers use the strict subset described
in [MAINTAINERS.md](../MAINTAINERS.md). The offline tier needs only Python's standard library.
Evaluation tooling and fixtures are development files
and are excluded from the installed npm package.

## Running the model workflow

[The model workflow](../.github/workflows/behavioural-evals.yml) runs manually and on
same-repository PRs with the `behavioural-evals` label. Fork PRs skip it; without the
`ANTHROPIC_API_KEY` repository secret it reports a credential skip, not a model pass. The
optional `EVAL_MODEL` and `EVAL_JUDGE_MODEL` repository variables select the models; otherwise
the CLI uses its normal configured model. Pin these variables for comparisons across model
updates; each CLI transcript records the actual resolved model. Full assistant
and judge transcripts, answers, case contracts and the skill hash are retained as artifacts
for 30 days. Locally, an authenticated CLI works without an API key; `--profile claude3`
uses that profile's normal shell alias, settings and loaded plugins. Evaluation invocations
use only the scoped evaluation MCP server, with built-in and other connected tools unavailable;
the profile itself is not reconfigured. The server rejects paths and symlinks outside `recipes/`.
The judge uses schema-validated structured output and sees the same fixtures.
For profiles that shorten large MCP outputs, `--reader native` uses native `Read` with
an explicit bounded line limit to read each selected file completely, matching the server's
complete-file default, and denies MCP tools instead. It requests `allow_large` for recipes
above Read's default token limit. The same line-coverage and
case requirements apply; a shortened response cannot pass as a complete recipe read.

## Before merging content changes

Before merging content changes, run the ten guardrail cases against an unchanged snapshot
of the current release, then run the complete suite against the proposed skill. For example,
`--baseline --skill /path/to/released/skill --output baseline-results` preserves the released
bytes and reports their static defects alongside the behavioural results. The baseline is
measured against the current case and guardrail contract; an absent historical instruction
can be a content gap rather than model disobedience. A failure is evidence to investigate,
not permission to weaken a case. `--case <id>` selects a bounded
rerun. Results are written into a new directory on each run so a retry cannot overwrite evidence.
Replay retains the original guardrail contract and raw traces. Recorded CI paths can be read
against a local copy only after its skill hash and selected case contracts match.

## Results

The [local evaluation report](../reports/issue-97-evaluation.md) records the observed results,
preserved failures, transport repairs and remaining acceptance gates.
Issue #97's owner-approved gate retains the failed release baseline and requires all
revised-candidate cases to pass; merge authorization is a separate decision.
Current-candidate cases can be validated with the authenticated local CLI profile.
Hosted model runs are optional and have no scheduled trigger.
