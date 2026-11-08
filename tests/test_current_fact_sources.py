"""Keep issue 83's archive, portal and legal claims bound to dated sources.

This is a reviewed inventory of the reported claims, not a detector of every new
institutional fact or a substitute for reading the cited page. Existing CI's
unittest discovery runs it alongside the source-credit and privacy checks.
"""

import json
import re
import unittest
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/genealogy-research-recipes"
INVENTORY = Path(__file__).with_name("current_fact_source_audit.json")
SOURCE = re.compile(r"^- \*\*(S\d+):\*\*", re.MULTILINE)
INSPECTED = re.compile(r"\b(?:checked|opened|read|inspected)(?: on)? (\d{4}-\d{2}-\d{2})\b")
URL = re.compile(r"https?://[^\s)<>]+")
CITED_SOURCE = r"S\d+(?:†)?(?: @\d{4}-\d{2}-\d{2})?"


def fold(text):
    return " ".join(text.split())


def source_entries(text):
    """Read numbered entries before Credits; a bare credit never defines a source."""
    body = text.split("## Credits", 1)[0]
    entries = {}
    matches = list(SOURCE.finditer(body))
    for index, match in enumerate(matches):
        source_id = match[1]
        if source_id in entries:
            raise AssertionError(f"duplicate numbered source {source_id}")
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        entries[source_id] = body[match.start():end].split("\n\n", 1)[0]
    return entries


def check_binding(recipe, sources, claim, expected_sources):
    paragraphs = [p for p in recipe.split("\n\n") if fold(claim) in fold(p)]
    if len(paragraphs) != 1:
        raise AssertionError(f"claim must identify one paragraph, found {len(paragraphs)}: {claim!r}")
    references = set()
    for citation in re.findall(r"\[([^\]]+)\]", paragraphs[0]):
        if re.fullmatch(CITED_SOURCE + r"(?:,\s*" + CITED_SOURCE + r")*", citation):
            references.update(re.findall(r"S\d+", citation))
    entries = source_entries(sources)
    for source_id in expected_sources:
        if source_id not in references:
            raise AssertionError(f"claim's paragraph needs [{source_id}]: {claim!r}")
        if source_id not in entries:
            raise AssertionError(f"no numbered entry for {source_id}")
        entry = entries[source_id]
        if not URL.search(entry):
            raise AssertionError(f"{source_id} needs a URL in its numbered entry")
        inspected = INSPECTED.search(entry)
        if not inspected:
            raise AssertionError(f"{source_id} needs an explicit inspection date, not just a publication date")
        try:
            date.fromisoformat(inspected[1])
        except ValueError as error:
            raise AssertionError(f"{source_id} has an invalid inspection date") from error


class BindingParserTests(unittest.TestCase):
    recipe = "The archive opens by appointment. [S2]\n"
    claim = "The archive opens by appointment."
    source = "- **S2:** Archive, [Visit](https://archive.example/visit), checked 2026-11-07.\n"

    def test_wrapped_claim_and_numbered_source_bind(self):
        check_binding(self.recipe.replace("opens by", "opens\nby"), self.source, self.claim, ["S2"])

    def test_dated_provenance_marker_keeps_the_same_source_binding(self):
        check_binding(self.recipe.replace('[S2]', '[S2 @2026-11-07]'), self.source, self.claim, ['S2'])
        with self.assertRaisesRegex(AssertionError, 'paragraph needs'):
            check_binding(self.recipe.replace('[S2]', '[S2 on 2026-11-07]'), self.source, self.claim, ['S2'])

    def test_a_source_cited_only_in_another_paragraph_does_not_bind(self):
        with self.assertRaisesRegex(AssertionError, "paragraph needs"):
            check_binding(self.claim + "\n\nOther facts. [S2]", self.source, self.claim, ["S2"])

    def test_a_bare_credit_with_a_url_and_date_is_not_a_numbered_entry(self):
        with self.assertRaisesRegex(AssertionError, "no numbered entry"):
            check_binding(self.recipe, "## Credits\n\n" + self.source, self.claim, ["S2"])

    def test_a_publication_date_alone_is_not_an_inspection_date(self):
        with self.assertRaisesRegex(AssertionError, "inspection date"):
            check_binding(self.recipe, self.source.replace("checked", "published"), self.claim, ["S2"])

    def test_an_adjacent_source_cannot_supply_a_missing_inspection_date(self):
        adjacent = self.source.replace("S2", "S3")
        sources = self.source.replace("checked", "published") + adjacent
        with self.assertRaisesRegex(AssertionError, "inspection date"):
            check_binding(self.recipe, sources, self.claim, ["S2"])

    def test_an_adjacent_source_cannot_supply_a_missing_url(self):
        adjacent = self.source.replace("S2", "S3")
        sources = self.source.replace("https://archive.example/visit", "Visit") + adjacent
        with self.assertRaisesRegex(AssertionError, "needs a URL"):
            check_binding(self.recipe, sources, self.claim, ["S2"])

    def test_a_date_without_a_source_url_does_not_bind(self):
        with self.assertRaisesRegex(AssertionError, "needs a URL"):
            check_binding(self.recipe, self.source.replace("https://archive.example/visit", "Visit"), self.claim, ["S2"])

    def test_an_invalid_date_is_rejected(self):
        with self.assertRaisesRegex(AssertionError, "invalid inspection date"):
            check_binding(self.recipe, self.source.replace("11-07", "02-30"), self.claim, ["S2"])

    def test_duplicate_source_numbers_are_rejected(self):
        with self.assertRaisesRegex(AssertionError, "duplicate numbered source"):
            source_entries(self.source + "\n" + self.source)


class CurrentFactSourcesTests(unittest.TestCase):
    def test_reported_claims_have_dated_numbered_sources_or_are_removed(self):
        inventory = json.loads(INVENTORY.read_text(encoding="utf-8"))
        self.assertEqual(inventory["issue"], 83)
        records = inventory["recipes"]
        self.assertEqual(len(records), 20, "audit every recipe named in issue 83")
        self.assertEqual(len({r["recipe"] for r in records}), len(records), "duplicate audit recipe")
        for record in records:
            name = record["recipe"]
            recipe = (SKILL / "recipes" / name).read_text(encoding="utf-8")
            sources = (SKILL / "sources" / name).read_text(encoding="utf-8")
            self.assertTrue(record["bindings"] or record["removed"], f"no disposition for {name}")
            for binding in record["bindings"]:
                with self.subTest(recipe=name, claim=binding["claim"]):
                    self.assertTrue(binding["sources"], "a retained fact needs its correcting/confirming source")
                    check_binding(recipe, sources, binding["claim"], binding["sources"])
            for removed in record["removed"]:
                with self.subTest(recipe=name, removed=removed["claim"]):
                    self.assertTrue(removed["reason"], "record why a claim was removed")
                    self.assertNotIn(fold(removed["claim"]), fold(recipe), "unbound claim returned; verify and cite it")


if __name__ == "__main__":
    unittest.main()
