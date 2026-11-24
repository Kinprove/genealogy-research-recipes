---
id: "scandinavian-patronymic-farm-name-record-recovery"
title: "Recover a Scandinavian emigrant's home-parish entries under patronymic, farm and soldier names"
summary: "Find a Danish, Norwegian, Swedish or Icelandic emigrant's home-parish entries under patronymic, farm and soldier names."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "SCANDINAVIAN-PATRONYMIC-FARM-NAME-RECORD-RECOVERY-01", "text": "The name in the parish register is usually not the American surname. Same-named parishioners are common, so separate them by birth date, parents, spouse, farm and vaccination entries, never by name alone."}]
handoff: ["scandinavian-parish-record-recovery", "danish-church-book-probate-recovery"]
checked: "2026-11-04"
checked_basis: "opened 2026-11-04"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": ["third-party-tool"], "contact": []}
router: {"section": "Records by country and region", "group": "Western and Northern Europe", "order": 166}
---

# Recover a Scandinavian emigrant's home-parish entries under patronymic, farm and soldier names

Use this when a Danish, Norwegian, Swedish or Icelandic emigrant is known from destination records and you need to find that person in the home parish. The main way this goes wrong is searching the American surname in home-country indexes, finding nothing or attaching the wrong same-named person. The name in the parish register is usually not the American surname. Same-named parishioners are common, so separate them by birth date, parents, spouse, farm and vaccination entries, never by name alone.

Covered elsewhere and not repeated here: [same-name elimination](evidence-proof-judgment.md), [searching through an associate (§9)](ancestry-record-search-recovery.md), [classifying name tokens](corpus-seeded-name-search.md), [native spellings and holdings audits (§2)](familysearch-practical-record-workflows.md).

## Contents

- Fix the identity anchors before touching home-country indexes
- Build the expected name forms and log them as a register
- Follow a Swedish soldier name beyond the muster index
- Search the forms, then browse to the known date
- Pivot through co-travellers when the passenger search fails
- Discriminate same-named candidates with a comparison table
- Read a Norwegian bygdebok by farm, then verify it
- Use Norwegian censuses and emigrant protocols within their ranges
- Denmark: go beyond the church books
- Iceland: use the farm, census and emigration sources separately
- Rebuild siblings and marriages from the named parents
- Close with an origin packet

## Fix the identity anchors before touching home-country indexes

From destination records (census, church, naturalization, obituary, passenger list), extract and keep separate:

- the exact birth date
- the town of birth or last residence, and the parish it belonged to
- the father's given name, if any record states it
- co-travellers such as siblings, a future spouse or neighbours

Start with destination records, identify the parish, and then search that parish [S2]. An approximate age is not an anchor. The exact birth date is. Swedish church books, including the household examination books, record the exact birth date, often in its own column, so the date works almost like an identifier for telling same-named people apart [S5].

**Privacy gate:** <!-- privacy-gate: third-party-tool --> The Swedish emigrant’s name and exact birth date go to ArkivDigital.

If destination records give a Swedish emigrant’s exact birth date and leave the parish unknown, search ArkivDigital’s *Population of Sweden* (*Befolkningen i Sverige*, BiS) under **Index Search** by name and birth date, with birthplace blank [S41 @2026-11-21], [S42 @2026-11-21], [S43 @2026-11-21]. If the surname is uncertain, try the given name and exact date alone [S42 @2026-11-21]. Use the birth parish in a strong match as a lead. Keep it separate from the parish of residence and check the original entries against the destination records before linking the person [S41 @2026-11-21], [S43 @2026-11-21].

Treat the American surname as one search form. For a Danish emigrant called Jensen abroad, use the father’s given name in the home parish to derive the patronymic expected at baptism [S2].

## Build the expected name forms and log them as a register

Create one row for each form you expect or observe. Record the literal form, the record it appears in, and its type: patronymic, matronymic, farm/house, soldier byname or adopted.

- **Patronymic.** The father’s given name supplies the stem for a son’s *-son/-sen* or a daughter’s *-dotter/-datter* [S1], [S5]. Search the father’s given-name variants as well as surname spellings. Persson, Pierson and Pettersson can lead to entries for the same person. Confirm each against the parish, dates and family [S1].
- **Matronymic.** A Swedish baptism may identify a child by a name derived from the mother’s given name [S3]. Inspect the parentage and marital-status fields before drawing an inference from the surname.
- **Farm or house name.** Trace the household through a move or marriage. A son-in-law could take the name of his wife’s farm or of her father [S3]. Enter the farm beside each dated record and use the household to test continuity when the name changes [S6].
- **Soldier byname.** Search the regiment and local muster under both civil and soldier names [S8]. John Falk in America was known as Johan Magnus Anderson in Swedish records [S1]. A brother could also adopt a soldier’s byname abroad [S5]. Confirm which man served before using the name to link his family.
- **Adopted American name.** A surname can name an earlier generation’s town. Walter Slangerup adopted the name of his great-grandfather’s Danish town after emigration. His own birth entry had to be sought under a patronymic [S2].

In Swedish household examination books, compare surname forms across generations before using a child's surname stem as a clue to the father's given name [S39], [S40]. A *-son* form that stays the same as the fathers' given names change points to a fixed surname [S40]. When the records support a patronymic, use the stem as a search lead and verify the father in the child's baptism entry.

In your tree, enter the name exactly as it appears in the christening (the first record) as the primary form. Log every farm, soldier or American name as an alternate with its source [S6].

## Follow a Swedish soldier name beyond the muster index

ArkivDigital's April 2026 demonstration distinguishes its general-muster index from other regimental rolls. Starting from a Swedish soldier name and regiment [S18]:

- Browse the regiment's rolls for intervening years as well as the periodic general musters; those separate rolls need not be in the general-muster index.
- If a dismissal note refers the soldier for *underhåll*, use that referral to investigate the Krigsmanshuset archive.
- If the original names a *rusthållare* and records a *krigsmanshusavgift*, investigate the fee documentation for changes of rusthållare. Keep that holder and fee distinct from the soldier and his support history.

Open the roll image even when the index has the soldier’s name. Copy the *underhåll* referral and any *krigsmanshusavgift* beside the named *rusthållare*. The latter points to the holder’s fee history, a different inquiry from the soldier’s support [S18].

## Search the forms, then browse to the known date

If the parish index misses every supported patronymic and farm name, browse the register by the known date. Match the parents, farm and witnesses in the entry before linking an emigrant whose surname later changed [S2].

Write down the parish, register volume and date range you browsed. If you get no hit, report that bounded range, not "not born there."

## Pivot through co-travellers when the passenger search fails

First search the departure registers kept in the home country:

- Denmark: Rigsarkivet says the police registered emigrants' shipping contracts from 1868 to 1959. Most emigrants left from Copenhagen and are in the Copenhagen police registers. From 1934 the State Emigration Office also checked the agents' contracts and received copies, while the Copenhagen police went on keeping the emigrant registers. The police registers it lists run to 1952; from 1941 they list emigrants together with other travellers. For 1953–1959 it lists only the office's copies. The registers from 1934 and the office's copies are not scanned, so a miss in the online material is not a negative for those years. The registers for 1868–1911 are name-searchable on the Danish Emigration Archives' site; that site's own year list runs to 1920, with 1912, 1917 and 1918 missing. [S23 @2026-11-13], [S24 @2026-11-13]
- Norway: search the police emigrant protocols in [Use Norwegian censuses and emigrant protocols within their ranges](#use-norwegian-censuses-and-emigrant-protocols-within-their-ranges).
- Sweden: search the port lists, *Emigranter 1861–1940* and the moving-out registers described in [Swedish household reconstruction](scandinavian-parish-record-recovery.md#before-1869-look-for-emigrants-in-the-moving-out-registers). Emiweb's *Emigranter i svenska kyrkböcker* (formerly Emibas) indexes emigrants from parish registers. It was compiled systematically only for about 1836–1895, and not for Uppsala, Norrbotten or Stockholm counties. It is a subscription database. [S25 @2026-11-13], [S26 @2026-11-13]

Record the register, years and index you searched. A miss is bounded by them.

If you cannot find the emigrant on a passenger list:

1. Browse the ship and year of a known co-traveller. Inspect the entries beside a future spouse or sibling under a father-derived patronymic even if the emigrant later used another surname [S5].
2. Scan past the family group and onto nearby pages. In one Norway Heritage transcription, a possible brother appeared on the parents’ page under the farm name, outside the group, while the daughter appeared later [S7]. Record the vessel, year and pages searched.
3. Verify the relationship against the home-parish baptism for both parents and the dated moving-out entry (*utflyttede*) before sailing [S7].

Follow a person between Norwegian parishes using the moving-out (*utflyttede*) and moving-in (*innflyttede*) sections. Check names, dates and destination against the next parish [S2].

## Discriminate same-named candidates with a comparison table

Same-named people are common in a parish. Families with the same parents' names and the same children's names are also common, so a careless search attaches other families' children [S1], [S4]. Build one row per candidate with these columns:

- exact birth date
- father's name, and mother's name where recorded
- spouse
- farm or house of residence, taken from house censuses and farm records [S4]
- smallpox vaccination date and place, from baptism, confirmation or marriage entries [S2]
- the locator for each entry

Compare any smallpox entry by date, place and wording across the records. An 1843 Norwegian marriage entry and confirmation examples illustrate the extra identifier [S2]. Denmark and Norway’s decree of 3 April 1810 accepted proof of vaccination **or** previous smallpox for marriage from 1 January 1811. For confirmation it directed the priest to encourage vaccination, and its school rule excluded the lowest common schools [S37]. Sweden introduced compulsory vaccination in 1816 [S38]. Check the particular register and period before drawing an inference from a blank column.

Tanner warns that a Norwegian line with no source at the house-census or farm level is very likely wrong in its places, its names or both [S4]. Treat such an inherited tree as unverified until you have tied it to farm-level records, such as the censuses and church records on Digitalarkivet.

A candidate matches only when several of these discriminators agree. Leave any column you could not fill blank, and send the merge-or-separate decision to [evidence/proof judgment](evidence-proof-judgment.md).

## Read a Norwegian bygdebok by farm, then verify it

- A bygdebok, often a *gard og slekt* (farm and family) volume, is a compiled secondary source. It is arranged by gårdsnummer and bruksnummer (farm and holding numbers), and husmannsplasser (cottars' places) are treated in the chapter of the farm they belong to. [S10], [S12] Find the volume for the parish and read it under the farm and its numbers, not by surname.
- Rygh's *Norske Gaardnavne* covers the matrikkel (land-register) farm names. For a plass, search under its parent farm. The same farm name recurs in different parishes; Rygh lists 13 farms called Nyborg. [S11] Fix the parish before you use a farm name as a key.
- Search nb.no (Nettbiblioteket, the National Library's online library) for the volume. If you cannot open the full text, log an access gap, not a miss.
- Check every bygdebok statement against the kirkebøker (church books) and censuses on Digitalarkivet before you use it.

## Use Norwegian censuses and emigrant protocols within their ranges

- The national censuses that name each person are 1801, 1865, 1875, 1891, 1900, 1910 and 1920. [S13], [S15] The 1815, 1825, 1835, 1845 and 1855 censuses were numeric counts. Only some name lists from them survive, in ministers' and town archives, so a gap between 1801 and 1865 is expected. [S13]
- A nil from a census name search is not a negative until you confirm the municipality is transcribed for that year.
- Police emigrant protocols start at different dates in each port. Oslo's begin in 1867. [S14] For any other port, read its start date on Digitalarkivet. For a departure before that range, search the home parish's church book for a moving-out note.
- Treat a link in Historisk befolkningsregister (histreg.no) as a derived hypothesis. Check it against the scanned record.

## Denmark: go beyond the church books

For the church books themselves, civil marriages and probate, use [Danish church books and probate](danish-church-book-probate-recovery.md).

- Rigsarkivet has scanned every census of the kingdom up to 1940 on Arkivalieronline. [S22 @2026-11-16] Its name-search guide lists fully transcribed censuses for 1787, 1801/1803, 1834, 1840, 1845, 1850, 1860, 1880, 1885 (Copenhagen only) and 1901, and describes DDD's coverage as 1787–1930. [S27 @2026-11-16] DDD (Dansk Demografisk Database) is run by Rigsarkivet. [S16 @2026-11-16] Rigsarkivet says DDD is closing as a separate platform and its data is being made searchable in Søg i Samlingerne. [S27 @2026-11-16] Check the actual transcription coverage for the locality and year; a nil in a partly transcribed year is not a negative. Check each transcription against the scan.
- Use the lægdsruller (military levying rolls) to bridge censuses for men. Males of the peasant class were liable in 1788–1848, and all men from 1849. Rigsarkivet gives the registration ages as 0–36 for 1788–1808, 0–45 for 1808–1849, 15–38 from 1849, 19–38 from 1869 and 18–36 from 1912. After 1849 a boy was not entered at birth: look for him in the rolls for the years when his age fell within his period's range. The rolls give the father's name (the mother's if the man was born outside marriage) and the man's moves while liable for service. Moves can be followed across the country from 1789. Before 1788 only scattered rolls survive. [S17 @2026-11-16]

## Iceland: use the farm, census and emigration sources separately

Recover a candidate parent's given name from the genitive form in an Icelandic patronymic or matronymic [S36]. In MyHeritage's example, *Jónsson* gives *Jón* as the father's given-name lead [S35], [S36]. Confirm the relationship in the child's baptism entry before attaching a parent.

Use Vesturfaraskrá as the 1983 printed emigration index for 1870–1914 described by Icelandic Roots, rather than assuming it is a searchable online database. Search its first-name arrangement with the observed patronymic and farm, then compare its year and destination with departure and arrival evidence. The index includes some planned departures that did not happen, so an entry alone does not prove that the person emigrated. [S28], [S29]

An Icelandic farm name is not a unique location. Resolve it through the sýsla (county) and sókn (parish), and carry both into the place register before matching a census household to a church entry. Preserve competing same-named farms until the dated household, parents or neighbouring places distinguish them; a bare farm-name match does not select one. [S28], [S30]

Check Íslendingabók’s access conditions before planning a lookup: its English information page restricts access to Icelandic citizens and legal residents with a kennitala. If that route is unavailable, retain it as unavailable and continue with the cited census and parish records. Treat a compiled family link as a lead to its evidence; no logged-in search or account access was tested for this guidance. [S28 @2026-11-16], [S31 @2026-11-16]

For an Icelandic emigrant, follow a diaspora memorial or serialised settlement history to its issue and page [S28]. For the Narrows, Manitoba, Byerly-Adams cites *Heimskringla*, 19 April 1906, p. 1, and the first instalment of Geirfinnur Peterson’s history in *Lögberg-Heimskringla*, 16 January 1969, p. 4 [S34]. Use those citations to obtain the newspaper pages before relying on the retelling.

### Earlier generations

Choose an Icelandic census by its actual fields. The 1703 census supplies names, ages and household/residence context; the 1762 census names the household head and counts other household members. A wife or child unnamed in that latter return is not thereby absent from the household. Copy the headings and stated relationships before comparing same-named people across years. [S28], [S32]

Check the Icelandic parish’s surviving years before inferring a birth from an early baptism search. FamilySearch’s guide dates record-keeping decrees to 1735 and 1746, identifies the earliest surviving records as 1664, and places most surviving series’ beginnings around 1750–1780. A decree date is not the start of every local book; record the actual parish, event series and earliest inspected year. [S28], [S33]

## Rebuild siblings and marriages from the named parents

- **Sibling sets.** Build these from the parents named in each baptism, not from a shared surname. Around a parish's change to fixed surnames, older children may carry the father's patronymic while younger ones carry a fixed surname [S6]. Brady says adult siblings in Sweden chose their own fixed surnames, so two brothers can have different surnames [S1].
- **Transition dates.** The laws differ by country, and people widely ignored them, so read the actual parish entries:
  - Denmark: a decree in 1828 and a ministerial circular in 1856.
  - Sweden: Brady places voluntary fixed surnames around the 1880s [S1], and Castillo dates the first changes to about 1860 [S3]. The ordinance of 5 December 1901 on adopting family names (SFS 1901:125) controlled which new family names a parish could enter in the church book. It obliged no one to take a family name, and patronymics were still in use in every registration district in the late 1950s [S19]. The Names Act (SFS 1963:521) took effect on 1 January 1964 [S20]. From 1 January 1983 the law allowed a person to take a -son or -dotter surname for special reasons, and from 1 July 2017 a child can get one at birth [S21]. A modern -son or -dotter surname therefore does not show the old practice.
  - Norway: the first Name Act came on 9 February 1923.
  - Iceland never abandoned patronymics [S9].

  Lisson's guest's "mid-1800s, each country its own year" [S6] fits Denmark only. Do not apply it to Swedish or Norwegian parishes. Tanner's "after about 1830, varying by country" [S9] is a rough orientation, not a rule.
- **Marriages.** Under traditional patronymic practice, wives keep their own patronymic or maiden name, so a wife whose surname differs from her husband's is not a mistake [S5]. Norway's 1923 Name Act required a wife to take her husband's surname, so for later Norwegian records also log her married-name form. A census household can list a man and several women, none of them with his surname, and nothing shows which woman is his wife. Prove the marriage in the parish register [S9].

## Close with an origin packet

Return:

- the name-form register
- the candidate comparison table, with the discriminators used for each candidate
- the baptism entry with its parish, volume, page or date, and image locator, or the bounded browse range with no hit
- the sibling and marriage reconstruction, citing the parents named in each entry
- any unresolved alternate identities, kept visible

A co-traveller row, a shared farm name or an indexed baptism hint is still a candidate until the parish entries agree.
