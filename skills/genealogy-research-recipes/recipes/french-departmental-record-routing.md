# Route French records by département, creator, series and access rule

Use this recipe before you search for a French birth, marriage, death, census, military, property, notarial, decoration or consular record. It identifies the relevant archive and series from the record's creator and period, and tells you when a civil act is open. It prevents failures such as looking for one national French index that does not exist; reporting "not in the census" after a name search of lists that are mostly unindexed; looking for a soldier's register under his birth year and birth département instead of his classe and recruitment bureau; calling a recent birth or marriage "missing" when it is closed but can be ordered; expecting a duplicate parish register before 1667; looking for a Paris-suburb notary at the Archives nationales; assuming a former Meurthe commune's present département without checking the 1871 annexation line; and stopping an early-1939 camp search at the Pyrénées-Orientales archives, which hold no lists for those months, when the Archives nationales do.

It covers routing, access delays, the INSEE death file, the succession tables, the censuses, the registres matricules, ancien-régime duplicates, property registers, notarial minutes and the Pyrénées-Orientales camp files. Link out for the shared steps:

For an adoption lead, a French Basque house-name change or a Breton marriage decree,
use section 10 to identify the separate judgment, house-entry or consent records to seek.
These are conditional retrieval routes; an uninspected record does not resolve the family link.

For a medal application or a French resident abroad, section 11 selects the award
administration or consular post before choosing its records. A consular record follows
its post and collection, rather than the domestic département route alone.

For a known property, section 8 carries a cadastral name into the relevant mortgage
records, or a historical Paris address into its property register and notarial reference.

- **Reading the act once you have it** (act date versus event date, Republican dates, *je dis* corrections, status words, legitimated children, margin notes): [French and Belgian civil act extraction](french-belgian-civil-act-extraction.md).
- **A commune you cannot place, or one renamed or merged:** [historical place-name resolution](historical-place-name-resolution.md).
- **Frame versus page, gaps in an image series and the inspection ledger:** [archival image coverage verification](archival-image-coverage-verification.md).
- **Citing the departmental image:** [source citation](source-citation.md).
- **Identity rulings:** [evidence/proof judgment](evidence-proof-judgment.md).

## Inputs to gather first

Gather these before searching:

- the event type and approximate year
- the commune under every spelling seen, each with the record it came from
- the département on the event date, and today's département if different
- for a man born from about 1847, his birth year and every known residence around age 20
- for a recent event, the person's death date if known, and for a marriage, both spouses' death dates
- any series reference (cote) or image locator already seen
- for a property inquiry, the historical location, bounded transfer period and any
  cadastral case, recorded name, address or deed reference, each with its own source

## 1. Route by département, not by a national index

- **Send each search to an Archives départementales (AD), not to a national index.** Older civil registers, census lists, military registers, Enregistrement tables and notarial minutes are kept by the AD, each with its own website and series. The Ministry of Culture publishes a directory of public archive services as open data [S4].
- **Fix the commune's département on the event date and today.** When the two differ, start from today's AD and read its finding aid for where the series for the event date are held.
- **Read series letters as a département's own classification.** Take each cote from that AD's finding aid, not from another département's. The series codes in steps 5, 7 and 8 are single-AD examples.
- **Fix the 1871–1918 annexation before routing a north-eastern commune.** The Treaty of Frankfurt ceded Bas-Rhin, Haut-Rhin except the Belfort area, most of the pre-1871 Moselle département, about one-third of Meurthe (the Château-Salins and Sarrebourg areas), and the Vosges cantons of Schirmeck and Saales [S15]. Saales was partitioned: the part left in France became the canton of Provenchères-sur-Fave [S17].
- **Place a former Meurthe commune before you route it.** The annexed Château-Salins and Sarrebourg areas joined Moselle [S16]. Do not assume which AD holds its pre-1871 registers: resolve the commune in the place-name recipe, then read the finding aid of its present AD.

## 2. Work out whether the act is open yet

- **Open birth and marriage registers 75 years after the register closed, or 25 years after the person's death if that comes first** (Code du patrimoine, art. L213-2 I 4° e) [S12], [S13]. For a marriage, the 25-year rule runs from the death of both spouses [S14].
- **Treat death acts as open at once.** Anyone may request one without giving a reason [S13], [S14]. A 25-year limit applies only to putting death acts online, so an online series can stop short of years that are open on request [S13].
- **Do not report a closed act as missing.** For a more recent birth or marriage, the person, the spouse, ascendants, descendants or a legal representative request a full copy (*copie intégrale*) or an extract with filiation (*extrait avec filiation*) from the mairie. Anyone may obtain an extract without filiation (*extrait sans filiation*) [S14].
- **Compute the window from today's date** and the register's closing year, and record it with the result.

## 3. Date a death after 1970 with the INSEE death file

- **Search INSEE's Fichier des personnes décédées (file of deceased persons) for a death from 1970 on.** It is free open data, published by INSEE under the Licence Ouverte [S1]. It holds deaths registered by INSEE, including some deaths abroad; INSEE warns that 1970–1975 may have gaps [S1].
- **Read the fields it gives:** date of birth, birth place code with the birth commune, or the birth country for a birth abroad, date of death, death place code, and the death act number [S1]. Use it to date a recent death or to find an emigrant's foreign birthplace.
- **Search it through deces.matchid.io.** This independent search engine over the INSEE open-data file has run since January 2020 [S2], [S3]. It is not an INSEE service.
- **Search several name forms.** Try the name with and without a second surname and without accents. Each monthly file is published once and not corrected afterwards [S1], so a misspelled entry stays misspelled.
- **Order the act with its number** (step 2): for a death in France, from the mairie of the death place or of the last domicile; for a death abroad, from the foreign-affairs ministry for a French national, otherwise from the authority that issued the act [S14]. INSEE says the file must not be used to certify anyone's vital status [S1]; cite the act, not the file.

## 4. Find a death when the commune is unknown

- **Search the Enregistrement tables des successions et absences (tables of estates and absences) for the area.** They are usually in sub-series 3 Q, kept by registration office (*bureau d'enregistrement*) and alphabetical by the deceased's surname [S7], [S8]. Some later volumes sit in W accessions [S8].
- **Expect the span to vary by AD.** In the Finistère they run from 1825 and give way to death cards (*fiches décès*) from 1969 [S7].
- **Read what an entry gives:** date of death and domicile, the surviving or predeceased spouse in tables opened from about the late 1880s, and the date of the succession declaration, with its number in later tables [S7]. Entries are not always complete [S8].
- **Follow the declaration date into the registre des mutations par décès (register of transfers on death)** of the same office [S7], then order the death act from the commune the domicile points to.

## 5. Read the nominative census lists household by household

- **Expect a list every five years from 1836 to 1936, then 1946.** The 1871 census was taken in 1872 and none was taken in 1916 [S5].
- **Find the lists by commune and year.** Up to 1936 they are often in sub-series 6 M [S5], [S6]; in the Côtes-d'Armor the 1946 lists are in a W series [S5]. Inside a commune they run by street and household [S6].
- **Read the columns of the year you open.** The lists give names and occupations [S6]; the role in the household (head, wife, children) is given only from 1881 [S5]. Other columns change by year: birthplace and nationality are absent from 1856 to 1866, and from 1906 a birth date replaces the age [S5]. Do not expect a birthplace in every year.
- **Browse, do not name-search.** Most years have no name index. A few have one, such as the Côtes-d'Armor 1906 census indexed by a local genealogy centre [S5]. Without an index, read the commune household by household, and record a miss only after reading every page of that list.

## 6. Follow the military record created at each stage

Use the classe/bureau route for the matricule series it covers. For earlier recruitment,
retain each selection stage separately; for unit context, start from independently
verified service dates.

### Find a man in the registres matricules by classe and bureau

- **Compute the classe as birth year plus 20.** The registers run from the classe of 1867, so men born about 1847 onward [S9].
- **Route by recruitment bureau, not by birthplace.** Registers are kept by classe and by recruitment bureau, and a man is recorded where he lived at age 20 [S9]. Some cantons belonged to a bureau in another département, whose archives hold their registers [S10]. Search the département of his residence around age 20 first, then his birth département.
- **Open the alphabetical table for each classe and bureau** [S9], then the register entry. Check the classes either side if the birth year is uncertain.
- **Use Grand Mémorial as a finder for the classes of 1887–1921.** It searches the departmental registre-matricule indexes nationally and links each hit to the departmental archive's record [S11]. Coverage depends on each AD's indexing. Cite the departmental register and image, not Grand Mémorial.

### Before classe 1867: follow the local recruitment stages

For a corroborated earlier class and locality, check the surviving recruitment series
before assuming the later matricule lookup applies. The 2025 presentation describes
municipal H and departmental R as finding leads [S38]; take each cote and covered year
from the actual local inventory.

1. Locate the municipal alphabetical recruitment list and preserve the commune, class
   year, person details and entry locator actually supplied. The presentation places
   this list in communal series H; verify its survival and custody for the commune.
2. Follow the candidate into the canton's *tableau de recensement*, described in
   departmental R. Compare the recorded identity details across the two entries;
   a same-name hit does not establish that they concern the same recruit.
3. Read that canton and class's lottery list. Copy the number, literal outcome and any
   recorded exemption, replacement or number exchange, keeping the named parties in
   their stated roles. A draw or a census entry alone does not establish service.
4. Seek the *liste définitive du contingent* in the relevant departmental inventory.
   Retain its recorded final status, dates and any destination unit or battalion; the
   source describes a destination as a possible field, not a universal one [S38].
5. Return the linked stages and unresolved links. A selection or final-contingent listing
   does not by itself establish physical departure or a complete service history.
   If the final record or destination is missing, leave it unresolved before choosing
   a unit to trace.

### A First World War matricule: select a bounded JMO interval

Start from an independently identified matricule and its dated unit transitions.
Preserve each unit designation, arrival, transfer and injury date with its source and
uncertainty. A blank departure field does not establish continuous presence.

1. Choose a small interval around a supported arrival or recorded injury, death or
   decoration, within the unit/date bounds actually documented. Distinguish assignment
   from confirmed presence and leave gaps unresolved. Do not select a convenient unit
   journal merely because its dates overlap the war.
2. The 2024 presentation carries matricule-derived regimental information to the
   histories and *journaux de marche et d'opérations* (JMO) on Mémoire des Hommes [S37].
   Verify the actual journal's unit and date coverage, then inspect the selected pages.
   Keep the journal date and page/image locator separate from the personal record.
3. Record what the journal states about the unit, and about an individual only where
   it actually identifies that person. Compare the unit context with the matricule's
   transitions and preserve conflicts. A unit action is not automatically the soldier's
   participation, and the journal may omit him entirely.
4. Return the bounded interval, pages inspected and resulting unit context, with any
   unavailable, uninspected or uncertain stretch explicit. Do not fill the soldier's
   personal chronology from the regiment's whole wartime narrative.

## 7. Look for the right copy of an ancien-régime parish register

- **Expect one copy before 1667.** The Ordonnance de Saint-Germain-en-Laye of 1667 required parish registers to be kept in two copies, one sent to the court registry (*greffe*) [S18].
- **Expect patchy greffe copies from 1667 to 1736.** The royal declaration of 9 April 1736 restated the duty because it had been widely neglected, and required two registers, both authentic [S19]. In the Gard the greffe collection starts between 1667 and 1736 depending on the parish [S20].
- **When one copy is lost or damaged, look for the other in a different series.** The parish original usually sits in the communal fonds (GG, then E) or E-dépôt; the greffe copy forms its own E sub-series [S18]. In the Côtes-d'Armor the greffe copy of the parish registers is in 6 E (7 E holds the civil registers) [S18]; read each AD's finding aid for both copies.

## 8. Find property transfers and notarial minutes

### When the notary is known

- **Look for minutes over 75 years old in the AD.** Take the sub-series from that AD's finding aid; the Nièvre, for example, files them in 3 E [S22]. Younger minutes usually stay with the notary's office [S21].
- **Send only Paris intra-muros notaries to the Archives nationales.** Their minutes go to the Minutier central; notaries elsewhere, the Paris suburbs included, deposit with their AD [S21].
- **Search by notary, not by client.** Identify the notaries working in the place and period, then read each one's chronological répertoire (*répertoire*), kept alongside the minutes [S21]. Use a name index only where one exists for that notary.
- **Expect marriage contracts and inventaires après décès (post-mortem inventories)** among the minutes; the Archives nationales publish a series of Minutier central inventaires après décès [S23].

### From a cadastral case to a transfer deed

Keep the fiscal case, named person and parcel as separate references. The 2024 presentation
warns that a case can continue after a death and omit intermediate heirs [S39]. Use the
entry as a retrieval lead, not as proof of an unbroken ownership or complete heir list.

1. Copy the recorded name and dated parcel information. Select the historical mortgage
   bureau covering the commune and the period from its actual inventory. The
   Côtes-d'Armor guide describes a name-based search: a cadastral reference first supplies
   a person's name, rather than directly identifying a mortgage account [S40].
2. Follow the bureau's *registre indicateur* from surname to the alphabetical table's
   volume and folio; identify the person there and copy the repertoire volume and case.
   The mortgage case is a person's account, not the cadastral case [S40]. Preserve both
   locators and resolve namesakes before joining them.
3. In that account, distinguish transcriptions from credit inscriptions. Follow any
   continuation account and retain the transcription volume/article and date [S40].
   The entries are not identified by parcel: inspect candidate acts within the supported
   period and compare their property descriptions rather than choosing by name alone.
4. Convert the fiscal volume reference to an archival cote through that bureau's
   inventory, then obtain the complete transcription [S40]. Use any actual notary/date
   reference to seek the minute through the route above. Keep the two copies distinct.
5. Compare the inspected act's parties and stated succession roles with the fiscal entry
   and other evidence. Reuse [land-index recovery](land-index-book-series-recovery.md)
   for the full-instrument inspection and [tax observations](tax-roll-observation-workflow.md)
   for fiscal capacity. A missing heir in the matrix proves neither exclusion nor title.

Return the name-to-account-to-act chain and the parcel match actually established.
An unidentified bureau, missing register or unresolved identity remains a retrieval gap;
no index hit establishes which heirs held this property.

### A Paris address: choose its property record before the notary

Fix the historical street name, number, date and location within the old Paris core or
an annexed commune. Use [place-name resolution](historical-place-name-resolution.md)
and [historical maps](historical-map-record-recovery.md) for name, numbering and
boundary changes; a modern arrondissement alone does not select the historical record.

- **Old core:** use a *calepin des propriétés bâties* for the recorded owners, occupants
  and building description, and a *sommier foncier* for mutation references [S39], [S41].
  These sources overlap: the official guide lists sommier periods 1809–1859, 1859–1880
  and 1880–1945. Do not stop the sommier search at 1852 when calepins begin.
- **Search the address as indexed for that period.** The guide indexes calepins under
  both the historical arrondissement or commune and the present location [S41]. Keep
  each returned cote and date span; an address match is not yet a person match.
- **Carry the sommier's actual mutation date, nature and notary into the minute search.**
  Its property entry is the bridge to the notary [S39], [S41]; retain the referring
  entry and the separate notarial act, including any conflicting names or dates.
- **A commune before its 1860 annexation:** select its cadastral records instead of
  assuming the old-core route applies [S39]. Compare intermediate dated plans when
  urban change prevents a secure parcel/address match; leave uncertain links open.
- **Check access before ordering.** The official page opened 2026-11-05 warns that
  D1P4 before 1901 is inaccessible because of asbestos [S41]. A descriptive hit does
  not establish that a calepin can be inspected; record its actual access status.

## 9. Follow a 1939 Spanish refugee into the Pyrénées-Orientales camp files

- **Take early-1939 camp lists from the Archives nationales, not the department.** The Pyrénées-Orientales departmental archives hold no nominative data for the crossing of January–February 1939 and the months after; their nominative data run from September 1939 to November 1942 [S24]. For Argelès, Sûreté nationale series F/7/14731 at the Archives nationales holds nominative lists and individual notices from 2 February 1939 to 17 May 1940, including the first arrivals of 31 January to 2 February 1939 [S25], [S28]. F/7/14732 covers Barcarès and F/7/14733 Saint-Cyprien and other Pyrénées-Orientales sites [S28]. These lists are partial [S25]: a miss in them is not a negative.
- **Search the department's camp name database and its list of internee files,** both linked from its camp resources page [S24]. In the prefecture fonds, 109 W 330 holds nominative lists for the Argelès-sur-Mer camps, 1939–1940 [S25]. The Argelès camp memorial holds no internee lists itself [S25].
- **Check the Archives nationales police card files for a refugee with a French police file:** the Sûreté nationale central file, individual files to 1940 [S27], and the administrative police file, about 150,000 files opened from March 1941 to 1949, which records internment, transfer and release [S26]. These are individual police files, not camp lists.
- **Carry the search back to Spain** from the birthplace or identity these files give.

## 10. Follow family-linkage clues into their separate records

### An adoption claim without its judgment

Search the person's marriage and death acts, including their margins, and the reported
adoptant's succession papers for an adoption-judgment date or reference. The 2022 adoption
presentation identifies these places as possible sources of the judgment date [S29].
Use the succession-table route in step 4 when it supplies a declaration to inspect;
do not assume the table itself contains the adoption reference.

- Copy the judgment date and any court, parties or locator actually written, beside the
  referring act's own date and image. Keep an unreadable or absent court unresolved.
- With those details, ask the relevant archive to identify the historically competent
  court, surviving judgment series and request conditions for that period. A date alone
  does not identify a court, and this route supplies no universal adoption-series code.
- Keep the judgment as a separate retrieval target. Do not apply the civil-register
  access calculation in step 2 automatically to it or to an earlier birth act replaced
  after adoption; confirm the applicable conditions with the custodian.
- Report the reference found and whether the judgment was requested, inspected,
  unavailable or still unidentified. Upbringing does not establish adoption. Use
  [evidence/proof judgment](evidence-proof-judgment.md) to keep any documented legal
  parentage distinct from biological descent.

### A Basque surname change across a marriage

In a French Basque inquiry, test a house-entry explanation when the records show a name
change across marriage. The 2022 names presentation describes a man entering an heiress's
household and using her surname, itself a house name [S30]. Treat that as a hypothesis
for the particular couple, rather than a rule for every family, period or inheritance.

1. Keep the person's earlier surname, spouse's surname and house name as separate fields,
   each with its dated source and commune. Preserve any wording for entry into the house.
2. Retrieve the marriage entry. Use step 8 to locate the relevant notary and any surviving
   marriage contract, inheritance instrument or post-mortem inventory described for that
   place and period. Follow an actual reference to house or succession papers; if no
   reference or custody is established, leave that target unresolved.
3. Compare the spouses, stated parents, dates, house wording and succession roles across
   the inspected documents. Record which document connects the earlier name to the later
   household, and which links remain hypotheses. A same-named house can have successive,
   unrelated occupants; a house label alone does not identify a person or establish title.
4. Return the name-and-house sequence with its supporting locators and missing links.
   Do not turn surname frequency into origin evidence, or house-name continuity into an
   uninterrupted paternal line. A claimed heiress's status or property right still needs
   documentary and historical legal support.

### A Breton marriage mentioning a decree of justice

When a historical Breton marriage says a party is *décrété* or names a *décret de justice*,
copy that wording and any jurisdiction, seat and date before searching only notarial
minutes. The 2022 presentation describes a judicial marriage-consent route for a party
under 25 whose father had died, with a sénéchal rather than a notary recording it [S31].
Confirm that context for the actual party and period; the label alone does not establish it.

1. Use the jurisdiction named in the marriage to select that court's finding aid at the
   relevant AD. Look for the described consent proceedings in series B, verifying the
   particular court, date span and cote rather than applying another AD's subdivision.
   If the marriage supplies no jurisdiction, ask the archive to resolve it for the stated
   residence and period; do not choose a court from a modern commune name alone.
2. Request the surviving decree or consent proceeding and record the actual access and
   image availability. The presentation's 2022 statement about documents not being online
   is not a current digitization rule or a survival guarantee.
3. Inspect the proceeding for filiation and for each person's stated relationship and
   paternal or maternal side. The source describes such kin statements; do not fill them
   into an uninspected file or expect every proceeding to preserve the same roster.
4. Return the marriage-to-court locator chain and the statements actually recovered.
   Keep friends, relatives and consenting parties in their stated roles, and test identity
   and kinship under the evidence/proof workflow. A marriage act or a notarial-only search
   does not exhaust this separate judicial route.

## 11. Select the creator behind a medal or consular lead

### Sainte-Hélène: departmental lists and the separate application

Start from an independently identified applicant and the supported application commune.
The 2026 presentation describes requests passing from the mairie to the préfecture and
central administration, with departmental communal lists in M or sometimes R and
separately surviving individual packets assembled by mayors [S32].

1. Check that department's actual inventory for the named decoration, commune and period.
   Treat M/R as search leads, not fixed cotes. A report of central-file loss does not
   establish the loss of local lists or packets.
2. Retrieve the communal entry and ask separately whether its application packet survives.
   Preserve each locator and the documents actually present; a list is not the packet.
3. Compare the index's birth year or age with the application statements, original birth
   entry and any dated service evidence recovered. Preserve conflicting values and any
   calendar-conversion basis; do not silently correct an index or infer service from age.
4. Return the index, local entry and packet as linked records with their retrieval status.
   An incomplete index miss or unresolved date does not settle identity or service.

### Epidemic decorations: distinguish the form, date and awarding administration

Record the medal's actual inscription, any named recipient, date, class and whether it is
a table medal or a wearable decoration. The 2022 presentation distinguishes these forms
and describes different responsible administrations over time [S33].

- Use the form and period to identify the issuing administration before choosing its
  records. Check the AD's decoration descriptions in M, then the responsible ministry's
  holdings. The source also names R for military material; confirm the actual series and
  creator rather than copying a code or assuming one ministry covers every form.
- Search the locality's press around a supported award date, using Gallica or RetroNews
  where relevant issues are available. Carry an announcement's date, recipient and award
  wording into the administrative search; keep it distinct from an inspected award file.
- Return the variant, issuer-selection basis, inventories and bounded press result.
  Leave uncertain attribution, missing files and conflicting dates unresolved. Census
  sub-series 6 M in step 5 is not a decoration-file locator.

### A French resident under an overseas consular post

Fix the consulate or consular section and residence period first. The official guide
routes immatriculation through the post fonds' *chancellerie*, distinguishes civil and
notarial primata collections from duplicata, and warns that registration was voluntary
[S35]. Check those separate inventories, including earlier notarial registers left in
the post fonds; take custody and request conditions from the selected description.

The consular-fonds guide also identifies military material [S36]. Keep military files
separate from consular immatriculation despite the shared word *matricule*. The 2022
presentation motivates these parallel searches [S34]; its reading-room and date-limit
statements are not current access instructions.

Return the post, period, collection, cote, inspection status and actual family or image
content. An unregistered person is not thereby absent from the country, and a file
description does not establish a photograph, service history or family relationship.

## Close with a routing packet

Return:

- **Jurisdiction row:** the commune under each spelling, its département on the event date and today, and the annexation status for an 1871–1918 north-eastern event.
- **Access row:** for each birth or marriage, the open date computed from closure and deaths, and whether the act was ordered from the mairie.
- **Series rows:** for each search, the AD, series and cote (or the INSEE file, Grand Mémorial or Archives nationales finding aid), the classe and bureau for a soldier, the notary for a notarial act, and the status: searched, found, not found, closed or not online.
- **Census rows:** each commune and year read, the pages read, and whether a name index existed.
- **Family-linkage rows:** the adoption-date reference and separate judgment target, the
  Basque name-and-house sequence, or the Breton marriage-to-consent locator chain, with
  the records inspected, unresolved custody/access and unproven links kept explicit.
- **Award/consular rows:** the decoration form and creator or consular post, separate
  index/list/packet or registration/civil/notarial/military targets, actual inventory
  references, inspected contents and unresolved date, custody or identity questions.
- **Military-stage/context rows:** linked municipal, canton, lottery and final-contingent
  entries with literal outcomes and any stated destination; or the matricule-derived
  unit/date bounds, selected JMO pages and unit observations kept separate from personal
  presence, departure or participation conclusions.
- **Property rows:** separate cadastral and mortgage cases, historical bureau, table and
  transcription locators, or the dated Paris address and selected property register;
  the deed/notary reference, actual access and inspection status, and unresolved parcel,
  person or succession links.
- **Gaps:** INSEE years 1970–1975, greffe copies before 1736, unindexed census years, and for early 1939 whether the Archives nationales camp lists were read.

The model assembles this packet. The researcher decides identity and kinship.
