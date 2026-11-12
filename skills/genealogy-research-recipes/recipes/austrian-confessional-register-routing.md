---
id: "austrian-confessional-register-routing"
title: "Route an Austrian or Czech-lands vital event to the confessional register that recorded it"
summary: "Route an Austrian or Czech-lands vital event to the register that legally recorded it: a confessional register, the 1870 register for people outside a recognised church, or the regional archive that now holds the books."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "AUSTRIAN-CONFESSIONAL-REGISTER-ROUTING-01", "text": "**Do not read a Catholic baptism or burial as proof of non-Jewish origin.**"}]
handoff: ["archival-image-coverage-verification", "burial-evidence-packet", "catholic-parish-diocesan-record-recovery", "city-directory-observation-workflow", "evidence-proof-judgment", "galicia-bukovina-habsburg-record-routing", "german-register-image-recovery", "historic-hungary-record-routing", "historical-place-name-resolution", "jewish-genealogy-conditional-hypotheses"]
checked: "2026-11-04"
checked_basis: "opened 2026-11-04"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": ["request"], "contact": []}
router: {"tier": "pointer", "group": "Central and Eastern Europe by period state", "order": 1041}
---

# Route an Austrian or Czech-lands vital event to the confessional register that recorded it

Use this recipe before you search for a birth, marriage or death in present-day Austria before 1939 (outside Burgenland, which was Hungarian until 1921), in Vienna at any date, or in the Czech lands. It sends each event to the register that legally recorded it: a church or religious-community register, or the regional archive that now holds the books. It prevents five failures: looking for a pre-1938 Standesamt (civil registry office) record that never existed, expecting today's Standesamt to hold the old confessional books, searching every Vienna parish instead of fixing the address first, paging through year volumes when a name index exists, and reading a Catholic baptism or burial as proof that a Viennese family had no Jewish origin.

It covers the 1938–1939 cutover, the Vienna address and index route, withdrawals from Judaism in Vienna, and the Czech regional-archive route. Link out for the shared steps:

- **Parish candidates, merged or closed parishes, diocesan copies:** [Catholic parish and diocesan record recovery](catholic-parish-diocesan-record-recovery.md).
- **Building a directory series and reading gaps between editions:** [city-directory observation workflow](city-directory-observation-workflow.md).
- **A grave, cemetery register or burial permit:** [burial evidence packet](burial-evidence-packet.md).
- **A village with German and Czech names, or a namesake problem:** [historical place-name resolution](historical-place-name-resolution.md); the GenTeam gazetteer step in [German register image recovery](german-register-image-recovery.md), step 2.
- **Galicia and Bukovina, including Austro-Hungarian military sheets:** [Galicia and Bukovina Habsburg record routing](galicia-bukovina-habsburg-record-routing.md).
- **A Jewish DNA signal or naming clue in a family recorded as Christian:** [Jewish genealogy conditional hypotheses](jewish-genealogy-conditional-hypotheses.md).
- **Frame versus volume and the inspection ledger:** [archival image coverage verification](archival-image-coverage-verification.md).
- **Identity rulings:** [evidence/proof judgment](evidence-proof-judgment.md).

## Contents

- Inputs to gather first
- 1\. Fix which register the law used on the event date (present-day Austria)
- 2\. In Vienna, fix the address before choosing the parish
- 3\. Check the Vienna indexes before paging through year volumes
- 4\. Search a Viennese withdrawal from Judaism in both communities
- 5\. In the Czech lands, route by the regional archive
- Close with a routing packet

## Inputs to gather first

Gather these before searching:

- the event type and exact or approximate date
- the place under every name form seen (German, Czech), each with the record it came from
- for Vienna: a street address and the year it was valid, if any record gives one
- the confession at the event date, and any sign of a change: a conversion, a withdrawal, a mixed marriage or an unexplained gap
- any register signature, Matricula volume or index hit already seen

## 1. Fix which register the law used on the event date (present-day Austria)

This step does not cover Burgenland, which was Hungarian until 1921.

- **Before the cutover, search the confessional register for a member of a recognised church or religious community.** Austria had no state civil registration for the general population before 1938. The recognised churches and religious communities kept the vital registers on the state's behalf: Catholic, Protestant and Jewish (Israelitische Kultusgemeinde, IKG) registers among them [S2]. These are the official records for the period, not a substitute.
- **For a person in no recognised church or religious community, search the civil register of the political authority.** Under the law of 9 April 1870, the Bezirkshauptmannschaft (district authority), or in a town with its own statute the municipal authority, handled their marriages and kept their birth and death registers [S13]. Someone who left a church without joining another confession is recorded there, not in a parish book.
- **Use the cutover dates exactly.** Standesämter recorded marriages from 1 August 1938 and births and deaths from 1 January 1939 [S1], [S2]. A marriage in autumn 1938 is in the Standesamt; a birth in the same months is still in the confessional register.
- **Search the old books at their holders, not at the Standesamt.** The law assigns the registers from before those dates to the churches, religious communities and authorities that hold them, which keep and continue them [S1].
- **Search each spouse's confession for a mixed or changed-confession family.** One household can have events in two confessional series.

## 2. In Vienna, fix the address before choosing the parish

- **Do not search every Vienna parish.** Catholic parishes cover street-defined territories, so the district does not fix the parish. Take the address for the event year, then place it in the parish that covered that street. Check the parish against the event date with the Catholic recipe.
- **Get the address from Lehmann's directory.** Lehmann's Vienna address book ran from 1859 to 1942, with no volumes for 1862, 1863, 1866 and 1869; Wienbibliothek Digital offers the digitised volumes with full-text search [S3]. It gives residence and occupation year by year, apart from those four years. Log those four missing years as gaps under the [city-directory observation workflow](city-directory-observation-workflow.md).
- **Search ANNO for death notices and announcements.** ANNO is the Austrian National Library's searchable portal of digitised newspapers [S4]. A notice can give the address, the date and the church of a funeral.
- **Search Friedhöfe Wien for a grave.** Its deceased search (Verstorbenensuche) covers the cemeteries Friedhöfe Wien runs and excludes the denominational cemeteries [S5]. A miss there says nothing about a Jewish, Protestant or other confessional cemetery.

## 3. Check the Vienna indexes before paging through year volumes

- **Look for a separate index volume on Matricula.** Vienna Catholic registers on Matricula include index volumes next to the year books; Döbling B-01, for example, is an "Index Trauungen" (marriage index) for 1783–1850 [S6]. Open the parish's volume list and search an index before you turn pages.
- **Search GenTeam's Vienna databases.** GenTeam is free with a registered login. Its Vienna databases include Catholic baptisms (Katholische Taufen) and Jewish registers (Jüdische Matriken), with separate Catholic, Protestant and Jewish index groups [S7].
- **Treat every index hit as a pointer.** Open the register image it points to and read the entry there before you record the event.

## 4. Search a Viennese withdrawal from Judaism in both communities

- **Search GenTeam's IKG Austritte 1868–1914 index for a withdrawal.** It indexes about 18,000 withdrawals from the official withdrawal declarations and the withdrawal protocols (Austrittsprotokolle) of the Vienna Jewish communities; its IKG field gives the year and sequence number of the protocol entry [S10]. If the person was baptised, also search the receiving parish's register for the adult baptism.
- **Use the published indexes by period:**

  | Period | Work | Scope |
  | --- | --- | --- |
  | 1782–1868 | Anna L. Staudacher, *Jüdische Konvertiten in Wien 1782–1868* (Peter Lang, 2002) | about 3,000 adults baptised in Vienna [S9] |
  | 1868–1914 | Anna L. Staudacher, *"… meldet den Austritt aus dem mosaischen Glauben": 18000 Austritte aus dem Judentum in Wien, 1868–1914* (Peter Lang, 2009) | about 18,000 withdrawals [S8] |

  Do not merge the two works into one range or count.
- **Do not read a Catholic baptism or burial as proof of non-Jewish origin.** For a Catholic Viennese family with a Jewish DNA signal or an unexplained gap, search both works and the parish adult baptisms before you call the Jewish link unproven.

## 5. In the Czech lands, route by the regional archive

**Privacy gate:** <!-- privacy-gate: request --> An entry just past its access period can still name a spouse, parent or informant who is living; answer the privacy gate in `SKILL.md` before you ask a registry office to show or copy it.

- **Search the state regional archive, not the parish.** Czech parish registers (matriky) are held by region in the state regional archives (státní oblastní archivy) [S11]. Route by the archive whose present territory includes the parish that kept the register.
- **Pick the archive by territory.** Bohemia has five state regional archives (SOA): Litoměřice for the north, Plzeň for the west, Třeboň for the south, Hradec Králové for the east (SOA Zámrsk until 2022, the name older guides use) and Praha for Central Bohemia only. In Moravia and Silesia, the Moravian Provincial Archive in Brno (MZA) covers the south and the Provincial Archive in Opava (Zemský archiv v Opavě) covers north Moravia and Silesia [S11], [S16]. A parish inside the city of Prague goes to the Prague City Archives (AHMP), not SOA Praha. Each archive runs its own online register portal.
- **Route the exceptions elsewhere** [S11]:
  - Jewish registers: the National Archive (Národní archiv);
  - military registers: the Military Central Archive;
  - Prague registers: the Prague City Archives.
- **Route a recent register by its book's last entry.** The registry office (matriční úřad) keeps a birth book for 100 years and a marriage or death book for 75 years after the book's last entry, then transfers it to the competent state regional archive [S14]. A book past that period is at the archive: find the volume in its catalogue, not at the registry office.
- **Ask the registry office for an open entry in a book it still holds.** Access periods run from the entry itself: 100 years for a birth, 75 for a marriage, 30 for a death. If the entry is past its period but later entries keep its book at the registry office, ask that matriční úřad to let you inspect it. Under § 25b of Act No. 301/2000 Coll., anyone may then inspect the entry and take extracts in the registrar's presence, with no proof of relationship; the fee is 50 Kč per entry [S17], [S18]. After those periods, anyone may also request a certificate under § 25b without proving relationship [S18]. Do not record the register as lost.
- **Use the archive's own viewer.** The Moravian Provincial Archive in Brno (Moravský zemský archiv, MZA) publishes the registers it holds in Acta Publica, filterable by church originator (Roman Catholic, Evangelical and others) and by civil registry office [S12]. Search the regional archive's online registers before you write to a parish.
- **Read the volume type.** Czech register catalogues sort volumes by event: N (narození, births or baptisms), O (oddaní, marriages), Z (zemřelí, deaths) [S20]. Acta Publica writes the types out in full (Narození, Oddaní, Zemřelí), gives each index its own field (index narození, index oddaní, index zemřelí) and uses the letters in its notes, as in N+O [S19]. Open the index before paging through a year book. Search a woman's surname with the feminine -ová ending as well as the masculine form [S15].

These steps cover a portal's limits on automated reading, an entry that is still closed, how a volume is arranged, later notes on an entry, and sources outside or older than the registers.

- **Check a portal's rules before any scripted reading.** SOA Praha's robots.txt bars ClaudeBot from the whole of eBadatelna and bars every automated client from its image paths [S33 @2026-11-09]. Porta fontium asks for 10 seconds between requests [S34 @2026-11-09]. A browser driven by an agent is still an automated client, so where a portal bars them, have the user open the image in their own browser and share it. At a 403, 429 or 503, stop and follow the block rule in [AI for documentary records](ai-for-documentary-records.md).

- **Privacy gate:** <!-- privacy-gate: request --> An entry inside its access period can name people who may be living; answer the privacy gate in `SKILL.md` before you ask for it.

- **Ask as close family for an entry still inside its access period.** Inside the 100, 75 or 30 years, a registry office gives a certificate, an inspection or a verbatim extract (doslovný výpis) only to the person the entry concerns, that person's family and a few official or legal applicants; the extract can be a copy of the entry [S21]. The Act limits family to a spouse, partner, parents, children, siblings, grandparents, grandchildren and great-grandchildren [S21], so a great-great-grandchild has no family route. For an adoption, only the adopters and, from age 12, the adopted person may see the entry; if a court kept the birth parent secret, the adopted person must wait for full legal capacity [S21].

- **Find out how a volume is arranged before you jump by year.** A volume can hold several villages and record types in separate stretches, and you usually have to page through the images to find where each one begins [S27]. Porta fontium's volume page gives the order of the records and often the pages in each section [S27]; other portals may not. A jump by year can land in another village's stretch, so log which stretches you read. A "not found" covers only those.

- **Follow a marriage note from the baptism entry.** A note beginning *Getraut*, *Oddán* or *Cop.* records a marriage [S22]. Copy it word for word, decide from its wording and dates whose marriage it records, and open the marriage entry it points to. Use [Catholic baptism–marriage cross-notations](catholic-sacramental-cross-notations.md) to weigh it.

- **Keep a legitimation note separate from the original entry.** A Czech legal dictionary cites a decision of 7 June 1877: a completed legitimation must be noted in the birth register, with the father's name entered and the parents' marriage mentioned [S23]. Record the entry as first written and the later note as two observations, then find the marriage.

- **Do not read the mother's father as the child's father.** The father's name is normally missing from the entry of a child born outside marriage [S24], but the mother's column can still name her own parents, as *Tochter des* (daughter of) [S22]. A man named there is the child's maternal grandfather.

- **For Prague in 1850–1918, get birth details from the police registration sheets.** The National Archives' [conscriptions database](https://na.gov.cz/en/for-public/research-room/digital-research-room-archival-records-on-line/conscriptions-1850-1918) holds 664,651 sheets indexing 2,054,852 person records [S25 @2026-11-09]. A sheet gives the year and place of birth, religion, a married woman's maiden name and the household [S25 @2026-11-09]. Use the birthplace to choose the parish. Names are transcribed as written, so search variants such as Čapek, Czapek and Tschapek; a move to another Prague quarter made a new sheet, and sheets can disagree [S25 @2026-11-09]. The archive's list of covered areas includes Karlín and Smíchov but not Žižkov or Vinohrady [S25 @2026-11-09], so a miss for someone living in either says nothing.

- **For a soldier, get birth details from the Military Central Archive's databases.** Its [Databáze VHA](https://www.vuapraha.cz/databaze-vha/) page searches by surname, first name, place and date of birth across legionnaires, the dead of both world wars, members of Czechoslovak units abroad in the Second World War and the Czechoslovak home guard in Italy [S26 @2026-11-09]. Treat a hit as a pointer and confirm the birth in the register.

- **Check the birth cohort before you look for a Czech-lands service sheet.** The Austrian State Archives says the service sheets (Grundbuchsblätter) of conscripts born 1865–1886 are at the military archive in Prague, that earlier cohorts survive there only in fragments, and that those of men born 1887–1898 are largely destroyed [S32 @2026-11-09]. Its Vienna war archive has sheets online for cohorts up to 1864 and, for southern Bohemia and southern Moravia, for cohorts 1865–1900 [S32 @2026-11-09]. For a man born 1887–1898 elsewhere, start with the [casualty lists](galicia-bukovina-habsburg-record-routing.md#6-search-the-austro-hungarian-casualty-lists).

- **For a Jewish family, search the Familiant books as well as the registers.** The National Archives has put online all 190 volumes of its [Books of Jewish Familiants](https://na.gov.cz/en/for-public/research-room/digital-research-room-archival-records-on-line/books-of-jewish-familiants), and has added Moravian Jewish family books from other archives [S31 @2026-11-09].

- **Before the registers, use the 1651 list and the 1654 tax roll.** The list of subjects by faith (Soupis poddaných podle víry) gives each person's name, status, occupation, age and religion, but mostly leaves out children under twelve [S28]. The National Archives' [Berounsko edition](https://www.nacr.cz/wp-content/uploads/2019/01/Berounsko_cele_H_zamceno.pdf) is one regional volume, as a PDF [S28]. The tax roll (berní rula) names the holders of taxable town houses, subject farmsteads and free courts; it survives for most of Bohemia and was not compiled for the Cheb region [S29]. A person who held no such property will not be in it.

- **To link generations, read the land books.** SOA Plzeň has published almost all its estate land books (pozemkové or gruntovní knihy) on Porta fontium: 6,083 volumes from 161 estate fonds, mainly for the Plzeň and Karlovy Vary regions, the oldest from 1558 [S30 @2026-11-09]. They name owners and often the relatives paid inheritance shares, and they record transfers, mortgages and marriage contracts [S30 @2026-11-09]. Elsewhere, check what the regional archive has put online.

## Close with a routing packet

Return:

- **Jurisdiction row:** the place under each name form, the confession at the event date, and which register the law used: confessional, the political authority's civil register for a person without a recognised confession, Standesamt, or Czech regional archive.
- **Address rows (Vienna):** each Lehmann edition read, the address and occupation found, missing editions, and the parish chosen for each address and year.
- **Series rows:** for each event, the register or index searched, its holder, the locator (Matricula signature, GenTeam database, archive and volume), and the status: searched, found, not found or not online.
- **Confession changes:** every withdrawal or adult baptism searched, with the work or register used and the result.
- **Gaps:** directory years missing, denominational cemeteries not searched, index hits not yet opened on the image.

The model assembles this packet. The researcher decides identity and kinship.
