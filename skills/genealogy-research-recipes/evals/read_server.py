"""Evaluation-only stdio MCP server: read complete recipes or a judgment section."""

import json
from pathlib import Path
import re
import sys

TOOL = {
    "name": "read_file",
    "description": "Read a recipe in full by path recipes/<id>.md. For judgment recipes only, optionally name a section heading to read its rules. No writes, network or files outside recipes are accessible.",
    "inputSchema": {
        "type": "object", "additionalProperties": False, "required": ["path"],
        "properties": {"path": {"type": "string"}, "section": {"type": "string"}},
    },
    "annotations": {"readOnlyHint": True, "openWorldHint": False},
}


def read_recipe(root, path, section=None):
    candidate = Path(path)
    if candidate.parts and candidate.parts[0] == "recipes":
        candidate = Path(*candidate.parts[1:])
    destination = (root / candidate).resolve()
    if destination.parent != root.resolve() or destination.suffix != ".md" or not destination.is_file():
        raise ValueError("Only existing Markdown files directly in recipes/ may be read")
    lines = destination.read_text(encoding="utf-8").splitlines()
    start, end = 0, len(lines)
    if section:
        matches = [(i, len(match[1])) for i, line in enumerate(lines)
                   if (match := re.match(r"^(#{1,6}) +(.+?)\s*$", line))
                   and match[2].casefold() == section.lstrip("# ").casefold()]
        if len(matches) != 1:
            raise ValueError("Section heading must match exactly once")
        start, level = matches[0]
        for index in range(start + 1, len(lines)):
            match = re.match(r"^(#{1,6}) +", lines[index])
            if match and len(match[1]) <= level:
                end = index
                break
    return "\n".join(f"{index+1}\t{lines[index]}" for index in range(start, end))


def dispatch(message, root):
    method, params = message.get("method"), message.get("params", {})
    if method == "initialize":
        return {"protocolVersion": params.get("protocolVersion", "2024-11-05"),
                "capabilities": {"tools": {}}, "serverInfo": {"name": "recipe-evals", "version": "1.0.0"}}
    if method == "ping":
        return {}
    if method == "tools/list":
        return {"tools": [TOOL]}
    if method == "tools/call":
        try:
            if params.get("name") != "read_file":
                raise ValueError("Unknown tool")
            content = read_recipe(root, **params["arguments"])
            return {"content": [{"type": "text", "text": content}], "isError": False}
        except (OSError, TypeError, KeyError, ValueError) as error:
            return {"content": [{"type": "text", "text": str(error)}], "isError": True}
    raise ValueError("Unsupported method")


def main():
    root = Path(sys.argv[1]).resolve()
    for line in sys.stdin:
        request = {}
        try:
            request = json.loads(line)
            if "id" not in request:
                continue  # notifications never receive replies
            result = dispatch(request, root)
            response = {"jsonrpc": "2.0", "id": request["id"], "result": result}
        except (ValueError, KeyError, TypeError) as error:
            response = {"jsonrpc": "2.0", "id": request.get("id"),
                        "error": {"code": -32601, "message": str(error)}}
        print(json.dumps(response, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
