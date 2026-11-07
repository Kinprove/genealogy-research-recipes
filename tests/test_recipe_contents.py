"""Every recipe longer than 100 lines starts with a `## Contents` list of its `##` sections."""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECIPES = ROOT / "skills/genealogy-research-recipes/recipes"
MAX_LINES_WITHOUT_CONTENTS = 100
CONTENTS = "## Contents"
NUMBERED = re.compile(r"^(\d+)\. ")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")


def h2_headings(lines):
    """Return (line index, line) for each `## ` heading outside fenced code blocks.

    As in CommonMark, a fence line is indented by at most three spaces, a backtick
    fence's info string has no backtick, and a fence closes only on a line of the same
    character, at least as long as the opening fence, with nothing after it. A ```` block
    can hold a ``` example.
    """
    fence = None
    headings = []
    for index, line in enumerate(lines):
        match = FENCE.match(line)
        if fence:
            if match and match[1][0] == fence[0] and len(match[1]) >= len(fence) and not match[2].strip():
                fence = None
        elif match and (match[1][0] == "~" or "`" not in match[2]):
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

    def test_only_a_fence_indented_up_to_three_spaces_opens_or_closes_a_block(self):
        lines = ["```text", "    ```", "## Not a section", "```", "    ```", "## A"]
        lines += ["   ```", "## Not a section either", "   ```", "``` not`a fence", "## B"]
        self.assertEqual([line for _, line in h2_headings(lines)], ["## A", "## B"])

    def test_contents_lists_name_every_section_in_order(self):
        paths = sorted(RECIPES.glob("*.md"))
        self.assertTrue(paths, f"no recipes found in {RECIPES}")
        checked = 0
        for path in paths:
            text = path.read_text(encoding="utf-8")
            # Routing metadata is not a body section and does not need navigation.
            if text.startswith("---\n"):
                text = text.split("\n---\n", 1)[1].lstrip("\n")
            lines = text.splitlines()
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

    def test_recipe_heading_counts_match_subsections(self):
        """Issue #78: Recipe heading counts of the form `## <Number word> ...` must match the `###` subsections."""
        word_to_num = {
            "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
            "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
            "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
            "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
        }
        h2_count_re = re.compile(r"^##\s+([A-Za-z]+)\s+.*")
        checked = 0
        for path in sorted(RECIPES.glob("*.md")):
            lines = path.read_text(encoding="utf-8").splitlines()
            for i, line in enumerate(lines):
                m = h2_count_re.match(line)
                if m and m.group(1).lower() in word_to_num:
                    expected = word_to_num[m.group(1).lower()]
                    sub_count = 0
                    for next_line in lines[i + 1 :]:
                        if next_line.startswith("## "):
                            break
                        if next_line.startswith("### "):
                            sub_count += 1
                    with self.subTest(recipe=path.name, heading=line):
                        self.assertEqual(
                            sub_count,
                            expected,
                            f"{path.name}: heading {line!r} claims {expected} sections but has {sub_count}",
                        )
                    checked += 1
        self.assertGreater(checked, 0)

    def test_skill_summary_counts_match_recipes(self):
        """Issue #78: Counts in SKILL.md recipe descriptions must match the actual number of procedures."""
        skill_file = ROOT / "skills/genealogy-research-recipes/SKILL.md"
        word_to_num = {
            "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
            "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
            "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
            "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
        }
        skill_text = skill_file.read_text(encoding="utf-8")
        pattern = re.compile(r"-\s+\*\*`recipes/([^`]+)`\*\*[^\r\n]*\r?\n\s+([A-Za-z]+)\s+.*")
        checked = 0
        for m in pattern.finditer(skill_text):
            recipe_name = m.group(1)
            word = m.group(2).lower()
            if word in word_to_num:
                expected = word_to_num[word]
                rpath = RECIPES / recipe_name
                if rpath.exists():
                    rlines = rpath.read_text(encoding="utf-8").splitlines()
                    h2_nums = [l for l in rlines if re.match(r"^##\s+\d+\.", l)]
                    h3_nums = [l for l in rlines if re.match(r"^###\s+\d+\.", l)]
                    actual = len(h2_nums) or len(h3_nums)
                    if actual:
                        with self.subTest(recipe=recipe_name):
                            self.assertEqual(
                                actual,
                                expected,
                                f"SKILL.md claims {expected} ({word}) for {recipe_name} but recipe has {actual}",
                            )
                        checked += 1
        self.assertGreater(checked, 0)


if __name__ == "__main__":
    unittest.main()
