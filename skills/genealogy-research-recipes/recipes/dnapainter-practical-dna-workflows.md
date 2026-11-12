---
id: "dnapainter-practical-dna-workflows"
title: "Practical DNA Painter maps, matrices and tree worklists"
summary: "Ten practical DNA Painter workflows: paint measured matches, copy or merge maps of one tester, intersect phased inheritance, calculate provisional missing intervals, combine coordinate spans, plan descendant tests, annotate cluster-derived maps, build direct-ancestor gap worklists, audit numeric pair amounts, and inspect Shared cM histograms and two-value range screens."
kind: "platform"
scope: {"platforms": ["dna-painter"], "tasks": ["Paint a new match, map duplication/CSV transfers, Common Segment Generator, Inferred Segments Generator, Distinct Segment Generator, Coverage Estimator, Cluster Auto Painter annotations, ancestral-tree reports, sourced numeric pair matrices, or Shared cM histograms and two-value range screens."]}
triggers: ["Paint a new match", "map duplication/CSV transfers", "Common Segment Generator", "Inferred Segments Generator", "Distinct Segment Generator", "Coverage Estimator"]
privacy: "genetic-third-party"
gates: ["privacy-transfer"]
guardrails: [{"id": "DNAPAINTER-PRACTICAL-DNA-WORKFLOWS-01", "text": "verify the people, chromosome copy and genome build; keep measured comparisons, inferred intervals, coordinate unions, pedigree estimates and documentary tree worklists distinguishable. A relationship note does not assign all of a match's intervals; matrix shading does not establish a relationship, and copied names do not supply cM."}]
handoff: ["unknown-parentage-wato", "xdna-phasing-judgment", "ydna-mtdna-interpretation"]
checked: "2026-10-04"
checked_basis: "accessed 2026-10-04"
capabilities: {"browse": ["dna-painter"], "local_script": [], "extensions": [], "data_transfer": ["export", "link", "publish", "third-party-tool", "upload"], "contact": []}
router: {"tier": "full", "group": "Featured workflows", "order": 40}
---

# Recipe: Practical DNA Painter maps, matrices and tree worklists

## Contents

- Goal
- Inputs and routing
- 1\. Paint a measured match and inspect the saved result
- 2\. Copy or merge map data without changing whose DNA it represents
- 3\. Remap inherited intervals with the Common Segment Generator
- 4\. Calculate provisional missing intervals with the Inferred Segments Generator
- 5\. Combine overlapping comparisons with the Distinct Segment Generator
- 6\. Plan the next descendant's test with the Coverage Estimator
- 7\. Annotate a cluster-derived map without assigning the whole cluster
- 8\. Turn a direct-ancestor tree into a bounded research worklist
- 9\. Audit a numeric pair matrix against its measurements and relationships
- 10\. Inspect Shared cM histograms and a two-value range screen
- Prompt pattern

## Goal

Build a reusable chromosome-map packet and perform the right operation on it: paint an observed match, move existing data, intersect inherited intervals, infer missing intervals, combine overlapping coordinates, or plan another descendant's test. Use a direct-ancestor tree separately when the next task is to inspect pedigree gaps or repeated paths. Use a numeric tester-pair matrix to audit sourced shared amounts beside documented relationships. Use Shared cM histograms and a two-value range screen to inspect sourced pair amounts.

The failure to prevent is treating everything DNA Painter draws or calculates as an observed match. A copied segment belongs to its original comparison; an intersection is coordinate geometry; an inferred interval is a deduction; the Coverage Estimator is a pedigree-based estimate. Keep those outputs distinguishable.

## Inputs and routing

Use a named focal tester, authorized segment tables, known relatives and a specific question. A segment table needs chromosome and start/end positions; retain reported cM and SNP counts when available. Raw genotype files and a match's total cM alone are not chromosome-painting inputs. [S1, S2]

For the ancestral-tree workflow, use a named root and an authorized pedigree or GEDCOM; it does not require segment data.

For the numeric-matrix workflow, use identified tester pairs, sourced shared cM amounts and
separate relationship evidence. An ICW cluster membership or pasted list of names supplies
no missing pairwise amount.

Provider download procedures belong to the relevant provider's documentation; provider investigation belongs to its own recipe. For segment validity, triangulation, X-DNA and phasing judgment use [X-DNA and phasing judgment](../../genealogy-research-recipes/recipes/xdna-phasing-judgment.md). For unknown-person placement use [Unknown parentage and WATO](../../genealogy-research-recipes/recipes/unknown-parentage-wato.md). This recipe owns the subsequent DNA Painter operations.

Keep a small operation register beside the map:

| Field | Record |
| --- | --- |
| Operation | Paint, copy, intersect, subtract, union, coverage estimate, cluster annotation, ancestor-gap worklist, numeric-pair audit or Shared cM histogram/range screen |
| People | Focal tester and both members of each source comparison |
| Inputs | Saved tables, provider, retrieval date, genome build and filters |
| Assignment | Maternal/paternal/unknown and named ancestor, couple or provisional group |
| Output | Saved map, tree or matrix, exported table and notes |
| Status | Observed coordinates or amounts, inferred assignment, provider population estimate, planning estimate or documentary worklist |

This register is a recommended research artifact; it is not a DNA Painter import format. A person's map is a container for research about that person's chromosomes. Do not reuse another person's coordinates merely because their map is convenient.

## 1. Paint a measured match and inspect the saved result

1. Create or open the focal tester's chromosome map. Select one identified relative with a usable pairwise segment table. Preserve the original table before editing or pasting. Require the incoming intervals and any existing painted intervals to use one verified genome build before painting. Convert differing coordinates to that common build outside DNA Painter and retain the originals and conversion record; stop if a build is unknown.
2. **Privacy gate:** <!-- privacy-gate: third-party-tool --> Pasting the segment table and match identity puts a living match's DNA data into DNA Painter; answer the privacy gate in `SKILL.md` first. Open **Paint a new match**, paste the segment table and use **Preview**. Compare the parsed chromosomes and interval endpoints with the original. Record the selected cM filter; parsing successfully does not mean every source row survived it. DNA Painter's documented ordinary painting default is 7 cM, adjustable in the form. [S1, S2]
3. Enter the match identity and assign the supported parental side and ancestor or couple. If the connection is unresolved, use a provisional group. A group label describes your interpretation; it does not establish it. Save the match. [S1]
4. Click a chromosome's number to open it and inspect all painted segments. In the closed view, groups higher in the key cover lower groups at overlapping positions. Dragging a group changes the visible layer, not its coordinates or evidential strength. [S3]
5. Preserve a note explaining the assignment and its source comparison. For an apparent contradiction, inspect the underlying intervals and provider comparison before recoloring anything. DNA Painter cannot compare raw DNA between two matches; a visual overlap is a reason to investigate, not a triangulation result. [S2]

To find candidates for that investigation, click one of the match's segments, choose **View match** and turn on the overlay's switch that shows overlapping segments; the overlay also lists matches who appear to share DNA with this one [S35 @2026-11-12], [H10 @2026-11-12], [H12 @2026-11-12]. Both views are built only from the coordinates entered in this map, so a match never painted cannot appear. Treat every name there as a candidate for the provider's own shared-match or triangulation check, never as a triangulated match.

**Artifact:** source segment table, saved match and assignment note. **Checkpoint:** every retained painted interval can be traced to the correct focal-tester/match comparison; hidden layers have been inspected.

**Privacy gate:** <!-- privacy-gate: export, third-party-tool --> A provider's segment file for the whole match list names every match and holds their segment data; answer the privacy gate in `SKILL.md` before downloading it or importing it into DNA Painter.

To review the whole map rather than one match at a time, download a provider's segment file and import it with **Import segment data**, which needs an active DNA Painter subscription. On 2026-11-12 DNA Painter's import help accepted FamilyTreeDNA's chromosome-browser **Download All Segments** file, a GEDmatch **Segment Search** CSV, a DNA Painter map's CSV export and a file built on its template, and said segment data is currently unavailable from 23andMe and MyHeritage [H9 @2026-11-12]. A 2024 post also lists 23andMe and MyHeritage files downloaded in late 2023 or before, and the output of DNA Painter's Bucketing tool [S10 @2026-11-12]; the current help page does not mention those older files, so check the imported result before relying on one. By default the import leaves out matches sharing more than 2,000 cM and matches already imported from that company under the same name [H9 @2026-11-12]. The 2023 subscriptions post also describes restricting an import to one chromosome or to matches above set thresholds [S29 @2026-11-12]. Record each filter and the imported match count: a stretch with few segments in a filtered import can be the filter's doing. Use the imported map to find stretches where few matches land, apparent personal pileups where more matches stack than elsewhere, and other matches on a segment whose source you have identified [S29 @2026-11-12]. A stack of matches on one interval is a reason to run the pileup and false-match checks in [X-DNA and phasing judgment](xdna-phasing-judgment.md), not a cluster, and an overlap is still not triangulation (step 5).

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Importing FTDNA segment and bucket
files moves the tester's and named matches' DNA data into DNA Painter; answer the privacy
gate in `SKILL.md` first.

If an FTDNA segment map already exists, keep any later import of parental-side information
as a separate operation. Jonny Perl's September 2024 tutorial describes importing a second
file containing FTDNA's match-level maternal/paternal bucket information after the segment
file. Preserve both dated files and check that they concern the same kit and matching
identities. Use that route only if the actual importer and its identity mapping can be
inspected; ambiguous matches remain unresolved. Keep the reported bucket label separate
from your evidence for a segment's parental side or ancestor. If the tool would silently
turn a match-level label into an unsupported interval assignment, retain the label in your
external match notes instead. Save which labels were added, left unassigned or could not
be mapped. [S10]

**Privacy gate:** <!-- privacy-gate: link --> Linking a kit or entering a haplogroup exposes
a tester's Y or mtDNA result in the map; answer the privacy gate in `SKILL.md` first.

For a map's optional Y/mt panel, keep three fields distinct: the reported haplogroup and
its tester/test level, an authorized kit link, and the documented direct-line ancestor
selected for display. A known lineage can be recorded while its haplogroup remains unknown;
choosing an ancestor group does not supply a test result. Check the saved panel and linked
kit before sharing. The chromosome-map panel and an ancestral tree's haplogroup fields are
different objects: record which was edited. If a tree propagates a label to other people,
inspect those annotations and preserve the original tester and the conditional lineage
basis; propagation does not mean those ancestors were tested. Use the
[Y/mt workflow](ydna-mtdna-interpretation.md) to assess the underlying result. [S19, S20]

**Privacy gate:** <!-- privacy-gate: export, third-party-tool --> The bookmarklet, the
downloaded CSV and the DNA Painter tools all handle the tester's own Ancestry segment data;
answer the privacy gate in `SKILL.md` before downloading, importing or pasting it.

Ancestry's Chromosome Painter shows population segments without coordinates. To get them,
use Kevin Borland's bookmarklet, linked from DNA Painter's [ACPS tool page](https://dnapainter.com/tools/acps):
drag it to the bookmarks bar, open the Chromosome Painter page and click it to download a
CSV. Its own page states build 37 output. The older ACPS copy-and-paste route still works,
but since August 2025 it needs a line of JavaScript in the browser console, and it does not
work in Firefox; ACPS estimates positions from build 37 chromosome lengths. Follow the
current steps on the tool page. Import the CSV with **Import segment data**, or paste only
the rows you need into **Paint a new match**; apply the build check in step 1 before adding
them to a map that already holds match segments. For segment sizes, paste chromosome,
start and end rows into the [cM estimator](https://dnapainter.com/tools/cme) and use
**Get centimorgans for a batch**; it takes up to 20 segments at a time and uses build 37.
[S27, S28, H6, H7, H8]

Put each painted population region in its own group labeled as a provider estimate, for
example `Ancestry region — Devon & Somerset`. Never use such a group as a parental-side or
ancestor assignment; ACPS itself warns that Ancestry's split between parents may not be
accurate. Use it only as a clue: compare it with intervals already assigned through
identified matches and with a tested parent's own region segments. When a region segment
lies on DNA assigned to a documented ancestor from elsewhere, the region label loses; it is
not evidence against the documentation. Treat a trace region on one parent's side that is
missing from that parent's own report but fits the other parent's ancestry as a suspected
side error. A region broad enough to cover both branches cannot tell them apart. Leave any
portion the provider does not attribute unassigned. [S27, H6]

**Privacy gate:** <!-- privacy-gate: export, third-party-tool --> FamilyTreeDNA's painted-segment file holds the tester's own DNA data; answer the privacy gate in `SKILL.md` before downloading it or importing it into DNA Painter.

Read FamilyTreeDNA's myOrigins Chromosome Painter segments, downloaded with **Download Segments**, as provider estimates in the same way, with two further limits. FamilyTreeDNA paints by super population or by continental region; its population clusters are listed in the sidebar but not painted [H15 @2026-11-12]. A regional percentage such as Ireland therefore has no painted segment of its own, and its absence is not a contradiction [S34 @2026-11-12]. FamilyTreeDNA also paints each chromosome's maternal and paternal copies in an arbitrary order [H15 @2026-11-12], so never read its haplotype 1 and haplotype 2 labels as parental sides, even when a parent has tested there. The developer found ancestry that came only from his father labelled as both haplotypes, and DNA Painter imports the file as unknown or both [S33 @2026-11-12].

## 2. Copy or merge map data without changing whose DNA it represents

**Privacy gate:** <!-- privacy-gate: export --> Copying or exporting map data moves matches' segment data and identities into the clipboard, a CSV file or another map; answer the privacy gate in `SKILL.md` first.

Choose the smallest transfer that answers the question. Duplicate the map for an alternative analysis; copy one match for a focused comparison; export a filtered subset for an ancestor; export the unfiltered table for a whole-map transfer. Use these as alternate maps of the same focal tester. [S4]

1. Duplicate through the settings cog if you need a working copy. Edit or remove groups in that copy.
2. For one match, click one of its segments, choose **View match**, then **Copy match segment data to clipboard**. Paste into the destination's **Paint a new match** form.
3. For one interval, click the segment, then the chromosome number inside its popup; the clipboard receives that segment's data.
4. For a map or subset, open settings → **All segment data**. Set or clear table filters deliberately, then choose **CSV file**. That CSV contains the table currently displayed. Import it through **Import segment data** where available. [S4]
5. Record the source and destination map names, filters and expected row count. Before pasting or importing into a nonempty map, require the incoming and existing intervals to use one verified genome build; convert differing coordinates outside DNA Painter with a retained conversion record, or stop if a build is unknown. Check the imported interval count, identities and assignments against the exported table; inspect duplicate-looking intervals rather than assuming import deduplicated them.

**Artifact:** original map, working copy or destination map, dated CSV and transfer register. **Checkpoint:** the subset is intentional and the destination still describes the correct tester. To derive a child's map from a parent's phased map, use the next workflow rather than copying the whole map.

## 3. Remap inherited intervals with the Common Segment Generator

Use this when the intervals' chromosome copies are already known. The [Common Segment Generator](https://dnapainter.com/tools/csg) intersects coordinates; it does not compare genotypes or establish that overlapping matches share the same DNA. [S5, H1]

1. Select a phased ancestral interval set for a tested parent and the child's measured inheritance through that parent. For example, intersect a child's match to a grandparent with the relevant parent-map intervals assigned to the child's great-grandparent.
2. Save both input sets and document why they refer to the same inherited chromosome copy. Require both sets and the destination child map to use one verified genome build before intersecting their coordinates. If builds differ, convert the coordinates to that common build outside the generator and retain the originals and conversion record. If either build or chromosome copy is unknown, stop this remapping operation.
3. **Privacy gate:** <!-- privacy-gate: third-party-tool --> These sets carry a parent's and a child's DNA match data into the generator; answer the privacy gate in `SKILL.md` first. Paste the two sets into the generator and record the cM cutoff. Generate the common intervals. The blog's low 3 cM default was chosen for phased known-family data; it is not a general threshold for trusting small matches. [S5]
4. Inspect output endpoints: each interval must lie inside an interval from both inputs. Review X results separately; the author's own worked use required removing false X intervals. [S5]
5. Paint the output on the child's map, naming the ancestral assignment and recording both inputs. Repeat separately for the other ancestral groups.

**Artifact:** paired inputs, intersected intervals and child-map entries. **Checkpoint:** the common genome build, chromosome copy and inheritance path are documented before any ancestral label is carried forward.

## 4. Calculate provisional missing intervals with the Inferred Segments Generator

Use subtraction when a close relative shares a known match on DNA the focal tester did not inherit. This requires the relationship path and grandparents' independence assumed by the method; coordinate subtraction alone cannot establish the ancestor. [S6]

1. Choose a match whose relevant relationship runs through one grandparent and establish that the relevant grandparents are unrelated. For example, use your sibling's comparison with a cousin who descends from your paternal grandfather's sibling. Retrieve two complete, comparable pairwise segment tables: focal tester–match and close relative–match. Record provider thresholds, genome build and comparison completeness. Require both tables and the destination map to use one verified genome build before subtraction; convert differing coordinates outside the generator and retain the conversion record, or stop if a build is unknown. A missing export or unavailable comparison is not a negative result.
2. **Privacy gate:** <!-- privacy-gate: third-party-tool --> Both tables carry living testers' and the match's segment data into the generator; answer the privacy gate in `SKILL.md` before pasting them. In the [Inferred Segments Generator](https://dnapainter.com/tools/isg), put the focal tester–match intervals in **box 1** and the close relative–match intervals in **box 2**. It returns box 2 minus box 1. A partial overlap can split or shorten an interval; reversing the boxes answers another question. [H2]
3. Save the generated intervals. Their cM values are recalculated; do not expect exact agreement with the provider's original values. [H2]
4. For a suitable parent/sibling comparison, a missing interval associated with one grandparent can support a provisional assignment to the other grandparent on that parental side. With a first cousin, the inference may only exclude a particular great-grandparent. Full-aunt/uncle segments can span fully identical regions and include DNA from both grandparents, so do not apply the simple whole-interval rule indiscriminately. [S6]
5. Keep all inferred intervals provisional. Paint using a match name such as `Match A — inferred`; put exclusions in segment notes instead of inventing a positive assignment. Compare with observed intervals before promoting any inferred label. A small shared subset below a provider's reporting threshold can explain an apparent discrepancy. [S6]

Preview inferred intervals before you save them. Paste the generator's output into **Paint a new match**, lower the cM filter below the 7 cM default so that short inferred pieces are kept, and click **Preview these segments** to overlay them without saving; then filter the map to the parental side the inference concerns [S30 @2026-11-12], [H10 @2026-11-12], [H11 @2026-11-12]. The developer lowers the filter to 6 cM in a full-aunt example because inferred intervals are often small parts of larger measured segments [S30 @2026-11-12]. Use the lower filter for inferred output only; it is no reason to paint small ordinary matches.

For the specific tested-grandparent scenario, box 1 can contain your measured match to that grandparent and box 2 can be populated with a full chromosome set to infer the other grandparent's contribution on that parental side. Use this shortcut here for autosomes: remove X from the populated second field before generating and handle X through the linked X-inheritance recipe. Missing X comparison data or a male's paternal-grandparent path otherwise risks an erroneous full-X inference. The built-in full set accounts for unsampled starts on chromosomes 13, 14, 15, 21 and 22; do not replace it with hand-made `1–end` intervals. [S7, H2]

**Artifact:** both pairwise tables, generated intervals and visibly inferred map labels. **Checkpoint:** verify the common genome build, distinguish `no reported interval` from demonstrated absence of inherited DNA, and retain the limited conclusion justified by the relative used.

## 5. Combine overlapping comparisons with the Distinct Segment Generator

Use the [Distinct Segment Generator](https://dnapainter.com/tools/dsg) when several relatives share segments with the same target match and you want the distinct coordinate span represented across their comparisons. Pasting multiple sets returns merged distinct intervals and recalculated cM; the tool assumes build 37. [S8, H3]

1. Save one pairwise table for each relative–target comparison. Label the people and require all input coordinates to be verified build 37 before combining sets. Convert other builds outside the generator and retain the originals and conversion record; stop if a build is unknown. [H3]
2. **Privacy gate:** <!-- privacy-gate: third-party-tool --> Several relatives' segment tables with the target match go into the generator; answer the privacy gate in `SKILL.md` first. Paste the selected sets into the single input box and generate distinct segments.
3. Save the output and total. Inspect an overlapping chromosome to confirm that the shared span is not counted repeatedly.
4. Keep the original per-person tables. The combined output is a coordinate union across these comparisons, not a measured match between an untested ancestor and the target, and not a single relative's ordinary pairwise cM total.
5. Use it to prioritize a match for further tree research while recording the proposed transmission paths and remaining alternatives. The developer presents this use as experimental, not a definitive relationship-identification method. [S8]

**Artifact:** labeled source tables, distinct intervals and a prioritization note. **Checkpoint:** no relationship or ancestral-genome coverage claim is inferred solely from the union total.

Treat the union total as a minimum for what the untested ancestor shared with the target
match only if every interval came through that ancestor and no other path connects the
testers and the target. If you divide the union by a Coverage Estimator percentage
(workflow 6), compute that percentage for exactly the testers whose comparisons formed the
union. Label the quotient a modeled estimate and keep it beside the observed union; a low
percentage magnifies every error in the union. A Shared cM Project lookup from that
estimate is a hypothesis for tree research. The 2022 Legacy Tree article ranks this
estimate as stronger evidence of the relationship than any single tester's pairwise
amount; that ranking is not adopted here, because the quotient carries the coverage
figure's uncertainty while the pairwise amounts are measured. [S25]

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Each sibling's segment table with the match goes into the Shared cM Investigator; answer the privacy gate in `SKILL.md` first.

When the testers are full siblings and the untested person is their parent, use the [Shared cM Investigator](https://dnapainter.com/tools/sci) to estimate that parent's total with the match. Paste each sibling's segments with the match into a separate field. For a sibling who tested and shares nothing with the match, tick **Sibling has tested but shares no segments of DNA with the match**: a blank field leaves that sibling out of the calculation, which raises the estimate [S37 @2026-11-12], [H13 @2026-11-12]. The tool needs valid data from two or more siblings with at least two distinct segments. It totals the siblings' distinct segments and divides by 1 − (½)^S, the average share of a parent's DNA that S siblings carry between them (75% for two) [H13 @2026-11-12], [S38 @2026-11-12].

Label that result a modeled estimate, never a measured cM, before you take it to the Shared cM tool or WATO. It runs low when the parent shared a segment that no tested child inherited, and it can run high when the tested children between them inherited all of it, most of all with only two siblings [S37]. It runs high under endogamy, pedigree collapse or related parents, because it assumes the shared DNA came through one parent [S37], [S38]. In the developer's own check of ten estimates made with four siblings, six came within 5% of the parent's measured amount and one was 25% low; that is a small sample, not an error rate [S37].

## 6. Plan the next descendant's test with the Coverage Estimator

Use the [Coverage Estimator](https://dnapainter.com/tools/coverage) for a different question: how much of an ancestor's autosomal DNA is expected to be represented by tested descendants? It takes a descendancy tree and tester marks, not a segment union. [S9, H4]

**Privacy gate:** <!-- privacy-gate: upload, export --> The descendancy tree holds living descendants' names, testing status and willingness, and a transfer moves a descendant's DNA results; answer the privacy gate in `SKILL.md` before entering or importing the tree, arranging a transfer or downloading the tree file.

1. Start a tree with the ancestor as root; add the documented descendants or import a GEDCOM and select that ancestor. Back up an existing tree before GEDCOM import, which replaces its contents.
2. Mark the descendants whose tests you can use. Check every tester's descent paths to the root: a tester related to the root more than once must appear on each documented path and be marked as tested at each occurrence. These are occurrences of the same tester, not additional independent tests. Record database access; realizing the full represented coverage requires access to the tests in the same database. A mixed-database tree is not automatically an accessible combined research dataset. [H4]
3. Mark deceased people and known testing willingness. Note the current estimate, request next-tester suggestions and compare feasible candidates. Suggestions exclude people marked willing as well as unwilling, so compare willing candidates manually too. A tested child of an already-tested parent does not add coverage in this model. [S9]
4. Record the proposed tester, the request the suggestion implies and the expected change, then compare feasibility with the research question. A suggested descendant may already have tested in another database or without sharing results with you; for that person the suggestion calls for access to the result or, where the research database accepts uploads, a transfer, not automatically a new test. This is a planning estimate based on typical inheritance; actual inherited DNA can differ. [S9, S25]
5. Save to the account where available and download the Coverage tree text file as a recoverable artifact. A browser-local tree can disappear when browser data is cleared. [H4]

**Artifact:** descendant tree, accessible-tester inventory, saved tree file and next-test decision. **Checkpoint:** the displayed percentage remains an estimate; the tree and available tests are checked before interpreting lack of useful matches as evidence against the ancestral hypothesis.

## 7. Annotate a cluster-derived map without assigning the whole cluster

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Cluster HTML, shared-segment CSVs and
the generated map name living matches and carry their DNA data; answer the privacy gate in
`SKILL.md` before importing or annotating them.

When an existing cluster result needs annotations, preserve its original HTML, focal tester,
database, run date and filters. The January 2020 Cluster Auto Painter walkthrough describes
supported cluster HTML and, for its GEDmatch/MyHeritage inputs, a separate shared-segment CSV.
Check the actual importer's requirements before generating a separate working map; a cluster
matrix without matching coordinates is not itself a segment table. [S11]

1. Inspect the generated map's available match report and find an identified match. Check the
   match's source comparison and the cluster it was placed in before annotating it.
2. Record the documented relationship and its source as a match-level note. Assign a parental
   side or ancestor to an interval only when that interval has its own support; leave uncertain
   intervals unassigned. Retain the original cluster membership in the notes or operation register.
3. Review other matches individually and save the annotated map beside the original cluster
   output. Keep the relationship evidence distinguishable from imported cluster membership.

The source describes match/group overlays and group/segment notes. The separate working copy
and annotation register extend this recipe's existing preservation controls. Its worked
example's overlap-to-parental-side inference is not adopted: an overlapping color does not
establish mutual matching, triangulation or an ancestral couple. [S11]

**Artifact:** original cluster inputs, annotated working map and assignment evidence.
**Checkpoint:** a documented relationship has not silently assigned all of the match's
segments or every member of its cluster to one parental side or ancestor.

## 8. Turn a direct-ancestor tree into a bounded research worklist

An ancestral tree starts with the person whose ancestors are being examined. It differs from
the descendancy tree used by the Coverage Estimator in workflow 6. The tutorials describe
GEDCOM root selection, tree completeness and repeated-path views, and a separate Brick Walls
report. Treat their button names, limits and defaults as dated descriptions. [S12, S13, S14]

**Privacy gate:** <!-- privacy-gate: upload, export, publish --> A pedigree or GEDCOM may include
living people; answer the privacy gate in `SKILL.md` before importing it, exporting a report
from it or sharing a view of it.

1. Preserve the input tree and identify the intended root. In the available import or manual
   entry view, record the included generation depth, notes and living-person handling. Check
   the resulting root and known ancestors against the input before interpreting gaps.
2. Inspect the tree's available completeness and repeated-path views. Distinguish a missing
   ancestor within the imported scope from a generation omitted by the import or view. Repeated
   appearances are paths to a person in the supplied pedigree, not independent proof of that
   person's identity or of DNA inherited along each path. [S12, S14]
3. Build a worklist from the available ancestor-gap report or visible tree. Record the displayed
   generation filter and preserve the shown rows when exporting; the December 2024 tutorial
   describes a default recent-generation subset and a CSV of the displayed table. Keep each
   gap or surname clue tied to its branch and label unproved clues as hypotheses. [S13, S14]
4. Keep source-backed annotations separate from inherited colors or automatically propagated
   labels. Before sharing, inspect the actual view and its living-person/notes scope; if that
   scope cannot be checked, keep the worklist local. The output selects documentary follow-up,
   not a new ancestral or genetic conclusion. [S12, S14]

**Artifact:** root and import-scope note, preserved tree, branch-specific ancestor-gap worklist.
**Checkpoint:** every gap is interpreted within the observed tree scope; the percentage or
color of a tree view has not become a measurement of inherited DNA.

When using an available **Dimensions** view, name the category and retain the tree fields
from which its values were generated. Compare generated values with the person's source
facts, especially a country inferred from free-text birthplace. Correct a value only with
support and keep unresolved values unknown. A custom category needs a source for each
person's entry; a propagation checkbox supplies none for that person's ancestors. Save
the checked category view with its root and scope. Religion, cause of death and other
personal facts must not spread through a pedigree merely because a shared color is useful.
The 2021 tutorial supplies category creation and per-value editing; its limits and privacy
defaults require checking in the actual interface. [S21]

For a **Places** view, retain the original birthplace wording beside the generated location
and the root, generation and lineage filters shown. Check ambiguous placements against the
person's supported locality. Where the actual interface offers text-based re-geocoding or
a coordinate selector, save the proposed correction and its evidence, inspect the resulting
placement and keep the original wording. Leave an unresolved place unresolved; a country
default or a map search result does not establish it. A root location omitted by living-person
privacy is missing input, not evidence of an unknown birthplace; do not disclose it merely
to make a map render. The displayed connections link pedigree birthplaces, not observed
travel routes or the transmission of a particular DNA segment. [S22]

## 9. Audit a numeric pair matrix against its measurements and relationships

**Use when:** you have pairwise shared amounts and want to check their entry or compare them
with separately documented relationships. This is a numeric audit, not an ICW graph analysis.

**Privacy gate:** <!-- privacy-gate: third-party-tool, publish --> The matrix holds identified
living testers' shared cM amounts; answer the privacy gate in `SKILL.md` before entering them
or sharing or exporting a view.

1. Give each tester a distinct identifier and retain each pair's provider, report date,
   supplied amount and source. Keep unknown amounts blank. Names copied from a cluster
   do not supply cM values; the November 2025 example explicitly leaves those for manual
   entry. Use only an import or manual-entry route actually available for the supplied
   data, then compare the saved cells with their sources. [S15, S18]
2. Enter relationships separately from measurements and retain their documentary basis.
   Leave an unresolved relationship unknown or in a hypothesis note. If a sibling-clone
   control is available, check every copied relationship for that new tester, including
   half relationships or multiple paths; enter the new tester's own measured amounts.
   The August 2025 example copies relationship labels but leaves cM blank. [S15, S17]
3. Inspect one tester's pair values at a time. Where relationship-based percentile or
   standard-deviation views are offered, retain the selected mode, displayed relationship
   and reference-data label beside the raw amount. Use an unusual display to recheck
   the input, tester identity and relationship evidence. A percentile describes position
   in the referenced distribution; it is not a probability that the relationship is true.
   No SD cutoff, exclusion threshold or reference-model validation is supplied here.
   If the display's basis is unavailable, retain it as an unexplained provider output. [S16, S17]
4. Preserve the original matrix and a correction log. Reopen the saved result after edits;
   do not assume that a historical edit-mode save/cancel behavior still applies. A symmetric
   pair shown twice remains one comparison. Keep any shared/exported view within the
   permissions and fields actually inspected. [S16]

**Privacy gate:** <!-- privacy-gate: export --> A matrix export file holds identified living testers' shared amounts and relationships; answer the privacy gate in `SKILL.md` before saving or sharing it.

When you preserve the matrix, export it in a form that keeps the relationships. On 2026-11-12 the example matrix offered **Export matrix as CSV**, **Export matrix as CSV with relationships** and **Export matrix JSON data**; a JSON file loads back through **Load** and overwrites everything in the matrix, so export the current matrix before loading one [H14 @2026-11-12]. The launch post describes the plain CSV as testers and shared amounts only, and pasted FamilyTreeDNA or GEDmatch data as bringing no relationships [S15 @2026-11-12]. Relationships come from your own entries or from a CSV that includes them [H14 @2026-11-12].

**Artifact:** an identified pair table with source amounts, independently sourced relationships,
observed display mode, discrepancies and correction history.
**Checkpoint:** no pasted name, copied relationship, blank cell or display outlier has become
a measured amount or a new relationship conclusion.

## 10. Inspect Shared cM histograms and a two-value range screen

Use the available Shared cM Project view to inspect a reported amount against a named
relationship's reference observations. Preserve the tester pair, provider, date, total
definition and displayed project version. These totals do not supply painting coordinates.

Where the view also shows relationship probabilities, record the basis it states for them;
if none is stated, record the basis as unknown. A basis drawn from AncestryDNA simulations
or probabilities fits Ancestry's Timber-weighted totals most directly. On 2026-10-23
DNA Painter's Shared cM Project tool credited its probabilities to "stats from The DNA
Geek"; the 2024 Legacy Tree article traces those to AncestryDNA's white paper. Before
using such a probability with another company's total, state that mismatch in the note;
do not present the figure as calibrated for that company. [S26, H5]

1. Open the histogram for a relationship being considered and retain the entered cM,
   bin and displayed number of submissions. A value inside the published range does
   not establish the relationship. Where percentages below and above the entered value
   are shown, record which relationship's distribution they describe. The August 2022
   tutorial uses approximate interpolation within histogram bins; these percentages
   are not probabilities that one relationship is true rather than another. [S23]

   In the probability table, a probability given for a group of genetically equivalent
   relationships belongs to the whole group: do not report it as the chance of one label
   in that group, such as second cousin when the group also holds first cousin twice
   removed. The histograms are per relationship and come from separate reference data;
   keep the two outputs apart. [S26]
2. For an available two-value view, identify both measured tester–match pairs first.
   Check that the two testers have the same genealogical relationship to the match
   under the hypothesis being examined. Full siblings are the tutorial's starting
   example; same-generation cousins need additional path checks. Extra relationships
   through an unshared ancestor or different generations can invalidate this screen.
   Preserve each total's definition; an unavailable comparison is not a measured zero.
   Do not choose between filtered and unfiltered totals to favor a hypothesis. [S24]
3. Enter the two eligible amounts and save the displayed relationship ranges that
   accommodate both. This is a range screen, not a joint probability calculation or
   relationship proof. The November 2022 tutorial's histogram percentages describe
   the **first** input: check the actual view's labels, and swap the order if needed
   to inspect the other amount. Keep the original pair labels with both views. [S24]
4. If using the highest and lowest of several eligible relatives' amounts, retain
   the full measurement set and eligibility checks. The relatives' results are not
   independent evidence. A surprising screen result sends you back to the inputs,
   paths and reference scope; it does not by itself reject a documented relationship.

Read each histogram bar by its upper label: a bar labelled 600 holds the submissions from 501 to 600 cM, so a bar covers the amounts above the previous bar's label up to its own [S31 @2026-11-12], [S23 @2026-11-12]. The relationship box gives the low-to-high range at the 99th percentile [H5 @2026-11-12]; before treating an amount near either end as typical, see where most submissions fall. In the 2020 launch post the parent/child lower bound was 2,376 cM while the great majority of submissions lay between 3,300 and 3,900 cM, and the developer could not tell whether the low ones were outliers or typing errors [S32 @2026-11-12]. For relationships more distant than half second cousin, the box average counts only pairs that shared detectable DNA [H5 @2026-11-12]. Do not use the fifth-cousin average of 25 cM as the amount any fifth cousin is expected to share: the same post estimates that only about 10–30% of fifth cousins share detectable DNA, so a missing match does not by itself count against a distant relationship [S32 @2026-11-12].

Relationships that share one expected amount can put the common ancestor at different depths. In one band of Estes's generation chart, which counts generations back from the tester, the common ancestor with a half 1C3R is in the grandparents' generation, with a 2C2R or half 2C1R in the great-grandparents', and with a 3C in the great-great-grandparents' [S36]. Several relationships share the same expected amount and cannot be told apart by the amount alone [S39]. For a removed cousin the common ancestor also sits deeper in the younger person's tree than in the older person's, by the number of removals. For each relationship the amount allows, search the generation it implies in both trees, using birth years to decide who is in the older generation; do not search only the same-generation depth.

**Artifact:** sourced pair amounts, relationship hypothesis and eligibility checks,
saved histogram/range views, reference version and interpretation note.
**Checkpoint:** a distribution percentage, missing comparison or two-input range fit
has not become a relationship probability or an inferred measurement.

## Prompt pattern

“For focal tester A, perform only [operation]. Inputs are these labeled tables/tree and these documented relationships. Preserve originals. Return an operation register, the resulting intervals, matrix or tree, and the checkpoint result. Keep observed, inferred and estimated outputs distinct. Do not turn an overlap, coordinate union or coverage percentage into a new measured match.”
