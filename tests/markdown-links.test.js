/** Resolve repository Markdown links offline, including GitHub heading fragments. */
import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { existsSync, mkdtempSync, mkdirSync, readFileSync, readdirSync, realpathSync, rmSync, statSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { dirname, isAbsolute, join, relative, resolve, sep } from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";
import GithubSlugger from "github-slugger";
import MarkdownIt from "markdown-it";
import { parseFragment } from "parse5";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const markdown = new MarkdownIt({ html: true });
const external = (href) => /^(?:[a-z][a-z\d+.-]*:|\/\/)/i.test(href);

function visit(node, callback) {
  callback(node);
  for (const child of node.childNodes ?? []) visit(child, callback);
}

function renderedText(inline) {
  const fragment = parseFragment(markdown.renderer.renderInline(inline.children, markdown.options));
  let text = "";
  visit(fragment, (node) => {
    if (node.nodeName === "#text") text += node.value;
  });
  return text;
}

function markdownDocument(text) {
  // YAML metadata is not a Setext heading. Preserve line numbers in diagnostics.
  text = text.replace(/\r\n/g, "\n").replace(
    /^---\n[\s\S]*?\n(?:---|\.\.\.)[ \t]*(?:\n|$)/,
    (header) => "\n".repeat(header.split("\n").length - 1),
  );
  const tokens = markdown.parse(text, {});
  const slugger = new GithubSlugger();
  const links = [];
  const anchors = new Set();
  for (const [index, token] of tokens.entries()) {
    if (token.type === "heading_open") anchors.add(slugger.slug(renderedText(tokens[index + 1])));
    const line = token.map ? token.map[0] + 1 : 1;
    for (const child of [token, ...(token.children ?? [])]) {
      if (child.type === "link_open") links.push({ href: child.attrGet("href"), line });
      if (child.type === "image") links.push({ href: child.attrGet("src"), line });
      if (child.type === "html_inline" || child.type === "html_block") {
        visit(parseFragment(child.content), (node) => {
          for (const { name, value } of node.attrs ?? []) {
            if (name === "href" || name === "src") links.push({ href: value, line });
            if (name === "id" || (node.tagName === "a" && name === "name")) anchors.add(value);
          }
        });
      }
    }
  }
  return { links, anchors };
}

function brokenLinks(root, paths) {
  root = realpathSync(root);
  const documents = new Map();
  function document(path) {
    if (!documents.has(path)) documents.set(path, markdownDocument(readFileSync(path, "utf8")));
    return documents.get(path);
  }
  const errors = [];
  for (const source of paths) {
    for (const { href, line } of document(source).links) {
      if (external(href)) continue;
      const hash = href.indexOf("#");
      const fragment = hash < 0 ? "" : decodeURIComponent(href.slice(hash + 1));
      const location = decodeURIComponent((hash < 0 ? href : href.slice(0, hash)).split("?")[0]);
      let target = location
        ? resolve(location.startsWith("/") ? root : dirname(source), location.replace(/^\/+/, ""))
        : source;
      if (existsSync(target)) target = realpathSync(target);
      const destination = relative(root, target);
      const prefix = `${relative(root, source)}:${line}: ${JSON.stringify(href)}`;
      if (destination === ".." || destination.startsWith(`..${sep}`) || isAbsolute(destination)) {
        errors.push(`${prefix}: target is outside the repository`);
      } else if (!existsSync(target)) {
        errors.push(`${prefix}: missing target ${destination}`);
      } else if (fragment) {
        // GitHub displays a directory's README. Other formats have their own
        // fragments (e.g. PDF #page=2), which are not Markdown heading IDs.
        if (statSync(target).isDirectory()) {
          target = join(target, readdirSync(target).find((name) => /^readme\.md$/i.test(name)) ?? "README.md");
        }
        if (/\.md$/i.test(target) && (!existsSync(target) || !document(target).anchors.has(fragment))) {
          errors.push(`${prefix}: missing anchor #${fragment} in ${relative(root, target)}`);
        }
      }
    }
  }
  return errors;
}

function fixture(t, files) {
  const root = realpathSync(mkdtempSync(join(tmpdir(), "markdown-links-")));
  t.after(() => rmSync(root, { recursive: true, force: true }));
  function write(name, text) {
    const path = join(root, name);
    mkdirSync(dirname(path), { recursive: true });
    writeFileSync(path, text);
    return path;
  }
  for (const [name, text] of Object.entries(files)) write(name, text);
  return { root, write };
}

test("missing recipes and renamed headings fail", (t) => {
  const { root, write } = fixture(t, {
    "SKILL.md": "[recipe](recipes/example.md#verification--privacy-discipline)\n",
    "recipes/example.md": "## Verification & privacy discipline\n",
  });
  const source = join(root, "SKILL.md");
  assert.deepEqual(brokenLinks(root, [source]), []);
  const target = write("recipes/example.md", "## Renamed heading\n");
  assert.match(brokenLinks(root, [source])[0], /missing anchor #verification--privacy-discipline/);
  rmSync(target);
  assert.match(brokenLinks(root, [source])[0], /missing target recipes\/example.md/);
});

test("relative paths, resources, queries and percent-encoded fragments resolve", (t) => {
  const { root } = fixture(t, {
    "recipes/first.md": [
      "[source](../sources/second.md?raw=1#%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D1%82-%E4%BD%A0%E5%A5%BD)",
      "[resource](../resources/names.json)", "[root](/README.md#home)", "[self](#local)", "## Local",
    ].join("\n"),
    "sources/second.md": "## Привет 你好\n",
    "resources/names.json": "{}",
    "README.md": "# Home\n",
  });
  assert.deepEqual(brokenLinks(root, [join(root, "recipes/first.md")]), []);
});

test("reference links, images, titles, parentheses and spaces are parsed", (t) => {
  const { root, write } = fixture(t, {
    "README.md": [
      '[inline](docs/file\\(copy\\).md#title "a title")',
      "[full][target]", "[collapsed][]", "[shortcut]", "![image](assets/example.svg)",
      "[spaced](<docs/space name.md#title> 'title')", "",
      "[target]: docs/file(copy).md#title", "[collapsed]: docs/file(copy).md#title",
      "[shortcut]: <docs/space name.md#title>",
    ].join("\n"),
    "docs/file(copy).md": "# Title\n",
    "docs/space name.md": "# Title\n",
    "assets/example.svg": "<svg/>",
  });
  const source = join(root, "README.md");
  assert.equal(markdownDocument(readFileSync(source, "utf8")).links.length, 6);
  assert.deepEqual(brokenLinks(root, [source]), []);
  rmSync(join(root, "assets/example.svg"));
  assert.match(brokenLinks(root, [source])[0], /missing target assets\/example.svg/);
  write("docs/file(copy).md", "# Changed\n");
  assert.equal(brokenLinks(root, [source]).length, 4);
});

test("heading IDs use rendered text, Unicode and duplicate collision rules", () => {
  const { anchors } = markdownDocument([
    "## Verification & privacy discipline", "## Apply *je dis* corrections",
    '## [Linked](https://example.org) `code` <em>text</em> &amp; ![image](a.svg)',
    "## Привет 你好", "## 😄 emoji", "## foo", "## foo", "## foo-1", "## foo",
    "Setext heading", "==============",
  ].join("\n"));
  assert.deepEqual(anchors, new Set([
    "verification--privacy-discipline", "apply-je-dis-corrections", "linked-code-text--",
    "привет-你好", "-emoji", "foo", "foo-1", "foo-1-1", "foo-2", "setext-heading",
  ]));
});

test("code, comments and front matter do not supply links or headings", () => {
  const document = markdownDocument([
    "---", "title: metadata", "link: '[metadata](missing.md)'", "---",
    "`[inline code](missing.md)`", "", "    [indented code](missing.md)", "    # Indented heading", "",
    "````markdown", "```example", "[fenced code](missing.md)", "## Fenced heading", "```", "````",
    '<!-- [comment](missing.md) <a href="missing.md" id="comment"> -->', "", "## Visible",
  ].join("\n"));
  assert.deepEqual(document.links, []);
  assert.deepEqual(document.anchors, new Set(["visible"]));
});

test("HTML links, custom anchors and directory READMEs resolve", (t) => {
  const { root, write } = fixture(t, {
    "README.md": [
      '<a id="custom"></a>', '<a name="legacy"></a>',
      '<a href="#custom">custom</a> [legacy](#legacy)', "",
      '<img src="assets/example.svg">', "", "[directory](docs/#title)",
    ].join("\n"),
    "assets/example.svg": "<svg/>",
    "docs/readme.md": "# Title\n",
  });
  const source = join(root, "README.md");
  assert.equal(markdownDocument(readFileSync(source, "utf8")).links.length, 4);
  assert.deepEqual(brokenLinks(root, [source]), []);
  write("docs/readme.md", "# Changed\n");
  assert.match(brokenLinks(root, [source])[0], /missing anchor #title/);
});

test("table links are checked", (t) => {
  const { root } = fixture(t, {
    "README.md": "| Recipe |\n| --- |\n| [missing](missing.md) |\n",
  });
  assert.match(brokenLinks(root, [join(root, "README.md")])[0], /missing target missing.md/);
});

test("external URLs are not fetched; other formats keep their own fragments", (t) => {
  const { root } = fixture(t, {
    "README.md": [
      "[external](https://example.invalid/missing.md#absent)",
      "[protocol relative](//example.invalid/missing.md)", "[mail](mailto:someone@example.invalid)",
      "[PDF](document.pdf#page=2)",
    ].join("\n"),
    "document.pdf": "a fixture, not a real PDF",
  });
  assert.deepEqual(brokenLinks(root, [join(root, "README.md")]), []);
});

test("missing local anchors and resources report the source file and line", (t) => {
  const { root } = fixture(t, { "docs/example.md": "# Title\n\n[bad](#Title) [missing](absent.json)\n" });
  const errors = brokenLinks(root, [join(root, "docs/example.md")]);
  assert.equal(errors.length, 2);
  assert.ok(errors.every((error) => error.startsWith("docs/example.md:3:")));
  assert.match(errors[0], /missing anchor #Title/);
  assert.match(errors[1], /missing target docs\/absent.json/);
});

test("links outside the repository fail", (t) => {
  const { root } = fixture(t, { "README.md": "[outside](../outside.md)\n" });
  assert.match(brokenLinks(root, [join(root, "README.md")])[0], /outside the repository/);
});

test("every tracked Markdown file's relative links and anchors resolve", () => {
  // Include dot directories; exclude installed runtimes, builds and node_modules.
  const names = execFileSync("git", ["ls-files", "-z", "--", "*.md"], { cwd: ROOT, encoding: "utf8" });
  const paths = names.split("\0").filter(Boolean).map((name) => join(ROOT, name));
  assert.ok(paths.length > 0, "no tracked Markdown files found");
  assert.ok(paths.some((path) => markdownDocument(readFileSync(path, "utf8")).links.some(({ href }) => !external(href))),
    "no local links found");
  const errors = brokenLinks(ROOT, paths);
  assert.deepEqual(errors, [], errors.join("\n"));
});
