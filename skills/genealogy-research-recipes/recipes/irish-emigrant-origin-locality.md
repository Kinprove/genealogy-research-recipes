---
id: "irish-emigrant-origin-locality"
title: "Resolve an Irish emigrant's origin locality from a place statement"
summary: "Resolve an Irish place named by an emigrant's records or family tradition to a searchable locality."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "none"
gates: []
guardrails: [{"id": "IRISH-EMIGRANT-ORIGIN-LOCALITY-01", "text": "Do not record a townland as the origin on a place-name, surname-distribution or farm-name match alone. Submit the person-specific evidence that ties this person to the townland, from destination or Irish records, and leave the identity ruling to the researcher."}]
handoff: []
checked: "2026-11-04"
checked_basis: "opened 2026-11-04"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"section": "Records by country and region", "group": "Britain and Ireland", "order": 129}
---

# Resolve an Irish emigrant's origin locality from a place statement

Use when a destination record or family tradition names an Irish place (Cork, Belfast, Mullingar,
Derry, Armagh, a farm name) and you are about to search for the emigrant there. Treat the name
as a lead whose administrative level is unknown. It may be a port, a well-known nearby town or a
same-named unit. Classify it, test it against surname distribution and denomination, then search
the whole locality before adopting any townland. For the Catholic-parish choice and register images,
use [Irish Catholic parish image recovery](irish-catholic-parish-image-recovery.md).
If a "previous parish" or residence field may be a transit point, use [U.S. immigration search recovery](usa-immigration-search-recovery.md).
The same place-role logic for the Russian Empire is in [Russian-Empire emigrant origin recovery](russian-empire-emigrant-origin-recovery.md).
Identity rulings belong in [evidence/proof judgment](evidence-proof-judgment.md).

## Contents

- The failure this prevents
- 1\. Collect and classify every place statement before choosing one
- 2\. Generate same-named and mis-transcribed candidates
- 3\. Test each candidate against surname and denomination
- 4\. Search the whole locality, including estate papers
- Recover additional origin statements
- 5\. Treat a townland-named farm as a hypothesis
- 6\. Output and handoff

## The failure this prevents

The usual error is to read a named town as the birthplace and search a common name there. That
attaches the wrong person. A related error treats conflicting family place statements as mistakes,
when they may name different levels. Surname presence in a valuation or census, or a farm name
that matches a townland, is also wrongly taken as proof of origin. Finally, the search is often
limited to the family's later church. Each step below blocks one of these errors.

## 1. Collect and classify every place statement before choosing one

- Collect all destination-side statements first: vital, church, immigration, naturalization,
  obituary, newspaper and land records, plus each family-tradition version. Include siblings who
  emigrated. A brother’s last census named the locality where the emigrant’s records gave only “Ireland” [S3], [S4]. Record its date and wording and compare the other family statements [S2].
- Classify each statement by every unit it could name: townland, civil parish, Catholic parish,
  barony, county, diocese, poor-law union/registration district, city, departure port or nearby
  well-known town. One word can name several units. Armagh is a city, civil parish, barony, county,
  archdiocese and poor-law union; Derry/Londonderry is both a city and a county [S3], [S4].
- A named place may be the departure port or the nearest town a stranger would recognize. The
  guests warn that a family convinced of Cork may be naming only the departure point, and that
  “Belfast” may stand for a smaller place nearby [S3], [S4]. One birth record placed the family about ten miles from the remembered Mullingar, across civil, ecclesiastical and registration boundaries [S2]. Search the jurisdiction for the recorded locality before accepting a common-name match.
- Different records may name the religious parish, the registration district or the townland.
  Keep conflicting statements side by side as possibly different levels. Do not choose a winner
  at this stage [S2], [S3], [S4].

## 2. Generate same-named and mis-transcribed candidates

- Do not assume the famous place. Ireland has more than 60,000 townlands, and many names repeat
  because they are descriptive (Derry from *doire*, “oakwood”; Bally-, Tully-, Drum-). In County Down, the Newcastle in one family’s account was a townland in Slanes civil parish on the Ards Peninsula, distinct from the seaside town near the Mournes [S3], [S4].
- Test one-letter transcription errors and older spellings. Confusing Portstewart (Co. Londonderry) with Fort Stewart (Co. Donegal, near Ramelton) sends the search to a different county [S3], [S4].
- Keep each priest’s spelling. Where two forms share a stem, as in one Kilkenny townland search, query the stem with the county and compare the candidate names in the gazetteer [S1]. Use PlaceNamesNI for the six counties of
  Northern Ireland, Logainm (the Placenames Database of Ireland) for the Republic, and the historic
  map viewers of PRONI and of Tailte Éireann (formerly Ordnance Survey Ireland) [S3], [S4].
  Keep the recorded spellings beside the standard form.

  Keep English and Irish forms in the candidate-place table. Logainm displays both forms [S25], [S31];
  search each relevant form.

- **Look for a road bearing the recorded place name.** If the birthplace is hard to place,
  search a modern map for a road with that name in the reported county [S39]. Use a road match
  to find candidate townlands and parishes on a period map or in a gazetteer. Keep the road as a
  lead until records tie the person to the locality.

  In Northern Ireland, compare a modern basemap with a historical Ordnance Survey map in the
  PRONI Historical Maps Viewer and read the townland and parish for points along the road
  [S41 @2026-11-21].

## 3. Test each candidate against surname and denomination

- Look up the surname in the Tithe Applotment books (1823–1837), Griffith's Valuation (1847–1864)
  and the 1901/1911 censuses, even if the person left earlier. Siblings, cousins and their
  descendants who stayed are what these later records capture. Use the clusters to choose
  candidate parishes for church-record searches; one presenter does this even for 1700s emigrants
  [S3], [S4]. Flag a candidate area where the surname does not occur and lower its priority;
  absence from a name list ranks an area down but does not exclude it. Houser describes the same
  approach, using surname-distribution views from the 1850s and 1901. It works best for a
  relatively uncommon surname [S7], [S8].

- Check which census years survive before you log a year as searched. The 1821–1851 returns were
  mostly destroyed in the 1922 Public Record Office fire at the Four Courts, leaving only fragments.
  The 1861 and 1871 returns were destroyed by government order shortly after collection, and 1881
  and 1891 were pulped during the First World War. 1901 and 1911 are the only complete returns
  from before independence [S14].

- For 1841 and 1851, use the census search forms: searches of those returns for people proving their age for an old-age pension under the 1908 Act. The National
  Archives of Ireland has withdrawn their online catalogue; use its Reading Room microfilm,
  FamilySearch or Findmypast, and PRONI for Ulster counties [S15 @2026-11-19]. The 1926 census covers only the
  26 counties of the Free State, not Northern Ireland, and has been free online at the National
  Archives of Ireland since 18 April 2026 [S16 @2026-11-19], [S32 @2026-11-19]. Report a missing year as a survival gap, not as a
  failed search.

- Use the 1901/1911 religious profile of the surname (both censuses record each person's religion)
  to decide which denominations’ registers to search. In one Australian Catholic family the grandfather’s conversion in Australia explained why a search restricted to Catholic registers in Ireland would have missed his earlier affiliation [S3], [S4].
- Limit: distribution and denomination tests rank where to search. They do not identify the
  family, and a cluster of a common surname shows very little.

**Search the surviving 1821–1851 census data before you log one of those years as a survival gap.**
The National Archives of Ireland's *Search the Census (c19)* page covers 1821, 1831, 1841 and 1851
[S20 @2026-11-13]. It searches that census data, not the 1841 and 1851 census search forms above.
Run it for the surname and county first.

## 4. Search the whole locality, including estate papers

- **Search estate papers by landlord and place.** NLI notes that Griffith's Valuation records the
  owner as well as the occupier of land, that surviving estate papers can be searched by the
  landlord's or the estate's name once a landlord is identified, and that a list of surviving
  estate papers arranged by civil parish is on the subscription site Irish Ancestors
  [S21 @2026-11-17]. Record the landlord as written and trace the relevant estate and holding
  repository. When using PRONI's catalogue, search the townland, parish or street as well as the
  person's name [S22 @2026-11-17]. Save the collection and item references.

- For Ulster tenant families, search the landed-estate rentals, lease books and correspondence
  for each candidate locality. Farmers were tenants, estate papers are rich for parts of Ulster,
  and most are held in archives such as PRONI rather than online [S9], [S10].
- Read rental margins for notes that a tenant went to America [S9], [S10].
- A rental or lease book dated after the emigration may recite earlier leases (tenants, details)
  that no longer survive [S3], [S4]. Record the date of the reciting document separately from the
  date of the lease it recites, and cite the recited lease only through the later document.
- Search every denomination's registers and every record type held for the locality: land,
  church and miscellaneous name lists. Do not stop at the presumed church [S9], [S10].
- Search the townland in these further name lists and court books for the years each covers, and
  log whom each one covers:
  - the 1766 religious census: surviving parts only, free in the Virtual Record Treasury of
    Ireland [S17];
  - the 1796 flax growers' premium lists: about 60,000 growers, most of them in Ulster [S18];
  - petty sessions order books, largely 1851–1924 with gaps: only people who came before the
    court [S19].

  Each list covers one class of people, so absence from it does not prove absence from the place.

## Recover additional origin statements

- **Look for a passport application when a deceased emigrant or relative returned to Ireland.**
  Use the approximate date of the trip, including a return to settle an estate, to search the
  historical passport applications of the issuing country [S39], [S40]. Transcribe the applicant's
  stated birthplace separately from any destination or reason for travel. Use a relative's
  birthplace as a lead for the emigrant and log the application date and number or archival reference.

  For a regular U.S. passport, start with M1372 (1795–1905, with gaps) or M1490
  (January 1906–March 1925) [S40].

- **Search the published passenger lists for the matching period.** Locate Brian Mitchell's
  *Irish Passenger Lists 1803–1806* for Hardwicke-paper departures from Irish ports in
  March 1803–March 1806, or *Irish Passenger Lists 1847–1871* for the Londonderry lists of
  J. & J. Cooke (1847–1867) and McCorkell (1864–1871) [S24], [S29]. Search the matching volume
  and read the passenger's stated address or residence and identifying details. Record the title,
  edition and page consulted.

- **Keep a famine-era Irish Sea crossing open when the passenger search is blank.** Travel from
  Ireland to Great Britain in 1845–1852 was within the United Kingdom [S33], [S34]. The Board of
  Trade series BT 26 and BT 27 start in 1878 and 1890 respectively and cover voyages to or from
  ports outside Europe and the Mediterranean [S35]. Treat a blank result in those series as a
  coverage gap and test the crossing through records in Britain.

- If the emigrant may have been in England or Wales on the night of 30 March 1851, search the
  1851 census (HO 107) for the emigrant and family. Read the household's birthplaces and
  relationships [S36].
  If the birthplace says only “Ireland,” use the census residence to target local parish registers
  and civil birth and marriage indexes for the family [S33].

- For a famine-era emigrant who settled in Australia, use the state death index as a locator for
  the death registration and check the gravestone inscription [S33]. For a New South Wales civil
  death from March 1856, read the certificate's birthplace, parents and informant details [S37].
  Log the gravestone's Irish place wording and any stated kinship separately from the certificate
  [S38].

- For a family in the Bytown area in 1829, search the McCabe List: a petition dated
  5 February 1829 by 673 men, mostly Irish, with family-origin details. Moran's guide points to
  Colonial Office reference CO 384/22 [S26], [S29]. Extract the stated Irish place and relatives
  and pursue the original. Appearance in this petition alone does not classify someone as a
  Peter Robinson emigrant.

- For an emigrant known to have served as a Latter-day Saint missionary, search the Church
  History Library's *Missionary Department Missionary Registers, 1860–1959* (CR 301 22), for
  missionaries set apart in Salt Lake City. Missionaries set apart elsewhere are generally not
  listed [S27], [S30]. Copy birth and parentage statements from a matching entry, then use them
  to seek the corresponding Irish records.

- Search *Boston Pilot* missing-friends advertisements for the emigrant and known associates.
  The *Information Wanted* series began in 1831 and continued for about 85 years [S28], [S31].
  Extract the seeker, person sought, Irish places and stated relationships from a matching
  advertisement; preserve its date, newspaper locator and the database or book volume used.

- **Read the loan record's later returns, not only the borrower index.** Findmypast's
  *Ireland, Poverty Relief Loans 1821–1874* contains T91 records, mostly dated 1824–1846, from ten
  county boards: Clare, Cork, Galway, Kerry, Leitrim, Limerick, Mayo, Roscommon, Sligo and
  Tipperary [S23]. Match the volume's locality and years to the borrower; some papers extend
  beyond those boards. Later returns can state residence, health or emigration [S23], [S29].
  Separate the loan date from each later report and distinguish borrower, guarantor and other
  named people.

## 5. Treat a townland-named farm as a hypothesis

The Gilmore interviews describe Ulster settlers who received Pennsylvania land grants in the 1780s
and, in many cases, named the property after their home townland. These farm names appear across
western Pennsylvania [S5], [S6]. Record the tract or farm name from the warrant, survey, patent or
family record. Then list every Irish townland of that name. Because of the duplication in step 2,
a match produces candidates only. Each one must pass steps 3–4 before it is adopted.

## 6. Output and handoff

Return:

1. **Place-statement table:** source | literal place | possible unit levels | same-named candidates |
   transcription alternatives.
2. **Candidate-locality register:** candidate | surname presence in Tithe/Griffith/1901–1911, with
   the dates seen | denomination profile | estate collections, denominations and record types
   searched | status (lead / tested / unsupported).
3. **Handoff:** the selected parish and denominations, sent to register retrieval (the Catholic
   parish image recipe above for Catholic registers), with the remaining gaps named. Examples are
   unsearched estates or denominations, and statements not yet classified.
4. **Retrieval log for additional origin statements:** collection or book title, volume/page or
   item reference, report date, literal Irish place and relationship wording, and inspection
   status.

Do not record a townland as the origin on a place-name, surname-distribution or farm-name match
alone. Submit the person-specific evidence that ties this person to the townland, from destination
or Irish records, and leave the identity ruling to the researcher.
