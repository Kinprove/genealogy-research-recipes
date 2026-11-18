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
router: {"section": "Records by country and region", "group": "Russian Empire and Soviet Union", "order": 68}
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
  - In one case the reply also said that a neighbouring parish's books for that year had never reached the archive. The researcher noticed this only on rereading, after a party file had already confirmed the birthplace [S3].
- **Check a "not preserved" reply against the archive's own inventory or online images where you can.** A participant said that one archive had reported no interwar Jewish metrical book for a town, yet its inventory listed a combined births-and-deaths book for 1922–1928. The participant suggested that only one event type might be missing for one year [S2].
- **For an Orthodox parish, ask about the second copy.** The second copy of the metrical book was kept at the consistory. A participant reported that the modern diocesan administration answers requests by sending people to the state archive [S3].
- **Privacy gate:** <!-- privacy-gate: request --> A ZAGS search or repeat-document request can concern acts naming people who may still be living; answer the privacy gate in `SKILL.md` first.
- **Russia: a ZAGS or Gosuslugi "not found" may cover only the electronic register.** When an act is not in the unified register (ЕГР ЗАГС), the law requires a check of the paper record (Federal Law 143-FZ, Art. 9, Part 4). Ask whether that office's paper books for the year were searched, and how a missing record is found and entered [S25].
  - Any ZAGS office accepts an in-person request for a repeat certificate or extract; it need not be the office that registered the event. Issue is same-day when the act is in the register; otherwise the office searches the paper record, which in Moscow takes up to 30 days [S25], [S27].
  - Moscow reported in December 2020 that its whole ZAGS archive from 1926 was digitised and can be requested at any ZAGS in Russia. Its "Мои документы" (My Documents) service centres also issue repeat ZAGS documents [S26], [S27].
- **Privacy gate:** <!-- privacy-gate: request --> A Ukrainian civil-status request, even for an act over 75 years old, can name people who are still living; answer the privacy gate in `SKILL.md` before writing to an archive, a ДРАЦС or a consulate.
- **Ukraine: route a civil-status request by the act's age.** Civil-registration offices (ДРАЦС) keep the act books for 75 years from the act's date. They then transfer them each year to the state archive of the oblast, of Kyiv or Sevastopol, or of the Autonomous Republic of Crimea (Ministry of Justice order No. 2804/5 of 30.12.2013, §§ II.1, V.1) [S22]. Send a request for an older act to that state archive, not to the ДРАЦС, unless it is a metrical-book entry bound into a combined book whose storage term at the office has not ended: the office keeps that book and issues copies from it [S34]. Russia's custody term differs: see [Russian-Empire Jewish metrical-book recovery § 6](russian-empire-jewish-metrical-book-recovery.md#6-switch-to-zags-registers-when-the-territory-changed-over).
  - A repeat certificate of a living person's own birth is a later derivative of the act, and requesting one is that person's own action. Read it as [§ 4 of that recipe](russian-empire-jewish-metrical-book-recovery.md#4-when-the-book-is-lost-search-for-named-substitutes) reads Soviet repeat certificates.
  - Diia (the Ukrainian state services portal) can order repeat certificates and extracts, but the application must be signed with a Ukrainian qualified electronic signature (КЕП) or Diia.Signature. Ukrposhta delivery of the result is available only within Ukraine (Diia notice of 10.07.2026, checked 2026-11-02). From abroad, apply through a Ukrainian consulate [S23], [S24].
- **Then stop chasing the register.** Participants reported the Jewish metrical books of Starodub and Kremenchug as not surviving. For losses like these they gave one instruction: work from Soviet-period files on work, study, evacuation and party membership [S2].

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
the units of that time, not as a modern address. A Tula-region researcher reports a repeat certificate
placing a birth in a village of a "Karachevsky district" of Tula oblast. A Karachevsky district
existed in Tula guberniya only from 1924 to November 1926, on land of the former Epifan uezd, and
the 1899 birth was in the metrical book of a neighbouring village's church. [S50], [S51] Check each
named unit against the administrative history of its date before you choose a parish.

**A record number does not replace the kinship chain.** For a dead person, Art. 9 of 143-FZ lets
ZAGS issue documents to a relative or another interested person, who shows an identity document and
documents proving the right to receive them (Parts 2 and 7). For a living adult, a repeat certificate
goes only to that person, to the guardian of a person declared legally incapable, or to someone
holding a notarised power of attorney from one of them; once the child is of age, a parent may ask
only for another document confirming the birth registration (Part 2). [S65]
A Dzen author who knew the number and date of a 1938 death record could not obtain the справка
because her kinship documents were incomplete [S68], and her mother was asked for the author's power
of attorney to obtain the author's birth and marriage справки. [S69] Build the chain of step 5 before
you apply.

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

Early Soviet books also sit elsewhere: a Dzen author read ZAGS books partly covering 1920–1924 in a
district archive in Krasnodar krai, and one ZAGS archive told her it held nothing before 1941
because the earlier books were with an inter-district ZAGS subdivision, which then forwarded her
request upward. [S71] Ask which body holds the earlier books before you treat the years as lost.

**A marriage of 1927–1944 may never have been registered.** The RSFSR code on marriage and the
family of 1926, in force from 1 January 1927, treated a de facto marriage as the legal equal of a
registered one. [S72], [S73] The decree of 8 July 1944 gave legal effect only to a registered
marriage and let couples already living together register, stating how long they had lived together
(Art. 19). [S74] So when no marriage is found for a couple of that period, search for a registration
after July 1944 and read its cohabitation date. Children's birth records naming both parents do not
show that the marriage was registered.

## 2. Build a life-course inventory for the subject, the spouse and the descendants

List every institution each person passed through. In each of them the person filled in a questionnaire and wrote an autobiography [S2]. Include:

- **The subject:** workplaces, schools, technical schools and universities, party membership, military service, any degree or award, emigration and return, and any loss of voting rights in the 1920s–1930s.
- **The children and grandchildren:** their school, student and workplace files. Their questionnaires had to name the parents and often the parents' workplace. Many entries give only a trade, such as "cutter in a studio" [S1], [S2].
- **The spouse:** the same set of institutions. A child's or spouse's file can name the wife's relatives and birthplaces [S2].
- **Kinship documents that are not vital records:** a court decision establishing maternity, the housing-office (ЖЭК) occupancy order and register, and the daughters' school and student files listing next of kin [S1].
- **Any pre-1917 social estate or town of registration** that turns up in an administrative list. A participant used a 1908 list of criminal-record certificates (ведомость справок о судимости) to fix the приписка before searching Soviet catalogues. The list gave the estate as мещанин of a named town [S2].

Do not stop at the subject's own files. A descendant's file can hold the parents' details even when nothing survives for the parents themselves. In one worked case, a son's party registration card gave his father's birth-year range, birthplace, occupations and year of death [S9]. In other cases participants pointed to a son's party files and to two sisters' university files as the next requests [S2].

**Read a Soviet internal passport field by field.** Copy each mark literally: the ZAGS marks of marriage and divorce, the прописка and выписка (residence registration and deregistration) stamps as dated residences, the birthplace as written, and the children entries.

- Under the 1974 Passport Regulation, ZAGS enters the holder's children and the marriage and divorce marks, and internal-affairs bodies make the residence stamps. When a passport is exchanged or replaced, only children under 16 are entered in the new one, so the page is not a complete list of children [S19].
- Identify the passport model before you read an absence or an unexpected mark. The 1974 rules forbid any marks other than those they list [S19]. Earlier passports could carry a residence-restriction entry citing Article 38 or 39 of the passport regulations, which applied to released convicts. Treat such an entry as a lead to a conviction file [S20], [S21].

- **Privacy gate:** <!-- privacy-gate: request --> A passport application card names the holder's parents and spouse, who may be living; answer the privacy gate in `SKILL.md` before writing to a passport office.
- **When the passport is lost, ask for its application card.** A 2025 guide by Olehadash describes the Soviet passport application, «форма № 1» (in Russian Federation usage «форма 1П»), as used for the nationwide exchange of passports that began in 1976. Its lines include the birthplace in the administrative units of the day and the father's and mother's full names. The guide quotes an MVD letter that a copy of a dead person's form goes, on personal application, to heirs who accepted the inheritance or are first-order heirs and show documents proving inheritance or kinship. It sends the request to the migration unit of the MVD body for the address where the passport was issued, one request per address the person lived at from the mid-1970s, and warns that no office is obliged to issue the form [S52]. Prepare the kinship-proof chain of step 5 before you write.

- **Privacy gate:** <!-- privacy-gate: request --> A marriage record found through a labour book names both spouses, who may be living; answer the privacy gate in `SKILL.md` before requesting it from ZAGS.
- **Look for the labour book (трудовая книжка) in the family's papers, and read more than its job list.** The employer handed the book to the worker on the day of dismissal and, after a death, to the closest relatives against a signature (1974 USSR instruction, пп. 4.1, 4.3) [S75], so originals survive at home: a Dzen genealogist keeps several in her family archive [S76]. Under that instruction:
  - education was entered on the title page from a diploma or certificate, and periods of study at higher and secondary specialised schools were entered among the work records (пп. 2.10, 2.17) [S75]. Add those schools to the inventory;
  - a change of surname was entered by striking out the old surname with one line and writing the new one, with a reference to the document, such as the marriage certificate, on the inside of the cover (п. 2.12) [S75]. A Dzen author took a relative's marriage-certificate number from such an entry and obtained the marriage справка from the ZAGS of the event [S77]. Request the record with that number and date;
  - the awards and incentives sections give each award, thanks, bonus or certificate of honour with its date, who granted it and for what, but not bonuses paid under the pay system (пп. 2.21–2.24) [S75]. A Dzen example shows 1973–1975 entries for a May Day bonus and certificate of honour [S78]. Each entry places the person at that employer on that date and names an occasion to look for in award papers.

  If the book is lost, the pension file can hold copies of its pages (step 3, Pensions) [S76], [S79].

## 3. Route each institution to its series and present custodian

Write one row per locator and person, using the fields in the output register at the end of this recipe. The routes below are the ones the sources demonstrate, and each applies only to the archive and years named.

**Search the federal archives' finding aids by name first.** Rosarkhiv opened ГИС УИАД (online.archives.ru) on 25 September 2023. It searches the file-level inventories of 13 federal archives, among them ГАРФ, РГАЭ, РГАСПИ, РГВА and РГАНИ, by a word or with filters for archive, fond, opis and file titles, dates and document types, and at its launch it was free and needed no registration [S53 @2026-11-15], [S54 @2026-11-15]. In a 2024 Dzen post, a search on a great-grandfather's full name returned the archive, fond, opis and title of his personnel file in РГАЭ, and the author warns that such a hit can be a namesake's [S54 @2026-11-15]. From 10 September 2025 the system also shows scans from three federal archives (РГАДА, РГИА ДВ and РГАНТД), viewable only after a Gosuslugi login and online payment [S55 @2026-11-15]. From outside Russia the portal did not answer on 2026-11-15. Log each hit as a title-only candidate (step 5).

**Workplace.**

- **Privacy gate:** <!-- privacy-gate: request --> Workplace personnel files are kept for decades and their subjects may be living; answer the privacy gate in `SKILL.md` before writing to an enterprise or labour archive.
- **Retention and transfer.** The enterprise keeps the personnel file or card for a fixed period. In Russia that period is 75 years for files closed before 1 January 2003 and 50 years for files closed from 2003 on (Federal Law 125-FZ, Art. 22.1). A participant writing from Ukraine in 2015 gave the 75-year figure. When an enterprise is liquidated, its files go to the city or district labour archive (трудовой архив) [S1].
- **After a merger,** ask the successor enterprise first and then the labour archive. Files went to both. One participant found 1950s–1960s cards in a labour archive and late-1940s cards in the personnel archive of a working institution [S1].
- **Get the enterprise's exact name before you write.** Labour archives store files in boxes by enterprise and year [S1]. Find the name in one of these places:
  - the executive-committee (ispolkom) fonds of an ordinary city archive, which hold branch lists of enterprises;
  - the fonds of the trusts the enterprise belonged to;
  - a telephone directory from the years the enterprise operated.

  Labour archives hold personal data, so expect to prove kinship [S1].
- **A dead end at the enterprise can be a naming problem.** One researcher was told by every plant he wrote to that his grandfather had never worked there. A participant pointed him to the large fonds of a former numbered plant held in the oblast archive [S2].
- **Workplace files also turn up in city archives.** One worked case received a workplace personal file from the Moscow central city archive (ЦГАМ), together with a party-penalty protocol [S9]. A participant quoted a 1921 entry from a personnel inventory in ЦГА СПб, f. Р-1284 [S2].
- **What a card gives.** A 1961 enterprise personal card quoted from the Urals gives birth date and village, nationality, year of party entry, education, last job, years employed and marital status [S8].

- **Before you write to a successor enterprise or a labour archive, look up where a liquidated organisation's personnel records went.** Some regional archive services publish interarchival or interagency guides (search for «справочник по личному составу» with the region's name) that map liquidated, renamed and reorganised organisations to the archive now holding their personnel records, with date ranges. The Republic of Khakassia's culture ministry describes its guide (Межархивный справочник документов по личному составу ликвидированных организаций) as covering the National Archive and the municipal archives, arranged by territory and fond number, current on 1 January 2026 and supplemented twice a year [S35 @2026-11-08]; the Pavlodar oblast archive in Kazakhstan describes a 2007 guide in two volumes (1922–2006 and 1992–2006), arranged by branch with an alphabetical index of organisations [S36 @2026-11-08]. An entry tells you where to ask, not whether a file survives, so confirm the holder on that archive's own site before you write.

**School, institute and university.**

- An admission file can contain a copy of the metrical birth record [S2].
- The Samara university fond (ЦГАСО, f. Р-28, op. 1) has two 1920 catalogue entries for two sisters found by name, each a separate request. The participant advised requesting them, so they remain title-only candidates [S2].
- A participant said that university personal files still held in the university's own archive need kinship documents, whatever their date [S2].

**Party.**

- **District-committee personal files** are held in the regional party archive and searched in its online catalogue.
  - A participant listed six district-committee personal-file hits under one name at the Samara party archive СОГАСПИ, dated 1942–1959, each a separate request [S2]. Each stays a title-only candidate until inspected.
  - Petrograd/Leningrad personal files for 1917–1950 are in ЦГАИПД СПб, f. Р-1728 (collection of personal files) [S2].
- **Perm ГАНИ.** A participant reported this sequence [S3]:
  - The archive answered an email request sent without kinship documents.
  - The reply listed the file's contents: a candidate's questionnaire, an autobiography, a character reference, three recommendations and two protocol extracts.
  - It quoted a per-page fee for copies or scans.
  - Work began only after payment.
- **Raikom fonds** can show party membership and expulsions. A participant reported that a Perm raikom fond for 1920–1922 (fond 13) recorded one member's 1922 expulsion for having employed hired workers in 1904 [S3].
- **RGASPI** holds party registration and accounting cards.
  - One card, filled in on 23 June 1941, gave the father's birth-year range, birthplace, occupation before and after 1917, a move in 1921 and death in 1935 [S9].
  - **Privacy gate:** <!-- privacy-gate: request --> A party card names the member and relatives, some of whom may be living; answer the privacy gate in `SKILL.md` before requesting copies.
  - Participants reported the steps: request copies by email, receive an invoice, get scans after payment. They said a request works best with an exact death date [S2].
  - RGASPI f. 585 is the fond of the Institute of Social Sciences (ИОН). One participant said that its op. 2 (listeners' files) has an inventory dated 1963–1989 and that RGASPI was not then fulfilling requests for that fond [S2].
- **The 1922–1923 All-Russian census of party members** (Всероссийская перепись членов РКП(б)). Questionnaires for the Sverdlovsk region are in ЦДООСО, f. 76, op. 1. They are digitised in the UrFU archive (idun.urfu.ru, "Анкеты" collection) and cited by folio. A participant pointed out that researchers search only the repression lists and miss this series [S7], [S8].

- **RGASPI requests: ask for every set, and give a key the archive files by.**
  - A registration form (регистрационный бланк) and an accounting card were filled in when a member joined and again at each exchange of party cards, in 1922, 1927, 1936, 1954 and 1973, and the earlier forms were kept [S56], [S57]. One researcher received two registration forms for one man from RGASPI, filled in when he joined in 1953 and at the 1954 exchange [S58]. Ask for every set in the file.
  - Ask for the registration form, not only the card. Its occupation table gives each period of study and work from and to by month and year, with the place, the organisation and the post, and so names the personnel files to request next [S57], [S58]. Its pre-1917 entries are self-reports: the guide warns that a member of non-proletarian origin could have written himself down as a peasant [S57].
  - RGASPI files the cards by party-card number. Without the number it searches the books of card issue by the date and place of joining, or the books of cancelled cards by the date and place of leaving the party, death included; that search costs more and takes longer [S59]. A death identifies the card only if it fell while party registration still ran, before 1991 [S57]. If you know little, ask the regional party archive for the card number first [S59].
  - Expect a kinship question. The guide says RGASPI asked for no proof of kinship [S57], but an article on party records says a written request may need documentary proof [S56], and one researcher received a 1936 file but not the 1954 one, because the member's birth record was required [S60].

- **Komsomol (ВЛКСМ) membership** is filed in the Komsomol district-committee (райком) fonds of the regional archive of recent history, the former party archive [S59], [S61]. A 2026 Dzen guide describes the series there: yearly lists of members by school, technical school and enterprise (birth year, education, occupation, party membership, army service, address and card number); books of card issue; journals of members taken onto and struck off the register (address, where the member came from or left for); and the applications and questionnaires of new members, some with an autobiography [S61]. Work out the raikom from the residence, school or workplace before you search, because in a city with many districts the wrong raikom means reading many files [S61]. Estimate the joining year from the age rules of the period: 14 to 23 under the 1918 and 1924 rules, a minimum of 16 until it was lowered to 14 in November 1942, and 14 to 28 in the post-war decades [S61], [S62], [S63].

- **Ask the archive of the place where the member joined the party, not only of the home region.** A party personal file can be requested from the regional archive by the date and place of joining [S80]. A Dzen genealogist sends this request to the regional archive of recent history and warns that a member may have joined away from home [S81].

**Military.**

- **Privacy gate:** <!-- privacy-gate: request --> Military personal files list the nearest relatives, who may be living; answer the privacy gate in `SKILL.md` before writing to a commissariat or to ЦАМО.
- **Write to the military commissariat (военкомат) at the last residence** for the personal file. It holds a questionnaire listing the nearest relatives, and an autobiography. A participant noted that under universal conscription every man had such a file [S2].
- **Card archives may be gone.** A participant reported that one city commissariat destroyed its card archives in the 2000s [S1]. Record a negative reply as a holdings result, not as proof that no file ever existed.
- **For officers,** request the officer personal file from the Ministry of Defence archive (ЦАМО). It holds more than a death certificate, including pre-war family details [S2].

- **For a man mobilised in 1941–1945, ask for his entry in the alphabetical book of those called up (алфавитная книга призванных по мобилизации).** Commissariats kept call-up books and amended them as fates became known; what an entry gives varies, and birth year, call-up date and address are not always there [S82]. In 2020 one commissariat in Kirov oblast answered a Dzen author that its book gave the name, birth year, residence or birthplace, rank group and call-up date, that a reported death or disappearance was noted against the name, and that no personal file or registration card was opened for these men [S83]. So a wartime mobilisee need not have the personal file described above.
- **A telephone "we have nothing" is not a reply.** Commissariats do not carry out requests made by telephone, and a written request can produce data after a telephone refusal. Send it by post with the kinship chain of step 5 [S82], [S84]. A Dzen author who did so received a household-survey (подворный опрос) extract recording one great-grandfather as missing, and learnt that another's given name and patronymic had been swapped in the records, which explained her failed searches [S85].

**Disenfranchised persons (лишенцы) and restoration of voting rights.**

- **Federal files.**
  - GARF fond A-5248 holds the personal files. Its inventories are arranged by surname, not by region: choose an opis on opisi.garf.su and filter by surname. The online search misses files that GARF's special card indexes still catch [S10].
  - A participant cited op. 13 ("Личные дела лишенных избирательных прав. 1934") as the inventory holding an individual disenfranchisement file from 1934 [S2].
  - One participant said that no proof of kinship was required [S10].
  - Another advised ordering a Moscow лишенец file from GARF's Yalutorovsk depository [S2].
  - A participant also found a GARF catalogue entry on restoring voting rights for a person bearing the searched patronymic. It is a candidate, not a confirmed child [S2].
- **Regional lists** are arranged by okrug, district, village soviet and year. A participant quoted these Sverdlovsk examples from database excerpts of ГАСО f. р-88, op. 9 [S4], [S5], [S6], [S12], [S13]:
  - d. 2, t. 1 (Sverdlovsk okrug, 1924);
  - d. 33, t. 2 (all okrugs, with correspondence, 1925);
  - d. 235 (Sverdlovsk okrug, 1929).
- **What an entry gives:** the status (служитель культа, wife of a cleric, просфорня), the occupation before and after the revolution, sometimes a birth year, and the village soviet [S6], [S12], [S13]. Record each entry as a dated observation of residence and status.
- **This series is separate from the security-service files.** In one case the KGB of Belarus and the Interior Ministry information centre both reported no data. A participant then found an inventory entry in GARF's лишенец files under a Russian name and patronymic that the woman might have used. The thread does not confirm that the entry was hers [S10].

District executive-committee fonds can hold both lists and individual files. In the Leningrad oblast
archive in Vyborg (ЛОГАВ), f. Р-1907 (Kingisepp district executive committee), op. 2 (1927–1937) holds
a book of record and lists of disenfranchised people by village soviet, extracts of protocols on
deprivation and restoration of voting rights, protocols of the commission reviewing the lists, and
files titled with individual names. [S44 @2026-11-13] Search the district executive-committee fond as
well as GARF's лишенец files.

**Degree (VAK).**

- Attestation files of the Higher Attestation Commission are in GARF, f. Р-9506.
- A participant cited op. 14, law sciences (doctors and professors), 1935–1969, with d. 114–115 in two volumes for 1947–1958, and advised ordering them through Yalutorovsk.
- The same participant noted that dissertations usually open with a short biographical part, sometimes covering parents and siblings [S2].

**Return from emigration.**

- GARF, f. А-327 (Main Resettlement Directorate), op. 1, holds files on receiving and resettling former émigrés.
- A participant cited d. 15 and d. 23–25 on émigrés arriving from France in 1946–1947. These are lists, certificates and correspondence with resettlement departments. The participant said there are "a couple dozen" more [S2].

**Civil award.**

- NARB f. 968 is the fond of the Supreme Soviet of the BSSR.
- A participant reported that it holds award sheets attached to the Presidium decrees on the Honorary Diploma, filed by award date. The sheets give position and workplace, birth date, nationality, party membership, education, home address and a short career note [S11].
- Participants said the nomination came from the enterprise together with its party, trade-union and Komsomol organisations, or from a raikom. Look for the character reference in the enterprise records or in the raikom fond in the party archive [S11].
- **Soviet maternal awards** were created by the Presidium decree of 8 July 1944: «Мать-героиня» (Mother Heroine) for ten or more children, the order «Материнская слава» (Maternal Glory, III, II and I class) for seven, eight or nine, and the «Медаль материнства» (Motherhood Medal, II and I class) for five or six [S16], [S18].
  - Under the 1944 text, the award was made once the youngest child reached one year and while the mother's other children were alive, and it counted children killed or missing at the front [S16]. So the class reflects the children counted at the award date, not all births, and the award date shows only that the youngest child was at least a year old by then.
  - The USSR Supreme Soviet Presidium conferred Mother Heroine by decree, the union- and autonomous-republic Supreme Soviet presidiums awarded Maternal Glory and the Motherhood Medal, and oblast, city and district executive committees handed over those two awards (statutes of 18 August 1944, Vedomosti 1944 No. 45) [S17]. Search those bodies' fonds for the award papers, under the mother's own surname, which may differ from her children's. Read the rules in the edition in force at the award date.

- **Privacy gate:** <!-- privacy-gate: request --> Award papers name the awardee and, for maternal awards, the children, who may be living; answer the privacy gate in `SKILL.md` before ordering an award extract or asking an archive to confirm an award.
- **Use maternal-award papers as a list of children.** A Dzen genealogist lists district-archive protocols on Mother Heroine awards, giving each child's full name and birth year, among her sources of family composition; in the same district archive she found wartime lists of residents taken for forced labour [S86]. Lists of women awarded Maternal Glory and the Motherhood Medal, and protocols of their presentation, also sit in republic fonds: the State Historical Archive of Chuvashia holds them in the fond of the republic Supreme Soviet, f. Р-1041 (a 1973 presentation protocol is in op. 18, d. 5) [S87].
- **To confirm a civil award, ask GARF as well as the regional archive.** A 2023 guide sends civil awards to GARF and regional archives, and military awards to «Память народа» and the Ministry of Defence archive [S80]; a Dzen genealogist confirmed an award through GARF [S88]. GARF's fond 7523 holds a 1946 report compiled in the Presidium's department for recording and registering awardees (op. 17, d. 353) [S89].
- **Find the published award decree.** A Presidium award decree can be found in print: the decree of 21 January 1939 on Uzbek SSR farm workers, printed in «Правда» on 22 January, gives a farm worker's post, farm and district and, for some, the achievement, such as a team leader's 113 centners of cotton per hectare [S90]. The decree of 21 February 1939 on Rostov oblast farm workers gives the same for its farm workers [S91], and a Dzen author quotes its entry for a kolkhoz team leader, with wheat and sunflower yields per hectare [S92]. For a farm worker with a state order of that period, search the decrees of that oblast and year before you write to an archive.

- **Exhibition awards: search arhiv.vdnh.ru.** The VDNKh archive portal opened in 2020 with almost 11,500 award decisions of the All-Union Agricultural Exhibition (ВСХВ) and VDNKh for 1939–1991. It searches by surname, given name and patronymic, award date, region, award type and organisation or kolkhoz, and takes orders for a copy of an extract, sent by post [S93 @2026-11-16], [S94 @2026-11-16]. Its form asks for the surname, the organisation and the region as they were at the award date [S95 @2026-11-16]. A medal's serial number also leads to its decision: in 2022 VDNKh staff identified a 1939 medal's holder from it [S94 @2026-11-16].

  When the name finds nothing, search by the region with the surname, by the kolkhoz or enterprise, or by a co-awardee, then open the whole decision and read every name for relatives and misspelt namesakes. A Dzen author whose relative's name gave no hit found the 1940 decision through a co-awardee named with the relative in a district local-history book, and reads each decision whole for namesakes and relatives [S96]; she also searches by enterprise [S92].

**Residence.**

- House books record the workplace [S1].
- A participant said that ЦГА Москвы answers house-book queries by address and full name, without proof of kinship for books up to 1950 inclusive [S2].
- For Leningrad, check the city archives website for surviving house books and taxpayer lists at a known address, and look there for relatives living at the same address [S2].
- **Privacy gate:** <!-- privacy-gate: request --> Detailed ZAGS extracts, especially for a child's birth, can be about people who are still living; answer the privacy gate in `SKILL.md` before requesting them.
- Detailed ZAGS extracts for a death, a marriage or a child's birth give addresses for these searches [S2].
- A Yad Vashem evacuation entry fixed one family's Moscow occupation and residence. The next steps were detailed ZAGS records and the лишенец file of the elderly dependant [S2].
- **For a rural family, add the village-soviet household books (похозяйственные книги).** Village soviets kept them from 1934 (decree No. 185 of 26 January 1934 of the СНК СССР, the USSR Council of People's Commissars), one entry per household beginning with its head [S14].
  - They now sit in district or city archives, sometimes in the oblast state archive, and some are still with the local administration [S14], [S15]. Runs can start late: in the Minsk oblast state archive most districts' books survive only from 1944 [S15].
  - **Privacy gate:** <!-- privacy-gate: request --> Household-book entries list every household member and their age, and some may still be living; answer the privacy gate in `SKILL.md` before requesting an entry or a surname search.
  - Request the book for the named settlement and period and the entry for the household of the named head, with name variants, and ask whether a copy of the family-composition entry is possible. If the head is unknown, request a surname search within that settlement and ask its terms.
  - An entry lists the members, their relation to the head and their age, with marks of arrival in and departure from the household. The form changed several times between 1934 and 1975, so read the columns of the book you receive [S14].

  - **For a book less than 75 years old, prove kinship in the request.** A 2023 Dzen guide says kinship must be proved for a household book less than 75 years old, the term of the closure in step 5, so the cut-off year moves forward each year [S64]. State how each household member is related to you and offer copies of the kinship documents. Its author did so by email to a municipal archive and received his family's books for 1936–1961 as certified copies by post [S64].

  - **When ZAGS has no rural death, read the household book.** A Dzen author who had asked ZAGS for an ancestor's death record several times over eight years found its full date in a 1936 household book, the earliest the district archive department held, where she had expected at most a year; the same entry gave a wrong birth year [S97]. Another post by the same author reports departure marks for deaths, deaths in the war and moves, with the dates of call-up and demobilisation [S98]. Use the date to ask ZAGS again, and check the book's birth years against other records.
  - **Follow the household into the next book.** Each new book copied the households again, and a Dzen author who found a woman still living in 1950 looks for her death in the later books [S98]. Read the span of each book: in one Omsk-region village soviet the books cover single years for 1934–1937, two years for 1938–1939 and three years for 1940–1942 [S99]. Request the whole run for the settlement, not one book.

  - **If the household books are lost, look for the kolkhoz's own records.** In the Mari El state archive, the fond of kolkhoz «Ноля» (f. Р-420, op. 1) holds members' personal accounts for 1933–1934, a household book of its members for 1936 and labour-day books (книги учёта трудодней) for 1938, 1939 and 1941 [S37 @2026-11-08]. Records of liquidated kolkhozes can also sit in a district archive that confirms former workers' service and pay for pensions, as in Sysert [S38 @2026-11-08], so search both the kolkhoz fonds and the personnel (по личному составу) fonds.

- **Privacy gate:** <!-- privacy-gate: request --> An apartment card lists everyone registered in a flat, some of whom may be living; answer the privacy gate in `SKILL.md` before requesting a copy or an extract.
- **For a city flat, ask for the apartment card (поквартирная карточка).** Cards are no longer issued; a copy of, or extract from, a card made before 17 April 2018 is requested from the city's archive service with an application, a passport and proof of ownership of the flat [S100 @2026-11-16].

  Some flats kept these cards instead of a house book. A Dzen genealogist saw an archival certificate, issued against kinship and ownership documents, that listed everyone registered in and removed from a flat, and reports that in her case the card was held by the МФЦ [S86]. If the archive service has no card, ask the МФЦ or the passport office.

**Collectivisation-era village records.** A participant quoted the regional fond on church closures (ГАСО f. Р-102, op. 1, d. 865, 1930). It contains collective-farm meeting minutes naming the chairman and secretary, with attendance lists on folios 13–17 [S12].

**Trace a kolkhoz through its mergers and district changes.** In the Batyrevo district archive (Chuvashia), «колхоз им. Ленина» of Nizhneye Turmyshevo merged in September 1950 with the «Авангард» kolkhoz of Verkhneye Atykovo, after the party resolution of 30 May 1950 on merging small kolkhozes, and kept its name; it changed district three times, merged into «Россия» in 1959, and its 1950–1959 files sit in f. 213, the united fond of the amalgamated kolkhoz «Знамя» [S39 @2026-11-08]. Take the farm's village soviet and district from its fond title, as most kolkhoz fond titles in the Mari El state archive's list of agricultural fonds give them, before you search a gazetteer [S40 @2026-11-08].

**Pensions.** Reports conflict. One participant said social-security (собес) pension files are destroyed within about five years of death. Another obtained a Kharkiv pension file for a 1962 death. The same participant's request in Dnipro for a 1968 death found nothing, which the participant put down to a move, although that office still held files for that year [S1]. Ask the office about the years you need instead of assuming either answer.

- **Privacy gate:** <!-- privacy-gate: request --> A pension file holds the pensioner's family documents, which name a spouse and children who may be living; answer the privacy gate in `SKILL.md` before requesting one.
- **Russia: request a dead pensioner's pension file (пенсионное дело) from the Social Fund.** The Social Fund of Russia (СФР), formed by reorganising the Pension Fund (ПФР), began work on 1 January 2023 [S101]. Apply in your own name to the regional branch that holds the file, as a rule that of the place of death or the one that paid the pension; attach copies of the kinship documents, and ask for the personal documents (work, education, birth, marriage, children, wartime service), not the pension amounts [S104]. When a pensioner moves, the branch of the new residence requests the file from the branch of the former one [S102], so a file can stay behind: ask the branch of the previous residence when the first reply is negative, as Fund staff advised a Dzen author for a pensioner who had moved from the former Chechen-Ingush ASSR [S103].
- **What the file can hold.** It holds the documents the pensioner submitted to obtain the pension, among them workplace certificates, copies of the labour book and, for kolkhoz work, protocols in which several people confirmed the period [S79]. Dzen reports add children's birth and marriage certificates and survivor-pension papers [S86]; a 1993 certificate of kolkhoz work in 1943–1944 [S68]; commissariat certificates of war participation issued in 1975 and 1990, which sent the author to the commissariat [S105]; and a whole work history when the labour book was lost [S106]. Order the file even when the labour book survives [S107].

- **Request it soon after a death.** Since 15 June 2025 an old-age pension recipient's payment file is kept 15 years from the date payments stopped, down from 20 years [S108 @2026-11-16]; a survivor-pension file is kept 10 years, and a disability pensioner's file 5 years after death, or 3 years when the disability is recorded in the unified social-sector platform [S116 @2026-11-16]. For Russia, use these terms, not the forum estimates above.

- **An older file may be gone.** After a cut in storage terms in April 2021, files were destroyed in bulk, though a few regions sent them to the regional archive [S79]. So the cut-off moves forward every year, and the files of the earlier generation are usually gone [S106]. Ask for an older file anyway: single documents can survive, especially for war veterans who died in the 1990s [S104].

**Death and inheritance (Russia).** The Federal Notarial Chamber's probate-case register (Реестр наследственных дел, notariat.ru) has run in the notarial information system since 1 July 2014 [S29]. It is an auxiliary index of opened inheritance cases, not a death record and not proof of kinship.

- Names match exactly: a query without a patronymic finds only cases recorded without one. Birth and death dates may be partial or left out; if a doubtful date filter returns nothing, retry without it. The form limits the number of queries per period of time [S28].
- A year in the case number is not the death year. The register states no coverage period, so completeness for older deaths is unknown and a miss is not a negative [S28].
- The notarial district does not prove the last residence. When the last residence is unknown or abroad, the inheritance opens where the inherited property in Russia lies, immovable property (or its most valuable part) first (Civil Code, Art. 1115, Part 2) [S30], [S31].
- Do not collect living heirs' addresses or contacts. For the grave itself, use the Russian cemetery-database rules in [burial evidence packet § 2](burial-evidence-packet.md#2-search-the-recorded-name-fields-separately).

## 4. Search under every name the person actually used

- **Search the Russified civil name and patronymic used in daily life,** not only the Yiddish or birth form.
  - In one case the security archives reported nothing. A participant asked what the grandmother was called "in the world" and found a GARF лишенец inventory entry under a proposed Russian name and patronymic. That entry is a title-only candidate until its contents are checked against what is known of her [S10].
  - A change of name could be official (an annotation in the metrical entry) or unofficial (new documents written from the person's own words) [S2].
  - A participant reported that ZAGS annotations recording new names appear in red ink on pre-1919 synagogue act records, dated from 1903 to 1991 [S1].
- **Expect clerks to vary the form.**
  - One woman appears in her three children's birth records first under a double Yiddish name and patronymic, then under a shortened form, then under a Russian name and patronymic, without any official change [S1].
  - A regional list entry gave a woman's given name in a form one letter different from the form used in the request [S4].
  - A participant said that when the patronymic was unknown, wartime clerks sometimes just wrote a generic one [S1].
- **Search a rare given name both as the person's own name and as a patronymic.** A participant searched a surname with a rare given name across regional and federal catalogues [S2]:
  - under the adult's own name: a file in a 1932 construction-directorate fond in Udmurtia (f. 164, op. 3);
  - under the patronymic, as possible descendants: a 1943–1945 wartime raikom fond and a GARF voting-rights restoration file.

  None of these relationships is confirmed until the files are checked.
- **Do not search under a nickname alone.** Ask whether any document was issued in that name [S2].

- **Search the press for a surname-change notice.** Under the 1918 decree, a citizen changing a surname applied to ZAGS and placed a paid newspaper notice, most often in «Известия», giving the old and new surname (a 1927 example also gives the birthplace and birth year); such notices ran until the late 1930s, and the change was registered about two months later if no interested person objected [S109]. A 1968 article cites 1930 «Известия» notices of whole families changing surname [S110], and a Dzen genealogist quotes notices asking objectors to write to the city ZAGS [S111]. Search the central and local papers of the likely years under both surnames: a notice links the two names with a date.

## 5. Log each catalogue hit as a candidate with its own locator

- **One row per locator.** Keep every fond/opis/delo with its date range as a separate row, even when several rows probably belong to one person. Mark each row *title only* or *file inspected*. The six СОГАСПИ rows in step 3 are six requests, not one file [S2].
- **A name match is a candidate.** Participants qualify their own hits: "could be namesakes", "probably the son", "possibly the daughter", or "could it be connected to yours?" [S2], [S13].
- **An estimate mismatch lowers the rank; it does not exclude.** In one case a participant offered a same-surname birth entry, and the researcher rejected it because it did not fit the town and birth years known from the son's party card [S9]. Rank a candidate lower when an estimated birth year disagrees, but do not exclude it on that ground alone. Leave the identity ruling to evidence/proof judgment.
- **Privacy gate:** <!-- privacy-gate: request --> Requests for personal-file copies, archival certificates or kinship-proof certificates can concern people who may be living; answer the privacy gate in `SKILL.md` before sending each one.
- **Request status is part of the row.** Note whether you asked for copies or only for an archival certificate (архивная справка). A participant noted that without proof of kinship you can still ask for the certificate, and that an older file may be released anyway [S2].
- **Build a kinship-proof chain only from documents the user holds.** When an archive requires proof of kinship for a personal file, make each missing link (for example one generation's birth or marriage certificate) its own early request. It gates access to that file only; carry on with the other searches. In Russia the basis is Federal Law 125-FZ, Art. 25, Part 3: archival documents containing a citizen's personal or family secrets or private life are closed for 75 years from the document's creation, and before then open only with the person's written permission or, after death, that of their heirs [S32].

- **List every link the chain needs.** A Dzen genealogist's list for ZAGS: your passport, your birth record and, if your surname changed, your marriage record; each generation's birth record up to the one that names the ancestor; a marriage record for each woman whose surname changed, and every marriage and divorce record when it changed more than once; and a death record for each dead link [S69]. For a collateral relative, such as a grandfather's sister, add her own birth, marriage and death records to the line of the common ancestor. Bring originals or certified copies, and if some records are missing, request them all at once: the clerk checks the whole chain together and issues them together, with a state fee for each [S112].
- **A spelling break stops the chain.** When two birth records with the same parents spell the surname differently, ZAGS may refuse to treat them as one family. A Dzen genealogist reports a man refused his sister's death справка for this reason and told that their kinship had to be established in court, on an application and witness testimony [S113]; establishing kinship is one of the facts a court establishes under the Civil Procedure Code, Art. 264, Part 2, item 1 [S114]. Look for another record that proves the link before you plan on a court case.

## 6. Read questionnaires and autobiographies as dated self-reports

- **Record context with every field.** Note the date, the form type and its purpose: party admission, employment, award nomination or attestation. Do not record a field as a fact about the person.
- **Treat origin and class statements as shaped by their purpose.** A 1922 expulsion for having employed hired workers in 1904 shows why social origin was presented carefully in party papers [S3]. An autobiography written for admission can still confirm what other records lack: one confirmed a birth date and village that the parish search had failed to find [S3].
- **Do not adopt a nationality field either way.** Participants reported:
  - the same soldier written with different nationalities in 1942 and in 1943/1945 records [S1];
  - a son recorded as Russian in the army, against a family claim of Jewish descent that other participants challenged [S2];
  - a workplace file that still recorded a man as Jewish in the 1950s [S9];
  - a woman who concealed being Jewish for decades after the war [S1].

  Keep each value with its record and date, and check it against independent sources. For the subject's own files after a confirmed loss, participants expect nationality and only sometimes the parents' names [S2]. The children's questionnaires in step 2 are the better route to the parents.
- **Treat a regional list's place as one observation.** In one case a person had two extracts, one with a query mark on the village [S4].
- **Read a birth date against both calendars.** An Orthodox metrical date, like other Russian dates written before 14 February 1918, is normally Old Style; check the document's own calendar note [S33]. A questionnaire may restate the metrical birth date in New Style, so a difference of 12 or 13 days is not by itself a conflict. Record both dates with their calendar; for the offsets, use [evidence/proof judgment: follow record versions and test disputed dates](evidence-proof-judgment.md#follow-record-versions-and-test-disputed-dates).

- **Read a fact confirmed by witnesses as later testimony.** When work records were lost, the RSFSR pension law of 1990 let work service be established on the testimony of two or more witnesses (Art. 97) [S115]. A pension file can hold such a protocol: a Dzen author found a 1993 one confirming kolkhoz work of 1943–1944, and has seen applications to establish a correct date of birth («Об установлении правильной даты рождения») whose witnesses were the applicant's peers [S68]. Record the fact with the protocol's date and witnesses, not as a record made at the time.

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
