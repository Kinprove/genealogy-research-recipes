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

- **AncestryDNA keeps only the current version and the most recent former version, and offers the former for download for 90 days after an update.** Older versions are not available [S1]. Save the previous version first, then the current one [S11].
- **Download route, website only:** the download is not offered in the Ancestry app [S1]. Open DNA > Origins > Regions. Below the last region, next to the update date, click the previous-results link. Then, beside "What changed?", click **Download PDF** [S1], [S11]. Find the link by its position: its wording changes between years ("See what changed and FAQs" in 2024, "View previous results and FAQs" in 2026) [S12], [S11].
- **The PDF lists the previous regions with each percentage and range [S11]. It holds nothing else.** Save every other view while the old version is still live: Chromosome Painter, By Parent (and By Grandparent where offered), Journeys and the map [S11], [S19]. Ancestry users reported an advance "update coming" banner before the 2025 release, and advised screenshotting the Chromosome Painter then, to see which stretches were reassigned [S19]. After the update, the "What changed?" comparison and its PDF are what Ancestry offers of the old version [S1].
- **Capture the current version in full.** Screenshot the whole regions list, from the first heading to the last region, including the update date, and the map. Ranges are not in the list: click each region, then its "i" icon, and record the range [S11].
- **Start every file name with the date in year-month-day order** [S11].
- **Save at every update, even when nothing seems to have changed.** With only two versions online at any time, your files are the only record of earlier versions.
- **MyHeritage:** existing users opt in to v2.5, and the previous model v0.95 stays selectable from the dropdown menu on the results page [S5], [S22]. Capture both versions now.
- **FamilyTreeDNA:** an upgrade to the NGS Family Finder removes the previous results, and FamilyTreeDNA warns that myOrigins can move by a few points [S8]. Save first, as the FamilyTreeDNA recipe describes.

## 2. Date each estimate by when the vendor computed it, and label its version

- **In the Ancestry PDF, "Processed in" dates the estimate; "Downloaded on" dates only your save.** Name the version by the processed date: a file processed in October 2025 is the 2025 estimate, whenever it was downloaded [S11]. A kit first processed after an update has no previous version [S11].
- **Do not take dates from the "What changed?" column headings or the regions-page date.** The same comparison was headed "October 2025 / October 2026" on one day and "Previous / Current" two weeks later [S11]. One presenter's regions page showed October 2024 right after the update and later July 2024, with the same percentages [S17]. Quote a displayed date as displayed, next to your own capture date.
- **Use the version label on the results page, not an announcement or email.** MyHeritage numbers its models (v0.95, a limited v2 in June 2024, v2.5) [S5], [S22]. One user was prompted for "V2.6", then got an email and results reading v2.5 [S20]. FamilyTreeDNA prints "Version 3" at the top of myOrigins [S7]. When no number can be found for a release, as for one 2024 MyHeritage version [S21], label it by its processed or capture date.
- **Rollouts are staggered kit by kit.** Kits in one MyHeritage family updated at different times, with uploaded and native kits in no consistent order [S20]. Ancestry's banner reached accounts at different times [S19]. Before comparing relatives, confirm that both kits show the same version label. Estimates from different versions are different measurements, not evidence about inheritance.
- **A new assay is a new version.** FamilyTreeDNA's NGS upgrade can move myOrigins by a few points without a new model [S8]. Record the assay with the version label.

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

## 4. Align the two versions through the vendor's hierarchy, broadest level first

- **Place every region of both versions in Ancestry's hierarchy: continent, then subregion, then region.** Ancestry's interactive list at `ancestry.com/ethnicity/all-regions` puts each region in one subregion of one of five continents [S10], [S11]. Add up each version by continent, then by subregion, and only then compare regions [S11].
- **Macro-region headings on the results page are a display grouping.** "Celtic & Gaelic" or "West Africa" are not derived from the tester's DNA and carry no percentage of their own [S2]. By late October 2026 the headings showed a percentage equal to the sum of the regions beneath them [S11]. Headings and subregions do not always match one to one: in one example, Northern Europe was the England heading plus the Celtic & Gaelic heading [S11]. Compute every subregion total from its regions, and use the headings only as a cross-check. The previous-version PDF has no headings, so group the old regions yourself [S11].
- **"Subregion" names different levels in different years.** Ancestry's 2024 results showed subregions as finer areas inside a region, calculated partly from DNA matches [S12]. The 2026 list uses subregion for the level between continent and region [S10]. Never align a 2024 subregion with a 2026 subregion by name.
- **A name is not a boundary.** Treat same or similar names in two versions as different regions: "Southeastern England & Northwestern Europe" (2025) and "Southeastern England" (2026); "Western Bantu Peoples" and "Western Bantu & Forest Peoples"; "Canada & United States" and "Atlantic Northeast (Canada & USA)" [S11]. Compare such pairs only through the subregion or continent total they share.
- **Place an old region that no longer exists by its map area** [S11]. Where an old name straddles two groups, count it with the group its name suggests and record which way the error runs. If part of 30% "Southeastern England & Northwestern Europe" was continental, the British total in 2025 was smaller and the 2026 British gain larger [S11].
- **Settler-sounding names in the Americas describe Indigenous-inherited DNA.** In 2026, regions such as "Atlantic Northeast (Canada & USA)" are built only from the Indigenous-inherited parts of reference genomes [S3 p. 5], [S15]. Never align one with a colonial European line.
- **MyHeritage: group the v2.5 ethnicities under the broad v0.95 groups by their maps**, and record each judgment. The boundaries do not nest exactly: East European took in the easternmost part of the old North and West European area, including part of Germany [S21].

## 5. Sort every change into a known update effect before calling it new

Work from the broadest level down. Stop at the first pattern that explains the change [S11].

| Pattern seen | Reading | Check |
| --- | --- | --- |
| A continent moves by 1 or 2 points | Update side effect; regions display as whole percentages, so a continent total can move a point from rounding alone | Treat the continent total as steady |
| One region gains about what its neighbours lose | The same DNA reassigned between look-alike neighbours | Add the gains and the losses inside the subregion; read the subregion total |
| A region drops to 0 and new names appear in the same area | Split, rename or retirement | Is the old name still on the current list? Compare the shared parent total |
| A region moves, but the new value sits inside the old range | The range gives no reading; go on to the subregion total | Section 6 |

- **A trade between neighbours is inside what Ancestry counts as correct.** In its 2026 single-origin tests, raw precision for a region is about 50%, while weighted precision, which counts an assignment to a genetically similar neighbour as a correct reading, is above 90% for most regions [S3 pp. 18, 22]. The hard choice is between close neighbours: England has six neighbouring regions, Nigeria eight and Mexico 15 [S3 p. 13]. Ancestry staff say this applies to large percentages too, not only small ones: which neighbour receives the DNA depends on who is in the reference panel [S16].
- **Worked reassignment:** Great Britain rose 15 points; Ireland and the Nordic countries fell 5 each, Western and Southern Europe 2 each. The losses total 14, close to the gain, so the DNA was reassigned. Northern Europe rose only from 55% to 60%, mostly with the 4 points Western and Southern Europe lost, and Europe as a whole moved one point [S11].
- **Worked split:** West Africa went from seven regions to nine, with nearly every name changed, while its total moved from 33% to 31% [S11]. Compare the West Africa total. Never divide an old percentage among the new regions.
- **"New" next to a region is a naming event.** Ancestry labels newly reported regions "New", and Ancestry staff explain such labels as a former single region broken out into several [S14], [S16]. Align a "New" region through its parent total before reading it.
- **A trade that runs over several updates is still an update effect.** One tester's Scotland went from 66% to 51% to 26% across three successive versions, while England & Northwestern Europe rose from 28% to 55% in the last step [S19]. Watch the subregion total, not one region's trend.
- **A category that disappeared with a version says nothing against that ancestry.** MyHeritage dropped Maasai and Sierra Leonean in v2.5 for lack of training samples and says they may return [S5]. Ancestry split its former Germanic Europe region and retired its Middle East region [S2].

## 6. Compare the new percentage with the old range, never one range with another

- **Ranges from different versions are built differently.** Ancestry's 2026 ranges come from measured error in simulated people of known ancestry [S3 p. 25]; its 2025 ranges came from 1,000 alternative model paths [S4 p. 19]; a 2013 Ancestry presentation described the percentage as the average of 40 runs [S9]. Do not compare an old range with a new one. A narrower new range is not new certainty about the person.
- **Ask one question: is the new percentage inside the old range?** Connacht fell from 10% (range 1–10%) to 2%; Leinster rose from 1% (0–10%) to 5%; three regions fell to 0% from ranges that already included 0 [S11].
- **Inside the old range:** the old estimate already allowed this value, so the move alone is no evidence about ancestry [S11]. Read its subregion total first, because neighbouring regions trade share, then run the region through sections 7 and 8 [S11]. A region that keeps bouncing between updates is wobble [S11].
- **Outside the old range:** look for a section 5 pattern first: a reassignment or split pushes one region outside its old range while the subregion total holds [S11]. If no section 5 pattern explains it at the subregion or continent level, it becomes a section 8 hypothesis.
- **Record every current range now.** The next update's PDF prints them, but only for 90 days [S1], [S11].

## 7. Apply the version's own reliability floor to small regions

- **Ancestry floors: 5% for planning, 2.5% for credibility.** Below 5%, a region is a hypothesis in every version: the 2025 paper measured a much higher error and missing rate below 5% [S4 p. 21], and the FAQ as of September 2026 says regions below about 5% more likely reflect DNA that is difficult to assign [S2]. Below 2.5%, the 2026 paper still reports a much higher error and missing rate under the new method [S3 p. 18], so such a region counts for nothing on its own.
- **Regions near the reporting minimum come and go by chance.** Ancestry reports only regions above a minimum share, which it does not publish. It spreads the rest over the reported regions and shows those windows as "Unassigned" in the Chromosome Painter [S3 p. 16]. A region sitting at that minimum can appear in one update and not the next with essentially unchanged evidence [S3 p. 16]. An "Unassigned" stretch is one whose low-probability assignment Ancestry filtered out [S3 p. 16]; it assigns no ancestry to that stretch.
- **Decision rule:** a region below 5%, or one that appeared or vanished between versions, is a hypothesis. Do not make it a research objective by itself. Carry it forward only with documents or with matches, as in [AI for DNA research](ai-for-dna-research.md) [S11].
- **Look up the region's published recall and precision before weighing it.** Recall answers whether testers with that ancestry usually get the region; precision answers whether testers who get it usually have that ancestry [S18]. Ancestry publishes per-region figures for a selection of regions only: a selected list in 2026, and in 2025 only regions updated in that release [S3 p. 19], [S4 p. 24]. If the region is missing from the table, record "not published"; never borrow a neighbour's figure. Precision falls below 50% for some regions, such as Burundi & Rwanda, West Midlands and Northeast Germany in 2026 [S3 p. 20].
- **Trace regions no longer exist.** Ancestry once listed "trace regions", renamed them "low confidence regions" in 2016–2017 and removed them in 2018 [S13]. Do not count the disappearance of a saved trace region as a change in the estimate.
- **Expect updates to clear away 1–2% regions.** Many 2026 Ancestry results lost odd 1% and 2% regions [S14]; MyHeritage's June 2024 update removed many small components [S20]. That is the floor at work, not a correction of the pedigree.

## 8. Keep a version log and form hypotheses only from what is left unexplained

- **Log one row per level, broadest first:** level, name in each version, percentage in each version, the range for a region, the pattern from sections 5–7, and any hypothesis [S11]. This log is the only multi-year comparison that will survive.
- **Write a hypothesis only for a change no pattern explains** [S11]. Candidates: a continent move larger than 2 points that no region on a continental boundary explains; a subregion total that moved with no matching loss elsewhere in its continent; a region above its floor that persists across versions and conflicts with the documented pedigree. Name the records or matches that would test it.
- **A new version that fits the paper trail better does not confirm the paper trail.** One tester's Germanic Europe went from 4% to 37%, closer to the documented lines [S19]. That shows the model changed, not that the pedigree is right.

## Close with a version-comparison packet

Return:

- **Version register:** vendor, kit and kit type, assay, version label, processed date, capture date and file names, what was saved (PDF, list, ranges, map, painter, parent views) and what was not.
- **Method rows:** one per version, from section 3.
- **Alignment table:** continent, subregion and region for each version, with old and new names and each mapping judgment.
- **Change table:** each change with its level, both values, the old range and its pattern.
- **Small-region register:** value, the version's floor, published recall and precision or "not published", and status.
- **Open hypotheses:** each unexplained change and the records or matches that would test it.

The comparison establishes no origin, ancestor or parentage by itself.
