---
id: "scandinavian-patronymic-farm-name-record-recovery"
title: "Recover a Scandinavian emigrant's home-parish entries under patronymic, farm and soldier names"
summary: "Find a Danish, Norwegian, Swedish or Icelandic emigrant's home-parish entries under patronymic, farm and soldier names."
kind: "records"
scope: {"platforms": [], "tasks": ["Find a Danish, Norwegian, Swedish or Icelandic emigrant's home-parish entries under patronymic, farm and soldier names."]}
triggers: ["Find a Danish", "Norwegian", "Swedish", "Icelandic emigrant's home-parish entries under patronymic", "farm and soldier names"]
privacy: "none"
gates: []
guardrails: [{"id": "SCANDINAVIAN-PATRONYMIC-FARM-NAME-RECORD-RECOVERY-01", "text": "the American surname is usually not the register name; separate same-named parishioners by birth date, parents, spouse and farm, never by name alone."}]
handoff: ["scandinavian-parish-record-recovery"]
checked: "2026-11-04"
checked_basis: "opened 2026-11-04"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"tier": "pointer", "group": "Church and civil registers", "order": 1057}
---

# Recover a Scandinavian emigrant's home-parish entries under patronymic, farm and soldier names

Use this when a Danish, Norwegian, Swedish or Icelandic emigrant is known from destination records and you need to find that person in the home parish. The main way this goes wrong is searching the American surname in home-country indexes, finding nothing or attaching the wrong same-named person. The name in the parish register is usually not the American surname. Same-named parishioners are common, so separate them by birth date, parents, spouse, farm and vaccination entries, never by name alone.

Covered elsewhere and not repeated here: [same-name elimination](evidence-proof-judgment.md), [searching through an associate (§9)](ancestry-record-search-recovery.md), classifying name tokens (the catalogue's recipe on name searches across scripts and OCR), [native spellings and holdings audits (§2)](familysearch-practical-record-workflows.md).

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
- Rebuild siblings and marriages from the named parents
- Close with an origin packet

## Fix the identity anchors before touching home-country indexes

From destination records (census, church, naturalization, obituary, passenger list), extract and keep separate:

- the exact birth date
- the town of birth or last residence, and the parish it belonged to
- the father's given name, if any record states it
- co-travellers such as siblings, a future spouse or neighbours

Start with destination records, identify the parish, and then search that parish [S2]. An approximate age is not an anchor. The exact birth date is. Swedish church books, including the household examination books, record the exact birth date, often in its own column, so the date works almost like an identifier for telling same-named people apart [S5].

Do not search the American surname backwards as if it were hereditary. Everett's example: a family known as Jensens in America cannot simply be looked for as Jensens in Denmark [S2].

## Build the expected name forms and log them as a register

Create one row for each form you expect or observe. Record the literal form, the record it appears in, and its type: patronymic, matronymic, farm/house, soldier byname or adopted.

- **Patronymic.** Built from the father's given name plus -son/-sen or -dotter/-datter. It changes every generation [S1], [S5]. Build spelling variants as well. Brady shows one man recorded as Persson, Pierson, Pettersson and similar forms across Swedish and U.S. records [S1]. Swedish given names also vary, for example Per, Petter, Peder and Pär for Peter [S1].
- **Matronymic.** An illegitimate Swedish child may carry a surname based on the mother's name [S3]. A female-based surname is a lead to an illegitimate birth, not an error. Check the baptism entry for it before you look for a father.
- **Farm or house name.** Clerks added these to tell parishioners apart. A farm name may stay with a family for generations or for only one [S6]. Castillo reports that the farm name changed when a person moved to another farm, and that she has seen a son-in-law who married into a family of daughters take his father-in-law's name or the farm's name [S3]. A change of farm name is therefore not a change of person.
- **Soldier byname.** The army assigned these because so many men had the same name, and soldiers may appear under either the patronymic or the soldier name. Some men kept the byname afterwards. Brady's example is Johan Magnus Anderson from Kalmar province, who was John Falk in the U.S. and Johan Magnus Anderson in Swedish records [S1]. In S5, the guest's family surname came from a great-great-uncle's army byname, which an emigrant brother adopted instead of the patronymic. Search military records by unit and by the soldier name, not only by the civil name, starting with the local muster [S8].
- **Adopted American name.** This may come from none of the forms above. Everett's Walter Slangerup was christened Waldemar … Martinson after his father. After emigrating he took the name of Slangerup, a town northwest of Copenhagen that his great-grandfather came from [S2]. Treat the American surname as one observed form, not as the search key.

In your tree, enter the name exactly as it appears in the christening (the first record) as the primary form. Log every farm, soldier or American name as an alternate with its source [S6].

## Follow a Swedish soldier name beyond the muster index

ArkivDigital's April 2026 demonstration distinguishes its general-muster index from other regimental rolls. Starting from a Swedish soldier name and regiment [S18]:

- Browse the regiment's rolls for intervening years as well as the periodic general musters; those separate rolls need not be in the general-muster index.
- If a dismissal note refers the soldier for *underhåll*, use that referral to investigate the Krigsmanshuset archive.
- If the original names a *rusthållare* and records a *krigsmanshusavgift*, investigate the fee documentation for changes of rusthållare. Keep that holder and fee distinct from the soldier and his support history.

The demonstration's original records contain support and fee annotations absent from the index. Check the actual indexed fields and the surviving regiment/archive volumes for the relevant interval; the demonstration does not establish current coverage or an individual's identity. [S18]

## Search the forms, then browse to the known date

Search the parish indexes under each patronymic and farm form in the register. If all of them fail, do not conclude the person is absent. Browse the parish register to the known birth date and recognize the entry from its context. Everett found Slangerup this way after no index search could reach him [S2].

Write down the parish, register volume and date range you browsed. If you get no hit, report that bounded range, not "not born there."

## Pivot through co-travellers when the passenger search fails

First search the departure registers kept in the home country:

- Denmark: the Copenhagen police registered emigrants' shipping contracts from 1868 to 1934, and the State Emigration Office from 1934. Rigsarkivet says the registers for 1868–1911 are name-searchable on the Danish Emigration Archives' site; that site's own year list runs to 1920, with 1912, 1917 and 1918 missing. [S23], [S24]
- Norway: search the police emigrant protocols in [Use Norwegian censuses and emigrant protocols within their ranges](#use-norwegian-censuses-and-emigrant-protocols-within-their-ranges).
- Sweden: search the port lists and moving-out registers described in [Swedish household reconstruction](scandinavian-parish-record-recovery.md#before-1869-look-for-emigrants-in-the-moving-out-registers). Emiweb's *Emigranter i svenska kyrkböcker* (formerly Emibas) indexes emigrants from parish registers. It was compiled systematically only for about 1836–1895, and not for Uppsala, Norrbotten or Stockholm counties. It is a subscription database. [S25]

Record the register, years and index you searched. A miss is bounded by them.

If you cannot find the emigrant on a passenger list:

1. Open the manifest of a known co-traveller, such as a future spouse or a sibling. In S5, the guest found his great-grandfather next to his future wife, listed under a father-derived "-son" form instead of the American surname.
2. Scan the nearby pages, not only the family group, for people with the same farm name and a matching patronymic. In S7, a probable brother was listed on the parents' page of a Norway Heritage transcription, outside the family group, under the same farm name; the family's daughter appeared a page or two later. Those transcriptions mainly cover 1825–1873/75. The site search is currently down, so browse by ship and year.
3. Treat any such person as a candidate only. Confirm through:
   - the home-parish baptism, which should name the expected parents and parish
   - the minister's record of people moving out (in Norwegian church books, the *utflyttede* section), with an entry dated before sailing [S7]

S7 found both records for its candidate. The moving-in and moving-out registers (*innflyttede* / *utflyttede* in Norway) also let you follow a person between parishes [S2], [S9].

## Discriminate same-named candidates with a comparison table

Same-named people are common in a parish. Families with the same parents' names and the same children's names are also common, so a careless search attaches other families' children [S1], [S4]. Build one row per candidate with these columns:

- exact birth date
- father's name, and mother's name where recorded
- spouse
- farm or house of residence, taken from house censuses and farm records [S4]
- smallpox vaccination date and place, from baptism, confirmation or marriage entries [S2]
- the locator for each entry

Vaccination became compulsory in Norway from 1810 and in Sweden from 1816. Denmark's decree of 3 April 1810 required a vaccination certificate for school, confirmation and marriage. In Danish confirmation and marriage entries after 1810, expect the vaccination note and use it. Everett shows it in a Norwegian marriage entry of 1843 and in confirmation entries, and uses the vaccination date and place to decide whether two records are the same person [S2]. In other places and periods, check whether the column exists before you count a blank against a candidate.

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

- Rigsarkivet has scanned every census of the kingdom up to 1940 on Arkivalieronline. Name-searchable transcriptions are complete for 1787, 1801/1803, 1834, 1840, 1845, 1850, 1860, 1880, 1885 (Copenhagen only) and 1901, and partial for other years up to 1930. They are in DDD (Dansk Demografisk Database, run by Rigsarkivet), which Rigsarkivet is moving into Søg i Samlingerne. A nil in a partly transcribed year is not a negative. Check each transcription against the scan. [S16], [S22]
- Use the lægdsruller (military levying rolls) to bridge censuses for men. From 1788 to 1848 they enrolled males of the peasant class from birth, and from 1849 all men. They give the father's name (the mother's if the man was born outside marriage) and the man's moves while liable for service. Moves can be followed across the country from 1789. Before 1788 only scattered rolls survive. [S17]

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
