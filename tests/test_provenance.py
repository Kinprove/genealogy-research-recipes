"""Observable provenance failures, conservative migration and real corpus coverage."""

import copy
import datetime as dt
import importlib.util
import io
import json
import shutil
import subprocess
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PARSER_AVAILABLE = bool(shutil.which('node')) and all(
    (ROOT / 'tests/markdown-links/node_modules' / name / 'package.json').is_file()
    for name in ('markdown-it', 'parse5'))
SPEC = importlib.util.spec_from_file_location('provenance', ROOT / 'scripts/provenance.py')
p = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(p)
TODAY = dt.date(2026, 11, 7)
SOURCE = ('## Sources\n\n- **S1:** Example Archive, '
          '[Help](https://example.org/Help?ID=AbC_12#View), '
          'opened 2026-11-07. Search is by parish.\n\n'
          '## Credits\n\n- Kinprove — original synthesis (kinprove-original)\n')
ANCHOR = 'The archive currently offers parish search. [S1 @2026-11-07]'
RECIPE = '# Parish search\n\n' + ANCHOR + '\n'


def reviewed():
    ledger = p.migrate(SOURCE, RECIPE)
    source = ledger['sources'][0]
    source.update(kind='help-page', review='reviewed', access='read', retrieved='2026-11-07',
                  basis='opened 2026-11-07')
    claim = ledger['claims'][0]
    claim.update(kind='platform-ui', review='reviewed', checked='2026-11-07', stated_as='fact')
    return ledger


class ParserSetupTests(unittest.TestCase):
    def test_missing_node_is_an_explicit_validation_error(self):
        text = 'unique setup probe without a Node runtime'
        p.VISIBLE_CACHE.pop(text, None)
        with patch.object(p.shutil, 'which', return_value=None):
            with self.assertRaisesRegex(p.ProvenanceError, 'Node.js is required'):
                p.prepare_visibility([text])


@unittest.skipUnless(PARSER_AVAILABLE, 'install the pinned Markdown parser before full provenance tests')
class ProvenanceTests(unittest.TestCase):
    def check(self, ledger=None, source=SOURCE, recipe=RECIPE, debt=None, today=TODAY):
        ledger = ledger if ledger is not None else reviewed()
        return p.validate('example', source, recipe, ledger, debt or {}, today)

    def rejects(self, ledger, message, **kwargs):
        with self.assertRaisesRegex(p.ProvenanceError, message):
            self.check(ledger, **kwargs)

    def test_reviewed_current_claim_passes_and_round_trips(self):
        ledger = reviewed()
        self.assertEqual(self.check(ledger), {})
        self.assertEqual(p.parse_ledger(p.render_ledger(ledger)), ledger)

    def test_a_ledger_block_inside_the_shipped_sidecar_is_refused(self):
        # A branch cut before #205 could merge a ledger block back into its sidecar.
        source = SOURCE.replace('## Credits', p.OLD_LEDGER_START + '\n\n## Credits')
        self.rejects(reviewed(), r'keep its ledger in provenance/example\.yml', source=source)

    def test_import_never_converts_publication_or_opened_prose_into_read_status(self):
        ledger = p.migrate(SOURCE, RECIPE)
        self.assertEqual(ledger['sources'][0]['access'], 'unknown')
        self.assertIsNone(ledger['sources'][0]['retrieved'])
        self.assertIsNone(ledger['claims'][0]['checked'])
        self.assertEqual(ledger['claims'][0]['review'], 'pending')

    def test_pending_records_need_exact_frozen_fingerprints(self):
        ledger = p.migrate(SOURCE, RECIPE)
        debt = {p.debt_key('example', k, r): p.fingerprint(r)
                for k in ('sources', 'claims') for r in ledger[k]}
        self.assertEqual(self.check(ledger, debt=debt), debt)
        ledger['sources'][0]['access'] = 'read'
        self.rejects(ledger, 'changed migration debt', debt=debt)

    def test_unknown_new_records_cannot_get_an_implicit_legacy_exception(self):
        self.rejects(p.migrate(SOURCE, RECIPE), 'new or changed migration debt')

    def test_removing_an_unsupported_pending_claim_can_prune_its_backlink(self):
        ledger = p.migrate(SOURCE, RECIPE)
        debt = {p.debt_key('example', k, r): p.fingerprint(r)
                for k in ('sources', 'claims') for r in ledger[k]}
        ledger['claims'] = []
        ledger['sources'][0]['claims'] = []
        active = self.check(ledger, recipe='# Example\n', debt=debt)
        self.assertEqual(len(active), 1)
        self.assertEqual(ledger['sources'][0]['access'], 'unknown')

    def test_bibliography_drift_is_not_repaired_by_normal_regeneration(self):
        self.rejects(reviewed(), 'entry drift', source=SOURCE.replace('Search is', 'Searching is'))

    def test_url_case_query_and_fragment_are_preserved_and_checked(self):
        value = 'https://example.org/Help?ID=AbC_12#View'
        self.assertEqual(p.urls('[A](' + value + ').'), [value])
        ledger = reviewed()
        ledger['sources'][0]['urls'][0] = value.lower()
        self.rejects(ledger, 'URLs differ')

    def test_parentheses_inside_urls_survive(self):
        self.assertEqual(p.urls('[A](https://example.org/A_(B)).'), ['https://example.org/A_(B)'])

    def test_duplicate_json_keys_lists_and_a_missing_schema_are_refused(self):
        with self.assertRaisesRegex(p.ProvenanceError, 'duplicate JSON key'):
            p.loads('{"access":"read","access":"unknown"}')
        text = p.render_ledger(reviewed())
        lists = text.removeprefix('schema: 1\n')
        with self.assertRaisesRegex(p.ProvenanceError, 'duplicate ledger list'):
            p.parse_ledger(text + lists)
        with self.assertRaisesRegex(p.ProvenanceError, 'schema: 1'):
            p.parse_ledger(lists)

    def test_duplicate_ids_and_missing_bibliography_entries_are_refused(self):
        ledger = reviewed()
        ledger['sources'].append(copy.deepcopy(ledger['sources'][0]))
        self.rejects(ledger, 'duplicate sources id')
        ledger = reviewed()
        ledger['sources'][0]['id'] = 'S2'
        self.rejects(ledger, 'IDs differ')

    def test_missing_source_and_changed_reverse_link_fail(self):
        ledger = reviewed()
        ledger['claims'][0]['sources'] = ['S1', 'S9']
        self.rejects(ledger, 'missing source')
        ledger = reviewed()
        ledger['sources'][0]['claims'] = []
        self.rejects(ledger, 'reverse claims differ')

    def test_new_reviewed_bibliography_entry_must_support_a_claim(self):
        ledger = reviewed()
        ledger['claims'] = []
        ledger['sources'][0]['claims'] = []
        self.rejects(ledger, 'not cited by any claim', recipe='# Example\n')

    def test_anchor_drift_and_ambiguous_anchor_fail(self):
        self.rejects(reviewed(), 'anchor drift', recipe=RECIPE.replace('offers', 'provides'))
        self.rejects(reviewed(), 'anchor must be unique', recipe=RECIPE + '\n' + ANCHOR)

    def test_bare_source_marker_cannot_cover_an_unregistered_new_paragraph(self):
        new = 'Currently a fee of €50 applies. [S1 @2026-11-07]'
        self.rejects(reviewed(), 'unregistered factual', recipe=RECIPE + '\n' + new)

    def test_new_uncited_factual_candidate_is_not_silently_ignored(self):
        self.rejects(reviewed(), 'unregistered factual', recipe=RECIPE + '\nA fee of £10 applies.\n')

    def test_unread_source_cannot_support_fact_even_with_dagger(self):
        for access in ('snippet-only', 'refused', 'private', 'unknown'):
            ledger = reviewed()
            ledger['sources'][0]['access'] = access
            self.rejects(ledger, 'unread source', recipe=RECIPE)

    def test_hedge_dagger_and_observation_are_all_needed(self):
        for wording, status, valid in [
            ('According to a search-result snippet, parish search is offered. [S1† @2026-11-07]', 'observation', True),
            ('According to a snippet, parish search is offered. [S1 @2026-11-07]', 'observation', False),
            ('Parish search is offered. [S1† @2026-11-07]', 'observation', False),
            ('According to a snippet, parish search is offered. [S1† @2026-11-07]', 'fact', False),
        ]:
            ledger = reviewed()
            ledger['sources'][0]['access'] = 'snippet-only'
            ledger['claims'][0].update(anchor=wording, stated_as=status)
            recipe = '# Example\n\n' + wording
            with self.subTest(wording=wording, status=status):
                if valid:
                    self.check(ledger, recipe=recipe)
                else:
                    self.rejects(ledger, 'unread source', recipe=recipe)

    def test_partial_source_needs_a_visible_qualification(self):
        ledger = reviewed()
        ledger['sources'][0]['access'] = 'partial'
        self.rejects(ledger, 'partial source', recipe=RECIPE)

    def test_report_nouns_and_generic_attribution_do_not_disclose_partial_access(self):
        for text, valid in [
            ('The archive currently provides parish reports.', False),
            ('According to the archive, it currently provides parish reports.', False),
            ('The archive currently provides partial parish reports.', False),
            ('The partially restored archive currently provides parish reports.', False),
            ('From the inspected excerpt, the archive appears to provide parish reports.', True),
            ('Only the first page was inspected; it describes parish reports.', True),
        ]:
            with self.subTest(text=text):
                ledger = reviewed()
                ledger['sources'][0]['access'] = 'partial'
                anchor = text + ' [S1 @2026-11-07]'
                ledger['claims'][0]['anchor'] = anchor
                if valid:
                    self.check(ledger, recipe='# Example\n\n' + anchor)
                else:
                    self.rejects(ledger, 'partial source', recipe='# Example\n\n' + anchor)

    def test_report_noun_does_not_turn_an_unread_claim_into_attribution(self):
        ledger = reviewed()
        ledger['sources'][0]['access'] = 'snippet-only'
        anchor = 'The archive currently provides parish reports. [S1† @2026-11-07]'
        ledger['claims'][0].update(anchor=anchor, stated_as='observation')
        self.rejects(ledger, 'unread source', recipe='# Example\n\n' + anchor)

    def test_one_hedged_sentence_does_not_qualify_another_sentence(self):
        ledger = reviewed()
        ledger['sources'][0]['access'] = 'snippet-only'
        anchor = ('According to a snippet, search exists. [S1† @2026-11-07] '
                  'The archive also offers free copies. [S1† @2026-11-07]')
        ledger['claims'][0].update(anchor=anchor, stated_as='observation')
        self.rejects(ledger, 'unread source', recipe='# Example\n\n' + anchor)

    def test_sentence_scope_follows_capitals_in_any_script_numbers_and_paragraphs(self):
        for anchor, valid in [
            # The hedge belongs to the first sentence only.
            ('According to a snippet, search exists. Österreichische Archive offer free copies. '
             '[S1† @2026-11-07]', False),
            ('According to a snippet, search exists. Архив offers free copies. [S1† @2026-11-07]', False),
            ('According to a snippet, the archive opens every day. 42 collections are online. '
             '[S1† @2026-11-07]', False),
            ('According to a snippet, search exists.\n- copies are free. [S1† @2026-11-07]', False),
            # Abbreviations do not end the hedged sentence.
            ('According to the U.S. Army page, search exists. [S1† @2026-11-07]', True),
            ('According to a snippet, f. 224 holds the lists. [S1† @2026-11-07]', True),
            ('According to a snippet, No. 301 holds the lists. [S1† @2026-11-07]', True),
        ]:
            with self.subTest(anchor=anchor):
                ledger = reviewed()
                ledger['sources'][0]['access'] = 'snippet-only'
                ledger['claims'][0].update(anchor=anchor, stated_as='observation')
                if valid:
                    self.check(ledger, recipe='# Example\n\n' + anchor)
                else:
                    self.rejects(ledger, 'unread source', recipe='# Example\n\n' + anchor)

    def test_an_inline_code_example_is_not_an_unqualified_source_citation(self):
        ledger = reviewed()
        ledger['sources'][0]['access'] = 'snippet-only'
        anchor = ('According to a snippet, search exists. [S1† @2026-11-07] '
                  'Do not treat the example marker `[S1]` as evidence of a read.')
        ledger['claims'][0].update(anchor=anchor, stated_as='observation')
        self.check(ledger, recipe='# Example\n\n' + anchor)

    def test_markdown_formatting_cannot_carry_a_qualification_into_a_new_sentence(self):
        for access, prefix, marker, status in [
            ('snippet-only', 'According to a search-result snippet, search is offered.',
             '[S1† @2026-11-07]', 'observation'),
            ('partial', 'From the inspected excerpt, search appears to be offered.',
             '[S1 @2026-11-07]', 'fact'),
        ]:
            for next_sentence in ('**Copies are free.**', '*Copies are free.*',
                                  '_Copies are free._', '~~Copies are free.~~',
                                  '<strong>Copies are free.</strong>', '“Copies are free.”',
                                  '**copies are free.**'):
                with self.subTest(access=access, next_sentence=next_sentence):
                    ledger = reviewed()
                    ledger['sources'][0]['access'] = access
                    anchor = prefix + ' ' + marker + ' ' + next_sentence + ' ' + marker
                    ledger['claims'][0].update(anchor=anchor, stated_as=status)
                    self.rejects(ledger, 'unread source|partial source', recipe='# Example\n\n' + anchor)

    def test_each_formatted_sentence_can_supply_its_own_scope_qualification(self):
        ledger = reviewed()
        ledger['sources'][0]['access'] = 'partial'
        anchor = ('From the inspected excerpt, search appears available. [S1 @2026-11-07] '
                  '**Within the inspected section, copies appear to be free.** [S1 @2026-11-07]')
        ledger['claims'][0]['anchor'] = anchor
        self.check(ledger, recipe='# Example\n\n' + anchor)

    def test_qualifier_words_inside_code_or_html_attributes_do_not_count(self):
        for prefix in ('`According to a snippet`', '``According to a snippet``',
                       '<span title="According to a snippet"></span>'):
            ledger = reviewed()
            ledger['sources'][0]['access'] = 'snippet-only'
            anchor = prefix + ' Parish search is offered. [S1† @2026-11-07]'
            ledger['claims'][0].update(anchor=anchor, stated_as='observation')
            self.rejects(ledger, 'unread source', recipe='# Example\n\n' + anchor)

    def test_a_hidden_only_citation_cannot_satisfy_any_access_state(self):
        for access, status, marker in [
            ('read', 'fact', '[S1 @2026-11-07]'),
            ('partial', 'fact', '[S1 @2026-11-07]'),
            ('snippet-only', 'observation', '[S1† @2026-11-07]'),
        ]:
            for hidden in (f'<span title="{marker}"></span>',
                           f'<span title=" > From the inspected excerpt {marker}"></span>',
                           f'<!-- According to a snippet {marker} -->',
                           f'`{marker}`'):
                with self.subTest(access=access, hidden=hidden):
                    ledger = reviewed()
                    ledger['sources'][0]['access'] = access
                    anchor = 'The archive currently offers free copies. ' + hidden
                    ledger['claims'][0].update(anchor=anchor, kind='fee', stated_as=status)
                    self.rejects(ledger, 'source markers differ|no visible citation', recipe='# Example\n\n' + anchor)

    def test_a_hidden_dated_marker_cannot_supply_a_visible_citations_check_date(self):
        ledger = reviewed()
        anchor = ('The archive currently offers parish search. [S1] '
                  '<span title="[S1 @2026-11-07]"></span>')
        ledger['claims'][0]['anchor'] = anchor
        self.rejects(ledger, 'missing dated marker', recipe='# Example\n\n' + anchor)

    def test_hidden_comments_cannot_qualify_a_visible_citation(self):
        for access, prefix, status, marker in [
            ('snippet-only', '<!-- According to a snippet -->', 'observation', '[S1† @2026-11-07]'),
            ('partial', '<!-- From the inspected excerpt -->', 'fact', '[S1 @2026-11-07]'),
        ]:
            ledger = reviewed()
            ledger['sources'][0]['access'] = access
            anchor = prefix + ' The archive currently offers free copies. ' + marker
            ledger['claims'][0].update(anchor=anchor, stated_as=status)
            self.rejects(ledger, 'unread source|partial source', recipe='# Example\n\n' + anchor)

    def test_link_titles_cannot_supply_source_ids_dates_or_scope_qualifiers(self):
        for access, status, marker in [
            ('read', 'fact', '[S1 @2026-11-07]'),
            ('partial', 'fact', '[S1 @2026-11-07]'),
            ('snippet-only', 'observation', '[S1† @2026-11-07]'),
        ]:
            for title in (f'"From the inspected excerpt {marker}"',
                          f"'From the inspected excerpt {marker}'",
                          f'(From the inspected excerpt {marker})'):
                ledger = reviewed()
                ledger['sources'][0]['access'] = access
                anchor = 'The archive currently offers free copies. [Help](https://example.org/ ' + title + ')'
                ledger['claims'][0].update(anchor=anchor, kind='fee', stated_as=status)
                self.rejects(ledger, 'source markers differ|no visible citation', recipe='# Example\n\n' + anchor)

    def test_reference_link_metadata_is_not_visible_evidence(self):
        text = ('The archive offers free copies. [Help][r]\n\n'
                '[r]: https://example.org/ "From the inspected excerpt [S1 @2026-11-07]"')
        self.assertEqual(p.markers(text), [])
        self.assertNotIn('inspected', p.visible_text(text))

    def test_a_visible_link_label_can_supply_its_own_qualified_source_marker(self):
        ledger = reviewed()
        ledger['sources'][0]['access'] = 'partial'
        anchor = '[From the inspected excerpt, search appears available. [S1 @2026-11-07]](https://example.org/)'
        ledger['claims'][0]['anchor'] = anchor
        self.check(ledger, recipe='# Example\n\n' + anchor)

    def test_access_basis_must_be_exact_dated_and_single_url(self):
        ledger = reviewed()
        ledger['sources'][0]['basis'] = 'opened 2026-11-06'
        self.rejects(ledger, 'exact bibliography basis')
        ledger = reviewed()
        ledger['sources'][0]['basis'] = 'Search is by parish.'
        self.rejects(ledger, 'basis needs retrieval date')
        source = SOURCE.replace('Search is by parish.', 'Search is by parish. <https://example.org/Other>')
        ledger = reviewed()
        ledger['sources'][0]['urls'] = p.urls(source)
        ledger['sources'][0]['entry_sha256'] = p.digest(p.source_entries(source)['S1'])
        self.rejects(ledger, 'split multi-URL', source=source)

    def test_future_dates_and_check_after_retrieval_fail(self):
        ledger = reviewed()
        ledger['claims'][0]['checked'] = '2026-11-08'
        self.rejects(ledger, 'future')
        ledger['sources'][0]['retrieved'] = '2026-11-06'
        ledger['sources'][0]['basis'] = 'opened 2026-11-06'
        ledger['claims'][0]['checked'] = '2026-11-07'
        source = SOURCE.replace('2026-11-07', '2026-11-06')
        ledger['sources'][0]['entry_sha256'] = p.digest(p.source_entries(source)['S1'])
        self.rejects(ledger, 'postdates', source=source)

    def test_current_claim_freshness_and_matching_dated_marker(self):
        self.check(today=TODAY + dt.timedelta(days=180))
        self.rejects(reviewed(), 'stale platform-ui', today=TODAY + dt.timedelta(days=181))
        ledger = reviewed()
        ledger['claims'][0]['kind'] = 'fee'
        self.rejects(ledger, 'stale fee', today=TODAY + dt.timedelta(days=91))
        ledger = reviewed()
        anchor = ANCHOR.replace(' @2026-11-07', '')
        ledger['claims'][0]['anchor'] = anchor
        self.rejects(ledger, 'missing dated marker', recipe=RECIPE.replace(ANCHOR, anchor))

    def test_durable_method_does_not_expire(self):
        ledger = reviewed()
        ledger['claims'][0]['kind'] = 'method'
        self.check(ledger, today=TODAY + dt.timedelta(days=1000))

    def test_formats_ranges_additions_and_unlabelled_urls_are_not_lost(self):
        source = ('## Sources\n\n- **H3:** First <https://example.org/One>.\n'
                  '- **H3 (addition):** Second <https://example.org/Two>.\n'
                  '## More\n\n1. Third <https://example.org/Three>.\n'
                  '| S9 | Fourth <https://example.org/Four>. |\n'
                  '## Other\n\n- An unlabelled entry\n  <https://example.org/Five>.\n'
                  '\nA context link <https://example.org/Six>.\n\n## Credits\n')
        entries = p.source_entries(source)
        self.assertTrue({'H3', 'H3-addition-1', 'N1', 'S9', 'B1'} <= set(entries))
        self.assertEqual({u for e in entries.values() for u in p.urls(e)}, set(p.urls(source)))
        self.assertEqual(p.markers('Example [S1–S3, O2; note] and (H3).'), ['S1', 'S2', 'S3', 'O2', 'H3'])
        self.assertEqual(p.markers('Example [H3-addition-1, B1, U0123456789ab].'),
                         ['H3-addition-1', 'B1', 'U0123456789ab'])
        self.assertEqual(p.markers('Series (M158, M845) and [S1; file B0143].'), ['S1'])
        self.assertEqual(p.markers('Collection [B0143]; source [B1].', {'B1'}), ['B1'])

    def test_fences_and_contents_do_not_generate_claims(self):
        text = '# Example\n\n## Contents\n\n- Current fee\n\n## Body\n\n```\n€10 [S1]\n```\n\nMethod.\n'
        self.assertEqual(p.candidate_blocks(text), [])
        self.assertEqual(p.markers('An example ``[S1]`` and a real marker [S2].'), ['S2'])


class LegacyBaseAndExpiryTests(unittest.TestCase):
    def test_legacy_inventory_may_shrink_but_not_grow_or_change(self):
        base = {'a': '1', 'b': '2'}
        self.assertEqual(p.legacy_growth(base, {'a': '1'}), [])
        self.assertEqual(p.legacy_growth(base, {'a': '1', 'c': '3'}), ['c'])
        self.assertEqual(p.legacy_growth(base, {'a': '9', 'b': '2'}), ['a'])

    @unittest.skipUnless(shutil.which('git'), 'git is required')
    def test_legacy_base_reads_the_inventory_at_the_given_commit(self):
        with tempfile.TemporaryDirectory(prefix='grr-legacy-') as tmp:
            root = Path(tmp)
            (root / 'tests').mkdir()
            debt = root / p.DEBT

            def git(*args):
                subprocess.run(['git', '-C', tmp, '-c', 'core.hooksPath=/dev/null', '-c', 'commit.gpgsign=false',
                                '-c', 'user.name=test', '-c', 'user.email=test@example.invalid', *args],
                               check=True, capture_output=True)

            git('init', '-q')
            debt.write_text(json.dumps({'a': '1', 'b': '2'}), encoding='utf-8')
            git('add', p.DEBT.as_posix())
            git('commit', '-q', '-m', 'base')
            debt.write_text(json.dumps({'a': '1'}), encoding='utf-8')
            p.check_legacy_base(root, 'HEAD')
            for grown in ({'a': '1', 'c': '3'}, {'a': '9'}):
                debt.write_text(json.dumps(grown), encoding='utf-8')
                with self.subTest(grown=grown), self.assertRaisesRegex(p.ProvenanceError, 'relative to HEAD'):
                    p.check_legacy_base(root, 'HEAD')
            with self.assertRaisesRegex(p.ProvenanceError, 'cannot read'):
                p.check_legacy_base(root, 'no-such-ref')

    def test_legacy_base_needs_check_mode(self):
        with self.assertRaises(SystemExit), redirect_stderr(io.StringIO()):
            p.main(['--write', '--legacy-base', 'HEAD'])

    def test_main_announces_expiring_claims_once_and_runs_the_base_check(self):
        today = dt.date(2027, 3, 1)

        def claim(cid, days_left, review='reviewed'):
            checked = today + dt.timedelta(days=days_left - p.AGES['fee'])
            return dict(id=cid, kind='fee', review=review, checked=checked.isoformat())

        claims = [claim(f'C-due{n}', p.WARN_DAYS - n) for n in range(12)]  # more than ten annotations
        claims += [claim('C-later', p.WARN_DAYS + 1), claim('C-pending', 0, review='pending'),
                   dict(id='C-method', kind='method', review='reviewed', checked='2000-01-01')]
        corpus = {'example': {'claims': claims}}
        due = dict(p.expiring_claims(corpus, today))
        self.assertEqual(sorted(due), sorted(f'example#C-due{n}' for n in range(12)))
        self.assertEqual(due['example#C-due0'], today + dt.timedelta(days=p.WARN_DAYS))
        out = io.StringIO()
        with patch.object(p, 'run', return_value=corpus), patch.object(p, 'utc_today', return_value=today), \
                patch.object(p, 'check_legacy_base') as base_check, redirect_stdout(out):
            self.assertEqual(p.main(['--check', '--legacy-base', 'base-ref']), 0)
        base_check.assert_called_once_with(p.ROOT, 'base-ref')
        warnings = [line for line in out.getvalue().splitlines() if line.startswith('::warning ')]
        self.assertEqual(len(warnings), 1)
        for n in range(12):
            self.assertIn(f'example#C-due{n} valid until {due[f"example#C-due{n}"]}', warnings[0])
        for absent in ('C-later', 'C-pending', 'C-method'):
            self.assertNotIn(absent, warnings[0])


@unittest.skipUnless(PARSER_AVAILABLE, 'install the pinned Markdown parser before full provenance tests')
class CorpusProvenanceTests(unittest.TestCase):
    def test_entire_corpus_and_generated_report_match(self):
        corpus = p.run(ROOT, 'check', dt.datetime.now(dt.timezone.utc).date())
        self.assertGreater(len(corpus), 100)

    def test_regeneration_cannot_enroll_new_debt_and_is_transactional(self):
        with tempfile.TemporaryDirectory(prefix='grr-provenance-') as tmp:
            root = Path(tmp)
            (root / p.SKILL / 'sources').mkdir(parents=True)
            (root / p.SKILL / 'recipes').mkdir()
            (root / 'tests').mkdir()
            src = root / p.SKILL / 'sources/example.md'
            recipe = root / p.SKILL / 'recipes/example.md'
            ledger_file = root / p.LEDGERS / 'example.yml'
            src.write_text(SOURCE, encoding='utf-8')
            recipe.write_text(RECIPE, encoding='utf-8')
            p.run(root, 'import-legacy', TODAY)
            # The ledger goes outside the shipped skill; the sidecar stays prose.
            self.assertTrue(ledger_file.is_file())
            self.assertEqual(src.read_text(encoding='utf-8'), SOURCE)
            initial = {f: f.read_bytes() for f in root.rglob('*') if f.is_file()}
            p.run(root, 'write', TODAY)
            self.assertTrue(all(f.read_bytes() == contents for f, contents in initial.items()))
            with self.assertRaisesRegex(p.ProvenanceError, 'already exists'):
                p.run(root, 'import-legacy', TODAY)
            recipe.write_text(RECIPE + '\nNow available at https://example.org/New.\n', encoding='utf-8')
            with self.assertRaisesRegex(p.ProvenanceError, 'unregistered factual'):
                p.run(root, 'write', TODAY)
            self.assertEqual(ledger_file.read_bytes(), initial[ledger_file])
            self.assertEqual((root / p.DEBT).read_bytes(), initial[root / p.DEBT])
            # Deleting an unsupported legacy claim should regenerate backlinks
            # and prune debt, without claiming that its source was read.
            ledger = p.parse_ledger(ledger_file.read_text(encoding='utf-8'))
            ledger['claims'] = []
            ledger_file.write_text(p.render_ledger(ledger), encoding='utf-8')
            recipe.write_text('# Example\n', encoding='utf-8')
            p.run(root, 'write', TODAY)
            updated = p.parse_ledger(ledger_file.read_text(encoding='utf-8'))
            self.assertEqual(updated['sources'][0]['claims'], [])
            self.assertEqual(updated['sources'][0]['access'], 'unknown')
            self.assertEqual(len(p.loads((root / p.DEBT).read_text(encoding='utf-8'))), 1)
            self.assertEqual(src.read_text(encoding='utf-8'), SOURCE)
            # A ledger left behind by a renamed or removed recipe is refused.
            (root / p.LEDGERS / 'renamed.yml').write_bytes(ledger_file.read_bytes())
            with self.assertRaisesRegex(p.ProvenanceError, r"ledgers without a recipe: \['renamed'\]"):
                p.run(root, 'check', TODAY)
            # A recipe without a ledger file names the file it needs, in every mode.
            (root / p.LEDGERS / 'renamed.yml').unlink()
            ledger_file.unlink()
            for mode in ('check', 'write'):
                with self.assertRaisesRegex(p.ProvenanceError, r'missing provenance ledger provenance/example\.yml'):
                    p.run(root, mode, TODAY)


if __name__ == '__main__':
    unittest.main()
