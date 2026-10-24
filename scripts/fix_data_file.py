#!/usr/bin/env python3
"""Build a clean enrich_topics_data.py from the working batch-2/3 data + add batch-1."""
import sys
from pathlib import Path

src = Path("D:/Taichi-Health-Finance/Intranet/taichikb_repo/scripts/enrich_topics_data.py")

# Step 1: extract the working parts (batch-2/3 list definitions)
# We know they're the top-level names: SUNG, SUNG_VS_SUI, ..., CO_THE_50_CONG_CU
BATCH23_NAMES = [
    "SUNG", "SUNG_VS_SUI", "YI_DAN_KHI", "MUSHIN", "OM_THU",
    "CHAM_LA_NHANH", "TAN_HU_TAN_THUC", "NGHICH_THO", "NAM_PHUT_TRU_THE",
    "BAI_30_PHUT", "CO_THE_SAU_50", "BA_DIEU_KIEN_CHUA_LANH",
    "TAP_20_PHUT_TAI_NHA", "RESET_5_PHUT", "BAY_SAI_LAM",
    "NGHICH_LY_CANG", "TAICHI_LA_GI", "TAM_BAO", "AM_DUONG",
    "SO_DO_CO_THE", "VO_VI_TRU_THE", "LAY", "TWENTY_FOUR_THUC_TONG_QUAT",
    "THO_DAN_DIEN", "BA_MO_NEO", "CO_THE_50_CONG_CU",
]

# Load the existing file as a module to extract the names
import importlib.util
spec = importlib.util.spec_from_file_location("old_data", src)
# The module fails to load because ALL_DATA is broken. We need raw text extraction.
text = src.read_text(encoding="utf-8")

# Extract each batch-2/3 list by regex: find the definition and copy until the matching `]`
import re
extracted = {}
for name in BATCH23_NAMES:
    # Find: ^NAME = [
    m = re.search(rf'^{name} = \[', text, re.MULTILINE)
    if not m:
        print(f"  WARN: {name} not found")
        continue
    # Find the matching `]`
    start = m.end()
    depth = 1  # we're inside [...]
    i = start
    while i < len(text) and depth > 0:
        c = text[i]
        if c == '[':
            depth += 1
        elif c == ']':
            depth -= 1
        i += 1
    body = text[m.start():i]  # includes opening "NAME = [" and closing "]"
    extracted[name] = body
    print(f"  extracted {name}: {len(body)} chars")

# Step 2: write a brand-new data file with proper structure
print(f"\n--- building new data file ---")
new_lines = []
new_lines.append('#!/usr/bin/env python3')
new_lines.append('"""Enrichment content for all 30 topics.')
new_lines.append('')
new_lines.append('Each entry: list of (en_html_card, vi_html_card) tuples.')
new_lines.append('Cards get inserted before the existing master-cue section in each page.')
new_lines.append('"""')
new_lines.append('')

# Add batch-2/3 lists verbatim
for name in BATCH23_NAMES:
    if name in extracted:
        new_lines.append('')
        new_lines.append(extracted[name])
        new_lines.append('')

# Batch-1 entries (peng/ji/an/xu-thuc) - clean source strings
BATCH1 = {
    "peng": [
        (
            "<h3>When Peng Becomes Visible</h3>"
            "<p>Beginners often feel Peng as a vague &ldquo;ball&rdquo; but cannot demonstrate it. The transition from feeling to showing usually takes 2&ndash;3 months of daily practice. The visible signs: a partner pushes on your arm and your structure yields <em>slightly</em> before springing back; the arm looks soft but the foot is anchored; the breath is even; the eyes are calm.</p>"
            "<p>Once visible, Peng becomes a diagnostic tool. If your structure starts to look rigid, you have left Peng and entered muscular holding. Return by releasing the shoulders, sinking the elbows, and re-grounding the feet.</p>",
            "<h3>Khi Nào Phòng Trở Nên Nhìn Thấy Được</h3>"
            "<p>Người mới thường cảm nhận Phòng như một &ldquo;quả cầu&rdquo; mơ hồ nhưng không thể thể hiện. Sự chuyển tiếp thường mất 2&ndash;3 tháng thực hành hằng ngày. Dấu hiệu nhìn thấy được: đối tác đẩy tay bạn và cấu trúc <em>hơi</em> nhườn trước khi bật lại; tay trông mềm nhưng chân neo chặt; hơi thở đều; mắt bình thản.</p>"
            "<p>Khi đã nhìn thấy được, Phòng trở thành công cụ chẩn đoán. Nếu cấu trúc bắt đầu trông cứng, bạn đã rời Phòng. Quay lại bằng cách thả vai, hạ khuỷu, và neo lại chân.</p>",
        ),
        (
            "<h3>Three Tests for Peng</h3>"
            "<ol><li><strong>Solo test</strong>: stand in Wuji stance, raise arms to shoulder height with palms down, ask a partner to press a fingertip under each wrist <em>up</em>. The wrist should rise, not collapse.</li>"
            "<li><strong>Single-direction test</strong>: have a partner push the shoulder from the side. Force should travel through your arm into the back foot.</li>"
            "<li><strong>Multi-directional test</strong>: have a partner push from three directions in quick succession. The body should remain anchored.</li></ol>",
            "<h3>Ba Kiểm Tra Phòng</h3>"
            "<ol><li><strong>Một mình</strong>: đứng Vô Cực, nâng tay ngang vai lòng xuống, nhờ đối tác ấn ngón tay dưới cổ tay <em>lên</em>. Cổ tay nên nâng, không sụp.</li>"
            "<li><strong>Một hướng</strong>: đối tác đẩy vai từ bên. Lực nên đi qua cánh tay vào chân sau.</li>"
            "<li><strong>Đa hướng</strong>: đối tác đẩy ba hướng nhanh. Cơ thể nên giữ neo.</li></ol>",
        ),
    ],
    "ji": [
        (
            "<h3>Ji vs Press in External Arts</h3>"
            "<p>In boxing, a &ldquo;press&rdquo; is a chest-and-shoulder action: the upper body drives the arms forward. In Tai Chi, Ji is the <em>opposite sequence</em>: feet &rarr; legs &rarr; hips &rarr; waist &rarr; back &rarr; shoulders &rarr; arms &rarr; hands. The arms are the last thing to move.</p>"
            "<p>This is why Ji is so disorienting to receive. It does not arrive like a push (which the body can brace against). It arrives like a wave (which the body must absorb or yield to).</p>",
            "<h3>Tỳ vs Đẩy Trong Võ Thuật Ngoại</h3>"
            "<p>Trong boxing, &ldquo;đẩy&rdquo; là hành động ngực-vai: thân trên lái tay tới. Trong Thái Cực Quyền, Tỳ là <em>trình tự ngược lại</em>: chân &rarr; hông &rarr; eo &rarr; lưng &rarr; vai &rarr; tay &rarr; bàn tay.</p>"
            "<p>Đây là lý do Tỳ gây mất phương hướng cho người nhận. Nó không đến như cú đẩy (chống lại được); nó đến như con sóng (phải hấp thụ).</p>",
        ),
        (
            "<h3>Common Errors in Ji</h3>"
            "<p><strong>Pressing with arms</strong>: tie the press to a forward step &mdash; if the step does not happen, the press does not. <strong>Pressing with upper back</strong>: lead with the dantian, not the shoulders. <strong>Pressing with held breath</strong>: exhale through the press.</p>",
            "<h3>Lỗi Phổ Biến Trong Tỳ</h3>"
            "<p><strong>Ép bằng tay</strong>: buộc cú ép vào bước tới. <strong>Ép bằng lưng trên</strong>: dẫn bằng Đan Điền. <strong>Ép với hơi thở bị giữ</strong>: thở ra qua cú ép.</p>",
        ),
    ],
    "an": [
        (
            "<h3>An in Grasp Bird's Tail</h3>"
            "<p>An is rarely taught in isolation. It is the fourth movement of the Grasp Bird's Tail sequence &mdash; the most studied passage in the Yang form. The four movements (Peng, Lu, Ji, An) teach the full grammar of Tai Chi interaction: receive, redirect, compress, finish.</p>"
            "<p>When An is taught inside the sequence, students learn it is not a separate &ldquo;push&rdquo; but a <em>resolution</em>. The compression of Ji already contains An.</p>",
            "<h3>Án Trong Lãm Tước Vỹ</h3>"
            "<p>Án hiếm khi được dạy riêng. Đó là chuyển động thứ tư của Lãm Tước Vỹ &mdash; đoạn nghiên cứu nhiều nhất trong bài Dương. Bốn chuyển động (Phòng, Lỹ, Tỳ, Án) dạy ngữ pháp: tiếp nhận, chuyển hướng, nén, kết thúc.</p>"
            "<p>Khi Án được dạy trong chuỗi, học viên học rằng nó không phải cú đẩy riêng mà là <em>sự giải quyết</em>.</p>",
        ),
        (
            "<h3>An in Push Hands</h3>"
            "<p>Push hands internalises An. Two people in contact; one pushes; the other receives and eventually pushes back. The common error is the &ldquo;arm-push&rdquo;: pushing with arms instead of through the ground. The correct exchange uses the centre, not the contact point.</p>",
            "<h3>Án Trong Tôi Thủ</h3>"
            "<p>Tôi Thủ nội tâm hóa Án. Hai người tiếp xúc; một đẩy; người kia tiếp nhận rồi đẩy lại. Lỗi phổ biến là &ldquo;đẩy bằng tay&rdquo; thay vì qua mặt đất. Trao đổi đúng dùng trung tâm.</p>",
        ),
    ],
    "xu-thuc": [
        (
            "<h3>Xū/Shí Across the Five Styles</h3>"
            "<p><strong>Chen</strong> uses large, low postures with visible weight shifts. <strong>Yang</strong> uses higher, more upright postures with subtler shifts. <strong>Wu</strong> emphasises compact, narrow steps. <strong>Wu (Hao)</strong> uses long, weighted steps with deep pauses. <strong>Sun</strong> uses high, mobile stances with frequent light-quick steps.</p>",
            "<h3>Hư/Thực Qua Năm Trường Phái</h3>"
            "<p><strong>Trần</strong> dùng tư thế thấp rộng với chuyển trọng lượng nhìn thấy. <strong>Dương</strong> dùng cao hơn với chuyển dịch tinh tế. <strong>Ngô</strong> nhấn mạnh bước hẹp. <strong>Vũ</strong> dùng bước dài với dừng sâu. <strong>Tôn</strong> dùng tư thế cao, di động với bước nhẹ-nhanh.</p>",
        ),
        (
            "<h3>The Cost of Double-Loading</h3>"
            "<p>The body resists single full, single empty because both feet loaded feels <em>safer</em>. The nervous system prefers certainty; Xū/Shí requires tolerating momentary instability.</p>"
            "<p>The cost: joints carry double load; muscles grip continuously; nervous system stays engaged; energy dissipates. The student who masters Xū/Shí is buying back joint life, muscular relaxation, cognitive bandwidth, and energetic efficiency.</p>",
            "<h3>Chi Phí Của Song Tải</h3>"
            "<p>Cơ thể chống lại một thực, một hư vì cả hai chân chịu tải cảm thấy <em>an toàn hơn</em>. Hệ thần kinh thích chắc chắn; Hư/Thực đòi hỏi chịu đựng bất ổn tạm thời.</p>"
            "<p>Chi phí: khớp mang gấp đôi tải; cơ liên tục nắm; hệ thần kinh luôn gắn kết; năng lượng bị tiêu hao. Học viên thành thạo Hư/Thực mua lại tuổi thọ khớp, thư giãn cơ, băng thông nhận thức, hiệu quả năng lượng.</p>",
        ),
    ],
}

# Append batch-1 lists using Python literal serialization
for slug, entries in BATCH1.items():
    new_lines.append(f'{slug.upper().replace("-", "_")} = [')
    for en, vi in entries:
        new_lines.append(f'    (')
        new_lines.append(f'        {en!r},')
        new_lines.append(f'        {vi!r},')
        new_lines.append(f'    ),')
    new_lines.append(f']')
    new_lines.append('')

# Build the ALL_DATA dict with all 30 entries
new_lines.append('')
new_lines.append('ALL_DATA = {')
all_keys = []
all_keys.extend(["peng", "ji", "an", "xu-thuc"])
all_keys.extend([
    "sung", "sung-vs-sui", "yi-dan-khi", "mushin", "om-thu",
    "cham-la-nhanh", "tan-hu-tan-thuc", "nghich-tho", "nam-phut-tru-the",
    "bai-30-phut", "co-the-sau-50", "ba-dieu-kien-chua-lanh",
    "tap-20-phut-tai-nha", "reset-5-phut", "bay-sai-lam",
    "nghich-ly-cang", "taichi-la-gi", "tam-bao", "am-duong",
    "so-do-co-the", "vo-vi-tru-the", "lay", "24-thuc-tong-quat",
    "tho-dan-dien", "ba-mo-neo", "co-the-50-cong-cu",
])

# Slug -> Python-valid variable name mapping (for slugs whose original
# extracted name didn't match the upper-cased slug form, e.g. those starting
# with a digit)
VAR_NAMES = {
    "24-thuc-tong-quat": "TWENTY_FOUR_THUC_TONG_QUAT",
}

def var_for(slug):
    return VAR_NAMES.get(slug, slug.upper().replace("-", "_"))

for i, k in enumerate(all_keys):
    sep = "," if i < len(all_keys) - 1 else ""
    new_lines.append(f'    "{k}": {var_for(k)}{sep}')
new_lines.append('}')
new_lines.append('')
new_lines.append('if __name__ == "__main__":')
new_lines.append('    print(f"Topics with enrichment data: {len(ALL_DATA)}")')

new_content = "\n".join(new_lines)
src.write_text(new_content, encoding="utf-8")
print(f"\nwrote {len(new_content)} chars")
print(f"topics in new file: {len(all_keys)}")

# Verify
sys.path.insert(0, str(src.parent))
# Force re-import
if 'enrich_topics_data' in sys.modules:
    del sys.modules['enrich_topics_data']
import enrich_topics_data as etd
print(f"verified: ALL_DATA has {len(etd.ALL_DATA)} topics")
for slug in ("peng", "ji", "an", "xu-thuc", "sung"):
    entries = etd.ALL_DATA.get(slug, [])
    print(f"  {slug}: {len(entries)} entries, first has {len(entries[0][0]) if entries else 0} chars")
