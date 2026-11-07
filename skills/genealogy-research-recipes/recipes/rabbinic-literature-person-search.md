# Search rabbinic and Hasidic literature for a person or a lineage

Use this recipe when a question about a Jewish ancestor depends on rabbinic or Hasidic books:

- a family tradition of descent from a rebbe, a tzaddik or a famous rabbi;
- a rabbi, judge or "learned man" said to be in the family;
- the rabbis of a town in a given period; or
- a name found in a sefer, a responsum, an approbation or a Hasidic tale.

The recipe finds the passages that name the person, reads them in the original, and decides
what each one establishes: a person, an office, a place or a kinship link. A hit can also turn
out to be only a namesake, a disciple or a legend.

For a HebrewBooks search that returns nothing, use
[HebrewBooks search recovery](hebrewbooks-search-recovery.md). For given-name equivalents, use
[Beider given-name variants](beider-given-name-variants.md); for spellings drawn from your own
sources, use [corpus-seeded name search](corpus-seeded-name-search.md). The crown rabbinate as
the body that kept metrical books is covered by
[Russian-Empire Jewish metrical book recovery](russian-empire-jewish-metrical-book-recovery.md).

## Contents

- 1\. How rabbinic literature differs from a records index
- 2\. Where to search
- 3\. Fix the era, the place and the exact claim first
- 4\. Collect the forms that the texts use
- 5\. Match Hebrew text the way it is printed
- 6\. Search by office, place and relation, not by surname
- 7\. Read the subject's own books and the front matter first
- 8\. Screen every hit before it becomes a person
- 9\. Count witnesses, not copies
- 10\. Test a lineage tradition before searching for a bloodline
- 11\. Record locators and limit every negative
- Output: a passage ledger
- Prompt patterns
- Failure modes

## 1. How rabbinic literature differs from a records index

- **People are named by office, father and town, rarely by surname.** A typical form is
  "R. Moshe son of R. Yaakov, av beit din of X", "the Rav of X" or "R. Leib Rivke's".
  Surnames arrive late. In one English edition of Breslov works, a rabbi's surname appeared
  once, while "the Rav of <town>" appeared 121 times for the same man.
- **One name is many men.** A bare "R. Nachman" names at least six different men in one
  Breslov anthology series. "The Rav of X" names every man who held that office.
- **The genealogy sits around the text, not in it.** Title pages, introductions,
  approbations (haskamot), subscriber lists (prenumeranten), letters, testaments, appendices
  and an author's own autobiographical passages name fathers, fathers-in-law and wives.
- **One account circulates as many copies.** Reprints, translations, retellings, lineage
  compilations and online trees repeat a single witness.
- **"Descended from the rebbe" usually means something else.** Discipleship, belonging to a
  court's following or a marriage into the rebbe's household are all more common than descent.
- **Search tools see a damaged layer.** OCR errors, attached prefix letters, vowel points,
  acronyms and Yiddish spellings hide names that are on the printed page.

## 2. Where to search

- **HebrewBooks.** A free library of scanned seforim with a catalogue and an OCR full-text
  search. Most PDFs carry a text layer. The catalogue's place is where a book was printed,
  not what it is about, and one title can belong to two different books. In October 2026 the
  advanced search displayed at most 200 result rows, so a long result list was not read in
  full.
- **Otzar HaHochma.** A large paid library with whole-library OCR search, used through its
  web viewer. Without a licence you see only the first pages of each book, and a licence does
  not open every publisher's books. Editions of one work paginate differently, so an older
  edition is not a page-for-page substitute. Export is limited: list the pages you need before
  paying for access.
- **Dicta library.** A free library of OCR'd rabbinic books, many of them responsa, each with
  a downloadable text file.
- **Sefaria.** Born-digital texts with their section structure and an API. It holds many
  Hasidic classics but few of the genres that carry family detail: tales, letters, lineage
  books and biographies. Its vowel points were often added by a modern editor: treat a pointed
  spelling there as a hint, never as the historical spelling. Pin the text version you cite.
- **Lubavitch Library** (chabadlibrary.org). Searchable full text of Chabad books, including
  the Tzemach Tzedek's responsa. A responsa index of the rabbis who asked the questions,
  arranged by town, lists a town's rabbis.
- **National Library of Israel.** The book catalogue (many items can be read only in the
  library building), the archives records and the Ktiv manuscript portal. The archives records
  include the microfilms that the Central Archives for the History of the Jewish People, now
  part of the library, made in archives of the former Soviet Union. The search reads catalogue
  descriptions, not the files, and Hebrew, Latin and Cyrillic spellings return different sets.
- **Project Zikaron** (Touro University Libraries). Full text of yizkor books, pinkasim and
  memoirs, where town rabbis and their families often appear. Its terms forbid automated
  access, and a printed page number can differ from the image number.
- **Dynasty and community websites.** Each Hasidic group keeps its own sites with early
  editions, bulletins, memorial biographies and images of documents that the big libraries
  lack. Modern retyped editions carry new page numbers.
- **Rabbinic directories and dictionaries.** *Oholei Shem* (1912) lists the rabbis serving
  around 1912 by town, with birth and appointment years. *Da'at Kedoshim* (1897–1898) gives
  genealogies of rabbinic families. Yitzhak Alfasi's personalities volumes of the
  *Encyclopedia of Hasidism* are cited by volume and page or column as printed. N. Z.
  Friedman's *Otzar ha-Rabbanim* (1975) gives numbered entries for about 20,000 rabbis, and
  Meir Wunder's *Me'orei Galitsiyah* gives genealogies of Galician rabbinic families by
  surname. Coverage of small towns is uneven; check a directory's scope before reading its
  silence.
- **Lineage compilations (sifrei yichus).** Dynasty genealogies, descendant lists and large
  published genealogies such as Neil Rosenstein's *The Unbroken Chain*. Their prefaces often
  warn that the early generations are not verified, and some modern compilations cite online
  trees. Treat each early-generation link as a lead until a contemporary text supports it.
  When an online tree agrees with a published genealogy, check whether the tree copied it.
- **State archives of the Russian Empire.** Files on the election of crown rabbis (candidates,
  voter lists, signatures), prayer-house board elections with member lists and
  rabbinical-school records. JewishGen's index "Jewish Religious Personnel in the Russian
  Empire, 1853–1854" lists rabbis and synagogue officials by town. The crown rabbi held a state
  post; he was not necessarily the community's spiritual rabbi, and neither office stands in
  for the other.
- **Online trees and wikis.** Geni, Wikipedia and community wikis give leads only. Their
  child lists are assembled by editors, and many rabbinic descent profiles sit behind a login.

## 3. Fix the era, the place and the exact claim first

1. Ask when the person lived (within about 30 years), where, and exactly what is claimed: a
   rabbi in the family, descent from a named rebbe, a town office, or discipleship.
2. Walk the documented tree two or three generations up before searching. An identification
   needs era, region and at least one more identifying link that the passage also gives: a
   named relative (father, father-in-law, wife or brother) or an office held at a known date.
   A common given name alone, such as a father named Yaakov, is not enough.
3. Read the era markers that follow names. הי"ד marks a man killed as a martyr; ז"ל and זצ"ל
   mark a man dead when the text was written; שליט"א, שיחי' and תחי' mark a person alive then.
   A posthumous printing can add ז"ל, so the printing year does not date a death. When the
   passage's own date is known, such as a dated introduction, ז"ל shows the person was dead
   by then.
4. Check the geographic pool before counting hits. Hits for a surname often belong to
   Lithuanian or Galician families of the same name: in one study, 80 of 81 hits for a
   Ukrainian family's surname were such namesakes.

## 4. Collect the forms that the texts use

1. List every form actually seen for the person and for each place, in Hebrew, Yiddish,
   Russian and Latin script, with where each was seen. Keep the user's spelling as a literal
   input; do not correct it silently.
2. Add the sacred and everyday given-name pairs: Tzvi and Hirsh, Aryeh and Leib, Dov and
   Ber, Ze'ev and Wolf, Naftali and Hirsh, Yehudah and Leib, Shlomo and Zalman.
3. Search Yiddish and Hebrew spellings of a place as separate queries. Breslov books write
   Uman as אומין far more often than אומן. On Otzar HaHochma, one town's Yiddish spelling
   returned five hits in four books where its Hebrew spelling returned none.
4. Find the spellings no one would guess from the texts themselves. A sweep for a
   distinctive letter pair, such as טש, surfaced קרימינטשאק for Kremenchug.
5. Keep a table of each spelling and its hit count. A missing form looks exactly like a
   missing person.

## 5. Match Hebrew text the way it is printed

- **Vowel points.** Remove them from both the text and the query. The points belong to one
  edition, not to the work.
- **Prefix letters.** Allow up to three attached prefixes (ו ב כ ל מ ש ה) at the start of a
  word only, and still require the word to end where the name ends. In some books a town name
  occurs only with a prefix, never bare.
- **Stems.** A final letter becomes a medial letter before a suffix, so חותן never matches
  חותנו. Search the stem חותנ.
- **Full and defective spelling.** Search both, for example קודש and קדש.
- **Acronyms.** Texts print them with Hebrew gershayim and geresh (״ ׳) or with ASCII quotes
  (" '). Search every form.
- **Whole words.** As a substring, הרב also matches הרבה, and ז"ל also matches inside חז"ל
  and וז"ל. Print the distinct forms that matched before you count.
- **OCR damage.** Expect letters of similar shape to be swapped (ד and ר, ב and כ, ו and י
  and ן, ט and ס), and words split by spaces. A swapped letter often still makes a real word.
- **Who finds the forms.** No one can read a whole library. Search the libraries to choose
  books, have a language model read the chosen books in full to find forms and kinship
  phrases, then search again with the forms found. Use exact-string tools only to check forms
  already found. A closed keyword list reported no candidates in hundreds of sections that a
  full reading then mined.

## 6. Search by office, place and relation, not by surname

1. Build queries from office and town (רב, אב"ד, מ"ץ followed by the town), given name with
   patronymic, given name with a town epithet, and relation phrases. Search relation phrases
   in both word orders, with stems such as חתנ (son-in-law), חותנ (father-in-law), גיס
   (brother-in-law), מחותנ (co-father-in-law), and phrases such as "X אחיו" or "X אשתו".
2. For a half-remembered name, search by attribute (סופר, שוחט, a town office) and test each
   candidate against the remembered fragment. A surname that looks like a trade can still be
   inherited.
3. Search every surname and place from the documented tree, not only the line the family
   remembers. Searching only the known names can confirm the known, never reveal the unknown.
4. Record the query, scope, settings, date and count for every search. On Otzar HaHochma,
   search the books' content (חפש בתוכן הספרים) across all books (בכל הספרים), note whether
   word adjacency (הצמדת מילים) and prefix letters (אותיות שימוש) are switched on, and wait
   until the result list refreshes. Only an explicit "no results" is a zero. Do not carry
   HebrewBooks' Boolean or proximity syntax over to Otzar HaHochma untested.
5. On HebrewBooks' advanced OCR search, choose the Boolean mode for AND, OR, NOT,
   parentheses, quoted phrases and proximity (`w/N`), and run a query you know has hits as a
   control.

## 7. Read the subject's own books and the front matter first

1. Read in this order:
   1. the subject's own book: title page ("X son of Y, av beit din of Z, author of …"),
      introduction and autobiographical passages;
   2. a relative's memoir or preface;
   3. approbations, subscriber lists, letters, testaments and appendices printed in other
      books;
   4. passing citations in other books, which usually give only an epithet;
   5. online summaries.
2. Read responsa headers. They name the addressee, often with his father and origin
   (מילידי X, "native of X"). A phrase such as "living in X" (יושב ב־X) describes a scholar
   resident in X, not the appointed town rabbi.
3. Let the genre set the order, never the verdict. Hasidic tale and oral-history anthologies
   yield the most family links, but as tradition: rank them below letters, title pages and
   documents. The body of a halakhic work yields few links. A halakhic book's
   front matter can still name the family, so sample it before deferring the book, and never
   write "no yield" from the genre alone.
4. Use finding aids to reach pages; they are not evidence. *Oholei Shem* gives a rabbi's
   appointment year, which is not his predecessor's death year. Berl Kagan's index of
   subscriber lists (*Sefer ha-prenumerantn*) names the books that printed subscribers from a
   town; read those lists next. A book's printed name and place indexes, read on the page
   image, find more than its OCR text does.
5. A town that appears inside a title ("the Rav of X") is often missing from a place index or
   indexed only under the person. Search both the place and the person indexes, and walk the
   chapters indexed under the person's relatives, teachers and in-laws.

## 8. Screen every hit before it becomes a person

- **Words that are not names.** Given names inside book titles (*Gur Aryeh*, *Torat Chaim*),
  Hebrew-letter numbers that read as words, חיים as "life", ישראל as the people or the land,
  and works such as *Avot de-Rabbi Natan*. Report raw hits, then filtered hits, then
  substantive hits.
- **The same name, a different man.** Compare era, town, father and in-laws for every
  candidate. "The Rav of X" can be two men a few sections apart. Two 19th-century Breslov
  figures, R. Nachman of Tulchin and R. Nachman of Tcherin, are repeatedly merged in trees
  and in machine-built indexes. Key people by identity, never by spelling.
- **Namesake chains.** "X son of Y son of X" is usually a grandson named after his
  grandfather: number them X-1 and X-2. Ashkenazi children were named after the dead, so a
  candidate grandfather who was alive at a child's birth is an unlikely namesake source.
- **Titles.** "Rav" can mean a teacher or the formal av beit din. A dayan is a judge; a moreh
  tzedek is a halakhic authority and, in some communities such as Minsk, the leading rabbi.
  Later writers promote titles. Do not call a man av beit din unless a passage does, and judge
  a missing אב"ד against how that community titled its rabbis.
- **Honorifics are not offices.** מו"ה, מוהר"ר, הר"ר and הרבני were given to learned laymen
  and ordinary householders in subscriber lists, letters and epitaphs, and ר' (Reb) to almost
  any adult man. They are a frequent source of a "rabbi in the family" story.
- **Kinship words that move a generation.** חותן (father-in-law) differs from חתן
  (son-in-law) by one letter. א"א usually means "my father" (אדוני אבי); זקני and אבי זקני
  mean a grandfather or a more remote ancestor. נכד can be any descendant, not only a
  grandchild, and בן can mean a disciple. "My brother" can be an honorific in a letter.
  "X Sarah's" can mean Sarah's husband or her son. בתו השניה is a second daughter, not a
  second wife. A מחותן is a co-father-in-law, not a blood relative.
- **Places.** In a list of names, a town epithet can belong to the preceding or the following
  name; settle which from another passage before you assign the place. An index gloss can
  move a place hundreds of kilometres: read the preposition in the original (שליד, "near").
  Two places can share a spelling, such as Bratslav in Podolia and Braslaw in Belarus.
- **Dates.** Convert a Hebrew date through its month or weekly Torah portion, never the year
  alone, because a Hebrew year spans two civil years. Title pages often give the year as a
  chronogram, a phrase whose marked letters add up to the year, and omit the thousands
  (לפ"ק, "by the small count"). For a letter dated by a fast or festival, check the weekday:
  the Fast of Esther moves to 11 Adar when 13 Adar falls on Shabbat. Identify the calendar
  before converting a Russian-Empire date, because Russian-Polish acts can give both Julian
  and Gregorian dates. Add 12 days to a Julian date from 1 March 1800 to 28 February 1900,
  and 13 days from 1 March 1900 until the 1918 change. A book's printing year is not the date
  of a letter printed in it.

## 9. Count witnesses, not copies

- Treat these as one witness: reprints; a new OCR of the same scan; a translation (where a
  translator expands an acronym into a name, that is the translator's reading); Hebrew and
  Yiddish versions of one talk; one story repeated across volumes of an anthology; and
  compilations that copy the same testament or pedigree letter.
- A book that cites an online tree is circular when you compare it with that tree.
- Carry a compiler's doubt words into your notes verbatim: אולי (perhaps), כנראה
  (apparently), יש אומרים (some say), כן שמעתי (so I heard). Classify each compiled claim as
  a statement, a hypothesis, hearsay or a disagreement, and check that its footnote really
  belongs to it.
- Online trees: child lists are incomplete, profile titles can be wrong, and a managed
  profile repeats its manager's tree. Absence there disproves nothing.
- Check every book ID or catalogue number supplied by a language model against the title on
  the library's own page before you use it.

## 10. Test a lineage tradition before searching for a bloodline

1. Ask "through whom?". Look for discipleship wording ("drew close to", "was among the
   followers of") as well as kinship wording.
2. Separate four claims: direct descent in the male line, descent through a woman,
   collateral kinship, and marriage into the rebbe's household. A rebbe's in-law (mechutan)
   is not his descendant; find which child married into the court.
3. Kohen and Levi status passes from father to son. A Kohen or Levi family cannot descend in
   the male line from a non-priestly dynasty, and a non-priestly family cannot descend in the
   male line from a Kohen or Levi; any such link runs through a marriage or a mother. Look for
   the HaKohen, HaLevi, Katz or Segal signature on title pages and epitaphs.
4. A prestige rabbinic surname (Horowitz, Rapoport, Shapiro, Margolis, Landau) is carried by
   unrelated families, so a surname match is not a lineage lead. Children were also named
   after a rebbe as a sign of following, not descent. Treat stock chains back to Rashi or
   King David as tradition unless each link is documented.
5. A famous lineage cannot replace a missing parent–child link. A claim of descent through a
   famous rabbi's daughter does not pass to an archival woman whose mother is not named.
6. Keep two questions apart: did the ancestor exist, and is the bridge from your person to
   that ancestor documented? Rabbinic books often answer the first and rarely prove the
   second. For writing the competing versions, use
   [Jewish genealogy conditional hypotheses](jewish-genealogy-conditional-hypotheses.md); for
   the final judgment, use [evidence and proof judgment](evidence-proof-judgment.md).

## 11. Record locators and limit every negative

1. Record the book ID, edition, viewer image number and printed page or siman separately.
   Numbering can restart inside one binding, the offset between image and printed page can
   change within a book, and a jump in the viewer leaves pages unread. Cite the library's
   permanent link, never a temporary download address.
2. A zero covers only the surfaces, spellings and pages actually searched. An access error,
   a result cap, an unsubmitted query, a partial run, a genre that would not record the fact
   and an unreadable book are not negatives.
3. Print the spellings that matched beside every count, and run a known-present control.
4. Treat a confidence label from any language-model reader as a lead until you have read the
   passage yourself.

## Output: a passage ledger

| Field | Content |
| --- | --- |
| Form | The literal form in the text, with its prefix |
| Source | Book, edition, library and ID |
| Locator | Viewer image, printed page or folio, siman or section |
| Text | The quoted words that name the person and each relation |
| Reading | Stated or inferred; office; place; era marker |
| Witness group | The earliest text this one depends on |
| Next check | The passage or record that would confirm or refute it |

## Prompt patterns

- **Forms:** "From these passages, list every form of [person or place] with its locator. Do
  not normalize spellings. Show prefixed and bare forms separately."
- **Screen a hit:** "Read this Hebrew passage. Who is named, with which title, patronymic,
  town and relation? Quote the words that state each relation, and mark each item as stated
  or inferred."
- **Tradition:** "The family says [claim]. State it as male-line descent, descent through a
  woman, collateral kinship, marriage or discipleship. For each reading, name the passage
  that would confirm or refute it."
- **Witnesses:** "These sources state [fact]. Group them by the earliest text each depends
  on."

## Failure modes

- Searching a civil surname and reporting the person absent from rabbinic literature.
- Merging two men who share a name and title, or splitting one man by spelling.
- Reading discipleship, a court's following or a marriage into the household as descent.
- Treating an index entry, an OCR hit, a catalogue record or a translation as the text.
- Counting a reprint, a translation or a compilation as an independent witness.
- Reading חותן as חתן, or an honorific "brother" as a sibling.
- Reading an honorific such as מו"ה or הר"ר as proof of a rabbinic office.
- Dating a letter by the book's printing year, or converting a Hebrew year without its month.
- Reporting a capped, blocked or partial search as a zero.
