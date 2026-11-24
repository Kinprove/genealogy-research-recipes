---
id: "myheritage-dna-match-investigation"
title: "MyHeritage DNA match investigation playbook"
summary: "Investigate MyHeritage DNA matches: the right kit, filtered shortlists, shared-match values, triangulation and Theory of Family Relativity."
kind: "platform"
scope: {"platforms": ["myheritage"], "tasks": ["MyHeritage DNA match investigation, kit relinking, largest-segment sorting, labels/favorites, Shared DNA Matches, Theory of Family Relativity or an investigation follow-up."]}
privacy: "genetic-third-party"
gates: ["privacy-transfer"]
guardrails: [{"id": "MYHERITAGE-DNA-MATCH-INVESTIGATION-01", "text": "Save empty results with their actual query, kit, filters and date. Do not fill an unshown DNA measurement with zero or infer that a person outside the list has no shared DNA."}]
handoff: ["ai-for-dna-research"]
checked: "2026-11-12"
checked_basis: "Rechecked 2026-11-12"
capabilities: {"browse": ["myheritage"], "local_script": [], "extensions": [], "data_transfer": ["export", "link", "publish", "third-party-tool", "upload"], "contact": ["contact"]}
router: {"section": "DNA", "group": "DNA testing sites and tools", "order": 31}
---

# Recipe: MyHeritage DNA match investigation playbook

## Contents

- Goal
- 1\. Start with the right kit and preserve theories before relinking
- 2\. Build a shortlist without losing matches behind an old filter
- 3\. Use labels for branches, notes for evidence, and favorites for follow-up
- 4\. Turn shared matches into specific comparison candidates
- 5\. Use the triangulation shortcut, then compare smaller subsets
- 6\. Audit a Theory of Family Relativity one connection at a time
- 7\. Recover genealogical leads when the match's tree is missing or private
- 8\. Send a message the match or manager can answer
- 9\. Resume with comparable snapshots and a preserved evidence packet
- Artifact schemas

## Goal

Produce a small, reproducible investigation packet: a match shortlist, dated notes and labels,
specific shared-match or segment observations, checked theory paths, and a follow-up queue.
Choose the workflow that answers the current question; running all nine is unnecessary.

**Privacy gate:** <!-- privacy-gate: export --> Exports of match and segment data hold living
matches' DNA data; answer the privacy gate in `SKILL.md` before delegating or running an export.

Use the companion **DNA data export** procedure for export schemas and **DNA match clustering**
for Leeds, AutoClusters and network mechanics. These separate procedures are outside this
playbook; check their availability in your research workspace before delegating those tasks.
Use [DNA research judgment](../../genealogy-research-recipes/recipes/ai-for-dna-research.md) for
relationship inference, endogamy and evidence weighting. This playbook supplies the MyHeritage
working loop and records, rather than another clustering or cM interpretation method.

## 1. Start with the right kit and preserve theories before relinking

**Use when:** managing several relatives' kits, or a kit appears disconnected from its tree.

1. Select the tested person's kit. Record the tested person, kit identifier as displayed, manager,
   linked tree/profile URL, and research question. Keep manager and tested person separate.
2. Inspect the linked profile before interpreting surnames or theories. Compare its identity,
   parents and tree context with the intended tested person; a matching display name is insufficient.
3. Record which tools this kit can open. An inaccessible tree, Shared DNA Matches panel or theory
   is an access limitation, not an empty result. Advanced-tool access depends on the current
   subscription or the kit's existing unlock status; check the current entitlement page.
4. Before correcting a wrong assignment, save every theory you need: match URL, proposed
   relationship, each path and its component links, displayed confidence, review status and date.
   **MyHeritage says reassignment permanently deletes existing Theory of Family Relativity data.**
5. **Privacy gate:** <!-- privacy-gate: link --> Reassignment links a living relative's DNA kit
   to a tree profile; answer the privacy gate in `SKILL.md` first. For a genealogy kit, use Manage DNA kits → kit menu → Re-assign kit to a different person,
   selecting the correct existing profile where available. Before the final Save, verify that
   you have that person's permission to manage their DNA data and check the permission box.
   Stop if permission is missing. Record the permission reference and attestation date in the
   session header, then save and recheck the association.
   The documented reassignment procedure does not apply to DNA Health kits.

On desktop, open the **DNA** tab if it appears on your own tree profile or on a relative's
profile for a kit you manage. Select the tested person's available results [S61 @2026-11-21].
If the tab is missing, open **DNA → Overview** and check which tester is selected
[S62 @2026-11-21].

**Privacy gate:** <!-- privacy-gate: publish --> Sharing a kit's results gives another person a
living tester's DNA matches, ethnicity estimate, Genetic Groups and family-site access
[S2 @2026-11-21]. That can expose living people in the matches and tree. The invitation sends
the collaborator's email address to MyHeritage [S2 @2026-11-21]. Answer the privacy gate in
`SKILL.md` first.

Before inviting a collaborator, review the linked family site's tree permissions. Acceptance
gives the collaborator family-site membership [S1 @2026-11-21], [S2 @2026-11-21]. For view-only
tree access, open **Family Tree → Manage trees → Edit tree settings → Permissions**. Restrict
editing to the webmaster, or allow the webmaster and site managers if the collaborator is a
regular site member [S1 @2026-11-21], [S63 @2026-11-21].

Keep your account password private when a helper such as a DNA coach works a kit
[S1 @2026-11-21], [S3 @2026-11-21]. Use **DNA → Manage DNA kits** → the kit's three-dot menu →
Share DNA results with a collaborator; only someone allowed to
invite members to the kit's family site can send the invitation [S2 @2026-11-21],
[S3 @2026-11-21]. Use this workflow for an adult tester and adult collaborator. Verify that
the collaborator has two-factor authentication on their own account before they open the
results [S1 @2026-11-21]. With the gate cleared, enter the collaborator's email address and
click **Share**. MyHeritage prompts invitees without an account to create one upon acceptance
[S2 @2026-11-21].

Check the arrow beside the kit number in **Manage DNA kits** before assigning any kit work.
Yellow means the invitation is pending, and green means the collaborator accepted
[S2 @2026-11-21]. Hover over the arrow to verify the collaborator's name if shown
[S1 @2026-11-21].

After accepting an invitation, choose the tester's entry with the shared-kit label in the DNA
kit selector. Verify the selected tester before reviewing **DNA Matches**, **Ethnicity Estimate**
or **Genetic Groups** [S1 @2026-11-21], [S2 @2026-11-21]. The collaborator can contact matches
and view or edit the tree as its settings allow. The collaborator cannot download raw data,
delete, reassign or reshare the kit, or change its DNA privacy preferences, and does not see
the notes and labels already on the matches [S2 @2026-11-21], [S1 @2026-11-21].

To change collaborators, check who already has access in **Manage DNA kits**. MyHeritage's
sharing announcement describes one collaborator per kit [S1 @2026-11-21]. In the kit's
three-dot menu choose **Remove results sharing** and confirm. Check that sharing has ended,
then send the replacement invitation through the privacy gate above for the new recipient
[S1 @2026-11-21], [S2 @2026-11-21], [S3 @2026-11-21].

If the former collaborator should also lose tree access, check their membership separately in
**Home → Site members** [S64 @2026-11-21].

To end your own access as a collaborator, find the kit at the bottom of **Manage DNA kits** and
choose **Remove shared kit** from its three-dot menu. This removes the kit from your access list
[S1 @2026-11-21], [S3 @2026-11-21].

**Privacy gate:** <!-- privacy-gate: export --> Downloading a raw DNA file exports the tested
person's genetic data; answer the privacy gate in `SKILL.md` before downloading it.

If one tested person has several MyHeritage kits (for example an upload and a lab-processed test),
record each kit's identifier and processing type before comparing their match lists or cM values.
MyHeritage's FAQ, as read in [GeneaVlogger's review](https://www.youtube.com/watch?v=arP83dD_7a0),
says the downloaded raw-file header states the processing used and that array-processed kits are
not reprocessed. Take the type from the header, otherwise record `not_observed`; do not infer it
from purchase date. This source does not measure how results differ between kit types.

An uploaded kit can only be an earlier one: MyHeritage's help (page dated 21 July 2026) says
DNA uploads are no longer supported. It says nothing about kits uploaded before the change, so record
what such a kit currently shows in the account rather than assuming its matches are gone or
complete.

Keep checking an earlier array kit or a previously uploaded kit for new matches
[S42 @2026-11-18]. MyHeritage's whole-genome sequencing FAQ says both can match testers whose
samples were sequenced [S31 @2026-11-18]. A new test is unnecessary just to keep looking for matches.

### Before replacing the whole linked tree

**Privacy gate:** <!-- privacy-gate: link --> Relinking kits to a replacement tree moves living
testers' DNA kits onto new profiles; answer the privacy gate in `SKILL.md` before each change.

While both trees remain accessible, list the affected kit identifiers and map each old
tree/person reference to its intended replacement. Confirm that the tested person's
profile exists inside the replacement tree using the identity checks above; resolve
absent, ambiguous or inaccessible profiles before removing their old mapping.
Reuse steps 4–5 for theory preservation, permission and reassignment. After an authorized
change, reopen each affected kit and compare its actual linked tree/person with the
crosswalk; record the check date and leave unobserved associations unverified.

This preflight addresses the tree-replacement question in [MyHeritage's 2022 Q&A](https://www.youtube.com/watch?v=0TUlka43n2I).
It supplies no guarantee that replacing a tree preserves links or deleted theories.

**Output:** one session header plus a saved theory packet before any reassignment;
for a whole-tree replacement, also the old/new kit-profile crosswalk and observed links.

## 2. Build a shortlist without losing matches behind an old filter

**Use when:** too many matches, a new branch question, or a surname search seems unexpectedly empty.

1. Start from the selected kit's DNA Matches list. Clear the text search and explicitly inspect
   and remove every unrelated active filter, including labels. Clearing a search is not evidence
   that all filters reset.
2. Write one research question: for example, “Which matches could help identify this grandparent's
   parental village?” Choose a documented relative as an anchor when one is available.
3. Make separate passes for relevant surnames and useful tree information using available
   search/filter controls; inspect ancestral places within match review. Try recorded spelling
   variants. Combined filters use AND: adding a tree or label condition narrows the search.
   The Location filter describes the match's country of residence, not ancestral origin.
   Log the exact query and active filters for each pass; one pass is not whole-list coverage.
4. Use Relationship → Extended Family, then Sort by → Largest segments, where available, as an
   optional pass for closer potential anchors. MyHeritage's Extended Family category covers first
   cousins once removed through second cousins twice removed; third cousins and more distant
   matches are in Distant Relatives. Before interpreting coverage or an empty result for a
   distant-branch question, also run a Distant Relatives pass or remove the Relationship filter.
   Log the remaining query and filters for that pass. Inspect tree-bearing candidates and record
   the chosen sort.
   Save a manageable shortlist with match links, total shared cM, largest segment and segment count
   where displayed, tree availability, reason selected, and next action. A tree or relevant place
   can make a moderate match more useful for this question than an uninformative higher-cM match.
5. Save empty results with their actual query, kit, filters and date. Do not fill an unshown DNA
   measurement with zero or infer that a person outside the list has no shared DNA.

Use **Tree details → Has shared surnames** for a pass looking for any ancestral surname the two
trees share [S51 @2026-11-20], [S52 @2026-11-20]. To look for a particular surname, run a separate
ancestral-surname search with that filter cleared, especially if the name is still missing from
the tester's tree.

When a match card shows a name in brackets after the original, use the Global Name Translation
rendering as a spelling lead. Save both forms with the match's identifier and verify the person's
identity before joining records across scripts [S47 @2026-11-20], [S49 @2026-11-20].

If a name has no transliteration in **Shared DNA Matches**, check **Review DNA Match** for the
bracketed form. If a new-match email shows a transliteration, flag it as a spelling lead and
check it against the match card. Respect a private name and leave its translation unobserved
[S49 @2026-11-22].

For an unknown branch, keep documented matches as anchors and make a separate shortlist of
unplaced matches. Start with a strong unplaced match whose tree or shared matches can move
the question forward. Leave its side open while you test whether it connects to a branch already
documented [S68].

If the first company's list stalls and relatives on the target branch are reported to use
MyHeritage, review an existing authorized MyHeritage kit for the same tester. If a parent helped
sort the first list, include that parent's authorized kit when available. Compare the tester's
results across services for new leads. Log each match under the kit and service that returned it
[S53], [S54].

If the first service gives no usable lead, review any other authorized kit already available for
the same tester, even before you know whether the target branch uses that database. Record the
kit and service that yielded each lead [S68].

When two full siblings' authorized kits are available, run the same shortlist pass for both.
Keep useful matches seen on either list, recording which kit returned each one. Siblings can
inherit different segments and have different matches [S69], [S81].

**Privacy gate:** <!-- privacy-gate: upload --> A new DNA test sends the living tester's kit
activation data to MyHeritage and their cheek sample to its testing lab. Answer the privacy gate
in `SKILL.md` first.

If there is no existing kit and the tester chooses this search, use a new MyHeritage DNA test
for the tester who needs matches [S55 @2026-11-20]. Treat the reported use of the site as a
reason to check that database. Leave relatives' testing status open until you have evidence.

Return to the kit’s DNA Matches list when AutoClusters leaves a lead out of the chart. Its thresholds select only a subset of the kit’s matches [S33 @2026-11-18]. One researcher’s only promising match shared 2.3% and did not appear in the chart [S32 @2026-11-18]. Keep that match on the shortlist.

A failure-to-pay maintenance warrant gave Fuller a possible father’s surname to search in DNA Matches. She reports that his First World War personnel file held court papers in which he admitted paternity and agreed to maintenance [S37]. Compare identifying details such as occupation and next of kin in the personnel file with the warrant and other records [S38]. Record the documentary admission separately from the surname hit.

Do not read few or no Russia-resident matches, or Russian matches missing from an older list,
as evidence about relatives living in Russia. MyHeritage stopped selling DNA kits in Russia at
the end of February 2020 [S4 @2026-11-12]. In emails reported on 31 December 2024, it told Russian users
that their accounts and associated data would be permanently deleted by 1 February 2025
[S5 @2026-11-12], [S6 @2026-11-12]. According to the published exchange, the company said that earlier messages would remain with the sender identified as a deleted member [S6 @2026-11-12]. Log the change in account or message status separately from any inference about the family.

**Privacy gate:** <!-- privacy-gate: contact --> Asking a Cousin Finder relative about DNA testing
contacts a living person; answer the privacy gate in `SKILL.md` first.

Outside the DNA Matches list, MyHeritage's tree-based Cousin Finder lists relatives found through
family trees, including people who may never have tested. Record each entry as a tree assertion
that is only as good as the trees behind it. Do not treat it as a DNA match or a DNA-supported
relationship, and do not give it shortlist cM fields. In one Cousin Finder comparison, relatives who had tested only elsewhere appeared without the “DNA Match” marker. Relatives with a MyHeritage test or upload could carry it [B18]. For an unmarked person, check other companies, or ask the relative when contact is authorized, before planning a test.

**Output:** shortlist rows and a search log, including filtered negative searches.

## 3. Use labels for branches, notes for evidence, and favorites for follow-up

**Use when:** revisiting the same matches or sorting observations into several possible branches.

1. Define a small label key before assigning colors: e.g. `maternal`, `paternal`,
   `candidate:grandparent-A`, `documented:grandparent-A`, and `needs-tree`. Use names to express
   meaning; colors alone do not explain whether an assignment is tentative.
2. Apply multiple labels when a match belongs in several working groups. MyHeritage supports
   bulk label edits; inspect the selected matches and intended label before applying a batch.
   Only the first seven label dots are displayed, so hidden dots do not establish missing labels.
3. Put the reason and next action in the match note; use this compact template:
   `DATE | question | observation + source URL | branch: candidate/documented | next action`.
   Read and preserve an existing note before updating it. Notes have a documented 2,000-character
   limit; keep the longer evidence record in the investigation packet.
4. Favorite the matches requiring a near-term action. A favorite is a queue marker, not a
   relationship conclusion. Filter by the relevant branch label when resuming work.
5. When evidence changes, update the label and note together, recording why. Keep the dated old
   assessment in the packet so a tentative label cannot later masquerade as original evidence.

When resuming from a match review, look for its labels at the top of **Review DNA Match** and
for each shared match's labels on its row. Open the label manager to read the full names and any
labels hidden from the row's display [S43 @2026-11-20], [S46 @2026-11-20], [S60 @2026-11-20].

### Record a relationship you have established

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Saving a confirmed DNA relationship sends the
living tester's and match's kinship and any selected family side to MyHeritage. Answer the
privacy gate in `SKILL.md` first.

Keep the evidence for the established relationship in the private packet. Once the gate is
cleared, verify the kit. On the match card, open the relationship label and choose **Select
relationship**, or use the pencil beside the relationship on desktop or on
**Review DNA Match** [S66 @2026-11-22], [S67 @2026-11-22]. Choose the documented relationship
from the list and select the family side if established, then click **Save relationship**.
If the supported relationship is absent from the list, retain it in the packet. If MyHeritage
instead asks a direct parent, child or full-sibling question, choose **Yes** only when you
have established that relationship [S67 @2026-11-22].

Read the blue checkmark on the match card, **Review DNA Match** or in **Shared DNA Matches**
as a relationship entered by the user for their own view. Record it as a user assertion and
keep its supporting evidence separately. If only a family side was entered, the underlying
relationship label remains an estimate. Review any Theory of Family Relativity separately
[S66 @2026-11-22], [S67 @2026-11-22].

**Output:** label key, dated match notes, and a follow-up queue.

## 4. Turn shared matches into specific comparison candidates

**Use when:** an interesting match has too little tree information on its own.

1. Open Review DNA Match for match A and inspect Shared DNA Matches. Record focal kit, A and each
   candidate B as three distinct people; the manager's name is not a substitute for a tested person.
2. For each useful B, copy the displayed relationships and DNA values with the pair they describe:
   focal–A, focal–B or A–B. If a pair's measurement is not displayed, record `not_observed`.
3. Prefer a B who can answer the question: a documented relative, a useful pedigree, or a relevant
   surname/place. Record why B is an anchor or lead before assigning a branch label.
4. Inspect A's and B's trees for specific people and relationships to investigate. Save the
   relevant profile links and the next record or question required.
5. If the next question is about a shared segment, use workflow 5. Being shared matches does not
   establish that all three share the same segment, nor name the ancestor who supplied it.

In **Shared DNA Matches**, hover over the tree icon on B's row and choose **View tree** if offered.
Hover over the note icon to read your existing note before repeating research
[S43 @2026-11-20], [S44 @2026-11-20]. If the tree cannot be opened, record the access state.

Use the **Shared DNA Matches** sort menu to rank B by DNA shared with A when looking for A's
strongest matches. Choose DNA shared with the focal kit when looking for the tester's strongest
matches. The default ranks by the sum of both amounts. Record which pair drove each pass
[S47 @2026-11-20], [S48 @2026-11-20].

Compare focal–B and A–B for the same shared match [S65 @2026-11-22]. When A–B is much stronger,
start by tracing the connection between A and B, then look for where the tester might join
their pedigree. Keep the three pair measurements distinct and test the proposed branch with
workflow 5 [S68 @2026-11-22].

On an unplaced match's shared-match rows, look for recurring documented branch labels.
Use a recurring label to choose a pedigree to inspect. If labels point to more than one
branch, record each as a candidate and test the connections separately [S71].

Place documented shared matches in the tester’s tree. In the published case, their lines converged on the tester’s great-grandparents, giving the family a couple whose descendants they could trace [S34], [S35]. Record how the unplaced match might descend from the couple, and leave that connection provisional until documents support it. Use workflow 5 to investigate the segment.

**Sort by side in one direction only when your anchor is on one side.** If a known relative on one
side, such as a maternal aunt, is your only anchor there, a match or cluster she shares is a lead to
that side; one she does not share stays unassigned, not paternal. You can carry DNA from your mother
that the aunt did not inherit, so some maternal matches are not shared with her (Price
Genealogy, 2023-07-28 [S20]; Legacy Tree, 2019-06-04 [S21]), and two sisters can carry different grandparents' DNA at the
same position (Perl, DNA Painter blog, 2021-07-28 [S22]). Move an unassigned cluster to the other
side only through an anchor from that side. Workflow 5's provisional other-side group is narrower:
it holds matches that overlap the anchor's own shared segment.

Test both parental sides when a new close match appears during a search for one parent. In one
paternity search, a half-sibling match belonged to the maternal line [S73].

When a second-cousin estimate leads to the two grandfathers, trace both men to their parents.
Check whether they shared one parent or two before assigning a side or a full-cousin
relationship. In one case the match's grandfather was a half-brother of the tester's maternal
grandfather, despite the initial paternal placement [S74].

### Record cM Explainer predictions in their direction and full range

Copy a predicted relationship in the direction MyHeritage gives it: the label says what the match
is to the tested person, so "Aunt" means the match is the tester's aunt, not the reverse
[S26 @2026-11-16]. Keep a directional label as written, such as "parent's first cousin" or "first
cousin's child", rather than collapsing it to "first cousin once removed" (MyHeritage blog,
2023-03-02 [S27 @2026-11-16]). The top label is one estimate among several. Clicking it on the
match card opens every estimated relationship with its probability, while Review DNA Match →
Possible relationships lists only the top four until you click Show more relationships plus
diagram, which adds the less likely ones and their paths [S26 @2026-11-16], [S28 @2026-11-16].
Open the full list before recording that a relationship is not among the predictions.

For a niece or half-niece lead, check which of the match's parents connects to the tester and
whether that parent and the tester share one parent or two. Keep an unidentified half-sibling
among the possibilities [S76]. In one account the match labeled **Niece** was the daughter
of a half-brother [S75].

Before adding or comparing probabilities in the diagram, set its top-right drop-down to all
relationships: only then do the probabilities total 100%, and a full-only or half-only view hides
the rest [S26 @2026-11-16]. The MRCA-probabilities checkbox gives the overall probability that the
pair shares each possible most recent common ancestor. That ancestor's generation is named relative
to the tested person; the same couple can sit further back in the match's tree, for example as
great-great-grandparents where the tester's label says great-grandparents, so do not assume the
same generation on the match's side [S26 @2026-11-16].

Read the explanation below the list before trusting its order: it says whether both ages, one or
neither informed the prediction, and predictions are most accurate with both [S26 @2026-11-16].
The ages come from the dates of birth on file for the kits. MyHeritage says a missing, year-only or
wrong date of birth, a kit assigned to the wrong profile, or a wrong gender on a profile can give
the wrong label, show both "Father" and "Son", or swap aunt and uncle or mother and father labels
[S28 @2026-11-16]. Record which ages were used. When one is missing or doubtful, record the whole
list rather than the top label, and check the tester's own profile as in workflow 1.

When comparing saved low-cM predictions across April 2023, check the dates against the model
revision. MyHeritage reported that its revision moved some predictions toward more distant
relationships and introduced **Estimated relationship** for matches at 100 cM or less.
Compare the recorded DNA amounts independently of the labels [S29].

Read the probabilities as estimates for a single line of descent. MyHeritage's 2023 introduction
says cM Explainer assumes neither endogamy nor pedigree collapse, though DNA shared through several
common ancestors raises the cM above what one relationship gives (MyHeritage blog, 2023-03-02
[S27 @2026-11-16]). Its April 2023 update adjusts only for Ashkenazi Jewish ethnicity, only for
matches under 200 cM, and not in the standalone tool, which has no ethnicity data (MyHeritage
blog, 2023-04-24 [S29 @2026-11-16]). For other endogamous communities, pedigree collapse or a
known double relationship, expect the top predictions to be too close, read the more distant
entries too, and take the analysis to DNA research judgment.

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Entering another company's match
measurement, or an age a match gave you privately, sends a living person's DNA and age data to
MyHeritage's tool; answer the privacy gate in `SKILL.md` first.

When a date of birth is doubtful, get a DNA-only reading: MyHeritage's help says to open cM
Explainer and enter the cM value without ages [S28 @2026-11-16]. Its standalone page,
myheritage.com/cm, takes the shared cM and, optionally, both ages, and also serves pairs tested at
other companies (MyHeritage blog, 2023-03-02 [S27 @2026-11-16]; Mohler, Your DNA Guide,
2023-03-02 [S30 @2026-11-16]). Enter numbers only, never names or kit identifiers.

**Privacy gate:** <!-- privacy-gate: contact --> Asking a match for their age contacts a living
person; answer the privacy gate in `SKILL.md` first.

If a match's age is missing or marked private and the question needs it, ask the match in
workflow 8's approved message, as the 2023 introduction suggests for a match you are in touch with
[S27]. Record the answer as the age the match reported, with its date. Do not look up a match's
age or date of birth anywhere else.

**Output:** a triplet record with pair-labeled measurements and one concrete next comparison.

## 5. Use the triangulation shortcut, then compare smaller subsets

**Use when:** testing whether a candidate shares a particular segment with a documented relative.

1. In Shared DNA Matches, look for the triangulation indicator. On desktop, hover to see the
   reported number of triangulated segments; click it to load the focal kit, A and B directly
   into the chromosome browser. This avoids manually reconstructing that three-person selection.
2. If using the browser directly, start with the focal kit, one documented relative and one
   candidate. Verify the selected people before reading the display.
3. Record the focal kit, browser's triangulated interval and its exact comparison set. Copy chromosome,
   start/end, cM, SNP count and coordinate build only where shown; otherwise use `not_observed`.
   Do not substitute the endpoints of one person's larger pairwise segment for the group's
   common interval or silently guess a coordinate build.
4. The browser supports up to seven matches plus the focal kit. Adding another match changes
   the group being tested. If the larger group shows no common triangulated interval, return to
   the informative three-person set and test additions separately. Keep each result tied to its
   exact members; a failed larger set does not erase a previously observed smaller set.
5. Record `triangulation_observed` or `no_triangulation_displayed` for that comparison. Overlapping
   bars alone do not establish triangulation. Use the documented relative as a lead to a branch;
   identifying a particular ancestor still requires the pedigree and record investigation.

**Privacy gate:** <!-- privacy-gate: export --> A segment export lists living matches' DNA data;
answer the privacy gate in `SKILL.md` before exporting or analysing it.

MyHeritage removed its export of segment data for all DNA matches in October 2023
[S7 @2026-11-12]. To get a segment file, select the matches in the One-to-Many Chromosome
Browser, scroll below the chromosomes and use Advanced options → Download shared DNA info. The
CSV lists any triangulated segments first, then the segments each selected match shares with
the focal kit, and it covers only the selected matches [S8 @2026-11-12]. Record its scope as
`selected_matches` (workflow 9). If DNA pages are refused, check that two-factor
authentication is on: MyHeritage made it mandatory for viewing DNA results by March 2024
[S1 @2026-11-12].

When working from an exported segment file rather than the browser, keep the unfiltered export and
analyse a copy sorted by chromosome, then start position. Matches overlapping a documented
relative's long segment are only candidates. Overlap at one position fits either parent's copy of
that chromosome. Check each candidate against that relative's shared-match list. Put overlapping
non-shared matches in a provisional other-side group to test against an anchor from that side.
Shared-match status is not triangulation, and a missing shared match may reflect a display
threshold. If a cM cutoff removes a candidate from the working copy, repeat the comparison in the unfiltered export. In Baker’s chromosome 13 example, sorting overlapping segments helped select candidates; the sort alone could not assign them to a branch [B16].

**Output:** one segment observation per exact comparison set, with display evidence and date.

## 6. Audit a Theory of Family Relativity one connection at a time

**Use when:** MyHeritage proposes a common ancestor or relationship path.

If the purple banner on DNA Matches offers **View theories**, use it to show all matches with a
theory [S36 @2026-11-18], [S10 @2026-11-18]. Use the Tree details filter below when the banner
is absent. On an individual match card, choose **View theory** and open each path tab in the
diagram [S36 @2026-11-18], [S12 @2026-11-18].

1. Save the proposed relationship, common ancestor, complete path and alternative paths before
   changing its review state. Overall displayed confidence is the lowest confidence of the
   component Smart/Record Match links, not a probability that the relationship is true.
   Record confidence at the connection it describes. Alternative path tabs are different
   evidence routes for the summarized theory; they are not automatically independent proof.
2. Follow every connection into its underlying tree or record. Distinguish a tree-to-tree identity
   match from a parent–child relationship: inspect identity evidence and the parentage asserted
   on either side of the join. Smart Matches and Record Matches can be wrong.
3. Create one row per connection with person/profile links, claim, underlying source, disposition
   (`supported`, `unresolved`, `contradicted`) and the exact next check. A copied claim in two
   trees is one assertion repeated, not two independent records.
4. Compare the proposed relationship with the observed DNA using the judgment recipe; do not
   replace a missing record with the theory's displayed confidence. An unresolved connection
   leaves that path provisional; inspect alternative paths separately.
   A path with every connection `supported` still does not show that the shared DNA came through
   it; the DNA may come from another line, as a
   [Legacy Tree review of these theories](https://www.legacytree.com/blog/myheritage-dna-theories-of-family-relativity)
   notes. Test the line against the match's shared matches and its AutoClusters cluster (run
   through the companion clustering procedure), looking for relatives documented to the proposed
   couple. Without that support, record the DNA source as unresolved.
5. Confirm or reject only after review. Save the reason in the packet. Confirmation tracks your
   assessment; it neither supplies documentary proof nor automatically updates the family tree.
   No theory means no generated suggestion currently visible, not no biological relationship.

Use **Confirm** or **Reject** above the full theory path and check the resulting status on the
DNA Match card. If new evidence reopens the question, select **View theory** and undo the decision
to return that theory to pending. When a card has several theories, record status in each theory's
own view. A card can show confirmed when only one theory is confirmed
[S11 @2026-11-20], [S50 @2026-11-20].

**Check the family group behind each connection, not only the join.** Test the family the
underlying tree shows against your records and against plausibility. Kessler found two near-namesakes born in 1796 and 1848 recorded as brothers in a theory. The 52-year gap suggested that the younger man might instead be a grandson [S23 @2026-11-14]. Mark the unsupported link `contradicted` or `unresolved`, consider where a generation may have been missed,
and keep the connections your records support. Two siblings with
one given name are only a warning sign: in many families the later child was named after one who
had died (Hoitink, Dutch Genealogy, 2014-07-16 [S25 @2026-11-14]). MyHeritage lets you confirm or
reject a theory as a whole, and its wiki says to confirm one that is accurate through any path
[S24 @2026-11-14], so keep the per-connection results in the connection ledger and decide on the
paths that survive.

MyHeritage adds theories in periodic runs, not as trees or matches change [S9 @2026-11-12],
[S10 @2026-11-12]. Its 2022 conditions are a tree that includes at least the tester, the
parents and the grandparents, and a plan with the advanced DNA features or the one-time unlock
of an uploaded kit; its 2025 update names Premium, PremiumPlus, Complete and Omni as the plans
that show a full theory [S11 @2026-11-12], [S12 @2026-11-12]. Check every authorized kit separately. One tester’s older kit already had theories while her new whole-genome kit had none [S14 @2026-11-12]. Record “no theory” with the kit and the
date checked, and look again after a later run. Theories from
the last 30 days carry a NEW badge, and the Has Theory of Family Relativity option under the
Tree details filter (All tree details in some views) lists the matches that have one
[S10 @2026-11-12], [S13 @2026-11-12], [S12 @2026-11-12], [S19 @2026-11-12].

Use a new-theory email as a cue to recheck the relevant kit and reopen unresolved matches.
Theory emails depend on notification preferences, so use the in-account theory list after a
later run even if no email arrived [S12 @2026-11-22], [S79 @2026-11-22].

Compare a visible theory with the saved path before recording it as revised. The June 2022 run
added theories without revising earlier ones [S11].

To give later runs more people to join on, extend the tree: MyHeritage says the number of
theories depends on the size and detail of the tree [S15 @2026-11-12]. Estes extends each ancestor's line
through the grandchildren where she can [S16 @2026-11-12]; do this with deceased people only.

Before the next run, check for documented deceased great-grandparents and great-great-grandparents
missing from the linked tree. List them for the deceased-only extension above [S11].

**Output:** theory packet, connection ledger and recorded review decision.

## 7. Recover genealogical leads when the match's tree is missing or private

**Use when:** a useful match has no accessible pedigree or its pedigree leaves the connection open.

1. Record whether the tree is absent, private, or inaccessible with the present account. Keep
   those states separate; do not invent ancestors from a surname or ethnicity display.
2. Use the match-review features available to the kit: ancestral surnames/places and useful
   shared matches. Save the actual observation and its source, even if it is only a research lead.
3. Look for a shared match with an accessible relevant pedigree and investigate that person's
   branch. Pedigree View shows direct ancestors and leaves out siblings and spouses; open the
   fuller tree when the question needs collateral relatives. Record which kit the accessible
   tree belongs to; it is not automatically A's tree.
4. Form one bounded question for A or the manager, such as a grandparent's birth surname and
   birthplace, or whether a specified documented ancestor appears in their tree.

Apply the [Living people rule](../SKILL.md#living-people) and skip **Site memberships** on a
living match's member profile [S61 @2026-11-21]. Use the match's accessible tree or a relevant
shared match's pedigree for the family-history lead [S65 @2026-11-21].

For a geography question, compare the tester's and match's **Genetic Groups** on **Review DNA
Match** if that panel is visible. Use a shared group to choose a place to investigate and check it
against the pedigrees. Keep the branch unassigned until you have evidence for it
[S43 @2026-11-20], [S45 @2026-11-20].

When none of the surnames in the match's tree are familiar, make a pass for ancestors who
lived in the target locality at the relevant time. Keep candidates from that pass even if the
match lives abroad. In one case the productive locality lead was in an overseas match's tree
under an unfamiliar surname [S72].

When matches placed on a side give no usable lead to an expected great-grandparent's family,
compare their accessible trees for a recurring ancestor, including unfamiliar names. Verify
that the repeated profiles describe the same person and trace how each match descends from
that person. Keep the genetic connection to the expected line open while testing the new
candidate [S80].

If the target surname is missing from the match names, search the match's accessible tree and
any relevant tree already available from the kit manager. Include the target ancestor's birth
surname. Record where it occurs and which connecting people remain to be found [S56], [S57].

When the connection remains open and a **Smart Match** places a known relative in another tree,
use **Discoveries → Matches by people → Review Match** to inspect the overlap [S58 @2026-11-20].
Compare that branch with the DNA match's tree for the missing person. Check whether a candidate's
child in one tree appears as the match's grandparent in the other, and verify each link before
recording the relationship [S57 @2026-11-20].

**Privacy gate:** <!-- privacy-gate: contact --> A message to a Smart Match tree manager can
disclose living relatives' identities or a tentative relationship to that manager. Answer the
privacy gate in `SKILL.md` first.

If a specific link is still missing, use workflow 8's approved first-message procedure to ask
the Smart Match tree manager where that match offers **Contact**. Ask only for the missing
relationship or its source [S57 @2026-11-20], [S59 @2026-11-20].

When a match at another company has no tree there or only a small one, look for the same
person in this kit's DNA Matches and in Cousin Finder, which finds relatives through matches
between family trees and labels those who are DNA matches [S17 @2026-11-12]. Estes found Cousin Finder trees for people whose match profiles at other companies had no tree [S18 @2026-11-12]. Compare the tree’s people and the shared matches before linking the profiles. A name match alone leaves their identity open.

**Output:** an access-state record, a linked lead, and one answerable question.

## 8. Send a message the match or manager can answer

**Use when:** a particular pedigree detail could resolve the next investigation step.

When an unsolicited message claims a DNA relationship, sign in to MyHeritage directly and look
in the correct kit's DNA Matches and the account's Inbox for the claimed match and any earlier
thread. Compare the displayed pair with the claim and record what you can corroborate before
replying [S77 @2026-11-22], [S78 @2026-11-22], [S82 @2026-11-22].

Before the first approved message to a close match, preserve its minimal visible basis in the
private `selected_matches` packet: kit/match identifiers, observation date, and the relevant
profile/tree or shared-match observations and links. This fixes the basis of the question if
access later changes; it neither establishes why a row disappeared nor turns it into a measured
zero. The [2024 Q&A](https://www.youtube.com/watch?v=Nsir-VBEhWg) motivates this timing;
the limited packet reuses workflow 9's preservation controls.

1. **Privacy gate:** <!-- privacy-gate: contact --> The message discloses tested people and shared
   DNA to a match or manager; answer the privacy gate in `SKILL.md` first.
   Use Contact on the DNA-match card. Identify whether the recipient manages another person's
   kit; address the tested person's relationship in the question.
2. Draft a short message naming the tested people, displayed shared DNA, research question, one
   relevant surname/place or profile link, and the one requested detail. Offer the equivalent
   detail from your own research. Contact from DNA-match cards is documented as free; access
   rules for other contact routes or private trees can differ.
3. Save the draft and obtain the researcher's approval before an assistant sends it. Record the
   sent date, recipient and question; keep reply/no reply separate from an evidence conclusion.
4. On a reply, attach its source and date, then update the next action. A reported family story
   starts a record search; an unanswered message does not contradict a relationship.

Use the approved first-message procedure for an unclustered match when you have one question they can answer. A 2.3% match outside the chart provided the researcher’s only promising lead [S32].

**Output:** approved message and correspondence row.

## 9. Resume with comparable snapshots and a preserved evidence packet

**Use when:** returning after weeks, a theory update, or a change in access/tool availability.

1. Reopen the same kit and research question. Record today's access state, queries and filters;
   compare with the saved session header before comparing lists.
2. Review the branch label and favorite queue, read the notes, and perform the recorded next
   actions. Check unresolved theory connections rather than accepting a new badge as validation.
3. **Privacy gate:** <!-- privacy-gate: export --> Match, shared-match and segment exports name
   living matches; answer the privacy gate in `SKILL.md` before exporting.
   Save the shortlist, comparison sets, theory paths and correspondence with dates and source
   links. Use available exports only after verifying their presence and actual coverage for this
   kit. If an export is unavailable, preserve the selected displayed evidence manually and mark
   the packet's scope as `selected_matches`, never `complete_match_list`.
4. Match observations across sessions using stable match links/identifiers where available.
   Record additions, changes and unavailable observations. A disappeared row under changed
   filters or access is not evidence that shared DNA became zero.

If an expected tester is missing after clearing the filters, check whether you have evidence
their kit is in the MyHeritage database [S42 @2026-11-22], [S83 @2026-11-22]. Check whether
DNA Matching is enabled for the kit you manage. Leave the other person's participation unknown unless established. Opting out can
keep an eligible kit off the match list [S69 @2026-11-22], [S70 @2026-11-22].

If the pedigrees point to third cousins and both kits are eligible for matching, keep the
documented relationship under consideration when the match is missing. Even tested cousins
can share too little DNA to be reported. Keep the pedigree evidence and the negative list
result together in the packet [S84], [S85].

If a retained MyHeritage match-list export contains labels, use those values to reconstruct
the groupings as of the export date. Check the match's live labels before treating the old
grouping as current [S43], [S46].

Recheck the same kit when new matches arrive after an unproductive review [S39 @2026-11-18]. In one case a strong-match email followed a list of distant cousins. The tester opened the account and found a first-cousin match [S40 @2026-11-18], [S41 @2026-11-18]. Read the card and log its relationship estimate before adding it to the shortlist.

**Output:** dated packet and a next-session queue with its actual coverage.

## Artifact schemas

These are investigator-created schemas, not claims about native MyHeritage CSV headers.
Use ISO dates and `not_observed` for unshown values. Keep personal match data in the researcher's
private workspace; the recipe and its examples contain no real match records.

| Artifact | Required fields, in order |
| --- | --- |
| Session | `observed_at, focal_kit_ref, tested_person, manager_ref, linked_profile_url, question, access_state, query, active_filters, sort_by, coverage` |
| Search log | `observed_at, focal_kit_ref, question, query, active_filters, sort_by, coverage, result_state, shortlist_refs, next_action` |
| Match shortlist | `focal_kit_ref, match_ref, match_url, observed_at, shared_cm, largest_segment_cm, segment_count, tree_state, labels, selection_reason, evidence_ref, next_action` |
| Label key/history | `observed_at, focal_kit_ref, match_ref, label_name, color, meaning, prior_label, new_label, reason, evidence_ref` |
| Triplet | `observed_at, focal_kit_ref, match_a_ref, match_b_ref, focal_a_cm, focal_a_relationship, focal_b_cm, focal_b_relationship, a_b_cm, a_b_relationship, anchor_basis_ref, source_url, next_action` |
| Segment observation | `observed_at, focal_kit_ref, comparison_set_refs, chromosome, start_bp, end_bp, segment_cm, snp_count, coordinate_build, triangulation_state, evidence_ref, branch_hypothesis, next_action` |
| Theory packet | `observed_at, focal_kit_ref, match_ref, match_url, theory_ref, proposed_relationship, common_ancestor_ref, path_refs, saved_evidence_refs, displayed_confidence, review_state, decision_reason` |
| Theory connection | `observed_at, match_ref, theory_ref, path_ref, connection_ref, claim, profile_urls, underlying_source_ref, displayed_confidence, disposition, next_check` |
| Correspondence | `match_ref, recipient_ref, draft_ref, approved_at, sent_at, question, reply_state, reply_source_ref, next_action` |

For kit reassignment, extend the Session with `permission_ref` and `permission_attested_at`:
a private reference to the assignee's permission and the date you attested to it in the form.
These fields do not apply to sessions without reassignment.

Completion means the selected workflow has its output record, source links, observation date and
next action. An inaccessible tool stays recorded as inaccessible; it is never a completed check.
