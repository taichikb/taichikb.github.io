#!/usr/bin/env python3
"""Rebuild the techniques index pages (EN + VI) from the TOPICS list.

The TOPICS list is gathered from build_topics.py + Batches 5-8 + any other
sources to ensure all 70 topics appear in the index without duplicates.

Usage: python scripts/rebuild_index.py
"""
from pathlib import Path
import re

REPO = Path("D:/Taichi-Health-Finance/Intranet/taichikb_repo")

# Full topic list: (slug, en_title, vi_title) — all 70 topics
ALL_TOPICS = [
    # Original 30 (from build_topics.py)
    ("peng", "Ward Off (Peng / 掤) — First Line of Defense", "Phòng (Phòng / 掤) — Đường Phòng Thứ Nhất"),
    ("ji", "Squeeze (Ji / 挤) — The Hidden Pull", "Tỳ (Tỳ / 挤) — Sức Kéo Đâu"),
    ("an", "Push (An / 按) — The Grounding Force", "Án (Án / 按) — Lực Đặt Đất"),
    ("xu-thuc", "Crossing the Threshold (Xu Thúc / 出阀) — The Moment of Entry", "Xu Thúc (Xu Thúc / 出阡) — Khoảnh Khắc Bước Vào"),
    ("sung", "Relaxed Power (Sung / 松) — Power Without Tension", "Sung (Sung / 松) — Sức Mạnh Không Căng"),
    ("sung-vs-sui", "Sung vs Sui (Sung vs Sui) — The Two Ways of Letting Go", "Sung vs Sui — Hai Cách Buông"),
    ("yi-dan-khi", "Breath and Energy (Ý Dĩ Khí / 意气) — Mind-Driven Breath", "Ý Dĩ Khí — Hơi Thở Do Tâm"),
    ("mushin", "No-Mind (Vô Tâm / 無心) — Moving Without Mental Interference", "Vô Tâm — Chuyển Động Không Can Thiệp"),
    ("om-thu", "Embrace the Pillow (Ôm Thù / 抱柄) — Yielding as Structure", "Ôm Thù — Sự Khuần Khái Như Cấu Trúc"),
    ("cham-la-nhanh", "Slow is Fast (Chậm Là Nhanh) — The Speed-Building Paradox", "Chậm Là Nhanh — Nhiễn Thuyền Tốc Độ"),
    ("tan-hu-tan-thuc", "Empty/Full Transition (Tản Hư Tạo Thực) — From Void to Reality", "Tan Hư Tạo Thực — Từ Không Sang Thực"),
    ("nghich-tho", "Counter-Breathing (Nghịch Hơi) — Breath Coordination Under Pressure", "Hơi Thở Ngược — Điều Phối Dưới Áp Lực"),
    ("nam-phut-tru-the", "Body Compression (Nam Pháp Tru Diệu) — Finding Space in Crowds", "Nén Cơ Thể — Tìm Không Gian Trong Đám Đông"),
    ("bai-30-phut", "30-Minute Form (Bài 30 Phút) — The Compressed Curriculum", "Bản Thánh Lễ 30 Phút"),
    ("co-the-sau-50", "50-Year-Old Practice (Cơ Thể Sau 50) — Adapted Movement", "Cơ Thể Sau 50 — Chuyển Động Thích Ứng"),
    ("ba-dieu-kien-chua-lanh", "Three Principals (Ba Điều Kiện) — The Prerequisites of Root", "Ba Điều Kiện — Tiên Quyết Của Nền Tảng"),
    ("tap-20-phut-tai-nha", "20-Minute Home Practice (Tập 20 Phút) — Micro-Sessions", "Tập 20 Phút Tại Nhà"),
    ("reset-5-phut", "5-Minute Reset (Reset 5 Phút) — Recovery from Desk Work", "Reset 5 Phút — Hồi Phục Từ Làm Văn Phòng"),
    ("bay-sai-lam", "Seven-Layer Adjustment (Bảy Sai Lầm) — Common Breakdown Points", "Bảy Sai Lầm"),
    ("nghich-ly-cang", "Counter-Principle (Nghịch Lý Cang) — Why Opposite Thinking Works", "Nghịch Lý Cang"),
    ("taichi-la-gi", "What is Taiji (Thái Cực Là Gì) — Foundational Understanding", "Thái Cực Là Gì"),
    ("tam-bao", "Three Treasures (Tam Bảo) — Jing, Qi, Shen", "Tam Bảo"),
    ("am-duong", "Yin-Yang (Âm Dương) — The Dynamic Balance", "Âm Dương"),
    ("so-do-co-the", "Body Map (Sơ Đồ Cơ Thể) — Joint-by-Joint Awareness", "Bản Đồ Cơ Thể"),
    ("vo-vi-tru-the", "Empty/Full Body (Vô Vi Trụ Thể) — The Embodied Paradox", "Thân Thể Vô Vi"),
    ("lay", "Shaking (Lay / Lắắng?) — Drilling Out Stagnation", "Rung Lên — Hối Thanh Tắc"),
    ("24-thuc-tong-quat", "Twenty-Four Forms Overview (24 Thái Cực) — The Complete Path", "Tổng Quan 24 Thái Cực"),
    ("tho-dan-dien", "Target Point (Thọ Điểm) — Energy Mapping", "Thọ Điểm"),
    ("ba-mo-neo", "Three-Movement Foundation (Ba Mở Neo) — The Core Alignment", "Ba Mở Neo"),
    ("co-the-50-cong-cu", "50 Tools (Công Cụ) — Daily Body Maintenance", "50 Công Cụ"),
    # Batch 5 (10 intermediate)
    ("san-shou", "San Shou (Sáng / 散手) — Free-Hand Applications", "Sáng (Sáng / 散手) — Kỹ Năng Tự Do"),
    ("dien", "Brush Knee (Diân / 剪) — The Universal Adjustment", "Diân — Sự Điều Chỉnh Vạn Năng"),
    ("xie-bu", "Twist Step (Quay / 轉) — Redirecting Power Through the Waist", "Xoay Bước (Xoay / 轉) — Điều Hướng Qua Eo"),
    ("kai-gong", "Rowing the Chariot (Khai Gôn / 開功) — The First Real Alignment", "Chèo Xe (Khai Gôn / 開功) — Sự Căn Bản Thực Sự"),
    ("tu-hu", "Lifting the Paten (Tô Hô) — Supporting the Unsupported", "Nâng Tô Hô — Hỗ Trợ Những Gì Không Được Hỗ Trợ"),
    ("hoa-buoc", "Flowing Steps (Hoa Bước / 化步) — Neutral, Not Passive", "Hoa Bước (Hoa Bước / 化步) — Trung Lương, Không Phải Thụ Động"),
    ("ba-hoi", "Opening Eight Directions (Bát Hướng) — Structure Before Reach", "Mở Tám Phương (Bát Hướng) — Cấu Trúc Trước Khi Tới"),
    ("thieu-hai", "Grasp Sparrow's Tail Summary — The Four Gates at a Glance", "Tóm Tắt Chưởng Tịch — Bốn Cửa Tại Một Nhìn"),
    ("shou-ba", "Guardian Posture (Thủ Bát Bảo) — Protecting Your Center", "Thủ Bát Bảo — Bảo Vệ Trung Tâm"),
    ("nghich-buoc", "Counter-Step (Nghịch Bước / 逆步) — Adhere, Stick, and Yield", "Bước Ngược (Nghịch Bước / 逆步) — Dính, Dán, Nhường"),
    # Batch 6 (10 advanced)
    ("chan-si-jin", "Silk Reeling Energy (Chan Si Jin / 缠丝劲) — The Spiral of Integrated Power", "Năng Lượng Xoắn Tơ (Chan Si Jin / 缠丝劲)"),
    ("wu-wei", "Wu Wei (Vô Vi / 无为) — The Art of Non-Action in Motion", "Vô Vi (Vô Vi / 无为) — Nghệ Thuật Hành Động Không Hành Động"),
    ("dantian", "The Dantian (Đan Điền / 丹田) — The Powerhouse Below the Navel", "Đan Điền (Đan Điền / 丹田) — Trung Tâm Năng Lượng Dưới Bụng"),
    ("fa-jin", "Fa Jin (Phá Tấn / 发劲) — Explosive Power Without Muscle", "Phá Tấn (Phá Tấn / 发劲) — Sức Mạnh Bùng Nổ Không Cơ Bắp"),
    ("ting-jin", "Listening Energy (Ting Jin / 听劲) — The Skill of Feeling Before Moving", "Năng Lượng Lắng Nghe (Ting Jin / 听劲) — Kỹ Năng Cảm Thấy Trước Khi Di Chuyển"),
    ("iron-shirt", "Iron Shirt (Cuồn Não / 铜人) — Conditioning for Impact Absorption", "Áo Sắt (Cuồn Não / 铜人) — Rèn Luyện Hấp Thụ Va Chạm"),
    ("yin-yang-loop", "The Yin-Yang Energy Loop (Âm Dương Tuần Hoàn) — Circular Power", "Vòng Tròn Năng Lượng Âm Dương — Sức Mạnh Hình Tròn"),
    ("zhong-ning", "Central Equilibrium (Trung Nghị / 中定) — The Middle Way of Balance", "Trung Nghị (Trung Nghị / 中定) — Con Đường Trung Lương Của Sự Cân Bằng"),
    ("ou-mo", "Embrace the Pot (Ôm Nồi / 抱磨) — Full Circle Connection", "Ôm Nồi (Ôm Nồi / 抱磨) — Kết Nối Đầy Đủ Vòng Tròn"),
    ("breath-channels", "Breath & Energy Channels (Hô Hấp Và Kênh Khí) — The Internal Highway", "Hơi Thở Và Kênh Khí — Xa Lộ Nội Tâm"),
    # Batch 7 (10 advanced)
    ("liu-jia", "Six Harmonies (Lục Hợp / 六合) — The Six-Way Integration", "Lục Hợp (六合) — Sự Hòa Nhất Sáu Cách"),
    ("wu-xing", "Five Elements (Ngũ Hành / 五行) — Cycles of Energetic Transformation", "Ngũ Hành (五行) — Những Vòng Biến Đổi Năng Lượng"),
    ("ba-gua", "Eight Trigrams (Bát Quái / 八卦) — Mapping Internal Directions", "Bát Quái (八卦) — Bản Đồ Các Hướng Nội Tại"),
    ("song-shen", "Collapse (Sụp / 塌) — The Deliberate Surrender Into Structure", "Sụp (Sụp / 塌) — Sự Đầu Hàng Có Chủ Đích Vào Cấu Trúc"),
    ("yin-yang-harmony", "Yin-Yang Integration (Âm Dương Hòa Nhất) — The Neutral Zone", "Âm Dương Hòa Nhất — Vùng Trung Lương"),
    ("root-suspend", "Root & Suspend (Neo & Treo) — The Dual Anchors of Structural Integrity", "Neo & Treo — Hai Mỏ Neo Toàn Thể Cấu Trúc"),
    ("silk-reeling-drills", "Advanced Silk-Reeling Drills (Chan Si Jin Nâng Cao)", "Bài Tập Xoắn Tơ Nâng Cao (Chan Si Jin Nâng Cao)"),
    ("spontaneous-movement", "Spontaneous Movement (Tự Sinh / 自生) — When Form Dissolves", "Chuyển Động Tự Sinh (Tự Sinh / 自生) — Khi Hình Thái Tan Rã"),
    ("merging-skill", "Merging Energy (Hòa Nhập / 合并) — Becoming One with the Push", "Hòa Nhập (Hòa Nhập / 合并) — Trở Thành Một Với Lực Ép"),
    ("ground-path", "The Ground Path (Đường Đất) — Full-Circle Force Transmission", "Đường Đất — Truyền Lực Qua Vòng Tròn Hoàn Chỉnh"),
    # Batch 8 (10 advanced 4.0+)
    ("ding-bai", "Fixed Stability (Ding / 定) — Unshakeable Center", "Sự Cố Định (Ding / 定) — Tâm Hồn Bất Động"),
    ("hua-jin", "Hua Jin (Hóa Tấn / 化勁) — Transforming Power Into Neutralization", "Hóa Tấn (Hóa / 化勁) — Biến Đổi Lực Thành Trung Hòa"),
    ("zhou-tian", "Circling the Moon (Trăng / 月) — The Hidden Spiral in Grasp Sparrow's Tail", "Đi Vòng Trăng (Trăng / 月) — Xoắn Ẩn Trong Chưởng Vịt"),
    ("kai-bu", "Emerging Step (Khai Bước / 開步) — Mechanics of the Expanding Stance", "Bước Mở (Khai Bước / 開步) — Cơ học của Thế Mở Rộng"),
    ("chan-dun", "Suspended & Heavy (Chanh / 穿) — Coordinating Lightness and Weight", "Chanh Treo Nặng — Điều Phối Ánh Nhẹ Với Trọng Lượng"),
    ("four-energies", "The Four Primary Energies (Pháp / 八) — Peng, Lu, Ji, An as Unified Skill", "Bốn Năng Lượng Chính (Pháp / 八) — Phòng, Lượ, Tỳ, Án Như Một"),
    ("tu-yi", "Empty Void (Thê / 空) — The Meaning Beyond Form", "Thê Không (Thê / 空) — Nghĩa Vượt Mẫu Hình"),
    ("zhen-dong", "True Lock (Chéng / 頂) — Internal Iron Shirt Against Impact", "Chéng Thực (Chéng / 頂) — Áo Sắt Nội Tại Chống Va Chạm"),
    ("song-jin", "Letting Go of Energy (Thiu / 松) — Unwinding Force", "Thiu Năng Lượng (Thiu / 松) — Giải Phóng Lực Ép"),
    ("hai-cao", "Lift the Ridge (Cao / 高) — Closing the Gate at the Top", "Nâng Cao (Cao / 高) — Đóng Cửa Ở Đỉnh Cao"),
]


def build_index_page(lang, topics_list, title_en, title_vi, desc_en, desc_vi):
    cards = "\n".join(
        f'        <div class="technique-card"><h3><a href="/{lang}/techniques/{slug}/">{en_t if lang=="en" else vi_t}</a></h3></div>'
        for slug, en_t, vi_t in topics_list
    )
    return f'''{desc_en if lang=="en" else desc_vi}

    <section id="topics" class="technique-section">
        <h2>{title_en if lang=="en" else title_vi}</h2>
        <p style="color:var(--gray-mid); font-style:italic;">{desc_en if lang=="en" else desc_vi}</p>
{cards}
    </section>
'''


def main():
    en_idx = REPO / "en" / "techniques" / "index.html"
    vi_idx = REPO / "vi" / "techniques" / "index.html"

    # Build index pages
    en_block = build_index_page("en", ALL_TOPICS,
        "New Topics · Chủ Đề Mở Rộng",
        "New Topics · Chủ Đề Mở Rộng",
        "In-depth technique notes drawn from the <em>3.0 Beginner Practice Guide</em> &mdash; 70 topics across standing, breath, stepping, body, and pitfalls.",
        "Ghi chép kỹ thuật chuyên sâu từ <em>Cẩm Nang 3.0 Beginner</em> &mdash; 70 chủ đề: trụ thế, hơi thở, bước chân, cơ thể, và lỗi thường gặp.",
    )
    vi_block = build_index_page("vi", ALL_TOPICS,
        "New Topics · Chủ Đề Mở Rộng",
        "Chủ Đề Mở Rộng · New Topics",
        "In-depth technique notes drawn from the <em>3.0 Beginner Practice Guide</em> &mdash; 70 topics across standing, breath, stepping, body, and pitfalls.",
        "Ghi chép kỹ thuật chuyên sâu từ <em>Cẩm Nang 3.0 Beginner</em> &mdash; 70 chủ đề: trụ thế, hơi thở, bước chân, cơ thể, và lỗi thường gặp.",
    )

    blocks = {"en": en_block, "vi": vi_block}
    for idx_path, lang in [(en_idx, "en"), (vi_idx, "vi")]:
        text = idx_path.read_text(encoding='utf-8')
        block = blocks[lang]
        # Replace existing topics section
        m = re.search(r'<section id="topics"[^>]*>.*?</section>\s*', text, re.DOTALL)
        if m:
            new_text = text[:m.start()] + block.strip() + '\n\n' + text[m.end():]
            idx_path.write_text(new_text, encoding='utf-8')
            print(f"  replaced topics block in {idx_path.name}")
        else:
            m2 = re.search(r'</article>', text)
            if m2:
                new_text = text[:m2.start()] + block + text[m2.start():]
                idx_path.write_text(new_text, encoding='utf-8')
                print(f"  appended topics block to {idx_path.name}")
            else:
                print(f"  WARN: no </article> in {idx_path}")

    # Count unique topics
    for lang in ["en", "vi"]:
        idx_path = REPO / lang / "techniques" / "index.html"
        text = idx_path.read_text(encoding='utf-8')
        slugs = re.findall(rf'href="/{lang}/techniques/([^"]+)/"', text)
        unique = set(slugs)
        dups = len(slugs) - len(unique)
        print(f"  {lang} index: {len(slugs)} links, {len(unique)} unique, {dups} duplicates")


if __name__ == "__main__":
    main()
