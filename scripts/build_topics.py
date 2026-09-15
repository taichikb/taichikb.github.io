#!/usr/bin/env python3
"""Build 10 EN + 10 VI technique-topic subpages.

Hand-curated content drawing on the 3.0 Beginner's Guide chapters we
extracted, but rewritten cleanly without source-table noise and VI
bleed. Each topic gets its own folder under techniques/<slug>/.
"""
from pathlib import Path
import re, sys

REPO = Path("D:/Taichi-Health-Finance/Intranet/taichikb_repo")

TAIJI_LOGO = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" class="taiji-logo"><circle cx="100" cy="100" r="98" fill="#ffffff" stroke="#000000" stroke-width="4"/><path d="M 100,2 A 98,98 0 0,1 100,198 A 49,49 0 0,1 100,100 A 49,49 0 0,0 100,2 Z" fill="#000000"/><circle cx="100" cy="51" r="12" fill="#ffffff"/><circle cx="100" cy="149" r="12" fill="#000000"/></svg>'


def page_shell(lang, title, slug):
    other_lang = "vi" if lang == "en" else "en"
    other_label = "🇻🇳 Tiếng Việt" if lang == "en" else "🇬🇧 English"
    other_href = f"/{other_lang}/techniques/{slug}/"
    if lang == "en":
        nav_items = [
            ("home", "Home", "/"),
            ("techniques", "Techniques", "/en/techniques/"),
            ("philosophy", "Philosophy", "/en/philosophy/"),
            ("history", "History", "/en/history/"),
            ("contact", "Contact", "/en/contact/"),
        ]
        home_href = "/"
    else:
        nav_items = [
            ("home", "Trang Chủ", "/vi/"),
            ("techniques", "Kỹ Thuật", "/vi/techniques/"),
            ("philosophy", "Triết Lý", "/vi/philosophy/"),
            ("history", "Lịch Sử", "/vi/history/"),
            ("contact", "Liên Hệ", "/vi/contact/"),
        ]
        home_href = "/vi/"
    nav_html = '\n'.join(
        f'<a href="{href}" class="{key}">{label}</a>'
        for key, label, href in nav_items
    )
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} — TaichiKB</title>
<meta name="description" content="TaichiKB — {title}. Black & white, Yin Yang themed bilingual knowledge base.">
<link rel="icon" href="/assets/images/taiji-logo.svg" type="image/svg+xml">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Inter:wght@400;500;600&family=Noto+Serif+SC:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/stylesheets/yin-yang.css">
</head>
<body>

<header class="site-header">
    <a href="{home_href}" class="brand">{TAIJI_LOGO}<span>TaichiKB</span></a>
    <nav class="site-nav">{nav_html}<a href="{other_href}" class="lang-switch">{other_label}</a></nav>
</header>

<main>

<article class="technique-content">
    <header class="page-header" style="text-align:center; padding:4rem 0 2rem;">
        <h1>{title}</h1>
    </header>

{{body}}

</article>

<nav class="page-nav">
    <a href="/{lang}/techniques/">← {'Techniques' if lang=='en' else 'Kỹ Thuật'}</a>
    <a href="{home_href}" class="home">⌂ {'Home' if lang=='en' else 'Trang Chủ'}</a>
    <a href="{other_href}">{other_label} →</a>
</nav>

</main>

<footer class="site-footer">
    <p>Built with ❤️ for the Vietnamese Tai Chi community <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="20" height="20" style="vertical-align:-3px;display:inline-block;"><circle cx="100" cy="100" r="98" fill="#ffffff" stroke="#000000" stroke-width="4"/><path d="M 100,2 A 98,98 0 0,1 100,198 A 49,49 0 0,1 100,100 A 49,49 0 0,0 100,2 Z" fill="#000000"/><circle cx="100" cy="51" r="12" fill="#ffffff"/><circle cx="100" cy="149" r="12" fill="#000000"/></svg> bởi Phạm Đức Hải</p>
    <p>Trang web này được xây dựng với ❤️ cho cộng đồng Thái Cực Quyền Việt Nam <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="20" height="20" style="vertical-align:-3px;display:inline-block;"><circle cx="100" cy="100" r="98" fill="#ffffff" stroke="#000000" stroke-width="4"/><path d="M 100,2 A 98,98 0 0,1 100,198 A 49,49 0 0,1 100,100 A 49,49 0 0,0 100,2 Z" fill="#000000"/><circle cx="100" cy="51" r="12" fill="#ffffff"/><circle cx="100" cy="149" r="12" fill="#000000"/></svg> bởi Phạm Đức Hải</p>
</footer>

</body>
</html>
'''


# Slugs + titles  (Batch 1 + Batch 2 = 20 topics total)
TOPICS = [
    # Batch 1 — already shipped
    ("peng",            "Peng (Phòng / 掤) — Ward Off",                "Phòng (掤) — Khối Cầu Sẵn Sàng"),
    ("ji",              "Ji (Tỳ / 挤) — Press",                         "Tỳ (挤) — Biểu Đạt Toàn Thân"),
    ("an",              "An (Án / 按) — Push",                           "Án (按) — Ấn Xuống Và Kết Thúc"),
    ("xu-thuc",         "Xū & Shí (Hư & Thực / 虚实) — Empty and Solid","Hư & Thực (虚实) — Nguyên Lý Vận Hành"),
    ("sung",            "Sōng (松) — Nine Points of Relaxation",         "Tùng (松) — Chín Điểm Thả Lỏng"),
    ("sung-vs-sui",     "Sōng vs Sūi (松 vs 塌) — Relaxation vs Collapse","Tùng vs Tập (松 vs 塌) — Thả Lỏng vs Sụp Đổ"),
    ("yi-dan-khi",      "Yi → Qi → Body (Ý → Khí → Thân)",               "Dụng Ý Dẫn Khí (意→气→身)"),
    ("mushin",          "Mushin (Vô Tâm / 無心) — Mind of No-Mind",        "Vô Tâm (無心) — Tâm Không Tâm"),
    ("om-thu",          "Hugging the Tree (Ôm Thụ / 抱树)",                "Ôm Thụ (抱树) — Tư Thế Trụ Thế"),
    ("cham-la-nhanh",   "Why Slow Is Fast",                                "Tại Sao Chậm Là Nhanh"),
    # Batch 2 — stepping, breath, practice, body, pitfalls
    ("tan-hu-tan-thuc", "Substantial & Insubstantial Stepping (Tấn Hư Tấn Thực)",
                        "Tấn Hư Tấn Thực — Bước Chân Thực Hư"),
    ("nghich-tho",      "Reverse Breathing (Nghịch Thở / 逆呼吸)",
                        "Nghịch Thở (逆呼吸) — Hơi Thở Đảo Cho Học Viên 3.0+"),
    ("nam-phut-tru-the","The 5-Minute Standing Practice",
                        "5 Phút Trụ Thế — Tập Đứng Thay Đổi Tất Cả"),
    ("bai-30-phut",     "The 30-Minute Daily Form",
                        "Bài 30 Phút Mỗi Ngày — Cấu Trúc, Tập Trung, Phục Hồi"),
    ("co-the-sau-50",   "What Taichi Does to Your Body After 50",
                        "Thái Cực Quyền Làm Gì Cho Cơ Thể Sau Tuổi 50"),
    ("ba-dieu-kien-chua-lanh","The 3 Conditions Taichi Heals (Balance, Blood Pressure, Sleep)",
                        "3 Điều Kiện Thái Cực Quyền Chữa Lành — Thăng Bằng, Huyết Áp, Giấc Ngủ"),
    ("tap-20-phut-tai-nha","The 20-Minute Home Practice (No Teacher Needed)",
                        "Buổi Tập 20 Phút Tại Nhà — Không Cần Thầy"),
    ("reset-5-phut",    "The 5-Minute Reset Practice for Busy Days",
                        "Buổi Tập Reset 5 Phút Cho Ngày Bận"),
    ("bay-sai-lam",     "The 7 Deadly Sins of the 3.0 Student",
                        "7 Lỗi \"Chết Người\" Của Học Viên 3.0"),
    ("nghich-ly-cang",  "The Tension Paradox — Why Strong Muscles Make Weak Taichi",
                        "Nghịch Lý Căng Cứng — Tại Sao Cơ Bắp Mạnh Lại Tạo Thái Cực Yếu"),
    # Batch 3 — definitions, three treasures, foundations, stance, rollback,
    # 24-form overview, breathing, diagnostic, 50+ body
    ("taichi-la-gi",    "What Is Taichi, Really? — The 3 Golden Rules of 3.0 Taichi",
                        "Thái Cực Quyền Thực Sự Là Gì? — 3 Quy Tắc Vàng Của 3.0"),
    ("tam-bao",         "The Three Treasures (Tam Bảo) — Jing, Qi, Shen",
                        "Tam Bảo — Tinh, Khí, Thần"),
    ("am-duong",        "Yin-Yang and the Dance of Opposites",
                        "Âm Dương Và Điệu Múa Của Các Cặp Đối Lập"),
    ("so-do-co-the",    "The Body Schema — Weight, Ground, Alignment",
                        "Sơ Đồ Cơ Thể — Trọng Lượng, Mặt Đất, Trục"),
    ("vo-vi-tru-the",   "The Wu Wei Stance (Vô Vi) and the Standing Post (Trụ Thế)",
                        "Tư Thế Vô Vi Và Trụ Thế Cơ Bản"),
    ("lay",             "Lu · Rollback (Lãy / 履) — Yielding and Redirecting",
                        "Lãy (履) — Nhường Và Chuyển Hướng"),
    ("24-thuc-tong-quat","The 24-Form at a Glance",
                        "24 Thức Nhìn Tổng Quan"),
    ("tho-dan-dien",    "Dan Tian Breathing — Lower Abdomen, Lower Dantian",
                        "Thở Đan Điền — Hạ Bộ, Hạ Tiêu"),
    ("ba-mo-neo",       "The 3-Anchor Check, 3-Question Diagnostic, One-Word Cues",
                        "3 Mỏ Neo Kiểm Tra, 3 Câu Hỏi Chẩn Đoán, Câu Nhắc Một Từ"),
    ("co-the-50-cong-cu","The 50+ Body as Taichi's Perfect Instrument",
                        "Cơ Thể 50+ Là Nhạc Cụ Hoàn Hảo Của Thái Cực"),
]

# Body content: list of (en_card_html, vi_card_html) per topic.
CONTENT = {

"peng": [
    (
        # EN
        "<h3>The Big Idea</h3>"
        "<p><strong>Peng (Phòng / 掤)</strong> is the foundational energy of Tai Chi Chuan. It is not a block or a ward-off in the karate sense. It is a <em>sphere of organized readiness</em> around the body — imagine an invisible ball of pressurized air that surrounds you. When something presses in, the sphere pushes back, not with muscular force, but with the integrated structure of bones, joints, and connective tissue.</p>"
        "<p>True Peng is <em>biao</em> (表 &mdash; outward but bouncy), like a basketball that gives when pressed and springs back. When a partner pushes your shoulder in Wuji stance, the energy should travel through your arm into your foot and return &mdash; that returning force is Peng.</p>",

        "<h3>Ý Tưởng Cốt Lõi</h3>"
        "<p><strong>Phòng (掤)</strong> là năng lượng nền tảng của Thái Cực Quyền. Không phải \"chặn\" hay \"đỡ\" theo nghĩa karate. Đó là <em>khối cầu sẵn sàng có tổ chức</em> bao quanh cơ thể &mdash; hãy tưởng tượng một quả cầu vô hình bằng không khí có áp lực. Khi có lực ép vào, quả cầu đẩy lại, không bằng sức cơ mà bằng cấu trúc tích hợp của xương, khớp, mô liên kết.</p>"
        "<p>Phòng thật là <em>biao</em> (表 &mdash; hướng ngoài nhưng đàn hồi), như quả bóng rổ nhún khi ép và nảy lại. Khi đối tác đẩy vai bạn ở tư thế Vô Cực, năng lượng phải đi qua cánh tay xuống chân và trở lại &mdash; lực trở về đó chính là Phòng.</p>",
    ),
    (
        "<h3>Why It's \"Expanded\" Not \"Stiff\"</h3>"
        "<p>A common mistake is to read Peng as puffed up or held tense. The 50+ body has a habit of unconsciously closing down &mdash; hunching, tightening, becoming smaller. Peng is the opposite: <em>open, expanded, ready</em>. Practising Peng teaches the body to claim space again, to <em>be present</em> in the world. People who have lost Peng look old; people who have it look alive.</p>",
        "<h3>Tại Sao \"Mở Rộng\" Mà Không \"Cứng\"</h3>"
        "<p>Sai lầm phổ biến là hiểu Phòng là phồng lên hay giữ căng. Cơ thể 50+ có thói quen vô thức thu nhỏ lại &mdash; khom, căng, trở nên nhỏ hơn. Phòng là ngược lại: <em>mở, mở rộng, sẵn sàng</em>. Thực hành Phòng dạy cơ thể chiếm lại không gian, <em>hiện diện</em> trong thế giới. Người mất Phòng trông già; người còn Phòng trông sống động.</p>",
    ),
    (
        "<h3>Drills</h3>"
        "<p><strong>Balloon Visualization (Hình ảnh quả bóng bay)</strong> &mdash; Stand in Bì Bộ with arms slightly forward, as if holding a large beach ball about 18 inches in front of you. Don't squeeze. Just keep it. Breathe 10 breaths and feel the spherical energy in your hands.</p>"
        "<p><strong>Wrist Float (Cổ tay nổi)</strong> &mdash; Hold arm out, palm down. Partner places a finger under your wrist and presses up gently. The wrist should float up under light pressure, not collapse.</p>"
        "<p><strong>Partner Press Test (Kiểm tra đẩy của đối tác)</strong> &mdash; Have your partner press gently on shoulder, arm, and back. The push should travel through you to your foot, not stop at the point of contact.</p>",
        "<h3>Bài Tập</h3>"
        "<p><strong>Hình ảnh quả bóng bay</strong> &mdash; Đứng Bì Bộ, tay đưa về trước như giữ quả bóng biển lớn cách 18 inch. Đừng bóp; chỉ giữ. Thở 10 hơi và cảm năng lượng hình cầu trong tay.</p>"
        "<p><strong>Cổ tay nổi</strong> &mdash; Đưa tay, lòng xuống. Đối tác đặt ngón tay dưới cổ tay và ấn nhẹ lên. Cổ tay phải nổi lên dưới áp lực nhẹ, không sụp.</p>"
        "<p><strong>Kiểm tra đẩy của đối tác</strong> &mdash; Nhờ đối tác ấn nhẹ vai, tay, lưng. Lực đẩy phải đi xuyên qua bạn đến chân, không dừng ở điểm tiếp xúc.</p>",
    ),
    (
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Master Cue</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Like a ball of pressurized air. Press in, push back."</p>',
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Câu Nhắc Tổng</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Như quả cầu khí áp lực. Ép vào, đẩy ra."</p>',
    ),
],

"ji": [
    (
        "<h3>The Big Idea</h3>"
        "<p><strong>Ji (Tỳ / 挤)</strong> is whole-body expression. Where Peng is the sphere of readiness around you, Ji is what happens when that sphere is compressed and projected outward in a single line. Imagine holding the energy at your chest, then squeezing both forearms toward each other and forward &mdash; not with the arms, but with the whole structure behind the arms.</p>"
        "<p>Ji issues from the back foot through the spine into the hands. The arms are the messengers; the hips and back are the engine. A common mistake is to press with the arms alone &mdash; this is a shoulder exercise, not Ji.</p>",
        "<h3>Ý Tưởng Cốt Lõi</h3>"
        "<p><strong>Tỳ (挤)</strong> là biểu đạt của toàn thân. Trong khi Phòng là khối cầu sẵn sàng bao quanh bạn, Tỳ là điều xảy ra khi khối cầu đó được nén lại và phóng ra ngoài theo một đường thẳng. Hãy tưởng tượng giữ năng lượng ở ngực, rồi ép hai cẳng tay lại gần nhau và tới trước &mdash; không phải bằng tay, mà bằng toàn bộ cấu trúc phía sau.</p>"
        "<p>Tỳ phát ra từ chân sau qua cột sống đến tay. Cánh tay là người truyền tin; hông và lưng là động cơ. Sai lầm phổ biến là chỉ ép bằng tay &mdash; đó chỉ là bài tập vai, không phải Tỳ.</p>",
    ),
    (
        "<h3>Drills</h3>"
        "<p><strong>Chest-to-Chest Compression (Nén ngực)</strong> &mdash; Stand in a slight bow stance, hands in front of the chest as if holding a softball between your palms. Without moving the hands much, contract the lower back and the space between the shoulder blades. Feel the energy project forward.</p>"
        "<p><strong>Hips Lead the Hands (Hông dẫn tay)</strong> &mdash; Place a partner's hand against your palm at chest height. The moment you press, ask your partner where they felt the force come from. If they say your palm, the power is shallow. If they say your hips or back, you have Ji.</p>",
        "<h3>Bài Tập</h3>"
        "<p><strong>Nén ngực</strong> &mdash; Đứng tư thế cung nhẹ, hai tay trước ngực như giữ quả bóng mềm giữa lòng bàn tay. Không di chuyển tay nhiều, co vùng lưng dưới và khoảng giữa hai bả vai. Cảm năng lượng phóng tới.</p>"
        "<p><strong>Hông dẫn tay</strong> &mdash; Đặt tay đối tác vào lòng bàn tay bạn ở ngang ngực. Khi bạn ép, hỏi đối tác cảm thấy lực từ đâu. Nếu họ nói lòng bàn tay &mdash; lực cạn. Nếu họ nói hông hoặc lưng &mdash; bạn có Tỳ.</p>",
    ),
    (
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Master Cue</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"The arms are the messengers. The back foot is the engine."</p>',
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Câu Nhắc Tổng</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Cánh tay là người truyền tin. Chân sau là động cơ."</p>',
    ),
],

"an": [
    (
        "<h3>The Big Idea</h3>"
        "<p><strong>An (Án / 按)</strong> is the finishing stroke. If Peng is the sphere, Ji is the compression, An is the resolution. The energy has been redirected back toward the opponent and now travels downward &mdash; through them, into the ground. An is the difference between a push that moves someone and a push that <em>roots</em> them.</p>"
        "<p>An is issued from a settled center. The kua (inguinal fold) drops, the tailbone sinks, the breath sinks. The hands appear to follow, but in fact the center has already moved &mdash; the hands just complete the picture.</p>",
        "<h3>Ý Tưởng Cốt Lõi</h3>"
        "<p><strong>Án (按)</strong> là nhát gõ kết thúc. Nếu Phòng là khối cầu, Tỳ là sự nén, Án là sự giải quyết. Năng lượng đã được chuyển hướng trở lại đối phương và bây giờ đi xuống &mdash; xuyên qua họ, xuống đất. Án là khác biệt giữa một cú đẩy di chuyển ai đó và một cú đẩy <em>neo</em> họ xuống.</p>"
        "<p>Án phát ra từ một trung tâm đã an trụ. Kua (nếp bẹn) hạ, xương cụt chìm, hơi thở chìm. Tay dường như theo sau, nhưng thực ra trung tâm đã chuyển động trước &mdash; tay chỉ hoàn thiện bức tranh.</p>",
    ),
    (
        "<h3>Drills</h3>"
        "<p><strong>Sinking the Tailbone (Chìm xương cụt)</strong> &mdash; Stand in a low bow stance, then imagine a string tied to your tailbone pulling gently downward. The lower back releases length, not compression. This is the root of An.</p>"
        "<p><strong>Finishing the Stroke (Hoàn thiện nhát gõ)</strong> &mdash; From any Peng-Ji sequence, let the final forward push ride downward through the partner rather than out beyond them. The energy should drop at their center of mass, not pass through it.</p>",
        "<h3>Bài Tập</h3>"
        "<p><strong>Chìm xương cụt</strong> &mdash; Đứng tư thế cung thấp, tưởng tượng có sợi dây buộc xương cụt kéo nhẹ xuống. Lưng dưới giãn dài, không nén. Đây là gốc của Án.</p>"
        "<p><strong>Hoàn thiện nhát gõ</strong> &mdash; Từ bất kỳ chuỗi Phòng-Tỳ nào, để cú đẩy cuối cùng đi xuống xuyên qua đối tác thay vì vượt ra ngoài họ. Năng lượng nên rơi vào trọng tâm của họ, không đi qua.</p>",
    ),
    (
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Master Cue</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Sink the center. The hands follow."</p>',
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Câu Nhắc Tổng</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Chìm trung tâm. Tay theo sau."</p>',
    ),
],

"xu-thuc": [
    (
        "<h3>The Core Operating Principle</h3>"
        "<p><strong>Hư (虚 / empty)</strong> and <strong>Thực (实 / full or solid)</strong> are the operating principle behind every movement. One leg is full, the other is empty. One hand is full, the other is empty. One direction is full, the other is empty. At every moment the body is moving between full and empty like waves.</p>"
        "<p>A common error is to be <em>double full</em> &mdash; weight on both feet, tension in both hands. Another is <em>double empty</em> &mdash; weight floating, structure unsupported. Single full, single empty. Always.</p>",
        "<h3>Nguyên Lý Vận Hành Cốt Lõi</h3>"
        "<p><strong>Hư (虚)</strong> và <strong>Thực (实)</strong> là nguyên lý vận hành đằng sau mọi chuyển động. Một chân thực, một chân hư. Một tay thực, một tay hư. Một hướng thực, một hướng hư. Cơ thể chuyển động giữa thực và hư như sóng biển.</p>"
        "<p>Một lỗi phổ biến là <em>Song Thực</em> &mdash; trọng lượng đều hai chân, căng cả hai tay. Lỗi khác là <em>Song Hư</em> &mdash; trọng lượng nổi, cấu trúc thiếu chống. Một thực, một hư. Luôn luôn.</p>",
    ),
    (
        "<h3>Why This Matters at 50+</h3>"
        "<p>Young bodies can absorb ambiguity &mdash; both feet, both hands engaged, and it's fine. The 50+ body, especially when joints ache or balance wavers, punishes ambiguity. Whenever both feet are loaded, the knees absorb twice the load. Whenever both hands grip, the shoulders tighten. Single full, single empty is easier on the joints and more stable on the ground.</p>",
        "<h3>Tại Sao Điều Này Quan Trọng Ở Tuổi 50+</h3>"
        "<p>Cơ thể trẻ có thể hấp thụ sự mơ hồ &mdash; cả hai chân, cả hai tay cùng tham gia, vẫn ổn. Cơ thể 50+, đặc biệt khi khớp đau hoặc thăng bằng chao đảo, sẽ trừng phạt sự mơ hồ. Khi cả hai chân đều chịu tải, gối hấp thụ gấp đôi. Khi cả hai tay đều nắm, vai căng. Một thực, một hư dễ chịu hơn cho khớp và vững hơn trên mặt đất.</p>",
    ),
    (
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Master Cue</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"One full, one empty. Always."</p>',
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Câu Nhắc Tổng</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Một thực, một hư. Luôn luôn."</p>',
    ),
],

"sung": [
    (
        "<h3>What Sōng Really Means</h3>"
        "<p><strong>Sōng (松)</strong> is often translated as \"relaxation,\" but it does not mean \"loose\" or \"floppy.\" It means a specific kind of relaxation: <em>release of unnecessary muscular tension while maintaining structural integrity</em>. The bones hold the shape; the muscles do not grip. The joints are open; the tendons are slack; the body is ready to move in any direction at any moment.</p>"
        "<p>The opposite is <em>sūi</em> (塌) &mdash; collapse. Sung keeps the structure upright; sūi lets it fall. The difference is between relaxed muscles and abandoned posture.</p>",
        "<h3>Tùng Thực Sự Nghĩa Là Gì</h3>"
        "<p><strong>Tùng (松)</strong> thường được dịch là \"thả lỏng,\" nhưng không có nghĩa là lỏng lẻo hay mềm oặt. Nó có nghĩa là một loại thả lỏng cụ thể: <em>giải phóng sự căng cơ không cần thiết trong khi vẫn duy trì tính toàn vẹn cấu trúc</em>. Xương giữ hình; cơ không nắm. Khớp mở; gân lỏng; cơ thể sẵn sàng di chuyển theo bất kỳ hướng nào.</p>"
        "<p>Ngược lại là <em>tập</em> (塌) &mdash; sụp đổ. Tùng giữ cấu trúc đứng thẳng; tập để nó rơi. Khác biệt nằm giữa cơ thả lỏng và tư thế bị bỏ rơi.</p>",
    ),
    (
        "<h3>The Nine Points of Relaxation</h3>"
        "<ol>"
        "<li><strong>Crown of the head (Bách hội 百會)</strong> &mdash; light, suspended, as if lifted by a thread.</li>"
        "<li><strong>Shoulders (Kiên 肩)</strong> &mdash; sunk, not raised. Drop them away from the ears.</li>"
        "<li><strong>Elbows (Trửu 肘)</strong> &mdash; dropped, never lifted. The elbow hangs heavier than the hand.</li>"
        "<li><strong>Wrists (Uyển 腕)</strong> &mdash; flexible, never locked. The wrist is the body's shock absorber.</li>"
        "<li><strong>Fingers (Chỉ 指)</strong> &mdash; gently curved as if holding a small bird.</li>"
        "<li><strong>Chest (Hưng 胸)</strong> &mdash; slightly hollow, not puffed out. Breath descends.</li>"
        "<li><strong>Waist (Yêu 腰)</strong> &mdash; the master hinge. Loose waist, mobile waist.</li>"
        "<li><strong>Kua (胯)</strong> &mdash; the inguinal fold. When the kua is loose, the legs move freely.</li>"
        "<li><strong>Knees (Tất 膝)</strong> &mdash; have direction, not compression. Energy passes through, not stops.</li>"
        "</ol>"
        "<p>Walk through these nine checkpoints before every session. After a few weeks the checklist becomes an internal gauge.</p>",
        "<h3>Chín Điểm Thả Lỏng</h3>"
        "<ol>"
        "<li><strong>Đỉnh đầu (Bách hội 百會)</strong> &mdash; nhẹ, treo, như có sợi chỉ kéo lên.</li>"
        "<li><strong>Vai (Kiên 肩)</strong> &mdash; chìm, không nâng. Hạ chúng ra xa tai.</li>"
        "<li><strong>Khuỷu (Trửu 肘)</strong> &mdash; rơi xuống, không nâng. Khuỷu nặng hơn bàn tay.</li>"
        "<li><strong>Cổ tay (Uyển 腕)</strong> &mdash; mềm dẻo, không khóa. Cổ tay là bộ giảm chấn của cơ thể.</li>"
        "<li><strong>Ngón tay (Chỉ 指)</strong> &mdash; cong nhẹ như đang giữ một con chim nhỏ.</li>"
        "<li><strong>Ngực (Hưng 胸)</strong> &mdash; hơi lõm, không phồng. Hơi thở đi xuống.</li>"
        "<li><strong>Eo (Yêu 腰)</strong> &mdash; bản lề chính. Eo lỏng, eo di động.</li>"
        "<li><strong>Kua (胯)</strong> &mdash; nếp bẹn. Khi kua lỏng, chân di chuyển tự do.</li>"
        "<li><strong>Đầu gối (Tất 膝)</strong> &mdash; có hướng, không nén. Năng lượng đi qua, không dừng.</li>"
        "</ol>"
        "<p>Điểm danh chín điểm này trước mỗi buổi tập. Sau vài tuần danh sách trở thành đồng hồ đo nội tại.</p>",
    ),
    (
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Master Cue</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Bones hold the shape. Muscles do not grip."</p>',
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Câu Nhắc Tổng</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Xương giữ hình. Cơ không nắm."</p>',
    ),
],

"sung-vs-sui": [
    (
        "<h3>The Subtle Distinction</h3>"
        "<p><strong>Sōng (松)</strong> and <strong>Sūi (塌)</strong> look almost identical from the outside. Both are relaxed. Both appear non-tense. The difference is structural: sōng maintains alignment; sūi has lost it.</p>"
        "<p>Imagine two people standing in the same soft stance. The sōng practitioner has the crown suspended, the chest hollow, the kua open, the knees on line with the toes &mdash; structure intact. The sūi practitioner has the same external relaxation but the chest has collapsed, the tailbone is tucked under, the lower back is no longer suspended. They look like the same posture, but one is alive and the other is about to fall.</p>",
        "<h3>Khác Biệt Tinh Tế</h3>"
        "<p><strong>Tùng (松)</strong> và <strong>Tập (塌)</strong> trông gần giống nhau từ bên ngoài. Cả hai đều thả lỏng. Cả hai đều không căng. Khác biệt nằm ở cấu trúc: tùng duy trì trục; tập đã mất.</p>"
        "<p>Hãy tưởng tượng hai người cùng đứng tư thế mềm. Người tùng có đỉnh đầu treo, ngực lõm, kua mở, đầu gối trên đường mũi chân &mdash; cấu trúc còn nguyên. Người tập có cùng thả lỏng bên ngoài nhưng ngực đã sụp, xương cụt cuộn dưới, lưng dưới không còn treo. Họ trông giống cùng tư thế, nhưng một đang sống và một sắp ngã.</p>",
    ),
    (
        "<h3>How to Test</h3>"
        "<p>Stand in your relaxed posture and ask a partner to place one finger on your crown. The partner should feel the head being gently pushed upward by an internal lift, not falling downward into the body. That upward lift is sōng. Without it, you are in sūi.</p>"
        "<p>A second test: ask your partner to push gently on your shoulder. With sōng, the push should travel through your structure and arrive at your foot &mdash; the bones transmit. With sūi, the shoulder collapses around the push and the energy dissipates at the surface.</p>",
        "<h3>Cách Kiểm Tra</h3>"
        "<p>Đứng ở tư thế thả lỏng và nhờ đối tác đặt một ngón tay lên đỉnh đầu bạn. Đối tác nên cảm thấy đầu được đẩy nhẹ lên bởi một lực nâng bên trong, không rơi xuống vào cơ thể. Lực nâng lên đó là tùng. Không có nó, bạn đang ở tập.</p>"
        "<p>Kiểm tra thứ hai: nhờ đối tác đẩy nhẹ vai bạn. Với tùng, lực đẩy nên đi qua cấu trúc của bạn và đến chân &mdash; xương truyền. Với tập, vai sụp quanh lực đẩy và năng lượng tiêu tan ở bề mặt.</p>",
    ),
    (
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Master Cue</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Sōng has lift. Sūi has collapse."</p>',
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Câu Nhắc Tổng</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Tùng có nâng. Tập có sụp."</p>',
    ),
],

"yi-dan-khi": [
    (
        "<h3>The Transmission Sequence</h3>"
        "<p>The classical sequence is <strong>Ý dẫn Khí, Khí dẫn Thân (意 → 氣 → 身)</strong>: <em>Yì (Intention) leads Qì (Energy), Qì leads the Body</em>. This is the operating system of the internal arts. It is not a metaphor &mdash; it is the order in which things must move if they are to be guided rather than forced.</p>"
        "<p>If the body leads, you have external movement without internal content &mdash; gymnastics. If the breath leads, you have energy movement without destination &mdash; qigong exercise. If intention leads, the body follows breath follows intention &mdash; this is internal martial art.</p>",
        "<h3>Chuỗi Truyền Dẫn</h3>"
        "<p>Chuỗi cổ điển là <strong>Ý dẫn Khí, Khí dẫn Thân (意 → 氣 → 身)</strong>: <em>Ý dẫn Khí, Khí dẫn Thân</em>. Đây là hệ điều hành của các môn nội công. Không phải ẩn dụ &mdash; đó là thứ tự mọi thứ phải di chuyển nếu chúng được dẫn dắt thay vì bị ép.</p>"
        "<p>Nếu thân dẫn, bạn có chuyển động bên ngoài mà không có nội dung bên trong &mdash; thể dục dụng cụ. Nếu hơi thở dẫn, bạn có chuyển động năng lượng mà không có đích đến &mdash; bài tập khí công. Nếu ý dẫn, thân theo hơi thở theo ý &mdash; đây là võ thuật nội gia.</p>",
    ),
    (
        "<h3>The Three Drills</h3>"
        "<p><strong>Yì First Drill (Bài tập Ý trước)</strong> &mdash; Stand in any posture. Without moving physically, simply <em>intend</em> the next movement. Hold the intention for 5 breaths. Then move. The body should arrive where the intention already was.</p>"
        "<p><strong>Qì Second Drill (Bài tập Khí sau)</strong> &mdash; During a slow form, notice where breath sits. If breath is moving before the body, you are correctly ordered. If breath arrives with the body or after, you are in external mode.</p>"
        "<p><strong>Thân Third Drill (Bài tập Thân cuối)</strong> &mdash; After practice, observe what the body wants to do next on its own. If your intention has imprinted correctly, the body suggests internal sequences rather than arbitrary movements.</p>",
        "<h3>Ba Bài Tập</h3>"
        "<p><strong>Bài tập Ý trước</strong> &mdash; Đứng ở bất kỳ tư thế nào. Khng di chuyển thể chất, chỉ <em>ý</em> chuyển động tiếp theo. Giữ ý 5 hơi thở. Rồi di chuyển. Thân nên đến nơi ý đã đến trước.</p>"
        "<p><strong>Bài tập Khí sau</strong> &mdash; Trong bài quyền chậm, nhận xét hơi thở ở đâu. Nếu hơi thở đi trước thân &mdash; thứ tự đúng. Nếu hơi thở đến cùng thân hoặc sau &mdash; bạn đang ở chế độ bên ngoài.</p>"
        "<p><strong>Bài tập Thân cuối</strong> &mdash; Sau khi tập, quan sát thân muốn làm gì tiếp theo. Nếu ý đã in đúng, thân gợi ý chuỗi bên trong thay vì chuyển động tùy ý.</p>",
    ),
    (
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Master Cue</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Intention first. Energy follows. Body arrives last."</p>',
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Câu Nhắc Tổng</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Ý trước. Khí theo. Thân đến cuối."</p>',
    ),
],

"mushin": [
    (
        "<h3>What Mushin Is</h3>"
        "<p><strong>Mushin (無心)</strong> is the Japanese term that survived into the martial arts vocabulary; the original Chinese is <em>wú xīn</em> (無心). It means \"no mind\" &mdash; not no thought, but no <em>gripping</em> on thought. The mind is clear, responsive, and unattached to any single plan.</p>"
        "<p>The everyday mind plans: <em>I will do this, then this, then this.</em> The mushin mind <em>observes</em>: <em>What is here? What wants to happen?</em> When a situation shifts, the planning mind scrambles to keep up; the mushin mind is already there.</p>",
        "<h3>Vô Tâm Là Gì</h3>"
        "<p><strong>Vô Tâm (無心)</strong> có nghĩa là \"không tâm\" &mdash; không phải không có suy nghĩ, mà là không <em>nắm giữ</em> suy nghĩ. Tâm trong suốt, đáp ứng, và không bám vào bất kỳ kế hoạch nào.</p>"
        "<p>Tâm thường ngày lên kế hoạch: <em>tôi sẽ làm cái này, rồi cái này, rồi cái này.</em> Tâm vô tâm <em>quan sát</em>: <em>điều gì đang ở đây? điều gì muốn xảy ra?</em> Khi tình huống thay đổi, tâm kế hoạch vội vã theo kịp; tâm vô tâm đã ở đó rồi.</p>",
    ),
    (
        "<h3>Why It Matters for Tai Chi</h3>"
        "<p>Every form has a memorized sequence &mdash; but no two practice sessions are identical. Some days the body is stiff; some days loose. The form that worked yesterday fails today. Mushin lets you <em>remember the form but follow the moment</em>. You keep the structure; you release the rigidity. The technique still happens, but it is shaped by what is actually present.</p>",
        "<h3>Tại Sao Quan Trọng Cho Thái Cực Quyền</h3>"
        "<p>Mỗi bài quyền có một chuỗi đã ghi nhớ &mdash; nhưng không có hai buổi tập nào giống nhau. Hôm thân cứng; hôm lỏng. Bài quyền hôm qua thành công, hôm nay thất bại. Vô tâm cho phép bạn <em>nhớ bài quyền nhưng theo khoảnh khắc</em>. Bạn giữ cấu trúc; thả sự cứng nhắc. Kỹ thuật vẫn xảy ra, nhưng được định hình bởi điều thực sự hiện diện.</p>",
    ),
    (
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Master Cue</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Plan less. Observe more."</p>',
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Câu Nhắc Tổng</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Lên kế hoạch ít. Quan sát nhiều."</p>',
    ),
],

"om-thu": [
    (
        "<h3>The Posture</h3>"
        "<p><strong>Hugging the Tree (Ôm Thụ / 抱树)</strong> is the foundational Zhan Zhuang (Trụ Thế / standing meditation) posture. Stand with feet shoulder-width apart, knees slightly bent, arms held in front of the chest as if embracing a large tree &mdash; rounded, suspended, alive.</p>"
        "<p>It looks like nothing is happening. Everything is happening. The body is learning to stand with structure, to breathe into the lower dantian, to release tension from the nine checkpoints of sōng, and to remain patient.</p>",
        "<h3>Tư Thế</h3>"
        "<p><strong>Ôm Thụ (抱树)</strong> là tư thế Trụ Thế (站樁) nền tảng. Đứng với hai chân rộng bằng vai, đầu gối hơi gập, hai tay trước ngực như đang ôm một cây lớn &mdash; tròn, treo, sống.</p>"
        "<p>Nhìn bề ngoài thì không có gì xảy ra. Nhưng mọi thứ đang xảy ra. Cơ thể đang học đứng với cấu trúc, thở vào Đan Điền dưới, thả căng từ chín điểm tùng, và duy trì sự kiên nhẫn.</p>",
    ),
    (
        "<h3>The 5-Minute Practice That Changes Everything</h3>"
        "<p>Five minutes a day of Ôm Thụ, done consistently, reshapes the body. The breath deepens by itself. The shoulders release. The kua opens. The standing form improves. The slow form improves. Push hands improves. Health improves.</p>"
        "<p>Set a timer. Stand against a wall for the first week if balance is uncertain. The wall is a teacher, not a crutch.</p>",
        "<h3>5 Phút Thay Đổi Tất Cả</h3>"
        "<p>Năm phút Ôm Thụ mỗi ngày, làm đều đặn, tái cấu trúc cơ thể. Hơi thở tự sâu hơn. Vai tự thả. Kua tự mở. Bài quyền đứng cải thiện. Bài quyền chậm cải thiện. Thôi Thủ cải thiện. Sức khỏe cải thiện.</p>"
        "<p>Đặt giờ. Tuần đầu hãy tựa tường nếu thăng bằng chưa vững. Tường là thầy, không phải nạng.</p>",
    ),
    (
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Master Cue</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Stand. Breathe. Wait. The body learns."</p>',
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Câu Nhắc Tổng</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Đứng. Thở. Chờ. Thân học."</p>',
    ),
],

"cham-la-nhanh": [
    (
        "<h3>Why Slow Is Fast</h3>"
        "<p>Tai Chi looks slow from the outside. Inside, it is densely packed: every micro-position is corrected, every joint angle is debated, every breath is placed. The 30-minute slow form packs more learning than a 10-minute fast form because the brain has time to absorb each layer. Slow is the speed at which skill compounds.</p>"
        "<p>Speed is a downstream effect. When the structure is correct, when the breath is correct, when the rhythm is correct, speed emerges naturally. Trying to be fast when the foundation is shallow produces external movement without internal content.</p>",
        "<h3>Tại Sao Chậm Là Nhanh</h3>"
        "<p>Thái Cực Quyền trông chậm từ bên ngoài. Bên trong, nó đặc kín: mỗi vị trí nhỏ được sửa, mỗi góc khớp được bàn, mỗi hơi thở được đặt. Bài quyền chậm 30 phút đóng gói nhiều học hơn bài quyền nhanh 10 phút vì não có thời gian hấp thụ mỗi lớp. Chậm là tốc độ mà kỹ năng cộng dồn.</p>"
        "<p>Tốc độ là hiệu ứng phía sau. Khi cấu trúc đúng, hơi thở đúng, nhịp điệu đúng, tốc độ tự nhiên xuất hiện. Cố nhanh khi nền tảng cạn tạo ra chuyển động bên ngoài mà không có nội dung bên trong.</p>",
    ),
    (
        "<h3>Slow as Diagnostic</h3>"
        "<p>Practising the form slowly exposes what quick practice hides. You can feel which shoulder is held, where the breath catches, which foot is double-loading. Speed lets you glide past these issues; slowness makes them unmissable.</p>"
        "<p>This is why the 3.0 beginner is told to stay slow for the first 1&ndash;2 years. Not because they are incapable of speed, but because speed would hide exactly what they most need to see.</p>",
        "<h3>Chậm Như Công Cụ Chẩn Đoán</h3>"
        "<p>Tập chậm phơi bày những gì tập nhanh che giấu. Bạn cảm nhận vai nào bị giữ, hơi thở vướng ở đâu, chân nào đang chịu tải kép. Tốc độ cho bạn lướt qua các vấn đề; sự chậm khiến chúng không thể bỏ qua.</p>"
        "<p>Vì thế người mới bắt đầu 3.0 được dặn tập chậm trong 1&ndash;2 năm đầu. Không phải vì họ không có khả năng nhanh, mà vì nhanh sẽ che giấu chính xác những gì họ cần thấy nhất.</p>",
    ),
    (
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Master Cue</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Slow is fast. Fast is shallow."</p>',
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Câu Nhắc Tổng</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Chậm là nhanh. Nhanh là cạn."</p>',
    ),
],

# ---------- Batch 2 — Stepping, breath, practice, body, pitfalls ----------

"tan-hu-tan-thuc": [
    (
        "<h3>Stepping as Hư/Thực in Motion</h3>"
        "<p>Every step in the form is a small story of <em>substantial</em> and <em>insubstantial</em>. The back foot leaves the ground only when it has nothing more to do (it has become empty). The forward foot settles into the ground only when it is ready to bear weight (it has become full). The middle of the step &mdash; when the entire body's weight is balanced between the two feet &mdash; is the riskiest moment. The skill is to <em>pass through it quickly</em>.</p>",
        "<h3>Bước Chân Là Hư/Thực Trong Chuyển Động</h3>"
        "<p>Mỗi bước trong bài quyền là một câu chuyện nhỏ của <em>thực</em> và <em>hư</em>. Chân sau rời mặt đất chỉ khi nó không còn gì để làm (nó đã trở thành hư). Chân trước đặt xuống đất chỉ khi nó sẵn sàng chịu tải (nó đã trở thành thực). Khoảnh khắc giữa bước &mdash; khi toàn bộ trọng lượng cơ thể cân bằng giữa hai chân &mdash; là lúc rủi ro nhất. Kỹ năng là <em>đi qua nó nhanh chóng</em>.</p>",
    ),
    (
        "<h3>Three Common Errors</h3>"
        "<p><strong>Leaning forward into the empty step</strong> &mdash; the head travels ahead of the foot, momentum steals weight before the foot is ready. <strong>Pushing off the back foot too hard</strong> &mdash; the body becomes a projectile instead of a pendulum, balance goes away. <strong>Planting the front foot and only <em>then</em> shifting weight</strong> &mdash; the foot arrives full too early, the back foot is unweighted too late, and the middle hangs around.</p>",
        "<h3>Ba Lỗi Phổ Biến</h3>"
        "<p><strong>Nghiêng về phía bước hư</strong> &mdash; đầu đi trước chân, quán tính lấy trọng lượng trước khi chân sẵn sàng. <strong>Đẩy chân sau quá mạnh</strong> &mdash; cơ thể trở thành đạn đạo thay vì con lắc, thăng bằng biến mất. <strong>Đặt chân trước rồi <em>mới</em> chuyển trọng lượng</strong> &mdash; chân đến thực quá sớm, chân sau thoát tải quá muộn, khoảnh khắc giữa kéo dài.</p>",
    ),
    (
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Master Cue</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Pass through the middle quickly."</p>',
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Câu Nhắc Tổng</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Đi qua giữa nhanh chóng."</p>',
    ),
],

"nghich-tho": [
    (
        "<h3>What Reverse Breathing Is</h3>"
        "<p>In normal breathing, the abdomen expands on inhale, contracts on exhale. In <strong>Nghịch Thở (reverse breathing)</strong>, the abdomen <em>contracts</em> on inhale and <em>expands</em> on exhale. This reversal increases the negative pressure in the lower abdomen during inhalation and pumps the lower dantian on exhalation.</p>"
        "<p>The sensation is like a bellows working in reverse: the chest draws up while the lower abdomen hollows on inhale, then the breath sinks while the lower abdomen fills and pushes outward on exhale. Most students need 6&ndash;12 months of daily lower-dantian breathing before trying this. It is not for the first year.</p>",
        "<h3>Nghịch Thở Là Gì</h3>"
        "<p>Bình thường, bụng phồng khi hít vào, xẹp khi thở ra. Trong <strong>Nghịch Thở</strong>, bụng <em>co</em> khi hít vào và <em>phồng</em> khi thở ra. Sự đảo ngược này tăng áp suất âm ở bụng dưới khi hít vào và bơm Đan Điền dưới khi thở ra.</p>"
        "<p>Cảm giác như cái bễ chạy ngược: ngực hút lên trong khi bụng dưới lõm xuống khi hít vào, rồi hơi thở chìm xuống trong khi bụng dưới đầy và đẩy ra ngoài khi thở ra. Hầu hết học viên cần 6&ndash;12 tháng thở Đan Điền dưới mỗi ngày trước khi thử cái này. Không dành cho năm đầu.</p>",
    ),
    (
        "<h3>Who Should Try It, Who Should Wait</h3>"
        "<p><strong>Ready</strong>: students 1+ year in, with a daily lower-dantian sitting practice. <strong>Not ready</strong>: anyone with abdominal hernia, recent abdominal surgery, severe disc issues, or uncontrolled hypertension &mdash; the abdominal pressure changes can complicate these conditions.</p>"
        "<p>The clearest sign you are ready: your normal dantian breathing has become smooth, quiet, and continuous. If you still need to remember to breathe into the lower abdomen, you are not yet ready to reverse it.</p>",
        "<h3>Ai Nên Thử, Ai Nên Chờ</h3>"
        "<p><strong>Sẵn sàng</strong>: học viên trên 1 năm, có thực hành Đan Điền dưới mỗi ngày. <strong>Chưa sẵn sàng</strong>: bất kỳ ai có thoát vị bụng, phẫu thuật bụng gần đây, vấn đề đĩa đệm nặng, hoặc cao huyết áp không kiểm soát &mdash; sự thay đổi áp suất bụng có thể làm phức tạp các tình trạng này.</p>"
        "<p>Dấu hiệu rõ ràng nhất bạn đã sẵn sàng: thở Đan Điền bình thường của bạn đã trở nên mượt mà, yên tĩnh, liên tục. Nếu bạn vẫn cần nhớ để thở vào bụng dưới, bạn chưa sẵn sàng để đảo ngược nó.</p>",
    ),
    (
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Master Cue</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Belly in on inhale. Belly out on exhale. Quietly."</p>',
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Câu Nhắc Tổng</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Bụng vào khi hít. Bụng ra khi thở. Nhẹ nhàng."</p>',
    ),
],

"nam-phut-tru-the": [
    (
        "<h3>Five Minutes That Reshape the Body</h3>"
        "<p>Five minutes of Ôm Thụ (Hugging the Tree) each day, done consistently over weeks, is more transformative than one 60-minute weekly class. The body learns what standing feels like when there is no agenda, no sequence, no movement to hide behind. Just the body and the breath.</p>"
        "<p>By week 4, students report &mdash; without being told to look &mdash; that their normal standing posture has improved. By week 8, the slow form has visibly deepened. By week 12, chronic tightness in the shoulders or lower back often releases.</p>",
        "<h3>5 Phút Tái Cấu Trúc Cơ Thể</h3>"
        "<p>Năm phút Ôm Thụ mỗi ngày, làm đều đặn trong nhiều tuần, biến đổi nhiều hơn một buổi học 60 phút mỗi tuần. Cơ thể học cảm giác đứng khi không có chương trình nào &mdash; không chuỗi, không chuyển động để trốn sau. Chỉ cơ thể và hơi thở.</p>"
        "<p>Đến tuần 4, học viên báo cáo &mdash; mà không được bảo nhìn &mdash; rằng tư thế đứng bình thường đã cải thiện. Đến tuần 8, bài quyền chậm đã sâu hơn rõ rệt. Đến tuần 12, sự căng cứng mãn tính ở vai hoặc lưng dưới thường được thả lỏng.</p>",
    ),
    (
        "<h3>The 30-Day Cure</h3>"
        "<p>Some teachers use a <em>Thirty Days of Five Minutes</em> cure: every morning, upon rising, stand in Ôm Thụ for five timed minutes. No music. No app. No phone. Just a timer. By day 30, the practice has a hold on the body that doesn't require willpower anymore.</p>"
        "<p>On day 1, five minutes can feel like an hour. By day 7, five minutes is five minutes. By day 30, five minutes is too short and you extend it yourself.</p>",
        "<h3>Liệu Trình 30 Ngày</h3>"
        "<p>Một số thầy dùng liệu trình <em>30 Ngày Năm Phút</em>: mỗi sáng khi thức dậy, đứng Ôm Thụ đúng năm phút theo đồng hồ. Không nhạc. Không ứng dụng. Không điện thoại. Chỉ đồng hồ. Đến ngày 30, thực hành đã có một giữ chặt trên cơ thể không cần ý chí nữa.</p>"
        "<p>Ngày 1, năm phút có thể cảm thấy như một giờ. Đến ngày 7, năm phút là năm phút. Đến ngày 30, năm phút là quá ngắn và bạn tự kéo dài.</p>",
    ),
    (
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Master Cue</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Five minutes. Every morning. No exception."</p>',
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Câu Nhắc Tổng</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Năm phút. Mỗi sáng. Không ngoại lệ."</p>',
    ),
],

"bai-30-phut": [
    (
        "<h3>What the 30-Minute Form Looks Like</h3>"
        "<p>A complete Tai Chi practice in 30 minutes is broken into <strong>three blocks of ten minutes</strong>: warm-up, form, cool-down. The warm-up is Jing Gong (quiet standing) plus a few release movements. The form is one or two repetitions of your current form. The cool-down is hands-on self-massage along the meridians, ending with three still breaths.</p>",
        "<h3>Bài 30 Phút Trông Như Thế Nào</h3>"
        "<p>Một buổi tập Thái Cực Quyền hoàn chỉnh trong 30 phút được chia thành <strong>ba khối mười phút</strong>: khởi động, bài quyền, hạ nhiệt. Khởi động là Tĩnh Công (đứng yên) cộng vài động tác thả lỏng. Bài quyền là một hoặc hai lần bài quyền hiện tại. Hạ nhiệt là tự xoa bóp dọc kinh mạch, kết thúc bằng ba hơi thở yên tĩnh.</p>",
    ),
    (
        "<h3>The Three Anchors Within the Half-Hour</h3>"
        "<p><strong>Anchor 1 (minute 0&ndash;10): body</strong> &mdash; where is my weight, where is my breath, what is tense that need not be. <strong>Anchor 2 (minute 10&ndash;20): form</strong> &mdash; what does this movement want to teach me today. <strong>Anchor 3 (minute 20&ndash;30): heart</strong> &mdash; what is the practice for, beyond technique. Who am I doing this for.</p>",
        "<h3>Ba Mỏ Neo Trong Nửa Giờ</h3>"
        "<p><strong>Mỏ neo 1 (phút 0&ndash;10): thân</strong> &mdash; trọng lượng ở đâu, hơi thở ở đâu, gì đang căng mà không cần. <strong>Mỏ neo 2 (phút 10&ndash;20): bài</strong> &mdash; chuyển động này hôm nay muốn dạy tôi điều gì. <strong>Mỏ neo 3 (phút 20&ndash;30): tâm</strong> &mdash; thực hành này vì cái gì, ngoài kỹ thuật. Tôi làm điều này vì ai.</p>",
    ),
    (
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Master Cue</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Body, Form, Heart &mdash; ten minutes each."</p>',
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Câu Nhắc Tổng</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Thân, Bài, Tâm &mdash; mỗi phần mười phút."</p>',
    ),
],

"co-the-sau-50": [
    (
        "<h3>What Actually Changes</h3>"
        "<p>After age 50, the body undergoes predictable changes: collagen production drops 1.5% per year, joint cartilage thins, vestibular neurons fire less reliably, fast-twitch muscle fibres shrink. These are not failures &mdash; they are shifts. Tai Chi works <em>with</em> these shifts, not against them.</p>"
        "<p>The slow, weight-bearing, balance-challenging, attention-anchored nature of Tai Chi addresses exactly the capacities that decline: proprioception, balance, fascia elasticity, vagal tone, breath depth, blood pressure regulation. It is almost a parody of coincidence: the body at 50+ is the body Tai Chi was designed for.</p>",
        "<h3>Điều Gì Thực Sự Thay Đổi</h3>"
        "<p>Sau tuổi 50, cơ thể trải qua những thay đổi có thể dự đoán: sản xuất collagen giảm 1,5% mỗi năm, sụn khớp mỏng đi, tế bào thần kinh tiền đình hoạt động kém tin cậy hơn, sợi cơ co nhanh co lại. Đây không phải thất bại &mdash; đó là sự chuyển dịch. Thái Cực Quyền làm việc <em>với</em> những chuyển dịch này, không chống lại.</p>"
        "<p>Tính chất chậm, chịu tải, đòi hỏi thăng bằng, neo sự chú ý của Thái Cực Quyền giải quyết chính xác những năng lực đang suy giảm: cảm giác bản thể, thăng bằng, đàn hồi cân, trương lực phế vị, độ sâu hơi thở, điều hòa huyết áp. Gần như là một sự trùng hợp mỉa mai: cơ thể ở tuổi 50+ là cơ thể mà Thái Cực Quyền được thiết kế cho.</p>",
    ),
    (
        "<h3>What You Will Notice in Your Own Body</h3>"
        "<p>Most students in their 50s notice four things within the first six months of daily practice: better sleep (deeper, fewer wake-ups), steadier blood pressure (often after 3 months), easier stairs (knees feel more supported, not less), and clearer recall (the mind feels less foggy at the end of a long day).</p>"
        "<p>Few things in medicine are this predictable across a population. Tai Chi is one of them.</p>",
        "<h3>Bạn Sẽ Nhận Ra Gì Trong Cơ Thể Mình</h3>"
        "<p>Hầu hết học viên ở độ tuổi 50 nhận thấy bốn điều trong sáu tháng đầu tập đều đặn: ngủ tốt hơn (sâu hơn, ít thức giấc hơn), huyết áp ổn hơn (thường sau 3 tháng), leo cầu thang dễ hơn (gối có vẻ được hỗ trợ hơn, không phải yếu hơn), và trí nhớ rõ hơn (đầu bớt mờ mờ vào cuối ngày dài).</p>"
        "<p>Ít thứ trong y học dự đoán được như thế này trên một quần thể. Thái Cực Quyền là một trong những thứ đó.</p>",
    ),
    (
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Master Cue</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"The body at 50+ is the body Tai Chi was designed for."</p>',
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Câu Nhắc Tổng</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Cơ thể 50+ là cơ thể mà Thái Cực Quyền được thiết kế cho."</p>',
    ),
],

"ba-dieu-kien-chua-lanh": [
    (
        "<h3>The Three Conditions</h3>"
        "<p>Tai Chi has the strongest evidence base for improving exactly three things at age 50+: <strong>balance</strong>, <strong>blood pressure</strong>, and <strong>sleep</strong>. Each is a real cause of suffering and a real cost to the healthcare system. Each improves measurably with daily Tai Chi within weeks to months.</p>",
        "<h3>Ba Điều Kiện</h3>"
        "<p>Thái Cực Quyền có cơ sở bằng chứng mạnh nhất cho việc cải thiện chính xác ba điều ở tuổi 50+: <strong>thăng bằng</strong>, <strong>huyết áp</strong>, và <strong>giấc ngủ</strong>. Mỗi thứ là nguyên nhân thực sự của đau khổ và chi phí thực sự cho hệ thống y tế. Mỗi thứ cải thiện đo được với Thái Cực Quyền mỗi ngày trong vài tuần đến vài tháng.</p>",
    ),
    (
        "<h3>What the Studies Show</h3>"
        "<p>A 2020 meta-analysis in JAMA Internal Medicine, pooling 32 randomized trials with more than 4,000 participants, found that Tai Chi reduced fall risk by <strong>43%</strong> compared to no exercise. A 2017 meta-analysis in Journal of the American Heart Association found Tai Chi lowered systolic blood pressure by <strong>15.6 mmHg</strong> on average &mdash; equivalent to a first-line blood pressure medication. A 25-week Emory study of older adults with sleep problems found sleep onset latency dropped from 28 to 16 minutes.</p>"
        "<p>These are not marginal effects. They are the scale of effect that gets randomized trial funding and meta-analysis attention.</p>",
        "<h3>Nghiên Cứu Cho Thấy Gì</h3>"
        "<p>Một phân tích tổng hợp năm 2020 trên JAMA Internal Medicine, gộp 32 thử nghiệm ngẫu nhiên với hơn 4.000 người tham gia, phát hiện Thái Cực Quyền giảm nguy cơ té ngã <strong>43%</strong> so với không tập. Một phân tích năm 2017 trên Journal of the American Heart Association phát hiện Thái Cực Quyền giảm huyết áp tâm thu trung bình <strong>15,6 mmHg</strong> &mdash; tương đương với thuốc huyết áp hàng đầu. Một nghiên cứu 25 tuần của Emory trên người lớn tuổi có vấn đề giấc ngủ phát hiện thời gian vào giấc ngủ giảm từ 28 xuống 16 phút.</p>"
        "<p>Đây không phải hiệu quả nhỏ. Đây là quy mô hiệu quả thu hút được tài trợ thử nghiệm ngẫu nhiên và sự chú ý của phân tích tổng hợp.</p>",
    ),
    (
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Master Cue</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Forty-three percent fewer falls. Sixteen mmHg lower. Sleep that arrives."</p>',
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Câu Nhắc Tổng</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Bốn mươi ba phần trăm ít té hơn. Mười sáu mmHg thấp hơn. Giấc ngủ đến."</p>',
    ),
],

"tap-20-phut-tai-nha": [
    (
        "<h3>The Structure</h3>"
        "<p>Twenty minutes at home, with no teacher, no equipment, no music, can be one of the most reliable daily practices in Tai Chi. The structure is simple: <strong>5 minutes Ôm Thụ</strong>, <strong>10 minutes slow form</strong>, <strong>5 minutes standing meditation and breath</strong>.</p>"
        "<p>That is the entire practice. The room can be small. The floor can be a carpet. The shoes can be socks.</p>",
        "<h3>Cấu Trúc</h3>"
        "<p>Hai mươi phút tại nhà, không thầy, không thiết bị, không nhạc, có thể là một trong những thực hành hằng ngày đáng tin nhất trong Thái Cực Quyền. Cấu trúc đơn giản: <strong>5 phút Ôm Thụ</strong>, <strong>10 phút bài quyền chậm</strong>, <strong>5 phút thiền đứng và thở</strong>.</p>"
        "<p>Đó là toàn bộ thực hành. Phòng có thể nhỏ. Sàn có thể là thảm. Giày có thể là tất.</p>",
    ),
    (
        "<h3>Substitutions When You Cannot Do the Form</h3>"
        "<p>Some mornings the body will not cooperate. The substitution stack: <strong>if the form is too much</strong>, do 15 minutes of Ôm Thụ instead. <strong>If even standing is too much</strong>, do 15 minutes of seated Zhan Zhuang on a chair with the arms rounded forward. <strong>If even sitting is too much</strong>, do 15 minutes of lying dantian breathing. <strong>Some practice always beats no practice</strong>.</p>",
        "<h3>Thay Thế Khi Không Thể Tập Bài Quyền</h3>"
        "<p>Một số buổi sáng cơ thể sẽ không hợp tác. Chuỗi thay thế: <strong>nếu bài quyền quá nhiều</strong>, làm 15 phút Ôm Thụ thay thế. <strong>Nếu ngay cả đứng cũng quá nhiều</strong>, làm 15 phút Trụ Thế ngồi trên ghế với tay tròn phía trước. <strong>Nếu ngay cả ngồi cũng quá nhiều</strong>, làm 15 phút thở Đan Điền nằm. <strong>Một số thực hành luôn tốt hơn không thực hành</strong>.</p>",
    ),
    (
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Master Cue</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Some practice always beats no practice."</p>',
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Câu Nhắc Tổng</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Một số thực hành luôn tốt hơn không thực hành."</p>',
    ),
],

"reset-5-phut": [
    (
        "<h3>The Five-Minute Reset</h3>"
        "<p>On days when the schedule has eaten the practice, when travel has interrupted everything, when the body is sore from a tennis match or a long meeting, you can still recover five minutes. The sequence:</p>"
        "<p>1. 60 seconds <strong>dantian breath</strong>, seated or standing.<br>"
        "2. 60 seconds <strong>spinal roll-down</strong>: chin to chest, vertebra by vertebra.<br>"
        "3. 60 seconds <strong>shoulder circles</strong>: both directions, slow.<br>"
        "4. 60 seconds <strong>ankle rotations</strong>: seated, both feet, both directions.<br>"
        "5. 60 seconds <strong>Ôm Thụ lite</strong>: standing, three breaths.</p>"
        "<p>This is not a substitute for the real practice. But it is a fraction of the real practice, and a fraction of the real practice, done daily, compounds.",
        "<h3>Reset 5 Phút</h3>"
        "<p>Vào những ngày lịch trình đã nuốt mất thực hành, khi du lịch làm gián đoạn mọi thứ, khi cơ thể đau từ trận tennis hay cuộc họp dài, bạn vẫn có thể lấy lại năm phút. Chuỗi:</p>"
        "<p>1. 60 giây <strong>thở Đan Điền</strong>, ngồi hoặc đứng.<br>"
        "2. 60 giây <strong>cuộn cột sống xuống</strong>: cằm về ngực, từng đốt sống một.<br>"
        "3. 60 giây <strong>xoay vai</strong>: cả hai chiều, chậm.<br>"
        "4. 60 giây <strong>xoay cổ chân</strong>: ngồi, cả hai chân, cả hai chiều.<br>"
        "5. 60 giây <strong>Ôm Thụ nhẹ</strong>: đứng, ba hơi thở.</p>"
        "<p>Đây không phải thay thế cho thực hành thật. Nhưng nó là một phần của thực hành thật, và một phần thực hành thật, làm mỗi ngày, sẽ cộng dồn.</p>",
    ),
    (
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Master Cue</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"A fraction of the practice, done daily, compounds."</p>',
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Câu Nhắc Tổng</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Một phần thực hành, mỗi ngày, sẽ cộng dồn."</p>',
    ),
],

"bay-sai-lam": [
    (
        "<h3>The Seven Sins</h3>"
        "<p>Almost every common beginner mistake falls into one of seven categories. Each is a way of <em>forcing</em> what should be <em>allowed</em>:</p>"
        "<ol>"
        "<li><strong>Holding the breath</strong> &mdash; power surges in the shoulders and neck.</li>"
        "<li><strong>Leading with the arms</strong> &mdash; the body becomes a passenger.</li>"
        "<li><strong>Locking the knees</strong> &mdash; the lower joints stop transmitting force.</li>"
        "<li><strong>Puffing the chest</strong> &mdash; breath rises, the lower dantian empties.</li>"
        "<li><strong>Double-loading</strong> &mdash; weight shared by both feet, both hands. No waves, no structure.</li>"
        "<li><strong>Sinking the shoulders too far</strong> &mdash; not sōng but sui. The chest collapses.</li>"
        "<li><strong>Moving the head before the body</strong> &mdash; the neck takes weight it shouldn't.</li>"
        "</ol>",
        "<h3>Bảy Lỗi</h3>"
        "<p>Gần như mọi sai lầm phổ biến của người mới rơi vào một trong bảy loại. Mỗi loại là một cách <em>ép</em> điều nên được <em>cho phép</em>:</p>"
        "<ol>"
        "<li><strong>Nín thở</strong> &mdash; lực dồn lên vai và cổ.</li>"
        "<li><strong>Dẫn bằng tay</strong> &mdash; cơ thể trở thành hành khách.</li>"
        "<li><strong>Khóa gối</strong> &mdash; khớp dưới ngừng truyền lực.</li>"
        "<li><strong>Phồng ngực</strong> &mdash; hơi thở dâng lên, Đan Điền dưới trống.</li>"
        "<li><strong>Song tải</strong> &mdash; trọng lượng chia cả hai chân, cả hai tay. Không sóng, không cấu trúc.</li>"
        "<li><strong>Hạ vai quá sâu</strong> &mdash; không phải tùng mà là tập. Ngực sụp.</li>"
        "<li><strong>Di chuyển đầu trước thân</strong> &mdash; cổ mang trọng lượng không nên mang.</li>"
        "</ol>",
    ),
    (
        "<h3>How to Use This List</h3>"
        "<p>Don't try to fix all seven. Pick the one your teacher or partner has pointed out most often and live with that for a month. Add the next one only when the first is no longer an issue. Most students clear the list in two to three years. Some never clear all seven; that is fine. <em>Tai Chi is a lifelong practice</em>.</p>",
        "<h3>Cách Dùng Danh Sách Này</h3>"
        "<p>Đừng cố sửa cả bảy. Chọn một lỗi mà thầy hoặc đối tác đã chỉ ra thường xuyên nhất và sống với nó trong một tháng. Thêm cái tiếp theo chỉ khi cái trước không còn là vấn đề. Hầu hết học viên sửa sạch danh sách trong hai đến ba năm. Một số không bao giờ sửa hết bảy; điều đó ổn. <em>Thái Cực Quyền là thực hành suốt đời</em>.</p>",
    ),
    (
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Master Cue</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Force is the enemy. Allowance is the path."</p>',
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Câu Nhắc Tổng</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Ép buộc là kẻ thù. Cho phép là con đường."</p>',
    ),
],

"nghich-ly-cang": [
    (
        "<h3>The Paradox</h3>"
        "<p>The most common shock in any Tai Chi class is when a 50-year-old office worker &mdash; who cannot lift their bodyweight and has not exercised in 20 years &mdash; produces a sharper fajin than a fit 30-year-old gym-goer. The reason is not magic. It is that Tai Chi uses a different muscular pathway: <em>fascia</em>, not <em>muscle</em>.</p>"
        "<p>Strong, bulky muscles are designed for short bursts of maximal effort. Tai Chi uses the elastic, springy, layered connective tissue that wraps every joint and links every bone. Heavy weight training atrophies that tissue (muscles win and squeeze the fascia). Long, slow, full-range movement nourishes it.</p>",
        "<h3>Nghịch Lý</h3>"
        "<p>Cú sốc phổ biến nhất trong bất kỳ lớp Thái Cực Quyền nào là khi một nhân viên văn phòng 50 tuổi &mdash; không nâng được trọng lượng cơ thể và đã 20 năm không tập thể dục &mdash; tạo ra phát lực sắc hơn một người 30 tuổi tập gym khỏe mạnh. Lý do không phải phép thuật. Đó là Thái Cực Quyền dùng con đường cơ bắp khác: <em>cân mạc</em>, không phải <em>cơ bắp</em>.</p>"
        "<p>Cơ bắp to khỏe được thiết kế cho các đợt nỗ lực tối đa ngắn. Thái Cực Quyền dùng mô liên kết đàn hồi, có lò xo, nhiều lớp bao bọc mọi khớp và liên kết mọi xương. Tập tạ nặng làm teo mô đó (cơ bắp thắng và ép cân mạc). Chuyển động dài, chậm, toàn phạm vi nuôi dưỡng nó.</p>",
    ),
    (
        "<h3>What This Means for Tennis Players</h3>"
        "<p>For the tennis player in particular, this is good news. The body's tennis strength is in the calves, quads, shoulders, and forearms &mdash; large muscles that produce short powerful movements. Tai Chi builds a different layer: deep core, fascia, balance reflexes, breath control, recovery. The two systems stack rather than compete. A body with both is harder to injure and harder to exhaust.</p>",
        "<h3>Điều Này Có Nghĩa Gì Cho Người Chơi Tennis</h3>"
        "<p>Đặc biệt cho người chơi tennis, đây là tin tốt. Sức mạnh tennis của cơ thể nằm ở bắp chân, đùi trước, vai và cẳng tay &mdash; cơ bắp lớn tạo ra các chuyển động ngắn mạnh mẽ. Thái Cực Quyền xây dựng một lớp khác: cốt lõi sâu, cân mạc, phản xạ thăng bằng, kiểm soát hơi thở, phục hồi. Hai hệ thống xếp chồng thay vì cạnh tranh. Một cơ thể có cả hai khó bị chấn thương hơn và khó kiệt sức hơn.</p>",
    ),
    (
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Master Cue</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Strong muscles make weak Tai Chi. Springy fascia makes powerful Tai Chi."</p>',
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Câu Nhắc Tổng</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Cơ bắp mạnh tạo Thái Cực yếu. Cân mạc có lò xo tạo Thái Cực mạnh."</p>',
    ),
],

# ---------- Batch 3 — Definitions, foundations, practice tools ----------

"taichi-la-gi": [
    (
        "<h3>What Taichi Is, Really</h3>"
        "<p>Taichi Chuan is not the slow-motion wave-hands you see in the park. It is a complete <em>internal</em> martial system: 8 Gates, 24-Form, Zhan Zhuang, silk reeling, push hands, sword, and the philosophy underneath. Most students never see 80% of the system from casual observation. The art's full depth only opens to a daily practice of years.</p>"
        "<p>The art is unusual in that <em>how</em> you do a movement matters more than <em>what</em> movement you do. A slow walking step with the correct internal sequence teaches more than a flashy kick done with muscular force. This is why teachers so often repeat the same simple movement for years.</p>",
        "<h3>Thái Cực Quyền Thực Sự Là Gì</h3>"
        "<p>Thái Cực Quyền không phải vẫy tay chậm ngoài công viên. Đó là một hệ thống võ thuật <em>nội gia</em> hoàn chỉnh: Bát Môn, 24 Thức, Trụ Thế, Chân Tư, Thôi Thủ, Kiếm, và triết lý bên dưới. Hầu hết học viên không bao giờ thấy 80% hệ thống từ quan sát thông thường. Chiều sâu đầy đủ của môn chỉ mở ra với thực hành hằng ngày nhiều năm.</p>"
        "<p>Môn này khác thường ở chỗ <em>cách</em> bạn thực hiện chuyển động quan trọng hơn <em>chuyển động</em> nào bạn làm. Một bước chậm với chuỗi nội tại đúng dạy nhiều hơn một cú đá hào nhoáng bằng lực cơ bắp. Vì thế các thầy thường lặp lại cùng một chuyển động đơn giản trong nhiều năm.</p>",
    ),
    (
        "<h3>The 3 Golden Rules of 3.0 Taichi</h3>"
        "<p><strong>1. Slow is fast.</strong> The 30-minute slow form packs more learning than a 10-minute fast form because the brain has time to absorb each layer. <strong>2. The breath leads.</strong> Breath descends into the lower dantian before any movement begins; the body then follows the breath, not the other way around. <strong>3. The waist is the master.</strong> When the waist is loose, the limbs move freely; when the waist is rigid, no amount of arm technique can save the form. Memorise these three and live with them for a year.</p>",
        "<h3>3 Quy Tắc Vàng Của Thái Cực 3.0</h3>"
        "<p><strong>1. Chậm là nhanh.</strong> Bài quyền chậm 30 phút đóng gói nhiều học hơn bài quyền nhanh 10 phút vì não có thời gian hấp thụ mỗi lớp. <strong>2. Hơi thở dẫn đầu.</strong> Hơi thở chìm xuống Đan Điền dưới trước khi bất kỳ chuyển động nào bắt đầu; thân sau đó theo hơi thở, không phải ngược lại. <strong>3. Eo là bậc thầy.</strong> Khi eo lỏng, tứ chi di chuyển tự do; khi eo cứng, không có kỹ thuật tay nào cứu nổi bài quyền. Ghi nhớ ba điều này và sống với chúng một năm.</p>",
    ),
    (
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Master Cue</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Slow is fast. Breath leads. The waist is the master."</p>',
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Câu Nhắc Tổng</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Chậm là nhanh. Hơi thở dẫn đầu. Eo là bậc thầy."</p>',
    ),
],

"tam-bao": [
    (
        "<h3>The Three Treasures</h3>"
        "<p>The <strong>Tam Bảo (Three Treasures)</strong> are the three layers of the human system that Tai Chi refines in order: <strong>Jing (精)</strong> essence, stored in the kidneys; <strong>Qi (氣)</strong> life energy, cultivated at the Dantian; <strong>Shen (神)</strong> spirit, expressed through the eyes and the will. The practice refines Jing into Qi, and Qi into Shen. This is not a metaphor &mdash; it is a description of what actually happens to the body and mind with daily practice.</p>",
        "<h3>Tam Bảo</h3>"
        "<p><strong>Tam Bảo (Ba Bảo)</strong> là ba tầng của hệ thống con người mà Thái Cực Quyền tinh luyện theo thứ tự: <strong>Tinh (精)</strong> tinh hoa, tồn tại tại thận; <strong>Khí (氣)</strong> năng lượng sống, tu tại Đan Điền; <strong>Thần (神)</strong> thần trí, biểu hiện qua mắt và ý chí. Thực hành tinh luyện Tinh thành Khí, Khí thành Thần. Đây không phải ẩn dụ &mdash; đó là mô tả những gì thực sự xảy ra với cơ thể và tâm trí qua thực hành hằng ngày.</p>",
    ),
    (
        "<h3>How the Three Refine</h3>"
        "<p><strong>Jing to Qi</strong> happens through breath and movement: deep dantian breathing pulls essence upward through the spine; silk-reeling movement circulates it through the limbs. <strong>Qi to Shen</strong> happens through stillness: when the mind stops chasing, the eyes sharpen and the will focuses. The Shen is what gives the Tai Chi practitioner their calm-gaze quality &mdash; it is visible to anyone who has spent time around senior students.</p>",
        "<h3>Cách Tam Bảo Tinh Luyện</h3>"
        "<p><strong>Tinh thành Khí</strong> xảy ra qua hơi thở và chuyển động: thở Đan Điền sâu kéo tinh hoa lên qua cột sống; chuyển động Chân Tư luân chuyển qua tứ chi. <strong>Khí thành Thần</strong> xảy ra qua tĩnh lặng: khi tâm ngừng đuổi theo, mắt sắc lại và ý chí tập trung. Thần là điều mang lại cho người tập Thái Cực phẩm chất ánh mắt bình thản &mdash; nó hiện rõ với bất kỳ ai đã dành thời gian bên các học viên cao cấp.</p>",
    ),
    (
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Master Cue</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Essence becomes Energy. Energy becomes Spirit."</p>',
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Câu Nhắc Tổng</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Tinh thành Khí. Khí thành Thần."</p>',
    ),
],

"am-duong": [
    (
        "<h3>The Dance</h3>"
        "<p>Yin-Yang is not a static symbol. It is a <em>dance</em>: every Yang contains a seed of Yin, every Yin contains a seed of Yang, and the boundary between them is curved &mdash; not a clean line. In Tai Chi, every movement embodies this dance: open and close, advance and retreat, hard and soft, full and empty. The art teaches you to <em>see</em> the dance, then to <em>be</em> the dance.</p>",
        "<h3>Điệu Múa</h3>"
        "<p>Âm Dương không phải biểu tượng tĩnh. Đó là một <em>điệu múa</em>: mỗi Dương chứa một mầm Âm, mỗi Âm chứa một mầm Dương, và ranh giới giữa chúng là đường cong &mdash; không phải đường thẳng. Trong Thái Cực Quyền, mỗi chuyển động thể hiện điệu múa này: mở và đóng, tiến và lùi, cứng và mềm, thực và hư. Môn võ dạy bạn <em>nhìn</em> điệu múa, rồi <em>trở thành</em> điệu múa.</p>",
    ),
    (
        "<h3>Where You See It in the Form</h3>"
        "<p>The 24-Form demonstrates Yin-Yang in every phrase. <em>Commencing Form</em> opens (Yang) and closes (Yin). <em>Parting the Wild Horse's Mane</em> is the Yang phase of a Yang-Yin pair. <em>White Crane Spreads Its Wings</em> is the most Yin movement in the form &mdash; the body lifts upward and the weight retreats into the back foot. <em>Step Back and Repulse the Monkey</em> shows the same Yang action retreating into a Yin posture. <strong>Once you see the dance, you cannot un-see it.</strong></p>",
        "<h3>Bạn Thấy Nó Ở Đâu Trong Bài Quyền</h3>"
        "<p>24 Thức thể hiện Âm Dương trong mỗi cụm. <em>Khởi Thức</em> mở (Dương) rồi đóng (Âm). <em>Dã Mã Phân Tung</em> là pha Dương của một cặp Dương-Âm. <em>Bạch Hạc Lượng Sí</em> là chuyển động Âm nhất trong bài quyền &mdash; thân nâng lên và trọng lượng rút về chân sau. <em>Đảo Toản Hầu</em> cho thấy cùng hành động Dương rút vào tư thế Âm. <strong>Một khi bạn nhìn thấy điệu múa, bạn không thể nhìn không thấy nữa.</strong></p>",
    ),
    (
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Master Cue</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Every Yang has a Yin seed. Every Yin has a Yang seed."</p>',
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Câu Nhắc Tổng</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Mỗi Dương có một mầm Âm. Mỗi Âm có một mầm Dương."</p>',
    ),
],

"so-do-co-the": [
    (
        "<h3>Three Maps You Always Carry</h3>"
        "<p>Every Tai Chi movement is the body's answer to three questions: <strong>where is my weight?</strong> (forward/back/left/right); <strong>where is the ground?</strong> (which points of the foot are pressing, which are light); <strong>where is my alignment?</strong> (is the spine vertical, is the breath unobstructed). Most beginners carry only one of these maps at a time. Experienced practitioners carry all three simultaneously, and the body answers them without thinking.</p>",
        "<h3>Ba Bản Đồ Bạn Luôn Mang Theo</h3>"
        "<p>Mỗi chuyển động Thái Cực Quyền là câu trả lời của cơ thể cho ba câu hỏi: <strong>trọng lượng ở đâu?</strong> (trước/sau/trái/phải); <strong>mặt đất ở đâu?</strong> (điểm nào của bàn chân đang ấn, điểm nào nhẹ); <strong>trục của tôi ở đâu?</strong> (cột sống có thẳng không, hơi thở có thông không). Hầu hết người mới chỉ mang một trong ba bản đồ này tại một thời điểm. Người tập có kinh nghiệm mang cả ba cùng lúc, và cơ thể trả lời chúng mà không cần suy nghĩ.</p>",
    ),
    (
        "<h3>Drill: The Three Maps in One Minute</h3>"
        "<p>Set a one-minute timer. Stand in a slight bow stance. For 20 seconds, say out loud where your weight is. For 20 seconds, name the points of the foot that touch the ground. For 20 seconds, trace your spine from tailbone to crown with your attention. The drill forces the three maps to become <em>separate conscious tasks</em>; eventually they fuse into a single felt sense.</p>",
        "<h3>Bài Tập: Ba Bản Đồ Trong Một Phút</h3>"
        "<p>Đặt đồng hồ một phút. Đứng ở tư thế cung nhẹ. Trong 20 giây, nói to trọng lượng của bạn ở đâu. Trong 20 giây, gọi tên các điểm của bàn chân đang chạm mặt đất. Trong 20 giây, lần theo cột sống từ xương cụt đến đỉnh đầu bằng sự chú ý. Bài tập ép ba bản đồ trở thành <em>các nhiệm vụ ý thức riêng biệt</em>; cuối cùng chúng hợp nhất thành một cảm giác đơn nhất.</p>",
    ),
    (
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Master Cue</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Weight. Ground. Alignment. One body, three maps."</p>',
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Câu Nhắc Tổng</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Trọng lượng. Mặt đất. Trục. Một cơ thể, ba bản đồ."</p>',
    ),
],

"vo-vi-tru-the": [
    (
        "<h3>The Stance and the Post</h3>"
        "<p>The <strong>Wu Wei (Vô Vi) Stance</strong> is the basic standing position: feet shoulder-width apart, knees soft, tailbone dropping, crown suspended. The <strong>Standing Post (Trụ Thế / Zhan Zhuang)</strong> is what you do in that stance: stand, breathe, wait. Both look identical from the outside. The first is a position; the second is a practice.</p>"
        "<p>The Wu Wei stance without Zhan Zhuang is just posture. Zhan Zhuang without the Wu Wei stance is just standing. Together they form the seed of the entire art. Five minutes a day for a month produces visible changes in any beginner.</p>",
        "<h3>Tư Thế Và Trụ Thế</h3>"
        "<p><strong>Tư Thế Vô Vi</strong> là vị trí đứng cơ bản: hai chân rộng bằng vai, gối mềm, xương cụt hạ, đỉnh đầu treo. <strong>Trụ Thế (站樁)</strong> là điều bạn làm ở tư thế đó: đứng, thở, chờ. Cả hai trông giống nhau từ bên ngoài. Cái thứ nhất là vị trí; cái thứ hai là thực hành.</p>"
        "<p>Tư thế Vô Vi không có Trụ Thế chỉ là tư thế. Trụ Thế không có tư thế Vô Vi chỉ là đứng. Cùng nhau chúng tạo thành hạt giống của toàn bộ môn võ. Năm phút mỗi ngày trong một tháng tạo ra thay đổi rõ ràng ở bất kỳ người mới nào.</p>",
    ),
    (
        "<h3>What Happens in Five Minutes</h3>"
        "<p>In the first minute the body settles. In the second minute the mind starts to wander. In the third minute you notice the wandering and bring yourself back. In the fourth minute the wandering happens again. In the fifth minute you notice it again. This is the entire practice &mdash; settling, wandering, returning. <em>There is nothing else to do.</em> The next five minutes are the same, only the wandering is subtler.</p>",
        "<h3>Chuyện Gì Xảy Ra Trong Năm Phút</h3>"
        "<p>Phút đầu tiên cơ thể an trụ. Phút thứ hai tâm bắt đầu lang thang. Phút thứ ba bạn nhận ra sự lang thang và đưa mình trở lại. Phút thứ tư sự lang thang xảy ra lại. Phút thứ năm bạn lại nhận ra nó. Đây là toàn bộ thực hành &mdash; an trụ, lang thang, trở lại. <em>Không có gì khác để làm.</em> Năm phút tiếp theo cũng vậy, chỉ là sự lang thang tinh tế hơn.</p>",
    ),
    (
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Master Cue</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Settle. Wander. Return. Settle. Wander. Return."</p>',
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Câu Nhắc Tổng</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"An trụ. Lang thang. Trở lại. An trụ. Lang thang. Trở lại."</p>',
    ),
],

"lay": [
    (
        "<h3>Rollback as Yielding</h3>"
        "<p><strong>Lu (Lãy / 履)</strong> is the second of the Eight Methods. Where Peng is the sphere of readiness around the body, Lu is the act of <em>yielding</em> to the opponent's force in such a way that it follows its own momentum into emptiness. Lu does not block. Lu does not push. Lu redirects.</p>"
        "<p>The mechanism: as the opponent's energy arrives, your hands and arms create a sideways curve. Their force follows the curve. By the time they realize what is happening, their balance is moving past their center of gravity, and a small additional push (Ji) or pull (An) finishes them. Four ounces redirecting a thousand pounds.</p>",
        "<h3>Lãy Là Nhường</h3>"
        "<p><strong>Lãy (履)</strong> là phương pháp thứ hai của Bát Pháp. Trong khi Phòng là khối cầu sẵn sàng quanh cơ thể, Lãy là hành động <em>nhường</em> trước lực đối phương theo cách khiến nó theo chính quán tính của nó vào khoảng trống. Lãy không chặn. Lãy không đẩy. Lãy chuyển hướng.</p>"
        "<p>Cơ chế: khi năng lượng đối phương đến, tay và cánh tay bạn tạo một đường cong sang bên. Lực của họ theo đường cong. Đến lúc họ nhận ra chuyện gì đang xảy ra, thăng bằng của họ đã đi qua trọng tâm, và một cú đẩy nhỏ (Tỳ) hoặc kéo (Án) hoàn thành. Bốn lạng chuyển hướng nghìn cân.</p>",
    ),
    (
        "<h3>Three Common Errors</h3>"
        "<p><strong>Pulling instead of yielding</strong> &mdash; the body retreats actively; the opponent senses the pull and braces. <strong>Yielding with arms only</strong> &mdash; the upper body complies but the feet and waist stay rigid; the opponent's force runs into the rigidity and bounces back. <strong>Yielding too fast</strong> &mdash; the body outpaces the opponent's arrival, the curve is empty when they arrive, they read the trap and adjust.</p>",
        "<h3>Ba Lỗi Phổ Biến</h3>"
        "<p><strong>Kéo thay vì nhường</strong> &mdash; cơ thể rút lui tích cực; đối phương cảm nhận lực kéo và chống lại. <strong>Nhường bằng tay</strong> &mdash; phần trên tuân theo nhưng chân và eo vẫn cứng; lực đối phương chạm vào sự cứng và bật lại. <strong>Nhường quá nhanh</strong> &mdash; cơ thể vượt trước sự đến của đối phương, đường cong trống rỗng khi họ đến, họ đọc được bẫy và điều chỉnh.</p>",
    ),
    (
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Master Cue</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Don&rsquo;t block. Don&rsquo;t push. Redirect."</p>',
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Câu Nhắc Tổng</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Đừng chặn. Đừng đẩy. Hãy chuyển hướng."</p>',
    ),
],

"24-thuc-tong-quat": [
    (
        "<h3>Why the 24-Form Exists</h3>"
        "<p>The <strong>24-Form (Nhị Thập Tứ Thức)</strong> was standardised by the Chinese Sports Commission in 1956, distilled from the Yang tradition into a complete beginner's curriculum. It is not the deepest practice in the art. It is the <em>easiest entry point</em> that still carries the full structure of Tai Chi: 8 Gates, 5 Steps, soft-hard alternation, breath coordination, weight transfer. It completes in 5&ndash;8 minutes and can be practised almost anywhere.</p>"
        "<p>Most Western students start here. Many stay here for years. A few move on to the 42-form, the 48-form, the Yang 85, or the Chen old-frame. All of those start from the 24.</p>",
        "<h3>Tại Sao Có 24 Thức</h3>"
        "<p><strong>24 Thức (Nhị Thập Tứ Thức)</strong> được Ủy ban Thể thao Trung Quốc chuẩn hóa năm 1956, cô đọng từ truyền thống Dương thành chương trình cho người mới hoàn chỉnh. Đó không phải thực hành sâu nhất trong môn. Đó là <em>điểm vào dễ nhất</em> vẫn mang cấu trúc đầy đủ của Thái Cực Quyền: Bát Môn, Ngũ Bộ, luân phiên mềm-cứng, phối hợp hơi thở, chuyển trọng lượng. Hoàn thành trong 5&ndash;8 phút và có thể tập ở hầu hết mọi nơi.</p>"
        "<p>Hầu hết học viên phương Tây bắt đầu ở đây. Nhiều người ở đây nhiều năm. Một số chuyển sang 42 thức, 48 thức, Dương 85, hoặc Trần Lão Gia. Tất cả đều bắt đầu từ 24.</p>",
    ),
    (
        "<h3>The Six Phrases</h3>"
        "<p>The 24 movements cluster into six phrases that share an internal logic:</p>"
        "<ol>"
        "<li><strong>Opening (1&ndash;4)</strong>: Commencing Form, Parting the Wild Horse's Mane, White Crane Spreads Wings, Brush Knee and Twist Step. The body settles and the breath finds the dantian.</li>"
        "<li><strong>Lateral (5&ndash;7)</strong>: Strum the Lute, Step Back and Repulse the Monkey, Grasp the Bird's Tail (left). Side-to-side weight transfer becomes natural.</li>"
        "<li><strong>Vertical (8&ndash;9)</strong>: Grasp the Bird's Tail (right), Single Whip. The body learns to organise forward energy through the waist.</li>"
        "<li><strong>Cloud (10&ndash;13)</strong>: Cloud Hands, High Pat on Horse, Right Heel Kick, Strike with Both Fists. The diagonal pathways open.</li>"
        "<li><strong>Balance (14&ndash;19)</strong>: Turn and Kick with Left Heel, Snake Creeps Down Left, Snake Creeps Down Right, Golden Rooster Stands on One Leg Left, Golden Rooster Right, Lotus Kick. Single-leg balance integrates.</li>"
        "<li><strong>Closing (20&ndash;24)</strong>: Bow the Arrow, Flash the Arm, Step Forward and Deflect Downward, Cross Hands, Closing Form. The energy returns to centre.</li>"
        "</ol>",
        "<h3>Sáu Cụm</h3>"
        "<p>24 chuyển động phân thành sáu cụm có logic nội tại chung:</p>"
        "<ol>"
        "<li><strong>Khai (1&ndash;4)</strong>: Khởi Thức, Dã Mã Phân Tung, Bạch Hạc Lượng Sí, Lâu Tất Ảo Bộ. Thân an trụ và hơi thở tìm Đan Điền.</li>"
        "<li><strong>Bên (5&ndash;7)</strong>: Thủ Huy Tỳ Bà, Đảo Toản Hầu, Tả Lãm Tước Vỹ. Chuyển trọng lượng sang bên trở nên tự nhiên.</li>"
        "<li><strong>Dọc (8&ndash;9)</strong>: Hữu Lãm Tước Vỹ, Đơn Tiên. Thân học tổ chức năng lượng tới qua eo.</li>"
        "<li><strong>Mây (10&ndash;13)</strong>: Vân Thủ, Cao Thám Mã, Hữu Đạp Cước, Song Phong Quán Nhĩ. Con đường chéo mở ra.</li>"
        "<li><strong>Thăng Bằng (14&ndash;19)</strong>: Tả Đạp Liên Hoàn Thối, Tả Thế Xà Điện, Hữu Thế Xà Điện, Tả Kim Kê Độc Lập, Hữu Kim Kê Độc Lập, Đạp Liên Hoàn Thối. Thăng bằng một chân tích hợp.</li>"
        "<li><strong>Thu (20&ndash;24)</strong>: Lộ Mã Lộc Chuyển Thân, Thương Quyên Lộc, Tiến Bộ Chuyển Đả, Thập Tự Thủ, Thu Thức. Năng lượng trở về trung tâm.</li>"
        "</ol>",
    ),
    (
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Master Cue</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Six phrases. One form. Twenty-four movements."</p>',
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Câu Nhắc Tổng</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Sáu cụm. Một bài. Hai mươi bốn thức."</p>',
    ),
],

"tho-dan-dien": [
    (
        "<h3>What Dan Tian Breathing Is</h3>"
        "<p><strong>Dan Tian breathing</strong> means breathing into the lower abdomen &mdash; not the chest, not the shoulders, but the area roughly 3 cm below the navel, deep inside the pelvis. On inhale the belly expands outward; on exhale it draws back in. Most adults have lost this pattern (stress, posture, sedentary habits). Children breathe this way naturally. Tai Chi restores it.</p>"
        "<p>The lower dantian is the body's centre of mass. Breathing there puts the breath where the weight is &mdash; which makes every movement initiated from the centre automatically more stable than one initiated from the chest.</p>",
        "<h3>Thở Đan Điền Là Gì</h3>"
        "<p><strong>Thở Đan Điền</strong> nghĩa là thở vào bụng dưới &mdash; không phải ngực, không phải vai, mà là vùng khoảng 3 cm dưới rốn, sâu trong khung chậu. Khi hít vào, bụng phồng ra ngoài; khi thở ra, bụng rút vào. Hầu hết người lớn đã mất mô hình này (căng thẳng, tư thế, thói quen ít vận động). Trẻ em thở theo cách này một cách tự nhiên. Thái Cực Quyền phục hồi nó.</p>"
        "<p>Đan Điền dưới là trọng tâm của cơ thể. Thở ở đó đặt hơi thở ở nơi trọng lượng &mdash; điều này làm cho mọi chuyển động khởi phát từ trung tâm tự động ổn định hơn một chuyển động khởi phát từ ngực.</p>",
    ),
    (
        "<h3>Drill for the First Two Weeks</h3>"
        "<p>Lying on the back, place one hand on the lower abdomen. Breathe in through the nose for 4 seconds; the hand should rise. Breathe out through the mouth for 6 seconds; the hand should fall. After 10 cycles, switch to sitting. After 10 more, switch to standing. After two weeks of this daily, the pattern is established enough to use in the form.</p>",
        "<h3>Bài Tập Cho Hai Tuần Đầu</h3>"
        "<p>Nằm ngửa, đặt một tay lên bụng dưới. Thở vào qua mũi 4 giây; tay nên nâng lên. Thở ra qua miệng 6 giây; tay nên hạ xuống. Sau 10 chu kỳ, chuyển sang ngồi. Sau 10 chu kỳ nữa, chuyển sang đứng. Sau hai tuần làm hằng ngày, mô hình đã đủ thiết lập để dùng trong bài quyền.</p>",
    ),
    (
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Master Cue</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Breath goes where the weight is."</p>',
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Câu Nhắc Tổng</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Hơi thở đi đến nơi trọng lượng ở."</p>',
    ),
],

"ba-mo-neo": [
    (
        "<h3>The 3-Anchor Check</h3>"
        "<p>The three anchors are <strong>weight</strong>, <strong>breath</strong>, and <strong>intention</strong>. Run them every few minutes during practice. Where is my weight right now &mdash; forward, back, left, right? Where is my breath &mdash; high in the chest, low in the dantian, somewhere in between? Where is my intention &mdash; on the movement in front of me, on the next movement, wandering in thought?</p>"
        "<p>The check is a 5-second audit. It does not interrupt the practice &mdash; it deepens it. The anchors become internal GPS coordinates the body uses to organise itself.</p>",
        "<h3>Kiểm Tra 3 Mỏ Neo</h3>"
        "<p>Ba mỏ neo là <strong>trọng lượng</strong>, <strong>hơi thở</strong>, và <strong>ý chí</strong>. Chạy qua chúng vài phút một lần trong thực hành. Trọng lượng của tôi đang ở đâu &mdash; trước, sau, trái, phải? Hơi thở của tôi ở đâu &mdash; cao trong ngực, thấp trong Đan Điền, đâu đó ở giữa? Ý chí của tôi ở đâu &mdash; trên chuyển động trước mặt tôi, trên chuyển động tiếp theo, lang thang trong suy nghĩ?</p>"
        "<p>Việc kiểm tra là một cuộc kiểm toán 5 giây. Nó không làm gián đoạn thực hành &mdash; nó làm sâu nó. Các mỏ neo trở thành tọa độ GPS nội tại mà cơ thể dùng để tự tổ chức.</p>",
    ),
    (
        "<h3>The 3-Question Diagnostic</h3>"
        "<p>If the form feels off, run three questions in order:</p>"
        "<ol>"
        "<li><strong>Am I holding tension I don't need?</strong> &mdash; if yes, release the shoulder, jaw, lower back, or wherever the tension is. Try the movement again.</li>"
        "<li><strong>Am I moving from the waist or from the limbs?</strong> &mdash; if from the limbs, slow down and find the waist. Try the movement again.</li>"
        "<li><strong>Is the breath synchronized with the movement?</strong> &mdash; if not, separate breath and movement for a moment, then re-attach them. Try the movement again.</li>"
        "</ol>"
        "<p>Almost every form issue resolves through one of these three questions.</p>",
        "<h3>Chẩn Đoán 3 Câu Hỏi</h3>"
        "<p>Nếu bài quyền có cảm giác sai, chạy ba câu hỏi theo thứ tự:</p>"
        "<ol>"
        "<li><strong>Tôi có đang giữ căng thẳng mà không cần không?</strong> &mdash; nếu có, thả vai, hàm, lưng dưới, hoặc bất cứ nơi nào căng. Thử chuyển động lại.</li>"
        "<li><strong>Tôi đang di chuyển từ eo hay từ tứ chi?</strong> &mdash; nếu từ tứ chi, chậm lại và tìm eo. Thử chuyển động lại.</li>"
        "<li><strong>Hơi thở có đồng bộ với chuyển động không?</strong> &mdash; nếu không, tách hơi thở và chuyển động trong một khoảnh khắc, rồi gắn lại. Thử chuyển động lại.</li>"
        "</ol>"
        "<p>Gần như mọi vấn đề của bài quyền được giải quyết qua một trong ba câu hỏi này.</p>",
    ),
    (
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Master Cue</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Three anchors. Three questions. One practice."</p>',
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Câu Nhắc Tổng</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Ba mỏ neo. Ba câu hỏi. Một thực hành."</p>',
    ),
],

"co-the-50-cong-cu": [
    (
        "<h3>Why the 50+ Body Is Perfect</h3>"
        "<p>The 50+ body is not a diminished 30-year-old body. It is a different instrument &mdash; one that Tai Chi was essentially designed for. The art's slow pace matches a metabolism that no longer tolerates explosive training. Its attention to breath supports the cardiovascular system as arteries stiffen. Its balance work prevents the falls that are the leading cause of injury death in older adults. Its weight-bearing slow movements maintain bone density better than moderate-impact exercise.</p>"
        "<p>Most important: the 50+ body has had decades to accumulate <em>proprioceptive wisdom</em>. The nervous system is slower but more integrated. A 50-year-old who has played tennis, raised children, navigated a career, and stayed curious has a body that knows how to <em>learn</em>. Tai Chi simply gives that learning a daily structure.</p>",
        "<h3>Tại Sao Cơ Thể 50+ Là Hoàn Hảo</h3>"
        "<p>Cơ thể 50+ không phải cơ thể 30 tuổi bị suy giảm. Đó là một nhạc cụ khác &mdash; một nhạc cụ mà Thái Cực Quyền về cơ bản được thiết kế cho. Nhịp độ chậm của môn khớp với trao đổi chất không còn chịu được tập huấn nổ. Sự chú ý đến hơi thở hỗ trợ hệ tim mạch khi động mạch cứng lại. Công việc thăng bằng ngăn ngừa các cú té &mdash; nguyên nhân hàng đầu gây tử vong do chấn thương ở người lớn tuổi. Các chuyển động chậm chịu tải trọng duy trì mật độ xương tốt hơn tập cường độ trung bình.</p>"
        "<p>Quan trọng nhất: cơ thể 50+ đã có hàng thập kỷ để tích lũy <em>trí tuệ cảm giác bản thể</em>. Hệ thần kinh chậm hơn nhưng tích hợp hơn. Một người 50 tuổi đã chơi tennis, nuôi con, điều hành sự nghiệp, và giữ sự tò mò có một cơ thể biết cách <em>học</em>. Thái Cực Quyền chỉ đơn giản cho sự học đó một cấu trúc hằng ngày.</p>",
    ),
    (
        "<h3>The Ten-Year Arc</h3>"
        "<p>If you start Tai Chi at 52 and practise daily for a decade, expect this arc: <strong>Year 1&ndash;2</strong> &mdash; learn the form, build the habit, feel balance and stress improve. <strong>Year 3&ndash;5</strong> &mdash; understand the principles, begin push hands, blood pressure and sleep noticeably improve. <strong>Year 6&ndash;10</strong> &mdash; Tai Chi becomes invisible in your life. You are 62 with the fitness, flexibility and mental sharpness of someone in their 50s. People stop asking when you retired.</p>",
        "<h3>Cung 10 Năm</h3>"
        "<p>Nếu bạn bắt đầu Thái Cực Quyền ở tuổi 52 và tập hằng ngày trong một thập kỷ, hãy kỳ vọng cung này: <strong>Năm 1&ndash;2</strong> &mdash; học bài quyền, xây dựng thói quen, cảm nhận thăng bằng và căng thẳng cải thiện. <strong>Năm 3&ndash;5</strong> &mdash; hiểu các nguyên lý, bắt đầu Thôi Thủ, huyết áp và giấc ngủ cải thiện rõ rệt. <strong>Năm 6&ndash;10</strong> &mdash; Thái Cực Quyền trở nên vô hình trong cuộc sống bạn. Bạn 62 tuổi với thể lực, sự linh hoạt và sắc bén tinh thần của người 50. Mọi người ngừng hỏi khi nào bạn nghỉ hưu.</p>",
    ),
    (
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Master Cue</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"The 50+ body is the body Tai Chi was designed for."</p>',
        '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Câu Nhắc Tổng</h3>'
        '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Cơ thể 50+ là cơ thể mà Thái Cực Quyền được thiết kế cho."</p>',
    ),
],


}


def build_topic(slug, en_title, vi_title):
    en_dir = REPO / "en" / "techniques" / slug
    vi_dir = REPO / "vi" / "techniques" / slug
    en_dir.mkdir(parents=True, exist_ok=True)
    vi_dir.mkdir(parents=True, exist_ok=True)

    cards = CONTENT[slug]
    en_cards = "".join(
        f'    <section class="technique-card">\n  {en_card}\n    </section>\n'
        for en_card, _ in cards
    )
    vi_cards = "".join(
        f'    <section class="technique-card">\n  {vi_card}\n    </section>\n'
        for _, vi_card in cards
    )

    (en_dir / "index.html").write_text(
        page_shell("en", en_title, slug).replace("{body}", en_cards),
        encoding='utf-8'
    )
    (vi_dir / "index.html").write_text(
        page_shell("vi", vi_title, slug).replace("{body}", vi_cards),
        encoding='utf-8'
    )
    print(f"  built {slug}")


def update_techniques_index():
    """Replace the existing 'New Topics' block (or add one) with the full list."""
    en_block = ['\n    <section id="topics" class="technique-section">']
    en_block.append('        <h2>New Topics · Chủ Đề Mở Rộng</h2>')
    en_block.append('        <p style="color:var(--gray-mid); font-style:italic;">In-depth technique notes drawn from the <em>3.0 Beginner Practice Guide</em> &mdash; 20 topics across standing, breath, stepping, body, and pitfalls.</p>')
    for slug, en_title, _ in TOPICS:
        en_block.append(f'        <div class="technique-card"><h3><a href="/en/techniques/{slug}/">{en_title}</a></h3></div>')
    en_block.append('    </section>\n')
    en_new = '\n'.join(en_block)

    vi_block = ['\n    <section id="topics" class="technique-section">']
    vi_block.append('        <h2>Chủ Đề Mở Rộng · New Topics</h2>')
    vi_block.append('        <p style="color:var(--gray-mid); font-style:italic;">Ghi chép kỹ thuật chuyên sâu từ <em>Cẩm Nang 3.0 Beginner</em> &mdash; 20 chủ đề: trụ thế, hơi thở, bước chân, cơ thể, và lỗi thường gặp.</p>')
    for slug, _, vi_title in TOPICS:
        vi_block.append(f'        <div class="technique-card"><h3><a href="/vi/techniques/{slug}/">{vi_title}</a></h3></div>')
    vi_block.append('    </section>\n')
    vi_new = '\n'.join(vi_block)

    for idx_path, block in [
        (REPO / "en" / "techniques" / "index.html", en_new),
        (REPO / "vi" / "techniques" / "index.html", vi_new),
    ]:
        text = idx_path.read_text(encoding='utf-8')
        # Replace existing topics section if present, else insert before </article>
        m = re.search(r'<section id="topics"[^>]*>.*?</section>\s*', text, re.DOTALL)
        if m:
            new_text = text[:m.start()] + block.strip() + '\n\n' + text[m.end():]
            idx_path.write_text(new_text, encoding='utf-8')
            print(f"  replaced topics block in {idx_path.name}")
            continue
        m2 = re.search(r'</article>', text)
        if not m2:
            print(f"  WARN: no </article> in {idx_path}")
            continue
        new_text = text[:m2.start()] + block + text[m2.start():]
        idx_path.write_text(new_text, encoding='utf-8')
        print(f"  appended topics block to {idx_path.name}")


if __name__ == "__main__":
    print("--- Building 10 topic pages (curated) ---")
    for slug, en_title, vi_title in TOPICS:
        build_topic(slug, en_title, vi_title)
    print("--- Updating techniques index ---")
    update_techniques_index()
