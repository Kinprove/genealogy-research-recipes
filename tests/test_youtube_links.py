"""Every YouTube link carries a well-formed video ID in its original letter case.

YouTube video IDs are case-sensitive: a lowercased ID opens a "video unavailable" page.
An ID copied from a lowercased file name or slug has no capital letter at all, while a
real 11-character ID almost always has one. A real all-lowercase ID is listed below after
it was opened and checked against its source.
"""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIPPED_DIRS = {".git", "node_modules"}
VIDEO_URL = re.compile(
    r"(?:youtube\.com/watch\?(?:[^\s<>()\]]*?&)?v=|youtube\.com/(?:shorts|embed|live)/|youtu\.be/)"
    r"([A-Za-z0-9_-]*)"
)
VIDEO_ID = re.compile(r"^[A-Za-z0-9_-]{11}$")
# Real IDs with no capital letter, each opened on YouTube and matched to its cited video.
VERIFIED_LOWERCASE_IDS = {"fn1m71109bg", "g5kj-arn5ts", "pdqsz950wnc"}


def bad_video_ids(text):
    """Return each video ID in `text` that is malformed or lowercase-only and not verified."""
    bad = []
    for video_id in VIDEO_URL.findall(text):
        if not VIDEO_ID.match(video_id):
            bad.append(video_id)
        elif not re.search("[A-Z]", video_id) and video_id not in VERIFIED_LOWERCASE_IDS:
            bad.append(video_id)
    return bad


class VideoIdParserTests(unittest.TestCase):
    def test_a_lowercased_id_is_reported(self):
        self.assertEqual(bad_video_ids("<https://www.youtube.com/watch?v=osykmf2mhgm>"), ["osykmf2mhgm"])

    def test_an_id_in_its_original_case_passes(self):
        for text in (
            "<https://www.youtube.com/watch?v=OsYKmF2mHgM>",
            "[talk](https://www.youtube.com/watch?v=Br_NSHmEH6E&t=95s)",
            "https://youtu.be/u_Ytw67pPAQ.",
            "https://www.youtube.com/watch?feature=share&v=nq-TQVwTi_s",
        ):
            with self.subTest(text=text):
                self.assertEqual(bad_video_ids(text), [])

    def test_a_verified_lowercase_id_passes(self):
        self.assertEqual(bad_video_ids("https://www.youtube.com/watch?v=pdqsz950wnc"), [])

    def test_a_truncated_or_overlong_id_is_reported(self):
        for video_id in ("OsYKmF2mHg", "OsYKmF2mHgMx", ""):
            with self.subTest(video_id=video_id):
                self.assertEqual(bad_video_ids(f"<https://www.youtube.com/watch?v={video_id}>"), [video_id])


class RepositoryVideoIdTests(unittest.TestCase):
    def test_every_youtube_id_keeps_its_original_case(self):
        paths = sorted(
            path for path in ROOT.rglob("*.md") if not SKIPPED_DIRS.intersection(path.relative_to(ROOT).parts)
        )
        found = 0
        for path in paths:
            text = path.read_text(encoding="utf-8")
            found += len(VIDEO_URL.findall(text))
            with self.subTest(file=str(path.relative_to(ROOT))):
                self.assertEqual(
                    bad_video_ids(text),
                    [],
                    "copy each YouTube ID from the video's own URL; an ID with no capital letter is"
                    " usually a lowercased copy. If the real ID has no capital, open it, then add it"
                    " to VERIFIED_LOWERCASE_IDS",
                )
        # A scan that matches nothing would pass silently; the recipes cite thousands of videos.
        self.assertGreater(found, 1000, "the YouTube link pattern matched almost nothing")


if __name__ == "__main__":
    unittest.main()
