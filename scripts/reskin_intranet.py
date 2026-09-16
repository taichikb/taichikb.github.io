#!/usr/bin/env python3
"""Re-skin intranet article HTML files with the Yin-Yang theme.

For each article in the source (D:/Taichi-Health-Finance/Intranet/deploy/articles/),
extract the <article class="article-body"> content and wrap it in the
Yin-Yang themed page shell.

Usage:
    python scripts/reskin_intranet.py
"""

import re
import sys
from pathlib import Path
from html import unescape

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_new_sections import page_shell, TAIJI

# Paths
INTRANET_ARTICLES = Path("D:/Taichi-Health-Finance/Intranet/deploy/articles")
INTRANET_DEEPDIVES = Path("D:/Taichi-Health-Finance/Intranet/deploy/deep-dives")
INTRANET_LIFESKILLS = Path("D:/Taichi-Health-Finance/Intranet/deploy/life-skills")
INTRANET_DAOIST = Path("D:/Taichi-Health-Finance/Intranet/deploy/daoist")
INTRANET_TAICHI = Path("D:/Taichi-Health-Finance/Intranet/deploy/tai-chi")
INTRANET_THAICUCQUYEN = Path("D:/Taichi-Health-Finance/Intranet/deploy/thai-cuc-quyen")
REPO = Path("D:/Taichi-Health-Finance/Intranet/taichikb_repo")


def extract_title(content):
    """Extract article title from <h1> in masthead or first <h1> in body."""
    m = re.search(r'<header class="masthead">\s*<div[^>]*>.*?</div>\s*<h1>([^<]+)</h1>', content, re.DOTALL)
    if m:
        return m.group(1).strip()
    m = re.search(r'<h1[^>]*>([^<]+)</h1>', content)
    if m:
        return m.group(1).strip()
    return "Untitled"


def extract_article_content(content):
    """Extract inner content of <article class="article-body">."""
    m = re.search(r'<article class="article-body">(.*?)</article>', content, re.DOTALL)
    if m:
        return m.group(1).strip()
    # Fallback: extract from <div class="md-content">
    m = re.search(r'<div class="md-content">(.*?)(?:</main>|<aside)', content, re.DOTALL)
    if m:
        return m.group(1).strip()
    # Fallback 2: extract <main>...</main> content
    m = re.search(r'<main[^>]*>(.*?)</main>', content, re.DOTALL)
    if m:
        return m.group(1).strip()
    return ""


def clean_content(content):
    """Clean intranet-specific patterns that don't fit the Yin-Yang theme."""
    # Remove the localhost badge at top
    content = re.sub(r'<div style="margin-bottom: 8px;">.*?</div>\s*', '', content, flags=re.DOTALL)

    # Remove article-meta-bar (we'll use our own header)
    content = re.sub(r'<div class="article-meta-bar">.*?</div>\s*', '', content, flags=re.DOTALL)

    # Remove the duplicate <h1> that already exists in article-header
    content = re.sub(r'<header class="article-header">.*?</header>\s*', '', content, flags=re.DOTALL)

    # Remove the topnav if present (we have our own header)
    content = re.sub(r'<nav class="topnav">.*?</nav>\s*', '', content, flags=re.DOTALL)

    # Remove masthead if present
    content = re.sub(r'<header class="masthead">.*?</header>\s*', '', content, flags=re.DOTALL)

    # Remove the section-title <h2> wrapper (we have our own hero)
    content = re.sub(r'<h2 class="section-title">[^<]+</h2>\s*', '', content)

    return content


def detect_lang(content):
    """Detect if content is primarily Vietnamese or English."""
    # Count Vietnamese diacritics
    vi_chars = len(re.findall(r'[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđĐ]', content))
    # Count Vietnamese-specific words
    vi_words = len(re.findall(r'\b(thái|cực|quyền|khí|công|thiền|đạo|pháp|tinh|thần|bài|tập|luyện|hơi|thở|nội|ngoại|năng|lượng)\b', content, re.IGNORECASE))
    total = len(content)
    return 'vi' if (vi_chars > 100 or vi_words > 20) else 'en'


def make_reskinned_html(title_en, content_html, lang="en", source_label=None):
    """Build a Yin-Yang-themed page with the article content."""
    # Build body
    body = f'''<section class="hero">
    <span class="taiji-large">{TAIJI}</span>
    <h1>{title_en}</h1>
    <p class="tagline">{("Sourced from the Taichi Health & Finance Intranet" if lang == "en" else "Nguồn từ Taichi Health & Finance Intranet")}</p>
</section>

<article class="intranet-content" style="max-width: 880px; margin: 0 auto; padding: 2rem 1rem;">
{content_html}
</article>

<nav class="page-nav">
    <a href="/{lang}/articles/">← {"Back to Articles" if lang == "en" else "Quay lại Bài Viết"}</a>
    <a href="/{lang}/" class="home">⌂ {"Home" if lang == "en" else "Trang Chủ"}</a>
</nav>'''
    return page_shell(
        lang,
        title_en,
        body,
        lang_switch_href=f"/{('vi' if lang == 'en' else 'en')}/articles/",
        other_label="🇻🇳 Tiếng Việt" if lang == "en" else "🇬🇧 English"
    )


def reskin_article(src_path, dest_lang_dir, slug, lang="en"):
    """Re-skin a single article."""
    content = src_path.read_text(encoding='utf-8', errors='ignore')

    title = extract_title(content)
    article_content = extract_article_content(content)
    article_content = clean_content(article_content)

    if not article_content:
        print(f"  SKIP {slug}: no content extracted")
        return False

    full_html = make_reskinned_html(title, article_content, lang=lang)

    out_path = REPO / dest_lang_dir / slug / "index.html"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(full_html, encoding='utf-8')
    print(f"  built {dest_lang_dir}/{slug}/  ({len(article_content)} bytes content)")
    return True


def reskin_directory(src_dir, dest_lang, dest_slug, recursive=False):
    """Re-skin all articles in a source directory."""
    if not src_dir.exists():
        return 0
    count = 0
    for article_dir in sorted(src_dir.iterdir()):
        if not article_dir.is_dir():
            continue
        # Check both the dir itself and any subdirectory for index.html
        index_path = article_dir / "index.html"
        if not index_path.exists() and recursive:
            # Look one level deeper
            for sub in article_dir.iterdir():
                if sub.is_dir() and (sub / "index.html").exists():
                    index_path = sub / "index.html"
                    break
        if not index_path.exists():
            continue
        # Use the directory name as the slug
        slug = article_dir.name
        if reskin_article(index_path, dest_lang, slug, lang=dest_lang):
            count += 1
    return count


# Articles in each language (these are VI-native article directories)
VI_ARTICLE_DIRS = [
    "01_taichi_qigong_10_notes",
    "02_health_tcm_energy_10_notes",
    "03_tuoi_52_tu_tap_noi_tai_10_notes",
    "04_minimalism_essentialism_10_notes",
    "05_self_help_practical_wisdom_10_notes",
    "06_coaching_deliberate_practice_10_notes",
    "07_psychology_philosophy_10_notes",
    "08_hanh_trinh_thuc_tinh_tam_linh_10_notes",
    "09_artifacts_audio_video_overview",
    "10-triet-ly-can-ban-cua-nguoi-nhat",
    "ban-chat-cua-qua-trinh-thu-gom-thong-tin-co-hoc-va-tri-tue-dich-thuc",
    "ban-chat-cua-qua-trinh-thu-gom-thong-tin-co-hoc-va-tri-tue-đich-thuc",
    "cach-hieu-va-song-thuan-theo-tu-nhien",
    "cach-tho",
    "complete-taichi-practice-guide-for-the-30-beginner",
    "deep-dives-readme",
    "essentialism_mindset_personal_finance",
    "gemini_notebooks_catalog_and_grounded_notes",
    "hoc-cach-song-nhe-nhang-sau-tuoi-nam-muoi",
    "long-tham-va-nhu-cau-hoc-hoi-chan-chinh",
    "phan-tich-tam-ly",
]


def main():
    print("=" * 60)
    print("RE-SKIN INTRANET ARTICLES WITH YIN-YANG THEME")
    print("=" * 60)

    total = 0

    # Process all articles in deploy/articles/ — copy to vi/articles/
    print("\n[1] Articles → vi/articles/")
    if INTRANET_ARTICLES.exists():
        for article_dir in sorted(INTRANET_ARTICLES.iterdir()):
            if not article_dir.is_dir():
                continue
            index_path = article_dir / "index.html"
            if not index_path.exists():
                continue
            slug = article_dir.name
            # Skip non-article directories
            if slug in ("index.html",):
                continue
            if reskin_article(index_path, "vi/articles", slug, lang="vi"):
                total += 1

    # Deep Dives
    print("\n[2] Deep Dives → en/deep-dives/ and vi/deep-dives/")
    if INTRANET_DEEPDIVES.exists():
        for article_dir in sorted(INTRANET_DEEPDIVES.iterdir()):
            if not article_dir.is_dir():
                continue
            slug = article_dir.name
            # Check dir itself first, then look one level deeper
            index_path = article_dir / "index.html"
            if not index_path.exists():
                for sub in article_dir.iterdir():
                    if sub.is_dir() and (sub / "index.html").exists():
                        index_path = sub / "index.html"
                        break
            if not index_path.exists():
                continue
            # Detect language
            content = index_path.read_text(encoding='utf-8', errors='ignore')
            lang = detect_lang(content)
            target_lang = "vi" if lang == "vi" else "en"
            target_dir = f"{target_lang}/deep-dives"
            if reskin_article(index_path, target_dir, slug, lang=target_lang):
                total += 1

    # Life Skills
    print("\n[3] Life Skills → vi/life-skills/")
    if INTRANET_LIFESKILLS.exists():
        for article_dir in sorted(INTRANET_LIFESKILLS.iterdir()):
            if not article_dir.is_dir():
                continue
            slug = article_dir.name
            index_path = article_dir / "index.html"
            if not index_path.exists():
                for sub in article_dir.iterdir():
                    if sub.is_dir() and (sub / "index.html").exists():
                        index_path = sub / "index.html"
                        break
            if not index_path.exists():
                continue
            if reskin_article(index_path, "vi/life-skills", slug, lang="vi"):
                total += 1

    # Daoist
    print("\n[4] Daoist → vi/daoist/")
    if INTRANET_DAOIST.exists():
        for article_dir in sorted(INTRANET_DAOIST.iterdir()):
            if not article_dir.is_dir():
                continue
            slug = article_dir.name
            index_path = article_dir / "index.html"
            if not index_path.exists():
                for sub in article_dir.iterdir():
                    if sub.is_dir() and (sub / "index.html").exists():
                        index_path = sub / "index.html"
                        break
            if not index_path.exists():
                continue
            if reskin_article(index_path, "vi/daoist", slug, lang="vi"):
                total += 1

    # Tai-chi / Thai-cuc-quyen — share content but render in both languages
    print("\n[5] Tai Chi / Thái Cực Quyền → vi/thai-cuc-quyen/ and en/tai-chi/")
    for src_dir, target_en, target_vi in [
        (INTRANET_TAICHI, "en/tai-chi", "vi/tai-chi"),
        (INTRANET_THAICUCQUYEN, "en/thai-cuc-quyen", "vi/thai-cuc-quyen"),
    ]:
        if not src_dir.exists():
            continue
        for article_dir in sorted(src_dir.iterdir()):
            if not article_dir.is_dir():
                continue
            slug = article_dir.name
            index_path = article_dir / "index.html"
            if not index_path.exists():
                for sub in article_dir.iterdir():
                    if sub.is_dir() and (sub / "index.html").exists():
                        index_path = sub / "index.html"
                        break
            if not index_path.exists():
                continue
            content = index_path.read_text(encoding='utf-8', errors='ignore')
            lang = detect_lang(content)
            # Pick target directory based on detected language
            target = target_vi if lang == "vi" else target_en
            target_lang = "vi" if lang == "vi" else "en"
            if reskin_article(index_path, target, slug, lang=target_lang):
                total += 1

    print(f"\n=== Total: {total} articles re-skinned ===")


if __name__ == "__main__":
    main()
