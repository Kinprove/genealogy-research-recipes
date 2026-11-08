---
id: "repository-photograph-collection-search"
title: "Search repository photograph collections by place and subject"
summary: "Search repository photograph collections for an ancestor, home, shop or community by place and subject."
kind: "records"
scope: {"platforms": [], "tasks": ["Search repository photograph collections for an ancestor, home, shop or community by place and subject.", "Search current and completed auction or marketplace lots for old family photographs."]}
triggers: ["Search repository photograph collections for an ancestor", "home", "shop", "community by place and subject", "auction or marketplace lots of old photographs"]
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "REPOSITORY-PHOTOGRAPH-COLLECTION-SEARCH-01", "text": "never compare faces or name anyone by appearance, and record a recognition by the user or a relative as that person's attributed claim; a name-search miss does not show that no image exists, and a donor caption or added geotag is not a settled identification or location."}]
handoff: ["family-photograph-attribution-and-dating", "soviet-personal-file-recovery", "usa-immigration-search-recovery"]
checked: "2026-11-02"
checked_basis: "opened 2026-11-02"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": ["publish", "third-party-tool"], "contact": ["contact"]}
router: {"tier": "pointer", "group": "Family papers, photographs and oral history", "order": 1127}
---

# Search repository photograph collections by place and subject

Use this recipe when you need an image of an ancestor, or of their home, shop or community. It covers holdings from photographers, studios, historical societies and manuscript collections. The common mistake is to search the photo database for the ancestor's name, get no hit and report that no image exists. A related mistake is to treat a donor caption, a geotag the holder added, or a facial resemblance as a settled identification or an exact location.

This recipe covers search coverage and caption provenance. For a located Swedish aerial view, it also names the next resident and ownership records to search.

- **Privacy gate:** <!-- privacy-gate: third-party-tool --> Pasting a photo into an AI tool sends images of people who may be living, and the photo holder's data, to a third party; answer the privacy gate in `SKILL.md` first.
- For AI analysis of context clues in a photo, such as a car model, a uniform or a shop sign, use [AI for documentary records § What to delegate freely](ai-for-documentary-records.md), which treats such output as leads. Faces are never compared.
- Identity rulings belong in [evidence/proof judgment](evidence-proof-judgment.md).
- Record your searches with the [research log](research-documentation.md).
- For street and business names by year, use [city-directory observations](city-directory-observation-workflow.md).

## Contents

- Find the collections that cover the town and period
- Browse by place, subject and business, not by person
- Riddarhuset portraits: select the branch, then inspect the object
- Browse neighboring aerial-image series and paper copies
- Exhaust each repository's surfaces before reporting no image
- Check records that carry a portrait
- Add family-uploaded memorial portals in former Soviet cases
- Search auction and marketplace lots
- Keep each statement about the image separate
- Record a proposed identification as an attribution
- Return

## Find the collections that cover the town and period

Start from the family's locality and date range, not from the name. List these candidate holdings:

- **Local photographer or studio negative collections.**
  - The Overson studio's glass-plate negatives from St. Johns/Apache County, Eastern Arizona, run from about the 1880s to 1940. They were being placed on FamilySearch Memories in 2016 [S1]. Group and student shots are among them, and the presenter estimates that most local families of that period were photographed at least once. Browse a locality's studio negatives early, by group and subject. The presenter says the originals went to a university. The University of Arizona's Overson family photograph collection (MS 549) lists access as in person only, and its contents date from 1840 to the 1950s, mostly 1920s–1940s. Log a holding like that as unsearched until someone searches it on site.
  - The Larson Studio negative collection (Provo and Utah County, studio active 1916–1968) is held by the Utah State Historical Society and hosted in the University of Utah Marriott Library's digital library [S2].
- **Historical-society photo databases.** Find them through the society's website or social-media page [S5].
- **Digital collections at county or local genealogy repositories.** One presenter reached her ancestor's photograph through a link on a county genealogy society's website [S4].
- **Orphan or unidentified-photo sites.** These hold both identified and unidentified photos. Search the identified ones by surname, and search the unidentified subset (on DeadFred, the "Mysteries") by place, not by name [S7].

Use only collections whose catalogue or description actually covers the place and period. Do not assume that a photographer's work survives for the family's town.

## Browse by place, subject and business, not by person

1. Limit the search to one relevant collection at a time. Search or browse by:
   - place and date
   - street and building
   - business name
   - group subject: classes, graduations, teams, events [S1], [S2], [S6]
2. Do not treat a personal-name miss as absence. The 2023 presenter in [S2] reported that a couple of thousand Larson Studio sitters were titled only "unknown man" or "unknown woman", and that about 1,500 were still unidentified. He found his mother-in-law's 1956 graduation portrait under "unknown woman". Browse the thumbnails for the right period instead.
3. Search the street or business, not the exact modern address, because addresses change [S5]. One presenter found a great-grandfather in a historical-society photo of his store. He was not named, but the store's name contained the family surname [S5]. Before searching, check the earlier street or business name against a directory.
4. On unidentified-photo sites, query the ancestral town and state. In [S7], a researcher typed the town and state instead of the surname and reached a "mystery photo" of her relative.
5. Also run a surname-only search with the format filter set to images. A presenter recommends the surname alone, without forenames, because it tolerates spelling variants [S3]. Log it as one surface among several, not as the whole search.

## Riddarhuset portraits: select the branch, then inspect the object

Use this branch for a portrait sought through a Swedish noble family. A surname can
return several distinct families or branches. ArkivDigital's October 2026 Minerva
demonstration distinguishes family searching from object searching, then demonstrates
a separate ArkivDigital portrait index leading to cards, images and identifying backs
[S14]. These are complementary search surfaces, not a demonstrated complete crosswalk
between the two services.

1. Start with independently supported family context. In Minerva's family results,
   preserve the full name, noble rank, introduced number and branch qualifier actually
   supplied. Keep same-surname entries separate until the target branch is resolved;
   an attractive portrait does not resolve that choice.
2. Search the selected family page's related objects and the separate object search.
   Record the family/branch filter and object type, such as portrait or photograph,
   used on each surface. The demonstration also searches other objects; a document
   result and a portrait result are different targets. Do not assume every family
   has the same object coverage or that one result searches the other surface.
3. Check ArkivDigital's Riddarhuset portrait finding aid as a separate surface, using
   the supported family name. Save the returned locator and open it. In the
   demonstration, the first image is a catalogue card rather than the portrait [S14].
   Verify which object the current image shows before marking a portrait retrieved.
4. Browse the adjoining images for the matching portrait and any photographed reverse.
   Record each card, front and back with its own image locator and observed connection;
   do not assume a fixed image offset or that every object has a digitized reverse.
   Copy identifying inscriptions and cataloguer attributions separately, retaining
   their wording and any conflict. A reverse can supply a statement about the sitter;
   it does not establish that statement's correctness.
5. Compare the retrieved object's stated person, dates and branch with the search
   context, keeping uncertainty explicit. Do not identify a face or adopt a family
   relationship from a surname, a card or the presentation's example. Return missing
   objects, uninspected reverses and unresolved branch matches as those exact gaps.

Record Minerva and ArkivDigital searches separately, linking their results only when
the inspected descriptions or objects support the connection. In the 2026 talk,
Riddarhuset explicitly describes its genealogies as Word/PDF documents rather than a
database answering spouse, child or parent queries [S14]. A family hit therefore does
not execute such a relationship search. The talk establishes a historical retrieval
route, not current controls, complete holdings or a verified portrait identification.

## Browse neighboring aerial-image series and paper copies

**A series marker is not the photographed house's coordinate.** In its July 2026
demonstration, ArkivDigital explains that it positioned aerial series from routes
drawn on flight maps, without knowing the exact house locations or the path flown
between houses [S15]. Keep that series position separate from a house location
established from the actual view. Proximity to a marker does not geolocate the image.

**Inspect several surrounding series, not only the nearest map marker.** In ArkivDigital's June 2024 demonstration, the presenter says the precise flight routes are unknown and recommends opening several nearby series [S11]. The nearest marker is a starting point; it does not establish which views the flight contains.

**Check for a corresponding paper-print series as well as the negatives.** Establish the relationship from the collection's actual metadata and images. ArkivDigital's June 2026 demonstration shows negative series marked O and paper-copy series marked R; some scanned print backs supply a place or purchaser's name [S12]. Follow that counterpart route where it exists, rather than assuming every negative has a surviving print.

Use [archival image coverage verification](archival-image-coverage-verification.md) to check the observed order and sides. In the 2026 demonstration, stepping two images at a time could show only fronts or only backs [S12]. Do not count a run of fronts as inspection of both sides. Record the series/item locator and the side that supplies a clue. The examples describe those historical demonstrations; check the actual collection and viewer before relying on their codes or controls.

**For a located Swedish aerial view, search residents by the period property designation.** ArkivDigital's April 2026 demonstration advises locating the view, using historical maps to recover its address or *fastighetsbeteckning* at that time, then searching the designation in *Sveriges befolkning 1940–1990* [S13]. Search it only for the ancestor's household, and note only the names and family positions the question needs; do not record later or possibly living residents or use the register to find a living person. An approximate flight marker or a name on a print back is a clue; it does not establish that location.

**Keep the ownership search separate.** The same demonstration directs ownership questions to *fastighetsböcker* (property books), mentioning Riksarkivet's reading rooms [S13]. A population-register resident is not thereby the owner. Check the relevant historical property and ownership entry separately; the demonstration does not establish current holdings or access.

## Exhaust each repository's surfaces before reporting no image

**Search every photographer collection that holds images of people, not only the largest one.** The [S3] example comes from BYU special collections. There, a surname search filtered to images returned mostly hits from the George Edward Anderson collection, but other collections also produced results. The presenter advises searching at least both of the main people-image collections, Anderson and C. R. Savage, rather than going straight to Anderson [S3]. The general lesson: one photographer's collection is never the whole repository.

**Then search the manuscript finding aids.** The same presenter notes that many photographs in BYU's manuscript collections had not been digitized and would not appear in the digital photo collections [S3]. Search the manuscript finding aids at every repository, not only at BYU.

**Log each surface separately.** For each one, record:

- the collection
- the search or browse mode
- the terms or browse range
- the date
- the result

"No image found" covers only the surfaces you logged. List undigitized manuscript photographs and on-site-only holdings as unsearched, not as negative results.

## Check records that carry a portrait

Some records about a person include that person's photograph, and for some families these may be the only surviving portraits. The record that holds the photograph attributes it; never match it to another image by face. Log each record type as its own surface, and note which copy you inspected: court, agency or family.

- **U.S. passport applications.** Photographs have been required since 21 December 1914. The National Archives holds applications from October 1795 to March 1925; the State Department holds later ones. As a general rule, U.S. citizens needed no passport to travel abroad until 1941, apart from 1861–1862 and 1918–1921, so a missing application is common [S16].
- **U.S. naturalization papers.** Declarations of intention filed from 1 July 1929 have a space for the declarant's photograph, and certificates issued from 1 July 1929 carry the holder's signed photograph [S17], [S18]. The National Archives usually has no copy of the certificate [S19]. The USCIS C-file holds a duplicate, and C-files (27 September 1906 to 31 March 1956) include photographs only from 1929 onward [S20]. A National Archives staff answer states that petitions for naturalization never carried a photograph [S21]. For the request route, see [U.S. immigration search recovery](usa-immigration-search-recovery.md).
- **Alien Files (A-files).** They can contain photographs among visas and applications [S22]. The 1940 alien registration form (AR-2) records a fingerprint and a physical description, not a photograph [S23].
- **U.S. federal prison inmate case files.** They can include identification photographs. The National Archives at Kansas City holds Leavenworth files for 1895 to 1957, and most include a mugshot, with front and side views [S29], [S24]. The National Archives at San Francisco holds Alcatraz files dated mainly 1934 to 1963, with prisoner identification photographs [S25].
- **Soviet internal passports and personnel files.** Under the 1974 Passport Regulation, applicants handed in two photographs, and new ones were pasted in at ages 25 and 45, so one passport can hold portraits from different ages [S26]. To bound the date of each, see [family photograph attribution and dating](family-photograph-attribution-and-dating.md). A workplace personnel file (личное дело) may have a photograph pasted in, but not always [S27]; to find the file, see [Soviet personal-file recovery](soviet-personal-file-recovery.md).

## Add family-uploaded memorial portals in former Soviet cases

For a person from the former Soviet Union, memorial portals filled by families are a separate surface for a person photograph. Choose them by case type and search each with its own search:

- **WWII participants:** Бессмертный полк (Immortal Regiment, moypolk.ru), whose veteran stories carry portraits [S8], and Дорога памяти (Road of Memory, 1418museum.ru, formerly foto.pamyat-naroda.ru), a Russian Ministry of Defence project that collects participants' photographs [S9]. Road of Memory's participant-search link was a placeholder when checked on 2026-11-02; working person search was not verified. Treat it as an unsearched lead until an actual search or browse surface is available, and do not count an unavailable search as a name miss.
- **Repression victims:** Бессмертный барак (Immortal Barracks, bessmertnybarak.com), which describes itself as collecting documents and photographs of victims [S10].
- **Deported or dekulakised families:** add local publications from the place of exile, not only from the place of origin.

Log each portal as its own surface. A family caption on a portal is an attribution: record it as in "Record a proposed identification as an attribution" below, but give its source as the portal's family contributor, with the relationship if the page shows one, never the contributor's name; and never compare faces.

**Privacy gate:** <!-- privacy-gate: contact --> A message through a portal's contact form reaches a living relative who keeps the page and may disclose the user's family details; answer the privacy gate in `SKILL.md` before sending it.

These portals concern living families. A Бессмертный полк page names the relative who keeps it, with their relationship, a contact form and sometimes a phone number [S28]. Record the person and the story, never collect contributors' names or contact details, and use a portal's contact form only when the user asks to make contact.

## Search auction and marketplace lots

Old photographs are also sold through online auctions and second-hand marketplaces: a 2022 commodity-evaluation study built its sample of 100 artistic, historical and scientific photographs from those put up for sale at the Violity auction [S30]. Log each such site as one more surface, covering completed sales as well as open lots, and run the place, studio and surname terms used on the repository surfaces. A seller's description is a claim to test against other evidence, like a donor's identification; record the lot number and page address as the item locator. If a lot includes papers of people who may be living, note only what the question needs.

On Meshok, checked 2026-11-08, keyword search matches lot titles only, so also browse its catalogue categories; a separate option searches successfully completed lots [S31 @2026-11-08] [S32 @2026-11-08].

## Keep each statement about the image separate

For every candidate image, record these as separate fields:

- **Photographer's original caption and date**, as the holder transcribes them. In the Frith collection on Findmypast, each record carries the photographer's original description, the date and the location [S6].
- **Holder-added coordinates**, flagged as approximate. The Frith records also give latitude and longitude. These were added after the fact, because 19th-century photographers did not record them. She says they are fairly precise for well-known landmarks and loose for general scenes such as a party on a mountainside [S6]. Never report them as the exact spot.
- **Recorded donor**, kept separate from what the image shows. A donor is a lead to where the identification came from and to related family material. The presenter in [S4] planned to contact the donor of her ancestor's photograph. A donor's identification is a claim to trace, not a confirmed fact.
- **Nearby-place images**, labelled "local context only". A view of the next village or the town centre does not show the ancestor's house or the ancestor.

## Record a proposed identification as an attribution

If the user or a relative recognises someone, record it as that person's attribution. Give:

- who made it
- when
- the basis they state: their own comparison with a family photo of known provenance that they hold, a store name, a group roster, the date or the setting

Do not compare faces yourself and do not name anyone from appearance. Resemblance is never evidence on its own: a recognition stays an attributed claim until documents support it. In [S7], the researcher recognised the man in a mystery photo found on the site by comparing it with a different photo of him that she owned. Never use an AI-enhanced or AI-generated face in any comparison (see the AI-for-documentary-records link above).

**Privacy gate:** <!-- privacy-gate: publish --> A suggested metadata correction makes the names of people in the photo public in the holder's catalogue, and some sitters may be living; answer the privacy gate in `SKILL.md` first.

Offer a supported identification to the holding institution as a suggested metadata correction. Keep the original caption alongside it, and do not overwrite it in your own notes. A presenter encourages suggesting such updates so that others can find the images [S2]. In [S5], the holder was glad of help identifying the people in the store photo.

## Return

- **A coverage log** by repository, collection and surface: photo database, each photographer collection, finding aids, county or society sites, records that carry a portrait (with the copy inspected), memorial portals. Mark each surface as browsed, searched or not yet searched.
- **Candidate image records**, each with:
  - the stable item locator
  - the original caption and date
  - the donor
  - holder-added coordinates, flagged approximate
  - any "local context only" label
- **Any proposed attribution and its basis**, kept separate, plus an optional draft metadata-correction suggestion.
- **For a Riddarhuset portrait search:** the exact family/rank/number/branch candidates,
  each search surface and object filter, linked card/front/back locators, literal
  identification statements and unresolved branch, object or reverse gaps.
