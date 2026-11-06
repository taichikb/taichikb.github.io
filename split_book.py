#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
split_book.py -- split a single-file Vietnamese reader into a TOC index + one
page per chapter, for ANY book that uses the TaichiNOW reader layout
(<main class="book-content" id="book-content"> + <aside class="book-sidebar">).

Output layout (mirrors vi/books/the_trigger_point_manual/ and
vi/books/y_gia_y_da_lieu_duc_quan/):

    vi/books/<slug>/index.html        -> TOC: book hero + linked chapter list
    vi/books/<slug>/chNN-<slug>.html   -> one page per chapter

Design notes
------------
* The source document's own head/CSS/JS is REUSED, so typography, figures,
  tables and the sidebar/font controls keep working.  We only replace the
  content inside <main id="book-content">.
* The book's own sidebar TOC (<a href="#secNN">) is rewritten into
  cross-page links to the chapter pages, so the sidebar becomes a real TOC
  with "links to TOC".
* Chapter detection:
    - if the content holds <section id="secNN"> blocks -> one chapter per
      section (this is how the Chinese taijiquan classics are built);
    - otherwise -> one chapter per <h2> that is not a "Phần N" marker.
* Every chapter page gets a bottom nav (prev / Mục lục / next) and a
  "read the whole book on one page" link back to the monolithic file.

Usage:
    python split_book.py --src vi/books/foo_vi.html --slug foo \
        --title "Tên Sách" --author "Tác giả" [--category "Đông Y"]
"""
import argparse
import html as htmlmod
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
HOUSE_CSS_FILE = os.path.join(HERE, 'split_reader_house.css')

# Vietnamese stopwords dropped from slugs (matches the deployed slug style,
# e.g. "mo-ta-cac-mau-cua-..." -> "mo-ta-cac-mau-...").
STOP = {
    'cua', 'va', 'co', 'la', 'thi', 'de', 'voi', 'trong', 'nhat', 'mot',
    'cac', 'nhung', 'theo', 'vao', 'tu', 'la', 'roi', 'khi', 'ma',
}

PART_RE = re.compile(r'^\s*Phần\s+(\d+)\s*$', re.I)
H2_RE = re.compile(r'<h2([^>]*)>(.*?)</h2>', re.S)
H3_RE = re.compile(r'<h3([^>]*)>(.*?)</h3>', re.S)
SECTION_RE = re.compile(r'<section id="(sec[^"]*)"[^>]*>', re.I)


def read(path):
    with open(path, encoding='utf-8') as f:
        return f.read()


def write(path, text):
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)


def plain(markup):
    t = re.sub(r'<[^>]+>', ' ', markup)
    t = htmlmod.unescape(t)
    return re.sub(r'\s+', ' ', t).strip()


def slugify(text):
    s = text.replace('đ', 'd').replace('Đ', 'D')
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.lower()
    s = re.sub(r'[^a-z0-9]+', ' ', s).strip()
    toks = s.split()
    kept = [t for t in toks if t not in STOP]
    if len(kept) < 2:
        kept = toks
    return '-'.join(kept) or 'ch'


def find_main(html):
    """Return (start, end) offsets of the inner HTML of the book-content main."""
    m = re.search(r'<main[^>]*id="book-content"[^>]*>', html)
    if not m:
        m = re.search(r'<main[^>]*class="[^"]*book-content[^"]*"[^>]*>', html)
    if not m:
        return None
    start = m.end()
    depth = 1
    pos = start
    for tag in re.finditer(r'<(/?)main\b[^>]*>', html[start:]):
        if tag.group(1):
            depth -= 1
            if depth == 0:
                return start, start + tag.start()
        else:
            depth += 1
    return start, len(html)


def split_sections(inner):
    """Split inner HTML on <section id="secNN"> blocks. -> list of (sid, html)"""
    hits = list(SECTION_RE.finditer(inner))
    if len(hits) < 3:
        return None
    out = []
    for i, m in enumerate(hits):
        end = hits[i + 1].start() if i + 1 < len(hits) else len(inner)
        out.append((m.group(1), inner[m.end():end]))
    return out


def find_section_end(inner, start):
    """Offset just after the </section> that closes the one opened before start."""
    depth = 1
    pos = start
    for tag in re.finditer(r'<(/?)section\b[^>]*>', inner[start:]):
        if tag.group(1):
            depth -= 1
            if depth == 0:
                return start + tag.end()
        else:
            depth += 1
    return len(inner)


def extract_chapters(inner):
    """-> (intro_html, [(label, title, content_html)], tail_html)"""
    secs = split_sections(inner)
    if secs:
        intro = inner[:SECTION_RE.search(inner).start()]
        chapters = []
        for sid, chunk in secs:
            # trim the closing </section> of this block
            chunk = re.sub(r'\s*</section>\s*$', '', chunk)
            label = ''
            title = ''
            drop = []            # (start, end) spans of headings to remove
            for m in H2_RE.finditer(chunk):
                t = plain(m.group(2))
                if PART_RE.match(t) and not title:
                    label = t
                    drop.append((m.start(), m.end()))
                    continue
                title = t
                drop.append((m.start(), m.end()))
                break
            # remove the consumed headings in ONE pass (descending order keeps
            # the remaining offsets valid)
            content = chunk
            for s, e in sorted(drop, reverse=True):
                content = content[:s] + content[e:]
            chapters.append((label, title, content.strip()))
        tail = ''
        return intro, chapters, tail

    # fallback: split on h2
    hits = list(H2_RE.finditer(inner))
    if len(hits) < 2:
        return inner, [], ''
    intro = inner[:hits[0].start()]
    chapters = []
    label = ''
    i = 0
    while i < len(hits):
        m = hits[i]
        t = plain(m.group(2))
        if PART_RE.match(t):
            label = t
            i += 1
            continue
        end = hits[i + 1].start() if i + 1 < len(hits) else len(inner)
        content = inner[m.end():end].strip()
        chapters.append((label, t, content))
        label = ''
        i += 1
    return intro, chapters, ''


def rewrite_links(markup, mapping):
    """Rewrite #secNN style anchors to cross-page links using `mapping`."""
    def sub(m):
        target = m.group(1)
        return 'href="%s"' % mapping.get(target, m.group(0)[6:-1])
    return re.sub(r'href="#([^"]+)"', sub, markup)


def build(args):
    src = read(args.src)
    base = os.path.basename(args.src)
    slug = args.slug or re.sub(r'_vi$', '', base[:-5])
    outdir = os.path.join(args.repo, 'vi', 'books', slug)
    os.makedirs(outdir, exist_ok=True)

    house_css = read(HOUSE_CSS_FILE)
    mm = find_main(src)
    if not mm:
        sys.exit('ERROR: no <main id="book-content"> in %s' % args.src)
    inner = src[mm[0]:mm[1]]
    intro, chapters, tail = extract_chapters(inner)
    if not chapters:
        sys.exit('ERROR: no chapters detected in %s' % args.src)

    # ---- filenames + title map -------------------------------------------
    files, titles, labels = [], [], []
    used = set()
    for i, (label, title, _c) in enumerate(chapters, 1):
        base_slug = slugify(title)[:60].strip('-') or ('phan-%d' % i)
        s = base_slug
        n = 2
        while s in used:
            s = '%s-%d' % (base_slug, n)
            n += 1
        used.add(s)
        files.append('ch%02d-%s.html' % (i, s))
        titles.append(title)
        labels.append(label)

    secmap = {}
    if split_sections(inner):
        secs = split_sections(inner)
        for i, (sid, _c) in enumerate(secs):
            if i < len(files):
                secmap[sid] = files[i] + '#' + sid

    # ---- chapter pages ---------------------------------------------------
    for i, (label, title, content) in enumerate(chapters):
        body = content
        # drop the source's own h2 (already consumed) and any leftover "Phần N"
        body = re.sub(r'<h2[^>]*>\s*Phần\s+\d+\s*</h2>', '', body, flags=re.I)
        # give every h3 a stable id so the in-chapter nav can link to it
        sec_items = []
        counter = [0]

        def add_id(m):
            counter[0] += 1
            attrs = m.group(1)
            if 'id=' in attrs:
                return m.group(0)
            return '<h3 id="s%d"%s>%s</h3>' % (counter[0], attrs, m.group(2))

        body = H3_RE.sub(add_id, body)
        for m in H3_RE.finditer(body):
            mid = re.search(r'id="([^"]+)"', m.group(1))
            if mid:
                sec_items.append((mid.group(1), plain(m.group(2))))

        body = rewrite_links(body, secmap)

        chead = args.title
        if label:
            chead = '%s · %s' % (args.title, label)
        elif args.author:
            chead = '%s · %s' % (args.title, args.author)

        prev = ('<span class="disabled"><span class="k">← Đầu sách</span>'
                'Bắt đầu cuốn sách</span>') if i == 0 else (
            '<a href="%s"><span class="k">← Chương %d</span>%s</a>'
            % (files[i - 1], i, titles[i - 1]))
        nxt = ('<span class="disabled"><span class="k">Hết sách →</span>'
               'Kết thúc cuốn sách</span>') if i == len(chapters) - 1 else (
            '<a href="%s" style="text-align:right"><span class="k">Chương %d →</span>%s</a>'
            % (files[i + 1], i + 2, titles[i + 1]))
        centre = '<a href="./" style="text-align:center"><span class="k">Trang chủ</span>Mục lục sách</a>'

        secnav = ''
        if sec_items:
            cap = 60
            shown = sec_items[:cap]
            links = ' · '.join('<a href="#%s">%s</a>' % (i2, t) for i2, t in shown)
            if len(sec_items) > cap:
                links += ' · <em>… và %d mục khác</em>' % (len(sec_items) - cap)
            secnav = ('<div class="chsecnav"><span class="lab">Trong chương này</span>'
                      '%s</div>' % links)

        page = src
        page = page[:mm[0]] + body + page[mm[1]:]
        page = rewrite_links(page, secmap)
        page = re.sub(r'<title>.*?</title>',
                      '<title>Chương %d: %s — %s | TaichiNOW</title>'
                      % (i + 1, htmlmod.escape(title), htmlmod.escape(args.title)),
                      page, count=1, flags=re.S)
        page = re.sub(r'<meta name="description" content="[^"]*">',
                      '<meta name="description" content="%s">'
                      % htmlmod.escape('Chương %d của %s: %s' % (i + 1, args.title, title)),
                      page, count=1)
        # inject the house nav CSS + the bottom nav bar before </main>
        nav = (
            '\n<nav class="tocbar"><a href="./">← Mục lục sách</a>'
            '<span class="sep">·</span>'
            '<a href="../%s">Đọc toàn bộ trong một trang</a>'
            '<span class="sep">·</span>'
            '<a href="./index.html">Trang mục</a></nav>\n'
            '<p class="chead">%s</p>\n'
            '<h3 class="chapter" id="ch%02d">%s</h3>\n'
            '%s\n'
            '<div class="partnav">%s\n%s\n%s\n</div>\n'
            '<p class="tnote">%s</p>\n'
            % (base, htmlmod.escape(chead), i + 1, htmlmod.escape(title),
               secnav, prev, centre, nxt,
               htmlmod.escape(args.footer or
                             'Bản dịch tiếng Việt trên TaichiNOW. Nội dung gốc: %s.'
                             % (args.author or args.title)))
        )
        page = page.replace('<main', nav + '<main', 1) if False else page
        # insert nav right after the opening <main ...> tag
        page = re.sub(r'(<main[^>]*id="book-content"[^>]*>)', r'\1' + nav.replace('\\', '\\\\'), page, count=1)
        # house CSS goes into the head, right before </head>
        page = page.replace('</head>', '<style>%s</style>\n</head>' % house_css, 1)
        write(os.path.join(outdir, files[i]), page)

    # ---- index (TOC) page ------------------------------------------------
    toc_items = []
    for i, (title, label) in enumerate(zip(titles, labels), 1):
        pg = ('<span class="pg">%s</span>' % htmlmod.escape(label)) if label else ''
        toc_items.append(
            '<li><a href="%s"><span class="num">%d</span>'
            '<span class="ttl">%s</span>%s</a></li>'
            % (files[i - 1], i, htmlmod.escape(title), pg))

    hero = intro
    toc_html = (
        '<h2 class="tocpart-h" id="muc-luc">Mục lục '
        '<span>(%d chương)</span></h2>\n'
        '<ul class="toclist">\n%s\n</ul>\n'
        % (len(chapters), '\n'.join(toc_items))
    )
    idx = src
    idx = idx[:mm[0]] + hero + toc_html + idx[mm[1]:]
    idx = rewrite_links(idx, secmap)
    idx = re.sub(r'<title>.*?</title>',
                 '<title>Mục Lục — %s | TaichiNOW</title>' % htmlmod.escape(args.title),
                 idx, count=1, flags=re.S)
    idx = re.sub(r'<meta name="description" content="[^"]*">',
                 '<meta name="description" content="%s">'
                 % htmlmod.escape('Mục lục %d chương của %s.' % (len(chapters), args.title)),
                 idx, count=1)
    idx = re.sub(r'(<main[^>]*id="book-content"[^>]*>)',
                 r'\1' + ('\n<nav class="tocbar">'
                          '<a href="../%s">Đọc toàn bộ trong một trang</a>'
                          '<span class="sep">·</span>'
                          '<a href="/vi/books/">← Thư Viện Sách</a></nav>\n' % base),
                 idx, count=1)
    idx = idx.replace('</head>', '<style>%s</style>\n</head>' % house_css, 1)
    write(os.path.join(outdir, 'index.html'), idx)

    print('%-34s -> %s/  (%d chapters + index)' % (base, slug, len(chapters)))
    return slug, len(chapters)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--src', required=True)
    ap.add_argument('--repo', default=HERE)
    ap.add_argument('--slug', default=None)
    ap.add_argument('--title', required=True)
    ap.add_argument('--author', default='')
    ap.add_argument('--category', default='')
    ap.add_argument('--footer', default='')
    a = ap.parse_args()
    build(a)


if __name__ == '__main__':
    main()
