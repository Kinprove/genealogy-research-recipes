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
router: {"tier": "pointer", "group": "Country record routing", "order": 1063}
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

| Index | What it covers | A miss there does not cover |
| --- | --- | --- |
| ArkivDigital name index to the general muster rolls (*generalmönsterrullor*) | The Krigsarkivet series 1683-1883, 4.4 million records [S17]; army regiments, both allotted and enlisted, from privates to officers, and the Finnish regiments until 1809 [S5], [S9], [S4] | rolls kept in regimental archives, including the rolls between musters and those after 1883 [S5], [S13]; the navy [S8], [S14] |
| Centrala soldatregistret (soldatreg.se), run from Axvall | About 500,000 records of allotted soldiers [S23]; men enrolled 1682-1901, privates, corporals and *båtsmän*, no NCOs or officers, only a few enlisted units, and not complete [S22] | enlisted men, NCOs, officers; corporals are in scope but often missing [S2], so a corporal's miss is not a negative. It is a separate database from ArkivDigital's: search both [S4] |
| ArkivDigital index to conscription cards (*värnpliktskort*, *stamkort*) | Men enrolled 1902-1950, born 1881-1930, about 2.4 million cards [S17] | men enrolled before 1902; lost cards: whole companies and regiments of cards are missing [S5], [S6] |
| Riksarkivet Värnpliktiga database | Conscripts born about 1888-1921, from enrolment to discharge [S19] | other birth years |
| ArkivDigital boatswain active list | Per-man *båtsman* books of the late 1800s, more than 4,600 men born 1816-1877 [S17] | earlier *båtsmän*, other navy rolls (step 8) |

**Conscription cards: an archive, not a database.** Riksarkivet's military page lists the cards in the "Riksarkivet Värnpliktiga database" row as the archive *Värnpliktskort. Stamkort och läkarhandlingar, avregistrerad*, for conscripts born about 1888-1921. Search Riksarkivet by that title. [S19 @2026-11-13]

Record the index, the fields you searched and its coverage in the routing row. A miss outside these limits is *not searched*, not *absent*.

## 3. Work the general muster rolls as dated snapshots, not a career file

- **A general muster was held every third year, later every fifth** [S20]. The roll records the man at that muster only. For what happened between musters (detachments, punishments, deaths, interim rolls), go to the regiment's own archive at Krigsarkivet, most of which is not online [S9], [S5]. The patronymic recipe covers browsing the interim rolls.
- **Search early rolls by name and regiment, not by birth data.** Rolls usually give age and a province, not a parish or birth date; from 1850 they are much more detailed [S20], [S13]. Start with the given name and soldier name, add the regiment, then a parish or year range if there are too many hits. Spellings differ from the parish books and given names may be abbreviated (*J:*, *J.*), so do not fill every field [S8]. In one demonstration, a given name alone gave over 3,300 hits and the regiment cut it to 42 [S2].
- **Search the *rote* or farm name to list everyone who served it** [S11]. This gives you the succession of soldiers for that number, which step 5 needs.
- **Record hiring and approval as separate dates.** In ArkivDigital's demonstration, a grenadier hired in November 1838 was approved and entered in the rolls only at the 1841 muster [S2]. Copy the predecessor's discharge note on the same line: it dates the vacancy [S2].
- **Read the remarks and anything pasted in.** Remarks record campaigns, wounds, presence or absence [S20]: "left sick in Germany" [S9], struck off for conduct [S11], a former civil name [S4]. Priests' certificates excusing an absence can be pasted into the roll [S16]. Late rolls carry lists of *gratialister* (pensioned soldiers) with the yearly amount [S2].
- **Before 1860, expect no home-parish entry for a man buried away from home.** Until 1860 the death and burial register recorded only burials in the parish's own church or churchyard; men buried elsewhere, for example soldiers in war, were left out [S31]. ArkivDigital staff give this as the reason a soldier who died in 1808 is missing from his home register [S10]. Read the roll remarks for the episode (left sick abroad, captured) [S9], [S12]. Then search the burial register of the place he was detached to, for example for canal or lock building [S5], [S9]. Then go to the regiment's archive, where commanders' notes on their men can survive [S10].
- **From 1860, search the home parish's death register first.** From 1860 a death was to be entered in the parish where the man was last registered, and also in the parish of burial if that was another parish [S31].
- **Find the man in the right copy.** Copies of each roll went to the War Office (now Krigsarkivet), the county governor (now the regional archives) and the regiment [S20]. ArkivDigital indexes the Krigsarkivet series; other copies are not in the index [S5].
- **After 1883.** The general muster rolls end in 1885: no more were made from 1885 until the allotment system was wound up in 1901 [S33], and the Krigsarkivet series runs, with a few exceptions, to 1885 [S20]. The indexed part ends in 1883 [S17]. For 1884-1901 use the regiment's surviving rolls, including *stamrullor* from 1885 at enlisted regiments and from 1889 at allotted regiments [S20], [S33]. They sit in each regiment's archive and are not indexed [S5].

**War years: also search *Rullor 1724–*.** Besides the rolls of 1620-1723, Riksarkivet's Arméns rullor database has the series *Rullor 1724–*: rolls of Swedish army units from 1724 to about 1865. Riksarkivet says this series holds almost the same information as the general muster rolls. Those are often incomplete in war years, so this series is often the only place to find a man, especially in the war of 1808-1809. Search it by regiment and year before you read a war-year gap as a negative. [S34 @2026-11-13]

## 4. Before 1683 and in the Great Northern War: browse by regiment and year

- The army rolls of 1620-1723 (*Rullor 1620-1723*) are the main source for the period, with large gaps [S20]. Riksarkivet offers them as the Arméns rullor database [S19]. Open the volumes for the year itself before you call a war year lost: volumes survive for 1709, for example SE/KrA/0022/1709/8 [S32]. For officers, open the series' personnel register first [S2].
- For losses and prisoners in the Great Northern War (1700-1721), search ArkivDigital for the Defensionskommissionen archive (rolls sent home from the field) and for the war-document collections titled *Krigshandlingar ... Stora nordiska kriget*, which include prisoners. There is no name index: you need the regiment and the period [S1].

## 5. Treat a soldier name as the *rote*'s label, not the man's identity

- **The name often stayed with the *rote* or the croft and passed to the next soldier** [S29]. ArkivDigital shows a discharged soldier and his successor under the same soldier name; they may or may not be related [S6]. One grenadier's roll entries end with his replacement by another man of the same soldier name [S5].
- **A discharged soldier usually stopped using the name** [S29]. Some took back their patronymic, so the soldiers' pension ledgers may list them under it [S18]. Search the pension and parish records under both forms.
- **Separate the holders by dates, not by name.** For each roll entry under a soldier name and number, record the age, the province of birth, and the approval and discharge dates. A roll that gives a former civil name (*förut kallad*, "formerly called") links the soldier name to the man [S4].
- **Search the soldier name in court records.** ArkivDigital's machine-transcribed court records let you search the byname. In one demonstration, a soldier appeared as a witness about 150-200 km from his *rote*, introducing himself as "soldier for" his home *rote* [S12]. Confirm such a hit by the *rote*, not by the name alone.

## 6. Officers and NCOs: the pension fund holds the career file

- **Officers and NCOs are in the general muster rolls.** Regimental officers are listed at the start of the roll and company officers at the start of their company [S20], [S9].
- **Army pension fund (Arméns pensionskassa), 1757-1937.** Officers, NCOs and civilian military staff paid into it [S18]. Before 1757 their pensions came from the Vadstena krigsmanshuskassa, which from then on served only privates and corporals [S18].
  - Officers and NCOs sent merit records (*meritförteckningar*: appointments, promotions, detachments, training) to the fund throughout their service. They are bound as *meritband* in series EV [S18].
  - Read the first and the last. The first can contain proof of age with details of the parents; the last summarizes the career up to its submission date [S18]. ArkivDigital shows a fund member's 1771 submission with a pastor's certificate of his birth in Saxony in 1714, which led the researcher to his German origin [S7].
  - Person registers to the *meritband* cover 1757-1895 [S18]. ArkivDigital has the merit books for 1757-1883 [S17]; for later years, ask Krigsarkivet.
  - Pension decisions: series C III (1757-1783) and D (1784-1914). Pension applications: series E II, with a person register for each year [S18].
- **Other merit series.** Krigsarkivet also has a collection of army officers' merit records [S19], and regiments kept their own series [S1], [S3]. Navy officers' merit lists are a separate series [S17].
- **Printed and inspection sources.**
  - For officers under Charles XII, use Adam Lewenhaupt, *Karl XII:s officerare* (1920), arranged alphabetically [S30]. A Riddarhuset card index, photographed on ArkivDigital, covers everyone named in its biographies, wives included [S3].
  - Regimental histories carry biographies of regimental officers (major and above) [S1].
  - Inspections (*husesyn*) of officers' and NCOs' official farms (*boställen*) at each change of holder are on ArkivDigital with a typed register [S7], [S9]. Use them to date when an officer took over or left a farm.
- **After 1885** the *stamrulla* replaced the general muster rolls for officers and NCOs. From 1945 the *tjänstekort* (service record card) replaced it [S20].

## 7. Conscripts: search the card by name, read both sides, and follow the number

- **Before 1902.** Conscripts (*beväring*) were enrolled from 1812. From 1885 each man got a three-part number, SSS RRR/YY: serial number, roll-keeping area and year of enrolment. Parish books show it in the *värnplikt* column [S25]. Enrolment rolls are at Krigsarkivet [S25]. These men are not in the 1902-1950 card index [S17].
- **1902-1950 cards.** Search by name and birth date, never by the number. Clerks wrote the number in several forms, and the number search needs an exact match [S2], [S6]. Use the number, from the *värnplikt* column or the remarks of the parish book [S4], only to read the roll-keeping area and the year of enrolment [S24]. The man enrolled at 21, or at 20 from 1914 [S17]. In 1953 the personal identity number replaced the enrolment number [S25].
- **The card moved with him.** Cards were introduced in 1918, replacing the *stamrulla*, and earlier service was copied onto them [S24]. When he moved to another enrolment area, his card was sent there. It was archived in the area where he lived when his liability ended (age 40 under the 1901 law, rising to 47 from 1942), or when he died, emigrated or was exempted [S24]. Look for an unindexed card in the area of his last residence, not the area of his birth. The cards are spread over many archive creators [S17].
- **Read both sides.** The front gives regiment codes (I 6, I 7 and so on), companies, training periods and days served. The back can record punishments, exemptions, and permission to leave the country [S2], [S4], [S6]. For where a company was stationed, go to the regiment's archive [S2].
- **Volunteers abroad.** A conscript needed leave from his unit to go to Finland in 1939-1940 [S27]. ArkivDigital staff show cards noting permission to leave the realm for the Winter War, and stays in Spain during the civil war [S1], [S2]. A man who enlisted but never left can have no unit record at all [S1].
  - The Winter War corps was the Svenska frivilligkåren, and the Finland Committee (*Finlandskommittén*) ran its enlistment [S27].
  - *Svenska brigaden* was the volunteer unit of the 1918 Finnish Civil War [S28]. Do not file a 1939-1940 volunteer under it.
  - On ArkivDigital, archive search for "Finland" returns two creators [S3]: *Frivilliga i Finland, Finlandskommittén* goes with the 1939-1940 enlistment, and *Svenska brigaden i Finland* with 1918.

## 8. Båtsmän: navy series by naval station

- **Navy rolls are not in the army general-muster index** [S8], [S14]. Search the navy series: *Rullor flottan* 1635-1915, which includes the navy general muster rolls [S26], [S17].
- **Each *båtsman* company belonged to a naval station**, and the rolls are arranged by station: Karlskrona (series IV) or Stockholm (series XIIIc). A Norrland company, for example Medelpad's, is filed under Stockholm [S26]. Search the station's series, not the home province [S26], [S15].
- **Late 1800s:** per-man *båtsmansrullor* (books) exist; use the ArkivDigital boatswain list to find them [S17], [S26].
- **Pensions:** *båtsmän* and navy officers and NCOs all belonged to the navy pension fund (Flottans pensionskassa), 1642-1937 [S18].
- **A *sjöman* on a merchant ship is a civilian.** He is in the seamen's house (*sjömanshus*) records, not the *båtsman* rolls [S3], [S15].

## 9. Enlisted men: rolls survive only for garrisoned regiments, and contracts sit in the regiment's archive

- Enlisted regiments' general muster rolls survive only for regiments garrisoned in Sweden, Finland or Swedish Pomerania [S20]. ArkivDigital's index shows an enlisted hussar of 1880 with his birth date, parish and former name [S4].
- Do not compute a birth year from an enlisted roll's age. Recruits older than about 20-23 were not normally accepted, which gave older men a reason to state a lower age [S20]. Take the birth year from the baptism or household entry.
- **Contracts.** Look for enlistment and soldier contracts in Riksarkivet's archive database (NAD) under the regiment's archive at Krigsarkivet. Before 1800, expect them to be missing; few are photographed, and ArkivDigital is now photographing the Skåne regimental archives [S1], [S15]. If NAD lists no contracts for the regiment, record *contracts not listed*.
- An enlisted man of 1912-1920 can have a card; the parish books may also place him on the regiment's grounds, which names his regiment and company [S3].

## Close with a routing packet

Return:

- **Classification row:** branch, allotted or enlisted, rank class and period, each with the entry that supports it; parallel rows where uncertain.
- **Series rows:** for each search, the index or series, its coverage, the fields searched, the locator (regiment, company, number, year, volume and page, or card archive), and the status: *found*, *not found within coverage*, *outside coverage*, *not indexed (browse needed)* or *not listed in NAD*.
- **Soldier-name table:** each roll entry under the name and number, with age, province of birth, approval and discharge dates, and the man you assign it to.
- **Officer file:** the *meritband* used, first and last merit record, any birth proof, and the pension series and decision references.
- **Gaps:** years between musters, 1884-1901, lost cards, unindexed navy rolls and unphotographed regimental archives, each with its custodian.

The model builds the packet. The researcher decides identity.
