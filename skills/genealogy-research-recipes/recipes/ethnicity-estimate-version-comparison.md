---
id: "ethnicity-estimate-version-comparison"
title: "Save, date and compare successive ethnicity-estimate versions"
summary: "Save, date and compare successive AncestryDNA, MyHeritage or FamilyTreeDNA ethnicity-estimate versions."
kind: "judgment"
scope: {"platforms": [], "tasks": []}
privacy: "genetic-third-party"
gates: ["privacy-transfer"]
guardrails: [{"id": "ETHNICITY-ESTIMATE-VERSION-COMPARISON-01", "text": "The tester's DNA did not change between versions; the vendor's method did. Ask first what the vendor changed, not what changed in the family [S11]."}]
handoff: ["23andme-match-research", "admixture-model-run-scope", "ai-for-dna-research", "dnapainter-practical-dna-workflows", "ftdna-practical-dna-workflows"]
checked: "2026-11-06"
checked_basis: "opened 2026-11-06"
capabilities: {"browse": [], "local_script": [], "extensions": [], "data_transfer": ["export"], "contact": []}
router: {"section": "DNA", "group": "Ethnicity, admixture and match outreach", "order": 42}
---

# Save, date and compare successive ethnicity-estimate versions

Use this recipe when a vendor has updated an ethnicity estimate (AncestryDNA Ancestral Regions above all, also MyHeritage Ethnicity Estimate and FamilyTreeDNA myOrigins), when someone asks what changed between two versions, or before a research question is built on a region from one version. It saves the outgoing version in time, dates each version correctly, aligns the two through the vendor's own region hierarchy and sorts every change into a known update effect before anything is read as new ancestry. It prevents these failures:

- losing the previous AncestryDNA version, which Ancestry withdraws 90 days after an update
- dating an estimate by the day it was downloaded instead of the date the vendor computed it
- comparing regions with the same or similar names as if their boundaries had not changed
- reading a 1–2 point continent move, a trade between neighbouring regions or a split as a new fact about ancestry
- comparing confidence ranges that the vendor built by different methods
- planning research on a region below the reliability floor of its version

Link out for the shared steps:

- **Reading one estimate as a dated observation, ranges, missing regions, parent and child checks, tracing a region through matches:** [AI for DNA research](ai-for-dna-research.md), section "Read ethnicity estimates as dated, version-bound observations".
- **23andMe Ancestry Composition versions and confidence levels:** [23andMe match research](23andme-match-research.md), recipe 7.
- **Saving FamilyTreeDNA results before an NGS upgrade:** [FamilyTreeDNA workflows](ftdna-practical-dna-workflows.md).
- **Exporting and painting Ancestry Chromosome Painter segments:** [DNA Painter workflows](dnapainter-practical-dna-workflows.md).
- **User-run calculators and admixture models:** [admixture run scope](admixture-model-run-scope.md).

## Contents

- Inputs to gather first
- 1\. Save the outgoing version before the vendor withdraws it
- 2\. Date each estimate by when the vendor computed it, and label its version
- 3\. Write down the method change before reading any number
- 4\. Align the two versions through the vendor's hierarchy, broadest level first
- 5\. Sort every change into a known update effect before calling it new
- 6\. Compare the new percentage with the old range, never one range with another
- 7\. Apply the version's own reliability floor to small regions
- 8\. Keep a version log and form hypotheses only from what is left unexplained
- Close with a version-comparison packet

## Inputs to gather first

- vendor, kit, whether the kit is the vendor's own test or an upload, the assay (chip or sequencing), and the version label each estimate shows
- the outgoing version as the vendor's file or your screenshots, with its processing date
- the current version: every region, its percentage and its range
- the vendor's region list and the white paper for each version
- relatives' kits at the same vendor, each with its own version label

## 1. Save the outgoing version before the vendor withdraws it

- **AncestryDNA keeps only the current version and the most recent former version, and offers the former for download for 90 days after an update.** Older versions are not available [S1 @2026-11-19], [S24 @2026-11-19]. Save the previous version first, then the current one [S11].
- **Privacy gate:** <!-- privacy-gate: export --> Downloading the estimate PDF and saving screenshots of the Chromosome Painter, parent views and map export the tester's DNA-derived results from the account; answer the privacy gate in `SKILL.md` first.
- **Download route, website only:** the download is not offered in the Ancestry app [S1]. Open DNA > Origins > Regions. Below the last region, next to the update date, click the previous-results link. Then, beside "What changed?", click **Download PDF** [S1], [S11]. Find the link by its position: its wording changes between years ("See what changed and FAQs" in 2024, "View previous results and FAQs" in 2026) [S12 @2026-11-19], [S11 @2026-11-19].
- **Save the views the PDF omits.** The previous-version PDF lists the regions, percentages and ranges. Save every other view while the old version is still live: Chromosome Painter, By Parent (and By Grandparent where offered), Journeys and the map [S11 @2026-11-19]. If an update banner appears, capture the Painter then so the outgoing chromosome assignments can be compared with the next version [S28 @2026-11-19].
- **Capture the current version in full.** Screenshot the whole regions list, from the first heading to the last region, including the update date, and the map. Ranges are not in the list: click each region, then its "i" icon, and record the range [S11].
- **Start every file name with the date in year-month-day order** [S11].
- **Save at every update, even when nothing seems to have changed.** With only two versions online at any time, your files are the only record of earlier versions.

- **MyHeritage:** for the v2.5 release, existing users could opt in and switch back to v0.95 through the results menu [S5], [S22]. The June 2024 v2 rollout had reached only some kits [S31]. Save each version you can still open.
- **FamilyTreeDNA:** its August 2026 NGS upgrade guide warned that previous results would be removed and that myOrigins estimates could shift by a few points [S8]. Save the outgoing results before an assay upgrade.

**Open the MyHeritage estimate for the kit you want to compare.** On the web, choose **DNA > Ethnicity Estimate**. In the app, tap the **DNA** icon at the bottom and select **Ethnicity Estimate**. If you manage several kits, use the arrow beside “This is you” to select the tester [S33 @2026-11-20].

**Request v2.5 if the selected kit still shows v0.95 and offers the update.** Choose “Get the update” in the invitation. If you chose “Maybe later”, look for the update banner at the top of the results or in the left panel [S32 @2026-11-20], [S5 @2026-11-20]. Use the existing MyHeritage kit even if it was tested years ago or used an older chip [S32 @2026-11-20], [S5 @2026-11-20]. Opt in for each eligible kit you plan to compare and reopen its results after the readiness email arrives. MyHeritage's rollout guidance allowed about a day for calculation [S32 @2026-11-20].

**Switch versions for that same kit.** On desktop or mobile web, check for the version dropdown directly below “Your ethnicity results”. When both versions are offered, open v0.95 and v2.5 in turn [S32 @2026-11-20], [S5 @2026-11-20].

## 2. Date each estimate by when the vendor computed it, and label its version

- Record the vendor’s processing date separately from the date you saved the estimate. In the Ancestry PDF shown in the 2026 guide, these fields were labelled “Processed in” and “Downloaded on.” A kit first processed after the update had no earlier version to compare [S11].
- Copy the comparison headings and regions-page date as displayed, alongside your capture date. A presenter saw the regions-page date change from October to July 2024 while her percentages stayed the same [S17]. Use the processing date or explicit model label to identify the estimate [S11].
- Copy the version from the results themselves. For example, FamilyTreeDNA’s 2020 release identified myOrigins with “Version 3” [S7]. A MyHeritage user reported a v2.6 prompt followed by v2.5 results [S29]. If the results give no model number, label them by processing date, or use a capture date explicitly marked as such [S21].
- Before comparing relatives, check the label on each kit. During the MyHeritage rollout, kits in the same family could still show different versions [S20], [S30]. Defer an inheritance comparison until the estimates use the same model.
- Record the assay alongside the model label. FamilyTreeDNA’s NGS upgrade guide described possible changes to myOrigins estimates following a change of assay [S8].

## 3. Write down the method change before reading any number

The tester's DNA did not change between versions; the vendor's method did. Ask first what the vendor changed, not what changed in the family [S11]. Make one method row per version from its white paper: number of regions, reference-panel size, assignment algorithm, smoothing, range method and performance floor.

- **AncestryDNA 2025 to 2026:**
  - regions: 146 to 302 [S3 p. 1];
  - reference panel: 185,063 samples to more than 295,000 [S4 p. 8], [S3 p. 7];
  - assignment: comparison with summary haplotype-cluster models replaced by direct comparison of each window with individual panel members [S3 p. 10];
  - a new first pass assigns each window to a broad super-population, then chooses a region inside it [S3 p. 13];
  - smoothing: hidden Markov model replaced by a transformer [S3 pp. 10, 14];
  - ranges: from 1,000 sampled model paths to the measured error in simulated people of known ancestry [S4 p. 19], [S3 p. 25];
  - performance reporting: a 5% cut-off and mean overlap in 2025; a 2.5% cut-off, median overlap and an added "weighted precision" in 2026 [S4 p. 21], [S3 pp. 18–19].
- **MyHeritage v0.95 to v2.5:** 42 to 79 ethnicities [S5]; earlier models used global ancestry prediction, and the new one uses window-based local ancestry inference [S6].
- **Do not rank two versions by their white-paper accuracy numbers.** The statistics, floors and simulation sets differ [S3], [S4], [S10].
- **A region can keep its continent and change its panel rule.** Ancestry builds its Americas panels from Indigenous-inherited segments only. In 2025 most of these panels required both copies to carry an Indigenous assignment; Cuba and Haiti & Dominican Republic instead combined single Indigenous-assigned chromosomes from different people. In 2026 the rule uses one or both copies [S4 pp. 6–7], [S3 p. 5].

**Compare regional percentages across the 2025 AncestryDNA update.** Keep Ancestral Journeys out of the regional change table and log any Journey changes separately by capture date [S38, from the available excerpt], [S39], [S25].

**Record how AncestryDNA expanded the 2025 reference panel.** Ancestry supplemented testers with documented roots by adding genetically close testers with similar Origins results, including testers without linked trees [S38, from the available excerpt], [S39], [S4 section 2.2]. Record this in the 2025 method row when explaining changed percentages for the same kit.

**Compare MyHeritage Genetic Groups by group name.** The v0.95-to-v2.5 release revised the Ethnicity Estimate and carried over the Genetic Groups algorithm [S32]. Use group membership as a separate geographic clue. The ethnicity heading a group sits under can change between versions [S5].

**Compare MyHeritage Ancient Origins reports in their own log.** Match the report and time period for the same kit and record each capture date. Before interpreting a change, check for additions to the sample database or research updates that may have affected the report [S36 @2026-11-20], [S37 @2026-11-20].

## 4. Align the two versions through the vendor's hierarchy, broadest level first

- Use the region list for each release to place regions under their subregion and continent. Start with the continent totals, compare subregions next, then examine individual regions [S10], [S11].
- Compute subtotals from the underlying regions. Ancestry’s 2026 FAQ describes macro-region headings as display groups without their own reference panels [S25]. In the October guide, the England and Celtic & Gaelic headings together covered the tester’s Northern Europe subregion [S11]. Use displayed heading sums as a check and apply the same grouping to older results that lack headings.
- **"Subregion" names different levels in different years.** Ancestry's 2024 results showed subregions as finer areas inside a region, calculated partly from DNA matches [S12]. The 2026 list uses subregion for the level between continent and region [S10]. Never align a 2024 subregion with a 2026 subregion by name.
- **A name is not a boundary.** Treat same or similar names in two versions as different regions: "Southeastern England & Northwestern Europe" (2025) and "Southeastern England" (2026); "Western Bantu Peoples" and "Western Bantu & Forest Peoples"; "Canada & United States" and "Atlantic Northeast (Canada & USA)" [S11]. Compare such pairs only through the subregion or continent total they share.
- Use the old map to place a retired region. If it spans two groups, keep its share unsplit, state which group you counted it in and record how that choice affects the comparison. Assigning all of “Southeastern England & Northwestern Europe” to Britain sets an upper bound on that region’s British contribution in the old estimate [S11].
- **Settler-sounding names in the Americas describe Indigenous-inherited DNA.** In 2026, regions such as "Atlantic Northeast (Canada & USA)" are built only from the Indigenous-inherited parts of reference genomes [S3 p. 5], [S15]. Never align one with a colonial European line.
- **MyHeritage: group the v2.5 ethnicities under the broad v0.95 groups by their maps**, and record each judgment. The boundaries do not nest exactly: East European took in the easternmost part of the old North and West European area, including part of Germany [S21].

If v0.95 shows **Scandinavian**, add the **Swedish**, **Norwegian** and **Danish** percentages shown for the same kit in v2.5 and compare that subtotal with the old Scandinavian share [S32].

## 5. Sort every change into a known update effect before calling it new

**Check for a newly available reference population.** If the new label fits a documented family location, check both releases’ reference-panel lists and maps for a new panel covering that place [S40, from the available excerpt], [S25]. AncestryDNA’s 2025 panel list had no separate Belgium entry, and its Southeastern England & Northwestern Europe map covered Belgium [S4 table 2.1 and fig. 4.2]. The 2026 panel list includes Belgium [S3 table 2.1]. In the same kit’s results, check whether the new region gained share as overlapping older regions lost it. Record added panel coverage as a possible explanation for that shift.

Work from the broadest level down. Stop at the first pattern that explains the change [S11].

| Pattern seen | Reading | Check |
| --- | --- | --- |
| A continent moves by 1 or 2 points | Update side effect; regions display as whole percentages, so a continent total can move a point from rounding alone | Treat the continent total as steady |
| One region gains about what its neighbours lose | A reassignment among neighbouring regions could explain the pattern | Compare the broader total and check the two saved Painter views for changes at the same chromosome positions |
| A region drops to 0 and new names appear in the same area | Split, rename or retirement | Is the old name still on the current list? Compare the shared parent total |
| A region moves, but the new value sits inside the old range | The range gives no reading; go on to the subregion total | Section 6 |

- **A trade between neighbours is inside what Ancestry counts as correct.** In its 2026 single-origin tests, raw precision for a region is about 50%, while weighted precision, which counts an assignment to a genetically similar neighbour as a correct reading, is above 90% for most regions [S3 pp. 18, 22]. The hard choice is between close neighbours: England has six neighbouring regions, Nigeria eight and Mexico 15 [S3 p. 13]. Ancestry staff say this applies to large percentages too, not only small ones: which neighbour receives the DNA depends on who is in the reference panel [S16], [S26].
- Add a region’s gain and its neighbours’ losses in percentage points. Similar totals support reassignment as a possible explanation. To locate a change on a chromosome, compare the same positions in both saved Painter views [S11], [S27], [S28].
- When a category splits, compare the total across the same map area. The published West Africa example went from seven labels to nine while the combined estimate moved from 33% to 31% [S11]. Leave the old share intact unless the older results themselves give a breakdown.
- Check the release’s explanation of labels. In Ancestry’s 2026 FAQ, “New” identified a newly reported region and “Split into” indicated a named split [S25]. Check the old regional map before interpreting a new name [S14], [S16].
- For movement across several updates, align the groups afresh for each release. Follow the broader total alongside the individual estimates before interpreting a recurring regional trend [S11], [S19].
- **A category that disappeared with a version says nothing against that ancestry.** MyHeritage dropped Maasai and Sierra Leonean in v2.5 for lack of training samples and says they may return [S5]. Ancestry split its former Germanic Europe region and retired its Middle East region [S25].

## 6. Compare the new percentage with the old range, never one range with another

- **Ranges from different versions are built differently.** Ancestry's 2026 ranges come from measured error in simulated people of known ancestry [S3 p. 25]; its 2025 ranges came from 1,000 alternative model paths [S4 p. 19]; a 2013 Ancestry presentation described the percentage as the average of 40 runs [S9]. Do not compare an old range with a new one. A narrower new range is not new certainty about the person.
- Check whether the new percentage falls within the old range, including zero. In the published Connacht comparison, the change from 10% to 2% stayed within the former 1–10% range [S11].
- **Inside the old range:** the old estimate already allowed this value, so the move alone is no evidence about ancestry [S11]. Read its subregion total first, because neighbouring regions trade share, then run the region through sections 7 and 8 [S11]. A region that keeps bouncing between updates is wobble [S11].
- **Outside the old range:** look for a section 5 pattern first: a reassignment or split pushes one region outside its old range while the subregion total holds [S11]. If no section 5 pattern explains it at the subregion or continent level, it becomes a section 8 hypothesis.

- Record the current ranges with the estimate. Ancestry makes the previous estimate available for 90 days after an update [S24 @2026-11-19]. The 2026 guide shows where the previous ranges appeared in the download [S11 @2026-11-19].

## 7. Apply the version's own reliability floor to small regions

- **Ancestry floors: 5% for planning, 2.5% for credibility.** Below 5%, a region is a hypothesis in every version: the 2025 paper measured a much higher error and missing rate below 5% [S4 p. 21], and the FAQ as of September 2026 says regions below about 5% more likely reflect DNA that is difficult to assign [S2]. Below 2.5%, the 2026 paper still reports a much higher error and missing rate under the new method [S3 p. 18], so such a region counts for nothing on its own.
- **Regions near the reporting minimum come and go by chance.** Ancestry reports only regions above a minimum share, which it does not publish. It spreads the rest over the reported regions and shows those windows as "Unassigned" in the Chromosome Painter [S3 p. 16]. A region sitting at that minimum can appear in one update and not the next with essentially unchanged evidence [S3 p. 16]. An "Unassigned" stretch is one whose low-probability assignment Ancestry filtered out [S3 p. 16]; it assigns no ancestry to that stretch.
- **Decision rule:** a region below 5%, or one that appeared or vanished between versions, is a hypothesis. Do not make it a research objective by itself. Carry it forward only with documents or with matches, as in [AI for DNA research](ai-for-dna-research.md) [S11].
- **Look up the region's published recall and precision before weighing it.** Recall answers whether testers with that ancestry usually get the region; precision answers whether testers who get it usually have that ancestry [S18]. Ancestry publishes per-region figures for a selection of regions only: a selected list in 2026, and in 2025 only regions updated in that release [S3 p. 19], [S4 p. 24]. If the region is missing from the table, record "not published"; never borrow a neighbour's figure. Precision falls below 50% for some regions, such as Burundi & Rwanda, West Midlands and Northeast Germany in 2026 [S3 p. 20].
- **Trace regions no longer exist.** Ancestry once listed "trace regions", renamed them "low confidence regions" in 2016–2017 and removed them in 2018 [S13]. Do not count the disappearance of a saved trace region as a change in the estimate.
- **Expect updates to clear away 1–2% regions.** Many 2026 Ancestry results lost odd 1% and 2% regions [S14]; MyHeritage's June 2024 update removed many small components [S20]. That is the floor at work, not a correction of the pedigree.

**An older Ancestry page's 0.5% is not this minimum.** An Ancestry help page on low confidence regions, read in its Internet Archive copy of 17 July 2025, lists a region under "other regions tested", shown after selecting "Show all regions", when its estimate is below 0.5% and its range does not exceed 2.5% [S23]. That page describes the low confidence regions that the trace-regions point above says Ancestry removed in 2018, not the 2025 or 2026 method. Do not record 0.5% as the reporting minimum of either version.

**Check the older MyHeritage display at low confidence.** If a v2.5 ethnicity looks new, check the same kit’s v0.95 view. Set the Genetic Groups confidence slider to Low if it appears, and look under the ethnicity headings and under “Additional Genetic Groups”. Record any geographic clue you find as a Genetic Group, separate from the percentage entries [S35 @2026-11-20].

A tester reported in January 2025 that Georgia appeared in the older view only at low confidence [S34].

## 8. Keep a version log and form hypotheses only from what is left unexplained

- **Log one row per level, broadest first:** level, name in each version, percentage in each version, the range for a region, the pattern from sections 5–7, and any hypothesis [S11].
- **Write a hypothesis only for a change no pattern explains** [S11]. Candidates: a continent move larger than 2 points that no region on a continental boundary explains; a subregion total that moved with no matching loss elsewhere in its continent; a region above its floor that persists across versions and conflicts with the documented pedigree. Name the records or matches that would test it.
- When a revised estimate agrees more closely with a documented line, keep the estimate and the records as separate observations. In one reported Germanic Europe result, the percentage changed from 4% to 37% between updates [S19]. Test the relationship against records and identified DNA matches.

## Close with a version-comparison packet

Return:

- **Version register:** vendor, kit and kit type, assay, version label, processed date, capture date and file names, what was saved (PDF, list, ranges, map, painter, parent views) and what was not.
- **Method rows:** one per version, from section 3.
- **Alignment table:** continent, subregion and region for each version, with old and new names and each mapping judgment.
- **Change table:** each change with its level, both values, the old range and its pattern.
- **Small-region register:** value, the version's floor, published recall and precision or "not published", and status.
- **Open hypotheses:** each unexplained change and the records or matches that would test it.

The comparison establishes no origin, ancestor or parentage by itself.
