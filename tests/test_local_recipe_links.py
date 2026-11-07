"""Bundled recipe handoffs must use the installed copy and work offline."""

import re
import unittest
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1] / "skills/genealogy-research-recipes"
SELF_BLOB_URL = re.compile(
    r"github\.com/Kinprove/genealogy-research-recipes/blob/", re.IGNORECASE
)


class LocalRecipeLinkTests(unittest.TestCase):
    def test_skill_and_recipes_do_not_link_to_github_copies(self):
        paths = [SKILL / "SKILL.md", *sorted((SKILL / "recipes").rglob("*.md"))]
        self.assertGreater(len(paths), 1, "no bundled recipes were found")
        for path in paths:
            with self.subTest(file=str(path.relative_to(SKILL))):
                hits = [
                    number
                    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1)
                    if SELF_BLOB_URL.search(line)
                ]
                self.assertEqual(
                    hits, [],
                    "use a relative link to the bundled file; GitHub blob URLs on these"
                    " lines require the network and can select a different version",
                )


if __name__ == "__main__":
    unittest.main()
