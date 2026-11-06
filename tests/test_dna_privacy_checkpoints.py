"""DNA recipes reach the privacy decision of SKILL.md step 5 before each upload, export, import or tree link."""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECIPES = ROOT / "skills/genealogy-research-recipes/recipes"
MARKER = "`SKILL.md` step 5"
PRIVACY_LINK = "ai-for-dna-research.md#verification--privacy-discipline"
HEADING = re.compile(r"^#{1,6} (.*)$", re.MULTILINE)

# (recipe, text of an action that moves genetic or match data outside the account;
# case, line breaks and indentation are ignored)
ACTIONS = [
    ("23andme-match-research.md", "pasting this CSV into a matrix through its **Load** menu"),
    ("23andme-match-research.md", "pasting the numerical comparison table into **Paint a new match**"),
    ("23andme-match-research.md", "Check the destination's current acceptance page"),
    ("23andme-match-research.md", "**Import 23andme ancestry composition**"),
    ("23andme-match-research.md", "before importing it into a third-party painter"),
    ("23andme-match-research.md", "Select your original segment CSV as the main file"),
    ("23andme-match-research.md", "Attach the actual DNA Relative to the right tree person"),
    ("23andme-match-research.md", "Enable **23andMe Download Matches Pages as CSV File**"),
    ("23andme-match-research.md", "Add a useful 23andMe match as an unconnected person"),
    ("ftdna-practical-dna-workflows.md", "Before connecting, switching or disconnecting the MyHeritage tree"),
    ("ftdna-practical-dna-workflows.md", "To link a match: **Link on Family Tree**"),
    ("ftdna-practical-dna-workflows.md", "Link documented relatives who identify one side first"),
    ("gedmatch-practical-dna-workflows.md", "use the vendor's current upload instructions"),
    ("gedmatch-practical-dna-workflows.md", "pass verified measurements to the painting workflow in DNA Painter"),
    ("unknown-parentage-wato.md", "GEDCOM import builds this fast"),
    ("unknown-parentage-wato.md", "enter the real matches and cM"),
    ("unknown-parentage-wato.md", "enter the shared cM between the target and each match already in the tree"),
    ("unknown-parentage-wato.md", "uploading the tester's raw data to a database that accepts third-party transfers"),
    ("wikitree-dna-tester-links.md", "Select the testing company and actual test type/level"),
    ("wikitree-dna-tester-links.md", "Add the GEDmatch kit ID in the applicable WikiTree test field"),
    ("wikitree-dna-tester-links.md", "enter the tester's WikiTree ID in the WikiTree field"),
]

# (recipe whose text links the anchor, target file, anchor)
ANCHORS = [
    ("unknown-parentage-wato.md", "ai-for-dna-research.md", "verification--privacy-discipline"),
    ("unknown-parentage-wato.md", "unknown-parentage-wato.md", "ethics-and-the-human-layer"),
]


def fold(text):
    """Ignore line breaks, indentation and case when matching text."""
    return re.sub(r"\s+", " ", text).casefold()


def sections(text):
    """Split the text before every heading line (`#` to `######`)."""
    return re.split(r"^(?=#{1,6} )", text, flags=re.MULTILINE)


def text_before_action(text, action):
    """Return the folded text from the nearest heading above `action` up to `action`.

    Fails unless `action` occurs exactly once, so a renamed or duplicated action cannot
    pass by going unchecked. A `#` line inside a code fence would count as a heading and
    only shorten the span, so it cannot make a missing checkpoint pass.
    """
    needle = fold(action)
    count = fold(text).count(needle)
    if count != 1:
        raise AssertionError(f"expected the action exactly once, found {count}: {action!r}")
    section = next(part for part in map(fold, sections(text)) if needle in part)
    return section[: section.index(needle)]


def github_slug(heading):
    slug = re.sub(r"[^\w\- ]", "", heading.strip().lower())
    return slug.replace(" ", "-")


class DnaPrivacyCheckpointTests(unittest.TestCase):
    def test_a_privacy_decision_precedes_each_action_in_its_section(self):
        for recipe, action in ACTIONS:
            with self.subTest(recipe=recipe, action=action):
                text = (RECIPES / recipe).read_text(encoding="utf-8")
                self.assertIn(fold(MARKER), text_before_action(text, action))

    def test_the_span_starts_at_the_nearest_heading_above_the_action(self):
        text = f"## A\n\n{MARKER} applies here.\n\n### B\n\nUpload the\n   file now.\n"
        self.assertEqual(text_before_action(text, "upload the file"), "### b ")
        self.assertIn(fold(MARKER), text_before_action(text.replace("### B", "Then"), "upload the file"))

    def test_an_action_must_occur_exactly_once(self):
        with self.assertRaises(AssertionError):
            text_before_action(f"{MARKER}. Upload it. Upload it.", "Upload it")
        with self.assertRaises(AssertionError):
            text_before_action(f"{MARKER}.", "Upload it")

    def test_each_recipe_links_the_privacy_rules(self):
        for recipe in sorted({recipe for recipe, _ in ACTIONS}):
            with self.subTest(recipe=recipe):
                self.assertIn(PRIVACY_LINK, (RECIPES / recipe).read_text(encoding="utf-8"))

    def test_linked_anchors_match_a_heading(self):
        for source, target, anchor in ANCHORS:
            with self.subTest(source=source, anchor=anchor):
                self.assertIn(f"#{anchor})", (RECIPES / source).read_text(encoding="utf-8"))
                headings = HEADING.findall((RECIPES / target).read_text(encoding="utf-8"))
                self.assertIn(anchor, {github_slug(heading) for heading in headings})


if __name__ == "__main__":
    unittest.main()
