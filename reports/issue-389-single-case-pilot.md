# Single reported cases in recipes: pilot, 2026-11-19

**Removing one single-case story from each of 19 recipes changed trap results little, and the two
host models moved in opposite directions. Sonnet 5.5 passed 66 of 76 trap answers with the story
and 60 without; Haiku 5.5 passed 35 with it and 42 without. In one recipe the story clearly
helped: without a counterexample in `us-freedpeople-record-recovery`, Sonnet missed the trap in 3
of 4 answers. Ordinary questions showed no difference.** Decision: compress stories recipe by
recipe and keep a counterexample to a tempting inference as one sentence with its citation.

[Issue #389](https://github.com/Kinprove/genealogy-research-recipes/issues/389) asked whether
single reported cases (a presenter's own family item, one researcher's find, one forum account)
earn their place in recipes. They cost context in every routed session and are often told as
events although nobody verified them. A concrete case might instead help a model recognise a
trap in the user's own evidence. The authoring rule went into
[`MAINTAINERS.md`](../MAINTAINERS.md) first; this pilot measured the possible benefit before any
existing recipe is edited.

## How common they are

Opus 5.5 read each of the 176 recipes with its source sidecar and marked every passage that tells
a single reported case. Documented facts (an archive's custody, a decree, a court decision, a
platform's documented behaviour) were excluded. It found such passages in 143 recipes: 1,917
passages, about 8% of recipe text. 1,791 passages in 139 recipes were eligible for the pilot:
stories the rule asks to compress, leaving out the rule's exceptions, passages with no lesson to
test, and the two recipes used to calibrate the pilot.

A blind second reading of 10 random recipes by Fable 5.2 matched 34 of the 37 passages Opus
marked; Opus missed 4 that Fable marked, and the two agreed on the passage's role in 25 of 34.
The remaining disagreements are borderline (a forum report, a presenter's wrong claim, a
platform demonstration). An earlier version of the marking prompt counted documented facts as
cases; the whole corpus was re-marked with the corrected prompt.

## Design

- **Selection.** 20 recipes, drawn at random (seed 389) in proportion to the eligible passages
  in each group of passage role (counterexample, sole support of a rule, illustration, pointer
  to a record type) and recipe kind (platform, record type, judgment), with at least five
  counterexamples. One passage per recipe was fixed before any question was written. One drawn
  passage proved to be a caveat about a superseded value, not a case, and was replaced by a
  seeded redraw from the same group.
- **Two variants.** The story variant is the recipe as published. The no-story variant removes
  only the chosen story. If the story carried an action the rule lacked, that action was added as
  one clause to both variants. Where the source sidecar retold the same story, the retelling was
  neutralised in both variants' copy. A script confirmed that the variants differ in one place;
  Fable 5.2 checked that nothing else changed.
- **Questions.** Per recipe, two trap questions with fictional user material, where the story's
  lesson decides the answer, and one ordinary question. Opus 5.5 wrote them from the no-story
  variant only. Fable 5.2 and the pilot lead (Opus 5.5) checked each for details copied from the story,
  wording that gives the answer away, and rubric items that reward the story's details.
- **Runs.** Sonnet 5.5 and Haiku 5.5 each answered with `SKILL.md`, the recipe variant and its
  sidecar in the prompt, no tools and no other files: two traps twice and the ordinary question
  once, per variant. 400 answers, none missing.
- **Grading.** Opus 5.5 graded each answer blind to the variant; an answer passes when every
  rubric item passes. Fable 5.2 regraded all 34 trap pairs whose variants got different grades
  and a seeded 10% of tied pairs (92 answers). The judges disagreed on 18 answers. The pilot lead
  read those with the variant hidden and one standard: pass when the answer does what the check is about, fail when it would
  still lead the user into the mistake. 15 passed and 3 failed; Opus had been the stricter judge
  in 17 of the 18.
- **Excluded after the run.** In `marks-and-brands-record-recovery` the recipe header quotes the
  tested story, so both variants carried it. That recipe is left out, which leaves 19.

## Results

Trap answers passed out of 4 per variant, with the story / without it.

| Recipe | Passage role | Sonnet 5.5 | Haiku 5.5 |
| --- | --- | --- | --- |
| `agent-research-project` | counterexample | 4 / 4 | 2 / 2 |
| `ftdna-practical-dna-workflows` | counterexample | 4 / 4 | 2 / 4 |
| `us-freedpeople-record-recovery` | counterexample | 4 / 1 | 0 / 1 |
| `soviet-personal-file-recovery` | counterexample | 4 / 4 | 4 / 3 |
| `russian-household-list-transcription-audit` | counterexample | 4 / 4 | 1 / 1 |
| `source-citation` | illustration | 4 / 4 | 3 / 3 |
| `convict-transportation-record-chain` | illustration | 4 / 4 | 3 / 4 |
| `periodical-index-search-retrieval` | illustration | 3 / 4 | 2 / 2 |
| `us-census-practical-workflows` | illustration | 2 / 2 | 0 / 0 |
| `russian-village-family-reconstitution` | illustration | 4 / 4 | 3 / 3 |
| `russian-imperial-service-record-recovery` | illustration | 4 / 4 | 3 / 4 |
| `german-military-record-period-routing` | pointer | 4 / 3 | 1 / 1 |
| `british-colonial-slave-registers` | pointer | 1 / 1 | 0 / 0 |
| `ydna-mtdna-interpretation` | sole support | 4 / 4 | 2 / 3 |
| `russian-orthodox-confession-list-reading` | sole support | 2 / 2 | 0 / 2 |
| `russian-revision-list-household-chaining` | sole support | 4 / 4 | 3 / 2 |
| `manuscript-collection-recovery` | sole support | 4 / 3 | 2 / 2 |
| `german-compensation-file-recovery` | sole support | 2 / 0 | 0 / 1 |
| `brazilian-parish-civil-registry-recovery` | sole support | 4 / 4 | 4 / 4 |
| **Total** | | **66 / 60** | **35 / 42** |

Change from removing the story, as the mean over recipes of the no-story pass rate minus the
story pass rate, with a 95% interval from resampling recipes:

| Model | Adjudicated grades | Opus grades alone |
| --- | --- | --- |
| Sonnet 5.5 | −7.9 points [−18.4, +1.3] | −11.8 points [−22.4, −1.3] |
| Haiku 5.5 | +9.2 points [0.0, +18.4] | +7.9 points [−1.3, +17.1] |

Whether the Sonnet change excludes zero depends on the grading standard. After adjudication,
of the trap pairs whose variants got different grades, Sonnet had 1 win and 7 losses for the
no-story variant, Haiku 9 wins and 2 losses.

**Where the story helped.** The rule fixed before the run flags a recipe when, for one model, the
no-story variant loses more pairs than it wins on each trap and at least two pairs net. Only
`us-freedpeople-record-recovery` on Sonnet met it. Its
[candidate step](../skills/genealogy-research-recipes/recipes/us-freedpeople-record-recovery.md#3-generate-and-eliminate-candidate-enslavers)
says to look for the man in the 1867 voter registers, then gives one Georgia example in which those
registers placed a freedman in a different county from his birthplace and later tax records. The
pilot added the example's action, "draw candidates from the 1867 county as well as the county of
the later records", to both variants. Even with that clause, Sonnet without the example treated
the 1867 register as a side lead and kept its candidates in the later county; with the example,
it searched the register and widened the candidate pool. The example shows a tempting inference
failing.

**Ordinary questions.** Sonnet passed 15 of 19 with and without the story; Haiku 11 with it and 12
without.

## Limits

- 19 recipes, one story removed from each. The pilot says nothing about removing several stories
  from one recipe, about recipe groups it did not sample, or about each passage role separately:
  Sonnet's counterexample losses all come from one recipe.
- The models received the recipe directly; routing through `SKILL.md` and partial reading were
  not tested. Only Anthropic models answered, and the user material was fictional.
- With 19 recipes a harm confined to a small share of recipes can go unseen.

## Decision

Compress single-case stories in existing recipes gradually, one recipe at a time: editing a
pending legacy paragraph requires a review of its sources. Keep a counterexample that shows a
tempting inference failing, as one sentence with its citation. `MAINTAINERS.md` now says so.
