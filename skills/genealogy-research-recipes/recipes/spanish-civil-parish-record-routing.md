---
id: "spanish-civil-parish-record-routing"
title: "Route a Spanish or Andorran record to the archive that holds it on the event date"
summary: "Route a Spanish or Andorran vital, padrón, notarial, military or Civil War record to the body that holds it on the event date."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "SPANISH-CIVIL-PARISH-RECORD-ROUTING-01", "text": "**Expect the national Registro Civil only from 1 January 1871.**"}]
handoff: ["catholic-parish-diocesan-record-recovery", "city-directory-observation-workflow", "evidence-proof-judgment", "hispanic-catholic-register-recovery", "historical-place-name-resolution", "school-university-record-recovery", "tax-roll-observation-workflow", "usa-immigration-search-recovery"]
checked: "2026-11-04"
checked_basis: "opened 2026-11-04"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": ["request", "third-party-tool"], "contact": []}
router: {"section": "Records by country and region", "group": "Western and Northern Europe", "order": 180}
---

# Route a Spanish or Andorran record to the archive that holds it on the event date

Use this recipe before you search for, request or write off a Spanish or Andorran record: a birth, marriage or death, a padrón (municipal resident list), a tax or Catastro entry, a notarial deed, a pedigree proof, a military or student file, or a Civil War and repression file. It sends each record to the body that holds it for that date and region. It prevents nine failures: expecting the Registro Civil (civil registry) to cover an event before 1871 and missing the 1841–1870 municipal registers; inferring the diocese from the modern province; calling a parish book lost without the diocesan survival list and duplicates; searching only Andorra for a family said to be "from Andorra"; searching the Catastro de Ensenada outside the Crown of Castile, or expecting its household books on PARES; searching notarial protocols by client name, or at the wrong custodian for their age; stopping a pedigree at the Inquisition files; requesting a post-1939 court-martial file without first finding the military court that owns it; and reading an index miss or a town hall's "not held" as proof that a record is lost.

Link out for the shared steps:

- **Reading a baptism field by field, grandparents, the two-surname and joining y/e search lanes, and the diocesan copy:** [Hispanic Catholic register recovery](hispanic-catholic-register-recovery.md), steps 2, 3 and 7.
- **Parish candidates, the widening order, originals against copies, and dispensation files:** [Catholic parish and diocesan record recovery](catholic-parish-diocesan-record-recovery.md).
- **A village you cannot place, or one with several names:** [historical place-name resolution](historical-place-name-resolution.md).
- **Directory entries as address evidence:** [city-directory observation workflow](city-directory-observation-workflow.md).
- **Yearly tax lists as a residence series:** [tax-roll observation workflow](tax-roll-observation-workflow.md).
- **Student files beyond the custody checks here:** [school and university record recovery](school-university-record-recovery.md).
- **The arrival-side search for a U.S. immigrant:** [U.S. immigration search recovery](usa-immigration-search-recovery.md).
- **Identity rulings:** [evidence/proof judgment](evidence-proof-judgment.md).

## Contents

- Inputs to gather first
- 1\. Fix the civil-registration period
- 2\. Find the diocese that held the parish on the event date
- 3\. Check survival and duplicates before calling a book lost
- 4\. For Andorra, ask the holders and widen to the Catalan valleys
- 5\. Find residence and household evidence: padrones, electoral rolls and tax lists
- 6\. Search the Catastro de Ensenada only where it was taken
- 7\. Search notarial protocols by notary, not by client
- 8\. Widen beyond the earliest parish book: pedigree proofs and university files
- 9\. Request military files and read the gazettes
- 10\. Route Civil War and repression files by holder
- 11\. Search the Spanish departure side for an emigrant
- Close with a routing packet

## Inputs to gather first

Gather these before searching:

- the event or record type and the approximate year
- the town, its municipality and its province, each with the record it came from
- the parish, if known, and the diocese you think held it
- every surname form seen, with and without the joining y
- any address, trade or office the person held (teacher, notary's client, officer, emigrant)
- any archive signature, PARES reference or diocesan index hit already seen

## 1. Fix the civil-registration period

**Privacy gate:** <!-- privacy-gate: request --> A certificación literal of a civil entry from 1871 onward can name people who are still living; answer the privacy gate in `SKILL.md` before you order it.

- **Expect the national Registro Civil only from 1 January 1871.** It rests on the Ley provisional del Registro Civil of 17 June 1870 [S1], [S2]. Before that date, use the parish books and the municipal registers below.
- **For 1841–1870, look for a municipal civil register as well as the parish books.** A decree of 24 January 1841 ordered civil registers in the provincial capitals, the district seats (cabezas de partido) and the towns of more than 500 vecinos (households) [S3]. Read the municipal archive's inventory for a surviving civil-register series.
- **Do not expect a register for every town.** Smaller towns were outside the 1841 decree [S3]. Read the inventory before you request a volume, and record a missing series as a coverage gap.
- **For an event from 1871, order the certificación literal (literal certificate).** It is the full copy of the entry, not the extract. Extract the fields from it with the Hispanic register recipe.

**Andorra had no civil register before 1997.** The Llei del Registre Civil, published on 14 August 1996, created the Registre Civil del Principat d'Andorra and came into force on publication [S40]. It registers events from the 180th day after that, in February 1997; for earlier events the church registers are the record, and their keepers may certify entries from them [S40]. Search an earlier Andorran event in the parish books (step 4).

Start a civil search from the recorded event place, but do not assume it always equals the registry’s municipality. The Ministry’s explanatory page also describes exceptions, including certain births registered at the parents’ domicile. Keep the physical event place, parents’ residence and registration office as separate fields, and check the applicable period’s rule when they differ. Only a transcript excerpt of the cited community video was inspected. [S46], [S47]

Decode a numbered section in a historical civil-register locator before choosing a book. The Ministry’s explanatory page maps section I to births and general matters, II to marriages, III to deaths, and IV to guardianship and legal representation. Confirm the actual volume title and period; this key to legacy section references does not mean that every present registry or digital catalogue retains the same arrangement. Only a transcript excerpt of the cited community video was inspected. [S46], [S48]

Inspect the margins of the marriage entry as well as its main text. The SSA’s Spain procedure identifies divorce as a marginal note on the marriage it terminated. Record the annotation’s own wording and date; do not turn that one supported annotation type into a promise that every later event or identity document will appear in every margin. Only a transcript excerpt of the cited community video was inspected. [S46], [S49]

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Submitting a municipal vital-record search sends the names and any event details you enter about the subject or relatives to MyHeritage. Answer the privacy gate in `SKILL.md` before submitting the search.

**Search MyHeritage's municipal birth and death indexes by province and event.** Start with Córdoba births or deaths (1509–1947) [S55 @2026-11-22], [S56 @2026-11-22], [S58 @2026-11-22], Málaga births or deaths (1760–1956) [S59 @2026-11-22], [S60 @2026-11-22], Sevilla births (1293–1966) [S61 @2026-11-22], or Asturias births (1470–1897) or deaths [S62 @2026-11-22], [S63 @2026-11-22], [S64 @2026-11-22]. In births, look for the date and place and the parents. In deaths, log the place and the date precision supplied, then look for birth year, age at death, parents and spouse. Use the catalogue spans to pick an index, and check the municipality, record type and year in the underlying series. Open the Asturias register image when the result includes one. For a Córdoba index miss, browse the municipality and series in FamilySearch's broader *Spain, Córdoba, Municipal Records* collection [S57 @2026-11-22].

**Use a historical wet-nurse advertisement to narrow a birth-register search.** If it gives the duration of nursing, count back from the issue date to estimate a birth window. Search the advertised locality and estimated month. Use the named contact to identify candidate families and prioritize entries naming a documented daughter of that contact as the mother. Keep the date window and family connection as leads until the records establish them [S69].

## 2. Find the diocese that held the parish on the event date

**Privacy gate:** <!-- privacy-gate: request --> A letter to a diocesan archive with names, parish and date (the last step in this list) can concern people who may be living; answer the privacy gate in `SKILL.md` before you send it.

- **Do not infer the diocese from the modern province.** Spanish dioceses do not follow provincial lines, and parishes have moved between dioceses. Fix the diocese for the event date before you write.
- **Examples:** on 19 September 1956 a decree moved a list of parishes in the Omaña, La Lomba and Páramo areas of León province from the Diocese of Astorga to the Diocese of León, and ordered the curia's papers on them sent to León [S7]. The Cantabrian municipality of Valle de Villaverde (Trucíos) belongs to the Diocese of Bilbao, while the Valle de Mena, in Burgos province, belongs to the Diocese of Santander [S8].
- **In the Basque Country, ask the diocesan archive for the parish books.** The diocesan archives of Bilbao, San Sebastián and Vitoria hold the parish books and their digitized images [S4].
- **Search the Archivo Histórico de Euskadi's Registros Sacramentales index for a Basque event.** It indexes baptisms, marriages and deaths of all the historical Basque parishes, about 1490–1900, under a cooperation programme with the three dioceses [S4], [S5]. The portal shows index entries only. Each entry is linked to the digitized image held by the owning diocesan archive (for Bizkaia, the Archivo Histórico Eclesiástico de Bizkaia), and copies come from that archive [S4].
- **Test an index miss in the book.** Use the rules in [Catholic parish and diocesan record recovery](catholic-parish-diocesan-record-recovery.md), step 4, and the surname lanes in [Hispanic Catholic register recovery](hispanic-catholic-register-recovery.md), step 3.
- **Where a diocese has no online index, write to its archive.** Give the parish, the record type, the approximate date and the names.

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Submitting this search sends the historical spouses' names and any marriage date or parents' names you enter to MyHeritage. Answer the privacy gate in `SKILL.md` before you submit it.

**Search MyHeritage's Spain, Barcelona Marriages, 1847-1904 index** for a Catholic marriage in Barcelona in that period [S50 @2026-11-20], [S51 @2026-11-20]. Search by the spouses' names and record the indexed date, place and parents' names when present [S51 @2026-11-20]. Treat a hit as a lead to the marriage book. If the search misses, check the parish and year in the Arxiu Diocesà de Barcelona's *Arxius Parroquials* catalogue before drawing a conclusion [S52 @2026-11-20].

**At the Archivos Eclesiásticos de Mérida-Badajoz, choose the fonds by record creator.** The archive distinguishes the cathedral chapter, diocesan, deposited parish, Order of Alcántara and Order of Santiago fonds [S72 @2026-11-22], [S73 @2026-11-22]. Within the parish deposits, identify the *arciprestazgo* and then the individual parish [S74 @2026-11-22]. Look under *Registros sacramentales* for sacramental books and under *Varios* for material such as *libros de fábrica*, *libros becerro* and chaplaincies [S72 @2026-11-22]. Check the current deposit before ruling out the parish series, because transfers recur [S74 @2026-11-22], [S76 @2026-11-22].

**Before an on-site lookup, check the archive's current address.** Its contact page lists C/ Obispo San Juan de Rivera, 13, Badajoz [S87 @2026-11-23].

**For early Badajoz diocesan papers missing from the diocesan series, check the cathedral's *Fondo Capitular*.** Use it as a second route for papers from before separate diocesan filing took shape in the sixteenth century [S73 @2026-11-23], [S76 @2026-11-23]. For episcopal visitations, decrees or correspondence, look under *1.2.3. Episcopal* in the chapter's classification [S90 @2026-11-23].

**If the historical district is uncertain, search the diocesan *Expedientes de demarcaciones y límites arciprestales*.** Find the file that added or removed the locality, read the effective date and use the district then in force to choose the parish series. The Mérida–Badajoz classification study identifies this series in the diocesan fonds [S70].

**For a record from a military order's ecclesiastical jurisdiction, use its own inventory.** Search the Santiago inventory for the Priorato de San Marcos de León and its Mérida and Llerena provisoratos [S88 @2026-11-23], or the Alcántara inventory for the prioratos of Magacela and Zalamea [S89 @2026-11-23]. Use the dates printed for the series even when they extend past the nineteenth-century end of the order's jurisdiction [S76 @2026-11-23], [S89 @2026-11-23].

**For a parish represented in the Order of Alcántara fonds, check that fonds as well as the ordinary parish inventory.** The Ibersid abstract describes the order's holdings [S77 @2026-11-22]. In the archive's classification, follow *2. Administración → 2.2. Parroquias → 2.2.1. Registros sacramentales* for baptism, communion, marriage, ordination and death files [S78 @2026-11-22].

**When a Mérida–Badajoz marriage is the lead to a kinship question, read the marriage entry for affinity or consanguinity.** Record the impediment and its stated degree when present, then use those details to look for the dispensation with the Catholic parish and diocesan recovery recipe [S72].

## 3. Check survival and duplicates before calling a book lost

- **Read the diocesan survival list for the parish before you request a book or call it lost.** Urgell, for example, publishes a per-parish spreadsheet with the first and last years of each surviving sacramental book [S6].
- **Check whether the diocesan archive keeps duplicates.** A book missing in the parish may survive there.
- **Record originals and duplicates as separate holdings,** with the rules in [Catholic parish and diocesan record recovery](catholic-parish-diocesan-record-recovery.md), step 3.

**Check the diocesan inventory by parish and sacrament for Castilian events before 1550.** The claimed 1550 start for Castilian church records [S53] would miss the 1494 Nofuentes baptism entry documented by the Archdiocese of Burgos [S54].

**For an Alburquerque death in 1833–1855, check both parish inventories.** The Archivos Eclesiásticos de Mérida-Badajoz lists San Mateo and Santa María separately [S75 @2026-11-22]. For Santa María del Mercado, use books 14 (1827–1841), 15 (1841–1851) and 16 (1851–1856). For San Mateo Apóstol, use books 15 (1832–1848), 16 (1848–1851) and 17 (1851–1856) [S72 @2026-11-22]. Check both adjoining books when the year appears in both spans.

**For a gap in the Badajoz ecclesiastical holdings, distinguish an unlisted book, a documented loss and an unreadable survivor.** The archive history records losses after an early nineteenth-century assault and deterioration while protecting documents around the Civil War [S72], [S73]. Assign either cause to a particular book only if the inventory or a record of the damage identifies it.

**For a missing Badajoz episcopal tribunal file, check the 22 December 1729 report in *Fondo Diocesano*, legajo 16, no. 400, fols. 38v–39v.** Test whether the file could have been among the papers affected by the 1705 explosion or, for lawsuits that went to the new archive, by damp after the move [S73], [S76]. Record these as possible losses unless a source identifies the file itself.

## 4. For Andorra, ask the holders and widen to the Catalan valleys

- **Ask the parish and the Arxiu Nacional d'Andorra [S42 @2026-11-13] where the parish books can be consulted.** Record which holder answered and what form (original or copy) they hold.
- **Check the Urgell diocesan spreadsheet for the parish** [S6 @2026-11-13], and record whether it is listed. It lists the Andorran parishes with books of 1863–1870 only [S6 @2026-11-13]. A year missing from it is not a lost book. The Arxiu Nacional d'Andorra's 1993 inventory of the La Massana parish archive (only the opening section was read) says that Urgell's 1972 transfer of parish books over 100 years old to the diocesan archive left out the Andorran parishes, because their books served as the civil register, and that the Andorran archives service took on the description, restoration and microfilming of the parish archives in 1980 [S43 @2026-11-13].
- **Widen a family "from Andorra" to the neighbouring Catalan valleys.** Search the Pallars and Alt Urgell parishes and the Catalan archives as well. Add accent and B/V spelling lanes.

## 5. Find residence and household evidence: padrones, electoral rolls and tax lists

- **Check which body holds a town's old padrones before you write to the town hall.** Bilbao's municipal fonds for 1300–1936 are at the Archivo Histórico Foral de Bizkaia, not in the municipal archive [S9]. Look for older Bilbao padrones there. A "not held" reply from a town hall does not mean the padrón is lost; ask where its older fonds were deposited.
- **Find the address first for a padrón without a name index.** If the padrón is arranged by street or district with no name index, take the address from a directory, an electoral roll, a civil act or an obituary, then read the padrón. Never report someone "not in the padrón" on the strength of a name search the source cannot support.
- **Use printed electoral rolls (censos electorales) between padrones and as address finders.** Read the column headings of the edition in hand before relying on any field. Expect women on the 1924 and 1928 rolls, none on those of 1923, 1930 and 1931, and women again from the 1932 renewal [S11]. Online examples: Palencia, 1890–1955, on the Diputación de Palencia website [S10]; Burgos (1890–1955) and Valladolid (1898) in the Biblioteca Digital de Castilla y León [S12]; Bizkaia (1895) in the Diputación Foral's Liburutegi Biltegi [S13].
- **In Catalonia, use the provincial Treasury delegation fonds (Delegació d'Hisenda) for residence and property.** They are catalogued in Arxius en Línia. The Arxiu Històric de Girona, for example, holds the padrons and llistes cobratòries (yearly tax lists) of the urban property tax for almost every Girona municipality, 1909–1994, and the rural amillaraments (assessment books) of 1941–1958 [S14]. Expect to consult the volumes at the archive or ask by email; the catalogue is online, the volumes may not be [S14].

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Submitting a municipal census search sends the household members' names and any residence or year details entered to MyHeritage. Answer the privacy gate in `SKILL.md` before submitting it.

**Search MyHeritage's municipal census collections by province and year.** The catalogue lists Girona (1836–1950) [S65 @2026-11-22], [S68 @2026-11-22], Alicante (1846–1920) and Almería (1831–1898) [S66 @2026-11-22], [S68 @2026-11-22], and Huelva (1889–1920), Jaén (1857–1920), La Coruña (1871–1950), Lugo (1901–1920), Murcia (1889–1924), Segovia (1881–1920) and Valencia (1857–1935) [S67 @2026-11-22], [S68 @2026-11-22]. Open the household image to read the address, names, ages or birth years, and each stated relationship to the head. Record the relationship as unstated if the column is missing or blank. For a miss, check the municipality and year in the archive's padrón inventory.

**Use ecclesiastical household lists alongside the municipal padrón.** At Mérida–Badajoz, look in the diocesan and parish fonds for *padrones parroquiales* and *registros de censos* [S70 @2026-11-22], [S71 @2026-11-22], [S74 @2026-11-22]. Browse by street and compare the same households across dated lists. Transcribe names, ages and stated relationships from the padrón. In the church census, record the age band, marital status and any occupation stated. Compare entries with the municipal list to test the household's parish affiliation [S76 @2026-11-22].

## 6. Search the Catastro de Ensenada only where it was taken

- **Search it only for the Crown of Castile, and not for the Canary Islands, the Basque provinces or Navarre.** The survey began with the royal decree of 10 October 1749 and was almost finished by 1756 [S15 @2026-11-13], [S17 @2026-11-13]. It covered the localities of the Crown of Castile [S15 @2026-11-13], except the Canary Islands and the exempt territories, the Basque Country and Navarre [S41 @2026-11-13].
- **Expect only the town-level answers on PARES.** The PARES Catastro portal publishes the Simancas copy of the Respuestas Generales (the town-level answers) [S15 @2026-11-13], [S16 @2026-11-13].
- **Look for the household-level books in the Archivo Histórico Provincial.** The original catastro documentation is kept in the Archivos Históricos Provinciales, and some towns kept copies [S16 @2026-11-13]. Some has been lost: most of the Asturian catastro burned with the Oviedo Treasury delegation in 1934 [S16 @2026-11-13].
- **A miss in the Respuestas Generales says nothing about a household.** They do not list households.

## 7. Search notarial protocols by notary, not by client

- **Find the notaries who worked in the district in that year, then search their protocols.** A protocol is one notary's ordered collection of deeds for one year [S18], and its index lists that notary's grantors only [S18], [S21]. Find the notary before you look for the name.
- **Route by the protocol's age:**

  | Age of the protocol | Holder | Access |
  | --- | --- | --- |
  | Under 5 years | the notary who now holds that notaría (notary's office), as keeper of its protocols [S18 @2026-11-13] | copies from that notary, for a party to the deed or an applicant with a legitimate interest [S18 @2026-11-13] |
  | 5 to 100 years | the Archivo General de Protocolos of the regional Colegio Notarial [S18 @2026-11-13] | copies from the notary in charge of the archive, for applicants who prove a legitimate interest [S18 @2026-11-13], [S19 @2026-11-13] |
  | Over 100 years | the historical section: a Colegio's historical protocol archive or the Archivo Histórico Provincial [S20 @2026-11-13], [S21 @2026-11-13] | archive consultation rules; certified copies only from the notary-archivist [S20 @2026-11-13], [S21 @2026-11-13] |

- **Expect older guides to give 25 years.** From 1862 until 8 November 2023 the law sent protocols to the general archive once they were more than 25 years old [S45 @2026-11-13]. Since 9 November 2023 the Colegio's archive keeps protocols at least five years old, and electronic files reach it after 25 years [S18 @2026-11-13]. A Colegio's own page can still give the old line: the Asturias Colegio says its archive holds the Oviedo district's protocols over 25 years old [S19 @2026-11-13].
- **Transfer dates vary, so check the archive's date range** before you write to it.

## 8. Widen beyond the earliest parish book: pedigree proofs and university files

- **Do not stop at the Inquisition for a limpieza de sangre (purity of blood) proof.** The military orders, cathedral chapters, colegios mayores (residential colleges) and many offices also required proofs [S24], [S25]. The Inquisition files are in the Archivo Histórico Nacional (AHN) and searchable on PARES [S22]. Search the AHN's Órdenes Militares section too, which holds the knights' proof files (expedientes de pruebas), for Santiago at least [S23]. Then search the other corporate fonds.
- **Use the current PARES host.** PARES is at pares.cultura.gob.es; the old pares.mcu.es root redirects there [S26]. Old deep links may fail, so rerun a dead link as a catalogue search.
- **Check the custodian before calling a student file lost.** The AHN holds indexes of Universidad Central (Madrid) student files by faculty [S27]. The cut-off varies by faculty, roughly 1920 to 1936, so later files may still be at the Complutense [S27]. The Universidad de Oviedo lost its own historic archive in the fire of October 1934 [S28]. Look for earlier Oviedo student records in the AHN or Asturian archives before calling them lost.

## 9. Request military files and read the gazettes

**Privacy gate:** <!-- privacy-gate: request --> A request for an army or navy personnel or service file sends the person's name, unit and call-up year or service dates, and a conscript after 1900 or a 20th-century officer or sailor may be living; answer the privacy gate in `SKILL.md` before you send it.

- **Route army personnel files by service category and period.** The Archivo General Militar de Segovia holds the service records (hojas de servicio) of professional personnel, from the mid-18th to the late 20th century, once 20 years have passed since retirement or death, and the files of conscripted troops before the Reemplazo (call-up class) of 1900 [S30]. For a conscript after the Reemplazo of 1900, write to the Archivo Intermedio Militar for the province where the unit was stationed and to the Archivo General Militar de Guadalajara, which receives those files when they are transferred [S30]. Give the name, the corps or unit and the call-up class or year of entry. Request Segovia files from Segovia itself, with its authorisation form for restricted-access files [S29].
- **Update old navy citations.** The former Archivo General de la Marina "Álvaro de Bazán" (Viso del Marqués, Ciudad Real) is now a sede of the Archivo Histórico de la Armada, which took over all its holdings under Real Decreto 33/2023 [S31]. Send a request that cites the old name to the new archive.
- **Label a death date taken from a pension notice as an inference.** If a notice transfers a pension from the day after the previous holder's death, that start date bounds the death. Record it as calculated, not as a death record.
- **Use the full-text option in the Biblioteca Virtual de Prensa Histórica.** Its search form offers "Buscar en el texto completo" beside the field (metadata) search [S32]. Tick it for a name search, and run the surname lanes from [Hispanic Catholic register recovery](hispanic-catholic-register-recovery.md), step 3.

## 10. Route Civil War and repression files by holder

**Privacy gate:** <!-- privacy-gate: request --> A request for a court-martial file of the Civil War or the Franco era sends the name of a person who may be living and asks for a repression record about them; answer the privacy gate in `SKILL.md` before you send it, and apply its rule for third persons named in the file.

- **Search PARES for the Centro Documental de la Memoria Histórica (CDMH) cards and the Causa General.** The CDMH general card index of the Secretaría General and the Sección Político-Social is described in PARES down to the single card; each card names the person and the file or archive signature that holds the information. The physical index is not open to users; its database and card images are consulted in the archive's reading room [S33]. Causa General files have item-level PARES records, some with images [S33].
- **Request a post-1939 court-martial file through the military court that owns it.** Find the Tribunal Militar Territorial (territorial military court) and the Defence archive that holds its files. For the Fourth Territorial Military Court's files at the Archivo Intermedio Militar Noroeste in Ferrol, ask the court for authorisation first [S34].
- **For Catalonia, use the Arxiu Nacional de Catalunya's open list.** It is a dataset of people tried by military courts sitting in Catalonia, April 1938 to December 1978, with case numbers and archive references; the original files come from the archive of the Third Territorial Military Court in Barcelona [S35]. Take the case number to the file's holder.
- **For a teacher or other public employee, also search the purge files.** The Archivo General de la Administración (AGA) holds files on the purge (depuración) of officials and publishes purge-file series in PARES [S36]. Also try the PARES portal for Civil War victims and people repressed under Franco, which covers depuraciones and lists the AGA among its archives [S37].
- **Run every surname lane in each repression source,** as set out in [Hispanic Catholic register recovery](hispanic-catholic-register-recovery.md), step 3.

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Submitting a commercial military-index search sends the subject's name and any service, court, place or date filters you enter to MyHeritage. A subject may be living and the query may reveal suspected repression. Answer the privacy gate in `SKILL.md` before submitting it.

**Search MyHeritage's Catalonia Third Territorial Military Courts and Tribunals index** as a second name-search route for 1936–1970 [S66 @2026-11-22], [S79 @2026-11-22]. Use the birth and residence details to distinguish people, then record the procedure type and start date. Record sentence approval and penalty only when stated. Log requests for pardon separately. Check the Generalitat's *Procediments judicials militars* entry or the file for a grant or commutation [S80 @2026-11-22].

**Search MyHeritage's First Territorial Military Courts and Tribunals index** for First Territorial Court cases from 1936. Record the trial year and place, the case number (*sumario*) and the archive storage reference when supplied [S67 @2026-11-22], [S81 @2026-11-22]. Check Defence's *Expedientes de justicia militar* nominal list for the archive locator. Use both references to request the complete proceeding from the holding archive and check the evidence, statements and any final decision in the file [S82 @2026-11-22].

**Search MyHeritage's Disciplinary Labour Battalions, 1937–1942 index** for a name and capture both the registration and case numbers [S67 @2026-11-22], [S83 @2026-11-22]. Look up the corresponding personal file in the Archivo General Militar de Guadalajara's alphabetical BDST indexes [S84 @2026-11-22]. BDST expands to *Batallones Disciplinarios de Soldados Trabajadores*. Workers classified as politically disaffected and guards can appear in the same index. Establish the person's role from the file before attributing a political classification [S83 @2026-11-22], [S84 @2026-11-22].

**Search MyHeritage's Republican Army Casualties, 1936–1939 index** for a Republican Army member. Record any listed occupation and copy the casualty type. Treat death, injury and disappearance as separate outcomes. Use a casualty hit as a lead to a death record only when the entry indicates death [S85 @2026-11-22], [S86 @2026-11-22].

## 11. Search the Spanish departure side for an emigrant

When the arrival record lacks the village, search the Spanish side:

- **Shipping agents' boarding books:** the Fondo Pérez y Cía. (the Compañía Trasatlántica's boarding-ticket books for passengers from Santander to America, 1900–1960), held by the Biblioteca de la Universidad de Cantabria [S39 @2026-11-13]. The library's database searches them by name, surname, destination, ship and departure date, and the digitized books are on its ReCrea site [S39 @2026-11-13]. The surviving books leave gaps, among them 1912–1916 and 1932–1944 [S39 @2026-11-13].
- **Emigrant societies:** the Archivo de Indianos (Colombres) gathers documentation from emigrant societies [S38 @2026-11-13]. The Centros Asturianos of Buenos Aires and Mexico, among others, helped build its collection [S38 @2026-11-13].
- **Passenger and emigrant lists from other archives:** the PARES Movimientos Migratorios search takes a name, a birth year and a place and year of departure or arrival [S44 @2026-11-13]. It covers series such as lists of passengers and emigrants, licences to sail to Cuba and Puerto Rico, and records from Montevideo, Mexico, the Dominican Republic and the Rosario consulate [S44 @2026-11-13].
- **The home town's archive:** read its inventory for any series that records departures.

## Close with a routing packet

Return:

- **Jurisdiction row:** the town, municipality, province and diocese on the event date, and the reason the diocese was chosen.
- **Holdings rows:** for each record, the series (parish original, diocesan duplicate, municipal 1841–1870 register, Registro Civil, padrón, electoral roll, Catastro book, protocol, file), the holder, the locator, the level inspected (index, inventory, image or request) and the result.
- **Requests sent:** the archive, the date and the particulars given.
- **Gaps:** series that do not exist for that place or date (Catastro outside Castile, no 1841 register), books lost with the survival list read, index misses not yet tested in the book, and protocols or court files not yet requested.
- **Name register:** every surname form searched, with and without the joining y, and where.
- **Inferences:** each calculated date (pension notices, baptism-only births) marked as calculated.

The model assembles this packet. The researcher decides identity and kinship.
