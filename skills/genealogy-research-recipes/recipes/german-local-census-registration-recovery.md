---
id: "german-local-census-registration-recovery"
title: "Recover German local census lists and residential-registration entries"
summary: "Recover German nominal census lists (roughly 1816–1916), residential-registration entries and associated settlement or trade-permission files."
kind: "records"
scope: {"platforms": [], "tasks": ["Recover German nominal census lists (roughly 1816–1916), residential-registration entries and associated settlement or trade-permission files."]}
triggers: ["Recover German nominal census lists (roughly 1816–1916)", "residential-registration entries and associated settlement", "trade-permission files"]
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "GERMAN-LOCAL-CENSUS-REGISTRATION-RECOVERY-01", "text": "\"we have no census\" is not proof of absence, statistical tables are not the record, and a stated origin town is not the birthplace. Request associated files separately; a residence occupation does not establish municipal employment."}]
handoff: ["german-emigrant-origin-sources"]
checked: "2026-11-06"
checked_basis: "checked 2026-11-06"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": ["request"], "contact": []}
router: {"tier": "pointer", "group": "German records", "order": 1078}
---

# Recover German local census lists and residential-registration entries

Use this recipe when the research needs a German nominal census list (roughly 1816–1916) or a residential-registration (newcomer/departure) entry for a known or probable town. It also applies when a destination record names a German origin town but that town's church and civil records do not contain the person. The common mistakes are:

- claiming that German nominal censuses rarely survive;
- searching only a "census" heading;
- writing only to a state archive;
- treating "we have no census" as proof of absence;
- accepting statistical tables as the record;
- treating a stated origin town as the birthplace.

This recipe covers locating German local records, keeping place roles separate and following
a supported settlement or residential-registration lead into its associated administrative
file. It does not cover these related tasks, which have their own recipes:

- Checking parent and child jurisdictions in the FamilySearch Catalog: [FamilySearch holdings audit](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/familysearch-practical-record-workflows.md) (§ 2).
- Getting from U.S. arrival records to a German origin locality: [German emigrant origin sources](german-emigrant-origin-sources.md).
- Retrieving records from Polish archives: [Polish original-record recovery](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/polish-index-original-record-recovery.md).
- Identity and birthplace rulings: [evidence/proof judgment](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/evidence-proof-judgment.md).

## Contents

- Do not open with a survival verdict
- Pin the town and county first
- Search the catalogues beyond "census"
- Write locally, in order
- Classify every reply; do not convert it to absence
- Read registration place roles separately
- Follow a settlement or residential entry into its associated file
- Close with a request-and-reply packet

## Do not open with a survival verdict

Do not claim that German nominal census lists are lost or rare.

- **Coverage:** Censuses were taken across the German states throughout 1816–1916. The presenter, who surveyed the topic state by state over several years, found censuses in all 38 states of the period. [S1] Many states counted every three years from 1834 under the customs union (Zollverein), whose population counts set each state's share of customs revenue. [S1] Regular imperial censuses followed in 1871, 1875 and every five years to 1910. [S1] For wartime years, establish the actual local enumeration and surviving list from its catalogue or original form; the prewar cycle alone does not establish wartime coverage.
- **Content:** Heads-only lists and lists naming every inhabitant coexist; no single date separates them. Until about the 1840s most lists name only the head of household, with household members counted by gender, status, occupation or religion. Heads-only series continued much later, though: Mecklenburg-Schwerin took a heads-of-household census every year from 1828 to 1868, and Schaumburg's surviving lists for 1836–67 are heads of household. Meanwhile an 1819 Mecklenburg list already gives every person's full name and birth date. Lists that name every inhabitant may give age, birth date or birthplace. Identify the format from the state, the year and the actual form before reading anything into a missing spouse or child. [S1]
- **Location:** Most surviving lists are in city and town archives: about 85% by the presenter's estimate, about 10% in regional archives, and very few in state or national archives. Start local. [S1], [S2]
- **Limits:** Indexes are very rare. The presenter knows only of a partial index for the 1852 Hanover census. Images exist on microfilm and online only patchily, with no system to their availability. [S1] Indexes do exist for Schleswig, Holstein, Lauenburg and Mecklenburg-Schwerin; see step 3 of "Write locally, in order". [S9] The presenter has never seen a filled-out original of the 1875 individual forms, so do not promise that layer. [S2]

## Pin the town and county first

Establish the town, then its county, using a period gazetteer such as Meyers Orts. Send requests to the lowest administrative level you can reach. [S1], [S2] If you know only a state or region (for example "Hessen" or "the Rhineland"), stop and recover the town before writing. A letter to a state archive that names only the state has close to no chance of success, and such archives refer you to the county. [S2] Use the German emigrant-origin recipe linked above for that step.

## Search the catalogues beyond "census"

In the FamilySearch Catalog and in the local archive's own finding aid (Findbuch), search at county level or lower. [S2] Open the census category, and also search these headings:

- house or housing lists;
- household(-head) lists and lists of inhabitants;
- residential registration;
- voter lists and homeowner-type lists;
- military lists and lists of subjects. [S1], [S2]

In German finding aids, use the German terms. The official word for census is *Volkszählung*. [S1] Useful variants for the headings above include *Häuserliste*, *Haushaltsvorstandsliste* and *Einwohnerliste*. For registration, search the word *Einwohner* in the archive's online Findbuch. [S3]

The "census" heading is not enough, for two reasons:

- House-census forms used in most states between 1840 and 1864 carried a "house list" title and have very often been miscatalogued. [S2]
- A researcher on the presenter's project found about 100 FamilySearch census items by using ten catalogue descriptions. Searching "census" alone would have found a few dozen. [S1]

In archives that had nothing under "census", the same other headings turned up enumerations. On three occasions the presenter showed staff census records they did not know they held. [S1] A missing catalogue category is therefore not a negative result. Record each heading searched and each heading not available.

## Write locally, in order

1. **Privacy gate:** <!-- privacy-gate: request --> Registration entries can name people who may still be living; answer the privacy gate in `SKILL.md` before writing for them. **Town or city first.** Find the official municipal website (the presenter's pattern is the town name under .de). Use the municipal site, not Wikipedia. Write to the Stadtarchiv. For registration entries, write to the Einwohnermeldeamt or the Stadtarchiv. [S3]
2. **Then the county archive.** [S2]
3. **Then the regional or state archive, for two kinds of holdings.** Ask for census series that reached it through government channels, and for local holdings sent up when local archives ran out of space or were renovating. [S1], [S3] Lower Saxony's regional archives are the presenter's examples: Oldenburg holds boxes of town lists, and the archive at Bückeburg holds Schaumburg's heads-of-household lists for 1836–67. [S1] Similarly, the Landesarchiv Schleswig-Holstein (Abt. 412) holds the count lists of 1803 for Schleswig and Holstein, of 1860 for Holstein and of 1864 for Holstein and Lauenburg. [S8] They arrived with the Rentekammer records, from the Danish Finance Ministry's statistical office, and probably from the Holstein ducal government's files. Abt. 412 also holds the 1845 lists for a few parishes of the Karrharde. The lists of 1835, 1840, 1845 and 1855 for both duchies, and of 1860 for Schleswig, are in the Rigsarkivet in Copenhagen; the Landesarchiv has them on microfilm (Abt. 415). [S8] Before you write, search the free Arbeitskreis Volkszahl-Register database (akvz.de), which covers censuses up to 1864 for Schleswig, Holstein, Lauenburg and Mecklenburg-Schwerin [S9], and the Danish Demographic Database (Dansk Demografisk Database). Check each hit against the census image.
4. **Towns now in Poland or France: write to the archive now responsible for the town.** The Polish archives hold millions of German-language documents created in places now in Poland. [S2] The presenter attributes this to an international agreement that records return to the town where they were created. Do not rely on that as a universal rule. Some German-era civil registers from the former eastern territories are still held in Germany, for example at Standesamt I in Berlin. [S1]

In each letter:

- Name the family and, where known, a census year for that state. [S2]
- Ask about census and registration records in the same request. [S3]
- Ask for copies of the actual enumeration or registration pages. [S2]
- State in writing that you will pay the standard fees. Government archives have fee schedules. [S1], [S3] The presenter calls fees usually nominal; one example he gives is about 50 documents for 37 dollars. Do not quote that as a current rate. [S3]

**Privacy gate:** <!-- privacy-gate: request --> A request for younger registration records sends the user's proof of kinship or ID copy and concerns people who may be living; answer the privacy gate in `SKILL.md` first.

**Privacy restriction:** By the presenter's account, registration records are transferred to the city archive after about 100 years and are open there. Younger records are released only if you show descent, for example with a family tree and a death certificate. [S3] The binding protection periods (*Schutzfristen*) and the terms of use by third parties are set by the state's archive law (*Archivgesetz*). [S4] Look up that law for the archive you are writing to. For records still inside the protection period, enclose with your first request the proof that law or the archive's use rules require; requirements differ (some archives asked for proof of kinship, others accepted a copy of an ID). [S4] A true loss can happen: one town told the presenter it had not kept its registration records. [S3]

**Privacy gate:** <!-- privacy-gate: request --> A district registration card names the person's partner, children and parents, who may be living; answer the privacy gate in `SKILL.md` before requesting it.

**District registration cards (former GDR, 20th century):** If the person's last residence was in the former GDR and the family documents were lost, ask the responsible county archive (Kreisarchiv) for the person's card in the GDR-era district registration file (*Kreismeldekartei*). A forum researcher received copies of these cards from several Kreisarchive. They named the partner, children and parents, plus birthplace and birth date, which the researcher had not known before. [S4] Release terms differ by archive: some asked for proof of kinship, some accepted a copy of an ID, and one released only names and birth dates, citing data protection. Another participant's advice: if your request is covered by the state's archive law, ask for the legal basis of a refusal under that law. [S4] Ask each district whether its cards survive before you build a plan on them. Treat each name, date and place on a card as a lead to the matching civil register entry, not as proof.

**Port cities:** For an emigrant who stayed months in a port city before sailing, also try that port city's registration records. [S3]

## Classify every reply; do not convert it to absence

Log each reply as one of the following statuses:

- no holdings claimed;
- statistics only;
- referred elsewhere;
- transferred to a named archive;
- restricted, descent proof required;
- not preserved;
- pages supplied.

State archives told the presenter that their state never had a census, or that they held only the counts. His survey contradicted both answers. [S1] Keep statistical summaries (counts by gender or district) in a separate row from nominal pages, and never cite a summary as an enumeration of the family. [S2] "No census here" ends that route only. Follow it with the other headings and the next archive.

## Read registration place roles separately

A registration entry can record the birthplace, the previous residence if different, and the next destination in separate columns. Some entries show family members born in three different places. [S3] For each person, transcribe these three place roles as separate fields. Never collapse them into a single "origin".

When a destination record names an origin town and searches of baptism, confirmation, marriage and civil records there all fail, check whether that town was the last residence rather than the birthplace:

1. Search that town's newcomer and departure registers for the person.
2. Read the "came from" place.
3. Search church and civil records in that place.

**Worked example (from the presenter):** A St. Louis marriage named Speyer. The three main Speyer churches had no entry, and neither did the civil records there (kept since the 1790s on the left bank of the Rhine; Reich-wide civil registration began only in 1876). An 1839 newcomer entry, filmed by the Genealogical Society of Utah in 1960, showed that he came from Rohrbach. The birth was then found at Rohrbach. [S3]

**Follow a departure entry forward.** When a registration entry records a departure to a named place (*abgemeldet nach X*), search that place's records. Also check its local or district address book (*Adressbuch*) for the following years yourself, even when the archives there report no entries. In one thread, a city archive showed a man deregistering to a village in 1947. Three local archives and the state archive then reported nothing further. A forum participant nevertheless found him in the 1950 district address book covering that village. [S5] An address-book line places the named person there in that edition's year. A gap between surviving editions is a coverage gap; it establishes no move or death interval.

An inferred birthplace stays a hypothesis until a church or civil entry in that place confirms it. Route the identity ruling to the proof recipe.

## Follow a settlement or residential entry into its associated file

### A Bavarian settlement or marriage-permission lead

When local marriage and parish records leave an origin unresolved, check the dated
settlement or permission administration as a separate record family. The Landshut
presentation describes this route in its discussion of patrimonial administration in
1808–1848, using a finder and an *Ansässigmachung* file with personal papers [S6].
That setting is a historical finding lead, not a rule for every Bavarian town or period.

1. Use the supported residence, person and period to identify the responsible settlement
   office in the actual holdings description, including a patrimonial court where the
   description places those records. Do not substitute the parish or modern municipality
   for the creating authority.
2. Inspect its settlement or marriage-permission finder. Preserve the name, any origin
   statement and the actual file reference supplied. Use that entry to identify the
   separate personal file; if the locator is unclear, retain the entry when asking the
   custodian to resolve it. A finder entry is not the file.
3. Retrieve the file and inspect its contents list and surviving enclosures. The source
   illustrates school or trade papers, military discharge, property statements and a
   travel book; these are examples, not a required attachment set [S6]. Record what was
   actually received, including missing or uninspected components.
4. Carry an attributed birthplace, former residence, institution or travel place into
   a dated follow-up search. Keep the place's stated role and the document's informant;
   an attachment or finder statement does not itself settle birthplace or identity.

### An occupation on a residential sheet leads to a trade file

Use the actual occupation wording and dates from an inspected residential sheet as
search keys, rather than treating its occupation list as a complete work history.
The Augsburg presentation follows a *Meldebogen* to a *Gewerbekartei* card naming an
additional trade and then to a separate *Gewerbeamt* permission file [S7].

1. Search the responsible archive's trade-card or trade-registration finder for the
   supported person and period. Compare its identifiers with the residential entry;
   preserve an additional occupation as a separately sourced statement.
2. Use the named trade and dates to select the actual office's surviving permission
   or concession-file descriptions. Follow any reference supplied, but do not invent
   one or assume every occupation required a licence. Verify custody and access for
   that product before requesting it.
3. Inspect the retrieved file's actual documents and dates. Attribute an employer's
   or colleague's assessment to that speaker and document, rather than turning adverse
   testimony into established biography. Keep an application, refusal, appeal and
   permission separate where the file actually records them.
4. **Privacy gate:** <!-- privacy-gate: request --> A municipal personnel file may concern
   a person who may still be living; answer the privacy gate in `SKILL.md` before requesting it.
   Seek a municipal personnel file only when a separate evidenced employment link
   supplies the municipal office or post and period. Use those details to select its
   personnel-file description. Private employment or a residence occupation alone
   does not establish municipal employment. The source's separate personnel-file
   example is not a promise that every resident has one [S7].

Return the linked entry, finder/card and separate file, with each locator, received
extent and attributed place or work statement. Leave unsupported employment links,
missing files and a complete career reconstruction unresolved.

## Close with a request-and-reply packet

Return:

- the gazetteer citation for the town and county;
- the catalogue headings tried (English and German), per catalogue and jurisdiction level;
- the archives contacted, in order, with dates and fee offers;
- the reply-status register;
- the inspected enumeration or registration pages, with archive locators kept separate from film or image locators;
- for each person, the birthplace, previous residence and destination fields, each with its confirmation status.
- where an associated-file route was followed, the referring entry, separate file and
  actual enclosures, with their retrieval status and unresolved links.

Name the next archive or heading for any route still open. Log searches using [research documentation](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/research-documentation.md).
