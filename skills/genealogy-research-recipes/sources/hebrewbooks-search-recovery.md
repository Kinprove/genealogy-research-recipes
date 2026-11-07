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
  2026-11-07 returned HTTP 403 with a Cloudflare challenge, so neither page could be read that
  day; the step therefore asks for a browser check.

## Credits

- Kinprove — original distillation and synthesis; the list of what to look for and the OCR and Otzar HaHochma notes paraphrase the JewishGen guides, the 2018 study and the Otzar HaHochma page above — FSL-1.1-MIT (kinprove-original)
