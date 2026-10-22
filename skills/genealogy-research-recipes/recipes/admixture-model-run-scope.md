# Record the run scope before reading a G25, calculator or qpAdm admixture result

Use this recipe before you read, compare or explain any of the following:

- a G25/Vahaduo fit;
- admixture-calculator output, such as a K-calculator, an Oracle list, a dendrogram or a vendor "ancient origins" report;
- a qpAdm model.

It covers three situations: someone pastes one run or one screenshot; a small unexpected component appears in a person whose pedigree is documented elsewhere; or two runs for the same person disagree. The recipe builds a run register, checks fit before anything else, tests a component with reruns that each change one input, and audits the reference labels the result depends on.

Related recipes:

- For vendor ethnicity estimates as dated, version-bound observations, use [AI for DNA research](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/ai-for-dna-research.md).
- For 23andMe Ancestry Composition confidence settings, use [23andMe match research](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/23andme-match-research.md).
- For haplogroup labels, tester-dependent trees and frequency maps, use [Y-DNA and mtDNA interpretation](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/ydna-mtdna-interpretation.md).
- For identity and kinship rulings, use [evidence/proof judgment](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/evidence-proof-judgment.md).

Nothing in this recipe establishes an ancestor, an origin locality or a relationship. A result that disagrees with a documented pedigree may make a candidate less likely. It never rules one out.

## 1. Open a run register before reading any number

Make one row per run, never one row per person. Record:

- **Target input.** Which raw file produced the coordinates (the vendor's own test or an upload). Whether they are real or simulated, and scaled or unscaled. The dataset release or date.
  - Two vendor files for one person gave different fits: 92.2% Spanish at 1.58% distance, and 76.6% Spanish plus 8.8% Icelandic at 1.90% [S8].
  - In another report, three uploaded files gave near-identical period models. The vendor's own file gave different populations and an unexpected Oceanian component [S9].
- **Reference sheet and edition.** Official averages; a curated averages sheet with or without simulated coordinates; ancients-only or moderns-only; or a named calculator panel [S11], [S4], [S2].
- **Mode.** Single/open, R2P–R5P, n-way Oracle, a nearest-population or nearest-individual list, or a dendrogram with its N-closest setting [S7], [S3], [S18].
- **Penalty, metric and constraints.**
  - The ADC penalty exactly as the tool prints it (for example "0.25x RC" or "0.5x RC").
  - Euclidean or Chebyshev distance.
  - Any source fixed or held within a min/max weight. One Vahaduo front end offers min%/max% weights, a fixed-source option and an "iteration mode" toggle.
  - References added or removed [S1], [S7], [S17], [S3].
- **Fit and date.** The distance, or for qpAdm the tail probability, copied next to the proportions.

Rerun an identical single-mode run before quoting it. Three R5P runs on one target gave distances of 1.43–1.45%, with a different minor fifth component each time [S3]. Report the spread, not one draw.

## 2. Label how each coordinate set was produced

- **Keep the tool's label word for word** (scaled, unscaled, "-sim"). Put the target and every reference on one scale, the one the sheet and tool expect, and never mix scales in one model. A participant blamed fits that made no sense on unscaled coordinates, and the fit improved after switching to scaled ones [S21].
- **Simulated coordinates are weaker evidence.** The curator of a large sheet said sims are converted from other calculators' results, get you into the neighbourhood, lose detail, and usually give smaller distances than real coordinates for the same person [S11].
  - A small distance to a simulated reference counts for less than the same distance to real data.
  - Runs that differ in whether sims are included cannot be compared.
- **Coordinates change between releases.** A participant warned that the v62 release changed many coordinates, so files posted before it are out of date [S12].
  - Record the release of every coordinate file.
  - Fetch the current file before running.
  - Never mix pre-release and post-release coordinates in one run or comparison.
  - Keep coverage tags ("Cov_unknown", "Cov_1.04%", "low_res") with ancient samples, and mark low-coverage samples as provisional [S12], [S17].
- **A re-derived or "purified" reference is the output of a method.** One reference's Amerindian share went from 77% to 87% after references were added. It then went to 72% under a different purification method, and a third calculator put it near 71% [S13]. That is variation between methods, not a change in the person.

## 3. Check fit and scope before reading proportions

- **Do not interpret components when the target is outside the calculator's intended scope.** A European-Neolithic calculator gave a South Asian target a distance of 14.68%. A participant called the fit terrible and the results unrealistic [S19].
- **Do not read any component of a run whose distance is far above comparable runs.** Three ancient samples fitted at about 2.0–2.5% and a fourth at 11.48%. A participant attributed the fourth to sample quality [S20].
- **Distances only mean something on their own tool's scale.** One K15 thread printed distances from about 197% to 3201% [S5]. Never rank runs across calculators.
- **A very low distance with an exotic sliver is not stronger evidence.** If a regional-only model fits almost as well and drops the sliver, record the sliver as model-dependent.
  - Example: 4.8% Peninsular Arab at 1.642%, against a British/Austrian/south German model with no Arab component at 2.027% [S1], [S2].
  - One participant offered cutoffs: overfit below 0.02, and genuine MENA ancestry at 0.03 or above. These are that person's rule of thumb for one panel. Do not reuse them as thresholds.

## 4. Test a minor component with reruns that change one input

For a component the pedigree does not predict, change one input per rerun and record the distance next to each result:

1. **Add a penalty.** An aunt with a documented Northwest European pedigree scored about 3% Arabian on one K-calculator and 3–5% Peninsular Arab on G25 [S1]. In one panel the component behaved like this:
   - 4.8% at 1.642%;
   - 3.2% at 1.814% with Scandinavian removed;
   - 2.8% at ADC 0.25x;
   - absent at ADC 0.5x (2.027%, with only two European components).
2. **Restrict the run to regional references.** British, Austrian and south German references alone fitted at 2.027% [S1].
3. **Remove the dominant or suspect source, or switch sheets.**
   - On the official sheet, two Near Eastern/Caucasus components appeared in 4-way fits. The participant read them as stand-ins for regional samples missing from that sheet. They did not appear in 4-way runs on the larger curated sheet [S4].
   - In another thread, swapping in a closer local reference shifted a small component. A control person of known ancestry then needed an extra southern source to balance that reference [S6].
4. **Add the reference the panel lacks.** K15 runs gave Native American shares (10.4% plus 6.0%, at 3201% distance) to a man described as having none. After Ashkenazi and Sephardic references were added, a reduced three-way run showed none. That rerun also switched mode from ADC 0.25x RC to R3P, so it changed two inputs and does not isolate the effect of the added references [S5].
5. **Find the single sample driving the component** in the unaggregated output, and rerun without it. One steppe signal rested mainly on a single sample. With that sample removed, part of the signal moved to a neighbouring cluster, and the cluster percentages fluctuated between runs [S22].
6. **Read near-tied Oracle rows together.** A 3-way Oracle returned about 0.8–0.9% of several unrelated East Asian labels at almost identical distances [S3]. Slivers that can be swapped for each other are one unresolved leftover, not several ancestries.

Classify the component by what the reruns showed:

- **Reference-gap artefact (tested):** it disappears when the missing reference is added or a larger sheet is used, at a comparable fit. An example is [S4].
- **Model-dependent:** it disappears under a penalty, regional restriction or source removal at a comparable fit [S1].
- **Possible proxy (untested):** this applies only while the missing-reference test has not been run.
- **Stable within those scopes:** it survives every tested change. This is still not an ancestry finding.

A second calculator that agrees [S22] is not independent if it draws on overlapping source samples. Record the overlap, or mark it as unknown.

## 5. Audit the reference labels the result depends on

- **Sample counts and singletons.** Curated sheets print "(n=1)" and "(low_res)" tags, and fits often lean on several n=1 rows [S11], [S4]. A singleton label is one person.
- **Who defined the label.** "Profile" tags and grouped names are the curator's groupings [S11], [S17].
  - One panel's labels come from clustering, and its combined names were explicitly not meant to say the groups are the same [S2].
  - A provider category means what the provider's own description says. Participants guessed that one ancient category was a single hunter-gatherer component. Another participant reported that the provider's info panel names two steppe-era cultures [S16]. Open that description before explaining a category.
- **Locality, checked against the study's sample table.**
  - For one newly released study, a participant found that the first locality tags in circulation were mostly wrong, and corrected them from the sample list [S15].
  - A regional reading was distorted by two villages with nearly the same name, Startsevo in the Rhodopes and Starchevo in the south-west. They are distinct places [S15].
  - Record whether the coordinates were built from the authors' published genotype data, as a participant said these were, or are simulated [S15].
- **Mislabelled samples.**
  - Participants identified one island reference as belonging to a different population [S14].
  - The maker of another average could not recall what was in it [S14].
  - Some sheet rows are themselves tagged "probably_misattributed" [S17].
- **Outliers and clusters.** Note any "_o", "_o1", "_o2" or core-cluster labels, and whether a run kept or removed them. One calculator maker said he removed source samples that gave odd results for even one or two targets [S22].
- **Circular inclusion.** Check whether the tested kit, or a close relative, is itself one of the references. One project built its references from uploaded kits [S13].

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
- **SNP count.** One combined consumer file used 420,180 SNPs against the 1240k build and about 149,192 against the HO build. The participant reported that ADMIXTOOLS 2 prints the count in a "Computing block lengths for … SNPs" line [S23].
- **Read the right p-value.** In classic qpAdm output, the model's p-value is "tail" on the rank line for (number of sources − 1). "taildiff" (with chisqdiff and dofdiff) is a different test: it compares that rank with the next lower rank. A participant equated taildiff with the p-value [S23]. The qpWave/qpAdm documentation does not support that, so never accept or reject a model on taildiff.
- **Runs on different data products are different measurements.** One model passed at about 0.3 on HO and failed on 1240k [S23].
- **Never pool pass/fail verdicts across software.** Participants reported that ADMIXTOOLS 2 passes models more easily than classic qpAdm [S23]. That is unverified, and the ADMIXTOOLS 2 tutorial says its results should generally match classic ADMIXTOOLS. Record the software either way.
- **Remove duplicate individuals, then rerun.** The same individual can appear under several IDs. Check the annotation file, including repeated outgroup, Caucasus and Natufian samples in a right set [S23], [S24].
- **Population size and platform limits.**
  - A participant advised against n=1 left populations unless a study used them [S23].
  - Note any platform cap on the number of right populations. One participant reported a cap of 30 on a web tool [S23].
- **Swap a left source and keep both runs on the same target.** Replace it with another sample of the same population. In one thread a child's model still passed at 0.16 after the African source was swapped for a two-sample alternative. The participant reported a worse fit, with the main source at 88.5% [S24]. A regional-average model in the same thread passed at tail probability 0.070 (dof 11, chi-square 18.524, coefficients 73.4/15.2/11.5%) [S24]. That run has a different target, so it is not the before-run for the swap, and the difference between the two says nothing about the swap.
- **Do not lower the acceptance threshold to manufacture a pass.**
  - Report the overall tail probability.
  - List the other passing models with their standard errors.
  - A passing model is one admissible fit only if every fitted weight lies between 0 and 1. Record that feasibility check with the run (ADMIXTOOLS 2 reports it separately from the p-value); a pass that needs a negative weight or one above 100% is not a feasible mixture.
  - A 0% coefficient is that source's fitted weight in that model and right set. It does not show the ancestry is absent.
- **If identical reruns differ, change one technical input at a time.** ADMIXTOOLS 2 accepts both PLINK (.bed/.bim/.fam) and EIGENSTRAT (.geno/.ind/.snp) input. One participant traced unstable f4 output to the PLINK input. The same runs were stable with .geno/.ind/.snp, and the instability came back on a second machine when PLINK input was used again [S25]. That participant was working around the v2.0.1 release (published 3 March 2024). Record input format and package version with every result.

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
