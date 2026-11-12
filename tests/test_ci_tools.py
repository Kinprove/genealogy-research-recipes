"""Guard the CI credential boundary and reproducible tool installs."""

import json
import os
import re
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CiToolTests(unittest.TestCase):
    def test_every_checkout_disables_persisted_credentials(self):
        for path in sorted((ROOT / ".github/workflows").glob("*.y*ml")):
            workflow = path.read_text(encoding="utf-8")
            checkouts = re.findall(
                r"(?m)^      - uses: actions/checkout@[^\n]+\n((?:        [^\n]*\n|\n)*)",
                workflow,
            )
            with self.subTest(workflow=path.name):
                self.assertTrue(checkouts, "No checkout steps checked")
                self.assertEqual(len(checkouts), workflow.count("uses: actions/checkout@"))
            for config in checkouts:
                with self.subTest(workflow=path.name, config=config):
                    self.assertRegex(config, r"(?m)^        with:\n")
                    self.assertEqual(re.findall(r"(?m)^          persist-credentials: (\S+)\s*$", config), ["false"])

    def test_ci_and_maintainers_use_the_locked_tools_without_install_scripts(self):
        workflow = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
        maintainers = (ROOT / "MAINTAINERS.md").read_text(encoding="utf-8")
        workflows = {path.name: path.read_text(encoding="utf-8")
                     for path in sorted((ROOT / ".github/workflows").glob("*.y*ml"))}
        for text in (*workflows.values(), maintainers):
            self.assertNotRegex(text, r"\bnpx\b|\bnpm (?:install|i) -g\b")
        # The distribution workflow needs only Git and standard-library Python.
        for name, text in workflows.items():
            if name != "dist.yml":
                self.assertIn("npm ci --prefix ci-tools --ignore-scripts", text)
        self.assertIn("npm ci --prefix ci-tools --ignore-scripts", maintainers)
        # Check every install, so a later step cannot silently reenable scripts.
        installs = re.findall(r"(?m)^.*\bnpm (?:ci|install|i)\b.*$", "\n".join(workflows.values()))
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

    def test_model_workflow_launcher_uses_locked_wrapper_and_preserves_arguments(self):
        workflow = (ROOT / ".github/workflows/behavioural-evals.yml").read_text(encoding="utf-8")
        match = re.search(r"<<'CLAUDE_SHIM'\n(.*?)^          CLAUDE_SHIM$", workflow, re.M | re.S)
        self.assertIsNotNone(match)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            launcher = root / "claude"
            launcher.write_text(textwrap.dedent(match.group(1)), encoding="utf-8")
            launcher.chmod(0o755)
            node = root / "node"
            node.write_text(f"#!{sys.executable}\nimport json, sys\nprint(json.dumps(sys.argv[1:]))\n", encoding="utf-8")
            node.chmod(0o755)
            workspace = root / "checkout with spaces"
            environment = {**os.environ, "PATH": str(root) + os.pathsep + os.environ["PATH"],
                           "GITHUB_WORKSPACE": str(workspace)}
            wrapper = str(workspace / "ci-tools/node_modules/@anthropic-ai/claude-code/cli-wrapper.cjs")
            for arguments in (["--version"], ["-p", "argument with spaces\nand a newline"]):
                result = subprocess.run([str(launcher), *arguments], env=environment,
                                        capture_output=True, text=True, check=True)
                self.assertEqual(json.loads(result.stdout), [wrapper, *arguments])

    def test_model_workflow_ignores_other_labels(self):
        workflow = (ROOT / ".github/workflows/behavioural-evals.yml").read_text(encoding="utf-8")
        group = re.search(r"(?m)^concurrency:\n  group: (.+)$", workflow)
        condition = re.search(r"(?ms)^  credentials:\n    if: >-\n(.*?)\n    runs-on:", workflow)
        self.assertIsNotNone(group)
        self.assertIsNotNone(condition)
        group, condition = group.group(1), condition.group(1)
        # Another label must neither cancel a running evaluation nor start a new one.
        self.assertIn("github.event.action == 'labeled' && github.event.label.name != 'behavioural-evals' "
                      "&& format('-{0}', github.run_id) || ''", group)
        self.assertIn("(github.event.action != 'labeled' || github.event.label.name == 'behavioural-evals')",
                      condition)

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
