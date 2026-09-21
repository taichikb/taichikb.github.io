#!/usr/bin/env python3
"""
Generate 200 health-article Markdown sources (100 EN + 100 VI) for taichikb.github.io
Follows 'Strategy & Content Expansion Plan: 100 English & 100 Vietnamese Articles'.
Sources: Health, TCM, Energy Medicine, Yoga, Taichi & Qigong NotebookLM vault (299 sources).
"""
import os, re

REPO = os.path.dirname(os.path.abspath(__file__))
VAULT_ID = "d2401afd-0718-4fac-b429-5bca391d27a9"
VAULT_URL = f"https://notebooklm.google.com/notebook/{VAULT_ID}"
DATE = "2026-09-21"

PILLARS = [
    ("TCM_Meridians", "Traditional Chinese Medicine, Meridian Science", "Y Học Cổ Truyền, Kinh Lạc"),
    ("Neigong_Energy", "Internal Alchemy, Energy Medicine", "Nội Công, Y Học Năng Lượng"),
    ("Qigong_Longevity", "Qigong, Organ Health", "Khí Công, Dưỡng Tạng"),
    ("Taichi_Biomechanics", "Taichi, Biomechanics", "Thái Cực Quyền, Cơ Sinh Học"),
    ("Yoga_Taichi_Synergy", "Yoga, Taichi, Flexibility", "Yoga, Thái Cực, Giãn Cơ"),
    ("Nervous_System", "Mind-Body, Neuroscience", "Thần Kinh, Tâm-Thân"),
    ("Respiratory_Health", "Breathing, Diaphragm", "Hô Hấp, Cơ Hoành"),
    ("Joint_Longevity", "Joints, Seniors, Balance", "Khớp, Người Cao Tuổi, Thăng Bằng"),
    ("Seasonal_Living", "Seasonal Living, Self-Healing", "Dưỡng Sinh, Tự Chữa Lành"),
    ("Tennis_Taichi", "Tennis, Cross-Training", "Tennis, Tập Chéo"),
]

# (slug_en, title_en, title_vi) x 10 per pillar
TOPICS = {
"TCM_Meridians": [
 ("meridian-flow-mechanics", "Meridian Flow Mechanics: How Qi Navigates the 12 Primary Channels", "Cơ Hoành & Đường Đi Của Khí Trong 12 Kinh Lạc Chính"),
 ("five-elements-diagnostics", "The Five Elements (Wu Xing) in Daily Health Diagnostics", "Ngũ Hành Lập Luận Trong Chẩn Đoán Sức Khỏe Hằng Ngày"),
 ("zang-fu-organ-dynamics", "Zang-Fu Organ Dynamics: Pairings, Functions, and Pathologies", "Học Thuyết Tạng Phủ: Mối Quan Hệ Hỗ Tương Giữa Tạng và Phủ"),
 ("extraordinary-vessels-ren-du", "Extraordinary Vessels: The Sea of Yin (Ren Mai) and Sea of Yang (Du Mai)", "Kỳ Kinh Bát Mạch: Mạch Nhâm, Mạch Đốc và Nguồn Năng Lượng Cốt Tủy"),
 ("acupressure-daily-energy", "Acupressure Points for Daily Energy Activation (ST36, LI4, PC6)", "Huyệt Vị Tự Chữa Lành: Túc Tam Lý, Hợp Cốc và Nội Quan"),
 ("qi-deficiency-vs-stagnation", "Qi Deficiency vs. Qi Stagnation: Clinical Symptoms and Exercises", "Khí Trệ và Khí Hư: Phân Biệt Biểu Hiện và Bài Tập Khắc Phục"),
 ("blood-essence-jing-longevity", "Blood and Essence (Jing): The Substrate of Longevity", "Tinh, Khí, Thần và Tinh Huyết: Nền Tảng Trường Thọ Theo Đông Y"),
 ("seasonal-tcm-solar-terms", "Seasonal TCM Living: Synchronizing Practice with Solar Terms", "Dưỡng Sinh Theo 24 Tiết Khí: Thuận Theo Tự Nhiên"),
 ("triple-burner-san-jiao", "The Triple Burner (San Jiao) Demystified: Water and Heat Regulation", "Tam Tiêu Trong Y Học Cổ Truyền: Điều Hòa Thủy Hỏa và Nhiệt Độ"),
 ("tongue-pulse-self-assessment", "Tongue and Pulse Diagnostics Principles for Self-Assessment", "Tự Theo Dõi Sức Khỏe Qua Biểu Hiện Lưỡi và Mạch Học Cơ Bản"),
],
"Neigong_Energy": [
 ("lower-dantian-cultivation", "Lower Dantian Cultivation: Anchoring Energy in Movement", "Phương Pháp Tụ Khí Hạ Đan Điền Trong Vận Động"),
 ("microcosmic-orbit-meditation", "Microcosmic Orbit Meditation: Unlocking the Spinal Channel", "Vòng Tiểu Chu Thiên: Khai Thông Mạch Nhâm Đốc"),
 ("biofield-physiology", "Biofield Physiology: Modern Biophysics Meets Energy Medicine", "Sinh Học Trường Biofield: Cầu Nối Giữa Y Học Hiện Đại và Năng Lượng"),
 ("three-cavities-alignment", "The Three Cavities: Skull, Thorax, and Pelvic Alignments", "Định Trục 3 Khang: Định Tâm Đầu, Lồng Ngực và Khung Chậu"),
 ("internal-heat-tummo-neigong", "Internal Heat Generation (Tummo & Neigong Principles)", "Nguyên Lý Sinh Nhiệt Nội Bội Của Nội Công và Khí Công"),
 ("inner-smile-stress-vitality", "Transforming Stress into Vitality: The Inner Smile Technique", "Chuyển Hóa Căng Thắng Thành Năng Lượng Qua \"Nụ Cười Nội Tâm\""),
 ("six-healing-sounds-liu-zi-jue", "The Six Healing Sounds (Liu Zi Jue) for Detoxification", "Lục Tự Khí Công: 6 Âm Thanh Chữa Lành Ngũ Tạng"),
 ("fascial-energy-transmission", "Fascial Energy Transmission: Collagen Networks as Bio-Conductors", "Mạng Lưới Cân Mạc: Kênh Dẫn Truyền Năng Lượng Tự Nhiên"),
 ("bone-marrow-washing-xi-sui-jing", "Bone Marrow Washing (Xi Sui Jing) Fundamentals", "Tẩy Tủy Kinh: Phương Pháp Dưỡng Tủy và Tái Tạo Tế Bào"),
 ("shielding-emotional-energy", "Shielding Emotional Energy: Maintaining Boundary and Center", "Bảo Vệ Trường Năng Lượng Cá Nhân Trước Tác Động Ngoại Cảnh"),
],
"Qigong_Longevity": [
 ("ba-duan-jin-biomechanics", "Ba Duan Jin (Eight Brocades): Step-by-Step Biomechanical Breakdown", "Bát Đoạn Cẩm: Phân Tích Cơ Học 8 Động Tác Cốt Tủy"),
 ("wu-qin-xi-five-animals", "Wu Qin Xi (Five Animal Frolics): Releasing Tension in Organs", "Ngũ Cầm Hí: Phục Hồi Chức Năng Ngũ Tạng Theo Linh Vật"),
 ("yi-jin-jing-tendon-changing", "Yi Jin Jing (Tendon Changing Classic): Structural Reconditioning", "Dịch Cân Kinh: Rèn Luyện Gân Cốt và Cấu Trúc Khung Xương"),
 ("shibashi-18-cardiovascular", "Shibashi 18 Movements: Flow States for Cardiovascular Health", "Thái Cực Khí Công 18 Thức: Dòng Chảy Năng Lượng Cho Tim Mạch"),
 ("crane-qigong-spine-lymph", "Crane Qigong for Spine Mobility and Lymphatic Drainage", "Hạc Khí Công: Nâng Cao Sự Linh Hoạt Cột Sống và Hệ Bạch Huyết"),
 ("dragon-qigong-spinal-twist", "Dragon Qigong for Spinal Twisting and Core Vitality", "Long Khí Công: Xoắn Cột Sống và Khơi Thông Năng Lượng Lõi"),
 ("zhan-zhuang-immune", "Standing Pole (Zhan Zhuang) for Immune System Enhancement", "Trụ Thế Khí Công (Zhan Zhuang): Tăng Cường Hệ Miễn Dịch"),
 ("kidney-qigong-lower-back", "Kidney Support Qigong: Strengthening Lower Back and Vital Will", "Khí Công Bổ Thận: Củng Cố Cột Sống Thắt Lưng và Nguyên Khí"),
 ("liver-detox-qigong-stress", "Liver Qi Detoxification Protocols for Stress Reduction", "Khí Công Giải Độc Gan: Tẩy Trừ Căng Thắng và Nóng Trong"),
 ("heart-qigong-sleep", "Heart-Centering Qigong: Emotional Balance and Sleep Quality", "Khí Công An Thần: Cân Bằng Cảm Xúc và Cải Thiện Giấc Ngủ"),
],
"Taichi_Biomechanics": [
 ("ground-reaction-yongquan", "Ground Reaction Force: Rooting Energy Through the Yongquan Point", "Lực Phản Hồi Từ Mặt Đất: Cắm Rễ Qua Huyệt Dũng Tuyền"),
 ("kua-integration-hip", "Kua Integration: Opening and Closing the Hip Joint", "Mở và Đóng Khai Hợp Vùng Háng (Kua) Trong Di Chuyển"),
 ("chan-si-gong-spiral", "Silk-Reeling (Chan Si Gong): Spiral Dynamics of the Extremities", "Trần Thị Triền Ty Công: Động Học Xoắn Ốc Của Tay Chân"),
 ("baihui-crown-suspension", "Suspension from the Crown (Baihui): Gravity Neutralization", "Treo Đỉnh Đầu (Bách Hội): Triệt Tiêu Căng Thắng Trọng Lực"),
 ("song-relaxation-vs-sagging", "Song (Relaxation) vs. Sagging: Functional Structural Integrity", "Thả Lỏng (Tùng - Sōng) Khác Với Bẹp Cấu Trúc Khung Xương"),
 ("pelvic-bowl-low-stances", "Pelvic Bowl Stabilization in Low Stances", "Ổn Định Vùng Khung Chậu Trong Các Tư Thế Hạ Thấp"),
 ("knee-alignment-acl-safety", "Knee Alignment Rules: Preventing Shear Stress and ACL Damage", "Bảo Vệ Khớp Gối: Quy Tắc Tránh Lệch Trục và Đau Khớp"),
 ("spine-coiling-yang-chen", "Spine Coiling and Uncoiling in Yang and Chen Styles", "Kỹ Thuật Xoắn Cột Sống Trong Thái Cực Quyền Dương Thị & Trần Thị"),
 ("chen-jian-zhui-zhou", "Shoulders Sinking and Elbows Dropping (Chen Jian Zhui Zhou)", "Trầm Vai Trụy Chỏ (Trầm Kiên Trụy Trữu): Giảm Tải Cổ Vai Gáy"),
 ("kinetic-chain-no-tension", "Kinetic Chain Continuity: Force Generation Without Muscular Tension", "Chuỗi Động Học Liên Tục: Phát Lực Không Dùng Cơ Bắp Thô"),
],
"Yoga_Taichi_Synergy": [
 ("asana-holds-taichi-flow", "Asana Holds Meets Taichi Flow: Combining Static and Dynamic Stretch", "Tĩnh Tọa Yoga Kết Hợp Luân Chuyển Thái Cực: Giãn Cơ Toàn Diện"),
 ("pranayama-tu-na-breathing", "Pranayama and Tu Na Breathing: Comparative Respiratory Science", "Phép Hít Thở Pranayama và Thổ Nạp (Tu Na): Phân Tích Sinh Lý"),
 ("backbends-taichi-back-safety", "Hatha Yoga Backbends and Taichi Back Extension Safety", "Uốn Lưng Yoga và Mở Ngực Thái Cực: An Toàn Cột Sống"),
 ("hip-openers-pigeon-stepping", "Hip Openers: Pigeon Pose vs. Taichi Stepping Drills", "Mở Háng: So Sánh Tư Thế Chim Bồ Câu và Bộ Pháp Thái Cực"),
 ("shoulder-mobility-gomukhasana-peng", "Shoulder Mobility: Gomukhasana Meets Ward Off (Peng)", "Linh Hoạt Khớp Vai: Tư Thế Mặt Quỷ và Thức Phòng (Peng)"),
 ("core-uddiyana-dantian", "Core Stability: Uddiyana Bandha and Dantian Compression", "Mũi Lõi Cốt Tủy: Khóa Uddiyana Bandha và Nén Đan Điền"),
 ("balance-tree-golden-rooster", "Balance Integration: Tree Pose vs. Golden Rooster Stands on One Leg", "Giữ Cân Bằng: Tư Thế Cái Cây Yoga và Kim Kê Độc Lập"),
 ("hamstring-low-stance-health", "Hamstring Lengthening for Low Stance Health", "Duỗi Cơ Đùi Sau Nhằm Hỗ Trợ Đứng Đinh Tấn An Toàn"),
 ("vagus-inversions-sinking", "Vagus Nerve Stimulation Through Yoga Inversions and Taichi Sinking", "Kích Thích Dây Thần Kinh Mê Tẩu Qua Tư Thế Đảo Ngược và Trầm Khí"),
 ("restorative-yoga-zhan-zhuang", "Restorative Yoga and Zhan Zhuang Integration for Burnout Recovery", "Phục Hồi Kiệt Sức Nhờ Yoga Phục Hồi và Đứng Trụ Khí Công"),
],
"Nervous_System": [
 ("parasympathetic-shift", "Parasympathetic Shift: Moving from Fight-or-Flight to Rest-and-Digest", "Kích Hoạt Hệ Thần Kinh Đối Giao Cảm: Thoát Khỏi Căng Thắng Cụm"),
 ("interoception-slow-movement", "Interoception: Training Internal Body Awareness Through Slow Movement", "Khả Năng Cảm Nhận Nội Tại (Interoception) Qua Chuyển Động Chậm"),
 ("proprioception-fall-prevention", "Proprioception Re-calibration for Fall Prevention in Seniors", "Cảm Nhận Thể Không Gian (Proprioception) Giúp Phòng Ngừa Té Ngã"),
 ("yi-dao-qi-dao-focus", "The Mind Directs the Qi (Yi Dao Qi Dao): Cognitive Focus Science", "Ý Đáo Khí Đáo: Cơ Sở Khoa Học Của Việc Dùng Ý Dẫn Khí"),
 ("cortisol-reduction-15min", "Cortisol Reduction Protocols Through Daily 15-Minute Practices", "Giảm Nồng Độ Cortisol Nhờ 15 Phút Tập Luyện Hằng Ngày"),
 ("hrv-coherent-breathing", "Heart Rate Variability (HRV) Optimization via Coherent Breathing", "Tối Ưu Hóa Biến Thiên Nhịp Tim (HRV) Nhờ Hít Thở Đồng Điệu"),
 ("somatic-experiencing-trauma", "Somatic Experiencing: Releasing Trauma Stored in Muscle Tissue", "Giải Phóng Căng Thắng Lưu Trữ Trong Mô Cơ Theo Y Học Thần Kinh"),
 ("brain-waves-alpha-theta", "Brain Wave Entrainment: Alpha and Theta States in Taichi Motion", "Sóng Não Alpha & Theta Trong Trạng Thái Chuyển Động Thái Cực"),
 ("neuroplasticity-adult-motor", "Neuroplasticity and Motor Skill Acquisition in Adult Practitioners", "Tính Mềm Dẻo Não Bộ (Neuroplasticity) Ở Người Trưởng Thành Tập Võ"),
 ("kinesiophobia-joint-injury", "Overcoming Movement Fear (Kinesiophobia) After Joint Injuries", "Vượt Qua Nỗi Sợ Vận Động Sau Chấn Thương Khớp"),
],
"Respiratory_Health": [
 ("diaphragm-primary-engine", "The Diaphragm as the Primary Breathing Engine", "Vai Trò Cốt Tủy Của Cơ Hoành Trong Hô Hấp Chuẩn Sinh Lý"),
 ("reverse-abdominal-breathing", "Reverse Abdominal Breathing (Ni Fu Shi Hu Xi) for Power", "Phép Hở Bụng Ngược (Phúc Khí Tăng Áp) Để Phát Lực Nội Công"),
 ("post-expiratory-pauses", "Post-Expiratory Pauses and Oxygen Exchange Efficiency", "Khoảng Tạm Ngừng Sau Khi Thở Ra và Hiệu Suất Trao Đổi Oxy"),
 ("ribcage-intercostal-mobility", "Ribcage Mobility: Intercostal Muscle Expansion Techniques", "Độ Mở Lồng Ngực: Bài Tập Co Giãn Cơ Liên Sườn"),
 ("nitric-oxide-nasal-breathing", "Nitric Oxide Production Through Nasal Breathing", "Tối Ưu Khí Nitric Oxide Qua Phép Thở Bằng Mũi"),
 ("breath-movement-sync", "Breath-Movement Synchronization in Form Practice", "Đồng Bộ Hóa Hơi Thở Với Nhịp Điệu Chuyển Động Thái Cực"),
 ("pelvic-floor-mulabandha-qi", "Pelvic Floor Diaphragm Co-Activation (Mulabandha and Qi)", "Sự Kết Hợp Giữa Cơ Hoành và Cơ Đáy Chậu Trong Khí Công"),
 ("copd-asthma-qigong-rehab", "COPD and Asthma Rehabilitation Exercises Through Qigong", "Phục Hồi Hô Hấp Cho Người Hen Suyễn & Hen Phế Quản Nhờ Khí Công"),
 ("qi-chen-dan-tian-science", "The Science of Sinking Breath to Dantian (Qi Chen Dan Tian)", "Khoa Học Sau Cụm Từ \"Khí Trầm Đan Điền\""),
 ("hyperventilation-slow-pacing", "Hyperventilation Recovery Through Slow Pacing Protocols", "Phương Pháp Điều Hòa Nhịp Thở Cho Người Hay Bị Thở Gấp"),
],
"Joint_Longevity": [
 ("synovial-fluid-circular-motion", "Synovial Fluid Stimulation Through Continuous Circular Motions", "Tăng Cường Dịch Khớp Nhờ Các Chuyển Động Tròn Liên Tục"),
 ("cartilage-weight-bearing", "Cartilage Preservation in Weight-Bearing Joints", "Bảo Vệ Lớp Sụn Ở Các Khớp Chịu Lực Cơ Thể"),
 ("ankles-feet-balance-foundation", "Ankles and Feet Strengthening: The Foundation of Balance", "Củng Cố Cổ Chân và Bàn Chân: Nền Tảng Giữ Cân Bằng"),
 ("osteoporosis-dynamic-loading", "Preventing Osteoporosis: Weight-Bearing Dynamic Loading", "Phòng Chống Loãng Xương Bằng Các Bài Tập Chịu Lực Động"),
 ("hip-arthritis-gentle-rotations", "Hip Arthritis Relief Strategies Using Gentle Taichi Rotations", "Giảm Đau Thoái Hóa Khớp Háng Nhờ Xoay Hông Thái Cực Chậm"),
 ("lumbar-decompression-standing", "Lumbar Spine Decompression in Standing and Seated Positions", "Giải Nén Cột Sống Thắt Lưng Khi Đứng Và Khi Tĩnh Tọa"),
 ("cervical-safety-neck-crown", "Cervical Spine Safety: Aligning the Neck and Crown", "An Toàn Đốt Sống Cổ: Giữ Trục Thẳng Cổ và Đỉnh Đầu"),
 ("fall-recovery-stepping", "Fall Recovery Dynamics: Stepping and Catching Equilibrium", "Phản Ứng Giữ Cân Bằng Tránh Ngã Khi Bị Trượt Chân"),
 ("chair-qigong-seniors", "Chair Qigong Protocols for Seniors and Mobility-Limited Individuals", "Khí Công Trên Ghế Dành Cho Người Cao Tuổi Hoặc Khó Di Chuyển"),
 ("chronic-pain-fibromyalgia", "Managing Chronic Pain Conditions (Fibromyalgia, Rheumatoid)", "Kiểm Soát Đau Mạn Tính (Mất Bằng Cơ, Viêm Khớp Dạng Thấp)"),
],
"Seasonal_Living": [
 ("spring-liver-tendon", "Spring Health: Liver Cleansing and Tendon Stretching", "Dưỡng Sinh Mùa Xuân: Nối Can Gan và Giãn Mềm Gân Cốt"),
 ("summer-heart-cooling", "Summer Heat Management: Heart-Nourishing Practices", "Dưỡng Sinh Mùa Hè: Thanh Nhiệt và Dưỡng Tâm"),
 ("autumn-lung-wei-qi", "Autumn Wellness: Lung Moisture and Defensive Qi (Wei Qi)", "Dưỡng Sinh Mùa Thu: Nhuận Phế và Tăng Cường Vệ Khí"),
 ("winter-kidney-storage", "Winter Preservation: Kidney Storage and Deep Zhan Zhuang", "Dưỡng Sinh Mùa Đông: Tàng Ẩn Năng Lượng Thận và Trụ Thế Sâu"),
 ("morning-10min-joint-routine", "Morning 10-Minute Wake-Up Routine for Joint Lubrication", "Bài Tập 10 Phút Buổi Sáng: Khởi Động Trơn Trù Toàn Bộ Khớp"),
 ("midday-desk-qigong-eyes", "Mid-day Energy Reset: Desk-Side Qigong and Eye Relief", "Tái Tạo Năng Lượng Giữa Giờ: Khí Công Văn Phòng & Thư Giãn Mắt"),
 ("evening-shen-sleep", "Evening Wind-Down: Calming the Shen Before Sleep", "Dưỡng Tâm Buổi Tối: An Thần Giúp Giấc Ngủ Sâu"),
 ("self-tuina-meridian-massage", "Self-Tui Na Massage for Meridians and Acupoints", "Tự Xoa Bóp Vuốt Kinh Lạc và Huyệt Vị Hằng Ngày"),
 ("hydrotherapy-herbal-foot-baths", "Hydrotherapy and Herbal Foot Baths in TCM Practice", "Ngâm Chân Thảo Dược Theo Y Học Cổ Truyền"),
 ("mindful-eating-digestive-qi", "Mindful Eating and Digestive Qi Energy Conservation", "Ăn Uống Tỉnh Thức và Tiết Kiệm Năng Lượng Tỳ Vị"),
],
"Tennis_Taichi": [
 ("weight-transfer-forehand", "Biomechanical Transfer: Taichi Weight Transfers for Tennis Forehands", "Ứng Dụng Chéo: Chuyển Trọng Lực Thái Cực Cho Cú Forehand Tennis"),
 ("kinetic-chain-serve-shoulder", "Kinetic Chain Fluidity: Serving with Less Shoulder Strain", "Chuỗi Động Học Mềm Mại: Phát Bóng Tennis Giảm Tải Cho Vai"),
 ("fa-jin-relaxed-core", "Explosive Release (Fa Jin) Supported by Relaxed Core", "Phát Lực (Phát Kình - Fa Jin) Nhờ Cơ Thể Thả Lỏng"),
 ("court-footwork-empty-solid", "Court Movement Footwork: Empty and Solid Weight Distribution", "Bộ Pháp Di Chuyển Sân Đấu: Phân Biệt Thực - Hư Chân Đứng"),
 ("tennis-elbow-tendon-care", "Preventing Tennis Elbow Through Tendon Conditioning", "Tránh Lỗi Đau Khuỷu Tay Tennis (Tennis Elbow) Nhờ Luyện Gân"),
 ("breathing-under-pressure", "Breathing Under Pressure: Maintaining Calm During Match Points", "Thở Trong Áp Lực: Giữ Bình Tĩnh Tại Các Điểm Quyết Định"),
 ("mental-toughness-equilibrium", "Mental Toughness: Taichi Equilibrium in Competitive Sports", "Tinh Thần Thép: Điểm Cân Bằng Thái Cực Trong Thi Đấu"),
 ("post-match-qigong-recovery", "Post-Match Recovery: Qigong Rehydration and Lactic Acid Flush", "Phục Hồi Sau Trận Đấu: Khí Công Xả Axit Lactic"),
 ("agility-taichi-stepping", "Agility Training via Tai Chi Stepping Patterns (Ba Gua / Tai Chi)", "Tập Bộc Phá Linh Hoạt Qua Các Bước Di Chuyển Thái Cực / Bát Quái"),
 ("athlete-longevity-50plus", "Longevity for Athletes: Extending Play Ability Beyond Age 50", "Trường Thọ Thể Thao: Duy trì Phong Độ Thi Đấu Sau Tuổi 50"),
],
}

SECTIONS_EN = [
 ("1. Executive Summary & Clinical Intent", "High-level breakdown of the health concept, biomechanical mechanism, or TCM principle. *(To be expanded from the vault's 299 grounded sources.)*"),
 ("2. Classical TCM & Energy Medicine Theory", "Classical grounding: channels, organ clock, element theory, classical citations from the vault. *(To be expanded.)*"),
 ("3. Modern Biomechanics & Neurophysiology", "Fascia, vagus nerve, biofield, piezoelectricity, motor-control science. *(To be expanded.)*"),
 ("4. Comprehensive Step-by-Step Movement Breakdown", "Numbered drill instructions with breathing cues and timing. *(To be expanded.)*"),
 ("5. Common Errors, Kinetic Deviations & Safety Protocols", "Error / Cause / Fix table plus contraindications. *(To be expanded.)*"),
 ("6. Anatomical Diagrams & Visual Cue Specs", "SVG/graphic specification for the key body-map. *(To be added.)*"),
 ("7. Video Demonstration Schema & Slow-Motion Drill Embeds", "YouTube embed schema with duration and source. *(To be added.)*"),
 ("8. Cross-Disciplinary Synergy", "Yoga, Tennis and Senior-Mobility applications. *(To be expanded.)*"),
 ("9. Self-Assessment Matrix & Progress Metrics", "Symptom / Indication / Practice-target table. *(To be expanded.)*"),
 ("10. Master Practice Quick-Reference Card (Printable)", "Goal / Action / Duration printable card. *(To be expanded.)*"),
]
SECTIONS_VI = [
 ("1. Tóm Tắt Điều Hành & Mục Tiêu Trị Liệu", "Phân tích cấp cao về khái niệm sức khỏe, cơ chế cơ sinh học hoặc nguyên lý Đông Y. *(Sẽ mở rộng từ 299 nguồn grounded của vault.)*"),
 ("2. Lý Luận Đông Y & Y Học Năng Lượng", "Cơ sở cổ truyền: kinh lạc, đồng hồ tạng phủ, ngũ hành, trích dẫn từ vault. *(Sẽ mở rộng.)*"),
 ("3. Sinh Lý Cơ Học & Thần Kinh Hiện Đại", "Cân mạc, dây thần kinh mê tẩu, biofield, áp điện, khoa học vận động. *(Sẽ mở rộng.)*"),
 ("4. Hướng Dẫn Chi Tiết Từng Bước", "Số thứ tự bài tập, gợi ý hô hấp và thời gian. *(Sẽ mở rộng.)*"),
 ("5. Lỗi Thường Gặp & Giao Thức An Toàn", "Bảng Lỗi / Nguyên Nhân / Cách Khắc Phục cùng chống chỉ định. *(Sẽ mở rộng.)*"),
 ("6. Sơ Đồ Giải Phẫu & Đặc Tả Hình Ảnh", "Đặc tả SVG/đồ họa cho sơ đồ cơ thể chính. *(Sẽ bổ sung.)*"),
 ("7. Mã Nhúng Video Minh Họa", "Schema nhúng YouTube với thời lượng và nguồn. *(Sẽ bổ sung.)*"),
 ("8. Ứng Dụng Liên Ngành", "Yoga, Tennis và phục hồi người cao tuổi. *(Sẽ mở rộng.)*"),
 ("9. Bảng Tự Đánh Giá & Chỉ Số Tiến Bộ", "Bảng Triệu chứng / Biểu hiện / Bài tập phù hợp. *(Sẽ mở rộng.)*"),
 ("10. Thẻ Thực Hành Nhanh (In Sổ Tay)", "Thẻ Mục tiêu / Hành động / Thời gian. *(Sẽ mở rộng.)*"),
]

def fm(num, pillar_label, title, lang, cats):
    return (f'---\ntitle: "{title}"\ndate: {DATE}\nauthor: "TaichiKB Knowledge Base"\n'
            f'categories: [{cats}]\nvault_ref: "{VAULT_ID}"\nvault_link: "{VAULT_URL}"\n'
            f'pillar: "{pillar_label}"\nlang: {lang}\nlayout: doc\n---\n')

def body(num, pillar_label, title, lang, slug):
    if lang == "en":
        h = f"# EN-{num:03d}: {title}\n\n> **Vault Grounding**: Integrated from the [Health, TCM, Energy Medicine, Yoga, Taichi and Qigong Vault]({VAULT_URL}) (299 Sources).\n"
        sections = SECTIONS_EN
    else:
        h = f"# VI-{num:03d}: {title}\n\n> **Nguồn Tư Liệu**: Trích xuất từ Kho dữ liệu [Health, TCM, Energy Medicine, Yoga, Taichi and Qigong]({VAULT_URL}) (299 Tác phẩm & Chuyên luận).\n"
        sections = SECTIONS_VI
    parts = [h]
    for sec, note in sections:
        parts.append(f"\n## {sec}\n\n{note}\n")
    parts.append(f"\n---\n\n*Status: SKELETON — content to be expanded from vault topic {num:03d} ({pillar_label}). Article spec: 10-section architecture, ~3,500–5,000 words when complete.*\n")
    return "\n".join(parts)

def main():
    made = 0
    for pi, (pillar, cats_en, cats_vi) in enumerate(PILLARS, 1):
        for ti, (slug, ten, tvi) in enumerate(TOPICS[pillar], 1):
            num = (pi - 1) * 10 + ti
            en_dir = os.path.join(REPO, "en", "articles")
            vi_dir = os.path.join(REPO, "vi", "articles")
            en_f = os.path.join(en_dir, f"EN-{num:03d}-{pillar}-{slug}.md")
            vi_f = os.path.join(vi_dir, f"VI-{num:03d}-{pillar}-{slug}.md")
            if not os.path.exists(en_f):
                with open(en_f, "w", encoding="utf-8") as fh:
                    fh.write(fm(num, pillar, ten, "en", cats_en) + "\n" + body(num, pillar, ten, "en", slug))
                made += 1
            if not os.path.exists(vi_f):
                with open(vi_f, "w", encoding="utf-8") as fh:
                    fh.write(fm(num, pillar, tvi, "vi", cats_vi) + "\n" + body(num, pillar, tvi, "vi", slug))
                made += 1
    total = len(os.listdir(os.path.join(REPO, "en", "articles"))) if os.path.isdir(os.path.join(REPO, "en", "articles")) else 0
    print(f"[OK] created {made} new files")
    # count our files
    n_en = len([f for f in os.listdir(os.path.join(REPO, "en", "articles")) if re.match(r'EN-\d{3}', f)])
    n_vi = len([f for f in os.listdir(os.path.join(REPO, "vi", "articles")) if re.match(r'VI-\d{3}', f)])
    print(f"[OK] EN health articles: {n_en}/100 | VI health articles: {n_vi}/100")

if __name__ == "__main__":
    main()
