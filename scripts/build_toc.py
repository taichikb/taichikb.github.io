#!/usr/bin/env python3
"""Build the article table of contents, linking each page to its GitHub source.

Reads the same git tree the site is published from, so the links always point at
the real files. Groups by section and notes which pages share an illustration.

Usage
-----
  python build_toc.py --out ../ARTICLES_TOC.md
  python build_toc.py --out ARTICLES_TOC.md --site https://taichinow.github.io
"""

from __future__ import annotations

import argparse
import html as htmllib
import json
import os
import re
import subprocess
import sys
from datetime import datetime

DEFAULT_REPO = r"D:\Taichi-Health-Finance\Intranet\deploy"
DEFAULT_BRANCH = "main"
DEFAULT_SITE = "https://taichinow.github.io"
DEFAULT_GH = "https://github.com/taichinow/taichinow.github.io"
SOURCE_DIRS = ("articles", "techniques", "vi/articles")
INDEX_SLUGS = {"articles", "techniques", "vi/articles"}
SECTION_TITLES = {
    "articles": "Articles",
    "techniques": "Techniques",
    "vi/articles": "Vietnamese Articles",
}

# Curated additions: pages that live inside another page rather than at their
# own top-level slug, so the git-tree walk above cannot find them. They are
# hand-registered here (with an explicit anchor) so the index stays exhaustive.
# Each entry: (section, slug, title, live_url_path, source_path, image_id)
CURATED = [
    (
        "vi/articles",
        "vi/books/martial_arts_qigong_health_vitality_vi#sec2b-guong-luong-tu",
        "“Khoa Học Trung Hoa” Soi Gương Qua Vật Lý Lượng Tử Hiện Đại "
        "(Nguyên Lý Âm Dương, Ngũ Hành & Cơ Học Lượng Tử)",
        "vi/books/martial_arts_qigong_health_vitality_vi.html#sec2b-guong-luong-tu",
        "vi/books/martial_arts_qigong_health_vitality_vi.html",
        "articles__complete-taichi-practice-guide-for-the-30-beginner",
    ),
]

# Illustration fallbacks for pages the plan does not cover (e.g. one half of a
# bilingual pair). Maps slug -> illustration id already present in the plan.
IMAGE_FALLBACK = {
    "vi/articles/giai-phau-nang-luong-toan-tap": "articles__complete-taichi-practice-guide-for-the-30-beginner",
}


def git(repo: str, *args: str) -> str:
    return subprocess.run(["git", "-C", repo, *args],
                          capture_output=True).stdout.decode("utf-8", "replace")


TITLE_SUFFIX_RE = re.compile(r"\s*(?:—|–|\||-)\s*Taichi\s*NOW\s*$", re.I)


def page_title(raw: str) -> str:
    m = re.search(r"<h1[^>]*>(.*?)</h1>", raw, re.S | re.I)
    if m:
        t = htmllib.unescape(re.sub(r"<[^>]+>", " ", m.group(1)))
        t = re.sub(r"\s+", " ", t).strip().rstrip("# ").strip()
        if t:
            return t
    # Some pages are plain <p> streams with no <h1> at all. Without this they
    # were silently dropped from the index entirely.
    m = re.search(r"<title>(.*?)</title>", raw, re.S | re.I)
    if not m:
        return ""
    t = htmllib.unescape(re.sub(r"<[^>]+>", " ", m.group(1)))
    t = re.sub(r"\s+", " ", t).strip()
    return TITLE_SUFFIX_RE.sub("", t).strip()


def page_description(raw: str) -> str:
    m = re.search(r'<meta\s+name="description"\s+content="(.*?)"', raw, re.S | re.I)
    if not m:
        return ""
    d = htmllib.unescape(m.group(1))
    return re.sub(r"\s+", " ", d).strip()


def page_h1_missing(raw: str) -> bool:
    return not re.search(r"<h1[^>]*>", raw, re.I)


def md_escape(text: str) -> str:
    return text.replace("|", "\\|").strip()


TAIJI_SVG = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" '
             'class="taiji-logo"><circle cx="100" cy="100" r="98" fill="#ffffff" '
             'stroke="#000000" stroke-width="4"/><path d="M 100,2 A 98,98 0 0,1 '
             '100,198 A 49,49 0 0,1 100,100 A 49,49 0 0,0 100,2 Z" fill="#000000"/>'
             '<circle cx="100" cy="51" r="12" fill="#ffffff"/>'
             '<circle cx="100" cy="149" r="12" fill="#000000"/></svg>')

NAV_ITEMS = [
    ("/", "Home"), ("/techniques/", "Techniques"), ("/books/", "Books"),
    ("/health/", "Health"), ("/videos/", "Videos"), ("/podcast/", "Podcast"),
    ("/philosophy/", "Philosophy"), ("/history/", "History"),
    ("/contact/", "Contact"),
]


def card_html(r: dict, e, args, section: str | None = None) -> str:
    """One index card. ``section`` overrides the card's data-section so curated
    cards can be surfaced under their own chip filter."""
    thumb = (f'<img src="/facebook/media/generated/{e(r["image"])}.jpg" '
             f'alt="" loading="lazy" decoding="async">'
             if r["image"] else
             '<div class="noimg">no illustration</div>')
    gh_img = (f'{args.github}/blob/{args.branch}/facebook/media/generated/'
              f'{r["image"]}.jpg' if r["image"] else "")
    links = [f'<a href="{e(r["live"])}">Đọc / Read</a>',
             f'<a href="{e(r["source"])}">Source</a>']
    if gh_img:
        links.append(f'<a href="{e(gh_img)}">Illustration</a>')
    tags = ""
    if r.get("curated"):
        tags += '<span class="tag tag-qm">Quantum Mirror</span>'
    elif r.get("shared_with"):
        tags += '<span class="tag">shared illustration</span>'
    sec = f' data-sec="{section}"' if section else ""
    slug_disp = r["slug"].split("#")[0] if r.get("curated") else r["slug"]
    return (
        f'<article class="card" data-t="{e(r["title"].lower())}"{sec}>'
        f'<a class="thumb" href="{e(r["live"])}">{thumb}</a>'
        f'<h3><a href="{e(r["live"])}">{e(r["title"])}</a></h3>'
        f'<p class="meta">{e(slug_disp)}{tags}</p>'
        f'<p class="links">{" · ".join(links)}</p>'
        f'</article>')


def render_index_html(sections, args, total, illustrated, missing_h1) -> str:
    """The new 'All Articles' section page: a searchable index of every page."""
    e = htmllib.escape
    nav = "\n".join(
        f'<a href="{href}" class="">{label}</a>' for href, label in NAV_ITEMS)
    nav += '\n<a href="/all-articles/" class="active">All Articles</a>'
    nav += '\n<a href="/en/" class="lang-switch">🇬🇧 English</a>'

    cards: list[str] = []
    for d in SOURCE_DIRS:
        rows = sections.get(d) or []
        cards.append(f'<h2 id="{SECTION_TITLES[d].lower().replace(" ", "-")}" '
                     f'data-section="{d}">{e(SECTION_TITLES[d])} '
                     f'<span class="count">{len(rows)}</span></h2>')
        cards.append(f'<div class="grid" data-section="{d}">')
        for r in rows:
            cards.append(card_html(r, e, args))
        cards.append('</div>')

    # Curated "Quantum Mirror" feature section. Its cards use a different
    # data-section so the chip filter can surface them on their own.
    qm_cards = [card_html(r, e, args, section="quantum")
                for d in SOURCE_DIRS for r in (sections.get(d) or [])
                if r.get("curated")]
    if qm_cards:
        cards.append('<h2 id="quantum-mirror" data-section="quantum">'
                     'Quantum Mirror · Khoa Học Trung Hoa &amp; Vật Lý Lượng Tử '
                     f'<span class="count">{len(qm_cards)}</span></h2>')
        cards.append('<p class="qnote">Đối chiếu nguyên lý Âm Dương, Ngũ Hành và Bát Quái '
                     'với chân không lượng tử, nguyên lý bổ sung, thang bậc và vấn đề đo lường '
                     'trong vật lý hiện đại — một lớp chú giải, không phải một phép quy đổi.</p>')
        cards.append('<div class="grid" data-section="quantum">')
        cards.extend(qm_cards)
        cards.append('</div>')

    generated = datetime.now().strftime("%Y-%m-%d")
    md_gh = f"{args.github}/blob/{args.branch}/ARTICLES_TOC.md"
    return f"""<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>All Articles · Tất Cả Bài Viết — TaichiNOW</title>
<link rel="icon" href="/assets/images/taiji-logo.svg" type="image/svg+xml">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/stylesheets/yin-yang.css">
<meta name="description" content="{total} illustrated Tai Chi, Qigong and health articles from TaichiNOW — {illustrated} original artworks by Phạm Đức Hải.">
<meta property="og:type" content="website">
<meta property="og:site_name" content="TaichiNOW">
<meta property="og:title" content="All Articles · Tất Cả Bài Viết — TaichiNOW">
<meta property="og:description" content="{total} illustrated articles · {illustrated} original artworks by Phạm Đức Hải.">
<meta property="og:url" content="{args.site}/all-articles/">
<style>
.idx {{ max-width: 1180px; margin: 0 auto; padding: 2rem 1rem 4rem; }}
.idx .lede {{ font-size: 1.05rem; line-height: 1.6; opacity: .8; max-width: 62ch; }}
.idx .stats {{ display: flex; gap: 1.6rem; flex-wrap: wrap; margin: 1.4rem 0 1rem;
  padding: 1rem 1.2rem; border: 1px solid rgba(0,0,0,.12); border-radius: 12px; }}
.idx .stats b {{ font-size: 1.5rem; display: block; font-variant-numeric: tabular-nums; }}
.idx .stats span {{ font-size: .8rem; opacity: .65; text-transform: uppercase; letter-spacing: .06em; }}
.idx .controls {{ position: sticky; top: 0; z-index: 5; display: flex; gap: .6rem;
  flex-wrap: wrap; align-items: center; padding: .8rem 0; margin-bottom: 1rem;
  background: var(--bg, #fff); border-bottom: 1px solid rgba(0,0,0,.08); }}
.idx input[type=search] {{ flex: 1 1 240px; min-width: 200px; padding: .6rem .8rem;
  font: inherit; border: 1px solid rgba(0,0,0,.2); border-radius: 8px; }}
.idx .chip {{ padding: .45rem .85rem; border: 1px solid rgba(0,0,0,.2);
  border-radius: 999px; font-size: .85rem; cursor: pointer; background: none;
  font-family: inherit; }}
.idx .chip[aria-pressed=true] {{ background: #111; color: #fff; border-color: #111; }}
.idx h2 {{ margin: 2.2rem 0 .9rem; font-family: "Cormorant Garamond", Georgia, serif;
  font-size: 1.7rem; border-bottom: 1px solid rgba(0,0,0,.12); padding-bottom: .35rem; }}
.idx h2 .count {{ font-size: .85rem; font-family: Inter, system-ui, sans-serif;
  opacity: .55; vertical-align: middle; }}
.idx .grid {{ display: grid; gap: 1.2rem;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); }}
.idx .card {{ border: 1px solid rgba(0,0,0,.12); border-radius: 12px;
  overflow: hidden; display: flex; flex-direction: column; }}
.idx .thumb {{ display: block; aspect-ratio: 1200 / 630; background: #f3f3f3; }}
.idx .thumb img {{ width: 100%; height: 100%; object-fit: cover; display: block; }}
.idx .noimg {{ display: grid; place-items: center; height: 100%; font-size: .8rem;
  opacity: .45; }}
.idx .card h3 {{ font-size: 1rem; line-height: 1.35; margin: .8rem .9rem .3rem;
  font-family: Inter, system-ui, sans-serif; font-weight: 600; }}
.idx .card h3 a {{ text-decoration: none; color: inherit; }}
.idx .card h3 a:hover {{ text-decoration: underline; }}
.idx .meta {{ margin: 0 .9rem; font-size: .72rem; opacity: .5; word-break: break-all; }}
.idx .tag {{ margin-left: .4rem; padding: .1rem .4rem; border-radius: 4px;
  background: rgba(0,0,0,.07); }}
.idx .tag-qm {{ background: rgba(37,99,235,.12); color: #1e3a8a; }}
.idx .qnote {{ margin: -.4rem 0 1rem; font-size: .9rem; line-height: 1.55;
  opacity: .72; max-width: 70ch; }}
.idx .links {{ margin: .6rem .9rem .9rem; font-size: .85rem; }}
.idx .links a {{ text-decoration: none; border-bottom: 1px solid rgba(0,0,0,.25); }}
.idx .empty {{ padding: 2rem 0; opacity: .6; }}
@media (prefers-color-scheme: dark) {{
  .idx .controls {{ background: #14161a; }}
  .idx .chip[aria-pressed=true] {{ background: #f2f2f2; color: #111; border-color: #f2f2f2; }}
  .idx .card, .idx .stats, .idx .thumb {{ border-color: rgba(255,255,255,.16); }}
  .idx .thumb {{ background: #1c1f24; }}
  .idx .tag-qm {{ background: rgba(96,165,250,.18); color: #bfdbfe; }}
}}
</style>
</head>
<body>

<header class="site-header">
    <a href="/" class="brand">{TAIJI_SVG}<span>TaichiNOW</span></a>
    <nav class="site-nav">
{nav}
    </nav>
</header>

<main class="idx">
<h1>All Articles · Tất Cả Bài Viết</h1>
<p class="lede">Every article on TaichiNOW, in one place. Each page is illustrated with an
original artwork signed <em>Phạm Đức Hải · TAICHINOW</em>. The <strong>Source</strong> link
opens the page's HTML in the GitHub repository.</p>

<div class="stats">
  <div><b>{total}</b><span>article pages</span></div>
  <div><b>{illustrated}</b><span>illustrations</span></div>
  <div><b>{generated}</b><span>generated</span></div>
</div>
<p><a href="{md_gh}">📄 Full table of contents (Markdown, with GitHub source links)</a></p>

<div class="controls">
  <input type="search" id="q" placeholder="Tìm bài viết… / search titles" aria-label="Search articles">
  <button class="chip" data-f="all" aria-pressed="true">All</button>
  {''.join(f'<button class="chip" data-f="{d}" aria-pressed="false">{e(SECTION_TITLES[d])}</button>' for d in SOURCE_DIRS)}
  <button class="chip" data-f="quantum" aria-pressed="false">Quantum Mirror</button>
</div>

{chr(10).join(cards)}

<p class="empty" id="empty" hidden>No article matches that search.</p>

<nav class="page-nav">
    <a href="/" class="home">⌂ Home</a>
</nav>
</main>

<footer class="site-footer">
    <p>Built with ❤️ for the Vietnamese Tai Chi community by Phạm Đức Hải</p>
    <p>Trang web này được xây dựng với ❤️ cho cộng đồng Thái Cực Quyền Việt Nam bởi Phạm Đức Hải</p>
</footer>

<script>
(function () {{
  var q = document.getElementById('q');
  var empty = document.getElementById('empty');
  var chips = [].slice.call(document.querySelectorAll('.chip'));
  var heads = [].slice.call(document.querySelectorAll('.idx h2'));
  var grids = [].slice.call(document.querySelectorAll('.idx .grid'));
  var filter = 'all';

  function apply() {{
    var term = (q.value || '').trim().toLowerCase();
    var shown = 0;
    grids.forEach(function (grid) {{
      var visible = 0;
      [].slice.call(grid.children).forEach(function (card) {{
        // A card may declare its own section (e.g. a curated "quantum" card
        // living in the vi/articles grid); otherwise it inherits the grid's.
        var sec = card.dataset.sec || grid.dataset.section;
        var ok = (filter === 'all' || sec === filter)
                 && (!term || card.dataset.t.indexOf(term) !== -1);
        card.hidden = !ok;
        if (ok) {{ visible++; shown++; }}
      }});
      grid.hidden = visible === 0;
    }});
    heads.forEach(function (h) {{ 
      var grid = document.querySelector('.grid[data-section="' + h.dataset.section + '"]');
      h.hidden = (h.dataset.section !== filter && filter !== 'all') || (grid && grid.hidden); }});
    empty.hidden = shown !== 0;
  }}

  chips.forEach(function (c) {{
    c.addEventListener('click', function () {{
      filter = c.dataset.f;
      chips.forEach(function (o) {{ o.setAttribute('aria-pressed', String(o === c)); }});
      apply();
    }});
  }});
  q.addEventListener('input', apply);
}})();
</script>

</body>
</html>
"""


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo", default=DEFAULT_REPO)
    ap.add_argument("--branch", default=DEFAULT_BRANCH)
    ap.add_argument("--site", default=DEFAULT_SITE)
    ap.add_argument("--github", default=DEFAULT_GH)
    ap.add_argument("--plan", default="queue/illustration_plan.json")
    ap.add_argument("--out", default="ARTICLES_TOC.md")
    ap.add_argument("--html", help="also write the 'All Articles' section page "
                                   "(e.g. <repo>/all-articles/index.html)")
    args = ap.parse_args(argv)

    repo = os.path.abspath(args.repo)

    # The tree walk uses a git ref, but the *links* must point at a real branch
    # name. "HEAD" resolves fine for git show but would produce blob/HEAD/... in
    # the GitHub URLs, so normalise it to the actual branch.
    if args.branch in ("HEAD", ""):
        resolved = git(repo, "rev-parse", "--abbrev-ref", "HEAD").strip()
        if resolved and resolved != "HEAD":
            args.branch = resolved

    # slug -> illustration id (from the plan), so duplicate pages share one image
    image_of: dict[str, str] = {}
    rep_of: dict[str, str] = {}
    if not os.path.isfile(args.plan):
        # Without the plan every page looks un-illustrated and gets skipped,
        # which would quietly emit an empty index. Refuse instead.
        print(f"error: illustration plan not found: {args.plan}", file=sys.stderr)
        print("       pass --plan <path to illustration_plan.json>", file=sys.stderr)
        return 2
    with open(args.plan, encoding="utf-8") as fh:
        plan = json.load(fh)
    for item in plan["items"]:
        for s in item["slugs"]:
            image_of[s] = item["id"]
            rep_of[s] = item["representative"]

    sections: dict[str, list[dict]] = {}
    missing_h1: list[str] = []
    unillustrated: list[str] = []
    for d in SOURCE_DIRS:
        rows = []
        for line in git(repo, "ls-tree", "-r", args.branch, "--name-only", "--", d).splitlines():
            if not line.endswith("/index.html"):
                continue
            slug = line[: -len("/index.html")]
            if slug in INDEX_SLUGS:
                continue
            if not image_of.get(slug) and not IMAGE_FALLBACK.get(slug):
                # No illustration: a section hub, a redirect notice, or a page
                # the illustration plan does not cover. Listing it here would
                # add a "no illustration" row, so it is reported and skipped.
                unillustrated.append(slug)
                continue
            raw = git(repo, "show", f"{args.branch}:{slug}/index.html")
            title = page_title(raw)
            if not title:
                continue
            if page_h1_missing(raw):
                missing_h1.append(slug)
            rows.append({
                "slug": slug,
                "title": title,
                "live": f"{args.site}/{slug}/",
                "source": f"{args.github}/blob/{args.branch}/{slug}/index.html",
                "image": image_of.get(slug) or IMAGE_FALLBACK.get(slug, ""),
                "shared_with": rep_of.get(slug, slug) if rep_of.get(slug) != slug else "",
            })
        # curated entries that belong to this section
        for section, slug, title, live_path, source_path, image_id in CURATED:
            if section != d:
                continue
            rows.append({
                "slug": slug,
                "title": title,
                "live": f"{args.site}/{live_path}",
                "source": f"{args.github}/blob/{args.branch}/{source_path}",
                "image": image_id,
                "shared_with": "",
                "curated": True,
            })
        rows.sort(key=lambda r: r["title"].lower())
        sections[d] = rows

    total = sum(len(v) for v in sections.values())
    illustrated = len({r["image"] for v in sections.values() for r in v if r["image"]})

    out: list[str] = []
    out.append("# TaichiNOW — Article Index")
    out.append("")
    out.append(f"> **{total}** article pages · **{illustrated}** original illustrations · "
               f"generated {datetime.now().strftime('%Y-%m-%d')}")
    out.append(">")
    out.append(f"> Live site: <{args.site}> · Source: <{args.github}>")
    out.append("")
    out.append("Every article is illustrated with a signed original artwork. "
               "The **Source** column links to the page's HTML in the GitHub repository.")
    out.append("")

    out.append("## Contents")
    out.append("")
    for d in SOURCE_DIRS:
        rows = sections.get(d) or []
        anchor = SECTION_TITLES[d].lower().replace(" ", "-")
        out.append(f"- [{SECTION_TITLES[d]}](#{anchor}) — {len(rows)} pages")
    out.append("")

    for d in SOURCE_DIRS:
        rows = sections.get(d) or []
        out.append(f"## {SECTION_TITLES[d]}")
        out.append("")
        out.append(f"{len(rows)} pages")
        out.append("")
        out.append("| # | Title | Read | Source (GitHub) | Illustration |")
        out.append("|---|-------|------|-----------------|--------------|")
        for i, r in enumerate(rows, 1):
            if r["image"]:
                img = (f"[jpg]({args.github}/blob/{args.branch}"
                       f"/facebook/media/generated/{r['image']}.jpg)")
            else:
                img = "—"
            note = " *(shared)*" if r["shared_with"] else ""
            out.append(f"| {i} | {md_escape(r['title'])}{note} | [open]({r['live']}) "
                       f"| [index.html]({r['source']}) | {img} |")
        out.append("")

    out.append("---")
    out.append("")
    out.append("*Illustrations: original artwork by Phạm Đức Hải for TaichiNOW. "
               "Each carries a small corner signature.*")
    out.append("")

    text = "\n".join(out)
    os.makedirs(os.path.dirname(os.path.abspath(args.out)) or ".", exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(text)

    print(f"pages written : {total}")
    print(f"illustrated   : {illustrated}")
    print(f"output        : {args.out}  ({len(text) / 1024:.1f} KB)")
    for d in SOURCE_DIRS:
        print(f"  {d:<14} {len(sections.get(d) or [])}")
    if missing_h1:
        print(f"note: {len(missing_h1)} page(s) had no <h1>; titled from <title> instead:")
        for s in missing_h1:
            print(f"  {s}")
    if unillustrated:
        print(f"note: {len(unillustrated)} page(s) skipped (no illustration):")
        for s in unillustrated:
            print(f"  {s}")

    if args.html:
        page = render_index_html(sections, args, total, illustrated, missing_h1)
        os.makedirs(os.path.dirname(os.path.abspath(args.html)) or ".", exist_ok=True)
        with open(args.html, "w", encoding="utf-8") as fh:
            fh.write(page)
        print(f"section page  : {args.html}  ({len(page) / 1024:.1f} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
