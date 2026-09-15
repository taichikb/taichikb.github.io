#!/usr/bin/env python3
"""Append the 4 missing batch-1 topics (peng, ji, an, xu-thuc) to enrich_topics_data.ALL_DATA."""
import sys
sys.path.insert(0, "D:/Taichi-Health-Finance/Intranet/taichikb_repo/scripts")

# Load existing
from enrich_topics_data import ALL_DATA

PENG = [
    (
        "<h3>When Peng Becomes Visible</h3>"
        "<p>Beginners often feel Peng as a vague &ldquo;ball&rdquo; but cannot demonstrate it. The transition from feeling to showing usually takes 2&ndash;3 months of daily practice. The visible signs: a partner pushes on your arm and your structure yields <em>slightly</em> before springing back; the arm looks soft but the foot is anchored; the breath is even; the eyes are calm. By contrast, a closed structure shows as rigid shoulders, lifted elbows, and a pushed-back stance with weight on the rear heel.</p>"
        "<p>Once visible, Peng becomes a diagnostic tool. If your structure starts to look rigid, you have left Peng and entered muscular holding. Return by releasing the shoulders, sinking the elbows, and re-grounding the feet.</p>",

        "<h3>Khi Nào Phòng Trở Nên Nhìn Thấy Được</h3>"
        "<p>Người mới thường cảm nhận Phòng như một &ldquo;quả cầu&rdquo; mơ hồ nhưng không thể thể hiện. Sự chuyển tiếp thường mất 2&ndash;3 tháng thực hành hằng ngày. Dấu hiệu nhìn thấy được: đối tác đẩy tay bạn và cấu trúc <em>hơi</em> nhườn trước khi bật lại; tay trông mềm nhưng chân neo chặt; hơi thở đều; mắt bình thản.</p>"
        "<p>Khi đã nhìn thấy được, Phòng trở thành công cụ chẩn đoán. Nếu cấu trúc bắt đầu trông cứng, bạn đã rời Phòng. Quay lại bằng cách thả vai, hạ khuỷu, và neo lại chân.</p>",
    ),
    (
        "<h3>Three Tests for Peng</h3>"
        "<ol>"
        "<li><strong>Solo test</strong>: stand in Wuji stance, raise the arms to shoulder height with palms down, and ask a partner to press a fingertip under each wrist <em>up</em>. The wrist should rise, not collapse.</li>"
        "<li><strong>Single-direction test</strong>: have a partner push on the shoulder from the side. The force should travel through your arm and into the back foot.</li>"
        "<li><strong>Multi-directional test</strong>: have a partner push from three directions in quick succession. The body should remain anchored and yield-and-return in each direction.</li>"
        "</ol>",

        "<h3>Ba Kiểm Tra Phòng</h3>"
        "<ol>"
        "<li><strong>Kiểm tra một mình</strong>: đứng tư thế Vô Cực, nâng tay ngang vai lòng bàn tay xuống, và nhờ đối tác ấn đầu ngón tay dưới mỗi cổ tay <em>lên</em>. Cổ tay nên nâng lên, không sụp.</li>"
        "<li><strong>Kiểm tra một hướng</strong>: nhờ đối tác đẩy vai từ bên. Lực nên đi qua cánh tay và vào chân sau.</li>"
        "<li><strong>Kiểm tra đa hướng</strong>: nhờ đối tác đẩy từ ba hướng nhanh liên tiếp. Cơ thể nên giữ neo và nhườn-trở-lại theo mỗi hướng.</li>"
        "</ol>",
    ),
]

JI = [
    (
        "<h3>Ji vs Press in External Arts</h3>"
        "<p>In an external martial art like boxing, a &ldquo;press&rdquo; is a chest-and-shoulder action: the upper body drives the arms forward. In Tai Chi, Ji is the <em>opposite sequence</em>: feet &rarr; legs &rarr; hips &rarr; waist &rarr; back &rarr; shoulders &rarr; arms &rarr; hands. The arms are the last thing to move.</p>"
        "<p>This is why Ji is so disorienting to receive. It does not arrive like a push (which the body can brace against). It arrives like a wave (which the body must absorb or yield to).</p>",

        "<h3>Tỳ vs Đẩy Trong Võ Thuật Ngoại</h3>"
        "<p>Trong võ thuật ngoại, &ldquo;đẩy&rdquo; là hành động ngực-vai: phần thân trên lái tay tới. Trong Thái Cực Quyền, Tỳ là <em>trình tự ngược lại</em>: chân &rarr; hông &rarr; eo &rarr; lưng &rarr; vai &rarr; tay &rarr; bàn tay.</p>"
        "<p>Đây là lý do Tỳ gây mất phương hướng cho người nhận. Nó không đến như cú đẩy (có thể chống lại); nó đến như con sóng (phải hấp thụ hoặc nhường).</p>",
    ),
    (
        "<h3>Common Errors in Ji</h3>"
        "<p><strong>Pressing with arms</strong>: tie the press to a forward step &mdash; if the step does not happen, the press does not. <strong>Pressing with upper back</strong>: lead with the dantian, not the shoulders. <strong>Pressing with held breath</strong>: exhale through the press; breath arriving with the press is the sign the body has organised around breath.</p>",

        "<h3>Lỗi Phổ Biến Trong Tỳ</h3>"
        "<p><strong>Ép bằng tay</strong>: buộc cú ép vào bước tới &mdash; nếu bước không xảy ra, cú ép không xảy ra. <strong>Ép bằng lưng trên</strong>: dẫn bằng Đan Điền, không phải vai. <strong>Ép với hơi thở bị giữ</strong>: thở ra qua cú ép.</p>",
    ),
]

AN = [
    (
        "<h3>An in Grasp Bird's Tail</h3>"
        "<p>An is rarely taught in isolation. It is the fourth movement of the Grasp Bird's Tail sequence &mdash; the most studied passage in the Yang form. The four movements (Peng, Lu, Ji, An) teach the full grammar of Tai Chi interaction: receive, redirect, compress, finish.</p>"
        "<p>When An is taught inside the sequence, students learn it is not a separate &ldquo;push&rdquo; but a <em>resolution</em>. The compression of Ji already contains An.</p>",

        "<h3>Án Trong Lãm Tước Vỹ</h3>"
        "<p>Án hiếm khi được dạy riêng lẻ. Đó là chuyển động thứ tư của Lãm Tước Vỹ &mdash; đoạn nghiên cứu nhiều nhất trong bài Dương. Bốn chuyển động (Phòng, Lỹ, Tỳ, Án) dạy ngữ pháp đầy đủ: tiếp nhận, chuyển hướng, nén, kết thúc.</p>"
        "<p>Khi Án được dạy trong chuỗi, học viên học rằng nó không phải cú đẩy riêng mà là <em>sự giải quyết</em>.</p>",
    ),
    (
        "<h3>An in Push Hands</h3>"
        "<p>Push hands internalises An. Two people in contact; one pushes; the other receives and eventually pushes back. The common error is the &ldquo;arm-push&rdquo;: pushing with arms instead of through the ground. The correct exchange uses the centre, not the contact point.</p>",

        "<h3>Án Trong Tôi Thủ</h3>"
        "<p>Tôi Thủ nội tâm hóa Án. Hai người tiếp xúc; một đẩy; người kia tiếp nhận rồi đẩy lại. Lỗi phổ biến là &ldquo;đẩy bằng tay&rdquo; thay vì qua mặt đất. Trao đổi đúng dùng trung tâm.</p>",
    ),
]

XU_THUC = [
    (
        "<h3>Xū/Shí Across the Five Styles</h3>"
        "<p>The handling of Xū/Shí varies by school. <strong>Chen</strong> uses large, low postures with visible weight shifts. <strong>Yang</strong> uses higher, more upright postures with subtler shifts. <strong>Wu</strong> emphasises compact, narrow steps. <strong>Wu (Hao)</strong> uses long, weighted steps with deep pauses. <strong>Sun</strong> uses high, mobile stances with frequent light-quick steps.</p>",

        "<h3>Hư/Thực Qua Năm Trường Phái</h3>"
        "<p>Cách xử lý Hư/Thực khác nhau theo trường phái. <strong>Trần</strong> dùng tư thế thấp rộng với chuyển trọng lượng nhìn thấy được. <strong>Dương</strong> dùng cao hơn với chuyển dịch tinh tế hơn. <strong>Ngô</strong> nhấn mạnh bước hẹp. <strong>Vũ</strong> dùng bước dài với dừng sâu. <strong>Tôn</strong> dùng tư thế cao, di động với bước nhẹ-nhanh.</p>",
    ),
    (
        "<h3>The Cost of Double-Loading</h3>"
        "<p>The body resists single full, single empty because both feet loaded feels <em>safer</em>. The nervous system prefers certainty; Xū/Shí requires tolerating momentary instability.</p>"
        "<p>The cost: joints carry double load; muscles grip continuously; nervous system stays engaged; energy dissipates. The student who masters Xū/Shí is buying back joint life, muscular relaxation, cognitive bandwidth, and energetic efficiency.</p>",

        "<h3>Chi Phí Của Song Tải</h3>"
        "<p>Cơ thể chống lại một thực, một hư vì cả hai chân chịu tải cảm thấy <em>an toàn hơn</em>. Hệ thần kinh thích sự chắc chắn; Hư/Thực đòi hỏi chịu đựng bất ổn tạm thời.</p>"
        "<p>Chi phí: khớp mang gấp đôi tải; cơ liên tục nắm; hệ thần kinh luôn gắn kết; năng lượng bị tiêu hao. Học viên thành thạo Hư/Thực mua lại tuổi thọ khớp, thư giãn cơ, băng thông nhận thức, hiệu quả năng lượng.</p>",
    ),
]

ALL_DATA["peng"] = PENG
ALL_DATA["ji"] = JI
ALL_DATA["an"] = AN
ALL_DATA["xu-thuc"] = XU_THUC

# Now write back
from pathlib import Path
data_file = Path("D:/Taichi-Health-Finance/Intranet/taichikb_repo/scripts/enrich_topics_data.py")
content = data_file.read_text(encoding="utf-8")

# Find the if __name__ block and insert before it
marker = 'if __name__ == "__main__":'
idx = content.find(marker)
if idx >= 0:
    # Build insertion: serialize the new entries
    new_entries = []
    for slug, entries in [("peng", PENG), ("ji", JI), ("an", AN), ("xu-thuc", XU_THUC)]:
        new_entries.append(f'\n# ---------- Batch-1 topics (appended) ----------\n')
        var = slug.upper().replace("-", "_")
        new_entries.append(f'{var} = [\n')
        for en, vi in entries:
            new_entries.append(f'    (\n')
            # Escape the HTML strings for Python repr
            en_esc = en.replace("'", "\\'").replace('"', '\\"')
            vi_esc = vi.replace("'", "\\'").replace('"', '\\"')
            new_entries.append(f'        "{en_esc}"\n')
            new_entries.append(f'        "{vi_esc}"\n')
            new_entries.append(f'    ),\n')
        new_entries.append(f']\n\n')
        new_entries.append(f'ALL_DATA["{slug}"] = {var}\n')

    insertion = "".join(new_entries)
    new_content = content[:idx] + insertion + "\n" + content[idx:]
    data_file.write_text(new_content, encoding="utf-8")
    print(f"wrote {len(ALL_DATA)} topics to data file")
else:
    print("ERROR: marker not found")
