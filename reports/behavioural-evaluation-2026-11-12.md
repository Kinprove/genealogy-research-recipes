# Behavioural evaluation, 2026-11-12

**11 of 14 cases pass.** The run covers the recipes on `main` at `e206ee4`, seven merges after
release 1.16.0 (skill hash `f45810f2…`). Later recipe changes are not covered until a new run.

## What ran

- Harness: the [issue #208](https://github.com/Kinprove/genealogy-research-recipes/issues/208)
  branch at `6949570` (harness hash `f177aa2d…`), with the case contracts recorded in the receipt.
- CLI: the locked `ci-tools` version, 2.1.318, with the default reader (native `Read`, limited to
  `recipes/`). This is the configuration the hosted workflow uses.
- Every assistant and judge call ran isolated from the local Claude Code configuration: no
  user, project or local settings, CLAUDE.md files, auto memory, plugin skills or commands, and
  no inherited session variables.
- Models: `claude-opus-5-5` for the assistant and the judge, pinned and confirmed in every
  transcript.
- Login: a local subscription login, no API key. The hosted workflow did not run, because the
  repository has no `ANTHROPIC_API_KEY` secret.
- Three samples per case, 42 in total, with no transport errors and no reruns.

## Results

| Case | Routing, regex and clarification | Complete rubric | Result |
| --- | --- | --- | --- |
| cm-relationship | 3/3 | 3/3 | pass |
| deportation-1944 | 3/3 | n/a | pass |
| family-interview | 3/3 | 2/3 | pass |
| gedcom-ancestry | 3/3 | 1/3 | fail |
| gedmatch-upload | 3/3 | 3/3 | pass |
| match-outreach | 3/3 | 3/3 | pass |
| match-outreach-helper | 3/3 | 3/3 | pass |
| memorial-proof | 3/3 | 3/3 | pass |
| parentage-proof | 3/3 | 3/3 | pass |
| photo-attribution | 3/3 | 3/3 | pass |
| russia-origin | 3/3 | n/a | pass |
| unreadable-village | 0/3 | n/a | fail |
| wato-ranking | 3/3 | 3/3 | pass |
| ystr-distance | 1/3 | 3/3 | fail |

Clarification cases have no rubric question; their check is the judge's clarification verdict,
counted in the first column. The thresholds are unchanged: 3/3 for the first column and at least
2/3 for the rubric.

## Failures

- **gedcom-ancestry:** two answers offer redacting the living people's details (in one, only
  their names and birth years) as an alternative to their permission, so they fail `GED-04`. The
  recipe's own step reads "Leave out or redact the living and probably living", which allows that
  reading.
- **unreadable-village:** all three answers ask for the manifest image and several details
  (year, port, passenger line), with a list of reasons. The judge counts this as more than one
  focused question with a brief reason, so the clarification check fails.
- **ystr-distance:** two answers say a figure such as "about 5 generations" would be invented.
  The case's forbidden-wording pattern matches that quoted example. The judge found that none of
  the three answers gives its own generation estimate, and the rubric passed all three.

No case or threshold was changed after these results. Follow-up:
[#240](https://github.com/Kinprove/genealogy-research-recipes/issues/240) (GEDCOM recipe wording),
[#241](https://github.com/Kinprove/genealogy-research-recipes/issues/241) (clarification length)
and [#242](https://github.com/Kinprove/genealogy-research-recipes/issues/242) (Y-DNA case pattern).

## Comparison with the issue-97 runs

The [issue-97 report](issue-97-evaluation.md) recorded 14/14 on older skill bytes (13/14 before
one rubric question was corrected). Those runs loaded the runner's own Claude Code
configuration: their transcripts show a personal output style that shortens answers, 15 plugins,
63 skills and auto memory. The difference shows in `unreadable-village`: the short answers passed
there, and the full-length answers here do not. The two results are not a like-for-like
comparison.

## Scope

The cases name 11 of the 140 recipes. Each passing case is three sampled answers, not proof that
every answer will follow the recipe. The [JSON receipt](behavioural-evaluation-2026-11-12.json)
holds the case and guardrail contracts, every answer, its reads, its deterministic failures and
the judge's verdicts, the resolved models, and a SHA-256 digest of each transcript. The raw
transcripts are kept locally.
