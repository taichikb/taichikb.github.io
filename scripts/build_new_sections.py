#!/usr/bin/env python3
"""Generate Yin-Yang-themed landing pages for new sections in taichikb_repo.

Sections to integrate from local intranet:
- articles/ (Knowledge Base / Cơ Sở Tri Thức)
- deep-dives/
- practice-vault/
- life-skills/
- daoist/
- tai-chi/ / thai-cuc-quyen/

Each section gets:
- en/<section>/index.html
- vi/<section>/index.html

Plus update main index pages en/index.html and vi/index.html to link to new sections.
"""

from pathlib import Path
import sys

REPO = Path("D:/Taichi-Health-Finance/Intranet/taichikb_repo")

TAIJI = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="20" height="20" style="vertical-align:-3px;display:inline-block;"><circle cx="100" cy="100" r="98" fill="#ffffff" stroke="#000000" stroke-width="4"/><path d="M 100,2 A 98,98 0 0,1 100,198 A 49,49 0 0,1 100,100 A 49,49 0 0,0 100,2 Z" fill="#000000"/><circle cx="100" cy="51" r="12" fill="#ffffff"/><circle cx="100" cy="149" r="12" fill="#000000"/></svg>'

def page_shell(lang, title, body_content, lang_switch_href, other_label):
    """Build a full Yin-Yang-themed page with header, body, footer."""
    nav = []
    if lang == "en":
        nav = [
            ("Home", "/en/", False),
            ("Techniques", "/en/techniques/", False),
            ("Articles", "/en/articles/", False),
            ("Deep Dives", "/en/deep-dives/", False),
            ("Practice Vault", "/en/practice-vault/", False),
            ("Daoist", "/en/daoist/", False),
            ("Life Skills", "/en/life-skills/", False),
            ("Philosophy", "/en/philosophy/", False),
            ("History", "/en/history/", False),
            ("Contact", "/en/contact/", False),
        ]
    else:
        nav = [
            ("Trang Chủ", "/vi/", False),
            ("Kỹ Thuật", "/vi/techniques/", False),
            ("Bài Viết", "/vi/articles/", False),
            ("Deep Dives", "/vi/deep-dives/", False),
            ("Kho Luyện Tập", "/vi/practice-vault/", False),
            ("Đạo Gia", "/vi/daoist/", False),
            ("Kỹ Năng Sống", "/vi/life-skills/", False),
            ("Triết Lý", "/vi/philosophy/", False),
            ("Lịch Sử", "/vi/history/", False),
            ("Liên Hệ", "/vi/contact/", False),
        ]
    nav_html = "\n".join(
        f'    <a href="{href}" class="">{label}</a>' for label, href, active in nav
    )

    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} — TaichiKB</title>
<link rel="icon" href="/assets/images/taiji-logo.svg" type="image/svg+xml">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Inter:wght@400;500;600&family=Noto+Serif+SC:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/stylesheets/yin-yang.css">
</head>
<body>

<header class="site-header">
    <a href="/{lang}/" class="brand">{TAIJI}<span>TaichiKB</span></a>
    <nav class="site-nav">
{nav_html}
    <a href="{lang_switch_href}" class="lang-switch">{other_label}</a></nav>
</header>

<main>

{body_content}

</main>

<footer class="site-footer">
    <p>Built with ❤️ for the Vietnamese Tai Chi community {TAIJI} bởi Phạm Đức Hải</p>
    <p>Trang web này được xây dựng với ❤️ cho cộng đồng Thái Cực Quyền Việt Nam {TAIJI} bởi Phạm Đức Hải</p>
    <p style="margin-top:1rem;">{TAIJI}</p>
</footer>

</body>
</html>
'''


def make_card(meta, title, desc, href):
    return f'''        <a href="{href}" class="card">
            <span class="card-meta">{meta}</span>
            <h3>{title}</h3>
            <p>{desc}</p>
        </a>'''


def make_section(title, cards_html):
    return f'''<section class="section">
    <div class="section-title"><h2>{title}</h2></div>
    <div class="card-grid">
{cards_html}
    </div>
</section>
'''


def make_page_header(title, subtitle):
    return f'''<section class="hero">
    <span class="taiji-large">{TAIJI}</span>
    <h1>{title}</h1>
    <p class="tagline">{subtitle}</p>
</section>
'''


def write_section_pages(section_slug, en_config, vi_config):
    """Write both EN and VI landing pages for a section."""
    en_dir = REPO / "en" / section_slug
    vi_dir = REPO / "vi" / section_slug
    en_dir.mkdir(parents=True, exist_ok=True)
    vi_dir.mkdir(parents=True, exist_ok=True)

    # EN page
    en_body = make_page_header(en_config["title_en"], en_config["subtitle_en"])
    for section_title, cards in en_config["sections"]:
        cards_html = "\n".join(make_card(*c) for c in cards)
        en_body += make_section(section_title, cards_html)
    (en_dir / "index.html").write_text(
        page_shell("en", en_config["title_en"], en_body, "/vi/" + section_slug + "/", "🇻🇳 Tiếng Việt"),
        encoding='utf-8'
    )

    # VI page
    vi_body = make_page_header(vi_config["title_vi"], vi_config["subtitle_vi"])
    for section_title, cards in vi_config["sections"]:
        cards_html = "\n".join(make_card(*c) for c in cards)
        vi_body += make_section(section_title, cards_html)
    (vi_dir / "index.html").write_text(
        page_shell("vi", vi_config["title_vi"], vi_body, "/en/" + section_slug + "/", "🇬🇧 English"),
        encoding='utf-8'
    )

    print(f"  built {section_slug}/ (EN+VI)")


# ============================================================================
# Define content for each new section
# ============================================================================

ARTICLES_EN = {
    "title_en": "Knowledge Base",
    "subtitle_en": "Articles · Notes · Catalogs · Research — sourced from the Taichi Health & Finance Intranet",
    "sections": [
        ("Practice Collections · 10-Notes Series", [
            ("Taichi · Qigong", "10 Notes: Tai Chi, Qigong & Fascia Biology", "Core notes on the Chen style lineage, qigong principles, and connective tissue science.", "/articles/01_taichi_qigong_10_notes/"),
            ("Health · TCM", "10 Notes: Traditional Chinese Medicine & Self-Healing", "Meridians, energy flow, and the TCM framework applied to modern practice.", "/articles/02_health_tcm_energy_10_notes/"),
            ("50+ Journey", "10 Notes: Age 52 — Inner Practice & Life Wisdom", "A personal journey through the inner arts after fifty.", "/articles/03_tuoi_52_tu_tap_noi_tai_10_notes/"),
            ("Minimalism", "10 Notes: Essentialism & Financial Minimalism", "Tối giản tài chính và thiết yếu — applied to life design.", "/articles/04_minimalism_essentialism_10_notes/"),
            ("Self-Help", "10 Notes: Self-Help & Practical Wisdom", "Trí tuệ thực hành cho đời sống.", "/articles/05_self_help_practical_wisdom_10_notes/"),
            ("Coaching", "10 Notes: Coaching & Deliberate Practice", "Luyện tập có chủ đích — the Anders Ericsson tradition.", "/articles/06_coaching_deliberate_practice_10_notes/"),
            ("Psychology", "10 Notes: Behavioral Psychology & Life Philosophy", "Triết học đời sống từ tâm lý học hành vi.", "/articles/07_psychology_philosophy_10_notes/"),
            ("Spiritual", "10 Notes: Awakening & Integral Spirituality", "Hành trình thức tỉnh & khoa học tâm linh toàn diện.", "/articles/08_hanh_trinh_thuc_tinh_tam_linh_10_notes/"),
            ("Audio · Video", "Tổng Hợp Audio & Video Overviews", "NotebookLM-generated overviews across all collections.", "/articles/09_artifacts_audio_video_overview/"),
            ("Japanese Philosophy", "10 Triết Lý Căn Bản Của Người Nhật", "10 foundational philosophies of the Japanese people — Bushido, wabi-sabi, ikigai.", "/articles/10-triet-ly-can-ban-cua-nguoi-nhat/"),
        ]),
        ("Foundational Catalogs", [
            ("Catalog", "Toàn Thư 32 Kho Tri Thức Gemini NotebookLM", "32 knowledge vaults — the complete Gemini-NotebookLM catalog and ecosystem.", "/articles/gemini_notebooks_catalog_and_grounded_notes/"),
            ("Practice Guide", "The Complete Taichi Practice Guide for the 3.0 Beginner", "Full bilingual guide to starting practice from zero — the foundational curriculum.", "/articles/complete-taichi-practice-guide-for-the-30-beginner/"),
            ("Mindset", "Essentialism, Deliberate Practice & Personal Finance", "The mindset trilogy for Tai Chi practitioners and life builders.", "/articles/essentialism_mindset_personal_finance/"),
            ("Wiki Bundle", "Taichi Wiki — Portable Bundle & Push Instructions", "The portable bundle structure for syncing across devices.", "/articles/push_instructions_taichi_wiki/"),
        ]),
        ("Standalone Articles", [
            ("Philosophy", "Bản Chất Của Quá Trình Thu Gom Thông Tin Cơ Học Và Trí Tuệ Đích Thực", "Mechanical information collection vs. true wisdom — the essential difference.", "/articles/ban-chat-cua-qua-trinh-thu-gom-thong-tin-co-hoc-va-tri-tue-dich-thuc/"),
            ("Living", "Cách Hiểu Và Sống Thuận Theo Tự Nhiên", "How to understand and live in accordance with nature — Daoist naturalness.", "/articles/cach-hieu-va-song-thuan-theo-tu-nhien/"),
            ("Breath", "Cách Thở", "On breathing — the foundation of all internal practice.", "/articles/cach-tho/"),
            ("Aging", "Học Cách Sống Nhẹ Nhàng Sau Tuổi Năm Mươi", "Learning to live gently after fifty — a Tai Chi approach to aging.", "/articles/hoc-cach-song-nhe-nhang-sau-tuoi-nam-muoi/"),
            ("Learning", "Lòng Tham Và Nhu Cầu Học Hỏi Chân Chính", "Greed vs. genuine learning need — distinguishing the two.", "/articles/long-tham-va-nhu-cau-hoc-hoi-chan-chinh/"),
            ("Analysis", "Phân Tích Tâm Lý", "Psychological analysis through the lens of internal practice.", "/articles/phan-tich-tam-ly/"),
        ]),
    ],
}

ARTICLES_VI = {
    "title_vi": "Cơ Sở Tri Thức",
    "subtitle_vi": "Bài Viết · Ghi Chú · Danh Mục · Nghiên Cứu — từ Taichi Health & Finance Intranet",
    "sections": [
        ("Bộ Sưu Tập Thực Hành · Chuỗi 10-Ghi-Chú", [
            ("Thái Cực · Khí Công", "10 Ghi Chú: Thái Cực Quyền, Khí Công & Cơ Sinh Học Cân Mạc", "Ghi chú cốt tủy về dòng Trần Thức, nguyên lý khí công, và khoa học mô liên kết.", "/articles/01_taichi_qigong_10_notes/"),
            ("Sức Khỏe · Y Học Cổ Truyền", "10 Ghi Chú: Y Học Cổ Truyền (TCM), Kinh Lạc & Năng Lượng Tự Chữa Lành", "Kinh lạc, lưu thông khí, và khung TCM áp dụng vào thực hành hiện đại.", "/articles/02_health_tcm_energy_10_notes/"),
            ("Hành Trình 50+", "10 Ghi Chú: Tuổi 52 — Hành Trình Tu Tập Nội Tại & Trí Tuệ Sống", "Hành trình cá nhân qua các nghệ thuật nội tại sau năm mươi.", "/articles/03_tuoi_52_tu_tap_noi_tai_10_notes/"),
            ("Tối Giản", "10 Ghi Chú: Chủ Nghĩa Thiết Yếu & Tối Giản Tài Chính", "Áp dụng cho thiết kế cuộc sống.", "/articles/04_minimalism_essentialism_10_notes/"),
            ("Tự Lực", "10 Ghi Chú: Tự Lực & Trí Tuệ Thực Hành Đời Sống", "Trí tuệ thực hành cho cuộc sống hàng ngày.", "/articles/05_self_help_practical_wisdom_10_notes/"),
            ("Huấn Luyện", "10 Ghi Chú: Huấn Luyện & Luyện Tập Có Chủ Đích", "Luyện tập có chủ đích — truyền thống Anders Ericsson.", "/articles/06_coaching_deliberate_practice_10_notes/"),
            ("Tâm Lý Học", "10 Ghi Chú: Tâm Lý Học Hành Vi & Triết Học Đời Sống", "Triết học sống qua lăng kính tâm lý học hành vi.", "/articles/07_psychology_philosophy_10_notes/"),
            ("Tâm Linh", "10 Ghi Chú: Hành Trình Thức Tỉnh & Khoa Học Tâm Linh Toàn Diện", "Khoa học tâm linh toàn diện và con đường thức tỉnh.", "/articles/08_hanh_trinh_thuc_tinh_tam_linh_10_notes/"),
            ("Audio · Video", "Tổng Hợp Tài Nguyên NotebookLM — Audio & Video", "Tổng quan do NotebookLM tạo ra xuyên suốt các bộ sưu tập.", "/articles/09_artifacts_audio_video_overview/"),
            ("Triết Lý Nhật Bản", "10 Triết Lý Căn Bản Của Người Nhật", "Mười triết lý nền tảng: Bushido, wabi-sabi, ikigai, và hơn thế nữa.", "/articles/10-triet-ly-can-ban-cua-nguoi-nhat/"),
        ]),
        ("Danh Mục Nền Tảng", [
            ("Danh Mục", "Toàn Thư 32 Kho Tri Thức Gemini NotebookLM", "32 kho tri thức — danh mục đầy đủ và hệ sinh thái.", "/articles/gemini_notebooks_catalog_and_grounded_notes/"),
            ("Cẩm Nang", "Cẩm Nang Tập Thái Cực Quyền Toàn Tập Cho Người Mới Bắt Đầu", "Cẩm nang song ngữ đầy đủ để bắt đầu từ số không — chương trình nền tảng.", "/articles/complete-taichi-practice-guide-for-the-30-beginner/"),
            ("Tư Duy", "Triết Lý Tối Giản, Luyện Tập Có Chủ Đích & Quản Trị Tài Chính Cá Nhân", "Bộ ba tư duy cho người luyện Thái Cực và người xây dựng cuộc sống.", "/articles/essentialism_mindset_personal_finance/"),
            ("Wiki Bundle", "Taichi Wiki — Portable Bundle & Push Instructions", "Cấu trúc gói di động để đồng bộ giữa các thiết bị.", "/articles/push_instructions_taichi_wiki/"),
        ]),
        ("Bài Viết Độc Lập", [
            ("Triết Lý", "Bản Chất Của Quá Trình Thu Gom Thông Tin Cơ Học Và Trí Tuệ Đích Thực", "Thu gom thông tin cơ học vs. trí tuệ đích thực — sự khác biệt cốt tủy.", "/articles/ban-chat-cua-qua-trinh-thu-gom-thong-tin-co-hoc-va-tri-tue-dich-thuc/"),
            ("Sống", "Cách Hiểu Và Sống Thuận Theo Tự Nhiên", "Hiểu và sống thuận theo tự nhiên — chất tự nhiên của Đạo.", "/articles/cach-hieu-va-song-thuan-theo-tu-nhien/"),
            ("Hơi Thở", "Cách Thở", "Về hơi thở — nền tảng của mọi thực hành nội tại.", "/articles/cach-tho/"),
            ("Lão Hóa", "Học Cách Sống Nhẹ Nhàng Sau Tuổi Năm Mươi", "Học cách sống nhẹ nhàng sau tuổi năm mươi — cách tiếp cận Thái Cực với lão hóa.", "/articles/hoc-cach-song-nhe-nhang-sau-tuoi-nam-muoi/"),
            ("Học Hỏi", "Lòng Tham Và Nhu Cầu Học Hỏi Chân Chính", "Lòng tham vs. nhu cầu học hỏi chân chính — phân biệt hai.", "/articles/long-tham-va-nhu-cau-hoc-hoi-chan-chinh/"),
            ("Phân Tích", "Phân Tích Tâm Lý", "Phân tích tâm lý qua lăng kính thực hành nội tại.", "/articles/phan-tich-tam-ly/"),
        ]),
    ],
}

DEEPDIVES_EN = {
    "title_en": "Deep Dives",
    "subtitle_en": "Long-form, in-depth explorations of the practice — form analysis, foundational philosophy, health research",
    "sections": [
        ("Form Analysis", [
            ("24-Form", "The 24-Form Deep Dive", "A complete analysis of every movement of the simplified 24-form sequence.", "/deep-dives/24-form/"),
            ("8-Gates", "The Eight Gates (Bā Mén)", "The eight power expressions — Peng, Lu, Ji, An, Cai, Lie, Zhou, Kao.", "/deep-dives/8-gates/"),
            ("Foundations", "Foundational Concepts", "Wuji, Taiji, Yin-Yang, Bagua — the generative chain.", "/deep-dives/foundations/"),
        ]),
        ("Practice & Health", [
            ("Practice Guide", "The Complete Practice Guide for the 3.0 Beginner", "Full-length curriculum from the 3.0 beginner through integration.", "/deep-dives/complete-practice-guide/"),
            ("Health", "Health & Longevity", "Clinical research on Tai Chi for the 50+ body, fall prevention, blood pressure, cognitive function.", "/deep-dives/health-longevity/"),
        ]),
    ],
}

DEEPDIVES_VI = {
    "title_vi": "Deep Dives",
    "subtitle_vi": "Khám phá chuyên sâu, dài hơi về thực hành — phân tích bài, triết lý nền tảng, nghiên cứu sức khỏe",
    "sections": [
        ("Phân Tích Bài Quyền", [
            ("24 Dạng", "Phân Tích Chuyên Sâu 24 Dạng", "Phân tích hoàn chỉnh mỗi chuyển động của chuỗi 24 dạng đơn giản.", "/deep-dives/24-form/"),
            ("Bát Môn", "Bát Môn (八門)", "Tám biểu hiện lực — Phòng, Lữ, Tỳ, Án, Thái, Liệt, Chủu, Khảo.", "/deep-dives/8-gates/"),
            ("Nền Tảng", "Khái Niệm Nền Tảng", "Vô Cực, Thái Cực, Âm Dương, Bát Quái — chuỗi sinh.", "/deep-dives/foundations/"),
        ]),
        ("Thực Hành & Sức Khỏe", [
            ("Cẩm Nang", "Cẩm Nang Tập Toàn Tập Cho Người Mới 3.0", "Chương trình dài hạn từ người mới 3.0 đến tích hợp.", "/deep-dives/complete-practice-guide/"),
            ("Sức Khỏe", "Sức Khỏe & Trường Thọ", "Nghiên cứu lâm sàng về Thái Cực cho cơ thể 50+, phòng ngừa té ngã, huyết áp, chức năng nhận thức.", "/deep-dives/health-longevity/"),
        ]),
    ],
}

PRACTICEVAULT_EN = {
    "title_en": "Practice Vault",
    "subtitle_en": "Audio, video, cheat sheets, research — the practitioner's working library",
    "sections": [
        ("Working Library", [
            ("Audio", "Audio Resources", "Guided meditations, form walk-throughs, breathwork audio.", "/practice-vault/audio/"),
            ("Video", "Video Resources", "Movement demonstrations, partner drills, push-hands examples.", "/practice-vault/video/"),
            ("Forms", "Forms Library", "24-form, 48-form, 88-form — different lengths and styles.", "/practice-vault/forms/"),
        ]),
        ("Reference", [
            ("Cheat Sheet", "Print Cheat Sheet", "Printable one-page reference of Eight Methods, Five Steps, core cues.", "/practice-vault/print-cheat-sheet/"),
            ("Local Classes", "Local Classes Directory", "Find a teacher near you — directory of certified instructors.", "/practice-vault/local-classes/"),
            ("Research", "Research & Science", "Peer-reviewed studies on Tai Chi's physiological and psychological effects.", "/practice-vault/research-science/"),
        ]),
    ],
}

PRACTICEVAULT_VI = {
    "title_vi": "Kho Luyện Tập",
    "subtitle_vi": "Audio, video, cheat sheet, nghiên cứu — thư viện làm việc của người luyện tập",
    "sections": [
        ("Thư Viện Làm Việc", [
            ("Audio", "Tài Nguyên Âm Thanh", "Thiền có hướng dẫn, đi qua bài, hơi thở công.", "/practice-vault/audio/"),
            ("Video", "Tài Nguyên Video", "Biểu diễn chuyển động, bài tập đối tác, ví dụ thôi thủ.", "/practice-vault/video/"),
            ("Bài Quyền", "Thư Viện Bài Quyền", "24 dạng, 48 dạng, 88 dạng — các độ dài và phong cách khác nhau.", "/practice-vault/forms/"),
        ]),
        ("Tham Khảo", [
            ("Cheat Sheet", "Cheat Sheet In Được", "Một trang tham khảo Bát Pháp, Ngũ Bộ, câu nhắc cốt lõi.", "/practice-vault/print-cheat-sheet/"),
            ("Lớp Học Địa Phương", "Danh Bạ Lớp Học Địa Phương", "Tìm giáo viên gần bạn — danh bạ giáo viên chứng nhận.", "/practice-vault/local-classes/"),
            ("Nghiên Cứu", "Nghiên Cứu & Khoa Học", "Nghiên cứu bình duyệt về tác động sinh lý và tâm lý của Thái Cực.", "/practice-vault/research-science/"),
        ]),
    ],
}

LIFESKILLS_EN = {
    "title_en": "Life Skills",
    "subtitle_en": "Mindset, learning, self-inquiry — the wisdom traditions applied to modern living",
    "sections": [
        ("Mindset & Practice", [
            ("Living", "Học Cách Sống Nhẹ Nhàng Sau Tuổi Năm Mươi", "Learning to live gently after fifty.", "/life-skills/h-c-c-ch-s-ng-nh-nh-ng-sau-tu-i-n-m-m-i/"),
            ("Audio Overview", "Life Skills Audio Overview", "Audio synthesis of the life skills series.", "/life-skills/audio-overview/"),
            ("Nature", "Cách Hiểu Và Sống Thuận Theo Tự Nhiên", "Living according to nature.", "/life-skills/c-ch-hi-u-v-s-ng-thu-n-theo-t-nhi-n/"),
        ]),
        ("Inquiry & Analysis", [
            ("Information", "Bản Chất Quá Trình Thu Gom Thông Tin", "The nature of information collection.", "/life-skills/b-n-ch-t-c-a-qu-tr-nh-thu-gom-th-ng-tin-c-h-c-v-tr-tu-ch-th-c/"),
            ("Breath", "Cách Thở", "On breathing.", "/life-skills/c-ch-th/"),
            ("Greed", "Lòng Tham Và Nhu Cầu Học Hỏi Chân Chính", "Greed vs. genuine learning.", "/life-skills/l-ng-tham-v-nhu-c-u-h-c-h-i-ch-n-ch-nh/"),
            ("Psychology", "Phân Tích Tâm Lý", "Psychological analysis.", "/life-skills/ph-n-t-ch-t-m-l/"),
        ]),
    ],
}

LIFESKILLS_VI = {
    "title_vi": "Kỹ Năng Sống",
    "subtitle_vi": "Tư duy, học hỏi, tự vấn — truyền thống trí tuệ áp dụng cho sống hiện đại",
    "sections": [
        ("Tư Duy & Thực Hành", [
            ("Sống", "Học Cách Sống Nhẹ Nhàng Sau Tuổi Năm Mươi", "Học sống nhẹ nhàng sau tuổi 50.", "/life-skills/h-c-c-ch-s-ng-nh-nh-ng-sau-tu-i-n-m-m-i/"),
            ("Audio Tổng Quan", "Audio Tổng Quan Kỹ Năng Sống", "Tổng hợp âm thanh của chuỗi kỹ năng sống.", "/life-skills/audio-overview/"),
            ("Tự Nhiên", "Cách Hiểu Và Sống Thuận Theo Tự Nhiên", "Sống thuận theo tự nhiên.", "/life-skills/c-ch-hi-u-v-s-ng-thu-n-theo-t-nhi-n/"),
        ]),
        ("Tự Vấn & Phân Tích", [
            ("Thông Tin", "Bản Chất Quá Trình Thu Gom Thông Tin", "Bản chất của việc thu gom thông tin.", "/life-skills/b-n-ch-t-c-a-qu-tr-nh-thu-gom-th-ng-tin-c-h-c-v-tr-tu-ch-th-c/"),
            ("Hơi Thở", "Cách Thở", "Về hơi thở.", "/life-skills/c-ch-th/"),
            ("Tham", "Lòng Tham Và Nhu Cầu Học Hỏi Chân Chính", "Tham và học hỏi chân chính.", "/life-skills/l-ng-tham-v-nhu-c-u-h-c-h-i-ch-n-ch-nh/"),
            ("Tâm Lý", "Phân Tích Tâm Lý", "Phân tích tâm lý.", "/life-skills/ph-n-t-ch-t-m-l/"),
        ]),
    ],
}

DAOIST_EN = {
    "title_en": "Daoist Arts",
    "subtitle_en": "Internal alchemy, neigong, talismans, feng shui, and the Daoist classics — the philosophical and esoteric roots",
    "sections": [
        ("Internal Alchemy", [
            ("Neigong", "Daoist Internal Alchemy, Neigong & Weigong Training", "Foundations of internal cultivation through Daoist alchemical practice.", "/daoist/daoist-internal-alchemy-neigong-and-weigong-training/"),
            ("Daode Jing", "Dao De Jing — Nguyễn Hiến Lê", "Vietnamese translation of the foundational Daoist classic.", "/daoist/dao-duc-kinh-nguyen-hien-le/"),
            ("Daode Jing 2", "Dao De Jing — Nhân tử Nguyễn Văn Thọ", "Second scholarly translation of the Dao De Jing.", "/daoist/dao-duc-kinh-nhan-tu-nguyen-van-tho-khao-luan-binh-dich/"),
        ]),
        ("Esoteric Practices", [
            ("Talismans", "Daoist Magical Talismans — The Secret Teaching", "The esoteric tradition of talismanic magic.", "/daoist/daoist-magical-talismans-the-secret-teaching-of-esoteric-daoist-magic/"),
            ("Plant/Animal/Mineral", "Daoist Plant, Animal and Mineral Magic", "Daoist magical uses of natural substances.", "/daoist/daoist-plant-animal-and-mineral-magic/"),
            ("Weather", "Daoist Weather Magic & Feng Shui", "Atmospheric and environmental Daoist practices.", "/daoist/daoist_weather_magic_and_feng_shui_by_jerry_alan_johnson/"),
            ("Wu Wei", "Đạo Vô Vi Trong Thái Cực Quyền", "Daoist Wu Wei applied to Tai Chi practice.", "/daoist/dao-vo-vi-trong-thai-cuc-quyen/"),
        ]),
    ],
}

DAOIST_VI = {
    "title_vi": "Đạo Gia",
    "subtitle_vi": "Nội đan, nội công, phù lục, phong thủy, và kinh điển Đạo gia — gốc rễ triết học và bí truyền",
    "sections": [
        ("Nội Đan", [
            ("Nội Công", "Đạo Gia Nội Đan, Nội Công & Ngoại Công", "Nền tảng tu luyện nội tại qua thực hành nội đan Đạo gia.", "/daoist/daoist-internal-alchemy-neigong-and-weigong-training/"),
            ("Đạo Đức Kinh", "Đạo Đức Kinh — Nguyễn Hiến Lê", "Bản dịch tiếng Việt kinh điển nền tảng Đạo gia.", "/daoist/dao-duc-kinh-nguyen-hien-le/"),
            ("Đạo Đức Kinh 2", "Đạo Đức Kinh — Nhân Tử Nguyễn Văn Thọ", "Bản khảo luận thứ hai của Đạo Đức Kinh.", "/daoist/dao-duc-kinh-nhan-tu-nguyen-van-tho-khao-luan-binh-dich/"),
        ]),
        ("Thực Hành Bí Truyền", [
            ("Phù Lục", "Phù Lục Thần Kỳ Đạo Gia — Bí Truyền", "Truyền thống bí truyền về phù lục thần kỳ.", "/daoist/daoist-magical-talismans-the-secret-teaching-of-esoteric-daoist-magic/"),
            ("Thực Vật/Động Vật/Khoáng", "Thần Kỳ Thực Vật, Động Vật Và Khoáng Chất Đạo Gia", "Sử dụng thần kỳ Đạo gia các chất tự nhiên.", "/daoist/daoist-plant-animal-and-mineral-magic/"),
            ("Phong Thủy", "Phép Thời Tiết & Phong Thủy Đạo Gia", "Thực hành Đạo gia về khí quyển và môi trường.", "/daoist/daoist_weather_magic_and_feng_shui_by_jerry_alan_johnson/"),
            ("Vô Vi", "Đạo Vô Vi Trong Thái Cực Quyền", "Vô Vi Đạo gia áp dụng vào Thái Cực Quyền.", "/daoist/dao-vo-vi-trong-thai-cuc-quyen/"),
        ]),
    ],
}


SECTIONS = [
    ("articles", ARTICLES_EN, ARTICLES_VI),
    ("deep-dives", DEEPDIVES_EN, DEEPDIVES_VI),
    ("practice-vault", PRACTICEVAULT_EN, PRACTICEVAULT_VI),
    ("life-skills", LIFESKILLS_EN, LIFESKILLS_VI),
    ("daoist", DAOIST_EN, DAOIST_VI),
]


def main():
    print("--- Building new Yin-Yang-themed section landing pages ---")
    for slug, en, vi in SECTIONS:
        write_section_pages(slug, en, vi)
    print("--- Done ---")


if __name__ == "__main__":
    main()
