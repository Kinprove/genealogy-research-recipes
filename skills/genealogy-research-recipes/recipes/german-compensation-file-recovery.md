---
id: "german-compensation-file-recovery"
title: "Recover a German compensation file from a Lastenausgleich or Wiedergutmachung index hit"
summary: "Carry a Lastenausgleich or Berlin Wiedergutmachung index hit to the file behind it."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "GERMAN-COMPENSATION-FILE-RECOVERY-01", "text": "The hit tells you a file exists for one indexed applicant or injured party. It does not tell you who filed the claim, which relatives the file names, or whether the indexed person is yours."}]
handoff: []
checked: "2026-11-07"
checked_basis: "checked 2026-11-07"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": ["request"], "contact": []}
router: {"section": "Records by country and region", "group": "Germany", "order": 138}
---

# Recover a German compensation file from a Lastenausgleich or Wiedergutmachung index hit

Use this recipe when a German postwar compensation index returns a name. That means a Lastenausgleich file at the Bundesarchiv's Lastenausgleichsarchiv (LAA, Bayreuth), or a Wiedergutmachungsamt (WGA) case at the Landesarchiv Berlin. Use it before you order the file, before you call the hit "the ancestor's claim", and before you read a no-hit for a relative as meaning no file mentions them. The hit tells you a file exists for one indexed applicant or injured party. It does not tell you who filed the claim, which relatives the file names, or whether the indexed person is yours.

Scope: this recipe covers the Lastenausgleich series reached through invenio and the Berlin WGA case titles. Section 1 also says where BEG compensation files are held, but a BEG hit, like a hit in any other compensation index, needs its own route: do not apply the search syntax or access rules below to it.

For the general rule that an index entry or no-hit is not the file's contents, use [archival image coverage verification](archival-image-coverage-verification.md). For the same locator-and-claimant pattern in another country, see [US military pension file recovery](us-military-pension-file-recovery.md). For scoping a zero-hit query to what the field covers, use [corpus-seeded name searches across scripts and OCR](corpus-seeded-name-search.md) and [FamilySearch workflows § 13](familysearch-practical-record-workflows.md). Same-name and identity rulings belong in [evidence/proof judgment](evidence-proof-judgment.md). Keep the request log in the format of the [research log](research-documentation.md).

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

- **Lastenausgleich (Bundesarchiv, invenio).** Participants in one forum thread described this route between 2019 and 2025 [S1 @2026-11-13]:
  - Under Search, switch from the general search (Allgemeine Suche) to the person search (Personensuche). A participant said the person search shows the archive signature and the Aktenzeichen directly, and in most cases a birth date and birthplace. Enter the surname, the given name and, if known, the birth date. [S1]
  - If needed, limit the results under "Eingrenzen" to the signature groups **ZLA 1, ZLA 2 and ZLA 3**, as a participant suggested. [S1] On Archivportal-D, ZLA 1 is the signature of the Bundesarchiv's Bestand of positively decided Feststellungsakten under the Feststellungsgesetz and the Reparationsschädengesetz. [S16 @2026-11-13] A person search returned records from outside Lastenausgleich, with the filters used unknown. Confirm the Bestand of each hit before treating it as a compensation file [S1].
  - A participant said the person-search results are sorted by subject area and then by birth date. Another participant said a result tree opens one level at a time, so keep clicking until each single entry is showing. [S1]
  - If the direct invenio URL gives an error, start at bundesarchiv.de instead. In 2020 a participant suggested the path "Finden → Invenio → Suche ohne Anmeldung", because the direct URL had given errors in some cases [S1]. The Bundesarchiv's Bayreuth page links to invenio ("Zur Recherche in invenio"). The same page specifies eID login for remote access to restricted datasets for which the researcher has individual permission. [S15 @2026-11-13]
- **Place-level Lastenausgleich material.** Search the locality outside the person search for a village plan (Ortsplan). Record the plan on a separate row with its own archive signature and use that signature to order it [S1].
- **Berlin Wiedergutmachungsamt.** The former WGA database closed on 1 January 2025. Its catalogue data have been searchable since 2021 in the Landesarchiv Berlin's findbuch.net and on Archivportal-D. [S7 @2026-11-13] Start with the prefix `wga` and the surname in findbuch.net [S2 @2026-11-13]. If adding a given name produces no matches, return to the surname query and compare the parties and addresses. In the reported search one given name produced no results while another returned several cases under the same surname. Log the exact string and its result [S2].
- **BEG compensation files (Entschädigungsakten).** A claim under the Federal Compensation Act (BEG) was handled by a Land's compensation office (Entschädigungsbehörde), and its file is held by that office or by the archive that took over that office's files. [S6] [S14] Archivportal-D's Themenportal Wiedergutmachung has a cross-archive file search, and its person search is still a demo. [S5 @2026-11-13] Archivportal-D announced that demo on 8 May 2025 with records of 940 people, mostly cards from the Bundeszentralkartei (BZK), so a miss there says nothing unless the portal now says the search is complete. [S14 @2026-11-13] The BZK at the Bezirksregierung Düsseldorf records which compensation office handled each BEG case and its file number. It is filed by birth date, so an enquiry needs the exact date of birth. It gives information only to public bodies, to people affected by the proceeding and their legal representatives, and to foreign authorities under international agreements. [S6 @2026-11-13] In Berlin, the Landesarchiv Berlin took over the files of the Entschädigungsbehörde on 1 May 2026. About 800 cases still open stay with the Entschädigungsbehörde at the Landesamt für Bürger- und Ordnungsangelegenheiten (LABO); request access to those files there. [S13 @2026-11-13]

## 2. Record every hit as a row with separate locator fields

For each hit, copy these fields exactly and keep each one separate:

- **Index and Bestand.** For example: Lastenausgleichsbehörden - Positiv beschiedene Feststellungsakten nach dem Feststellungsgesetz (FG) und Reparationsschädengesetz (RepG), as a participant wrote it [S1]; Archivportal-D lists this Bestand as ZLA 1 [S16]. For WGA titles, record the complete B Rep. group separately for each case, including suffixes such as 025-08, 025-03 and 025-09-26. The same indexed name occurs in all three [S2].
- **Archive signature.** This is the ordering key. [S1]
- **Aktenzeichen or WGA number.** Do not merge it into the signature. In the titles posted in one thread, the signature appears as "B Rep. 025-08 : number/year" or, for a JRSO case, "B Rep. 025-03 : number/JRSO". The WGA number appears on its own line after the cross-reference, as a prefix followed by the case number, for example "81 WGA number/year". [S2]
- **Cross-references.** The posted WGA titles carry a "Verweis" to trustee files in **B Rep. 032**, with a Treuhänder register number. [S2] Record it as a second locator, but request the trustee file only when the WGA file is missing. The Landesarchiv Berlin says that B Rep. 032 keeps copies of the applications and decisions of the WGA proceedings, that the trustee file need not be ordered when the WGA file exists, and that the trustee file holds no further information. [S7]
- **Identifying fields.** Record the birth date, the birthplace or place of origin, and the place of application or residence. A participant said that entries in the positively decided Feststellungsakten show the place of origin and the place of application so that a hit can be checked. [S1] For a WGA title, record the parties (claimant against respondent) and, where the title has them, the "Geschädigt" (injured party) line and an address. [S2]

The ZLA 1 title limits that series to positive decisions [S16]. A researcher received a file for a rejected claim whose proceedings continued until 1979, so a miss in ZLA 1 leaves open whether anyone filed [S1]. Check which other series the archive can search for the decision.

## 3. Keep same-name hits apart until the fields match

- Compare birth date, origin and place of application before linking same-name claimants. Two Galician claimants with the same name were born in 1890 and 1911 in villages only about 5 km apart [S1]. Keep a separate row for each candidate.
- In WGA titles, distinguish a claimant’s address abroad from wording such as «zuletzt wohnhaft» for an earlier residence. A Dutch address and a last residence in Magdeburg appear in separate cases under the same name [S2]. Record the address, its date and role from each file before deciding whether the parties match.
- An age or place mismatch ranks a hit lower. On its own it never removes the hit from the register.

## 4. Separate the indexed person, the applicant and the relatives inside the file

- **Identify the injured person, filer and successors separately.** Under § 229(1) LAG, if the directly injured person died before 1 April 1952, the heirs on that date can count as injured persons. The claim to Hauptentschädigung can pass to heirs under § 244, subject to its listed qualifications [S4], [S12]. Compare the application, succession papers and award for names and dates: a reported claim continued through a son after his father’s death and the award went to the surviving children [S1]. Section 234(4) generally capped applications at 31 December 1995 and three years after entitlement arose, subject to the provisions it names [S11]. A reported file end date of 2014 alone establishes neither the filing date nor a change of applicant [S3].
- **Search inside the file for relatives, co-owners and witnesses.** A person mentioned only in testimony or a Gemeindeseelenliste can be absent from the person index. Record which pages or lists you inspected. For a protected or unavailable file, use the privacy checkpoint in section 6 before submitting a named-person lookup. Log the archive’s reply. Until then distinguish a zero-hit index query from an in-file search [S1].
- **Record kin declarations in their claim context.** An applicant reported only his current wife although the researcher knew of two grandchildren [S1]. Copy the form’s question and the answer, then check the relatives independently.

## 5. Estimate family content from the applicant's role before ordering

Participants reported that content varies from file to file. Many files are mostly about property and assets and say little about people. [S1] Use the applicant's role to set expectations:

- **An heir or spouse filing for a missing or deceased owner, or a jointly owned property.** Look for proof of death, inheritance and the claimants’ shares. Two daughters claiming for a missing father supplied a Todeserklärung and an Erbschein. Use those documents’ dates, issuing courts and reference numbers to trace the declaration of death and the inheritance proceedings [S1].
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
- **Request by exact signature.** Specify whether you need a copy of a known file or a search within unindexed material. A request for an Ortsplan can likewise use its own signature [S1 @2026-11-19]. For WGA copies, check the Landesarchiv’s fee or exemption for the requested files (see below) [S2 @2026-11-19], [S13 @2026-11-19].
- **LAA forms.** Record the Benutzungsantrag, any declaration accepting costs and the date of the access review (Zugänglichkeitsprüfung) as separate steps [S1 @2026-11-19]. The Bundesarchiv describes its pilot as a way to reduce time spent on rights checks [S15 @2026-11-19].
- **Pilot procedure.** The Bayreuth page, checked 2026-11-19, describes a pilot procedure for LAA use. Under it, requesters receive three documents: [S15 @2026-11-19]
  - a questionnaire on the planned use;
  - an explanation of the data-protection rules;
  - a "Besondere Verpflichtungserklärung".

  Requests from public bodies, and requests made with official or court authority such as heir searches, are exempt. [S15 @2026-11-19] Copy the archive’s correspondence reference (Vorgangszeichen) separately from the signatures of the files you seek. Record your relationship to each person, the research questions, prior enquiries to Bundesarchiv departments and the maximum cost you accept. If the reference is unclear, check the archive’s letter [S1 @2026-11-19].
- **Legitimate interest.** Under § 14 Abs. 2 BArchG, after the affected person's death their relatives have a right to information or inspection if they show a legitimate interest. This does not apply if the deceased left a different instruction or clearly wished otherwise. [S9 @2026-11-19] The questionnaire asks you to state that interest. A participant suggested two ways to word it: research into the flight or expulsion and its economic consequences, or tracing further heirs. [S1 @2026-11-19]
- **Check the urgency criteria for a request from 16 January 2026.** Bayreuth’s stated priority period runs through 31 December 2027. If no criterion applies, it asks researchers to apply again from 1 January 2028 [S8 @2026-11-19]. Its FAQ distinguishes a requester personally separated from a missing relative during expulsion from an ancestral search. Clarifying someone’s fate after Nazi or SED persecution is another listed ground. Match the circumstances to the archive’s wording before using the forum suggestion «Klärung Verwandtenschicksal» [S15 @2026-11-19], [S3 @2026-11-19].
- **Log every state with its date:**
  - request sent;
  - acknowledgement and reference number;
  - cost query;
  - access-review forms received;
  - forms returned;
  - delivery (download or post);
  - invoice.

  Distinguish archive processing time from time awaiting the requester’s reply. One log records access-review forms in 2021, their return in 2023 and delivery in 2024 [S1 @2026-11-19]. Use the archive’s own estimate and invoice for the current request.
- **Digitised copy in invenio.** A digitised file appeared while the request was still pending, and the request for online access produced no commitment to complete it [S1 @2026-11-19]. Log the visible copy, the request and the access decision separately. Check what your authorised account can actually open [S15 @2026-11-19].
- **Reading room.** The Bayreuth site requires an approved research project and an appointment for reading-room use. [S15 @2026-11-19] Protection periods (Schutzfristen) apply, and there are forms for shortening them. A participant said that once these forms are done, you view the files or digitised copies in the reading room under your access profile. [S1 @2026-11-19]

**Free copies for relatives in Berlin.** The Landesarchiv Berlin says that relatives of people persecuted by the Nazis, or people they authorise, can have up to ten files a calendar year digitised free of charge for research into the persecution. Besides compensation files, the quota covers files from its other holdings, such as Wiedergutmachung or prison files, when they concern the persecution. Other scans and digital copies can cost fees under the archive's fee schedule. In that case the archive sends a quote in advance. [S13 @2026-11-12]

## 7. Route residences and dates to the next records

- Treat postwar addresses from a WGA title or a file as residence leads, not as civil-registration facts. In Berlin, continue in the Einwohnermeldekartei (residents' registration card index). The Landesarchiv Berlin says the index was kept from 1874. The city's original central index was moved out of Berlin in 1943 and is considered lost. The Landesarchiv holds the West Berlin index, rebuilt after the war from cards kept at police stations: it covers residents who were in the city after 1945 and had deregistered by 1960, and it is incomplete for the years before 1945. A new index of the whole population was begun in 1945; it was located in East Berlin from 1948 and is now kept by the LABO. [S10 @2026-11-13] For address-book follow-up, use the [city-directory workflow](city-directory-observation-workflow.md).
- **Privacy gate:** <!-- privacy-gate: request --> A request for postwar death and marriage entries can concern later spouses and other people who may still be living. Answer the privacy gate in `SKILL.md` before you request any register entry.
- Use a file's postwar residence, later marriages and stated death date and place to choose the Standesamt for the death and marriage entries. One file supplied a previously unknown postwar residence, three later marriages and the death date and place [S1 @2026-11-13]. Record each item’s page and stated source, and verify the event in the register before treating it as confirmed.

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
