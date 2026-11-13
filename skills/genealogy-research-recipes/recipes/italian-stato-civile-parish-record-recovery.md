---
id: "italian-stato-civile-parish-record-recovery"
title: "Recover an Italian ancestor in the Stato civile, parish books and conscription lists"
summary: "Send an Italian birth, marriage or death to the register that was the legal record in that place and year (a Napoleonic municipal register, an Austrian-era parish book or the comune's Stato civile), then search conscription lists and the population register as separate series."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "ITALIAN-STATO-CIVILE-PARISH-RECORD-RECOVERY-01", "text": "Fix who registered the event before you choose a series. Use the event year and the place's ruler in that year, not today's region."}]
handoff: ["archival-image-coverage-verification", "catholic-parish-diocesan-record-recovery", "catholic-sacramental-cross-notations", "evidence-proof-judgment", "familysearch-practical-record-workflows", "historical-place-name-resolution"]
checked: "2026-11-04"
checked_basis: "opened 2026-11-04"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": ["request"], "contact": []}
router: {"tier": "pointer", "group": "Country record routing", "order": 1058}
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

| Place and period | Legal register of the event |
| --- | --- |
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

## 3. Read the marriage's supporting file before chasing the previous generation

- **Look for a supporting file beside the civil marriage act.** If the holding archive catalogues one for that comune and year, open it before you search the spouses' parents.
- **Treat every extract in it as a copy.** Carry each one back to the original act and cite both.
- **Record "not searched" for the supporting file when you skip it.** A marriage act alone does not close the search for the spouses' origins.

**Use the archive's names for the file when you search its catalogue.** Napoleonic civil registers often have allegati or processetti matrimoniali (marriage attachments) beside them, which can give the spouses' parents and their consent [S20 @2026-11-13]. For the Stato civile from 1866, look for the Allegati (attachments) series: it was kept in one original only, at the court, and later passed to the State Archive, so the comune does not have it [S20 @2026-11-13].

## 4. Route parish books by the historical diocese

- **Before civil registration and in its gaps, search the parish books.** Baptisms, marriages, burials and the stato delle anime (status animarum, a household-by-household parish census) are normally kept by the parish or gathered into the diocesan archive [S9]. Parish priests had to keep stati delle anime regularly after the Rituale Romanum of 1614, household by household with ages [S10].
- **Find the holder through BeWeB** (beweb.chiesacattolica.it), the Italian bishops' conference (CEI) catalogue of ecclesiastical archives. It lists only archives registered with it and gives their contact details. It does not do research; you arrange access with the archive itself [S11].
- **Check Antenati for parish books only in a State Archive's gap years.** Where a State Archive holds parish-kept registers that served as the civil record, check Antenati for those years [S9]. Alessandria's parish registers of 1838–1865 are an example [S9]. Expect most parish books, especially before 1800, only at the parish or diocese [S9].
- **For the diocese in the event year** (Italian dioceses do not follow modern provinces), a priest's statement that books burned, diocesan copies, merged parishes and dispensations, follow the Catholic parish recipe.

## 5. Search conscription lists and service rolls as two series

**Privacy gate:** <!-- privacy-gate: request --> A request to a Centro documentale for a service sheet (the last step in this list) sends a man's name and birth year, and a man born in the 20th century may still be living; answer the privacy gate in `SKILL.md` before you send it.

- **Search the liste di leva (conscription lists) by comune and classe.** The comuni compiled them, with each man's birth and residence details [S12 @2026-11-13], [S13 @2026-11-13]. Look in the comune of birth as well as the comune of residence at call-up [S9 @2026-11-13], [S12 @2026-11-13]. The classe is the year of birth [S12 @2026-11-13].
- **Search the ruoli matricolari (service rolls) by distretto militare and classe.** The distretto militare (military district) of the man's residence at age 20 called him up and kept his roll [S12 @2026-11-13]. A volunteer can sit in an earlier class and a deferred man in a later one, so search at least three classes either side before you log a miss [S12 @2026-11-13].
- **Do not read a missing service roll as disproof.** Not every man in the liste has a ruolo or foglio matricolare (service sheet) [S13 @2026-11-13]. A man found in the liste and missing from the ruoli is still the man in the liste.
- **Look for both series in a State Archive.** The Modena and Bergamo State Archives hold and describe them [S12 @2026-11-13], [S13 @2026-11-13]. Confirm which State Archive holds the man's district before you log a miss.
- **Ask the Army's Centro documentale for a service sheet not yet transferred.** Army service sheets that have not reached the State Archive are with the Centri documentali (former Distretti Militari); the Navy, Air Force and Carabinieri keep theirs in other offices [S24 @2026-11-13].

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
