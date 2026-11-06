"""The skill description must stay inside the hosts' length limit, with room for the next edit."""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/genealogy-research-recipes/SKILL.md"
HOST_LIMIT = 1024
BUDGET = 1000


def folded_description(skill_text: str) -> str:
    """Return the frontmatter description as YAML folds a `>-` block: lines joined by single spaces."""
    match = re.match(r"^---\n(.*?)\n---\n", skill_text, re.DOTALL)
    assert match is not None, "SKILL.md has no frontmatter"
    block = re.search(r"^description: >-\n((?:  .*\n?)+)", match.group(1) + "\n", re.MULTILINE)
    assert block is not None, "description is not a `>-` block"
    return " ".join(line.strip() for line in block.group(1).splitlines() if line.strip())


class SkillDescriptionTests(unittest.TestCase):
    def test_description_fits_the_budget(self):
        description = folded_description(SKILL.read_text(encoding="utf-8"))
        self.assertGreater(len(description), 0)
        self.assertLessEqual(len(description), HOST_LIMIT, "over the 1,024-character host limit")
        self.assertLessEqual(len(description), BUDGET, f"{len(description)} characters; keep it within {BUDGET}")

    def test_folding_matches_yaml(self):
        sample = "---\nname: x\ndescription: >-\n  first line\n  second line\n---\nbody\n"
        self.assertEqual(folded_description(sample), "first line second line")


if __name__ == "__main__":
    unittest.main()
