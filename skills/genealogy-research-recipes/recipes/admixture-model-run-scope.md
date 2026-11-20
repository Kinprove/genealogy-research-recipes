---
id: "admixture-model-run-scope"
title: "Record the run scope before reading a G25, calculator or qpAdm admixture result"
summary: "Record the run scope of a G25, calculator or qpAdm admixture result before reading it."
kind: "judgment"
scope: {"platforms": [], "tasks": []}
privacy: "genetic-third-party"
gates: ["privacy-transfer"]
guardrails: [{"id": "ADMIXTURE-MODEL-RUN-SCOPE-01", "text": "Nothing in this recipe establishes an ancestor, an origin locality or a relationship. A result that disagrees with a documented pedigree may make a candidate less likely. It never rules one out."}]
handoff: []
checked: null
checked_basis: null
capabilities: {"browse": [], "local_script": [], "extensions": [], "data_transfer": ["third-party-tool"], "contact": []}
router: {"section": "DNA", "group": "Ethnicity, admixture and match outreach", "order": 32}
---

# Record the run scope before reading a G25, calculator or qpAdm admixture result

Use this recipe before you read, compare or explain any of the following:

- a G25/Vahaduo fit;
- admixture-calculator output, such as a K-calculator, an Oracle list, a dendrogram or a vendor "ancient origins" report;
- a qpAdm model.

It covers three situations: someone pastes one run or one screenshot; a small unexpected component appears in a person whose pedigree is documented elsewhere; or two runs for the same person disagree. The recipe builds a run register, checks fit before anything else, tests a component with reruns that each change one input, and audits the reference labels the result depends on.

Related recipes:

- For vendor ethnicity estimates as dated, version-bound observations, use [AI for DNA research](ai-for-dna-research.md).
- For 23andMe Ancestry Composition confidence settings, use [23andMe match research](23andme-match-research.md).
- For haplogroup labels, tester-dependent trees and frequency maps, use [Y-DNA and mtDNA interpretation](ydna-mtdna-interpretation.md).
- For identity and kinship rulings, use [evidence/proof judgment](evidence-proof-judgment.md).

Nothing in this recipe establishes an ancestor, an origin locality or a relationship. A result that disagrees with a documented pedigree may make a candidate less likely. It never rules one out.

## Contents

- 1\. Open a run register before reading any number
- 2\. Label how each coordinate set was produced
- 3\. Check fit and scope before reading proportions
- 4\. Test a minor component with reruns that change one input
- 5\. Audit the reference labels the result depends on
- 6\. qpAdm: specify the model and screen the population lists
- 7\. Compare only within one declared scope
- Output: run register and component status

## 1. Open a run register before reading any number

Make one row per run, never one row per person. Record:

- **Target input.** Record the raw-file vendor, upload or native test, release, and whether the coordinates are real or simulated and scaled or unscaled. Different files for the same person produced different population labels in reported runs [S8], [S9]. Keep the files in separate rows and compare them under identical settings before attributing a difference to the input.
- **Reference sheet and edition.** Official averages; a curated averages sheet with or without simulated coordinates; ancients-only or moderns-only; or a named calculator panel [S11], [S4], [S2].
- **Mode.** Single/open, R2P–R5P, n-way Oracle, a nearest-population or nearest-individual list, or a dendrogram with its N-closest setting [S7], [S3], [S18].
- **Penalty, metric and constraints.**
  - The ADC penalty exactly as the tool prints it (for example "0.25x RC" or "0.5x RC").
  - Euclidean or Chebyshev distance.
  - Any source fixed or held within a min/max weight. One Vahaduo front end offers min%/max% weights, a fixed-source option and an "iteration mode" toggle.
  - References added or removed [S1], [S7], [S17], [S3].
- **Fit and date.** The distance, or for qpAdm the tail probability, copied next to the proportions.

Repeat a run with the identical target, panel, mode and settings. In repeated R5P fits, a different minor fifth component gave nearly the same distance [S3]. Report the spread in distance and weights, including interchangeable labels.

## 2. Label how each coordinate set was produced

- **Keep the tool's label word for word** (scaled, unscaled, "-sim"). Put the target and every reference on one scale, the one the sheet and tool expect, and never mix scales in one model. If a fit is implausible, check the expected scale before interpreting any component and rerun with compatible coordinates [S21].
- **Trace simulated coordinates to their inputs.** A sheet curator described converting other calculators’ results to make some references [S11]. Label those references and rerun with measured coordinates where available. A shorter distance to a simulated reference by itself cannot establish a closer relationship.
- **Coordinates change between releases.** A participant warned that the v62 release changed many coordinates, so files posted before it are out of date [S12].
  - Record the release of every coordinate file.
  - Fetch the current file before running.
  - Never mix pre-release and post-release coordinates in one run or comparison.
  - Keep coverage tags ("Cov_unknown", "Cov_1.04%", "low_res") with ancient samples, and mark low-coverage samples as provisional [S12], [S17].
- **Trace a re-derived reference to its method.** In one reported comparison, changing the reference set and then the “purification” method moved the same reference’s estimated Amerindian share in opposite directions [S13]. Preserve each reference version and compare one change at a time.

**MyHeritage DeepAncestry Coordinates.** Record the target as the provider's 25-dimensional PCA vector, derived from the tester's raw DNA against a panel of modern and ancient populations [S28 @2026-11-20] [S29 @2026-11-20]. Verify the coordinate system and scaling before using any reference sheet with it.

## 3. Check fit and scope before reading proportions

- **Check geographic and temporal coverage.** Compare the target with the populations the calculator was constructed to represent. Mark an out-of-scope result uninterpretable, even when the tool prints proportions [S19].
- **Investigate an outlying distance.** Compare like targets under identical settings. Check coverage, sample quality and possible missing references before interpreting the proportions. One conspicuously worse ancient-sample fit did not establish the cause of the discrepancy [S20].
- **Read the distance in its printed units.** A K15 output displayed distances above 100% [S5]. Keep both the metric and its scale; compare distances only within the same calculator and specification.
- **Test a minor component against a regional model.** In one report, the Peninsular Arab component disappeared while a European-only model retained a similar distance [S1]. Record both fits, the panel and the settings [S2]. A suggested threshold from one panel cannot diagnose ancestry on another.

### MyHeritage Ancient Origins

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Clear the [privacy gate](../SKILL.md#privacy-gate) before opting in to generate reports or requesting a recalculation. MyHeritage sends the tester's DNA-derived DeepAncestry Coordinates to IllustrativeDNA to generate the reports [S28 @2026-11-20] [S29 @2026-11-20].

**Set the Breakdown origin.** At the prompt after the tester consents, select one origin [S30 @2026-11-20]. Follow MyHeritage's recommendation to choose the tester's dominant ethnicity if known, or "Global" if there is no dominant origin or the tester is unsure [S29 @2026-11-20] [S30 @2026-11-20]. Record the selection because it guides which references the Breakdown uses [S28 @2026-11-20] [S29 @2026-11-20].

**Change the Breakdown origin.** Use "Tailor the model" to try another region that may better represent the tester's origins [S28 @2026-11-20] [S29 @2026-11-20]. Keep the era fixed and give the recalculated Breakdown its own row with the new origin.

**Match the era to the score.** Use the era slider in the Breakdown or the Genetic Similarities dual-origin view to select the Bronze Age, Iron Age, Roman Era or Middle Ages [S28 @2026-11-20] [S29 @2026-11-20]. Read a lower Genetic Fit as a closer fit to the model's references. Copy the Breakdown's Genetic Fit from the selected era because the score updates as the era changes [S28 @2026-11-20] [S29 @2026-11-20].

**Choose the report by population count.** Use Closest Populations, formerly the "Single origin" view in Genetic Similarities, to rank individual ancient populations [S28 @2026-11-20] [S29 @2026-11-20] [S31 @2026-11-20]. Use Genetic Similarities' dual-origin and triple-origin views for models combining two or three populations, respectively [S29 @2026-11-20] [S31 @2026-11-20]. Read both reports against the provider's full reference panel and keep the origin-tailored Breakdown in its own row [S29 @2026-11-20].

**Record the map region.** Use the region dropdown in Genetic Distance Maps. MyHeritage suggests "Europe" for finer detail when examining European origins. Choose "Global" to see the tester's position relative to all samples and populations in the reference panel [S28 @2026-11-20] [S29 @2026-11-20]. Record the region alongside the plot.

## 4. Test a minor component with reruns that change one input

For a component the pedigree does not predict, change one input per rerun and record the distance next to each result:

1. **Add a penalty.** Keep the target and reference roster fixed. Record each penalty, the distance and the minor component’s weight, including zero [S1].
2. **Restrict the panel to plausible regional references.** Record the references kept and compare the regional model’s distance with the broader fit [S1].
3. **Remove the dominant or suspect source, or switch sheets.**
   - Replace an omitted regional reference or compare matched runs on the official and curated sheets. A component that disappears may have stood in for a missing source [S4].
   - Test the substitute on a control of independently documented ancestry. A closer local reference shifted another component in one target but required an extra balancing source in the control [S6].
4. **Add the missing reference without changing mode.** A K15 component disappeared after the reference panel and the fitting mode both changed [S5]. Repeat each change separately before attributing the disappearance to the new sources.
5. **Inspect the individual samples behind a cluster.** Remove the sample carrying the signal and rerun. Record whether weight disappears or moves to neighbouring clusters [S22].
6. **Keep near-tied Oracle rows together.** If minor labels can replace each other at almost identical distances, report the unresolved alternatives and their weights [S3].

Classify the component by what the reruns showed:

- **Reference-gap artefact (tested):** adding the missing reference under otherwise identical settings removes the component at a comparable fit. If replacing a whole sheet also changed other samples, describe it as model-dependent until the isolated addition has been tested [S4].
- **Model-dependent:** it disappears under a penalty, regional restriction or source removal at a comparable fit [S1].
- **Possible proxy (untested):** this applies only while the missing-reference test has not been run.
- **Stable within those scopes:** it survives every tested change. This is still not an ancestry finding.

A second calculator that agrees [S22] is not independent if it draws on overlapping source samples. Record the overlap, or mark it as unknown.

## 5. Audit the reference labels the result depends on

- **Sample counts and singletons.** Curated sheets print "(n=1)" and "(low_res)" tags, and fits often lean on several n=1 rows [S11], [S4]. A singleton label is one person.
- **Who defined the label.** "Profile" tags and grouped names are the curator's groupings [S11], [S17].
  - Read the curator’s clustering notes and the provider’s description before interpreting a combined or historical label. Record its named constituent samples, populations or cultures. A cluster label or a provider category can combine groups whose genealogical histories differ [S2], [S16].
- **Locality, checked against the study's sample table.**
  - Match each sample’s identifier to the locality in the study table. A reported correction distinguished Startsevo in the Rhodopes from Starchevo in southwest Bulgaria [S15]. Record which genotype data the coordinates derive from and whether they are simulated.
- **Mislabelled samples.**
  - Verify the individuals included in an average, especially if the location or population is disputed or the curator cannot identify the underlying samples [S14]. Preserve warnings such as «probably_misattributed» beside the row [S17].
- **Outliers and clusters.** Record any «_o», «_o1», «_o2» or core-cluster label. Check whether the curator dropped samples based on how individual targets fitted, and rerun with and without the exclusions if the data permit [S22].
- **Circular inclusion.** If a panel accepts uploaded kits, check whether the test kit or a close relative helped build the reference. Record membership as unknown when the roster is unavailable [S13].

## 6. qpAdm: specify the model and screen the population lists

qpAdm models a target as a mix of "left" (source) populations, tested against a set of "right" (reference) populations.

- **Record the full specification:**
  - target;
  - left populations, with individual counts;
  - right populations, in order;
  - reference release and data product;
  - software and version;
  - input format;
  - the SNP count actually used.
- **Data product.** The AADR reference data are distributed in 1240K and Human Origins (HO) versions. A participant said the raw-file merge step offered "v62.0_1240k or v62.0_HO" [S23].
- **SNP overlap.** Record the SNP count actually used for the target and reference data product. Check any merge or filtering step and retain the program’s precisely labelled count: the number entering block construction can differ from the effective overlap for a particular statistic [S23].
- **Read the overall model test.** In classic qpAdm, read `tail` at rank (number of sources − 1). `taildiff` compares adjacent ranks, and its meaning depends on the row. In the authors’ example, the full-rank row’s `taildiff` equals the model’s overall tail on the preceding row [S26]. Copy the field, rank and degrees of freedom with the value before interpreting a forum or software report [S23].
- **Keep the data product fixed.** A model reportedly passed the chosen threshold on HO and failed it on 1240k [S23]. Keep separate rows and inspect SNP overlap and model settings before interpreting the difference.
- **Record implementation and version.** Compare classic ADMIXTOOLS and ADMIXTOOLS 2 only with matched data, SNP treatment, population lists and settings. A forum observation about which version passes a model more readily cannot establish a general difference [S23].
- **Remove duplicate individuals, then rerun.** The same individual can appear under several IDs. Check the annotation file, including repeated outgroup, Caucasus and Natufian samples in a right set [S23], [S24].
- **Population size and platform limits.**
  - A participant advised against n=1 left populations unless a study used them [S23].
  - Record the software’s actual limit, if any, on the number of right populations and which entries were excluded. Limits reported for a particular web interface do not establish a qpAdm-wide cap [S23].
- **Swap a left source while keeping the target fixed.** Retain the original and replacement sample IDs, group sizes, weights, standard errors and overall test for both runs. A regional-average model and a child’s individual model had different targets in the reported comparison [S24]; substituting one as the baseline cannot show the effect of the source swap.
- **Do not lower the acceptance threshold to manufacture a pass.**
  - Report the overall tail probability.
  - List the other passing models with their standard errors.
  - A passing model is one admissible fit only if every fitted weight lies between 0 and 1. Record that feasibility check with the run (check the fitted weights alongside the overall test [S27]); a pass that needs a negative weight or one above 100% is not a feasible mixture.
  - A 0% coefficient is that source's fitted weight in that model and right set. It does not show the ancestry is absent.
- **Reproduce unstable runs.** With the data and software fixed, compare input formats and verify sample, allele and SNP mappings through conversion. A participant reported unstable f4 reruns with PLINK input and repeatable results from EIGENSTRAT files [S25]. Preserve the inputs, version and rerun output; this report does not identify a general PLINK defect.

## 7. Compare only within one declared scope

- **Change one setting and you have a new row.** A different raw file, sheet, sim setting, mode, penalty, metric, roster or software makes a new row. It is not a contradiction and not a confirmation [S7], [S8], [S17].
- **Never merge ranked lists.** Euclidean and Chebyshev rankings put the same target's matches in a different order, and population lists differ again from individual lists [S7], [S17].
- **Keep a dendrogram's distance list next to the tree.** The tree's grouping depends on the N-closest count, so the plotted neighbour is not necessarily the closest population. A chatbot reading of the image, including a "genetic midpoint" location, is not a finding [S18].
- **Provider reruns and fixed components cannot test the pedigree.**
  - A provider rerun that leaves out references in response to a pedigree complaint is a new model with its own scope. It neither confirms nor corrects the paper trail [S10].
  - A run with a component fixed to a pedigree share [S3], [S2] depends on that assumption and cannot test it.

## Output: run register and component status

Return:

1. the run register;
2. a sensitivity table for each disputed component across the one-input reruns, with paired distances or p-values;
3. a label audit for the labels it depends on: n, singleton, real or simulated, defined by curator, provider or study, checked locality, outliers kept or removed, duplicates, circular inclusion;
4. a status for each component, using one of:
   - reference-gap artefact (tested);
   - model-dependent;
   - possible proxy (untested);
   - stable within tested scopes;
   - uninterpretable (poor fit, out-of-scope target, mixed-scale or otherwise mixed inputs).

State plainly that no origin, identity or kinship finding follows.
