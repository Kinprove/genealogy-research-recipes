"""Build channel distributions from a Git commit; check their policy and local links."""

import argparse
import fnmatch
import html
from html.parser import HTMLParser
import io
import json
from pathlib import Path, PurePosixPath
import posixpath
import re
import subprocess
import sys
import tarfile
from urllib.parse import unquote, urlsplit
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL = "skills/genealogy-research-recipes"
COMMON = (
    "README.md", "LICENSE", "NOTICE", "assets/banner.png",
    SKILL + "/SKILL.md", SKILL + "/CHANGELOG.md", SKILL + "/LICENSE", SKILL + "/NOTICE",
    # fnmatch's * also includes subdirectories.
    SKILL + "/recipes/*.md", SKILL + "/sources/*.md", SKILL + "/resources/*.json",
)
HELPER = SKILL + "/scripts/lookup_beider_name.py"
TARGETS = {
    "claude-directory": COMMON + (".claude-plugin/plugin.json", ".claude-plugin/icon.png"),
    "hermes-catalog": COMMON + ("plugin.yaml", "__init__.py", HELPER),
    "openai-plugin": COMMON + ("plugin.json", "assets/logo.png", HELPER),
}
IMAGES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico"}
TEXT = {".md", ".txt", ".json", ".yaml", ".yml"}
PACKAGE_FILES = (
    "package.json", "package-lock.json", "npm-shrinkwrap.json", "yarn.lock",
    "pnpm-lock.yaml", "bun.lock", "bun.lockb", "requirements*.txt", "pyproject.toml",
    "pipfile*", "poetry.lock", "uv.lock",
)
# Top-level fields in the official Claude plugin reference (including directory metadata).
CLAUDE_FIELDS = {
    "$schema", "name", "displayName", "version", "description", "author", "homepage",
    "repository", "license", "keywords", "metadata", "icon", "documentationUrl",
    "supportUrl", "privacyPolicyUrl", "termsOfServiceUrl", "defaultEnabled", "dependencies",
    "settings", "userConfig", "types", "channels", "skills", "commands", "agents", "hooks",
    "mcpServers", "lspServers", "outputStyles", "workflows", "experimental",
}


def archive_files(repository, source):
    """Read regular files from git archive, without consulting the working tree."""
    sha = subprocess.run(
        ["git", "rev-parse", "--verify", "--end-of-options", source + "^{commit}"],
        cwd=repository, capture_output=True, text=True, check=True,
    ).stdout.strip()
    data = subprocess.run(["git", "archive", "--format=tar", sha], cwd=repository,
                          capture_output=True, check=True).stdout
    files = {}
    with tarfile.open(fileobj=io.BytesIO(data), mode="r:") as archive:
        for member in archive:
            if member.isdir():
                continue
            path = PurePosixPath(member.name)
            if path.is_absolute() or ".." in path.parts:
                raise ValueError("unsafe archive path: " + member.name)
            # Reject selected symlinks rather than dereferencing a working-tree file.
            if not member.isfile():
                if any(fnmatch.fnmatchcase(member.name, pattern)
                       for patterns in TARGETS.values() for pattern in patterns):
                    raise ValueError("non-regular archive file: " + member.name)
                continue
            with archive.extractfile(member) as stream:
                files[member.name] = stream.read()
    return files


def tree_files(root):
    root = Path(root)
    if not root.is_dir():
        raise ValueError("not a distribution directory: " + str(root))
    files = {}
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            raise ValueError("symlink in distribution: " + str(path))
        if path.is_file():
            files[path.relative_to(root).as_posix()] = path.read_bytes()
    return files


def check_claude_files(files):
    for name, data in sorted(files.items()):
        path = PurePosixPath(name)
        if any(fnmatch.fnmatchcase(path.name.lower(), pattern) for pattern in PACKAGE_FILES):
            raise ValueError(name + ": package-manager file is disallowed")
        extension = path.suffix.lower()
        if extension not in TEXT | IMAGES and path.name not in {"LICENSE", "README.md", ".gitignore"}:
            raise ValueError(name + ": disallowed file type")
        if data.startswith(b"#!"):
            raise ValueError(name + ": shebang is disallowed")
        if extension not in IMAGES:
            try:
                data.decode("utf-8")
            except UnicodeDecodeError as exc:
                raise ValueError(name + ": text is not UTF-8") from exc
    manifest = ".claude-plugin/plugin.json"
    if manifest not in files:
        raise ValueError("missing " + manifest)
    plugin = json.loads(files[manifest])
    if not isinstance(plugin, dict):
        raise ValueError(manifest + ": expected an object")
    unknown = set(plugin) - CLAUDE_FIELDS
    if unknown:
        raise ValueError(manifest + ": undocumented fields: " + ", ".join(sorted(unknown)))


def check_claude(root):
    check_claude_files(tree_files(root))


class HTMLLinks(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []

    def handle_starttag(self, tag, attrs):
        self.links.extend(value for key, value in attrs if key in {"href", "src"} and value)


def markdown_links(text):
    """Extract inline, reference and HTML destinations, excluding metadata and code."""
    text = re.sub(r"\A---\n.*?\n(?:---|\.\.\.)\s*\n", "", text, flags=re.S)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    prose = []
    fence = None
    list_indents = []
    for line in text.splitlines():
        line = line.expandtabs(4)
        indent = len(line) - len(line.lstrip())
        if line.strip():
            while list_indents and indent < list_indents[-1]:
                list_indents.pop()
        item = re.match(r"^ *(?:[-+*]|\d+[.)]) +", line)
        if item and indent < (list_indents[-1] if list_indents else 0) + 4:
            list_indents.append(item.end())
        marker = re.match(r"^ *(`{3,}|~{3,})", line)
        if fence:
            if re.match(r"^ *" + re.escape(fence[0]) + "{" + str(len(fence)) + r",}\s*$", line):
                fence = None
        elif marker and indent < (list_indents[-1] if list_indents else 0) + 4:
            fence = marker.group(1)
        elif indent < (list_indents[-1] if list_indents else 0) + 4:
            prose.append(line)
    text = "\n".join(prose)
    text = re.sub(r"(`+).*?\1", "", text, flags=re.S)
    # Destinations may have escaped punctuation, balanced parentheses or angle-quoted spaces.
    destination = r"(<[^>\n]*>|(?:\\.|[^\s()\\]|\((?:\\.|[^()\\])*\))+)"
    label = r"\[((?:\\.|[^\]\\])*)\]"
    definitions = {}

    def definition(match):
        definitions[" ".join(match.group(1).split()).casefold()] = match.group(2)
        return ""

    text = re.sub(r"(?m)^ {0,3}" + label + r":\s*" + destination + r"[^\n]*$", definition, text)
    links = []

    def inline(match):
        links.append(match.group(2))
        return ""

    text = re.sub(label + r"\(\s*" + destination + r"(?:\s+[^\n]*?)?\s*\)", inline, text)
    for match in re.finditer(label + r"(?:\[([^\]]*)\])?", text):
        key = " ".join((match.group(2) or match.group(1)).split()).casefold()
        if key in definitions:
            links.append(definitions[key])
    parser = HTMLLinks()
    parser.feed(text)
    links.extend(parser.links)
    return [html.unescape(re.sub(r"\\([!\"#$%&'()*+,\-./:;<=>?@\[\]^_`{|}~\\])", r"\1", link.strip("<>")))
            for link in links]


def check_link_files(files):
    errors = []
    for name, data in sorted(files.items()):
        if PurePosixPath(name).suffix.lower() != ".md":
            continue
        for link in markdown_links(data.decode("utf-8")):
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue
            location = unquote(url.path)
            target = posixpath.normpath(
                posixpath.join(posixpath.dirname(name), location) if location else name)
            # A leading slash is relative to the distribution root, as on GitHub.
            if location.startswith("/"):
                target = posixpath.normpath(location.lstrip("/"))
            if target == ".." or target.startswith("../"):
                errors.append(f"{name}: {link!r}: target is outside the distribution")
            elif target == ".":
                continue
            elif target not in files and not any(path.startswith(target.rstrip("/") + "/") for path in files):
                errors.append(f"{name}: {link!r}: missing target {target}")
    if errors:
        raise ValueError("\n".join(errors))


def check_links(path):
    path = Path(path)
    if path.is_dir():
        files = tree_files(path)
    else:
        with zipfile.ZipFile(path) as archive:
            files = {name: archive.read(name) for name in archive.namelist() if not name.endswith("/")}
    check_link_files(files)


def build(target, source, out, repository=ROOT):
    archived = archive_files(repository, source)
    files = {}
    for pattern in TARGETS[target]:
        matches = [name for name in archived if fnmatch.fnmatchcase(name, pattern)]
        if not matches:
            raise ValueError("allowlisted pattern matches nothing: " + pattern)
        for name in matches:
            destination = name + ".md" if target == "claude-directory" and PurePosixPath(name).name == "NOTICE" else name
            files[destination] = archived[name]
    if target == "claude-directory":
        check_claude_files(files)
    out = Path(out)
    if out.exists() and (not out.is_dir() or any(out.iterdir())):
        raise ValueError("output directory must be empty: " + str(out))
    out.mkdir(parents=True, exist_ok=True)
    if target == "openai-plugin":
        version = json.loads(files["plugin.json"])["version"]
        if not isinstance(version, str) or not re.fullmatch(r"\d+\.\d+\.\d+", version):
            raise ValueError("plugin.json: expected a release version")
        result = out / ("genealogy-research-recipes-" + version + ".zip")
        with zipfile.ZipFile(result, "w", compression=zipfile.ZIP_STORED) as archive:
            for name, data in sorted(files.items()):
                entry = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
                entry.create_system = 3
                entry.external_attr = 0o100644 << 16
                archive.writestr(entry, data)
        return result
    for name, data in sorted(files.items()):
        path = out / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        path.chmod(0o644)
    return out


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--target", choices=sorted(TARGETS))
    mode.add_argument("--check-claude", type=Path, metavar="TREE")
    mode.add_argument("--check-links", type=Path, metavar="TREE_OR_ZIP")
    parser.add_argument("--source", help="source commit or ref (working-tree changes are ignored)")
    parser.add_argument("--out", type=Path)
    args = parser.parse_args(argv)
    if args.target and (not args.source or args.out is None):
        parser.error("--target requires --source and --out")
    try:
        if args.target:
            print(build(args.target, args.source, args.out))
        elif args.check_claude:
            check_claude(args.check_claude)
            print("Claude directory policy: PASS")
        else:
            check_links(args.check_links)
            print("Relative Markdown links: PASS")
    except (ValueError, OSError, subprocess.CalledProcessError, zipfile.BadZipFile, tarfile.TarError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
