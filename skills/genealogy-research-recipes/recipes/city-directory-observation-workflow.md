# Recipe: Build a checked city-directory observation series

## Goal

Turn city-directory entries into a comparable series of names, addresses and occupations.
Preserve which editions and locality sections you inspected, so a missing result does not
silently become a move, death or identity conclusion.

## Before starting

Choose a person or bounded surname group, locality and edition-year range. Keep an image
locator with every extracted entry. Use the directory's own wording for names and addresses;
put expanded abbreviations and proposed identity groups in separate fields.
The worksheets below work with manually read images or copied index rows.

## 1. Audit the editions and their internal sections

1. List the editions actually available at each repository. Record individual years and gaps,
   rather than treating a collection's broad date range as uninterrupted coverage.
2. Open a volume's title page, contents and section headings. A directory named for one city
   can include separate alphabetic sections for surrounding communities or a county taxpayer list.
3. Record which section should contain the target and which you inspected. Inspect another
   relevant locality section when the first does not contain the expected entry.
4. Save the abbreviation key for that edition. Decode an entry with that key before expanding
   residence, boarding or occupational abbreviations.
5. Mark an inaccessible edition or uninspected section separately from an inspected section
   with no matching entry. [S2, S3, H1]
6. For a former-resident directory, read the foreword to identify the addresses' roles.
   The 1949/50 Breslauer Adressbuch lists later addresses of former Breslau residents but
   orders entries by earlier street and house number. The ordering address is a lookup key;
   do not record it as residence in the titled city at publication. [S4]

**Artifact:** One coverage row per edition and relevant section:
repository, directory title, edition year, locality/section, available/access status,
section image range, inspected range, abbreviation-key locator and result.

**Check:** The year and locality come from the volume, not only its database label. Another
repository's copy of that same volume supplies another access route, not another observation.

## 2. Extract comparable rows without importing the index's mistakes

1. Locate the surname group or candidate entry using the volume's actual arrangement.
   If the name index fails, browse a relevant alphabetical section only when one exists,
   and compare the printed entry with its indexed name. For a former-resident list, use
   the former street/house as a lookup key only when the foreword or heading confirms
   that ordering and the former address is available. If the required key is unknown
   and no usable index supplies another route, leave the entry unlocated and record
   the lookup as unresolved. Do not invent an alphabetical or DES route. [S3, S4]
2. Copy the entry as printed, including initials, spouse wording, occupation and address when
   present. Preserve uncertain readings. Keep any normalized name in a separate column.
3. If copying a site's tabular index into a spreadsheet, take the header once, paste subsequent
   records beneath it, and add the correct edition year to every imported row.
4. Compare imported fields with the image. Information printed next to a name can be a locality
   or post office rather than another given name; retain the correction and the original index value.
5. Check the first and last imported entries, remove repeated headers or interface text, and
   confirm that each row still has its year and locator. Manual extraction uses the same schema.
   [S1, S3]

**Artifact:** An observation table with these columns:

| Field | Preserve |
| --- | --- |
| Observation ID | A stable identifier for this row |
| Edition and section | Directory title, year, locality and section |
| Name | Printed form, indexed form if used, normalized form separately |
| Address | Printed street/number or locality/post-office wording |
| Other entry text | Occupation, spouse or other relationship wording actually present |
| Reading status | Image checked, index only, or uncertain reading |
| Locator | Repository/collection, volume, printed page, image link/number |
| Candidate group | A provisional identifier; leave competing groups separate |

For entries in a former-resident list, add these columns only where that structure applies:

| Field | Preserve |
| --- | --- |
| Former address / ordering key | Earlier street and house number as printed in the row or its heading, with locator |
| Later address as reported | Later address/place as printed, including care-of or household wording |
| Address-role and time basis | Foreword/heading locator, dates actually stated, and unresolved roles or dates |

**Check:** Do not import an index field as printed evidence when the image says something else.
An edition year identifies the volume; it does not by itself establish a residence date for
each printed address or an exact move date. Keep an unstated time basis unknown. [S4]

## 3. Sort the series into questions you can investigate

1. Append the next available edition using the same columns.
2. Sort complete rows by normalized surname and given name, then by edition year.
3. Compare occupation and address within each tentative group. Try an occupation-first or
   address-first view when repeated names remain ambiguous.
4. Keep raw spellings and initials visible while filtering variants. An initial-only filter
   may miss a spelled-out given name; inspect the records admitted and excluded by that filter.
5. When the volume has an address-arranged or reverse directory, use it to inspect the
   relevant street and nearby entries. Record those observations separately.
6. Create a question for each change or competing group, with the row IDs that caused it.
   A recurring name, occupation or address is a comparison clue, not an automatic merge. [S1, S2]
7. For a located former-resident entry with a reported later locality, use that place for
   one bounded follow-up, such as a later directory or a relevant civil-register search there.
   Keep it as a source-attributed lead; it does not establish a move at the edition date. [S4]

**Artifact:** The observation table, saved sort/filter criteria, provisional groups and a
worklist such as “retrieve a record linking observations D07 and D12.”

**Check:** Sorting preserves each row's year, source and raw wording. A group assignment remains
provisional until the records support that person's identity.

For a supported same-block or building question, retain each literal building and unit number,
including fractional addresses. Compare dated street/reverse entries and stable-neighbor
context before choosing between a move, unit conversion, renumbering or an erroneous entry.
Keep the proposed correspondence provisional until supported; do not silently correct numbers.
The [old-home address example](https://dna-explained.com/2023/04/09/finding-the-old-home-place-with-zillow-52-ancestors-394/)
motivates the comparison without proving occupancy, identity, a conveyance or renumbering.

If an inspected auxiliary section labels a land-register reference, preserve its heading,
locality, street/house wording and land number separately. Carry the stated reference into
the [land-index/book-series workflow](land-index-book-series-recovery.md); house, parcel and
land-register numbers are different roles. [CompGen's directory example](https://www.compgen.de/2023/02/adressbuch-mit-unerwartetem-inhalt-entdeckt/)
identifies such a section, but its missing illustrated table does not establish fields in
another volume or prove ownership.

## 4. Describe gaps before assigning events to them

1. For the first or last apparent appearance, return to the coverage sheet.
2. Check whether an omitted year is absent from this repository, was not published, is
   inaccessible, or remains unlocated. Keep the unknown state when you cannot distinguish these.
3. Check whether the earlier edition included the same community or taxpayer/resident section.
4. Search another available edition or repository when that specific gap affects the question.
5. Report the actual observations and remaining gaps. For example: “Listed in the inspected 1931
   taxpayer section; not found in the inspected 1929 volume; comparable 1929 section coverage
   remains unconfirmed.” Do not replace that with a dated arrival. [S3, H1]

**Artifact:** A short timeline of observed entries plus a gap table and the next bounded search.

**Check:** A gap in a database's editions and an absent entry on inspected pages are different
results. Neither alone establishes why the person is missing.

Record the edition's stated inclusion rule and its locator beside the coverage row; leave
that rule unknown when the volume does not establish it. A directory listing household heads
does not make an unlisted household member absent from the household or locality. CompGen's
address-book example also distinguishes a woman's marital-status wording from an occupation;
retain the printed role without inferring employment from it. [S5]

## Prompt pattern

> Using these directory images, edition descriptions and earlier worksheet rows, produce the
> coverage sheet and observation table above. Preserve printed names and abbreviations, identify
> which section and year each row belongs to, and show corrections to index fields separately.
> For former-resident lists, retain the earlier/ordering and later-address roles separately.
> Group candidates provisionally, keeping alternatives. Explain each gap using the recorded
> coverage, then give one bounded next search. Do not infer a move or death from a missing row.
