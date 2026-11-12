---
id: "galicia-bukovina-habsburg-record-routing"
title: "Route a Galician or Bukovinian record by date, confession and custodian"
summary: "Route a Galician or Bukovinian event by date, confession and custodian, and decide the army before searching WWI records."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "GALICIA-BUKOVINA-HABSBURG-RECORD-ROUTING-01", "text": "**Start an ethnic Ukrainian villager in Galicia in Greek Catholic books, not Orthodox ones.**"}]
handoff: ["austrian-confessional-register-routing", "bessarabia-moldova-record-routing", "corpus-seeded-name-search", "evidence-proof-judgment", "familysearch-practical-record-workflows", "historic-hungary-record-routing", "historical-map-record-recovery", "historical-place-name-resolution", "jewishgen-search-family-reconstruction", "polish-index-original-record-recovery", "russian-military-repression-record-episodes", "soviet-personal-file-recovery"]
checked: "2026-11-02"
checked_basis: "checked on 2026-11-02"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": ["request"], "contact": []}
router: {"tier": "pointer", "group": "Central and Eastern Europe by period state", "order": 1038}
---

# Route a Galician or Bukovinian record by date, confession and custodian

Use this recipe when an ancestor's baptism, marriage, death or military service falls in Habsburg Galicia or Bukovina, or in the same villages after 1918 under Poland, Romania or the Soviet Union. It prevents six failures:

- carrying one jurisdiction chain across the whole region
- reading an interwar voivodeship as today's country
- searching a Ukrainian Galician villager in Orthodox books
- searching only Cyrillic name forms
- sending every book search to one archive
- routing a Habsburg soldier's papers by his birthplace

Transcarpathia is not covered. Link out for the shared steps:

- **Dated place-name candidates and renamed villages:** [historical place-name resolution](historical-place-name-resolution.md).
- **Latin given names and case endings, lane logging and filing-order browsing:** [name searches across scripts and OCR](corpus-seeded-name-search.md).
- **From a Polish index or an AGAD register description to the original entry:** [Polish index to original record](polish-index-original-record-recovery.md).
- **Galician house numbers against cadastral parcel numbers, and the householder rolls of the Josephine (TsDIAL fond 19) and Franciscan (TsDIAL fond 20) cadastres:** [historical map record recovery](historical-map-record-recovery.md), section "Read landowner maps and overlays with limits" [S43].
- **FamilySearch Catalog, film and image mechanics:** [FamilySearch practical workflows](familysearch-practical-record-workflows.md).
- **Jewish database searches:** [JewishGen search and family reconstruction](jewishgen-search-family-reconstruction.md).
- **Russian WWI service, captivity in Russia and Soviet repression episodes:** [Russian military and repression record episodes](russian-military-repression-record-episodes.md).
- **Identity rulings:** [evidence/proof judgment](evidence-proof-judgment.md).

## Contents

- Inputs to gather first
- 1\. Fix the jurisdiction at the event date
- 2\. Choose the books by confession
- 3\. Read the register language, then build name lanes
- 4\. Find who holds the books
- 5\. Decide the army before searching military records
- 6\. Search the Austro-Hungarian casualty lists
- 7\. Find the Grundbuchblatt by birth cohort and domicile
- 8\. When no Grundbuchblatt is found, use the loss cards and hospital sheets
- 9\. Find Northern Bukovina repression cases in Нескорена Буковина
- Close with a routing packet

## Inputs to gather first

- every place form as written, with its record, date and language
- the event type and year; for a soldier, his birth year
- each confession recorded for the family, or "unknown"
- any parish, district (Bezirk, powiat) or voivodeship a record names
- for a soldier: unit, rank, Heimatort or domicile, and any capture or hospital stay
- every name form seen, with its script and the record it came from

## 1. Fix the jurisdiction at the event date

- **Do not carry one chain across the region.** Galicia and Bukovina came to the Habsburgs on different dates and left for different states [S2], [S4], [S33], [S34]. Take each event's regime from its village and its year.
- **Habsburg dates.** Galicia came under Habsburg rule in 1772, at the first partition of Poland [S2], [S3]. Austrian troops occupied Bukovina in 1774, and the Ottoman cession followed on 7 May 1775 [S4], [S5]. In 1786 Bukovina became a district of Galicia [S4], [S6]. In 1849, under that year's Austrian constitution, it became a separate crownland, the Duchy of Bukovina [S4], [S6]. For a Bukovinian event of 1786–1849, list Galicia's provincial authorities among the possible record creators.
- **Record each level of the chain:** crownland (Kronland); the Kreis until the mid-1860s, then from 1867 the political district (Bezirkshauptmannschaft, Polish powiat) [S2], [S35]; the commune (Gemeinde, Polish gmina), organised under the Galician municipal statute of 12 August 1866 [S36]; and the parish that served the village for each confession.
- **After 1918, record the regime of the event's year:**
  - **Eastern Galicia, 1918–1923:** the West Ukrainian People's Republic from late 1918, at war with Poland until its army retreated east across the Zbruch in July 1919. The Conference of Ambassadors accepted the region as part of Poland in March 1923 [S2], [S33].
  - **Bukovina, from November 1918:** Romanian. The Romanian army occupied Chernivtsi on 11 November, a congress declared union with Romania on 28 November, and the Treaty of Sèvres of 10 August 1920 ceded all of Bukovina to Romania [S34].
  - **Interwar:** Eastern Galicia in Poland, in the Lwów, Stanisławów and Tarnopol voivodeships [S8], [S33]; Bukovina an ordinary Romanian province [S34].
  - **1939–1944:** the Red Army occupied Galicia east of the San in September 1939, and Soviet troops entered Northern Bukovina on 28 June 1940. From 1 August 1941 Galicia was a district of the German Generalgouvernement, and Bukovina was under Romanian military rule in 1941–44. Soviet rule returned in 1944 [S33], [S34].
  - **After 1945:** western Galicia, with the Przemyśl and Lemko borderlands, in Poland; the rest of Galicia in four oblasts of the Ukrainian SSR [S33]. Northern Bukovina, Chernivtsi oblast since August 1940, in the Ukrainian SSR and Southern Bukovina in Romania; the 1947 peace treaty recognised the border of 28 June 1940 [S34].
- **Do not read a voivodeship as today's country.** The 1920 act that organised the Lwów voivodeship listed Przemyśl, Rzeszów, Jarosław, Sanok, Krosno and Tarnobrzeg among its powiats [S7], and all are now in Poland. An interwar "województwo lwowskie" entry can lead to a Polish archive. Route by the village.
- **Resolve the village before you choose an archive.** Use the place-name recipe to list and date its candidates, and keep the form each record gives.

## 2. Choose the books by confession

- **Start an ethnic Ukrainian villager in Galicia in Greek Catholic books, not Orthodox ones.** The Habsburg authorities had the Roman Catholic and Greek Catholic clergy keep the vital records [S9]. For Lemko families the default holds until 1926 [S10]. In 1921 the five powiats of Kraków voivodeship where Lemkos lived counted 51,044 Greek Catholics and 142 Orthodox [S10].
- **Add Orthodox books for a Lemko event from late 1926.** Conversions to Orthodoxy began in Tylawa on 16 November 1926. By 1931, four of those powiats counted 48,722 Greek Catholics and 11,335 Orthodox [S10]. Search both confessions.
- **Start a Bukovinian event in Orthodox books.** Orthodoxy was the majority confession in Bukovina in 1910 [S11], [S12].
- **Search each confession as its own search.** When the confession is unknown or the household mixed, search the village's Greek Catholic and Roman Catholic books separately. A miss in one confession's books says nothing about the other's.
- **Search Jewish events in the Jewish registers.** The rules of 20 February 1784 covered every religious community. From 7 May 1789 the Jewish communities kept their own birth, marriage and death books. From 1875 the Austrians set up Jewish register districts, in most cases matching the religious community [S13]. Look for a village's Jewish event under the register district's seat, which can be another town.
- **Expect uneven Jewish books before 1877.** JRI-Poland's overview says the 1784 system did not work for Jewish records in most places, some communities complied in the 1850s, and Jewish record-keeping had no formal regulations or consistency until 1877. For 1784–1788, the years its table assigns to the Catholic Church, it found no Jewish entries in Catholic registers [S42]. Until the law of 10 July 1868, Catholic parish priests supervised the Jewish books, which the communities kept from 1789 [S41], [S13].
- **Do not take 1784 as every parish's first year.** Joseph II's rules date from 1784 [S13], but earlier books survive for some parishes; one Church Slavonic register runs from 1764 [S9]. Take the first year from the parish's own inventory.

## 3. Read the register language, then build name lanes

- **Read the book's language before its names.** Galician books were kept in Latin, Polish or Cyrillic, varying by parish and period, and a Latin book can mix in Polish, Ukrainian or Church Slavonic [S9], [S14]. Greek Catholic books moved from Church Slavonic to Latin to Ukrainian, with mixed-language stretches at each change [S9]. Cyrillic can therefore be early as well as late.
- **Expect Polish spelling or a Latin equivalent.** A Latin book wrote names in Polish orthography [S9]: Wasyl for Василь, Iwan for Іван, and -czuk for the surname ending -чук. A given name can also appear in its Latin form, such as Gregorius for Григорій [S9] or Basilius for Василь [S15].
- **Search the lanes, not only the Cyrillic form.** Generate Polish-orthography lanes (w for в, cz for ч, sz for ш, y for и) and a Latin given-name lane, and log each lane's results separately. A lane is a query, not an identity. For Latin case endings and lane logging, use the name-search recipe.

## 4. Find who holds the books

**Privacy gate:** <!-- privacy-gate: request --> A request to the Warsaw civil registry office (USC) for a book under 100 years old can name people who are still living; answer the privacy gate in `SKILL.md` before you send it.

- **Eastern Galicia: search Lviv, Warsaw, Przemyśl and the oblast archive for every confession.**
  - TsDIAL (Центральний державний історичний архів України у Львові, the Central State Historical Archive of Ukraine in Lviv) holds many Austrian-era Eastern Galician metrical books. Its Greek Catholic books are in fond 201, opys 4a, and its Roman Catholic books mainly in fond 618, opys 2; about 500 Roman Catholic books identified so far sit in fond 201, opys 4a, because they came from civil-registry offices. TsDIAL says most of its metrical books are copies [S16], [S43]. It publishes metrical-book catalogues and fond inventories as PDFs on tsdial.archives.gov.ua, among them a Roman Catholic catalogue dated 2026 [S16].
  - AGAD (Archiwum Główne Akt Dawnych) in Warsaw holds almost 8,500 metrical books of several confessions and rites, mainly from the pre-war Lwów, Stanisławów, Tarnopol and Volhynia voivodeships [S8]. In mid-2022 its Fond 300 held 4,145 Jewish vital-record books and indexes from 109 localities, nearly all in eastern Galicia [S17].
  - **Open the scans before you write to an archive.** AGAD's online inventories link most units of fond 298 (Greek Catholic), fond 300 (Jewish) and fond 301 (Roman Catholic, Lwów archdiocese) to scan galleries. Birth books less than 100 years after closing, marriage and death books less than 80 years after closing, and books too damaged to use (destrukty) are not shown [S47]. Geneteka's **Ukraina** territory indexes many of these books, with SKAN links to the same galleries [S48]. FamilySearch collection 1910265, "Ukraine, Western Ukraine, Catholic Church Book Duplicates, 1600–1937", holds the duplicates priests made for the civil authorities, mainly Greek Catholic. On 2026-11-07 it had an index of baptisms through 1900 and browsable images of baptisms, marriages and deaths; FamilySearch says its images and indexes are subject to contractual limits and changes [S49].
  - **Ask the Warsaw civil registry office for a recent book.** Vital records of five confessions from the former eastern voivodeships reached Warsaw in the early 1950s. In the early 1980s, sets over 100 years old went to AGAD and younger ones to the Warsaw civil registry office (Urząd Stanu Cywilnego, USC), which since 1997 has passed Jewish books to AGAD as each turns 100 [S17].
  - **Check the oblast archives too.** The State Archive of Ivano-Frankivsk Oblast (ДАІФО) holds a collection of metrical books of the Stanisławów voivodeship, 2,594 units, 1752–1946 [S44]. The State Archive of Ternopil Oblast (ДАТО) holds Greek Catholic parish books in fond 487 (1705–1944) and Roman Catholic deanery books in fond 485 (1704–1944); its guide says much of the Roman Catholic material went to Poland [S45].
  - **Check Przemyśl for the western Greek Catholic deaneries.** The State Archive in Przemyśl, fond 56/142 (archive of the Greek Catholic bishopric of Przemyśl), holds consistory copies of metrical books by deanery, mostly from 1784 to the 1850s–1870s. They include deaneries now in Ukraine, such as Drohobycz, Sambor, Stary Sambor, Turka, Mościska and Jaworów. Its scans are on Szukaj w Archiwach, and some units are marked as passed to a civil registry office [S46].
  - **Check Kraków for Lviv-archdiocese Roman Catholic books.** The archive of the Lviv archdiocese is now split among the Archbishop Eugeniusz Baziak Archive in Kraków, AGAD, the Przemyśl archive, the Lviv civil-registry offices and TsDIAL [S16].
  - **Privacy gate:** <!-- privacy-gate: request --> A request to a Ukrainian civil-registry office (ДРАЦС) can name people who are still living; answer the privacy gate in `SKILL.md` before you send it.
  - **Ask the civil-registry office for a recent or bound-in book.** A book under 75 years old is still at the ДРАЦС, and so is an older metrical book bound into a combined book whose storage term at the office has not ended; the office issues copies from it [S50]. For the 75-year rule, see [Soviet personal-file recovery, step 1](soviet-personal-file-recovery.md#1-read-the-negative-reply-before-you-treat-it-as-a-dead-end).
  - Check each of these before you call a book missing. To get from an AGAD description to the entry, use the Polish index recipe.
- **Log a blocked fetch as an access state.** On 2026-11-02, automated requests for TsDIAL's PDFs and home page returned HTTP 403, and the catalogue files showed only in search results [S16]. On 2026-11-07 TsDIAL's catalogue e-resource, archium.tsdial.archives.gov.ua, answered while the main site still returned 403 [S43]. Open the catalogue in a browser session. Record a 403 as "access blocked", never as "no catalogue".
- **Northern Bukovina: the State Archive of Chernivtsi Oblast.** A search-result summary reports Orthodox metrical books there and only fragmentary survival for 1784–1840; the thesis itself was not read, so those holdings and survival claims remain unconfirmed [S18]. Search-result catalogue text also reports FamilySearch films of originals at the Chernivtsi State Archive; the full entries were not read, so confirm the actual books and film coverage before treating them as available [S19]. For a village in Chernivtsi oblast that was in Khotin uezd of Bessarabia before 1918, use [Route a Bessarabian or Moldovan record](bessarabia-moldova-record-routing.md).
- **A village now in Poland or Romania leaves this route.** For a western Galician parish, or a former Lwów-voivodeship parish now in Poland, start with the Polish index recipe. For Southern Bukovina, search the Suceava County Branch of the National Archives of Romania. Its civil-status collection (Colecție de stare civilă, fond 12) holds birth, marriage and death books of 1784–1950, mostly kept by the clergy, for the localities of today's Suceava county, which includes all of Southern Bukovina. It is arranged by locality, then by confession [S37].
- **Before 1772, choose the archive by the institution that created the record, not by today's border.** TsDIAL, for example, holds the court books of eastern Galicia from the 15th to 18th centuries, more than 6,500 volumes [S38].
- **Do not assume an Austrian church-book portal covers Galicia.** Check that Matricula's catalogue lists the parish before you search it.
- **Check survival before an exhaustive search for a Jewish town.** Open Gesher Galicia's record inventories (geshergalicia.org/inventory/, including its inventory of AGAD Fond 300) [S17], [S39]. Then search the Routes to Roots Foundation Archive Database (rtrfoundation.org/search.php), which lists by town the surviving Jewish and civil records of Eastern European archives, with years and holding archive; use its "Begins With" town search so district-level records also appear [S40].
- **A book on no list is "not located", not lost.** Record each archive and catalogue you checked.

## 5. Decide the army before searching military records

- **Start a Galician or Bukovinian man born about 1865–1900 with the Austro-Hungarian army.** Galicia and Bukovina were Cisleithanian (Austrian) provinces under the conscription introduced in 1868, and the Grundbuchblätter of their men from the 1865 cohort survive in Lviv [S25]. Take the Austro-Hungarian records first and the Russian WWI databases as a second branch.
- **Do not let birthplace decide the army.** Check subjecthood, moves, volunteer service and captivity, and confirm the army from a document. When a record ties him to service in 1914–18 but not to an army, keep both branches open. For the Russian branch, including captivity in Russia, use the Russian episodes recipe.

## 6. Search the Austro-Hungarian casualty lists

- **Search CompGen's index of the Verlustlisten Österreich-Ungarns.** It covers the lists published from 1914 into 1919 [S20]. Indexing was completed in January 2022, with 2.69 million entries [S21]. Do not record the index as partial.
- **Search the surname with the Heimatort.** The search form filters by surname, given name, Offizier/Mannschaft, Charge, Truppenkörper, Unterabteilung, Land, Bezirk, Heimatort and Geburtsjahr, among other fields [S22]. Use the Austrian-era place name and the Polish-orthography surname lanes from step 3.
- **Read every field as optional.** An entry can give the list number (Ausgabe) and date, officer or other rank (Offizier/Mannschaft), grade (Charge), unit (Truppenkörper), sub-unit (Unterabteilung), Land, district (Bezirk), Heimatort, birth year, status, and event date and place. Many fields are blank in a given entry. Cite the Ausgabe and its date.
- **Treat a hit as a lead and a miss as narrow.** A Heimatort is not a birthplace. A miss means only that your queries matched no entry in the lists; it does not show that he never served. Carry any unit into step 7.

## 7. Find the Grundbuchblatt by birth cohort and domicile

- **From November 1820 each soldier had a Grundbuchblatt** (GB, a personnel record sheet) kept by his regiment, replacing the earlier muster lists (Musterlisten) [S24]. For service before 1868, give the Kriegsarchiv the unit and the approximate discharge year, or search its online name indices, which cover all regiments together [S24].
- **After conscription began in 1868,** the recruiting-district commands (Ergänzungsbezirkskommanden) drew up, updated and kept the GBs locally, not in Vienna [S25].
- **For men born 1865–1900, route by domicile.** After the Treaty of Saint-Germain (1919), the GBs of these cohorts went to the successor state where the man held his right of domicile (Heimatrecht, Heimatzuständigkeit) [S25], [S26]. Domicile and birthplace need not match, so give the archive both [S25]. For these cohorts, Vienna holds GBs only for present-day Austria [S25].
- **Search TsDIAL fond 780 first for a Galician or Bukovinian man.** The GBs of Galician and Bukovinian men from the 1865 cohort onward are in TsDIAL, fond 780. They are digitised and indexed alphabetically by the Wojak project [S25]. The index also covers other military documents in the fond [S25]. Do not record his GB as destroyed until you have checked that index.
- **For a man born about 1850–1864, do not assume Vienna.** S25 places Galician and Bukovinian GBs in TsDIAL only from the 1865 cohort and lists no earlier Galician series in Vienna. A Kriegsarchiv reply quoted in S26 says the sheets of the 1850–1900 cohorts domiciled outside today's Austria did not stay in Vienna [S25], [S26]. Search the fond 780 index, and record a miss as "not located".

## 8. When no Grundbuchblatt is found, use the loss cards and hospital sheets

- **Search the Kriegsarchiv's First World War loss holdings (Kriegsverluste).** They cover 1914–1918 and men born 1865–1900 [S26], [S27]. They include the phonetic cadastre of war losses (Phonetischer Kataster der Kriegsverluste) and the prisoner-of-war card files (Kriegsgefangenenkarteien) [S28]. Their death card file (Totenkartei) is far from complete and is online through FamilySearch [S30].
- **Expect personal data, not a career.** The cards give surname, given name, birth year, birthplace, Heimatort, rank and unit [S28]. POW cards record the date of capture and the camp [S31].
- **Browse the sound-alike positions.** The cards are mostly filed phonetically, partly in rough alphabetical order, and the series do not share one phonetic system [S28], [S29]. Check neighbouring sound-alike forms and record the ranges browsed.
- **Plan the POW search yourself.** Kriegsarchiv staff do not search the POW card files for enquirers [S31]. Record an unanswered or declined request as "not searched", not as "searched without a match".
- **Add the field-hospital sick sheets** (Krankenblätter der Feldspitäler). They stayed in Vienna, whereas garrison-hospital records were kept territorially and went to the successor states [S26]. With the loss cards, they are often the only surviving source for a soldier from outside present-day Austria. Many sheets are lost [S26], [S27].

## 9. Find Northern Bukovina repression cases in Нескорена Буковина

- **Use the project for case numbers.** «Нескорена Буковина» ("Unbroken Bukovina", neskorena-bukovyna.com.ua) publishes digitised archival documents [S32]. They include lists of criminal cases against repressed persons held in the main fond of the SBU sectoral state archive in Chernivtsi (ГДА СБУ), with case numbers of the form NNNN-ФО [S32]. It also publishes documents from other archives, so record which archive each document names [S32].
- **Browse its repressed-persons pages by district and village** [S32].
- **Do not expect names on the 1940–41 deportation pages.** They give totals, plans and lists of the officials who carried out the deportations. Named lists of insurgents' families appear only for August 1945 [S32].
- **Cite the case number, then confirm the file's present custodian** before any request. For episode discipline, use the Russian episodes recipe.

## Close with a routing packet

Return:

- **Jurisdiction rows:** for each event, the village as written, the date, the regime, the crownland, district and commune, any interwar voivodeship, and today's country.
- **Confession rows:** the books searched for each confession, with the reason (Greek Catholic default, Lemko event after 1926, Bukovinian Orthodox default, Jewish register district).
- **Name lanes:** each literal form, each Polish-orthography and Latin lane, and where it was searched.
- **Holdings rows:** TsDIAL, AGAD, the Warsaw civil registry office (USC), the oblast archive, the Przemyśl archive, the Ukrainian civil-registry office (ДРАЦС), the Chernivtsi archive, the Suceava County Branch of the National Archives of Romania and FamilySearch, each with the catalogue or inventory checked, the unit and years, the locator and the access state.
- **Military rows:** the army decision and the document behind it; each casualty-list query with its fields and spellings, and each hit with its Ausgabe and date; the GB route by cohort and domicile, with the fond 780 index result; the loss cards and hospital sheets checked, and the POW-file search status.
- **Repression rows:** the Нескорена Буковина section, the case number and the custodian check.
- **Gaps:** each labelled *not located*, *access blocked*, *not searched* or *searched without a match*.

The model assembles this packet. The researcher decides identity and kinship.
