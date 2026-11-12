## Sources

- Nahum Zitter, *HebrewBooks: first among equals*,
  [Safranim](https://safranim.com/גיליון-ח/ג-נחום-זיטר-מאגר-היברובוקס-ראשון-בין-ש/).
  Circa 2010–2011, incorporating a November 2010 announcement.
  Supports catalogue/full-text separation,
  spelling variation and the historical absence of authority control.
- Mississippi Fred MacDowell, *Searching online in Hebrew with imperfect OCR*,
  [On the Main Line, 2011-09-02](https://onthemainline.blogspot.com/2011/09/searching-online-in-hebrew-with.html).
  Supports the three OCR-confusion examples and external site-search route.
- Ezra Brand, *Guide and Review of Online Resources 2022, Part I*,
  [Seforim Blog, 2022-03-30](https://seforimblog.com/2022/03/guide-and-review-of-online-resources-2022-part-i/).
  Recommends the beta search entry point.
- [Shafeh catalogue form](https://shafeh.org/hb/search) and
  [submitted title query](https://shafeh.org/hb/search?title=%D7%9E%D7%A1%D7%99%D7%9C%D7%AA+%D7%99%D7%A9%D7%A8%D7%99%D7%9D&author=&ocr=&commit=%D7%97%D7%99%D7%A4%D7%95%D7%A9),
  inspected independently twice on 2026-10-03. Both requests returned HTTP 200; the query
  rendered catalogue records. The form submits separate `title`, `author` and `ocr`
  parameters. The footer attributes data to beta.hebrewbooks.org.
- [J-Roots topic 64, “Случайные находки”](https://forum.j-roots.info/viewtopic.php?f=15&t=64).
  A participant corrected surname index order to given-name order.
- [Hebrew Wikisource template documentation](https://he.wikisource.org/wiki/תבנית:היברובוקס-דף),
  last edited 2016-03-08. Distinguishes viewer and printed page numbers.
- HebrewBooks public mobile app, commit `7b2443c23854ef8fa68b3d3d0104bf1ec2dcb428`:
  [search screen](https://github.com/hebrewbooks/mobile_app_public/blob/7b2443c23854ef8fa68b3d3d0104bf1ec2dcb428/lib/screens/search.dart#L205),
  [results widget](https://github.com/hebrewbooks/mobile_app_public/blob/7b2443c23854ef8fa68b3d3d0104bf1ec2dcb428/lib/shared/widgets/book_list.dart#L342),
  [query provider](https://github.com/hebrewbooks/mobile_app_public/blob/7b2443c23854ef8fa68b3d3d0104bf1ec2dcb428/lib/providers/search_query_provider.dart#L28).
  The screen's length guard selects history/empty state; the widget's guard precedes
  `fetchSearchBooks` at line 359; the provider stores the supplied value without trimming.
  [Dart String.length documentation](https://api.dart.dev/dart-core/String/length.html)
  confirms that the measurement is UTF-16 code units.
- Tom Chatt, *Prenumerantn*, [JewishGen InfoFile](https://www.jewishgen.org/InfoFiles/prenumerantn.htm),
  checked 2026-11-07. Supports the bibliographic details of Berl Kagan's *Sefer HaPrenumerantn*
  (New York, 1975) and its arrangement as an index by town to the books that list the town's
  subscribers.
- Chaim Freedman, [prenumeranten](https://www.jewishgen.org/Rabbinic/infofiles/prenumeranten.htm),
  JewishGen Rabbinic Genealogy infofile, checked 2026-11-07. Supports subscriber lists as a
  genealogical source and the family information in rabbinic books' introductions and title pages.
- JewishGen Rabbinic Genealogy, [resources](https://www.jewishgen.org/Rabbinic/infofiles/resources.htm),
  checked 2026-11-07. Lists introductions, approbations, responsa and pedigree documents among
  rabbinic texts used in genealogy.
- Shahar Mahpod and Yosi Keller, *Auto-ML Deep Learning for Rashi Scripts OCR*,
  [arXiv:1811.01290](https://arxiv.org/abs/1811.01290), 2018, checked 2026-11-07. Supports the
  use of commercial OCR packages by HebrewBooks and similar projects and the absence, at the
  time, of commercial or academic OCR for Rashi script. It is not a measurement of HebrewBooks'
  current OCR.
- Otzar HaHochma, [English home page](https://www.otzar.org/otzaren/indexeng.asp), checked
  2026-11-07. Supports the size (156,000 books), the OCR full-text search and its sale as a
  paid product.
- Automated requests to `https://beta.hebrewbooks.org/` and `https://hebrewbooks.org/` on
  2026-11-07 got mixed answers: several returned HTTP 403 with a Cloudflare challenge, a later
  one returned HTTP 200, and the pages' content was not inspected. The step therefore asks for a
  browser check instead of stating the beta site's status.

### Platform recheck, 2026-11-12

Rechecked 2026-11-12: the Shafeh form still offers separate title, author and OCR fields, and its
footer still says the data load from beta.hebrewbooks.org; the submitted title query returned 110
results, with record 41768 first and both partial titles quoted in the recipe among them. The beta
and main HebrewBooks home pages each answered two plain automated requests that day with HTTP 200
and no challenge, and both rendered a search form with title, author and OCR fields; the recipe
still asks for a browser check because the earlier answers were mixed. A viewer link of the shape
the recipe gives, for the Wikisource template's own example book and page, opened page 23 of 101 of
that book. The Wikisource template documentation (last edited 2016-03-08) still says its page
parameter is the HebrewBooks page, not necessarily the printed number. The three app files at the
pinned commit still hold the length guards at the cited lines, the search request at line 359 and
the untrimmed assignment, and the Dart documentation still counts UTF-16 code units. Chatt's guide
(updated March 2016) and the two JewishGen rabbinic-genealogy pages still support the subscriber
list, introduction and approbation statements. The Otzar HaHochma page still gives 156,000 books, an
OCR search engine and paid hard-drive and online versions. The 2018 study's abstract page was
reachable; its body was not re-read, as it supports history. The articles by Zitter, MacDowell and
Brand were not re-read, as they support history and methods, and the J-Roots topic could not be read
because the forum's certificate had expired. The recipe text was not changed.

## Credits

- Kinprove — original distillation and synthesis; the list of what to look for and the OCR and Otzar HaHochma notes paraphrase the JewishGen guides, the 2018 study and the Otzar HaHochma page above — FSL-1.1-MIT (kinprove-original)
