"""The European and Hispanic recipes keep the corrections from the expert review in issue #90.

Each test pins a corrected fact and checks that the wrong wording is gone, so a later edit
cannot quietly bring it back.
"""

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECIPES = ROOT / "skills/genealogy-research-recipes/recipes"


def recipe(name: str) -> str:
    """Return a recipe's text with each run of whitespace folded to one space."""
    return " ".join((RECIPES / name).read_text(encoding="utf-8").split())


class EuropeHispanicReviewCorrectionsTests(unittest.TestCase):
    def test_dutch_marriages_1811_to_1838_follow_the_code_civil_ages(self):
        text = recipe("dutch-civil-church-record-recovery.md")
        self.assertIn("a son under 25 and a daughter under 21 needed their parents' consent", text)
        self.assertIn("by a formal acte respectueux", text)
        self.assertNotIn("apply no age threshold", text)

    def test_german_census_recipe_routes_origin_work_to_the_german_recipe(self):
        text = recipe("german-local-census-registration-recovery.md")
        self.assertIn(
            "to a German origin locality: [German emigrant origin sources](german-emigrant-origin-sources.md)",
            text,
        )
        self.assertNotIn("russian-empire-emigrant-origin-recovery", text)

    def test_swedish_1901_ordinance_obliged_no_one_to_take_a_surname(self):
        text = recipe("scandinavian-patronymic-farm-name-record-recovery.md")
        self.assertIn("It obliged no one to take a family name", text)
        self.assertIn("took effect on 1 January 1964", text)
        self.assertIn("From 1 January 1983 the law allowed a person to take a -son or -dotter surname for special reasons", text)
        self.assertNotIn("required anyone without a fixed surname", text)

    def test_swedish_census_database_years_name_their_counties(self):
        text = recipe("scandinavian-parish-record-recovery.md")
        sentences = text.split(". ")
        self.assertTrue(any("1860" in s and "only Jämtland" in s for s in sentences))
        self.assertTrue(any("1870" in s and "Västerbotten" in s and "Norrbotten" in s for s in sentences))
        self.assertNotIn("You can search it for 1860, 1870, 1880", text)

    def test_places_without_a_parish_are_many_and_one_in_ten_stays_attributed(self):
        text = recipe("german-register-image-recovery.md")
        self.assertIn("Many smaller places had no parish of their own. One presenter estimates", text)
        self.assertNotIn("Most towns had no parish of their own", text)

    def test_meyers_edition_year_matches_across_recipes(self):
        german = recipe("german-register-image-recovery.md")
        self.assertIn("Meyers Orts- und Verkehrs-Lexikon (1912)", german)
        self.assertNotIn("(1912–13)", german)
        self.assertIn("Meyers Orts- und Verkehrs-Lexikon (1912 edition)", recipe("historical-place-name-resolution.md"))

    def test_prussian_hospital_books_are_at_the_bundesarchiv(self):
        text = recipe("german-military-record-period-routing.md")
        self.assertIn("The surviving books of the Krankenbuchlager Berlin", text)
        self.assertIn("are in the Bundesarchiv (Abteilung PA)", text)
        self.assertNotIn("Landesarchiv Berlin", text)


if __name__ == "__main__":
    unittest.main()
