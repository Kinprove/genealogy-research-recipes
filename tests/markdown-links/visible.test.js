import assert from "node:assert/strict";
import test from "node:test";
import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import { visibleText } from "../../scripts/provenance_visible.mjs";

test("link labels remain, while destinations and all title syntaxes are excluded", () => {
  for (const title of ['"From the inspected excerpt [S1 @2026-11-07]"', "'From the inspected excerpt [S1 @2026-11-07]'", "(From the inspected excerpt [S1 @2026-11-07])"]) {
    const text = visibleText(`The archive offers free copies. [Help](https://example.org/ ${title})`);
    assert.match(text, /Help/);
    assert.doesNotMatch(text, /S1|inspected|example\.org/);
  }
  assert.match(visibleText("From the inspected excerpt, search exists. [S1 @2026-11-07](https://example.org/)"), /\[S1 @2026-11-07\]/);
});

test("reference definitions and link metadata never supply prose", () => {
  const text = visibleText('The archive offers free copies. [Help][ref]\n\n[ref]: https://example.org/ "From the inspected excerpt [S1 @2026-11-07]"');
  assert.match(text, /Help/);
  assert.doesNotMatch(text, /S1|inspected|example\.org/);
});

test("code, comments, attributes and hidden DOM content cannot supply evidence", () => {
  for (const hidden of ['`[S1]`', '``[S1]``', '<!-- [S1] -->', '<span title=" > [S1]"></span>', '<script>[S1]</script>', '<svg><title>[S1]</title><desc>[S1]</desc></svg>', '<span hidden>[S1]</span>', '<span style="display: none">[S1]</span>']) {
    assert.doesNotMatch(visibleText(`Ordinary prose. ${hidden}`), /S1/);
  }
  assert.match(visibleText("<strong>From the inspected excerpt</strong>, search exists. [S1]"), /inspected excerpt.*\[S1\]/);
});

test("batch protocol returns only parsed text and keeps escaped visible markers", () => {
  const helper = fileURLToPath(new URL("../../scripts/provenance_visible.mjs", import.meta.url));
  const output = JSON.parse(execFileSync(process.execPath, [helper], { input: JSON.stringify(['Visible \\[S1\\]', '[Help](https://example.org/ "hidden [S2]")']), encoding: "utf8" }));
  assert.match(output[0], /\[S1\]/);
  assert.doesNotMatch(output[1], /S2/);
});
