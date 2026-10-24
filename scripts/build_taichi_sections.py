#!/usr/bin/env python3
"""Build Tai Chi / Thái Cực Quyền landing pages for both languages."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_new_sections import page_shell, make_section, make_card, make_page_header, TAIJI

REPO = Path("D:/Taichi-Health-Finance/Intranet/taichikb_repo")

TAICHI_EN = {
    "title_en": "Tai Chi (English Library)",
    "subtitle_en": "The full bilingual collection — Chen style, Baguazhang, Hsing Yi, Qi Gong, and the deeper arts",
    "sections": [
        ("Chen Style & Yang Style", [
            ("Chen Style", "Chen Style Tai Chi Chuan — The Source", "The original village tradition, source of all modern styles.", "/tai-chi/chen-style-taichi/"),
            ("Yang Style", "Advanced Yang Style Tai Chi Chuan", "The most widely practiced modern style.", "/tai-chi/advance-yang-style-tai-chi-chuan/"),
            ("Source", "Chen Style Taijiquan — The Source of Taiji Boxing", "Deep analysis of the Chen lineage as the root.", "/tai-chi/chen-style-taijiquan-the-source-of-taiji-boxing/"),
            ("Chen Forms", "Chen Style Taijiquan — Forms & Applications", "Forms and applications of the Chen tradition.", "/tai-chi/chen-style-taijiquan/"),
        ]),
        ("Internal Arts & Energy", [
            ("Silk Reeling", "Developing Jin — Silk Reeling Power in Tai Chi", "The foundational spiral of internal power.", "/tai-chi/developing-jin-silk-reeling-power-in-tai-chi-and-the-internal-martial-arts/"),
            ("Body Mechanics", "Body Mechanics of Tai Chi Chuan", "How the body moves correctly — joint sequencing, weight transfer.", "/tai-chi/body-mechanics-of-tai-chi-chuan/"),
            ("Beginners", "Beginners' Tai Chi Chuan", "The entry point — first steps into the practice.", "/tai-chi/beginners-tai-chi-chuan/"),
            ("Baguazhang", "Baguazhang — Eight Trigrams Palm", "The sister internal art — circle walking, palm changes.", "/tai-chi/bat-quai-quyen/"),
            ("Hình-Y Quyền", "Hình-Y Quyền — Form-Y Boxing", "A Vietnamese internal boxing tradition.", "/tai-chi/hinh-y-quyen/"),
            ("Healing", "Healing Bodies, Healing Hearts — Qigong & Tai Chi", "Therapeutic applications for body and mind.", "/tai-chi/healing-bodies-healing-hearts-with-qigong-and-tai-chi-chuan/"),
        ]),
    ],
}

TAICHI_VI = {
    "title_vi": "Thái Cực Quyền (Thư Viện Tiếng Việt)",
    "subtitle_vi": "Bộ sưu tập song ngữ đầy đủ — Trần phái, Bát Quái, Hình Ý, Khí Công và các nghệ thuật sâu hơn",
    "sections": [
        ("Trần Phái & Dương Phái", [
            ("Trần Phái", "Trần Thức Thái Cực Quyền — Nguồn Cội", "Truyền thống làng gốc, nguồn của mọi phong cách hiện đại.", "/thai-cuc-quyen/chen-style-taichi/"),
            ("Dương Phái", "Thái Cực Quyền Dương Phái Nâng Cao", "Phong cách hiện đại được luyện tập rộng rãi nhất.", "/thai-cuc-quyen/advance-yang-style-tai-chi-chuan/"),
            ("Nguồn", "Trần Thức Thái Cực Quyền — Nguồn Cội Thái Cực Quyền", "Phân tích sâu dòng Trần là gốc.", "/thai-cuc-quyen/chen-style-taijiquan-the-source-of-taiji-boxing/"),
            ("Bài Trần", "Trần Thức Thái Cực Quyền — Bài Quyền & Ứng Dụng", "Bài quyền và ứng dụng của truyền thống Trần.", "/thai-cuc-quyen/chen-style-taijiquan/"),
        ]),
        ("Nghệ Thuật Nội Tâm & Năng Lượng", [
            ("Xoắn Tơ", "Phát Triển Jin — Lực Xoắn Tơ Trong Thái Cực", "Xoắn ốc nền tảng của lực nội tại.", "/thai-cuc-quyen/developing-jin-silk-reeling-power-in-tai-chi-and-the-internal-martial-arts/"),
            ("Cơ Học Cơ Thể", "Cơ Học Cơ Thể Thái Cực Quyền", "Cách cơ thể di chuyển đúng — trình tự khớp, chuyển trọng lượng.", "/thai-cuc-quyen/body-mechanics-of-tai-chi-chuan/"),
            ("Người Mới", "Thái Cực Quyền Cho Người Mới Bắt Đầu", "Điểm vào — bước đầu tiên vào thực hành.", "/thai-cuc-quyen/beginners-tai-chi-chuan/"),
            ("Bát Quái", "Bát Quái Quyền — Chưởng Bát Quái", "Nghệ thuật nội tâm chị em — đi vòng, biến chưởng.", "/thai-cuc-quyen/bat-quai-quyen/"),
            ("Hình Ý Quyền", "Hình Ý Quyền — Quyền Hình Y", "Truyền thống quyền nội tâm Việt Nam.", "/thai-cuc-quyen/hinh-y-quyen/"),
            ("Chữa Lành", "Chữa Lành Thân Thể, Chữa Lành Tâm Hồn — Khí Công & Thái Cực Quyền", "Ứng dụng trị liệu cho thân và tâm.", "/thai-cuc-quyen/healing-bodies-healing-hearts-with-qigong-and-tai-chi-chuan/"),
        ]),
    ],
}


def write_page(slug, lang, config):
    """Write EN or VI landing page."""
    out_dir = REPO / lang / slug
    out_dir.mkdir(parents=True, exist_ok=True)

    body = make_page_header(
        config.get("title_en", config.get("title_vi")),
        config.get("subtitle_en", config.get("subtitle_vi"))
    )
    for section_title, cards in config["sections"]:
        cards_html = "\n".join(make_card(*c) for c in cards)
        body += make_section(section_title, cards_html)

    if lang == "en":
        page = page_shell("en", config["title_en"], body, f"/vi/{slug}/", "🇻🇳 Tiếng Việt")
    else:
        page = page_shell("vi", config["title_vi"], body, f"/en/{slug}/", "🇬🇧 English")

    (out_dir / "index.html").write_text(page, encoding='utf-8')
    print(f"  built {lang}/{slug}/index.html")


def main():
    print("--- Building tai-chi/ and thai-cuc-quyen/ landing pages ---")
    write_page("tai-chi", "en", TAICHI_EN)
    write_page("tai-chi", "vi", TAICHI_VI)
    write_page("thai-cuc-quyen", "en", TAICHI_EN)  # share EN content
    write_page("thai-cuc-quyen", "vi", TAICHI_VI)
    print("--- Done ---")


if __name__ == "__main__":
    main()
