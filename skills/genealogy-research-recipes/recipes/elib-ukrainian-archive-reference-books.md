---
id: "elib-ukrainian-archive-reference-books"
title: "Recovering and identifying Ukrainian archival guides in ELIB"
summary: "Retrieve Ukrainian archival guides from ELIB and identify the correct volume, part and fund scope."
kind: "platform"
scope: {"platforms": ["elib.nlu.org.ua"], "tasks": ["catalogue-card versus PDF confusion, leading-zero item IDs, keyword misses, similar volume titles or garbled cover-text extraction."]}
privacy: "none"
gates: []
guardrails: [{"id": "ELIB-UKRAINIAN-ARCHIVE-REFERENCE-BOOKS-01", "text": "Prefer the current card's link over a constructed URL. A constructed route is a retrieval lead until its response is verified as the intended PDF; redirects, error HTML or an access failure leave acquisition unresolved."}]
handoff: ["archival-image-coverage-verification"]
checked: "2026-11-12"
checked_basis: "Rechecked 2026-11-12"
capabilities: {"browse": ["elib.nlu.org.ua"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"tier": "full", "group": "Featured workflows", "order": 1}
---

# Recipe: Recovering and identifying Ukrainian archival guides in ELIB

Use for a Ukrainian regional archive's `Путівник`, `Анотований реєстр описів` or
related finding aid in the Institute of History of Ukraine's electronic library
at `resource.history.org.ua`. The goal is the correct volume and its archival
scope, followed by a usable citation to the actual guide.

## Retrieve the object behind the catalogue card

Keep the item identifier as text, including leading zeros. According to its card,
the checked example `0014010` is the Chernihiv archive guide, volume 1, published
in 2001; the card also links the full-text PDF. [S1]

Start with the item page, for example:

```text
https://resource.history.org.ua/item/0014010
```

Read its archive, title, year, volume and series fields, then follow the actual
full-text link. Do not count the catalogue HTML or cover thumbnail as acquisition
of the finding aid. For the checked item, the PDF route uses this pattern: [S1, S2]

```text
https://resource.history.org.ua/cgi-bin/eiu/history.exe?C21COM=2&I21DBN=ELIB&P21DBN=ELIB&Image_file_name=book/<ID>.pdf&IMAGE_FILE_DOWNLOAD=0
```

Prefer the current card's link over a constructed URL. A constructed route is a
retrieval lead until its response is verified as the intended PDF; redirects,
error HTML or an access failure leave acquisition unresolved.

## Resolve the volume from the book

Compare the card with the PDF's title page, publication information and contents.
Record `Том`, `Частина` or `Книга` and the covered funds or chronological sections
before naming the downloaded file. Similar archive titles and publication years
do not distinguish volumes by themselves. Keep the item ID alongside the volume
identity so a renamed local file remains traceable.

If extracted cover text is unreadable, inspect the rendered title page or OCR
that small area. The checked PDF is accessible, but text extracted from its first
pages is garbled: poor extraction alone does not establish a corrupt document. [S2]
Check readable interior pages separately; neither a title guess nor a successful
download settles the book's identity or completeness.

## Check the consolidated metrical-book catalogue

Once a guide names the archive, check whether the consolidated catalogue series
`Зведений каталог метричних книг, що зберігаються в державних архівах України`
(consolidated catalogue of metrical books held in the state archives of Ukraine;
Ukrderzharkhiv and UNDIASD) has a volume for it. Volume 8 covers the State
Archive of Khmelnytskyi Oblast (Kyiv, 2013, two books); ELIB items `0013670`
and `0013671` are its cards. Book 1 covers Orthodox parishes of all twelve
Podolia uyezds, some now in Vinnytsia and Odesa oblasts. Book 2 covers Orthodox
parishes in Volhynia and Kyiv guberniyas, plus Roman Catholic, Old Believer and
Jewish records. Book 1 opens with an overview of the fonds that hold the
registers, and both books have settlement indexes. [S3, S4]

The archive hosts both PDFs without login, as `mbv8-b1.pdf` and `mbv8-b2.pdf`
under `https://dahmo.gov.ua/pdf/`. [S5]

## Recover from a failed catalogue search without inventing coverage

A keyword miss can reflect the search interface, indexing or the query. If a
known relevant item is available, inspect its series and collection links first.
A small, explicitly bounded set of neighbouring item IDs can be a fallback lead:
inspect every returned title and record the range actually checked. Numeric
proximity alone does not establish a series, archive or continuous collection.
Stop at the declared bound; do not report a guessed ID range as the full catalogue.

This fallback and the volume-verification sequence are research procedures,
not a provider guarantee that adjacent IDs belong together.

## Cite the guide at the right evidentiary level

Keep archive, title, volume/part, publication year, item ID, source URL, access date
and local artifact pointer. For an archival lead, add the guide's printed page and
PDF image/page separately, the literal fund/inventory description and any proposed
mapping to a current catalogue.

A historical guide describes its publication's scope. It does not by itself prove
current holdings, access conditions, digitization, or the presence of a particular
person. Check those narrower questions against current archive information and
the actual case. Continue with [archival-image-coverage-verification.md](archival-image-coverage-verification.md)
when identifying or inspecting retrieved case images.

Provider examples were checked on 2026-10-18 and the consolidated-catalogue
volume on 2026-11-02; see [source notes](https://github.com/Kinprove/genealogy-research-recipes/blob/311dea4a7f115010941467dc3f922b68c165198b/skills/genealogy-research-recipes/sources/elib-ukrainian-archive-reference-books.md).
