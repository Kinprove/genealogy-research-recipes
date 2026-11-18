"""The Danish church-book and probate recipe keeps each route tied to its period and authority (#384).

A model answering without the recipe invented the duplicate-register system, searched the church
book first for a South Jutland birth after 1874, and misdated civil marriage. Each test reads one
paragraph or bullet, or the opening of a section, and checks that the event or class of person, the
period and the authority or register appear together there, so swapping two authorities while keeping every word and year
still fails.
"""

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECIPE = ROOT / "skills/genealogy-research-recipes/recipes/danish-church-book-probate-recovery.md"


def blocks() -> list[str]:
    """Return the recipe's blank-line blocks and list items, each with whitespace folded."""
    result = []
    for block in RECIPE.read_text(encoding="utf-8").split("\n\n"):
        lines = block.strip().splitlines()
        if lines and all(line.startswith("- ") for line in lines):
            result.extend(" ".join(line.split()) for line in lines)
        else:
            result.append(" ".join(block.split()))
    return result


def section(heading: str) -> str:
    """Return the whitespace-folded text from a level-2 heading up to the next one."""
    text = RECIPE.read_text(encoding="utf-8")
    begin = text.index(f"\n## {heading}\n")
    end = text.find("\n## ", begin + 1)
    return " ".join(text[begin : end if end != -1 else len(text)].split())


def passage(start: str) -> str:
    """Return the single block or list item that begins with start."""
    found = [block for block in blocks() if block.startswith(start)]
    if len(found) != 1:
        raise AssertionError(f"expected one passage starting {start!r}, found {len(found)}")
    return found[0]


class ChurchBookTests(unittest.TestCase):
    def test_two_copies_and_their_writers(self):
        text = passage("Outside South Jutland, a rescript of 11 December 1812")
        self.assertIn("preprinted forms from about 1814", text)
        self.assertIn("the hovedministerialbog, kept by the priest", text)
        self.assertIn("the kontraministerialbog, kept by the parish clerk (degn)", text)
        self.assertIn("dates the forms and the two sets from about 1812", text)
        self.assertIn("names the schoolteacher or the parish clerk as the second writer", text)

    def test_single_book_before_1814(self):
        text = passage("Outside South Jutland, before about 1814 a parish kept one book")
        self.assertIn("the enesteministerialbog", text)
        self.assertIn("confirmations (from 1736)", text)

    def test_other_copy_rule(self):
        passage("When an entry is missing, damaged or unreadable in one copy, read the same event in the other copy.")


class CivilMarriageTests(unittest.TestCase):
    def test_who_could_marry_civilly(self):
        text = passage("Before 1851 only a priest could marry a couple.")
        self.assertIn("From 1851 civil marriage was allowed when one or both partners belonged to no recognised "
                      "faith, or when the two belonged to different faiths; from 1923 anyone could choose it.", text)

    def test_authority_by_period(self):
        text = passage("Civil marriages are filed under the civil authority, not the parish.")
        self.assertIn("For 1851–1919 look under the byfoged, herredsfoged or birk", text)
        self.assertIn("For 1919–1922 look under the police district in the countryside and the town council "
                      "(kommune) in market towns.", text)
        self.assertIn("For 1923–1970 look under the sognefoged (parish bailiff) in the countryside", text)
        self.assertIn("From 1971 look under the kommune; those books are not scanned.", text)


class SouthJutlandTests(unittest.TestCase):
    def test_own_church_book_dates(self):
        text = passage("South Jutland's church books reach back further")
        self.assertIn("Fixed forms began there in 1763, and from 1775 the books were to be kept in two copies.", text)

    def test_civil_register_first_1874_to_1925(self):
        text = passage("After South Jutland became part of Prussia in 1864")
        self.assertIn("civil registration of births, marriages and deaths began in 1874", text)
        self.assertIn("Rigsarkivet calls the church books for 1874–1925 secondary sources.", text)
        self.assertIn("The personregister covered births, marriages and deaths; confirmations stayed in the "
                      "church book.", text)
        self.assertIn("For a South Jutland birth, marriage or death in 1874–1925, search the personregister "
                      "first, then the church book.", text)

    def test_general_sections_open_with_the_south_jutland_pointer(self):
        pointer = ("If the place is in South Jutland, read the South Jutland section first: it says which routes "
                   "in this section apply there.")
        for heading in ("Read the church book for the period",
                        "Check civil marriages before calling a marriage missing",
                        "Route a probate by status and date"):
            with self.subTest(heading=heading):
                self.assertTrue(section(heading).startswith(f"## {heading} {pointer}"))

    def test_church_weddings_return_in_1926(self):
        text = passage("From 1926 priests again married couples")
        self.assertIn("marriages were again entered as in the rest of the country, while births and deaths "
                      "stayed in the personregistre", text)

    def test_route_grid_by_event_and_date(self):
        rows = {
            "- **Births and deaths:**": "the church book before 1874; the personregister first for 1874–1925, "
                                         "with the church book as a secondary source",
            "- **Confirmations:**": "the church book in every period",
            "- **Marriages before 1874:**": "the church book; the guide names no civil-marriage route",
            "- **Marriages in 1874–1925:**": "the civil registers (personregistre), which hold every marriage",
            "- **Marriages from 1926:**": "a church wedding in the church book; Rigsarkivet says marriages were then "
                                          "entered as in the rest of the country, so a civil wedding follows the "
                                          "general civil-marriage routes",
            "- **Probates up to 1920, ordinary or private:**": "start with the Register over sønderjyske skifter op "
                                                               "til 1920",
            "- **Probates after 1920:**": "use the general probate routes",
            "- **Soldiers, officers and their families in South Jutland before 1864:**": "the Schleswig and Holstein regiments stayed with their "
                                                         "auditors until 1864",
        }
        for start, route in rows.items():
            with self.subTest(row=start):
                self.assertIn(route, passage(start))

    def test_south_jutland_probate_authorities(self):
        self.assertIn("the herredsfoged or birkefoged in the countryside and the byfoged in towns before 1864, none "
                      "named for 1864–1866 (see the rule below), and the Prussian district courts (amtsretter) for 1867–1920",
                      passage("- **Probates up to 1920, ordinary or private:**"))


class ProbateTests(unittest.TestCase):
    def test_market_town_residents(self):
        self.assertIn("the town's byfoged", passage("- **Market-town residents (købstadsbeboere):**"))

    def test_tenants(self):
        text = passage("- **Tenants (fæstere) and employees of an estate:**")
        self.assertIn("the estate's own archive.", text)
        self.assertIn("From 1817 the tenants of smaller estates went to the herredsfoged or birkefoged.", text)
        self.assertIn("Tenants in a cavalry district (rytterdistrikt) went to the district or its birk; the cavalry "
                      "districts were abolished in 1776.", text)

    def test_non_tenant_rural_people(self):
        text = passage("- **Estate owners, freeholders (selvejere) and other rural people without tenant status:**")
        self.assertIn("the amt before 1793, then the herredsfoged or birk until 1851.", text)

    def test_status_decides_before_1851(self):
        passage("Until 1851 the deceased's status decided which authority held the probate.")

    def test_military_families_go_to_the_auditor(self):
        text = passage("- **Soldiers, officers and their families before 1864:**")
        self.assertIn("each regiment's auditor.", text)
        self.assertIn("units elsewhere to the civil courts in 1805", text)

    def test_ordinary_and_executor_probates_1851_to_1919(self):
        self.assertIn("ordinary probates went to the byfoged, herredsfoged or birk, and private (executor) probates "
                      "were filed with the amt once settled.", passage("From 1851 to 1919 ordinary probates"))

    def test_executor_estates_after_1919(self):
        text = passage("From 1919 each court district's probate court (skifteret) handled probates.")
        self.assertIn("Executor estates were filed with the amt until about 1933 and with the probate court "
                      "afterwards.", text)


if __name__ == "__main__":
    unittest.main()
