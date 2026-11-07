"""The Beider recipe's snapshot claims, article keys and index rows match the bundled data."""

import importlib.util
import json
import re
import unittest
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]
RECIPE = SKILL / "recipes/beider-given-name-variants.md"
HELPER = SKILL / "scripts/lookup_beider_name.py"
SPEC = importlib.util.spec_from_file_location("lookup_beider_name", HELPER)
lookup = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(lookup)

COMPANIONS = "### Sacred names and their vernacular companions"
CHECK_ENTRIES = "### Entries to check against the dictionary"
CODE = re.compile(r"`([^`]+)`")
KEY_OPTION = re.compile(r"`--key ([^`]+)`")


def table_rows(text, heading):
    """Return the cells of each body row of the first table after `heading`."""
    lines = text.splitlines()
    start = lines.index(heading) + 1
    rows = []
    for line in lines[start:]:
        if line.startswith("#"):
            break
        if line.startswith("|") and not set(line) <= set("|- "):
            rows.append([cell.strip() for cell in line.strip("|").split("|")])
        elif rows and not line.startswith("|"):
            break
    return rows[1:]  # drop the header row


class BeiderRecipeKeyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = RECIPE.read_text(encoding="utf-8")
        cls.indexes = lookup.load_manifest()
        cls.pairs = {sex: set(index["entries"]) for sex, index in cls.indexes.items()}

    def assert_article(self, sex, key, message):
        """Use the lookup the helper runs for `--key`."""
        self.assertIsNotNone(lookup.find_variants(self.indexes[sex]["entries"], key=key, limit=1), message)

    def test_recipe_snapshot_counts_and_dates_match_bundled_data(self):
        paragraph = re.search(
            r"The bundled snapshot contains (?P<male>[\d,]+) male and "
            r"(?P<female>[\d,]+) female name/article associations from "
            r"complete first-post archive captures dated (?P<capture>\d{4}-\d{2}-\d{2}), "
            r"retrieved on (?P<snapshot>\d{4}-\d{2}-\d{2})\.",
            " ".join(self.text.split()),
        )
        self.assertIsNotNone(paragraph, "snapshot counts and dates paragraph not found")
        manifest = json.loads(lookup.MANIFEST.read_text(encoding="utf-8"))
        for sex in ("male", "female"):
            with self.subTest(sex=sex):
                record = manifest["indexes"][sex]
                self.assertEqual(int(paragraph[sex].replace(",", "")), record["entry_count"])
                self.assertEqual(paragraph["capture"], record["source_capture_date"])
        self.assertEqual(paragraph["snapshot"], manifest["snapshot_date"])

    def test_every_companion_key_is_a_male_article(self):
        rows = table_rows(self.text, COMPANIONS)
        self.assertGreaterEqual(len(rows), 10, "companion table not found or too short")
        for row in rows:
            keys = CODE.findall(row[2])
            self.assertTrue(keys, f"no article key in row {row}")
            for key in keys:
                self.assert_article("male", key, f"unknown male article {key}")

    def test_every_entry_to_check_is_in_the_stated_index(self):
        rows = table_rows(self.text, CHECK_ENTRIES)
        self.assertGreaterEqual(len(rows), 5, "entries-to-check table not found or too short")
        for row in rows:
            sex = row[0].lower()
            (name,) = CODE.findall(row[1])
            keys = CODE.findall(row[2])
            self.assertTrue(keys, f"no article key in row {row}")
            for key in keys:
                pair = (lookup.normalize_name(name), lookup.normalize_name(key))
                self.assertTrue(pair in self.pairs[sex], f"{sex} index has no row {pair}")
            for key in KEY_OPTION.findall(row[3]):
                self.assert_article(sex, key, f"`--key {key}` names no {sex} article")

    def test_table_reader_stops_at_the_next_heading(self):
        text = f"{COMPANIONS}\n\nNo table here.\n\n### Next\n\n| A | B | C |\n| --- | --- | --- |\n| q | r | `S` |\n"
        self.assertEqual(table_rows(text, COMPANIONS), [])

    def test_table_reader_returns_only_the_first_table(self):
        text = f"{COMPANIONS}\n\n| A | B | C |\n| --- | --- | --- |\n| x | y | `Z` |\n\nText.\n\n| A | B | C |\n| q | r | `S` |\n"
        self.assertEqual(table_rows(text, COMPANIONS), [["x", "y", "`Z`"]])


if __name__ == "__main__":
    unittest.main()
