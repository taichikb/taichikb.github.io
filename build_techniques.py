#!/usr/bin/env python3
"""
Build EN and VI techniques pages for taichikb.github.io
Uses PDF content and follows TennisKB structure
"""
import os
import re
from pathlib import Path

REPO_ROOT = Path("D:/Taichi-Health-Finance/Intranet/taichikb_repo")

def read_base_template(lang="en"):
    """Read the base template for a language"""
    if lang == "en":
        template_path = REPO_ROOT / "index_clean.html"
    else:
        template_path = REPO_ROOT / "vi" / "index.html"
    
    with open(template_path, 'r', encoding='utf-8') as f:
        return f.read()

def extract_content(html):
    """Extract main content from template (between <main> tags)"""
    # Find the main content area
    main_start = html.find('<main')
    if main_start == -1:
        main_start = html.find('<article')
    main_end = html.find('</main>')
    if main_end == -1:
        main_end = html.find('</article>')
    if main_start != -1 and main_end != -1:
        return html[main_start:main_end+7]
    return ""

def replace_content(template, new_content, lang="en"):
    """Replace the main content in template"""
    main_start = template.find('<main')
    if main_start == -1:
        main_start = template.find('<article')
    main_end = template.find('</main>')
    if main_end == -1:
        main_end = template.find('</article>')
    
    if main_start != -1 and main_end != -1:
        return template[:main_start] + new_content + template[main_end+7:]
    return template

def build_techniques_en():
    """Build English techniques page"""
    template = read_base_template("en")
    
    content = '''<main class="techniques-page" role="main">
    <article class="technique-content">
        <header class="page-header">
            <h1>Chen Style Tai Chi Techniques</h1>
            <p class="page-subtitle">Fundamental methods and principles from the Chen family tradition</p>
        </header>
        
        <nav class="technique-nav" aria-label="Technique categories">
            <ul>
                <li><a href="#eight-methods" class="active">Eight Methods (Ba Fa)</a></li>
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
            <h2>Eight Methods (八法 - Ba Fa)</h2>
            <div class="technique-card">
                <h3>Peng (掤) - Ward Off</h3>
                <p>The fundamental expanding energy, like water supporting a boat. Peng is the root of all Tai Chi energies - an upward and outward expansive force that neutralizes incoming pressure.</p>
            </div>
            <div class="technique-card">
                <h3>Lu (履) - Rollback</h3>
                <p>Sideways yielding energy that leads the opponent's force into emptiness. Lu follows the incoming force and redirects it laterally without resistance.</p>
            </div>
            <div class="technique-card">
                <h3>Ji (擠) - Press</h3>
                <p>Forward squeezing energy generated from the ground through the legs, directed through the hands. Ji compresses the opponent's space.</p>
            </div>
            <div class="technique-card">
                <h3>An (按) - Push</h3>
                <p>Downward and forward pressing energy. An settles the opponent's structure and uproots their balance through sinking force.</p>
            </div>
            <div class="technique-card">
                <h3>Cai (採) - Pluck</h3>
                <p>Sudden downward jerking energy, like picking fruit. Cai disrupts the opponent's root with a quick, sharp pull.</p>
            </div>
            <div class="technique-card">
                <h3>Lie (挒) - Split</h3>
                <p>Spiraling, rending energy that separates connected parts. Lie uses opposing forces to tear the opponent's structure apart.</p>
            </div>
            <div class="technique-card">
                <h3>Zhou (肘) - Elbow Strike</h3>
                <p>Close-range striking energy using the elbow. Zhou generates power from the shoulder and back, delivering concentrated force.</p>
            </div>
            <div class="technique-card">
                <h3>Kao (靠) - Shoulder/Body Strike</h3>
                <p>Full-body leaning energy. Kao uses the shoulder, back, or hip to unbalance the opponent through body weight transfer.</p>
            </div>
            <p class="section-note"><em>Source: "Chen Style TaiChi Chuan - Eight Methods" PDF</em></p>
        </section>
        
        <section id="history" class="technique-section">
            <h2>History & Lineage</h2>
            <div class="technique-card">
                <h3>Chen Village Origins</h3>
                <p>Chen Style Tai Chi originated in Chenjiagou (Chen Village), Wen County, Henan Province, China. The art was created by Chen Wangting (1600-1680), 9th generation Chen family member, who synthesized family boxing with Qi cultivation, Daoist philosophy, and military strategy.</p>
            </div>
            <div class="technique-card">
                <h3>Key Generations</h3>
                <ul>
                    <li><strong>Chen Wangting</strong> - Founder, created 7 routines</li>
                    <li><strong>Chen Changxing</strong> (14th gen) - Taught Yang Luchan</li>
                    <li><strong>Chen Fake</strong> (17th gen) - Spread art to Beijing</li>
                    <li><strong>Chen Xiaowang</strong> (19th gen) - Global ambassador</li>
                </ul>
            </div>
            <div class="technique-card">
                <h3>Two Main Forms</h3>
                <p><strong>Lao Jia (Old Frame)</strong> - Large circles, obvious silk reeling, lower stances.<br>
                <strong>Xin Jia (New Frame)</strong> - Smaller circles, more subtle silk reeling, higher stances, more fajin.</p>
            </div>
            <p class="section-note"><em>Source: "Chen Style TaiChi Chuan - History" PDF</em></p>
        </section>
        
        <section id="la-jin" class="technique-section">
            <h2>La Jin (拉筋) - Pulling Tendons</h2>
            <div class="technique-card">
                <h3>Purpose</h3>
                <p>La Jin stretches the tendons, opens the joints, and lengthens the myofascial chains. It prepares the body for silk reeling (Chan Si) by creating elasticity in the connective tissue.</p>
            </div>
            <div class="technique-card">
                <h3>Key Principles</h3>
                <ul>
                    <li>Relax (Song) - release unnecessary tension</li>
                    <li>Extend (Shen) - lengthen through joints</li>
                    <li>Connect (Tong) - link fingers to toes</li>
                    <li>Breathe - coordinate with Tu Na</li>
                </ul>
            </div>
            <div class="technique-card">
                <h3>Common Exercises</h3>
                <ul>
                    <li>Standing La Jin - arms forward, sink and stretch</li>
                    <li>Seated La Jin - legs extended, reach forward</li>
                    <li>Partner La Jin - mutual stretching</li>
                </ul>
            </div>
            <p class="section-note"><em>Source: "La Kinh" PDF & "Lu Jin - Lu Kinh - La Kinh" PDF</em></p>
        </section>
        
        <section id="lu-jin" class="technique-section">
            <h2>Lu Jin (履勁) - Rollback Energy</h2>
            <div class="technique-card">
                <h3>Definition</h3>
                <p>Lu is the second of the Eight Methods. It is a yielding, redirecting energy that receives incoming force and leads it sideways into emptiness. The body rotates around the central axis while the arms maintain connection.</p>
            </div>
            <div class="technique-card">
                <h3>Key Points</h3>
                <ul>
                    <li>Do not resist - follow the force</li>
                    <li>Rotate the waist (Yao) as the axis</li>
                    <li>Keep arms in the "Lu" arc - neither collapsing nor pushing</li>
                    <li>Sink the weight (Chen) into the rear foot</li>
                </ul>
            </div>
            <div class="technique-card">
                <h3>Application</h3>
                <p>In push hands, Lu neutralizes a direct push by turning the torso and guiding the force past your center. The opponent's momentum continues forward while you remain stable.</p>
            </div>
            <p class="section-note"><em>Source: "Lu Jin - Lu Kinh - La Kinh" PDF</em></p>
        </section>
        
        <section id="tu-na" class="technique-section">
            <h2>Tu Na (吐納) - Breathing Method</h2>
            <div class="technique-card">
                <h3>Tu (吐) - Exhale</h3>
                <p>Expel stale Qi. Exhale through the mouth during fajin (power release) or when sinking. The exhale drives Qi to the extremities.</p>
            </div>
            <div class="technique-card">
                <h3>Na (納) - Inhale</h3>
                <p>Gather fresh Qi. Inhale through the nose during opening/upward movements. The inhale draws Qi into the Dantian.</p>
            </div>
            <div class="technique-card">
                <h3>Coordination</h3>
                <ul>
                    <li>Natural breathing for form practice</li>
                    <li>Reverse breathing for Nei Gong</li>
                    <li>Breath matches movement - open/inhale, close/exhale</li>
                    <li>Never force - let breath follow intention (Yi)</li>
                </ul>
            </div>
            <p class="section-note"><em>Source: "Chinese sources-2.md" - Tu Na section</em></p>
        </section>
        
        <section id="nei-gong" class="technique-section">
            <h2>Nei Gong (內功) - Internal Work</h2>
            <div class="technique-card">
                <h3>Three Treasures (San Bao)</h3>
                <ul>
                    <li><strong>Jing (精)</strong> - Essence, stored in kidneys</li>
                    <li><strong>Qi (氣)</strong> - Vital energy, cultivated in Dantian</li>
                    <li><strong>Shen (神)</strong> - Spirit, manifested in the eyes/intent</li>
                </ul>
            </div>
            <div class="technique-card">
                <h3>Core Practices</h3>
                <ul>
                    <li>Zhan Zhuang (Standing Post) - build root and Qi</li>
                    <li>Chan Si Gong (Silk Reeling) - spiral whole-body connection</li>
                    <li>Dantian rotation - internal engine</li>
                    <li>Meridian circulation - Microcosmic Orbit</li>
                </ul>
            </div>
            <p class="section-note"><em>Source: "Chinese sources-2.md" - Nei Gong section</em></p>
        </section>
        
        <section id="sword" class="technique-section">
            <h2>Sword (劍 - Jian)</h2>
            <div class="technique-card">
                <h3>Chen Style Sword Principles</h3>
                <p>The sword extends the body's energy. The 49-posture Chen Sword form combines soft flowing movements with sudden fajin releases. Key: the tip follows the Yi (intent), the body moves as one unit.</p>
            </div>
            <div class="technique-card">
                <h3>Four Major Techniques</h3>
                <ul>
                    <li><strong>Ci (刺)</strong> - Thrust: direct, penetrating</li>
                    <li><strong>Pi (劈)</strong> - Chop: downward cleaving</li>
                    <li><strong>Liao (撩)</strong> - Flick: upward wrist snap</li>
                    <li><strong>Dian (點)</strong> - Point: precise fingertip control</li>
                </ul>
            </div>
            <p class="section-note"><em>Source: "Chinese sources-2.md" - Sword section</em></p>
        </section>
        
        <section id="ethics" class="technique-section">
            <h2>Martial Ethics (武德 - Wu De)</h2>
            <div class="technique-card">
                <h3>Five Virtues</h3>
                <ul>
                    <li><strong>Ren (仁)</strong> - Benevolence: protect the weak</li>
                    <li><strong>Yi (義)</strong> - Righteousness: do what is right</li>
                    <li><strong>Li (禮)</strong> - Respect: honor teachers, peers, art</li>
                    <li><strong>Zhi (智)</strong> - Wisdom: discernment in action</li>
                    <li><strong>Xin (信)</strong> - Trustworthiness: keep your word</li>
                </ul>
            </div>
            <div class="technique-card">
                <h3>Training Principles</h3>
                <ul>
                    <li>Perseverance (Heng) - daily practice</li>
                    <li>Humility (Qian) - empty cup mindset</li>
                    <li>Patience (Ren) - Kung Fu takes time</li>
                </ul>
            </div>
            <p class="section-note"><em>Source: "Chinese sources-2.md" - Ethics section</em></p>
        </section>
        
        <footer class="page-footer">
            <p><a href="/en/">← Back to English Home</a> | <a href="/vi/techniques/">Tiếng Việt</a></p>
        </footer>
    </article>
</main>'''
    
    # Also need to add navigation - replace the nav in template
    # First, let's find and replace the nav section
    nav_replacement = '''<nav class="main-nav" role="navigation" aria-label="Main navigation">
    <div class="nav-container">
        <a href="/en/" class="nav-brand">🏠 TaichiKB</a>
        <ul class="nav-links">
            <li><a href="/en/">Home</a></li>
            <li><a href="/en/books/">Books</a></li>
            <li><a href="/en/deep-dives/">Deep Dives</a></li>
            <li><a href="/en/articles/">Chen Articles</a></li>
            <li><a href="/en/techniques/" class="active">Techniques</a></li>
            <li><a href="/vi/techniques/" class="lang-switch">🇻🇳 Tiếng Việt</a></li>
        </ul>
        <button class="theme-toggle" id="themeToggle" aria-label="Toggle dark mode">🌙</button>
    </div>
</nav>'''
    
    # Replace nav in template
    nav_start = template.find('<nav class="main-nav"')
    if nav_start == -1:
        nav_start = template.find('<nav ')
    nav_end = template.find('</nav>')
    if nav_start != -1 and nav_end != -1:
        template = template[:nav_start] + nav_replacement + template[nav_end+6:]
    
    final_html = replace_content(template, content, "en")
    return final_html

def build_techniques_vi():
    """Build Vietnamese techniques page"""
    template = read_base_template("vi")
    
    content = '''<main class="techniques-page" role="main">
    <article class="technique-content">
        <header class="page-header">
            <h1>Kỹ Thuật Trần thức Thái cực quyền</h1>
            <p class="page-subtitle">Các phương pháp và nguyên lý cơ bản từ truyền thống họ Chen</p>
        </header>
        
        <nav class="technique-nav" aria-label="Danh mục kỹ thuật">
            <ul>
                <li><a href="#eight-methods" class="active">Bát Pháp (八法)</a></li>
                <li><a href="#history">Lịch Sử & Truyền Thống</a></li>
                <li><a href="#la-jin">La Kinh (拉筋)</a></li>
                <li><a href="#lu-jin">Lữ Kinh (履勁)</a></li>
                <li><a href="#tu-na">Tổ Nha (吐納)</a></li>
                <li><a href="#nei-gong">Nội Công (內功)</a></li>
                <li><a href="#sword">Kiếm (劍)</a></li>
                <li><a href="#ethics">Võ Đức (武德)</a></li>
            </ul>
        </nav>
        
        <section id="eight-methods" class="technique-section">
            <h2>Bát Pháp (八法 - Ba Fa)</h2>
            <div class="technique-card">
                <h3>Bình (掤) - Chânẩy</h3>
                <p>Năng lượng giãn nở cơ bản, như nước đỡ thuyền. Bình là gốc của tất cả các năng lực Thiền Võ - một lực giãn nở lên và ra ngoài trung hòa áp lực đến.</p>
            </div>
            <div class="technique-card">
                <h3>Lữ (履) - Lướt/Gác</h3>
                <p>Năng lượng nhường bên dẫn dắt lực đối phương vào hư không. Lữ theo sau lực đến và chuyển hướng nó theo chiều ngang mà không cưỡng lại.</p>
            </div>
            <div class="technique-card">
                <h3>Crowd (擠) - Ép</h3>
                <p>Năng lượng nén về phía trước sinh từ mặt đất qua chân, dẫn dắt qua tay. Crowd nén không gian của đối phương.</p>
            </div>
            <div class="technique-card">
                <h3>An (按) - Đẩy</h3>
                <p>Năng lượng đè xuống và đẩy về trước. An落ち着 cấu trúc đối phương và làm rễ bề của họ bằng lực chìm.</p>
            </div>
            <div class="technique-card">
                <h3>Thái (採) - Hái</h3>
                <p>Năng lượng giật xuống đột ngột, như hái trái cây. Thái làm rung chuyển gốc rễ của đối phương bằng một cái kéo nhanh, sắc bén.</p>
            </div>
            <div class="technique-card">
                <h3>Liê (挒) - Tách</h3>
                <p>Năng lượng xoắn ốc, tách rời các bộ phận liên kết. Liê sử dụng lực đối nghịch để xé rách cấu trúc đối phương.</p>
            </div>
            <div class="technique-card">
                <h3>Chủ (肘) - Đánh Chỏ</h3>
                <p>Năng lượng đánh gần bằng chỏ. Chủ sinh lực từ vai và lưng, tập trung lực vào một điểm.</p>
            </div>
            <div class="technique-card">
                <h3>Khào (靠) - Đ Вал Going/Lean</h3>
                <p>Năng lượng trần cả người. Khào dùng vai, lưng hoặc hông để làm mất cân bằng đối phương bằng chuyển dịch trọng tâm.</p>
            </div>
            <p class="section-note"><em>Nguồn: "Chen Style TaiChi Chuan - Eight Methods" PDF</em></p>
        </section>
        
        <section id="history" class="technique-section">
            <h2>Lịch Sử & Truyền Thống</h2>
            <div class="technique-card">
                <h3>Nguồn Gốc Làng Chen</h3>
                <p>Trần thức Thái cực quyền bắt nguồn từ Làng Chen (Chenjiagou), huyện Wen, tỉnh Hà Nam, Trung Quốc. Nghệ thuật được sáng lập bởi Trần Vương Đình (Chen Wangting, 1600-1680), người thế hệ 9 của gia tộc Chen, người đã tổng hợp quyền gia truyền với tu hành Khí, triết học Đạo giáo và chiến thuật quân sự.</p>
            </div>
            <div class="technique-card">
                <h3>Các Thế Hệ Then Chốt</h3>
                <ul>
                    <li><strong>Trần Vương Đình</strong> - Người sáng lập, tạo 7 bộ quyền</li>
                    <li><strong>Trần Trưởng Hưng</strong> (thế hệ 14) - Dạy Dương Lục Tranh</li>
                    <li><strong>Trần Phát</strong> (Chen Fake, thế hệ 17) - Lan truyền nghệ thuật đến Bắc Kinh</li>
                    <li><strong>Trần Tiểu Vương</strong> (Chen Xiaowang, thế hệ 19) - Đại sứ toàn cầu</li>
                </ul>
            </div>
            <div class="technique-card">
                <h3>Hai Bộ Chính Thống</h3>
                <p><strong>Lão Gia (Old Frame)</strong> - Vòng tròn lớn, chanın rõ rệt, bước thấp.<br>
                <strong>Tân Gia (New Frame)</strong> - Vòng tròn nhỏ, chanın tinh tế hơn, bước cao hơn, nhiều phát lực hơn.</p>
            </div>
            <p class="section-note"><em>Nguồn: "Chen Style TaiChi Chuan - History" PDF</em></p>
        </section>
        
        <section id="la-jin" class="technique-section">
            <h2>La Kinh (拉筋) - Kéo Gân</h2>
            <div class="technique-card">
                <h3>Mục Đích</h3>
                <p>La Kinh kéo giãn gân, mở khớp, và kéo dài các chuỗi cơ-màng. Nó chuẩn bị cơ thể cho Chân Tư (Silk Reeling) bằng cách tạo độ đàn hồi cho mô liên kết.</p>
            </div>
            <div class="technique-card">
                <h3>Nguyên Tắc Cốt Lõi</h3>
                <ul>
                    <li>Thư (Song) - thả bỏ căng thẳng không cần thiết</li>
                    <li>Kéo (Thân) - kéo dài qua các khớp</li>
                    <li>Kết (Thông) - nối ngón tay đến ngón chân</li>
                    <li>Thở - phối hợp với Tổ Nha</li>
                </ul>
            </div>
            <div class="technique-card">
                <h3>Bài Tập Phổ Biến</h3>
                <ul>
                    <li>La Kinh đứng - tay伸 ra, chìm và kéo</li>
                    <li>La Kinh ngồi - chân duỗi, về phía trước</li>
                    <li>La Kinh đôi - kéo giãn lẫn nhau</li>
                </ul>
            </div>
            <p class="section-note"><em>Nguồn: "La Kinh" PDF & "Lu Jin - Lu Kinh - La Kinh" PDF</em></p>
        </section>
        
        <section id="lu-jin" class="technique-section">
            <h2>Lữ Kinh (履勁) - Năng Lực Lướt</h2>
            <div class="technique-card">
                <h3>Định Nghĩa</h3>
                <p>Lữ là phương pháp thứ hai trong Bát Pháp. Là năng lượng nhường, dẫn dắt nhận lực đến và dẫn nó sang bên vào hư không. Cơ thể xoay quanh trục trung tâm trong khi tay duy trì liên kết.</p>
            </div>
            <div class="technique-card">
                <h3>Điểm Then Chốt</h3>
                <ul>
                    <li>Không cưỡng lại - theo sau lực</li>
                    <li>Xoay eo (Yao) làm trục</li>
                    <li>Giữ tay trong cung "Lữ" - không sụp cũng không đẩy</li>
                    <li>Chìm trọng lực (Trần) vào chân sau</li>
                </ul>
            </div>
            <div class="technique-card">
                <h3>Ứng Dụng</h3>
                <p>Trong đẩy tay, Lữ trung hòa đòn đẩy thẳng bằng cách xoay thân và dẫn lực qua trung tâm. Động lượng đối phương tiếp tục về trước trong khi bạn ổn định.</p>
            </div>
            <p class="section-note"><em>Nguồn: "Lu Jin - Lu Kinh - La Kinh" PDF</em></p>
        </section>
        
        <section id="tu-na" class="technique-section">
            <h2>Tổ Nha (吐納) - Phương Pháp Thở</h2>
            <div class="technique-card">
                <h3>Tổ (吐) - Thở Ra</h3>
                <p>Thải Khí cũ. Thở ra qua miệng khi phát lực (fajin) hoặc khi chìm. Hơi thở ra dẫn Khí đến chi cuối.</p>
            </div>
            <div class="technique-card">
                <h3>Nha (納) - Thở Vào</h3>
                <p>Tụ Khí tươi. Thở vào qua mũi khi mở/lên. Hơi thở vào kéo Khí vào Đan Điền.</p>
            </div>
            <div class="technique-card">
                <h3>Phối Hợp</h3>
                <ul>
                    <li>Thở tự nhiên khi luyện bộ</li>
                    <li>Thở ngược cho Nội Công</li>
                    <li>Hơi thở theo động tác - mở/hít, khép/thở</li>
                    <li>Không ép buộc - để hơi thở theo Ý (Intention)</li>
                </ul>
            </div>
            <p class="section-note"><em>Nguồn: "Chinese sources-2.md" - Phần Tu Na</em></p>
        </section>
        
        <section id="nei-gong" class="technique-section">
            <h2>Nội Công (內功) - Công Phu Nội</h2>
            <div class="technique-card">
                <h3>Tam Bảo (Three Treasures)</h3>
                <ul>
                    <li><strong>Tinh (精)</strong> - Tinh huyết, tồn tại tại thận</li>
                    <li><strong>Khí (氣)</strong> - Năng lượng sống, tu tại Đan Điền</li>
                    <li><strong>Thần (神)</strong> - Thần trí, biểu hiện qua mắt/ý chí</li>
                </ul>
            </div>
            <div class="technique-card">
                <h3>Luyện Tập Cốt Lõi</h3>
                <ul>
                    <li>Trạm Trang (Standing Post) - xây gốc và Khí</li>
                    <li>Chân Tư Công (Silk Reeling) - xoắn kết nối toàn thân</li>
                    <li>Xoay Đan Điền - động cơ nội tại</li>
                    <li>Tu hành kinh lạc - Chu Thiên Tiểu</li>
                </ul>
            </div>
            <p class="section-note"><em>Nguồn: "Chinese sources-2.md" - Phần Nội Công</em></p>
        </section>
        
        <section id="sword" class="technique-section">
            <h2>Kiếm (劍 - Jian)</h2>
            <div class="technique-card">
                <h3>Nguyên Lý Kiếm Phái Chen</h3>
                <p>Kiếm mở rộng năng lượng cơ thể. Bộ Kiếm 49 thức Chen kết hợp động tác mềm mại flow với phát lực fajin đột ngột. Then chốt: đầu kiếm theo Ý (intent), cơ thể động như một khối.</p>
            </div>
            <div class="technique-card">
                <h3>Bốn Kỹ Thuật Chính</h3>
                <ul>
                    <li><strong>Thi (刺)</strong> - Xuyên: thẳng, xuyên thấu</li>
                    <li><strong>Bạch (劈)</strong> - Eff�: chém xuống</li>
                    <li><strong>Liêu (撩)</strong> - Bật: củng cổ tay lên</li>
                    <li><strong>Điểm (點)</strong> - Chấm: kiểm soát đầu ngón tay chính xác</li>
                </ul>
            </div>
            <p class="section-note"><em>Nguồn: "Chinese sources-2.md" - Phần Kiếm</em></p>
        </section>
        
        <section id="ethics" class="technique-section">
            <h2>Võ Đức (武德) - Đạo Đức Võ Thuật</h2>
            <div class="technique-card">
                <h3>Ngũ Đức (Five Virtues)</h3>
                <ul>
                    <li><strong>Nhân (仁)</strong> - Nhân ái: bảo vệ yếu thế</li>
                    <li><strong>Nghĩa (義)</strong> - Nghĩa khí: làm điều đúng</li>
                    <li><strong>Lễ (禮)</strong> - Lễ nghĩa: tôn sư trọng đạo</li>
                    <li><strong>Trí (智)</strong> - Trí tuệ: phân biệt trong hành động</li>
                    <li><strong>Tín (信)</strong> - Tín nghĩa: giữ lời hứa</li>
                </ul>
            </div>
            <div class="technique-card">
                <h3>Nguyên Tắc Luyện Tập</h3>
                <ul>
                    <li>Kiên trì (Hằng) - tập hàng ngày</li>
                    <li>Khiêm tốn (Khiêm) - tâm thái ly cốc</li>
                    <li>Ki nhẫn (Nhẫn) - Công phu cần thời gian</li>
                </ul>
            </div>
            <p class="section-note"><em>Nguồn: "Chinese sources-2.md" - Phần Đạo Đức</em></p>
        </section>
        
        <footer class="page-footer">
            <p><a href="/vi/">← Về Trang Chủ</a> | <a href="/en/techniques/">English</a></p>
        </footer>
    </article>
</main>'''
    
    nav_replacement = '''<nav class="main-nav" role="navigation" aria-label="Điều hướng chính">
    <div class="nav-container">
        <a href="/vi/" class="nav-brand">🏠 TaichiKB</a>
        <ul class="nav-links">
            <li><a href="/vi/">Trang Chủ</a></li>
            <li><a href="/vi/books/">Sách</a></li>
            <li><a href="/vi/deep-dives/">Sâu Sâu</a></li>
            <li><a href="/vi/articles/">Bài Chen</a></li>
            <li><a href="/vi/techniques/" class="active">Kỹ Thuật</a></li>
            <li><a href="/en/techniques/" class="lang-switch">🇬🇧 English</a></li>
        </ul>
        <button class="theme-toggle" id="themeToggle" aria-label="Chế độ tối">🌙</button>
    </div>
</nav>'''
    
    nav_start = template.find('<nav class="main-nav"')
    if nav_start == -1:
        nav_start = template.find('<nav ')
    nav_end = template.find('</nav>')
    if nav_start != -1 and nav_end != -1:
        template = template[:nav_start] + nav_replacement + template[nav_end+6:]
    
    final_html = replace_content(template, content, "vi")
    return final_html

def build_landing_page():
    """Build clean landing page (index.html) without top band"""
    template = read_base_template("en")
    
    content = '''<main class="landing-page" role="main">
    <header class="hero">
        <div class="hero-content">
            <h1>Taichi Knowledge Base</h1>
            <p class="tagline">Chen Style Tai Chi — Techniques, History, and Internal Arts</p>
            <p class="subtitle">Trần thức Thái cực quyền — Kỹ Thuật, Lịch Sử, và Nội Công</p>
        </div>
    </header>
    
    <section class="features-grid">
        <article class="feature-card">
            <h2><a href="/en/techniques/">🇬🇧 Techniques (EN)</a></h2>
            <p>Eight Methods, History, La Jin, Lu Jin, Tu Na, Nei Gong, Sword, Ethics</p>
        </article>
        <article class="feature-card">
            <h2><a href="/vi/techniques/">🇻🇳 Kỹ Thuật (VI)</a></h2>
            <p>Bát Pháp, Lịch Sử, La Kinh, Lữ Kinh, Tổ Nha, Nội Công, Kiếm, Võ Đức</p>
        </article>
        <article class="feature-card">
            <h2><a href="/en/books/">📖 Books</a></h2>
            <p>Classic and modern texts on Chen Style Tai Chi</p>
        </article>
        <article class="feature-card">
            <h2><a href="/en/deep-dives/">🌊 Deep Dives</a></h2>
            <p>Detailed analyses of specific principles and applications</p>
        </article>
        <article class="feature-card">
            <h2><a href="/en/articles/">📚 Chen Articles</a></h2>
            <p>Translated articles from Chen Style Tai Chi sources</p>
        </article>
    </section>
    
    <footer class="site-footer">
        <p>Built with ❤️ for the Vietnamese Tai Chi community 🎾 by Henry Phạm</p>
        <p>Trang web này được xây dựng với ❤️ cho cộng đồng Thiền Võ Việt Nam 🎾 by Henry Phạm</p>
    </footer>
</main>'''
    
    nav_replacement = '''<nav class="main-nav" role="navigation" aria-label="Main navigation">
    <div class="nav-container">
        <a href="/en/" class="nav-brand">🏠 TaichiKB</a>
        <ul class="nav-links">
            <li><a href="/en/">Home</a></li>
            <li><a href="/en/books/">Books</a></li>
            <li><a href="/en/deep-dives/">Deep Dives</a></li>
            <li><a href="/en/articles/">Chen Articles</a></li>
            <li><a href="/en/techniques/" class="active">Techniques</a></li>
            <li><a href="/vi/techniques/" class="lang-switch">🇻🇳 Tiếng Việt</a></li>
        </ul>
        <button class="theme-toggle" id="themeToggle" aria-label="Toggle dark mode">🌙</button>
    </div>
</nav>'''
    
    nav_start = template.find('<nav class="main-nav"')
    if nav_start == -1:
        nav_start = template.find('<nav ')
    nav_end = template.find('</nav>')
    if nav_start != -1 and nav_end != -1:
        template = template[:nav_start] + nav_replacement + template[nav_end+6:]
    
    final_html = replace_content(template, content, "en")
    return final_html

def main():
    print("Building techniques pages...")
    
    # Create en/techniques directory
    en_tech_dir = REPO_ROOT / "en" / "techniques"
    en_tech_dir.mkdir(parents=True, exist_ok=True)
    
    # Create vi/techniques directory
    vi_tech_dir = REPO_ROOT / "vi" / "techniques"
    vi_tech_dir.mkdir(parents=True, exist_ok=True)
    
    # Build pages
    en_html = build_techniques_en()
    vi_html = build_techniques_vi()
    landing_html = build_landing_page()
    
    # Write files
    with open(en_tech_dir / "index.html", 'w', encoding='utf-8') as f:
        f.write(en_html)
    print(f"✅ Created {en_tech_dir / 'index.html'}")
    
    with open(vi_tech_dir / "index.html", 'w', encoding='utf-8') as f:
        f.write(vi_html)
    print(f"✅ Created {vi_tech_dir / 'index.html'}")
    
    # Update landing page
    with open(REPO_ROOT / "index.html", 'w', encoding='utf-8') as f:
        f.write(landing_html)
    print(f"✅ Updated {REPO_ROOT / 'index.html'}")
    
    print("\n✅ All pages built successfully!")

if __name__ == "__main__":
    main()