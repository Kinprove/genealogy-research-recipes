#!/usr/bin/env python3
"""Validate recipe headers and render the router and capability table (stdlib only)."""

import argparse
import datetime as dt
import json
import re
import sys
import textwrap
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILL_PATH = Path("skills/genealogy-research-recipes")
MAX_PLATFORM_AGE_DAYS = 90
ROUTER_START = "<!-- recipe-catalog:start -->"
ROUTER_END = "<!-- recipe-catalog:end -->"
TABLE_START = "<!-- recipe-capabilities:start -->"
TABLE_END = "<!-- recipe-capabilities:end -->"
FIELDS = {
    "id", "title", "summary", "kind", "scope", "privacy", "gates",
    "guardrails", "handoff", "checked", "checked_basis", "capabilities", "router",
}
CAPABILITIES = {"browse", "local_script", "extensions", "data_transfer", "contact"}
SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")


class CatalogError(ValueError):
    pass


def require(ok, message):
    if not ok:
        raise CatalogError(message)


def string(value):
    return isinstance(value, str) and bool(value.strip()) and "\n" not in value


def string_list(value, nonempty=False):
    return (isinstance(value, list) and (bool(value) or not nonempty)
            and all(string(v) for v in value) and len(value) == len(set(value)))


def normalized(text):
    """Collapse whitespace runs, so a quote matches a body passage across line wraps."""
    return " ".join(text.split())


def parse_recipe(text):
    """Read our YAML subset: one key and JSON-encoded value per line.

    JSON scalars/arrays/objects are YAML 1.2 values. Restricting the syntax avoids
    implicit date/bool coercion, duplicate keys and a host runtime dependency.
    """
    require(text.startswith("---\n"), "missing recipe header")
    header, separator, body = text[4:].partition("\n---\n")
    require(separator, "unclosed recipe header")
    metadata = {}
    for line in header.splitlines():
        key, separator, value = line.partition(": ")
        require(separator and key not in metadata, f"invalid or duplicate header key: {key}")
        try:
            metadata[key] = json.loads(value)
        except json.JSONDecodeError as exc:
            raise CatalogError(f"{key}: use a JSON-encoded YAML value: {exc}") from exc
    return metadata, body.lstrip("\n")


def emit_recipe(metadata, body):
    return "---\n" + "\n".join(
        f"{key}: {json.dumps(value, ensure_ascii=False)}" for key, value in metadata.items()
    ) + "\n---\n\n" + body.lstrip("\n")


def validate_header(m, body, filename, today):
    require(set(m) == FIELDS, f"header fields differ: {set(m) ^ FIELDS}")
    require(string(m["id"]) and SLUG.fullmatch(m["id"]), "invalid id")
    require(filename == m["id"] + ".md", "id must equal filename stem")
    for field in ("title", "summary"):
        require(string(m[field]), f"{field} must be a nonempty single-line string")
    heading = re.search(r"^# (.+)$", body, re.M)
    require(heading and heading[1].removeprefix("Recipe: ") == m["title"], "title differs from body heading")
    require(m["kind"] in ("judgment", "platform", "records"), "unknown kind")
    route = m["router"]
    require(isinstance(route, dict) and set(route) == {"tier", "group", "order"}, "invalid router")
    require(route["tier"] in ("full", "pointer") and string(route["group"]), "invalid router tier/group")
    require(type(route["order"]) is int and route["order"] >= 0, "invalid router order")
    scope = m["scope"]
    require(isinstance(scope, dict) and set(scope) == {"platforms", "tasks"}, "invalid scope")
    require(string_list(scope["platforms"]) and string_list(scope["tasks"]), "invalid scope lists")
    require(scope["tasks"] or route["tier"] != "full", "full router entries need tasks")
    summary = normalized(m["summary"]).casefold()
    for task in scope["tasks"]:
        require(normalized(task).casefold().rstrip(".") not in summary,
                f"task repeats the summary: {task}")
    require(m["privacy"] in ("none", "living-person", "genetic-self", "genetic-third-party"), "invalid privacy")
    require(string_list(m["gates"]) and set(m["gates"]) <= {"privacy-transfer"}, "unknown gates")
    require(string_list(m["handoff"]) and all(SLUG.fullmatch(s) for s in m["handoff"]), "invalid handoff")
    rules = m["guardrails"]
    require(isinstance(rules, list) and bool(rules), "guardrails must not be empty")
    quotable = normalized(body)
    for rule in rules:
        require(isinstance(rule, dict) and set(rule) == {"id", "text"}, "invalid guardrail")
        require(string(rule["id"]) and string(rule["text"]), "empty guardrail id/text")
        require(normalized(rule["text"]) in quotable,
                f"guardrail {rule['id']} is not an excerpt of the recipe body")
    caps = m["capabilities"]
    require(isinstance(caps, dict) and set(caps) == CAPABILITIES, "invalid capabilities")
    require(all(string_list(v) for v in caps.values()), "capabilities must be string lists")
    outbound = any(caps[k] for k in ("extensions", "data_transfer", "contact"))
    gated = "privacy-transfer" in m["gates"]
    require(not outbound or gated, "outbound capabilities require privacy-transfer")
    require(gated == (m["privacy"] != "none"), "privacy and gates disagree")
    if m["kind"] == "platform":
        require(bool(scope["platforms"]), "platform recipe needs a platform")
        require(m["checked"] is not None, "platform recipe needs a dated source check")
    require((m["checked"] is None) == (m["checked_basis"] is None), "checked needs a checked_basis")
    if m["checked"] is not None:
        try:
            checked = dt.date.fromisoformat(m["checked"])
        except (ValueError, TypeError) as exc:
            raise CatalogError("checked must be an ISO date or null") from exc
        require(checked <= today, "checked is in the future")
        basis = m["checked_basis"]
        require(isinstance(basis, str) and bool(basis.strip()), "checked_basis must quote dated source evidence")
        require(re.fullmatch(
            r"(?:rechecked|checked|read|consulted|accessed|retrieved|fetched|verified|opened)(?: on)?\s+"
            r"(?:20\d\d-\d\d-\d\d|\d{1,2} [A-Z][a-z]+ 20\d\d)", basis, re.I),
            "checked_basis must name a source check, not a publication/capture date")
        dates = re.findall(r"20\d\d-\d\d-\d\d|\d{1,2} [A-Z][a-z]+ 20\d\d", basis)
        parsed = []
        for value in dates:
            try:
                parsed.append(dt.date.fromisoformat(value))
            except ValueError:
                parsed.append(dt.datetime.strptime(value, "%d %B %Y").date())
        require(checked in parsed, "checked date differs from checked_basis")
        if m["kind"] == "platform":
            require((today - checked).days <= MAX_PLATFORM_AGE_DAYS,
                    f"platform source check is older than {MAX_PLATFORM_AGE_DAYS} days")


def recipe_references(text):
    """Find local Markdown links, code filenames and bold recipe slugs.

    External URLs are deliberately excluded: a GitHub/source URL is not a local
    recipe handoff. Bare slug names in bold are a supported routing notation.
    """
    targets = re.findall(r"\[[^\]\n]*\]\(([^)\s]+)(?:\s+[^)]*)?\)", text)
    targets += re.findall(r"^ {0,3}\[[^\]\n]+\]:\s*<?([^\s>]+)>?", text, re.M)
    for target in targets:
        url = urlsplit(target.strip("<>"))
        path = unquote(url.path)
        if url.scheme or url.netloc:
            continue
        if path.endswith(".md") and ("recipes/" in path or Path(path).parent == Path(".")):
            yield Path(path).stem
    for name in re.findall(r"`(?:recipes/)?([a-z0-9]+(?:-[a-z0-9]+)*)\.md(?:#[^`]+)?`", text):
        yield name
    for name in re.findall(r"\*\*(?:recipes/)?([a-z0-9]+(?:-[a-z0-9]+)*)\.md\*\*", text):
        yield name
    for name in re.findall(r"(?:recipe (?:names|complements)|use)\s+`([a-z0-9]+(?:-[a-z0-9]+)+)`", text):
        if name != "genealogy-research-recipes":  # the containing skill is also a valid destination
            yield name
    for name in re.findall(r"\brecipe\s+\*\*`?([a-z0-9]+(?:-[a-z0-9]+)+)`?\*\*", text, re.I):
        yield name


def load_catalog(root=None, today=None, replacement=None):
    root = root or ROOT
    today = today or dt.datetime.now(dt.timezone.utc).date()
    skill = root / SKILL_PATH
    texts = {p.name: p.read_text(encoding="utf-8") for p in (skill / "recipes").glob("*.md")}
    if replacement:
        texts[replacement[0]] = replacement[1]
    require(bool(texts), "no recipes found")
    catalog = []
    ids, rule_ids, orders = set(), set(), set()
    for name, text in sorted(texts.items()):
        try:
            m, body = parse_recipe(text)
            validate_header(m, body, name, today)
            require(m["id"] not in ids, "duplicate id")
            ids.add(m["id"])
            order = m["router"]["order"]
            require(order not in orders, "duplicate router order")
            orders.add(order)
            for rule in m["guardrails"]:
                require(rule["id"] not in rule_ids, f"duplicate guardrail id: {rule['id']}")
                rule_ids.add(rule["id"])
            if m["checked_basis"]:
                source = skill / "sources" / name
                require(source.is_file(), "missing source sidecar for dated check")
                source_text = source.read_text(encoding="utf-8")
                occurrences = list(re.finditer(re.escape(m["checked_basis"]), source_text))
                require(bool(occurrences), "checked_basis is absent from source sidecar")
                require(any(not re.search(r"topic(?: was)?\s+$", source_text[max(0, x.start() - 30):x.start()], re.I)
                            for x in occurrences), "checked_basis is a topic opening date, not a source check")
            catalog.append((m, body))
        except CatalogError as exc:
            raise CatalogError(f"{name}: {exc}") from exc
    for m, body in catalog:
        routed_text = "\n".join([body, m["summary"], *m["scope"]["tasks"]])
        for target in set(m["handoff"]) | set(recipe_references(routed_text)):
            require(target in ids, f"{m['id']}: missing recipe {target}")
    # The independently maintained, reviewed checkpoint inventory catches a header
    # that understates its outbound actions; headers do not replace those checks.
    inventory = json.loads((root / "tests/privacy_gate_inventory.json").read_text(encoding="utf-8"))
    by_id = {m["id"]: m for m, _ in catalog}
    for step in inventory:
        slug = Path(step["recipe"]).stem
        require(slug in by_id, f"privacy inventory names missing recipe {slug}")
        caps = by_id[slug]["capabilities"]
        field = "contact" if step["kind"] == "contact" else "data_transfer"
        require(step["kind"] in caps[field], f"{slug}: capability omits inventoried {step['kind']}")
    catalog.sort(key=lambda item: item[0]["router"]["order"])
    pointer_seen = False
    for m, _ in catalog:
        pointer_seen |= m["router"]["tier"] == "pointer"
        require(not pointer_seen or m["router"]["tier"] == "pointer",
                f"{m['id']}: full entries must precede topic pointers")
    return catalog


def wrap(text):
    return textwrap.fill(text, width=100, initial_indent="  ", subsequent_indent="  ",
                         break_long_words=False, break_on_hyphens=False)


def render_router(catalog):
    lines = [ROUTER_START, "## Recipes", "",
             "Generated from the recipe headers. Full entries list the tasks they serve and quote the",
             "recipe's core guardrail. The short topic pointers are discovery links; they list tasks only",
             "where the header names some beyond the summary. Both tiers require reading the recipe before",
             "advising. A dated source check is a maintenance reminder, not verification of every claim or",
             "live control.", ""]
    group = None
    pointer = False
    for m, _ in catalog:
        route = m["router"]
        if route["tier"] == "pointer" and not pointer:
            lines += ["## More recipes by topic", ""]
            pointer = True
            group = None
        if route["group"] != group:
            group = route["group"]
            if route["tier"] == "pointer":
                lines += ["### " + group, ""]
        lines += [f"- **`recipes/{m['id']}.md`** — {m['title']}.", wrap(m["summary"])]
        if m["scope"]["tasks"]:
            lines += [wrap("*Use for:* " + "; ".join(m["scope"]["tasks"]))]
        if route["tier"] == "full":
            lines += [wrap("*Core guardrail:* " + m["guardrails"][0]["text"])]
        if m["kind"] == "platform":
            lines += [wrap(f"*Dated source check:* {m['checked']}.")]
        lines += [""]
    lines += [ROUTER_END]
    return "\n".join(lines)


def render_capabilities(catalog):
    lines = [TABLE_START,
             "These are described actions, not permissions or tools that the plugin runs. An empty cell means",
             "no declared action of that kind. The privacy gate also applies to unlisted outbound steps.", "",
             "| Recipe | Browse | Local script | Extensions | Data transfer | Contact | Privacy gate |",
             "| --- | --- | --- | --- | --- | --- | --- |"]
    for m, _ in sorted(catalog, key=lambda item: item[0]["id"]):
        cells = [f"[{m['id']}]({SKILL_PATH}/recipes/{m['id']}.md)"]
        cells += [", ".join(m["capabilities"][k]).replace("|", "&#124;") or "—"
                  for k in ("browse", "local_script", "extensions", "data_transfer", "contact")]
        cells += ["required" if m["gates"] else "—"]
        lines.append("| " + " | ".join(cells) + " |")
    lines += [TABLE_END]
    return "\n".join(lines)


def replace_region(text, start, end, content):
    require(text.count(start) == text.count(end) == 1, f"expected one {start} / {end} region")
    before, rest = text.split(start)
    _, after = rest.split(end)
    return before + content + after


def generated_files(root, catalog):
    skill_file = root / SKILL_PATH / "SKILL.md"
    text = skill_file.read_text(encoding="utf-8")
    rendered = replace_region(text, ROUTER_START, ROUTER_END, render_router(catalog))
    ids = {m["id"] for m, _ in catalog}
    # Removed/renamed recipes can remain in the old generated region until this
    # very write. Validate the replacement and the retained handwritten text.
    for target in recipe_references(rendered):
        require(target in ids, f"SKILL.md: missing recipe {target}")
    yield skill_file, rendered
    readme = root / "README.md"
    yield readme, replace_region(readme.read_text(encoding="utf-8"), TABLE_START, TABLE_END,
                                render_capabilities(catalog))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--check", action="store_true", help="fail on schema, references, freshness or generated drift")
    modes.add_argument("--write", action="store_true", help="regenerate the router and README table")
    modes.add_argument("--export-body", type=Path, help="add a reviewed body using --metadata JSON")
    parser.add_argument("--metadata", type=Path, help="complete header object for --export-body")
    args = parser.parse_args(argv)
    try:
        require(bool(args.export_body) == bool(args.metadata), "--export-body and --metadata must be used together")
        replacement = None
        if args.export_body:
            metadata = json.loads(args.metadata.read_text(encoding="utf-8"))
            require(isinstance(metadata, dict), "metadata must be an object")
            slug = metadata.get("id")
            require(string(slug) and SLUG.fullmatch(slug), "invalid export id")
            require(not (ROOT / SKILL_PATH / "recipes" / f"{slug}.md").exists(),
                    "export is for new recipes; edit an existing public recipe directly")
            body = args.export_body.read_text(encoding="utf-8")
            require(not body.startswith("---\n"), "export body already has a header")
            replacement = (f"{slug}.md", emit_recipe(metadata, body))
        catalog = load_catalog(replacement=replacement)
        outputs = list(generated_files(ROOT, catalog))
        stale = [str(p.relative_to(ROOT)) for p, text in outputs if p.read_text(encoding="utf-8") != text]
        if args.check:
            require(not stale, "generated output differs: " + ", ".join(stale) + "; run --write")
        else:
            if replacement:
                (ROOT / SKILL_PATH / "recipes" / replacement[0]).write_text(replacement[1], encoding="utf-8")
            for path, text in outputs:
                path.write_text(text, encoding="utf-8")
        print(f"Validated {len(catalog)} recipe headers, references, privacy capabilities and generated files.")
        return 0
    except (CatalogError, OSError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
