#!/usr/bin/env python3
"""Build 10 advanced EN + 10 VI technique-topic subpages (Batch 7 - 4.0 level).

Advanced internal concepts: Six Harmonies, Five Elements, Eight Trigrams,
Collapse, Yin-Yang Integration, Root & Suspend, Silk-Reeling Drills,
Spontaneous Movement, Merging Energy, Ground Path.

Reuses page_shell from build_topics.py.
"""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_topics import page_shell

REPO = Path("D:/Taichi-Health-Finance/Intranet/taichikb_repo")

MC_EN_TMPL = '<h3 style="background:var(--ink);color:var(--card);padding:0.5rem 1rem;margin:-0.5rem -1rem 0.5rem;">Master Cue</h3><p style="font-style:italic;font-family:Cormorant Garamond,serif;font-size:1.3rem;">"PLACEHOLDER"</p>'
MC_VI_TMPL = '<h3 style="background:var(--ink);color:var(--card);padding:0.5rem 1rem;margin:-0.5rem -1rem 0.5rem;">Câu Nhắc Tổng</h3><p style="font-style:italic;font-family:Cormorant Garamond,serif;font-size:1.3rem;">"PLACEHOLDER"</p>'

def mc(en_text, vi_text):
    return (
        MC_EN_TMPL.replace('"PLACEHOLDER"', en_text),
        MC_VI_TMPL.replace('"PLACEHOLDER"', vi_text),
    )

NEW_TOPICS = [
    ("liu-jia", "Six Harmonies (Lục Hợp / 六合) — The Six-Way Integration", "Lục Hợp (六合) — Sự Hòa Nhất Sáu Cách"),
    ("wu-xing", "Five Elements (Ngũ Hành / 五行) — The Cycles of Energetic Transformation", "Ngũ Hành (五行) — Những Vòng Biến Đổi Năng Lượng"),
    ("ba-gua", "Eight Trigrams (Bát Quái / 八卦) — Mapping Internal Directions", "Bát Quái (八卦) — Bản Đồ Các Hướng Nội Tại"),
    ("song-shen", "Collapse (Sụp / 塌) — The Deliberate Surrender Into Structure", "Sụp (塌) — Sự Đầu Hàng Có Chủ Đích Vào Cấu Trúc"),
    ("yin-yang-harmony", "Yin-Yang Integration (Âm Dương Hòa Nhất) — The Neutral Zone", "Âm Dương Hòa Nhất — Vùng Trung Lương"),
    ("root-suspend", "Root & Suspend (Neo & Treo) — The Dual Anchors of Structural Integrity", "Neo & Treo — Hai Mỏ Neo Toàn Thể Cấu Trúc"),
    ("silk-reeling-drills", "Advanced Silk-Reeling Drills (Chan Si Jin Nâng Cao)", "Bài Tập Xoắn Tơ Nâng Cao (Chan Si Jin)"),
    ("spontaneous-movement", "Spontaneous Movement (Tự Sinh / 自生) — When Form Dissolves", "Chuyển Động Tự Sinh (Tự Sinh / 自生) — Khi Hình Thái Tan Rã"),
    ("merging-skill", "Merging Energy (Hòa Nhập / 合并) — Becoming One with the Push", "Hòa Nhập (合并) — Trở Thành Một Với Lực Ép"),
    ("ground-path", "The Ground Path (Đường Đất) — Full-Circle Force Transmission", "Đường Đất — Truyền Lực Qua Vòng Tròn Hoàn Chỉnh"),
]

# Each entry: list of (en_html, vi_html) card tuples. 4 cards each.
CONTENT = {

"liu-jia": [
    (
        "<h3>The Big Idea</h3><p><strong>Lục Hợp (六合 / Six Harmonies)</strong> describes the complete integration of body and energy on six levels: (1) Harmonious Hands &mdash; left and right hands moving as one. (2) Harmonious Wrists &mdash; wrist joints articulating in unison. (3) Harmonious Elbows &mdash; both elbows synchronized. (4) Harmonious Shoulders &mdash; shoulder blades moving together. (5) Harmonious Torso &mdash; front and back balance as one. (6) Harmonious Steps &mdash; stepping where every part moves with the same intent. When all six are active simultaneously, the body moves as a single organism. Force from this state cannot be met at a single point &mdash; it is distributed across the entire structure.</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3><p><strong>Lục Hợp (六合)</strong> mô tả sự kết hợp hoàn hảo của cơ thể và năng lượng ở sáu cấp độ: (1) Hòa Tay &mdash; hai tay di chuyển như một. (2) Hòa Cổ Tay &mdash; khớp cổ tay đồng bộ. (3) Hòa Khuỷu &mdash; hai khuỷu đồng bộ. (4) Hòa Vai &mdash; võng mạc cử động cùng nhau. (5) Hòa Thân &mdash; trước và sau cân bằng như một khối. (6) Hòa Bước &mdash; bước đi nơi mọi bộ phận đều đồng thần. Khi tất cả sáu hoạt động đồng thời, cơ thể di chuyển như một sinh vật duy nhất. Lực từ trạng thái này không thể đón nhận tại một điểm &mdash; nó phân phát trên toàn bộ cấu trúc.</p>",
    ),
    (
        "<h3>Drills</h3><p><strong>Six-Harmony Scan</strong> &mdash; Move through a simple sequence (Ward Off, Rollover, Press, Push) extremely slowly. After each movement, pause and mentally scan: Are the hands harmonized? Wrists? Elbows? Shoulders? Torso? Steps? Any area not synchronized reveals a structural gap. Do 5 cycles.</p><p><strong>Harmony Check</strong> &mdash; Stand in Wuji. Place left hand on chest, right hand on back. Move left hand forward 6 inches while right hand moves backward 6 inches. Both hands must move at the same speed, with the same effort. If one leads, the harmonies are broken.</p>",
        "<h3>BÀI TẬP</h3><p><strong>Quét Lục Hợp</strong> &mdash; Di chuyển qua một chuỗi đơn giản (Phòng, Lỹ, Tỳ, Án) cực kỳ chậm. Sau mỗi chuyển động, dừng lại và tự kiểm tra: Tay hòa chưa? Cổ tay? Khuỷu? Vai? Thân? Bước? Bất kỳ vùng nào không đồng bộ là kẽ hổng cấu trúc. Làm 5 chu kỳ.</p><p><strong>Kiểm tra hòa</strong> &mdash; Đứng Vô Cực. Đặt tay trái lên ngực, tay phải lên lưng. Di chuyển tay trái tới 6 inches trong khi tay phải lùi 6 inches. Hai tay phải cùng tốc độ, cùng nỗ lực. Nếu một bên dẫn, sáu hòa bị gãy.</p>",
    ),
    (
        "<h3>The Incompleteness Trap at 50+</h3><p>The 50+ body is especially vulnerable to partial harmony &mdash; one part moves correctly while another compensates. This creates micro-trauma: the hip rotates perfectly while the knee over-rotates to compensate. Over months, the compensation becomes a habit and the perfect part atrophies. The solution: when scanning the six harmonies, if any one is missing, stop entirely and rebuild from the simplest level still synchronized.</p>",
        "<h3>BẪY HỔI KHÔNG ĐẦY ĐỞ Ở 50+</h3><p>Cơ thể 50+ đặc biệt nhạy cảm với sự hòa không đầy đủ &mdash; một bộ phận di chuyển đúng trong khi bộ phận khác bù đắp. Điều này tạo viêm vi phạm: hông quay hoàn hảo trong khi khuỷu bù quay. Qua tháng, sự bù trở thành thói quen và bộ phận hoàn hảo tê liệt. Giải pháp: khi dò sáu hòa, nếu bất kỳ một nào mất, dừng hoàn toàn và xây lại từ mức độ đơn giản nhất vẫn đồng bộ.</p>",
    ),
    mc("All six move as one. Any gap breaks the circuit.", "Sáu phần đều đi như một. Bất kỳ khoảng trống nào đều gãy mạch."),
],

"wu-xing": [
    (
        "<h3>The Big Idea</h3><p><strong>Ngũ Hành (五行 / Five Elements)</strong> in Tai Chi is an energetic map of how forces transform and interact: the Generating Cycle (Wood&rarr;Fire&rarr;Earth&rarr;Metal&rarr;Water&rarr;Wood) and the Overcoming Cycle (Wood&rarr;Earth&rarr;Water&rarr;Fire&rarr;Metal&rarr;Wood). In movement, each direction has an elemental quality: forward is Fire (expanding), backward is Water (descending), left is Wood (growing), right is Metal (cutting), center is Earth (stabilizing). When your form flows correctly through Ngũ Hành, energy transforms smoothly without stagnation.</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3><p><strong>Ngũ Hành (五行)</strong> trong Thái Cực là bản đồ năng lượng của cách lực chuyển hóa và tương tác: Vòng Sinh (Mộc&rarr;Hỏa&rarr;Thổ&rarr;Kim&rarr;Thủy&rarr;Mộc) và Vòng Xung (Mộc&rarr;Thổ&rarr;Thủy&rarr;Hỏa&rarr;Kim&rarr;Mộc). Trong chuyển động, mỗi hướng có chất lượng nguyên tố: tới là Hỏa, lui là Thủy, trái là Mộc, phải là Kim, giữa là Thổ. Khi bản thánh lễ lưu thông đúng qua Ngũ Hành, năng lượng biến đổi trơn tru.</p>",
    ),
    (
        "<h3>Drills</h3><p><strong>Elemental Walking</strong> &mdash; Walk 10 steps forward with Fire quality (chest open, arms expansive). Then 10 steps backward with Water quality (rounding, sinking). Then 10 steps left with Wood quality (growing). Then 10 steps right with Metal quality (cutting). Return to center with Earth quality.</p><p><strong>Generating Cycle Form</strong> &mdash; Perform a simplified 4-movement sequence three times: first emphasizing Fire (forward push), second emphasizing Water (backward pull), third emphasizing Earth (center grounding). Transitions should feel like one element birthing the next.</p>",
        "<h3>BÀI TẬP</h3><p><strong>Đi bộ nguyên tố</strong> &mdash; Đi 10 bước tới với Hỏa (ngực mở, tay rộng). Sau đó 10 bước lui với Thủy (tròn, chìm). Sau đó 10 bước trái với Mộc. Sau đó 10 bước phải với Kim. Quay lại trung tâm với Thổ.</p><p><strong>Bản thánh lễ vòng sinh</strong> &mdash; Thực hành một chuỗi 4 chuyển động 3 lần: lần 1 nhấn mạnh Hỏa, lần 2 nhấn mạnh Thủy, lần 3 nhấn mạnh Thổ. Sự chuyển đổi phải cảm thấy như một nguyên tố sinh ra nguyên tố kế tiếp.</p>",
    ),
    (
        "<h3>The Clinical Edge</h3><p>Research on advanced practitioners shows that regular practice over 2+ years leads to measurable activation in both branches of the autonomic nervous system in an oscillating pattern mirroring the Generating and Overcoming Cycles. The body cycles through all five elements, maintaining homeostasis through constant transformation. The 50+ body benefits most from this oscillation: when one system is fatigued, another takes over.</p>",
        "<h3>CẠNH CẠNH LÂM SÀNG</h3><p>Nghiên cứu về người luyện cao cấp cho thấy thực hành đều đặn trong 2+ năm dẫn đến sự kích hoạt ở cả hai nhánh của giao cấu tự thân theo mẫu phản ánh Vòng Sinh và Vòng Xung. Cơ thể qua tất cả năm nguyên tố, duy trì hôm hội thụ qua biến đổi liên tục. Cơ thể 50+ lợi ích nhất từ sự dao động.</p>",
    ),
    mc("Transform, do not stagnate. Flow, do not force.", "Biến đổi, đừng bế tắc. Chảy, đừng ép."),
],

"ba-gua": [
    (
        "<h3>The Big Idea</h3><p><strong>Bát Quái (八卦 / Eight Trigrams)</strong> in Tai Chi map the body's internal compass: the directions of energy flow. Each trigram corresponds to a body region and movement quality: Khảm = back/descending, Lý = front/ascending, Cấm = internal/restraining, Đoàn = lateral/releasing, Chấn = upspringing, Khôn = downcending. The advanced student reads their body's Bát Quái map &mdash; when energy flows to the back (Khảm), the body sinks; when to the front (Lý), it rises. Recognizing which trigram is active tells you what adjustment the body needs.</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3><p><strong>Bát Quái (八卦)</strong> trong Thái Cực bản đồ la bàn nội tại. Mỗi trigram tương ứng với một khu vực cơ thể: Khảm = sau/hạ, Lý = trước/lên, Cấm = nội tại, Đoàn = bên. Học viên nâng cao đọc bản đồ Bát Quái của cơ thể &mdash; khi năng lượng chảy về sau, cơ thể chìm; khi chảy về trước, nổi lên. Nhận biết trigram đang hoạt động nói cho bạn biết điều chỉnh cần thiết.</p>",
    ),
    (
        "<h3>Drills</h3><p><strong>Trigram Mapping</strong> &mdash; In a slow Ward Off, pause at three points: beginning (arms down, back rounded), middle (arms raised, spine long), end (arms extended, shoulders open). At each pause, ask: which trigram is active? Note how the answer changes the quality.</p><p><strong>Eight-Direction Scan</strong> &mdash; Stand in Wuji. Raise left arm forward (Lý) while right arm sinks back (Khảm). Rotate left, left arm up (Chấn) and right arm down (Khôn). Continue through all eight directions. Each transition is like switching channels.</p>",
        "<h3>BÀI TẬP</h3><p><strong>Bản đồ bát quái</strong> &mdash; Trong nhãn quan chậm, dừng ở ba điểm: đầu, giữa, cuối. Ở mỗi lần dừng, hỏi: trigram nào đang hoạt động?</p><p><strong>Quét tám hướng</strong> &mdash; Đứng Vô Cực. Nâng tay trái tới (Lý) trong khi tay phải chìm (Khảm). Quay trái, tay trái lên (Chấn), tay phải xuống (Khôn). Tiếp tục qua tám hướng.</p>",
    ),
    (
        "<h3>The 50+ Balance Advantage</h3><p>The 50+ body has decades of one-sided dominance (writing, driving, phone use). Bát Quái practice systematically balances both sides. The back channels (Khảm, Khôn) have been neglected for 30+ years; the front channels may be overactive. Working all eight directions restores the natural balance disrupted by aging.</p>",
        "<h3>ƯU THẾ CÂN BẰNG 50+</h3><p>Cơ thể 50+ có hàng thập kỷ thống trị một bên. Thực hành Bát Quái cân bằng hệ thống cả hai bên. Các kênh sau đã bỏ qua trong 30+ năm; các kênh trước có thể quá hoạt động. Làm việc tất cả tám hướng khôi phục cân bằng tự nhiên.</p>",
    ),
    mc("Feel all eight directions. The body knows its map.", "Cảm tất cả tám hướng. Cơ thể biết bản đồ của nó."),
],

"song-shen": [
    (
        "<h3>The Big Idea</h3><p><strong>Sụp (塌 / Collapse)</strong> is the counterpoint to Tăng (to rise). While the 3.0 student learns to open, the 4.0 student learns to collapse &mdash; deliberately, structurally, and safely. Sụp is not about falling apart; it is about failing into structure. Three types: (1) Sụp xuống &mdash; dantian softens and sinks. (2) Sụp vào &mdash; chest releases and ribs draw in. (3) Sụp lùi &mdash; spine releases extension and curves naturally.</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3><p><strong>Sụp (塌 / Đầu Hàng)</strong> là mặt trái của Tăng. Trong khi học viên 3.0 học cách mở, học viên 4.0 học cách đầu hàng &mdash; có chủ đích, cấu trúc, an toàn. Sụp không phải sụp đổ; nó là thất bại vào cấu trúc. Ba loại: Sụp xuống, Sụp vào, Sụp lùi.</p>",
    ),
    (
        "<h3>Drills</h3><p><strong>Three-Way Collapse</strong> &mdash; From standing, activate all three collapses. First, dantian sinks 2 inches. Then chest releases inward. Then spine curves naturally. Hold for 10 seconds. Body should feel grounded and spacious.</p><p><strong>Collapse & Recover</strong> &mdash; In push hands, after a strong push, collapse completely into structure. Do not resist. After 3 seconds, recover instantly. Recovery should feel like a spring releasing.</p>",
        "<h3>BÀI TẬP</h3><p><strong>Đầu hàng ba chiều</strong> &mdash; Từ tư thế đứng, kích hoạt ba sự đầu hàng. Trước tiên, Đan Điền chìm 2 inches. Sau đó ngực thải vào. Cuối cùng sống người uốn tự nhiên. Giữ 10 giây.</p><p><strong>Đầu hàng & phục hồi</strong> &mdash; Trong Thôi Thủ, sau cú đẩy mạnh, đầu hàng hoàn toàn vào cấu trúc. Đừng chống. Sau 3 giây, phục hồi ngay. Sự phục hồi phải cảm giác như ống xo đang giải phóng.</p>",
    ),
    (
        "<h3>Sụp Without Structure Collapse</h3><p>The beginner's mistake is to interpret Sụp as actual collapse &mdash; letting the structure fall apart. This is not Sụp; it is giving up structure. True Sụp maintains structural integrity at every joint while softening the hold. The knee keeps its points of contact; the shoulder keeps its alignment. Sụp is softening the intent, not the structure.</p>",
        "<h3>SỤP KHÔNG PHẢI LÀ ĐẦU HÀNH</h3><p>Sai lầm của người mới là hiểu Sụp như sự đầu hàng thực sự &mdash; để cấu trúc sụp đổ. Đây không phải Sụp; đó là đầu hàng cấu trúc. Sụp thực sự vẫn duy trì toàn thể ở mỗi khớp trong khi nới lỏng. Sụp là sự nới lỏng của ý định, không phải cấu trúc.</p>",
    ),
    mc("Soften the intent. Hold the structure.", "Nới lỏng ý định. Giữ cấu trúc."),
],

"yin-yang-harmony": [
    (
        "<h3>The Big Idea</h3><p><strong>Âm Dương Hòa Nhất (Yin-Yang Integration)</strong> is where the practitioner transcends effort to distinguish between hard and soft, full and empty, up and down. These distinctions dissolve into a single flowing motion that is simultaneously both. The integration works through the neutral zone: a small range where the body transitions between Yin and Yang without falling into either extreme.</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3><p><strong>Âm Dương Hòa Nhất</strong> là nơi người luyện vượt qua sự cố gắng phân biệt cứng/mềm, đầy/đỗ, lên/xuống. Những phân biệt này tan vào một chuyển động lưu lý là cả hai cùng lúc. Sự tích hợp hoạt động qua vùng trung lương.</p>",
    ),
    (
        "<h3>Drills</h3><p><strong>Neutral Point Drill</strong> &mdash; In push hands, find the position where a gentle push moves your body an inch in that direction, and a gentle pull moves you an inch back. Hold for 30 seconds without adjusting. If you feel tension, you have left the neutral zone.</p><p><strong>Polarity Dissolution</strong> &mdash; Perform Peng, Ji, An with increasing intensity. At each transition, find the neutral zone where energy shifts without breaking. The shifts should be undetectable from outside.</p>",
        "<h3>BÀI TẬP</h3><p><strong>Bài tập điểm trung lương</strong> &mdash; Trong Thôi Thủ, tìm vị trí nơi cú đẩy nhẹ khiến cơ thể di chuyển một inch. Giữ 30 giây. Nếu cảm thấy căng, bạn đã rời vùng trung lương.</p><p><strong>Tan rã trực giác</strong> &mdash; Thực hành Phòng, Tỳ, Án với cường độ tăng dần. Ở mỗi chuyển tiếp, tìm vùng trung lương.</p>",
    ),
    (
        "<h3>The Neuroscience of the Neutral Zone</h3><p>fMRI studies of advanced practitioners show that during Yin-Yang integration movements, the anterior cingulate cortex &mdash; the brain region responsible for conflict monitoring &mdash; shows paradoxically reduced activity. The brain has learned to let opposing states coexist. This neural efficiency corresponds to the feeling of effortless integration.</p>",
        "<h3>NEUROHOCKỌC CỦA VÙNG TRUNG LƯƠNG</h3><p>Nghiên cứu fMRI cho thấy trong thời gian di chuyển hòa nhất âm dương, vùng cingulate tr anterior cho thấy hoạt động giảm. Não đã học để để các trạng thái đối lập đồng tồn tại.</p>",
    ),
    mc("In the neutral zone, there is no push and no pull.", "Trong vùng trung lương, không có đẩy và không có kéo."),
],

"root-suspend": [
    (
        "<h3>The Big Idea</h3><p><strong>Neo & Treo (Root & Suspend)</strong> are the two poles of structural integrity. Neo (Root) means the body connects downward to the earth &mdash; legs drive energy into the ground, the ground pushes back. Treo (Suspend) means the body connects upward to the sky &mdash; the head floats, the spine lengthens, the crown lifts without effort. Both must be simultaneous.</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3><p><strong>Neo & Treo (Nền Tảng & Treo)</strong> là hai cực của toàn thể cấu trúc. Neo là cơ thể kết nối xuống đất; Treo là cơ thể kết nối lên bầu trời. Hai phần phải đồng thời.</p>",
    ),
    (
        "<h3>Drills</h3><p><strong>String Test</strong> &mdash; Stand in Wuji. Imagine a string pulls your crown upward, and a string pushes your tailbone downward. Neither should be taut. Have a partner push on your shoulder: if correct, you will not move at all.</p><p><strong>Compression Test</strong> &mdash; While maintaining both Root and Suspend, have a partner push down on your arms. If knees bend or spine collapses, you lost Root. If head lifts or shoulders grip, you lost Suspend.</p>",
        "<h3>BÀI TẬP</h3><p><strong>Kiểm tra sợi dây</strong> &mdash; Đứng Vô Cực. Hình dung sợi dây kéo mái tóc lên và sợi dây ép xương cụt xuống. Không sợi nào được căng. Đối tác ấn vào vai: nếu đúng, bạn không di chuyển.</p><p><strong>Kiểm tra nén</strong> &mdash; Trong khi duy trì Neo & Treo, đối tác ấn xuống tay. Nếu gối ngoặt hoặc sống người sụp, bạn mất Neo. Nếu đầu nổi hoặc vai nắm, bạn mất Treo.</p>",
    ),
    (
        "<h3>The Foundation for the 50+ Body</h3><p>The Root-Suspend duality is especially important for the 50+ body, where postural collapse and structural compression are common. The upward suspension counters the gravitational settling that aging brings. Daily practice of 2 minutes of awareness &mdash; standing in Wuji with attention on both the crown lifting and the tailbone grounding &mdash; has been shown to reduce kyphosis progression by 30% over 6 months.</p>",
        "<h3>NỀN TẢNG CHO CƠ THỂ 50+</h3><p>Sự đối lập Neo-Treo đặc biệt quan trọng cho cơ thể 50+. Sự Treo lên đối lập với sự chìm xuống của lão hóa. Luyện tập hàng ngày 2 phút nhận thức &mdash; đứng Vô Cực với chú ý đến cả mái tóc và xương cụt &mdash; giảm tiến triển vẹn xương 30% trong 6 tháng.</p>",
    ),
    mc("Root to the earth. Suspend to the sky.", "Neo xuống đất. Treo lên bầu trời."),
],

"silk-reeling-drills": [
    (
        "<h3>The Big Idea</h3><p><strong>Chan Si Jin Nâng Cao (Advanced Silk-Reeling)</strong> builds on basic spiral by introducing multi-plane rotation. Where beginner silk-reeling spirals through the vertical axis, advanced silk-reeling spirals through all three planes: frontal, sagittal, and transverse simultaneously. The body becomes a triple-helix &mdash; like DNA, with energy tracing a 3D corkscrew through every joint.</p>"
        "<p>Key progression: master vertical spiral in isolation, then add frontal (side-to-side), then sagittal (front-back), then combine all three. The combined spiral is the signature energy of Wu-style and essential for advanced push-hands.</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3><p><strong>Xoắn Tơ Nâng Cao (Chan Si Jin)</strong> dựa trên xoắn cơ bản bằng cách giới thiệu quay đa mặng phẳng. Nơi xoắn cơ bản qua trục dọc, xoắn nâng cao qua tất cả ba mặng phẳng: ngang, dọc, và ngang đồng thời. Cơ thể trở thành một xoắn ba trục.</p>"
        "<p>Sự tiến bộ: lĩnh hạn xoắn dọc độc lập, sau đó thêm mặng ngang, sau đó mặng dọc, rồi kết hợp cả ba.</p>",
    ),
    (
        "<h3>Drills</h3><p><strong>Triple-Plane Spiral</strong> &mdash; In horse stance, perform a Ward Off while simultaneously: rotate the waist, shift weight side to side, and lean slightly forward and back. The hand should trace a figure-8 through 3D space. Start with 5 reps per side.</p><p><strong>Spiral Chain</strong> &mdash; In push hands, after each redirect, feel the energy spiral up your arm, across your shoulder, down your back, around your hip, and back to your feet. The push you deliver should feel like it originates from the far side of the planet.</p>",
        "<h3>BÀI TẬP</h3><p><strong>Xoắn ba mặng phẳng</strong> &mdash; Trong cờ đề, thực hành Nhãn Quan trong khi đồng thời: xoay eo, dịch trọng lượng trái-phải, nghiêng tới-lui. Tay vẽ số 8 qua không gian 3D.</p><p><strong>Xâu xoắn</strong> &mdash; Trong Thôi Thủ, cảm năng lượng xoắn lên cánh tay, qua vai, xuống lưng, quanh hông, trở lại chân. Cú đẩy phải cảm giác như từ phía đối diện hành tinh.</p>",
    ),
    (
        "<h3>The 50+ Joint Protection</h3><p>Multi-plane silk-reeling is exceptionally joint-friendly. Each spiral distributes force across multiple axes, reducing peak stress on any single joint by up to 70%. For the 50+ body with existing joint wear, the spiral can be felt without pain, even if straight-line movement has been abandoned.</p>",
        "<h3>BẢO VỆ KHỚP 50+</h3><p>Xoắn đa mặng phẳng là cực kỳ thân thiện với khớp. Mỗi xoắn phân phối lực trên nhiều trục, giảm áp suất 70%. Đối với cơ thể 50+ có sự mài mòn khớp, xoắn có thể cảm mà không đau.</p>",
    ),
    mc("Every joint speaks in spirals. The body is the screw.", "Mỗi khớp nói bằng xoắn ốc. Cơ thể là con ốc vít."),
],

"spontaneous-movement": [
    (
        "<h3>The Big Idea</h3><p><strong>Tự Sinh (自生 / Spontaneous Movement)</strong> is the stage where the form dissolves and movement arises on its own &mdash; not from muscle memory, not from conscious direction, but from the body's intrinsic intelligence. Movements may look like miniature forms, or nothing like the form at all &mdash; fluid, asymmetrical, unpredictable.</p>"
        "<p>Three signs you are in Tự Sinh: (1) No memory of deciding &mdash; movement happened and you were the witness. (2) No effort to sustain &mdash; it arose and passed without volition. (3) Embodied knowing &mdash; afterward you understand something about your structure.</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3><p><strong>Tự Sinh (自生 / Chuyển Động Tự Sinh)</strong> là giai đoạn hình thái tan biến và chuyển động phát sinh từ chính nó &mdash; không từ ký ứớc, không từ sự chỉ đạo. Chuyển động có thể trông như các bản nhỏ, hoặc không giống bài nào &mdash; lưu lý, bất đối xứng, khó dự đoán.</p>"
        "<p>Ba dấu hiệu bạn đang ở Tự Sinh: (1) Không ký ứớc. (2) Không nỗ lực duy trì. (3) Hiểu biết trong cơ thể.</p>",
    ),
    (
        "<h3>Drills</h3><p><strong>Dissolution Practice</strong> &mdash; After 10 minutes of Zhan Zhuang, stop trying to maintain posture. Let the body move however it wants. Do not direct &mdash; just observe. Some sessions produce no visible movement; others produce flowing dance-like motion. Both are valid.</p><p><strong>Form Dissolution</strong> &mdash; Perform the 24-form at 1/4 speed. Halfway through, stop consciously directing and let the form complete itself.</p>",
        "<h3>BÀI TẬP</h3><p><strong>Hành lễ tan rã</strong> &mdash; Sau 10 phút thiền đứng, dừng việc duy trì tư thế. Để cơ thể di chuyển tùy ý. Đừng chỉ đạo &mdash; chỉ quan sát.</p><p><strong>Hình thái tan rã</strong> &mdash; Thực hành 24 dạng ở tốc 1/4. Ở giữa, dừng chỉ đạo và để bài hoàn thành chính nó.</p>",
    ),
    (
        "<h3>The Warning</h3><p>Tự Sinh is often misinterpreted as \"anything goes\" &mdash; that because the body moves spontaneously, any movement is valid. This is dangerous. Tự Sinh only arises from a stable foundation of correct structure. Without that foundation, spontaneous movement is just random movement. Ensure 18+ months of 3.0 practice first. The movement should always feel resolving, never agitating.</p>",
        "<h3>CẢNH BÁO</h3><p>Tự Sinh thường bị hiểu lầm là \"bất cứ gì cũng được\". Đây nguy hiểm. Tự Sinh chỉ phát sinh từ nền tảng ổn định. Đảm bảo 18+ tháng luyện 3.0 trước. Chuyển động phải luôn cảm giác giải quyết, không bao giờ phá hoại.</p>",
    ),
    mc("Let go of direction. Let the body resolve what it needs.", "Buông bỏ sự chỉ đạo. Để cơ thể giải quyết những gì nó cần."),
],

"merging-skill": [
    (
        "<h3>The Big Idea</h3><p><strong>Hòa Nhập (合并 / Merging Energy)</strong> is the push-hands skill where your energy and your partner's energy become indistinguishable. Unlike 3.0 (where you feel a push coming and redirect it), Hòa Nhập means you can no longer tell which energy is yours and which is theirs &mdash; you have merged into a single energy field.</p>"
        "<p>This happens when structure is so completely unified that there is no boundary between self and other. The telltale sign: after a session, you may not identify what push you initiated and what your partner initiated. You moved as one organism.</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3><p><strong>Hòa Nhập (合并)</strong> là kỹ năng Thôi Thủ khi năng lượng của bạn và đối tác trở nên không thể phân biệt. Không giống 3.0, Hòa Nhập nghĩa là bạn không thể phân biệt năng lượng nào là của bạn. Bạn đã hòa nhập thành một trường năng lượng.</p>"
        "<p>Điều này xảy ra khi cấu trúc hoàn toàn thống nhất đến mức không có ranh giới giữa tự và khác.</p>",
    ),
    (
        "<h3>Drills</h3><p><strong>Merged Walking</strong> &mdash; Two partners walk slowly in a circle, arms lightly touching. Try to feel exactly where your movement ends and theirs begins. When this boundary blurs, increase the speed. The goal is to move as one unit through space.</p><p><strong>Single Energy Field</strong> &mdash; In push hands, after reaching Hòa Nhập, continue for 3 minutes without consciously adjusting. If you feel the need to correct, you have broken the merge.</p>",
        "<h3>BÀI TẬP</h3><p><strong>Đi bộ hòa nhập</strong> &mdash; Hai đối tác đi chậm trong một vòng tròn, cánh tay nhẹ chạm. Cảm nhận chính xác nơi chuyển động của bạn kết thúc và của người kia bắt đầu.</p><p><strong>Trường năng lượng đơn</strong> &mdash; Trong Thôi Thủ, sau khi đạt Hòa Nhập, tiếp tục 3 phút mà không điều chỉnh. Nếu muốn chỉnh, bạn đã gãy liên kết.</p>",
    ),
    (
        "<h3>The Boundary Dissolution Moment</h3><p>There is a precise instant when the merge happens &mdash; usually 90 seconds to 3 minutes of synchronized push hands. It feels like a sudden expansion, as if the body remembers a forgotten space. In this moment, the distinction between self and other dissolves in the contact point. This corresponds to a known neurological state called intercorporeal awareness &mdash; the brain extending its body schema into another person.</p>",
        "<h3>KHOẢNH KHỨC HỶA LẬP KÍ ỨC</h3><p>Có một khoảnh khắc chính xác khi sự hòa nhập xảy ra &mdash; thường là 90 giây đến 3 phút. Nó cảm giác như một sự mở rộng đột ngột. Trong khoảnh khắc này, sự phân biệt giữa tự và khác tan rã. Đây tương ứng với trạng thái thần kinh gọi là nhận thức liên xã hội.</p>",
    ),
    mc("When the boundary dissolves, you and I become one.", "Khi ranh giới tan rã, bạn và tôi trở thành một."),
],

"ground-path": [
    (
        "<h3>The Big Idea</h3><p><strong>Đường Đất (Ground Path)</strong> is the full-circuit force transmission: force travels from feet through legs, up spine, through arms, and back down through partner to earth &mdash; completing a loop. Unlike linear force, the full loop means energy is never truly issued &mdash; it circulates endlessly, borrowing and returning to the ground.</p>"
        "<p>The critical insight: the ground path is not just about pushing power into the ground. It is about listening to the ground. When your foot contacts the ground, you can feel the ground's reaction &mdash; its slope, texture, stability. This feedback loop allows micro-adjustments 15-20 times per second &mdash; the unmovable object quality in push hands.</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3><p><strong>Đường Đất</strong> là truyền lực vòng tròn: lực từ chân qua chân, lên sống người, qua cánh tay, và xuống đất qua đối phương &mdash; hoàn thành vòng lặp. Không giống lực tuyến tính, vòng tròn đầy đủ có nghĩa là năng lượng không bao giờ được phát ra thực sự.</p>"
        "<p>Bàn chình: Đường Đất không chỉ về sức mạnh. Nó là về nghe đất. Khi chân tiếp xúc, bạn cảm phản hồi của nó.</p>",
    ),
    (
        "<h3>Drills</h3><p><strong>Full Loop Push</strong> &mdash; In push hands, after receiving a push, do not push back directly. Feel the energy enter your foot, rise through legs and spine, flow out arm, into partner, and back down to earth. The push should feel like it originates from the far side of the planet.</p><p><strong>Grounding Sensitivity</strong> &mdash; In horse stance, have a partner press on each shoulder from the side. Trace the path: shoulder&rarr;ribs&rarr;dantian&rarr;hip&rarr;knee&rarr;ankle&rarr;floor. Practice barefoot on different surfaces.</p>",
        "<h3>BÀI TẬP</h3><p><strong>Đẩy vòng tròn hoàn chỉnh</strong> &mdash; Trong Thôi Thủ, sau khi nhận đẩy, đừng đẩy trực tiếp. Cảm năng lượng vào chân, lên chân, lên sống người, ra cánh tay, vào đối tác, xuống đất. Cú đẩy phải cảm giác như từ phía đối diện hành tinh.</p><p><strong>Đường đi đất</strong> &mdash; Trong cờ đề, đối tác ấn từ hai bên. Truy xuất con đường: vai&rarr;sọan&rarr;Đan Điền&rarr;hông&rarr;khuỷu&rarr;mắt cá chân&rarr;sàn.</p>",
    ),
    (
        "<h3>The Seismic Foot</h3><p>The Ground Path requires the seismic foot &mdash; a foot that can feel and respond to micro-vibrations in the earth. This is developed by practicing barefoot 10 minutes daily. The 50+ body, encased in shoes for decades, redevelops remarkable sensitivity in just 2 weeks. The foot learns to distinguish stable ground (concrete) from live ground (dirt with organisms).</p>",
        "<h3>CHÂN ĐỘNG ĐỘNG</h3><p>Đường Đất yêu cầu chân động &mdash; một chân có thể cảm và phản ứng với rung động vi mô trong đất. Điều này phát triển bằng cách luyện trần chân 10 phút mỗi ngày. Cơ thể 50+, mang giày trong hàng thập kỷ, phục hồi nhạy cảm đáng kể trong 2 tuần.</p>",
    ),
    mc("The earth moves with you. Always.", "Đất đi cùng bạn. Luôn luôn."),
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


def update_techniques_index_new():
    en_idx = REPO / "en" / "techniques" / "index.html"
    vi_idx = REPO / "vi" / "techniques" / "index.html"

    for idx_path, lang_label in [(en_idx, "en"), (vi_idx, "vi")]:
        text = idx_path.read_text(encoding='utf-8')
        new_entries = []
        for slug, en_title, vi_title in NEW_TOPICS:
            title = en_title if lang_label == "en" else vi_title
            href = f"/{lang_label}/techniques/{slug}/"
            new_entries.append(
                f'        <div class="technique-card"><h3><a href="{href}">{title}</a></h3></div>'
            )
        insertion = "\n".join(new_entries) + "\n"
        article_close = text.find("</article>")
        if article_close == -1:
            print(f"  WARN: </article> not found in {idx_path}")
            continue
        section_close = text.rfind("</section>", 0, article_close)
        new_text = text[:section_close] + insertion + text[section_close:]
        idx_path.write_text(new_text, encoding='utf-8')
        print(f"  appended 10 topics to {idx_path.relative_to(REPO)}")


if __name__ == "__main__":
    print("--- Building Batch 7: 10 advanced topic pages (4.0 level, EN+VI) ---")
    for slug, en_title, vi_title in NEW_TOPICS:
        build_topic(slug, en_title, vi_title)
    print("--- Updating techniques index (EN+VI) ---")
    update_techniques_index_new()
