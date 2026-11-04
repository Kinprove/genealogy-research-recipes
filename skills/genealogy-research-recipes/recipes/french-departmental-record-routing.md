# Route a French record search to the right département, series and access rule

Use this recipe before you search for a French birth, marriage, death, census, military or notarial record. It sends each search to the département archive and series that hold it, and tells you when an act is open. It prevents eight failures: looking for one national French index that does not exist; reporting "not in the census" after a name search of lists that are mostly unindexed; looking for a soldier's register under his birth year and birth département instead of his classe and recruitment bureau; calling a recent birth or marriage "missing" when it is closed but can be ordered; expecting a duplicate parish register before 1667; looking for a Paris-suburb notary at the Archives nationales; assuming a former Meurthe commune's present département without checking the 1871 annexation line; and stopping an early-1939 camp search at the Pyrénées-Orientales archives, which hold no lists for those months, when the Archives nationales do.

It covers routing, access delays, the INSEE death file, the succession tables, the censuses, the registres matricules, ancien-régime duplicates, notarial minutes and the Pyrénées-Orientales camp files. Link out for the shared steps:

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

## 6. Find a man in the registres matricules by classe and bureau

- **Compute the classe as birth year plus 20.** The registers run from the classe of 1867, so men born about 1847 onward [S9].
- **Route by recruitment bureau, not by birthplace.** Registers are kept by classe and by recruitment bureau, and a man is recorded where he lived at age 20 [S9]. Some cantons belonged to a bureau in another département, whose archives hold their registers [S10]. Search the département of his residence around age 20 first, then his birth département.
- **Open the alphabetical table for each classe and bureau** [S9], then the register entry. Check the classes either side if the birth year is uncertain.
- **Use Grand Mémorial as a finder for the classes of 1887–1921.** It searches the departmental registre-matricule indexes nationally and links each hit to the departmental archive's record [S11]. Coverage depends on each AD's indexing. Cite the departmental register and image, not Grand Mémorial.

## 7. Look for the right copy of an ancien-régime parish register

- **Expect one copy before 1667.** The Ordonnance de Saint-Germain-en-Laye of 1667 required parish registers to be kept in two copies, one sent to the court registry (*greffe*) [S18].
- **Expect patchy greffe copies from 1667 to 1736.** The royal declaration of 9 April 1736 restated the duty because it had been widely neglected, and required two registers, both authentic [S19]. In the Gard the greffe collection starts between 1667 and 1736 depending on the parish [S20].
- **When one copy is lost or damaged, look for the other in a different series.** The parish original usually sits in the communal fonds (GG, then E) or E-dépôt; the greffe copy forms its own E sub-series [S18]. In the Côtes-d'Armor the greffe copy of the parish registers is in 6 E (7 E holds the civil registers) [S18]; read each AD's finding aid for both copies.

## 8. Find notarial minutes through the notary

- **Look for minutes over 75 years old in the AD.** Take the sub-series from that AD's finding aid; the Nièvre, for example, files them in 3 E [S22]. Younger minutes usually stay with the notary's office [S21].
- **Send only Paris intra-muros notaries to the Archives nationales.** Their minutes go to the Minutier central; notaries elsewhere, the Paris suburbs included, deposit with their AD [S21].
- **Search by notary, not by client.** Identify the notaries working in the place and period, then read each one's chronological répertoire (*répertoire*), kept alongside the minutes [S21]. Use a name index only where one exists for that notary.
- **Expect marriage contracts and inventaires après décès (post-mortem inventories)** among the minutes; the Archives nationales publish a series of Minutier central inventaires après décès [S23].

## 9. Follow a 1939 Spanish refugee into the Pyrénées-Orientales camp files

- **Take early-1939 camp lists from the Archives nationales, not the department.** The Pyrénées-Orientales departmental archives hold no nominative data for the crossing of January–February 1939 and the months after; their nominative data run from September 1939 to November 1942 [S24]. For Argelès, Sûreté nationale series F/7/14731 at the Archives nationales holds nominative lists and individual notices from 2 February 1939 to 17 May 1940, including the first arrivals of 31 January to 2 February 1939 [S25], [S28]. F/7/14732 covers Barcarès and F/7/14733 Saint-Cyprien and other Pyrénées-Orientales sites [S28]. These lists are partial [S25]: a miss in them is not a negative.
- **Search the department's camp name database and its list of internee files,** both linked from its camp resources page [S24]. In the prefecture fonds, 109 W 330 holds nominative lists for the Argelès-sur-Mer camps, 1939–1940 [S25]. The Argelès camp memorial holds no internee lists itself [S25].
- **Check the Archives nationales police card files for a refugee with a French police file:** the Sûreté nationale central file, individual files to 1940 [S27], and the administrative police file, about 150,000 files opened from March 1941 to 1949, which records internment, transfer and release [S26]. These are individual police files, not camp lists.
- **Carry the search back to Spain** from the birthplace or identity these files give.

## Close with a routing packet

Return:

- **Jurisdiction row:** the commune under each spelling, its département on the event date and today, and the annexation status for an 1871–1918 north-eastern event.
- **Access row:** for each birth or marriage, the open date computed from closure and deaths, and whether the act was ordered from the mairie.
- **Series rows:** for each search, the AD, series and cote (or the INSEE file, Grand Mémorial or Archives nationales finding aid), the classe and bureau for a soldier, the notary for a notarial act, and the status: searched, found, not found, closed or not online.
- **Census rows:** each commune and year read, the pages read, and whether a name index existed.
- **Gaps:** INSEE years 1970–1975, greffe copies before 1736, unindexed census years, and for early 1939 whether the Archives nationales camp lists were read.

The model assembles this packet. The researcher decides identity and kinship.
