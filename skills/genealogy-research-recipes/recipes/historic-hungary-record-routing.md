---
id: "historic-hungary-record-routing"
title: "Route a record from historic Hungary by county, successor state and record type"
summary: "Route a birth, marriage, death, census or tax entry from the pre-1920 Kingdom of Hungary by county, successor state and record type."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "none"
gates: []
guardrails: [{"id": "HISTORIC-HUNGARY-RECORD-ROUTING-01", "text": "**Start with the archive of the state the village lies in today for local registers.** The MNL in Budapest holds them for today's Hungary, not for the whole kingdom."}]
handoff: ["archival-image-coverage-verification", "austrian-confessional-register-routing", "catholic-parish-diocesan-record-recovery", "evidence-proof-judgment", "familysearch-practical-record-workflows", "galicia-bukovina-habsburg-record-routing", "historical-place-name-resolution", "illegitimacy-record-recovery", "jewishgen-search-family-reconstruction", "tax-roll-observation-workflow"]
checked: "2026-11-04"
checked_basis: "opened 2026-11-04"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"tier": "pointer", "group": "Central and Eastern Europe by period state", "order": 1040}
---

# Route a record from historic Hungary by county, successor state and record type

Use this recipe before you search for a birth, marriage, death, census or tax entry from the pre-1920 Kingdom of Hungary: today's Hungary, Slovakia, Transylvania and the rest of western Romania, Vojvodina, Croatia, Prekmurje, Burgenland and Transcarpathia. It sends each event to the record type and holder of its own date and place. It prevents seven failures:

- assuming every village in today's Croatia has, or lacks, 1895 state civil registers without checking its 1895 county
- skipping Međimurje's and Prekmurje's Hungarian civil registers because the villages are in Croatia or Slovenia today
- carrying Austria's 1938–1939 civil-registration dates into Burgenland
- sending every search to the National Archives of Hungary (MNL) in Budapest
- swapping a Hungarian surname and given name
- reading an 18th- or 19th-century conscription as a full household list, and an absence from it as evidence
- calling an early Jewish event missing before checking when that community's register starts

Link out for the shared steps:

- **A village you cannot place, or one with several names:** [historical place-name resolution](historical-place-name-resolution.md).
- **A Catholic register's diocesan copies and each holder's span, with the Kalocsa locality list as a worked example:** [Catholic parish and diocesan record recovery](catholic-parish-diocesan-record-recovery.md), "Each holder's span, by record type".
- **A diocesan list of paternity suits (the Kalocsa impraegnatio rows):** [illegitimacy record recovery](illegitimacy-record-recovery.md).
- **A Habsburg Galician or Bukovinian event, or Austro-Hungarian army papers for those men:** [Galicia and Bukovina record routing](galicia-bukovina-habsburg-record-routing.md).
- **JewishGen's Hungarian databases and their phonetic options:** [JewishGen search and family reconstruction](jewishgen-search-family-reconstruction.md).
- **A tax list read as an annual series:** [tax-roll observation workflow](tax-roll-observation-workflow.md).
- **Browsing an unindexed FamilySearch image group, or a failed name search:** [FamilySearch practical workflows](familysearch-practical-record-workflows.md), workflows 2 and 3.
- **Frame versus leaf and the inspection ledger:** [archival image coverage verification](archival-image-coverage-verification.md).
- **Identity rulings and negative evidence:** [evidence/proof judgment](evidence-proof-judgment.md).

## Inputs to gather first

Gather these before searching:

- the event type and approximate year
- the village under every name form seen (Hungarian, German, Latin, Slovak, Romanian, Croatian, Serbian or other local form), each with the record it came from
- the county (vármegye) and district as any record gives them, with that record's date
- the confession: Roman or Greek Catholic, Reformed, Lutheran, Orthodox or Jewish
- the person's name exactly as each record writes it, in its order
- any FamilySearch collection, image group or archive reference already seen

## 1. Place the village in its 1895 county and today's successor state

- **Do not route by the word "Hungary".** A pre-1920 record that says "Hungary" can point to any of the successor states. Look the village up in a period Hungarian gazetteer, using the place-name recipe for the lookup. Record four things: the historical county (vármegye), the district, the successor state and the modern name.
- **Keep every name form as its own search lane.** The same village has a Hungarian name, often a German one, and a local-language name. Search each holder under all of them. Fix ambiguous names with the place-name recipe before you choose a holder.
- **Fix the county on 1 October 1895 before you choose civil or church books.** That date decides which series exists (step 2).

## 2. Choose civil or church books by date and territory

- **From 1 October 1895, expect state civil registers (állami anyakönyv).** Act XXXIII of 1894 made state registration general, and it began on 1 October 1895 [S1]. Before that date, the church registers are the vital records.
- **Do search Hungarian civil registers for Međimurje and Prekmurje, 1895–1918.** Međimurje lay in Zala county; Prekmurje was divided between Vas and Zala counties [S2], [S18]. FamilySearch "Slovenia, Prekmurje and Međimurje, Civil Registers, 1895–1918" (collection 1985107) holds them, filmed from the Maribor Regional Archive [S2].
- **For any other village in today's Croatia, check its 1895 county first.** Take the post-1895 series for Croatia-Slavonia from the Croatian archive guide, and search the parish books for every post-1895 event as well.
- **Do not carry Austria's dates into Burgenland.** In Austria, civil marriage registers start on 1 August 1938 and civil birth and death registers on 1 January 1939 [S3]. Those are Austrian cutoffs. A Burgenland event from before the region passed to Austria happened in Hungary: route it by its 1895 county, as in step 1, to the church books before 1 October 1895 and the state civil registers from that date.

**In Burgenland, expect state civil registers after 1921 as well.** When the region passed to Austria, Hungary's obligatory civil marriage and the state register system tied to it stayed in force there as special federal law, and the marriage law of 1938 took the state registrars over as registry officials [S19]. So do not stop a Burgenland search for a state register at 1921: the series runs on to the Austrian cutover described above.

## 3. Take custody from the successor state, not from Budapest

**Inside today's Hungary, three holders share the registers.** Before 1895 the churches, more exactly the parishes, kept them; the national archive in Budapest borrowed those pre-1895 books and filmed them between 1960 and 1970 [S20 @2026-11-13]. Act XXIII of 1827 ordered church registers kept in two copies, the second going to the county or free royal town archive; state registers were also kept in two copies from 1895 to 1980, and the archives keep the second copies [S21 @2026-11-13]. So read "the MNL in Budapest" in the first rule below as the films of the pre-1895 church books, and look in the county archive for a second copy.

- **Start with the archive of the state the village lies in today for local registers.** The MNL in Budapest holds them for today's Hungary, not for the whole kingdom.
- **Search the 1828 national conscription in MNL series N 26, wherever the village lies today.** It covers the whole kingdom, Croatia, Slavonia and the Littoral included, but not Transylvania [S17].
- **Slovakia (Upper Hungary):** reach the church books through FamilySearch first. "Slovakia, Church and Synagogue Books, 1592–1935" (collection 1554443) holds christening, marriage and burial images, and the originals are in the Slovak state archives [S13]. The ministry's list names the Slovak National Archives and the regional state archives in Banská Bystrica, Bratislava, Košice, Nitra, Prešov, Trenčín, Trnava and Žilina (seat in Bytča) [S14]. Map each image group back to the regional archive that holds the original. The same 1 October 1895 civil registration applies there [S1], [S15].
- **Use Slovakiana for the 1930 Czechoslovak census sheets.** All 1930 sheets have been online on the Slovakiana cultural-heritage portal since November 2022 [S16].
- **Romania (Transylvania, Banat, Crișana, Maramureș):** civil-status registers pass to the county service of the Arhivele Naționale (National Archives) 100 years after they were created [S4]. Ask the county service for an older register. A younger one is still with the civil-status service.
- **Treat a FamilySearch film as a copy of the successor-state holding.** Record which archive the collection page names as the source of the originals.
- **For Croatia, Vojvodina, Transcarpathia and Burgenland, take the holder from the successor state's own archive guide.** Mark the route unconfirmed in the series row until that guide names the holder.

**For a village now outside Hungary, also check the Hungarian archive of its 1895 county.** The Sopron archive lists, for Sopron county and the city of Sopron, second copies of the state registers of 1895–1921 from the places annexed to Austria in 1921 [S22 @2026-11-13]. Look for the same kind of holding in another border county's archive before you mark a route unconfirmed.

## 4. Search both name orders and every language form of the given name

- **Expect the surname first in a Hungarian-language entry:** Nagy János, not János Nagy [S5], [S6].
- **Expect the given name translated into Latin or German in many records** [S5]. Search Joannes, Johann and János as separate lanes for the same man.
- **Search every person in a Latin or German entry under both name orders.** Keep the literal order as written in the name register, and never index a surname as a given name.
- **Expect Latin as the register language in many parishes until the 1840s.** Act VI of 1840 ordered parish registers to be written in Hungarian within three years, even where sermons were not preached in Hungarian [S8]. Act II of 1844 made Hungarian the official language of the Diet, the government and the courts in place of Latin [S7]. Read each register's language from the register itself.

## 5. Read tax conscriptions as taxpaying heads and the 1784–87 census as a count

- **Read the 1828 national conscription as taxpaying heads of families only.** Its recorded units are the heads of taxpaying families, and the nobles are not included [S10], [S11], [S17].
- **Read any other tax-based conscription by its own instructions for who was counted.** Do not rely on the list until you have read them.
- **Expect nobles in the 1784–87 Josephine census, but not named women.** It counted the whole population, nobles and clergy included; women were recorded only as numbers [S9]. Its main enumeration ran in 1784–85, with revisions to 1787 [S9].
- **Record each tax-conscription entry as a taxpaying head present at a place and date.** Do not reconstruct a household from a conscription line. Treat absence from a tax-based list as uninformative: the person may have been noble, untaxed, a dependant or a servant. For reading a run of tax lists, use the tax-roll recipe.

## 6. Use the context portals as finding aids

- **MNL AdatbázisokOnline:** the National Archives of Hungary's portal of thematic databases, many of them built around named persons [S12].
- **Treat each hit as a lead.** An OCR line or a database row is not the record. Open the item, and cite the contributing archive and the item, not only the portal.

## 7. Check where a Jewish register starts before calling an event missing

- **Find the start year of the community's own register before you call an earlier event missing.** Record a year before that start as a coverage gap, not as a negative search.
- **From 1 October 1895, search the state civil registers too** (step 2) [S1].

## Close with a routing packet

Return:

- **Jurisdiction row:** the village under each name form, its 1895 county and district, its successor state and modern name, and the gazetteer entry used.
- **Series rows:** for each event, the series (church register, state civil register, Jewish register, conscription or census), the holder, the locator, and the status: searched, found, not found or not online.
- **Image-group rows:** the FamilySearch collection and image group, the archive it names as the source, and the frames inspected.
- **Gaps:** years before a community's register starts, conscription absences, and routes still marked unconfirmed.
- **Name register:** every literal form in its written order, with its record and language, and every lane searched, with where.

The model assembles this packet. The researcher decides identity and kinship.
