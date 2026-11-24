---
id: "australia-nz-record-routing"
title: "Route an Australian or New Zealand record to the holder and window of its date"
summary: "Route an Australian or New Zealand vital, electoral, arrival, Māori Land Court or Aboriginal agency record to its holder and date window."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "AUSTRALIA-NZ-RECORD-ROUTING-01", "text": "**Do not send a Port Phillip or Moreton Bay event to New South Wales because it predates separation.** Today's Victorian or Queensland index is the first stop."}]
handoff: ["convict-transportation-record-chain", "evidence-proof-judgment", "historical-place-name-resolution", "newspapers-com-search-recovery", "research-documentation", "source-citation"]
checked: "2026-11-04"
checked_basis: "opened 2026-11-04"
capabilities: {"browse": ["record catalogues and original images", "MyHeritage Australian vital and passenger indexes", "NAA RecordSearch and research guides"], "local_script": [], "extensions": [], "data_transfer": ["third-party-tool", "request"], "contact": []}
router: {"section": "Records by country and region", "group": "Canada, Latin America, Asia and Oceania", "order": 268}
---

# Route an Australian or New Zealand record to the holder and window of its date

Use this recipe before you search for an Australian or New Zealand birth, marriage, death, electoral roll, passenger arrival, naturalisation, newspaper notice, Māori Land Court record or Aboriginal agency file. Use it also for New South Wales gaol books and Victorian probate applications. It sends each search to the body that holds the record for that date and tells you when a miss means nothing. It prevents these failures:

- sending a pre-separation Port Phillip or Moreton Bay event to the New South Wales registry instead of today's state
- citing a pre-civil index entry as a civil certificate
- reading a miss inside a closure window, a pre-1912 roll or a Māori event in the general register as negative evidence
- assuming Federation moved every passenger list to the Commonwealth
- reading a miss in an API or an outdated catalogue as an absence
- treating whakapapa given in the Native Land Court as neutral fact

Link out for the shared steps:

- **A transported convict:** [convict transportation record chain](convict-transportation-record-chain.md).
- **OCR misses and reading a notice on the page image:** [newspaper search recovery](newspapers-com-search-recovery.md).
- **A place you cannot fix to a colony or district:** [historical place-name resolution](historical-place-name-resolution.md).
- **Citation format and the research log:** [source citation record](source-citation.md) and [research log and report](research-documentation.md).
- **Identity rulings:** [evidence/proof judgment](evidence-proof-judgment.md).

## Contents

- Inputs to gather first
- 1\. Send an Australian BDM search to today's state registry
- 2\. Read a pre-civil index entry as a church record
- 3\. Check the release window before reading a miss
- 4\. Search both New Zealand registers for a Māori event
- 5\. Route Aboriginal and Torres Strait Islander records by state and agency
- 6\. Read an electoral roll against the enrolment law of its date
- 7\. Route passenger lists by port and date, not by Federation
- 8\. Search Trove and Papers Past inside their digitised runs
- 9\. Search Archives New Zealand in Collections Search
- 10\. Read Māori Land Court minute books as contested testimony
- 11\. Route a naturalisation to the custodian for its date
- 12\. Check access and digitisation in NAA RecordSearch
- 13\. Find a New South Wales gaol entry by gaol and date
- 14\. Route a Victorian probate application by filing date and status
- Close with a routing packet

## Inputs to gather first

Gather these before searching:

- the event type and approximate date
- the place as each record writes it, and the colony, state or territory it lies in today
- whether the person was Māori, or Aboriginal or Torres Strait Islander, and the state or territory involved
- the port and year of arrival, and whether the passage was assisted
- any locator already seen: registration number, archive series and item number, Archives NZ R-number, minute book reference

## 1. Send an Australian BDM search to today's state registry

- **Search the registry of the state that holds the place today.** Its index also covers events from before the colony split off from New South Wales: Victoria from 1836 and Queensland from 1829 [S1], [S5], [S7].
- **Do not send a Port Phillip or Moreton Bay event to New South Wales because it predates separation.** Today's Victorian or Queensland index is the first stop.
- **Split the Northern Territory at 24 August 1870.** Civil registration there began on that date, and those records are with the NT registry [S24]. For NT events of 1856–1863, search New South Wales records; for 1863–1870, search South Australian records [S1].
- **Fix the start of civil registration for the state.** Tasmania 1838, Western Australia 1841, South Australia 1842, Victoria 1 July 1853, New South Wales and Queensland 1856 [S2], [S3], [S4].

**The Australian Capital Territory is the exception.** The area was part of New South Wales until 1911 [S1 @2026-11-13]. For births in the Canberra region before 1918, and marriages and deaths there before 1930, search the New South Wales indexes; such events may be registered under the districts of Queanbeyan or Yass [S1 @2026-11-13].

**If an Italian proxy-marriage packet lacks Victorian civil banns, look for the returned request in the consular correspondence.** In dispatch no. 167 of 15 January 1937, the Royal Italian Consulate in Melbourne returned the Carlton request, explaining that Victorian law did not require banns and that the notice could be posted at the consulate [S70].

**Read a Victorian “No Record” marriage return against the issuing office, name searched and index dates.** In the Office of the Government Statist’s 1937 return no. 6969, the negative result covers one name from 1928 through 30 June 1936 [S70]. In a migration case, test the opening year as an arrival lead in the passenger lists before recording a landing date [S70].

## 2. Read a pre-civil index entry as a church record

- **In the NSW, Victorian and Queensland indexes, entries from before those dates are transcribed church baptisms, marriages and burials.** The NSW registry holds transcribed copies, not the original church registers [S3]. The ranges are NSW 1788–1855 [S3], Victoria 1836–1853 [S5], and Queensland baptisms and burials 1829–1856 and marriages 1839–1856 [S7].
- **Record such an entry as a church-register entry, not a civil certificate.** Cite the church and the transcript.
- **Search the church registers directly before you call a pre-1853 Victorian event missing.** Every church was required to send its pre-1853 registers to the Victorian Registrar, and not every church did [S6].
- **For Tasmania, Western Australia and South Australia, read the registry's own page before you cite a pre-civil entry.**

## 3. Check the release window before reading a miss

- **Historical BDM indexes stop at rolling closure periods.** They differ by event type and jurisdiction. Look up each Australian state's windows on its own registry page. Never apply one state's cutoff to another.
- **New Zealand historical records open** [S8]:

  | Event | Released when |
  | --- | --- |
  | Birth of a living person | born 100 years ago or more |
  | Birth of a deceased person | died 50 years ago or more, or born 80 years ago or more |
  | Marriage | 75 years ago or more |
  | Death | 50 years ago or more, or the deceased was born 80 years ago or more |

- **A miss for an event still inside the window is out of scope, not negative evidence.**
- **Search the NZ historical index at bdmhistoricalrecords.dia.govt.nz.** It needs no verified RealMe account [S8]. BDM Online (bdmonline.dia.govt.nz) is the certificate-ordering service for verified RealMe users and approved organisations [S9]. Do not use it as the historical index.

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Apply the [privacy gate](../SKILL.md#privacy-gate) before sending the subject’s name and any event year or place to MyHeritage.

**Search MyHeritage’s Victorian indexes as a second pass.** Use the Victoria Birth Index for baptisms in 1837–1853 and birth registrations in 1853–1920 [S35 @2026-11-18] [S36 @2026-11-18]. Use the Victoria Death Index for burials in 1836–1853 and death registrations in 1853–1985 [S35 @2026-11-18] [S37 @2026-11-18]. For events outside those spans, check the Victorian registry’s historical index and its own release window [S38 @2026-11-18].

**Search MyHeritage’s Tasmanian birth and death indexes as a second pass.** Search *Australia, Tasmania Births* (1803–1933) for the child’s birth date and parents. Use the image to distinguish the place of registration from the place of birth when both appear [S45 @2026-11-22] [S47 @2026-11-22]. Search *Australia, Tasmania Deaths* (1803–1939) for the date of death and the separate registration year and place. Check the image for parents, spouse, burial and any reference to a will [S53 @2026-11-22] [S54 @2026-11-22]. In the official Tasmanian Names Index, the 1900–1933 birth and death search results cover baptisms and burials respectively. Use the record type when judging a miss [S48 @2026-11-22].

**Search MyHeritage’s Queensland birth and marriage indexes as a second pass.** Use *Australia, Queensland Births* (1829–1922) for the birth date and parents’ names and *Australia, Queensland Marriages* (1839–1947) for the marriage date and both spouses [S53 @2026-11-22] [S55 @2026-11-22] [S56 @2026-11-22]. If a search falls beyond those end years, return to the Queensland registry’s rolling windows [S74 @2026-11-22].

## 4. Search both New Zealand registers for a Māori event

- **New Zealand kept separate Māori registers:** marriages from 1911 until 1952, and births and deaths from 1913 until 1961–62 [S18]. The birth and death regulations apply to events from 1 March 1913 [S19].
- **For those years, search both the general and the Māori registers,** because some Māori events were entered in the general system [S18].
- **Read a birth- or death-index miss for a Māori person as expected, not negative,** before 1913 and in the Māori-register years after it. Registration could not be enforced, and many Māori births and deaths were never registered [S18]. Turn to the Māori Land Court minute books (step 10).

## 5. Route Aboriginal and Torres Strait Islander records by state and agency

- **Treat protector, mission and child-removal records as agency series.** They are held by state archives, churches and welfare departments [S21], [S22].
- **BDM indexes do not cover these agency files.** Search the holder's own catalogue by the person's name and place [S21], and its name indexes, such as church name indexes to mission registers [S22].
- **Expect restricted access.** Some Queensland records are closed for up to 100 years and are released through an administrative process [S21]. Access goes through dedicated Aboriginal records units, such as Queensland's Community and Personal Histories unit, and family-tracing services such as Link-Up [S21], [S23].
- **Read a BDM-index absence for such an ancestor as expected, not negative.**

## 6. Read an electoral roll against the enrolment law of its date

- **Commonwealth rolls survive from 1903** [S13]. Enrolment became compulsory by an Act passed in December 1911 that commenced on 27 March 1912 [S10]. Voting became compulsory in 1924 [S11].
- **Do not read a pre-1912 roll as near-complete.** An absence from a pre-1912 roll is not evidence of non-residence.
- **For Indigenous Australians, read the franchise steps.** The federal vote was extended in 1949 to ex-servicemen and to those already enrolled for state elections. In 1962 all Indigenous Australians gained the right to enrol, but enrolment stayed voluntary. Enrolment became compulsory in 1984 [S12], [S13]. Read an absence against the law for that person and date.
- **Treat the recorded address and any recorded occupation as dated observations for that subdivision.** Rolls omit occupation after 1983 [S13]. An entry does not prove household membership.

## 7. Route passenger lists by port and date, not by Federation

- **Before 1924, search the archive of the state where the ship arrived, except for Western Australia after 1900.** For those Western Australian arrivals, search the NAA first: the State Records Office says the lists after 1900 are generally held by the WA Branch of the National Archives of Australia [S32 @2026-11-16].

- **For Victoria, distinguish the original series from its copies.** Public Record Office Victoria holds inward overseas lists of unassisted passengers for 1852–1923 in VPRS 947, covering British, foreign and New Zealand ports. VPRS 7666 is the microfiche copy for British ports [S14 @2026-11-16].
- **After 1923, search the National Archives of Australia too.** PROV states that Victorian immigration records after 1923 are held by the NAA [S25 @2026-11-16]. Keep the state archive in the search: Queensland State Archives indexes immigrant ships bound for Queensland for 1922–1940 [S26 @2026-11-16].
- **Route by colony and date before you call a passenger search negative.**

**For an Irish famine-era arrival around 1848–1850, search both assisted and unassisted records at each plausible port, including Sydney, Port Phillip and Moreton Bay** [S39]. Use the ship and arrival date to identify the voyage. Record the native place, parents and any relatives in the colony as written when the assisted list gives them [S40].

**For assisted arrivals, include the NSW colonial lists.** Search the Agent’s and Board’s lists (NRS 5316 and NRS 5317) for Sydney and Moreton Bay, and NRS 5318 for Port Phillip [S40 @2026-11-20]. For Port Phillip, also search Public Record Office Victoria’s assisted index for 1839–1871 [S41 @2026-11-20]. For Moreton Bay, also check Queensland State Archives’ Assisted Immigration index for 1848–1912 [S44 @2026-11-20].

**For unassisted arrivals, choose a source that covers the port and year.** For Sydney, use the 1842–1855 name index (National Library of Australia, mc N 1187) [S40 @2026-11-20]. For Port Phillip before 1852, look for the voyage in Melbourne’s inward shipping register and check the shipping columns of *The Argus* for names [S42 @2026-11-20]. Treat a miss in Victoria’s unassisted index as out of window for those years [S42 @2026-11-20]. For Moreton Bay, use *Early Shipping in Moreton Bay*, volume 1 (1846–1859), to identify the voyage. Its extracts name saloon passengers [S43 @2026-11-20]. For steerage, take the voyage details to the original shipping columns of *The Moreton Bay Courier*. A steerage-name miss in the extracts leaves the question open [S43 @2026-11-20].

**For Victorian assisted passages, read “assisted” as a colonial-government subsidy that could cover all or part of the fare.** Check the list’s employment fields for the person’s actual arrangements [S45] [S41].

**For Queensland assisted arrivals in 1848–1912, use the state archive’s Assisted Immigration index to reach the register.** Follow the linked scan and use the indexed page number when supplied to locate the passenger on the original. Record the ship and arrival date and port as shown [S45 @2026-11-22] [S44 @2026-11-22].

**For South Australian travel, check both directions.** Use State Records’ arrival indexes and the lists of ships and passengers departing Port Adelaide for overseas ports in GRG 41/35 (1889–1940) [S49 @2026-11-22] [S51 @2026-11-22]. For earlier direct overseas departures, search the Horner Index (1836–1887) by surname or ship. Record the ship and dated ports for each leg the records identify [S52 @2026-11-22].

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Apply the [privacy gate](../SKILL.md#privacy-gate) before sending passengers’ names and any voyage dates or ports to MyHeritage.

**Search MyHeritage’s British Assisted Passengers to Victoria index for 1839–1871 arrivals.** Use the reported age, ship, captain and arrival date to distinguish candidates. Take the matching ship and year to the official assisted list [S45 @2026-11-22] [S46 @2026-11-22] [S41 @2026-11-22].

**Search MyHeritage’s Queensland Nominated Immigrants index by passenger name for 1905–1928.** Use birth year and ship as clues when shown [S49 @2026-11-22] [S50 @2026-11-22]. Keep an enquiry, sponsorship or nomination year under its own event type. Use the Queensland State Archives index to identify that event and seek a passenger arrival for confirmation before recording immigration [S44 @2026-11-22].

**If the Australian voyage has no complete passenger list, pivot to the ship and arrival date.** Search the port’s immigration or shipping registers, arrival indexes and newspaper shipping columns. Record which source establishes the voyage and which names the passenger [S63] [S40].

**Check how the list counts steerage passengers and children.** A steerage total leaves the names unknown. When a child has no individual entry, search the parent or accompanying adult and read the original entry for a child count or a “child with” notation [S63] [S40] [S64].

**For postwar assisted migration, follow the passenger arrival to the migrant selection file.** Use the ship and arrival date in RecordSearch and in the port’s newspaper shipping reports. In the selection records, check the voyage’s nominal roll and any family entry for accompanying names. For displaced persons, search the Canberra guide’s voyage or flight roll route, where one catalogue entry can cover a family [S63 @2026-11-22] [S65 @2026-11-22] [S71 @2026-11-22] [S40 @2026-11-22].

**For Italian migration, search RecordSearch for the passenger arrival and use the NAA’s Perth, Sydney and Brisbane guides to select a series.** In Perth and Sydney, check the migrant selection series for the relevant period. In Brisbane, check the passenger lists, personal documents and reception files by date [S69 @2026-11-22] [S65 @2026-11-22] [S66 @2026-11-22] [S67 @2026-11-22] [S68 @2026-11-22].

If the question concerns what immigration staff recorded about health or character, check the medical report and officer assessment in the postwar selection paperwork. Attribute each assessment to its author and record when it was made [S63] [S66] [S73].

For a surviving steamship passenger contract ticket, record the fare, class and ports shown as terms of the booking. Verify the voyage actually taken against the arrival record [S63] [S72].

Search the ship name and sailing date for another passenger’s diary, journal or shipboard newsletter. Match the vessel and voyage, and use the account as that passenger’s description [S33]. Only a transcript excerpt was inspected for this search suggestion [S34].

## 8. Search Trove and Papers Past inside their digitised runs

- **Use Trove (Australia) and Papers Past (New Zealand) for family notices and shipping arrivals.**
- **Read each title's digitised run before you search it.** A zero-hit search outside that run is a coverage gap, not a negative.
- **Treat a DigitalNZ API search of Papers Past as a first pass.** A key is optional for public content but recommended for regular use [S15]. Re-run any miss on the Papers Past site, and check each hit on the Papers Past page image with the newspaper recipe.

- **Search Trove's government gazettes as a lane of their own, not only its newspapers.** The National Library of Australia lists certificates of naturalisation, employment notices and military service among what they hold [S27 @2026-11-12] [S29 @2026-11-12]. Its gazette guide adds bankruptcies, company registrations and Public Service appointments. On Trove the Commonwealth gazette runs 1901–2012 and New South Wales 1832–2001; Victoria's, for 1836–1997, are on a State Library Victoria site instead [S28 @2026-11-12].

- **Give at least three letters before Trove's `*` wildcard** [S31 @2026-11-12]. A shorter stem is not a valid search of a variably spelled surname, so its zero is not a negative.

## 9. Search Archives New Zealand in Collections Search

- **Search Collections Search (collections.archives.govt.nz), the live Archives NZ catalogue** [S20]. If an older guide points to another catalogue, re-run its search in Collections Search before you read a miss.
- **Record the R-number.** It is each record's unique code, and you can search it directly [S20].

## 10. Read Māori Land Court minute books as contested testimony

- **Use the Native (Māori) Land Court minute books as a major written source of whakapapa (genealogy).** They record the court's proceedings and decisions, including whakapapa and tribal history given as evidence in title hearings [S16], [S17].
- **Record the full minute book reference as the locator.**
- **Read whakapapa recited to win title as claimant testimony in a contested hearing, not neutral fact.** Record who gave it, for which block and against whom.

## 11. Route a naturalisation to the custodian for its date

- **From 1904, request the file from the National Archives of Australia.** Naturalisation became a Commonwealth responsibility that year [S30 @2026-11-12].
- **Before 1904, go to the state archives for Queensland, New South Wales, Tasmania and Western Australia, and to the NAA for Victoria and South Australia** [S30 @2026-11-12]. Date the naturalisation from its gazette notice first, then choose the custodian.

**For an early Queensland naturalisation, check Queensland State Archives’ Naturalisations 1851–1908 index.** Carry the oath year and number, any place given and the catalogue reference into the underlying series. Use the reference to select the Supreme Court district (Brisbane, Rockhampton or Townsville) or the Colonial Secretary’s Office or Government Residents Office records. For 1904–1908, check the Queensland index alongside the Commonwealth search [S83 @2026-11-23] [S84 @2026-11-23].

**For a Queensland oath in 1880–1885, also check the printed return.** Look up the *Return of aliens naturalized 1880–1885* in the Queensland Legislative Assembly’s *Votes and Proceedings*, 1885 session, volume II, pages 231–260. Record the page and the oath date as shown [S53] [S84] [S85].

## 12. Check access and digitisation in NAA RecordSearch

**Use the National Archives of Australia’s topic guides to choose a RecordSearch series** for Commonwealth immigration, naturalisation, war service, Aboriginal and Torres Strait Islander history or other federal records. For a missing service or postwar immigration file, check the relevant guide and search for the series as well as the item. Record separately whether the item is listed and whether it has an image [S57 @2026-11-22] [S58 @2026-11-22] [S59 @2026-11-22] [S61 @2026-11-22].

**Calculate the open access date under the Archives Act 1983.** For ordinary Commonwealth records created after 2000, use 1 January of the creation year plus 21. Check the Act’s separate tables or rules for earlier records, Cabinet notebooks and Census information. Then check the item’s access status [S57 @2026-11-22] [S60 @2026-11-22] [S62 @2026-11-22].

**Read the access status separately from digitisation.** Open means the whole item has been released. Open with exception means some content is withheld under an exemption. Check the reason for restriction. View the released material online if an image is available [S57 @2026-11-22] [S58 @2026-11-22] [S60 @2026-11-22].

**Privacy gate:** <!-- privacy-gate: request --> Apply the [privacy gate](../SKILL.md#privacy-gate) and the [record request rules](../SKILL.md#record-requests) before sending the requester’s contact details, the item identifier and any required details about the people named in the request to the NAA.

**Request a copy or research-centre viewing** for released material with no online image [S57 @2026-11-22] [S58 @2026-11-22].

**Submit an access application for an item marked “Not yet examined”** if it is in the open access period. In RecordSearch, start with “Request copy” or “Issue to research centre” and select “Submit an access application”. Allow for a decision within the standard 90-business-day consideration period or the extended period the NAA gives you [S57 @2026-11-22] [S60 @2026-11-22] [S61 @2026-11-22].

## 13. Find a New South Wales gaol entry by gaol and date

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Apply the [privacy gate](../SKILL.md#privacy-gate) before sending the inmate’s name and any birth details or gaol name to MyHeritage.

**Search MyHeritage’s New South Wales Gaol Inmates & Photos collection (1870–1930).** Use the gaol and portrait date to identify the Gaol Photographic Description Book in the NSW State Archives Collection. Check the date span for that gaol before interpreting a miss. Cite the gaol, archival series and volume or item reference, with the page if shown [S75 @2026-11-23] [S77 @2026-11-23] [S78 @2026-11-23] [S79 @2026-11-23].

**Read the original entry for the prisoner number, recorded birth year and place, and portrait date.** Transcribe the written physical description and any scars or other recorded marks. Use the portrait as part of the record and keep facial resemblance out of the identity assessment [S76] [S77] [S78] [S79].

**Record the sentencing court and gaol as separate places.** Treat the gaol and portrait date as a dated custody lead. Check the gaol’s entrance records to corroborate custody, and seek separate evidence of any residence in the town [S79] [S86].

In one published case the researcher reported a sentence at Coonamble and a gaol entry at Goulburn [S75].

## 14. Route a Victorian probate application by filing date and status

**Search the Supreme Court of Victoria’s Probate Office application index** for probate or administration applications filed from 1970 onwards. Search by the deceased’s surname and narrow by year or date of death. Expand the matching row and record the application number and status. Verify that a grant was issued before recording one [S80 @2026-11-23] [S81 @2026-11-23].

**Use the Public Record Office Victoria (PROV) for applications filed before 1 July 2020 or marked “Transferred to PROV”.** Use the filing date and index status to choose the holder [S81 @2026-11-23] [S82 @2026-11-23].

**Privacy gate:** <!-- privacy-gate: request --> Apply the [privacy gate](../SKILL.md#privacy-gate) and the [record request rules](../SKILL.md#record-requests) before sending the requester’s details, the application number and any required personal details about people named in the request to the Victorian Probate Office through RedCrest-Probate.

**Request a search through RedCrest-Probate** for an application marked “Application granted”, filed on or after 1 July 2020 and still held by the court. Enter the application number in “My File Searches” [S81 @2026-11-23] [S82 @2026-11-23].

Use the [probate case document inventory](probate-case-document-inventory.md) to work through the file.

## Close with a routing packet

Return:

- **Jurisdiction row:** the place under each form seen, today's state or territory, the colony on the event date, and the registry searched.
- **Series rows:** for each search, the holder, the series or index, the years and release window it covers, the locator (registration number, archive series and item number, Archives NZ R-number, minute book reference), and the status: searched, found, not found, out of window or restricted.
- **Record type:** civil certificate, transcribed church entry, roll observation or testimony.
- **Gaps:** events inside a closure window, pre-1912 rolls, Māori or Aboriginal events outside the BDM indexes, digitised-run gaps, and restricted files with their access route.

The model assembles this packet. The researcher decides identity and kinship.
