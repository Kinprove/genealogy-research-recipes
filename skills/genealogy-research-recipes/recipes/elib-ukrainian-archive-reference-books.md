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

Provider examples were checked on 2026-10-18; see [source notes](../sources/elib-ukrainian-archive-reference-books.md).
