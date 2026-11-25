---
id: "italian-stato-civile-parish-record-recovery"
title: "Recover an Italian ancestor in the Stato civile, parish books and conscription lists"
summary: "Send an Italian birth, marriage or death to the register legal in that place and year, then search conscription and population registers."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "ITALIAN-STATO-CIVILE-PARISH-RECORD-RECOVERY-01", "text": "Fix who registered the event before you choose a series. Use the event year and the place's ruler in that year, not today's region."}]
handoff: ["archival-image-coverage-verification", "catholic-parish-diocesan-record-recovery", "catholic-sacramental-cross-notations", "evidence-proof-judgment", "familysearch-practical-record-workflows", "historical-place-name-resolution"]
checked: "2026-11-04"
checked_basis: "opened 2026-11-04"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": ["request", "third-party-tool"], "contact": []}
router: {"section": "Records by country and region", "group": "Western and Northern Europe", "order": 174}
---

# Recover an Italian ancestor in the Stato civile, parish books and conscription lists

Use this recipe before you search for an Italian birth, marriage or death, or before you write that one does not exist. It sends each event to the register that was the legal record in that place and year: a pre-unification civil register, a parish book kept under Austrian law as the civil record, or the Italian Stato civile (civil registration). It prevents seven failures:

- dating Italian civil registration by one national year instead of by the state that ruled the place;
- logging Austrian-era years in Veneto, Trentino or Venezia Giulia as "no civil register" when the parish book was the civil record;
- reading a Portale Antenati name-search miss, or a missing year, as proof that no record exists;
- searching the previous generation from scratch before reading the marriage's supporting file;
- treating Antenati as either the only home or no home of parish registers;
- reading a man's absence from the service rolls as proof he was never in the conscription lists;
- sending a vital-act request to the comune's population office, or the reverse.

Link out for the shared steps:

- **Parish custody, diocesan copies, successor parishes and dispensation files:** [Catholic parish and diocesan record recovery](catholic-parish-diocesan-record-recovery.md).
- **Baptism–marriage margin notes between parishes:** [Catholic sacramental cross-notations](catholic-sacramental-cross-notations.md).
- **A town with several names or a frazione (hamlet) you cannot place:** [historical place-name resolution](historical-place-name-resolution.md).
- **Using a photographed index to browse an unindexed FamilySearch register:** [FamilySearch practical workflows](familysearch-practical-record-workflows.md), workflow 3.
- **Frame versus page, and scan availability versus index coverage:** [archival image coverage verification](archival-image-coverage-verification.md).
- **Identity rulings:** [evidence/proof judgment](evidence-proof-judgment.md).

## Contents

- Inputs to gather first
- 1\. Date the civil record by the state that ruled the place
- 2\. Search Antenati by its scope, not as a complete holding
- 3\. Read the marriage's supporting file before chasing the previous generation
- 4\. Route parish books by the historical diocese
- 5\. Search conscription lists and service rolls as two series
- 6\. Send each comune request to the right office
- Close with a register packet

## Inputs to gather first

Gather these before searching:

- the event type and approximate year
- the comune (municipality) and any frazione, each under every name form seen, with the record it came from
- the province today and the state that ruled the place in the event year
- for a man born after about 1840, his birth year (his classe di leva, conscription class)
- the parish and diocese, if any record names them
- any register, act number, Antenati image or FamilySearch image group already seen

## 1. Date the civil record by the state that ruled the place

Fix who registered the event before you choose a series. Use the event year and the place's ruler in that year, not today's region.

**Check the first Napoleonic register for the comune and event type.** Use the 27 March 1806 regulation as a search lead for comuni it covered in the Napoleonic Kingdom of Italy [S27], [S28]. For comuni in Piedmont's Po department, search the *Atti dello Stato Civile napoleonico* from 1803 [S29]. For comuni covered by the *Stato civile di Toscana*, start in 1808 [S30].

| Place and period | Legal register of the event |
| --- | --- |
| Mainland South (Kingdom of Naples), 1809 to 1814 | Civil register kept by the comune under Murat's decree of 29 October 1808, no. 198 [S27], [S31] |
| Mainland South (Kingdom of the Two Sicilies, roughly today's southern Italy), 1815 to 1865 | Civil register kept by the comune; the Napoleonic civil register stayed in use there after 1815 [S20] |
| Sicily, from 1820 | Civil registers kept by the comuni under the Codice per lo Regno delle Due Sicilie (code of the Two Sicilies) [S1], [S20] |
| Comuni then in the Kingdom of Italy, from 1 January 1866 | Stato civile of the comune under R.D. 15 November 1865 n. 2602 [S2], [S20] |
| Veneto and Trentino under Napoleonic rule (Venice from 16 June 1806, Trentino 1811–1815) | Civil register kept by the comune's civil-status office [S17], [S18], [S19] |
| Veneto under the Austrian registration system, to 31 August 1871 | Parish book; the parishes kept the civil-status registers under Austrian law [S3], [S17], [S18] |
| Veneto, from 1 September 1871 | Stato civile of the comune [S3] |
| Rome and its province, from 1 February 1871 | Stato civile of the comune; R.D. 27 November 1870 n. 6030 extended the 1865 decree to the province [S22] |
| Trentino from 1815, and Trieste and Gorizia, to 31 December 1923 (the Austrian system stayed in force after 1918) | Parish book; under Austrian law the parishes served as the civil-status office [S5], [S6], [S7]. In Trieste the other officially recognised faiths kept their own registers [S5] |
| Trentino, Trieste and Gorizia, from 1 January 1924 | Stato civile of the comune; R.D. 24 September 1923 n. 2013 extended the 1865 decree to the territories annexed after the First World War [S23], [S5], [S6] |

**Find where the earlier registers are now.** The Naples State Archive holds the civil registers of Naples and its province from 1809 to 1865 [S21 @2026-11-13]. Venice's Napoleonic registers were gathered into the State Archive [S17 @2026-11-13], and the Vicenza State Archive holds those of the Vicenza cantons [S18 @2026-11-13]. Trentino's Napoleonic registers survive at the Provincial Archive of Trento for nine comuni [S19 @2026-11-13]. A 1919 memo cited in its inventory says that many records of several Trentino comuni from that period had ended up in Innsbruck [S19 @2026-11-13]. In Vicenza province the Austrian-era parish books are searched in the parishes or the Diocese of Vicenza's historical archive [S18 @2026-11-13]. For Trieste before 1924, search the parish archives, the Trieste diocesan archive (copies of the parish registers of the Diocese of Trieste and Capodistria, 1833–1941) or the archives of the other recognised faiths [S5 @2026-11-13]. For Gorizia, the archbishop's curia archive holds copies of the birth, marriage and death registers from 1835 [S6 @2026-11-13]. Neither the Trieste nor the Gorizia State Archive holds its province's Stato civile series [S5 @2026-11-13], [S6 @2026-11-13]. The Trieste State Archive does hold the registers of the Italian consulate, which recorded Italian citizens living in Trieste in 1867–1915, and those of the Anglican community [S5 @2026-11-13].

- **Do not apply the 1865 decree to the whole country.** It covers only the comuni then in the Kingdom. The others came under the comune Stato civile later: Veneto in 1871 [S3]; Rome in 1871 [S22]; Trentino, Trieste and Gorizia in 1924 [S23], [S5], [S6].
- **Search a Napoleonic-period event in the municipal civil register, not the parish book.** In Venice that register ran from 16 June 1806; parish competence returned on 1 July 1815 for marriages and 1 January 1816 for births and deaths [S17]. For a place not in the table, take the Napoleonic dates from the local State Archive's guide.
- **Log a priest-as-officer year as a parish search, not a civil gap.** Where the parish kept the state civil-status register, the parish book or its state copy is the civil record. Its absence from a comune series is expected. Send the search to the parish or diocese (step 4).
- **For a former Austrian place outside Trentino, Trieste and Gorizia,** take the changeover year from the local State Archive's guide, not from this table.
- **For a place and period not in the table,** take the start of civil registration from the guide of the State Archive that holds the province's Stato civile.
- **Fix the place first.** A frazione moved between comuni or a comune between provinces changes the series. Resolve it with the place-name recipe.

## 2. Search Antenati by its scope, not as a complete holding

- **Use antenati.cultura.gov.it.**
- **Read Antenati as State Archive material, not as the whole record.** Its registers come from over 100 Archivi di Stato (State Archives) [S8 @2026-11-13]. Former Austrian areas differ: there the parish kept the registers before the changeover (step 1).
- **Know which original you are reading.** Each Stato civile register was kept in two originals. One stays at the comune; until 2001 the second went to the court (Tribunale) and later to the State Archive [S20 @2026-11-13]. Some State Archives never took in the courts' second originals: Alessandria's holds no Stato civile from 1866 for lack of space and sends readers to the courts or the comuni [S9 @2026-11-13].
- **Do not trust a name-search miss.** Cerca per nome (search by name) reaches only what has been indexed. A miss says nothing about the registers it did not reach.
- **Browse the indexes before the year volumes.** Use the indici decennali (ten-year indexes) and the annual index at the end of each register. Then open the act.
- **Classify a missing comune or year as a coverage gap.** Check, in order:
  - the comune's own register at its Ufficio dello Stato Civile (step 6);
  - the court's second original, where the State Archive never received it;
  - whether the series has been digitised and published at all;
  - FamilySearch, for the same comune and years.
- **Do not use an Antenati image as a certificate.** Antenati says the documents found on the portal have no legal value and cannot be used for legal or administrative purposes, in particular citizenship requests [S24 @2026-11-13]. For a certificate, ask the comune's Ufficio dello Stato Civile (step 6).
- **Cite each layer separately:** the State Archive, the series, the comune, the register and year, the act number, and the Antenati image. Keep the act number even when the image number changes.

### Recover a birth act

**Separate the birth from its declaration.** Take the birth date from the sentence that says when the child was born and record the declaration date separately. For an act under the 1865 Civil Code, inspect the margin for a waiver of presenting the newborn. Record any stated reason and leave the method of verification open when the act is silent. [S43], [S42]

**Follow a legible marriage annotation out of a damaged birth act.** Preserve the readable text and check the other register original. Use the annotation’s marriage comune, date, part and act number to locate the marriage act, then look for a pre-damage birth extract in its allegati. Match the extract to the birth comune, year, part and number and record its issuing office and date. [S32], [S37]

The author reports that a surviving marriage annotation on a water-damaged Gonzaga birth act led to a certified extract made before the damage [S38†].

**Check the parents’ comune of residence for a transcription.** If the birth was registered in a different comune, look in both registers and cite the birth entry and its transcription separately. Under the 1865 Civil Code, the office receiving the original declaration sent an authentic copy to the comune of domicile or residence. Under R.D. 1238/1939, look in Parte II, Serie A for the transcription of a birth that occurred and was registered during a temporary stay in another comune. [S43], [S32]

## 3. Read the marriage's supporting file before chasing the previous generation

- **Look for a supporting file beside the civil marriage act.** If the holding archive catalogues one for that comune and year, open it before you search the spouses' parents.
- **Treat every extract in it as a copy.** Carry each one back to the original act and cite both.
- **Record "not searched" for the supporting file when you skip it.** A marriage act alone does not close the search for the spouses' origins.

**Use the archive's names for the file when you search its catalogue.** Napoleonic civil registers often have allegati or processetti matrimoniali (marriage attachments) beside them, which can give the spouses' parents and their consent [S20 @2026-11-13]. For the Stato civile from 1866, look for the Allegati (attachments) series: it was kept in one original only, at the court, and later passed to the State Archive, so the comune does not have it [S20 @2026-11-13].

When an Italian record places fu before a parent’s name, read that parent as deceased by the date of the act. In a Piedmont notarial abstract of 10 January 1645, Martra fu Gioanni identifies Martra as the daughter of the late Gioanni [S26]. Use it to set a death-before bound and search the parent’s death separately; fu does not provide the death date, and its absence alone does not establish that a parent was alive. [S25], [S26]

### Find the ceremony and its transcriptions

**Read the part and series in the register for that year.** For years before 1940, use the printed title page to establish what its parts and series cover. Browse all of Parte II for a First World War proxy marriage when the index does not identify the series. Under R.D. 1238/1939, effective 1 January 1940, look in Parte II, Serie A for a religious marriage first transcribed in the celebrating comune and Serie B for its further transcription from another comune. Read the act in Serie C before classifying it because that series includes civil proxy celebrations and other acts, including marriages celebrated abroad. For a religious wedding, establish who appeared from the ceremony act. [S32], [S33], [S40], [S34]

**Follow a religious transcription back to the ceremony.** Record the parish act and the civil transcription with their own dates and numbers. For a late-December celebration, include the next year’s civil volume. Where the required publications and dispensation are both absent under Law 847/1929, check for the Article 12 impediment review and a ten-day Article 13 notice of the celebration before civil transcription. Keep this notice out of the pre-wedding banns chronology. [S35], [S32]

**Privacy gate:** <!-- privacy-gate: request --> A request for the second signed parish original sends the spouses’ names and marriage locator to the celebrating comune. Check access and clear the privacy gate in `SKILL.md` for anyone named who may be living before sending the request.

**Ask the celebrating comune for the second signed parish original.** For a marriage under Law 847/1929, trace the original sent for civil transcription when the parish copy cannot be consulted. Use the date and number of the transcription to identify the papers. [S35]

The author reports that in the Asiago case the registrar posted a notice after the religious wedding and before its civil transcription [S36†].

### Trace the banns and the mandate

**Search the civil pubblicazioni even when the wedding act is missing.** Record the request and posting dates separately, and keep parish banns separate from municipal postings. Use the marriage act or banns file to trace each place of publication, including a destination abroad named in a forwarding request. Distinguish the request from a certificate that posting took place. Check for a dispensation or opposition. Under R.D. 1238/1939, the banns papers moved to the marriage annexes once the marriage was celebrated. Use the celebration act to establish whether the wedding took place. [S32], [S35], [S34]

**Follow the record of consent to the parent’s act.** If the banns or marriage papers name a parent giving assent, record the name and relationship. Use a death certificate cited for the other parent to locate that parent’s death entry. [S32], [S37], [S42]

The author reports a surviving Asti banns act for a proposed wedding that the registrar stopped after learning of a prior marriage [S39†].

**Read the mandate’s operative words and the ceremony signatures.** A mandate to request banns (*per richiedere le pubblicazioni di matrimonio*) leads to the receiving comune’s incoming protocol and banns entry. For a ceremony by proxy, look for authority to contract the marriage (*per contrarre matrimonio*), the intended spouse, and the act’s statement and signature showing who appeared in whose place. The case documented in Conselice in 1942 has a military mandate for banns and the groom’s own signature at the later ceremony. Follow the filing, publication, celebration and transcription as separate events. [S34], [S33], [S32]

**Check a wartime mandate’s birth details against the municipal birth acts.** A parish marriage act can repeat the mandate’s incorrect birth date. Record each version and use the municipal birth entry to test the discrepancy. [S34], [S32]

**Use a First World War military mandate to find the service sheet.** Under Decree 903/1915, look in the marriage annexes for the principal’s rank and corps and, for rank-and-file soldiers, the matriculation number. Use those identifiers with the district and class to locate the foglio matricolare (step 5). Use the marriage act to date the ceremony. [S40], [S41], [S37]

**Search for a legitimation decree if a First World War mandate did not lead to a ceremony.** If the military principal’s death prevented the wedding, follow the mandate and any legitimation annotation on the child’s birth act to the royal decree and its case papers under Decree 1496/1915. The legitimation can be recorded even when the marriage was never celebrated. [S54], [S40], [S33]

### Use the attachments to recover earlier records

**Match the separately bound attachments to the act.** Use the year and act number to find the cover, then confirm the spouses and compare the papers with the cover list or count when present. When the birth predates local civil registration, look for a parish baptismal certificate in the processetti. For each parish or civil extract, record its issuance date separately from the events it records. Use the issuing comune or parish and the cited register, year, part, folio or act number to find the entry it copies. [S37], [S32]

The author reports that an 1841 Piscopio marriage packet preserved a parish extract of a baptism from 1796, before local civil registration [S52†].

**Search forward from a child’s birth when the parents’ marriage is missing.** Read any later recognition or legitimation annotation and follow it to the marriage entry. If the marriage act names children, use the recognition clause and the birth records in its annexes to find their original birth entries. Put their recorded birth dates and places in sequence to identify other comuni to search. [S32], [S37]

The author reports tracing a family across comuni through children’s birth acts assembled for a later marriage in Prignano [S53†].

## 4. Route parish books by the historical diocese

- **Before civil registration and in its gaps, search the parish books.** In the province of Alessandria, the State Archive's guide says parish archives, including birth, marriage and death registers and stati delle anime (status animarum, household-by-household parish censuses), generally remain at the parish, with some gathered into diocesan archives [S9 @2026-11-16]. The Barga inventory, partially read on pp. 6 and 73, says the Rituale Romanum of 1614 required systematic compilation of stati delle anime and warns that relationships and ages are not always recorded and actual regularity at Barga varied over time [S10 @2026-11-16].
- **Find the holder through BeWeB** (beweb.chiesacattolica.it), the Italian bishops' conference (CEI) catalogue of ecclesiastical archives. It lists only archives registered with it and gives their contact details. It does not do research; you arrange access with the archive itself [S11 @2026-11-16].
- **Check Antenati's local coverage of parish books.** The Alessandria State Archive reports that Antenati publishes the 1838–1865 parish registers of the Comune di Alessandria and its outlying villages (sobborghi); this coverage does not extend to the rest of the province [S9 @2026-11-16]. For another comune in the province, check the parish, diocesan and municipal historical archives [S9 @2026-11-16]. For years before 1804 in the province of Alessandria, the State Archive's guide directs researchers only to the territorial parish, or to the curia if the parish archive was deposited in the diocesan archive [S9 @2026-11-16].
- **For the diocese responsible for the parish in the event year**, a priest's statement that books burned, diocesan copies, merged parishes and dispensations, follow the Catholic parish recipe.

**Check the volume’s transfer and access dates.** Verify that the register has entered the historical archive before arranging direct consultation [S59 @2026-11-23]. Apply the local diocesan rule. In Udine, count 70 years from the last act or document entered in the volume [S60 @2026-11-23]. Log a closed volume as restricted access.

**Privacy gate:** <!-- privacy-gate: request --> A request for an individual marriage certificate or extract sends the spouses’ names, the marriage parish and date, and any known act number to the issuing parish or diocesan office. Clear the privacy gate in `SKILL.md` for anyone named who may be living before sending.

**Check eligibility for an individual marriage certificate or extract.** When direct consultation is closed, an individual request is the next route to try according to the community guide [S61† @2026-11-23]. Check the issuing parish or diocesan office’s rules for your purpose before sending a request. Identify the act by the spouses’ names, the marriage parish and date, and the act number if known [S59 @2026-11-23], [S62 @2026-11-23].

**Privacy gate:** <!-- privacy-gate: third-party-tool --> A parish-index query sends names and any dates, places or relatives entered to MyHeritage. Clear the privacy gate in `SKILL.md` before entering data about anyone who may be living.

**Search the relevant MyHeritage parish index.** For the Diocese of Trento, use Catholic Church Baptisms (1548–1937) for birth and baptism details and parents [S45 @2026-11-22]. Use Catholic Church Deaths (1567–1911) for death place and date and any parents or spouse recorded [S46 @2026-11-22]. Use the death collection’s own dates when the roundup table gives the baptism range [S44 @2026-11-22].

**For Calabria, choose the index by event.** In Parish Births and Baptisms (1591–1963), note the baptism place and parents, and godparents where listed [S48 @2026-11-22], [S47 @2026-11-22]. In Parish Deaths and Burials (1593–1969), record death and burial separately and note parents or spouse where listed [S49 @2026-11-22], [S47 @2026-11-22]. For either region, use a hit to locate the parish book. After a miss, check the holder’s catalogue for the parish and year.

## 5. Search conscription lists and service rolls as two series

**Privacy gate:** <!-- privacy-gate: request --> A request to a Centro documentale for a service sheet (the last step in this list) sends a man's name and birth year, and a man born in the 20th century may still be living; answer the privacy gate in `SKILL.md` before you send it.

- **Search the liste di leva (conscription lists) by comune and classe.** The comuni compiled them, with each man's birth and residence details [S12 @2026-11-13], [S13 @2026-11-13]. Look in the comune of birth as well as the comune of residence at call-up [S9 @2026-11-13], [S12 @2026-11-13]. The classe is the year of birth [S12 @2026-11-13].
- **Search the ruoli matricolari (service rolls) by distretto militare and classe.** The distretto militare (military district) of the man's residence at age 20 called him up and kept his roll [S12 @2026-11-13]. A volunteer can sit in an earlier class and a deferred man in a later one, so search at least three classes either side before you log a miss [S12 @2026-11-13].
- **Do not read a missing service roll as disproof.** Not every man in the liste has a ruolo or foglio matricolare (service sheet) [S13 @2026-11-13]. A man found in the liste and missing from the ruoli is still the man in the liste.
- **Look for both series in a State Archive.** The Modena and Bergamo State Archives hold and describe them [S12 @2026-11-13], [S13 @2026-11-13]. Confirm which State Archive holds the man's district before you log a miss.
- **Ask the Army's Centro documentale for a service sheet not yet transferred.** Army service sheets that have not reached the State Archive are with the Centri documentali (former Distretti Militari); the Navy, Air Force and Carabinieri keep theirs in other offices [S24 @2026-11-13].

**Read the service roll for civilian occupation and residence changes.** Record the occupation with its entry date or service stage. Check later annotations for changes of residence, including a move abroad. Keep the first residence, the military district and the later residence as separate leads. [S50], [S51]

**Check landholding separately from the recorded occupation.** In a civil act or service roll, read *agricoltore* as work in agriculture, which can include owners, tenants and hired workers [S50], [S55]. Read *bracciante* in an agricultural entry as a clue to manual wage work and leave landownership open [S56]. Use the locality and date to look for the person in the historical *catasto*’s holder index and for a farm lease or sharecropping contract. Record the role each document gives the person and leave ownership unresolved if the only evidence is an occupation or a missed index entry [S57], [S58].

## 6. Send each comune request to the right office

**Privacy gate:** <!-- privacy-gate: request --> A request to a comune office can name, or ask about, people who may be living: a recent vital act names its parties, and a family sheet lists every member of a household and their changes of residence. Until the privacy gate in `SKILL.md` is answered for each such person, the request stays an unsent draft, even when the person you are tracing is dead. The office's rule on who may order a record is not that person's permission. Never ask the anagrafe where a living person lives now.

- **Ask the Ufficio dello Stato Civile for a vital act.** Every comune has one [S14 @2026-11-13]. It keeps the birth, marriage, death and citizenship registers [S15 @2026-11-13].
- **Ask the Ufficio Anagrafe for a household or a move.** The anagrafe holds the registro di popolazione (population register): fogli di famiglia (family sheets) listing each household's members [S16 @2026-11-13], and records of each change of residence [S15 @2026-11-13].
- **Date the population register by the place.** It was set up by R.D. 31 December 1864 n. 2105, and its first family sheets describe each household as of 1 January 1865 [S16 @2026-11-13]. In Frosinone, in the part of Lazio that was Papal until 1870, the register followed the law of 20 June 1871 n. 297 [S15 @2026-11-13]. For a place annexed later, take the dates from the local archive's guide: Trieste's family sheets begin in 1857, under the imperial ordinance of 23 March 1857, and are kept by the Comune di Trieste [S5 @2026-11-13].
- **Treat a request to the wrong office as unanswered, not negative.** Re-send it to the right office before you log a miss.

## Close with a register packet

Return:

- **Jurisdiction row:** the comune and frazione under each name form, the state in the event year, the register type from step 1, and the diocese in that year.
- **Series rows:** for each event, the series (civil register, marriage supporting file, parish book, stato delle anime, liste di leva, ruolo matricolare, population register), the holder, the locator down to act number and image, and the status: searched, found, not found or not online.
- **Gaps:** coverage gaps on Antenati with their cause, unsearched marriage supporting files, and parish books not yet located.
- **Extract chain:** every extract or copy found in a marriage supporting file, with the original act it points to and whether that act has been opened.
- **Name register:** every literal form of each name with its record and year.

The model assembles this packet. The researcher decides identity and kinship.
