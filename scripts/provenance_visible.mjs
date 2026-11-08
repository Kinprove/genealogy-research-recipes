/** Extract prose using the repository's pinned Markdown and HTML parsers. */
import { readFileSync } from "node:fs";
import { createRequire } from "node:module";
import { pathToFileURL } from "node:url";

const require = createRequire(new URL("../tests/markdown-links/package.json", import.meta.url));
const MarkdownIt = require("markdown-it");
const { parseFragment } = await import(pathToFileURL(require.resolve("parse5")).href);
const markdown = new MarkdownIt({ html: true });
const excluded = new Set(["code", "pre", "script", "style", "template", "head", "title", "desc", "noscript"]);
const blocks = new Set(["p", "div", "li", "tr", "blockquote", "section", "article", "h1", "h2", "h3", "h4", "h5", "h6"]);

function prose(node) {
  if (node.nodeName === "#text") return node.value;
  if (node.nodeName === "#comment" || excluded.has(node.tagName)) return "";
  const attributes = new Map((node.attrs ?? []).map(({ name, value }) => [name, value]));
  if (attributes.has("hidden") || /(?:^|;)\s*(?:display\s*:\s*none|visibility\s*:\s*hidden)\s*(?:!important)?\s*(?:;|$)/i.test(attributes.get("style") ?? "")) return "";
  if (node.tagName === "br") return "\n";
  const text = (node.childNodes ?? []).map(prose).join("");
  // Keep a source-shaped link label recognizable as a citation. URL/title
  // attributes never enter this text; exact raw anchors are retained in Python.
  if (node.tagName === "a") return `[${text}]`;
  if (node.tagName === "td" || node.tagName === "th") return text + " ";
  return text + (blocks.has(node.tagName) ? "\n\n" : "");
}

export function visibleText(source) {
  if (typeof source !== "string") throw new TypeError("Markdown input must be a string");
  return prose(parseFragment(markdown.render(source)));
}

if (process.argv[1] && pathToFileURL(process.argv[1]).href === import.meta.url) {
  const inputs = JSON.parse(readFileSync(0, "utf8"));
  if (!Array.isArray(inputs)) throw new TypeError("Expected a Markdown string array");
  process.stdout.write(JSON.stringify(inputs.map(visibleText)));
}
