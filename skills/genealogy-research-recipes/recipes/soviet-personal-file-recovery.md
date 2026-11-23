---
id: "soviet-personal-file-recovery"
title: "Recover Soviet personal files when ZAGS or metrical records are lost"
summary: "Rebuild a Soviet-era life from institutional personal files when ZAGS or metrical records are lost."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "SOVIET-PERSONAL-FILE-RECOVERY-01", "text": "Keep questionnaires (анкеты) and autobiographies found there as dated self-reports, and keep catalogue hits found by name as candidates."}]
handoff: ["burial-evidence-packet", "evidence-proof-judgment", "russian-empire-jewish-metrical-book-recovery"]
checked: "2026-10-21"
checked_basis: "checked on 2026-10-21"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": ["request"], "contact": []}
router: {"section": "Records by country and region", "group": "Russian Empire and Soviet Union", "order": 97}
---

# Recover Soviet personal files when ZAGS or metrical records are lost

Use this recipe when a metrical book from before 1917 or a ZAGS act book is reported lost, never received or not found, and the person lived into the Soviet period. It also applies when the only advice so far has been "ask ZAGS" or "search the military databases". The method has three parts:

- Turn the person's life course into a list of institutions.
- For each institution, name the personal-file or list series it created and the custodian that holds it now.
- Keep questionnaires (анкеты) and autobiographies found there as dated self-reports, and keep catalogue hits found by name as candidates.

Related recipes:

- Wives' natal families, house books and family files when vital records fail: [JewishGen search and family reconstruction](jewishgen-search-family-reconstruction.md).
- Arrest, investigation and prisoner files: [Russian military and repression record episodes](russian-military-repression-record-episodes.md).
- Pre-1917 registration (приписка) and name re-registration: [Russian-Empire Jewish identity attribution](russian-empire-jewish-identity-attribution.md).
- Spelling expansion across scripts: [corpus-seeded name searches across scripts and OCR](corpus-seeded-name-search.md).
- Identity, namesake and nationality rulings: [evidence/proof judgment](evidence-proof-judgment.md).

## Contents

- 1\. Read the negative reply before you treat it as a dead end
- 2\. Build a life-course inventory for the subject, the spouse and the descendants
- 3\. Route each institution to its series and present custodian
- 4\. Search under every name the person actually used
- 5\. Log each catalogue hit as a candidate with its own locator
- 6\. Read questionnaires and autobiographies as dated self-reports
- Output: personal-file register

## 1. Read the negative reply before you treat it as a dead end

- **Record the archive's exact wording.** "Not found in the book for that year", "books not preserved" and "books were never received by the archive" are three different results.
  - Reread the reply for neighbouring parishes, years and books the archive never received [S3].
- **Check the inventory or images.** A reported «not preserved» reply conflicted with an inventory listing a combined births-and-deaths book for the town [S2]. Verify the event type and year in the volume.
- **For an Orthodox parish, trace the consistory copy.** Ask which state archive holds it if the diocesan office refers the search elsewhere [S3].

- **Privacy gate:** <!-- privacy-gate: request --> A ZAGS search or repeat-document request can concern acts naming people who may still be living; answer the privacy gate in `SKILL.md` first.
- **Russia: a ZAGS or Gosuslugi "not found" may cover only the electronic register.** When an act is not in the unified register (ЕГР ЗАГС), the law requires a check of the paper record (Federal Law 143-FZ, Art. 9, Part 4). Ask whether that office's paper books for the year were searched, and how a missing record is found and entered [S25 @2026-11-02].
  - Any ZAGS office accepts an in-person request for a repeat certificate or extract; it need not be the office that registered the event. Issue is same-day when the act is in the register; otherwise the office searches the paper record, which in Moscow takes up to 30 days [S25 @2026-11-02], [S27 @2026-11-02].
  - Moscow reported in December 2020 that its whole ZAGS archive from 1926 was digitised and can be requested at any ZAGS in Russia. Its "Мои документы" (My Documents) service centres also issue repeat ZAGS documents [S26 @2026-11-02], [S27 @2026-11-02].

- **Privacy gate:** <!-- privacy-gate: request --> A Ukrainian civil-status request, even for an act over 75 years old, can name people who are still living; answer the privacy gate in `SKILL.md` before writing to an archive, a ДРАЦС or a consulate.
- **Ukraine: route a civil-status request by the act's age.** Civil-registration offices (ДРАЦС) keep the act books for 75 years from the act's date. They then transfer them each year to the state archive of the oblast, of Kyiv or Sevastopol, or of the Autonomous Republic of Crimea (Ministry of Justice order No. 2804/5 of 30.12.2013, §§ II.1, V.1) [S22 @2026-11-02]. Send a request for an older act to that state archive after confirming transfer. Russia's custody term differs: see [Russian-Empire Jewish metrical-book recovery § 6](russian-empire-jewish-metrical-book-recovery.md#6-switch-to-zags-registers-when-the-territory-changed-over).

  For a metrical entry bound into a combined book, the archived 2018 rules let the office issue copies while its retention term continued [S34]. Confirm the current holder before applying.
  - A repeat certificate of a living person's own birth is a later derivative of the act, and requesting one is that person's own action. Read it as [§ 4 of that recipe](russian-empire-jewish-metrical-book-recovery.md#4-when-the-book-is-lost-search-for-named-substitutes) reads Soviet repeat certificates.

- Check whether the needed repeat certificate or extract is available in Diia (the Ukrainian state services portal). Where available, it can be ordered online, but the application must be signed with a Ukrainian qualified electronic signature (КЕП) or Diia.Signature. Ukrposhta delivery of the result is available only within Ukraine (Diia notice of 10.07.2026, checked 2026-11-02). From abroad, apply through a Ukrainian consulate [S23 @2026-11-02], [S24 @2026-11-02]. The death-extract service was marked temporarily unavailable at that check [S24 @2026-11-02].

- **After a confirmed loss, change record series.** Trace the person in work, study, evacuation and party records [S2].

**Ask for a справка with the record lines you need.** Besides a repeat certificate, a Russian ZAGS
office issues справки on a registered act. Birth, marriage, divorce, adoption, paternity, name-change
and death справки (forms No. 2, 4–10 and 12) have a line «Иные сведения». On the applicant's written
application, it carries information from the act record that the form does not provide, each item
introduced by the name of the record line (for example «последнее место жительства умершего:») and
copied word for word from the record. It never carries adoption information in a birth справка, or
the declarant's place of residence when a private person declared the registration. [S41], [S42] So
name each record line you need.

**For a death, name the lines a death record can hold.** Death справка form No. 12 prints the
deceased's date and place of birth, citizenship, nationality, the date and place of death, the cause
of death and the record's number, and adds «Иные сведения»; form No. 11, issued for the burial, has
no «Иные сведения» line. [S66] Death справки from Soviet records can also give the last address,
the place of work, marital status and education, where the record held them. [S67] Ask for each of
those lines by name in a form No. 12 application.

**When only the name and year of death are known, request a repeat death certificate.** Under Federal
Law 143-FZ the death certificate states the deceased's date and place of birth (Art. 68), and a
relative of the deceased or another interested person may receive a repeat one (Art. 9, Part 2).
[S48], [S65] Both lines are copied from the death record: a line the record lacks is printed as a
dash, and the birthplace keeps the elements in the order the record gives them (Minjust order No. 167
of 13.08.2018, App. 2, rules 10 and 15). [S49] So read the birthplace as written at registration, in
the units of that time. One repeat certificate used a district name introduced decades after the birth [S50], [S51]. Check the unit’s dates before choosing a parish and include neighbouring churches.

**A record number does not replace the kinship chain.** For a dead person, Art. 9 of 143-FZ lets
ZAGS issue documents to a relative or another interested person, who shows an identity document and
documents proving the right to receive them (Parts 2 and 7). For a living adult, a repeat certificate
goes only to that person, to the guardian of a person declared legally incapable, or to someone
holding a notarised power of attorney from one of them; once the child is of age, a parent may ask
only for another document confirming the birth registration (Part 2). [S65]
A requester who knew a death record’s date and number was reportedly refused a справка because the kinship chain was incomplete [S68]. Build the chain in step 5 and check whose authorisation a living adult’s documents require [S69].

**Second copies.** Paper act records from before 1 October 2018 were made in two copies. Books of
second copies are kept by the regional body in charge of civil registration where the records were
made. They are destroyed once the books of first copies go to the state archive, but not when the
first-copy book has not survived, and a record lost from a first-copy book is replaced from the second
copy. First-copy books made before Federal Law No. 219-FZ of 2016 took effect, and metrical books, go to
the state archive only after their data are entered in the unified register of civil-status records.
[S43 @2026-11-13] If a справка has a gap, an unreadable place or a discrepancy, ask which copy was read
and where the other copy is kept.

A Ukrainian court decision can quote an archive's reply about a birth register. Court decisions, among
them decisions establishing a fact of birth, are published in the Unified State Register of Court
Decisions (reyestr.court.gov.ua), whose context search finds a decision by a fragment of its text.
Names and other identifying details are replaced there by letters or numbers (Law No. 3262-IV,
art. 7). [S45 @2026-11-13], [S46 @2026-11-13] A 2025 decision (register No. 132430639, case
No. 129/2514/25) quotes an Odesa oblast archive reference of January 2025: the 1930 birth register of
Kodyma never reached the archive and is considered lost during the occupation and fighting of
1941–1944. [S47 @2026-11-13] Search reyestr.court.gov.ua for the place name, record the archive, the
birth register, its years and the date of the quoted reply as a lead, and confirm the custody with the
archive. Do not try to identify the parties.

**Read "no books before year X" as a custody answer.** ZAGS bodies keep paper act books for 100
years and then hand them to state archives (143-FZ, Art. 77). [S70 @2026-11-16]

A ZAGS office that reported no holdings before 1941 referred the requester to an inter-district ZAGS subdivision [S71]. Ask about district archives and inter-district offices before recording a loss.

**A marriage of 1927–1944 may never have been registered.** The RSFSR code on marriage and the
family of 1926, in force from 1 January 1927, treated a de facto marriage as the legal equal of a
registered one. [S72], [S73] The decree of 8 July 1944 gave legal effect only to a registered
marriage and let couples already living together register, stating how long they had lived together
(Art. 19). [S74] So when no marriage is found for a couple of that period, search for a registration
after July 1944 and read its cohabitation date. Children's birth records naming both parents do not
show that the marriage was registered.

## 2. Build a life-course inventory for the subject, the spouse and the descendants

List the institutions each person passed through and check which kept questionnaires or autobiographies [S2]. Include:

- **The subject:** workplaces, schools, technical schools and universities, party membership, military service, any degree or award, emigration and return, and any loss of voting rights in the 1920s–1930s.
- **The children and grandchildren:** their school, student and workplace files. Their questionnaires had to name the parents and often the parents' workplace. Many entries give only a trade, such as "cutter in a studio" [S1], [S2].
- **The spouse:** the same set of institutions. A child's or spouse's file can name the wife's relatives and birthplaces [S2].
- **Kinship documents that are not vital records:** a court decision establishing maternity, the housing-office (ЖЭК) occupancy order and register, and the daughters' school and student files listing next of kin [S1].
- **Pre-1917 estate and registered town.** Check administrative lists, including ведомости справок о судимости (criminal-record certificate lists), for the person’s estate and приписка before searching Soviet catalogues [S2].

Search descendants’ party and student files for a parent’s birth, places, occupations and death. Record which relative supplied each detail [S9], [S2].

**Read a Soviet internal passport field by field.** Copy each mark literally: the ZAGS marks of marriage and divorce, the прописка and выписка (residence registration and deregistration) stamps as dated residences, the birthplace as written, and the children entries.

- Under the 1974 Passport Regulation, ZAGS enters the holder's children and the marriage and divorce marks, and internal-affairs bodies make the residence stamps. When a passport is exchanged or replaced, only children under 16 are entered in the new one, so the page is not a complete list of children [S19].
- Identify the passport model before you read an absence or an unexpected mark. The 1974 rules forbid any marks other than those they list [S19]. Earlier passports could carry a residence-restriction entry citing Article 38 or 39 of the passport regulations, which applied to released convicts. Treat such an entry as a lead to a conviction file [S20], [S21].

- **Privacy gate:** <!-- privacy-gate: request --> A passport application card names the holder's parents and spouse, who may be living; answer the privacy gate in `SKILL.md` before writing to a passport office.
- **When the passport is lost, ask for its application card.** A 2025 guide by Olehadash describes the Soviet passport application, «форма № 1» (in Russian Federation usage «форма 1П»), as used for the nationwide exchange of passports that began in 1976. Its lines include the birthplace in the administrative units of the day and the father's and mother's full names. The guide quotes an MVD letter that a copy of a dead person's form goes, on personal application, to heirs who accepted the inheritance or are first-order heirs and show documents proving inheritance or kinship. It sends the request to the migration unit of the MVD body for the address where the passport was issued, one request per address the person lived at from the mid-1970s, and warns that no office is obliged to issue the form [S52]. Prepare the kinship-proof chain of step 5 before you write.

- **Privacy gate:** <!-- privacy-gate: request --> A marriage record found through a labour book names both spouses, who may be living; answer the privacy gate in `SKILL.md` before requesting it from ZAGS.
- **Look for the labour book (трудовая книжка) in the family's papers, and read more than its job list.** The employer handed the book to the worker on the day of dismissal and, after a death, to the closest relatives against a signature (1974 USSR instruction, пп. 4.1, 4.3) [S75], so check family papers for the original [S76]. Under that instruction:
  - education was entered on the title page from a diploma or certificate, and periods of study at higher and secondary specialised schools were entered among the work records (пп. 2.10, 2.17) [S75]. Add those schools to the inventory;
  - a change of surname was entered by striking out the old surname with one line and writing the new one, with a reference to the document, such as the marriage certificate, on the inside of the cover (п. 2.12) [S75]. Request the справка using the certificate number and date [S77];
  - the awards and incentives sections give each award, thanks, bonus or certificate of honour with its date, who granted it and for what, but not bonuses paid under the pay system (пп. 2.21–2.24) [S75]. Each entry places the person at that employer on that date and names an occasion to look for in award papers [S78].

  If the book is lost, the pension file can hold copies of its pages (step 3, Pensions) [S76], [S79].

## 3. Route each institution to its series and present custodian

Write one row per locator and person, using the fields in the output register at the end of this recipe. The routes below are the ones the sources demonstrate, and each applies only to the archive and years named.

**Search the federal archives' finding aids by name first.** Rosarkhiv opened ГИС УИАД (online.archives.ru) on 25 September 2023. It searches the file-level inventories of 13 federal archives, among them ГАРФ, РГАЭ, РГАСПИ, РГВА and РГАНИ, by a word or with filters for archive, fond, opis and file titles, dates and document types, and at its launch it was free and needed no registration [S53 @2026-11-15], [S54 @2026-11-15]. Copy the archive, fond, opis and title from a name hit [S54 @2026-11-15]. From 10 September 2025 the system also shows scans from three federal archives (РГАДА, РГИА ДВ and РГАНТД), viewable only after a Gosuslugi login and online payment [S55 @2026-11-15]. From outside Russia the portal did not answer on 2026-11-15. Log each hit as a title-only candidate (step 5).

**Workplace.**

- **Privacy gate:** <!-- privacy-gate: request --> Workplace personnel files are kept for decades and their subjects may be living; answer the privacy gate in `SKILL.md` before writing to an enterprise or labour archive.
- **Retention and transfer.** In Russia, Art. 22.1 of Federal Law 125-FZ gives 75 years for personnel records closed before 1 January 2003 and 50 years for those closed after that date, subject to the applicable retention schedule and special service rules [S117]. After liquidation, check the city or district labour archive (трудовой архив) for the enterprise’s records [S1].
- **After a merger,** ask the successor enterprise and the labour archive which years and series each received [S1].
- **Get the enterprise's exact name before you write.** Labour archives store files in boxes by enterprise and year [S1]. Find the name in one of these places:
  - the executive-committee (ispolkom) fonds of an ordinary city archive, which hold branch lists of enterprises;
  - the fonds of the trusts the enterprise belonged to;
  - a telephone directory from the years the enterprise operated.

  Labour archives hold personal data, so expect to prove kinship [S1].
- **Check former names and numbers.** In one search, plant replies denying employment missed the lead to a numbered plant’s fond in the oblast archive [S2].
- **Search city archives too.** Check Moscow and St Petersburg personnel inventories under the employer, including ЦГА СПб, f. Р-1284 where relevant [S9], [S2].
- **Read the personal card.** Extract the birth date and village, stated nationality, party entry, education, employment dates and marital status where the card gives them [S8].

- **Before you write to a successor enterprise or a labour archive, look up where a liquidated organisation's personnel records went.** Some regional archive services publish interarchival or interagency guides (search for «справочник по личному составу» with the region's name) that map liquidated, renamed and reorganised organisations to the archive now holding their personnel records, with date ranges. The Republic of Khakassia's culture ministry describes its guide (Межархивный справочник документов по личному составу ликвидированных организаций) as covering the National Archive and the municipal archives, arranged by territory and fond number, current on 1 January 2026 and supplemented twice a year [S35 @2026-11-08]; the Pavlodar oblast archive in Kazakhstan describes a 2007 guide in two volumes (1922–2006 and 1992–2006), arranged by branch with an alphabetical index of organisations [S36 @2026-11-08]. An entry tells you where to ask, not whether a file survives, so confirm the holder on that archive's own site before you write.

**School, institute and university.**

- An admission file can contain a copy of the metrical birth record [S2].
- Look up each applicant separately in the university inventory (for Samara, ЦГАСО f. Р-28 op. 1). Keep each name hit as a title-only candidate until you inspect the file [S2].
- If the university still holds the file, ask what proof of kinship it requires for that series and date [S2].

**Party.**

- **District-committee personal files** are held in the regional party archive and searched in its online catalogue.
  - Keep each dated raikom file in a separate row, even under the same name in СОГАСПИ [S2].
  - Petrograd/Leningrad personal files for 1917–1950 are in ЦГАИПД СПб, f. Р-1728 (collection of personal files) [S2].
- **Perm ГАНИ.** Read the contents list for questionnaires, autobiographies, references, recommendations and protocol extracts. Confirm kinship requirements, copying charges and payment terms for the requested file [S3].
- **Raikom fonds.** Look for expulsion decisions and copy the grounds as stated in the protocol (for Perm in 1920–1922, check fond 13) [S3].
- **RGASPI** holds party registration and accounting cards.
  - Check the member’s card for parents’ birthplaces, ages, occupations, moves and deaths [S9].
  - **Privacy gate:** <!-- privacy-gate: request --> A party card names the member and relatives, some of whom may be living; answer the privacy gate in `SKILL.md` before requesting copies.
  - Ask what identifier the archive needs, including date of death for a search of cancelled cards, and confirm the ordering and payment terms [S2], [S59].
  - For listeners at the Institute of Social Sciences (ИОН), check RGASPI f. 585 op. 2 for the 1963–1989 inventory and ask what can be ordered [S2].
- **1922–1923 All-Russian census of party members** (Всероссийская перепись членов РКП(б)). Search the Sverdlovsk questionnaires in ЦДООСО f. 76 op. 1, including the UrFU «Анкеты» collection. Record each folio and search this series separately from repression lists [S7], [S8].

- **RGASPI requests: ask for every set, and give a key the archive files by.**
  - A registration form (регистрационный бланк) and an accounting card were filled in when a member joined and again at each exchange of party cards, in 1922, 1927, 1936, 1954 and 1973, and the earlier forms were kept [S56], [S57]. Ask for every set, including the original registration and subsequent exchanges [S58].
  - Ask for the registration form, not only the card. Its occupation table gives each period of study and work from and to by month and year, with the place, the organisation and the post, and so names the personnel files to request next [S57], [S58]. Its pre-1917 entries are self-reports: the guide warns that a member of non-proletarian origin could have written himself down as a peasant [S57].
  - RGASPI files the cards by party-card number. Without the number it searches the books of card issue by the date and place of joining, or the books of cancelled cards by the date and place of leaving the party, death included; that search costs more and takes longer [S59]. A death identifies the card only if it fell while party registration still ran, before 1991 [S57]. If you know little, ask the regional party archive for the card number first [S59].
  - Check the requirements for each file [S56], [S57]. One reported request produced the 1936 papers but required the member’s birth record for the 1954 papers [S60].

- **Komsomol (ВЛКСМ) membership** is filed in the Komsomol district-committee (райком) fonds of the regional archive of recent history, the former party archive [S59], [S61]. A 2026 Dzen guide describes the series there: yearly lists of members by school, technical school and enterprise (birth year, education, occupation, party membership, army service, address and card number); books of card issue; journals of members taken onto and struck off the register (address, where the member came from or left for); and the applications and questionnaires of new members, some with an autobiography [S61]. Work out the raikom from the residence, school or workplace before you search, because in a city with many districts the wrong raikom means reading many files [S61]. Estimate the joining year from the age rules of the period: 14 to 23 under the 1918 and 1924 rules, a minimum of 16 until it was lowered to 14 in November 1942, and 14 to 28 in the post-war decades [S61], [S62], [S63].

- **Ask the archive of the place where the member joined the party, not only of the home region.** A party personal file can be requested from the regional archive by the date and place of joining [S80]. A Dzen genealogist sends this request to the regional archive of recent history and warns that a member may have joined away from home [S81].

**Military.**

- **Privacy gate:** <!-- privacy-gate: request --> Military personal files list the nearest relatives, who may be living; answer the privacy gate in `SKILL.md` before writing to a commissariat or to ЦАМО.
- **Write to the military commissariat (военкомат) at the last residence.** Ask whether a personal file was opened and whether it includes a questionnaire naming relatives or an autobiography [S2].
- **Record what survived.** Ask whether the relevant card series was kept, transferred or destroyed before interpreting a negative reply [S1].
- **For officers,** request the officer personal file from the Ministry of Defence archive (ЦАМО). It holds more than a death certificate, including pre-war family details [S2].

- **For a man mobilised in 1941–1945, ask for his entry in the alphabetical book of those called up (алфавитная книга призванных по мобилизации).** Commissariats kept call-up books and amended them as fates became known; what an entry gives varies, and birth year, call-up date and address are not always there [S82]. One Kirov oblast commissariat reported keeping an alphabetical call-up book for these men without opening individual files or cards [S83]. Check the entry for rank group, residence and any later death or disappearance note.
- **A telephone "we have nothing" is not a reply.** Commissariats do not carry out requests made by telephone, and a written request can produce data after a telephone refusal. Send it by post with the kinship chain of step 5 [S82], [S84]. Ask about household-survey (подворный опрос) extracts and test a transposition of given name and patronymic [S85].

**Disenfranchised persons (лишенцы) and restoration of voting rights.**

- **Federal files.**
  - For GARF A-5248, search inventories by surname and check the special card indexes for files missed online [S10].
  - For 1934, check op. 13, «Личные дела лишенных избирательных прав» [S2].
  - Check current access and ordering arrangements, including whether the Yalutorovsk depository handles the file [S10], [S2].
  - Search voting-rights restoration files under a candidate patronymic and verify the relationship in the file [S2].
- **Regional lists** are arranged by okrug, district, village soviet and year. For Sverdlovsk, reported inventory leads point to ГАСО f. р-88, op. 9 [S4], [S5], [S6], [S12], [S13]:
  - d. 2, t. 1 (Sverdlovsk okrug, 1924);
  - d. 33, t. 2 (all okrugs, with correspondence, 1925);
  - d. 235 (Sverdlovsk okrug, 1929).
- **What an entry gives:** the status (служитель культа, wife of a cleric, просфорня), the occupation before and after the revolution, sometimes a birth year, and the village soviet [S6], [S12], [S13]. Record each entry as a dated observation of residence and status.
- **After a negative security-service or police reply**, search GARF’s voting-rights files under documented Russian name forms. A catalogue hit there is a candidate even if its name fits the family account [S10].

District executive-committee fonds can hold both lists and individual files. In the Leningrad oblast
archive in Vyborg (ЛОГАВ), f. Р-1907 (Kingisepp district executive committee), op. 2 (1927–1937) holds
a book of record and lists of disenfranchised people by village soviet, extracts of protocols on
deprivation and restoration of voting rights, protocols of the commission reviewing the lists, and
files titled with individual names. [S44 @2026-11-13] Search the district executive-committee fond as
well as GARF's лишенец files.

**Degree (VAK).**

- Attestation files of the Higher Attestation Commission are in GARF, f. Р-9506.
- For law-science doctors and professors, check op. 14 (1935–1969), including dd. 114–115 for 1947–1958. Confirm the ordering route with GARF. Check the dissertation’s opening pages for a biography naming parents or siblings [S2].

**Return from emigration.**

- GARF, f. А-327 (Main Resettlement Directorate), op. 1, holds files on receiving and resettling former émigrés.
- For arrivals from France in 1946–1947, check dd. 15 and 23–25 for lists, certificates and correspondence with resettlement departments. Search neighbouring file titles for the same route [S2].

**Civil award.**

- NARB f. 968 is the fond of the Supreme Soviet of the BSSR.
- Look for award sheets attached to the Presidium decrees on the Honorary Diploma, filed by award date. Check the sheet for position and workplace, birth date, nationality, party membership, education, home address and a short career note [S11].
- Trace the nomination through the enterprise and its party, trade-union and Komsomol organisations or the raikom. Look for the character reference in the enterprise records or in the raikom fond in the party archive [S11].
- **Soviet maternal awards** were created by the Presidium decree of 8 July 1944: «Мать-героиня» (Mother Heroine) for ten or more children, the order «Материнская слава» (Maternal Glory, III, II and I class) for seven, eight or nine, and the «Медаль материнства» (Motherhood Medal, II and I class) for five or six [S16], [S18].
  - Under the 1944 text, the award was made once the youngest child reached one year and while the mother's other children were alive, and it counted children killed or missing at the front [S16]. So the class reflects the children counted at the award date, not all births, and the award date shows only that the youngest child was at least a year old by then.
  - The USSR Supreme Soviet Presidium conferred Mother Heroine by decree, the union- and autonomous-republic Supreme Soviet presidiums awarded Maternal Glory and the Motherhood Medal, and oblast, city and district executive committees handed over those two awards (statutes of 18 August 1944, Vedomosti 1944 No. 45) [S17]. Search those bodies' fonds for the award papers, under the mother's own surname, which may differ from her children's. Read the rules in the edition in force at the award date.

- **Privacy gate:** <!-- privacy-gate: request --> Award papers name the awardee and, for maternal awards, the children, who may be living; answer the privacy gate in `SKILL.md` before ordering an award extract or asking an archive to confirm an award.
- **Use maternal-award papers as a list of children.** Check the district award protocols for each child’s full name and birth year. In the district archive, also look for wartime forced-labour lists if relevant [S86]. For Maternal Glory or the Motherhood Medal, check the republic Supreme Soviet’s lists and presentation protocols (Chuvashia, f. Р-1041 op. 18 d. 5 for a 1973 protocol) [S87].
- **To confirm a civil award, ask GARF as well as the regional archive.** A 2023 guide sends civil awards to GARF and regional archives, and military awards to «Память народа» and the Ministry of Defence archive [S80]. Ask GARF to identify the decision or confirm the award [S88]. GARF's fond 7523 holds a 1946 report compiled in the Presidium's department for recording and registering awardees (op. 17, d. 353) [S89].
- **Find the published award decree.** Search contemporary newspapers by oblast, year and award. Compare the person’s post, farm, district and any cited achievement before requesting the archival papers [S90], [S91], [S92].

- **Exhibition awards: search arhiv.vdnh.ru.** The VDNKh archive portal opened in 2020 with almost 11,500 award decisions of the All-Union Agricultural Exhibition (ВСХВ) and VDNKh for 1939–1991. It searches by surname, given name and patronymic, award date, region, award type and organisation or kolkhoz, and takes orders for a copy of an extract, sent by post [S93 @2026-11-16], [S94 @2026-11-16]. Its form asks for the surname, the organisation and the region as they were at the award date [S95 @2026-11-16]. If only the medal’s serial number is known, ask VDNKh staff whether it identifies the holder and award decision [S94 @2026-11-16].

  When the name finds nothing, search by region and surname, employer or kolkhoz, or a co-awardee named in a district history. Read the whole decision for misspellings, relatives and namesakes [S96], [S92].

**Residence.**

- House books record the workplace [S1].
- For Moscow, search ЦГА Москвы house books by address and full name and ask what proof of kinship is required for the dates [S2].
- For Leningrad, check the city archives website for surviving house books and taxpayer lists at a known address, and look there for relatives living at the same address [S2].
- **Privacy gate:** <!-- privacy-gate: request --> Detailed ZAGS extracts, especially for a child's birth, can be about people who are still living; answer the privacy gate in `SKILL.md` before requesting them.
- Detailed ZAGS extracts for a death, a marriage or a child's birth give addresses for these searches [S2].
- Check evacuation entries for an address and occupation, then use detailed ZAGS records, house books and any disenfranchisement file to test the household link [S2].

- **For a rural family, add the village-soviet household books (похозяйственные книги).** Village soviets kept them from 1934 (decree No. 185 of 26 January 1934 of the СНК СССР, the USSR Council of People's Commissars), one entry per household beginning with its head [S14 @2026-11-02].
  - They now sit in district or city archives, sometimes in the oblast state archive, and some are still with the local administration [S14 @2026-11-02], [S15 @2026-11-02]. Runs can start late: in the Minsk oblast state archive most districts' books survive only from 1944 [S15 @2026-11-02].
  - **Privacy gate:** <!-- privacy-gate: request --> Household-book entries list every household member and their age, and some may still be living; answer the privacy gate in `SKILL.md` before requesting an entry or a surname search.
  - Request the book for the named settlement and period and the entry for the household of the named head, with name variants, and ask whether a copy of the family-composition entry is possible. If the head is unknown, request a surname search within that settlement and ask its terms.
  - An entry lists the members, their relation to the head and their age, with marks of arrival in and departure from the household. The form changed several times between 1934 and 1975, so read the columns of the book you receive [S14 @2026-11-02].

  - **For a book less than 75 years old, prove kinship in the request.** A 2023 Dzen guide says kinship must be proved for a household book less than 75 years old, the term of the closure in step 5, so the cut-off year moves forward each year [S64]. State how each household member is related to you and offer copies of the kinship documents. Ask whether the archive can supply a certified copy [S64].

  - **When ZAGS has no rural death**, check household-book departure marks for a death date, wartime loss, move, call-up or demobilisation. Use a dated lead to renew the ZAGS request and check a copied birth year independently [S97], [S98].
  - **Follow the household into later books.** Identify the actual years each volume covers and request the whole surviving run. A household still present at the end of one book gives a starting point for the next [S98], [S99].

  - **If the household books are lost, look for the kolkhoz's own records.** In the Mari El state archive, the fond of kolkhoz «Ноля» (f. Р-420, op. 1) holds members' personal accounts for 1933–1934, a household book of its members for 1936 and labour-day books (книги учёта трудодней) for 1938, 1939 and 1941 [S37 @2026-11-08]. Records of liquidated kolkhozes can also sit in a district archive that confirms former workers' service and pay for pensions, as in Sysert [S38 @2026-11-08], so search both the kolkhoz fonds and the personnel (по личному составу) fonds.

- **Privacy gate:** <!-- privacy-gate: request --> An apartment card lists everyone registered in a flat, some of whom may be living; answer the privacy gate in `SKILL.md` before requesting a copy or an extract.
- **For a city flat, ask for the apartment card (поквартирная карточка).** Cards are no longer issued; a copy of, or extract from, a card made before 17 April 2018 is requested from the city's archive service with an application, a passport and proof of ownership of the flat [S100 @2026-11-16].

  If the city archive service has no card, ask the МФЦ or passport office about a registration extract listing arrivals and departures. Confirm the kinship or ownership documents required for that flat [S86].

**Collectivisation-era village records.** Check church-closure files for kolkhoz attendance lists, which can name the chairman, secretary and members. One reported locator is ГАСО f. Р-102 op. 1 d. 865, 1930, folios 13–17 [S12].

**Trace a kolkhoz through its mergers and district changes.** In the Batyrevo district archive (Chuvashia), «колхоз им. Ленина» of Nizhneye Turmyshevo merged in September 1950 with the «Авангард» kolkhoz of Verkhneye Atykovo, after the party resolution of 30 May 1950 on merging small kolkhozes, and kept its name; it changed district three times, merged into «Россия» in 1959, and its 1950–1959 files sit in f. 213, the united fond of the amalgamated kolkhoz «Знамя» [S39 @2026-11-08]. Take the farm's village soviet and district from its fond title, as most kolkhoz fond titles in the Mari El state archive's list of agricultural fonds give them, before you search a gazetteer [S40 @2026-11-08].

**Pensions.** A reported Kharkiv file for a 1962 death contradicts the suggestion that all pension files were destroyed five years after death [S1]. Ask the office about its holdings for the year, including transfers after a move.

- **Privacy gate:** <!-- privacy-gate: request --> A pension file holds the pensioner's family documents, which name a spouse and children who may be living; answer the privacy gate in `SKILL.md` before requesting one.
- **Russia: request a dead pensioner's pension file (пенсионное дело) from the Social Fund.** The Social Fund of Russia (СФР), formed by reorganising the Pension Fund (ПФР), began work on 1 January 2023 [S101]. Apply in your own name to the regional branch that holds the file, as a rule that of the place of death or the one that paid the pension; attach copies of the kinship documents, and ask for the personal documents (work, education, birth, marriage, children, wartime service), not the pension amounts [S104]. When a pensioner moves, the branch of the new residence requests the file from the branch of the former one [S102]. Check the branch at the previous residence if the current one has no file [S103].
- **What to request.** Look for copies of the labour book or workplace certificates [S79], children’s birth and marriage certificates and survivor-pension papers [S86], kolkhoz work certificates or witness protocols [S68], and military-service certificates naming the issuing commissariat [S105]. Request the supporting papers whether the labour book is lost [S106] or survives [S107].

- **Request it soon after a death.** Since 15 June 2025 an old-age pension recipient's payment file is kept 15 years from the date payments stopped, down from 20 years [S108 @2026-11-16]; a survivor-pension file is kept 10 years, and a disability pensioner's file 5 years after death, or 3 years when the disability is recorded in the unified social-sector platform [S116 @2026-11-16]. For Russia, use these terms, not the forum estimates above.

- **An older file may be gone.** After a cut in storage terms in April 2021, files were destroyed in bulk, though a few regions sent them to the regional archive [S79]. So the cut-off moves forward every year, and the files of the earlier generation are usually gone [S106]. Ask for an older file anyway: single documents can survive, especially for war veterans who died in the 1990s [S104].

**Death and inheritance (Russia).** The Federal Notarial Chamber's probate-case register (Реестр наследственных дел, notariat.ru) has run in the notarial information system since 1 July 2014 [S29]. It is an auxiliary index of opened inheritance cases, not a death record and not proof of kinship.

- Names match exactly: a query without a patronymic finds only cases recorded without one. Birth and death dates may be partial or left out; if a doubtful date filter returns nothing, retry without it. The form limits the number of queries per period of time [S28].
- A year in the case number is not the death year. The register states no coverage period, so completeness for older deaths is unknown and a miss is not a negative [S28].
- The notarial district does not prove the last residence. When the last residence is unknown or abroad, the inheritance opens where the inherited property in Russia lies, immovable property (or its most valuable part) first (Civil Code, Art. 1115, Part 2) [S30], [S31].
- Do not collect living heirs' addresses or contacts. For the grave itself, use the Russian cemetery-database rules in [burial evidence packet § 2](burial-evidence-packet.md#2-search-the-recorded-name-fields-separately).

## 4. Search under every name the person actually used

- **Search the Russified civil name and patronymic used in daily life,** not only the Yiddish or birth form.
  - Ask which civil name the family used, search it in the relevant fonds and check the file before linking a catalogue hit to the person [S10].
  - A change of name could be official (an annotation in the metrical entry) or unofficial (new documents written from the person's own words) [S2].
  - Check the margins of the original synagogue record for a later ZAGS name annotation, including in red ink [S1].
- **Search clerk-written variants.** Compare double, shortened and Russian forms across the children’s birth records. A spelling difference or an unexpected wartime patronymic needs corroboration before you infer a formal change [S1], [S4].
- **Search a rare given name twice.** In regional and federal catalogues, look for the person under that given name and possible descendants under the matching patronymic. Verify each relationship in the file [S2].
- **Do not search under a nickname alone.** Ask whether any document was issued in that name [S2].

- **Search the press for a surname-change notice.** Under the 1918 decree, a citizen changing a surname applied to ZAGS and placed a paid newspaper notice, most often in «Известия», giving the old and new surname; such notices ran until the late 1930s, and the change was registered about two months later if no interested person objected [S109]. Check whether the notice names other family members [S110] or an office receiving objections [S111]. Search the central and local papers of the likely years under both surnames: a notice links the two names with a date.

## 5. Log each catalogue hit as a candidate with its own locator

- **One row per locator.** Keep every fond/opis/delo with its date range as a separate row, even when several rows probably belong to one person. Mark each row *title only* or *file inspected*. Treat each file as a separate request [S2].
- **A name match is a candidate.** Test namesakes and proposed relatives against the identifiers in the file [S2], [S13].
- **Rank an estimate mismatch.** A birth year or town estimated from a relative’s party card may disagree with a birth entry. Record the conflict and check both sources before excluding the candidate [S9]. Leave the identity ruling to evidence/proof judgment.
- **Privacy gate:** <!-- privacy-gate: request --> Requests for personal-file copies, archival certificates or kinship-proof certificates can concern people who may be living; answer the privacy gate in `SKILL.md` before sending each one.
- **Request status is part of the row.** Distinguish a request for copies from a request for an archival certificate (архивная справка). Check eligibility for each with the archive [S2].
- **Build a kinship-proof chain only from documents the user holds.** When an archive requires proof of kinship for a personal file, make each missing link (for example one generation's birth or marriage certificate) its own early request. It gates access to that file only; carry on with the other searches. In Russia the basis is Federal Law 125-FZ, Art. 25, Part 3: archival documents containing a citizen's personal or family secrets or private life are closed for 75 years from the document's creation, and before then open only with the person's written permission or, after death, that of their heirs [S32].

- **List every link the chain needs.** For ZAGS, assemble your passport, your birth record and, if your surname changed, your marriage record; each generation's birth record up to the one that names the ancestor; a marriage record for each woman whose surname changed, and every marriage and divorce record when it changed more than once; and a death record for each dead link [S69]. For a collateral relative, such as a grandfather's sister, add her own birth, marriage and death records to the line of the common ancestor. Bring originals or certified copies, and if some records are missing, request them all at once: the clerk checks the whole chain together and issues them together, with a state fee for each [S112].
- **Bridge spelling differences.** A reported ZAGS request was refused because two siblings’ birth records spelled their surname differently [S113]. Look for another record linking the names. If the link remains disputed, establishing kinship is among the facts covered by Civil Procedure Code Art. 264, Part 2, item 1 [S114].

## 6. Read questionnaires and autobiographies as dated self-reports

- **Record context with every field.** Note the date, the form type and its purpose: party admission, employment, award nomination or attestation. Do not record a field as a fact about the person.
- **Social origin and class.** Read a party questionnaire alongside any expulsion decision, recording the stated grounds. An autobiography can supply a birth date and village to test when the parish entry is missing [S3].
- **Nationality.** Compare the value in each military, workplace and family source. Record changes, omissions and conflicts with oral accounts without inferring ancestry or concealment from a discrepancy [S1], [S2], [S9].

  Log each stated nationality with its date, form and informant. Seek independent evidence and check the children’s questionnaires for the parents’ names [S2].
- **Treat each listed place as an observation.** Transcribe any question mark and compare duplicate extracts before assigning the village [S4].
- **Read a birth date against both calendars.** An Orthodox metrical date, like other Russian dates written before 14 February 1918, is normally Old Style; check the document's own calendar note [S33]. A questionnaire may restate the metrical birth date in New Style, so a difference of 12 or 13 days is not by itself a conflict. Record both dates with their calendar; for the offsets, use [evidence/proof judgment: follow record versions and test disputed dates](evidence-proof-judgment.md#follow-record-versions-and-test-disputed-dates).

- **Read a fact confirmed by witnesses as later testimony.** When work records were lost, the RSFSR pension law of 1990 let work service be established on the testimony of two or more witnesses (Art. 97) [S115]. Check pension files for work-service testimony and applications establishing a date of birth. Record the protocol date and witnesses separately from the event date [S68].

## Output: personal-file register

Return one row per locator and person (subject, spouse, child, grandchild). Each row gives:

- the institution and years;
- the file class;
- the custodian today;
- the locator (fond/opis/delo/folio or volume) and its date range;
- the name form searched;
- the match basis: name only, or corroborated by a named independent field;
- the level reached: title only, certificate or inspected file;
- the request status: copies or certificate requested, kinship documents sent, fee invoiced, reply received.

Keep the observations from inspected questionnaires and autobiographies in a separate list, each with its writer, date and purpose. Keep negative replies with their exact wording and the years they cover.
