"""Every sources file ends with one Credits list, and every Credits line ends with its rights class."""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "skills/genealogy-research-recipes/sources"
CREDITS_HEADING = "## Credits"
# Each Credits bullet: "- <source> — <rights statement> (<class>)", with the classes NOTICE defines.
CREDIT_LINE = re.compile(r"^- \S.* — .*\S \((kinprove-original|quoted|adapted)\)$")


def credit_bullets(text):
    """Return the Credits bullets, each with its indented continuation lines joined.

    Raise ValueError when the file has no Credits section, more than one, a section after it,
    or anything other than one bullet list inside it.
    """
    lines = text.splitlines()
    starts = [index for index, line in enumerate(lines) if line == CREDITS_HEADING]
    if len(starts) != 1:
        raise ValueError(f"needs exactly one `{CREDITS_HEADING}` heading, found {len(starts)}")
    body = lines[starts[0] + 1 :]
    if any(line.startswith("#") for line in body):
        raise ValueError(f"`{CREDITS_HEADING}` must be the last section")
    while body and not body[0].strip():
        body.pop(0)
    while body and not body[-1].strip():
        body.pop()
    bullets = []
    for line in body:
        if line.startswith("- "):
            bullets.append(line)
        elif bullets and line.startswith("  ") and line.strip():
            bullets[-1] += " " + line.strip()
        else:
            raise ValueError(f"Credits must be one bullet list with no blank lines; unexpected line {line!r}")
    if not bullets:
        raise ValueError("the Credits list is empty")
    return bullets


def unclassed(bullets):
    return [bullet for bullet in bullets if not CREDIT_LINE.match(bullet)]


class CreditsParserTests(unittest.TestCase):
    def test_wrapped_bullet_is_joined_before_its_class_is_read(self):
        text = "## Sources\n\n- **S1:** A.\n\n## Credits\n\n- Source A —\n  short quotation (quoted)\n"
        bullets = credit_bullets(text)
        self.assertEqual(bullets, ["- Source A — short quotation (quoted)"])
        self.assertEqual(unclassed(bullets), [])

    def test_a_line_without_one_of_the_three_classes_at_its_end_is_reported(self):
        for bullet in (
            "- Source A — cited procedural source (adapted; no record images reproduced)",
            "- Source A — cited and paraphrased (not reproduced)",
            "- Source A — bibliographic attribution only; not relicensed here.",
            "- Source A (adapted)",
        ):
            with self.subTest(bullet=bullet):
                self.assertEqual(unclassed([bullet]), [bullet])

    def test_a_blank_line_inside_the_list_is_refused(self):
        with self.assertRaisesRegex(ValueError, "one bullet list"):
            credit_bullets("## Credits\n\n- A — x (quoted)\n\n- B — y (adapted)\n")

    def test_a_missing_repeated_or_non_final_credits_section_is_refused(self):
        for text, message in (
            ("## Sources\n\n- **S1:** A.\n", "exactly one"),
            ("## Credits\n\n- A — x (quoted)\n\n## Credits\n\n- B — y (quoted)\n", "exactly one"),
            ("## Credits\n\n- A — x (quoted)\n\n## Notes\n\nText.\n", "last section"),
            ("## Credits\n\n", "empty"),
        ):
            with self.subTest(message=message), self.assertRaisesRegex(ValueError, message):
                credit_bullets(text)


class SourcesCreditsTests(unittest.TestCase):
    def test_every_credits_line_names_its_rights_class(self):
        paths = sorted(SOURCES.glob("*.md"))
        self.assertTrue(paths, f"no sources files found in {SOURCES}")
        for path in paths:
            with self.subTest(sources=path.name):
                bullets = credit_bullets(path.read_text(encoding="utf-8"))
                self.assertEqual(
                    unclassed(bullets),
                    [],
                    "end each Credits line with ' — <rights statement> (kinprove-original)', '(quoted)' or '(adapted)'",
                )


if __name__ == "__main__":
    unittest.main()
