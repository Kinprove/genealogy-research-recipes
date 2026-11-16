# Missing-record clarification, 2026-11-16

[Issue #241](https://github.com/Kinprove/genealogy-research-recipes/issues/241) takes the
instruction-tightening option. Rule 1 in
[`SKILL.md`](../skills/genealogy-research-recipes/SKILL.md#how-to-use) now explicitly covers a
request to read or interpret a specific record the user has not supplied when the answer
depends on seeing it.
After any required privacy gate is satisfied, ask only for an image or link:
one question sentence and at most one short explanatory
sentence, then wait. Ask for identifying details after the reply only if still needed.

The example uses a parish register rather than the manifest in the existing `unreadable-village` case.
The clarification case, judge and thresholds are unchanged. The
[2026-11-12 report](behavioural-evaluation-2026-11-12.md) and its
[receipt](behavioural-evaluation-2026-11-12.json) retain the historical 0/3 clarification passes.

## Validation

- Both offline Python suites pass: 419 repository tests and 62 skill tests.
- Catalog and provenance checks pass for 143 recipes; evaluator static checks bind 14 cases
  and 170 guardrails. These checks do not establish model behavior.
- All 15 offline Markdown link tests pass. The locked Markdown linter reports no issues.

Model validation is in progress; behavior on the changed instruction remains unassessed.
The [evaluation procedure](../docs/evaluation.md#before-merging-content-changes) requires the
ten guardrail cases on the unchanged current release and the complete suite on the proposed skill.
`unreadable-village` must pass three of three unchanged clarification checks; investigate all other
failures against baseline and history, and resolve any newly attributable regression.
An incomplete or failing `unreadable-village` keeps #241 open. Do not change the acceptance criteria to pass it.
