"""Catalog invariants and mutation tests for the authoring/export boundary."""

import copy
import datetime as dt
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("recipe_catalog", ROOT / "scripts/recipe_catalog.py")
catalog = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(catalog)


class RecipeCatalogTests(unittest.TestCase):
    def setUp(self):
        self.today = dt.date.today()
        self.items = catalog.load_catalog(today=self.today)
        self.metadata, self.body = copy.deepcopy(self.items[0])

    def assert_invalid(self, metadata, message):
        with self.assertRaisesRegex(catalog.CatalogError, message):
            catalog.validate_header(metadata, self.body, metadata["id"] + ".md", self.today)

    def test_every_recipe_has_a_valid_header_and_both_outputs_are_current(self):
        files = list((ROOT / catalog.SKILL_PATH / "recipes").glob("*.md"))
        self.assertEqual(len(self.items), len(files))
        for path, expected in catalog.generated_files(ROOT, self.items):
            self.assertEqual(path.read_text(encoding="utf-8"), expected, f"run --write: {path}")

    def test_header_round_trip_preserves_unicode_lists_and_body(self):
        text = catalog.emit_recipe(self.metadata, self.body)
        self.assertEqual(catalog.parse_recipe(text), (self.metadata, self.body))

    def test_schema_rejects_missing_unknown_duplicate_and_malformed_fields(self):
        for field in ("scope", "guardrails", "capabilities", "checked"):
            m = copy.deepcopy(self.metadata)
            del m[field]
            self.assert_invalid(m, "header fields")
        m = copy.deepcopy(self.metadata)
        m["extra"] = True
        self.assert_invalid(m, "header fields")
        for header in ('id: "one"\nid: "two"', 'id: [broken', 'id: plain-yaml'):
            with self.subTest(header=header), self.assertRaises(catalog.CatalogError):
                catalog.parse_recipe("---\n" + header + "\n---\n# Body\n")

    def test_schema_rejects_empty_rules_bad_ids_and_wrong_titles(self):
        for key, value, error in (("guardrails", [], "guardrails"), ("id", "../escape", "invalid id"),
                                  ("title", "Other title", "title differs"), ("triggers", [], "triggers")):
            m = copy.deepcopy(self.metadata)
            m[key] = value
            self.assert_invalid(m, error)

    def test_dangling_references_fail_in_body_and_handoff(self):
        for reference in ("[other](no-such-recipe.md)", "**`recipes/no-such-recipe.md`**",
                          "recipe **no-such-recipe**", "**recipes/no-such-recipe.md**",
                          "when this recipe names `russian-empire-immigration-research`",
                          "[other](../recipes/no-such-recipe.md#part)"):
            with self.subTest(reference=reference), self.assertRaisesRegex(catalog.CatalogError, "missing recipe"):
                catalog.load_catalog(replacement=(self.metadata["id"] + ".md",
                    catalog.emit_recipe(self.metadata, self.body + "\n" + reference)))
        self.metadata["handoff"].append("no-such-recipe")
        with self.assertRaisesRegex(catalog.CatalogError, "missing recipe"):
            catalog.load_catalog(replacement=(self.metadata["id"] + ".md",
                catalog.emit_recipe(self.metadata, self.body)))

    def test_external_links_and_non_recipe_bold_labels_are_not_handoffs(self):
        text = "[paper](https://example.org/paper.md) **segment-level** `foo.csv` [source](../sources/a.md)"
        self.assertEqual(list(catalog.recipe_references(text)), [])

    def test_router_dangling_reference_and_changed_core_guardrail_fail(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skill = root / catalog.SKILL_PATH
            skill.mkdir(parents=True)
            source = (ROOT / catalog.SKILL_PATH / "SKILL.md").read_text(encoding="utf-8")
            (skill / "SKILL.md").write_text(source + "\n**`recipes/not-a-recipe.md`**\n")
            with self.assertRaisesRegex(catalog.CatalogError, "SKILL.md: missing recipe"):
                list(catalog.generated_files(root, self.items))
        original = catalog.render_router(self.items)
        changed = copy.deepcopy(self.items)
        changed[0][0]["guardrails"][0]["text"] = "A different rule."
        self.assertNotEqual(original, catalog.render_router(changed))
        self.assertIn("*Core guardrail:* A different rule.", catalog.render_router(changed))
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skill = root / catalog.SKILL_PATH
            skill.mkdir(parents=True)
            source = (ROOT / catalog.SKILL_PATH / "SKILL.md").read_text(encoding="utf-8")
            (skill / "SKILL.md").write_text(source.replace("*Core guardrail:*", "*Changed guardrail:*", 1))
            (root / "README.md").write_text((ROOT / "README.md").read_text(encoding="utf-8"))
            with patch.object(catalog, "ROOT", root), patch.object(catalog, "load_catalog", return_value=self.items):
                self.assertEqual(catalog.main(["--check"]), 1)

    def test_guardrail_ids_are_unique_across_recipes(self):
        self.metadata["guardrails"][0]["id"] = self.items[1][0]["guardrails"][0]["id"]
        with self.assertRaisesRegex(catalog.CatalogError, "duplicate guardrail id"):
            catalog.load_catalog(replacement=(self.metadata["id"] + ".md",
                catalog.emit_recipe(self.metadata, self.body)))

    def test_each_outbound_capability_needs_a_gate_even_without_inventory(self):
        for key in ("extensions", "data_transfer", "contact"):
            m = copy.deepcopy(self.metadata)
            m["gates"], m["privacy"] = [], "none"
            m["capabilities"] = {field: [] for field in catalog.CAPABILITIES}
            m["capabilities"][key] = ["new action"]
            with self.subTest(key=key):
                self.assert_invalid(m, "require privacy-transfer")

    def test_inventory_catches_underdeclared_actions(self):
        m, body = copy.deepcopy(next(item for item in self.items if item[0]["id"] == "gedmatch-practical-dna-workflows"))
        m["capabilities"]["data_transfer"] = []
        with self.assertRaisesRegex(catalog.CatalogError, "capability omits inventoried"):
            catalog.load_catalog(replacement=(m["id"] + ".md", catalog.emit_recipe(m, body)))

    def test_platform_freshness_has_a_fixed_boundary_and_needs_evidence(self):
        m, body = next(item for item in self.items if item[0]["kind"] == "platform")
        m = copy.deepcopy(m)
        date = dt.date.fromisoformat(m["checked"])
        catalog.validate_header(m, body, m["id"] + ".md", date + dt.timedelta(days=catalog.MAX_PLATFORM_AGE_DAYS))
        with self.assertRaisesRegex(catalog.CatalogError, "older than"):
            catalog.validate_header(m, body, m["id"] + ".md", date + dt.timedelta(days=catalog.MAX_PLATFORM_AGE_DAYS + 1))
        m["checked"] = self.today.isoformat()
        with self.assertRaisesRegex(catalog.CatalogError, "differs from checked_basis"):
            catalog.validate_header(m, body, m["id"] + ".md", self.today)
        m["checked"], m["checked_basis"] = None, None
        with self.assertRaisesRegex(catalog.CatalogError, "dated source check"):
            catalog.validate_header(m, body, m["id"] + ".md", self.today)

    def test_export_emits_header_and_regenerates_both_consumers(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skill = root / catalog.SKILL_PATH
            (skill / "recipes").mkdir(parents=True)
            (root / "tests").mkdir()
            (root / "tests/privacy_gate_inventory.json").write_text("[]")
            (skill / "SKILL.md").write_text(catalog.ROUTER_START + "\n" + catalog.ROUTER_END)
            (root / "README.md").write_text(catalog.TABLE_START + "\n" + catalog.TABLE_END)
            m = copy.deepcopy(self.metadata)
            m.update(id="new-recipe", kind="judgment", checked=None, checked_basis=None, handoff=[])
            body = "# " + m["title"] + "\n\nA reviewed body.\n"
            (root / "body.md").write_text(body)
            (root / "header.json").write_text(json.dumps(m))
            args = ["--export-body", str(root / "body.md"), "--metadata", str(root / "header.json")]
            with patch.object(catalog, "ROOT", root):
                invalid = copy.deepcopy(m)
                invalid["handoff"] = ["missing-recipe"]
                (root / "header.json").write_text(json.dumps(invalid))
                before = (skill / "SKILL.md").read_text(), (root / "README.md").read_text()
                self.assertEqual(catalog.main(args), 1)
                self.assertFalse((skill / "recipes/new-recipe.md").exists())
                self.assertEqual(before, ((skill / "SKILL.md").read_text(), (root / "README.md").read_text()))
                (root / "header.json").write_text(json.dumps(m))
                self.assertEqual(catalog.main(args), 0)
                self.assertEqual(catalog.main(["--check"]), 0)
                self.assertEqual(catalog.main(args), 1)  # must not overwrite a public recipe
            m2, b2 = catalog.parse_recipe((skill / "recipes/new-recipe.md").read_text())
            self.assertEqual((m2, b2), (m, body))
            self.assertIn("new-recipe", (root / "README.md").read_text())
            self.assertIn(m["guardrails"][0]["text"], " ".join((skill / "SKILL.md").read_text().split()))

    def test_command_check_runs_without_optional_host_dependencies(self):
        process = subprocess.run([sys.executable, "-B", "scripts/recipe_catalog.py", "--check"],
                                 cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(process.returncode, 0, process.stderr)


if __name__ == "__main__":
    unittest.main()
