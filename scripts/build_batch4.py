#!/usr/bin/env python3
"""Batch 4 — 10 richer technique-topic pages (EN+VI), 1–2 pages each."""

from pathlib import Path
import re, sys

REPO = Path("D:/Taichi-Health-Finance/Intranet/taichikb_repo")

TAIJI_LOGO = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" class="taiji-logo"><circle cx="100" cy="100" r="98" fill="#ffffff" stroke="#000000" stroke-width="4"/><path d="M 100,2 A 98,98 0 0,1 100,198 A 49,49 0 0,1 100,100 A 49,49 0 0,0 100,2 Z" fill="#000000"/><circle cx="100" cy="51" r="12" fill="#ffffff"/><circle cx="100" cy="149" r="12" fill="#000000"/></svg>'

FOOTER = (
    '<footer class="site-footer">\n'
    '    <p>Built with ❤️ for the Vietnamese Tai Chi community <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="20" height="20" style="vertical-align:-3px;display:inline-block;"><circle cx="100" cy="100" r="98" fill="#ffffff" stroke="#000000" stroke-width="4"/><path d="M 100,2 A 98,98 0 0,1 100,198 A 49,49 0 0,1 100,100 A 49,49 0 0,0 100,2 Z" fill="#000000"/><circle cx="100" cy="51" r="12" fill="#ffffff"/><circle cx="100" cy="149" r="12" fill="#000000"/></svg> bởi Phạm Đức Hải</p>\n'
    '    <p>Trang web này được xây dựng với ❤️ cho cộng đồng Thái Cực Quyền Việt Nam <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="20" height="20" style="vertical-align:-3px;display:inline-block;"><circle cx="100" cy="100" r="98" fill="#ffffff" stroke="#000000" stroke-width="4"/><path d="M 100,2 A 98,98 0 0,1 100,198 A 49,49 0 0,1 100,100 A 49,49 0 0,0 100,2 Z" fill="#000000"/><circle cx="100" cy="51" r="12" fill="#ffffff"/><circle cx="100" cy="149" r="12" fill="#000000"/></svg> bởi Phạm Đức Hải</p>\n'
    '</footer>'
)


def shell(lang, title, slug):
    other_lang = "vi" if lang == "en" else "en"
    other_label = "🇻🇳 Tiếng Việt" if lang == "en" else "🇬🇧 English"
    other_href = f"/{other_lang}/techniques/{slug}/"
    home_href = "/" if lang == "en" else "/vi/"
    if lang == "en":
        nav = [("Home","/"),("Techniques","/en/techniques/"),("Philosophy","/en/philosophy/"),("History","/en/history/"),("Contact","/en/contact/")]
        home_label = "Home"
        tech_label = "Techniques"
    else:
        nav = [("Trang Chủ","/vi/"),("Kỹ Thuật","/vi/techniques/"),("Triết Lý","/vi/philosophy/"),("Lịch Sử","/vi/history/"),("Liên Hệ","/vi/contact/")]
        home_label = "Trang Chủ"
        tech_label = "Kỹ Thuật"
    nav_html = '\n'.join(
        f'<a href="{href}" class="{label.lower().replace(" ","-") if label != "Home" and label != "Trang Chủ" else "home"}">{label}</a>'
        for label, href in nav
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
    <a href="/{lang}/techniques/">← {tech_label}</a>
    <a href="{home_href}" class="home">⌂ {home_label}</a>
    <a href="{other_href}">{other_label} →</a>
</nav>

</main>

{FOOTER}

</body>
</html>
'''


# Topics: each entry contains EN title, VI title, slug, list of (en_html_card, vi_html_card) pairs.
TOPICS = []


def add(slug, en_title, vi_title, cards):
    """cards: list of (en_html_str, vi_html_str)."""
    TOPICS.append((slug, en_title, vi_title, cards))


# ---------- 1. Kinh Khởi Vu Căn ----------
add("kinh-khoi-vu-can",
    "Kình Khởi Vu Căn — Force Originates at the Foot",
    "Kình Khởi Vu Căn — Kình Lực Khởi Từ Chân",
    [
        (
            "<h3>The Classical Statement</h3>"
            "<p>One of the most quoted lines in the internal martial arts is the formula <strong>&ldquo;Kình khởi vu căn, chủ tể vu yêu, hình vu thủ&rdquo;</strong> (劲起于根，主宰于腰，形于手). In English: <em>force originates at the root (the foot), is governed by the waist, and is expressed through the hand</em>. The sentence is short; the implications run deep.</p>"
            "<p>Tai Chi is not a hand art. The hands are the <em>last</em> place force appears. By the time it reaches the fingers, it has travelled through the foot, the ankle, the knee, the hip, the waist, the lower back, the shoulder, the upper arm, the elbow, the forearm, the wrist, and the palm. If any link in this chain is loose, the force leaks before it reaches the hand. If any link is tight, it stops.</p>",

            "<h3>Cổ Câu Kinh Điển</h3>"
            "<p>Một trong những câu được trích dẫn nhiều nhất trong võ thuật nội gia là công thức <strong>&ldquo;Kình khởi vu căn, chủ tể vu yêu, hình vu thủ&rdquo;</strong>. Tạm dịch: <em>kình lực khởi từ chân (căn), được điều khiển bởi eo (yêu), và biểu hiện qua tay (thủ)</em>. Câu ngắn; hàm ý sâu.</p>"
            "<p>Thái Cực Quyền không phải môn võ tay. Tay là nơi <em>cuối cùng</em> kình lực xuất hiện. Khi đến ngón tay, nó đã đi qua chân, cổ chân, đầu gối, hông, eo, lưng dưới, vai, cánh tay trên, khuỷu, cẳng tay, cổ tay, và lòng bàn tay. Nếu bất kỳ mắt xích nào trong chuỗi này lỏng, kình lực rò rỉ trước khi đến tay. Nếu bất kỳ mắt xích nào cứng, nó dừng lại.</p>",
        ),
        (
            "<h3>The Root (Căn)</h3>"
            "<p>The <em>căn</em> in classical usage does not mean only the foot. It means <em>the place where the body meets the ground</em> &mdash; specifically the bubbling-well point (Yongquan, Kidney 1, K1) on the sole of the foot. When the body weight settles into Yongquan and the toes grip the floor lightly, the foot becomes a living root &mdash; capable of pushing, pulling, twisting, or remaining still. The root is what connects the body to the earth so that the earth can push back.</p>"
            "<p>Most beginners have no root because their weight is on the heels. Heels carry weight but cannot push. The weight must come forward into the sole, the toes gripping the ground, and the knees slightly bent. Only then does the foot become a real root.</p>",

            "<h3>Căn (Gốc)</h3>"
            "<p><em>Căn</em> trong sử dụng cổ điển không chỉ có nghĩa là bàn chân. Nó có nghĩa là <em>nơi cơ thể gặp mặt đất</em> &mdash; cụ thể là huyệt Dũng Tuyền (K1) ở lòng bàn chân. Khi trọng lượng cơ thể an xuống Dũng Tuyền và các ngón chân nhẹ nhàng bám đất, bàn chân trở thành một gốc sống &mdash; có khả năng đẩy, kéo, xoay, hoặc đứng yên. Căn là thứ kết nối cơ thể với đất để đất có thể đẩy ngược lại.</p>"
            "<p>Hầu hết người mới không có căn vì trọng lượng ở gót chân. Gót chân mang trọng lượng nhưng không thể đẩy. Trọng lượng phải đưa về phía trước vào lòng bàn chân, các ngón chân bám nhẹ đất, và đầu gối hơi gập. Chỉ khi đó bàn chân mới trở thành căn thật sự.</p>",
        ),
        (
            "<h3>The Waist (Yêu) as Commander</h3>"
            "<p>The waist is the <em>commander</em>, not a passive conduit. Every redirection, every change of direction, every spiral originates here. The waist must be loose enough to rotate freely but stable enough to transmit force from the root to the hands. When the waist is tense, the upper and lower body become two disconnected halves; the hands move, the feet stay, and no force arrives.</p>"
            "<p>Three classical instructions describe waist operation: <strong>turn like a wheel</strong> (rotation must be smooth and continuous), <strong>distinguish left from right</strong> (the waist must know at every moment which side is leading), and <strong>empty the lower back</strong> (no gripping in the lumbar spine; let the spine hang from the crown). When all three are true, the waist becomes the master.</p>",

            "<h3>Eo (Yêu) Làm Chủ Tể</h3>"
            "<p>Eo là <em>chủ tể</em>, không phải ống dẫn thụ động. Mọi sự chuyển hướng, mọi thay đổi phương, mọi xoắn ốc đều khởi phát từ đây. Eo phải đủ lỏng để xoay tự do nhưng đủ ổn định để truyền lực từ căn đến tay. Khi eo căng, thân trên và thân dưới trở thành hai nửa rời nhau; tay di chuyển, chân đứng yên, và không có lực nào đến.</p>"
            "<p>Ba chỉ dẫn cổ điển mô tả vận hành của eo: <strong>xoay như bánh xe</strong> (sự xoay phải mượt mà và liên tục), <strong>phân biệt trái phải</strong> (eo phải biết ở mọi khoảnh khắc bên nào dẫn), và <strong>trống lưng dưới</strong> (không gồng ở cột sống thắt lưng; để cột sống treo từ đỉnh đầu). Khi cả ba đúng, eo trở thành chủ tể.</p>",
        ),
        (
            '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Master Cue</h3>'
            '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Root at the foot. Governed by the waist. Expressed through the hand."</p>',
            '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Câu Nhắc Tổng</h3>'
            '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Kình khởi ở chân. Chủ tể ở eo. Hình thành ở tay."</p>',
        ),
    ])


# ---------- 2. Khop Hang / Song Kua ----------
add("khop-hang-song-kua",
    "Mở Kua — Opening the Hip Joint",
    "Mở Kua — Mở Khớp Háng Nội Gia",
    [
        (
            "<h3>What Kua Is</h3>"
            "<p>The <strong>kua</strong> (胯) is the inguinal fold &mdash; the crease between the front of the hip and the inner thigh. In Tai Chi this small anatomical zone is treated as the master joint of the lower body, more important than the knee, the ankle, or even the hip joint itself. Why? Because the kua is where the leg meets the torso. If the kua is closed, the legs and torso are two separate systems. If the kua is open, they become one.</p>"
            "<p>Opening the kua means releasing the deep hip rotators (psoas, iliacus, obturators, gemelli, piriformis) so that the femur can sit in the hip socket with room to rotate. A closed kua pulls the pelvis forward, flattens the lumbar curve, restricts the hip joint, and forces the knees to do the work the hips should be doing. This is one of the most common sources of knee pain in Tai Chi.</p>",

            "<h3>Kua Là Gì</h3>"
            "<p><strong>Kua (胯)</strong> là nếp bẹn &mdash; nếp gấp giữa phía trước hông và mặt trong đùi. Trong Thái Cực Quyền, vùng giải phẫu nhỏ này được coi là khớp chủ của thân dưới, quan trọng hơn gối, cổ chân, hay thậm chí chính khớp háng. Tại sao? Bởi vì kua là nơi chân gặp thân. Nếu kua đóng, chân và thân là hai hệ thống riêng biệt. Nếu kua mở, chúng trở thành một.</p>"
            "<p>Mở kua có nghĩa là giải phóng các cơ xoay sâu của hông (psoas, iliacus, obturators, gemelli, piriformis) để xương đùi có thể ngồi trong ổ cối với không gian xoay. Kua đóng kéo khung chậu về phía trước, làm phẳng đường cong thắt lưng, hạn chế khớp háng, và ép đầu gối phải làm công việc mà hông nên làm. Đây là một trong những nguồn đau gối phổ biến nhất trong Thái Cực Quyền.</p>",
        ),
        (
            "<h3>Three Tests for Closed Kua</h3>"
            "<p>Stand in a slight bow stance and try these three tests:</p>"
            "<ol>"
            "<li><strong>The Toe Touch</strong>: can you keep your back straight and touch your toes without rounding the lumbar spine? If you cannot, the kua is closed and the lower back is doing the job the hips should do.</li>"
            "<li><strong>The Lateral Squat</strong>: stand with feet wide, sit to one side (right knee bent, left leg straight), and see if your right heel can stay grounded while your pelvis drops below the right knee. If the heel lifts or the knee hurts, the kua is closed.</li>"
            "<li><strong>The Bow-Stance Squat</strong>: drop into a deep bow stance (right knee bent, left leg straight) and see if you can keep your torso vertical without leaning forward. Closed kua forces the torso to lean forward to keep balance.</li>"
            "</ol>"
            "<p>None of these tests need to be done deeply the first time. They are diagnostic: they show you what your current range is so you can work on opening it.</p>",

            "<h3>Ba Kiểm Tra Kua Đóng</h3>"
            "<p>Đứng ở tư thế cung nhẹ và thử ba kiểm tra này:</p>"
            "<ol>"
            "<li><strong>Chạm Ngón Chân</strong>: bạn có thể giữ lưng thẳng và chạm ngón chân mà không cong cột sống thắt lưng? Nếu không, kua đã đóng và lưng dưới đang làm công việc mà hông nên làm.</li>"
            "<li><strong>Tư Thế Squat Bên</strong>: đứng với chân rộng, ngồi sang một bên (gối phải gập, chân trái thẳng), và xem gót phải có thể giữ chạm đất trong khi khung chậu hạ xuống dưới gối phải. Nếu gót nâng lên hoặc gối đau, kua đã đóng.</li>"
            "<li><strong>Tư Thế Cung Sâu</strong>: hạ xuống tư thế cung sâu (gối phải gập, chân trái thẳng) và xem bạn có thể giữ thân thẳng đứng mà không nghiêng về phía trước. Kua đóng ép thân phải nghiêng về phía trước để giữ thăng bằng.</li>"
            "</ol>"
            "<p>Không cần kiểm tra nào trong số này cần thực hiện sâu lần đầu. Chúng là chẩn đoán: chúng cho thấy phạm vi hiện tại của bạn để bạn có thể làm việc để mở rộng nó.</p>",
        ),
        (
            "<h3>Three Drills to Open Kua</h3>"
            "<p><strong>1. The Deep Squat Hold</strong>: stand with feet shoulder-width-plus, hold onto a door frame for balance, and lower into a deep squat with heels grounded. Hold 1&ndash;2 minutes. The first weeks will feel impossible; within a month, real progress appears. <strong>2. The Frog Stretch</strong>: from hands-and-knees, slide the knees wide and let the pelvis drop back toward the heels. Hold 90 seconds. Repeat. <strong>3. The Standing Bow</strong>: in a deep right bow stance, slowly shift weight back toward the left foot without lifting the right toes. The right kua opens as the weight retreats; the left kua closes as the weight arrives. Repeat 10 times each side.</p>"
            "<p>None of these drills are Tai Chi forms. They are preparation. After a month of daily drilling, the form itself becomes easier &mdash; the kua is already open when you arrive.</p>",

            "<h3>Ba Bài Tập Mở Kua</h3>"
            "<p><strong>1. Giữ Squat Sâu</strong>: đứng với chân rộng hơn vai, vịn khung cửa để thăng bằng, và hạ xuống squat sâu với gót chân chạm đất. Giữ 1&ndash;2 phút. Những tuần đầu sẽ cảm thấy không thể; trong một tháng, tiến bộ thực sự xuất hiện. <strong>2. Tư Thế Ếch</strong>: từ tư thế tay-gối, trượt hai gối rộng ra và để khung chậu rơi về phía gót chân. Giữ 90 giây. Lặp lại. <strong>3. Cung Đứng</strong>: ở tư thế cung phải sâu, từ từ chuyển trọng lượng về phía chân trái mà không nâng các ngón chân phải. Kua phải mở khi trọng lượng rút lui; kua trái đóng khi trọng lượng đến. Lặp lại 10 lần mỗi bên.</p>"
            "<p>Không bài tập nào trong số này là bài quyền Thái Cực. Chúng là sự chuẩn bị. Sau một tháng tập hằng ngày, bài quyền trở nên dễ hơn &mdash; kua đã mở khi bạn bắt đầu.</p>",
        ),
        (
            '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Master Cue</h3>'
            '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Open the kua. The legs become one with the torso. The knees stop hurting."</p>',
            '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Câu Nhắc Tổng</h3>'
            '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Mở kua. Chân và thân thành một. Gối ngừng đau."</p>',
        ),
    ])


# ---------- 3. Triền Ty Kinh ----------
add("trien-ty-kinh",
    "Triền Ty Kình — The Silk-Reeling Force",
    "Triền Ty Kình — Kình Lực Cuộn Tơ",
    [
        (
            "<h3>What Silk Reeling Is</h3>"
            "<p><strong>Chân Tư (纏絲) — silk reeling</strong> — is the spiral motion that underlies every Tai Chi movement. The image is precise: a silkworm drawing silk from its cocoon produces a continuous, spiralling thread. The Tai Chi body, in motion, produces a continuous, spiralling force. Every joint is rotating slightly; every segment is winding or unwinding; no part of the body translates in a straight line.</p>"
            "<p>Silk reeling is most characteristic of the <strong>Chen style</strong>, where it is treated as the source of all power. It is also present in Yang style (more subtly), Wu style, and Sun style. Even forms that look linear are, on close inspection, built from compound rotations: a push that looks straight actually contains a small spiral of the waist, the shoulder, the forearm, and the wrist.</p>",

            "<h3>Triền Ty Là Gì</h3>"
            "<p><strong>Chân Tư (纏絲) — cuộn tơ</strong> — là chuyển động xoắn ốc nằm bên dưới mọi chuyển động Thái Cực Quyền. Hình ảnh chính xác: con tằm rút tơ từ kén tạo ra một sợi tơ liên tục, xoắn ốc. Cơ thể Thái Cực Quyền, trong chuyển động, tạo ra lực liên tục, xoắn ốc. Mọi khớp đều xoay nhẹ; mọi đoạn đều cuộn hoặc tháo; không phần nào của cơ thể tịnh tiến theo đường thẳng.</p>"
            "<p>Triền ty đặc trưng nhất cho <strong>trường phái Trần</strong>, nơi nó được coi là nguồn gốc của mọi lực. Nó cũng hiện diện trong trường phái Dương (tinh tế hơn), Ngô thức, và Tôn thức. Ngay cả những động tác trông thẳng cũng, khi quan sát kỹ, được xây từ các xoay ghép: một cú đẩy trông thẳng thực sự chứa một xoắn nhỏ của eo, vai, cẳng tay, và cổ tay.</p>",
        ),
        (
            "<h3>Why Silk Reeling Generates Power</h3>"
            "<p>Linear force is delivered by linear muscles &mdash; the bicep curls the arm, the quad extends the knee. These muscles produce force quickly but in small amounts. They fatigue fast. They are dominant in external martial arts.</p>"
            "<p>Spiral force is delivered by the <strong>connective tissue web</strong> &mdash; the fascia, tendons, and aponeuroses that wrap every muscle and link every bone. The connective tissue web stores energy under load and releases it under release, like an elastic band. A spiral engages the entire web at once, multiplying the force many times beyond what any single muscle could produce. This is why Tai Chi generates more power than its speed suggests. The web is doing most of the work.</p>"
            "<p>More importantly, the web does not fatigue quickly. It is metabolically cheap. A Tai Chi practitioner can perform for hours because most of the work is being done by elastic recoil rather than muscular contraction. The slow, spiral form is not slow because it is easy. It is slow because that speed is the most metabolically efficient way to engage the entire connective tissue web.</p>",

            "<h3>Tại Sao Triền Ty Tạo Ra Lực</h3>"
            "<p>Lực thẳng được tạo ra bởi các cơ thẳng &mdash; bắp tay cuộn cánh tay, đùi trước duỗi gối. Các cơ này tạo lực nhanh nhưng với lượng nhỏ. Chúng mệt nhanh. Chúng chiếm ưu thế trong võ thuật bên ngoài.</p>"
            "<p>Lực xoắn ốc được tạo ra bởi <strong>mạng lưới mô liên kết</strong> &mdash; cân mạc, gân, và màng bao bọc mọi cơ và liên kết mọi xương. Mạng lưới mô liên kết lưu trữ năng lượng dưới tải và giải phóng khi tháo, như một dây thun. Một xoắn ốc gắn toàn bộ mạng lưới cùng một lúc, nhân lực lên nhiều lần so với bất kỳ cơ đơn lẻ nào có thể tạo ra. Đây là lý do Thái Cực Quyền tạo ra nhiều lực hơn tốc độ của nó gợi ý. Mạng lưới đang làm phần lớn công việc.</p>"
            "<p>Quan trọng hơn, mạng lưới không mệt nhanh. Nó rẻ về trao đổi chất. Một người tập Thái Cực Quyền có thể thực hành hàng giờ vì phần lớn công việc được thực hiện bởi sự đàn hồi thay vì co cơ. Hình thức xoắn chậm không chậm vì dễ. Nó chậm vì tốc độ đó là cách hiệu quả nhất về trao đổi chất để gắn toàn bộ mạng lưới mô liên kết.</p>",
        ),
        (
            "<h3>Practising Silk Reeling</h3>"
            "<p>The simplest drill is the <strong>silk-reeling arm</strong>: stand in a basic stance, raise both arms in front of you at shoulder height, palms down, and rotate them in small, continuous circles &mdash; clockwise on the right arm, counter-clockwise on the left, then reverse. The arms should remain at shoulder height while the shoulders, elbows, wrists, and fingers all participate in the rotation. Do not move the arms independently of the body; let the rotation begin in the waist and travel out through the shoulders, elbows, wrists, and fingers.</p>"
            "<p>After the arm drill, add a basic step: in a bow stance, rotate the arms in sync with the weight shift. Forward step, arms rotate one way; backward weight shift, arms rotate the other way. This is the simplest silk-reeling form. The body learns that movement is <em>always</em> spiral.</p>",

            "<h3>Thực Hành Triền Ty</h3>"
            "<p>Bài tập đơn giản nhất là <strong>tay cuộn tơ</strong>: đứng ở tư thế cơ bản, nâng hai tay trước mặt ở ngang vai, lòng bàn tay xuống, và xoay chúng trong các vòng nhỏ liên tục &mdash; thuận chiều kim đồng hồ ở tay phải, ngược chiều ở tay trái, rồi đảo lại. Hai tay nên giữ ở ngang vai trong khi vai, khuỷu, cổ tay, và ngón tay đều tham gia xoay. Không di chuyển tay độc lập với thân; để sự xoay bắt đầu ở eo và đi ra qua vai, khuỷu, cổ tay, và ngón tay.</p>"
            "<p>Sau bài tập tay, thêm một bước cơ bản: ở tư thế cung, xoay tay đồng bộ với sự chuyển trọng lượng. Bước tới, tay xoay một hướng; chuyển trọng lượng về sau, tay xoay hướng kia. Đây là hình thức cuộn tơ đơn giản nhất. Cơ thể học rằng chuyển động <em>luôn luôn</em> là xoắn ốc.</p>",
        ),
        (
            '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Master Cue</h3>'
            '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"No movement is linear. Every movement is a spiral."</p>',
            '<h3 style="background:var(--ink); color:var(--card); padding:0.5rem 1rem; margin:-0.5rem -1rem 0.5rem;">Câu Nhắc Tổng</h3>'
            '<p style="font-style:italic; font-family:Cormorant Garamond,serif; font-size:1.3rem;">"Không chuyển động nào thẳng. Mọi chuyển động là xoắn ốc."</p>',
        ),
    ])


print(f"Topics defined so far: {len(TOPICS)}")

# ---------- Build ----------
def build_all():
    for slug, en_title, vi_title, cards in TOPICS:
        en_dir = REPO / "en" / "techniques" / slug
        vi_dir = REPO / "vi" / "techniques" / slug
        en_dir.mkdir(parents=True, exist_ok=True)
        vi_dir.mkdir(parents=True, exist_ok=True)

        # Build body
        en_cards = "".join(
            f'    <section class="technique-card">\n  {ec}\n    </section>\n'
            for ec, _ in cards
        )
        vi_cards = "".join(
            f'    <section class="technique-card">\n  {vc}\n    </section>\n'
            for _, vc in cards
        )

        (en_dir / "index.html").write_text(
            shell("en", en_title, slug).replace("{body}", en_cards),
            encoding='utf-8'
        )
        (vi_dir / "index.html").write_text(
            shell("vi", vi_title, slug).replace("{body}", vi_cards),
            encoding='utf-8'
        )
        print(f"  built {slug}")


if __name__ == "__main__":
    print("--- Batch 4 (3 of 10) ---")
    build_all()
