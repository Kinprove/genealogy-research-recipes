---
id: "ftm-research-workflows"
title: "Family Tree Maker: Ancestry Sync, FamilySearch Branches, Places, Web Search, Undo and Guest Sharing"
summary: "Use Family Tree Maker to keep Ancestry record images locally, compare a FamilySearch branch, list people by place, search and merge records, undo edits and share with relatives."
kind: "platform"
scope: {"platforms": ["familytreemaker", "ancestry", "familysearch"], "tasks": ["Ancestry membership lapse", "FamilySearch branch download", "Places workspace", "Web Merge Wizard", "Turn Back Time rollback", "Connect guests and sticky notes"]}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "FTM-RESEARCH-WORKFLOWS-01", "text": "Treat a FamilySearch branch, a Web Search result and a relative's sticky note as leads to check against records, never as facts for the research file."}, {"id": "FTM-RESEARCH-WORKFLOWS-02", "text": "Rolling back returns the tree to its state before the selected action and deletes every later change"}, {"id": "FTM-RESEARCH-WORKFLOWS-03", "text": "Sync before the membership ends"}, {"id": "FTM-RESEARCH-WORKFLOWS-04", "text": "Edit only deceased people"}, {"id": "FTM-RESEARCH-WORKFLOWS-05", "text": "Run it only for people known to be deceased."}, {"id": "FTM-RESEARCH-WORKFLOWS-06", "text": "Do not import the address book and do not look up anyone's email address"}]
handoff: ["evidence-proof-judgment", "ancestry-record-search-recovery", "familysearch-practical-record-workflows", "family-interviews-and-oral-tradition", "dna-match-outreach-staging"]
checked: "2026-11-16"
checked_basis: "read 2026-11-16"
capabilities: {"browse": ["familytreemaker", "ancestry", "familysearch"], "local_script": [], "extensions": [], "data_transfer": ["link", "publish", "upload"], "contact": ["contact"]}
router: {"section": "Research method", "group": "Family trees and research planning", "order": 11}
---

# Family Tree Maker: Ancestry Sync, FamilySearch Branches, Places, Web Search, Undo and Guest Sharing

Use this recipe when the user keeps a tree in Software MacKiev's Family Tree Maker (FTM) and wants to keep Ancestry record images after a membership ends, compare a FamilySearch branch with their own file, list everyone the file ties to a place, search Ancestry or FamilySearch from FTM, undo a bad edit, or collect corrections from relatives. Rick Crume's January 2026 interview for Family Tree Magazine describes these workflows in FTM 2024; it is used here through transcript excerpts (a partial read), and each step names the documentation behind it and the edition that documentation covers [S1]. Treat a FamilySearch branch, a Web Search result and a relative's sticky note as leads to check against records, never as facts for the research file.

For identity and kinship decisions, use [evidence/proof judgment](evidence-proof-judgment.md). For searches on the Ancestry and FamilySearch websites themselves, use [Ancestry record search recovery](ancestry-record-search-recovery.md) and [FamilySearch practical record workflows](familysearch-practical-record-workflows.md). For weighing what a relative says, use [family interviews and oral tradition](family-interviews-and-oral-tradition.md).

## Contents

- What goes wrong
- 1\. Download Ancestry record images while the membership is active
- 2\. Keep a FamilySearch branch as a separate comparison file
- 3\. List everyone the file ties to a place
- 4\. Search Ancestry and FamilySearch from Web Search
- 5\. Roll back with Turn Back Time only when later work can go
- 6\. Collect relatives' corrections through Connect
- 7\. View your own tree in FTM Connect
- Return packet

## What goes wrong

- Expecting an Ancestry tree to keep its records viewable after the membership ends. Ancestry's cancellation help, seen here only in search-result extracts, says that attached records needing a membership stay linked but cannot be viewed, while copies downloaded to the computer remain available. [S2† @2026-11-16]
- Merging a FamilySearch branch, a FamilySearch search hit or a Web Search likely match into the research file as if it were evidence. All FamilySearch users can see and edit the FamilySearch Tree. [S3 @2026-11-16]
- Expecting FTM to send corrections to FamilySearch. The MacKiev articles read here document downloading a branch and matching people, and matching transfers no information from the computer. [S4 @2026-11-16], [S5 @2026-11-16]
- Using Turn Back Time to fix one old mistake. Rolling back deletes every change made after the selected action. [S6 @2026-11-16]
- Reading the Places list as complete while place names are unstandardized. FTM flags an unrecognized name, such as a misspelling or a name missing its county, with a question mark. [S7 @2026-11-16]
- Sharing a tree with guests before checking what they see. MacKiev's FTM 2024 feature list names research notes among what guests can view. [S8 @2026-11-16]

## 1. Download Ancestry record images while the membership is active

Ancestry's help on accounts after cancellation says that records attached to a tree that need a membership stay linked but are not visible after the membership ends, and that records and media downloaded to the computer remain available. The page refused direct access (HTTP 403) on 2026-11-16, so this rests on search-result extracts [S2† @2026-11-16]. FTM 2017, 2019 and 2024 download Ancestry source images to the computer when the tree syncs (FamilySync), but only from databases the user's subscription covers [S9 @2026-11-16]. Sync before the membership ends: afterwards FTM cannot download an image the subscription no longer covers.

1. Make a manual backup with the Media files box ticked. FTM's automatic backups contain no media, and MacKiev advises a backup before any sync. [S10 @2026-11-16]
2. **Privacy gate:** <!-- privacy-gate: link --> A sync also sends the FTM file's changes up to the linked Ancestry tree [S11 @2026-11-16], so answer the privacy gate in `SKILL.md` first for every living person in the file. Private facts, notes and media, and elements linked to private data, do not sync up to Ancestry [S12 @2026-11-16]; mark private what must stay local and record what you marked. Then sync.
3. For each person in the research question, open the source citations. MacKiev says a citation's image download button is no longer available once its image has been downloaded [S9 @2026-11-16]. A citation that still offers the button has no local image: download it while the subscription covers that database, or log it as a gap.
4. Keep the tree file and its media folder on the user's own device, not in a shared folder or another service.

## 2. Keep a FamilySearch branch as a separate comparison file

The MacKiev articles read here document downloading a branch of the FamilySearch Family Tree and matching people to it, but no route that sends FTM data to FamilySearch [S4 @2026-11-16], [S5 @2026-11-16]. Compare in FTM, and correct FamilySearch on FamilySearch itself.

1. Sign in to FamilySearch from FTM, open the Plan workspace and, on the New Tree tab, choose Download a Tree from FamilySearch. Set the home person (Me, or another person's FamilySearch Person ID), the number of ancestor and descendant generations, and whether to add each ancestor's descendants. FTM saves the branch as a new tree, matches every person in it to FamilySearch and shows FamilySearch hints for them. MacKiev's article covers FTM 2019. [S4 @2026-11-19]
2. Keep that tree as its own file and do not merge it into the research file: it copies a tree that all FamilySearch users can see and edit [S3 @2026-11-19], and MacKiev describes no later synchronization of the copy [S4 @2026-11-19].
3. Compare it with the research file person by person. Log each difference (name, date, place, parent, spouse) with its FamilySearch Person ID as a question for records, not as a correction to either tree.
4. **Privacy gate:** <!-- privacy-gate: publish --> Attaching a record to a person on the FamilySearch website publishes the link between that record and that person in a tree that all FamilySearch users can see and edit [S3 @2026-11-19]. Answer the privacy gate in `SKILL.md` first. To match a person already in the research file, select the person, open Web Search, pick the FamilySearch result and click Match. Matching adds only a FamilySearch Person ID fact and transfers no information from the computer. FTM cannot merge FamilySearch historical records directly: attach the record to the person on the FamilySearch website and then merge the data in FTM, or use Web Clipping. [S5 @2026-11-19]
5. **Privacy gate:** <!-- privacy-gate: publish --> A correction to FamilySearch is published to a tree that all FamilySearch users can see and edit [S3 @2026-11-19]. Answer the privacy gate in `SKILL.md` first. Edit only deceased people: FamilySearch keeps living people in private spaces visible only to those with access, while deceased people are typically in the public space that all users see [S13 @2026-11-19]. Make each change on FamilySearch one person at a time, with its source attached. Before saving from FTM's Web Search, identify which tree the open page will change. Kenney reported that saving on the embedded FamilySearch page wrote to FamilySearch; she still had to merge or enter the information to bring it into her FTM file [S11 @2026-11-19]. Reopen the FamilySearch person and the local FTM person separately to verify each intended change.
6. Keep the downloaded file on the user's own device.

## 3. List everyone the file ties to a place

The Places workspace lists the people associated with a selected location; the descriptions available are MacKiev's for FTM 2017 and a reviewer's for FTM 2009 [S14 @2026-11-16], [S15 @2026-11-16]. The list comes from the places entered in facts, so it shows whom the file ties to the place, not who lived there.

1. Standardize first. FTM checks place names against a database of more than 3 million places and marks an unrecognized name, such as a misspelling or a name missing its county, with a question mark in the Places workspace. Run Resolve All Place Names from the Tools menu, or resolve each flagged name. MacKiev files this article under FTM 2014 and older. [S7 @2026-11-16]
2. Select the county, then check each unresolved variant and each town entry in the county as a separate place. In FTM 2024 the Place Usage Report can sort locations by country, state, county and city, which puts a county's entries together. [S8 @2026-11-16]
3. Use the people found as a worklist for the locality: each is someone the file ties to the place by a fact already entered. Record an empty list as no fact in this file naming the place, not as a negative finding.

## 4. Search Ancestry and FamilySearch from Web Search

Web Search starts from what the file already says about a person, and its hits are candidates. Run it only for people known to be deceased. Treat anyone who may be living as living and do not search for them: the Living people rule in `SKILL.md` applies.

1. Ancestry: select the person and open Web Search. FTM fills the search fields from the person's data; remove guessed dates and mark only certain terms Exact before searching. Anyone can see the result list, but records and images need an Ancestry subscription. MacKiev's article covers FTM 2017 for Windows. [S16 @2026-11-16]
2. FamilySearch: after signing in to FamilySearch from FTM, choose FamilySearch.org under Search Locations and enter the person's details. MacKiev's FTM 2017 and 2019 article describes this as a search of the FamilySearch Family Tree, so a hit is another user's profile, not a historical record [S17 @2026-11-16]. FamilySearch historical record hints start once the person is matched (§2) [S18 @2026-11-16].
3. Compare each candidate with what the file already proves before merging, and settle identity with evidence/proof judgment.
4. In the Web Merge Wizard, decide each fact: keep one as preferred, keep the other as an alternate, or discard it. For each family member, ignore the person, add them as new or merge them with an existing person. When you discard a fact, keep its source with the Keep sources box. MacKiev's article covers FTM 2017 for Windows. [S19 @2026-11-16]

## 5. Roll back with Turn Back Time only when later work can go

FTM 2024 keeps the last 5,000 actions, including merges, in its Turn Back Time history, up from 1,000 in FTM 2019, and the history survives closing and reopening the tree [S6 @2026-11-16], [S8 @2026-11-16]. As excerpted (a partial read), Crume's interview presents this as a way to correct one change made up to 5,000 changes ago [S1 @2026-11-16]. That is not what it does. Rolling back returns the tree to its state before the selected action and deletes every later change [S6 @2026-11-16].

- To fix one old mistake, correct it by hand.
- Roll back only when the selected action, such as a bad merge or sync, did more harm than everything done since. A sync or another multi-change action carries an information icon that lists every item it changed; view or print that list first, and tick Backup your tree before rolling back. [S6 @2026-11-16]
- MacKiev's page does not say what a rollback does to the linked Ancestry tree; inspect the Ancestry tree before the next sync. [S6 @2026-11-16]
- Before any merge or sync, make the manual backup with media from §1. [S10 @2026-11-16]

## 6. Collect relatives' corrections through Connect

In FTM 2024 the Connect workspace shares the tree through TreeVault cloud services and needs a TreeVault subscription or free trial; invited relatives view the tree in the free Family Tree Maker Connect app on Apple and Android phones and tablets [S20 @2026-11-16], [S8 @2026-11-16]. Guests can open, view and comment on the tree, keep viewing it offline once opened, and see the owner's changes in real time when online [S21 @2026-11-16].

1. **Privacy gate:** <!-- privacy-gate: upload --> Sharing puts the tree in TreeVault and in front of every guest. Answer the privacy gate in `SKILL.md` first. MacKiev's FTM 2024 feature list says guests see relationships, person notes, research notes and web links [S8 @2026-11-16]; first remove research notes about DNA, parentage, health or other sensitive findings. The MacKiev pages read here do not say whether guests see living people, so treat every person in the shared tree as visible to every guest until you inspect the setting and record what you saw. A guest who has opened the tree can keep viewing it offline [S21 @2026-11-16], so a later settings change may not reach that copy.
2. **Privacy gate:** <!-- privacy-gate: contact --> An invitation contacts a living person. Answer the privacy gate in `SKILL.md` and apply the consent and disclosure rules and log of [DNA match outreach staging](dna-match-outreach-staging.md), skipping its DNA-only parts. The Connect workspace takes guests from people in the tree, from the computer's contacts or from typed email addresses, and sends a default or personalized email invitation [S20 @2026-11-16], [S22 @2026-11-16]. Add only the relatives the user names, with addresses the user already has. Do not import the address book and do not look up anyone's email address: the Living people rule applies.
3. A guest's Relative Hint sticky note appears in the tree as soon as it is added [S8 @2026-11-16]. Review the notes on the Get Hints tab, which can turn a note into a fact or a permanent note [S20 @2026-11-16]. Before you convert one, record it as that relative's statement: who said it, when, and whether they saw the event. Then look for a record, and weigh the statement with [family interviews and oral tradition](family-interviews-and-oral-tradition.md).

## 7. View your own tree in FTM Connect

According to the episode transcript (partial read), Andrew Koch suggests consulting the tree on a phone or tablet when away from the desktop [S23†], [S24].

In FTM 2024, use a TreeVault trial or subscription to maintain the Antenna Tree and the Family Tree Maker Connect mobile app to view it [S25 @2026-11-18], [S26 @2026-11-18]. Leave the desktop Connect workspace's guest invitations for §6.

**Privacy gate:** <!-- privacy-gate: upload --> The Source tree's data and later edits go to Software MacKiev's TreeVault, including data about people who may be living [S27 @2026-11-18]. Identify the people, facts, notes and any media the upload would include. Answer the privacy gate in `SKILL.md` before accepting any prompt to create an Antenna Tree.

Reuse the Antenna Tree if it already belongs to the Source tree you need. If the account has an Antenna Tree for a different Source tree, stop before replacing it. If there is none, open the intended Source tree and choose **Create Antenna Tree** from the TreeVault menu. Wait for the upload to finish [S27 @2026-11-18].

Before leaving the desktop, sign in to FTM Connect on the phone or tablet with the owner's TreeVault account and verify that the expected tree opens [S25 @2026-11-18], [S28 @2026-11-18].

## Return packet

- Ancestry: for each citation in the research question, whether its image is local or a gap naming the database; the backup file name; the privacy-gate answers for the sync.
- FamilySearch: the branch file name, download date, home person and generations; a difference log by FamilySearch Person ID; each FamilySearch edit with its person ID, attached source and gate answers.
- Places: the place entries and variants checked, and the resulting worklist.
- Web Search: each candidate with its decision and the evidence used.
- Turn Back Time: any rollback, the action rolled back and the backup file name.
- Connect: the guests invited, the gate answers, and each relative's note logged as a statement with its follow-up record search.
- For mobile reference, record which Antenna Tree opened on the device and the privacy-gate answers for any upload.
