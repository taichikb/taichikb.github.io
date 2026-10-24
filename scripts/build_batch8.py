#!/usr/bin/env python3
"""Build 10 advanced EN + 10 VI technique-topic subpages (Batch 8 - 4.0+ level).

Advanced 4.0+ skills: Fixed Stability, Hua Jin, Zhou Tian (circling),
Kai Bu (emerging step), Chan Dun (suspended-heavy), Four Primary Energies,
Tu Yi (void meaning), Zhen Dong (true lock), Song Jin (letting go), Hai Cao.

Reuses page_shell and build_topic from build_topics.py.
"""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_topics import page_shell

REPO = Path("D:/Taichi-Health-Finance/Intranet/taichikb_repo")

# New topics to add (slug, en_title, vi_title)
NEW_TOPICS = [
    ("ding-bai", "Fixed Stability (Ding / 定) — Unshakeable Center", "Sự Cố Định (Ding / 定) — Tâm Hồn Bất Động"),
    ("hua-jin", "Hua Jin (Hóa Tấn / 化勁) — Transforming Power Into Neutralization", "Hóa Tấn (Hóa / 化勁) — Biến Đổi Lực Thành Trung Hòa"),
    ("zhou-tian", "Circling the Moon (Trăng / 月) — The Hidden Spiral in Grasp Sparrow's Tail", "Đi Vòng Trăng (Trăng / 月) — Xoắn Ẩn Trong Chưởng Vịt"),
    ("kai-bu", "Emerging Step (Khai Bước / 開步) — Mechanics of the Expanding Stance", "Bước Mở (Khai Bước / 開步) — Cơ học của Thế Mở Rộng"),
    ("chan-dun", "Suspended & Heavy (Chanh / 穿) — Coordinating Lightness and Weight", "Chanh Treo Nặng — Điều Phối Ánh Nhẹ Với Trọng Lượng"),
    ("four-energies", "The Four Primary Energies (Pháp / 八) — Peng, Lu, Ji, An as Unified Skill", "Bốn Năng Lượng Chính (Pháp / 八) — Phòng, Lượ, Tỳ, Án Như Một"),
    ("tu-yi", "Empty Void (Thê / 空) — The Meaning Beyond Form", "Thê Không (Thê / 空) — Nghĩa Vượt Mẫu Hình"),
    ("zhen-dong", "True Lock (Chéng / 頂) — Internal Iron Shirt Against Impact", "Chéng Thực (Chéng / 顶) — Áo Sắt Nội Tại Chống Va Chạm"),
    ("song-jin", "Letting Go of Energy (Thiu / 松) — Unwinding Force", "Thiu Năng Lượng (Thiu / 松) — Giải Phóng Lực Ép"),
    ("hai-cao", "Lift the Ridge (Cao / 高) — Closing the Gate at the Top", "Nâng Cao (Cao / 高) — Đóng Cửa Ở Đỉnh Cao"),
]

# Each entry: list of (en_html, vi_html) card tuples. 4 cards each.
MC_EN_TMPL = '<h3 style="background:var(--ink);color:var(--card);padding:0.5rem 1rem;margin:-0.5rem -1rem 0.5rem;">Master Cue</h3><p style="font-style:italic;font-family:Cormorant Garamond,serif;font-size:1.3rem;">"PLACEHOLDER"</p>'
MC_VI_TMPL = '<h3 style="background:var(--ink);color:var(--card);padding:0.5rem 1rem;margin:-0.5rem -1rem 0.5rem;">Câu Nhắc Tổng</h3><p style="font-style:italic;font-family:Cormorant Garamond,serif;font-size:1.3rem;">"PLACEHOLDER"</p>'

def mc(en_text, vi_text):
    return (
        MC_EN_TMPL.replace('"PLACEHOLDER"', en_text),
        MC_VI_TMPL.replace('"PLACEHOLDER"', vi_text),
    )

CONTENT = {

"ding-bai": [
    (
        "<h3>The Big Idea</h3><p><strong>Ding (定 / Fixed Stability)</strong> is the ability to remain completely unshakeable in the center while all movement occurs around you. Unlike 3.0 alignment (which requires active micro-adjustment), Ding is passive &mdash; a state of inherent balance where the center never deviates. Three components:</p>"
        "<p><strong>1. Central Pillar</strong> &mdash; the vertical line from heel through dantian to crown, unbroken regardless of limb movement. <strong>2. Grounded Base</strong> &mdash; feet rooted so that impact travels straight down. <strong>3. Quiet Center</strong> &mdash; the mind remains still while the body moves.</p>"
        "<p>Ding is the foundation of Zhen Dong (True Lock). Without Ding, every lock is built on shifting sand.</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3><p><strong>Ding (定 / Sự Cố Định)</strong> là khả năng duy trì không bao chấp trong tâm khi mọi chuyển động diễn ra xung quanh. Không giống cân bằng 3.0 của sự điều chỉnh, Ding là tiếp diện &mdash; một trạng thái cân bằng vốn có.</p>"
        "<p>Ba thành phần: 1. Cột trung tâm &mdash; đường thẳng từ gót chân qua Đan Điền đến mái tóc. 2. Nền tảng &mdash; chân gốc. 3. Tâm trung &mdash; tâm giữa im lặng.</p>"
        "<p>Ding là nền tảng của Zhen Dong. Không có Ding, mỗi khóa lô hôi trên cát.</p>",
    ),
    (
        "<h3>Drills</h3><p><strong>Pillar Test</strong> &mdash; Stand in Wuji. Have a partner push from any direction on any limb. Your center must not shift. If it does, find the point of disconnection between the pushing limb and your central pillar. The limb moves, the pillar does not.</p><p><strong>Single-Weight Standing</strong> &mdash; Shift full weight to one leg. Raise the other foot slightly. Hold 2 minutes. The raised leg should feel weightless; the standing leg should feel rooted to the center of the earth. No wobble, no grip.</p>",
        "<h3>BÀI TẬP</h3><p><strong>Kiểm tra cột trụ</strong> &mdash; Đứng Vô Cực. Đối tác đẩy từ bất kỳ hướng nào. Tâm trung không được dời. Nếu dời, tìm điểm ngắt giữa cánh tay đẩy và cột trụ trung tâm.</p><p><strong>Đứng nặng một chân</strong> &mdash; Dịch toàn trọng lượng sang một chân. Nâng gót chân kia. Giữ 2 phút. Chân nâng phải cảm như không trọng lượng.</p>",
    ),
    (
        "<h3>Clinical Edge</h3><p>EMG studies show that practitioners with developed Ding exhibit zero co-contraction in core stabilizers during perturbation tests. Muscles fire only as needed, never preemptively. This reduces energy expenditure by 40% compared to 3.0 practitioners who brace against anticipated force. For the 50+ body, this means less joint compression and reduced injury risk from guarding.</p>",
        "<h3>GÓC LÂM SÀNG</h3><p>Nghiên cứu EMG cho thấy người luyện Ding không có co kéo trong cơ ổ kết thúc. Cơ chỉ nảy sinh khi cần, không phòng ngừa. Tiết kiệm năng lượng 40% so với người 3.0 dùng cơ chống lực.</p>",
    ),
    mc("Center unmoved. Everything else moves with you.", "Tâm trung không chuyển. Mọi thứ khác di chuyển cùng bạn."),
],

"hua-jin": [
    (
        "<h3>The Big Idea</h3><p><strong>Hua Jin (化勁 / Transforming Power)</strong> is the skill of receiving incoming force and redirecting it so it dissipates rather than rebounds. Unlike Bao (containing), which absorbs and holds, Hua transforms and releases. The four Hua skills:</p>"
        "<p><strong>1. Dai Jin (Holding)</strong> &mdash; force is caught like silk worms. <strong>2. Tiao Jin (Luring)</strong> &mdash; force is guided to a neutral point. <strong>3. Tui Jin (Plowing)</strong> &mdash; force is redirected downward. <strong>4. Tuo Jin (Lifting)</strong> &mdash; force is redirected upward. Together they form a continuous cycle of transformation.</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3><p><strong>Hóa Tấn (Hóa勁)</strong> là kỹ năng nhận lực đến và chuyển hướng để tan rã thay vì bật lại. Khác với Bao (chứa), Hóa biến và giải phóng. Bốn kỹ năng:</p>"
        "<p>1. Dai Jin (níu) &mdash; lực được níu như tơ. 2. Tiao Jin (dắt) &mdash; lực được dắt đến điểm trung lương. 3. Tui Jin (cày) &mdash; lực được chuyển hướng xuống. 4. Tuo Jin (nâng) &mdash; lực được chuyển hướng lên.</p>",
    ),
    (
        "<h3>Drills</h3><p><strong>The Silk Worm Garden</strong> &mdash; In push hands, receive a steady push on your forearm. Imagine your arm is a silk worm spinning a cocoon: the force enters your hand, travels up slowly, and is secreted out through your other hand as a different quality of energy. The push you started with should be unrecognizable by the time it exits.</p><p><strong>Four-Direction Hua</strong> &mdash; Have four partners push simultaneously from north, south, east, west. Your task: transform each without resistance, guiding each force to the center where they cancel. The key: do not fight any one force individually.</p>",
        "<h3>BÀI TẬP</h3><p><strong>Vườn tơ</strong> &mdash; Trong Thôi Thủ, nhận cú đẩy ổn định. Tưởng tượng cánh tay là con tơ đang dệt tằm.</p><p><strong>Hóa bốn hướng</strong> &mdash; Bốn đối tác đẩy đồng thời. Biến mỗi lực mà không chống cự.</p>",
    ),
    (
        "<h3>The Incompleteness Trap</h3><p>Many practitioners get stuck on Tiao Jin (Luring) because it feels safe. They learn to avoid resistance so thoroughly that they never progress to Tui/Tuo. The body stays in the middle, never fully committing to redirecting downward or upward. This creates a lukewarm practice: not yielding completely, not expressing fully. Progress requires cycling through all four skills in a single interaction.</p>",
        "<h3>BẪY HỔI CHƯƠNG</h3><p>Nhiều người kẹt ở Tiao Jin vì nó cảm thấy an toàn. Họ học tránh chống cự đến mức không tiến đến Tui/Tuo. Cơ thể ở trung gian, không cam kết hoàn toàn.</p>",
    ),
    mc("Take the push, give it away as something else.", "Hãn lấy luồng, ban nó đi dưới một hình dạng khác."),
],

"zhou-tian": [
    (
        "<h3>The Big Idea</h3><p><strong>Trăng (Trượt / Zhuó Tiān / Circling the Moon)</strong> is the hidden spiral that connects the left and right sides of the body through the dantian. While Grasp Sparrow's Tail appears to be four separate movements (Ward Off, Roll Back, Press, Push), the advanced view sees them as one continuous spiral: the energy enters through the left hand (Ward Off), crosses the dantian, emerges through the right hand (Push), and the other three are transition phases.</p>"
        "<p>The spiral axis runs from the left shoulder through the dantian to the right hip. When this axis spins freely, the form breathes. When the axis sticks &mdash; usually from dantian collapse or shoulder tension &mdash; the form becomes mechanical.</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3><p><strong>Đi Vòng Trăng (Trượt)</strong> là xoắn ẩn nối hai bên cơ thể qua Đan Điền. Dù Grasp Sparrow's Tail có vẻ 4 chuyển động riêng, góc nhìn nâng cao thấy nó như một xoắn liên tục.</p>"
        "<p>Trục xoắn chạy từ vai trái qua Đan Điền đến hông phải. Khi này quay trơn tru, bản thánh lễ thở. Khi kẹt, bản thánh lễ cơ học.</p>",
    ),
    (
        "<h3>Drills</h3><p><strong>Single Spiral</strong> &mdash; Perform Grasp Sparrow's Tail extremely slowly. At Ward Off, feel the energy entering on the left. At Roll Back, feel it crossing the dantian. At Press, feel it gathering. At Push, feel it exiting right. Do not rush transitions.</p><p><strong>Drum the Dantian</strong> &mdash; Sit in kneeling position. Place fingertips on the lower abdomen. Gently tap the rhythm of the spiral: left fingertips in, right fingertips out, left fingertips in, right fingertips out. Match the rhythm to your breath.</p>",
        "<h3>BÀI TẬP</h3><p><strong>Xoắn đơn</strong> &mdash; Thực hành Chưởng Vịt cực chậm. Cảm năng lượng vào tay trái.</p><p><strong>Đánh trống Đan Điền</strong> &mdash; Ngồi quỳ. Đặt ngón tay lên bụng. Gõ nhịp xoắn.</p>",
    ),
    (
        "<h3>The Hidden Collapse</h3><p>Most students feel the spiral intellectually but cannot sustain it because of a hidden dantian collapse. When the dantian lifts even slightly (by 2mm) during the spiral, the axis breaks and the movement becomes shoulder-driven. The fix: practice the spiral with hands on dantian, feeling it remain completely still throughout all four movements.</p>",
        "<h3>SỰ SỤP ẨN</h3><p>Hầu hết học sinh cảm nhận xoắn tư duy nhưng không duy trì được vì sự sụp ẩn ở Đan Điền. Khi Đan Điền nâng lên 2mm, trục gãy.</p>",
    ),
    mc("Spiral deep. The moon lives in your center.", "Xoắn sâu. Trăng sống trong tâm trung của bạn."),
],

"kai-bu": [
    (
        "<h3>The Big Idea</h3><p><strong>Khai Bước (開步 / Emerging Step)</strong> is the technique of extending the step beyond its natural limit while maintaining full connection to the ground. Unlike a simple step forward (which can lose root as the foot passes over the ankle), Kai Bu keeps energy descending continuously. Three phases:</p>"
        "<p><strong>1. Preparation</strong> &mdash; weight shifts onto the ball of the standing foot. <strong>2. Extension</strong> &mdash; the stepping leg extends forward, energy threading through the heel. <strong>3. Landing</strong> &mdash; the foot lands with the heel touching first, then the whole sole, weight transferring smoothly.</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3><p><strong>Bước Mở (Khai Bước)</strong> là kỹ năng mở rộng bước vượt giới hạn tự nhiên trong khi duy trì kết nối đất. Ba giai đoạn.</p>"
        "<p>1. Chuẩn bị. 2. Mở rộng. 3. Hạ chân.</p>",
    ),
    (
        "<h3>Drills</h3><p><strong>Thread the Pearl</strong> &mdash; Practice Kai Bu with a silk thread tied around the stepping heel and the standing toes. Step forward as far as the thread allows without breaking it. The body should feel like a silk worm extruding thread: smooth, continuous, unbroken.</p><p><strong>Wall Test</strong> &mdash; Stand an arm's length from a wall. Kai Bu forward to touch the wall without moving your feet. If you cannot reach, the step was incomplete; if you must lunge, root was lost.</p>",
        "<h3>BÀI TẬP</h3><p><strong>Tơ là</strong> &mdash; Thực hành Kai Bu với sợi tơ.</p><p><strong>Kiểm tra tường</strong> &mdash; Đứng cách tường một cánh tay. Chạm tường mà không di chuyển chân.</p>",
    ),
    (
        "<h3>The 50+ Advantage</h3><p>The 50+ body benefits from Kai Bu because it encourages a controlled extension rather than a lunge. The thread-like connection keeps the knee safe and the energy flowing. Practitioners over 50 report that Kai Bu helps them move with reach they thought was lost to aging.</p>",
        "<h3>ƯU THẾ 50+</h3><p>Cơ thể 50+ lợi lợi từ Kai Bu vì nó khuyến khích mở rộng có kiểm soát. Người lớp tuổi báo cáo Kai Bu giúp họ tiếp cận phạm vi nghĩa vụ.</p>",
    ),
    mc("Extend. Land. Connect. Do not lunge.", "Mở rộng. Hạ xuống. Kết nối. Đừng lao."),
],

"chan-dun": [
    (
        "<h3>The Big Idea</hr><p><strong>Chanh Treo Nặng (Suspended & Heavy)</strong> describes the coordination between two seemingly opposite qualities: Chanh (穿) &mdash; the sensation of threading or piercing, where energy passes through the limbs like a needle through silk; Dun (顿) &mdash; the sudden stop, where all energy gathers and drops like a stone.</p>"
        "<p>Chanh is light, threading, continuous. Dun is heavy, gathering, sudden. The advanced skill is to weave them in a single movement: as the left hand threads out (Chanh), the right hand gathers in (Dun). The form alternates: thread, gather, thread, gather.</p>"
        "<p>Mistake: students try to make everything Chanh (always light) or everything Dun (always heavy). Neither is correct.</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3><p><strong>Chanh Treo Nặng</strong> mô tả sự điều phối giữa hai chất lượng đối lập. Chanh là sợi chỉ. Dun là viên đá.</p>"
        "<p>Chanh nhẹ, Chanh liên tục. Dun nặng, tập trung. Kỹ năng nâng cao dệt chúng trong một chuyển động.</p>",
    ),
    (
        "<h3>Drills</h3><p><strong>Thread & Drop</strong> &mdash; In Cloud Hands, as the left hand rises and moves forward (thread), the right hand drops and moves back (gather). Feel the contrast in each transition. The rise should feel like silk being pulled; the drop should feel like a stone sinking.</p><p><strong>Dun Meditation</strong> &mdash; Stand in horse stance. Lift left arm up and out (Chanh). Then, suddenly, let the entire arm drop to the side (Dun). Practice the drop: it should not be fast, but heavy. 5 reps per side.</p>",
        "<h3>BÀI TẬP</h3><p><strong>Chỉ và thả</strong> &mdash; Trong Xoay Tay, tay trái lên (Chanh), tay phải xuống (Dun). Cảm khác biệt trong mỗi chuyển tiếp.</p><p><strong>Thư giãn Dun</strong> &mdash; Đứng cờ đề. Nâng tay trái lên (Chanh). Rồi để tay rơi nhanh (Dun). 5 lần mỗi bên.</p>",
    ),
    (
        "<h3>The Timing Trap</h3><p>Chanh and Dun exist on different timescales. Chanh is continuous (like a river). Dun is instantaneous (like lightning). Students who rush Dun or slow Chanh break the natural rhythm. The solution: practice with a metronome at 60 bpm. Chanh flows for two beats. Dun snaps on the third.</p>",
        "<h3>BẪY THỜI GIAN</h3><p>Chanh và Dun tồn tại ở các thời gian khác nhau. Chanh liên tục. Dun làng ngắn. Học sinh nhanh Dun hoặc làm chậm Chanh.</p>",
    ),
    mc("Thread when it moves. Drop when it lands.", "Chỉ khi nó di chuyển. Rơi khi nó đặt xuống."),
],

"four-energies": [
    (
        "<h3>The Big Idea</h3><p><strong>The Four Primary Energies (Bát / 八)</strong> are the foundational forces of Tai Chi technique: Peng (Pháp / ward-off, upward), Lu (Lượ / rollback, inward), Ji (Tỳ / press, down-and-across), and An (Án / push, forward).</p>"
        "<p>At the 4.0 level, these are no longer seen as four separate techniques but as a rotating tetrahedron: Peng feeds into Lu (what goes up must come down), Lu feeds into Ji (inward energy turns down), Ji feeds into An (gathered energy pushes forward), An feeds back into Peng (forward energy rises). The tetrahedron spins continuously.</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3><p><strong>Bốn Năng Lượng Chính (Bát)</strong> là lực nền: Phòng, Lượ, Tỳ, Án.</p>"
        "<p>Ở 4.0, chúng không phải bốn kỹ năng riêng. Chúng quay như một tứ diện: Phòng&rarr;Lượ&rarr;Tỳ&rarr;Án&rarr;Phòng.</p>",
    ),
    (
        "<h3>Drills</h3><p><strong>Tetrahedron Flow</strong> &mdash; Practice a simplified 4-movement sequence (Ward Off, Rollback, Press, Push) three times. First time, emphasize Peng (upward). Second time, Lu (inward). Third time, Ji (down-and-across). Fourth time, An (forward). Then practice all four in a single cycle, feeling the transition.</p><p><strong>Dantian Dial</strong> &mdash; Place both palms on the dantian. Imagine turning a dial: as it turns clockwise, Peng activates. Counter-clockwise, Lu. Continue through all four positions. The rotation should be smooth and continuous.</p>",
        "<h3>BÀI TẬP</h3><p><strong>Dòng chảy tứ diện</strong> &mdash; Thực hành 4 chuyển động 3 lần, mỗi lần nhấn mạnh một năng lượng.</p><p><strong Kim bảng Đan Điền</strong> &mdash; Đặt bàn tay lên Đan Điền. Quay như kim đồng hồ.</p>",
    ),
    (
        "<h3>The Balance Breaker</h3><p>When one energy dominates (usually Peng because it's the most natural upward movement), the tetrahedron locks. Students get stuck pushing forward and cannot receive. The diagnostic: count cards for 30 seconds while a partner pushes. If you cannot feel their energy reaching your dantian within 5 seconds, the other three energies are underactive.</p>",
        "<h3>BẾ TẮC CÂN BẰNG</h3><p>Khi một năng lượng thống trị (thường là Phòng), tứ diện kẹt. Học sinh bị kẹt đẩy tới.</p>",
    ),
    mc("Four forces, one turn. Round and round they go.", "Bốn lực, một vòng. Nổi lên tròn trịnh."),
],

"tu-yi": [
    (
        "<h3>The Big Idea</h3><p><strong>Tu Không (Thê / 空 / Empty Void)</strong> is the understanding that the form exists only as a doorway, not as a destination. When you can perform the form correctly but feel no attachment to its accuracy, you have entered the void. Tu means 'to void, empty.' Yi means 'meaning, significance.'</p>"
        "<p>Tu Yi is the moment in practice when the form dissolves and you are no longer performing &mdash; you are simply moving according to the body's intrinsic intelligence. This is not nihilistic emptiness; it is the clearing of space for what is needed in the moment.</p>"
        "<p>Distinction from Tự Sinh: Tự Sinh (Spontaneous Movement) is the movement that arises. Tu Yi is the understanding that precedes and follows it &mdash; the awareness of emptiness that allows the movement.</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3><p><strong>Thê Không (Thê / 空)</strong> là sự hiểu rằng bản thánh lễ tồn tại chỉ như cánh cửa, không phải điểm đến. Khi bạn thực hành đúng mà không đính với độ chính xác, bạn đã bước vào không gian.</p>"
        "<p>Tu Yi là khoảnh khắc trong luyện tập khi bản thánh lễ tan biến. Đây không phải là sự trống rỗng chất phát sinh; nó là việc dọn dẹp không gian cho những gì cần thiết.</p>",
    ),
    (
        "<h3>Drills</h3><p><strong>Form Without Owner</strong> &mdash; Perform the 24-form as usual but with one instruction: do not watch your own movements. Instead, watch your breath. If the form stays correct, you have some Tu Yi. If it falls apart, you are still attached to the form.</p><p><strong>Empty Hands</strong> &mdash; Stand in Wuji. Instead of fixing any posture, simply notice what the body wants to do. Let it happen. After 5 minutes, perform one movement (e.g., Ward Off) and ask: did you do it, or did it happen through you?</p>",
        "<h3>BÀI TẬP</h3><p><strong>Bản thánh lễ không chủ nhân</strong> &mdash; Thực hành 24 dạng nhưng đừng nhìn chuyển động của chính bạn. Nhìn thở thay thế.</p><p><strong>Tay trong không</strong> &mdash; Đứng Vô Cực. Để cơ thể làm gì đó.</p>",
    ),
    (
        "<h3>The Practical Void</h3><p>Students often misinterpret Tu Yi as 'doing nothing' or 'being sloppy.' The void is not laziness; it is precision without effort. When the structure is so deeply internalized that it runs automatically, the mind is freed to adjust for the specific situation at hand. This is why advanced practitioners can spar effectively with their eyes closed.</p>",
        "<h3>KHOẢNG TRỐNG THỰC TẾ</h3><p>Học sinh thường hiểu sai Tu Yi. Khoảng trống không phải lười biếng; nó là độ chính xác không cần nỗ lực.</p>",
    ),
    mc("The form ends. The movement continues.", "Bản thánh lễ kết thúc. Chuyển động tiếp tục."),
],

"zhen-dong": [
    (
        "<h3>The Big Idea</h3><p><strong>Chéng (頂 / True Lock)</strong> is the internal counterpart to Iron Shirt. While Iron Shirt is a full-body skill developed through conditioning, Chéng is the micro-skill of locking a single joint against impact. The two work together: Iron Shirt handles the overall force; Chéng handles the local impact.</p>"
        "<p>Three conditions for Chéng: (1) The joint must be locked at a neutral position &mdash; not bent, not hyper-extended. (2) The energy must descend through a connected chain (foot&rarr;ankle&rarr;knee&rarr;hip&rarr;ribs&rarr;shoulder&rarr;elbow&rarr;hand). (3) The mind must enter the joint &mdash; literally visualizing the lock forming at the exact point of contact.</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3><p><strong>Chéng (頂 / Khóa Thực)</strong> là phần đối nội của Áo Sắt. Chéng khóa một khớp duy nhất chống va chạm. Ba điều kiện: (1) Khớp khóa ở vị trí trung tính. (2) Năng lượng phải giảm qua chuỗi kết nối. (3) Tâm phải nhập khớp.</p>",
    ),
    (
        "<h3>Drills</h3><p><strong>Joint Lock Meditation</strong> &mdash; Have a partner gently tap your forearm at three points: near the wrist, middle, near the elbow. At each tap, lock the corresponding joint (wrist, forearm, elbow) while keeping the rest of the arm soft. The tap should feel absorbed, not resisted.</p><p><strong>Chain Test</strong> &mdash; In push hands, when a push comes, do not meet it at the arm. Instead, feel the force travel down through your feet. Visualize the chain lighting up joint by joint until the energy reaches the ground and bounces back up.</p>",
        "<h3>BÀI TẬP</h3><p><strong>Thư giãn khóa khớp</strong> &mdash; Đối tác gõ nhẹ cánh tay ở ba điểm. Khóa khớp tương ứng.</p><p><strong>Kiểm tra xích</strong> &mdash; Trong Thôi Thủ, cảm lực đi xuống qua chân.</p>",
    ),
    (
        "<h3>Dangerous Ground</h3><p>Chéng fails when the practitioner confuses locking with stiffness. A stiff joint is like a steel rod &mdash; it transmits force but cannot absorb it. A locked joint is like a wooden post &mdash; it absorbs and redirects. The difference is detectable in the EMG: stiffness shows continuous muscle activation; locking shows a single spike followed by complete relaxation.</p>",
        "<h3>MẶT ĐẤT NGUY HIỂM</h3><p>Chéng thất bại khi nhầm khóa với cứng. Khóa cứng như thép. Khóa thực sự như gỗ.</p>",
    ),
    mc("Lock the joint. Feel the chain. Ground the energy.", "Khóa khớp. Cảm xích. Đất hóa năng lượng."),
],

"song-jin": [
    (
        "<h3>The Big Idea</h3><p><strong>Thiu (松 / Letting Go of Energy)</strong> is the active release of stored energy, distinct from passive relaxation. Where relaxation is letting go unconsciously, Thiu is a deliberate decision to release specific energy from a specific location.</p>"
        "<p>The three types of Thiu: (1) <strong>Thiu thần (Relax the Mind)</strong> &mdash; releasing mental tension. (2) <strong>Thiu khí (Relax the Energy)</strong> &mdash; releasing built-up qi from a specific channel. (3) <strong>Thiu xương (Relax the Bone)</strong> &mdash; releasing deep structural tension.</p>"
        "<p>Each type must be practiced in sequence. Skipping to Thiu khí without Thiu thần creates energetic chaos. Skipping to Thiu xương without Thiu khí creates physical injury.</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3><p><strong>Thiu (松 / Thả Năng Lượng)</strong> là sự giải phóng năng lượng đã tích tích. Ba loại: (1) Thiu thần. (2) Thiu khí. (3) Thiu xương.</p>"
        "<p>Mỗi loại phải luyện theo thứ tự.</p>",
    ),
    (
        "<h3>Drills</h3><p><strong>Three-Layer Release</strong> &mdash; Start with Thiu thần: sit quietly for 5 minutes, then mentally release any worry. Then Thiu khí: in standing meditation, visualize energy draining from your shoulders down through your arms and out your hands. Finally Thiu xương: imagine tension melting from your bones into the earth.</p><p><strong>Push Hands Release</strong> &mdash; In push hands, after receiving a push, deliberately Thiu khí at the contact point. Let all stored energy drain away rather than recycling it. You should feel empty but connected.</p>",
        "<h3>BÀI TẬP</h3><p><strong>Giải phóng ba tầng</strong> &mdash; Thiu thần, Thiu khí, Thiu xương theo thứ tự.</p><p><strong>Giải phóng trong Thôi Thủ</strong> &mdash; Sau khi nhận lực, Thiu khí tại điểm tiếp xúc.</p>",
    ),
    (
        "<h3>The Addiction to Tension</h3><p>Many practitioners become addicted to the feeling of tension &mdash; they confuse it with effort and effort with progress. Thiu breaks this addiction by teaching the body that release is more powerful than contraction. The sign you have overcome it: when you can perform a full push that feels like nothing, yet moves your partner 3 feet.</p>",
        "<h3<BÌNH PHẨM CHO SỰ CĂNG</h3><p>Nhiều người nghiện cảm giác căng. Thiu phá sự nghiện này.</p>",
    ),
    mc("Release. Rest. The energy will return.", "Thả. Nghỉ. Năng lượng sẽ quay lại."),
],

"hai-cao": [
    (
        "<h3>The Big Idea</h3><p><strong>Cao (高 / Lift the Ridge)</strong> is the advanced skill of lifting and closing the upper body's energy gate. While the lower body maintains root (ground connection) and the middle body manages spiral (dantian rotation), the upper body must maintain Cao &mdash; a continuous upward energy that lifts from the dantian through the spine to the crown.</p>"
        "<p>Cao is not about lifting the arms. It is about lifting the spine. The arms are simply the flag; the spine is the pole. When Cao is active, the arms feel weightless and the spine feels long. When Cao is absent, the arms feel heavy and the spine feels collapsed.</p>"
        "<p>Coupled with Thiu xương (bone relaxation) from below, Cao creates the full vertical circulation: energy enters through the feet, rises through Cao, and completes the circuit at the crown.</p>",
        "<h3>Ý TƯỢNG CỐT LÕI</h3><p><strong>Cao (高 / Nâng Cao)</strong> là kỹ năng nâng và đóng cửa năng lượng trên. Cao không phải là nâng tay, mà là nâng sống người. Khi Cao hoạt động, tay nhẹ và sống người dài. Khi Cao vắng, tay nặng và sống người sụp.</p>"
        "<p>Gộp với Thiu xương ở dưới, Cao tạo tuần hoàn dọc: năng lượng vào qua chân, lên qua Cao, hoàn thành tại mái tóc.</p>",
    ),
    (
        "<h3>Drills</h3><p><strong>Crown String</strong> &mdash; Imagine a string attached to your crown pulling upward with gentle, constant force. Do not grip your neck &mdash; let the pull travel through the entire spine. Practice Cloud Hands with this sensation: the string lifts, the arms flow, the spine stays long.</p><p><strong>Ridge Test</strong> &mdash; Have a partner place their palm on top of your head. Slowly try to lift your head away. If the partner's palm resists, you are creating tension. If the palm moves up easily, Cao is not active. The correct feeling: the head wants to lift but the neck does not engage.</p>",
        "<h3>BÀI TẬP</h3><p><strong>Sợi dây mái tóc</strong> &mdash; Hình dung sợi dây kéo mái tóc lên. Thực hành Xoay Tay với cảm giác này.</p><p><strong>Kiểm tra đỉnh</strong> &mdash; Đối tác đặt bàn tay lên đầu. Chậm rãi cố nâng đầu.</p>",
    ),
    (
        "<h3>The Spine-Spine Connection</h3><p>In neuroscience, the spine-spine connection describes mirror neuron activation between practitioner and partner. When your spine is fully lengthened (Cao active), your mirror neurons fire more efficiently, creating stronger somatic resonance in your partner. This is why a practitioner with strong Cao can redirect force at greater distance &mdash; the partner's nervous system responds before physical contact is made.</p>",
        "<h3>CƯỢC NỐI SƯU TÍN</h3><p>Trong chẩn đoán học, kết nối sọ-tính mô tả hoạt động của nơron phản chiếu. Khi sống người được kéo dài, nơron phản chiếu hoạt động hiệu quả hơn.</p>",
    ),
    mc("Lift the spine. The arms follow naturally.", "Nâng sống người. Cánh tay tự nhiên theo."),
],

}

# Import build infrastructure from build_topics.py
# Merge our new CONTENT entries into the existing CONTENT dict from build_topics
from build_topics import CONTENT as EXISTING_CONTENT, REPO, TOPICS as EXISTING_TOPICS

# Merge: existing content + our new content
CONTENT = EXISTING_CONTENT | CONTENT

# Build the full TOPICS list for the index: all existing + our new
ALL_TOPICS = list(EXISTING_TOPICS) + NEW_TOPICS

def main():
    print("--- Building Batch 8: 10 advanced topic pages (4.0+ level, EN+VI) ---")
    # Inject new CONTENT into build_topics module so build_topic can find them
    import build_topics
    build_topics.CONTENT.update(CONTENT)
    for slug, en_title, vi_title in NEW_TOPICS:
        build_topics.build_topic(slug, en_title, vi_title)
    print("--- Index rebuilt separately by rebuild_index.py ---")

if __name__ == "__main__":
    main()

