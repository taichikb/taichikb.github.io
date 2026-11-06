#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
repoint_split_books.py -- repoint book cards from the monolithic single-file
reader (X_vi.html) to the split folder (X/) that now holds the TOC index +
one page per chapter.

Only EXACT href values are rewritten, so sibling pages that are NOT split
(e.g. chen_style_taijiquan_shen_gu_vi.html  -- the separate "summary
treatment" of the same book, or wu_hao_style_..._overview_vi.html) are left
untouched.

Files handled:
  * vi/books/index.html, books/index.html, library/index.html, index.html
        href="/vi/books/<slug>_vi.html"  ->  href="/vi/books/<slug>/"
  * deep-map data pages
        "viHref": "vi/books/<slug>_vi.html"  ->  "viHref": "vi/books/<slug>/"
  * books/read/<book>/index.html  (reader landing pages)

Usage:
    python repoint_split_books.py [--repo <repo root>] [--dry-run]
"""
import argparse
import json
import os
import re
import sys

# slug -> (monolithic file name inside vi/books/, split folder name)
BOOKS = {
    'sun_style_taijiquan_sun_jianyun': 'sun_style_taijiquan_sun_jianyun_vi.html',
    'chen_style_taijiquan_shen_gu_1963': 'chen_style_taijiquan_shen_gu_1963_vi.html',
    'jiujue_81_wu_mengxia': 'jiujue_81_wu_mengxia_vi.html',
    'wu_hao_style_taijiquan_hao_shaoru': 'wu_hao_style_taijiquan_hao_shaoru_vi.html',
    'quan_shu_chen_shi_1995': 'quan_shu_chen_shi_1995_vi.html',
    'fu_yang_style_taijiquan_fu_zhongwen': 'fu_yang_style_taijiquan_fu_zhongwen_vi.html',
    'taijiquan_nine_secrets_wu_mengxia': 'taijiquan_nine_secrets_wu_mengxia_vi.html',
    'zhongjing_febrile_diseases_caused_by_cold': 'zhongjing_febrile_diseases_caused_by_cold_vi.html',
    'hoang_de_noi_kinh_to_van': 'hoang_de_noi_kinh_to_van_vi.html',
    'huynh_dinh_noi_canh_kinh': 'huynh_dinh_noi_canh_kinh_vi.html',
    'illustrated_canon_of_medicine': 'illustrated_canon_of_medicine_vi.html',
    'basic_theory_tcm': 'basic_theory_tcm_vi.html',
    'five_ganzhi_meihuazhuang_techniques': 'five_ganzhi_meihuazhuang_techniques.html',
}

# HTML index / landing pages that carry book cards
HTML_PAGES = [
    'vi/books/index.html',
    'books/index.html',
    'library/index.html',
    'index.html',
]

# pages whose book links live inside a JSON blob ("viHref": "...")
DATA_PAGES = [
    'books/thu-vien-taichinow-deep-map/index.html',
    'deep-dives/thu-vien-taichinow-deep-map/index.html',
]

# pages whose book links live inside a JSON blob ("href":"...")
DATA_PAGES_HREF = [
    'books/khi-cong-y-hoc-tap1-deep-map/index.html',
    'deep-dives/khi-cong-y-hoc-tap1-deep-map/index.html',
]

# reader landing pages under books/read/
READ_PAGES = [
    'books/read/hoang-de-noi-kinh-to-van/index.html',
]


def read(p):
    with open(p, encoding='utf-8') as f:
        return f.read()


def write(p, t):
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write(t)


def repoint_html(text):
    """Rewrite absolute /vi/books/<mono>.html hrefs to /vi/books/<slug>/."""
    n = 0
    for slug, mono in BOOKS.items():
        pat = 'href="/vi/books/%s"' % mono
        if pat in text:
            c = text.count(pat)
            text = text.replace(pat, 'href="/vi/books/%s/"' % slug)
            n += c
    return text, n


def repoint_data(text):
    """Rewrite "viHref": "vi/books/<mono>.html" to "vi/books/<slug>/"."""
    n = 0
    for slug, mono in BOOKS.items():
        pat = '"viHref": "vi/books/%s"' % mono
        if pat in text:
            c = text.count(pat)
            text = text.replace(pat, '"viHref": "vi/books/%s/"' % slug)
            n += c
    return text, n


def repoint_data_href(text):
    """Rewrite "href":"vi/books/<mono>.html" to "vi/books/<slug>/"."""
    n = 0
    for slug, mono in BOOKS.items():
        pat = '"href":"vi/books/%s"' % mono
        if pat in text:
            c = text.count(pat)
            text = text.replace(pat, '"href":"vi/books/%s/"' % slug)
            n += c
    return text, n


def repoint_read(text):
    """Rewrite reader landing links to the split folder."""
    n = 0
    for slug, mono in BOOKS.items():
        pat = 'href="/vi/books/%s"' % mono
        if pat in text:
            c = text.count(pat)
            text = text.replace(pat, 'href="/vi/books/%s/"' % slug)
            n += c
    return text, n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', default=os.path.dirname(os.path.abspath(__file__)))
    ap.add_argument('--dry-run', action='store_true')
    a = ap.parse_args()

    total = 0
    jobs = ([(p, repoint_html) for p in HTML_PAGES]
            + [(p, repoint_data) for p in DATA_PAGES]
            + [(p, repoint_data_href) for p in DATA_PAGES_HREF]
            + [(p, repoint_read) for p in READ_PAGES])

    for rel, fn in jobs:
        path = os.path.join(a.repo, rel)
        if not os.path.exists(path):
            print('  SKIP (missing)  %s' % rel)
            continue
        before = read(path)
        after, n = fn(before)
        if n == 0:
            print('  no change       %s' % rel)
            continue
        total += n
        print('  %-52s %d link(s)' % (rel, n))
        if not a.dry_run:
            write(path, after)

    print('TOTAL repointed links: %d%s' % (total, '  (dry run)' if a.dry_run else ''))
    return 0


if __name__ == '__main__':
    sys.exit(main())
