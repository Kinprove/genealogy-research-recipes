"""Offline invariants shared by unittest and the behavioural runner (stdlib only)."""

import datetime as dt
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

HERE = Path(__file__).resolve().parent
SKILL = HERE.parent
sys.path.insert(0, str(HERE.parents[2] / "scripts"))
from recipe_catalog import generated_files, load_catalog, normalized, parse_recipe, validate_header
from read_server import read_recipe


def load_cases(directory=HERE / "cases"):
    # JSON is a YAML 1.2 subset. Keeping cases in that subset avoids a runtime dependency.
    paths = sorted(Path(directory).glob("*.yaml"))
    if not paths:
        raise ValueError("No evaluation cases")
    cases = [json.loads(path.read_text(encoding="utf-8")) for path in paths]
    ids = [case["id"] for case in cases]
    if len(set(ids)) != len(ids):
        raise ValueError("Duplicate case IDs")
    for case in cases:
        if not re.fullmatch(r"[a-z0-9-]+", case["id"]) or not case["prompt"].strip():
            raise ValueError("Invalid case ID or empty prompt")
        if type(case["expect"]["clarify"]) is not bool:
            raise ValueError(f"{case['id']}: clarify must be boolean")
        if not case["assert"]["rubric"] and not case["expect"]["clarify"]:
            raise ValueError(f"{case['id']}: empty rubric")
        for pattern in case["assert"]["regex_present"] + case["assert"]["regex_absent"]:
            re.compile(pattern, re.I | re.S)
        for material in case["materials"]:
            fixture = (HERE / "fixtures" / material).resolve()
            if not fixture.is_relative_to(HERE / "fixtures") or not fixture.is_file():
                raise ValueError(f"{case['id']}: invalid fixture {material}")
    return cases


def header(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}, text
    return parse_recipe(text)


def judgment_recipes(skill=SKILL):
    names = {path.stem for path in (Path(skill) / "recipes").glob("*.md")
             if header(path)[0].get("kind") == "judgment"}
    return names if names or Path(skill) == SKILL else judgment_recipes()


JUDGMENT = judgment_recipes()


def required_lines(skill, recipe, sections):
    lines = set()
    for section in sections:
        text = read_recipe(Path(skill) / "recipes", recipe + ".md", section)
        lines.update(int(line.partition("\t")[0]) for line in text.splitlines())
    return lines


def guardrails(skill=SKILL):
    result = {}
    for path in sorted((Path(skill) / "recipes").glob("*.md")):
        metadata, body = header(path)
        if metadata and metadata["id"] != path.stem:
            raise ValueError(f"{path.name}: header ID differs from filename")
        for rule in metadata.get("guardrails", []):
            key = rule["id"]
            if key in result:
                raise ValueError(f"Duplicate guardrail ID: {key}")
            quote = rule["text"]
            quoted = bool(quote) and normalized(quote) in normalized(body)
            # Locate the quoted sentence in the body, never in its header copy.
            start = path.read_text(encoding="utf-8").index(body)
            body_lines = body.splitlines(keepends=True)
            line = None
            for index in range(len(body_lines)) if quoted else []:
                if normalized(quote) in normalized("".join(body_lines[index:])):
                    line = path.read_text(encoding="utf-8")[:start].count("\n") + index + 1
                else:
                    break
            result[key] = {"recipe": path.stem, "quote": quote, "line": line}
    return result


def prose(text):
    return re.sub(r"(?ms)^(`{3,}|~{3,}).*?^\1\s*$", "", text)


def static_checks(skill=SKILL, cases_dir=HERE / "cases", today=None):
    """Raise on broken routes, local links, case bindings or stale declared checks."""
    skill = Path(skill).resolve()
    today = today or dt.datetime.now(dt.timezone.utc).date()
    if skill == SKILL.resolve():
        root = skill.parents[1]
        catalog = load_catalog(root=root, today=today)
        for path, expected in generated_files(root, catalog):
            if path.read_text(encoding="utf-8") != expected:
                raise ValueError(f"Generated output differs: {path.name}; run scripts/recipe_catalog.py --write")
    recipe_paths = sorted((skill / "recipes").glob("*.md"))
    recipes = {path.stem for path in recipe_paths}
    router = (skill / "SKILL.md").read_text(encoding="utf-8")
    routes = set(re.findall(r"recipes/([a-z0-9-]+)\.md", router))
    if routes != recipes:
        raise ValueError(f"Route mismatch: unreferenced={recipes-routes}, dangling={routes-recipes}")
    dated = []
    for path in [skill / "SKILL.md", *recipe_paths]:
        text = prose(path.read_text(encoding="utf-8"))
        for reference in re.findall(r"`(?:recipes/)?([a-z0-9-]+)\.md(?:#[^`]+)?`", text):
            if reference != "SKILL" and reference not in recipes:
                raise ValueError(f"{path.name}: unknown recipe {reference}")
        for target in re.findall(r"\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)", text):
            url = urlsplit(target.strip("<>"))
            if url.scheme or url.netloc:
                continue
            destination = (path.parent / unquote(url.path)).resolve() if url.path else path
            if not destination.is_relative_to(skill) or not destination.is_file():
                raise ValueError(f"{path.name}: dangling local link {target}")
            if url.fragment and destination.suffix == ".md":
                headings = re.findall(r"(?m)^#{1,6} +(.+?) *#* *$", destination.read_text(encoding="utf-8"))
                anchors = set()
                for heading in headings:
                    slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
                    original, suffix = slug, 0
                    while slug in anchors:
                        suffix += 1
                        slug = f"{original}-{suffix}"
                    anchors.add(slug)
                anchors.update(re.findall(r'(?:id|name)="([^"]+)"', destination.read_text(encoding="utf-8")))
                if unquote(url.fragment) not in anchors:
                    raise ValueError(f"{path.name}: missing anchor {target}")
        if path.parent.name == "recipes":
            metadata, body = header(path)
            validate_header(metadata, body, path.name, today)
            if metadata.get("checked"):
                dated.append(f"{path.stem}:{metadata['checked']}")
    rules = guardrails(skill)
    cases = load_cases(cases_dir)
    for case in cases:
        expected = case["expect"]
        for name in expected["recipes"] + expected.get("any_of", []) + expected.get("read_full", []):
            if name not in recipes:
                raise ValueError(f"{case['id']}: missing recipe {name}")
        required_sections = expected.get("read_sections", {})
        optional_sections = expected.get("optional_read_sections", {})
        if set(required_sections) & set(optional_sections):
            raise ValueError(f"{case['id']}: required and optional section bindings overlap")
        for name, sections in {**required_sections, **optional_sections}.items():
            if name not in recipes or not sections:
                raise ValueError(f"{case['id']}: invalid rule-section binding")
            required_lines(skill, name, sections)
        for name in (set(expected["recipes"]) | set(expected.get("any_of", []))) & JUDGMENT:
            if name not in expected.get("read_full", []) and name not in expected.get("read_sections", {}):
                raise ValueError(f"{case['id']}: judgment recipe {name} needs a rule-section binding")
        for item in case["assert"]["rubric"]:
            if item["guardrail"] not in rules or not item["question"].endswith("?"):
                raise ValueError(f"{case['id']}: missing guardrail or invalid yes/no question")
        for material in case["materials"]:
            fixture = (HERE / "fixtures" / material).resolve()
            if not fixture.is_relative_to(HERE / "fixtures") or not fixture.is_file():
                raise ValueError(f"{case['id']}: invalid fixture {material}")
    return {"recipes": len(recipes), "cases": len(cases), "guardrails": len(rules), "dated_checks": dated}
