---
id: "swedish-military-record-routing"
title: "Route a Swedish soldier, sailor, officer or conscript to the military series that survive for his type and period"
summary: "Route a Swedish soldier, sailor, officer or conscript to the military series that survive for his type and period."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "none"
gates: []
guardrails: [{"id": "SWEDISH-MILITARY-RECORD-ROUTING-01", "text": "Swedish military records are not one searchable pool. Each index covers one series, one branch and one period, so classify the man first and read every miss against the coverage of the index you searched."}]
handoff: ["evidence-proof-judgment", "scandinavian-parish-record-recovery", "scandinavian-patronymic-farm-name-record-recovery"]
checked: "2026-11-06"
checked_basis: "opened 2026-11-06"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"section": "Records by country and region", "group": "Western and Northern Europe", "order": 124}
---

# Route a Swedish soldier, sailor, officer or conscript to the military series that survive for his type and period

Use this recipe when a Swedish or pre-1809 Finnish parish entry, census, emigrant record or family story calls a man *soldat*, *ryttare*, *dragon*, *husar*, *grenadjär*, *artillerist*, *båtsman*, *korpral*, an NCO or officer title, *värvad*, *volontär* or *värnpliktig*, or gives a military number. Swedish military records are not one searchable pool. Each index covers one series, one branch and one period, so classify the man first and read every miss against the coverage of the index you searched. It prevents these failures:

- reading a miss in the Central Soldiers Register (Centrala soldatregistret) as covering enlisted men, NCOs, officers or every corporal
- reading a miss in the general-muster name index as covering the years between musters, the years after 1883, or the navy
- treating a soldier name as one man's identity when it passed to his successor on the same *rote*
- expecting a home-parish entry before 1860 for a man who died and was buried away on campaign or detachment, or skipping the home register for a death from 1860 on
- searching a conscript's card by his enrolment number, or searching the 1902-1950 cards for a man enrolled before 1902
- sending an officer search to the soldier indexes when the officer's own career file sits in the army pension fund
- routing a Winter War volunteer to the 1918 volunteer brigade

Link out for the shared steps:

- **Why soldier names exist, men who kept them, intervening regimental rolls, *underhåll* referrals and *rusthållare* fees:** [patronymic, farm and soldier names](scandinavian-patronymic-farm-name-record-recovery.md).
- **Following the household and the moving registers:** [Swedish parish record recovery](scandinavian-parish-record-recovery.md).
- **Identity rulings:** [evidence/proof judgment](evidence-proof-judgment.md).

## Contents

- Inputs to gather first
- 1\. Classify the man before choosing a series
- 2\. Read a nil only against what the index actually covers
- 3\. Work the general muster rolls as dated snapshots, not a career file
- 4\. Before 1683 and in the Great Northern War: browse by regiment and year
- 5\. Treat a soldier name as the *rote*'s label, not the man's identity
- 6\. Officers and NCOs: the pension fund holds the career file
- 7\. Conscripts: search the card by name, read both sides, and follow the number
- 8\. Båtsmän: navy series by naval station
- 9\. Enlisted men: rolls survive only for garrisoned regiments, and contracts sit in the regiment's archive
- Close with a routing packet

## Inputs to gather first

- the title exactly as written in each parish entry, with its date, and any regiment, company, number or *rote* (allotment district) named
- whether the man lived in a country parish or in a town or fortress
- the soldier name and the civil name (patronymic or family name), each with its source
- any three-part number in the parish book's *värnplikt* or *värnpliktsförhållanden* column
- birth date and parish, and the years he is first and last seen with a military title

## 1. Classify the man before choosing a series

Record three things, each with the entry that supports it. If one is uncertain, open a row for each possibility.

- **Branch and recruitment.** The title fixes the branch, and the titles are not interchangeable: *soldat* is infantry, *ryttare* cavalry, and *dragon*, *husar* and *artillerist* name their own regiment types [S8]. *Båtsman* is navy. Between 1682 and 1901 a regiment was either allotted (*indelt*: the soldier was kept by a *rote* of farms, usually with a croft) or enlisted (*värvat*: paid recruits garrisoned in towns or fortresses) [S21]. Decide by residence: a soldier who served while living in a country parish was allotted, and enlisted units were garrisoned in towns and fortresses [S21]. For an allotted man, look up his parish in Riksarkivet's Indelningsverket (Grill) database to get his company, regiment and *rote* [S19], [S21]. Grill was published in the 1850s, so for a regiment divided before then, such as the Närke-Värmland regiment, map the parish to the older unit separately [S21].
- **Rank class.** Private or corporal; NCO (for example *rustmästare*, *furir*, *sergeant*, *fältväbel*); or officer. The series differ by rank class (steps 2 and 6).
- **Period.**
  - Before 1683: the army rolls of 1620-1723 (step 4).
  - 1683-1883: the general muster rolls (step 3).
  - 1884-1901: no indexed series. Use the regiment's unindexed rolls, including *stamrullor* (step 3).
  - Conscripts 1812-1901 (*beväring*) and 1902 onward: enrolment records and cards (step 7).

## 2. Read a nil only against what the index actually covers

| Index or archive | What it covers | A miss there does not cover |
| --- | --- | --- |
| ArkivDigital name index to the general muster rolls (*generalmönsterrullor*) | The October 2024 catalogue gives the Krigsarkivet series 1683-1883, 4.4 million records [S17 @2026-11-16]; from the inspected excerpt of each video transcript, the presenters describe army regiments, both allotted and enlisted, from privates to officers, and the Finnish regiments until 1809 [S5 @2026-11-16], [S9 @2026-11-16], [S4 @2026-11-16], [S8 @2026-11-16] | From the inspected excerpt of each video transcript: rolls kept in regimental archives, including the rolls between musters and those after 1883 [S5 @2026-11-16], [S13 @2026-11-16]; the navy [S14 @2026-11-16] |
| Centrala soldatregistret (soldatreg.se), run from Axvall | About 500,000 records of allotted soldiers [S23 @2026-11-16]; men enrolled 1682-1901, privates, corporals and *båtsmän*, no NCOs or officers, only a few enlisted units, and not complete [S22 @2026-11-16] | Most enlisted units, NCOs, officers; from the inspected excerpt of each video transcript, corporals are in scope but often missing, so a corporal's miss is not a negative [S2 @2026-11-16], and this is a separate database from ArkivDigital's: search both [S4 @2026-11-16] |
| ArkivDigital index to conscription cards (*värnpliktskort*, *stamkort*) | The October 2024 catalogue describes men enrolled 1902-1950, born 1881-1930, about 2.4 million cards [S17 @2026-11-16] | Men enrolled before 1902; from the inspected excerpt of each video transcript, whole companies and regiments of cards are missing [S5 @2026-11-16], [S6 @2026-11-16] |
| Riksarkivet archive: *Värnpliktskort. Stamkort och läkarhandlingar, avregistrerad* | The October 2026 copy of its military guide lists conscripts born about 1888-1921, from enrolment to discharge; search Riksarkivet by that title [S19 @2026-11-16] | Other birth years |
| ArkivDigital boatswain active list | The October 2024 catalogue describes per-man *båtsman* books of the late 1800s, more than 4,600 men born 1816-1877 [S17 @2026-11-16] | Earlier *båtsmän*, other navy rolls (step 8) |

Record the index, the fields you searched and its coverage in the routing row. A miss outside these limits is *not searched*, not *absent*.

## 3. Work the general muster rolls as dated snapshots, not a career file

- **Use each general muster as a dated snapshot.** Check the regiment’s own interim rolls and commanders’ papers for detachments, punishments or deaths between musters [S20], [S9], [S5].
- **Narrow the search by regiment.** Start with the given and soldier names, then add the regiment [S2]. Try abbreviated given names (*J:*, *J.*) and alternative spellings [S8]. Early rolls commonly give age and province. A birth parish or exact date can exclude the right entry, particularly before the rolls became more detailed around 1850 [S20], [S13].
- **Search the *rote* or farm name to list everyone who served it** [S11]. This gives you the succession of soldiers for that number, which step 5 needs.
- **Record the predecessor’s discharge, the replacement’s hiring and his formal approval separately.** At Sunnerbo company no. 120, the roll dates Peter Lind’s discharge to June 1838 and Salomon Trofast’s hiring to November. Trofast was approved at the 1841 muster [S2].
- **Read the remarks and any enclosures.** Copy the exact wording for campaigns, wounds, absence abroad or discharge for conduct [S20], [S9], [S11]. A former civil name can identify the man [S4]. Look for a priest’s certificate pasted into the roll to explain an absence [S16] and for a pension amount in the appended list of *gratialister* [S2].
- **Before 1860, trace an absent soldier to the place of burial.** A parish recorded burials in its own church or churchyard, and could omit a resident buried elsewhere [S31]. In a reported 1808 death the home-parish search failed and the burial place remained unknown [S10]. Read the muster remarks for illness abroad or capture [S9], [S12]. A detachment for canal or lock construction can point to another parish’s burial book [S5], [S9]. If the place is unclear, check the regiment’s or company commander’s notes [S10].
- **From 1860, search the home parish's death register first.** From 1860 a death was to be entered in the parish where the man was last registered, and also in the parish of burial if that was another parish [S31].
- **Identify the copy you searched.** The War Office, county governor and regimental commander received copies. A fourth was divided among company commanders [S20]. The name index in the ArkivDigital demonstration used the War Office copy. A miss leaves other copies to check [S5].
- **After the index ends.** ArkivDigital’s October 2024 catalogue lists general muster rolls indexed through 1883 [S17]. Some rolls in the military archive extend to about 1885 [S20]. For the transition to 1901, look in the regiment’s records for *stamrullor*, introduced at enlisted regiments in 1885 and allotted regiments in 1889 [S20], [S33].

**War years: also search *Rullor 1724–*.** Besides the rolls of 1620-1723, Riksarkivet's Arméns rullor database has the series *Rullor 1724–*: rolls of Swedish army units from 1724 to about 1865. Riksarkivet says this series holds almost the same information as the general muster rolls. Those are often incomplete in war years, so this series is often the only place to find a man, especially in the war of 1808-1809. Search it by regiment and year before you read a war-year gap as a negative. [S34 @2026-11-13]

## 4. Before 1683 and in the Great Northern War: browse by regiment and year

- The army rolls of 1620-1723 (*Rullor 1620-1723*) are the main source for the period, with large gaps [S20]. Riksarkivet offers them as the Arméns rullor database [S19]. Open the volumes for the year itself before you call a war year lost: volumes survive for 1709, for example SE/KrA/0022/1709/8 [S32]. For officers, open the series' personnel register first [S2].
- For losses and prisoners in the Great Northern War (1700-1721), search ArkivDigital for the Defensionskommissionen archive (rolls sent home from the field) and for the war-document collections titled *Krigshandlingar ... Stora nordiska kriget*, which include prisoners. There is no name index: you need the regiment and the period [S1].

## 5. Treat a soldier name as the *rote*'s label, not the man's identity

- **Follow the holders of a name by *rote* and date.** A soldier name could stay with the croft or *rote* [S29]. Two consecutive roll entries can therefore name different men identically. Use the discharge and replacement entries to separate their service, then establish any family relationship from other records [S6], [S5].
- **Search the pension and parish records under the soldier name and the patronymic.** A discharged man could resume his patronymic, including in the pension ledger [S29], [S18].
- **Separate the holders by dates, not by name.** For each roll entry under a soldier name and number, record the age, the province of birth, and the approval and discharge dates. A roll that gives a former civil name (*förut kallad*, "formerly called") links the soldier name to the man [S4].
- **Search court records beyond the home *rote*.** A witness to a fire at Åhus identified himself in court as the soldier for Vittaryd. Compare that place with the roll when a soldier name appears far from home [S12].

## 6. Officers and NCOs: the pension fund holds the career file

- **Officers and NCOs are in the general muster rolls.** Regimental officers are listed at the start of the roll and company officers at the start of their company [S20], [S9].
- **Army pension fund (Arméns pensionskassa), 1757-1937.** Officers, NCOs and civilian military staff paid into it [S18]. Before 1757 their pensions came from the Vadstena krigsmanshuskassa, which from then on served only privates and corporals [S18].
  - Officers and NCOs sent merit records (*meritförteckningar*: appointments, promotions, detachments, training) to the fund throughout their service. They are bound as *meritband* in series EV [S18].
  - Read the first submission for an age certificate or parents’ names and the last for the career up to that date [S18]. A pastor’s certificate accompanying a 1771 submission identifies the member’s birth in Saxony in 1714. Use the certificate’s locality to find the corresponding parish entry [S7].
  - ArkivDigital’s October 2024 catalogue lists merit books for 1757–1883 [S17]. For 1884–1895, use the fund’s person register, which covers 1757–1895. For 1896–1937, consult the finding aid for Arméns pensionskassa at Krigsarkivet and check the surviving series EV volumes by date [S18].
  - Pension decisions: series C III (1757-1783) and D (1784-1914). Pension applications: series E II, with a person register for each year [S18].
- **Other merit series.** Krigsarkivet also has a collection of army officers' merit records [S19], and regiments kept their own series [S1], [S3]. Navy officers' merit lists are a separate series [S17].
- **Printed and inspection sources.**
  - For officers under Charles XII, look up the officer alphabetically in Adam Lewenhaupt’s *Karl XII:s officerare* [S30]. For another person named in his biography, including a wife, consult the Riddarhuset card index [S3].
  - Regimental histories carry biographies of regimental officers (major and above) [S1].
  - Look up inspections (*husesyn*) of officers’ and NCOs’ official farms (*boställen*) by holder in the typed register, then read the inspection at the change of occupant to date the handover [S7], [S9].
- **After 1885** the *stamrulla* replaced the general muster rolls for officers and NCOs. From 1945 the *tjänstekort* (service record card) replaced it [S20].

## 7. Conscripts: search the card by name, read both sides, and follow the number

- **Before 1902.** Conscripts (*beväring*) were enrolled from 1812. From 1885 the three-part number in the parish book records the serial number, roll-keeping area and enrolment year. Use it to identify the enrolment roll [S25]. ArkivDigital’s October 2024 catalogue dates the conscription-card index to 1902–1950 [S17].
- **Find the card by name and birth date.** Clerks wrote the enrolment number in several forms, so an exact-number search can miss [S2], [S6]. Copy it from the parish book’s *värnplikt* or remarks column and use it to identify the roll-keeping area and year [S4], [S24]. Enrolment was at 21, or at 20 from 1914 [S17]. The personal identity number replaced the enrolment number in 1953 [S25].
- **The card moved with him.** Cards were introduced in 1918, replacing the *stamrulla*, and earlier service was copied onto them [S24]. When he moved to another enrolment area, his card was sent there. It was archived in the area where he lived when his liability ended (age 40 under the 1901 law, rising to 47 from 1942), or when he died, emigrated or was exempted [S24]. Look for an unindexed card in the area of his last residence, not the area of his birth. The cards are spread over many archive creators [S17].
- **Read both sides.** The front gives regiment codes (I 6, I 7 and so on), companies, training periods and days served. The back can record punishments, exemptions, and permission to leave the country [S2], [S4], [S6]. For where a company was stationed, go to the regiment's archive [S2].
- **Separate permission, travel and service abroad.** A Swedish draftee needed leave to go to Finland in 1939–1940 [S27]. Copy the card’s wording for permission to leave Sweden or a recorded stay in Spain, then seek a dated unit entry for service [S1], [S2]. One volunteer registered in Sweden but the war ended before he left, so searching field rolls alone missed the enlistment [S1].
  - The Winter War corps was the Svenska frivilligkåren, and the Finland Committee (*Finlandskommittén*) ran its enlistment [S27].
  - *Svenska brigaden* was the volunteer unit of the 1918 Finnish Civil War [S28]. Do not file a 1939-1940 volunteer under it.
  - Search the archive creators by their names. *Frivilliga i Finland, Finlandskommittén* covers the 1939–1940 recruitment and *Svenska brigaden i Finland* the 1918 brigade [S3].

## 8. Båtsmän: navy series by naval station

- **Navy rolls are not in the army general-muster index** [S8], [S14]. Search the navy series: *Rullor flottan* 1635-1915, which includes the navy general muster rolls [S26], [S17].
- **Each *båtsman* company belonged to a naval station**, and the rolls are arranged by station: Karlskrona (series IV) or Stockholm (series XIIIc). A Norrland company, for example Medelpad's, is filed under Stockholm [S26]. Search the station's series, not the home province [S26], [S15].
- **Late 1800s:** per-man *båtsmansrullor* (books) exist; use the ArkivDigital boatswain list to find them [S17], [S26].
- **Pensions:** *båtsmän* and navy officers and NCOs all belonged to the navy pension fund (Flottans pensionskassa), 1642-1937 [S18].
- **A *sjöman* on a merchant ship is a civilian.** He is in the seamen's house (*sjömanshus*) records, not the *båtsman* rolls [S3], [S15].

## 9. Enlisted men: rolls survive only for garrisoned regiments, and contracts sit in the regiment's archive

- Surviving general muster rolls of enlisted regiments cover those garrisoned in Sweden, Finland or Swedish Pomerania [S20]. Open the roll image for a former surname, birth date and parish. The entry for a hussar recruited in 1880 gives his former name as Christian Johansson and his birthplace as Sövde, enough to check the parish register [S4].
- Do not compute a birth year from an enlisted roll's age. Recruits older than about 20-23 were not normally accepted, which gave older men a reason to state a lower age [S20]. Take the birth year from the baptism or household entry.
- **Contracts.** Search the National Archival Database (NAD) under the regiment’s archive for enlistment and soldier contracts, including those of Skåne regiments [S1], [S15]. If the inventory lists none, record the regiment, years and series examined.
- For a recruit thought to have enlisted between 1912 and 1920, seek the conscription or service card. If the regiment is unknown, follow the man through parish books. A residence entry on regimental grounds may identify the regiment and company [S3].

## Close with a routing packet

Return:

- **Classification row:** branch, allotted or enlisted, rank class and period, each with the entry that supports it; parallel rows where uncertain.
- **Series rows:** for each search, the index or series, its coverage, the fields searched, the locator (regiment, company, number, year, volume and page, or card archive), and the status: *found*, *not found within coverage*, *outside coverage*, *not indexed (browse needed)* or *not listed in NAD*.
- **Soldier-name table:** each roll entry under the name and number, with age, province of birth, approval and discharge dates, and the man you assign it to.
- **Officer file:** the *meritband* used, first and last merit record, any birth proof, and the pension series and decision references.
- **Gaps:** years between musters, 1884-1901, lost cards, unindexed navy rolls and unphotographed regimental archives, each with its custodian.

The model builds the packet. The researcher decides identity.
