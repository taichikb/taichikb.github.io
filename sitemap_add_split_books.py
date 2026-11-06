#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sitemap_add_split_books.py -- add the split-book TOC folder URLs to
sitemap.xml, following the house convention used by the books that were
already split (dao_duc_kinh_*, thai_cuc_quyen_* ...):

    <url>
      <loc>https://taichinow.github.io/vi/books/<slug>/</loc>
      <lastmod>YYYY-MM-DD</lastmod>
      <priority>0.7</priority>
    </url>

Chapter pages are NOT listed (same as the existing split books), and the
monolithic "read all on one page" file stays listed as before.

The entries are inserted in the sitemap's existing alphabetical order.

Usage:
    python sitemap_add_split_books.py [--repo <repo>] [--date YYYY-MM-DD]
"""
import argparse
import os
import re
import sys
from urllib.parse import quote

SLUGS = [
    'sun_style_taijiquan_sun_jianyun',
    'chen_style_taijiquan_shen_gu_1963',
    'jiujue_81_wu_mengxia',
    'wu_hao_style_taijiquan_hao_shaoru',
    'quan_shu_chen_shi_1995',
    'fu_yang_style_taijiquan_fu_zhongwen',
    'taijiquan_nine_secrets_wu_mengxia',
    'zhongjing_febrile_diseases_caused_by_cold',
    'hoang_de_noi_kinh_to_van',
    'huynh_dinh_noi_canh_kinh',
    'illustrated_canon_of_medicine',
    'basic_theory_tcm',
    'five_ganzhi_meihuazhuang_techniques',
]

BASE = 'https://taichinow.github.io'
URL_BLOCK = re.compile(r'  <url>\n    <loc>([^<]+)</loc>\n    <lastmod>([^<]*)</lastmod>\n'
                       r'    <priority>([^<]*)</priority>\n  </url>\n')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', default=os.path.dirname(os.path.abspath(__file__)))
    ap.add_argument('--date', default=None)
    a = ap.parse_args()

    path = os.path.join(a.repo, 'sitemap.xml')
    with open(path, encoding='utf-8') as f:
        text = f.read()

    date = a.date or '2026-11-05'

    # locate the vi/books/ section and its neighbours
    blocks = list(URL_BLOCK.finditer(text))
    if not blocks:
        sys.exit('ERROR: could not parse sitemap url blocks')

    existing = {b.group(1) for b in blocks}
    to_add = []
    for slug in SLUGS:
        loc = '%s/vi/books/%s/' % (BASE, slug)
        if loc in existing:
            print('  already present: %s' % loc)
            continue
        if not os.path.exists(os.path.join(a.repo, 'vi', 'books', slug, 'index.html')):
            print('  SKIP (no index.html): %s' % slug)
            continue
        to_add.append((loc, slug))
    if not to_add:
        print('nothing to add')
        return 0

    # insert each new block in alphabetical position among the vi/books/ blocks
    for loc, slug in sorted(to_add, key=lambda x: x[0]):
        new_block = ('  <url>\n    <loc>%s</loc>\n    <lastmod>%s</lastmod>\n'
                     '    <priority>0.7</priority>\n  </url>\n' % (loc, date))
        # find the first vi/books/ block that sorts after loc
        inserted = False
        for b in blocks:
            if b.group(1).startswith(BASE + '/vi/books/') and b.group(1) > loc:
                text = text[:b.start()] + new_block + text[b.start():]
                inserted = True
                break
        if not inserted:
            # append before </urlset>
            i = text.rfind('</urlset>')
            text = text[:i] + new_block + text[i:]
        blocks = list(URL_BLOCK.finditer(text))
        print('  added: %s' % loc)

    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)
    print('sitemap.xml updated (+%d entries)' % len(to_add))
    return 0


if __name__ == '__main__':
    sys.exit(main())
