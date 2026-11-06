"""Every manifest declares the licence that NOTICE defines, and NOTICE and LICENSE ship as identical copies."""

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills/genealogy-research-recipes"
THIRD_PARTY_REF = "LicenseRef-Third-Party-Content"
EXPRESSION = f"FSL-1.1-MIT AND {THIRD_PARTY_REF}"
# openclaw.plugin.json has no license field.
LICENSED_JSON_MANIFESTS = (".claude-plugin/plugin.json", "package.json", "plugin.json")


def declared_licences():
    licences = {
        name: json.loads((ROOT / name).read_text(encoding="utf-8"))["license"] for name in LICENSED_JSON_MANIFESTS
    }
    marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
    for plugin in marketplace["plugins"]:
        licences[f"marketplace.json {plugin['name']}"] = plugin["license"]
    hermes = re.search(r"^license:\s*(.+)$", (ROOT / "plugin.yaml").read_text(encoding="utf-8"), re.MULTILINE)
    assert hermes is not None, "plugin.yaml has no license"
    licences["plugin.yaml"] = hermes.group(1).strip()
    return licences


class LicenseMetadataTests(unittest.TestCase):
    def test_every_manifest_declares_the_same_expression(self):
        licences = declared_licences()
        self.assertEqual(len(licences), 5, licences)
        self.assertEqual(set(licences.values()), {EXPRESSION}, licences)

    def test_notice_defines_the_licence_reference(self):
        notice = (ROOT / "NOTICE").read_text(encoding="utf-8")
        self.assertRegex(notice, rf"(?m)^{THIRD_PARTY_REF}$", f"NOTICE needs a section headed {THIRD_PARTY_REF}")

    def test_notice_and_license_copies_are_identical(self):
        for name in ("NOTICE", "LICENSE"):
            with self.subTest(file=name):
                self.assertEqual((ROOT / name).read_bytes(), (SKILL_DIR / name).read_bytes())


if __name__ == "__main__":
    unittest.main()
