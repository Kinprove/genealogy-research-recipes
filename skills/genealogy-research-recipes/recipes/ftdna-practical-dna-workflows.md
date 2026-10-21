# Recipe: Maintaining FamilyTreeDNA exports and tree links

## Goal

Keep a usable FamilyTreeDNA (FTDNA) match/segment dataset through exports, name collisions and tree
relinking. The output is a paired export, a name-safe joined table and a dated link/bucket inventory.

For a public Y-DNA project, the output can instead be a dated Group Time Tree view packet:
selected subgroups, visible branches/estimates, display exceptions and any authorized
administrator configuration check. This route does not require Family Finder exports.
For a Family Finder Matrix question, save a dated comparison roster and metric-labeled cells,
with separate references for any focal and direct-pair interval evidence. This route also works
without the paired exports.
For a supplied animated map, preserve the node and time view actually inspected, including
any displayed upstream substitute. Its locations and dates remain attributed model output.
For two supplied Y-haplogroup labels, retain their report basis and the actual comparison
reference before interpreting the observed joining node or shared display categories.
All worked dataset examples below are synthetic.

## The failure to prevent

A match name is a join key, not a unique person identifier. Matching Bucket and Linked Relationship
are values observed at download. Record link changes separately from the retrieval date, keep the
export choice and kit with the rows, and refresh match metadata after relinking.
A Matrix pair value reports sharing between two matches; it does not locate that sharing on
an interval where both overlap the focal kit.

## Before starting

For workflows 1–4, use authorized account access and start with the paired export in workflow 1. FTDNA downloads
require two-factor authentication. [H6]
Keep original files and profile details private; use opaque handles in shared summaries.

For an authorized kit-continuity handoff, distinguish present access from a recorded kit
manager and any separately recorded beneficiary. Leave missing or unconfirmed designations
unresolved; shared credentials do not establish either designation. The [2023 update](https://dna-explained.com/2023/12/11/familytreedna-2023-update-past-present-and-future/)
motivates this distinction without establishing current forms, legal effect or continuing access.

## Eight workflows

### 1. Export the match and segment pair, and record its scope

On Family Finder Matches, use **Export CSV → All Matches** for the match list. In the Chromosome
Browser, use **Download All Segments** for all matches' segment rows; **Download Segments** produces
only the comparison subset. [S1, S2, H6, H7]

Record kit, retrieval date/time, export choice, active filters and row counts for both files. Compare
match-file rows with the displayed All Matches count; count distinct segment-file names separately
from interval rows. Compare the distinct-name sets in both directions for the all/all pair.
If names are absent from the segment file, check that **Download All Segments**, rather than
**Download Segments**, was used. If names are absent from the match file, check **All Matches**
rather than a filtered export. After correcting the export choice, re-export both files in the same
session. Resolve remaining name mismatches through the note-handle procedure below before joining. Record intentional filtered or
selected exports as subsets with their criteria and actual export choice.

When the match list is filtered by ancestral surname or haplogroup, treat the result as a search
subset. A surname search may return similar spellings: check each returned row's surname fields for
the target surname, and mark the others `similar-name hit` before following their shared matches. A
haplogroup filter or same-haplogroup indicator covers only haplogroups FTDNA holds for those kits.
Record a match missing from that result as `haplogroup not shown`, not as carrying a different
haplogroup. The [2021 search discussion](https://www.youtube.com/watch?v=gNFNKpvy1no) motivates both
checks, including a haplogroup known only from another vendor's test that did not appear. It leaves
untested whether an upload changes this. It does not establish current matching rules, current
filter behaviour or how the surname columns are filled.

Treat a match-date value as the date shown on that match row, not as the match's test date, chip version or processing cohort. A [Family Finder match-date discussion](https://genarchivist.net/showthread.php?tid=275) reports older matches showing 2021 dates after matching was recalculated. It also shows a kit's order history and administrator lab-results view recording a later chip procedure for an earlier order. Where authorized, take test and chip history from those records; otherwise record `test date unknown`. The posts do not establish which rows were re-dated, or the current display rules.

A match present in only one of two dated exports of the same kit is a list change (`absent in later export` or `new in later export`, with both retrieval dates), not relationship evidence. A [Family Finder reprocessing discussion](https://forum.molgen.org/index.php/topic,1298.0.html) shows matches removed and later restored after provider reruns; it does not establish current processing or which list is correct.

**Artifact:** export manifest, one row per file: kit handle, retrieval date/time, file name, tool, export
choice, active filters, scope (`all`, `filtered: <criteria>`, `selected: <n>`), row count, interface
count, `links_as_of`, check results. **Stop when** the recorded scope, displayed match count and
cross-file name check reconcile. Carry that scope into the joined table.

**Synthetic manifest example:** kit `K1`, retrieval date/time `2026-10-03T10:00:00Z`, file `K1-matches.csv`, tool
`Family Finder Matches`, export choice `All Matches`, active filters `none`, scope `all`, row count
`240`, interface count `240`, links as of `2026-10-02`, checks `passed`.

### 2. Join matches to segments without collisions

The match file has one row per match; the segment file repeats a match for each reported interval.
Use the match CSV's full-name column, rather than its separate first/middle/last-name columns,
and compare its exact values with names in the segment CSV. [S1, S2] Use files from the same kit
and export session. Hold out duplicated names and any unmatched spelling for the note-handle
procedure below.

For each held-out person, open the separate match profiles and assign opaque local handles in the
private working ledger. Append that person's handle to their FTDNA match note, preserving the
existing note. Notes are included in the match CSV: re-export the pair through workflow 1 and
verify that each handle identifies exactly one metadata row. [S1, H7]

On the Matches page, select only the row for one handled person and click **Compare Relationship**.
In the Chromosome Browser, use **Download Segments** and label the resulting file with that handle.
Repeat for each other person. Keep the original ambiguous segment rows out of the join; replace
them with the labeled single-match files, joined to their handled metadata rows. [H6, H7]
Use the displayed **Shared DNA**, **Longest Block** and linked relationship as cross-checks; the
note handle binds the row even when those values tie. Keep views by match and by chromosome/start/end.

Carry **Linked Relationship**, **Matching Bucket** and **X-Match cM** from the match export into the
joined table. Those columns preserve the tree relationship, provider side assignment and X amount
without retyping the screen. FTDNA reports X matches only for people who also match on an autosome;
X-only relatives do not appear in this Family Finder match export. [S1] Keep the original exports and
save the join as a separate file.

**Artifact:** joined table and a collision ledger mapping note handles to selected-match files.
**Stop when** every held-out person has a unique note handle and a labeled single-match
segment file. Do not join a held-out person until both conditions hold.

### 3. Inventory links before any tree change; relink deliberately

Before connecting, switching or disconnecting the MyHeritage tree, seed a link inventory from the
match export's **Linked Relationship** and **Matching Bucket** columns, then record the corresponding
tree person from your existing link ledger and documented pedigree path for each linked match.
[S1, S4] The MyHeritage tree does not mark who is linked, so the inventory comes from the FTDNA
side. [H3] After a tree transfer, formerly linked people arrive flagged in the GEDCOM, but each must be searched and confirmed again through Account Settings → Genealogy →
Link your matches: **Search**, then confirm each suggested person. These are suggestions, not
preserved links. [H3]

To link a match: **Link on Family Tree** beside it, then search the person's name as written in
MyHeritage, including prefixes and the maiden surname. [S4, H3] Candidates return with relationship
to the kit, full name and birth/death years; choose by the documented path recorded beforehand, not the first
name hit.

**Artifact:** link ledger — match handle, tree person, relationship, side, documentary basis, date,
status (`linked`, `suggested-unconfirmed`, `not in tree`, `deliberately changed`). **Stop when**
every inventoried person is linked again, absent from the new tree, or deliberately changed with
a recorded corrected path/removal reason. There must be zero `suggested-unconfirmed` rows at
completion; those rows are work still to do.

**Synthetic link-ledger example:** match `M1`, tree person `P1`, relationship `maternal second
cousin`, side `maternal`, documentary basis `synthetic record set D1`, date `2026-10-03`, status
`suggested-unconfirmed`. Leave it in that state until its FTDNA link is confirmed.

### 4. Anchor Family Matching with side-specific relatives

Family Matching requires a Family Finder result, matches, a MyHeritage connection and at least one
linked maternal or paternal match. It uses linked testers from parent to third cousin and excludes
linked relatives whose shared DNA contradicts the stated relationship (a "parent" calculated as a
second cousin). To assign a match, FTDNA detects a shared phased DNA block between the tester,
match and linked relative: the block is carried by the same alleles and meets the special Family
Matching threshold. The linked relative's tree position supplies the parental side. ICW is not
used for bucketing. [H4, S5]

Link documented relatives who identify one side first: parents and grandparents, then aunts,
uncles and cousins. Children and full siblings share both sides and cannot split them. [S5] An
anchor linked under the wrong parent supplies the wrong side to phasing. The shared-cM relationship check does
not validate a relative's tree position: trace each anchor's path to the kit holder's mother or
father.

Capture maternal, paternal, both and unassigned counts before each anchor link. After linking,
check that the anchor's Matches row shows the expected **Linked Relationship**, then re-export
the match list. Record the link-change time separately from the export time and save the bucket
counts shown in that dated export. [H3, H4]

Compare the dated counts and known-side paths. If counts are unchanged, check H4's eligibility
conditions: the correct person linked, relationship within parent-to-third-cousin range, and
shared DNA consistent with that relationship. If a bucket conflicts with a documented path,
check the tree positions of the linked kits on the reported side and look for an additional path
through that parent. Correct or remove a misplaced link and re-export. With anchor identities and
tree positions verified, the bucket means FTDNA found a qualifying phased block shared with a
linked relative on that side. A documented relationship through the other parent does not refute
that assignment. Record both and test the additional descent path using `ai-for-dna-research.md`.
Preserve the provider's assignments exactly, including unassigned rows, in each snapshot.

**Artifact:** before-link and later dated exports, bucket counts and a `links_as_of` note.
**Stop when** each new anchor is confirmed on its match row, checked against H4's supported
relationship range and shared-DNA validation, and included in a post-link export. Record
unavailable anchors separately. Compare that export with the baseline and send any remaining
side/path conflicts to `ai-for-dna-research.md` with the two exports and the link ledger.

### 5. Record a Group Time Tree view and its display scope

Use this workflow for a project's public Y-DNA Group Time Tree. It does not require the
Family Finder exports above. A public project view contains selected participating Big Y
lineages; it is shaped by subgroup selection and publication settings. [S6–S8]

1. Open the project's public website and its **DNA Results → Group Time Tree** entry, or find
   the project through Discover's **Group Project** search. Select the relevant subgroup(s)
   before reading the tree. Record the project URL, retrieval time and selected subgroup names.
   A broad selection can combine distant branches and compress the recent part of the
   timeline; narrow the selection to the documented project question. [S6, S8]
2. Save the visible view and record the displayed branch label, time estimate and interval
   exactly as shown, together with the selected display options. Distinguish a branch estimate
   from a named historical person's dates. A dashed connection can represent collapsed
   intermediate branches in this selected view. It does not show that those branches or their
   SNPs are absent from the underlying tree. [S6, S8]
3. If the view is blank or a known participant's details are missing, diagnose the display in
   order: selected subgroup, presence of participating Big Y results, public project results
   settings, member sharing and update timing. A padlock can hide a member's name or earliest
   known ancestor. Record `details withheld` rather than inventing the missing identity or
   classifying that kit as absent. Save the retrieval date and recheck date; the 2023 instructions
   describe periodic updates, not an immediate reflection of every change. [S6, S7]

**Optional administrator branch:** use authorized Group Administrator access to inspect the
project's public-results configuration. Save the previous settings before any change. The
Group Time Tree instructions require public Y-SNP or Y-STR results; use a public report only
within the project's agreed publication scope. Arrange the relevant Big Y kits into useful
subgroups and verify the entered display names and earliest known ancestors. Those ancestor
fields are maintained in the account; the administrator guide does not derive them from an
uploaded tree. Preserve member sharing choices. [S6, S7]

The 2023 S6 instructions locate report-publication options at GAP → **Public Website**,
per-member Y-DNA result display at **Public Results Display Settings**, and subgroup assignment
at **Member Subgrouping**. Use these dated entry points to locate the corresponding functions;
record the current screen names and controls actually offered before any change. [S6]

A member's **Account Settings → Project Preferences → Group Project Profile** sharing choice
controls permission to publish that project profile. Administrator access levels are a separate
setting. Having access to a kit does not by itself authorize its public display. Check the
public tree after an update and record unresolved display exceptions instead of changing a
member's opt-in to make a row appear. [H8]

When using a project Country Map beside the tree, inspect and record the map's own included
population and active filters. Do not carry the tree's subgroup selection over by assumption.
Label a broader project population separately from the selected paternal line; leave an unknown
population unresolved. The [tree preview](https://dna-explained.com/2023/01/13/sneak-preview-introducing-the-familytreedna-group-time-tree/)
and [administrator example](https://dna-explained.com/2023/01/17/project-administrators-how-to-prepare-your-project-for-familytreednas-new-group-time-tree/)
motivate this cross-view check; their dated descriptions do not establish one current map rule.

If the question needs broader tested-tree context, retain an available broader branch view
beside the selected project view, with its own branch, population and selection. Project
membership, map population and haplotree country counts do not carry over automatically.
The [project-to-broader-tree example](https://dna-explained.com/2023/10/18/y-dna-haplogroup-o-when-and-how-did-it-get-to-the-americas/)
supplies this handoff; modern earliest-ancestor places plus node ages do not establish a
historical ancestor's location, migration or identity.

When quoting a branch's tester count, country distribution or ancient-sample list from FamilyTreeDNA's public trees or Discover, record the view, branch level and retrieval date with each number. A [haplotree-versus-Discover count comparison](https://genarchivist.net/showthread.php?tid=275) found materially different country counts for the same branch, matching the pages' own descriptions of FTDNA-tested users versus testers plus academic participants; an [mtDNA Ancient Connections versus Classic Tree count](https://genarchivist.net/showthread.php?tid=1508) also differed, without an explained cause. Do not combine, subtract or substitute counts across views, and do not read a sample missing from one view as absent from the branch. The threads do not establish each view's current inclusion rules or completeness.

Treat a public haplotree surname report as a display subset, not a branch roster. A [surname-report discussion](https://genarchivist.net/showthread.php?tid=275) quotes a display rule requiring at least two kits with public project-profile sharing and the same surname spelling; posters also observed names listed only at the kits' terminal branch. Record a surname missing from the report as `surname not displayed`, not as evidence that no tester of that surname sits on the branch, and note the branch level viewed. The thread does not establish current display rules, and a listed surname does not establish a shared recent ancestor.

When a Discover branch shows a tester who is not among the kit's matches, check whether the branch's suggested projects lead to a public project results page listing that tester. Record the project URL, retrieval date and the displayed surname, earliest known ancestor and haplotype exactly as published, labelled as project-display data. Record how the project row was tied to the branch entry; if the link rests only on inference, label it `unconfirmed link`. A [Discover-to-project lookup](https://genarchivist.net/showthread.php?tid=416) motivates this route. It shows only what that project chooses to publish. It establishes no match, contact route or genealogical connection.

**Artifact:** one dated view record: project URL, selected subgroups, display options, branch
label, displayed estimate/interval, screenshot reference and participant-display exceptions.
If you administer the project, add a private configuration record: prior/current public-report
settings, subgroup assignment, member sharing state observed, change time and next public check.

**Stop when** the saved view can be reproduced from its recorded subgroup/display selection,
and each expected but unresolved display is labeled `selection mismatch`,
`no participating Big Y result verified`, `details withheld`, `update pending` or
`unresolved`. A publication change remains pending until checked in the public view.

**Synthetic example:** project `P1`, subgroup `Documented branch A`, retrieved
`2026-10-07T10:00:00Z`, branch `synthetic node N1`, displayed interval `copied from view V1`,
exception `K2: details withheld`. This record establishes what was visible in that selection,
not that a historical ancestor has been identified. Send lineage, SNP or date interpretation
with the saved view to `genealogy-research-recipes` → `ydna-mtdna-interpretation.md`.

### 6. Record a Family Finder Matrix comparison

Using authorized access, select the intended people on Family Finder Matches and open the
Matrix, or select them within the Matrix. Save the focal kit handle, retrieval time, exact
roster and displayed comparison label. The documented quantities are **Total Shared cM**,
**Number of Shared Segments**, and **Predicted Relationship Range**; current Help uses slightly
different labels for the same three choices. Record the label actually offered. [S9, H9]

Keep each metric separate: the cM and segment-count views exclude X; the relationship range is
a provider estimate, not a documented pedigree relationship. Preserve each selected pair's
displayed value, including any blank or unavailable state, rather than turning it into a
measured zero. [S9] Use `dna-comparison-controls.md` for the common observation-state rules.

For an interval question, save the focal Chromosome Browser comparison for the same people,
including coordinates and build when available. A Matrix cell does not identify the segment
that the two matches in that cell share with each other. Before recording that pair as sharing the
focal overlap, obtain its direct pair segment comparison through an authorized data source
and check the interval. A count of one segment does not replace that check. Without it, record
`mutual interval unverified` and retain the group as a lead. [S9, H6]

**Artifact:** one row per selected pair and metric: focal kit handle, retrieval time, roster,
row/column handles, displayed metric label/value, focal-interval reference, direct-pair reference
and interval status. **Stop when** the selected roster and displayed values or unavailable states
are preserved, and every interval claim has direct-pair evidence or remains explicitly unverified.
Route segment trust and triangulation to `xdna-phasing-judgment.md`, and ancestral attribution to
`ai-for-dna-research.md`.

### 7. Inspect the node actually displayed in a supplied time map

For a dated Globetrekker view or recording, retain the requested terminal node and the node
actually displayed, including an upstream substitute. If a later co-located marker covers
an earlier node, use an actually available earlier time view, enlargement or linked tree to
inspect it; otherwise record that view as unavailable. The [2023 map-view example](https://dna-explained.com/2023/08/04/globetrekker-a-new-feature-for-big-y-customers-from-familytreedna/)
motivates this check without promising current controls or validating the model.

**Artifact:** node identifier, time/view and source reference, with the displayed location/date
labels and any substitution or inspection gap. An obscured marker is not absent data; a model
path is not a documented ancestral journey or evidence identifying a particular ancestor.

### 8. Preserve the inputs and reference in a two-label comparison

Keep both supplied Y-haplogroup labels verbatim with their stated assay/report basis and
retrieval date. In an actually available comparison, record which input or logged-in report
serves as the displayed reference. Preserve conflicting labels rather than silently resolving
them. Save the observed joining node and paths separately from shared study, celebrity or
geographical categories. An upstream label or upgrade prompt does not establish assay history.
The [2023 comparison example](https://dna-explained.com/2023/10/11/new-discover-tool-compare-haplogroups-more-at-familytreedna/)
motivates this input/reference crosswalk without promising current controls, colours or access.

With each supplied Y label, also record the haplotree version shown in Discover's About section, if available, and the date the label last changed. Treat a label that changed recently or is under a pending analysis as `provisional`. Recheck it after a later published tree version, including the haplogroup's variants/equivalents details. A [Big Y results discussion](https://genarchivist.net/showthread.php?tid=6) reports a dated snapshot version, publication lag and a placement that reverted within a day. It establishes no current update cadence, waiting period or error rate.

**Artifact:** two source-labelled inputs, the observed reference/view and displayed results,
with unresolved labels or unavailable views. These are attributed provider outputs, not
measured pairwise DNA sharing or documented descent from a named person. Send interpretation
to [Y-DNA and mtDNA judgment](ydna-mtdna-interpretation.md).

## Hand off interpretation

Use `myheritage-dna-match-investigation.md` first for MyHeritage work. Verify MyHeritage export
availability and coverage for the kit; if an export is unavailable, preserve the selected
displayed evidence manually and mark that recipe's packet scope as `selected_matches`, never
`complete_match_list`. For FTDNA, use the export manifest and joined-table schema above.
Before adapting those schemas to another vendor, verify its available exports and fields.
For side/path conflicts and additional descent paths, use `genealogy-research-recipes` →
`ai-for-dna-research.md`. For segment validity, triangulation and X, use
`genealogy-research-recipes` → `xdna-phasing-judgment.md`. The joined table and bucket snapshots are
inputs to the relevant interpretation.
