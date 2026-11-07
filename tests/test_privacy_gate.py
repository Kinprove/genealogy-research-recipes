"""Every listed privacy-relevant recipe step sits behind its own Privacy gate checkpoint.

`SKILL.md` holds the one privacy gate. A recipe step that uploads, exports, links, publishes,
contacts a person, pastes data into a third-party tool, or (in the file-recovery recipes)
requests a record about a person who may be living, is preceded in its section by a
checkpoint line of the form

    **Privacy gate:** <!-- privacy-gate: export --> What leaves, whose data ...

`privacy_gate_inventory.json` lists each such step with the checkpoint that guards it. The
list came from reading every recipe; a new step needs a checkpoint and an entry.
"""

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills/genealogy-research-recipes"
SKILL = SKILL_DIR / "SKILL.md"
RECIPES = SKILL_DIR / "recipes"
INVENTORY = json.loads((Path(__file__).parent / "privacy_gate_inventory.json").read_text(encoding="utf-8"))

KINDS = {"upload", "export", "link", "publish", "contact", "request", "third-party-tool"}
MARKER = re.compile(r"<!--\s*privacy-gate:([^>]*?)-->")
LABEL_BEFORE_MARKER = re.compile(r"\*\*[^*\n]*Privacy gate[^*\n]*\*\*\s*$")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
HEADING = re.compile(r"^#{1,6} (.*)$", re.MULTILINE)

GATE_HEADING = "## Privacy gate"
GATE_ITEMS = ["People", "Data", "Destination", "Audience", "Controls", "Permission", "Redaction", "Retention", "Jurisdiction"]
GATE_SUBHEADINGS = ["### Living people", "### Record requests", "### Third persons in sensitive files"]

PRIVACY_LINK = "ai-for-dna-research.md#verification--privacy-discipline"
DNA_RECIPES = [
    "23andme-match-research.md",
    "ftdna-practical-dna-workflows.md",
    "gedmatch-practical-dna-workflows.md",
    "unknown-parentage-wato.md",
    "wikitree-dna-tester-links.md",
]
# (file whose text links the anchor, target file, anchor); paths relative to the skill folder
ANCHORS = [
    ("SKILL.md", "SKILL.md", "privacy-gate"),
    ("SKILL.md", "SKILL.md", "living-people"),
    ("SKILL.md", "recipes/ai-for-dna-research.md", "verification--privacy-discipline"),
    ("SKILL.md", "recipes/japanese-koseki-honseki-recovery.md", "4-check-eligibility-before-requesting"),
    ("SKILL.md", "recipes/soviet-personal-file-recovery.md", "5-log-each-catalogue-hit-as-a-candidate-with-its-own-locator"),
    ("recipes/unknown-parentage-wato.md", "recipes/ai-for-dna-research.md", "verification--privacy-discipline"),
    ("recipes/unknown-parentage-wato.md", "recipes/unknown-parentage-wato.md", "ethics-and-the-human-layer"),
]


def blank_fences(text):
    """Replace every line of a fenced code block, fences included, with an empty line.

    The fence rule matches `test_recipe_contents.py`: a fence is indented at most three
    spaces and closes only on a line of the same character, at least as long, with nothing
    after it. Line numbers stay the same, so nothing inside a code block counts.
    """
    fence = None
    lines = []
    for line in text.split("\n"):
        match = FENCE.match(line)
        if fence:
            if match and match[1][0] == fence[0] and len(match[1]) >= len(fence) and not match[2].strip():
                fence = None
            lines.append("")
        elif match and (match[1][0] == "~" or "`" not in match[2]):
            fence = match[1]
            lines.append("")
        else:
            lines.append(line)
    return "\n".join(lines)


def find_once(text, needle):
    """Return the offset in `text` where `needle` starts; it must occur exactly once.

    Case, line breaks and runs of spaces are ignored, so a rewrapped line still matches.
    """
    folded, origin = [], []
    for index, char in enumerate(text):
        if char.isspace():
            if folded and folded[-1] == " ":
                continue
            char = " "
        for part in char.casefold():  # one character can fold to several ("ß" -> "ss")
            folded.append(part)
            origin.append(index)
    folded = "".join(folded)
    target = re.sub(r"\s+", " ", needle.strip()).casefold()
    count = folded.count(target)
    if count != 1:
        raise AssertionError(f"expected exactly once, found {count}: {needle!r}")
    return origin[folded.index(target)]


def line_of(text, offset):
    return text.count("\n", 0, offset)


def markers(text):
    """Return (line index, kinds, line) for each marker outside code blocks."""
    found = []
    for index, line in enumerate(blank_fences(text).split("\n")):
        for match in MARKER.finditer(line):
            kinds = [kind.strip() for kind in match[1].split(",") if kind.strip()]
            found.append((index, kinds, line, match.start()))
    return found


def check_marker_format(line, start, kinds):
    if not kinds or not set(kinds) <= KINDS:
        raise AssertionError(f"unknown or missing kind in {line!r}")
    if not LABEL_BEFORE_MARKER.search(line[:start]):
        raise AssertionError(f"a bold 'Privacy gate' label must come right before the marker: {line!r}")


def check_entry(text, kind, action, checkpoint):
    """Fail unless `checkpoint` guards `action`: before it, same section, marker of `kind`."""
    live = blank_fences(text)
    lines = live.split("\n")
    action_at = find_once(live, action)
    checkpoint_at = find_once(live, checkpoint)
    if checkpoint_at > action_at:
        raise AssertionError(f"checkpoint comes after the action: {checkpoint!r}")
    action_line, checkpoint_line = line_of(live, action_at), line_of(live, checkpoint_at)
    for line in lines[checkpoint_line + 1 : action_line + 1]:
        if HEADING.match(line):
            raise AssertionError(f"a heading separates the checkpoint from the action: {line!r}")
    kinds = [kinds for index, kinds, _, _ in markers(text) if index == checkpoint_line]
    if not any(kind in found for found in kinds):
        raise AssertionError(f"no {kind!r} marker on the checkpoint's first line: {lines[checkpoint_line]!r}")
    return checkpoint_line


def github_slug(heading):
    slug = re.sub(r"[^\w\- ]", "", heading.strip().lower())
    return slug.replace(" ", "-")


def section(text, heading):
    """Return the text from `heading` to the next heading of the same or a higher level."""
    level = heading.split(" ", 1)[0]
    start = text.index(f"\n{heading}\n") + 1
    rest = re.search(rf"^#{{1,{len(level)}}} ", text[start + len(heading) :], re.MULTILINE)
    return text[start : start + len(heading) + rest.start()] if rest else text[start:]


class PrivacyGateSectionTests(unittest.TestCase):
    def test_skill_has_one_gate_with_its_items_in_order(self):
        text = SKILL.read_text(encoding="utf-8")
        self.assertEqual(blank_fences(text).split("\n").count(GATE_HEADING), 1)
        gate = section(text, GATE_HEADING)
        positions = [gate.index(f"- **{item}.**") for item in GATE_ITEMS]
        positions += [gate.index(f"\n{heading}\n") for heading in GATE_SUBHEADINGS]
        self.assertEqual(positions, sorted(positions))

    def test_how_to_use_points_to_the_gate(self):
        self.assertIn("](#privacy-gate)", section(SKILL.read_text(encoding="utf-8"), "## How to use"))


class InventoryTests(unittest.TestCase):
    def test_inventory_entries_are_well_formed(self):
        self.assertTrue(INVENTORY)
        for entry in INVENTORY:
            with self.subTest(entry=entry):
                self.assertEqual(set(entry), {"recipe", "kind", "action", "checkpoint"})
                self.assertIn(entry["kind"], KINDS)
                self.assertTrue((RECIPES / entry["recipe"]).is_file())

    def test_each_listed_step_has_its_checkpoint(self):
        for entry in INVENTORY:
            with self.subTest(recipe=entry["recipe"], action=entry["action"]):
                text = (RECIPES / entry["recipe"]).read_text(encoding="utf-8")
                check_entry(text, entry["kind"], entry["action"], entry["checkpoint"])

    def test_every_marker_is_well_formed_and_guards_a_listed_step(self):
        guarded = {}
        for entry in INVENTORY:
            live = blank_fences((RECIPES / entry["recipe"]).read_text(encoding="utf-8"))
            guarded.setdefault(entry["recipe"], set()).add(line_of(live, find_once(live, entry["checkpoint"])))
        checked = 0
        for path in sorted(RECIPES.glob("*.md")):
            for index, kinds, line, start in markers(path.read_text(encoding="utf-8")):
                checked += 1
                with self.subTest(recipe=path.name, line=index + 1):
                    check_marker_format(line, start, kinds)
                    self.assertIn(index, guarded.get(path.name, set()), "marker guards no listed step")
        self.assertGreaterEqual(checked, len({(e["recipe"], e["checkpoint"]) for e in INVENTORY}))

    def test_dna_recipes_link_the_dna_privacy_rules(self):
        for recipe in DNA_RECIPES:
            with self.subTest(recipe=recipe):
                self.assertIn(PRIVACY_LINK, (RECIPES / recipe).read_text(encoding="utf-8"))

    def test_linked_anchors_match_a_heading(self):
        for source, target, anchor in ANCHORS:
            with self.subTest(source=source, anchor=anchor):
                self.assertIn(f"#{anchor})", (SKILL_DIR / source).read_text(encoding="utf-8"))
                headings = HEADING.findall(blank_fences((SKILL_DIR / target).read_text(encoding="utf-8")))
                self.assertIn(anchor, {github_slug(heading) for heading in headings})


class CheckerSelfTests(unittest.TestCase):
    """The checker itself: each case fails for the right reason."""

    TWO_EXPORTS = (
        "## Export\n\n"
        "**Privacy gate:** <!-- privacy-gate: export --> The match list names living matches.\n\n"
        "Download the match list.\n\n"
        "**Privacy gate:** <!-- privacy-gate: export --> The segment file holds their segments.\n\n"
        "Download the segment file.\n"
    )

    def test_two_checkpoints_in_one_section_each_guard_their_own_step(self):
        check_entry(self.TWO_EXPORTS, "export", "Download the match list", "The match list names living")
        check_entry(self.TWO_EXPORTS, "export", "Download the segment file", "The segment file holds")

    def test_deleting_the_second_checkpoint_fails_although_the_first_remains(self):
        text = self.TWO_EXPORTS.replace(
            "**Privacy gate:** <!-- privacy-gate: export --> The segment file holds their segments.\n\n", ""
        )
        with self.assertRaises(AssertionError):
            check_entry(text, "export", "Download the segment file", "The segment file holds")

    def test_a_checkpoint_in_another_section_does_not_guard(self):
        text = self.TWO_EXPORTS.replace("Download the segment file.", "### Later\n\nDownload the segment file.")
        with self.assertRaises(AssertionError):
            check_entry(text, "export", "Download the segment file", "The segment file holds")

    def test_a_marker_of_another_kind_does_not_guard(self):
        text = self.TWO_EXPORTS.replace("export --> The segment", "upload --> The segment")
        with self.assertRaises(AssertionError):
            check_entry(text, "export", "Download the segment file", "The segment file holds")

    def test_a_checkpoint_after_the_step_does_not_guard(self):
        text = "## A\n\nUpload the file.\n\n**Privacy gate:** <!-- privacy-gate: upload --> Ask first.\n"
        with self.assertRaises(AssertionError):
            check_entry(text, "upload", "Upload the file", "Ask first")
        same_line = "## A\n\n2. Upload the file. **Privacy gate:** <!-- privacy-gate: upload --> Ask first.\n"
        with self.assertRaises(AssertionError):
            check_entry(same_line, "upload", "Upload the file", "Ask first")

    def test_a_character_that_folds_to_several_keeps_positions(self):
        text = "## Straße\n\n**Privacy gate:** <!-- privacy-gate: upload --> Ask first.\n\nUpload the file.\n"
        check_entry(text, "upload", "Upload the file", "Ask first")

    def test_a_fenced_checkpoint_or_heading_does_not_count(self):
        fenced = "## A\n\n```text\n**Privacy gate:** <!-- privacy-gate: upload --> Ask first.\n```\n\nUpload the file.\n"
        with self.assertRaises(AssertionError):
            check_entry(fenced, "upload", "Upload the file", "Ask first")
        self.assertEqual(markers(fenced), [])
        heading = "## A\n\n**Privacy gate:** <!-- privacy-gate: upload --> Ask first.\n\n```sh\n# step\n```\n\nUpload the file.\n"
        check_entry(heading, "upload", "Upload the file", "Ask first")

    def test_a_checkpoint_text_that_starts_off_the_marker_line_fails(self):
        text = "## A\n\n**Privacy gate:** <!-- privacy-gate: upload --> Ask\nfirst, then upload.\n\nUpload the file.\n"
        check_entry(text, "upload", "Upload the file", "Ask first")
        with self.assertRaises(AssertionError):
            check_entry(text, "upload", "Upload the file", "first, then upload")

    def test_action_or_checkpoint_text_must_occur_exactly_once(self):
        text = self.TWO_EXPORTS + "\nDownload the match list.\n"
        with self.assertRaises(AssertionError):
            check_entry(text, "export", "Download the match list", "The match list names living")
        with self.assertRaises(AssertionError):
            check_entry(self.TWO_EXPORTS, "export", "Download the match list", "Privacy gate")

    def test_marker_format(self):
        good = "- **Privacy gate:** <!-- privacy-gate: export, third-party-tool --> Text."
        ((_, kinds, line, start),) = markers(good)
        check_marker_format(line, start, kinds)
        for bad in (
            "<!-- privacy-gate: export --> **Privacy gate:** Text.",
            "**Privacy gate:** <!-- privacy-gate: send --> Text.",
            "**Privacy gate:** <!-- privacy-gate: --> Text.",
            "Text <!-- privacy-gate: export --> more.",
        ):
            with self.subTest(line=bad), self.assertRaises(AssertionError):
                ((_, kinds, line, start),) = markers(bad)
                check_marker_format(line, start, kinds)


if __name__ == "__main__":
    unittest.main()
