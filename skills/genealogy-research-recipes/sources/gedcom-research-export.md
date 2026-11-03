## Sources

- **S1:** FamilySearch, [The FamilySearch GEDCOM Specification](https://gedcom.io/specifications/FamilySearchGEDCOMv7.html) (version 7.0.18, 17 February 2026), opened 2026-11-02. Used for:
  - GEDCOM as a format for transmitting and storing genealogical data
  - UTF-8 as the only character set, the removal of `CONC`, and `HEAD.SCHMA` for documented extension tags
  - the calendar keywords, the Gregorian default, and `@#D` escapes as dates in versions 4.0 to 5.5.1
  - the date modifiers `ABT`, `CAL`, `EST`, `BEF`, `AFT` and `BET … AND`
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

**What is authored synthesis:** the decision order, the version checklist, the one-parent family rule as written here, the status-in-NOTE rule, the import rules and the export packet are this recipe's own. The sources supply the specification facts (S1, S2, S4–S8) and the vendor default (S3).

## Credits

- Kinprove original procedural synthesis, with facts checked against the FamilySearch GEDCOM 7.0 specification and the gedcom.io specifications index, a Chronoplex Software blog post, the GEDCOM 5.5.1 standard with inline errata, the ged4py documentation, a Tamura Jones article, the gedcom Ruby gem documentation and the gedcomkit source cited as S1 to S8 — FSL-1.1-MIT (kinprove-original)
