---
id: "german-compensation-file-recovery"
title: "Recover a German compensation file from a Lastenausgleich or Wiedergutmachung index hit"
summary: "Carry a Lastenausgleich or Berlin Wiedergutmachung index hit to the file behind it."
kind: "records"
scope: {"platforms": [], "tasks": ["Carry a Lastenausgleich or Berlin Wiedergutmachung index hit to the file behind it."]}
triggers: ["Carry a Lastenausgleich", "Berlin Wiedergutmachung index hit to the file behind it"]
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "GERMAN-COMPENSATION-FILE-RECOVERY-01", "text": "a hit does not show who filed, which relatives the file names or that the indexed person is yours, and a no-hit does not mean no file mentions a relative."}]
handoff: []
checked: "2026-11-07"
checked_basis: "checked 2026-11-07"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": ["request"], "contact": []}
router: {"tier": "pointer", "group": "German records", "order": 1082}
---

# Recover a German compensation file from a Lastenausgleich or Wiedergutmachung index hit

Use this recipe when a German postwar compensation index returns a name. That means a Lastenausgleich file at the Bundesarchiv's Lastenausgleichsarchiv (LAA, Bayreuth), or a Wiedergutmachungsamt (WGA) case at the Landesarchiv Berlin. Use it before you order the file, before you call the hit "the ancestor's claim", and before you read a no-hit for a relative as meaning no file mentions them. The hit tells you a file exists for one indexed applicant or injured party. It does not tell you who filed the claim, which relatives the file names, or whether the indexed person is yours.

Scope: this recipe covers the Lastenausgleich series reached through invenio and the Berlin WGA case titles. Section 1 also says where BEG compensation files are held, but a BEG hit, like a hit in any other compensation index, needs its own route: do not apply the search syntax or access rules below to it.

For the general rule that an index entry or no-hit is not the file's contents, use [archival image coverage verification](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/archival-image-coverage-verification.md). For the same locator-and-claimant pattern in another country, see [US military pension file recovery](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/us-military-pension-file-recovery.md). For scoping a zero-hit query to what the field covers, use the catalogue's recipe on recovering attested spellings across scripts and OCR and [FamilySearch workflows § 13](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/familysearch-practical-record-workflows.md). Same-name and identity rulings belong in [evidence/proof judgment](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/evidence-proof-judgment.md). Keep the request log in the format of the [research log](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/research-documentation.md).

## Contents

- 1\. Choose the index that fits the file class
- 2\. Record every hit as a row with separate locator fields
- 3\. Keep same-name hits apart until the fields match
- 4\. Separate the indexed person, the applicant and the relatives inside the file
- 5\. Estimate family content from the applicant's role before ordering
- 6\. Order by exact signature and log each access state with dates
- 7\. Route residences and dates to the next records
- Output: hit register

## 1. Choose the index that fits the file class

- **Lastenausgleich (Bundesarchiv, invenio).** This is the route described by participants who order these files regularly [S1]:
  - Under Search, switch from the general search (Allgemeine Suche) to the person search (Personensuche). A participant said the person search shows the archive signature and the Aktenzeichen directly, and in most cases a birth date and birthplace. Enter the surname, the given name and, if known, the birth date. [S1]
  - Under "Eingrenzen", limit the results to the signature groups **ZLA 1, ZLA 2 and ZLA 3**, as a participant gave them. ZLA 1 is the Bestand of positively decided Feststellungsakten (Archivportal-D). Without this limit the person search can return other holdings: one participant's hits were not Lastenausgleich files at all. [S1]
  - A participant said the results are sorted by subject area and then by birth date. The result tree opens one level at a time, so keep clicking until each single entry is showing. [S1]
  - If the direct invenio URL gives an error, start at bundesarchiv.de instead. A participant went through "Finden → Invenio → Suche ohne Anmeldung" [S1]. The current Bundesarchiv site lists invenio under Im Archiv recherchieren → Recherchesysteme → invenio. The Bayreuth instructions specify eID login for remote access to restricted datasets for which the researcher has individual permission. [S8]
- **Place-level Lastenausgleich material.** Use the *general* invenio search, not the person search, for items about the home locality such as a village plan (Ortsplan). A participant ordered one by its exact signature. Record these items as their own rows, separate from the family's personal files. [S1]
- **Berlin Wiedergutmachungsamt.** The former WGA database closed on 1 January 2025, and its old web address no longer belongs to the archive. Its catalogue data have been searchable since 2021 in the Landesarchiv Berlin's findbuch.net and on Archivportal-D. [S7] A participant searches findbuch.net with the prefix `wga` followed by the surname. [S2] A common surname can return hundreds of titles: the participant reported more than 200 for one surname. Record the exact query string. A query with a given name added (`wga` + given name + surname) returned nothing for one researcher. The thread did not treat that as proof that no case existed, so record it as a zero-hit for that query string only. [S2]
- **BEG compensation files (Entschädigungsakten).** A claim under the Federal Compensation Act (BEG) was decided by the compensation office of a Land, and its file is held by that office or by the archive that took over its files. Archivportal-D's Themenportal Wiedergutmachung has a cross-archive file search; its person search opened on 8 May 2025 as a demo with records of 940 people, so a miss there says nothing unless the portal now says the search is complete. [S5] The Bundeszentralkartei (BZK) at the Bezirksregierung Düsseldorf records which compensation office handled each BEG case and its file number. It is filed by birth date, so an enquiry needs the exact date of birth, and it answers only public bodies, people affected by the proceeding and their legal representatives. [S6] In Berlin, the Landesarchiv Berlin took over the closed files of the Entschädigungsbehörde on 1 May 2026; about 860 cases still open stay with that authority. [S7]

## 2. Record every hit as a row with separate locator fields

For each hit, copy these fields exactly and keep each one separate:

- **Index and Bestand.** For example: Lastenausgleichsbehörden – Positiv beschiedene Feststellungsakten nach dem Feststellungsgesetz (FG) und Reparationsschädengesetz (RepG) (ZLA 1). [S1] For WGA titles, record the B Rep. group. In one thread, the same name returned three separate cases, in B Rep. 025-08, B Rep. 025-03 and B Rep. 025-09-26. [S2]
- **Archive signature.** This is the ordering key. [S1]
- **Aktenzeichen or WGA number.** Do not merge it into the signature. In the titles a participant posted, the signature appears as "B Rep. 025-08 : number/year", and a separate WGA number appears in the cross-reference line. [S2]
- **Cross-references.** The posted WGA titles carry a "Verweis" to trustee files in **B Rep. 032**, with a Treuhänder register number. Record it as a second locator to request. [S2]
- **Identifying fields.** Record the birth date, the birthplace or place of origin, and the place of application or residence. A participant said that entries in the positively decided Feststellungsakten show the place of origin and the place of application so that a hit can be checked. [S1] For a WGA title, record the parties (claimant against respondent), the "Geschädigt" (injured party) line and the address. [S2]

The Bestand name describes one series: positively decided files. A participant also received a file for a claim that had been rejected. A missing hit in the positively decided series is therefore not proof that nobody filed a claim. [S1]

## 3. Keep same-name hits apart until the fields match

- Treat each same-name hit as a separate person until the birth date, origin and place of application agree with your person. One participant found a second person with the same name who had also filed a Lastenausgleich claim. That person was born about two decades earlier, in a village about 5 km from the father's home in the same region. [S1]
- In one WGA search, a single name returned three case titles in different B Rep. groups. One was a claim from an address abroad, and another named a last residence in a German city. A participant judged the last one "probably the wrong" person without comparing it field by field. Record a judgement like that as a hypothesis, not a ruling. [S2]
- An age or place mismatch ranks a hit lower. On its own it never removes the hit from the register.

## 4. Separate the indexed person, the applicant and the relatives inside the file

- **The indexed name may not be the applicant.** Heirs can be claimants. If the directly injured person died before 1 April 1952, the people who were his heirs on that date count as the injured persons (§ 229(1) LAG), and the claim to Hauptentschädigung can be inherited and transferred (§ 244 LAG). [S4] A participant added that legal successors could also file, because they were economically affected, and gave 1995 as the cut-off. That deadline is not confirmed. The file in that thread was reported to run until 2014, which the participant read as a claim that may have passed from the original owner to an heir. [S3] Another participant described a claim that a son took over after his father died. It ended in the early 1970s with an award to the surviving children. [S1] Record the applicant as "not yet established" until you have read the file.
- **People mentioned only inside a file are not indexed.** A participant who orders files regularly stated that invenio cannot find people who are named only inside a file. That includes relatives, co-owners, witnesses and people on lists such as a parish population list (Gemeindeseelenliste). If you have the file or can read it, search it for them first: participants found further people, a death date and place, and residences by reading delivered files. For files still under protection periods, that participant asked the archive for a search within the files and reported such searches take many months. [S1] If a relative has no index hit, write "no hit in [recorded query and scope]; in-file search not done", not a negative.
- **The applicant's statements about kin are declarations made for the claim.** One applicant declared no relatives besides his current wife, although the researcher knew of two grandchildren. [S1] Record what the file says as the applicant's statement, and compare it with known kin before you conclude anything.

## 5. Estimate family content from the applicant's role before ordering

Participants reported that content varies from file to file. Many files are mostly about property and assets and say little about people. [S1] Use the applicant's role to set expectations:

- **Heirs or a spouse filing for a missing or dead person, or property owned jointly.** Expect details of relatives. In one 90-page file, two daughters filed for a father listed as missing. They first had to obtain a declaration of death (Todeserklärung) and a certificate of inheritance (Erbschein) to establish their shares. [S1]
- **An owner filing alone.** Expect mainly property. A participant noted that the application form still asks for the applicant's residences at several dates. [S1]
- Depending on the file, participants also reported:
  - asset evidence: insurance policies, house photos and floor plans, valuations, tax assessments, a gift contract;
  - witness statements from tenants;
  - interrogation records of relatives and acquaintances;
  - children and some siblings named;
  - a curriculum vitae. [S1]
- Files reported in the thread ran from about 50 to about 270 pages, with many duplicate pages and blank backs. [S1] A participant who uses WGA files said they run from dozens to several hundred pages and hold much more than the case title, including family history. [S2]
- When the file arrives, list each witness or interviewee with their name, their stated role (for example tenant of the claimed house, niece) and the page. Treat each one as a lead. [S1]

## 6. Order by exact signature and log each access state with dates

- **Privacy gate:** <!-- privacy-gate: request --> A file request asks the archive for postwar files that name applicants, heirs, relatives and witnesses who may still be living. Answer the privacy gate in `SKILL.md` before each request, including requests for B Rep. 032 trustee files.
- **Request by exact signature.** A participant who files requests regularly reported that a commissioned search took months to years. A request for a scan of a stated signature went quickly once the forms were done. [S1] For WGA files, a participant said digitised copies can be ordered for a fee. [S2]
- **LAA forms.** Participants described a user application (Benutzungsantrag) and a declaration accepting costs. [S1] A participant said every file has to be assessed under data-protection law before it can be released, and another participant's dated log calls this step the Zugänglichkeitsprüfung. [S1] The Bundesarchiv's Bayreuth page explains that the pilot aims to reduce time-consuming rights checks. [S8]
- **Pilot procedure.** The Bayreuth page, checked 2026-11-07, describes a pilot procedure for LAA use. Under it, requesters receive three documents: [S8]
  - a questionnaire on the planned use;
  - an explanation of the data-protection rules;
  - a "Besondere Verpflichtungserklärung".

  Requests from public bodies, and requests made with official or court authority such as heir searches, are exempt. [S8] Participants received the forms from late 2025, often years after their first request. As participants described them, the forms ask for a case reference, the signatures, the relationship of each person sought, the questions you want answered, which other Bundesarchiv departments you have asked, and how much you are willing to pay. One participant asked whether the case reference is the number from the archive's first reply. [S1]
- **Legitimate interest.** Under § 14 Abs. 2 BArchG, after the affected person's death their relatives have a right to information or inspection if they show a legitimate interest. This does not apply if the deceased left a different instruction or clearly wished otherwise. [S9] The questionnaire asks you to state that interest. A participant suggested two ways to word it: research into the flight or expulsion and its economic consequences, or tracing further heirs. [S1]
- **Prioritisation from 2026.** The LAA processes requests received from 16 January 2026 in order of urgency, until 31 December 2027. Requesters who do not meet the criteria are asked to apply again from 1 January 2028. [S8] The notice lists no general category for a relative's fate. The closest criterion covers clarifying a person's fate, or rehabilitation, after NS or SED persecution. A participant suggested a "Klärung Verwandtenschicksal" (relative's fate) category [S3]. Do not assume a purely genealogical request qualifies; check the current criteria before applying. [S8]
- **Log every state with its date:**
  - request sent;
  - acknowledgement and reference number;
  - cost query;
  - access-review forms received;
  - forms returned;
  - delivery (download or post);
  - invoice.

  One reported sequence included all of these, with years between some steps. [S1] Several participants reported waits of four to five years, followed by delivery within weeks once the returned forms were processed. [S1] Reported costs differed widely. Do not quote any figure as a fee.
- **Digitised copy in invenio.** If the file shows up in invenio as a digitised copy while your request is still open, note that in the log. One participant in that situation was not given access through it. [S1]
- **Reading room.** The Bayreuth site requires an approved research project and an appointment for reading-room use. [S8] Protection periods (Schutzfristen) apply, and there are forms for shortening them. A participant said that once these forms are done, you view the files or digitised copies in the reading room under your access profile. [S1]

## 7. Route residences and dates to the next records

- Treat postwar addresses from a WGA title or a file as residence leads, not as civil-registration facts. In Berlin, continue in the Einwohnermeldekartei (residents' registration card index). The Landesarchiv Berlin says the index was kept from 1874. The part that survives is the West Berlin index of residents who were in the city after 1945 and had deregistered by 1960, plus a few earlier cards. [S10] For address-book follow-up, use the [city-directory workflow](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/city-directory-observation-workflow.md).
- **Privacy gate:** <!-- privacy-gate: request --> A request for postwar death and marriage entries can concern later spouses and other people who may still be living. Answer the privacy gate in `SKILL.md` before you request any register entry.
- Use a file's postwar residence, later marriages and stated death date and place to choose the Standesamt for the death and marriage entries. One participant found an unknown postwar residence, three later marriages and the death date and place this way. Another wanted the file precisely to learn where to look for a death entry. [S1] Until you have seen the register entry, record the date as "stated in the file".

## Output: hit register

Return one row per hit with these columns:

- index and exact query string;
- Bestand;
- signature;
- Aktenzeichen or WGA number;
- cross-references (B Rep. 032 register number);
- identifying fields;
- status: match candidate, namesake or unresolved. A mismatch lowers the rank of a row but never deletes it.

Add:

- a role note for each file: indexed person, applicant (or "not established"), heirs, and relatives named in the file;
- a list of people with no index hit, each marked "in-file search not requested" or "requested on [date]";
- a dated log of requests and access states;
- residence and death leads, each routed to the Einwohnermeldekartei, address books or the Standesamt.
