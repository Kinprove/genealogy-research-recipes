---
id: "french-belgian-civil-act-extraction"
title: "Extract French and Belgian civil acts field by field"
summary: "Extract French or Belgian civil acts field by field, follow marginal notes and copies, and use Paris reconstructions for lost originals."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "FRENCH-BELGIAN-CIVIL-ACT-EXTRACTION-01", "text": "Store two fields: the act date, and the event date as stated (literal) or as resolved. Never fill only one date field."}]
handoff: ["french-departmental-record-routing"]
checked: "2026-11-04"
checked_basis: "opened 2026-11-04"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": ["third-party-tool"], "contact": []}
router: {"section": "Records by country and region", "group": "Western and Northern Europe", "order": 145}
---

# Extract French and Belgian civil acts field by field

Use this when you have the image of a French-language birth, marriage or death act from France or Belgium and need its fields: the act date, the event date, declarants, life-status words, clerk corrections, statements about a parent's death, and children legitimated by the marriage. The output is a field table and a list of acts to retrieve next. It does not rule on identity or proof. For status words read as a statement on one date, see [evidence/proof judgment](evidence-proof-judgment.md). For AI transcription limits and keeping a date's type separate from the event, see [AI for documentary records](ai-for-documentary-records.md).

Work from the original image. A yearly index or a ten-year table (*table décennale*, available for Belgian civil registers in the FamilySearch catalog) is only a way to find the act. Marriage acts hold leads that an index leaves out. [S1], [S2] For when French registers and tables begin and where they are kept, see [French departmental record routing, step 1](french-departmental-record-routing.md#1-route-by-département-not-by-a-national-index).

## Contents

- Find civil acts through MyHeritage indexes
- Find Belgian register images in AGATHA
- Check a Paris reconstructed-record branch
- Anchor every act on its own date
- Extract declarants and family details
- Convert Republican dates with a tool, never by arithmetic
- Apply *je dis* corrections
- Read status words as limits at the act date
- Classify every statement about a parent's death
- Read a marriage to the end for legitimated children
- Check marginal continuations and separate copies
- Follow French death registers and later transcriptions
- Output

## Find civil acts through MyHeritage indexes

**Privacy gate:** <!-- privacy-gate: third-party-tool --> The subject’s name and any event date and locality entered in the search go to MyHeritage.

After clearing the gate, search the matching MyHeritage collection using the subject’s name and only the event date and locality needed to find the act.

For Val-de-Marne, use the **Civil Births** index for 1792–1900 and the **Civil Deaths** index for 1792–1937 [S14 @2026-11-20], [S16 @2026-11-20]. Open the associated image where available. The death collection’s coverage varies by commune [S17 @2026-11-20]. When either index misses, check the commune and year in the departmental tables and registers [S22 @2026-11-20].

When the French commune is uncertain, use **France, Church Burials and Civil Deaths** or **France, Church Marriages and Civil Marriages** as a locality lead [S42 @2026-11-22], [S43 @2026-11-22], [S44 @2026-11-22]. Read the heading and text of the image to distinguish a civil act from a burial, church marriage or banns entry. Record the actual type and use any stated commune as a lead to an applicable civil register.

For Belgium, use **Civil Birth Registers** for 1800–1925, **Civil Marriage Registers** for 1800–1938 and **Civil Death Registers** for 1800–1950 [S15 @2026-11-20], [S18 @2026-11-20]. Apply the end year for each act type. Use any registration place, date or act number in the hit to locate the register entry. If the index misses, check the commune’s own tables and available images in AGATHA [S19 @2026-11-20].

If the national index misses and the province is known, try the corresponding **Civil Registration of Births** collection for Antwerp, East Flanders, Hainaut, Liège, Limburg or Namur [S28 @2026-11-22], [S29 @2026-11-22], [S30 @2026-11-22], [S31 @2026-11-22]. For deaths, look for **Civil Registration of Deaths** under Antwerp, Brabant, East Flanders, Hainaut, Liège, Limburg or Namur [S28 @2026-11-22], [S29 @2026-11-22], [S32 @2026-11-22]. For Limburg deaths, check the target year against the collection description and check the commune’s own registers before ruling the year out [S35 @2026-11-22].

For a Liège or Hainaut birth-index hit, read the image to determine whether the date and place refer to a birth or a baptism. Record each event separately as stated and leave the birth fields open if the entry gives only a baptism [S28 @2026-11-22], [S29 @2026-11-22], [S33 @2026-11-22], [S34 @2026-11-22].

For Aalst and its villages, also check **Belgium, Aalst Births** or **Belgium, Aalst Deaths** [S36 @2026-11-22], [S37 @2026-11-22], [S38 @2026-11-22], [S39 @2026-11-22]. When the lead names Baardegem, Erembodegem, Gijzegem, Herdersem, Hofstade, Meldert, Moorsel or Nieuwerkerken, retain that locality for the register lookup [S36 @2026-11-22], [S38 @2026-11-22].

## Find Belgian register images in AGATHA

For Belgian events around the start of civil registration, browse the commune’s earliest civil volume [S26], [S27]. The registers generally begin in 1796–1797 [S19]. France decreed annexation in 1795 and extended its civil-registration rules to the annexed departments in 1796 [S27]. Check the corresponding parish books for earlier events or gaps in the civil series [S19]. Some parish books contain the first civil acts because the 1796 order kept those books in use until 22 September 1796 [S27].

- Search Belgian parish and civil registers in the State Archives' AGATHA (agatha.arch.be). It replaced the old SEARCH site (search.arch.be), which was shut down on 23 December 2024. Links and guides that point to search.arch.be no longer reach the registers. A SEARCH account also works on AGATHA. [S5]
- Create an AGATHA account from its homepage before opening register images. [S5]
- A person hit in AGATHA is a pointer. Open the register image and extract the act from it.
- Search the locality under its French, Dutch and German forms. Belgian place names have several official forms, and an index may use only one.
- For a large city such as Antwerp or Brussels, also check the city archives before closing a population or migration search.

A Belgian act younger than its public term is not open to everyone. The Archives de la Ville de Bruxelles say that from 1 January 2025, for genealogical, historical or scientific research, birth acts are public after 100 years and marriage and death acts after 75 years; an act exactly 75 or 100 years old is not yet public, and the ten-year tables follow the same terms [S7]. That page dates the change to the law of 13 September 2023 and its royal decree of 11 November 2024 [S7]. The State Archives' page for genealogists still gave 50 years for death acts when it was read on 2026-11-13 [S8], so do not take a death act between 50 and 75 years old as open on the strength of that page.

## Check a Paris reconstructed-record branch

The Archives de Paris say the Paris civil registers before 1860 were destroyed in May 1871, and only about a third of the 8 million lost acts were restored. [S6] For a Paris event before 1860, or when the original series is otherwise unavailable, [S3] identifies a
separate *état civil reconstitué* and its *fichiers*. Check the actual collection
description and coverage, then use an applicable reconstruction-file name/date lead
to locate the reconstructed act. Searching the ordinary register series does not
search this separately created corpus.

Read and cite that act as a reconstruction. Preserve any stated reconstruction
date and basis separately from the event date; a named parish register, notarial act
or family paper remains an uninspected source until retrieved. Record the
reconstruction ranges actually checked. A miss there does not show that the event
did not occur or that no other reconstruction survives.

## Anchor every act on its own date

1. Record the act's opening date first, as its own field. In birth and death acts this is the date the act was recorded, not the date of the event. [S1]
2. Resolve relative expressions against that act date: *aujourd'hui* (today), *hier* (yesterday), "the Nth of this month", or a late declaration that gives a day and says "N years ago". Store two fields: the act date, and the event date as stated (literal) or as resolved. Never fill only one date field. [S1]
3. In a marriage act, the opening date is the marriage date. The spouses' birth extracts were handed to the officer, who worked out each spouse's age from them. These ages contain errors. Treat the age as derived, and keep any mismatch with the birth act visible instead of correcting it. [S1]
4. Transcribe a year written in words before normalising it. A clerk’s *quatre-vingt-onze* contributes 91 to the year, so look for the preceding thousands and hundreds in the same date [S2].

## Extract declarants and family details

In a French birth act, copy the child’s name and birthplace and each parent’s name as written, including the mother’s birth surname and either parent’s stated age [S14], [S22]. Identify the declarant from the opening formula and keep that role separate from parentage. The 1803 text of Code civil article 56 allowed a birth attendant such as a midwife to declare in the father’s absence and provided for the person who hosted an out-of-home delivery to declare it [S20].

In a French death act, record the deceased’s name, stated birth date and place, and any named parents or spouse [S14]. Capture each declarant’s role and any explicit degree of kinship. The 1918 text of Code civil article 78 allowed neighbors and other nonrelatives to declare a death. Leave a declarant’s kinship open if the act gives none [S21].

On the French death-act image, look for stated marital status, any date or place given for a spouse’s death, and each parent’s life status. Keep the deceased’s domicile separate from the place of death. Copy the declarants’ stated ages, occupations and domiciles, and record the civil officer separately [S21], [S41], [S42], [S45].

When coworkers declare a widower’s death, record his stated marital status and each declarant’s role separately, and require explicit evidence for any shared household or partnership [S21], [S40].

On a French marriage-act image, record each spouse’s birth date and place. Read the witness clause and attach each stated relationship to the spouse it names. Classify any reported parental death under the parental death rules below [S42], [S45].

In a Belgian birth act, record the child’s name and keep the place of birth separate from the place of registration. Copy each parent’s name, residence and any stated birth date. For a death, capture the deceased’s birth and death places and dates, marital status and any named parents or spouse. For a marriage, capture the place and date of marriage, both spouses’ names and birth details, and their parents’ names. Leave fields open where the act is silent [S15], [S19].

On an Aalst birth-act image, copy each parent’s stated birthplace and occupation alongside the residence. Keep the declarant, witnesses and registrar in their stated roles [S19], [S37], [S38]. On an Aalst death-act image, record the deceased’s residence separately from the place of death and distinguish the witnesses from the registrar [S19], [S36].

## Convert Republican dates with a tool, never by arithmetic

1. Copy the day, month and Republican year exactly. Enter them in the Fondation Napoléon converter or look up the matching row and month column in the Gard archives’ concordance. Record which table or tool you used [S9], [S10]. The concordance gives 7 May 1803 for 17 Floréal an XI and 29 July 1801 for 10 Thermidor an IX [S9].
2. Many registers are filed by Republican year. To browse them, convert the Gregorian target date into a Republican year first. Later marriage acts can still give a spouse's birth in Republican form, so you will need the converter for acts written after 1805 as well. [S2]
3. If the handwriting could read *Brumaire* or *Frimaire*, compare the surrounding dated acts. The two names indicate consecutive months. Convert both readings and leave the date unresolved if the sequence supports either [S2], [S9].
4. France dated the Republican era from 22 September 1792, decreed the calendar in October 1793 and returned to Gregorian dates on 1 January 1806 [S10]. A Nieuwerkerken local-history guide dates its introduction in Belgian civil registers to 17 June 1796 and general compulsory use to 3 April 1798 [S11]. Check the calendar actually used by the commune and clerk.

## Apply *je dis* corrections

When the clerk writes *je dis* to correct an earlier word or date, transcribe both in sequence. Enter the clerk’s replacement in the field and mark the first reading as superseded. Verify that the correction applies to that field before carrying it into the timeline [S1].

## Read status words as limits at the act date

- *veuf / veuve de* (widower / widow of): the named spouse died before the act date. The presenter says a widower clause in a marriage may give the first spouse's death date and place. If it does, add that as a death-act lead. [S1]
- *époux / épouse de* (husband / wife of): record the named spouse. Where the wording leaves survival uncertain, check a later appearance or death record [S1].
- *défunt / décédé(e)(s)*: identify the noun or names the adjective modifies. A plural ending can apply to both parents. If it qualifies only one named parent, leave the other parent’s status open. Copy any stated date and commune of death and look for the death act [S1], [S2].
- *présent(e)* parent: the parent was alive and present at the marriage. [S1]

Each of these words limits the date range of an event. None of them is the event's own record. Whether the word is reliable is a question for evidence/proof judgment.

## Classify every statement about a parent's death

For each parent marked as deceased, record the basis of the statement as one of the following:

1. **Dated statement** (a date and usually a commune). Convert the date if it is Republican, then search that commune's death register around that date. [S2]
2. **Undated death.** A statement that a parent had already died sets an upper bound at the act date. Leave the date and commune open unless the act supplies them. Record any search for the death act only if the text describes it [S2].
3. **Witness attestation.** For the procedure in the Avis du Conseil d’État of 4 Thermidor an XIII, distinguish the declaration by the adults marrying from the four witnesses’ sworn certification concerning the unknown place of death or last domicile [S12]. Record what each party actually attested. Hutchison reads a marriage act that dated a mother’s death to roughly 22 years earlier and named the locality whose registers lacked a death entry [S2]. Count back from the attestation as an estimate, log only the locality and registers specified, and keep other places and years open.

## Read a marriage to the end for legitimated children

1. Read past the marriage formula for a declaration that the spouses recognise children born before their wedding [S1], [S2]. Under the 1804 version of Code civil article 331, both parents had to recognise the child before or in the marriage act. The article excluded children born of adultery or incest [S13]. Check the law in force for the act’s place and date.
2. Make a separate row for every child in the clause. Copy the sex, name as registered, commune of registration and literal date. Convert any Republican date beside the original and continue reading for additional children [S1], [S2].
3. Look for the birth act in that commune on that date under the **mother's surname**, and check its margin for a legitimation note. Then link it to the **father's surname** the child is expected to use in later records. Keep both forms as linked name variants, not as a merge. Whether the man legitimating the child is the biological father is a separate question. [S1], [S2]

## Check marginal continuations and separate copies

For French acts, [S4] describes margin notes continued on the register's end pages or beside a
neighbouring act. Before treating a margin as complete, inspect those places where available.
Retain each note's locator and establish which person or act it concerns from its wording and
any cross-reference; proximity alone does not assign it to the adjacent act.

Where the local descriptions establish separate municipal and court copies, compare the
available annotations with a separate locator for each copy. Check any stated transfer or
annotation-maintenance dates instead of assuming both copies were updated alike. A missing
note in one copy is not proof of no marriage, divorce or death, nor of an event before a
cutoff. [S4]

For a French birth recorded outside marriage, check the birth margin for a reference to an act of recognition or to a legitimation. Use the note’s date and any commune or act number to retrieve the referenced act. Record what the note does and retain its locator alongside the original wording [S14], [S20], [S22].

## Follow French death registers and later transcriptions

For a death in Val-de-Marne, start with the death register of the commune where the person died. When only the death date is known, inspect entries from that date and the days immediately following [S14], [S22].

When a child was stillborn or died before the birth was registered, search the death table and register in the commune of delivery around the delivery date [S14]. Where the French decree of 4 July 1806 applies, look for *présenté sans vie* and use the parents’ names to identify candidate entries. If the table gives no hit, scan the register itself. That wording alone leaves live birth unresolved [S23].

For a French First World War soldier who died away from home, follow the transcription commune and date in the military death record if given [S24]. Otherwise, check the death registers of the last known domicile for a transcription of the death act or declaratory judgment [S14], [S21], [S25]. Search later register years if the entry is absent in the death year. Some September 1914 deaths appear in the 1918 registers [S25]. Record the death, judgment and transcription dates separately when stated.

## Output

For each act, return a table with these fields:

- commune, register type and image locator
- act date
- event date (literal, converted or resolved, and the converter used)
- names, places and family details stated for the act type
- declarants, in order, with their roles, stated particulars and any stated kinship
- witnesses and civil officer, where stated, with each witness’s stated relationship
- the status limit for each spouse and parent
- *je dis* corrections (kept value / superseded value)
- the basis of each parental death statement

Then add:

- a follow-up list of death and birth acts to retrieve, each with commune and date range
- the legitimated children, each with both surname forms
- unresolved readings, such as a month name you could not settle
