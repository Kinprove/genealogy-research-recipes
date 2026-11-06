"""Every recipe longer than 100 lines starts with a `## Contents` list of its `##` sections."""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECIPES = ROOT / "skills/genealogy-research-recipes/recipes"
MAX_LINES_WITHOUT_CONTENTS = 100
CONTENTS = "## Contents"
NUMBERED = re.compile(r"^(\d+)\. ")
FENCE = re.compile(r"^(`{3,}|~{3,})(.*)$")


def h2_headings(lines):
    """Return (line index, line) for each `## ` heading outside fenced code blocks.

    As in CommonMark, a fence closes only on a line of the same character, at least as
    long as the opening fence, with nothing after it. A ```` block can hold a ``` example.
    """
    fence = None
    headings = []
    for index, line in enumerate(lines):
        match = FENCE.match(line.lstrip())
        if fence:
            if match and match[1][0] == fence[0] and len(match[1]) >= len(fence) and not match[2].strip():
                fence = None
        elif match:
            fence = match[1]
        elif line.startswith("## "):
            headings.append((index, line))
    return headings


def contents_item(heading):
    # Escape a leading "1." so that the item does not start a nested numbered list.
    return "- " + NUMBERED.sub(r"\1\\. ", heading[len("## "):], count=1)


def expected_contents(section_headings):
    return [CONTENTS, "", *(contents_item(heading) for heading in section_headings), ""]


class RecipeContentsTests(unittest.TestCase):
    def test_a_longer_fence_hides_an_inner_fence_and_its_headings(self):
        lines = ["## A", "````markdown", "```text", "## Not a section", "```", "````"]
        lines += ["~~~", "## Not a section either", "```", "~~~", "## B"]
        self.assertEqual([line for _, line in h2_headings(lines)], ["## A", "## B"])

    def test_contents_lists_name_every_section_in_order(self):
        paths = sorted(RECIPES.glob("*.md"))
        self.assertTrue(paths, f"no recipes found in {RECIPES}")
        checked = 0
        for path in paths:
            lines = path.read_text(encoding="utf-8").splitlines()
            headings = h2_headings(lines)
            has_contents = any(line == CONTENTS for _, line in headings)
            if len(lines) <= MAX_LINES_WITHOUT_CONTENTS and not has_contents:
                continue
            checked += 1
            with self.subTest(recipe=path.name):
                sections = [line for _, line in headings if line != CONTENTS]
                expected = expected_contents(sections)
                hint = "the Contents list must name every `##` section in file order:\n" + "\n".join(expected)
                self.assertTrue(sections, "the Contents list has no `##` sections to name")
                self.assertTrue(
                    headings[0][1] == CONTENTS,
                    f"a recipe longer than {MAX_LINES_WITHOUT_CONTENTS} lines needs `{CONTENTS}` as its first "
                    f"`##` heading; {hint}",
                )
                self.assertEqual(len(headings) - len(sections), 1, f"`{CONTENTS}` appears more than once")
                actual = lines[headings[0][0] : headings[1][0]]
                self.assertEqual(actual, expected, hint)
        self.assertGreater(checked, 0, "no recipe needed a Contents list; the line count is probably wrong")


if __name__ == "__main__":
    unittest.main()
