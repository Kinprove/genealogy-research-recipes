# Keeping the skill in reach during long sessions

[Issue #776](https://github.com/Kinprove/genealogy-research-recipes/issues/776) separated three
reasons a long or busy research session gets less from this skill: the skill is not loaded, the
recipe list is lost when Claude Code summarizes the conversation, and the recipes on research logs
and long projects open only when the user asks for that output. This report records the checks on
the change.

## What changed

- "How to use" is now the first section of `SKILL.md`. "Version and updates" moved below the
  recipe list. Claude Code keeps the first 5,000 tokens of a skill after it summarizes a
  conversation ([skills documentation](https://code.claude.com/docs/en/skills)). The new opening
  paragraph ends at byte 1,928 of 57,789; the recipe list starts at byte 16,556. Where exactly the
  5,000 tokens end was not measured.
- That opening paragraph asks the agent to check the open recipe's `handoff` list and then the
  recipe list when the question moves on, and to load the skill again when the list is no longer in
  its context. For an investigation of more than one step, it names the
  [Research log](../skills/genealogy-research-recipes/recipes/research-documentation.md#research-log)
  section to read and three things to keep without being asked: the research question, a log of the
  searches run, including those that found nothing, and a list of next actions.
- The README gives a line a user can add to a project's own instructions, so that the skill loads
  before a project's tool guide. It is not tested here.

## Case contract

The [open-investigation case](../skills/genealogy-research-recipes/evals/cases/open-investigation-log.yaml)
asks where to start on a great-grandfather's parents, given an approximate birthplace, the family's
religion, an emigration year, a death place and a DNA match. It does not mention a log. The case
passes when all three samples read the Research log section of `research-documentation` and at
least two answers pass both rubric questions: `RESEARCH-DOCUMENTATION-01` (a log of each search,
including searches that find nothing, set up without being asked) and `RESEARCH-DOCUMENTATION-02`
(the research question stated and the next actions listed as items to keep and update). The second
guardrail is new; it quotes the recipe's sentence on pending actions. The case was committed at
`eaa4b3a` before the first model run and did not change afterwards.

## Model runs

The local evaluator used the native reader and the locked Claude Code 2.1.327 CLI with
`claude-opus-5-5` as assistant and judge. The [receipt](issue-776-session-durability.json) records
each batch's skill and harness hashes, summaries, every sample of the new case, and the other cases'
failing or rerun samples.

| Skill | Run | Result |
| --- | --- | --- |
| Release 2.2.0 (`83bf32b`) | New case | Failed. No sample opened `research-documentation`; no answer passed either rubric question. Each sample opened four to eight other recipes. |
| First wording (`eaa4b3a`) | Full suite | 17/18. All 17 existing cases passed. New case: no sample opened the recipe; `-01` passed 3/3 and `-02` 0/3. |
| Second wording, an uncommitted copy | New case | Failed. No sample opened the recipe; both rubric questions passed 3/3. |
| Third wording (`206a320`) | New case | Passed. All three samples read the recipe; two answers passed both questions. |
| `206a320` | Full suite | 16/18 as run. The new case passed again. |
| `206a320` | Judge-only replays | `gedcom-ancestry`: 3/3 answers passed in the second replay. `match-outreach`: 2/3. |

The first wording told the agent to keep the three things "as the research log describes". The
answers kept a log but did not open the recipe. The second wording asked for the section to be read
and the three things kept; the answers improved, but still without the read. The third wording names
the file and asks for the section to be read before answering.

Two existing cases failed in the final full suite:

- `gedcom-ancestry`: for one answer the judge returned one of the three rubric items, so the sample
  could not be scored. A first replay of the same answers had the same judge fault twice; a second
  replay scored all three answers as passing.
- `match-outreach`: one answer failed `OUT-01`, and the judge returned an incomplete verdict for
  another. The failing answer recommended a facts-only first message and added a second draft that
  states the relationship "as you asked". Across all runs of this case on 2026-11-22, release 2.2.0
  gave 3 failing `OUT-01` verdicts out of 9 (three runs), `206a320` 5 out of 10 valid verdicts
  (four runs, including the full suite) and the first wording 0 out of 3. In every failing verdict
  on either version, the recommended draft left the relationship out, but the answer added wording
  that names or suggests it: a second draft, an optional sentence, or an offer to write the direct
  version. The rates are not distinguishable at this size, and the receipt of
  [#391](issue-391-notes-confirmation.md) shows the same pattern on older skill bytes. It is
  tracked as [#777](https://github.com/Kinprove/genealogy-research-recipes/issues/777).

The ten-case release baseline in [docs/evaluation.md](../docs/evaluation.md) was not run in full:
the release was run on the new case and on `match-outreach`, the only existing case that failed on
the change for a reason other than a judge fault.

## After a context summary

One manual trace used Claude Code 2.1.330 through `claude -p` with `claude-opus-5-5`, the plugin
loaded from a checkout, no settings, memory, other plugins or MCP servers, and only the `Read` and
`Skill` tools. Turn 1 asked how to reach the record behind an index entry without a scan link. Then
`/compact` summarized the session. Turn 2 asked what to do about a man missing from a passenger
database.

The same thing happened with `eaa4b3a` and with release 2.2.0. In turn 1 the agent loaded the skill
and opened `polish-index-original-record-recovery` and `galicia-bukovina-habsburg-record-routing`.
After the summary, turn 2 loaded the skill again and opened `usa-immigration-search-recovery`. In
this setup the agent reloads the skill without being told to, so the trace does not show that the
new sentence is needed. A first attempt, with a read permission that blocked the recipe files,
reloaded the skill in the same places.

## Not covered

- A project with competing skills or a long session with many tools, where the skill was not
  loaded at all; the README line for that case is untested.
- Hosts other than Claude Code, and models other than `claude-opus-5-5`.
- A `SessionStart` hook shipped with the plugin. It was left out; whether the plugin should run its
  own code on a user's machine is an open decision in #776.
