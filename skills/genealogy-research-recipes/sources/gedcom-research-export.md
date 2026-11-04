## Sources

- **S1:** FamilySearch, [The FamilySearch GEDCOM Specification](https://gedcom.io/specifications/FamilySearchGEDCOMv7.html) (version 7.0.18, 17 February 2026), opened 2026-11-02. Used for:
  - GEDCOM as a format for transmitting and storing genealogical data
  - UTF-8 as the only character set, the removal of `CONC`, and `HEAD.SCHMA` for documented extension tags
  - the calendar keywords, the Gregorian default, and `@#D` escapes as dates in versions 4.0 to 5.5.1
  - the date modifiers `ABT`, `CAL`, `EST`, `BEF`, `AFT` and `BET … AND`
  - the year as a plain integer, and the PHRASE examples for a 1648/9 dual year (opened 2026-11-04)
  - earlier versions allowing several character encodings with ANSEL as the default (opened 2026-11-04)
  - `@` doubled only at the start of a line string in 7.0 against every `@` in earlier versions, the cross-reference ID grammar, and date phrases moved from the 5.5.1 date value to PHRASE (opened 2026-11-04)
  - HUSB and WIFE as optional in a FAM record, and not inferring a partner's sex or role from them
  - PAGE as the location within the source
  - QUAY and its values
  - pointers that must resolve within the file, and `@VOID@` as the null pointer
- **S2:** FamilySearch, [GEDCOM specifications](https://gedcom.io/specs/), opened 2026-11-02. Used for the official specification of each version, and for 5.5 and 5.5.1 being still in use in the marketplace.
- **S3:** Chronoplex Software, [Blog archive 2021](https://chronoplexsoftware.com/blog/archive/2021.htm), opened 2026-11-02. Used for a vendor's 2021 announcement that its export would default to 5.5.1 until 7.0 is in widespread use.
- **S4:** FamilySearch, [The GEDCOM Standard, Release 5.5.1, with inline errata](https://gedcom.io/specifications/ged551-with-inline-errata.html) (15 November 2019), opened 2026-11-02. Used for `UTF-8` among the 5.5.1 character sets, HUSB and WIFE as optional ({0:1}) in the 5.5.1 FAM record, the 5.5.1 assumption that HUSB is male and WIFE is female, and `@#DJULIAN@` as a 5.5.1 calendar escape.
- **S5:** ged4py documentation, [Technical information](https://ged4py.readthedocs.io/en/latest/techinfo.html), opened 2026-11-02. Used for UTF-8 as a permitted 5.5.1 character set.
- **S6:** Tamura Jones, [Same-Sex Marriage in GEDCOM](https://www.tamurajones.net/SameSexMarriageInGEDCOM.xhtml), opened 2026-11-02. Used for HUSB and WIFE as optional ({0:1}) in the 5.5.1 FAM record.
- **S7:** gedcom Ruby gem documentation, [Date_record](https://www.rubydoc.info/gems/gedcom/Date_record), opened 2026-11-02. Used for the 5.5.1 calendar escapes, including `@#DJULIAN@`.
- **S8:** gedcomkit 0.1.3 source, [dates.rs](https://docs.rs/crate/gedcomkit/0.1.3/source/src/dates.rs), opened 2026-11-02. Used for the `@#DJULIAN@` form of a 5.5.1 date.
- **S9:** legislation.gov.uk, [Calendar (New Style) Act 1750, introductory text](https://www.legislation.gov.uk/apgb/Geo2/24/23/introduction), opened 2026-11-04. Used for the English year beginning on 25 March before the Act, and the change to 1 January from 1752 across the Crown's dominions, America included.
- **S10:** National Records of Scotland, ScotlandsPeople, [Dates](https://www.scotlandspeople.gov.uk/scottish-handwriting/coaching/numbers/dates), opened 2026-11-04. Used for Scotland's year beginning on 1 January from 1600, and the rest of the British Isles keeping 25 March until 1 January 1752.
- **S11:** Familio, [GEDCOM import help](https://services.familio.org/gedcom), opened 2026-11-04. Used for a re-import always fully replacing person pages, the new file replacing the old one, and manual edits on Familio being lost. Platform behaviour on that date.

**What is authored synthesis:** the decision order, the version checklist, the one-parent family rule as written here, the status-in-NOTE rule, the import rules, the decode-then-relink-then-deduplicate order, the test-tree rule and the export packet are this recipe's own. The sources supply the specification facts (S1, S2, S4–S8), the vendor default (S3), the year-start dates (S9, S10) and the re-import behaviour (S11).

## Credits

- Kinprove original procedural synthesis, with facts checked against the FamilySearch GEDCOM 7.0 specification and the gedcom.io specifications index, a Chronoplex Software blog post, the GEDCOM 5.5.1 standard with inline errata, the ged4py documentation, a Tamura Jones article, the gedcom Ruby gem documentation, the gedcomkit source, the Calendar (New Style) Act 1750, a ScotlandsPeople guide and Familio's GEDCOM help cited as S1 to S11 — FSL-1.1-MIT (kinprove-original)
