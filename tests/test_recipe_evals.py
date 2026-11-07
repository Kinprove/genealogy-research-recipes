"""Regression tests for the evaluator's failure modes, independent of a model/key."""

import datetime as dt
import json
from pathlib import Path
import shutil
import sys
import subprocess
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
EVALS = ROOT / "skills/genealogy-research-recipes/evals"
sys.path.insert(0, str(EVALS))
from checks import SKILL, guardrails, header, load_cases, required_lines, static_checks
from recipe_catalog import emit_recipe
from run_evals import aggregate, deterministic, parse_judgment, read_failures, sample, successful_reads, unexpected_tools, verify_replay_materials
from read_server import read_recipe


class StaticEvaluationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="recipe-evals-")
        self.addCleanup(self.temporary.cleanup)
        self.skill = Path(self.temporary.name) / "genealogy-research-recipes"
        shutil.copytree(SKILL, self.skill, ignore=shutil.ignore_patterns("__pycache__"))

    def test_current_skill_and_all_cases_are_bound(self):
        report = static_checks()
        self.assertEqual(report["cases"], 13)
        self.assertGreater(report["recipes"], 100)
        self.assertGreaterEqual(report["guardrails"], 20)

    def test_router_cannot_lose_or_invent_a_recipe(self):
        router = self.skill / "SKILL.md"
        original = router.read_text(encoding="utf-8")
        for replacement in ("", "recipes/does-not-exist.md"):
            router.write_text(original.replace("recipes/rabbinic-literature-person-search.md", replacement), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Route mismatch"):
                static_checks(self.skill)

    def test_dangling_handoff_and_fragment_fail(self):
        path = self.skill / "recipes/burial-evidence-packet.md"
        original = path.read_text(encoding="utf-8")
        for target in ("missing-recipe.md", "source-citation.md#missing-section"):
            path.write_text(original + f"\n[Handoff]({target})\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "dangling local link|missing anchor"):
                static_checks(self.skill)

    def test_case_quote_must_remain_in_body_not_just_header(self):
        path = self.skill / "recipes/ai-for-dna-research.md"
        text = path.read_text(encoding="utf-8")
        quote = guardrails(self.skill)["CM-01"]["quote"]
        metadata, body = text.split("\n---\n", 1)
        path.write_text(metadata + "\n---\n" + body.replace(quote, "REMOVED"), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "quote no longer occurs"):
            static_checks(self.skill)

    def test_duplicate_guardrail_id_is_rejected(self):
        path = self.skill / "recipes/burial-evidence-packet.md"
        path.write_text(path.read_text(encoding="utf-8").replace('"BUR-01"', '"CM-01"'), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Duplicate guardrail"):
            guardrails(self.skill)

    def test_dates_expire_and_future_checks_are_not_accepted(self):
        path = self.skill / "recipes/gedmatch-practical-dna-workflows.md"
        metadata, body = header(path)
        today = dt.datetime.now(dt.timezone.utc).date()
        for age in (91, -1):
            date = today - dt.timedelta(days=age)
            metadata["checked"] = date.isoformat()
            metadata["checked_basis"] = f"checked {date.isoformat()}"
            path.write_text(emit_recipe(metadata, body), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "older than 90 days|in the future"):
                static_checks(self.skill)

    def test_declared_platform_cannot_omit_its_check_date(self):
        path = self.skill / "recipes/burial-evidence-packet.md"
        metadata, body = header(path)
        metadata["kind"] = "platform"
        metadata["scope"]["platforms"] = ["test-platform"]
        metadata["checked"] = metadata["checked_basis"] = None
        path.write_text(emit_recipe(metadata, body), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "platform recipe needs a dated source check"):
            static_checks(self.skill)

    def test_missing_case_guardrail_and_fixture_are_rejected(self):
        cases = Path(self.temporary.name) / "cases"
        cases.mkdir()
        original = load_cases()[0]
        path = cases / "case.yaml"
        for field in ("guardrail", "fixture"):
            case = json.loads(json.dumps(original))
            if field == "guardrail":
                case["assert"]["rubric"][0]["guardrail"] = "MISSING"
            else:
                case["materials"] = ["../../SKILL.md"]
            path.write_text(json.dumps(case), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "missing guardrail|invalid fixture"):
                static_checks(self.skill, cases)


class BehaviouralHarnessTests(unittest.TestCase):
    def setUp(self):
        self.case = next(case for case in load_cases() if case["id"] == "cm-relationship")

    def trace(self, path, content="1\tFirst line", error=False):
        return [
            {"type": "assistant", "message": {"content": [{"type": "tool_use", "name": "Read", "id": "read1", "input": {"file_path": str(path), "offset": 1, "limit": 80}}]}},
            {"type": "user", "message": {"content": [{"type": "tool_result", "tool_use_id": "read1", "is_error": error, "content": content}]}},
        ]

    def test_claiming_a_recipe_in_answer_is_not_routing(self):
        failures = deterministic(self.case, "I read ai-for-dna-research. Shared cM, endogamy.", {})
        self.assertTrue(any("Unread recipes" in failure for failure in failures))

    def test_equivalent_stone_wording_does_not_fail_the_inscription_regex(self):
        case = next(case for case in load_cases() if case["id"] == "memorial-proof")
        reads = {"burial-evidence-packet": {"complete": True, "lines": []}}
        failures = deterministic(case, "The database, headstone and burial give claims about death.", reads)
        self.assertEqual(failures, [])

    def test_denied_read_and_outside_path_never_count(self):
        path = SKILL / "recipes/ai-for-dna-research.md"
        self.assertEqual(successful_reads(self.trace(path, error=True), SKILL), {})
        self.assertEqual(successful_reads(self.trace(Path("/tmp/not-a-recipe.md")), SKILL), {})
        self.assertEqual(successful_reads(self.trace(path)[:1], SKILL), {})

    def test_denied_or_unfinished_reads_fail_even_after_a_successful_read(self):
        path = SKILL / "recipes/ai-for-dna-research.md"
        trace = self.trace(path, error=True) + self.trace(path)
        self.assertTrue(any("Denied/error read" in failure for failure in read_failures(trace)))
        self.assertTrue(any("Incomplete read" in failure for failure in read_failures(self.trace(path)[:1])))
        self.assertTrue(any("Out-of-scope" in failure for failure in read_failures(self.trace(Path("/tmp/private.md")))))

    def test_goal_or_first_line_cannot_stand_in_for_judgment_rules(self):
        case = next(case for case in load_cases() if case["id"] == "parentage-proof")
        path = SKILL / "recipes/evidence-proof-judgment.md"
        goal = read_recipe(SKILL / "recipes", path.name, "Goal")
        for content in ("1\t---", goal):
            reads = successful_reads(self.trace(path, content), SKILL)
            self.assertTrue(any("Judgment rules not read" in failure for failure in deterministic(case, "A plan", reads)))
        sections = case["expect"]["read_sections"][path.stem]
        content = "\n".join(read_recipe(SKILL / "recipes", path.name, section) for section in sections)
        reads = successful_reads(self.trace(path, content), SKILL)
        self.assertFalse(reads[path.stem]["complete"])
        self.assertTrue(required_lines(SKILL, path.stem, sections) <= set(reads[path.stem]["lines"]))
        self.assertFalse(any("Judgment rules not read" in failure for failure in deterministic(case, "A plan", reads)))

    def test_replay_subset_uses_only_selected_fixtures_but_rejects_changed_ones(self):
        previous = {"materials": {"matches.csv": "same", "family.ged": "unselected"}}
        verify_replay_materials(previous, {"matches.csv": "same"})
        with self.assertRaisesRegex(ValueError, "fixture contents differ"):
            verify_replay_materials(previous, {"matches.csv": "changed"})
        with self.assertRaisesRegex(ValueError, "fixture contents differ"):
            verify_replay_materials(previous, {"missing.csv": "new"})
        with self.assertRaisesRegex(ValueError, "no frozen fixtures"):
            verify_replay_materials({}, {})

    def test_successful_chunks_accumulate_and_tasks_require_every_line(self):
        path = SKILL / "recipes/family-interviews-and-oral-tradition.md"
        count = len(path.read_text(encoding="utf-8").splitlines())
        trace = self.trace(path, "\n".join(f"{n}\tline" for n in range(1, 41)))
        trace += self.trace(path, "\n".join(f"{n}\tline" for n in range(41, count + 1)))
        evidence = successful_reads(trace, SKILL)
        self.assertTrue(evidence[path.stem]["complete"])
        partial = successful_reads(trace[:2], SKILL)
        self.assertFalse(partial[path.stem]["complete"])
        case = next(case for case in load_cases() if case["id"] == "family-interview")
        self.assertTrue(any("not read in full" in failure for failure in deterministic(case, "record consent", partial)))

    def test_artifact_task_still_requires_full_read_when_catalog_kind_is_judgment(self):
        case = next(case for case in load_cases() if case["id"] == "gedcom-ancestry")
        evidence = {"gedcom-research-export": {"complete": False, "lines": [1]}}
        failures = deterministic(case, "living QUAY redact", evidence)
        self.assertTrue(any("not read in full" in failure for failure in failures))

    def test_regex_failure_cannot_be_outvoted_by_rubrics(self):
        rows = [{"case": self.case["id"], "rubric_pass": True, "deterministic_failures": []} for _ in range(3)]
        self.assertTrue(aggregate([self.case], rows)[self.case["id"]]["pass"])
        rows[0]["deterministic_failures"] = ["Forbidden percentage"]
        self.assertFalse(aggregate([self.case], rows)[self.case["id"]]["pass"])

    def test_rubrics_need_two_of_three_and_missing_samples_fail(self):
        rows = [{"case": self.case["id"], "rubric_pass": index < 2, "deterministic_failures": []} for index in range(3)]
        self.assertTrue(aggregate([self.case], rows)[self.case["id"]]["pass"])
        self.assertFalse(aggregate([self.case], rows[:2])[self.case["id"]]["pass"])
        rows[1]["rubric_pass"] = False
        self.assertFalse(aggregate([self.case], rows)[self.case["id"]]["pass"])

    def test_competing_task_recipes_fail_clarification(self):
        case = next(case for case in load_cases() if case["id"] == "russia-origin")
        reads = {name: {"complete": True} for name in ("gedmatch-practical-dna-workflows", "ancestry-record-search-recovery")}
        self.assertTrue(deterministic(case, "Which place?", reads))

    def test_unexpected_tool_attempts_are_visible_even_if_denied(self):
        trace = [{"message": {"content": [{"type": "tool_use", "name": "Bash"}]}}]
        self.assertEqual(unexpected_tools(trace, {"Read"}), ["Bash"])

    def test_sample_integration_writes_evidence_and_uses_fixture_in_judge(self):
        case = next(case for case in load_cases() if case["id"] == "gedcom-ancestry")
        path = SKILL / "recipes/gedcom-research-export.md"
        count = len(path.read_text(encoding="utf-8").splitlines())
        trace = self.trace(path, "\n".join(f"{n}\tline" for n in range(1, count + 1)))
        judgment = {"clarify": False, "items": [{"guardrail": item["guardrail"], "pass": True, "reason": "Observed"}
                                               for item in case["assert"]["rubric"]]}
        with tempfile.TemporaryDirectory() as directory:
            args = SimpleNamespace(output=Path(directory), skill=SKILL, model="test", judge_model="test",
                                   profile="claude", replay=None)

            def transport(prompt, skill, output, model, *positional, **options):
                output.write_text("{}\n", encoding="utf-8")
                if output.name == "judge.jsonl":
                    self.assertIn("1942", prompt)
                    self.assertIn("guardrail_sentence", prompt)
                    self.assertIsNotNone(options.get("schema"))
                    return json.dumps(judgment), []
                self.assertIn("SYNTHETIC-EVAL", prompt)
                return "Keep living people private; redact before sharing. QUAY is not research status.", trace

            with patch("run_evals.invoke", side_effect=transport):
                result = sample(case, 1, args, guardrails())
            self.assertEqual(result["deterministic_failures"], [])
            self.assertTrue(result["rubric_pass"])
            destination = args.output / case["id"] / "1"
            for name in ("result.json", "assistant.jsonl", "assistant-events.json", "judge.jsonl"):
                self.assertTrue((destination / name).is_file())


class ReadFileToolTests(unittest.TestCase):
    def test_server_returns_all_lines_and_sections_keep_original_line_numbers(self):
        root = SKILL / "recipes"
        content = read_recipe(root, "recipes/gedmatch-practical-dna-workflows.md")
        self.assertEqual(len(content.splitlines()), len((root / "gedmatch-practical-dna-workflows.md").read_text(encoding="utf-8").splitlines()))
        section = read_recipe(root, "evidence-proof-judgment.md", "Hard rules — apply these before you rule (the load-bearing directives)")
        self.assertIn("A converged match is evidence", section)
        self.assertNotIn("What the HUMAN must own", section)
        self.assertNotEqual(section.splitlines()[0].split("\t")[0], "1")

    def test_traversal_absolute_outside_and_symlink_are_denied(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "recipes"
            root.mkdir()
            outside = Path(directory) / "private.md"
            outside.write_text("private", encoding="utf-8")
            (root / "alias.md").symlink_to(outside)
            for target in ("../private.md", str(outside), "alias.md"):
                with self.assertRaisesRegex(ValueError, "Only existing Markdown"):
                    read_recipe(root, target)

    def test_real_stdio_protocol_initializes_lists_and_reads_without_extra_stdout(self):
        requests = [
            {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2024-11-05"}},
            {"jsonrpc": "2.0", "method": "notifications/initialized"},
            {"jsonrpc": "2.0", "id": 2, "method": "tools/list"},
            {"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "read_file", "arguments": {"path": "burial-evidence-packet.md"}}},
            {"jsonrpc": "2.0", "id": 4, "method": "tools/call", "params": {"name": "read_file", "arguments": {"path": "../../README.md"}}},
        ]
        result = subprocess.run([sys.executable, str(EVALS / "read_server.py"), str(SKILL / "recipes")],
                                input="\n".join(json.dumps(item) for item in requests) + "\n",
                                text=True, capture_output=True, timeout=10, check=True)
        replies = [json.loads(line) for line in result.stdout.splitlines()]
        self.assertEqual([reply["id"] for reply in replies], [1, 2, 3, 4])
        self.assertEqual(replies[1]["result"]["tools"][0]["name"], "read_file")
        self.assertFalse(replies[2]["result"]["isError"])
        self.assertTrue(replies[3]["result"]["isError"])

class JudgeVerdictTests(unittest.TestCase):
    def setUp(self):
        self.case = next(case for case in load_cases() if case["id"] == "cm-relationship")

    def test_judge_cannot_use_truthy_strings_or_omit_questions(self):
        items = [{"guardrail": item["guardrail"], "pass": True, "reason": "Observed"} for item in self.case["assert"]["rubric"]]
        valid = {"clarify": False, "items": items}
        self.assertEqual(parse_judgment(json.dumps(valid), self.case), valid)
        invalid = json.loads(json.dumps(valid))
        invalid["items"][0]["pass"] = "true"
        with self.assertRaises(ValueError):
            parse_judgment(json.dumps(invalid), self.case)
        valid["items"].pop()
        with self.assertRaises(ValueError):
            parse_judgment(json.dumps(valid), self.case)


if __name__ == "__main__":
    unittest.main()
