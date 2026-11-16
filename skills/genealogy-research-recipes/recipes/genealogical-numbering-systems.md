---
id: "genealogical-numbering-systems"
title: "Decode Ahnentafel, Henry, Register and NGSQ numbers in charts and compiled genealogies"
summary: "Decode Ahnentafel, Henry, Register and NGSQ numbers when extracting people and relationships from a pedigree chart, descendancy list or compiled genealogy."
kind: "judgment"
scope: {"platforms": [], "tasks": ["read a Register-format or NGSQ-format published genealogy", "find parents, child or generation from an ahnentafel number", "split given names from surname at a generation superscript"]}
privacy: "none"
gates: []
guardrails: [{"id": "GENEALOGICAL-NUMBERING-SYSTEMS-01", "text": "Find the compiler's key or introduction and name the system before decoding a single number."}, {"id": "GENEALOGICAL-NUMBERING-SYSTEMS-02", "text": "Take person 1's sex from the records, not from the number."}, {"id": "GENEALOGICAL-NUMBERING-SYSTEMS-03", "text": "Read 11 as two positions, one and one, never as eleven."}, {"id": "GENEALOGICAL-NUMBERING-SYSTEMS-04", "text": "Never decode a letter or bracket in a Henry number until the document's key says which child position it stands for."}, {"id": "GENEALOGICAL-NUMBERING-SYSTEMS-05", "text": "Do not read a child without an identification number as childless or as dying young."}, {"id": "GENEALOGICAL-NUMBERING-SYSTEMS-06", "text": "So decide continuation by the plus sign, never by the presence of a number."}]
handoff: ["published-book-catalogue-and-full-text-discovery", "ydna-mtdna-interpretation", "evidence-proof-judgment"]
checked: null
checked_basis: null
capabilities: {"browse": [], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"section": "Research method", "group": "Family trees and research planning", "order": 15}
---

# Decode Ahnentafel, Henry, Register and NGSQ numbers in charts and compiled genealogies

Use this recipe when you extract people and relationships from an ahnentafel (ancestor) list, a Henry- or d'Aboville-numbered descendancy list, or a compiled genealogy in Register or NGSQ format. Each system encodes kinship and generation in the numbers themselves, and a wrong decoding attaches children to the wrong parents. Decode every number under the system the document uses, and keep each decoded relationship as the compiler's statement, not as proof.

To find the compiled genealogy or periodical article, use [published book catalogue and full-text discovery](published-book-catalogue-and-full-text-discovery.md). For a DNA test along a direct line, use [Y-DNA and mtDNA interpretation](ydna-mtdna-interpretation.md). To judge whether a compiler's relationship holds, use [evidence/proof judgment](evidence-proof-judgment.md).

## Contents

- What goes wrong
- 1\. Name the system before decoding
- 2\. Ahnentafel: parents, child, generation and direct lines
- 3\. Henry and d'Aboville: count positions, not digits
- 4\. Register: follow identification numbers to full entries
- 5\. NGSQ: decide continuation by the plus sign
- 6\. Split given names from surname at the generation superscript
- Return packet

## What goes wrong

- Reading Henry number 11 as eleven. Each position after the first is a child's birth position, so 11 is the progenitor's first child. [S2]
- Giving person 1 in an ahnentafel a sex from the number. Person 1 is the subject, male or female; the even-male, odd-female pattern starts at 2. [S3], [S6]
- Treating every even-numbered ancestor as being on the father's side. The mother's side has men too, and they carry even numbers. [S6]
- Reading a letter or parenthesis in a Henry number without the document's key. Henry's own scheme and Modified Henry write the tenth child differently. [S2]
- Reading a Register child without an identification number as childless. The number marks a child treated in full later, usually one with offspring. [S4], [S2]
- Following every numbered child forward in an NGSQ genealogy. Every child has a number; the plus sign marks the ones with a later entry. [S2], [S3]
- Counting a superscript generation number from the person you are researching. It counts from the publication's own first generation. [S5]

## 1. Name the system before decoding

Find the compiler's key or introduction and name the system before decoding a single number. Ahnentafel numbers ancestors upward from one subject; Henry, d'Aboville, Register and NGSQ number descendants downward from a progenitor. [S2] Register and NGSQ look alike on the page but differ in which children receive Arabic numbers (§4, §5). [S2] Record the system and the page of its key in the extraction, and decode by that key rather than by the system's name, because the schemes handle large families differently (§3).

## 2. Ahnentafel: parents, child, generation and direct lines

- Person 1 is the subject, male or female. For any person n, the father is 2n and the mother is 2n + 1. [S3], [S6], [S2]
- Every number from 2 up is therefore male if even and female if odd. Take person 1's sex from the records, not from the number. [S3], [S6]
- By the same rule, person n's child in the chart is n divided by 2, rounded down. Each generation starts at a power of two: the parents are 2 and 3, the grandparents 4 to 7, the great-grandparents 8 to 15. This arithmetic is the recipe's own.
- To read a long number as a path, write it in binary, drop the leading 1 and read the remaining digits from the subject upward: 0 is a father, 1 is a mother. Tree & Leaf's example 116 (binary 1110100) is the subject's mother's mother's father's mother's father's father. [S3]
- The direct paternal line is 2, 4, 8, 16 and so on, the powers of two. [S6] By the same rule, the direct maternal line is 3, 7, 15, 31.
- Even numbers do not mark the paternal side. That side is 2 and all of 2's ancestors, and the maternal side is 3 and all of 3's ancestors, with men and women on each. [S6]

The paternal line 2, 4, 8, 16 is the line a Y-DNA test follows: men inherit the Y chromosome from their fathers, so person 1 carries it only if male. [S7] Take any test or match question to [Y-DNA and mtDNA interpretation](ydna-mtdna-interpretation.md).

The Just Genealogy presenter reports the father-is-2 numbering and the 1, 2, 4, 8, 16 line as the Y-DNA line [S1†].

## 3. Henry and d'Aboville: count positions, not digits

Henry numbering gives the progenitor 1 and each child the parent's number followed by one more position for birth order: 11 is the progenitor's first child, 12 the second, and 112 the first child's second child. [S2] Read 11 as two positions, one and one, never as eleven. The number of positions is the generation, counting the progenitor as 1, so 112 is in the third generation.

Positions past nine differ by scheme. In Henry's own scheme the tenth child is X, the eleventh A and the twelfth B; Modified Henry puts the position in parentheses, so the tenth child of 12 is 12(10) rather than 12X. [S2] Count a parenthesized group as one position. d'Aboville numbering separates generations with periods, so count the period-separated segments instead. [S2] Never decode a letter or bracket in a Henry number until the document's key says which child position it stands for.

The Just Genealogy presenter reports the same reading of 11 and 112 with the digit count as the generation, and reports a working-paper extension under the Modified Henry name that continues past nine with letters [S1†].

## 4. Register: follow identification numbers to full entries

In Register format each child in a family's list has a lowercase Roman numeral for birth order. A child who will be treated in full later, usually one with offspring, also has an Arabic identification number before the numeral, and that number heads the child's own entry in the next generation. [S4], [S2]

- Follow each identification number to its entry, and attach the spouse, children and dates found there to the same person.
- Do not read a child without an identification number as childless or as dying young. The number marks who is carried forward; a child without one has no known progeny or is simply not treated further. [S4], [S2], [S8]

The Just Genealogy presenter reports the identification number as the pointer to the entry carried forward elsewhere in the publication, and numbering only the people carried forward as the key to the format [S1†].

## 5. NGSQ: decide continuation by the plus sign

The NGSQ system, also called the Record or Modified Register system, gives every child an Arabic number whether or not the child is known to have progeny. [S2], [S8] A plus sign before a child's number marks a child with a fuller entry further on. [S3] So decide continuation by the plus sign, never by the presence of a number. For a child without a plus sign, the parent's child list is the whole treatment; do not search the genealogy for a later entry.

The Just Genealogy presenter reports that NGSQ numbering gives everybody a number and that the plus sign determines who moves forward [S1†].

## 6. Split given names from surname at the generation superscript

In NEHGS-style genealogies the superscript generation number follows the given names and precedes the surname, as in Christopher Challender⁶ Child, and a parenthetical list after the name gives the ancestors back to generation 1, each with a superscript. [S5], [S3] Treat the words before the superscript as given names and those after it as the surname, even when the surname has more than one word. Published genealogies differ in where the superscript sits relative to the surname, so confirm the placement on an entry whose names you already know before splitting names across a whole publication. [S5]

Read a superscript against the publication's own generation 1, not against the person you are researching. Child, for example, numbers the first generation living in the United States as 1 and marks earlier, non-emigrant generations with letters, A being the immigrant's father. [S5]

The Just Genealogy presenter reports placing a number between the given names and the surname to tell surnames, including unhyphenated ones, from other names [S1†].

## Return packet

- The system name and the page of the key for each document.
- One row per numbered person: the number exactly as printed (with any plus sign, Roman numeral or superscript), the decoded relationship and generation, the page of the person's full entry if any, and the split between given names and surname.
- Each decoded relationship labelled as the compiler's statement, for testing under [evidence/proof judgment](evidence-proof-judgment.md).
- Explicit gaps: no key found, unresolved positions past nine, children not carried forward, superscript placement not confirmed.
