#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
split_qa.py -- QA for books produced by split_book.py.

Checks, per split folder:
  1. every visible word of the SOURCE page's book-content appears in the
     generated chapter pages (no content loss)
  2. the generated pages do not duplicate source content (no repeated blocks)
  3. every relative link/asset resolves to a real file
  4. the TOC page links exactly the chapter files that exist
  5. every chapter page carries the bottom nav with correct prev/next
  6. chapter pages carry a heading and a link back to the TOC

Duplication detection (2) is BLOCK-level, not word-level: the splitter
injects a navigation chrome (tocbar / chead / chsecnav / partnav / tnote /
toclist) on every page, so a naive word-multiset diff reports thousands of
"extra" words that are pure navigation overhead.  Instead we compare
paragraph-sized blocks:

    * blocks are extracted from the source <main> and from every generated
      page,
    * injected chrome blocks are removed before extraction,
    * a block is DUPLICATED when it occurs more often in the generated output
      than in the source (a block that the source itself repeats - e.g. a
      certificate header printed on many pages - is not a defect).

Usage:
    python split_qa.py <repo>/vi/books/<slug> [--src <source html>]
"""
import argparse
import html as htmlmod
import os
import re
import sys
from collections import Counter

# chrome the splitter injects -- excluded before block extraction
CHROME_RES = [
    re.compile(r'<nav class="tocbar">.*?</nav>', re.S),
    re.compile(r'<p class="chead">.*?</p>', re.S),
    re.compile(r'<div class="chsecnav">.*?</div>', re.S),
    re.compile(r'<div class="partnav">.*?</div>', re.S),
    re.compile(r'<p class="tnote">.*?</p>', re.S),
    re.compile(r'<ul class="toclist">.*?</ul>', re.S),
]

BLOCK_END = re.compile(
    r'</(?:p|div|section|h1|h2|h3|h4|h5|li|td|th|tr|blockquote|pre|figure|'
    r'figcaption|table|thead|tbody|ul|ol|dl|dd|dt|article|aside)>',
    re.I)

MIN_BLOCK_WORDS = 30


def read(p):
    with open(p, encoding='utf-8') as f:
        return f.read()


def main_inner(h):
    m = re.search(r'<main[^>]*id="book-content"[^>]*>', h)
    if not m:
        return h
    s = m.end()
    d = 1
    for t in re.finditer(r'<(/?)main\b[^>]*>', h[s:]):
        if t.group(1):
            d -= 1
            if d == 0:
                return h[s:s + t.start()]
        else:
            d += 1
    return h[s:]


def plain(x):
    x = re.sub(r'(?s)<(script|style)[^>]*>.*?</\1>', ' ', x)
    x = re.sub(r'<[^>]+>', ' ', x)
    x = htmlmod.unescape(x)
    return re.sub(r'\s+', ' ', x).strip()


def words(x):
    return plain(x).split()


def strip_chrome(h):
    for rx in CHROME_RES:
        h = rx.sub(' ', h)
    return h


def blocks(h):
    """-> Counter of word-tuples of paragraph-sized blocks (chrome removed)."""
    h = strip_chrome(h)
    out = Counter()
    for chunk in BLOCK_END.split(h):
        w = words(chunk)
        if len(w) >= MIN_BLOCK_WORDS:
            out[tuple(w)] += 1
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('folder')
    ap.add_argument('--src', default=None)
    a = ap.parse_args()

    folder = a.folder
    files = sorted(f for f in os.listdir(folder) if f.endswith('.html'))
    chapters = [f for f in files if f.startswith('ch')]
    idx = 'index.html' if 'index.html' in files else None
    errs, warns = [], []

    if not chapters:
        errs.append('no chapter pages found')
    if not idx:
        errs.append('no index.html found')

    # --- 3. relative links resolve -----------------------------------
    for f in files:
        h = read(os.path.join(folder, f))
        for href in re.findall(r'(?:href|src)="([^"]+)"', h):
            if href.startswith(('http', '//', '/', '#', 'mailto', 'data:', 'javascript')):
                continue
            tgt = href.split('#')[0]
            if not tgt:
                continue
            p = os.path.normpath(os.path.join(folder, tgt))
            if not os.path.exists(p):
                errs.append('%s -> broken link %s' % (f, href))

    # --- 4. TOC links == chapter files --------------------------------
    if idx:
        h = read(os.path.join(folder, idx))
        m = re.search(r'<ul class="toclist">(.*?)</ul>', h, re.S)
        toc = m.group(1) if m else ''
        links = re.findall(r'href="(ch[^"]+)"', toc)
        if sorted(links) != sorted(chapters):
            errs.append('TOC links mismatch: %d links vs %d files'
                        % (len(links), len(chapters)))
        # every chapter must be reachable from the TOC
        missing = set(chapters) - set(links)
        if missing:
            errs.append('chapters not linked from TOC: %s' % sorted(missing))
        if not toc:
            errs.append('index.html has no <ul class="toclist">')

    # --- 5/6. nav + heading on each chapter ----------------------------
    for i, f in enumerate(chapters):
        h = read(os.path.join(folder, f))
        if 'class="partnav"' not in h:
            errs.append('%s: missing bottom nav' % f)
        if 'class="chapter"' not in h:
            errs.append('%s: missing chapter heading' % f)
        if 'href="./"' not in h and 'href="./index.html"' not in h:
            errs.append('%s: no link back to TOC' % f)
        if i > 0 and chapters[i - 1] not in h:
            warns.append('%s: prev link missing' % f)
        if i < len(chapters) - 1 and chapters[i + 1] not in h:
            warns.append('%s: next link missing' % f)

    # --- 1/2. content preservation + duplication ------------------------
    if a.src:
        src_html = read(a.src)
        sw = words(main_inner(src_html))
        cw = []
        for f in chapters:
            cw += words(main_inner(read(os.path.join(folder, f))))
        if idx:
            # the hero / front-matter block lives on the TOC page
            cw += words(main_inner(read(os.path.join(folder, idx))))
        cs, cc = Counter(sw), Counter(cw)
        missing = {w: c - cc.get(w, 0) for w, c in cs.items() if c > cc.get(w, 0)}
        extra = sum(cc.get(w, 0) - cs.get(w, 0) for w in cc)
        if missing:
            errs.append('CONTENT LOSS: %d source words missing (e.g. %s)'
                        % (len(missing), list(missing.items())[:8]))

        # --- duplication, block level, nav-immune -----------------------
        sb = blocks(main_inner(src_html))
        gb = Counter()
        for f in chapters:
            gb += blocks(main_inner(read(os.path.join(folder, f))))
        if idx:
            gb += blocks(main_inner(read(os.path.join(folder, idx))))
        dups = []
        for blk, n in gb.items():
            if n > sb.get(blk, 0):
                dups.append((n - sb.get(blk, 0), blk))
        if dups:
            dups.sort(reverse=True)
            errs.append('DUPLICATION: %d block(s) repeated more often than in the '
                        'source (e.g. +%d "%s...")'
                        % (len(dups), dups[0][0], ' '.join(dups[0][1][:12])))

        ratio = extra / max(1, len(sw))
        print('   source words %d | chapter+index words %d | missing %d | '
              'nav-overhead %d (+%.1f%%) | dup blocks %d'
              % (len(sw), len(cw), len(missing), extra, ratio * 100, len(dups)))

    print('== %s ==' % folder)
    print('   files: %d chapters + %s' % (len(chapters), 'index' if idx else 'NO INDEX'))
    for e in errs:
        print('   ERROR  ' + e)
    for w in warns:
        print('   WARN   ' + w)
    if not errs:
        print('   PASS (no errors)')
    return 1 if errs else 0


if __name__ == '__main__':
    sys.exit(main())
