"""Guard the CI credential boundary and reproducible tool installs."""

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CiToolTests(unittest.TestCase):
    def test_every_checkout_disables_persisted_credentials(self):
        workflow = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
        checkouts = re.findall(
            r"(?m)^      - uses: actions/checkout@[^\n]+\n((?:        [^\n]*\n|\n)*)",
            workflow,
        )
        self.assertTrue(checkouts, "No checkout steps checked")
        self.assertEqual(len(checkouts), workflow.count("uses: actions/checkout@"))
        for config in checkouts:
            with self.subTest(config=config):
                self.assertRegex(config, r"(?m)^        with:\n")
                self.assertEqual(re.findall(r"(?m)^          persist-credentials: (\S+)\s*$", config), ["false"])

    def test_ci_and_maintainers_use_the_locked_tools_without_install_scripts(self):
        workflow = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
        maintainers = (ROOT / "MAINTAINERS.md").read_text(encoding="utf-8")
        for text in (workflow, maintainers):
            self.assertNotRegex(text, r"\bnpx\b|\bnpm (?:install|i) -g\b")
            self.assertIn("npm ci --prefix ci-tools --ignore-scripts", text)
        # Check every install, so a later step cannot silently reenable scripts.
        installs = re.findall(r"(?m)^.*\bnpm (?:ci|install|i)\b.*$", workflow)
        self.assertTrue(installs)
        for install in installs:
            with self.subTest(install=install):
                self.assertRegex(
                    install,
                    r"^\s*(?:run: )?npm ci --prefix (?:ci-tools|tests/markdown-links) --ignore-scripts\s*$",
                )
                self.assertNotIn("--ignore-scripts=false", install)
        self.assertIn("node ci-tools/node_modules/@anthropic-ai/claude-code/cli-wrapper.cjs plugin validate", workflow)
        self.assertIn("clawhub package validate . --openclaw ci-tools/node_modules/openclaw", workflow)
        self.assertIn("ci-tools/node_modules/.bin/markdownlint-cli2", workflow)
        self.assertIn('ci-tools/node_modules/.bin" >> "$GITHUB_PATH"', workflow)
        self.assertIn("ci-tools/node_modules/.bin/clawhub package publish", maintainers)

    def test_lock_covers_exact_tools_and_integrity_checked_transitive_archives(self):
        packages = (
            ("ci-tools", {"openclaw", "@anthropic-ai/claude-code", "markdownlint-cli2", "clawhub"}),
            ("tests/markdown-links", {"github-slugger", "markdown-it", "parse5"}),
        )
        for directory, expected in packages:
            with self.subTest(package=directory):
                package = json.loads((ROOT / directory / "package.json").read_text(encoding="utf-8"))
                lock = json.loads((ROOT / directory / "package-lock.json").read_text(encoding="utf-8"))
                self.assertIs(package["private"], True)
                tools = package["devDependencies"]
                self.assertEqual(set(tools), expected)
                self.assertEqual(lock["packages"][""]["devDependencies"], tools)
                for name, version in tools.items():
                    with self.subTest(tool=name):
                        self.assertRegex(version, r"^\d+\.\d+\.\d+$")
                        self.assertEqual(lock["packages"]["node_modules/" + name]["version"], version)
                for name, entry in lock["packages"].items():
                    if not name or entry.get("inBundle"):
                        continue  # Bundled bytes are covered by the containing archive's integrity.
                    with self.subTest(dependency=name):
                        self.assertTrue(entry["resolved"].startswith("https://registry.npmjs.org/"))
                        self.assertRegex(entry["integrity"], r"^sha512-[A-Za-z0-9+/]+={0,2}$")


if __name__ == "__main__":
    unittest.main()
