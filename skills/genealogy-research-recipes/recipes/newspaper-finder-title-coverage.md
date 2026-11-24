---
id: "newspaper-finder-title-coverage"
title: "Find a digitized newspaper by title, place and issue date"
summary: "Use Newspaper Finder to discover alternate hosts for a historical newspaper and verify whether a host carries the target issue."
kind: "platform"
scope: {"platforms": ["Newspaper Finder"], "tasks": []}
privacy: "none"
gates: []
guardrails: [{"id": "NEWSPAPER-FINDER-TITLE-COVERAGE-01", "text": "A listed year range is a lead to the host. Confirm the target issue in the host's own holdings."}]
handoff: ["newspapers-com-search-recovery", "historical-newspaper-section-search", "local-repository-uncatalogued-holdings"]
checked: "2026-11-20"
checked_basis: "Read 2026-11-20"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"section": "Record websites, libraries and maps", "group": "Record websites", "order": 50}
---

# Find a digitized newspaper by title, place and issue date

Use this recipe when the target town or title is known and you need to find an online copy of a particular issue. A listed year range is a lead to the host. Confirm the target issue in the host's own holdings.

## Find titles by locality and year

Open Search in Newspaper Finder. Enter a start and end year and the publication country. Narrow by publication place or by title when known. Open the map pin for the locality and read the title, date range and database in each row. Inspect nearby towns' pins when they could have served the locality [S1 @2026-11-20] [S2 @2026-11-20] [S3 @2026-11-20].

Use Catalog for a title-first lookup. Enter the newspaper's title or a distinctive part of it in **Newspaper Title**, then sort the results table by clicking a column header. For an exact town lookup, select one country and one state before choosing the town in **Towns** [S3 @2026-11-22] [S4 @2026-11-22].

Start a locality search with all databases and narrow by state or province where applicable. If the target town has no listing, zoom out across county lines and inspect pins near the historical locality even where the modern map has no town label. If the event date is uncertain, compare map results for successive plausible date windows [S2 @2026-11-22] [S5 @2026-11-22].

## Compare hosts and confirm the issue

Compare rows for the same title and choose the hosts whose listed runs cross the event date. Check any free host among them. Follow the title to the host and inspect its issue list for the exact date. Determine whether that issue can be searched or must be browsed. Use the host's own holdings and issue access when deciding whether a subscription would help [S1 @2026-11-20] [S3 @2026-11-20].

When a Google News Archive listing omits the publication place, open the front-page scan of an issue from the target period and transcribe the place printed in the masthead. If the masthead gives no place, check the publisher's statement. Record the place as printed with the issue date and page URL, then compare it with the place and dates in the title record before treating similar listings as the same newspaper [S5 @2026-11-23] [S27 @2026-11-23] [S28 @2026-11-23].

## Find holdings beyond Newspaper Finder

For a U.S. title, search the Library of Congress **Directory of U.S. Newspapers in American Libraries** by title or publication place. Use its publication dates, place and links to preceding and succeeding titles to identify which paper and masthead to look for on the target date. Follow any digitized-issue or holding-library links and compare their issue or holdings lists against the title's publication span. If two papers shared a masthead, keep their runs separate by publication place and title record [S5 @2026-11-22] [S6 @2026-11-22] [S7 @2026-11-22] [S8 @2026-11-22] [S9 @2026-11-22].

To look for a smaller U.S. archive, follow the state links in The Ancestor Hunt's **Newspaper Links**. For Advantage Archives, also search **Community History Archives** by publication place or partner institution and open the local archive's title list. Check the institution's own holdings page if no online run turns up [S5 @2026-11-22] [S6 @2026-11-22] [S10 @2026-11-22] [S11 @2026-11-22] [S12 @2026-11-22].

If Newspaper Finder does not surface a host, open **Projects** on Veridian's website and choose **Newspaper Collections**. Scan the project descriptions for the publication place, period and type of newspaper. Follow a matching project's link to the institution's collection, open the title and verify the exact issue date [S24 @2026-11-23] [S25 @2026-11-23].

For Japanese diaspora newspapers, use the title or publication-place browse links in Hoover's **Asia Collections** guide to reach the **Hoji Shinbun Digital Collection**. Check the matching title's issues for the target date [S24 @2026-11-23] [S25 @2026-11-23] [S26 @2026-11-23].

When the country or title has sparse results in Newspaper Finder, check the country's own newspaper collections. For Dutch titles, look in **Delpher** and check the Dutch national library's newspaper catalogue for print holdings if the target issue is missing online [S5 @2026-11-22] [S13 @2026-11-22].

For a Swedish title missing from **Svenska tidningar**, check the National Library of Sweden's holdings in **Libris**. Read the coverage through 1906 as the library's collection of Swedish daily newspapers, with selected periodicals. For example, if *Stockholm Gazette* is missing from your search, check Libris record 2811179 for the library's holdings [S14 @2026-11-22] [S15 @2026-11-22] [S16 @2026-11-22].

## Distinguish a publication break from a holdings gap

If an installment series stops at the end of a digitized run, check the publication history for a pause or a successor title and check other holdings for the next issue. For Finnish-American newspapers, check the National Library of Finland's digitized holdings and microfilm listings. Track each installment by newspaper title, issue date, issue number and page [S17 @2026-11-22] [S18 @2026-11-22] [S19 @2026-11-22].

After *Amerikan suomalainen lehti* no. 6 of 9 February 1894, look under *Amerikan suomalainen* for no. 7 of 9 March 1894, listed on reel Mf 35 670 [S17] [S18].

If the issue is missing from a legal-deposit collection, look for evidence of receipt or non-delivery and check other holdings before ruling out publication. For *Tidningen Upsala* in 1874, the library's correspondence about missing issues records a failure to deliver the deposit copies [S20] [S21].

For U.S. research around World War I, verify which local German-language titles were still publishing at the target date and look for contemporaneous English-language papers serving the same place if the German-language search comes up empty [S22] [S23].

## Handoffs

- [newspapers com search recovery](newspapers-com-search-recovery.md)
- [historical newspaper section search](historical-newspaper-section-search.md)
- [local repository uncatalogued holdings](local-repository-uncatalogued-holdings.md)
