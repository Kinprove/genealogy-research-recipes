"""Every recipe longer than 100 lines starts with a `## Contents` list of its `##` sections."""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECIPES = ROOT / "skills/genealogy-research-recipes/recipes"
MAX_LINES_WITHOUT_CONTENTS = 100
CONTENTS = "## Contents"
NUMBERED = re.compile(r"^(\d+)\. ")


def h2_headings(lines):
    """Return (line index, line) for each `## ` heading outside fenced code blocks."""
    in_fence = False
    headings = []
    for index, line in enumerate(lines):
        if line.lstrip().startswith(("```", "~~~")):
            in_fence = not in_fence
        elif not in_fence and line.startswith("## "):
            headings.append((index, line))
    return headings


def contents_item(heading):
    # Escape a leading "1." so that the item does not start a nested numbered list.
    return "- " + NUMBERED.sub(r"\1\\. ", heading[len("## "):], count=1)


def expected_contents(section_headings):
    return [CONTENTS, "", *(contents_item(heading) for heading in section_headings), ""]


class RecipeContentsTests(unittest.TestCase):
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
                self.assertTrue(
                    headings and headings[0][1] == CONTENTS,
                    f"a recipe longer than {MAX_LINES_WITHOUT_CONTENTS} lines needs `{CONTENTS}` as its first `##` heading",
                )
                sections = [line for _, line in headings[1:]]
                self.assertTrue(sections, "the Contents list has no `##` sections to name")
                self.assertNotIn(CONTENTS, sections, f"`{CONTENTS}` appears more than once")
                expected = expected_contents(sections)
                actual = lines[headings[0][0] : headings[1][0]]
                self.assertEqual(
                    actual,
                    expected,
                    "the Contents list must name every `##` section in file order:\n" + "\n".join(expected),
                )
        self.assertGreater(checked, 0, "no recipe needed a Contents list; the line count is probably wrong")


if __name__ == "__main__":
    unittest.main()
