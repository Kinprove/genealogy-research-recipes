"""Sources numbering is contiguous, and every bracketed citation in a recipe has an entry."""

import re
import unittest
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills/genealogy-research-recipes"
RECIPES = SKILL_DIR / "recipes"
SOURCES = SKILL_DIR / "sources"

ID = r"([A-Z]{1,2})(\d+)(?:[–-]([A-Z]{1,2})?(\d+))?"
# "- **S12:** ...", "- **S12.** ...", "- **H1–H4:** ..." or a support-table row "| S12 | ...".
ENTRY = re.compile(rf"^(?:- \*\*{ID}[:.]|\| {ID} \|)", re.MULTILINE)
PLACEHOLDER = "No entry; this number is not cited by the recipe."
# A bracket that opens with a source ID (or ID range) followed by ",", ";", "]" or a page
# marker: [S3], [S1, H2], [S4–S6], [S3 p. 1], [S3 pp. 10, 14], [H2; interpretation of the
# form]. An ID followed by plain words, such as the haplogroup in "[D0 dating comparison]",
# is not a citation.
CITATION = re.compile(r"\[([A-Z]{1,2}\d+(?:[–-][A-Z]{0,2}\d+)?(?=[,;\]]|\s+pp?\.\s)[^\[\]]*)\]")
# Each comma- or semicolon-separated part that starts with an ID; page numbers and
# annotations after the ID are ignored.
CITED_ID = re.compile(r"^([A-Z]{1,2})(\d+)(?:[–-]([A-Z]{0,2})(\d+))?(?![\w])")


def expand(series, first, last):
    return {(series, number) for number in range(int(first), int(last or first) + 1)}


def entries(text):
    """Return ({(series, number)}, {placeholder ids}) for a sources file."""
    found = set()
    placeholders = set()
    for line in text.splitlines():
        match = ENTRY.match(line)
        if not match:
            continue
        groups = match.groups()
        series, first, _, last = groups[:4] if groups[0] else groups[4:]
        ids = expand(series, first, last)
        found |= ids
        if PLACEHOLDER in line:
            placeholders |= ids
    return found, placeholders


def citations(text):
    cited = set()
    for match in CITATION.finditer(text):
        for part in re.split(r"[,;]\s*", match[1]):
            item = CITED_ID.match(part)
            if item:
                cited |= expand(item[1], item[2], item[4])
    return cited


def gaps(found):
    by_series = defaultdict(set)
    for series, number in found:
        by_series[series].add(number)
    return {
        series: sorted(set(range(1, max(numbers) + 1)) - numbers)
        for series, numbers in by_series.items()
        if set(range(1, max(numbers) + 1)) - numbers
    }


class SourceNumberingTests(unittest.TestCase):
    def test_numbering_is_contiguous_and_citations_resolve(self):
        paths = sorted(SOURCES.glob("*.md"))
        self.assertTrue(paths)
        for path in paths:
            found, placeholders = entries(path.read_text(encoding="utf-8"))
            recipe = RECIPES / path.name
            cited = citations(recipe.read_text(encoding="utf-8")) if recipe.exists() else set()
            with self.subTest(sources=path.name):
                self.assertEqual(gaps(found), {}, "numbering gap")
                self.assertEqual(sorted(cited - found), [], "cited in the recipe but not listed")
                self.assertEqual(sorted(cited & placeholders), [], "a placeholder number is cited")

    def test_parsing_rules(self):
        text = "\n".join((
            "- **S1:** A.",
            "- **S2:** " + PLACEHOLDER,
            "- **H1–H3:** Range.",
            "- **S4.** Dotted form.",
            "| S3 | Table row | 2024 | 1 |",
        ))
        found, placeholders = entries(text)
        self.assertEqual(found, {("S", 1), ("S", 2), ("S", 3), ("S", 4), ("H", 1), ("H", 2), ("H", 3)})
        self.assertEqual(placeholders, {("S", 2)})
        self.assertEqual(gaps({("S", 1), ("S", 3)}), {"S": [2]})
        self.assertEqual(
            citations("x [S1], [S2, H3] and [S4–S6](https://example.org) but not [Link](y)"),
            {("S", 1), ("S", 2), ("H", 3), ("S", 4), ("S", 5), ("S", 6)},
        )
        self.assertEqual(
            citations("[S3 p. 1] [S7 pp. 10, 14] [H2; interpretation of the form] [S8, H9 p. 2]"),
            {("S", 3), ("S", 7), ("H", 2), ("S", 8), ("H", 9)},
        )
        self.assertEqual(citations("[SS] [S1x] [Smith 1990] [DNA] [D0 dating comparison]"), set())

    def test_a_citation_to_a_series_the_file_lacks_is_reported(self):
        found, _ = entries("- **H1:** A.\n- **H2:** B.")
        cited = citations("Mistyped [S1] next to [H1].")
        self.assertEqual(sorted(cited - found), [("S", 1)])


if __name__ == "__main__":
    unittest.main()
