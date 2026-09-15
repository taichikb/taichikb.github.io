#!/usr/bin/env python3
"""
TaichiKB Yin Yang redesign build script.
Rebuilds index.html, en/techniques/, vi/techniques/ with new black/white theme.
Strips all MkDocs chrome via CSS overrides.
"""
import os
import shutil
from pathlib import Path

REPO = Path("D:/Taichi-Health-Finance/Intranet/taichikb_repo")

TAIJI_LOGO = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" class="taiji-logo"><circle cx="100" cy="100" r="98" fill="#ffffff" stroke="#000000" stroke-width="4"/><path d="M 100,2 A 98,98 0 0,1 100,198 A 49,49 0 0,1 100,100 A 49,49 0 0,0 100,2 Z" fill="#000000"/><circle cx="100" cy="51" r="12" fill="#ffffff"/><circle cx="100" cy="149" r="12" fill="#000000"/></svg>'

def page_shell(lang, title, body, active="home", page_nav=None):
    """Wrap content in the Yin Yang themed page shell."""
    nav_items = {
        "en": [
            ("home", "Home", "/"),
            ("techniques", "Techniques", "/en/techniques/"),
            ("philosophy", "Philosophy", "/en/philosophy/"),
            ("history", "History", "/en/history/"),
            ("contact", "Contact", "/en/contact/"),
        ],
        "vi": [
            ("home", "Trang Chủ", "/vi/"),
            ("techniques", "Kỹ Thuật", "/vi/techniques/"),
            ("philosophy", "Triết Lý", "/vi/philosophy/"),
            ("history", "Lịch Sử", "/vi/history/"),
            ("contact", "Liên Hệ", "/vi/contact/"),
        ],
    }

    other_lang = "vi" if lang == "en" else "en"
    other_label = "🇻🇳 Tiếng Việt" if lang == "en" else "🇬🇧 English"
    other_href = f"/{other_lang}/techniques/" if active == "techniques" else f"/{other_lang}/"

    nav_html = '\n'.join(
        f'<a href="{href}" class="{"active" if key == active else ""}">{label}</a>'
        for key, label, href in nav_items[lang]
    )

    home_href = "/" if lang == "en" else "/vi/"

    page_nav_html = ""
    if page_nav:
        prev_h, prev_l = page_nav.get("prev", ("#", "←"))
        next_h, next_l = page_nav.get("next", ("#", "→"))
        page_nav_html = f'''
<nav class="page-nav">
    <a href="{prev_h}">{prev_l}</a>
    <a href="{home_href}" class="home">⌂ Home</a>
    <a href="{next_h}">{next_l}</a>
</nav>'''

    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} — TaichiKB</title>
<meta name="description" content="TaichiKB — Chen Style Tai Chi. Black & white, Yin Yang themed bilingual knowledge base.">
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
{body}
{page_nav_html}
</main>

<footer class="site-footer">
    <p>Built with ❤️ for the Vietnamese Tai Chi community <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="20" height="20" style="vertical-align:-3px;display:inline-block;"><circle cx="100" cy="100" r="98" fill="#ffffff" stroke="#000000" stroke-width="4"/><path d="M 100,2 A 98,98 0 0,1 100,198 A 49,49 0 0,1 100,100 A 49,49 0 0,0 100,2 Z" fill="#000000"/><circle cx="100" cy="51" r="12" fill="#ffffff"/><circle cx="100" cy="149" r="12" fill="#000000"/></svg> bởi Phạm Đức Hải</p>
    <p>Trang web này được xây dựng với ❤️ cho cộng đồng Thái Cực Quyền Việt Nam <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="20" height="20" style="vertical-align:-3px;display:inline-block;"><circle cx="100" cy="100" r="98" fill="#ffffff" stroke="#000000" stroke-width="4"/><path d="M 100,2 A 98,98 0 0,1 100,198 A 49,49 0 0,1 100,100 A 49,49 0 0,0 100,2 Z" fill="#000000"/><circle cx="100" cy="51" r="12" fill="#ffffff"/><circle cx="100" cy="149" r="12" fill="#000000"/></svg> bởi Phạm Đức Hải</p>
    <p style="margin-top:1rem;">{TAIJI_LOGO}</p>
</footer>

</body>
</html>'''


def build_index_en():
    """Build clean English landing page."""
    body = f'''
<section class="hero">
    <span class="taiji-large">{TAIJI_LOGO}</span>
    <h1>TaichiKB</h1>
    <p class="tagline">Chen Style Tai Chi — Techniques, History, Internal Arts</p>
    <p style="color: var(--gray-mid); font-style: italic;">Trần thức Thái cực quyền — Kỹ Thuật, Lịch Sử, Nội Công</p>
</section>

<section class="section">
    <div class="section-title"><h2>Eight Methods · Bát Pháp</h2></div>
    <div class="card-grid">
        <a href="/en/techniques/#eight-methods" class="card">
            <span class="card-meta">Fundamental</span>
            <h3>Peng · Ward Off (掤)</h3>
            <p>The root of all Tai Chi energies — an upward and outward expansive force that neutralizes pressure.</p>
        </a>
        <a href="/en/techniques/#eight-methods" class="card">
            <span class="card-meta">Fundamental</span>
            <h3>Lu · Rollback (履)</h3>
            <p>Sideways yielding energy that leads the opponent's force into emptiness without resistance.</p>
        </a>
        <a href="/en/techniques/#eight-methods" class="card">
            <span class="card-meta">Fundamental</span>
            <h3>Ji · Press (擠)</h3>
            <p>Forward squeezing energy generated from the ground through the legs, directed through the hands.</p>
        </a>
        <a href="/en/techniques/#eight-methods" class="card">
            <span class="card-meta">Fundamental</span>
            <h3>An · Push (按)</h3>
            <p>Downward and forward pressing energy that settles the opponent's structure.</p>
        </a>
        <a href="/en/techniques/#eight-methods" class="card">
            <span class="card-meta">Corner</span>
            <h3>Cai · Pluck (採)</h3>
            <p>Sudden downward jerking energy — disrupts the opponent's root with a quick, sharp pull.</p>
        </a>
        <a href="/en/techniques/#eight-methods" class="card">
            <span class="card-meta">Corner</span>
            <h3>Lie · Split (挒)</h3>
            <p>Spiraling, rending energy that separates connected parts of the opponent's structure.</p>
        </a>
        <a href="/en/techniques/#eight-methods" class="card">
            <span class="card-meta">Corner</span>
            <h3>Zhou · Elbow (肘)</h3>
            <p>Close-range striking energy using the elbow — concentrated force from shoulder and back.</p>
        </a>
        <a href="/en/techniques/#eight-methods" class="card">
            <span class="card-meta">Corner</span>
            <h3>Kao · Shoulder (靠)</h3>
            <p>Full-body leaning energy using shoulder, back, or hip to unbalance through weight transfer.</p>
        </a>
    </div>
</section>

<section class="section">
    <div class="feature-row">
        <div class="feature-image">{TAIJI_LOGO}</div>
        <div class="feature-text">
            <h2>Lu Jin — The Art of Rollback</h2>
            <p><strong>Lu Jin (捋劲)</strong> is one of the most subtle and profound techniques in Tai Chi. It means following the opponent's attack and reflecting their force back.</p>
            <p>When the opponent strikes straight, do not block or resist. Instead, use one or both hands, or forearm and humerus, or the combined strength of both hands, to rotate and push the opponent's force along their attack direction — redirecting the attack.</p>
            <p><em>"Use four ounces to deflect a thousand pounds."</em></p>
            <p><a href="/en/techniques/#lu-jin">Read the full analysis →</a></p>
        </div>
    </div>
</section>

<section class="section">
    <div class="section-title"><h2>Internal Practice · Nội Công</h2></div>
    <div class="card-grid">
        <a href="/en/techniques/#tu-na" class="card">
            <span class="card-meta">Breathing</span>
            <h3>Tu Na · 吐納</h3>
            <p>Exhale the stale (Tu), inhale the fresh (Na) — natural breathing as the foundation of internal work.</p>
        </a>
        <a href="/en/techniques/#nei-gong" class="card">
            <span class="card-meta">Internal</span>
            <h3>Nei Gong · 內功</h3>
            <p>The essence and soul of Tai Chi — Jing, Qi, and Shen cultivated through standing meditation and silk reeling.</p>
        </a>
        <a href="/en/techniques/#la-jin" class="card">
            <span class="card-meta">Tendon</span>
            <h3>La Jin · 拉筋</h3>
            <p>Pulling tendons — stretches connective tissue and opens the joints, preparing the body for silk reeling.</p>
        </a>
        <a href="/en/techniques/#sword" class="card">
            <span class="card-meta">Weapon</span>
            <h3>Jian · Sword 劍</h3>
            <p>The 49-form Chen Sword extends the body's energy through four major techniques: Ci, Pi, Liao, Dian.</p>
        </a>
    </div>
</section>

<section class="section">
    <div class="section-title"><h2>The Practice Path</h2></div>
    <div class="card-grid">
        <div class="card">
            <span class="card-meta">01</span>
            <h3>Relax (Song)</h3>
            <p>Release unnecessary tension throughout the body — the gateway to all Tai Chi skill.</p>
        </div>
        <div class="card">
            <span class="card-meta">02</span>
            <h3>Extend (Shen)</h3>
            <p>Lengthen through the joints, connect fingers to toes, head to tailbone.</p>
        </div>
        <div class="card">
            <span class="card-meta">03</span>
            <h3>Connect (Tong)</h3>
            <p>Unify the body — every part moves as one unit, directed by the Yi (intent).</p>
        </div>
        <div class="card">
            <span class="card-meta">04</span>
            <h3>Breathe (Tu Na)</h3>
            <p>Coordinate breath with movement — long, slow, even, natural.</p>
        </div>
        <div class="card">
            <span class="card-meta">05</span>
            <h3>Sink (Chen)</h3>
            <p>Drop weight into the feet — root through Yongquan (Kidney 1) into the earth.</p>
        </div>
        <div class="card">
            <span class="card-meta">06</span>
            <h3>Emptiness (Xu)</h3>
            <p>The opponent attacks a thousand pounds; I meet them with four ounces of nothing.</p>
        </div>
    </div>
</section>
'''
    return page_shell("en", "TaichiKB — Chen Style Tai Chi", body, active="home")


def build_index_vi():
    """Build clean Vietnamese landing page."""
    body = f'''
<section class="hero">
    <span class="taiji-large">{TAIJI_LOGO}</span>
    <h1>TaichiKB</h1>
    <p class="tagline">Trần thức Thái cực quyền — Kỹ Thuật, Lịch Sử, Nội Công</p>
    <p style="color: var(--gray-mid); font-style: italic;">Chen Style Tai Chi — Techniques, History, Internal Arts</p>
</section>

<section class="section">
    <div class="section-title"><h2>Bát Pháp · Eight Methods</h2></div>
    <div class="card-grid">
        <a href="/vi/techniques/#eight-methods" class="card">
            <span class="card-meta">Cơ bản</span>
            <h3>Bình · Chân (掤)</h3>
            <p>Gốc của tất cả năng lực Thiền Võ — lực giãn nở lên và ra ngoài trung hòa áp lực đến.</p>
        </a>
        <a href="/vi/techniques/#eight-methods" class="card">
            <span class="card-meta">Cơ bản</span>
            <h3>Lữ · Lướt (履)</h3>
            <p>Năng lượng nhường bên dẫn dắt lực đối phương vào hư không mà không cưỡng lại.</p>
        </a>
        <a href="/vi/techniques/#eight-methods" class="card">
            <span class="card-meta">Cơ bản</span>
            <h3>Crowd · Ép (擠)</h3>
            <p>Năng lượng nén về phía trước sinh từ mặt đất qua chân, dẫn dắt qua tay.</p>
        </a>
        <a href="/vi/techniques/#eight-methods" class="card">
            <span class="card-meta">Cơ bản</span>
            <h3>An · Đẩy (按)</h3>
            <p>Năng lượng đè xuống và đẩy về trước — làm ổn định cấu trúc đối phương.</p>
        </a>
        <a href="/vi/techniques/#eight-methods" class="card">
            <span class="card-meta">Góc</span>
            <h3>Thái · Hái (採)</h3>
            <p>Năng lượng giật xuống đột ngột — làm rung chuyển gốc rễ đối phương.</p>
        </a>
        <a href="/vi/techniques/#eight-methods" class="card">
            <span class="card-meta">Góc</span>
            <h3>Liê · Tách (挒)</h3>
            <p>Năng lượng xoắn ốc tách rời các bộ phận liên kết của cấu trúc đối phương.</p>
        </a>
        <a href="/vi/techniques/#eight-methods" class="card">
            <span class="card-meta">Góc</span>
            <h3>Chủ · Chỏ (肘)</h3>
            <p>Năng lượng đánh gần bằng chỏ — lực tập trung từ vai và lưng.</p>
        </a>
        <a href="/vi/techniques/#eight-methods" class="card">
            <span class="card-meta">Góc</span>
            <h3>Khào · Vai (靠)</h3>
            <p>Năng lượng tràn cả người — dùng vai, lưng hoặc hông để mất cân bằng đối phương.</p>
        </a>
    </div>
</section>

<section class="section">
    <div class="feature-row">
        <div class="feature-image">{TAIJI_LOGO}</div>
        <div class="feature-text">
            <h2>Lữ Kinh — Nghệ Thuật Vuốt</h2>
            <p><strong>Lữ Kinh (捋劲)</strong> là một trong những kỹ thuật tinh tế và sâu sắc nhất của Thái Cực Quyền. Nó có nghĩa là theo đà tấn công của đối phương và phản lại lực của họ.</p>
            <p>Khi đối phương tấn công thẳng, đừng chống đỡ. Hãy dùng sức mạnh của một hoặc cả hai tay để xoay và đẩy lực theo hướng tấn công của họ — làm chệch hướng đòn tấn công.</p>
            <p><em>"Dùng bốn cân đỡ một nghìn cân."</em></p>
            <p><a href="/vi/techniques/#lu-jin">Đọc phân tích đầy đủ →</a></p>
        </div>
    </div>
</section>

<section class="section">
    <div class="section-title"><h2>Nội Công · Internal Practice</h2></div>
    <div class="card-grid">
        <a href="/vi/techniques/#tu-na" class="card">
            <span class="card-meta">Hơi thở</span>
            <h3>Tổ Nha · 吐納</h3>
            <p>Thở ra cái cũ (Tổ), hít vào cái mới (Nha) — hơi thở tự nhiên là nền tảng nội công.</p>
        </a>
        <a href="/vi/techniques/#nei-gong" class="card">
            <span class="card-meta">Nội công</span>
            <h3>Nội Công · 內功</h3>
            <p>Tinh túy và linh hồn Thái Cực — Tinh, Khí, Thần tu luyện qua Trạm Trang và Chân Tư.</p>
        </a>
        <a href="/vi/techniques/#la-jin" class="card">
            <span class="card-meta">Gân</span>
            <h3>La Kinh · 拉筋</h3>
            <p>Kéo gân — giãn mô liên kết, mở khớp, chuẩn bị cơ thể cho Chân Tư Công.</p>
        </a>
        <a href="/vi/techniques/#sword" class="card">
            <span class="card-meta">Vũ khí</span>
            <h3>Kiếm · 劍</h3>
            <p>Bộ Kiếm 49 thức Chen mở rộng năng lượng cơ thể qua bốn kỹ thuật chính: Thi, Bạch, Liêu, Điểm.</p>
        </a>
    </div>
</section>

<section class="section">
    <div class="section-title"><h2>Con Đường Tu Luyện</h2></div>
    <div class="card-grid">
        <div class="card">
            <span class="card-meta">01</span>
            <h3>Thư (Song)</h3>
            <p>Thả bỏ căng thẳng không cần thiết — cánh cửa đến mọi kỹ năng Thái Cực.</p>
        </div>
        <div class="card">
            <span class="card-meta">02</span>
            <h3>Kéo (Shen)</h3>
            <p>Kéo dài qua các khớp, nối ngón tay đến ngón chân, đầu đến xương cụt.</p>
        </div>
        <div class="card">
            <span class="card-meta">03</span>
            <h3>Kết (Tong)</h3>
            <p>Thống nhất cơ thể — mọi phần chuyển động như một khối, theo Ý (Intention).</p>
        </div>
        <div class="card">
            <span class="card-meta">04</span>
            <h3>Thở (Tu Na)</h3>
            <p>Phối hợp hơi thở với chuyển động — dài, chậm, đều, tự nhiên.</p>
        </div>
        <div class="card">
            <span class="card-meta">05</span>
            <h3>Trầm (Chen)</h3>
            <p>Buông trọng lượng vào chân — gốc qua huyệt Vĩnh Quyền vào lòng đất.</p>
        </div>
        <div class="card">
            <span class="card-meta">06</span>
            <h3>Hư (Xu)</h3>
            <p>Đối phương công nghìn cân; ta đón bằng bốn cân hư không.</p>
        </div>
    </div>
</section>
'''
    return page_shell("vi", "TaichiKB — Trần thức Thái cực quyền", body, active="home")


def build_techniques_vi():
    """Build VI techniques page with full content from the sources."""
    body = '''
<article class="technique-content">
    <header class="page-header" style="text-align:center; padding:4rem 0 2rem;">
        <h1>Kỹ Thuật Trần thức Thái cực quyền</h1>
        <p style="color: var(--gray-mid); font-style: italic; font-size:1.2rem;">
        Các phương pháp và nguyên lý cơ bản từ truyền thống họ Chen</p>
    </header>

    <nav class="technique-nav">
        <ul>
            <li><a href="#eight-methods">Bát Pháp (八法)</a></li>
            <li><a href="#history">Lịch Sử</a></li>
            <li><a href="#la-jin">La Kinh (拉筋)</a></li>
            <li><a href="#lu-jin">Lữ Kinh (捋劲)</a></li>
            <li><a href="#tu-na">Tổ Nha (吐納)</a></li>
            <li><a href="#nei-gong">Nội Công (內功)</a></li>
            <li><a href="#sword">Kiếm (劍)</a></li>
            <li><a href="#ethics">Võ Đức (武德)</a></li>
        </ul>
    </nav>

    <section id="eight-methods" class="technique-section">
        <h2>Bát Pháp · Eight Methods (八法)</h2>
        <p style="color:var(--gray-mid); font-style:italic;">Tám phương pháp chiến đấu cơ bản của Thái Cực Quyền, chia thành bốn hướng chính (Bình, Lữ, Cơ, An) và bốn hướng góc (Thái, Liễu, Chủ, Khào).</p>

        <div class="technique-card">
            <h3>Bình · 掤 — Ward Off</h3>
            <p>Năng lượng giãn nở cơ bản, như nước đỡ thuyền. Bình là gốc của tất cả các năng lực Thiền Võ — một lực giãn nở lên và ra ngoài trung hòa áp lực đến. Trong lý thuyết Thái Cực Quyền, Bình Kinh là Dương, Lữ Kinh là Âm.</p>
        </div>

        <div class="technique-card">
            <h3>Lữ · 履 — Rollback</h3>
            <p>Năng lượng nhường bên dẫn dắt lực đối phương vào hư không. Lữ theo sau lực đến và chuyển hướng nó theo chiều ngang mà không cưỡng lại. Lữ Kinh là biểu hiện chính của sự bám dính, dính chặt và theo đuổi trong Thái Cực Quyền.</p>
        </div>

        <div class="technique-card">
            <h3>Cơ · 擠 — Press</h3>
            <p>Năng lượng nén về phía trước sinh từ mặt đất qua chân, dẫn dắt qua tay. Cơ nén không gian của đối phương và chuẩn bị cho lực tiếp theo.</p>
        </div>

        <div class="technique-card">
            <h3>An · 按 — Push</h3>
            <p>Năng lượng đè xuống và đẩy về trước. An ổn định cấu trúc đối phương và làm rễ bề của họ bằng lực chìm.</p>
        </div>

        <div class="technique-card">
            <h3>Thái · 採 — Pluck</h3>
            <p>Năng lượng giật xuống đột ngột, như hái trái cây. Thái làm rung chuyển gốc rễ của đối phương bằng một cái kéo nhanh, sắc bén.</p>
        </div>

        <div class="technique-card">
            <h3>Liễu · 挒 — Split</h3>
            <p>Năng lượng xoắn ốc, tách rời các bộ phận liên kết. Liễu sử dụng lực đối nghịch để xé rách cấu trúc đối phương.</p>
        </div>

        <div class="technique-card">
            <h3>Chủ · 肘 — Elbow Strike</h3>
            <p>Năng lượng đánh gần bằng chỏ. Chủ sinh lực từ vai và lưng, tập trung lực vào một điểm.</p>
        </div>

        <div class="technique-card">
            <h3>Khào · 靠 — Shoulder/Body Strike</h3>
            <p>Năng lượng tràn cả người. Khào dùng vai, lưng hoặc hông để làm mất cân bằng đối phương bằng chuyển dịch trọng tâm.</p>
        </div>
    </section>

    <section id="history" class="technique-section">
        <h2>Lịch Sử & Truyền Thống</h2>
        <div class="technique-card">
            <h3>Nguồn Gốc Làng Chen</h3>
            <p>Trần thức Thái cực quyền bắt nguồn từ Làng Chen (Chenjiagou), huyện Wen, tỉnh Hà Nam, Trung Quốc. Nghệ thuật được sáng lập bởi <strong>Trần Vương Đình (Chen Wangting, 1600-1680)</strong>, người thế hệ 9 của gia tộc Chen, người đã tổng hợp quyền gia truyền với tu hành Khí, triết học Đạo giáo và chiến thuật quân sự.</p>
        </div>
        <div class="technique-card">
            <h3>Các Thế Hệ Then Chốt</h3>
            <ul>
                <li><strong>Trần Vương Đình</strong> — Người sáng lập, tạo 7 bộ quyền</li>
                <li><strong>Trần Trưởng Hưng</strong> (thế hệ 14) — Dạy Dương Lục Tranh</li>
                <li><strong>Trần Phát (Chen Fake)</strong> (thế hệ 17) — Lan truyền nghệ thuật đến Bắc Kinh</li>
                <li><strong>Trần Tiểu Vương (Chen Xiaowang)</strong> (thế hệ 19) — Đại sứ toàn cầu</li>
            </ul>
        </div>
        <div class="technique-card">
            <h3>Hai Bộ Chính Thống</h3>
            <p><strong>Lão Gia (Old Frame)</strong> — Vòng tròn lớn, Chân Tư rõ rệt, bước thấp.<br>
            <strong>Tân Gia (New Frame)</strong> — Vòng tròn nhỏ, Chân Tư tinh tế hơn, bước cao hơn, nhiều phát lực hơn.</p>
        </div>
    </section>

    <section id="la-jin" class="technique-section">
        <h2>La Kinh · 拉筋 — Kéo Gân</h2>
        <div class="technique-card">
            <h3>Mục Đích</h3>
            <p>La Kinh kéo giãn gân, mở khớp, và kéo dài các chuỗi cơ-màng. Nó chuẩn bị cơ thể cho Chân Tư (Silk Reeling) bằng cách tạo độ đàn hồi cho mô liên kết.</p>
        </div>
        <div class="technique-card">
            <h3>Nguyên Tắc Cốt Lõi</h3>
            <ul>
                <li><strong>Thư (Song)</strong> — thả bỏ căng thẳng không cần thiết</li>
                <li><strong>Kéo (Shen)</strong> — kéo dài qua các khớp</li>
                <li><strong>Kết (Tong)</strong> — nối ngón tay đến ngón chân</li>
                <li><strong>Thở</strong> — phối hợp với Tổ Nha</li>
            </ul>
        </div>
        <div class="technique-card">
            <h3>Bài Tập Phổ Biến</h3>
            <ul>
                <li><strong>La Kinh đứng</strong> — tay duỗi ra, chìm và kéo</li>
                <li><strong>La Kinh ngồi</strong> — chân duỗi, về phía trước</li>
                <li><strong>La Kinh đôi</strong> — kéo giãn lẫn nhau (đối tác)</li>
            </ul>
        </div>
    </section>

    <section id="lu-jin" class="technique-section">
        <h2>Lữ Kinh · 捋劲 — Năng Lực Lướt</h2>

        <div class="technique-card">
            <h3>Định Nghĩa</h3>
            <p>Lữ Kinh (捋劲) là một phương pháp chiến đấu cơ bản của Thái Cực Quyền, thuộc loại Mười ba hình thức và Tám kỹ thuật chiến đấu. Cốt lõi của nó là <em>mượn lực để tấn công</em>, chuyển đổi lực thẳng của đối phương thành lực xoay bằng cách theo đà, để đạt được hiệu quả dùng mềm để khắc phục cứng — <strong>dùng bốn cân để đỡ một nghìn cân (四两拨千斤)</strong>.</p>
        </div>

        <div class="technique-card">
            <h3>Ba Yếu Tố Cốt Lõi</h3>
            <ol>
                <li>Theo hướng lực của đối phương</li>
                <li>Luôn sử dụng sức mạnh của chính mình (dù chỉ là lực nhẹ)</li>
                <li>Quỹ đạo chuyển động là sang bên cạnh cơ thể (hình vòng cung)</li>
            </ol>
        </div>

        <div class="technique-card">
            <h3>Điểm Then Chốt</h3>
            <ul>
                <li>Không cưỡng lại — theo sau lực</li>
                <li>Xoay eo (Yao) làm trục</li>
                <li>Giữ tay trong cung "Lữ" — không sụp cũng không đẩy</li>
                <li>Chìm trọng lực (Trầm) vào chân sau</li>
                <li>Chìa khóa nằm ở eo, chân và ý chí — KHÔNG ở cánh tay</li>
            </ul>
        </div>

        <div class="technique-card">
            <h3>Hai Loại Lữ Kinh</h3>
            <p><strong>Lữ bám dính, theo sát:</strong> dùng lực đối phương để khiến họ trượt. Nguyên tắc giống như giày trượt patin, khúc gỗ lăn, đường ray xe lửa — bản thân không có sức mạnh, sức mạnh đến từ đối thủ.</p>
            <p><strong>Lữ giải phóng:</strong> lực đến từ eo và chân, thường mượn sức cản của đối thủ, quỹ đạo là vòng cung.</p>
        </div>

        <div class="technique-card">
            <h3>Lắng Nghe Lực (聽劲)</h3>
            <p>Lắng nghe sức mạnh bao gồm tiếp nhận thông tin về đòn tấn công và phòng thủ của đối phương thông qua thính giác, thị giác và <strong>xúc giác</strong>, cảm nhận qua da thịt và lông trên cơ thể. Chỉ khi nhận biết được cường độ và hướng của sức mạnh, người tập mới có thể nhanh chóng và dứt khoát đưa ra các biện pháp thích hợp.</p>
            <p><em>Phải loại bỏ mọi lực cứng nhắc, vụng về và cứng đờ khỏi cơ thể trước.</em></p>
        </div>

        <div class="technique-card">
            <h3>Ứng Dụng Thực Tiễn</h3>
            <p>Ví dụ: khi đối thủ tung cú đấm trái hoặc đánh vào mặt tôi, tôi hạ thấp tư thế, ổn định trọng tâm, giữ cho phần thân dưới vững chắc nhưng linh hoạt trong khi phần thân trên vẫn thư giãn. Tôi giơ cả hai tay sang bên phải trước người, tay phải ở phía trước và tay trái ở phía sau, đỡ cú đấm của đối thủ. Tận dụng đà tiến về phía trước của đối thủ, tôi dùng cả hai tay kéo đối thủ sang trái một cách nhẹ nhàng đồng thời xoay eo sang trái — khiến đối thủ ngã xuống. Đây chính là Lữ Kinh.</p>
        </div>

        <div class="technique-card">
            <h3>Biện Pháp Phòng Ngừa</h3>
            <ul>
                <li>Tránh dùng sức mạnh thô bạo</li>
                <li>Tận dụng động lượng và sức mạnh của đối thủ — "mượn sức để phản công"</li>
                <li>Đối thủ càng mạnh, đòn phản công càng mạnh</li>
                <li>Thời điểm là vô cùng quan trọng — quá sớm hoặc quá muộn đều thất bại</li>
                <li>Lực kéo chỉ cần "bốn cân" — không được quá mạnh (đối phương sẽ nhận ra), không được quá nhẹ (vô hiệu)</li>
                <li>"Sử dụng lực giống như bắn tên" — phải tập trung và nhanh chóng</li>
            </ul>
        </div>
    </section>

    <section id="tu-na" class="technique-section">
        <h2>Tổ Nha · 吐納 — Phương Pháp Thở</h2>

        <div class="technique-card">
            <h3>Tổ · 吐 — Thở Ra</h3>
            <p>Thải Khí cũ. Thở ra qua miệng khi phát lực (fajin) hoặc khi chìm. Hơi thở ra dẫn Khí đến chi cuối. Càng sâu, năng lượng càng chìm sâu.</p>
        </div>

        <div class="technique-card">
            <h3>Nha · 納 — Thở Vào</h3>
            <p>Tụ Khí tươi. Thở vào qua mũi khi mở/lên. Hơi thở vào kéo Khí vào Đan Điền.</p>
        </div>

        <div class="technique-card">
            <h3>Năm Loại Khí Đục (phải thải ra)</h3>
            <ol>
                <li><strong>Khí ngang</strong> — tức ngực, khó thở khi tập</li>
                <li><strong>Khí tà ác</strong> — thở không đều, mặt tái nhợt</li>
                <li><strong>Khí nổi loạn</strong> — nâng vai và chỏ không biết hạ</li>
                <li><strong>Khí ứ trệ</strong> — tắc nghẽn khí, cản trở lưu thông</li>
                <li><strong>Không khí đục</strong> — thân trên nặng, thân dưới nhẹ</li>
            </ol>
        </div>

        <div class="technique-card">
            <h3>Năm Loại Khí Thuần Khiết (phải hít vào)</h3>
            <ol>
                <li><strong>Khí tự nhiên bẩm sinh</strong> — nguồn năng lượng lúc sinh</li>
                <li><strong>Chính Khí Trời Đất</strong> — năng lượng Âm Dương, mềm và cứng</li>
                <li><strong>Khí Đại Hòa</strong> — Khí ở Đan Điền, Ngũ Khí Trở Về Nguyên Thủy</li>
                <li><strong>Tinh thần công chính</strong> — thuần khiết, không pha tạp, một hiệp không hụt hơi</li>
                <li><strong>Khí nguyên thủy</strong> — khi võ thuật thuần thục, năng lượng tập trung thành một thể vững chắc</li>
            </ol>
        </div>

        <div class="technique-card">
            <h3>Phối Hợp</h3>
            <ul>
                <li>Thở tự nhiên cho luyện bộ</li>
                <li>Thở ngược cho Nội Công</li>
                <li>Hơi thở theo động tác — mở/hít, khép/thở</li>
                <li>Không ép buộc — để hơi thở theo Ý (Intention)</li>
                <li>Tập giúp hơi thở dài, chậm, đều, tự nhiên</li>
            </ul>
        </div>
    </section>

    <section id="nei-gong" class="technique-section">
        <h2>Nội Công · 內功 — Công Phu Nội</h2>

        <div class="technique-card">
            <h3>Tam Bảo (Three Treasures)</h3>
            <ul>
                <li><strong>Tinh (精)</strong> — Tinh huyết, tồn tại tại thận</li>
                <li><strong>Khí (氣)</strong> — Năng lượng sống, tu tại Đan Điền</li>
                <li><strong>Thần (神)</strong> — Thần trí, biểu hiện qua mắt/ý chí</li>
            </ul>
        </div>

        <div class="technique-card">
            <h3>Đặc Điểm Chung Của Nội Công</h3>
            <ol>
                <li>Tập trung, điều hòa hơi thở, thư giãn hoàn toàn. Bạch Hội ↔ Vĩnh Quyền, toàn thân thư giãn.</li>
                <li>Hấp thụ, kết dính, nắm bắt, khép kín để lấp đầy Đại Mạch.</li>
                <li>Tuần hoàn liên tục — nội khí bắt nguồn từ và trở về Vĩnh Quyền.</li>
                <li>Luyện tập và ứng dụng linh hoạt — dùng ngoại lực ép hạ thấp để tăng cường sức cánh tay.</li>
                <li>Thích ứng và linh hoạt — khi bên trái nặng, bên trái trở nên trống rỗng.</li>
            </ol>
        </div>

        <div class="technique-card">
            <h3>Luyện Tập Cốt Lõi</h3>
            <ul>
                <li><strong>Trạm Trang (Standing Post)</strong> — xây gốc và Khí</li>
                <li><strong>Chân Tư Công (Silk Reeling)</strong> — xoắn kết nối toàn thân, lực cuộn tơ</li>
                <li><strong>Xoay Đan Điền</strong> — động cơ nội tại (36 vòng thuận, 24 vòng nghịch)</li>
                <li><strong>Tuần Kinh Lạc</strong> — Chu Thiên Tiểu (Microcosmic Orbit)</li>
                <li><strong>Đỉnh Đầu Cảm Ứng</strong> — Bạch Hội + Yintang cho ý chí chiến đấu</li>
            </ul>
        </div>

        <div class="technique-card">
            <h3>Tinh Hoa Của Chân Tư</h3>
            <p>Trần Vương Đình viết: <em>"Không ai biết sự giãn nở và co thắt của thân thể; ta dựa vào tất cả các kỹ thuật cuộn xoắn."</em> Trần Tâm viết: <em>"Thái Cực Quyền là phương pháp cuộn xoắn."</em></p>
            <p>Mọi động tác đều là chuyển động cuộn xoắn và xoắn ốc. Năng lượng cuộn tơ cho phép nội lực lưu chuyển toàn thân — đạt đến trạng thái "một chiếc lông vũ cũng không thể thêm vào, một con ruồi cũng không thể đậu xuống".</p>
        </div>
    </section>

    <section id="sword" class="technique-section">
        <h2>Kiếm · 劍 — Chen Style Sword</h2>

        <div class="technique-card">
            <h3>Nguyên Lý Kiếm Chen</h3>
            <p>Kiếm mở rộng năng lượng cơ thể. Bộ Kiếm 49 thức Chen kết hợp động tác mềm mại flow với phát lực fajin đột ngột. Then chốt: <strong>đầu kiếm theo Ý (intent), cơ thể động như một khối.</strong></p>
        </div>

        <div class="technique-card">
            <h3>Bốn Kỹ Thuật Chính</h3>
            <ul>
                <li><strong>Thi (刺)</strong> — Thrust: trực tiếp, xuyên thấu</li>
                <li><strong>Bạch (劈)</strong> — Chop: chém xuống</li>
                <li><strong>Liêu (撩)</strong> — Flick: bật cổ tay lên</li>
                <li><strong>Điểm (點)</strong> — Point: kiểm soát đầu ngón tay chính xác</li>
            </ul>
        </div>
    </section>

    <section id="ethics" class="technique-section">
        <h2>Võ Đức · 武德 — Đạo Đức Võ Thuật</h2>

        <div class="technique-card">
            <h3>Ngũ Đức (Five Virtues)</h3>
            <ul>
                <li><strong>Nhân (仁)</strong> — Benevolence: bảo vệ yếu thế</li>
                <li><strong>Nghĩa (義)</strong> — Righteousness: làm điều đúng</li>
                <li><strong>Lễ (禮)</strong> — Respect: tôn sư trọng đạo</li>
                <li><strong>Trí (智)</strong> — Wisdom: phân biệt trong hành động</li>
                <li><strong>Tín (信)</strong> — Trustworthiness: giữ lời hứa</li>
            </ul>
        </div>

        <div class="technique-card">
            <h3>Nguyên Tắc Luyện Tập</h3>
            <ul>
                <li><strong>Kiên trì (Hằng)</strong> — tập hàng ngày</li>
                <li><strong>Khiêm tốn (Khiêm)</strong> — tâm thái ly cốc</li>
                <li><strong>Kiên nhẫn (Nhẫn)</strong> — Công phu cần thời gian</li>
            </ul>
        </div>
    </section>
</article>
'''
    return page_shell("vi", "Kỹ Thuật — TaichiKB", body, active="techniques",
                       page_nav={"prev": ("/vi/", "← Trang Chủ"), "next": ("/vi/philosophy/", "Triết Lý →")})


def build_techniques_en():
    """Build EN techniques page mirroring VI content."""
    body = '''
<article class="technique-content">
    <header class="page-header" style="text-align:center; padding:4rem 0 2rem;">
        <h1>Chen Style Tai Chi Techniques</h1>
        <p style="color: var(--gray-mid); font-style: italic; font-size:1.2rem;">
        Fundamental methods and principles from the Chen family tradition</p>
    </header>

    <nav class="technique-nav">
        <ul>
            <li><a href="#eight-methods">Eight Methods (Ba Fa)</a></li>
            <li><a href="#history">History & Lineage</a></li>
            <li><a href="#la-jin">La Jin (Pulling Tendons)</a></li>
            <li><a href="#lu-jin">Lu Jin (Rollback Energy)</a></li>
            <li><a href="#tu-na">Tu Na (Breathing)</a></li>
            <li><a href="#nei-gong">Nei Gong (Internal Work)</a></li>
            <li><a href="#sword">Sword (Jian)</a></li>
            <li><a href="#ethics">Martial Ethics</a></li>
        </ul>
    </nav>

    <section id="eight-methods" class="technique-section">
        <h2>Eight Methods · Bát Pháp (八法)</h2>
        <p style="color:var(--gray-mid); font-style:italic;">The eight fundamental combat methods of Tai Chi, divided into four cardinal (Peng, Lu, Ji, An) and four corner (Cai, Lie, Zhou, Kao) directions.</p>

        <div class="technique-card">
            <h3>Peng · 掤 — Ward Off</h3>
            <p>The fundamental expanding energy, like water supporting a boat. Peng is the root of all Tai Chi energies — an upward and outward expansive force that neutralizes incoming pressure. In Tai Chi theory, Peng Jin is Yang, Lu Jin is Yin.</p>
        </div>

        <div class="technique-card">
            <h3>Lu · 履 — Rollback</h3>
            <p>Sideways yielding energy that leads the opponent's force into emptiness. Lu follows the incoming force and redirects it laterally without resistance. Lu Jin is the principal expression of sticking, adhering, connecting, and following.</p>
        </div>

        <div class="technique-card">
            <h3>Ji · 擠 — Press</h3>
            <p>Forward squeezing energy generated from the ground through the legs, directed through the hands. Ji compresses the opponent's space and prepares for the next force.</p>
        </div>

        <div class="technique-card">
            <h3>An · 按 — Push</h3>
            <p>Downward and forward pressing energy. An settles the opponent's structure and uproots their balance through sinking force.</p>
        </div>

        <div class="technique-card">
            <h3>Cai · 採 — Pluck</h3>
            <p>Sudden downward jerking energy, like picking fruit. Cai disrupts the opponent's root with a quick, sharp pull.</p>
        </div>

        <div class="technique-card">
            <h3>Lie · 挒 — Split</h3>
            <p>Spiraling, rending energy that separates connected parts. Lie uses opposing forces to tear the opponent's structure apart.</p>
        </div>

        <div class="technique-card">
            <h3>Zhou · 肘 — Elbow Strike</h3>
            <p>Close-range striking energy using the elbow. Zhou generates power from the shoulder and back, delivering concentrated force.</p>
        </div>

        <div class="technique-card">
            <h3>Kao · 靠 — Shoulder/Body Strike</h3>
            <p>Full-body leaning energy. Kao uses the shoulder, back, or hip to unbalance the opponent through body weight transfer.</p>
        </div>
    </section>

    <section id="history" class="technique-section">
        <h2>History & Lineage</h2>
        <div class="technique-card">
            <h3>Chen Village Origins</h3>
            <p>Chen Style Tai Chi originated in Chenjiagou (Chen Village), Wen County, Henan Province, China. The art was created by <strong>Chen Wangting (1600-1680)</strong>, 9th generation Chen family member, who synthesized family boxing with Qi cultivation, Daoist philosophy, and military strategy.</p>
        </div>
        <div class="technique-card">
            <h3>Key Generations</h3>
            <ul>
                <li><strong>Chen Wangting</strong> — Founder, created 7 routines</li>
                <li><strong>Chen Changxing</strong> (14th gen) — Taught Yang Luchan</li>
                <li><strong>Chen Fake</strong> (17th gen) — Spread art to Beijing</li>
                <li><strong>Chen Xiaowang</strong> (19th gen) — Global ambassador</li>
            </ul>
        </div>
        <div class="technique-card">
            <h3>Two Main Forms</h3>
            <p><strong>Lao Jia (Old Frame)</strong> — Large circles, obvious silk reeling, lower stances.<br>
            <strong>Xin Jia (New Frame)</strong> — Smaller circles, more subtle silk reeling, higher stances, more fajin.</p>
        </div>
    </section>

    <section id="la-jin" class="technique-section">
        <h2>La Jin · 拉筋 — Pulling Tendons</h2>
        <div class="technique-card">
            <h3>Purpose</h3>
            <p>La Jin stretches the tendons, opens the joints, and lengthens the myofascial chains. It prepares the body for silk reeling (Chan Si) by creating elasticity in the connective tissue.</p>
        </div>
        <div class="technique-card">
            <h3>Key Principles</h3>
            <ul>
                <li><strong>Relax (Song)</strong> — release unnecessary tension</li>
                <li><strong>Extend (Shen)</strong> — lengthen through joints</li>
                <li><strong>Connect (Tong)</strong> — link fingers to toes</li>
                <li><strong>Breathe</strong> — coordinate with Tu Na</li>
            </ul>
        </div>
        <div class="technique-card">
            <h3>Common Exercises</h3>
            <ul>
                <li><strong>Standing La Jin</strong> — arms forward, sink and stretch</li>
                <li><strong>Seated La Jin</strong> — legs extended, reach forward</li>
                <li><strong>Partner La Jin</strong> — mutual stretching</li>
            </ul>
        </div>
    </section>

    <section id="lu-jin" class="technique-section">
        <h2>Lu Jin · 捋劲 — Rollback Energy</h2>

        <div class="technique-card">
            <h3>Definition</h3>
            <p>Lu Jin (捋劲) is one of the fundamental combat methods of Tai Chi, among the Thirteen Postures and Eight Techniques. Its core is <em>borrowing force to attack</em> — converting the opponent's straight force into rotational force by following their momentum, achieving the effect of <strong>using softness to overcome hardness, using four ounces to deflect a thousand pounds (四两拨千斤)</strong>.</p>
        </div>

        <div class="technique-card">
            <h3>Three Core Elements</h3>
            <ol>
                <li>Follow the direction of the opponent's force</li>
                <li>Always apply your own force (even if only light)</li>
                <li>The movement trajectory is along an arc to your body's side</li>
            </ol>
        </div>

        <div class="technique-card">
            <h3>Key Points</h3>
            <ul>
                <li>Do not resist — follow the force</li>
                <li>Rotate the waist (Yao) as the axis</li>
                <li>Keep arms in the "Lu" arc — neither collapsing nor pushing</li>
                <li>Sink the weight (Chen) into the rear foot</li>
                <li><strong>The key lies in the waist, legs, and Yi (intent) — NOT in the arms</strong></li>
            </ul>
        </div>

        <div class="technique-card">
            <h3>Two Types of Lu Jin</h3>
            <p><strong>Sticking-adhering-following Lu:</strong> uses the opponent's force to make them slip. The principle is like an ice skate, rolling log, or train rail — itself without power, the power comes from the opponent.</p>
            <p><strong>Releasing Lu:</strong> the force comes from the waist and legs, usually borrowing the opponent's resistance, trajectory is an arc.</p>
        </div>

        <div class="technique-card">
            <h3>Listening to Force (聽劲)</h3>
            <p>Listening to force means receiving information about the opponent's attack and defense through hearing, sight, and <strong>touch</strong>, sensing through the skin and hair of the body. Only when you immediately perceive the intensity and direction of the opponent's power can you quickly and decisively apply appropriate countermeasures.</p>
            <p><em>You must first eliminate all rigid, awkward, and stiff force from the body.</em></p>
        </div>

        <div class="technique-card">
            <h3>Practical Application</h3>
            <p>Example: When the opponent throws a left punch or strikes at my face, I lower my posture, stabilize my center of gravity, keep my lower body solid but flexible while my upper body remains relaxed. I raise both hands to my right front, right hand in front, left hand behind, to receive the opponent's strike. Taking advantage of the opponent's forward momentum, I use both hands to gently pull them to my left while simultaneously rotating my waist leftward — causing the opponent to fall. This is Lu Jin.</p>
        </div>

        <div class="technique-card">
            <h3>Precautions</h3>
            <ul>
                <li>Avoid using brute strength</li>
                <li>Leverage the opponent's momentum and power — "borrow force to counter-attack"</li>
                <li>The stronger the opponent, the stronger your counter</li>
                <li><strong>Timing is everything</strong> — too early or too late, you fail</li>
                <li>The pulling force needs only "four ounces" — not too strong (opponent will detect), not too weak (ineffective)</li>
                <li>"Using force is like shooting an arrow" — focus and speed</li>
            </ul>
        </div>
    </section>

    <section id="tu-na" class="technique-section">
        <h2>Tu Na · 吐納 — Breathing Method</h2>

        <div class="technique-card">
            <h3>Tu · 吐 — Exhale</h3>
            <p>Expel stale Qi. Exhale through the mouth during fajin (power release) or when sinking. The exhale drives Qi to the extremities. The deeper, the more the energy sinks.</p>
        </div>

        <div class="technique-card">
            <h3>Na · 納 — Inhale</h3>
            <p>Gather fresh Qi. Inhale through the nose during opening/upward movements. The inhale draws Qi into the Dantian.</p>
        </div>

        <div class="technique-card">
            <h3>Five Types of Dirty Qi (to expel)</h3>
            <ol>
                <li><strong>Horizontal Qi</strong> — chest tightness, breathlessness during practice</li>
                <li><strong>Evil Qi</strong> — irregular breathing, pallid face</li>
                <li><strong>Rebellious Qi</strong> — raising shoulders and elbows without releasing</li>
                <li><strong>Stagnant Qi</strong> — Qi blockage, prevents circulation</li>
                <li><strong>Turbid Qi</strong> — heavy upper, light lower</li>
            </ol>
        </div>

        <div class="technique-card">
            <h3>Five Types of Pure Qi (to gather)</h3>
            <ol>
                <li><strong>Innate Natural Qi</strong> — energy at birth</li>
                <li><strong>Heaven-Earth Correct Qi</strong> — Yin-Yang, soft and hard</li>
                <li><strong>Great Harmony Qi</strong> — Qi of Dantian, Five Qi Return to Origin</li>
                <li><strong>Righteous Spirit Qi</strong> — pure, unmixed, one form without breathlessness</li>
                <li><strong>Primordial Qi</strong> — when skill is mature, energy concentrated as one</li>
            </ol>
        </div>

        <div class="technique-card">
            <h3>Coordination</h3>
            <ul>
                <li>Natural breathing for form practice</li>
                <li>Reverse breathing for Nei Gong</li>
                <li>Breath matches movement — open/inhale, close/exhale</li>
                <li>Never force — let breath follow Yi (intent)</li>
                <li>Practice helps breath become long, slow, even, natural</li>
            </ul>
        </div>
    </section>

    <section id="nei-gong" class="technique-section">
        <h2>Nei Gong · 內功 — Internal Work</h2>

        <div class="technique-card">
            <h3>Three Treasures (San Bao)</h3>
            <ul>
                <li><strong>Jing (精)</strong> — Essence, stored in kidneys</li>
                <li><strong>Qi (氣)</strong> — Vital energy, cultivated in Dantian</li>
                <li><strong>Shen (神)</strong> — Spirit, manifested in the eyes/intent</li>
            </ul>
        </div>

        <div class="technique-card">
            <h3>Common Features of Nei Gong</h3>
            <ol>
                <li>Focus, regulated breath, complete relaxation. Baihui ↔ Yongquan, whole body relaxed.</li>
                <li>Absorb, adhere, grasp, close to fill the Du Mai.</li>
                <li>Continuous circulation — internal Qi originates from and returns to Yongquan.</li>
                <li>Flexible practice and application — use external force to deepen stance, strengthen arms.</li>
                <li>Adaptive and flexible — when left is heavy, left becomes empty.</li>
            </ol>
        </div>

        <div class="technique-card">
            <h3>Core Practices</h3>
            <ul>
                <li><strong>Zhan Zhuang (Standing Post)</strong> — build root and Qi</li>
                <li><strong>Chan Si Gong (Silk Reeling)</strong> — spiral whole-body connection, reeling energy</li>
                <li><strong>Dantian rotation</strong> — internal engine (36 circles clockwise, 24 counter)</li>
                <li><strong>Meridian circulation</strong> — Microcosmic Orbit</li>
                <li><strong>Crown Spiritual Inspiration</strong> — Baihui + Yintang for combat will</li>
            </ul>
        </div>

        <div class="technique-card">
            <h3>The Essence of Silk Reeling</h3>
            <p>Chen Wangting wrote: <em>"No one knows the body's expansion and contraction; I rely entirely on the coiling techniques."</em> Chen Xin wrote: <em>"Tai Chi is the method of coiling."</em></p>
            <p>Every movement is spiral and coiling. The silk-reeling energy allows internal Qi to circulate throughout the entire body — achieving the state where <strong>"not a feather can be added, not a fly can land"</strong>.</p>
        </div>
    </section>

    <section id="sword" class="technique-section">
        <h2>Sword · 劍 — Chen Style Sword</h2>

        <div class="technique-card">
            <h3>Chen Style Sword Principles</h3>
            <p>The sword extends the body's energy. The 49-form Chen Sword combines soft flowing movements with sudden fajin releases. Key: <strong>the tip follows the Yi (intent), the body moves as one unit.</strong></p>
        </div>

        <div class="technique-card">
            <h3>Four Major Techniques</h3>
            <ul>
                <li><strong>Ci (刺)</strong> — Thrust: direct, penetrating</li>
                <li><strong>Pi (劈)</strong> — Chop: downward cleaving</li>
                <li><strong>Liao (撩)</strong> — Flick: upward wrist snap</li>
                <li><strong>Dian (點)</strong> — Point: precise fingertip control</li>
            </ul>
        </div>
    </section>

    <section id="ethics" class="technique-section">
        <h2>Martial Ethics · 武德 (Wu De)</h2>

        <div class="technique-card">
            <h3>Five Virtues</h3>
            <ul>
                <li><strong>Ren (仁)</strong> — Benevolence: protect the weak</li>
                <li><strong>Yi (義)</strong> — Righteousness: do what is right</li>
                <li><strong>Li (禮)</strong> — Respect: honor teachers, peers, art</li>
                <li><strong>Zhi (智)</strong> — Wisdom: discernment in action</li>
                <li><strong>Xin (信)</strong> — Trustworthiness: keep your word</li>
            </ul>
        </div>

        <div class="technique-card">
            <h3>Training Principles</h3>
            <ul>
                <li><strong>Perseverance (Heng)</strong> — daily practice</li>
                <li><strong>Humility (Qian)</strong> — empty cup mindset</li>
                <li><strong>Patience (Ren)</strong> — Kung Fu takes time</li>
            </ul>
        </div>
    </section>
</article>
'''
    return page_shell("en", "Techniques — TaichiKB", body, active="techniques",
                       page_nav={"prev": ("/", "← Home"), "next": ("/en/philosophy/", "Philosophy →")})


def main():
    # Remove old MkDocs-generated HTML and rebuild fresh
    print("Building TaichiKB Yin Yang themed pages...")

    # Index (root)
    (REPO / "index.html").write_text(build_index_en(), encoding="utf-8")
    print(f"✅ {REPO / 'index.html'}")

    # English techniques
    (REPO / "en" / "techniques" / "index.html").write_text(build_techniques_en(), encoding="utf-8")
    print(f"✅ {REPO / 'en/techniques/index.html'}")

    # Vietnamese index — replace existing
    vi_index = REPO / "vi" / "index.html"
    if vi_index.exists():
        vi_index.write_text(build_index_vi(), encoding="utf-8")
        print(f"✅ {vi_index}")

    # Vietnamese techniques
    (REPO / "vi" / "techniques" / "index.html").write_text(build_techniques_vi(), encoding="utf-8")
    print(f"✅ {REPO / 'vi/techniques/index.html'}")

    print("\n✅ All pages built with Yin Yang theme!")

if __name__ == "__main__":
    main()
