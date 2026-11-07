"""Count words in recipe headings and header summaries match the numbered sections."""

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills/genealogy-research-recipes"
RECIPES = SKILL_DIR / "recipes"

NUMBER_WORDS = {
    word: value
    for value, word in enumerate(
        "zero one two three four five six seven eight nine ten eleven twelve thirteen "
        "fourteen fifteen sixteen seventeen eighteen nineteen twenty".split()
    )
    if value >= 2
}
COUNTED_H2 = re.compile(r"^## (\w+) ")
NUMBERED_H2 = re.compile(r"^## (?:Recipe )?(\d+)[.:] ")
NUMBERED_H3 = re.compile(r"^### (\d+)\. ")
SUMMARY = re.compile(r"^summary: (\".*\")$", re.MULTILINE)
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")


def headings(lines):
    """Return `##` and `###` heading lines outside fenced code blocks, in order."""
    fence = None
    found = []
    for line in lines:
        match = FENCE.match(line)
        if fence:
            if match and match[1][0] == fence[0] and len(match[1]) >= len(fence) and not match[2].strip():
                fence = None
        elif match and (match[1][0] == "~" or "`" not in match[2]):
            fence = match[1]
        elif line.startswith(("## ", "### ")):
            found.append(line)
    return found


def counted_sections(lines):
    """Map each `## <Number word> ...` heading to the `###` headings under it."""
    sections = {}
    current = None
    for line in headings(lines):
        if line.startswith("## "):
            match = COUNTED_H2.match(line)
            word = match[1].lower() if match else None
            current = line if word in NUMBER_WORDS else None
            if current:
                sections[current] = []
        elif current:
            sections[current].append(line)
    return sections


def numbered_section_count(lines):
    """Count `## 1. ...` / `## Recipe 1: ...` sections, else numbered `### 1. ...` ones."""
    found = headings(lines)
    count = sum(1 for line in found if NUMBERED_H2.match(line))
    return count or sum(1 for line in found if NUMBERED_H3.match(line))


def read_lines(path):
    return path.read_text(encoding="utf-8").splitlines()


class SectionCountTests(unittest.TestCase):
    def test_counted_heading_matches_its_numbered_subsections(self):
        paths = sorted(RECIPES.glob("*.md"))
        self.assertTrue(paths, f"no recipes found in {RECIPES}")
        for path in paths:
            for heading, subsections in counted_sections(read_lines(path)).items():
                with self.subTest(recipe=path.name, heading=heading):
                    expected = NUMBER_WORDS[COUNTED_H2.match(heading)[1].lower()]
                    numbers = [NUMBERED_H3.match(line) for line in subsections]
                    unnumbered = [line for line, number in zip(subsections, numbers) if not number]
                    self.assertEqual(unnumbered, [], "unnumbered section under a counted heading")
                    self.assertEqual([int(number[1]) for number in numbers], list(range(1, expected + 1)))

    def test_header_summary_counts_match_the_recipes(self):
        """The generated SKILL.md router copies each header summary, so check it at the source."""
        checked = 0
        for path in sorted(RECIPES.glob("*.md")):
            text = path.read_text(encoding="utf-8")
            match = SUMMARY.search(text)
            if not match:
                continue
            word = json.loads(match[1]).split(" ", 1)[0]
            if word.lower() not in NUMBER_WORDS:
                continue
            with self.subTest(recipe=path.name):
                lines = text.splitlines()
                counted = list(counted_sections(lines).values())
                actual = len(counted[0]) if len(counted) == 1 else numbered_section_count(lines)
                self.assertEqual(NUMBER_WORDS[word.lower()], actual, f"summary says {word}")
            checked += 1
        self.assertGreater(checked, 0, "no counted summaries found in recipe headers")

    def test_an_unnumbered_section_breaks_the_count(self):
        lines = ["## Two methods", "### 1. A", "### Extra", "### 2. B", "## Next"]
        subsections = counted_sections(lines)["## Two methods"]
        self.assertEqual(len(subsections), 3)
        self.assertFalse(NUMBERED_H3.match(subsections[1]))


if __name__ == "__main__":
    unittest.main()
