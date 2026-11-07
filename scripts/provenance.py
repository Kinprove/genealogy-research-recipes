#!/usr/bin/env python3
"""Offline source/claim contracts; importing prose never establishes verification."""

import argparse
import datetime as dt
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = Path('skills/genealogy-research-recipes')
START = '<!-- provenance-ledger:start -->'
END = '<!-- provenance-ledger:end -->'
DEBT = Path('tests/provenance_legacy.json')
REPORT = Path('PROVENANCE.md')
ACCESS = {'read', 'partial', 'snippet-only', 'refused', 'private', 'unknown'}
KINDS = {'video', 'help-page', 'forum', 'statute', 'pdf', 'catalogue', 'web-page', 'unknown'}
CLAIM_KINDS = {'platform-ui', 'fee', 'portal-availability', 'custody', 'historical',
               'method', 'example', 'unclassified'}
AGES = {'fee': 90, 'portal-availability': 90, 'platform-ui': 180, 'custody': 180}
ENTRY = re.compile(r'^(?:- \*\*([A-Z]\d+)\b|([0-9]+)\.\s|\|\s*([A-Z]\d+)\s*\|)')
SOURCE_ID = r'(?:[SHPOCNB]\d+(?:-addition-\d+)?|U[0-9a-f]{12})'
MARKER = re.compile(r'[\[(](' + SOURCE_ID + r'\b[^\]\n)]*)[\])]')
CURRENT = re.compile(
    r'https?://|\b[a-zA-Z0-9-]+\.(?:com|org|gov|net|ie|uk)\b|[$€£]|'
    r'\b(?:currently|as of|now available|fees?|subscription|custod(?:y|ian)|'
    r'National Archives|National Library|State Archives|ScotlandsPeople|GRONI)\b', re.I)
HEDGE = re.compile(r'\b(?:reports?|reported|according to|snippet|search[- ]result|'
                   r'not (?:independently )?(?:read|inspected|verified)|could not|'
                   r'unverified|partial|refused|inaccessible|private video|HTTP 403)\b', re.I)
SOURCE_FIELDS = {'id', 'kind', 'urls', 'published', 'retrieved', 'access', 'rights',
                 'basis', 'entry_sha256', 'claims', 'review'}
CLAIM_FIELDS = {'id', 'kind', 'anchor', 'sources', 'checked', 'stated_as', 'review'}


class ProvenanceError(ValueError):
    pass


def require(ok, message):
    if not ok:
        raise ProvenanceError(message)


def digest(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f'duplicate JSON key: {key}')
        result[key] = value
    return result


def loads(text):
    return json.loads(text, object_pairs_hook=unique_object)


def urls(text):
    """Keep exact URL bytes, including case, query order, escapes and fragments."""
    result = []
    for match in re.finditer(r'https?://[^\s<>"`]+', text):
        value = match[0].rstrip('.,;')
        while value.endswith(')') and value.count(')') > value.count('('):
            value = value[:-1]
        if value not in result:
            result.append(value)
    return result


def split_ledger(text):
    require(text.count(START) == text.count(END), 'unbalanced ledger delimiters')
    if START not in text:
        return text, None
    require(text.count(START) == 1, 'duplicate ledger block')
    before, rest = text.split(START)
    block, after = rest.split(END)
    require('## Credits' in after and '## Credits' not in before, 'ledger must precede final Credits')
    lines = block.strip().splitlines()
    require(lines[:2] == ['```yaml', 'schema: 1'] and lines[-1:] == ['```'], 'invalid ledger envelope')
    ledger = {'schema': 1, 'sources': [], 'claims': []}
    field = None
    seen = set()
    for line in lines[2:-1]:
        if line in ('sources:', 'claims:'):
            field = line[:-1]
            require(field not in seen, 'duplicate ledger list')
            seen.add(field)
        else:
            require(field is not None and line.startswith('  - {'), 'use one JSON object per YAML list item')
            ledger[field].append(loads(line[4:]))
    require(seen == {'sources', 'claims'}, 'ledger needs sources and claims lists')
    return before.rstrip() + '\n\n' + after.lstrip(), ledger


def render_ledger(ledger):
    lines = [START, '```yaml', 'schema: 1']
    for field in ('sources', 'claims'):
        lines.append(field + ':')
        lines.extend('  - ' + json.dumps(item, ensure_ascii=False, separators=(',', ':'))
                     for item in ledger[field])
    return '\n'.join(lines + ['```', END])


def attach_ledger(text, ledger):
    plain, _ = split_ledger(text)
    require(plain.count('## Credits\n') == 1, 'needs one Credits section')
    before, after = plain.split('## Credits\n')
    return before.rstrip() + '\n\n' + render_ledger(ledger) + '\n\n## Credits\n' + after


def source_entries(text):
    """Bibliographic blocks, plus explicit URL-only residuals; no inferred access.

    Numbered bibliographies get N IDs. Unlabelled bullets get B IDs. Historical
    H3 additions stay separate records rather than overwriting the first H3.
    """
    plain, _ = split_ledger(text)
    plain = plain.split('## Credits')[0]
    entries = {}
    current = None
    lines = []
    repetitions = Counter()
    bullet = 0

    def flush():
        if current:
            entries[current] = '\n'.join(lines).strip()

    for line in plain.splitlines():
        match = ENTRY.match(line)
        new = None
        if match:
            base = match[1] or ('N' + match[2] if match[2] else match[3])
            repetitions[base] += 1
            new = base if repetitions[base] == 1 else f'{base}-addition-{repetitions[base] - 1}'
        elif line.startswith('- ') and urls(line):
            bullet += 1
            new = f'B{bullet}'
        # Some unlabelled bibliographic bullets put their URL on a continuation.
        elif line.startswith('- '):
            bullet += 1
            new = f'B{bullet}'
        if new or line.startswith('#'):
            flush()
            current, lines = new, []
        if current:
            lines.append(line)
    flush()
    covered = {url for entry in entries.values() for url in urls(entry)}
    for block in re.split(r'\n\s*\n', plain):
        for url in urls(block):
            if url not in covered:
                entries['U' + digest(url)[:12]] = block.strip()
                covered.add(url)
    return entries


def recipe_body(text):
    if text.startswith('---\n'):
        _, separator, text = text[4:].partition('\n---\n')
        require(separator, 'unclosed recipe header')
    return text.lstrip('\n')


def prose_blocks(text):
    """Keep exact anchors; omit code fences, headings and the contents navigation."""
    body = recipe_body(text)
    fence = None
    contents = False
    kept = []
    for line in body.splitlines(keepends=True):
        match = re.match(r'^ {0,3}(`{3,}|~{3,})(.*)', line.rstrip('\n'))
        if fence:
            if match and match[1][0] == fence[0] and len(match[1]) >= len(fence) and not match[2].strip():
                fence = None
            kept.append('\n')
        elif match:
            fence = match[1]
            kept.append('\n')
        elif line.startswith('#'):
            contents = line.rstrip() == '## Contents'
            kept.append('\n')
        else:
            kept.append('\n' if contents else line)
    return list(dict.fromkeys(block.strip() for block in re.split(r'\n\s*\n', ''.join(kept)) if block.strip()))


def markers(anchor, known=None):
    result = []
    for match in MARKER.finditer(re.sub(r'`[^`\n]*`', '', anchor)):
        group = match[1]
        # Ranges are part of the legacy citation syntax.
        group = re.sub(r'([SHPOCNB])(\d+)\s*[–-]\s*(?:\1)?(\d+)',
                       lambda m: ', '.join(f'{m[1]}{n}' for n in range(int(m[2]), int(m[3]) + 1))
                       if 0 <= int(m[3]) - int(m[2]) <= 1000 else m[0], group)
        # Read the citation list, not source-looking collection/box numbers in
        # explanatory prose after it (for example "S1; file B0143").
        while match := re.match(r'(' + SOURCE_ID + r')(?:†)?(?: @\d{4}-\d{2}-\d{2})?', group):
            sid = match[1]
            # B/U are synthetic ledger IDs, also used for unrelated archive
            # reference codes. Interpret them only when declared in this sidecar.
            synthetic = sid.startswith(('B', 'U'))
            if sid not in result and (not synthetic or known is None or sid in known):
                result.append(sid)
            group = group[match.end():]
            separator = re.match(r'\s*(?:[,;/&]|and\b|or\b)\s*(?=' + SOURCE_ID + r'\b)', group)
            if not separator:
                break
            group = group[separator.end():]
    return result


def marker_contexts(anchor, sid):
    """Each source marker's sentence, so a separate hedge cannot qualify a fact."""
    visible = re.sub(r'`[^`\n]*`', lambda m: ' ' * len(m[0]), anchor)
    boundaries = [0] + [m.end() for m in re.finditer(
        r'[.!?](?:\s*\[[^\]\n]+\])*\s+(?=[A-Z])', visible)] + [len(anchor)]
    for match in MARKER.finditer(visible):
        if sid in markers(match[0]):
            start = max(n for n in boundaries if n <= match.start())
            end = min(n for n in boundaries if n >= match.end())
            yield match[0], anchor[start:end]


def candidate_blocks(text):
    return [b for b in prose_blocks(text) if markers(b) or CURRENT.search(b)]


def fingerprint(record):
    # Backlinks are checked against claims separately. Removing an unsupported
    # claim must not force an invented source read just to update a derived list.
    if 'entry_sha256' in record:
        record = {k: v for k, v in record.items() if k != 'claims'}
    return digest(json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(',', ':')))


def debt_key(slug, category, record):
    return f'{slug}#{category}/{record["id"]}'


def migrate(source_text, recipe_text):
    entries = source_entries(source_text)
    ledger = {'schema': 1, 'sources': [], 'claims': []}
    for sid, entry in entries.items():
        links = urls(entry)
        kind = 'video' if links and all('youtube.com/' in u or 'youtu.be/' in u for u in links) else 'unknown'
        ledger['sources'].append(dict(id=sid, kind=kind, urls=links, published=None,
                                      retrieved=None, access='unknown', rights=None, basis=None,
                                      entry_sha256=digest(entry), claims=[], review='pending'))
    for anchor in candidate_blocks(recipe_text):
        refs = markers(anchor, entries)
        ledger['claims'].append(dict(id='C-' + digest(anchor)[:12], kind='unclassified',
                                     anchor=anchor, sources=refs, checked=None,
                                     stated_as=None, review='pending'))
    reverse_links(ledger)
    return ledger


def reverse_links(ledger):
    for source in ledger['sources']:
        source['claims'] = [c['id'] for c in ledger['claims'] if source['id'] in c['sources']]


def iso_date(value, today, label, required=False):
    if value is None:
        require(not required, f'{label} is required')
        return None
    require(isinstance(value, str) and re.fullmatch(r'\d{4}-\d{2}-\d{2}', value), f'invalid {label}')
    parsed = dt.date.fromisoformat(value)
    require(parsed <= today, f'{label} is in the future')
    return parsed


def string_list(value):
    return (isinstance(value, list) and all(isinstance(x, str) and x for x in value)
            and len(value) == len(set(value)))


def validate(slug, source_text, recipe_text, ledger, exceptions, today):
    require(ledger is not None, f'{slug}: missing provenance ledger')
    entries = source_entries(source_text)
    body = recipe_body(recipe_text)
    sources = {}
    claims = {}
    active_debt = {}
    for category, fields in [('sources', SOURCE_FIELDS), ('claims', CLAIM_FIELDS)]:
        index = sources if category == 'sources' else claims
        for record in ledger[category]:
            require(isinstance(record, dict) and set(record) == fields, f'{slug}: invalid {category} fields')
            rid = record['id']
            require(isinstance(rid, str) and re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9-]*', rid), 'invalid record id')
            if category == 'sources':
                require(re.fullmatch(SOURCE_ID, rid), f'{slug}: source id cannot be cited: {rid}')
            require(rid not in index, f'{slug}: duplicate {category} id {rid}')
            index[rid] = record
            require(record['review'] in ('pending', 'reviewed'), f'{slug}#{rid}: invalid review state')
            if record['review'] == 'pending':
                key = debt_key(slug, category, record)
                value = fingerprint(record)
                require(exceptions.get(key) == value, f'{key}: new or changed migration debt; review the record')
                active_debt[key] = value
    require(set(entries) == set(sources), f'{slug}: bibliography/ledger IDs differ: {sorted(set(entries) ^ set(sources))}')
    for sid, source in sources.items():
        label = f'{slug}#{sid}'
        require(source['kind'] in KINDS and source['access'] in ACCESS, f'{label}: invalid type/access')
        require(string_list(source['urls']), f'{label}: invalid URL list')
        require(source['urls'] == urls(entries[sid]), f'{label}: URLs differ from bibliography (case/order matter)')
        require(source['entry_sha256'] == digest(entries[sid]), f'{label}: bibliography entry drift')
        for field in ('rights', 'basis'):
            require(source[field] is None or isinstance(source[field], str) and bool(source[field].strip()),
                    f'{label}: invalid {field}')
        iso_date(source['published'], today, 'published')
        retrieved = iso_date(source['retrieved'], today, 'retrieved')
        require(string_list(source['claims']), f'{label}: invalid reverse claims')
        require(source['claims'] == [c['id'] for c in claims.values() if sid in c['sources']],
                f'{label}: reverse claims differ')
        if source['review'] == 'reviewed':
            require(bool(source['claims']), f'{label}: reviewed source is not cited by any claim')
        if source['review'] == 'reviewed' and source['access'] != 'unknown':
            require(retrieved and source['basis'] and source['basis'] in entries[sid],
                    f'{label}: access needs a dated exact bibliography basis')
            require(source['retrieved'] in source['basis'], f'{label}: access basis needs retrieval date')
            require(len(source['urls']) == 1, f'{label}: split multi-URL entries before reviewing access')
    for cid, claim in claims.items():
        label = f'{slug}#{cid}'
        anchor = claim['anchor']
        require(isinstance(anchor, str) and bool(anchor.strip()) and anchor in body, f'{label}: anchor drift')
        require(claim['kind'] in CLAIM_KINDS and string_list(claim['sources']), f'{label}: invalid kind/sources')
        checked = iso_date(claim['checked'], today, 'checked')
        require(claim['stated_as'] in ('fact', 'observation', None), f'{label}: invalid stated_as')
        if claim['review'] == 'pending':
            continue
        require(body.count(anchor) == 1, f'{label}: reviewed anchor must be unique')
        require(claim['kind'] != 'unclassified' and claim['stated_as'] is not None, f'{label}: incomplete review')
        require(bool(claim['sources']) and set(claim['sources']) <= set(sources), f'{label}: missing source')
        require(set(markers(anchor, sources)) == set(claim['sources']), f'{label}: source markers differ from claim sources')
        for sid in claim['sources']:
            source = sources[sid]
            require(source['review'] == 'reviewed', f'{label}: source {sid} is pending')
            if source['access'] not in ('read', 'partial'):
                require(claim['stated_as'] == 'observation' and all(
                    re.search(rf'\b{re.escape(sid)}†', marker) and HEDGE.search(context)
                    for marker, context in marker_contexts(anchor, sid)),
                    f'{label}: unread source {sid} needs an attributed dagger observation')
            if source['access'] == 'partial':
                require(all(HEDGE.search(context) for _, context in marker_contexts(anchor, sid)),
                        f'{label}: partial source needs a visible qualification')
            if checked:
                require(source['retrieved'] and checked <= dt.date.fromisoformat(source['retrieved']),
                        f'{label}: claim check postdates source retrieval')
        if claim['kind'] in AGES:
            require(checked is not None, f'{label}: current-state claim needs a check date')
            require((today - checked).days <= AGES[claim['kind']], f'{label}: stale {claim["kind"]} check')
            for sid in claim['sources']:
                require(re.search(rf'\[{re.escape(sid)}†? @{claim["checked"]}\]', anchor),
                        f'{label}: missing dated marker for {sid}')
    for block in candidate_blocks(recipe_text):
        require(any(block == c['anchor'] for c in claims.values()),
                f'{slug}: unregistered factual/cited passage: {block[:100]!r}')
    return active_debt


def render_report(corpus, today):
    source_count = sum(len(l['sources']) for l in corpus.values())
    claim_count = sum(len(l['claims']) for l in corpus.values())
    lines = ['# Provenance report', '',
             'Generated by `python3 scripts/provenance.py --write`. Pending means attribution or access',
             'has not been reviewed. A migrated marker is not evidence that its source was read.', '',
             f'Coverage: {len(corpus)} sidecars, {source_count} source records, {claim_count} candidate claim anchors.',
             'Candidate detection is heuristic; uncited factual claims can still require editorial review.', '',
             '## Reviewed current-state claims', '',
             '| Claim | Kind | Last check | Due | Sources |',
             '| --- | --- | --- | --- | --- |']
    for slug, ledger in sorted(corpus.items()):
        for c in ledger['claims']:
            if c['review'] == 'reviewed' and c['kind'] in AGES:
                due = dt.date.fromisoformat(c['checked']) + dt.timedelta(days=AGES[c['kind']])
                lines.append(f'| `{slug}#{c["id"]}` | {c["kind"]} | {c["checked"]} | {due} | {", ".join(c["sources"])} |')
    lines += ['', '## Legacy migration debt', '',
              'Frozen exceptions allow existing uncertainty to remain visible; new or changed pending',
              'records fail CI. Source IDs and numbering gaps are preserved, including unresolved markers.', '',
              '| Recipe | Pending sources | Pending anchors | Unlinked anchors | Missing source IDs |',
              '| --- | ---: | ---: | ---: | --- |']
    for slug, ledger in sorted(corpus.items()):
        sources = {s['id'] for s in ledger['sources']}
        pending_s = sum(s['review'] == 'pending' for s in ledger['sources'])
        pending_c = sum(c['review'] == 'pending' for c in ledger['claims'])
        unlinked = sum(not c['sources'] for c in ledger['claims'])
        missing = sorted({s for c in ledger['claims'] for s in c['sources']} - sources)
        lines.append(f'| [{slug}]({SKILL}/sources/{slug}.md) | {pending_s} | {pending_c} | {unlinked} | {", ".join(missing) or "—"} |')
    return '\n'.join(lines) + '\n'


def run(root, mode, today):
    source_dir = root / SKILL / 'sources'
    recipe_dir = root / SKILL / 'recipes'
    paths = sorted(source_dir.glob('*.md'))
    require(paths, 'no source sidecars found')
    require({p.name for p in paths} == {p.name for p in recipe_dir.glob('*.md')}, 'recipe/source sidecars differ')
    debt_path = root / DEBT
    if mode == 'import-legacy':
        require(not debt_path.exists(), 'legacy inventory already exists; normal commands cannot add exceptions')
        exceptions = {}
    else:
        exceptions = loads(debt_path.read_text(encoding='utf-8'))
        require(isinstance(exceptions, dict), 'legacy inventory must be an object')
    corpus, outputs, active = {}, {}, {}
    for path in paths:
        slug = path.stem
        source_text = path.read_text(encoding='utf-8')
        recipe_text = (recipe_dir / path.name).read_text(encoding='utf-8')
        _, ledger = split_ledger(source_text)
        if mode == 'import-legacy':
            require(ledger is None, f'{slug}: refusing to replace an existing ledger')
            ledger = migrate(source_text, recipe_text)
            for category in ('sources', 'claims'):
                for record in ledger[category]:
                    exceptions[debt_key(slug, category, record)] = fingerprint(record)
        if mode == 'write':
            reverse_links(ledger)
        active.update(validate(slug, source_text, recipe_text, ledger, exceptions, today))
        corpus[slug] = ledger
        outputs[path] = attach_ledger(source_text, ledger)
    require(set(active) <= set(exceptions), 'new migration exceptions')
    outputs[debt_path] = json.dumps(active, indent=2, sort_keys=True) + '\n'
    outputs[root / REPORT] = render_report(corpus, today)
    stale = [str(p.relative_to(root)) for p, text in outputs.items()
             if not p.exists() or p.read_text(encoding='utf-8') != text]
    if mode == 'check':
        require(not stale, 'generated provenance differs: ' + ', '.join(stale) + '; run --write')
    else:
        for path, text in outputs.items():
            path.write_text(text, encoding='utf-8')
    return corpus


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    for mode in ('check', 'write', 'import-legacy'):
        modes.add_argument('--' + mode, action='store_const', const=mode, dest='mode')
    args = parser.parse_args(argv)
    try:
        corpus = run(ROOT, args.mode, dt.datetime.now(dt.timezone.utc).date())
        print(f'Validated {len(corpus)} provenance ledgers; unresolved legacy evidence is listed in {REPORT}.')
        return 0
    except (ProvenanceError, OSError, ValueError, TypeError, KeyError) as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
