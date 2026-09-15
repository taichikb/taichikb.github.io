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
    <p>Built with ❤️ for the Vietnamese Tai Chi community 🎾 by Henry Phạm</p>
    <p>Trang web này được xây dựng với ❤️ cho cộng đồng Thiền Võ Việt Nam 🎾 by Henry Phạm</p>
</footer>

</body>
</html>
'''


# Slugs + titles
TOPICS = [
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
    en_block = ['\n    <section id="topics" class="technique-section">']
    en_block.append('        <h2>New Topics · Chủ Đề Mở Rộng</h2>')
    en_block.append('        <p style="color:var(--gray-mid); font-style:italic;">In-depth technique notes drawn from the <em>3.0 Beginner Practice Guide</em>.</p>')
    for slug, en_title, _ in TOPICS:
        en_block.append(f'        <div class="technique-card"><h3><a href="/en/techniques/{slug}/">{en_title}</a></h3></div>')
    en_block.append('    </section>\n')
    en_new = '\n'.join(en_block)

    vi_block = ['\n    <section id="topics" class="technique-section">']
    vi_block.append('        <h2>Chủ Đề Mở Rộng · New Topics</h2>')
    vi_block.append('        <p style="color:var(--gray-mid); font-style:italic;">Ghi chép kỹ thuật chuyên sâu từ <em>Cẩm Nang 3.0 Beginner</em>.</p>')
    for slug, _, vi_title in TOPICS:
        vi_block.append(f'        <div class="technique-card"><h3><a href="/vi/techniques/{slug}/">{vi_title}</a></h3></div>')
    vi_block.append('    </section>\n')
    vi_new = '\n'.join(vi_block)

    for idx_path, block in [
        (REPO / "en" / "techniques" / "index.html", en_new),
        (REPO / "vi" / "techniques" / "index.html", vi_new),
    ]:
        text = idx_path.read_text(encoding='utf-8')
        if 'id="topics"' in text:
            print(f"  skip {idx_path.name}: topics block already present")
            continue
        m = re.search(r'</article>', text)
        if not m:
            print(f"  WARN: no </article> in {idx_path}")
            continue
        new_text = text[:m.start()] + block + text[m.start():]
        idx_path.write_text(new_text, encoding='utf-8')
        print(f"  updated {idx_path.name}: appended topics section")


if __name__ == "__main__":
    print("--- Building 10 topic pages (curated) ---")
    for slug, en_title, vi_title in TOPICS:
        build_topic(slug, en_title, vi_title)
    print("--- Updating techniques index ---")
    update_techniques_index()
