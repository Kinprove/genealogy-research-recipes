"""Every host manifest and the skill's own version line must carry the same release version."""

import datetime
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JSON_MANIFESTS = (".claude-plugin/plugin.json", "openclaw.plugin.json", "package.json", "plugin.json")
SKILL = ROOT / "skills/genealogy-research-recipes/SKILL.md"
SKILL_VERSION_LINE = re.compile(r"^This copy is version (\S+), released (\d{4}-\d{2}-\d{2})\.$", re.MULTILINE)


class ManifestVersionTests(unittest.TestCase):
    def test_all_manifests_share_one_version(self):
        versions = {
            name: json.loads((ROOT / name).read_text(encoding="utf-8"))["version"] for name in JSON_MANIFESTS
        }
        hermes = re.search(r"^version:\s*(\S+)", (ROOT / "plugin.yaml").read_text(encoding="utf-8"), re.MULTILINE)
        assert hermes is not None, "plugin.yaml has no version"
        versions["plugin.yaml"] = hermes.group(1)

        stamps = SKILL_VERSION_LINE.findall(SKILL.read_text(encoding="utf-8"))
        self.assertEqual(len(stamps), 1, "SKILL.md must state its version and release date exactly once")
        skill_version, released = stamps[0]
        versions["SKILL.md"] = skill_version
        datetime.date.fromisoformat(released)

        self.assertEqual(len(set(versions.values())), 1, versions)
        self.assertEqual(versions["package.json"], "1.9.2")


if __name__ == "__main__":
    unittest.main()
