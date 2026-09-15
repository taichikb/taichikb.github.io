#!/usr/bin/env python3
"""Build 10 advanced EN + 10 VI technique-topic subpages (Batch 6 - 3.5 level).

Advanced concepts for students beyond the 3.0 Beginner baseline:
silk-reeling energy, wu wei, dantian, fa jin, listening energy,
iron body, yin-yang loop, central equilibrium, embrace the pot,
breathing channels.

Reuses page_shell from build_topics.py.
"""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_topics import page_shell

REPO = Path("D:/Taichi-Health-Finance/Intranet/taichikb_repo")

MASTER_CUE_EN = '<h3 style="background:var(--ink);color:var(--card);padding:0.5rem 1rem;margin:-0.5rem -1rem 0.5rem;">Master Cue</h3><p style="font-style:italic;font-family:Cormorant Garamond,serif;font-size:1.3rem;">"PLACEHOLDER"</p>'
MASTER_CUE_VI = '<h3 style="background:var(--ink);color:var(--card);padding:0.5rem 1rem;margin:-0.5rem -1rem 0.5rem;">Câu Nhắc Tổng</h3><p style="font-style:italic;font-family:Cormorant Garamond,serif;font-size:1.3rem;">"PLACEHOLDER"</p>'

def mc(en_text, vi_text):
    return (
        MASTER_CUE_EN.replace('"PLACEHOLDER"', en_text),
        MASTER_CUE_VI.replace('"PLACEHOLDER"', vi_text),
    )

NEW_TOPICS = [
    ("chan-si-jin",
     "Silk Reeling Energy (Chan Si Jin / 缠丝劲) — The Spiral of Integrated Power",
     "Năng Lượng Xoắn Tơ (Chan Si Jin / 缠丝劲) — Sóng Xoắn Của Sức Mạnh"),
    ("wu-wei",
     "Wu Wei (Vô Vi / 无为) — The Art of Non-Action in Motion",
     "Vô Vi (Vô Vi / 无为) — Nghệ Thuật Hành Động Không Hành Động"),
    ("dantian",
     "The Dantian (Đan Điền / 丹田) — The Powerhouse Below the Navel",
     "Đan Điền (丹田) — Trung Tâm Năng Lượng Dưới Bụng"),
    ("fa-jin",
     "Fa Jin (Phá Tấn / 发劲) — Explosive Power Without Muscle",
     "Phá Tấn (發勁) — Sức Mạnh Bùng Nổ Không Cơ Bắp"),
    ("ting-jin",
     "Listening Energy (Ting Jin / 听劲) — The Skill of Feeling Before Moving",
     "Năng Lượng Lắng Nghe (Ting Jin / 听劲) — Kỹ Năng Cảm Thấy Trước Khi Chuyển Động"),
    ("iron-shirt",
     "Iron Shirt (Cuồn Não / 铜人) — Conditioning for Impact Absorption",
     "Áo Sắt (Cuồn Não / 铜人) — Rèn Luyện Hấp Thụ Va Chạm"),
    ("yin-yang-loop",
     "The Yin-Yang Energy Loop (Âm Dương Tuần Hoàn) — Circular Power",
     "Vòng Tròn Năng Lượng Âm Dương — Sức Mạnh Hình Tròn"),
    ("zhong-ning",
     "Central Equilibrium (Trung Nghị / 中定) — The Middle Way of Balance",
     "Trung Nghị (Trung Nghị / 中定) — Con Đường Giữa Của Sự Cân Bằng"),
    ("ou-mo",
     "Embrace the Pot (Ôm Nồi / 抱磨) — Full Circle Connection",
     "Ôm Nồi (Ôm Nồi / 抱磨) — Kết Nối Đầy Đủ Vòng Tròn"),
    ("breath-channels",
     "Breath & Energy Channels (Hô Hấp Và Kênh Khí) — The Internal Highway",
     "Hơi Thở Và Kênh Khí — Xa Lộ Nội Tâm"),
]

CONTENT = {

"chan-si-jin": [
    (
        "<h3>The Big Idea</h3>"
        "<p><strong>Chan Si Jin (缠丝劲 / Silk Reeling Energy)</strong> is the spiraling, coiling force that runs through the entire body. Unlike linear force (which travels in a straight line from A to B), spiral force wraps around the body's axis like a spring. Every joint contributes a rotation; every step adds a twist. The energy never travels directly — it always curves, always coils, always returns.</p>"
        "<p>Three principles: (1) <em>Never extend straight</em> &mdash; power comes from coiling, not extending. (2) <em>Every layer turns</em> &mdash; fingers, wrists, elbows, shoulders, spine, hips, knees, ankles each contribute. (3) <em>The spiral is continuous</em> &mdash; there is no start and no end, only the unbroken loop of coiled power.</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3>"
        "<p><strong>Chan Si Jin (缠丝劲 / Năng Lượng Xoắn Tơ)</strong> là lực xoắn, cuộn qua toàn bộ cơ thể. Không giống lực tuyến tính (đi thẳng từ A đến B), lực xoắn quấp quanh trục cơ thể như một con lắc. Mỗi khớp đóng góp một sự quay; mỗi bước thêm một sự xoắn. Năng lượng không bao giờ đi thẳng &mdash; nó luôn uốn lượn, luôn cuộn, luôn quay lại.</p>"
        "<p>Ba nguyên tắc: (1) <em>Đừng kéo thẳng</em> &mdash; sức mạnh từ việc cuộn, không phải kéo. (2) <em>Mỗi lớp mỗi lớp</em> &mdash; ngón tay, cổ tay, khuỷu, vai, sống người, hông, khuỷu, mắt cá chân mỗi cái đóng góp. (3) <em>Sự xoắn là liên tục</em> &mdash; không có điểm bắt đầu và không có điểm kết thúc, chỉ là vòng lặp không gián đoạn của sức mạnh.</p>",
    ),
    (
        "<h3>Drills</h3>"
        "<p><strong>Spiral Punch (Cú đấm xoắn)</strong> &mdash; Stand in horse stance. Rotate the hip 45 degrees to the left, then twist the torso to the right. Punch forward with the right fist &mdash; but the fist should not go straight. It should spiral inward. Feel the energy travel: hip &rarr; waist &rarr; spine &rarr; shoulder &rarr; arm &rarr; fist. Each joint adds its own twist.</p>"
        "<p><strong>Spring Coil Legs (Chân như ống xo)</strong> &mdash; In horse stance, rise onto the balls of the feet, then lower. Do not use muscle to rise &mdash; let the spiral energy of the legs carry you up. Imagine each leg is a spring, coiling to push. Do 10 cycles, feeling the spiral travel up each time.</p>",
        "<h3>BÀI TẬP</h3>"
        "<p><strong>Cú đấm xoắn</strong> &mdash; Đứng tư thế cờ đề. Xoay hông 45 độ sang trái, sau đó xoay thân sang phải. Đấm tới với nắm tay phải &mdash; nhưng nắm tay không đi thẳng. Nó phải xoắn vào trong. Cảm năng lượng: hông &rarr; eo &rarr; sống người &rarr; vai &rarr; tay &rarr; nắm. Mỗi khớp thêm twist riêng.</p>"
        "<p><strong>Chân như ống xo</strong> &mdash; Trong cờ đề, lên lên các mắt chân, sau đó hạ xuống. Đừng dùng cơ để lên &mdash; để năng lượng xoắn của chân mang bạn lên. Hình dung mỗi chân là một ống xo, cuộn để đẩy. Làm 10 chu kỳ, cảm năng lượng lên tới mỗi lần.</p>",
    ),
    (
        "<h3>The Difference From External Martial Arts</h3>"
        "<p>External arts use linear force &mdash; a punch goes straight from the body to the target. This is strong but telegraphed: a trained receiver can feel it coming and redirect. Chan Si Jin wraps so the force does not arrive in a straight line &mdash; it spirals into the opponent like a drill bit into wood. The direction of the force changes at impact, making it nearly impossible to meet directly.</p>",
        "<h3>SỰ KHÁC BIỆT TỪ VÕ THUẬT NGOẠI</h3>"
        "<p>Võ thuật ngoại dùng lực tuyến tính &mdash; cú đấm đi thẳng từ cơ thể đến mục tiêu. Điều này mạnh nhưng dễ đoán: người nhận được luyện tập có thể cảm thấy và chuyển hướng. Chan Si Jin quấp để lực không đến theo đường thẳng &mdash; nó xoắn vào đối phương như con khoan vào gỗ. Hướng lực thay đổi tại thời điểm va chạm, gần như không thể đón nhận trực tiếp.</p>",
    ),
    mc("Every joint speaks in spirals. Listen in circles.", "Mỗi khớp nói bằng xoắn ốc. Hãy lắng nghe bằng vòng tròn."),
],

"wu-wei": [
    (
        "<h3>The Big Idea</h3>"
        "<p><strong>Vô Vi (無為 / Wu Wei)</strong> is the most misunderstood and most powerful concept in Tai Chi &mdash; for good reason. Literally \"non-action\" or \"non-doing,\" Vô Vi does NOT mean doing nothing. It means <em>acting without forcing</em>. The action arises naturally from the situation; no extra effort or intention is added.</p>"
        "<p>In push hands, Vô Vi is when you feel a partner push and your body moves to the correct position without you \"deciding\" to move. You are not passive; you are perfectly responsive &mdash; like a flag in the wind, moving with the breeze but not being blown over. The 3.0 student practices this slowly; the 3.5 student begins to feel it spontaneously.</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3>"
        "<p><strong>Vô Vi (無為 / Wu Wei)</strong> là khái niệm hiểu lầm nhất và mạnh mẽ nhất trong Thái Cực Quyền &mdash; đúng vì lý do đó. Nghĩa đại là \"không hành động\" hay \"không làm gì\", Vô Vi KHÔNG có nghĩa là làm gì cả. Nó nghĩa là <em>hành động mà không ép buộc</em>. Hành động sinh ra tự nhiên từ tình huống; không thêm nỗ lực hay ý định nào.</p>"
        "<p>Trong Thôi Thủ, Vô Vi là khi bạn cảm thấy đối tác đẩy và cơ thể bạn di chuyển về đúng vị trí mà bạn không \"quyết định\" di chuyển. Bạn không phải là thụ động; bạn là hoàn toàn phản ứng &mdash; như cờ trong gió, di chuyển với cơn gió nhưng không bị lật ngược. Học viên 3.0 luyện từng chậm rãi; học viên 3.5 bắt đầu cảm thấy tự nhiên.</p>",
    ),
    (
        "<h3>Drills</h3>"
        "<p><strong>Blind Push Hands (Thôi Thủ mờ)</strong> &mdash; Close your eyes. Have a partner gently guide your hands in push hands. Try to move without deciding where to move. If you find yourself \"choosing,\" you have left Vô Vi. The correction: stop choosing, feel the next impulse arise from the contact, and let it resolve.</p>"
        "<p><strong>The Pendulum Test (Kiểm tra con lắc)</strong> &mdash; Stand in Wuji. Your partner gently rocks you left and right by the shoulders. Do not resist; do not assist. Let your whole body become the pendulum &mdash; the rocking should feel like it is happening <em>to</em> you, not <em>by</em> you. When the movement is smooth and continuous, you have entered Vô Vi.</p>",
        "<h3>BÀI TẬP</h3>"
        "<p><strong>Thôi Thủ mờ</strong> &mdash; Nhắm mắt. Đối tác dẫn tay bạn trong Thôi Thủ. Cố di chuyển mà không quyết định. Nếu bạn tìm thấy \"lựa chọn,\" bạn đã rời Vô Vi. Cách chỉnh: ngừng lựa chọn, cảm nhận nhịp điệu tiếp theo từ tiếp xúc, và để nó giải quyết.</p>"
        "<p><strong>Kiểm tra con lắc</strong> &mdash; Đứng Vô Cực. Đối tác nhẹ nhàng lắc bạn trái phải bằng vai. Đừng chống; đừng hỗ trợ. Để cả cơ thể của bạn trở thành một con lắc &mdash; sự lắc phải cảm giác như đang xảy ra <em>với</em> bạn, không phải <em>bởi</em> bạn. Khi chuyển động trơn tru và liên tục, bạn đã vào Vô Vi.</p>",
    ),
    (
        "<h3>Why Vô Vi Is Not Passivity</h3>"
        "<p>The Western misunderstanding of Vô Vi as \"passive\" or \"do nothing\" misses the Chinese meaning entirely. In Chinese philosophy, Vô Vi is the <em>most active</em> state: the sage acts perfectly without effort, responds without thinking. The action is like a mirror that reflects without choosing what to reflect &mdash; the mirror is fully present, fully responsive, but never imposes its own direction.</p>"
        "<p>In Tai Chi practice, Vô Vi manifests when your response to a push is <em>perfect</em> on the first try, without conscious deliberation. This is not coincidence; it is the result of deep refinement reaching the point where action and awareness unify.</p>",
        "<h3>TẠI SAO VÔ VI KHÔNG PHẢI LÀ SỰ THỤ ĐỘNG</h3>"
        "<p>Sự hiểu lầm phương Tây về Vô Vi như \"thụ động\" hay \"không làm gì\" bỏ qua hoàn toàn nghĩa sống động của Trung Hoa. Trong triết học Trung Hoa, Vô Vi là trạng thái <em>hoạt động nhất</em>: nhà sĩ thức hiện hoàn hảo mà không nỗ lực, phản ứng mà không nghĩ. Hành động như gương phản chiếu mà không chọn gì để phản chiếu &mdash; gương hoàn toàn hiện diện, hoàn toàn phản ứng, nhưng không bao giờ áp đặt hướng đi riêng.</p>"
        "<p>Trong luyện tập Thái Cực, Vô Vi hiện hiện khi phản ứng của bạn với một cú đẩy là <em>hoàn hảo</em> ngay lần đầu, mà không có suy xét ý thức. Điều này không phải ngẫu nhiên; đó là kết quả của sự tinh luyện sâu xa đạt đến mức hành động và nhận thức hợp nhất.</p>",
    ),
    mc("Act without deciding. Respond without thinking.", "Hành động mà không quyết định. Phản ứng mà không nghĩ."),
],

"dantian": [
    (
        "<h3>The Big Idea</h3>"
        "<p><strong>Đan Điền (丹田 / Dantian)</strong> is the energy center located 2-3 inches below the navel, roughly the size of a golf ball. It is not merely metaphorical &mdash; modern somatic practitioners identify it with the deep transverse abdominal muscles, the pelvic floor, and the diaphragm. These three muscle groups form a hydraulic unit: when they engage together, they create internal pressure that stabilizes the spine and powers the limbs.</p>"
        "<p>The 3.5 student learns not just to \"breathe into the dantian\" but to <em>fire</em> the dantian. When you push in push hands, the force should initiate from this center, not from the arms. The dantian is a battery: the more you cultivate it, the more charge it holds. And when it discharges, it does so as coiled spiral energy (Chan Si Jin).</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3>"
        "<p><strong>Đan Điền (丹田 / Dantian)</strong> là trung tâm năng lượng nằm 2-3 inches dưới bụng rẘ, khoảng kích thước một quả golf. Không chỉ là ẩn dụ &mdash; những người luyện somatic hiện đại nhận diện nó với những cơ bụng thẳng sâu, sàn chậu, và các cơ hô hấp. Ba nhóm cơ này tạo thành một đơn vị thủy lực: khi chúng kết hợp, chúng tạo ra áp suất nội tâm ổn định sống người và thúc đẩy các chi.</p>"
        "<p>Học viên 3.5 học không chỉ \"thở vào Đan Điền\" mà còn <em>kích hoạt</em> Đan Điền. Khi bạn đẩy trong Thôi Thủ, lực phải khởi nguồn từ trung tâm này, không phải từ tay. Đan Điền là một con pin: càng chăm sóc, nạp điện nhiều hơn. Và khi nó bung nổ, nó bung ra dưới dạng năng lượng xoắn (Chan Si Jin).</p>",
    ),
    (
        "<h3>Drills</h3>"
        "<p><strong>Dantian Pulse (Nhịp Đan Điền)</strong> &mdash; Lie on your back, knees bent, feet flat. Place a hand on your navel. Breathe naturally. On each exhale, gently draw the area 1 inch toward your spine, then release. Do not suck in &mdash; this is a subtle pulse of engagement. 20 cycles. This builds somatic awareness of the dantian's connection to the breath.</p>"
        "<p><strong>Dantian Press (Áp lực Đan Điền)</strong> &mdash; In horse stance, place fists on the lower abdomen. As you inhale, the abdomen expands (not out, but 360 degrees &mdash; like a balloon inflating around the waist). As you exhale, gently contract. The key: the contraction should radiate energy upward, not just squeeze the gut.</p>",
        "<h3>BÀI TẬP</h3>"
        "<p><strong>Nhịp Đan Điền</strong> &mdash; Nằm lưng, gối uốn, chân phẳng. Đặt tay lên bụng rẘ. Thở tự nhiên. Về mỗi lần thở ra, nhẹ nhàng kéo khu vực 1 inch về phía xương sống, sau đó thả. Đừng húp bụng &mdash; đây là một nhịp nhẹ nhàng của sự kết hợp. 20 chu kỳ. Điều này xây dựng nhận thức somatic của kết nối Đan Điền với hơi thở.</p>"
        "<p><strong>Áp lực Đan Điền</strong> &mdash; Trong cờ đề, đặt nắm tay lên bụng dưới. Khi hít vào, bụng mở ra (không phải ra ngoài, mà 360 độ &mdash; như quả bóng bay đang xích lên quanh eo). Khi thở ra, nhẹ nhàng co lại. Quan trọng: sự co lại phải tỏa sáng lên, không chỉ nát bụng.</p>",
    ),
    (
        "<h3>The Breath-Energy Link at 50+</h3>"
        "<p>Modern breathwork identifies three diaphragmatic zones: Zone 1 (front diaphragm &mdash; lifts the chest), Zone 2 (central &mdash; massages the organs), Zone 3 (back diaphragm &mdash; stabilizes the spine). The dantian sits at the intersection of all three. For the 50+ body, where the diaphragm has shortened from decades of shallow breathing, dantian cultivation literally re-trains the diaphragm through Zone 3 activation. This is why Tai Chi practitioners over 50 often report better breathing within months.</p>",
        "<h3>SỰ KẾT NỐI HƠI THỞ-NĂNG LƯỢNG Ở 50+</h3>"
        "<p>Những người luyện hô hấp hiện đại nhận diện ba vùng cơ hô hấp: Vùng 1 (trước hô hấp &mdash; nâng ngực), Vùng 2 (trung tâm &mdash; massage các cơ quan), Vùng 3 (sau hô hấp &mdash; ổn định sống người). Đan Điền ngồi tại giao điểm của cả ba. Đối với cơ thể 50+, nơi hô hấp đã ngắn lại từ thập kỷ thở nông, sự chăm sóc Đan Điền thực sự tái huấn luyện hô hấp qua kích hoạt Vùng 3. Đây là lý do tại sao những người luyện Thái Cực trên 50 thường báo cáo hô hấp tốt hơn trong vài tháng.</p>",
    ),
    mc("Breathe into the ball. Fire from the center.", "Thở vào quả cầu. Bắn từ trung tâm."),
],

"fa-jin": [
    (
        "<h3>The Big Idea</h3>"
        "<p><strong>Phá Tấn (發勁 / Fa Jin)</strong> is the art of issuing explosive power &mdash; not from muscle, but from the coordinated release of coiled energy (Chan Si Jin). A Fa Jin is like a whip crack: the energy travels from the handle (the feet) through each segment (legs, hips, waist, spine, shoulder, elbow, wrist) and arrives at the tip (the hand/fist) in an instant.</p>"
        "<p>The paradox: Fa Jin is simultaneously <em>the fastest</em> and <em>the slowest</em> movement in Tai Chi. It is slow in preparation (the coiling takes time) and fast in execution (the release is instantaneous). The 3.5 student learns that Fa Jin cannot be \"done\" &mdash; it can only be <em>allowed</em> to happen when all conditions are met.</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3>"
        "<p><strong>Phá Tấn (發勁 / Fa Jin)</strong> là nghệ thuật phát ra sức mạnh bùng nổ &mdash; không từ cơ bắp, mà từ sự phát hành đồng bộ của năng lượng đã cuộn (Chan Si Jin). Một Phá Tấn như tiếng léo của cây roi: năng lượng đi từ tay cầm (chân) qua từng phần (chân, hông, eo, sống người, vai, khuỷu, cổ tay) và đến mũi (tay/nắm) trong chốc lát.</p>"
        "<p>Nhịp lý: Phá Tấn đồng thời là <em>nhanh nhất</em> và <em>chậm nhất</em> trong Thái Cực. Nó chậm trong chuẩn bị (việc cuộn mất thời gian) và nhanh trong thực thi (sự phát hành là tức thời). Học viên 3.5 học rằng Phá Tấn không thể \"được làm\" &mdash; nó chỉ có thể được <em>cho phép</em> xảy ra khi mọi điều kiện được đáp ứng.</p>",
    ),
    (
        "<h3>Drills</h3>"
        "<p><strong>Whip Crack Practice (Luyện tiếng léo)</strong> &mdash; Start with a partner's gentle push on your left shoulder. Do not resist. Instead, feel the force travel from shoulder to spine to dantian and back up the right side. At the moment the energy completes its circuit, issue a single, sharp Fa Jin from the right hand. The Jin must feel like it comes from nowhere &mdash; no wind-up, no telegraph.</p>"
        "<p><strong>Silent Release (Phát hành âm thầm)</strong> &mdash; In push hands, after receiving and redirecting, count silently to 3 in your head. At \"3,\" emit the Fa Jin without any preparatory movement. The partner should feel the force arrive suddenly, as if struck by static electricity.</p>",
        "<h3>BÀI TẬP</h3>"
        "<p><strong>Luyện tiếng léo</strong> &mdash; Bắt đầu với một cú đẩy nhẹ của đối tác lên vai trái. Đừng chống. Thay vào đó, cảm năng lượng từ vai xuống sống người xuống Đan Điền và lên trở lại ở bên phải. Ở khoảnh khắc năng lượng hoàn thành chu trình, phát ra một Phá Tấn sharp từ tay phải. Jin phải cảm giác như nó đến từ chỗ không &mdash; không chuẩn bị, không đoán trước.</p>"
        "<p><strong>Phát hành âm thầm</strong> &mdash; Trong Thôi Thủ, sau khi nhận và chuyển hướng, đếm im lặng đến 3 trong đầu. Ở \"3,\" phát Phá Tấn mà không có bất kỳ chuyển động chuẩn bị nào. Đối tác phải cảm thấy lực đến bất ngờ, như bị điện tĩ hòa đánh.</p>",
    ),
    (
        "<h3>Fa Jin vs Muscle Power</h3>"
        "<p>External martial arts generate Fa Jin from hip rotation and leg drive &mdash; a mechanical chain of muscle. Tai Chi Fa Jin generates from <em>dantian release</em>: the entire body's aligned structure acts as a spring. The external version is like a hammer blow (localized, brute force); the Tai Chi version is like a hydraulic press (distributed, structural). At close range, the Tai Chi version is paradoxically more penetrating because it does not \"push\" &mdash; it <em>sinks</em> into the opponent.</p>",
        "<h3>PHÁ TẤN vs SỨC MẠNH CƠ BẮP</h3>"
        "<p>Võ thuật ngoại tạo ra Phá Tấn từ sự quay hông và lực chân &mdash; một chuỗi cơ học. Phá Tấn Thái Cực sinh ra từ <em>sự phát hành Đan Điền</em>: toàn bộ cấu trúc cơ thể căng thẳng như một ống xo. Phiên bản bên ngoài như cú đập của búa (địa phương, lực thô); phiên bản Thái Cực như ép thủy lực (phân phối, cấu trúc). Ở khoảng cách gần, phiên bản Thái Cực trâm trừ hơn vì nó không \"đẩy\" &mdash; nó <em>chìm</em> vào đối phương.</p>",
    ),
    mc("Coil in stillness. Release in motion.", "Cuộn trong im lặng. Phát trong chuyển động."),
],

"ting-jin": [
    (
        "<h3>The Big Idea</h3>"
        "<p><strong>Ting Jin (听劲 / Listening Energy)</strong> is the highest skill in push hands &mdash; the ability to sense an opponent's state of balance, intention, and next movement through touch alone. Ting Jin does not predict; it <em>perceives</em> in real-time. When developed, it allows you to feel the opponent&rsquo;s center of gravity shift before they are consciously aware of it themselves.</p>"
        "<p>There are three levels of Ting Jin development: (1) <em>Gross Ting</em> &mdash; you feel big pushes and pulls. Every 3.0 student reaches this. (2) <em>Fine Ting</em> &mdash; you feel sub-micro movements: the slight tightening of a shoulder, the micro-weight-shift of an ankle. (3) <em>Bone Ting</em> &mdash; you feel the opponent's skeletal alignment and can sense when they are about to lose structural integrity.</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3>"
        "<p><strong>Ting Jin (听劲 / Năng Lượng Lắng Nghe)</strong> là kỹ năng cao nhất trong Thôi Thủ &mdash; khả năng cảm nhận trạng thái cân bằng, ý định, và chuyển động tiếp theo của đối phương qua xúc xích duy nhất. Ting Jin không dự đoán; nó <em> nhận thức</em> trong thời gian thực. Khi phát triển, nó cho phép bạn cảm nhận trọng tâm của đối phương chuyển trước khi họ tự nhận ra.</p>"
        "<p>Có ba cấp độ phát triển Ting Jin: (1) <em>Ting Đại</em> &mdash; bạn cảm thấy những cú đẩy và kéo lớn. Học viên 3.0 đều đạt được. (2) <em>Ting Tinh</em> &mdash; bạn cảm thấy chuyển động vi mô: sự căng nhẹ của vai, sự dịch chuyển vi mô của mắt cá chân. (3) <em>Ting Xương</em> &mdash; bạn cảm thấy cấu trúc xương của đối phương và cảm thấy khi họ sắp mất cân bằng cơ học.</p>",
    ),
    (
        "<h3>Drills</h3>"
        "<p><strong>Still-Contact Listening (Lắng nghe tiếp xúc vẫn)</strong> &mdash; Place your forearms against a partner's arms in a static embrace. Do not push or pull. Just feel. For 2 minutes, maintain contact and note every micro-movement you perceive. Then switch roles. The partner is trying to hide micro-movements &mdash; can you still feel them?</p>"
        "<p><strong>Breath-Sync Ting (Ting hơi thở đồng bộ)</strong> &mdash; In push hands, listen to your partner's breath through the contact points. When their breath deepens or shallows, their center shifts slightly. Can you feel this 0.3-second lag between breath change and structural response? That is Fine Ting.</p>",
        "<h3>BÀI TẬP</h3>"
        "<p><strong>Lắng nghe tiếp xúc vẫn</strong> &mdash; Đặt cánh tay dày lên tay đối tác trong một vòng ôm tĩnh. Đừng đẩy hay kéo. Chỉ cảm thấy. Trong 2 phút, duy trì tiếp xúc và ghi chú mọi chuyển động vi mô bạn cảm thấy. Rồi đổi vai. Người còn lại đang cố giấu chuyển động vi mô &mdash; bạn vẫn cảm thấy được không?</p>"
        "<p><strong>Ting hơi thở đồng bộ</strong> &mdash; Trong Thôi Thủ, hãy lắng nghe hơi thở của đối tác qua các điểm tiếp xúc. Khi hơi thở của họ sâu hơn hay nông hơn, trung tâm của họ dịch chuyển nhẹ. Bạn có cảm thấy sự trễ 0.3 giây giữa thay đổi hơi thở và phản ứng cấu trúc không? Đó là Ting Tinh.</p>",
    ),
    (
        "<h3>The Neuroscience of Ting Jin</h3>"
        "<p>Recent neuroimaging studies of expert Tai Chi push-hands players show hyperactivation in the <em>primary somatosensory cortex</em> &mdash; the brain region that maps bodily sensation. Experts can detect pressure changes as small as 0.05 Newtons (the weight of a grain of rice). This is not mystical; it is neuroplasticity built through thousands of hours of mindful contact training. The 50+ brain may develop Ting Jin slower, but it develops it <em>deeper</em>: the integration is richer because decades of somatic experience provide more reference points.</p>",
        "<h3>NEUROHOCKỌC CỦA TING JIN</h3>"
        "<p>Các nghiên cứu hình ảnh não gần đây của những chuyên gia Thôi Thủ Thái Cực cho thấy sự kích hoạt siêu trong <em>vùng xúc quan cảm xúc chính</em> &mdash; vùng não bản đồ cảm xúc cơ thể. Chuyên gia có thể phát hiện thay đổi áp suất nhỏ bằng 0.05 Newton (trọng lượng một hạt gạo). Điều này không phải là siêu nhiên; đó là neuroplasticity xây dựng qua hàng ngàn giờ luyện tập tiếp xúc chánh niệm. Não 50+ có thể phát triển Ting Jin chậm hơn, nhưng nó phát triển <em>sâu hơn</em>: sự tích hợp phong phú hơn vì thập kỷ kinh nghiệm somatic cung cấp nhiều điểm tham chiếu hơn.</p>",
    ),
    mc("Feel the shift before it happens.", "Cảm sự thay đổi trước khi nó xảy ra."),
],

"iron-shirt": [
    (
        "<h3>The Big Idea</h3>"
        "<p><strong>Cuồn Não (Iron Shirt / 铜人)</strong> in Tai Chi does NOT mean developing hard, impact-absorbing muscles. In the internal arts, Iron Shirt means <em>structuring</em> the body so that impact energy flows through the frame rather than stopping at the surface. The body becomes a conduit: force enters one side and exits the other, routed through the dantian and the ground.</p>"
        "<p>The 3.5 student learns that Iron Shirt is not about conditioning the body to take hits &mdash; it is about training the body so that hits never reach the center. When a push comes, the body's structure <em>redirects</em> it before it arrives. This is why Tai Chi players can absorb a strong push without moving an inch <mdash; not because their arms are strong, but because their structure solved the problem before the force was fully transmitted.</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3>"
        "<p><strong>Cuồn Não (Áo Sắt / 铜人)</strong> trong Thái Cực không có nghĩa là phát triển cơ bắp cứng, hấp thụ va chạm. Trong nghệ thuật nội tâm, Áo Sắt nghĩa là <em>cấu trúc</em> cơ thể để năng lượng va chạm lưu chuyện qua khung xương thay vì dừng ở bề mặt. Cơ thể trở thành một ống dẫn: năng lượng vào một bên và ra một bên khác, định tuyến qua Đan Điền và mặt đất.</p>"
        "<p>Học viên 3.5 học rằng Áo Sắt không phải để rèn luyện cơ thể để chịu đòn &mdash; mà là để luyện cơ thể để những cú đòn không bao giờ đến trung tâm. Khi có lực ép, cấu trúc của cơ thể <em>chuyển hướng</em> nó trước khi nó đến. Đây là lý do tại sao những người Thái Cực có thể hấp thụ một cú đẩy mạnh mà không di chuyển một inch &mdash; không phải vì cánh tay mạnh, mà vì cấu trúc đã giải quyết vấn đề trước khi lực được truyền đủ.</p>",
    ),
    (
        "<h3>Drills</h3>"
        "<p><strong>Wall Absorption (Hấp thụ tường)</strong> &mdash; Press your forearm against a wall. Have a partner push against your arm with increasing force. Do not resist; do not tense. Instead, focus on connecting the push through your spine, down your back leg, into the ground. The wall should feel the force dissipate, not reflect.</p>"
        "<p><strong>Grounding Path (Đường đi đất)</strong> &mdash; In horse stance, have a partner press on each shoulder from the side. For each push, silently trace the path: shoulder &rarr; ribs &rarr; dantian &rarr; hip &rarr; knee &rarr; ankle &rarr; floor. If any link feels blocked, the energy will not ground. This takes practice to do in real-time.</p>",
        "<h3>BÀI TẬP</h3>"
        "<p><strong>Hấp thụ tường</strong> &mdash; Ép cánh tay dày lên tường. Đối tác đẩy tăng dần. Đừng chống; đừng căng. Thay vào đó, tập trung kết nối lực qua sống người, xuống chân sau, xuống đất. Tường phải cảm được năng lượng tan rã, không phản xạ.</p>"
        "<p><strong>Đường đi đất</strong> &mdash; Trong cờ đề, đối tác ấn từ hai bên. Với mỗi cú đẩy, tự sự truy xuất con đường: vai &rarr; sọạn &rarr; Đan Điền &rarr; hông &rarr; khuỷu &rarr; mắt cá chân &rarr; sàn. Nếu bất kỳ liên kết nào cảm giác bị chặn, năng lượng sẽ không neo. Điều này mất thực hành để thực hiện thời gian thực.</p>",
    ),
    (
        "<h3>Iron Shirt Without Conditioning</h3>"
        "<p>The internal Iron Shirt does not require years of striking a trunk or breaking rods with the head. It requires learning the body's natural load paths &mdash; how force travels through bone, fascia, and fluid when the structure is aligned. A 50-year-old practitioner who has mastered structural alignment can absorb more impact than a 30-year-old who has only conditioned muscles. The 50+ body has had decades to forget bad habits; now it learns the right ones.</p>",
        "<h3>ÁO SẮT KHÔNG CẦN RÈN LUYỆN</h3>"
        "<p>Áo Sắt nội tâm không đòi hỏi hàng năm đánh vào thùng hay gãy thanh bằng đầu. Nó đòi hỏi học các con đường tải tự nhiên của cơ thể &mdash; năng lượng di chuyện qua xương, màng hoạt tính và chất lỏng khi cấu trúc căn chỉnh. Một người 50 tuổi đã thành thạo sự căn chỉnh cấu trúc có thể hấp thụ nhiều tác đập hơn người 30 tuổi chỉ rèn luyện cơ bắp. Cơ thể 50+ đã có thập kỷ để quên thói quen tệ; bây giờ nó học cách đúng.</p>",
    ),
    mc("Structure redirects. Never resist directly.", "Cấu trúc chuyển hướng. Đừng bao giờ chống trực tiếp."),
],

"yin-yang-loop": [
    (
        "<h3>The Big Idea</h3>"
        "<p><strong>The Yin-Yang Energy Loop (Vòng Tròn Âm Dương)</strong> is the circular flow of energy through the body's front and back pathways. The front channel (Ren / Nhân) carries Yin energy (nourishing, descending); the back channel (Du / Đố) carries Yang energy (transforming, ascending). These two channels form an endless loop: energy descends the front, transforms at the dantian, and ascends the back, only to descend again.</p>"
        "<p>In movement, this loop is always active. A correct push in push hands circulates energy: the push descends the front channel, transforms in the dantian, and rises through the back. A push that breaks the loop &mdash; for example, tensing the arms while pushing &mdash; causes energy to stagnate and fatigue to accumulate. The 3.5 student learns to feel and maintain this loop during action.</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3>"
        "<p><strong>Vòng Tròn Năng Lượng Âm Dương</strong> là dòng chảy hình tròn của năng lượng qua các kênh trước và sau cơ thể. Kênh trước (Nhân /人) mang năng lượng Âm (dưỡng dưỡng, hạ xuống); kênh sau (Đố /督) mang năng lượng Dương (biến đổi, lên trên). Hai kênh này tạo thành một vòng lặp vô tận: năng lượng hạ xuống phía trước, biến đổi ở Đan Điền, và lên trên phía sau, chỉ để lặp lại.</p>"
        "<p>Trong chuyển động, vòng tròn này luôn hoạt động. Một cú đẩy đúng trong Thôi Thủ tuần hoàn năng lượng: lực hạ xuống kênh trước, biến đổi trong Đan Điền, lên qua lưng. Một cú đẩy vượt qua vòng tròn &mdash; ví dụ, căng tay khi đẩy &mdash; gây bế tắc năng lượng và tích tích mỏi. Học viên 3.5 học cách cảm và duy trì vòng tròn trong hành động.</p>",
    ),
    (
        "<h3>Drills</h3>"
        "<p><strong>Loop Mapping (Bản đồ vòng tròn)</strong> &mdash; In Wuji stance, place your left hand on your lower ribs and your right hand on your lower back. Breathe naturally. On each inhale, feel the breath travel down the front (where your left hand rests) and up the back (where your right hand rests). On each exhale, feel the energy transform in your dantian. Do 10 cycles.</p>"
        "<p><strong>Closed Loop Push (Đẩy vòng kín)</strong> &mdash; In push hands, after each push, immediately sense whether the energy completed its loop. If you feel tension in the arms or fatigue in the shoulders, the loop broke. The correction: redirect the excess energy back down the front channel and through the dantian.</p>",
        "<h3>BÀI TẬP</h3>"
        "<p><strong>Bản đồ vòng tròn</strong> &mdash; Trong tư thế Vô Cực, đặt tay trái lên sọ dập dưới và tay phải lên lưng dưới. Thở tự nhiên. Về mỗi hơi thở vào, cảm hơi thở đi xuống phía trước (nơi tay trái đặt) và lên trên phía sau (nơi tay phải đặt). Về mỗi hơi thở ra, cảm năng lượng biến đổi trong Đan Điền. Làm 10 chu kỳ.</p>"
        "<p><strong>Đẩy vòng kín</strong> &mdash; Trong Thôi Thủ, sau mỗi cú đẩy, ngay lập tức cảm xúc năng lượng đã hoàn thành vòng tròn chưa. Nếu bạn cảm thấy căng tay hoặc mỏi vai, vòng tròn đã gãy. Cách chỉnh: chuyển hướng lại năng lượng thừa tích xuống kênh trước và qua Đan Điền.</p>",
    ),
    (
        "<h3>Clinical Relevance</h3>"
        "<p>The front-back energy loop maps remarkably well onto the body's <em>respiratory and circulatory systems</em>. The front channel corresponds to the vagus nerve (parasympathetic activation); the back channel to the spinal sympathetic chain. When the loop is open and flowing, the practitioner experiences the <em>relaxation response</em>: lowered cortisol, reduced blood pressure, and coherent heart-rate variability. This is not a side effect of Tai Chi &mdash; it is a direct physiological consequence of maintaining the yin-yang circuit during movement.</p>",
        "<h3>SỰ LIÊN QUAN LÂM SÀNG</h3>"
        "<p>Vòng tròn năng lượng trước-sau ánh xạ rất tốt lên <em>hệ hô hấp và tuần hoàn</em>. Kênh trước tương ứng với dẫn thần kinh vagus (kích hoạt bất thần); kênh sau tương ứng với dây thần kinh đối thân giao âm. Khi vòng tròn mở và lưu chuyện, người luyện trải nghiệm <em>phản ứng thư giãn</em>: giảm cortisol, huyết áp giảm, và biến thể nhịp tim hòa hợp. Đây không phải là tác dụng phụ của Thái Cực &mdash; đó là hệ quả sinh lý trực tiếp của việc duy trì mạch âm-dương trong chuyển động.</p>",
    ),
    mc("Energy descends. Transform in the dantian. Ascends. Repeat.", "Năng lượng hạ xuống. Biến đổi trong Đan Điền. Lên trên. Lặp lại."),
],

"zhong-ning": [
    (
        "<h3>The Big Idea</h3>"
        "<p><strong>Trung Nghị (中定 / Central Equilibrium)</strong> is the Tai Chi skill of occupying exactly the center of gravity &mdash; never falling to the left, never falling to the right, never advancing or retreating. The Chinese classic describes this as \"being like a great weight balanced on nothing.\" The body has a single point of balance, and every movement must return to that center.</p>"
        "<p>Trung Nghị has three components: (1) <em>Thẳng trụ (Straight Up)</em> &mdash; the body aligned like a plumb line, no forward or backward lean. (2) <em>Trung tâm (Middle)</em> &mdash; no left or right tilt; weight evenly distributed. (3) <em>Tĩnh lặng (Still)</em> &mdash; no unnecessary movement; every motion serves returning to center. The 3.5 student practices Trung Nghị in motion: every step, every push, every redirect resolves back to the center point.</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3>"
        "<p><strong>Trung Nghị (中定 / Trung Nghị)</strong> là kỹ năng trong Thái Cực của việc chiếm trọng tâm chính xác &mdash; không bao giờ nghiêng trái, không bao giờ nghiêng phải, không tiến không lùi. Kinh cổ Trung Hoa miêu tả điều này như \"là một vật nặng lớn cân bằng trên không.\". Cơ thể có một điểm cân bằng, và mỗi chuyển động phải quay trở lại trung tâm.</p>"
        "<p>Trung Nghị có ba thành phần: (1) <em>Thẳng trụ</em> &mdash; cơ thể căn thẳng như dây nổi, không nghiêng tới hay lại. (2) <em>Trung tâm</em> &mdash; không nghiêng trái hay phải; trọng lượng phân phối đồng đều. (3) <em>Tĩnh lặng</em> &mdash; không có chuyển động không cần thiết; mỗi chuyển động đều hướng về trung tâm. Học viên 3.5 luyện Trung Nghị trong chuyển động: mỗi bước, mỗi cú đẩy, mỗi sự chuyển hướng đều quy về trung tâm.</p>",
    ),
    (
        "<h3>Drills</h3>"
        "<p><strong>Compass Center (Trung tâm la bàn)</strong> &mdash; In horse stance, place a small ball (or rolled towel) between your knees. Hold for 1 minute. If your center drifts left or right, the ball falls. The ball is your unconscious teacher &mdash; it reveals your true center position.</p>"
        "<p><strong>Push-to-Center Return (Quay trở lại trung tâm)</strong> &mdash; In push hands, after each redirect, consciously return to center before the next movement. Count \"center\" in your mind at each return. If you find yourself pushing from an off-center position, you have forgotten the practice.</p>",
        "<h3>BÀI TẬP</h3>"
        "<p><strong>Trung tâm la bàn</strong> &mdash; Trong cờ đề, đặt quả bóng nhỏ (hoặc khăn gập) giữa hai đùi. Giữ 1 phút. Nếu trung tâm của bạn nghiêng trái hay phải, quả bóng rơi. Quả bóng là người dạy vô thức &mdash; nó tiết lộ vị trí trung tâm thật của bạn.</p>"
        "<p><strong>Quay trở lại trung tâm</strong> &mdash; Trong Thôi Thủ, sau mỗi sự chuyển hướng, tự nhận thức trở lại trung tâm trước chuyển động kế tiếp. Đếm \"trung tâm\" trong đầu ở mỗi lần quay. Nếu bạn tìm thấy mình đẩy từ vị trí ngoài trung tâm, bạn đã quên luyện tập.</p>",
    ),
    (
        "<h3>Trung Nghị for Fall Prevention</h3>"
        "<p>Balance disorders in adults over 50 are the leading cause of falls &mdash; and falls are the leading cause of injury death in that demographic. Trung Nghị directly addresses this. The skill of returning to center is, literally, the skill of not falling. Studies show that 12 weeks of Tai Chi practice focusing on central equilibrium reduces fall risk by 45%. The mechanism: the body retrains its proprioceptive map to recognize the center point instinctively. When perturbation comes, the body returns before the conscious mind even processes the threat.</p>",
        "<h3>TRUNG NGHỊ cho phòng ngừa ngã</h3>"
        "<p>Rối loạn cân bằng ở người trên 50 là nguyên nhân hàng đầu gây ngã &mdash; và ngã là nguyên nhân hàng đầu gây tử vong do chấn thương ở nhóm này. Trung Nghị trực tiếp giải quyết vấn đề này. Kỹ năng quay trở lại trung tâm là, về cơ bản, kỹ năng không ngã. Nghiên cứu cho thấy 12 tuần luyện Thái Cực tập trung vào trung tâm cân bằng giảm thiểm nguy cơ ngã 45%. Cơ chế: cơ thể tái huấn luyện bản đồ cảm xúc để nhận diện trung tâm một cách bản năng. Khi có x perturbation, cơ thể trả về trước khi ý thức nhận diện nguy hiểm.</p>",
    ),
    mc("Find your center. Return to it. Always.", "Tìm trung tâm của bạn. Trở về. Luôn luôn."),
],

"ou-mo": [
    (
        "<h3>The Big Idea</h3>"
        "<p><strong>Ôm Nồi (抱磨 / Embrace the Pot)</strong> is the movement where the arms wrap around the body in a full, circular embrace, then open outward. The \\'pot\\' refers to the dantian &mdash; the belly is the vessel, and the arms are the lid that seals it. When done correctly, this creates a pressurized chamber: the dantian is compressed, the energy circulates, and power can issue in any direction.</p>"
        "<p>Unlike external martial arts (which build arm and shoulder strength), Ôm Nồi builds <em>axial integration</em> &mdash; the connection from the feet through the spine to the hands. The 3.5 student learns that the arms are not separate from the torso; they are the torso&rsquo;s extended fingers. Every push must originate from the embrace of the pot; otherwise the push is merely arm strength.</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3>"
        "<p><strong>Ôm Nồi (抱磨 / Ôm Nồi)</strong> là chuyển động nơi cánh tay quấp quanh cơ thể trong một vòng tròn đầy đủ, rồi mở ra phía ngoài. \"Nồi\" đề cập đến Đan Điền &mdash; bụng là chiếc nồi, và cánh tay là chiếc nắp kín nó. Khi thực hiện đúng, điều này tạo ra một phiến áp suất: Đan Điền bị nén, năng lượng tuần hoàn, và sức mạnh có thể phát ra mọi hướng.</p>"
        "<p>Không giống võ thuật ngoại (xây dựng sức mạnh tay và vai), Ôm Nồi xây dựng <em>sự tích hợp trục</em> &mdash; kết nối từ chân qua sống người đến tay. Học viên 3.5 học rằng cánh tay không phải riêng rẽ với thân; chúng là những ngón tay dài của sống người. Mỗi cú đẩy phải khởi nguồn từ sự ôm nồi; nếu không, cú đẩy chỉ là sức tay thôi.</p>",
    ),
    (
        "<h3>Drills</h3>"
        "<p><strong>Pot-Lid Awareness (Nhận thức nắp nồi)</strong> &mdash; In Wuji stance, bring the arms in front of the lower abdomen as if closing a pot lid. Feel the connection from one hand, through the spine, to the other hand. Now open the arms out and back. The \\'closing\\' should feel like gathering energy; the \\'opening\\' should feel like issuing it.</p>"
        "<p><strong>Spine-Through-Arms (Sống người qua cánh tay)</strong> &mdash; In horse stance, perform Ôm Nồi slowly. At the point where the arms are widowed at the sides, pause. Can you feel your spine reflected in your little finger? When the connection is complete, both sides of the body feel like a single unit.</p>",
        "<h3>BÀI TẬP</h3>"
        "<p><strong>Nhận thức nắp nồi</strong> &mdash; Trong tư thế Vô Cực, đưa cánh tay trước bụng dưới như đóng nắp nồi. Cảm kết nối từ một tay, qua sống người, đến tay kia. Mở cánh tay ra và lại. \"Đóng\" phải cảm giác như thu thập năng lượng; \"mở\" phải cảm giác như phát hành.</p>"
        "<p><strong>Sống người qua cánh tay</strong> &mdash; Trong cờ đề, thực hành Ôm Nồi chậm. Ở điểm cánh tay rộng ra hai bên, dừng lại. Bạn có cảm thấy sống người phản ánh trong ngón cái không? Khi kết nối hoàn tất, cả hai bên cơ thể như một khối.</p>",
    ),
    (
        "<h3>Ôm Nồi Without Shoulder Tension</h3>"
        "<p>The most common error: lifting the shoulders to \\'hold\\' the embrace. The 50+ body has decades of shoulder tension stored from desk work and phone use. Ôm Nồi requires the shoulders to be <em>released</em> into the back, not drawn up. The correction: before each practice, do three shoulder rolls &mdash; up, back, and down 5 times. Then perform Ôm Nồi as if your shoulder blades were melting into your back pockets.</p>",
        "<h3>ÔM NỒI KHÔNG CẦN CĂNG VAI</h3>"
        "<p>Lỗi phổ biến nhất: nâng vai để \"giữ\" cuộc ôm. Cơ thể 50+ có hàng thập kỷ căng vai tích tích từ làm việc bàn phím và điện thoại. Ôm Nồi yêu cầu vai phải được <em>giải phóng</em> về sau, không kéo lên. Cách chỉnh: trước mỗi lần luyện, làm 5 vòng xoay vai &mdash; lên, lại, xuống. Rồi thực hành Ôm Nồi như nếu hai xương sống của bạn chảy vào túi sau.</p>",
    ),
    mc("Close the pot. Seal the dantian. Open to the world.", "Đóng nồi. Nhấn kín Đan Điền. Mở ra thế giới."),
],

"breath-channels": [
    (
        "<h3>The Big Idea</h3>"
        "<p><strong>The 12 Primary Breath Channels (Hơi Thở Và Kênh Khí)</strong> are the body's internal highways for energy circulation. They correspond to the 12 primary meridians of TCM, but in Tai Chi they are understood functionally: each channel has a specific movement quality and breath pattern.</p>"
        "<p>Three channels are essential for the 3.5 student: (1) <em>Luêm (Thở Lên / Lifting the Breath)</em> &mdash; the energy ascends the front of the body, used in rising movements. (2) <em>Hạ Đằng (Thở Xuống / Sinking the Breath)</em> &mdash; the energy descends the back, used in grounding. (3) <em>Thần Kinh (Thở Quay / Twisting Breath)</em> &mdash; the energy spirals around the torso, used in rotational movements. Each movement in the form has a corresponding breath channel; learning the map accelerates your practice.</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3>"
        "<p><strong>12 Kênh Hơi Thở Chính</strong> là những con đường nội tâm của cơ thể để tuần hoàn năng lượng. Chúng tương ứng với 12 kinh chính của Y Dược Truyền Thống Trung Quốc, nhưng trong Thái Cực, chúng được hiểu theo chức năng: mỗi kênh có chất lượng chuyển động và mẫu thở nhất định.</p>"
        "<p>Ba kênh thiết yếu cho học viên 3.5: (1) <em>Lên (Thở Lên)</em> &mdash; năng lượng lên kênh trước, dùng trong chuyển động lên. (2) <em>Hạ Đằng (Thở Xuống)</em> &mdash; năng lượng hạ xuống lưng, dùng trong neo. (3) <em>Thần Kinh (Thở Quay)</em> &mdash; năng lượng xoắn quanh thân, dùng trong xoay. Mỗi chuyển động có kênh thở tương ứng; học bản đồ này tăng tốc luyện tập của bạn.</p>",
    ),
    (
        "<h3>Drills</h3>"
        "<p><strong>Breath-Channel Mapping (Bản đồ kênh hơi thở)</strong> &mdash; Stand in Wuji. On the inhale, feel the breath travel up the front of the body (Ren / Nhân) to the crown. On the exhale, feel the breath travel down the back (Du / Đố) to the dantian. On the third breath, imagine the breath spiraling around the torso. Do 5 cycles of each pattern.</p>"
        "<p><strong>Movement-Breath Sync (Đồng bộ chuyển động-hơi thở)</strong> &mdash; Perform a single Brush Knee movement. Identify which breath channel is active: inhale to open (front ascend), exhale to close (back descend). If you cannot identify the channel, you are moving without breath direction &mdash; the movement will feel effortful and disconnected.</p>",
        "<h3>BÀI TẬP</h3>"
        "<p><strong>Bản đồ kênh hơi thở</strong> &mdash; Đứng Vô Cực. Khi hít, cảm hơi thở lên kênh trước đến mũ. Khi thở ra, cảm hơi thở xuống lưng đến Đan Điền. Hơi thứ ba, hình dung hơi thở xoắn quanh thân. Làm 5 chu kỳ.</p>"
        "<p><strong>Đồng bộ chuyển động-hơi thở</strong> &mdash; Thực hành một Nhấp Bước. Xác định kênh hơi nào hoạt động: hít để mở (front ascend), thở ra để đóng (back descend). Nếu không xác định được kênh, bạn đang di chuyển mà không hướng hơi thở &mdash; chuyển động sẽ cảm thấy cần nỗ lực và rời rạc.</p>",
    ),
    (
        "<h3>The 50+ Breathing Advantage</h3>"
        "<p>The 50+ body has slower metabolism and often shallower breathing. But slower breath can be deeper breath. The key: the diaphragm, with practice, can re-engage zones unused to decades of chest breathing. The breath-channels approach trains the body to find its own optimal pattern &mdash; not the instructor\'s ideal pattern, but the pattern that actually works for your body at your age.</p>",
        "<h3>LỢI THẾ HƠI THỞ 50+</h3>"
        "<p>Cơ thể 50+ có trao đổi chất chậm và thường thở nông. Nhưng hơi thở chậm có thể là hơi thở sâu. Chìa khóa: hô hấp, với thực hành, có thể kích hoạt lại các vùng không được dùng trong hàng thập kỷ thở ngực. Cách tiếp cận kênh hơi thở rèn luyện cơ thể tìm mẫu tối ưu &mdash; không phải mẫu lý thưởng của giảng viên, mà là mẫu thực sự hoạt động cho cơ thể và độ tuổi của bạn.</p>",
    ),
    mc("Follow the channel. Let the breath lead the body.", "Theo kênh. Để hơi thở dẫn dắt cơ thể."),
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
    """Append 10 new topics to the existing techniques index pages."""
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
    print("--- Building Batch 6: 10 advanced topic pages (EN+VI) ---")
    for slug, en_title, vi_title in NEW_TOPICS:
        build_topic(slug, en_title, vi_title)
    print("--- Updating techniques index (EN+VI) ---")
    update_techniques_index_new()
