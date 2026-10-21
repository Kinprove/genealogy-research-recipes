## Sources (provenance + dates)

> Original Kinprove synthesis. Third-party passages are not reproduced.

Primary documentation opened and checked 2026-10-18. Public documentation confirms
the described scope; it does not verify a signed-in account or every kit generation.

- **H1:** MyHeritage, [DNA Results And Filtering Your DNA Matches](https://education.myheritage.com/article/dna-results-and-filtering-your-dna-matches/),
  sections on searching and filters. The search can target the match's name or an
  ancestral surname. It does not establish the tested person's identity from a hit.
- **H2:** GEDmatch / Andy Lee, [An overview of DNA comparison matrices in Multiple Kit Analysis](https://www.gedmatch.com/education/an-overview-of-dna-comparison-matrices-in-multiple-kit-analysis/),
  approximately 05:52–06:58. The overlap matrix reports common SNP counts for a kit
  pair; no universal minimum local support is supplied by this citation.
- **H3:** FamilyTreeDNA, [Family Finder Matching 5.0 white paper](https://blog.familytreedna.com/wp-content/uploads/2021/08/Family_Finder_Matching_WhitePaper.pdf),
  2021, printed pp. 5–6, matching workflow. Describes chip-set imputation, no-call
  handling, adjacent-segment joining, cM mapping and filtering. It documents that
  method, not every later algorithm version or the cause of an individual discrepancy.
- **H4:** Genome Reference Consortium, [Human Genome Overview](https://www.ncbi.nlm.nih.gov/grc/human),
  GRCh37 and GRCh38 pseudoautosomal-region tables. Coordinates must be interpreted
  against the input's assembly; the recipe intentionally delegates boundary lookup.
- **H5:** MyHeritage Help, [How do I use the Chromosome Browser for shared DNA segments on the MyHeritage app?](https://www.myheritage.com/help/en/articles/12852203-how-do-i-use-the-chromosome-browser-for-shared-dna-segments-on-the-myheritage-app),
  dated 2026-07-21. Describes the app browser's autosomal scope and separately
  distinguishes unsampled markers. No inference about all raw downloads is made.
- **H6:** FamilyTreeDNA Help, [X-Matches](https://help.familytreedna.com/hc/en-us/articles/9134064538895-X-Matches),
  section “Measuring X matches.” List admission requires autosomal qualification;
  X sharing is separate from overall shared cM in that documented list.
- **P1:** Page et al., [Linkage, Physical Mapping, and DNA Sequence Analysis of Pseudoautosomal Loci on the Human X and Y Chromosomes](https://www.pagelab.wi.mit.edu/_files/ugd/8c39a0_415339fd6f6c47728f70d505ae078a55.pdf),
  *Genomics* 1 (1987), 243–256, DOI 10.1016/0888-7543(87)90051-6; author-hosted full
  paper, abstract and introduction. Demonstrates male X–Y recombination and
  inheritance in the pseudoautosomal region. No contemporary array or match-rate
  claim is taken from this historical study.
- **H7:** Family History Fanatics, [The Debate Continues Over Usefulness of Small cM DNA Matches](https://www.youtube.com/watch?v=ZqK9b2Vt6gQ),
  published 2022-04-27. Used for running known-unrelated pairs at the same lowered
  segment threshold as a negative control; the reported true-segment percentages are not
  adopted.
- **H8:** GeneaVlogger with Cairenn Binder, [The Impact of Ancestry's Ban on Forensic Genealogy | Discussion with Cairenn Binder](https://www.youtube.com/watch?v=3xodviufcG4),
  published 2025-11-22. Used for the practice of recording a degraded kit's call rate and
  checking the SNPs read within a segment before trusting a match; the call-rate figures
  and the unnamed study are not adopted.
- **H9:** Family History Fanatics, [Heirloom DNA For Genealogy Sounds Amazing… Until You See This Problem](https://www.youtube.com/watch?v=lMnm4UjIO60),
  published 2026-04-22. Used for the point that coverage gaps in a sparse heirloom kit can
  split or merge segments, which makes the reported cM unreliable; the presenter's
  illustrative ranges are not adopted.
- **H10:** Lisa Lisson with Mary, [Ask Mary Your DNA Questions!](https://www.youtube.com/watch?v=ecwbM9Lc-Gg),
  published 2021-03-12. Used for recomputing a match total from the segment export at a
  common minimum before comparing vendors.
- **H11:** GeneaVlogger, [Answering Live Genealogy and DNA Test Questions](https://www.youtube.com/watch?v=W278DGiDKq0),
  published 2025-07-12. Used for the point that a low minimum for later segments raises a
  vendor's totals; the charted threshold values are not adopted.
- **H12:** GenArchivist Forum, [The quality is deteriorating - 435k vs 677k snps](https://genarchivist.net/showthread.php?tid=2449),
  first post 2026-03-13; [Y and X SNPs missing in new myHeritage raw data?](https://genarchivist.net/showthread.php?tid=1739),
  first post undated; [MyHeritage upgrades its consumer DNA test to whole-genome sequencing](https://genarchivist.net/showthread.php?tid=1999),
  first post undated; [Additional lines/rsids in 23andMe raw data file](https://genarchivist.net/showthread.php?tid=729),
  first post 2024-04-14. Rights: cited reference, not reproduced. Used for inventorying each
  raw file by download date, header and per-chromosome counts, for comparing two files' SNP sets
  and no-calls directly because the same format label covered different marker sets, and for
  keeping file counts separate from a tool's usable counts; reported vendor policies are not
  adopted.
- **H13:** GenArchivist Forum, [FTDNA is updating Family Finder](https://genarchivist.net/showthread.php?tid=2412),
  first post 2026-02-24. Rights: cited reference, not reproduced. Used for recording the assay
  generation of each file; the reported batch and date cutoffs are not adopted.
- **H14:** МолГен forum, [WGSExtract, FASTQ и разные референсные геномы](https://forum.molgen.org/index.php/topic,14971.0.html),
  first post 2023-09-09. Rights: cited reference, not reproduced. Used for building a
  WGS-derived comparison file in the comparison data's reference build instead of lifting
  coordinates over, and for screening a derived file's summary statistics (no-call share,
  heterozygosity) before treating it as comparison input; the posters' figures and causal
  hypotheses are not adopted.
- **H15:** GenArchivist Forum, [Sampling by Country for YFull and FTDNA](https://genarchivist.net/showthread.php?tid=106),
  first post undated. Rights: cited reference, not reproduced. Used for treating excess
  heterozygosity, sex-chromosome calls inconsistent with known sex, and implausible matches to
  known samples as signs of a bad sequencing-derived file.
- **H16:** GenArchivist Forum, [Dante's hell](https://genarchivist.net/showthread.php?tid=1345),
  first post 2024-12-21. Rights: cited reference, not reproduced. Used for the point that a
  variant-only VCF yields limited chip-format data and that a BAM rebuilt from a VCF adds no
  coverage, so BAM/CRAM is the conversion source.
- **H17:** GenArchivist Forum, [MyHeritage Update June 2024](https://genarchivist.net/showthread.php?tid=939),
  first post 2024-06-27. Rights: cited reference, not reproduced. Used for converting a WGS BAM
  to a chip-format raw file before upload, which makes the uploaded kit a derived input.
- **H18:** МолГен forum, [GEDmatch Genesis](https://forum.molgen.org/index.php/topic,10116.0.html),
  first post 2017-06-22. Rights: cited reference, not reproduced. Used for keeping one match's
  several platform kits as separate rows with their compared-SNP overlap; the poster's causal
  explanation is not adopted.
- **H19:** МолГен forum, [LivingDNA](https://forum.molgen.org/index.php/topic,10423.0.html),
  first post 2017-10-27. Rights: cited reference, not reproduced. Used for recording
  self-conversion and receiving-site imputation per kit when one match's total differs widely
  between services; the chip SNP counts and imputation confidences are not adopted.
- **H20:** GenArchivist Forum, [Timber is deeply, deeply flawed](https://genarchivist.net/showthread.php?tid=137),
  first post undated. Rights: cited reference, not reproduced. Used for comparing another
  vendor's total with Ancestry's unweighted figure rather than its Timber-adjusted total.
- **H21:** GenArchivist Forum, [Multiple AncestryDNA Tests](https://genarchivist.net/showthread.php?tid=905),
  first post 2024-06-17. Rights: cited reference, not reproduced. Used for treating a direct
  comparison in another tool, made when an Ancestry match is missing or reduced, as a separate
  measurement.

## Synthesis boundaries

The exact-test registry, known-positive query check, result-status table, local
coverage requirement and reciprocal-row reconciliation are original methodological
synthesis. The sources establish concrete measurement limitations; none supplies a
universal “good overlap,” sensitivity threshold, relationship ceiling or error rate.
An operational control checks the operation and scope exercised, not all claims
about the tested person. No family data, private kit identifiers or account findings
are part of this recipe.

## Credits

- Kinprove — original distillation and synthesis — FSL-1.1-MIT (kinprove-original)
