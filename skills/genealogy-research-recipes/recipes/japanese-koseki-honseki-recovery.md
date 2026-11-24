---
id: "japanese-koseki-honseki-recovery"
title: "Recover the kanji name and honseki before requesting a Japanese koseki"
summary: "Recover the kanji name and full historical domicile (honseki) before requesting a Japanese family register (koseki)."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "JAPANESE-KOSEKI-HONSEKI-RECOVERY-01", "text": "One spoken reading can be written with many kanji combinations, so a romanized name does not identify the person. The request needs the exact registered Japanese spelling, kanji or kana as recorded ([Kagoshima City naming FAQ](https://www.city.kagoshima.lg.jp/faq-kurashi/shimin/q113.html))."}]
handoff: []
checked: "2026-11-07"
checked_basis: "opened 2026-11-07"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": ["request"], "contact": []}
router: {"section": "Records by country and region", "group": "Canada, Latin America, Asia and Oceania", "order": 263}
---

# Recover the kanji name and honseki before requesting a Japanese koseki

Use this recipe when someone wants a Japanese family register (koseki) for an emigrant ancestor and has only a romanized name, a remembered region or a prefecture. It covers the steps that come before the request: get the exact kanji name and the full historical permanent domicile (honseki), then trace that domicile to the municipal office that holds the register today. It also covers eligibility and retention checks. The record routes in steps 1 and 2 are for emigrants to Brazil. Routes for other destinations such as Hawaii, the US mainland or Peru are not covered here. Do not use this recipe to rule on identity. A passenger-list or emigrant-list hit is a candidate, so route identity questions to [evidence/proof judgment](evidence-proof-judgment.md). Record locators with [source citation](source-citation.md).

## Avoid the usual errors

Treat an empty online search for a koseki as inconclusive [S25 @2026-11-22]. Computerized koseki remain subject to municipal certificate eligibility rules [S26 @2026-11-22]. Recover the registered name and honseki, then check the municipal request route in steps 3 and 4.

- **Searching on a romanized name.** One spoken reading can be written with many kanji combinations, so a romanized name does not identify the person. The request needs the exact registered Japanese spelling, kanji or kana as recorded ([Kagoshima City naming FAQ](https://www.city.kagoshima.lg.jp/faq-kurashi/shimin/q113.html)). Retain the romanized reading for index searches and confirm the written form in a record [S1 @2026-11-19], [S2 @2026-11-19], [S3 @2026-11-19].
- **Identify the registered domicile before choosing an office.** Sekiguchi traced one family's honseki to the Tokyo area despite a remembered origin in western Japan [S1 @2026-11-19], [S2 @2026-11-19]. The proposed western visit never established a search result. Kagoshima says it will not confirm a honseki or its lot number by telephone [S4 @2026-11-19]. For requests by mail or proxy, identify the municipality of the honseki. Since 1 March 2024 an eligible person attending in person can obtain eligible computerized certificates at a nearer municipal office under wide-area issuance [S22 @2026-11-19]. Check the certificate type and the eligibility rules in step 4.
- **Check residence independently.** A honseki can use a valid lot address with no connection to where the family lived. A stadium is one documented choice [S1 @2026-11-19], [S6 @2026-11-19]. Treat an older honseki as a place to investigate and verify residence with a dated address or household record.
- **Treating a "no record" reply as proof that no register existed.** The reply may come from the wrong office or a merged municipality. The register may also have been discarded or destroyed (see step 5). [S1 @2026-11-19]

## 1. Get the exact kanji from emigration records

For Japanese emigrants to Brazil, search the São Paulo Japanese immigration museum's passenger database by romanized surname, ship, prefecture or period [S23]. In Sekiguchi's demonstration, the family entry supplied the kanji spelling, ship, departure and arrival dates, and relatives who travelled together [S2]. Preserve the travelling group and dates so that you can distinguish people with the same reading in the next index.

If the passenger-list search for a deceased emigrant yields no match under the surname used in Brazil, rerun it with the earlier Japanese surname documented in a public historical record, such as a passport [S27], [S28]. Record each surname with its source.

Record the kanji exactly as shown, together with the database, the search terms and the returned entry. A kanji form taken from one index entry is still a reading to confirm against the passport or emigrant record or the koseki.

When a name is written in traditional Japanese order, read the family name first and keep the full given name in one field. Leave the middle-name field blank for this form. [S20] For a romanized entry, confirm which part is the family name before filling the fields, because either order can occur. [S21]

## 2. Get the full honseki from passport and emigrant records

A prefecture alone is not enough. You need the complete address, including the house or lot number. [S1], [S2]

- Prewar emigrant passport-issuance records are held at the Diplomatic Archives of the Ministry of Foreign Affairs in Tokyo ([S7 @2026-11-19]). The presenter describes entries that give the passport number, the name in kanji, the place of origin and address, age and birth date. Not all of them are digitized. For undigitized volumes you have to read entry by entry around the departure date. [S2 @2026-11-19]
- The National Diet Library's guide lists the emigration-company series 『伯剌西爾行移民名簿』 for 1908–1963 and identifies the part available digitally [S7 @2026-11-19]. Search the registered characters within that series. In the demonstration, one return identified a farmer from Wakayama and included his birth date, passport number and issue date [S2 @2026-11-19]. Cite the emigrant-list entry, then use those details to locate the separate passport-issuance record at the Diplomatic Archives if you still need the full address [S7 @2026-11-19].

Record the entry's locator and the domicile exactly as written, before any normalization.

## 3. Trace the historical domicile to today's office

Transcribe the historical prefecture, county and village before looking up the present municipality. Sekiguchi followed an address in Ōshima village, Higashimuro County, Wakayama [S2]. Kushimoto's municipal chronology records that it incorporated Ōshima in 1958 and that the present town emerged from the 2005 Kushimoto–Koza merger [S24]. Retain the old address for identifying the register and the successor name for locating the responsible office.

**Privacy gate:** <!-- privacy-gate: request --> A koseki request sends the requester's identity and proof of descent to a municipal office for a register that may name living relatives, so answer the privacy gate in `SKILL.md` first.

Record the historical name and the current municipality side by side, with each step in the merger chain and where you found it. Send the request to the current successor's office, not the one nearest a remembered hometown. Confirm the merger with the municipality if the chain is unclear.

## 4. Check eligibility before requesting

- Under Family Register Act Art. 10, a register can be requested by the persons recorded in it, their spouses, and their direct ascendants and descendants ([Art. 10 text](https://ja.wikibooks.org/wiki/%E6%88%B8%E7%B1%8D%E6%B3%95%E7%AC%AC10%E6%9D%A1)). A spouse has no entitlement, simply as a spouse, to the partner's ancestors' registers. The descendant has to request those. Art. 10-2 separately allows third parties who have a legitimate purpose, such as exercising rights or inheritance. [S1]
- Requests go up the direct line: yourself, then parents, grandparents and further back. Collateral relatives' registers (aunts, uncles, nieces, nephews, cousins) are not available as of right. [S1]
- A proxy can request on the descendant's behalf with a letter of authorization (委任状) signed by the requester. The proxy presents the request form, the 委任状 and the proxy's own ID ([Edogawa City FAQ](https://www.city.edogawa.tokyo.jp/e031/qa/kurashi/todokede/kosekishomei08.html)). The presenter asks his clients for a notarized power of attorney. That is his own practice, not a general legal requirement. [S1]
- Prove direct descent with ID plus birth and death certificates and immigration records that link you to the ancestor. If you hold your own koseki, ID plus that koseki is enough to start, because it names your parents. [S1], [S2]
- Direct-line eligibility also applies to **foreign-national descendants**. If Japanese registers do not establish the chain, assemble the civil certificates linking every generation to the ancestor, with Japanese translations of the foreign-language documents. Gobo City's overseas-request instructions explicitly require descent certificates and Japanese translations for foreign descendants; confirm the required chain, ID and translation details with the honseki municipality. Foreign nationality does not by itself remove eligibility, and it does not make an incomplete descent chain sufficient. [S16], [S17]
- **Privacy gate:** <!-- privacy-gate: request --> Each koseki or closed-register request sends ID and descent proof and returns registers that may name the requester, parents and other living relatives, so answer the privacy gate in `SKILL.md` before each request.
- Each koseki is organized by family unit and names the parents. Request one generation at a time until no earlier register survives. Genealogy requests of this kind are common, and they can take weeks ([Fukuoka City](https://www.city.fukuoka.lg.jp/shimin/kusei/life/koseki_kouikikoufu.html)). [S2]
- **Wide-area issuance (広域交付).** Since 1 March 2024, an eligible requester can get koseki and closed-register (除籍) certificates at any municipal office in Japan. Some koseki and closed registers that have not been computerized are excluded, so request those from the honseki municipality. The requester must appear in person, requests by post or by a proxy are not allowed, and it covers only the requester, the spouse and direct-line relatives ([MOJ](https://www.moj.go.jp/MINJI/minji04_00082.html)). Fukuoka City's list of certificates under this route also includes pre-revision registers (改製原戸籍) ([Fukuoka City](https://www.city.fukuoka.lg.jp/shimin/kusei/life/koseki_kouikikoufu.html)). Most overseas descendants cannot appear in person, so for them this route does not help.
  - This route supplies **full-register certificates** (謄本／全部事項証明), not individual extracts (抄本／個人事項証明), partial certificates or the address-history attachment (戸籍の附票). Request those excluded products from the honseki municipality. [S18]
  - If the descent chain depends on foreign civil documents rather than linked Japanese registers, confirm with the office whether it can process the proposed request under wide-area issuance. Do not assume ordinary direct-descendant eligibility guarantees that particular issuance route.

## 5. Allow for registers that were discarded or lost

The earliest ordinarily issuable register **format** is the Meiji 19 (1886) format, if it survives. The Meiji 5 (1872) registers, also called 壬申戸籍 (Jinshin koseki), are not an earlier request route: a Ministry of Justice directive of 29 March 1968 required the retained material to be sealed against inspection, and certificates cannot be issued from it. A person born before 1886 can still appear in a later register; the format date is not a birth-year cutoff. [S19]

The retention period for closed registers was extended from 80 to 150 years by an ordinance amendment that took effect on 1 June 2010 ([commentary](https://www.mc-law.jp/kigyohomu/17566)). Registers whose former 80-year retention period had expired before that date may already have been lawfully discarded; the extension did not restore them. Disasters and wars destroyed others. [S1], [S12] If a register cannot be found, record it as missing with the cause unconfirmed. Record discard or destruction only when the office's reply or other specific evidence says so. A missing register does not show that the family was never registered there. The presenter advises requesting soon. [S1]

## 6. Hand off land and temple leads

These are follow-on leads, not substitutes for the koseki.

- **Old land ledgers (旧土地台帳, Legal Affairs Bureau).** The presenter says these list the assets for an address and the people tied to it, along with land size and tax in old units. He describes the people as household heads. Treat them as owners (所有者), because that is what the ledger records. He also says ledger copies are free and that anyone may request them, with no descent requirement. Confirm ledger access and cost with the bureau that covers the area; some municipalities hold copies under different rules. Keep the historical lot address separate from a modern honseki, and check their relationship before linking them. [S1]
- **Map certificates are a separate product.** The indexed [MOJ fee table](https://www.moj.go.jp/MINJI/TESURYO/index.html) calls this 地図等情報: from 1 April 2025, 500 yen by written application, 470 yen online with postal delivery and 440 yen online with counter collection. Only indexed text was checked; direct retrieval returned HTTP 403, so the full table was not read [S13]. These are map-information certificate fees, not a charge for the old land ledger. Confirm the applicable map, parcel unit and current fee with the bureau.
- **Family temple (bodaiji) and its death register (kakochō).** In the Edo period everyone had to be affiliated with a Buddhist temple (the terauke system), which was tied to the ban on Christianity ([Kotobank](https://kotobank.jp/word/%E6%AA%80%E5%AE%B6%E5%88%B6%E5%BA%A6-1363649)). Use the oldest honseki to identify the family's affiliated temple, then ask about its death register and graves. The presenter warns that entries may give only a Buddhist posthumous name that differs from the koseki name. Temples may also refuse to show records to people who have no existing connection. [S1]
- **Local history journals.** Look in local libraries and history museums. Many are not digitized, so contact them directly. [S1]

## Return a koseki request packet

Return the following:

- The exact registered name (kanji or kana as recorded), with the source entry and locator.
- The historical honseki as written, the merger chain, and the current municipality and office.
- Proof of the direct-descent line and the requester's role: descendant in person (wide-area issuance possible), descendant by post, or proxy with a signed 委任状.
- Retention and loss notes.
- Land, map, temple and local-history leads, each marked as a lead.

If a step was not completed, name it as a gap. Do not fill it with a guessed office or address. This recipe does not cover postal request forms or fee payment from abroad, so confirm those with the target office.
