"""Recipes and sources link over https unless an entry says the host is http only."""

import importlib.util
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('provenance', ROOT / 'scripts/provenance.py')
PROVENANCE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PROVENANCE)
SKILL_DIR = ROOT / "skills/genealogy-research-recipes"
HTTP = re.compile(r"http://")
# The original address inside an archive capture URL keeps its own scheme.
ARCHIVED = re.compile(r"web\.archive\.org/web/\d+(?:[a-z]{2}_)?/$")
MARKER = "http only"


def plain_http_links(text):
    # The ledger mirrors the exact bibliography URLs. Its own validator enforces
    # equality; read the original prose for the reviewed "http only" qualification.
    text, _ = PROVENANCE.split_ledger(text)
    problems = []
    for number, line in enumerate(text.splitlines(), 1):
        if MARKER in line:
            continue
        for match in HTTP.finditer(line):
            if not ARCHIVED.search(line[: match.start()]):
                problems.append((number, line[match.start(): match.start() + 80]))
    return problems


class HttpsLinkTests(unittest.TestCase):
    def test_recipes_and_sources_use_https(self):
        paths = sorted((SKILL_DIR / "recipes").glob("*.md")) + sorted((SKILL_DIR / "sources").glob("*.md"))
        self.assertTrue(paths)
        problems = [
            f"{path.relative_to(ROOT).as_posix()}:{number}: {snippet}"
            for path in paths
            for number, snippet in plain_http_links(path.read_text(encoding="utf-8"))
        ]
        self.assertEqual(problems, [], "\n".join(problems))

    def test_rule_allows_archived_originals_and_marked_entries_only(self):
        text = "\n".join((
            "[a](https://web.archive.org/web/20251104212945/http://example.org/)",
            "[b](https://web.archive.org/web/20251104212945id_/http://example.org/)",
            "[c](http://example.org/) (http only: no https response)",
            "[d](http://example.org/)",
            "[e](http://web.archive.org/web/2025/https://example.org/)",
        ))
        self.assertEqual([number for number, _ in plain_http_links(text)], [4, 5])

    def test_ledger_copies_keep_the_original_http_qualification(self):
        source = ('## Sources\n\n- **S1:** [A](http://example.org/) '
                  '(http only: no https response).\n\n## Credits\n')
        ledger = PROVENANCE.migrate(source, '# Example\n')
        self.assertEqual(plain_http_links(PROVENANCE.attach_ledger(source, ledger)), [])
        source = source.replace('(http only: no https response)', '')
        self.assertEqual(len(plain_http_links(PROVENANCE.attach_ledger(source, ledger))), 1)


if __name__ == "__main__":
    unittest.main()
