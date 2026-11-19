# Reading the privacy rules before a GEDmatch upload reply

The GEDmatch upload case checks two things a maintainer needs to distinguish. The
read record shows whether the assistant consulted the consent guidance. The answer
shows what it told the tester. In both runs flagged in
[issue #392](https://github.com/Kinprove/genealogy-research-recipes/issues/392),
the answer passed both privacy questions even when the assistant skipped the read.

## What the saved samples show

Each row below compares answers to the same raw-DNA upload request. Every sample
read the GEDmatch recipe in full. The four that opened the companion recipe also
read it in full (300 lines), covering *Verification & privacy discipline*. The
other two recorded a single failure, `Unread recipes: ai-for-dna-research`.

| Receipt and batch | Sample | Companion read | What the saved answer said about identifying the tester |
| --- | --- | --- | --- |
| [#241, `proposal_integrated`](issue-241-missing-record-clarification.json) | 1 | Missed | Asked about kit ownership and the matching option. Did not address whether hiding the name protects the genome. |
| #241, same batch | 2 | Complete | Asked about kit ownership and the matching option. Also omitted the limit of hiding the name. |
| #241, same batch | 3 | Complete | Distinguished using a display alias from redacting the genotype file. |
| [#385, `proposal_full_48ac975`](issue-385-privacy-gate-record-reuse.json) | 1 | Complete | Distinguished reducing the displayed name and email from de-identifying the genome. |
| #385, same batch | 2 | Missed | Asked about kit ownership and the matching option. Did not address whether hiding the name protects the genome. |
| #385, same batch | 3 | Complete | Described the raw file itself as identifying. |

All six asked whose kit it was, distinguished access or analysis from permission
to transfer it, and directed the tester to check GEDmatch's current visibility and
law-enforcement matching options. All six passed `GM-03` and `GM-02`. The
redaction comparison above illustrates guidance the section can contribute. It
was outside those two rubric questions and leaves all six verdicts intact.

## Decision

Keep the supplemental read mandatory and clarify when to make it. At both tested
commits (`aad4be6` and `48ac975`), the GEDmatch recipe told the reader to apply
the consent rules, then spelled out enough of the first reply to satisfy both
rubric questions locally. A reader could follow those instructions without opening
the link. The [companion section](../skills/genealogy-research-recipes/recipes/ai-for-dna-research.md#verification--privacy-discipline)
explains why the handoff matters even while an upload is under consideration.
Removing direct identifiers leaves raw DNA re-identifiable.

The [upload instructions](../skills/genealogy-research-recipes/recipes/gedmatch-practical-dna-workflows.md#before-starting)
now explicitly say to read that section before drafting the first reply. The
[case](../skills/genealogy-research-recipes/evals/cases/gedmatch-upload.yaml)
still requires the read in all three samples. Both historical proposals remain
failed on this case. The 1.20.0 and 1.22.0 release batches and the later
`proposal_full_b235c0e` batch passed it 3/3. The cause of either miss and the
long-run miss rate remain unknown.

## Checking the change

The [evaluation receipt](issue-392-gedmatch-upload-read.json) records the unchanged
release baseline, the proposed suite and a judge replay. The repository harness
used the native reader and locked CLI 2.1.322 with `claude-opus-5-5` for both
assistant and judge. The case, rubric and thresholds were fixed throughout.

The first baseline login hit its weekly limit on all 30 samples. On the fallback
login, release 1.22.0 passed 10/10 cases. All three GEDmatch samples read the
companion recipe and passed both rubric items.

The full proposed suite at `7a27a33` passed 15/16 cases. All three GEDmatch samples
read the full 499-line task recipe and the full 300-line companion. The judge
returned only `GM-03` for sample 2, omitting `GM-02`. This made GEDmatch the
sole failed case as run. Replaying those same three
answers with the repository evaluator produced two passing verdicts per answer.
The assistant transcripts, answers and read records match across the original run
and replay.
