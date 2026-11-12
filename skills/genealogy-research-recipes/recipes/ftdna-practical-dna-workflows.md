---
id: "ftdna-practical-dna-workflows"
title: "Maintaining FamilyTreeDNA exports and tree links"
summary: "Eight FTDNA workflows for Matrix observations, paired match/segment exports, duplicate-name joins, MyHeritage tree links, Family Matching and public Y-DNA Group Time Tree, supplied Globetrekker map or two-label comparison packets."
kind: "platform"
scope: {"platforms": ["familytreedna"], "tasks": ["Family Finder CSV scope, opaque note handles, selected-match segment files, transferred links that need confirmation, dated parental-bucket inventories, subgroup selections, branch estimates, obscured map nodes, hidden details or authorized project-display checks."]}
privacy: "genetic-third-party"
gates: ["privacy-transfer"]
guardrails: [{"id": "FTDNA-PRACTICAL-DNA-WORKFLOWS-01", "text": "A match name is a join key, not a unique person identifier. Matching Bucket and Linked Relationship are values observed at download. Record link changes separately from the retrieval date, keep the export choice and kit with the rows, and refresh match metadata after relinking."}]
handoff: ["ai-for-dna-research", "dna-comparison-controls", "myheritage-dna-match-investigation", "xdna-phasing-judgment", "ydna-mtdna-interpretation"]
checked: "2026-10-03"
checked_basis: "checked 2026-10-03"
capabilities: {"browse": ["familytreedna"], "local_script": [], "extensions": [], "data_transfer": ["export", "link", "publish"], "contact": []}
router: {"tier": "full", "group": "Featured workflows", "order": 39}
---

# Recipe: Maintaining FamilyTreeDNA exports and tree links

## Contents

- Goal
- The failure to prevent
- Before starting
- Eight workflows
- Hand off interpretation

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
Authorized access covers analysis, not tree changes: workflows 3 and 4 also need the privacy
gate in `SKILL.md`, set out at the start of workflow 3, before any tree connection or
match link.

For an authorized kit-continuity handoff, distinguish present access from a recorded kit
manager and any separately recorded beneficiary. Leave missing or unconfirmed designations
unresolved; shared credentials do not establish either designation. The [2023 update](https://dna-explained.com/2023/12/11/familytreedna-2023-update-past-present-and-future/)
motivates this distinction.

For a tester who has died, FamilyTreeDNA's kit-access FAQ asks for proof of death (a death
certificate or an unambiguous obituary) and then gives access to the listed beneficiary, who may
pass it on. With no beneficiary, or a deceased one, it asks for the document appointing the
executor or personal representative; anyone else needs that person's written authorization
[S34 @2026-11-12]. FamilyTreeDNA also says it can give a recorded Kit Manager access when the
tester has died and no beneficiary is named [S35 @2026-11-12]. Record which route the requester
has and which documents exist; until one is in place, record the kit as `access route not
established`, not as lost. A living tester who wants the kit usable later names a beneficiary (a
person or a Group Project) and a Kit Manager in Account Settings [S35 @2026-11-12]. Estes reports
that a project administrator given Advanced access in Project Preferences can order upgrades
that the administrator pays for [S36 @2026-11-12]. These are the tester's own settings: describe
them, and do not change them for the tester.

For an intended mtDNA/autosomal match intersection, record the verified tested person,
each kit identifier and which test results are available to the actual query. If results
are held under separate kit identities and the available query cannot combine them, record
the intersection as unavailable, not an empty match result. Before any separately authorized
transfer or additional test, verify the intended destination kit and current provider handling.
Retain the test-to-kit mapping and query scope. The [2025 discussion](https://www.youtube.com/watch?v=essG5JYMERw)
motivates this check without establishing a current kit-merging rule. [S19] Read a returned
multiple-test roster with the Advanced Matches checks at the end of
[workflow 6](#6-record-a-family-finder-matrix-comparison).

## Eight workflows

### 1. Export the match and segment pair, and record its scope

**Privacy gate:** <!-- privacy-gate: export --> The match list and segment file, including any
re-export, hold living matches' names and DNA data; answer the privacy gate in `SKILL.md` first.

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
checks, including a haplogroup known only from another vendor's test that did not appear.

For a same-surname search, also compare the Y haplogroups shown for male matches. A label may
be STR-predicted, derived from the Family Finder test (partial, SNP-based) or SNP-tested; a
more refined Family Finder label replaces the STR prediction. Ancestry and 23andMe transfers
show no haplogroup to matches, and female testers have no Y label: record those as
`haplogroup not shown`, never as a mismatch. A label from a different source or at a different
depth is not a conflict until both labels have been put into Discover's **Compare** and recorded
as in [workflow 8](#8-preserve-the-inputs-and-reference-in-a-two-label-comparison). If they fall
in the same lineage, keep the man as a candidate for Y-DNA testing or for shared-match and
triangulation work. Reliable, incompatible SNP-defined lineages rule him out as a recent direct
paternal-line candidate, even within one major haplogroup; he can still be an autosomal relative.
Different upstream and downstream labels alone do not establish incompatibility. [S24, S26, S27, S28]

Read a match's ancestral surname list as self-reported. Its order carries no fixed meaning: a list may run by generation, alphabetically or in order of appearance, and a [2020 FamilyTreeDNA walkthrough](https://dna-explained.com/?p=31186) shows surnames shared with the viewer moved to the top in bold. Do not infer side, generation or line from a surname's position. To reconstruct the tree of a match without a usable tree, search compiled trees for combinations of the listed surnames and any most distant paternal and maternal ancestors named on the profile. Record a couple found this way as `candidate couple` until descendancy research accounts for the other listed surnames; list any surname it leaves unexplained. A [2024 case-study article](https://www.legacytree.com/blog/genetic-genealogy-proceed-if-a-dna-match-never-responds) motivates this check. [S20, S21]

Treat a match-date value as the date shown on that match row, not as the match's test date, chip version or processing cohort. A [Family Finder match-date discussion](https://genarchivist.net/showthread.php?tid=275) reports older matches showing 2021 dates after matching was recalculated. It also shows a kit's order history and administrator lab-results view recording a later chip procedure for an earlier order. Where authorized, take test and chip history from those records; otherwise record `test date unknown`.

A match present in only one of two dated exports of the same kit is a list change (`absent in later export` or `new in later export`, with both retrieval dates), not relationship evidence. A [Family Finder reprocessing discussion](https://forum.molgen.org/index.php/topic,1298.0.html) shows matches removed and later restored after provider reruns in 2012–2013.

**Artifact:** export manifest, one row per file: kit handle, retrieval date/time, file name, tool, export
choice, active filters, scope (`all`, `filtered: <criteria>`, `selected: <n>`), row count, interface
count, `links_as_of`, check results. **Stop when** the recorded scope, displayed match count and
cross-file name check reconcile. Carry that scope into the joined table.

**Synthetic manifest example:** kit `K1`, retrieval date/time `2026-10-03T10:00:00Z`, file `K1-matches.csv`, tool
`Family Finder Matches`, export choice `All Matches`, active filters `none`, scope `all`, row count
`240`, interface count `240`, links as of `2026-10-02`, checks `passed`.

**Privacy gate:** <!-- privacy-gate: export --> Preserved files hold the tester's raw data and
origins report and living matches' match and segment data; answer the privacy gate in `SKILL.md`
before saving them.

Before an independently authorized upgrade or replacement of an existing Family Finder
result, preserve the currently available match and segment files, raw data and origins
report, or the supplied views where exports are unavailable. Record each saved product's
kit, date and processing/test version, plus anything unavailable to save. Keep later results
separate. The [2026 upgrade notice](https://blog.familytreedna.com/family-finder-ngs-upgrade/)
warned that prior results would be removed and described different export access for transfer
kits. [S12]

A kit transferred from another company holds only that company's data file. No DNA comes with an
upload, so the upload gives FamilyTreeDNA no sample [S30 @2026-11-12]. For a transfer customer who
has never submitted a sample to FamilyTreeDNA, the Family Finder NGS upgrade is the first time
FamilyTreeDNA sequences that person's DNA, and a collection kit is mailed after the order
[S12 @2026-11-12]. The Autosomal Unlock has been retired [S46 @2026-11-12], [S31 @2026-11-12].
A transfer that was never unlocked has its matches and the Family Finder Matrix [S12 @2026-11-12]
but no Chromosome Browser, Chromosome Painter, myOrigins or ancientOrigins [S31 @2026-11-12],
[S46 @2026-11-12]. A missing Chromosome Browser there reflects the lock, not missing data, and
workflow 2's single-match segment files cannot be made: keep held-out persons out of the join as
`unresolved`. For workflow 1's export pair the sources disagree. Estes's August 2026 table lists a
segment download as free [S31 @2026-11-12]; FamilyTreeDNA says a locked transfer cannot save its
data before an upgrade [S12 @2026-11-12]. Record each file the account does not offer as
`unavailable`, not as an empty result.

Before concluding that a tester who has died or cannot swab again can get no further
FamilyTreeDNA test, have the account holder ask Customer Service whether samples from an earlier
test remain in storage, how many and how old [S31 @2026-11-12], [S32 @2026-11-12]. Stored samples
degrade, and older ones are less likely to give a result [S32 @2026-11-12]. Record the answer and
its date. Estes ordered Family Finder on her late mother's stored sample, so that close relative
is at FamilyTreeDNA, and later at MyHeritage by upload, but can never be at AncestryDNA or 23andMe
[S33 @2026-11-12]. A close relative missing from those two databases may still be at
FamilyTreeDNA.

### 2. Join matches to segments without collisions

The match file has one row per match; the segment file repeats a match for each reported interval.
Use the match CSV's full-name column, rather than its separate first/middle/last-name columns,
and compare its exact values with names in the segment CSV. [S1, S2] Use files from the same kit
and export session. Hold out duplicated names and any unmatched spelling for the note-handle
procedure below.

**Privacy gate:** <!-- privacy-gate: export --> The re-exported pair and each single-match segment
file hold living matches' names, note handles and DNA data; answer the privacy gate in `SKILL.md` first.

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

**Privacy gate before connecting a tree or linking a match:** <!-- privacy-gate: link --> A link ties a tester's DNA
result to a person in the tree, and the tree's settings decide who else can see that person and
relationship. Before connecting or switching a tree, or linking or relinking a match, answer the
privacy gate in `SKILL.md`: record each match and tree person involved, inspect the current tree and
profile visibility settings, and require explicit permission covering each link from the kit
holder and from the linked tester. Account access does not establish it. If permission or
visibility is unclear, keep the ledger rows local and leave the current link unchanged. Apply the
consent rules in [AI for DNA research](ai-for-dna-research.md#verification--privacy-discipline).

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

**Privacy gate:** <!-- privacy-gate: link, export --> Each anchor link puts a relative's DNA result on the tree, and each re-export saves living matches' data. Apply the
workflow 3 checkpoint (the privacy gate in `SKILL.md`) to every anchor before linking or relinking, including that
relative's own permission; keep each re-exported file on the user's device and delete it when the question is answered.

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

To work one grandparent's line, do not filter to that parent's bucket. A match is bucketed only
when it shares a segment with a linked relative on that side, and some matches stay unassigned
even with close relatives linked [S41]. If neither that parent nor any relative from that
grandparent's line is linked, many of the line's matches sit in the unassigned rows. Work that
side's bucket and the unassigned matches together, and set aside only the opposite side's bucket
[S42]. Keep any match from that bucket that also has a documented or plausible path through the
target grandparent: a match related through both parents sits in one side's bucket when only that
side has a qualifying linked relative [S41].

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

**Privacy gate:** <!-- privacy-gate: publish --> Public project results expose members' display
names, earliest known ancestors and Y results, and members may be living; answer the privacy gate
in `SKILL.md` before any publication change, and preserve member sharing choices.

**Optional administrator branch:** use authorized Group Administrator access to inspect the
project's public-results configuration. Save the previous settings before any change. The
Group Time Tree instructions require public Y-SNP or Y-STR results; use a public report only
within the project's agreed publication scope. Arrange the relevant Big Y kits into useful
subgroups and verify the entered display names and earliest known ancestors. Those ancestor
fields are maintained in the account; the administrator guide does not derive them from an
uploaded tree. Preserve member sharing choices. [S6, S7]

The 2023 S6 instructions locate report-publication options at GAP → **Public Website**,
per-member Y-DNA result display at **Public Results Display Settings**, and subgroup assignment
at **Member Subgrouping**. Start from these entries and record the screen names and controls
actually offered before any change. [S6]

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
motivate this cross-view check.

If the question needs broader tested-tree context, retain an available broader branch view
beside the selected project view, with its own branch, population and selection. Project
membership, map population and haplotree country counts do not carry over automatically.
The [project-to-broader-tree example](https://dna-explained.com/2023/10/18/y-dna-haplogroup-o-when-and-how-did-it-get-to-the-americas/)
supplies this handoff; modern earliest-ancestor places plus node ages do not establish a
historical ancestor's location, migration or identity.

When quoting a branch's tester count, country distribution or ancient-sample list from FamilyTreeDNA's public trees or Discover, record the view, branch level and retrieval date with each number. A [haplotree-versus-Discover count comparison](https://genarchivist.net/showthread.php?tid=275) found materially different country counts for the same branch, matching the pages' own descriptions of FTDNA-tested users versus testers plus academic participants; an [mtDNA Ancient Connections versus Classic Tree count](https://genarchivist.net/showthread.php?tid=1508) also differed, without an explained cause. Do not combine, subtract or substitute counts across views, and do not read a sample missing from one view as absent from the branch.

Record whether each Discover report was read in the public view, through a shared page, or signed
in through the tester's own kit. Signed in with a Big Y kit, Discover shows up to 30 Ancient
Connections for the haplogroup, against up to 10 otherwise [S37 @2026-11-12]. Globetrekker and the
Y-DNA Match Time Tree open only for a Big Y tester signed in to that kit [S38 @2026-11-12],
[S39 @2026-11-12], [S36 @2026-11-12]. Estes saw two or three Ancient Connections on a publicly
shared page where the signed-in tester had more than 20 [S40 @2026-11-12]. Record a report missing
from a public or shared view as `not inspected in this view`, never as absent.

Treat a public haplotree surname report as a display subset, not a branch roster. A [surname-report discussion](https://genarchivist.net/showthread.php?tid=275) quotes a display rule requiring at least two kits with public project-profile sharing and the same surname spelling; posters also observed names listed only at the kits' terminal branch. Record a surname missing from the report as `surname not displayed`, not as evidence that no tester of that surname sits on the branch, and note the branch level viewed. A listed surname does not establish a shared recent ancestor.

When a Discover branch shows a tester who is not among the kit's matches, check whether the branch's suggested projects lead to a public project results page listing that tester. Record the project URL, retrieval date and the displayed surname, earliest known ancestor and haplotype exactly as published, labelled as project-display data. Record how the project row was tied to the branch entry; if the link rests only on inference, label it `unconfirmed link`. A [Discover-to-project lookup](https://genarchivist.net/showthread.php?tid=416) motivates this route. It shows only what that project chooses to publish. It establishes no match, contact route or genealogical connection.

An mtDNA tester listed in a Discover haplogroup report but absent from the kit's mtDNA matches may
simply be beyond the match threshold. At the coding-region level, tested only by mtFull Sequence,
two testers match with up to three differences and only within the exact same haplogroup
[S43 @2026-11-12]. Estes gives this threshold as the reason a tester may not match everyone in the
haplogroup [S44 @2026-11-12]. Record such a tester as `not a match at this threshold`, not as
outside the haplogroup or unrelated.

Before searching a project's public results for a line, set the page size so every row is on one page; a browser search of the first page alone gives a false negative. A [2026 walkthrough](https://dna-explained.com/2026/10/23/focus-step-2-finding-the-y-dna-and-mitochondrial-dna-of-your-ancestors/) changed a default of 25 rows to 5000. If a very large page size fails to load, step through the pages instead. Search the earliest-known-ancestor column for each surname in the documented line, generation by generation, in every subgroup: results sit in subgroups the project administrator defines. A haplogroup's colour can mark it as predicted rather than SNP-confirmed. Record a surname hit as `candidate row` until the listed ancestor is shown to be a documented member of the line; for mtDNA, that means a woman in the direct maternal chain or her matrilineal relative, such as a sister. [S29, H11]

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

The Matrix compares at most ten selected matches at a time [S9 @2026-11-12], [S45 @2026-11-12].
Split a larger roster into separately saved comparisons, each with its own roster record. A pair
that never shared a saved comparison is `not compared`, not a blank cell.

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

For a locality or surname question, check whether the authorized focal kit offers a
project-restricted Family Finder view, such as the Advanced Matches report demonstrated in
[this 2026 project example](https://www.youtube.com/watch?v=84MgafRdVg0). Save the focal kit,
selected project, test/filter state, retrieval date, returned identities and displayed
relationship labels. Record the project's stated admission scope, or `unknown` if unavailable.
This is a roster of matches to that focal kit within the selected project: membership or
concentration does not establish origin, an ancestral path or pairwise matching among members.
Use it as a scoped documentary research queue.

For a supplied Advanced Matches result using multiple tests, preserve each selected test and
the displayed combination setting. Establish whether the supplied setting requires a match on
all selected tests or includes matches on any selected test before using its roster; if that
scope cannot be verified, record it as unknown. Keep differently configured results separate.
The [2025 example](https://dna-explained.com/2025/09/02/mitochondrial-dna-a-z-a-step-by-step-guide-to-matches-mitotree-and-mtdna-discover/)
distinguishes these scopes for mtDNA and Family Finder. Matching the focal kit on both tests
does not establish that both matches come through the same ancestor or descent path; such a
match still needs
[separate ancestral-path analysis](ydna-mtdna-interpretation.md#combining-tests-establish-which-ancestral-path-each-supports). [S11]

When a Y-DNA test is among the selections, record the exact Y choice. A
[2026 example](https://dna-explained.com/2026/11/02/focus-step-3-breaking-through-brick-walls-using-y-dna-and-mitochondrial-dna/)
reports that **All Y-DNA** requires a match at every marker level from 12 through 111, not at
any one level. For a Y/Family Finder overlap, select one Y-DNA marker level both men have
tested and set **Show only people I match in all selected tests** to Yes; otherwise the roster
combines both tests' matches. Record a person absent from an **All Y-DNA** roster as
`not shown under All Y-DNA`, not as a non-match. [S26, H10]

### 7. Inspect the node actually displayed in a supplied time map

For a dated Globetrekker view or recording, retain the requested terminal node and the node
actually displayed, including an upstream substitute. If a later co-located marker covers
an earlier node, use an actually available earlier time view, enlargement or linked tree to
inspect it; otherwise record that view as unavailable. The [2023 map-view example](https://dna-explained.com/2023/08/04/globetrekker-a-new-feature-for-big-y-customers-from-familytreedna/)
motivates this check.

Globetrekker reconstructs only pre-Columbian migrations. For a European or African paternal line
whose descendants live in the Americas or Oceania, the path ends on the original continent
[S38 @2026-11-12]. A non-Native American haplogroup recorded with an earliest known ancestor in
the Americas is not mapped there [S23 @2026-11-12]. Read the endpoint as the branch's modelled
pre-Columbian location, not as where the line last lived or as evidence against a later
migration.

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
motivates this input/reference crosswalk.

With each supplied Y label, also record the haplotree version shown in Discover's About section, if available, and the date the label last changed. Treat a label that changed recently or is under a pending analysis as `provisional`. Recheck it after a later published tree version, including the haplogroup's variants/equivalents details. A [Big Y results discussion](https://genarchivist.net/showthread.php?tid=6) reports a dated snapshot version, publication lag and a placement that reverted within a day.

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
