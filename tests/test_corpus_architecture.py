"""Corpus-level routing decisions from issue 101: court recipes, the Eastern-Europe front door, the roadmap."""

import datetime as dt
import importlib.util
import re
import unittest
from itertools import permutations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("recipe_catalog", ROOT / "scripts/recipe_catalog.py")
catalog = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(catalog)

SKILL = ROOT / catalog.SKILL_PATH / "SKILL.md"
COURTS = ("court-case-file-recovery", "criminal-court-prison-record-recovery",
          "us-federal-court-case-file-recovery")
EAST_GROUP = "Central and Eastern Europe by period state"
EAST_ROUTERS = ("galicia-bukovina-habsburg-record-routing", "bessarabia-moldova-record-routing",
                "historic-hungary-record-routing", "austrian-confessional-register-routing")
EAST_HANDOFFS = (
    ("galicia-bukovina-habsburg-record-routing", "bessarabia-moldova-record-routing"),
    ("bessarabia-moldova-record-routing", "galicia-bukovina-habsburg-record-routing"),
    ("galicia-bukovina-habsburg-record-routing", "historic-hungary-record-routing"),
    ("historic-hungary-record-routing", "galicia-bukovina-habsburg-record-routing"),
    ("galicia-bukovina-habsburg-record-routing", "austrian-confessional-register-routing"),
    ("austrian-confessional-register-routing", "galicia-bukovina-habsburg-record-routing"),
    ("historic-hungary-record-routing", "austrian-confessional-register-routing"),
    ("austrian-confessional-register-routing", "historic-hungary-record-routing"),
    ("russian-empire-jewish-metrical-book-recovery", "galicia-bukovina-habsburg-record-routing"),
)


class CorpusArchitectureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.recipes = {m["id"]: (m, body) for m, body in catalog.load_catalog(today=dt.date.today())}
        cls.skill = SKILL.read_text(encoding="utf-8")

    def test_court_recipes_link_each_other_in_body_and_handoff(self):
        for source, target in permutations(COURTS, 2):
            metadata, body = self.recipes[source]
            with self.subTest(source=source, target=target):
                self.assertIn(target, metadata["handoff"])
                self.assertIn(f"]({target}.md)", body)

    def test_criminal_recipe_leaves_the_state_case_file_to_the_court_recipe(self):
        criminal, _ = self.recipes["criminal-court-prison-record-recovery"]
        self.assertIn("a state or local court's case file belongs to court case-file recovery",
                      criminal["summary"])
        self.assertNotIn("criminal court", criminal["title"].casefold())
        court, court_body = self.recipes["court-case-file-recovery"]
        self.assertIn("state or local", court["summary"])
        self.assertIn("Start here for a case file from any U.S. state, county or local court", court_body)

    def test_eastern_europe_routers_form_the_first_topic_group(self):
        east = {slug: m["router"] for slug, (m, _) in self.recipes.items() if m["router"]["group"] == EAST_GROUP}
        self.assertEqual(set(east), set(EAST_ROUTERS))
        self.assertEqual({route["tier"] for route in east.values()}, {"pointer"})
        other_pointers = [m["router"]["order"] for slug, (m, _) in self.recipes.items()
                          if m["router"]["tier"] == "pointer" and slug not in east]
        self.assertLess(max(route["order"] for route in east.values()), min(other_pointers))

    def test_every_router_group_heading_appears_once(self):
        start = self.skill.index(catalog.ROUTER_START)
        router = self.skill[start:self.skill.index(catalog.ROUTER_END, start)]
        headings = re.findall(r"^### (.+)$", router, re.M)
        self.assertIn(EAST_GROUP, headings)
        self.assertEqual(len(headings), len(set(headings)), "a router group is split; give it consecutive orders")

    def test_how_to_use_points_to_the_eastern_europe_front_door(self):
        how_to = self.skill.split("\n## How to use\n", 1)[1].split("\n## ", 1)[0]
        self.assertIn("](#central-and-eastern-europe-by-period-state)", how_to)
        for slug in ("russian-orthodox-metrical-book-recovery", "russian-empire-jewish-metrical-book-recovery",
                     "polish-index-original-record-recovery"):
            self.assertIn(f"](recipes/{slug}.md)", how_to)
        self.assertIn("for Jewish events outside the Kingdom of Poland", " ".join(how_to.split()))

    def test_eastern_europe_routers_hand_off_to_their_neighbours(self):
        for source, target in EAST_HANDOFFS:
            with self.subTest(source=source, target=target):
                self.assertIn(target, self.recipes[source][0]["handoff"])

    def test_contributing_links_the_coverage_roadmap(self):
        self.assertIn("](docs/coverage-roadmap.md)", (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
