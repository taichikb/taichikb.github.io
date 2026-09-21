#!/usr/bin/env python3
"""
Build full-depth health articles (EN/VI) for taichikb.github.io.
Converts the 10-section Markdown articles into the site base template,
mirroring the build_techniques.py injection pattern.
"""
import os, re, html
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
VAULT_URL = "https://notebooklm.google.com/notebook/d2401afd-0718-4fac-b429-5bca391d27a9"

ARTICLES = [
    {
        "md": "en/articles/EN-001-TCM_Meridians-meridian-flow-mechanics.md",
        "out": "en/articles/meridian-flow-mechanics",
        "lang": "en",
        "title": "Meridian Flow Mechanics: How Qi Navigates the 12 Primary Channels",
        "subtitle": "TaichiKB Health Article EN-001 · Traditional Chinese Medicine & Meridian Science",
        "crosslink": "/vi/articles/co-hoanh-12-kinh-lac/",
        "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-001-TCM_Meridians-meridian-flow-mechanics.md",
        "out": "vi/articles/co-hoanh-12-kinh-lac",
        "lang": "vi",
        "title": "Cơ Hoành & Đường Đi Của Khí Trong 12 Kinh Lạc Chính",
        "subtitle": "TaichiKB Health Article VI-001 · Y Học Cổ Truyền & Kinh Lạc",
        "crosslink": "/en/articles/meridian-flow-mechanics/",
        "crosslabel": "🇬🇧 English",
    },
]

def read_base_template(lang):
    if lang == "en":
        cand = [REPO_ROOT / "index_clean.html", REPO_ROOT / "index.html"]
    else:
        cand = [REPO_ROOT / "vi" / "index.html"]
    for c in cand:
        if c.exists():
            return c.read_text(encoding="utf-8")
    raise FileNotFoundError("no base template found")

def inline_md(text):
    """Bold, italic, links, inline code."""
    t = html.escape(text, quote=False)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)', r'<em>\1</em>', t)
    t = re.sub(r'`([^`]+?)`', r'<code>\1</code>', t)
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank" rel="noopener">\1</a>', t)
    return t

def md_to_html(md):
    lines = md.split("\n")
    out, i, n = [], 0, len(lines)
    in_list = False
    def close_list():
        nonlocal in_list
        if in_list:
            out.append("</ol>" if out and out[-2 if len(out)>1 else 0].find("<ol")>=0 else "</ul>")
            nonlocal_flag = None
    list_stack = []
    def close_open_lists():
        while list_stack:
            out.append("</ul>" if list_stack.pop() == "ul" else "</ol>")
    while i < n:
        line = lines[i].rstrip()
        s = line.strip()
        if not s:
            close_open_lists(); i += 1; continue
        # code fence
        if s.startswith("```"):
            close_open_lists()
            lang = s[3:].strip()
            out.append('<div class="code-block"><pre><code>')
            i += 1
            buf = []
            while i < n and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1  # skip closing fence
            code = "\n".join(buf)
            # raw HTML embeds (video iframes) passthrough
            if lang.lower() == "html" and "<iframe" in code:
                out.pop()  # remove the code-block opener
                out.append('<div class="video-embed">')
                out.append(code)
                out.append("</div>")
            else:
                out.append(html.escape(code))
                out.append("</code></pre></div>")
            continue
        # headings
        m = re.match(r'^(#{1,3})\s+(.*)$', s)
        if m:
            close_open_lists()
            level = len(m.group(1))
            txt = inline_md(m.group(2))
            if level == 1: out.append(f'<h1 class="article-title">{txt}</h1>')
            elif level == 2: out.append(f'<h2 class="section-heading" id="sec-{len(out)}">{txt}</h2>')
            else: out.append(f'<h3 class="sub-heading">{txt}</h3>')
            i += 1; continue
        # horizontal rule
        if re.match(r'^-{3,}$', s):
            close_open_lists(); out.append('<hr class="art-hr">'); i += 1; continue
        # blockquote
        if s.startswith(">"):
            close_open_lists()
            quote = []
            while i < n and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip().lstrip(">").strip())
                i += 1
            out.append('<blockquote class="callout-box">' + inline_md(" ".join(quote)) + "</blockquote>")
            continue
        # table
        if "|" in s and i+1 < n and re.match(r'^\s*\|[\s:\-|]+\|\s*$', lines[i+1]):
            close_open_lists()
            header = [c.strip() for c in s.strip("|").split("|")]
            i += 2
            rows = []
            while i < n and "|" in lines[i] and lines[i].strip():
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            out.append('<div class="table-scroll"><table class="data-table"><thead><tr>')
            out += [f"<th>{inline_md(c)}</th>" for c in header]
            out.append("</tr></thead><tbody>")
            for r in rows:
                out.append("<tr>" + "".join(f"<td>{inline_md(c)}</td>" for c in r) + "</tr>")
            out.append("</tbody></table></div>")
            continue
        # ordered list
        m = re.match(r'^\s*(\d+)[.)]\s+(.*)$', line)
        if m:
            if not list_stack or list_stack[-1] != "ol":
                close_open_lists(); list_stack.append("ol"); out.append("<ol>")
            out.append(f"<li>{inline_md(m.group(2))}</li>")
            i += 1; continue
        # unordered list
        if re.match(r'^\s*[-*]\s+', line):
            if not list_stack or list_stack[-1] != "ul":
                close_open_lists(); list_stack.append("ul"); out.append("<ul>")
            item = re.sub(r'^\s*[-*]\s+', '', line)
            out.append(f"<li>{inline_md(item)}</li>")
            i += 1; continue
        close_open_lists()
        # video/iframe raw html passthrough
        if s.startswith("<"):
            out.append(line); i += 1; continue
        out.append(f"<p>{inline_md(s)}</p>")
        i += 1
    close_open_lists()
    return "\n".join(out)

def article_css():
    return """
<style>
.article-wrap { max-width: 900px; margin: 0 auto; padding: 24px 16px 60px; }
.article-title { font-size: 1.8em; line-height: 1.3; margin: .3em 0 .6em; }
.article-hero { text-align:center; padding: 30px 10px 6px; }
.article-hero .page-subtitle { color: var(--muted, #777); }
.section-heading { margin-top: 2em; padding-bottom: .3em; border-bottom: 2px solid var(--accent,#8b2635); color: var(--accent,#8b2635); font-size: 1.35em; }
.sub-heading { margin-top: 1.4em; font-size: 1.1em; }
.art-hr { border: 0; border-top: 1px solid var(--border,#ddd); margin: 2em 0; }
.callout-box { border-left: 4px solid var(--accent,#8b2635); background: rgba(139,38,53,.06); padding: 14px 18px; margin: 1.5em 0; border-radius: 0 8px 8px 0; }
.dark-mode .callout-box { background: rgba(217,138,149,.08); }
.table-scroll { overflow-x: auto; margin: 1.4em 0; }
.data-table { border-collapse: collapse; width: 100%; font-size: .95em; }
.data-table th { background: var(--accent,#8b2635); color: #fff; text-align: left; padding: 8px 12px; }
.data-table td { border: 1px solid var(--border,#ddd); padding: 8px 12px; vertical-align: top; }
.dark-mode .data-table td { border-color: #3a3a3a; }
.code-block { background: #181818; color: #f0f0f0; border: 1px solid rgba(255,255,255,.15); border-radius: 8px; padding: 14px 16px; overflow-x: auto; font-size: .88em; line-height: 1.5; margin: 1.2em 0; }
.code-block pre, .code-block code { color: #f0f0f0 !important; background: transparent !important; margin: 0; }
.video-embed { margin: 1.5em 0; }
.vault-note { text-align: center; font-size: .9em; color: var(--muted,#777); }
article p { margin: .8em 0; }
article ol, article ul { margin: .8em 0 .8em 1.4em; }
article li { margin: .35em 0; }
</style>
"""

def build_article(a):
    template = read_base_template(a["lang"])
    md = (REPO_ROOT / a["md"]).read_text(encoding="utf-8")
    # strip front matter
    md = re.sub(r'^---\n.*?\n---\n', '', md, count=1, flags=re.S)
    body_html = md_to_html(md)
    lang_sw = f'<a class="lang-switch" href="{a["crosslink"]}">{a["crosslabel"]}</a>'
    vault = f'<a href="{VAULT_URL}" target="_blank" rel="noopener">299 grounded sources</a>'
    main = f"""<main class="health-article" role="main">
{article_css()}
<article class="article-wrap">
    <header class="article-hero">
        <p class="page-subtitle">{html.escape(a["subtitle"])}</p>
        <h1 class="article-title">{html.escape(a["title"])}</h1>
        <p class="vault-note">Health, TCM, Energy Medicine, Yoga, Taichi & Qigong Vault · {vault}</p>
        <p>{lang_sw}</p>
    </header>
    {body_html}
    <footer class="page-footer">
        <p><a href="/{a["lang"]}/">← Back to {a["lang"].upper()} Home</a></p>
    </footer>
</article>
</main>"""
    # inject into template
    m = template.find("<main")
    if m == -1:
        m = template.find("<article")
    e = template.find("</main>")
    if e == -1:
        e = template.find("</article>")
    if m != -1 and e != -1:
        html_out = template[:m] + main + template[e+7:]
    else:
        html_out = template + main
    outdir = REPO_ROOT / a["out"]
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "index.html").write_text(html_out, encoding="utf-8")
    print(f"OK built {outdir / 'index.html'} ({len(html_out)//1024} KB)")

def main():
    for a in ARTICLES:
        build_article(a)

if __name__ == "__main__":
    main()
