---
id: "scottish-parish-statutory-record-recovery"
title: "Recover a Scottish birth, marriage or death across parish and statutory registers"
summary: "Recover a Scottish birth, baptism, marriage or death across Old Parish, statutory, corrected-entry and kirk-session records."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "SCOTTISH-PARISH-STATUTORY-RECORD-RECOVERY-01", "text": "Treat register gaps and unsearched denominations as coverage still to search, not as proof the event did not happen."}]
handoff: ["quaker-meeting-record-recovery", "uk-census-and-1939-register-interpretation"]
checked: "2026-11-04"
checked_basis: "opened 2026-11-04"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": ["request"], "contact": []}
router: {"section": "Records by country and region", "group": "Britain and Ireland", "order": 149}
---

# Recover a Scottish birth, marriage or death across parish and statutory registers

Use this recipe to recover a Scottish birth, baptism, marriage or death. First match the event date to the right register system and parish unit. Read each Old Parish Register (OPR) entry type from the image. Treat register gaps and unsearched denominations as coverage still to search, not as proof the event did not happen. Retrieve statutory, Register of Corrected Entries (RCE) and kirk-session leads as separate dated sources.

Some steps overlap with other recipes; use those recipes for them:

- Banns indexed as marriage dates, and reading the whole marriage entry: [evidence/proof judgment](evidence-proof-judgment.md) (§ creation stages within a marriage record).
- Deciding whether two entries are one child or two: the same recipe, § same-named siblings and apparent twins.
- FamilySearch Catalog and image routes: [FamilySearch workflows](familysearch-practical-record-workflows.md).
- Whether a negative search is reasonably exhaustive: [standards audit](genealogy-standards-audit.md).

## Contents

- Fix the jurisdiction as of the event date
- Choose the register system by date
- Classify each OPR entry from the image
- Test gaps before reporting absence
- Follow corrections and church-court records as later sources
- Read Scottish census images as enumeration books
- Route executry and land apart from English probate
- Bridge censuses with valuation rolls
- Check school records and parish context
- Close with an event register

## Fix the jurisdiction as of the event date

- **Record the county exactly as the record writes it.** Before 1890, some parishes lay in detached parts of another county, and some parishes straddled a county line. The Boundary Commissioners under the Local Government (Scotland) Act 1889 reassigned these in 1889–92. For example, most of Caputh's detached parts went to Angus parishes in 1891. Indexes can therefore put one parish in different counties before and after the change. The historical index can use a different county from the one written in the entry [S1], [S3]. For Cairnie, the Scotland’s People gazetteer gives both Aberdeen and Banff before 1891, and places the civil parish wholly in Aberdeen from 1891 [S43]. Search both historical county headings and record the parish and date.
- **Do not accept a modern standardized place.** FamilySearch place standardization can offer present-day units. [S3] "Aberdeen, Grampian" is correct only for events in the regional period, 16 May 1975 to 1 April 1996. County names also changed: Edinburghshire became Midlothian, Elginshire became Moray and Forfarshire became Angus. Follow a family across a renaming under both names. [S1], [S3]
- **Record the parish number as well as its name.** The number resolves Gaelic or misspelled forms. [S10] One presenter says a number with a decimal suffix (her example is 542.1) marks a parish carved from the parent parish (542), and that for years before the daughter parish existed you should search the parent parish. NRS and ScotlandsPeople guidance does not confirm this meaning; ScotlandsPeople uses suffixes such as 685-2 to split city registration districts. Check what a suffix means for your parish before you rely on it. [S10]
- **Identify the parish within the town.** For Aberdeen, Brady distinguishes St Nicholas and Old Machar among the parishes serving the city [S2]. Compare the parish or registration-district name and number on the entry before selecting the next register.
- **Classify each "parish."** It may be a civil parish, a church (ecclesiastical) parish or both. A statutory registration district is a third unit: ScotlandsPeople says districts were formed from parishes and burghs, some divided and others united, and cities are split into numbered districts such as 685-2. A quoad sacra parish has church functions but no civil ones, and several can lie inside one civil parish. ScotlandsPeople's place pages label a parish that is both civil and church as *quoad omnia*. Search statutory records by the registration district in force in the event year and church registers by the church unit. Do not use map distance between two parishes to decide whether children belong to one family. [S5], [S6], [S7]

## Choose the register system by date

- **Before 1855:** search the Church of Scotland OPRs, the Free Church registers and other denominations' registers. The presenters say OPRs are sparse before about 1750, and some parishes have none. [S1 @2026-11-07], [S8 @2026-11-07] Earlier baptism entries often leave out the mother's name, and practice varies by parish. In Brady’s 1743 baptism example, the entry identifies the father as a schoolmaster and omits the mother. Retain the occupation when tracing the family. [S1 @2026-11-07]
- **From 1 January 1855:** use statutory registration. [S1 @2026-11-07]
- **Check whether the image is online yet.** ScotlandsPeople shows statutory images only for births over 100 years old, marriages over 75 and deaths over 50. One more year is added each January; since January 2026 the newest images are births of 1925, marriages of 1950 and deaths of 1975. A younger entry is in the index only. Its missing image is an access limit, not a register gap. [S27 @2026-11-07], [S28 @2026-11-07] An image costs 6 credits (£1.50) as of 7 November 2026. NRS consulted from 13 July to 4 October 2026 on raising it to 10 credits (£2.50); no decision had been published by 7 November 2026, so check the current charges. [S29 @2026-11-07], [S30 @2026-11-07], [S45 @2026-11-07]
- **Privacy gate:** <!-- privacy-gate: request --> A certificate of a younger entry can name people who may be living; answer the privacy gate in `SKILL.md` before ordering it. For an entry still inside the closure period, use the search result's "order certificate" link: an official copy costs £12 as of 7 November 2026. [S27 @2026-11-07], [S31 @2026-11-07]
- **If a pre-1855 baptism names only the father:** look for a sibling whose birth, death or registration falls after 1855. That record gives the mother's name and maiden surname, which you can use to search for the parents' marriage. [S9 @2026-11-07]
- **Turn statutory fields into retrieval targets, not facts.** Each item below is a statement made by the informant.
  - **Birth entry:** gives the date and place of the parents' marriage in 1855 and from 1861 onward. Births registered in 1856–60 leave this field out, so its absence in those years is not missing data. [S1 @2026-11-07]
  - **Marriage entry:** copy both partners’ parents, including the mothers’ maiden surnames. A parent marked “deceased” gives a lead for a death before the marriage. Brady found exceptions, so check the death or a later record before assigning the date range [S1 @2026-11-07].
  - **Death entry:** names the decedent's spouse or spouses, except in 1856–60, when spouses were not recorded. One death entry lists three wives in sequence, though Brady found only two of the marriages. Keep one search row per spouse and use the order to narrow the third search. Use the informant's stated relationship and address as the next census lead. [S1 @2026-11-07], [S4 @2026-11-07] The death index gives the decedent's mother's maiden surname from 1974; for earlier years it is being added gradually and is often missing, so leave that search field blank for a pre-1974 death. [S32 @2026-11-07]
- **Check any family registration from 1855.** Entries from that first year carry extra fields. A birth adds the parents' ages and birthplaces, the parents' marriage, and counts of living brothers and sisters. A death lists the decedent's children and their ages. Turn the counts into a list of named children still to find in registers and censuses. Do not treat the counts as a finished family. [S1 @2026-11-07]
- **Do not treat "Jr" or "Sr" as father and son.** The labels can mark a grandfather, an uncle or a more distant relative. [S4 @2026-11-07]
- **Search the minor records for a death at sea.** A Scot who died at sea on a British-registered merchant ship is recorded in the Marine Returns, not a district death register. [S24 @2026-11-07], [S25 @2026-11-07] To find them, search statutory deaths on ScotlandsPeople and choose Minor Records. [S24 @2026-11-07] The Marine Returns cover merchant seamen, including Second World War losses. They also cover some wartime Royal Navy, Royal Marines and naval reserve deaths at sea. [S24 @2026-11-07], [S26 @2026-11-07] The Second World War War Returns cover only members of the armed forces, and they are incomplete. [S25 @2026-11-07] Search them as well for a serviceman, but not for a merchant seaman. Do not treat a missing district death entry as survival until you have searched the minor records. [S23 @2026-11-07]

For a person born before 1855 whose parents are unknown, search for a Scottish death from 1855 onward, including for someone who married before statutory registration. Most death entries give the father's name, surname and occupation, the mother's name and maiden surname, and whether each parent had died [S34]. Read them as the informant's statements, like the other fields. John Dawson was 67 in the 1861 Scottish census, but Perl traced him to Pennsylvania, where he died around 1869 [S35]. Use the last known residence and emigration evidence to redirect the death search.

## Classify each OPR entry from the image

- **Leave an OPR index entry unclassified until you read the original.** The index does not show whether an entry is a proclamation of banns or a marriage. [S8]
- **Read the date's meaning from the entry wording, register by register.** Some registers record the marriage date and some record the proclamation of banns. [S8] Where an entry says "regularly proclaimed and married", Brady reads the date as the first proclamation, with the ceremony after the third Sunday's reading. Record that as "married on or after [date]", not as the marriage date. All three proclamations could be made on one day if a fee was paid, so the marriage can follow the date closely. [S4], [S8]
- **Keep every date the entry gives as its own field.** Some rural entries give both a contract date and a marriage date. Early baptism entries can give both a birth date and a baptism date. [S1]
- **Do not move a Scottish January–March date into the next year.** Scotland has started the year on 1 January since 1600, while England kept 25 March until 1752. [S12], [S13], [S14] An OPR date between 1 January and 24 March from 1600 onward is already in the modern year: do not add a year to it and do not double-date it. Where a Scottish document itself writes a double date such as 1 February 1699/1700, the later year is the Scottish year. [S12] The only 1752 change in Scotland is the Gregorian 11-day shift: Wednesday 2 September was followed by Thursday 14 September. [S12], [S14] The English 25 March check still applies to English dates before 1752, including English Quaker records; see [Quaker meeting record recovery](quaker-meeting-record-recovery.md).
- **Keep two entries for one couple or child as two observations.** They may be:
  - banns proclaimed in both partners' parishes [S8];
  - a baptism in a neighbouring parish [S8];
  - separate birth and baptism dates [S1];
  - a later batch or neglected-entry registration (see the next section).

  Send any merge or separation decision to evidence/proof judgment.
- **Read the rough draft as well.** Where a rough draft ("blot" or scroll) register survives alongside the fair-copy register, compare them entry by entry; it can hold entries missing from the OPR. Keep each reading and locator separate. [S7]
- **Treat an entry marking a nonconformist as a lead to that church's records.** Nonconformist and seceding congregations kept separate record sets. [S7]

## Test gaps before reporting absence

- **Stamp duty years, 1783–1794.** The Stamp Duty Act 1783 charged 3d on each register entry until its repeal in 1794. Marriages largely survive, but many baptisms are missing and burials are nearly absent. Some families waited for the tax to end and then had entries made. A burial register from those years can be mainly a record of tax paid. [S2], [S4], [S7]
- **Register of Neglected Entries.** The Registrar General for Scotland compiled this register after civil registration began in 1855. It holds births, marriages and deaths from 31 December 1800 to 1 January 1855 that had not been registered, entered later on a sheriff's warrant with a fee. Record the date of entry separately from the stated event date.
- **Batch entries inside the OPR.** Brady describes ministers closing registers in 1819 and 1853–55 and entering earlier unrecorded baptisms as a group. Four children appear consecutively in the same 1854 Old Parish Register. Record the registration date separately from the stated birth or baptism date. [S1] Tanner says quoad sacra parishes that began registers after 1855 also added some delayed entries; NRS and ScotlandsPeople guidance does not confirm this. [S7]
- **The Disruption, 1843–1855.** Families who joined the Free Church drop out of Church of Scotland registers. Search the Free Church registers before inferring a move or a death. Brady puts the walk-out at 60% of congregations, "especially to the north and east", and says it matters anywhere north of the Highland line; those figures and that direction are hers and unconfirmed. Brady found no earlier entries in either set for the family whose four children appear together in the 1854 OPR [S1], [S2]. Extend the date range past the expected baptism before reporting a gap.
- **Other recorded breaks.** Presenters note other breaks in the records before 1855 and parishes left without a minister, when baptisms may have gone unrecorded. Check the coverage of the specific parish register. [S5], [S6], [S8]
- **Search each denomination separately.** ScotlandsPeople splits church registers into Church of Scotland OPRs, Catholic Parish Registers and Other Church registers. Run and log each as its own search; a no-hit in one does not cover the others. [S5]
- **Treat payment entries as indirect evidence.** Fee and payment records (caution fees, stamp-duty payments, mortcloth records) show a charge or payment, not the event itself. [S4], [S8], [S11]

**Search the selected Scottish births and baptisms index.** For a missing Scottish birth or baptism, search MyHeritage’s *Scotland, Selected Births & Baptisms, c. 1640 - c. 1860* (collection 10321), listed as free, and open plausible matches [S46 @2026-11-21], [S47 @2026-11-21]. Use any parish and event details to locate the underlying church record. Continue searching the relevant parish and denominational registers after a miss.

**Use children’s baptisms to trace a census household before 1855.** Record any stated abode separately from the parish of baptism [S49]. Compare the parents named in the baptism entries with the names and relationships in the census before linking the records [S48], [S49]. If the family drops out of the parish registers, search church registers in places where relatives are documented and in nearby industrial communities that fit the family’s work history [S48].

## Follow corrections and church-court records as later sources

- **Check for an RCE stamp.** Follow the marginal reference from the statutory entry to the Register of Corrected Entries, and cite the later entry separately. Brady describes a marriage correction with a summary of a bigamy case and a related divorce [S4 @2026-11-19]. Scotland’s People says birth corrections may add a father after a paternity case or subsequent marriage; its statutory birth guide says the link to the RCE page is free to view [S44 @2026-11-19].
- **Browse the unindexed kirk-session minutes.** On ScotlandsPeople these are in Virtual Volumes, found by place search. They are free to view; saving an image costs 2 credits (50p) as of 7 November 2026. [S29 @2026-11-19], [S33 @2026-11-19] Read:
  - a couple of weeks either side of a banns entry, for a marriage date [S4 @2026-11-19];
  - around a conception or birth date, for discipline cases. [S5 @2026-11-19], [S6 @2026-11-19]
- **Record each kirk-session meeting separately.** A local transcription of the 1840 Sandwick proceedings in Shetland records the mother naming the father, his denial and then his admission at a later meeting [S5 @2026-11-19], [S6 @2026-11-19]. Preserve the date, speaker and wording of each statement.

  Compare the named mother with the woman in the next census household. In the Sandwick case the woman who raised the child was the stepmother [S5], [S6]. The minutes establish what the church court recorded about paternity.
- **Choose the church register from the civil marriage entry's denomination, not its venue.** Read the "how married" wording (for example, "after banns according to the forms of" a named church) and the officiating minister's signature to identify the denomination and congregation. Use the place of marriage only as an extra locator: regular marriages often took place in private homes. An irregular marriage has no officiating minister and may have no church entry. Where the entry indicates a Catholic marriage, search Findmypast's Scottish Catholic collection, which covers all eight dioceses, for the religious record of the same event. Keep the civil and church entries as two records. [S11]

- **Locate the kirk-session volume before browsing.** NRS's OPR coverage guide links Appendix 1 for pre-1855 vital entries in CH2 records [S37 @2026-11-16]. Use that list to select the reference and years. If the volume is absent from ScotlandsPeople, or the search extends beyond 1855, search the NRS catalogue by parish name and "kirk session" [S41 @2026-11-16]. Record the holding repository and CH2 volume reference. Local archives hold some originals under NRS charge and superintendence [S38 @2026-11-16].

- **Search accounts as well as minutes when an OPR event is missing.** Check for baptisms and marriages dispersed through session minutes, including irregular-marriage payments, and for grave-digging, coffin and mortcloth charges as indirect death leads [S41]. ScotlandsPeople also describes mortcloth accounts, poor relief and certificates of transference [S36]. Record the person, payment or certificate, date and wording separately; a transference certificate is a movement lead rather than proof of where someone was born.

## Read Scottish census images as enumeration books

- **Every Scottish census image from 1841 to 1911 is an enumeration book.** The household schedules, 1911 included, were destroyed once the census work was finished; the books hold the enumerator's transcription of them. [S20], [S21] A Scottish 1911 entry is therefore an enumerator's copy, not the household's own statement. Do not carry over the England and Wales 1911 household-schedule rule from [UK census and 1939 Register interpretation](uk-census-and-1939-register-interpretation.md). The images are on ScotlandsPeople, and some 1841 books are lost. [S21]
- **Gaelic was first counted in 1881, not 1871.** [S22] The G or G and E marking in the enumeration books dates from 1891. [S21] Do not expect a Gaelic answer before 1881.

## Route executry and land apart from English probate

- **Executry is not probate.** Commissary courts confirmed executors until 1823, when the local courts were abolished and their business passed to the sheriff courts; Edinburgh's court kept a limited jurisdiction until it was abolished in 1836. [S16] Search the commissary court registers before that and the sheriff court registers after it.
- **A testament dative does not prove intestacy.** A testament testamentar confirms an executor the deceased named. A testament dative confirms an executor appointed by the court because the deceased named none; the statutory form defines it by the missing executor, not by a missing will. [S15], [S18] NRS and ScotlandsPeople guides shorten this to "no will"; do not repeat that as a finding.
- **Do not look for land in a testament before 1868.** Only from 1868 could a will pass heritable property. [S15] Trace earlier land through sasines and services of heirs (retours).
- **Search the right index for the year.** ScotlandsPeople indexes wills and testaments from 1513 to 1925 [S17] (NRS gives the start as 1514 [S15]). For 1926–1984 use the Calendar of Confirmations: NRS holds the 1901–1959 volumes as digitised Virtual Volumes in its search rooms, and the 1960–1984 Calendar as digitised microfiche cards. For 1985–1999, ask NRS staff to search their computer index, which covers only part of 1999. For a testament recorded from 2000 onwards, ask the Commissary Department of Edinburgh Sheriff Court; NRS does not hold it. [S15]

## Bridge censuses with valuation rolls

- **Use the rolls for residence and ownership between censuses.** Assessors compiled valuation rolls every year from 1855, naming the proprietor, tenant and occupier of each property with its annual rateable value. [S19] ScotlandsPeople has indexes and images for 1855, 1865, 1875, 1885, 1895, 1905, 1915, 1920, 1925, 1930, 1935 and 1940. [S19]
- **A roll is not a household list.** It names only the owner and the resident head of household. Properties rented at under £4 a year, unless on a long lease, carry little detail. [S19] Absence or a bare entry does not prove the person lived elsewhere.
- **Search by place as well as by name.** The search form has place, parish and burgh fields. The index expands every Mc to Mac; also allow for M' spellings and tee-names (by-names). [S19]

## Check school records and parish context

- **Privacy gate:** <!-- privacy-gate: request --> An admission entry for a pupil who may be living names that person; answer the privacy gate in `SKILL.md` before requesting it from an archive.

- **Use school admissions for a later statement about a child's birth.** Admission registers can contain the pupil's name, birth date and address. Log books concern school events and staff and very rarely give individual pupil information [S39]. Retrieve the admission entry for a pupil; use the log for a teacher or school context. Keep the school's birth-date statement separate from a statutory birth entry and record any disagreement. A child's absence from the log does not establish absence from the school.

- **Use parish reports to choose BMD substitutes.** Read the parish's Old Statistical Account (1791–99) and New Statistical Account (1834–45) for ministers' descriptions of local conditions [S40], [S42]. Follow any named church or school as a lead to its own records when a register entry is missing.

## Close with an event register

Return the following:

- the jurisdiction as written and as of the event date, the parish number and type, the registration district, and the register system;
- each entry classified from its image, with its locator;
- the gap periods and denominations searched, and those not searched;
- the informant-supplied statutory leads as retrieval targets, noting the 1856–60 field omissions where relevant;
- RCE and kirk-session observations, each dated separately;
- the testament, valuation-roll and census series searched, with the court or index years covered.

Leave identity and parentage rulings to evidence/proof judgment.
