"""Channel contents, policy failures, reproducibility and archive-only source selection."""

import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("build_dist", ROOT / "scripts/build_dist.py")
dist = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(dist)
SKILL = "skills/genealogy-research-recipes"


class BuildDistTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)

    def test_head_claude_tree_passes_policy_and_renames_notices(self):
        tree = dist.build("claude-directory", "HEAD", self.root / "claude")
        dist.check_claude(tree)
        files = dist.tree_files(tree)
        for name in (".claude-plugin/plugin.json", ".claude-plugin/icon.png", "README.md",
                     "LICENSE", "NOTICE.md", SKILL + "/SKILL.md", SKILL + "/NOTICE.md"):
            self.assertIn(name, files)
        archived = dist.archive_files(ROOT, "HEAD")
        base = ("https://github.com/Kinprove/genealogy-research-recipes/blob/"
                + dist.resolve_commit(ROOT, "HEAD") + "/" + SKILL + "/sources")
        for name in ("NOTICE", SKILL + "/NOTICE"):
            expected = dist.pin_sources(name + ".md", archived[name].decode("utf-8"), base)
            self.assertEqual(files[name + ".md"].decode("utf-8"), expected)
            self.assertNotIn(name, files)
        self.assertFalse(any(name.endswith((".py", ".js")) for name in files))
        self.assertNotIn(".claude-plugin/marketplace.json", files)

    def test_head_claude_tree_links_sources_on_github_at_the_source_commit(self):
        tree = dist.build("claude-directory", "HEAD", self.root / "claude")
        files = dist.tree_files(tree)
        self.assertFalse(any(name.startswith(dist.SOURCES) for name in files))
        self.assertLess(sum(len(data) for data in files.values()), dist.CLAUDE_MAX_BYTES)
        base = ("https://github.com/Kinprove/genealogy-research-recipes/blob/"
                + dist.resolve_commit(ROOT, "HEAD") + "/" + SKILL + "/sources/")
        archived = dist.archive_files(ROOT, "HEAD")
        for name, data in files.items():
            if name.endswith(".md"):
                text = data.decode("utf-8")
                with self.subTest(name=name):
                    self.assertNotRegex(text, r"(?<![\w./:-])sources/")
                    for link in dist.markdown_links(text):
                        if "/sources/" in link:
                            self.assertTrue(link.startswith(base), link)
                            path = SKILL + "/sources/" + link[len(base):].split("#")[0]
                            self.assertTrue(any(key.startswith(path) for key in archived), link)
        recipe = files[SKILL + "/recipes/research-documentation.md"].decode("utf-8")
        self.assertIn("](" + base + "research-documentation.md)", recipe)
        self.assertIn(base + "<recipe-id>.md", files[SKILL + "/SKILL.md"].decode("utf-8"))

    def test_other_channels_keep_sources(self):
        for target in ("hermes-catalog", "openai-plugin"):
            with self.subTest(target=target):
                result = dist.build(target, "HEAD", self.root / target)
                if target == "openai-plugin":
                    with zipfile.ZipFile(result) as archive:
                        names = archive.namelist()
                else:
                    names = list(dist.tree_files(result))
                self.assertIn(dist.SOURCES + "research-documentation.md", names)

    def test_head_hermes_tree_has_adapter_and_complete_skill(self):
        tree = dist.build("hermes-catalog", "HEAD", self.root / "hermes")
        files = dist.tree_files(tree)
        for name in ("plugin.yaml", "__init__.py", SKILL + "/SKILL.md", dist.HELPER,
                     SKILL + "/resources/beider-name-indexes.json", SKILL + "/NOTICE"):
            self.assertIn(name, files)
        for name in ("package.json", "plugin.json", "index.js", "openclaw.plugin.json"):
            self.assertNotIn(name, files)

    def test_head_openai_zip_layout_icons_and_determinism(self):
        first = dist.build("openai-plugin", "HEAD", self.root / "first")
        second = dist.build("openai-plugin", "HEAD", self.root / "second")
        self.assertEqual(first.read_bytes(), second.read_bytes())
        with zipfile.ZipFile(first) as archive:
            names = archive.namelist()
            self.assertEqual(names, sorted(names))
            self.assertEqual(len(names), len(set(names)))
            self.assertIn("plugin.json", names)
            self.assertIn(SKILL + "/SKILL.md", names)
            self.assertIn(dist.HELPER, names)
            self.assertFalse(any(set(name.split("/")) & {".claude-plugin", "tests", "evals", ".github"}
                                 for name in names))
            for name in ("plugin.yaml", "__init__.py", "index.js", "package.json", "openclaw.plugin.json"):
                self.assertNotIn(name, names)
            plugin = json.loads(archive.read("plugin.json"))
            self.assertEqual(first.name, "genealogy-research-recipes-" + plugin["version"] + ".zip")
            interface = plugin["extensions"]["com.openai"]["interface"]
            for field in ("logo", "composerIcon"):
                self.assertTrue(interface[field].startswith("./"))
                self.assertIn(interface[field][2:], names)
            for entry in archive.infolist():
                self.assertEqual(entry.date_time, (1980, 1, 1, 0, 0, 0))
                self.assertEqual(entry.external_attr >> 16, 0o100644)

    def candidate_repository(self):
        """Commit the candidate files in a disposable repo, including uncommitted corrections."""
        repository = self.root / "source"
        names = ["README.md", "LICENSE", "NOTICE", "assets/banner.png", "assets/logo.png",
                 ".claude-plugin/plugin.json", ".claude-plugin/icon.png", "plugin.json",
                 "plugin.yaml", "__init__.py", dist.HELPER,
                 SKILL + "/SKILL.md", SKILL + "/CHANGELOG.md", SKILL + "/LICENSE", SKILL + "/NOTICE"]
        for folder, extension in (("recipes", "md"), ("sources", "md"), ("resources", "json")):
            names.extend(path.relative_to(ROOT).as_posix()
                         for path in (ROOT / SKILL / folder).rglob("*." + extension))
        for name in names:
            target = repository / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, target)
        self.git(repository, "init", "--quiet")
        self.commit(repository)
        return repository

    def git(self, repository, *arguments):
        return subprocess.run(["git", *arguments], cwd=repository, capture_output=True,
                              text=True, check=True).stdout.strip()

    def commit(self, repository):
        self.git(repository, "add", ".")
        return self.git(repository, "-c", "user.name=Distribution test",
                        "-c", "user.email=distribution@example.invalid", "-c", "commit.gpgsign=false",
                        "commit", "--quiet", "-m", "Fixture")

    def test_candidate_built_trees_and_zip_have_resolvable_links(self):
        repository = self.candidate_repository()
        for target in dist.TARGETS:
            with self.subTest(target=target):
                result = dist.build(target, "HEAD", self.root / target, repository)
                dist.check_links(result)

    def test_older_commit_ignores_newer_modified_and_untracked_files(self):
        repository = self.candidate_repository()
        older = self.git(repository, "rev-parse", "HEAD")
        before = {target: dist.build(target, older, self.root / (target + "-before"), repository)
                  for target in dist.TARGETS}
        (repository / "README.md").write_text("newer committed README\n", encoding="utf-8")
        (repository / SKILL / "recipes/newer.md").write_text("newer commit\n", encoding="utf-8")
        self.commit(repository)
        (repository / "README.md").write_text("dirty README\n", encoding="utf-8")
        (repository / SKILL / "recipes/untracked.md").write_text("untracked\n", encoding="utf-8")
        for target in dist.TARGETS:
            with self.subTest(target=target):
                after = dist.build(target, older, self.root / (target + "-after"), repository)
                if target == "openai-plugin":
                    self.assertEqual(after.read_bytes(), before[target].read_bytes())
                else:
                    self.assertEqual(dist.tree_files(after), dist.tree_files(before[target]))
                    readme = (after / "README.md").read_bytes()
                    self.assertNotIn(b"newer committed", readme)
                    self.assertNotIn(b"dirty", readme)
                    if target == "hermes-catalog":
                        self.assertEqual(readme, (ROOT / "README.md").read_bytes())
                    self.assertFalse((after / SKILL / "recipes/newer.md").exists())
                    self.assertFalse((after / SKILL / "recipes/untracked.md").exists())

    def test_missing_allowlisted_input_is_refused(self):
        repository = self.candidate_repository()
        (repository / "assets/banner.png").unlink()
        self.commit(repository)
        with self.assertRaisesRegex(ValueError, "allowlisted pattern matches nothing: assets/banner.png"):
            dist.build("claude-directory", "HEAD", self.root / "out", repository)
        self.assertFalse((self.root / "out").exists())


class ClaudePolicyTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.write(".claude-plugin/plugin.json", b'{"name":"example"}')

    def write(self, name, data):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)

    def test_python_file_is_refused(self):
        self.write("script.py", b"print('example')\n")
        with self.assertRaisesRegex(ValueError, "disallowed file type"):
            dist.check_claude(self.root)

    def test_shebang_text_is_refused(self):
        self.write("script.txt", b"#!/bin/sh\n")
        with self.assertRaisesRegex(ValueError, "shebang"):
            dist.check_claude(self.root)

    def test_package_json_is_refused(self):
        self.write("package.json", b"{}")
        with self.assertRaisesRegex(ValueError, "package-manager file"):
            dist.check_claude(self.root)

    def test_non_utf8_text_is_refused(self):
        self.write("bad.txt", b"\xff")
        with self.assertRaisesRegex(ValueError, "not UTF-8"):
            dist.check_claude(self.root)

    def test_extensionless_notice_is_refused(self):
        self.write("NOTICE", b"attribution\n")
        with self.assertRaisesRegex(ValueError, "disallowed file type"):
            dist.check_claude(self.root)

    def test_other_extensionless_files_are_refused(self):
        self.write("program", b"example\n")
        with self.assertRaisesRegex(ValueError, "disallowed file type"):
            dist.check_claude(self.root)

    def test_all_package_manager_names_are_refused(self):
        for name in ("package-lock.json", "npm-shrinkwrap.json", "yarn.lock", "pnpm-lock.yaml",
                     "bun.lock", "bun.lockb", "requirements.txt", "requirements-dev.txt",
                     "pyproject.toml", "Pipfile", "Pipfile.lock", "poetry.lock", "uv.lock"):
            with self.subTest(name=name):
                self.write(name, b"{}")
                with self.assertRaisesRegex(ValueError, "package-manager file"):
                    dist.check_claude(self.root)
                (self.root / name).unlink()

    def test_oversized_tree_is_refused(self):
        self.write("large.md", b"x" * (dist.CLAUDE_MAX_BYTES + 1))
        with self.assertRaisesRegex(ValueError, "the limit is"):
            dist.check_claude(self.root)

    def test_unknown_manifest_field_is_refused(self):
        self.write(".claude-plugin/plugin.json", b'{"name":"example","extensions":{}}')
        with self.assertRaisesRegex(ValueError, "undocumented fields: extensions"):
            dist.check_claude(self.root)

    def test_documented_directory_fields_and_file_types_are_allowed(self):
        plugin = {"name": "example", "icon": "./.claude-plugin/icon.png"}
        plugin.update({key: "https://example.org" for key in (
            "documentationUrl", "supportUrl", "privacyPolicyUrl", "termsOfServiceUrl")})
        self.write(".claude-plugin/plugin.json", json.dumps(plugin).encode("utf-8"))
        for name in ("LICENSE", "README.md", ".gitignore", "NOTICE.md", "file.txt", "file.json",
                     "file.yaml", "file.yml"):
            self.write(name, b"example\n")
        for extension in dist.IMAGES:
            self.write("image" + extension, b"\xffimage")
        dist.check_claude(self.root)


class PinSourcesTests(unittest.TestCase):
    BASE = "https://github.com/o/r/blob/abc/" + SKILL + "/sources"

    def test_relative_links_and_mentions_are_pinned(self):
        text = ("[a](../sources/x.md#credits) [b](<../sources/x.md>) [c](../recipes/y.md)\n"
                "Read `sources/<slug>.md` and the `sources/` folder; resources/z.json stays.\n"
                "[web](https://example.org/sources/x.md)\n")
        pinned = dist.pin_sources(SKILL + "/recipes/y.md", text, self.BASE)
        self.assertIn("[a](" + self.BASE + "/x.md#credits)", pinned)
        self.assertIn("[b](<" + self.BASE + "/x.md>)", pinned)
        self.assertIn("[c](../recipes/y.md)", pinned)
        self.assertIn("`" + self.BASE + "/<slug>.md`", pinned)
        self.assertIn("`" + self.BASE + "/` folder", pinned)
        self.assertIn("resources/z.json", pinned)
        self.assertIn("https://example.org/sources/x.md", pinned)

    def test_root_relative_folder_link_is_pinned(self):
        pinned = dist.pin_sources("README.md", "[s](" + SKILL + "/sources/)", self.BASE)
        self.assertEqual(pinned, "[s](" + self.BASE + "/)")


class DistributionLinkTests(unittest.TestCase):
    def test_indented_list_links_are_checked(self):
        for line in ("continued [link](missing.md)", "- Nested [link](missing.md)"):
            with self.subTest(line=line), self.assertRaisesRegex(ValueError, "missing target"):
                text = "1. Parent item\n    " + line + "\n"
                dist.check_link_files({"README.md": text.encode("utf-8")})

    def test_missing_and_escaping_links_are_refused(self):
        for link, error in (("missing.md", "missing target"), ("../outside.md", "outside the distribution")):
            with self.subTest(link=link), self.assertRaisesRegex(ValueError, error):
                dist.check_link_files({"README.md": ("[link](" + link + ")").encode("utf-8")})

    def test_links_to_the_distribution_root_resolve(self):
        for link in ("./", "/", "skills/.."):
            with self.subTest(link=link):
                dist.check_link_files({"README.md": ("[root](" + link + ")").encode("utf-8"),
                                       "skills/x.md": b""})

    def test_inline_reference_html_and_image_links(self):
        text = ('[inline](docs/file(copy).md#heading) [code label](docs/space%20name.md)\n'
                '[`code`](docs/file(copy).md) [space](<docs/space name.md>)\n'
                '[full][ref] [short][] [shortcut] ![image](assets/image.png)\n'
                '<a href="docs/file(copy).md">HTML</a>\n\n'
                '[ref]: docs/file(copy).md\n[short]: docs/file(copy).md\n'
                '[shortcut]: docs/file(copy).md\n')
        files = {"README.md": text.encode("utf-8"), "docs/file(copy).md": b"# Heading\n",
                 "docs/space name.md": b"text\n", "assets/image.png": b"image"}
        self.assertEqual(len(dist.markdown_links(text)), 9)
        dist.check_link_files(files)
        del files["docs/file(copy).md"]
        with self.assertRaisesRegex(ValueError, "missing target"):
            dist.check_link_files(files)

    def test_code_metadata_and_external_links_are_ignored(self):
        text = ('---\nexample: "[link](missing.md)"\n---\n'
                '```md\n[code](missing.md)\n```\n`[inline](missing.md)`\n'
                '    [indented](missing.md)\n<!-- [comment](missing.md) -->\n'
                '[web](https://example.org) [mail](mailto:example@example.org) [self](#heading)\n')
        dist.check_link_files({"README.md": text.encode("utf-8")})


if __name__ == "__main__":
    unittest.main()
