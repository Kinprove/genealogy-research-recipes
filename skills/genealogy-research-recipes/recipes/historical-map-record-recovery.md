---
id: "historical-map-record-recovery"
title: "Recover and read historical maps as dated, copy-specific evidence"
summary: "Read a historical map, atlas, plat or fire-insurance sheet as dated evidence, and trace a detached archival map to its case."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "HISTORICAL-MAP-RECORD-RECOVERY-01", "text": "retain the map-to-case link as a candidate until the records establish it. Keep the estimated map-production date, the case-file span and any dated event statements separate. Seek the case's actual statements before dating the depicted event or moving a same-named person to another generation."}]
handoff: ["french-departmental-record-routing", "galicia-bukovina-habsburg-record-routing", "german-register-image-recovery", "historical-place-name-resolution"]
checked: "2026-11-02"
checked_basis: "opened 2026-11-02"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": [], "contact": ["contact"]}
router: {"section": "Record websites, libraries and maps", "group": "Places and maps", "order": 66}
---

# Recover and read historical maps as dated, copy-specific evidence

Use this recipe when you are about to use a Sanborn fire-insurance sheet, a landowner atlas or plat, a topographic quadrangle, a directory or ward map, or a georeferenced overlay to place a person, building, address, cemetery or parcel. Each map records what one producer observed in one edition, and a given copy may carry its own corrections. Read it that way, and take people's names from other dated records. Use [city-directory observation](city-directory-observation-workflow.md) for the directory series. Use [land-index recovery](land-index-book-series-recovery.md) for the deeds behind a mapped holder, and the [burial evidence packet](burial-evidence-packet.md) once you find a cemetery. Use [evidence/proof judgment](evidence-proof-judgment.md) for any identity, kinship or ownership conclusion, and [AI for documentary records](ai-for-documentary-records.md) when an AI suggests readings of handwriting.

## Contents

- Errors to refuse
- Find the map and confirm what it covers
- Read a Sanborn volume, not a loose sheet
- Link a person to a building only through dated records
- Place a recorded historical address
- Trace a post office and its mail routes
- Test a mapped migration route
- Find a vanished cemetery, church or settlement
- Read landowner maps and overlays with limits
- Return a map packet

## Errors to refuse

- A Sanborn sheet does not name the people who lived in a building, and it almost never names the owner. Businesses are usually labelled only by type, such as "auto top works" or "mattress factory". A firm's name was added only for a large concern when there was room on the sheet [S1], [S2], [S3], [S4], [S5]. Get names from directories, land records, newspapers and censuses.
- Do not date a building to the base year of a corrected volume.
- None of these means a place was unmapped or did not exist: missing from one holder's list, uncoloured on a key map, missing from one edition, or missing from a gazetteer.
- Do not use a colour or symbol key from another volume or a generic online key without checking it against the key in the volume itself.
- An overlay outline is not a modern parcel, footprint or address.
- A modern street with the same name is not the historical street. Living near someone does not make them kin.
- Absence from a landowner map does not prove the family did not live there or owned no land.

## Find the map and confirm what it covers

1. Search every holder before you call a place unmapped. The Library of Congress does not have every Sanborn edition online. Some sheets are still under copyright, and some volumes are not digitized or not held [S1]. Also check university, state and public-library sets. Examples are the University of Utah Marriott Library's Utah Sanborn site (the Utah Sanborn maps it holds, with georeferenced sheets you can download for Google Earth) and BYU's ProQuest access [S1], [S5], [S9]. The LoC city table lists each volume's date and sheet count, plus any other places included [S10]. When you are looking for a small place next to a large city, always check the city's volumes as well. Sanborn put sheets for outlying places into city volumes, such as Manchester and South Richmond in a Richmond volume [S10].
2. Search by area as well as by name. OldMapsOnline lists the historic maps that fall inside a rectangle you draw, and the list updates as you pan or zoom [S25]. The USGS Historical Topographic Map Collection viewer shows a timeline of every digitized map for the area. Tanner cited about 178,000 maps in 2016 [S25].
3. A keyword hit is a hit on catalogue information. On David Rumsey, a keyword finds any term in a map's metadata [S7]. So check that the map image actually shows the target place before you count it as coverage. Start with a broad search without exact-phrase quotes, then narrow it [S7].
4. Land-ownership maps are rarely indexed, so expect to browse. Narrow the search with the census township name or the land description [S11]. Not every county had an atlas published [S11]. Record which sites, holders and editions you checked. A site you did not check is a gap, not a negative result.

When an archival map has been detached into a map collection, search relevant finding aids
for a possible originating dispute or court case, using the supported places, parties and
subject. Copy the map and file references and the evidence joining them. For a border dispute, compare place-names, opposing parties and witness statements [S31]; retain the map-to-case link as a candidate until the records establish it.
Keep the estimated map-production date, the case-file span and any dated event statements
separate. Seek the case's actual statements before dating the depicted event or moving a
same-named person to another generation. [S31]

**Google Earth Pro:** For a known historical locality, look for the Rumsey Historical Maps layer under Gallery and check it for maps of the area. The layer is a selection from the David Rumsey collection. If it is unavailable or yields no map for the locality, search the full collection and other holders. [S69 @2026-11-18], [S70 @2026-11-18]

**U.S. county boundaries.** Select the state in the Newberry Library's Atlas of Historical County Boundaries and open its interactive map [S80 @2026-06-08], [S81 @2026-06-08]. Choose the last boundary-change date on or before the event date. Identify the county that contained the locality then and record the effective date and boundary-change citation before choosing which county's records to search [S81 @2026-06-08], [S95 @2026-06-08]. Use the county chronology or dated PDF maps if the viewer is unavailable [S95 @2026-06-08]. For local map work, download the state files or the U.S. dataset. Choose KMZ for Google Earth Pro or the GIS shapefiles for date-filtered GIS work [S80 @2026-06-08], [S82 @2026-06-08].

**Polish border changes.** In OldMapsOnline, search for the locality or pan to it. Open a map close to the event date and record the administrative division shown and the sheet date [S85 @2026-06-08], [S86 @2026-06-08]. The site's “Galicia” landing page leads to Spain, so use the settlement's location to find maps of Habsburg Galicia [S87 @2026-06-08]. Use the historical division to identify candidate archive inventories across today's borders. For Galician parish registers, check the inventories in Warsaw's AGAD and Lviv's TsDIAL by parish, confession and year [S88 @2026-06-08], [S89 @2026-06-08]. See [Galician and Bukovinian record routing](galicia-bukovina-habsburg-record-routing.md) for the record series and holders.

**European locality searches.** Search for the settlement in Arcanum Maps and check city plans, country maps and thematic maps for the date and area you need [S90 @2026-06-08], [S91 @2026-06-08]. Look for the name on the historical sheet itself. A search marker can appear even if the settlement did not exist when the map was made [S91 @2026-06-08].

**Kanawha Valley waterways.** Trace each named waterway to its junction with the main river or another tributary. Compare the detailed sheet with the water-route inset on John S. Swann's 1867 *Title Map of the Coal Field of the Great Kanawha Valley*. Search the Library of Congress under that title or use David Rumsey map 4965.001 [S92], [S93], [S94]. If the sheet ends before the junction, check an adjoining map from the period before ruling out the connection.

**Overlapping claims.** Read disputed outlines on colonial Pennsylvania maps as the mapmaker's representation of a claim. Check the boundary at the date of the record and search the record series created by each claimant. For a tract in Pennsylvania's Westmoreland County that Virginia also claimed, check Pennsylvania's warrant registers and the Pennsylvania Land Office's *Virginia Entries*, series 17.209. Settlers sometimes warranted the same tract in both jurisdictions [S96], [S97].

**Privacy gate:** <!-- privacy-gate: contact --> The user's approved name, reply address and map question go to the Library of Congress Geography and Map Division. Remove family names, private addresses and attachments from the question.

If the catalogue leaves a sheet or edition unresolved, send a map-location question through **Ask a Librarian: Maps, Geography**. Give the locality, period, map series and editions checked, and ask for the missing sheet or call number [S98 @2026-11-21], [S99 @2026-11-21].

## Read a Sanborn volume, not a loose sheet

1. Use the street index and graphic index to find the detail sheet. Read the adjoining-sheet numbers in its margins to continue across the edge. For an uncoloured block, check other volumes of the same edition and record the bounds of the surveyed area before reporting a gap [S3], [S77].
2. For a corrected copy, read the base date and the latest correction date from the volume or its catalogue record. Look for the correction record on the title page [S6], [S77]. In a Richmond volume dated 1924 through April 1950, that range identifies the base and last update; it does not date an individual paste-over [S10], [S77]. Cite the holder, volume, both dates and sheet.
3. Read the legend in this edition, often at the front, back or on the first sheet. Check the marks for construction, height, openings and use: commonly yellow denotes wood frame, pink brick and blue stone, and a large X can mark a stable [S1], [S3], [S7], [S77]. If only another edition’s or an online legend is available, identify it and mark the interpretation provisional [S2], [S4].
4. Open the individual sheet and its neighbour where a mosaic overlaps: in the Spanish Fork mosaic, the upper sheet’s border hid shops visible on the underlying sheet [S1].
5. Compare the same lot across dated editions, recording each structure that appears or disappears. Trace ownership independently through a dated plat and the underlying land records [S9].

**Mixed use.** Check use abbreviations on each part of the building and record any floors the sheet assigns to a use. A shop label can coexist with dwelling space. Use colour for the material indicated by the edition's key and check the use labels separately [S98], [S100].

## Link a person to a building only through dated records

Match a dated advertisement or directory entry to the building’s occupancy label and nearby landmarks. Search the whole edition for competing matches: Spanish Fork had two banks, so an advertisement locating a firm near a bank needed the bank’s name or another landmark [S1], [S2]. Compare the editions nearest the advertisement, especially when the firm may have moved. Record the printed address, the independent clues and any later renumbering before linking a person to the building.

When following a household across addresses, plot each residence on the Sanborn edition closest to its record date. Compare nearby factories, businesses or rail lines with the recorded occupation. Use those features to identify possible employers and verify a match or a reason for moving in dated records about the household [S98].

## Place a recorded historical address

1. Transcribe the dated address, list uncertain readings and test each against a period plan and records of institutions at the address. If AI suggested a reading, verify the handwriting, historical address, landmark and modern location independently [S22]. Test a slash as a possible corner-house number by reading numbers along both streets. For a 1928 Sverdlovsk envelope addressed to 218/25, the 1910 plan put 220 on the corner, but a participant read the 1931 plan as showing 27 across the junction, supporting 25 as a cross-street number [S26]. Record the interpretation as provisional until a contemporary record confirms it.
2. Compare editions on either side of the record date [S15], [S20]. A house absent from a 1905 sheet appeared at the later census address in the Halls’ case [S17]. Test historical-to-modern numbering against dated plans, a renumbering or land record, and the number visible on the building. For Berlin-Weißensee no. 131, a local society proposed modern no. 166, but the house a researcher picked out in Street View bore 165 [S27]. Record the proposed equivalence and its source; a war-damage map may help explain a gap.
3. Connect a lost street to the present through dated evidence:
   - Use the census ward to choose the period ward map. Follow the historical street through a dated renaming list for that city [S21].
   - When the same street name occurs in several districts, check any postal code on the address against a period postal-district map before following a renaming. Even a documented street rename leaves house-number continuity open: Berlin’s former Auguststraße in Zehlendorf became Claszeile, but the researcher could not match old no. 1 to a present number [S27]. Record both street names, the change date and the source of the district identification.
   - Align the directory’s bound-in map on surviving landmarks; a modern highway may have replaced the street you are trying to trace [S18].
   - period maps plus city directories [S16].
4. Plot residences on a dated map. Label the observation year and any estimated placement. A cluster suggests where to search for documented ties among the households [S19].
5. Use the placement to choose a record search. For Chicago, compare a dated church map with the parish’s language community and surviving registers [S12], [S79]. To investigate an associate, plot the work address on a dated record such as a First World War draft registration card alongside the known residence [S21].

**Electoral address dates:** For a historical British address, read the register's qualifying date as well as the date it came into force. Date its residence statement to the qualifying date, as The London Archives guide explains, and for London and Middlesex registers use the guide's name/address search route. Copy the qualifying date into the address worksheet before comparing street numbers. These lists contain eligible electors rather than every resident, so an absent name does not show that the building was empty or the whole household lived elsewhere. [S63 @2026-11-17], [S64 @2026-11-17]

**Conflicting census addresses.** Plot both addresses on the plans nearest their respective census years. Compare the lots and cross streets, and check a dated conversion table for a street rename or house renumbering before recording a move. In Chicago, start with the 1909 conversion guide outside the Loop and the separate 1911 guide in the Loop [S101], [S102].

## Trace a post office and its mail routes

**Find the route map.** Start with the state's list in National Archives *Special List 29*, then check the Topographer's series in Record Group 28, section 28.6.2. Use Preliminary Inventory 168 entries 189 and 190 for printed post-route maps and entry 191 for manuscript maps. Carry over the full filing reference. For example, Special List 29, New Jersey entry 565, gives the filing reference *RG 28: State Maps, New Jersey, 1915* and an operating date of 1 April 1915 [S103 @2026-11-21], [S104 @2026-11-21], [S105 @2026-11-21], [S122 @2026-11-21], [S106 @2026-11-21].

**Date the postal evidence.** Identify the producer and record the date the sheet says its routes were in operation. The Post Office Department bought maps before it appointed its first Topographer in 1837. The public state and multistate map series ordered in 1862 was updated over time, so compare editions around the event [S103], [S105], [S107].

**Place the post office.** Find the digitized rolls of microfilm M1126 in National Archives Catalog series 608210. Browse by state or territory, then county, parish or district, then office name. Check a former name or jurisdiction when the first search misses. Enlarge each dated report and look for the township, range and section where applicable, the mail-route number and distance to the route, and named waterways, roads or railroads. Plot the written distances and landmarks when the sketch is missing. Check whether the report concerns a proposed office, a move or a name change before marking its location [S103 @2026-11-21], [S107 @2026-11-21].

## Test a mapped migration route

**Railroad routes:** Read the map's date and purpose before tracing a corridor. The Library of Congress collection described by TeachingHistory includes surveys, company-report maps and public route guides; distinguish a proposed or surveyed line from an operating route. Use a dated operating-route map to test travel between documented places, keeping the line's operating status separate from evidence of the family's actual journey. [S65], [S66]

**California Gold Rush.** Start from the last documented residence before the journey and the earliest documented arrival. Compare an overland route, a crossing via Panama and a voyage around Cape Horn. Use Ensigns & Thayer's 1849 *Map of the gold region[s] of California* to identify suggested routes, then test the alternatives against dated waypoints. Search for named wagon-company records on a land route or ship manifests at the relevant ports on a sea route. For Panama, check each sea leg. For a coastal voyage, search departure-port coastal manifests as well as arrival records [S98], [S108], [S109], [S110].

When documented waypoints imply a detour, compare the direct line and the candidate route on a topographic map. Locate passes, river crossings and alternate tracks, then date the segment that could explain the detour. On the California Trail's Truckee Route, Roller Pass was one of several climbs out of the same basin [S98], [S111].

**Appalachian atlas.** Search for Carrie Eldridge's *An Atlas of Appalachian Trails to the Ohio River*. For a Blue Ridge crossing, start with figure 9, *Virginia’s Blue Ridge Gaps*, and confirm the trail through the gap on a dated route map. For settlement into Kentucky, use figure 10, *Kentucky Settlement Area*. In the contents, look under *The Carolina Road (Upper Road-Rogues Road)* for the names Eldridge groups there, then compare the dated segments before treating labels as interchangeable [S112], [S113], [S114].

When a river route crosses the fall line, locate the falls or rapids for that river. Check period maps or travel accounts for the extent of navigation and any portage before tracing a continuous upstream journey [S112], [S123].

**Trail or wagon road.** Check when a foot or pack trail became usable by wagons at the crossing you need. Compare the military roads in Eldridge's figure 6 with the earlier trails. Braddock's 1755 expedition widened an existing trail for its wagons and artillery, and Forbes's campaign took a separate route to Fort Duquesne in 1758. Use records of the household to decide whether it travelled either road [S112], [S113], [S115], [S116].

**Modern corridor locators.** In Pennsylvania, use U.S. 40 near Fort Necessity to find the Braddock corridor and U.S. 30 near Bedford to find the Forbes corridor. Verify the historical alignment on a route map before carrying a modern highway segment into the itinerary [S112], [S116], [S118].

**Cumberland Gap.** Date the documented crossing separately from the settlement road. Thomas Walker crossed the Gap in 1750, and Daniel Boone blazed the Wilderness Road through it for settlement in 1775. Check earlier trails for a journey before that road was cut [S112], [S117].

**National Road into Ohio.** Date the specific segment before assigning a household to the road. Construction started in Cumberland, Maryland, in 1811, reached Wheeling by 1818, and began in Ohio in 1825. For an earlier itinerary, look for an earlier trail or road serving the documented waypoints [S112], [S118], [S119].

**Great Wagon Road.** Check the Shenandoah Valley segment against a dated map. In Middletown, Virginia, use the Valley Pike, now U.S. 11, to locate the corridor and confirm the historical alignment at the place in question [S112], [S120].

**Great Trail.** Search for *Tuscarawas Path* as well as *Great Trail* when tracing the westbound corridor from the Forks of the Ohio. Verify the junction and route onward to Detroit separately on a dated trail map [S112], [S124].

**Zane's Trace.** For a journey through Ohio to Kentucky, trace the road opened in 1797 from Wheeling to Limestone, now Maysville. Check where the family's documented waypoints join or leave the trace before extending an itinerary to Lexington [S112], [S121].

## Find a vanished cemetery, church or settlement

Start with a known point and compare dated editions, recording the feature and its printed name on each [S25]. Check a cemetery’s listing, map pin and photographed grave coordinates separately. Tanner’s 2016 Joseph City search found a Find a Grave listing whose directions led elsewhere; GPS-tagged BillionGraves photographs helped locate the cemetery [S24]. Record the service, search date and evidence for the position.

For a rural name, search the historical parish or town’s sheet for farms, estates and namesakes. For Courland’s “Krogkalnos”, the Goldingen sheet (K14) yielded the candidate Krogekaln southwest of Goldingen, distinct from the modern Krogkalni farm found near Libau [S29]. Compare the candidate with the settlements grouped in the original register and check adjacent returns. A Perm researcher questioned a mapped Godovalov roughly 20 km from Bolshaya Sosnova because the two names were entered together in the 1748 and 1763 revisions [S30]. Distance can prompt a search for another settlement; identify the family’s place through the records.

For the Russian Empire and the USSR, use these map locators, and link the maps rather than redistributing them:

- Retromap (retromap.ru) is a lead for old-map overlays and city plans. A search-result title lists the Столистовая карта (hundred-sheet map) of the Russian Empire under an 1804 label; the map page could not be read, so that label and its interactive display remain unconfirmed [S38]. The map's compilation in 1801–1804 is separately supported by S39. Record the title and year actually shown when you open a map [S39].
- maps.vlasenko.net holds Soviet military topographic sheets from 1:50,000 to 1:1,000,000, mainly for Ukraine, with partial coverage of Moldova, Belarus and Russia that depends on scale. Record the sheet nomenclature and survey year [S40].
- etomesto.com overlays old maps of Russia and the former USSR on modern maps. Record the map and sheet [S41].

For a settlement in the former USSR that emptied after 1960, look for declassified US reconnaissance satellite frames. USGS EROS holds three sets: Declass 1, from the CORONA, ARGON and LANYARD systems, 1960–1972 [S55 @2026-11-16]; Declass 2, from KH-7 and the KH-9 mapping camera, 1963–1980 [S56 @2026-11-16]; and Declass 3, from the KH-9 Hexagon panoramic cameras, 1971–1984, whose high-resolution frames resolve 2–4 feet [S57 @2026-11-16]. Search and preview them in EarthExplorer (earthexplorer.usgs.gov). A frame that already has a digital copy downloads at no cost; any other frame is scanned to order for $30, and for Declass 3 only the film duplicates held at EROS can be scanned [S55 @2026-11-16], [S56 @2026-11-16], [S57 @2026-11-16]. Record each frame's ID and date.

Preview several dated frames for cloud and blur before ordering. Align clear frames to surviving landmarks, then compare the street and visible plots with a dated or remembered village plan. In Karpovka, comparing 1972 and 1984 imagery helped place former houses whose dismantled logs had left no visible ruins [S58], [S59]. If you divide the street into roughly equal lots to align a sketch, label the assumed widths and seek boundaries or house positions visible on another frame [S58].

When a Soviet-era birthplace is missing from modern directories, also run the checks in [place-name resolution § 3](historical-place-name-resolution.md#3-date-the-name-before-matching-it).

For other countries, use these historical map services. Link the maps rather than redistributing them, and record the series, the sheet and its edition or survey year, not only the year you set on a slider:

- **Denmark:** Historiske Kort (historiskekort.dk), Klimadatastyrelsen's historical map viewer [S49 @2026-11-13].
- **France:** cartes.gouv.fr shows the Cassini map [S54 @2026-11-13]. It replaced Géoportail (geoportail.gouv.fr), whose pages redirect to cartes.gouv.fr from 30 September 2026 [S53 @2026-11-13]. The Cassini map was made between 1756 and 1815 in 180 sheets. It shows the kingdom's borders of its time, so Nice, Savoy and Corsica are missing [S44 @2026-11-13]. IGN's Remonter le temps (remonterletemps.ign.fr) offers IGN's historical series, among them the état-major map, surveyed from 1818 to 1881 [S45 @2026-11-13].
- **France, Napoleonic cadastre:** the cadastre begun in 1807 is kept by each Archives départementales. Its plans divide a commune into lettered sections and numbered parcels, and the *état de sections* lists each parcel with its owner and *lieu-dit* when the plan was drawn. Take the reference from that archive's finding aid (3 P in the Côtes-d'Armor). Some communes have two series of plans, so match the état de sections to the plan's date before you read an owner [S46 @2026-11-13]. An owner's name is a tax entry, not proof of title. To follow it to a deed, use [French departmental routing, step 8](french-departmental-record-routing.md#8-find-property-transfers-and-notarial-minutes).
- **Germany:** the Messtischblätter (topographic sheets at 1:25,000) are in the SLUB Dresden Virtuelles Kartenforum (kartenforum.slub-dresden.de), georeferenced, with a Messtischblätter filter, a place search and a time slider [S50 @2026-11-13]. SLUB set out to digitise about 6,000 sheets covering the whole Reich (1860–1935) [S51 @2026-11-13]; if the sheet you need does not appear, record it as not found in the Kartenforum, not as absent. To place a village from its railway station on the 1:100,000 Karte des Deutschen Reiches, see [German register image recovery § 3](german-register-image-recovery.md#3-separate-namesakes-with-the-kreis-and-non-parish-records).
- **Netherlands:** Topotijdreis (topotijdreis.nl) shows Kadaster's topographic maps from 1815 to the present [S42 @2026-11-13]; choose the year on the slider [S43 @2026-11-13]. Different zoom levels show different map series, so zoom in to the most detailed one before you read a feature [S43 @2026-11-13]. Each sheet has its own edition years, so record the sheet's edition year, not the slider year [S42 @2026-11-13].
- **Norway:** Kartverket's historical map archive (Historiske kart on kartverket.no) has thousands of scanned maps, among them amtskart and gradteigskart, free to download, with a map-based entry [S48 @2026-11-13].
- **Sweden:** Lantmäteriet's Historiska kartor (historiskakartor.lantmateriet.se) shows maps and survey files from 1628. It shows the survey authorities' material only up to 1875; ask Lantmäteriet for later files [S47 @2026-11-13].

To test an oral report of a farm burial ground, check dated county maps and atlases for a cemetery mark. Private cemeteries of the 1840s and 1870s were drawn on them [S23]. Then work out which county held the site at that date. Lehigh was formed from Northampton in 1812, and Berks lost territory to Schuylkill in 1811 and to Lebanon in 1865. Some churches and burial grounds have moved between these counties [S23]. Treat a plotted symbol as an approximate lead for a site visit [S24].

**Rural school sites:** Search school-property sale and auction notices for the legal description or the distance and direction from named towns. Plot the clues on a dated map and seek the original advertisement or conveyance. Use records naming pupils to establish attendance [S67], [S68].

## Read landowner maps and overlays with limits

Record the map’s title, publisher, purpose, date and holder. Check maps made for other purposes, including battle maps, for printed landholder labels [S14]. Use a labelled property and its neighbours as leads for the deeds or surveys that could identify the holder and date the ownership [S11].

**Maiden-name leads from plats:** Start with the earliest landowner plat that covers the family's documented locality near the period in question. Use the nearby landowners' names to identify families whose daughters could match the woman you are tracing. Keep each surname as a candidate and test the daughter's dates and relationships against records that name her. [S71], [S72]

**Federal first-grantee maps:** Read the introduction and the dates behind each label to distinguish a map reconstructed from federal entries or patents from owners at one publication date. Federal tract books stop at transfer to private ownership; trace later private buyers through county conveyances. Compare the family's arrival and acquisition dates with the grant dates before expecting it on a first-grantee map. [S60], [S61], [S62]

**Old Frederick County tracts:** Copy both the tract identifier and the numbered map reference from Cecil O’Dell’s *Pioneers of Old Frederick County, Virginia*. Locate the tract using its parent patent, named streams and roads [S73], [S74]. Check whether the locator points to a map printed in the book or a loose sheet: the 1995 review lists two loose maps in addition to the printed sections [S75]. For a missing loose map, search separately under its mapmaker and title, such as Galtjo Geertsema’s *Northern Neck of Virginia, Old Frederick County* [S76].

A house number in a Galician metrical record and a building parcel number on a final cadastral map can identify the same building under different numbering systems. The 1849 Jaworów centre sheets carry land and building parcel numbers [S78]. Check the local inventory for an earlier field sketch with house numbers, an intermediate indication sketch with both numbers, or a property register linking parcel, owner and residence [S33]. Verify the entry for the locality and survey year: the Jaworów researcher proposed checking a Lviv index but reported no lookup [S28]. Cite the map and the concordance actually used, with both numbers.

Galicia also has two earlier land surveys whose rolls name householders: the Josephine cadastre (1785–1788) and the Franciscan survey (from 1819–1820), whose records are TsDIAL (Central State Historical Archive of Ukraine in Lviv) fond 19, the Йосифінська метрика (Josephine metrica), and fond 20, the Францисканська метрика (Franciscan metrica) [S32], [S35], [S52]. The fond identities come from the archive catalogue read for S52; the survey dates come from S32. Use those rolls as people-bearing series to separate same-named household heads and to trace a holding divided between heirs. They are not map series: no maps or sketches survive from the Franciscan survey, and few Josephine field sketches were kept [S32]. Field sketches (Feldskizzen) and mapped parcels belong to the later stable cadastre. The earliest Galician stable-cadastre maps in the Gesher Galicia Map Room are based on 1826–1828 surveys [S32], [S33].

To place a vanished hamlet, use Arcanum's Mapire, which overlays the georeferenced Habsburg military surveys on a modern map. mapire.eu now redirects to maps.arcanum.com, where full access needs a subscription. It carries the first survey (1763–1787; Galicia 1779–1783, Bukovina 1773–1775) and the second (1806–1869; Galicia and Bukovina 1861–1864) [S36], [S37]. Keep the Gesher Galicia Map Room as the route to cadastral maps [S32]. For the jurisdiction and record holders that put these Galician cadastral and military-survey maps in context, see [Route a Galician or Bukovinian record by date, confession and custodian](galicia-bukovina-habsburg-record-routing.md).

Check an overlay’s alignment against surviving roads, railways or other fixed features across the area of interest, and retain the georeferencing files with the image [S13]. A historical atlas may distort locally even where the roads align [S11], [S14]. For a hand-drawn Sanborn outline, check whether the line denotes a building or parcel before measuring from it [S8]. Establish a property boundary from the deed or survey; on PLSS land, plot the aliquot parts in the description [S2], [S11]. Use [land-index recovery](land-index-book-series-recovery.md) to retrieve the deed.

**Custom overlays in Google Earth Pro.** If the available overlays miss the place or period, choose a public map image of the right edition and open it from the computer with **Add → Image Overlay → Browse**. Lower the opacity until both maps are visible. Move, rotate or resize the image to match several surviving landmarks across the area. Record the map edition, the landmarks used and where the fit breaks down [S83 @2026-06-08], [S84 @2026-06-08].

## Return a map packet

- **Sheet citation:** holder, volume, base and correction dates, sheet, and where the legend came from.
- **Edition register:** series, sheet, date, scale, feature shown, whether it is absent or not covered, and the name as printed.
- **Structure observations by edition,** kept apart from occupant or owner inferences and the reasoning behind them.
- **Address worksheet:** literal address, candidate readings, the edition used and how far its date is from the record, bridging evidence, the historical and current house numbers (or parcel and house numbers) with where each came from, whether the position is approximate or estimated, and a provisional modern address.
- **Coverage note:** holders and services checked, and those not checked.
