# Missing-record clarification, 2026-11-16

**`unreadable-village` passes 3/3; the final suite passes 13/14 cases.** The
[receipt](issue-241-missing-record-clarification.json) retains every attempt, including failures
and incomplete evaluations. Its synthetic model answers are evaluation evidence.

[Issue #241](https://github.com/Kinprove/genealogy-research-recipes/issues/241) takes the
instruction-tightening option. Rule 1 in
[`SKILL.md`](../skills/genealogy-research-recipes/SKILL.md#how-to-use) now explicitly covers a
request to read or interpret a specific record the user has not supplied when the answer
depends on seeing it.
After any required privacy gate is satisfied, ask only for an image or link:
one question sentence and at most one short explanatory
sentence, then wait. Ask for identifying details after the reply only if still needed.
The other record-source scoping questions have the same sentence limit and explicitly defer
record types, collections, source lists and workflows until after the reply.

The example uses a parish register rather than the manifest in the existing `unreadable-village` case.
The clarification case, judge and thresholds are unchanged. The
[2026-11-12 report](behavioural-evaluation-2026-11-12.md) and its
[receipt](behavioural-evaluation-2026-11-12.json) retain the historical 0/3 clarification passes.

The initial proposal at `565b06f` passed 13/14 cases: `unreadable-village` passed 3/3, but
`russia-origin` sample 2 added passenger, naturalization and census suggestions before receiving
the scoping answer. That failure stands. The shared waiting instruction now explicitly limits
the explanation to one short sentence and defers those suggestions.

Release 1.20.0 and changes to twenty recipes, including GEDCOM, arrived on main during validation.
The final proposal integrates main at `1a62edd` and tests the shared waiting-limit edit at
`aad4be6f2d455bb40bfdcdabaf2f3abfd04569bb`. The earlier results remain in the receipt.

## Validation

- Both offline Python suites pass: 419 repository tests and 62 skill tests.
- Catalog and provenance checks pass for 143 recipes; evaluator static checks bind 14 cases
  and 170 guardrails. These checks do not establish model behavior.
- All 15 offline Markdown link tests pass. The locked Markdown linter reports no issues.

## Model evaluation

The unchanged repository evaluator used the locked CLI **2.1.322**, native `Read`, two workers,
and **`claude-opus-5-5` for both assistant and judge**, confirmed in the completed final transcripts.
Each case has three samples. Calls were isolated from local settings, user plugins, memory and
inherited session behavior. The skill was supplied literally as system instructions. These were
local subscription runs; no hosted model run is claimed. The historical run used CLI 2.1.318.

The [evaluation procedure](../docs/evaluation.md#before-merging-content-changes) was applied to
the unchanged release snapshot and complete proposed suite. Cases, judge, read requirements and
thresholds were not changed. Routing, regex and clarification checks require 3/3; the complete
rubric requires at least 2/3, with strict items requiring 3/3. Clarification cases have no rubric.

| Attempt | Cases passing | Recorded limitation |
| --- | --- | --- |
| Release 1.19.0 baseline | 9/10 | GEDmatch sample 2's judge omitted a required item; incomplete |
| Initial proposal `565b06f` | 13/14 | Russia clarification sample 2 gave source suggestions |
| Release 1.20.0 baseline, first login | 0/10 | All 30 attempts incomplete from a usage limit; behavior unassessed |
| Release 1.20.0 baseline, fallback login | 10/10 | All 30 samples passed |
| Integrated proposal `aad4be6` | 13/14 | GEDmatch sample 1 missed a required supplemental read |

The usage-limit fallback used the next configured login with the same isolated evaluator,
CLI and model pins. All failed and incomplete attempts remain separate; none was overwritten
or regraded. Raw transcripts and immutable source snapshots are retained locally; the receipt
records source commits, skill and harness hashes, contracts, answers, read coverage, verdicts,
observed models and transcript digests.

### Final results

| Case | Routing, regex and clarification | Complete rubric | Result |
| --- | --- | --- | --- |
| cm-relationship | 3/3 | 3/3 | pass |
| deportation-1944 | 3/3 | n/a | pass |
| family-interview | 3/3 | 2/3 | pass |
| gedcom-ancestry | 3/3 | 3/3 | pass |
| gedmatch-upload | 2/3 | 3/3 | fail |
| match-outreach-helper | 3/3 | 3/3 | pass |
| match-outreach | 3/3 | 3/3 | pass |
| memorial-proof | 3/3 | 3/3 | pass |
| parentage-proof | 3/3 | 3/3 | pass |
| photo-attribution | 3/3 | 3/3 | pass |
| russia-origin | 3/3 | n/a | pass |
| unreadable-village | 3/3 | n/a | pass |
| wato-ranking | 3/3 | 3/3 | pass |
| ystr-distance | 3/3 | 3/3 | pass |

`gedmatch-upload` sample 1 read the task recipe completely but omitted the required
`ai-for-dna-research` privacy section. Both privacy rubric items passed. Its 435-word reply used
the privacy-gate workflow, not the new scoping limit. The task, supplemental consent handoff and
judgment-selection rule are unchanged. Review found no demonstrated introduced defect; the
cause of this single read miss remains unresolved. The case stays **failed** under its 3/3 read
requirement, and no replacement sample was drawn. The read miss remains unresolved.
The clarification target in #241 passed 3/3.

`family-interview` sample 1 failed `ORAL-01`: its plan began recording before settling the topic,
audience and use. Its other two samples passed, meeting the unchanged 2/3 rubric threshold.
That missed item remains in the receipt.

### The three final missing-record replies

1. "Can you share an image or link to the manifest page? I need to see the handwriting before
   I can suggest what the village name says."
2. "Can you share an image or link to the manifest page? I need to see the handwriting before
   I can try to read the village name."
3. "Can you share an image or a link to the manifest page? I need to see how the village name
   is written before I can suggest what it might be."

These results cover the sampled requests and recorded configuration. The final overall score
is still 13/14, with a different failed case from the initial proposal. Changes between those
batches include the shared scoping instruction, integrated recipes, release version and login;
the runs do not isolate a causal effect on overall performance or establish future compliance.
