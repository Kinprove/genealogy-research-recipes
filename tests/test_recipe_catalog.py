"""Catalog invariants and mutation tests for the authoring/export boundary."""

import copy
import datetime as dt
import importlib.util
import io
import json
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
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

    def assert_invalid(self, metadata, message, body=None):
        with self.assertRaisesRegex(catalog.CatalogError, message):
            catalog.validate_header(metadata, body or self.body, metadata["id"] + ".md", self.today)

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
        for field in ("extra", "triggers"):  # triggers was retired: only scope.tasks routes
            m = copy.deepcopy(self.metadata)
            m[field] = ["a phrase"]
            self.assert_invalid(m, "header fields")
        for header in ('id: "one"\nid: "two"', 'id: [broken', 'id: plain-yaml'):
            with self.subTest(header=header), self.assertRaises(catalog.CatalogError):
                catalog.parse_recipe("---\n" + header + "\n---\n# Body\n")

    def test_schema_rejects_empty_rules_bad_ids_and_wrong_titles(self):
        for key, value, error in (("guardrails", [], "guardrails"), ("id", "../escape", "invalid id"),
                                  ("title", "Other title", "title differs")):
            m = copy.deepcopy(self.metadata)
            m[key] = value
            self.assert_invalid(m, error)

    def test_tasks_add_to_the_summary_and_only_full_entries_need_them(self):
        m = copy.deepcopy(self.metadata)
        m["router"]["tier"] = "full"
        m["scope"]["tasks"] = []
        self.assert_invalid(m, "full router entries need tasks")
        m["router"]["tier"] = "pointer"
        catalog.validate_header(m, self.body, m["id"] + ".md", self.today)
        m["summary"] = "Route a birth, marriage or death by county, successor state and record type."
        # The whole summary, any case, and the summary cut at commas add nothing to route on.
        for task in (m["summary"].upper(), "marriage or death by county", "successor state and record type."):
            m["scope"]["tasks"] = [task]
            with self.subTest(task=task):
                self.assert_invalid(m, "task repeats the summary")
        m["scope"]["tasks"] = ["Search a county marriage register by the groom's parish"]
        catalog.validate_header(m, self.body, m["id"] + ".md", self.today)

    def test_every_guardrail_is_an_excerpt_of_the_body(self):
        m = copy.deepcopy(self.metadata)
        body = ("# " + m["title"] + "\n\nNever treat a title match as\nproof of the   contents. "
                "Keep unchecked cases.\n")
        m["guardrails"] = [{"id": "T-01", "text": "Never treat a title match as proof of the contents."}]
        catalog.validate_header(m, body, m["id"] + ".md", self.today)  # a line wrap and extra spaces
        for text in ("never treat a title match as proof of the contents.", "Never treat a title as proof."):
            m["guardrails"][0]["text"] = text
            with self.subTest(text=text):
                self.assert_invalid(m, "guardrail T-01 is not an excerpt", body)
        # Later guardrails are checked too, not only the core rule that the router prints.
        m["guardrails"] = [{"id": "T-01", "text": "Keep unchecked cases."},
                           {"id": "T-02", "text": "A rule the body never states."}]
        self.assert_invalid(m, "guardrail T-02 is not an excerpt", body)

    def test_router_prints_tasks_in_both_tiers_and_the_core_guardrail_for_full_entries(self):
        full = copy.deepcopy(next(item for item in self.items if item[0]["router"]["tier"] == "full"))
        pointer = copy.deepcopy(next(item for item in self.items if item[0]["router"]["tier"] == "pointer"))
        pointer[0]["scope"]["tasks"] = []
        head, tail = catalog.render_router([full, pointer]).split("## More recipes by topic")
        self.assertIn("*Use for:* " + full[0]["scope"]["tasks"][0].split()[0], head)
        self.assertIn("*Core guardrail:*", head)
        self.assertNotIn("*Use for:*", tail)
        self.assertNotIn("*Core guardrail:*", tail)
        pointer[0]["scope"]["tasks"] = ["Search auction lots", "Read the lot photographs"]
        tail = catalog.render_router([full, pointer]).split("## More recipes by topic")[1]
        self.assertIn("*Use for:* Search auction lots; Read the lot photographs", tail)

    def test_dangling_references_fail_in_body_and_handoff(self):
        for reference in ("[other](no-such-recipe.md)", "**`recipes/no-such-recipe.md`**",
                          "recipe **no-such-recipe**", "**recipes/no-such-recipe.md**",
                          "when this recipe names `russian-empire-immigration-research`",
                          "[other](./no-such-recipe.md)", "[other][r]\n\n[r]: no-such-recipe.md",
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

    def test_removing_a_recipe_can_regenerate_its_stale_old_catalog_entry(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skill = root / catalog.SKILL_PATH
            skill.mkdir(parents=True)
            keep, remove = self.items[:2]
            (skill / "SKILL.md").write_text(catalog.render_router([keep, remove]))
            (root / "README.md").write_text(catalog.render_capabilities([keep, remove]))
            outputs = list(catalog.generated_files(root, [keep]))
            for path, text in outputs:
                self.assertNotIn(remove[0]["id"], text)
                path.write_text(text)
            self.assertEqual(outputs, list(catalog.generated_files(root, [keep])))

    def test_jewishgen_uses_actual_documentation_checks_and_platform_freshness(self):
        m, body = next(item for item in self.items if item[0]["id"] == "jewishgen-search-family-reconstruction")
        self.assertEqual(m["kind"], "platform")
        self.assertIn("jewishgen", m["scope"]["platforms"])
        expired = dt.date.fromisoformat(m["checked"]) + dt.timedelta(days=catalog.MAX_PLATFORM_AGE_DAYS + 1)
        with self.assertRaisesRegex(catalog.CatalogError, "older than"):
            catalog.validate_header(m, body, m["id"] + ".md", expired)
        m = copy.deepcopy(m)
        m.update(kind="records", checked="2009-08-18", checked_basis="opened 2009-08-18")
        with self.assertRaisesRegex(catalog.CatalogError, "topic opening date"):
            catalog.load_catalog(replacement=(m["id"] + ".md", catalog.emit_recipe(m, body)))

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
        m["checked"] = (date - dt.timedelta(days=1)).isoformat()  # never the basis date, even on a recheck day
        with self.assertRaisesRegex(catalog.CatalogError, "differs from checked_basis"):
            catalog.validate_header(m, body, m["id"] + ".md", self.today)
        m["checked"], m["checked_basis"] = None, None
        with self.assertRaisesRegex(catalog.CatalogError, "dated source check"):
            catalog.validate_header(m, body, m["id"] + ".md", self.today)
        m["checked"], m["checked_basis"] = self.today.isoformat(), "published " + self.today.isoformat()
        with self.assertRaisesRegex(catalog.CatalogError, "not a publication"):
            catalog.validate_header(m, body, m["id"] + ".md", self.today)
        # Sidecars record a dated reading as "read YYYY-MM-DD".
        m["checked_basis"] = "read " + self.today.isoformat()
        catalog.validate_header(m, body, m["id"] + ".md", self.today)

    def test_expiring_platform_checks_are_announced_once_before_ci_fails(self):
        platform, _ = next(item for item in self.items if item[0]["kind"] == "platform")
        records, _ = next(item for item in self.items if item[0]["kind"] == "records")
        today = dt.date(2027, 3, 1)
        fake = []
        for n in range(13):  # more than the ten warning annotations GitHub keeps per step
            days_left = catalog.WARN_DAYS + 1 if n == 12 else catalog.WARN_DAYS - n
            m = copy.deepcopy(platform)
            m.update(id=f"platform-{n}", checked=(
                today + dt.timedelta(days=days_left - catalog.MAX_PLATFORM_AGE_DAYS)).isoformat())
            fake.append((m, ""))
        old_records = dict(copy.deepcopy(records), checked="2000-01-01")
        fake.append((old_records, ""))
        due = dict(catalog.expiring_checks(fake, today))
        self.assertEqual(sorted(due), sorted(f"platform-{n}" for n in range(12)))
        self.assertEqual(due["platform-0"], today + dt.timedelta(days=catalog.WARN_DAYS))
        out = io.StringIO()
        with patch.object(catalog, "load_catalog", return_value=fake), \
                patch.object(catalog, "generated_files", return_value=[]), \
                patch.object(catalog, "utc_today", return_value=today), redirect_stdout(out):
            self.assertEqual(catalog.main(["--check"]), 0)
        warnings = [line for line in out.getvalue().splitlines() if line.startswith("::warning ")]
        self.assertEqual(len(warnings), 1)
        for n in range(12):
            self.assertIn(f"platform-{n} valid until {due[f'platform-{n}']}", warnings[0])
        self.assertNotIn("platform-12", warnings[0])
        self.assertNotIn(old_records["id"], warnings[0])

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
            m.update(id="new-recipe", kind="judgment", checked=None, checked_basis=None, handoff=[],
                     guardrails=[{"id": "NEW-01", "text": "Quote the reviewed rule."}])
            body = "# " + m["title"] + "\n\nA reviewed body. Quote the reviewed rule.\n"
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
