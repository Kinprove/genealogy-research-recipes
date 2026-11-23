---
id: "german-local-census-registration-recovery"
title: "Recover German local census lists and residential-registration entries"
summary: "Recover German nominal census lists, residential-registration entries and related settlement or trade-permission files."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "GERMAN-LOCAL-CENSUS-REGISTRATION-RECOVERY-01", "text": "\"No census here\" ends that route only. Follow it with the other headings and the next archive."}]
handoff: ["german-emigrant-origin-sources"]
checked: "2026-11-06"
checked_basis: "checked 2026-11-06"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": ["request"], "contact": []}
router: {"section": "Records by country and region", "group": "Germany", "order": 115}
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

- Checking parent and child jurisdictions in the FamilySearch Catalog: [FamilySearch holdings audit](familysearch-practical-record-workflows.md) (§ 2).
- Getting from U.S. arrival records to a German origin locality: [German emigrant origin sources](german-emigrant-origin-sources.md).
- Retrieving records from Polish archives: [Polish original-record recovery](polish-index-original-record-recovery.md).
- Identity and birthplace rulings: [evidence/proof judgment](evidence-proof-judgment.md).

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
- **Limits:** Indexes are very rare. The presenter knows only of a partial index for the 1852 Hanover census. Images exist on microfilm and online only patchily, with no system to their availability. [S1] Indexes do exist for Schleswig, Holstein, Lauenburg and Mecklenburg-Schwerin; see step 3 of "Write locally, in order". [S9] For 1875, distinguish the individual enumeration slip from a blank form or an aggregate table. The lecturer reports that he had not seen a completed original slip. Check which layer survives for the town [S2].

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
- Search the catalogue under the equivalent headings above, then record which headings and places produced nominal pages. A search confined to «census» missed items catalogued under other descriptions in the presenter’s FamilySearch survey [S1].

Check older finding aids and filmed material when staff report no census. In one search a loose sheet led the archive director to a microfiche cabinet holding the records [S1]. Record the heading and format checked, including any unavailable guide.

**Hamburg alien registrations (1868–1889).** Include arrivals from other German states when tracing people who came to Hamburg to live or work. Here *Fremde* (“alien”) refers to people who lacked Hamburg citizenship [S13] [S16].

Search MyHeritage’s *Germany, Hamburg Alien Registrations, 1868-1889* by the registrant’s name [S14 @2026-11-22]. Record the indexed birth date and place, the registration date and place, and the occupation when shown [S13 @2026-11-22] [S14 @2026-11-22]. Use each hit as a lead to the protocol entry.

Search the Staatsarchiv Hamburg’s alphabetical registers for the *Fremdenmeldeprotokolle* in **332-8 Meldewesen**, even if MyHeritage has no match [S15 @2026-11-22]. Use A 5 and the surname’s letter range for men, and A 6 for women. Copy the number pair after the birthplace. It usually gives the volume first and the page second. Check the reverse order if the first reading fails. For men’s protocols, record the separate microfilm order reference from the archive catalogue [S15 @2026-11-22]. Use the volume and page to check the protocol entry.

## Write locally, in order

1. **Privacy gate:** <!-- privacy-gate: request --> Registration entries can name people who may still be living; answer the privacy gate in `SKILL.md` before writing for them. **Town or city first.** Find the official municipal website (the presenter's pattern is the town name under .de). Use the municipal site, not Wikipedia. Write to the Stadtarchiv. For registration entries, write to the Einwohnermeldeamt or the Stadtarchiv. [S3]
2. **Then the county archive.** [S2]
3. **Then the regional or state archive, for two kinds of holdings.** Ask for census series that reached it through government channels, and for local holdings sent up when local archives ran out of space or were renovating. [S1], [S3] Lower Saxony's regional archives are the presenter's examples: Oldenburg holds boxes of town lists, and the archive at Bückeburg holds Schaumburg's heads-of-household lists for 1836–67. [S1] Similarly, the Landesarchiv Schleswig-Holstein (Abt. 412) holds the count lists of 1803 for Schleswig and Holstein, of 1860 for Holstein and of 1864 for Holstein and Lauenburg. [S8] They arrived with the Rentekammer records, from the Danish Finance Ministry's statistical office, and probably from the Holstein ducal government's files. Abt. 412 also holds the 1845 lists for a few parishes of the Karrharde. The lists of 1835, 1840, 1845 and 1855 for both duchies, and of 1860 for Schleswig, are in the Rigsarkivet in Copenhagen; the Landesarchiv has them on microfilm (Abt. 415). [S8] Before you write, search the free Arbeitskreis Volkszahl-Register database (akvz.de), which covers censuses up to 1864 for Schleswig, Holstein, Lauenburg and Mecklenburg-Schwerin [S9], and the Danish Demographic Database (Dansk Demografisk Database). Check each hit against the census image.
4. **Towns now in Poland or France: write to the archive now responsible for the town.** The Polish archives hold millions of German-language documents created in places now in Poland. [S2] The presenter attributes this to an international agreement that records return to the town where they were created. Do not rely on that as a universal rule. Some German-era civil registers from the former eastern territories are still held in Germany, for example at Standesamt I in Berlin. [S1]

**For step 3's Danish database:** Rigsarkivet says the Danish Demographic Database (ddd.dda.dk) is being phased out, that all its data moves to Search the Collections (Søg i Samlingerne), whose interface is in Danish, and that it expects most datasets there by 1 September 2026 [S10 @2026-11-13]. It also warns that a dataset may not yet be in Search the Collections, and that ddd.dda.dk searches can take a very long time or fail to return results [S10 @2026-11-13]. Search there first. Record a NIL only for a completed search of a dataset you have confirmed is there; if the census year is not yet there and ddd.dda.dk fails, log an interrupted search, not a NIL, and search again later.

**For Mecklenburg-Schwerin after 1864, look for the census images on FamilySearch.** A FamilySearch post of May 2012 lists three censuses online, for 1867, 1890 and 1900, with a searchable index for 1890 and 1900 and none then for 1867, which had to be browsed by town [S11]. That post is not a statement of present coverage; check each collection as it is now.

In each letter:

- Name the family and, where known, a census year for that state. [S2]
- Ask about census and registration records in the same request. [S3]
- Ask for copies of the actual enumeration or registration pages. [S2]
- State in writing that you will pay the standard fees. Government archives have fee schedules. [S1], [S3] Ask for the archive’s fee schedule or an estimate for your own request, recording the charge separately from the number of pages [S3].

**Privacy gate:** <!-- privacy-gate: request --> A request for younger registration records sends the user's proof of kinship or ID copy and concerns people who may be living; answer the privacy gate in `SKILL.md` first.

**Privacy restriction:** Establish which office holds the registration records and which law or access rules it applies. Report the date range, transfer and release conditions for that place. For records still inside the protection period, enclose with your first request the proof that law or the archive’s rules require, such as evidence of kinship where requested [S4]. The lecturer reports that one town had not kept its registration records [S3]. Distinguish a retention gap from a refusal to release an existing file.

**Privacy gate:** <!-- privacy-gate: request --> A district registration card names the person's partner, children and parents, who may be living; answer the privacy gate in `SKILL.md` before requesting it.

**District registration cards (former GDR, 20th century):** If the person’s last residence was in the former GDR, ask the responsible county archive (Kreisarchiv) for the person's card in the GDR-era district registration file (*Kreismeldekartei*). Dahme-Spreewald describes cards for the former districts of Königs Wusterhausen, Luckau and Lübben, approximately 1949–1990, filed alphabetically. The police also kept address-based indexes [S12 @2026-11-19]. Ask about the person’s district and year. Compare the card’s birthplace, birth date and any relatives it names with the corresponding civil registers. One district released only names and birth dates for a card that the researcher expected to include family members [S4 @2026-11-19]. If a request is restricted, ask which rule applies and which fields can be supplied.

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

A state archive’s reply that it holds only counts describes its own holdings. Nominal pages can be filed locally under another heading [S1]. Log statistical totals separately from lists naming people, then check the municipal holdings and their catalogue descriptions [S2]. "No census here" ends that route only. Follow it with the other headings and the next archive.

## Read registration place roles separately

A registration entry can record the birthplace, the previous residence if different, and the next destination in separate columns. A registration sheet gave the father, mother and child three different birthplaces [S3]. For each person, transcribe these three place roles as separate fields. Never collapse them into a single "origin".

When a destination record names an origin town and searches of baptism, confirmation, marriage and civil records there all fail, check whether that town was the last residence rather than the birthplace:

1. Search that town's newcomer and departure registers for the person.
2. Read the "came from" place.
3. Search church and civil records in that place.

A St. Louis marriage named Speyer, where searches of three churches and the civil records failed. The reported 1839 newcomer entry in Speyer named Rohrbach as the previous residence, and a subsequent search found the birth there [S3]. Use the arrival entry to choose the next locality and the birth entry to establish birthplace.

**Follow a departure entry forward.** When a registration entry records a departure to a named place (*abgemeldet nach X*), search that place's records. Also check its local or district address book (*Adressbuch*) for the following years yourself, even when the archives there report no entries. A 1947 deregistration from Hannover named Haste. After three local archives and the state archive reported no further trace, the 1950 *Grafschaft Schaumburg* address book listed the name in Haste [S5]. An address-book line places the named person there in that edition's year. A gap between surviving editions is a coverage gap; it establishes no move or death interval.

An inferred birthplace stays a hypothesis until a church or civil entry in that place confirms it. Route the identity ruling to the proof recipe.

## Follow a settlement or residential entry into its associated file

### A Bavarian settlement or marriage-permission lead

When marriage and parish records leave an origin unresolved, search the responsible court’s finder for settlement or marriage permission. The Landshut lecture describes an *Ansässigmachung* file with personal papers in its discussion of Bavarian patrimonial administration in 1808–1848 [S6]. Confirm which court held jurisdiction over the settlement on the relevant date.

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

Transcribe the occupation and dates from the *Meldebogen*. In the Augsburg lecture, the *Gewerbekartei* added a trade missing from the residential sheet and supplied a route into a separate *Gewerbeamt* permission file [S7]. Search for the card, then for the permission to practise that trade.

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
   does not establish municipal employment. Check the town’s staff records for the independently documented post [S7].

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

Name the next archive or heading for any route still open. Log searches using [research documentation](research-documentation.md).
