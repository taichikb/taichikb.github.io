#!/usr/bin/env python3
"""Reskin all mkdocs-style pages in taichikb_repo to Yin-Yang theme.

Handles:
- Priority pages (books/, vi/books/, deep-dives/, cn/)
- Facebook posts (72 files)

Run: python scripts/reskin_mkdocs.py
"""

import re
import html as html_module
import sys
from pathlib import Path

REPO = Path("D:/Taichi-Health-Finance/Intranet/taichikb_repo")

TAIJI = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="20" height="20" style="vertical-align:-3px;display:inline-block;"><circle cx="100" cy="100" r="98" fill="#ffffff" stroke="#000000" stroke-width="4"/><path d="M 100,2 A 98,98 0 0,1 100,198 A 49,49 0 0,1 100,100 A 49,49 0 0,0 100,2 Z" fill="#000000"/><circle cx="100" cy="51" r="12" fill="#ffffff"/><circle cx="100" cy="149" r="12" fill="#000000"/></svg>'


def extract_mkdocs_content(html_text):
    title_m = re.search(r'<h1[^>]*>(.*?)</h1>', html_text)
    if title_m:
        title_text = title_m.group(1)
        title_text = re.sub(r'<a class="headerlink"[^>]*>.*?</a>', '', title_text)
        title_text = re.sub(r'<[^>]+>', '', title_text).strip()
        title_text = html_module.unescape(title_text)
    else:
        title_m = re.search(r'<title>([^<]+)</title>', html_text)
        title_text = title_m.group(1).strip() if title_m else "Untitled"

    article_m = re.search(r'<article[^>]*>(.*?)</article>', html_text, re.DOTALL)
    if article_m:
        article = article_m.group(1)
        article = re.sub(r'<h1[^>]*>.*?</h1>', '', article, count=1, flags=re.DOTALL)
        article = re.sub(r'<a class="headerlink"[^>]*>.*?</a>', '', article)
        article = re.sub(r'(href|src)="\.\.\/\.\.\/assets', r'\1="/assets', article)
        article = re.sub(r'(href|src)="\.\.\/assets', r'\1="/assets', article)
        article = re.sub(r'(href|src)="\.\.\/\.\.\/\.\.\/assets', r'\1="/assets', article)
        article = re.sub(r'href="\.\.\/\.\./vi/books/', 'href="/vi/books/', article)
        article = re.sub(r'href="\.\./vi/books/', 'href="/vi/books/', article)
        article = re.sub(r'href="vi/books/', 'href="/vi/books/', article)
        article = re.sub(r'href="books/', 'href="/vi/books/', article)
        article = re.sub(r'href="\.\./taichi/', 'href="/', article)
        article = re.sub(r'href="taichi/', 'href="/', article)
    else:
        article = ""
    return title_text, article


def detect_lang(content_sample):
    has_vi = bool(re.search(r'[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđĐ]', content_sample))
    return "vi" if has_vi else "en"


def page_shell(title, body, lang="en"):
    if lang == "en":
        home = "/en/"
        nav_items = [
            ("Home", home), ("Techniques", "/en/techniques/"),
            ("Articles", "/en/articles/"), ("Deep Dives", "/en/deep-dives/"),
            ("Practice Vault", "/en/practice-vault/"), ("Daoist", "/en/daoist/"),
            ("Life Skills", "/en/life-skills/"), ("Philosophy", "/en/philosophy/"),
            ("History", "/en/history/"), ("Contact", "/en/contact/"),
        ]
        lang_link = "/vi/"
        lang_label = "Tiếng Việt"
    else:
        home = "/vi/"
        nav_items = [
            ("Trang Chủ", home), ("Kỹ Thuật", "/vi/techniques/"),
            ("Bài Viết", "/vi/articles/"), ("Deep Dives", "/vi/deep-dives/"),
            ("Kho Luyện Tập", "/vi/practice-vault/"), ("Đạo Gia", "/vi/daoist/"),
            ("Kỹ Năng Sống", "/vi/life-skills/"), ("Triết Lý", "/vi/philosophy/"),
            ("Lịch Sử", "/vi/history/"), ("Liên Hệ", "/vi/contact/"),
        ]
        lang_link = "/en/"
        lang_label = "English"

    nav_html = "\n".join(f'    <a href="{href}">{label}</a>' for label, href in nav_items)
    back_label = "Back to Articles" if lang == "en" else "Quay lại Bài Viết"
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} - TaichiKB</title>
<link rel="icon" href="/assets/images/taiji-logo.svg" type="image/svg+xml">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Inter:wght@400;500;600&family=Noto+Serif+SC:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/stylesheets/yin-yang.css">
</head>
<body>

<header class="site-header">
    <a href="{home}" class="brand">{TAIJI}<span>TaichiKB</span></a>
    <nav class="site-nav">
{nav_html}
    <a href="{lang_link}" class="lang-switch">{lang_label}</a></nav>
</header>

<main>

<section class="hero">
    <span class="taiji-large">{TAIJI}</span>
    <h1>{title}</h1>
</section>

<article class="intranet-content" style="max-width: 880px; margin: 0 auto; padding: 2rem 1rem;">
{body}
</article>

<nav class="page-nav">
    <a href="{home}articles/">{back_label}</a>
    <a href="{home}" class="home">Home</a>
</nav>

</main>

<footer class="site-footer">
    <p>Trang web này được xây dựng với ❤️ cho cộng đồng Thái Cực Quyền Việt Nam {TAIJI} bởi Phạm Đức Hải</p>
    <p style="margin-top:1rem;">{TAIJI}</p>
</footer>

</body>
</html>
"""


def main():
    count = 0
    for html_file in REPO.rglob("*.html"):
        try:
            content = html_file.read_text(encoding="utf-8", errors="ignore")[:3000]
        except:
            continue
        if "mkdocs" not in content and "main.484c7ddc.min.css" not in content:
            continue
        rel = str(html_file.relative_to(REPO)).replace("\\\\", "/")
        if rel in ("404.html", "index_clean.html"):
            continue

        full_content = html_file.read_text(encoding="utf-8", errors="ignore")
        title, body = extract_mkdocs_content(full_content)
        if not body:
            continue

        lang = detect_lang(title + body[:2000])
        page = page_shell(title, body, lang=lang)
        html_file.write_text(page, encoding="utf-8")
        count += 1

    print(f"Reskinned {count} mkdocs files")


if __name__ == "__main__":
    main()
