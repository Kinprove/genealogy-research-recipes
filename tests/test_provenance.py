"""Observable provenance failures, conservative migration and real corpus coverage."""

import copy
import datetime as dt
import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
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


class ProvenanceTests(unittest.TestCase):
    def check(self, ledger=None, source=SOURCE, recipe=RECIPE, debt=None, today=TODAY):
        ledger = ledger if ledger is not None else reviewed()
        return p.validate('example', source, recipe, ledger, debt or {}, today)

    def rejects(self, ledger, message, **kwargs):
        with self.assertRaisesRegex(p.ProvenanceError, message):
            self.check(ledger, **kwargs)

    def test_reviewed_current_claim_passes_and_round_trips_before_credits(self):
        ledger = reviewed()
        self.assertEqual(self.check(ledger), {})
        emitted = p.attach_ledger(SOURCE, ledger)
        plain, parsed = p.split_ledger(emitted)
        self.assertEqual(plain, SOURCE)
        self.assertEqual(parsed, ledger)
        self.assertLess(emitted.index(p.END), emitted.index('## Credits'))

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

    def test_duplicate_json_keys_and_multiple_blocks_are_refused(self):
        with self.assertRaisesRegex(p.ProvenanceError, 'duplicate JSON key'):
            p.loads('{"access":"read","access":"unknown"}')
        text = p.attach_ledger(SOURCE, reviewed())
        with self.assertRaisesRegex(p.ProvenanceError, 'duplicate ledger'):
            p.split_ledger(text + '\n' + text)

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

    def test_an_inline_code_example_is_not_an_unqualified_source_citation(self):
        ledger = reviewed()
        ledger['sources'][0]['access'] = 'snippet-only'
        anchor = ('According to a snippet, search exists. [S1† @2026-11-07] '
                  'Do not treat the example marker `[S1]` as evidence of a read.')
        ledger['claims'][0].update(anchor=anchor, stated_as='observation')
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
            src.write_text(SOURCE, encoding='utf-8')
            recipe.write_text(RECIPE, encoding='utf-8')
            p.run(root, 'import-legacy', TODAY)
            initial = {f: f.read_bytes() for f in root.rglob('*') if f.is_file()}
            p.run(root, 'write', TODAY)
            self.assertTrue(all(f.read_bytes() == contents for f, contents in initial.items()))
            with self.assertRaisesRegex(p.ProvenanceError, 'already exists'):
                p.run(root, 'import-legacy', TODAY)
            recipe.write_text(RECIPE + '\nNow available at https://example.org/New.\n', encoding='utf-8')
            with self.assertRaisesRegex(p.ProvenanceError, 'unregistered factual'):
                p.run(root, 'write', TODAY)
            self.assertEqual(src.read_bytes(), initial[src])
            self.assertEqual((root / p.DEBT).read_bytes(), initial[root / p.DEBT])
            # Deleting an unsupported legacy claim should regenerate backlinks
            # and prune debt, without claiming that its source was read.
            plain, ledger = p.split_ledger(src.read_text(encoding='utf-8'))
            ledger['claims'] = []
            src.write_text(p.attach_ledger(plain, ledger), encoding='utf-8')
            recipe.write_text('# Example\n', encoding='utf-8')
            p.run(root, 'write', TODAY)
            _, updated = p.split_ledger(src.read_text(encoding='utf-8'))
            self.assertEqual(updated['sources'][0]['claims'], [])
            self.assertEqual(updated['sources'][0]['access'], 'unknown')
            self.assertEqual(len(p.loads((root / p.DEBT).read_text(encoding='utf-8'))), 1)


if __name__ == '__main__':
    unittest.main()
