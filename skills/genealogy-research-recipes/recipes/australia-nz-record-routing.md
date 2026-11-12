---
id: "australia-nz-record-routing"
title: "Route an Australian or New Zealand record to the holder and window of its date"
summary: "Route an Australian or New Zealand birth, marriage, death, electoral roll, arrival, newspaper notice, Māori Land Court record or Aboriginal agency file to the holder and date window of its record."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "none"
gates: []
guardrails: [{"id": "AUSTRALIA-NZ-RECORD-ROUTING-01", "text": "**Do not send a Port Phillip or Moreton Bay event to New South Wales because it predates separation.** Today's Victorian or Queensland index is the first stop."}]
handoff: ["convict-transportation-record-chain", "evidence-proof-judgment", "historical-place-name-resolution", "newspapers-com-search-recovery", "research-documentation", "source-citation"]
checked: "2026-11-04"
checked_basis: "opened 2026-11-04"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"tier": "pointer", "group": "Country record routing", "order": 1064}
---

# Route an Australian or New Zealand record to the holder and window of its date

Use this recipe before you search for an Australian or New Zealand birth, marriage, death, electoral roll, passenger arrival, newspaper notice, Māori Land Court record or Aboriginal agency file. It sends each search to the body that holds the record for that date and tells you when a miss means nothing. It prevents these failures:

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

- **Before 1924, search the archive of the state where the ship arrived.** Federation did not move the lists: Public Record Office Victoria holds inward overseas passenger lists from British ports for 1852–1923 (VPRS 947 and 7666) [S14].
- **After 1923, search the National Archives of Australia too.** PROV states that Victorian immigration records after 1923 are held by the NAA [S25]. Keep the state archive in the search: Queensland State Archives indexes immigrant ships bound for Queensland for 1922–1940 [S26].
- **Route by colony and date before you call a passenger search negative.**

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

## Close with a routing packet

Return:

- **Jurisdiction row:** the place under each form seen, today's state or territory, the colony on the event date, and the registry searched.
- **Series rows:** for each search, the holder, the series or index, the years and release window it covers, the locator (registration number, archive series and item number, Archives NZ R-number, minute book reference), and the status: searched, found, not found, out of window or restricted.
- **Record type:** civil certificate, transcribed church entry, roll observation or testimony.
- **Gaps:** events inside a closure window, pre-1912 rolls, Māori or Aboriginal events outside the BDM indexes, digitised-run gaps, and restricted files with their access route.

The model assembles this packet. The researcher decides identity and kinship.
