#!/usr/bin/env python3
"""Build 10 more EN + 10 VI technique-topic subpages (Batch 5).

Extends the 3.0 Beginner curriculum with: free-hand push hands, brush knee,
twist step, rowing chariot, lifting the paten, flowing steps, eight-direction
opening, grasp sparrow's tail summary, guardian posture, and counter-step.

Follows the same pattern as build_topics.py — reuses page_shell and
update_techniques_index by importing from that module.
"""
from pathlib import Path
import sys

# Reuse the page_shell function from build_topics.py
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_topics import page_shell  # noqa: E402

REPO = Path("D:/Taichi-Health-Finance/Intranet/taichikb_repo")

MASTER_CUE_EN = '<h3 style="background:var(--ink);color:var(--card);padding:0.5rem 1rem;margin:-0.5rem -1rem 0.5rem;">Master Cue</h3><p style="font-style:italic;font-family:Cormorant Garamond,serif;font-size:1.3rem;">"PLACEHOLDER"</p>'
MASTER_CUE_VI = '<h3 style="background:var(--ink);color:var(--card);padding:0.5rem 1rem;margin:-0.5rem -1rem 0.5rem;">Câu Nhắc Tổng</h3><p style="font-style:italic;font-family:Cormorant Garamond,serif;font-size:1.3rem;">"PLACEHOLDER"</p>'

def mc(en_text, vi_text):
    """Create a master cue card pair from a one-line cue in each language."""
    return (
        MASTER_CUE_EN.replace('"PLACEHOLDER"', en_text),
        MASTER_CUE_VI.replace('"PLACEHOLDER"', vi_text),
    )

# 10 new entries (batch 5)
NEW_TOPICS = [
    ("san-shou",
     "San Shou (Free-Hand Push Hands) — Contact Without Armor",
     "San Shou — Thôi Thủ Không Giáp"),
    ("dien",
     "Brush Knee (Diân / 剪) — The Universal Adjustment",
     "Chỉ Lông / Nhấp Bước (Diên / 剪) — Điều Chỉnh Vạn Dụng"),
    ("xie-bu",
     "Twist Step (Quay / 轉) — Redirecting Power Through the Waist",
     "Bước Xoay (Quay / 轉) — Chuyển Lực Qua Eo"),
    ("kai-gong",
     "Rowing the Chariot (Khai Gôn / 开功) — The First Real Alignment",
     "Kéo Xe (Khai Gôn / 开功) — Sự Thăng Bằng Đầu Tiên"),
    ("tu-hu",
     "Lifting the Paten (Tô Hô) — Supporting the Unsupported",
     "Nâng Nhiễn (Tô Hô) — Đỡ Lấy Những Gì Không Được Nâng"),
    ("hoa-buoc",
     "Flowing Steps (Hoa Bước / 化步) — Neutral, Not Passive",
     "Bước Hóa (Hoa Bước / 化步) — Trung Lập, Không Phải Thụ Động"),
    ("ba-hoi",
     "Opening Eight Directions (Bát Hướng) — Structure Before Reach",
     "Mở Bát Hướng (Bát Hướng) — Cấu Trúc Trước Sự Vươn Lên"),
    ("thieu-hai",
     "Grasp Sparrow's Tail Summary — The Four Gates at a Glance",
     "Tóm Tắt Lãm Tước Vỹ — Bốn Cửa Tại Một Nhìn"),
    ("shou-ba",
     "Guardian Posture (Thủ Bát Bảo) — Protecting Your Center",
     "Tư Thế Thủ Bát Bảo — Bảo Vệ Trung Tâm Của Bạn"),
    ("nghich-buoc",
     "Counter-Step (Nghịch Bước / 逆步) — Adhere, Stick, and Yield",
     "Bước Ngược (Nghịch Bước / 逆步) — Dính, Dính, Nhường"),
]

# Body content: list of (en_card_html, vi_card_html) per topic
CONTENT = {

"san-shou": [
    (
        "<h3>The Big Idea</h3>"
        "<p><strong>San Shou (Tự Thủ)</strong> &mdash; free-hand push hands &mdash; is the first place you test your structure outside of a mirror. One partner offers a light push; the other receives and returns. Unlike external push hands (where people trade force), San Shou operates on <em>neutral meeting</em>: the contact point does not lock; it adheres, sticks, and connects.</p>"
        "<p>The goal is not to win a shove. The goal is to feel the opponent's center &mdash; their balance, intention, next micro-movement &mdash; before they commit. This is why San Shou is called \"listening hands.\"</p>",
        "<h3>Ý Tưởng CỐT LÕI</h3>"
        "<p><strong>San Shou (Tự Thủ)</strong> &mdash; Thôi Thủ không giáp &mdash; là nơi bạn thử cấu trúc ngoài gương. Một đối tác đẩy nhẹ; người kia tiếp nhận và trả lại. Không giống Thôi Thủ ngoại, San Shou hoạt động theo <em>gặp gỡ trung lương</em>: điểm tiếp xúc không khóa; nó dính, dính, nối kết.</p>"
        "<p>Mục tiêu không phải thắng cú nặn. Mục tiêu là cảm thấy trung tâm của đối phương &mdash; sự cân bằng, ý định, chuyển động vi mô &mdash; trước khi họ quyết định. Đây là lý do San Shou được gọi là \"tay lắng nghe\".</p>",
    ),
    (
        "<h3>Drills</h3>"
        "<p><strong>Wall Test (Kiểm tra tường)</strong> &mdash; Face a wall 2 feet away. Place both palms flat on it, shoulder-width apart. Without moving feet, push gently. Feel the wall's reaction travel back through arms into dantian and legs. The wall never moves but you should feel a full-body connection.</p>"
        "<p><strong>Floor Test (Kiểm tra sàn)</strong> &mdash; Sit with legs extended. Partner places palm lightly on your knee. As they shift weight forward, practice maintaining contact without gripping. The knee should feel intention but not force.</p>",
        "<h3>BÀI TẬP</h3>"
        "<p><strong>Kiểm tra tường</strong> &mdash; Hướng thẳng bức tường cách 2 feet. Đặt cả bàn tay phẳng lên, rộng vai. Không di chuyển chân, đẩy nhẹ. Cảm nhận phản hồi qua cánh tay xuống Đan Điền và chân. Tường không di chuyển nhưng bạn cảm thấy kết nối toàn thân.</p>"
        "<p><strong>Kiểm tra sàn</strong> &mdash; Ngồi với chân duỗi thẳng. Đối tác đặt bàn tay nhẹ lên đầu gối. Khi họ dịch trọng lượng, luyện duy trì tiếp xúc mà không nắm chặt. Đầu gối cảm thấy ý định nhưng không cảm thấy lực.</p>",
    ),
    (
        "<h3>Common Errors</h3>"
        "<p><strong>Leading with the hands</strong>: stepping before establishing root means hands pull structure forward and you lose the listening connection. <strong>Holding at the wrist</strong>: gripping to resist force instead of flowing through. <strong>Collapsing the chest</strong>: rounding the upper back to absorb push instead of yielding from the center.</p>",
        "<h3>LỖI PHỔ BIẾN</h3>"
        "<p><strong>Động thủ trước tiếng</strong>: bước trước khi thiết lập nền tảng có nghĩa là tay kéo cấu trúc tới trước và mất kết nối lắng nghe. <strong>Nhấp vai ở cổ tay</strong>: nắm để chống lực thay vì chảy qua. <strong>Collapsed ngực</strong>: quăn lưng trên để hấp thụ lực thay vì nhường từ trung tâm.</p>",
    ),
    mc("Meet like water. Return like a wave.", "Gặp như nước. Trở lại như sóng."),
],

"dien": [
    (
        "<h3>The Big Idea</h3>"
        "<p><strong>Brush Knee (Diên / 剪)</strong> is the most repeated movement in the 24-form &mdash; and the most done carelessly. At its core it is a <em>coordination test</em>: the waist rotates to bring the front hand across the body, the rear hand follows, and the step adjusts. All three parts must move together.</p>"
        "<p>If the waist stops halfway, the front hand pulls too far and the shoulder collapses (\"sheep shoulder\"). If the step does not adjust, the hip binds. Brush Knee is the form's built-in diagnostic: do your parts still move as one?</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3>"
        "<p><strong>Chỉ Lông / Nhấp Bước (Diên / 剪)</strong> là chuyển động lặp lại nhiều nhất trong bài 24 và thường thực hiện sơ suất. Ở trọng tâm, nó là <em>kiểm tra phối hợp</em>: eo quay để đưa tay trước ngang qua người, tay sau theo, bước điều chỉnh. Ba phần phải cùng chuyển động.</p>"
        "<p>Nếu eo dừng nửa đường, tay trước kéo quá và vai sụp. Nếu bước không điều chỉnh, hông khóa. Nhấp Bước là trình chẩn đoán: các bộ phận có còn di chuyển như một khối không?</p>",
    ),
    (
        "<h3>Drills</h3>"
        "<p><strong>Mirror Brush (Chỉ lông gương)</strong> &mdash; Stand facing a mirror. Perform Brush Knee on one side only. Watch the line from front shoulder to front wrist. It should stay straight; the hand sweeps like a brush, not a hook.</p>"
        "<p><strong>Waist Count (Đếm eo)</strong> &mdash; For 10 reps on one side, count \"1-2-3\" in your head: 1 = waist starts to turn, 2 = hand crosses center, 3 = step adjusts. If you cannot say all three clearly, the parts are out of sync.</p>",
        "<h3>BÀI TẬP</h3>"
        "<p><strong>Chỉ lông gương</strong> &mdash; Đứng trước gương. Thực hành Nhấp Bước chỉ ở một bên. Nhìn đường từ vai trước đến cổ tay. Phải thẳng; tay cọ như bàn chữ, không phải móc.</p>"
        "<p><strong>Đếm eo</strong> &mdash; Với 10 lần ở một bên, đếm \"1-2-3\": 1 = eo bắt đầu quay, 2 = tay vượt qua trung tâm, 3 = bước điều chỉnh. Nếu không nói rõ 3 số, các bộ phận bất đồng bộ.</p>",
    ),
    (
        "<h3>Why It Appears 4 Times</h3>"
        "<p>The 24-form repeats Brush Knee twice per side (4 total). Each repetition uses a different body mechanic: first time leads with hip rotation, second with waist rotation, third with shoulder blade squeeze, fourth integrates all three. This progressive layering &mdash; the form teaching the body to refine one skill through different doors &mdash; is one of Tai Chi's deepest pedagogical tricks.</p>",
        "<h3>TẠI SAO LẶP LẠI 4 LẦN</h3>"
        "<p>Bài 24 lặp lại Nhấp Bước 2 lần mỗi bên (4 tổng cộng). Mỗi lần dùng cơ chế khác: lần 1 dẫn bằng hông, lần 2 bằng eo, lần 3 bằng võng mạc, lần 4 tích hợp cả ba. Lớp hóa tiến bộ này &mdash; dạy cơ thể tinh luyện một kỹ năng qua những cánh cửa khác nhau &mdash; là một trong những “thủ thuật” dạy học sâu nhất của Thái Cực.</p>",
    ),
    mc("Brush the knee, feel the waist turn. Do not force the hand.", "Chỉ lông, cảm thấy eo quay. Đừng ép tay."),
],

"xie-bu": [
    (
        "<h3>The Big Idea</h3>"
        "<p><strong>Twist Step (Quay / 轉 bước)</strong> is where Waist (Dẫn Bất Đối) meets Step (Bước Thật). The feet plant firmly to anchor; the waist rotates to redirect; the step carries the redirect. Unlike a pivot (which rotates around a fixed axis), twist step is a <em>traveling rotation</em>: the axis moves through the body as the center shifts.</p>"
        "<p>The power vector shifts from vertical (root) to horizontal (redirect). The 50+ body often does this backwards &mdash; twisting from the shoulders or knees. The correct path: root through the feet, rotate from the dantian, land the step with the center forward.</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3>"
        "<p><strong>Bước Xoay (Quay / 轉 bước)</strong> là nơi Eo (Dẫn Bất Đối) gặp Bước (Bước Thật). Chân đặt chắc để neo; eo quay để chuyển hướng; bước mang sự chuyển hướng. Không giống pivot (xoay quanh trục cố định), twist step là <em>sự xoay dịch chuyển</em>: trục di chuyển qua cơ thể khi trung tâm dịch chuyển.</p>"
        "<p>Vector lực chuyển từ thẳng đứng (nền tảng) sang ngang (chuyển hướng). Cơ thể 50+ thường ngược lại &mdash; xoay từ vai hoặc khớp. Đường đi đúng: neo qua chân, quay từ Đan Điền, đặt bước với trung tâm phía trước.</p>",
    ),
    (
        "<h3>Drills</h3>"
        "<p><strong>Grounding the Anchor (Neo chân)</strong> &mdash; In a shallow horse stance, lift the front heel. Feel the front ball of foot root down. Now rotate the waist 45 degrees (if left foot is forward). The lifted heel should naturally settle back down. Do not force it &mdash; let the rotation carry it.</p>"
        "<p><strong>Torso vs Feet Check (Kiểm tra người vs chân)</strong> &mdash; Perform a twist step slowly. At maximum waist rotation, pause. Can you draw a straight line from nose to front big toe? If not, the twist is disconnected from the step.</p>",
        "<h3>BÀI TẬP</h3>"
        "<p><strong>Neo chân</strong> &mdash; Trong tư thế cờ đề, nhấc gót chân trước. Cảm thấy mắt chân cảm xuống. Bây giờ quay eo 45 độ (nếu chân trái trước). Gót nhấc tự nhiên đặt xuống. Đừng ép &mdash; để sự xoay mang nó.</p>"
        "<p><strong>Kiểm tra người vs chân</strong> &mdash; Thực hành xoay bước chậm. Ở độ xoay tối đa, dừng. Bạn có vẽ đường thẳng từ mũi đến ngón chân cái không? Nếu không, sự xoay tách rời khỏi bước.</p>",
    ),
    (
        "<h3>Knee Protection at 50+</h3>"
        "<p>The twist step is the single best protection for aging knees. In a pure pivot, the knee must torque under load &mdash; the femur rotates while the tibia stays fixed, putting shear on the joint. In a twist step, the knee follows the same direction as the hip; femur and tibia rotate together. The joint never experiences shear; it only rotates as naturally designed.</p>",
        "<h3>BẢO VỆ KHỚP 50+</h3>"
        "<p>Bước xoay là sự bảo vệ tốt nhất cho khớp gối lão hóa. Trong pivot thuần túy, gối phải chịu mômen xoắn dưới tải &mdash; xương đùi quay trong khi cẳng dưới ổn định, gây ma sát trên khớp. Trong bước xoay, gối đi theo cùng hướng với hông; xương đùi và cẳng dưới quay cùng. Khớp không chịu ma sát; chỉ nhận sự quay một cách tự nhiên.</p>",
    ),
    mc("Root the feet. Rotate the dantian. Let the step follow.", "Neo chân. Xoay Đan Điền. Để bước tự đi theo."),
],

"kai-gong": [
    (
        "<h3>The Big Idea</h3>"
        "<p><strong>Khai Gôn (開功 / Rowing the Chariot)</strong> is the second movement of the form, the moment when your body first learns to coordinate front and back. The front hand pushes forward (palms down) while the rear hand pulls back (palms up). The spine lengthens; the waist turns; the step adjusts. This is the first full-body pattern students can actually <em>feel</em>.</p>"
        "<p>Before Khai Gôn, most students move in fragments. After Khai Gôn, the body must decide: move as one, or never move at all in Tai Chi.</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3>"
        "<p><strong>Khai Gôn (開功 / Kéo Xe)</strong> là chuyển động thứ hai trong bài, khoảnh khắc cơ thể học phối hợp trước và sau. Tay trước đẩy tới (lòng xuống) trong khi tay sau kéo lại (lòng lên). Sống người dài ra; eo quay; bước điều chỉnh. Đây là pattern toàn thân đầu tiên mà học viên thực sự <em>cảm thấy</em> được.</p>"
        "<p>Trước Khai Gôn, hầu hết học viên di chuyển từng mảnh. Sau Khai Gôn, cơ thể phải quyết định: di chuyển như một khối, hoặc sẽ không bao giờ di chuyển trong Thái Cực.</p>",
    ),
    (
        "<h3>Drills</h3>"
        "<p><strong>Finger-to-Fingertip Coordination (Từ ngón đến ngón)</strong> &mdash; In Khai Gôn, keep the front wrist soft. The rear hand should reach full extension at the exact moment the front hand reaches its midpoint. Feel the energy transfer like a wave rolling from tailbone to fingertips.</p>"
        "<p><strong>Breath Sync Check (Kiểm tra đồng bộ hơi thở)</strong> &mdash; Exhale during push; inhale during pull. If you cannot maintain this breath pattern, the waist is not turning sufficiently.</p>",
        "<h3>BÀI TẬP</h3>"
        "<p><strong>Từ ngón đến ngón</strong> &mdash; Trong Khai Gôn, giữ cổ tay trước mềm. Tay sau phải kéo dài đúng lúc tay trước đạt điểm giữa. Cảm năng lượng như sóng lăn từ xương cụt đến ngón tay.</p>"
        "<p><strong>Kiểm tra đồng bộ hơi thở</strong> &mdash; Thở ra khi đẩy; thở vào khi kéo. Nếu không duy trì được, eo không quay đủ.</p>",
    ),
    (
        "<h3>The Spine Lengthening Secret</h3>"
        "<p>The detail that separates correct Khai Gôn from broken: the front shoulder blade must rotate <em>before</em> the arm pushes. This is invisible to observers but essential. Without it, arms lead and the spine collapses. With it, the spine lengthens under the movement &mdash; the body literally grows taller during the push.</p>",
        "<h3>BÍ MẬT DÀNH CHO SỐNG NGƯỜI</h3>"
        "<p>Chi tiết tách biệt Khai Gôn đúng với sai: võng mạc trước phải quay <em>trước</em> khi tay đẩy. Không nhìn thấy nhưng thiết yếu. Nếu thiếu, tay dẫn và sống người sụp. Nếu có, sống người dài ra &mdash; cơ thể đơ thực sự cao hơn trong giai đoạn đẩy.</p>",
    ),
    mc("Let the shoulder blade lead. Feel the spine lengthen.", "Để võng mạc dẫn. Cảm sống người dài ra."),
],

"tu-hu": [
    (
        "<h3>The Big Idea</h3>"
        "<p><strong>Tô Hô (Lifting the Paten)</strong> appears in the 24-form as Part the Wild Horse's Mane and in the 42-form as Lift the Paten. The imagery is borrowed from Buddhist temple life: the paten (the plate that holds the offering) is lifted with two hands, slowly, with the whole body.</p>"
        "<p>In Tai Chi, Tô Hô is a full-body integration movement. The front hand does not grab; it <em>supports</em>. The waist rotates to lift; the legs root to stabilize. The arms act as extensions of the spine, not independent movers. This is why Tô Hô is so revealing &mdash; it shows whether your arm is connected to your dantian.</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3>"
        "<p><strong>Tô Hô (Nâng Nhiễn)</strong> xuất hiện trong bài 24 ở phần \"Chia Tàu Bì\" và trong 42 dưới tên \"Nâng Nhiễn\". Hình ảnh lấy từ đời sống chùa chiền: nhiễn (đĩa chứa lễ vật) được nâng bằng hai tay, chậm rãi, bằng cả cơ thể.</p>"
        "<p>Trong Thái Cực, Tô Hô là chuyển động tích hợp toàn thân. Tay trước không nắm; nó <em>hỗ trợ</em>. Eo quay để nâng; chân neo để ổn định. Cánh tay như phần kéo dài của sống người, không phải bộ phận độc lập. Đây là lý do Tô Hô rất tiết lộ &mdash; nó cho thấy tay bạn có kết nối Đan Điền không.</p>",
    ),
    (
        "<h3>Drills</h3>"
        "<p><strong>Lift from the Seat (Nâng từ xích)</strong> &mdash; As you lift, imagine the front hand is suspended by a rope tied to your tailbone. The rope pulls up through the center; the hand is the last to rise. If the hand rises before the center, you are using arm strength.</p>"
        "<p><strong>Plate Balance (Cân bằng nhiễn)</strong> &mdash; Perform Tô Hô slowly. At the peak of the lift, pause for 3 full breaths. The front hand should float, not grip. Any sensation of contraction in the arm = losing the lift.</p>",
        "<h3>BÀI TẬP</h3>"
        "<p><strong>Nâng từ xích</strong> &mdash; Khi nâng, hình tưởng tay trước được treo bằng sợi dây buộc vào xương cụt. Sợi dây kéo lên qua trung tâm; tay là thứ cuối cùng nổi lên. Nếu tay nổi trước trung tâm, bạn đang dùng sức tay.</p>"
        "<p><strong>Cân bằng nhiễn</strong> &mdash; Thực hành Tô Hô chậm. Ở đỉnh nâng, dừng 3 hơi thở. Tay trước nên lơ lửng, không nắm chặt. Bất kỳ cảm giác co cốt ở tay = mất nâng.</p>",
    ),
    (
        "<h3>The Support vs Pull Distinction</h3>"
        "<p>Tô Hô has two energies: <em>support</em> (the upward lift that stabilizes the opponent) and <em>pull</em> (the downward adjustment that redirects force). Beginners feel support easily; the pull takes longer. The pull is what happens after you feel the opponent leaning into you: you do not resist, you do not meet their force head-on, you let them step into emptiness.</p>",
        "<h3>SỰ PHÂN BIỆT HỖ TRỢ VÀ KÉO</h3>"
        "<p>Tô Hô có hai năng lượng: <em>hỗ trợ</em> (nâng lên ổn định đối phương) và <em>kéo</em> (điều chỉnh hạ để chuyển hướng). Người mới dễ cảm thấy hỗ trợ; kéo mất thời gian hơn. Kéo là điều xảy ra sau khi bạn cảm thấy đối phương dựa vào bạn: bạn không chống, bạn không đối mặt, bạn để họ bước vào hư không.</p>",
    ),
    mc("Lift from the center. Let the hand follow.", "Nâng từ trung tâm. Để tay theo sau."),
],

"hoa-buoc": [
    (
        "<h3>The Big Idea</h3>"
        "<p><strong>Hoa Bước (化步 / Flowing Step)</strong> is the step of redirection. Instead of meeting an opponent's push with resistance, you flow around it like water parting around a stone. The name \"Hoa\" means \"to flow\" or \"to transform,\" not \"to soften passively.\"</p>"
        "<p>The technique: as force enters, you step <em>offline</em> &mdash; not backward (that is retreat), not forward (that is collision), but at an angle. The angle absorbs the force into the ground through your legs. This is why Hoa Bước is the antidote to San Shou&rsquo;s direct engagement.</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3>"
        "<p><strong>Bước Hóa (Hoa Bước / 化步)</strong> là bước chuyển hướng. Thay vì đối mặt với lực ép của đối phương bằng kháng cự, bạn chảy quanh như nước chảy quanh đá. \"Hoa\" nghĩa là \"chảy\" hay \"biến đổi,\" không phải \"hóa nhẹ thụ động\".</p>"
        "<p>Kỹ thuật: khi lực đến, bạn bước <em>không thẳng</em> &mdash; không lùi (đó là thu hút), không tới (đó là va chạm), mà theo góc. Góc hút lực xuống đất qua chân. Đây là lý do Bước Hóa là thuốc đối với sự va chạm trực tiếp của San Shou.</p>",
    ),
    (
        "<h3>Drills</h3>"
        "<p><strong>Angle Practice (Luyện góc)</strong> &mdash; Mark a line on the floor with tape (6 feet long). Stand on it with left foot forward. Have a partner push your shoulder from straight ahead. Step 45 degrees to your left so the force travels through your left leg to the ground. Do not stop moving your feet &mdash; the angle must stay active.</p>"
        "<p><strong>Blind Angle Walk (Đi bước hóa mờ)</strong> &mdash; Eyes closed, walk 10 steps in a room with furniture. Every time you encounter a chair leg, execute a Hoa Bước around it. Your body learns the angle without thinking.</p>",
        "<h3>BÀI TẬP</h3>"
        "<p><strong>Luyện góc</strong> &mdash; Vẽ một đường dây dính 6 feet. Đứng trên với chân trái trước. Đối tác đẩy vai từ phía trước thẳng. Bước 45 độ sang trái để lực qua chân trái xuống đất. Đừng dừng chân &mdash; góc phải luôn hoạt động.</p>"
        "<p><strong>Đi bước hóa mờ</strong> &mdash; Nhắm mắt, đi 10 bước trong phòng có đồ nội thất. Mỗi lần gặp chân ghế, thực hành Bước Hóa quanh. Cơ thể học góc mà không cần nghĩ.</p>",
    ),
    (
        "<h3>Why \\'Hoa\\' Is Not \\'Soft\\'</h3>"
        "<p>Western students hear \"flow\" and collapse. They step offline but go limp &mdash; no root, no structure, no follow-up. Correct Hoa Bước flows <em>while rooted</em>. You are like a reed that bends in the wind but holds in the earth. The flow is active, not passive; it redirects while maintaining connection.</p>",
        "<h3>TẠI SAO \\'Hoa\\' KHÔNG PHẢI \\'MỀM\\'</h3>"
        "<p>Sinh viên Tây nghe \"chảy\" và sụp xuống. Họ bước lệch nhưng tay lỏng &mdash; không neo, không cấu trúc, không tiếp tục. Bước Hóa đúng phải chảy <em>trong khi neo</em>. Bạn như cây cỏ uốn trong gió nhưng vững trong đất. Sự chảy là hoạt động, không phải thụ động; nó chuyển hướng trong khi duy trì kết nối.</p>",
    ),
    mc("Flow online while rooted. Redirect, do not resist.", "Chảy theo góc trong khi neo. Chuyển hướng, đừng chống."),
],

"ba-hoi": [
    (
        "<h3>The Big Idea</h3>"
        "<p><strong>Bát Hướng (Opening Eight Directions)</strong> is a stance and movement pattern that establishes the body's axes &mdash; forward/back, left/right, up/down &mdash; all anchored simultaneously. You are a cross: arms outstretched, legs in horse stance, feet rooting into earth and sky.</p>"
        "<p>The movement principle: each direction is a door. When you push forward, the back door opens. When you pull back, the front door opens. The 50+ body needs this spatial awareness to compensate for the narrowed peripheral vision that aging brings. Bát Hướng is literally \"opening\" to the world again.</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3>"
        "<p><strong>Mở Bát Hướng (Opening Eight Directions)</strong> là tư thế và mẫu chuyển động thiết lập trục cơ thể &mdash; trước/sau, trái/phải, trên/dưới &mdash; đều được neo đồng thời. Bạn là một cái cánh tay: tay đưa rộng, chân cờ đề, nền tảng xuống đất và bầu trời.</p>"
        "<p>Nguyên lý: mỗi hướng là một cánh cửa. Khi bạn đẩy tới, cánh cửa sau mở ra. Khi kéo lại, cánh cửa trước mở ra. Cơ thể 50+ cần nhận thức không gian này để bù đắp thị lực vi mô mà lão hóa mang lại. Bát Hướng về cơ bản là \"mở\" ra thế giới một lần nữa.</p>",
    ),
    (
        "<h3>Drills</h3>"
        "<p><strong>Wall Frame (Khung tường)</strong> &mdash; Stand facing a wall, arms extended, palms flat on the wall at shoulder height. Slowly lower yourself into a horse stance while keeping palms in contact. If you lean forward, you have moved your center; if the palms lift, you have lost root. Find the depth where both conditions hold.</p>"
        "<p><strong>Eight-Point Compass (La bàn tám điểm)</strong> &mdash; From Bát Hướng stance, point each finger, thumb, and elbow in a different cardinal direction. Then point each toe, heel, and knee. When all 14 points are oriented correctly, the body is a compass.</p>",
        "<h3>BÀI TẬP</h3>"
        "<p><strong>Khung tường</strong> &mdash; Đứng trước tường, tay đưa, lòng bàn tay phẳng lên ở ngang vai. Chậm rãi hạ xuống cờ đề trong khi giữ tay chạm tường. Nếu nghiêng tới, bạn dịch chuyển trung tâm; nếu bàn tay nâng lên, bạn mất neo. Tìm độ sâu giữa cả hai.</p>"
        "<p><strong>La bàn tám điểm</strong> &mdash; Từ Bát Hướng, chỉ từng ngón tay, ngón cái, và khuỷu. Sau đó chỉ từng ngón chân, gót, và khuỷu. Khi 14 điểm đều hướng đúng, cơ thể là một chiếc la bàn.</p>",
    ),
    (
        "<h3>The \\'Opening\\' Mechanism</h3>"
        "<p>Bát Hướng is not about stretching further. It is about <em>releasing</em> what you have been unconsciously holding. Most people carry tension in their jaws, their shoulders, their hips. The \\'opening\\' is the body&rsquo;s natural response when that tension is removed &mdash; arms float out, spine lengthens, breath deepens. For the 50+ body, this \"opening\" may be the first time in years the shoulders have moved freely.</p>",
        "<h3>CƠ CHẾ \\'MỞ\\' CỦA BÁT HƯỚNG</h3>"
        "<p>Bát Hướng không phải kéo dài thêm. Nó là <em>giải phóng</em> những gì bạn đã không tỉnh thức giữ. Nhiều người mang căng vào hàm, vai, hông. \"Mở\" là phản hồi tự nhiên của cơ thể khi căng được loại bỏ &mdash; tay bay ra, sống người dài ra, hơi thở sâu hơn. Đối với cơ thể 50+, \"mở\" này có thể là lần đầu tiên trong nhiều năm mắt cá chân của bạn.</p>",
    ),
    mc("Open to receive. Do not reach to grab.", "Mở để nhận. Đừng vươn để nắm."),
],

"thieu-hai": [
    (
        "<h3>The Big Idea</h3>"
        "<p><strong>Lãm Tưọc Vỹ (Grasp Sparrow's Tail)</strong> is the signature sequence of Yang-style Tai Chi: Peng &rarr; Lu &rarr; Ji &rarr; An &rarr; Turn &rarr; Repulse. It combines all four primary energies in one flowing phrase. You will practice it 4 times in the 24-form &mdash; twice on each side.</p>"
        "<p>The sequence teaches four things simultaneously: (1) the four energies flow as one wave, (2) each energy has its own precise hand shape, (3) the waist turns to carry the next movement, (4) the step adjusts to ground each transition. Mastery is not memorizing the shape &mdash; it is feeling the wave.</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3>"
        "<p><strong>Lãm Tưọc Vỹ (Grasp Sparrow's Tail)</strong> là câu nói đặc trưng của Thái Cực Dương phái: Phòng &rarr; Lỹ &rarr; Tỳ &rarr; Án &rarr; Quay &rarr; Lãm Tưọc Vỹ. Nó kết hợp bốn năng lượng trong một câu lạch ngàn. Bạn sẽ luyện 4 lần trong bài 24 &mdash; hai lần mỗi bên.</p>"
        "<p>Câu này dạy bốn điều đồng thời: (1) bốn năng lượng chảy như một con sóng, (2) mỗi năng lượng có hình dạng tay riêng, (3) eo quay để mang chuyển động kế tiếp, (4) bước đi để neo từng chuyển tiếp. Sự thành thạo không phải học thuộc hình dạng &mdash; mà là cảm thấy con sóng.</p>",
    ),
    (
        "<h3>Drills</h3>"
        "<p><strong>Wave Visualization (Hình ảnh sóng)</strong> &mdash; As you perform the sequence, imagine your body is a wave moving through deep water. Peng is the rise, Lu is the curl, Ji is the compression, An is the fall. The wave does not stop at each phase; it carries momentum through the entire sequence.</p>"
        "<p><strong>Energy Isolation (Cá nhân năng lượng)</strong> &mdash; Practice the sequence extremely slowly. At each transition, pause for 3 seconds and name the energy: \"peng...\" (pause) \"lu...\" (pause) \"ji...\" (pause) \"an.\" Only when the names flow naturally should you speed up.</p>",
        "<h3>BÀI TẬP</h3>"
        "<p><strong>Hình ảnh sóng</strong> &mdash; Khi thực hành câu này, hình tưởng cơ thể là một con sóng trong nước sâu. Phòng là sóng lên, Lỹ là sóng cuốn, Tỳ là nén, Án là sóng xuống. Sóng không dừng lại ở mỗi giai đoạn; nó mang động lượng qua toàn bộ câu.</p>"
        "<p><strong>Cá nhân năng lượng</strong> &mdash; Thực hành câu này cực kỳ chậm. Ở mỗi chuyển tiếp, dừng 3 giây và đặt tên năng lượng: \"phòng...\" (dừng) \"lỹ...\" (dừng) \"tỳ...\" (dừng) \"án.\" Chỉ khi các tên chảy tự nhiên nên bạn mới tăng tốc.</p>",
    ),
    (
        "<h3>The Hand Shapes</h3>"
        "<p>Each energy has a precise hand shape: Peng uses the back of the hand (receiving face up), Lu uses the thumb-side edge (guiding), Ji uses the palm center (compressing), An uses the full palm (finishing). These are not arbitrary &mdash; the bone structure of each hand shape matches the force direction of its energy. Getting the hand shape right makes the energy automatic.</p>",
        "<h3>HÌNH DẠNG TAY</h3>"
        "<p>Mỗi năng lượng có hình dạng tay chính xác: Phòng dùng lưng tay (mặt nhận lên), Lỹ dùng mép thái dương (dẫn dắt), Tỳ dùng trung tâm lòng bàn tay (nén), Án dùng toàn bàn tay (kết thúc). Những dạng này không ngẫu nhiên &mdash; cấu trúc xương của mỗi hình dáng khớp với hướng lực của năng lượng. Lấy hình dạng tay đúng làm cho năng lượng tự động.</p>",
    ),
    mc("Feel the wave. Not the steps.", "Cảm con sóng. Đừng cảm các bước."),
],

"shou-ba": [
    (
        "<h3>The Big Idea</h3>"
        "<p><strong>Thủ Bát Bảo (Guardian Posture)</strong> appears in the 24-form as \"Hug the Sparrow\" and in the 108-form at several points. The imagery: you are guarding a treasure (a bowl of rice, a child, a secret). Your arms form a protective circle around your center; your legs root wide to resist any direction of force.</p>"
        "<p>The technique principle: the center never moves. The arms and legs respond &mdash; they do not lead. When a partner pushes your left arm, your right leg pushes back into the ground. The force does not meet at the contact; it is resolved in the earth through the opposite leg.</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3>"
        "<p><strong>Tư Thế Thủ Bát Bảo</strong> xuất hiện trong bài 24 ở \"Ôm Chim Én\" và trong 108 ở nhiều điểm. Hình ảnh: bạn đang canh giữ kho báu (bát cơm, đứa trẻ, bí mật). Cánh tay hình thành vòng tròn bảo vệ trung tâm; chân rộng để chịu bất kỳ hướng lực nào.</p>"
        "<p>Nguyên lý: trung tâm không bao giờ di chuyển. Cánh tay và chân phản ứng &mdash; chúng không dẫn. Khi đối tác đẩy tay trái, chân phải đẩy ngược xuống đất. Lực không gặp nhau ở điểm tiếp xúc; nó được giải quyết trong đất qua chân đối diện.</p>",
    ),
    (
        "<h3>Drills</h3>"
        "<p><strong>Unmoving Center (Trung tâm bất động)</strong> &mdash; Stand in Thủ Bát Bảo. Have a partner push and pull on both arms alternately. Your task is to keep your dantian perfectly still &mdash; no forward, no back, no side-to-side. If your center moves, you are using arm strength, not root.</p>"
        "<p><strong>Opposite Leg Resolution (Giải quyết bằng chân đối)</strong> &mdash; Partner pushes your left arm hard. Instead of tensing the left side, feel your right leg press harder into the ground. The force travels: arm &rarr; spine &rarr; dantian &rarr; right leg &rarr; earth. Name each link as the force passes.</p>",
        "<h3>BÀI TẬP</h3>"
        "<p><strong>Trung tâm bất động</strong> &mdash; Đứng Thủ Bát Bảo. Đối tác đẩy kéo hai tay luân phiên. Nhiệm vụ giữ Đan Điền hoàn toàn không chuyển &mdash; không tới, không lại, không qua. Nếu trung tâm di chuyển, bạn đang dùng sức tay, không phải neo.</p>"
        "<p><strong>Giải quyết bằng chân đối</strong> &mdash; Đối tác đẩy tay trái mạnh. Thay vì căng bên trái, hãy cảm nhận chân phải ép mạnh xuống đất. Lực di chuyển: tay &rarr; sống người &rarr; Đan Điền &rarr; chân phải &rarr; đất. Đặt tên mỗi liên kết.</p>",
    ),
    (
        "<h3>The Treasure You Are Guarding</h3>"
        "<p>The treasure is not external &mdash; it is the space inside your own rib cage. Your arms guard that space. When you breathe correctly in Thủ Bát Bảo, the rib cage expands on the inhale and the arms open slightly; on the exhale, the rib cage settles and the arms settle. This is why the posture is so therapeutic for the 50+ body: it creates a moving space for the internal organs.</p>",
        "<h3>CHIẾN Vật Bạn Đang Canh Giữ</h3>"
        "<p>Chiến vật không phải bên ngoài &mdash; mà là khoảng không gian trong ngực của chính bạn. Cánh tay canh giữ không gian đó. Khi bạn hít đúng, ngực mở ra và tay mời chút; khi thở ra, ngực hạ và tay xuống. Đây là lý do tư thế rất hữu ích cho cơ thể 50+: nó tạo không gian cho các cơ quan nội tạng.</p>",
    ),
    mc("Guard the center. Let the legs resolve.", "Canh giữ trung tâm. Để chân giải quyết."),
],

"nghich-buoc": [
    (
        "<h3>The Big Idea</h3>"
        "<p><strong>Nghịch Bước (Counter-Step / 逆步)</strong> is the step of yielding. When an opponent pushes forward, instead of meeting their force, you step <em>backward and offline</em> at a 45-degree angle. This does two things: (1) it puts your body outside the line of their force, and (2) it positions your rear foot to drive the counter-redirect.</p>"
        "<p>Crucial: Nghịch Bước is <em>not retreat</em>. A retreat steps straight back, leaving the force to dissipate harmlessly. A counter-step steps offline while maintaining root pressure &mdash; you are still grounded, still ready to return the redirection.</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3>"
        "<p><strong>Bước Ngược (Nghịch Bước / 逆步)</strong> là bước nhường. Khi đối phương đẩy tới, thay vì đối mặt với lực, bạn bước <em>lùi và lệch</em> 45 độ. Điều này làm hai việc: (1) đưa cơ thể ra ngoài đường lực của đối phương, (2) đặt chân sau để thúc đẩy chuyển hướng.</p>"
        "<p>Thiêng liêng: Bước Ngược không phải là <em>hồi thuyen</em>. Hội chẩn thẳng lùi, để lực tan biến. Bước Ngược bước lệch trong khi duy trì áp lực neo &mdash; bạn vẫn đất, vẫn sẵn sàng trả lại chuyển hướng.</p>",
    ),
    (
        "<h3>Drills</h3>"
        "<p><strong>Counter-Angle Walk (Đi bước ngược góc)</strong> &mdash; Place tape on the floor in an L-shape (2 feet each leg). Start at the corner. As you step back along one leg of the L, keep the other foot planted. Feel how the planted foot grounds the redirect. Repeat on the other side.</p>"
        "<p><strong>Push-&-Step (Đẩy & rồi bước)</strong> &mdash; Partner pushes your left shoulder. Instead of resisting, immediately step your right foot back and offline. The movement should be simultaneous, not sequential. Time it with your breath: push in, step out.</p>",
        "<h3>BÀI TẬP</h3>"
        "<p><strong>Đi bước ngược góc</strong> &mdash; Dán băng giấy trên sàn thành hình L (2 feet mỗi chân). Bắt đầu ở góc. Khi bước lùi dọc một cánh của L, giữ chân kia đặt chân. Cảm thấy chân đặt làm việc với chuyển hướng. Lặp lại bên kia.</p>"
        "<p><strong>Đẩy & rồi bước</strong> &mdash; Đối tác đẩy vai trái. Thay vì chống, ngay lập tức bước chân phải lùi và lệch. Chuyển động phải đồng thời, không tuần tự. Đồng bộ với hơi thở: hít vào, thở ra.</p>",
    ),
    (
        "<h3>When to Use Counter-Step vs Flow Step</h3>"
        "<p>Nghịch Bước is for <strong>strong, direct pushes</strong> &mdash; when the opponent's force is too concentrated to redirect passively. Hoa Bước is for <strong>gentle, probing pushes</strong> &mdash; when you can feel and redirect without changing position. The decision threshold: if the push moves your center, use Nghịch Bước. If the push only affects your arms, use Hoa Bước.</p>",
        "<h3>KHI NÀO DÙNG BƯỚC NGUỘC vs BƯỚC HÓA</h3>"
        "<p>Bước Ngược dùng cho <strong>những cú đẩy mạnh trực tiếp</strong> &mdash; khi lực của đối phương quá tập trung để chuyển hướng thụ động. Bước Hóa dùng cho <strong>những cú đẩy nhẹ nhàng thăm dò</strong> &mdash; khi bạn có thể cảm và chuyển hướng mà không thay đổi vị trí. Ngưỡng quyết định: nếu cú đẩy di chuyển trung tâm, dùng Bước Ngược. Nếu cú đẩy chỉ ảnh hưởng tay, dùng Bước Hóa.</p>",
    ),
    mc("Step offline. Stay rooted. Return the wave.", "Bước lệch. Giữ neo. Trả con sóng."),
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
        # Find the end of the topics <section> by looking for </article> before page-nav
        article_close = text.find("</article>")
        if article_close == -1:
            print(f"  WARN: </article> not found in {idx_path}")
            continue
        # The </section> before </article> closes the topics section
        section_close = text.rfind("</section>", 0, article_close)
        new_text = text[:section_close] + insertion + text[section_close:]
        idx_path.write_text(new_text, encoding='utf-8')
        print(f"  appended 10 topics to {idx_path.relative_to(REPO)}")


if __name__ == "__main__":
    print("--- Building Batch 5: 10 new topic pages (EN+VI) ---")
    for slug, en_title, vi_title in NEW_TOPICS:
        build_topic(slug, en_title, vi_title)
    print("--- Updating techniques index (EN+VI) ---")
    update_techniques_index_new()
