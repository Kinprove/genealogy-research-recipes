"""Every host manifest, the skill's version line and the release history agree on the current release."""

import datetime
import importlib.util
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JSON_MANIFESTS = (".claude-plugin/plugin.json", "openclaw.plugin.json", "package.json", "plugin.json")
SKILL = ROOT / "skills/genealogy-research-recipes/SKILL.md"
SKILL_VERSION_LINE = re.compile(r"^This copy is version (\S+), released (\d{4}-\d{2}-\d{2})\.$", re.MULTILINE)
CHANGELOG = ROOT / "skills/genealogy-research-recipes/CHANGELOG.md"
CHANGELOG_ROW = re.compile(r"^\| (\d+\.\d+\.\d+) \| (\d{4}-\d{2}-\d{2}) \| (\d{4}-\d{2}-\d{2}) \|$", re.MULTILINE)
EXPECTED_VERSION = "1.19.0"
SPEC = importlib.util.spec_from_file_location("bump_version", ROOT / "scripts/bump_version.py")
release = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(release)
# Reviewed first-availability days (UTC) of the versions released before the history file existed.
EARLIER_RELEASES = {
    "1.12.0": "2026-11-06", "1.11.0": "2026-11-06", "1.10.0": "2026-11-05", "1.9.2": "2026-11-04",
    "1.9.1": "2026-11-04", "1.9.0": "2026-11-04", "1.8.0": "2026-11-04", "1.7.2": "2026-11-03",
    "1.7.1": "2026-11-03", "1.7.0": "2026-11-02", "1.6.4": "2026-10-27", "1.6.3": "2026-10-27",
    "1.6.2": "2026-10-27", "1.6.1": "2026-10-22", "1.6.0": "2026-10-22", "1.5.0": "2026-10-20",
    "1.4.0": "2026-10-18", "1.3.0": "2026-10-18", "1.2.0": "2026-10-07", "1.1.1": "2026-10-06",
    "1.1.0": "2026-10-06", "1.0.0": "2026-10-04", "0.2.2": "2026-10-04", "0.2.0": "2026-10-04",
}


def skill_stamp():
    stamps = SKILL_VERSION_LINE.findall(SKILL.read_text(encoding="utf-8"))
    assert len(stamps) == 1, "SKILL.md must state its version and release date exactly once"
    return stamps[0]


def history_rows():
    """(version, released, becomes MIT on) strings for each table row, in file order."""
    return CHANGELOG_ROW.findall(CHANGELOG.read_text(encoding="utf-8"))


def version_key(version):
    return tuple(int(part) for part in version.split("."))


class ManifestVersionTests(unittest.TestCase):
    def test_all_manifests_share_one_version(self):
        versions = {
            name: json.loads((ROOT / name).read_text(encoding="utf-8"))["version"] for name in JSON_MANIFESTS
        }
        hermes = re.search(r"^version:\s*(\S+)", (ROOT / "plugin.yaml").read_text(encoding="utf-8"), re.MULTILINE)
        assert hermes is not None, "plugin.yaml has no version"
        versions["plugin.yaml"] = hermes.group(1)

        skill_version, released = skill_stamp()
        versions["SKILL.md"] = skill_version
        day = datetime.date.fromisoformat(released)
        release.version_key(skill_version)
        release.validate_release_date(day, release.previous_tag_date(ROOT, skill_version))

        self.assertEqual(len(set(versions.values())), 1, versions)
        self.assertEqual(versions["package.json"], EXPECTED_VERSION)


class ManifestDescriptionTests(unittest.TestCase):
    def test_openai_listing_category_and_display_limits(self):
        plugin = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
        interface = plugin["extensions"]["com.openai"]["interface"]
        self.assertEqual(interface["category"], "Education & Research")
        for field in ("displayName", "shortDescription"):
            with self.subTest(field=field):
                self.assertTrue(interface[field])
                self.assertLessEqual(len(interface[field]), 30)

    def test_all_hosts_carry_one_description(self):
        descriptions = {
            name: json.loads((ROOT / name).read_text(encoding="utf-8"))["description"] for name in JSON_MANIFESTS
        }
        marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
        descriptions[".claude-plugin/marketplace.json"] = marketplace["plugins"][0]["description"]
        for name, pattern in (
            ("plugin.yaml", r"^description:\s*(.+?)\s*$"),
            ("index.js", r'^\s*description:\s*"([^"]+)"'),
            ("__init__.py", r'^\s*description="([^"]+)"'),
        ):
            match = re.search(pattern, (ROOT / name).read_text(encoding="utf-8"), re.MULTILINE)
            assert match is not None, f"{name} has no description"
            descriptions[name] = match.group(1)
        self.assertEqual(len(set(descriptions.values())), 1, descriptions)

    def test_package_json_carries_the_listing_metadata(self):
        package = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
        marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
        plugin = marketplace["plugins"][0]
        for field in ("keywords", "homepage", "author"):
            with self.subTest(field=field):
                self.assertEqual(package.get(field), plugin[field])
        self.assertEqual(package["peerDependencies"]["openclaw"], package["openclaw"]["compat"]["pluginApi"])
        self.assertIs(package["peerDependenciesMeta"]["openclaw"]["optional"], True)


class ReleaseHistoryTests(unittest.TestCase):
    def test_newest_row_is_this_release(self):
        rows = history_rows()
        self.assertTrue(rows, f"no release rows found in {CHANGELOG}")
        self.assertEqual(
            rows[0][:2],
            skill_stamp(),
            "add a row for this release to the top of CHANGELOG.md with the SKILL.md release date",
        )

    def test_versions_descend_and_dates_never_increase(self):
        rows = history_rows()
        for newer, older in zip(rows, rows[1:]):
            with self.subTest(newer=newer[0], older=older[0]):
                self.assertGreater(version_key(newer[0]), version_key(older[0]))
                self.assertGreaterEqual(newer[1], older[1])

    def test_each_version_becomes_mit_on_its_second_anniversary(self):
        for version, released, mit in history_rows():
            with self.subTest(version=version):
                day = datetime.date.fromisoformat(released)
                try:
                    anniversary = day.replace(year=day.year + 2)
                except ValueError:
                    anniversary = day.replace(year=day.year + 2, day=28)
                self.assertEqual(datetime.date.fromisoformat(mit), anniversary)

    def test_earlier_releases_keep_their_reviewed_dates(self):
        rows = {version: released for version, released, _ in history_rows()}
        for version, released in EARLIER_RELEASES.items():
            with self.subTest(version=version):
                self.assertEqual(rows.get(version), released, "keep every earlier row; add new releases above them")


if __name__ == "__main__":
    unittest.main()
