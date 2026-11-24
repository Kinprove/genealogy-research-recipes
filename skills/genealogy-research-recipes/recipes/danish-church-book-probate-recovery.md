---
id: "danish-church-book-probate-recovery"
title: "Reconstruct a Danish household from church books and probate"
summary: "Find a Danish ancestor's church-book entries, civil marriage and probate by choosing the register copy, South Jutland civil register and probate authority that apply to the date."
kind: "records"
scope: {"platforms": [], "tasks": ["kirkebøger, kontraministerialbog, skifteprotokol, dødsanmeldelsesprotokol, borgerlig vielse and personregister searches"]}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "DANISH-CHURCH-BOOK-PROBATE-RECOVERY-01", "text": "Choose the probate authority from the deceased's status and the date of death, not from the parish alone."}, {"id": "DANISH-CHURCH-BOOK-PROBATE-RECOVERY-02", "text": "When an entry is missing, damaged or unreadable in one copy, read the same event in the other copy."}, {"id": "DANISH-CHURCH-BOOK-PROBATE-RECOVERY-03", "text": "For a South Jutland birth, marriage or death in 1874–1925, search the personregister first, then the church book."}]
handoff: ["scandinavian-patronymic-farm-name-record-recovery", "evidence-proof-judgment"]
checked: "2026-11-18"
checked_basis: "Read 2026-11-18"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": ["request", "third-party-tool"], "contact": []}
router: {"section": "Records by country and region", "group": "Western and Northern Europe", "order": 171}
---

# Reconstruct a Danish household from church books and probate

Use this recipe when you have a Danish ancestor's name, a parish or estate, and a rough date, and you need the church-book entries, a civil marriage or a probate (skifte). Work event by event through the church books, then tie the events into one household with censuses, levying rolls and probate. Choose the probate authority from the deceased's status and the date of death, not from the parish alone.

Related recipes:

- [Scandinavian patronymic and farm names](scandinavian-patronymic-farm-name-record-recovery.md) for Danish censuses, DDD, the lægdsruller (levying rolls) and emigrants' name forms.
- [Swedish parish registers](scandinavian-parish-record-recovery.md) for Sweden and Finland.
- [Evidence/proof judgment](evidence-proof-judgment.md) for merge, separate and proof rulings.

## Contents

- Find the parish and the authority for the date
- Read the church book for the period
- Trace a historical cause of death
- Check civil marriages before calling a marriage missing
- South Jutland: follow the period's register
- Route a probate by status and date
- Combine the sources into one household
- Close with a household packet

## Find the parish and the authority for the date

Rigsarkivet's guides find church books by parish, and probates and civil marriages by the authority that created them: the market town's byfoged (town judge), the herredsfoged (rural district judge), the birk, the amt, the estate or, later, the court district. When you know the place but not the parish or district name, the guides point to DigDag, the historical administrative map. [S1 @2026-11-18], [S3 @2026-11-18], [S5 @2026-11-18]

For each event date, write down the parish, the market town or herred or birk, the amt and, for a tenant, the estate. Search each record type under the authority that applies on that date, not under today's names.

## Read the church book for the period

If the place is in South Jutland, read the South Jutland section first: it says which routes in this section apply there.

Rigsarkivet's guide says special rules apply to the church books of recognised faith communities (anerkendte trossamfund), which have a guide of their own. [S1]

Royal letters of 1645 and 1646 ordered priests throughout the country to register baptisms, betrothals or marriages, and deaths, but far from every parish has a church book from the 1600s. [S1]

Outside South Jutland, before about 1814 a parish kept one book, the enesteministerialbog. It was written in date order, not on fixed forms, and its basic entries are births, confirmations (from 1736), marriages and deaths. Some priests also entered mothers' churchings (introduktion), communion, betrothals (until 1799) and public confessions. Some of these single books were lost in rectory fires. [S1]

Outside South Jutland, a rescript of 11 December 1812 brought preprinted forms from about 1814 and two copies of each book: the hovedministerialbog, kept by the priest, and the kontraministerialbog, kept by the parish clerk (degn); the two were to be stored under separate roofs against loss by fire. [S1] Rigsarkivet's leaflet on nineteenth-century church books dates the forms and the two sets from about 1812, names the schoolteacher or the parish clerk as the second writer, and says the two copies were meant to hold the same information. [S2] From about 1814 the entries run by event type in the order born, confirmed, married, arrivals, departures and dead, and births, confirmations and deaths list males before females. [S1]

When an entry is missing, damaged or unreadable in one copy, read the same event in the other copy. Cite the copy you used. If the copies differ, record both readings.

**Privacy gate:** <!-- privacy-gate: request --> A church book from 1961 on can name people who may be living; unless the entry concerns only people known to be dead, answer the privacy gate in `SKILL.md` before you order it for the reading room.

Rigsarkivet holds church books from the whole country from the 1600s to about 2000. Its guide sends you to the scans on Arkivalieronline, by parish, for the single books before about 1814 and for both copies from about 1814 to 1960. From 1961 it routes you to the kontraministerialbog through Søg i Samlingerne: death lists up to 1969 may be scanned there, and the rest is ordered for the reading room. [S1 @2026-11-18]

Rigsarkivet says Link Lives searches transcriptions of Danish parish registers for 1814–1891. [S9 @2026-11-18] Treat a Link Lives hit as a pointer to the scanned page and read the entry there.

Some parishes kept lists of people moving in and out (af- og tilgangslister) in about 1814–1875. [S1] The leaflet says the lists were kept until 1854 in towns and 1875 in the countryside, and often record only servants and poor people. [S2] A missing arrival or departure entry does not show that the family stayed put.

Use the other entries to link people. A baptism names the child, the parents and their residence; the godparents were often relatives of the parents. A confirmation names the confirmand, the parents or the master (husbond) and their residence, often says whether a parent was dead, and in older books gives grades. A marriage names the couple and their residence, may name their parents, and names the sureties (forlovere), normally close male relatives. A newer burial entry may name the parents and spouse and the couple's last common residence. A confirmand described as the child of a late ("afdøde") parent dates that parent's death before the confirmation, so search the burials backwards from it. [S2]

Church books after 1925 can contain CPR (personal identity) numbers and fall under a 100-year access period. In the books on Arkivalieronline, CPR numbers are blurred, and from 1892 the remarks column of the birth lists is blurred. [S1 @2026-11-18] A blurred field is withheld and an unscanned book is offline; neither is missing, so do not record either as a nil.

## Trace a historical cause of death

Take the death date and any recorded residence or place of death to Rigsarkivet's death-certificate guide. Use the residence at death to identify the medical district, then search Dødsattester under the creator the guide specifies. For a sudden or unexplained death, check the medico-legal certificates. The guide routes rural medico-legal certificates from 1871 to Sundhedsstyrelsen and lists South Jutland separately, with no surviving certificates noted for 1864–1920 and Sundhedsstyrelsen coverage from 1921. [S17 @2026-11-22]

Use the place of death or discovery and the date to identify the local police or judicial authority that could have investigated. In the catalogue, look for series under that creator using dødfundne personer or selvmord, and check its forhørsprotokol (inquiry register) or politiprotokol where applicable. [S16 @2026-11-22], [S18 @2026-11-22], [S19 @2026-11-22]

For a suspected suicide, also search Danmarks Statistik's Rapporter over selvmord by year and open the exact bundle, using the region or journal-number range where listed. [S20 @2026-11-22], [S24 @2026-11-22] Check the bundle's access in the catalogue. The Arkivalieronline list headed 1895–1924 ends at 1904, and Daisy lists the 1905–1924 bundles for ordering. [S21 @2026-11-22], [S22 @2026-11-22]

Compare the statistical return with the underlying local investigation and the death certificate. Identify each by record type and locator, and use published aggregate tables for context only. [S16], [S23]

**Privacy gate:** <!-- privacy-gate: request --> A request for a death certificate, investigation file or individual statistical return can disclose the deceased's identity and sensitive death information, names of relatives or witnesses who may be living, and the requester's kinship evidence to Rigsarkivet. Apply the record-request gate in `SKILL.md` before sending the request.

For a relevant unit with no scan, check the series' access rules and use Rigsarkivet's reading-room order route for that exact unit. Death certificates have a 75-year access period. [S17 @2026-11-22], [S19 @2026-11-22], [S22 @2026-11-22]

## Check civil marriages before calling a marriage missing

If the place is in South Jutland, read the South Jutland section first: it says which routes in this section apply there.

Before 1851 only a priest could marry a couple. From 1851 civil marriage was allowed when one or both partners belonged to no recognised faith, or when the two belonged to different faiths; from 1923 anyone could choose it. [S3]

**Privacy gate:** <!-- privacy-gate: request --> A civil marriage book can name people who may be living; unless the entry concerns only people known to be dead, answer the privacy gate in `SKILL.md` before you order it for the reading room.

Civil marriages are filed under the civil authority, not the parish. For 1851–1919 look under the byfoged, herredsfoged or birk, in the marriage book (ægteskabsbog or ægteskabsprotokol) or, where none was kept, the notarial protocol (notarialprotokol). For 1919–1922 look under the police district in the countryside and the town council (kommune) in market towns. For 1923–1970 look under the sognefoged (parish bailiff) in the countryside and the market-town council in towns, starting from the register to the marriage book. From 1971 look under the kommune; those books are not scanned. [S3 @2026-11-18]

In Copenhagen the 1851–1922 originals are at Københavns Stadsarkiv, and the 1923–1970 marriage books are scanned under Københavns kommune. [S3 @2026-11-18]

Rigsarkivet says a civil marriage is often noted at the back of the church book, up to 1922 in the bride's parish, and that in some market towns civil marriages are found in the magistrate or town-hall archives. [S3 @2026-11-18] Check both before you call a marriage missing.

## South Jutland: follow the period's register

South Jutland's church books reach back further than the rest of the country's: the oldest is from 1573. Fixed forms began there in 1763, and from 1775 the books were to be kept in two copies. [S4] Do not apply the dates for the rest of the country there.

The other-copy rule applies to the two copies kept there from 1775.

After South Jutland became part of Prussia in 1864, civil registration of births, marriages and deaths began in 1874, kept by the Standesamt (in Danish, personregister) under a registrar (personregisterfører). Rigsarkivet calls the church books for 1874–1925 secondary sources. The personregister covered births, marriages and deaths; confirmations stayed in the church book. [S4] For a South Jutland birth, marriage or death in 1874–1925, search the personregister first, then the church book.

From 1926 priests again married couples, and marriages were again entered as in the rest of the country, while births and deaths stayed in the personregistre. [S4]

Route each South Jutland search by event and date:

- **Births and deaths:** the church book before 1874; the personregister first for 1874–1925, with the church book as a secondary source; from 1926 the guide gives both the personregister and the church book. [S4 @2026-11-18]
- **Confirmations:** the church book in every period. [S4 @2026-11-18]
- **Marriages before 1874:** the church book; the guide names no civil-marriage route for South Jutland before 1874. [S3 @2026-11-18], [S4 @2026-11-18]
- **Marriages in 1874–1925:** the civil registers (personregistre), which hold every marriage of those years; the church book is secondary. [S3 @2026-11-18], [S4 @2026-11-18]
- **Marriages from 1926:** a church wedding in the church book; Rigsarkivet says marriages were then entered as in the rest of the country, so a civil wedding follows the general civil-marriage routes. [S4 @2026-11-18]
- **Probates up to 1920, ordinary or private:** start with the Register over sønderjyske skifter op til 1920 (below); then the authority for the date: the herredsfoged or birkefoged in the countryside and the byfoged in towns before 1864, none named for 1864–1866 (see the rule below), and the Prussian district courts (amtsretter) for 1867–1920. The guide names no other South Jutland authority for ordinary or private probates, so do not route a South Jutland probate to an estate or an amt by the deceased's status. For a soldier or officer, also check the army row below. [S5 @2026-11-18]
- **Probates after 1920:** the guide's South Jutland rules stop at 1920, so use the general probate routes. [S5 @2026-11-18]
- **Soldiers, officers and their families in South Jutland before 1864:** also check the army rule in the probate section; the Schleswig and Holstein regiments stayed with their auditors until 1864. [S7 @2026-11-18]

**Privacy gate:** <!-- privacy-gate: request --> A South Jutland register or church book from 1960/61 on can name people who may be living; unless the entry concerns only people known to be dead, answer the privacy gate in `SKILL.md` before you order it for the reading room.

Before 1874 the parish's hovedministerialbog or kontraministerialbog is scanned on Arkivalieronline. The personregistre are scanned on Arkivalieronline by registration district, which is roughly the parish, up to 1960/61, and the 1926–1960/61 church books are scanned as kontraministerialbøger. For 1960/61–1973, deaths are online up to about 1970, and the rest is ordered through Søg i Samlingerne for the reading room in Aabenraa. Rigsarkivet's guide gives separate routes from 1974. [S4 @2026-11-18]

Private probate was easier to arrange in Schleswig, so fewer probates survive than elsewhere in Denmark. Rigsarkivet's index to South Jutland probates up to 1920 is the Register over sønderjyske skifter op til 1920 in DDD; the guide says all probates are entered there with the series and the protocol page. [S5 @2026-11-18] If the register gives no authority for a probate from 1864–1866, treat its route as unresolved rather than following another period's route.

The register's search page answered on 18 November 2026. [S10 @2026-11-18] Rigsarkivet is phasing DDD out, is moving its data to Søg i Samlingerne and warns that DDD searches may fail. [S9 @2026-11-18] If the DDD search fails or the register has gone, try Søg i Samlingerne, and record the probate search as incomplete. Record an empty result as a nil for that index only, not as proof that no probate was held.

## Route a probate by status and date

If the place is in South Jutland, read the South Jutland section first: it says which routes in this section apply there.

A probate (skifte) lists the deceased's property and heirs. The oldest surviving probates are from about 1650, and older protocols may be lost. [S5]

Until 1851 the deceased's status decided which authority held the probate. [S5]

- **Market-town residents (købstadsbeboere):** the town's byfoged, in the probate protocol (skifteprotokol). [S5 @2026-11-18]
- **Tenants (fæstere) and employees of an estate:** the estate's own archive. From 1817 the tenants of smaller estates went to the herredsfoged or birkefoged. Tenants in a cavalry district (rytterdistrikt) went to the district or its birk; the cavalry districts were abolished in 1776. For North Jutland, the Stedregister til Nørrejyske Godsarkiver helps you find the estate from the parish. [S5 @2026-11-18]
- **Estate owners, freeholders (selvejere) and other rural people without tenant status:** the amt before 1793, then the herredsfoged or birk until 1851. [S5 @2026-11-18]
- **Private probates** (samfrændeskifte, kommissionsskifte, eksekutorskifte, eksekutorbo), settled outside the authorities: the amt's archive, in series for probates or executors. [S5 @2026-11-18]

From 1851 to 1919 ordinary probates went to the byfoged, herredsfoged or birk, and private (executor) probates were filed with the amt once settled. [S5 @2026-11-18]

**Privacy gate:** <!-- privacy-gate: request --> A probate can name heirs who may be living; unless it concerns only people known to be dead, answer the privacy gate in `SKILL.md` before you order it for the reading room.

For an ordinary probate before 1919, open the name register to the probate protocol first where one exists; it gives the protocol page. If the probate is not in the protocol, search the death register (dødsanmeldelsesprotokol), kept from about 1820. It records deaths with nothing to divide, surviving spouses who kept the estate undivided (uskiftet bo) and private probates. For a known private probate, go to the amt's series for probates or executors; some amter kept registers of their private probates. Most of this material is scanned on Arkivalieronline and reached through Søg i Samlingerne; the rest is ordered for the reading room. [S5 @2026-11-18]

From 1919 each court district's probate court (skifteret) handled probates. Start from the register to the case list where one exists; otherwise take the case number from the death register or the case list (skiftesagliste), then open the case documents, which are filed by that number. Executor estates were filed with the amt until about 1933 and with the probate court afterwards. Most of this material is ordered for the reading room, and Søg i Samlingerne links any scanned part. Probate records are closed for 75 years. [S5 @2026-11-18]

Copenhagen kept its probate protocols in a system of its own; use Rigsarkivet's separate guide to Copenhagen probates. [S5]

Some groups had their own probate authority:

- **Clergy, parish clerks, bell-ringers, schoolmasters and grammar-school teachers before 1807:** the deanery (provsti) as archive creator, series skift. Copenhagen's clergy went to the Copenhagen probate court after 1771, and the rest of the country's to the byfoged, herredsfoged or birkefoged after 1807. [S6 @2026-11-18]
- **Soldiers, officers and their families before 1864:** each regiment's auditor. Copenhagen's regiments went to the Copenhagen court (Hof- og Stadsret) in 1771, and units elsewhere to the civil courts in 1805, except Christiansø (until 1856) and the Schleswig and Holstein regiments (until 1864). Almost none of the regimental auditors' probates from before 1771 survive; for 1688–1771, look under the auditor of the Copenhagen garrison command, the auditor of Rendsborg fortress and the Generalauditøren. The military probate series are not digitised and are seen in the reading room. [S7 @2026-11-18]
- **Navy crews, their spouses and children, 1659–1771:** the Underadmiralitetsretten, whose oldest surviving probates are from 1659. Its probate books and their registers are scanned; its other series are seen in the reading room. After 1771 navy probates were handled like other citizens'. [S7 @2026-11-18]
- **Jewish citizens before 1814:** Det Mosaiske Troessamfund. Its probates survive from 1760, without finding aids, in four series kept in date order. [S8 @2026-11-18]

### Use a Gazette notice to locate a probate

**Privacy gate:** <!-- privacy-gate: third-party-tool --> A search of the National Gazette index sends the deceased's name to MyHeritage. Apply the third-party tool gate before sending the query and leave relatives' details out.

For a death from 1918 onward, search the deceased's name in MyHeritage's *Denmark, Deaths Published in National Gazette* index to Statstidende. Record the birth date or year, residence, death date, publication date and spouse as given. Use only the deceased's details in the search. [S11 @2026-11-22], [S12 @2026-11-22]

Use the publication date to locate and read the original notice. Record its issue and page or notice number when available. For a print issue, check the Statstidende holdings at Det Kgl. Bibliotek by that date. [S15 @2026-11-22]

Read a dødsbo notice (proklama) as a call for claims against the estate. [S13 @2026-11-22] When the notice names an estate contact or a bobestyrer, record the role as printed. [S11 @2026-11-22], [S14 @2026-11-22] A private estate's contact may be a relative. [S14 @2026-11-22] Use any named court or case reference to follow the probate route above. If the index is empty, continue with the death register or the relevant probate series. Danmarks Domstole gives boudlæg, a way to settle small estates, as an example where no proklama is published. [S13 @2026-11-22]

## Combine the sources into one household

1. Start from the census that shows the household, and note each person's age, birthplace and position in it. For census coverage and transcriptions, use [Denmark: go beyond the church books](scandinavian-patronymic-farm-name-record-recovery.md#denmark-go-beyond-the-church-books).
2. Take each birth, marriage and death to the register that its place, date and event type require, using the church-book, civil-marriage and South Jutland sections above. When an entry is missing, damaged or unreadable in one copy, read the other copy. Use confirmations to tie a child to a later adult, and burials to close each life. Follow the [cause-of-death route](#trace-a-historical-cause-of-death) when the death entry raises that question.
3. For a man between censuses, follow the levying rolls in [Denmark: go beyond the church books](scandinavian-patronymic-farm-name-record-recovery.md#denmark-go-beyond-the-church-books).
4. For each death, establish the deceased's status, residence and date, and route the probate with the section above. Use the [Gazette route](#use-a-gazette-notice-to-locate-a-probate) for a death or probate lead within the index period. Use the heirs named in the probate to confirm the children, their spouses and their places.
5. When a person leaves the parish, check the moves lists where the parish kept them, the next census's birthplace and the probate heirs' residences before you call the person lost.

## Close with a household packet

For each person, record the parish and its market town, herred or birk, amt and, for a tenant, the estate on each event date; each church-book entry with the book or copy (enesteministerialbog, hovedministerialbog or kontraministerialbog), year, page and event type; any civil-marriage or personregister entry; the probate authority, series and protocol page or case number; and each search that found nothing, with the copy, years and series searched. Record a search of withheld, blurred, unscanned or failed material as incomplete, and keep "nil" for a completed search of named material.
