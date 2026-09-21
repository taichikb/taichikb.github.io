#!/usr/bin/env python3
"""
Build full-depth health articles (EN/VI) for taichikb.github.io.
Converts the 10-section Markdown articles into the site base template,
mirroring the build_techniques.py injection pattern.
"""
import os, re, html
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
VAULT_URL = "https://notebooklm.google.com/notebook/d2401afd-0718-4fac-b429-5bca391d27a9"

ARTICLES = [
    {
        "md": "en/articles/EN-001-TCM_Meridians-meridian-flow-mechanics.md",
        "out": "en/articles/meridian-flow-mechanics",
        "lang": "en",
        "title": "Meridian Flow Mechanics: How Qi Navigates the 12 Primary Channels",
        "subtitle": "TaichiKB Health Article EN-001 · Traditional Chinese Medicine & Meridian Science",
        "crosslink": "/vi/articles/co-hoanh-12-kinh-lac/",
        "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-001-TCM_Meridians-meridian-flow-mechanics.md",
        "out": "vi/articles/co-hoanh-12-kinh-lac",
        "lang": "vi",
        "title": "Cơ Hoành & Đường Đi Của Khí Trong 12 Kinh Lạc Chính",
        "subtitle": "TaichiKB Health Article VI-001 · Y Học Cổ Truyền & Kinh Lạc",
        "crosslink": "/en/articles/meridian-flow-mechanics/",
        "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-002-TCM_Meridians-five-elements-diagnostics.md",
        "out": "en/articles/five-elements-diagnostics",
        "lang": "en",
        "title": "The Five Elements (Wu Xing) in Daily Health Diagnostics",
        "subtitle": "TaichiKB Health Article EN-002 · Traditional Chinese Medicine & Meridian Science",
        "crosslink": "/vi/articles/ngu-hanh-chan-doan/",
        "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-002-TCM_Meridians-five-elements-diagnostics.md",
        "out": "vi/articles/ngu-hanh-chan-doan",
        "lang": "vi",
        "title": "Ngũ Hành Lập Luận Trong Chẩn Đoán Sức Khỏe Hằng Ngày",
        "subtitle": "TaichiKB Health Article VI-002 · Y Học Cổ Truyền & Kinh Lạc",
        "crosslink": "/en/articles/five-elements-diagnostics/",
        "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-003-TCM_Meridians-zang-fu-organ-dynamics.md",
        "out": "en/articles/zang-fu-organ-dynamics",
        "lang": "en",
        "title": "Zang-Fu Organ Dynamics: Pairings, Functions, and Pathologies",
        "subtitle": "TaichiKB Health Article EN-003 · Traditional Chinese Medicine & Meridian Science",
        "crosslink": "/vi/articles/tang-phu-ho-tuong/",
        "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-003-TCM_Meridians-zang-fu-organ-dynamics.md",
        "out": "vi/articles/tang-phu-ho-tuong",
        "lang": "vi",
        "title": "Học Thuyết Tạng Phủ: Mối Quan Hệ Hỗ Tương Giữa Tạng và Phủ",
        "subtitle": "TaichiKB Health Article VI-003 · Y Học Cổ Truyền & Kinh Lạc",
        "crosslink": "/en/articles/zang-fu-organ-dynamics/",
        "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-004-TCM_Meridians-extraordinary-vessels-ren-du.md",
        "out": "en/articles/ren-du-extraordinary-vessels",
        "lang": "en",
        "title": "Extraordinary Vessels: The Sea of Yin (Ren Mai) and Sea of Yang (Du Mai)",
        "subtitle": "TaichiKB Health Article EN-004 · Traditional Chinese Medicine & Meridian Science",
        "crosslink": "/vi/articles/ky-kinh-nham-doc/",
        "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-004-TCM_Meridians-extraordinary-vessels-ren-du.md",
        "out": "vi/articles/ky-kinh-nham-doc",
        "lang": "vi",
        "title": "Kỳ Kinh Bát Mạch: Mạch Nhâm, Mạch Đốc và Nguồn Năng Lượng Cốt Tủy",
        "subtitle": "TaichiKB Health Article VI-004 · Y Học Cổ Truyền & Kinh Lạc",
        "crosslink": "/en/articles/ren-du-extraordinary-vessels/",
        "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-005-TCM_Meridians-acupressure-daily-energy.md",
        "out": "en/articles/acupressure-st36-li4-pc6",
        "lang": "en",
        "title": "Acupressure Points for Daily Energy Activation (ST36, LI4, PC6)",
        "subtitle": "TaichiKB Health Article EN-005 · Traditional Chinese Medicine & Meridian Science",
        "crosslink": "/vi/articles/huyet-tu-chua-lanh/",
        "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-005-TCM_Meridians-acupressure-daily-energy.md",
        "out": "vi/articles/huyet-tu-chua-lanh",
        "lang": "vi",
        "title": "Huyệt Vị Tự Chữa Lành: Túc Tam Lý, Hợp Cốc và Nội Quan",
        "subtitle": "TaichiKB Health Article VI-005 · Y Học Cổ Truyền & Kinh Lạc",
        "crosslink": "/en/articles/acupressure-st36-li4-pc6/",
        "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-006-TCM_Meridians-qi-deficiency-vs-stagnation.md",
        "out": "en/articles/qi-deficiency-vs-stagnation",
        "lang": "en",
        "title": "Qi Deficiency vs. Qi Stagnation: Clinical Symptoms and Exercises",
        "subtitle": "TaichiKB Health Article EN-006 · Traditional Chinese Medicine & Meridian Science",
        "crosslink": "/vi/articles/khi-tre-va-khi-hu/",
        "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-006-TCM_Meridians-qi-deficiency-vs-stagnation.md",
        "out": "vi/articles/khi-tre-va-khi-hu",
        "lang": "vi",
        "title": "Khí Trệ và Khí Hư: Phân Biệt Biểu Hiện và Bài Tập Khắc Phục",
        "subtitle": "TaichiKB Health Article VI-006 · Y Học Cổ Truyền & Kinh Lạc",
        "crosslink": "/en/articles/qi-deficiency-vs-stagnation/",
        "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-007-TCM_Meridians-blood-essence-jing-longevity.md",
        "out": "en/articles/jing-blood-longevity",
        "lang": "en",
        "title": "Blood and Essence (Jing): The Substrate of Longevity",
        "subtitle": "TaichiKB Health Article EN-007 · Traditional Chinese Medicine & Meridian Science",
        "crosslink": "/vi/articles/tinh-khi-than-truong-tho/",
        "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-007-TCM_Meridians-blood-essence-jing-longevity.md",
        "out": "vi/articles/tinh-khi-than-truong-tho",
        "lang": "vi",
        "title": "Tinh, Khí, Thần và Tinh Huyết: Nền Tảng Trường Thọ Theo Đông Y",
        "subtitle": "TaichiKB Health Article VI-007 · Y Học Cổ Truyền & Kinh Lạc",
        "crosslink": "/en/articles/jing-blood-longevity/",
        "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-008-TCM_Meridians-seasonal-tcm-solar-terms.md",
        "out": "en/articles/seasonal-tcm-solar-terms",
        "lang": "en",
        "title": "Seasonal TCM Living: Synchronizing Practice with Solar Terms",
        "subtitle": "TaichiKB Health Article EN-008 · Traditional Chinese Medicine & Meridian Science",
        "crosslink": "/vi/articles/duong-sinh-24-tiet-khi/",
        "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-008-TCM_Meridians-seasonal-tcm-solar-terms.md",
        "out": "vi/articles/duong-sinh-24-tiet-khi",
        "lang": "vi",
        "title": "Dưỡng Sinh Theo 24 Tiết Khí: Thuận Theo Tự Nhiên",
        "subtitle": "TaichiKB Health Article VI-008 · Y Học Cổ Truyền & Kinh Lạc",
        "crosslink": "/en/articles/seasonal-tcm-solar-terms/",
        "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-009-TCM_Meridians-triple-burner-san-jiao.md",
        "out": "en/articles/triple-burner-san-jiao",
        "lang": "en",
        "title": "The Triple Burner (San Jiao) Demystified: Water and Heat Regulation",
        "subtitle": "TaichiKB Health Article EN-009 · Traditional Chinese Medicine & Meridian Science",
        "crosslink": "/vi/articles/tam-tieu-thuy-hoa/",
        "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-009-TCM_Meridians-triple-burner-san-jiao.md",
        "out": "vi/articles/tam-tieu-thuy-hoa",
        "lang": "vi",
        "title": "Tam Tiêu Trong Y Học Cổ Truyền: Điều Hòa Thủy Hỏa và Nhiệt Độ",
        "subtitle": "TaichiKB Health Article VI-009 · Y Học Cổ Truyền & Kinh Lạc",
        "crosslink": "/en/articles/triple-burner-san-jiao/",
        "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-010-TCM_Meridians-tongue-pulse-self-assessment.md",
        "out": "en/articles/tongue-pulse-self-assessment",
        "lang": "en",
        "title": "Tongue and Pulse Diagnostics Principles for Self-Assessment",
        "subtitle": "TaichiKB Health Article EN-010 · Traditional Chinese Medicine & Meridian Science",
        "crosslink": "/vi/articles/luoi-va-mach-tu-danh-gia/",
        "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-010-TCM_Meridians-tongue-pulse-self-assessment.md",
        "out": "vi/articles/luoi-va-mach-tu-danh-gia",
        "lang": "vi",
        "title": "Tự Theo Dõi Sức Khỏe Qua Biểu Hiện Lưỡi và Mạch Học Cơ Bản",
        "subtitle": "TaichiKB Health Article VI-010 · Y Học Cổ Truyền & Kinh Lạc",
        "crosslink": "/en/articles/tongue-pulse-self-assessment/",
        "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-011-Neigong_Energy-lower-dantian-cultivation.md", "out": "en/articles/lower-dantian-cultivation", "lang": "en",
        "title": "Lower Dantian Cultivation: Anchoring Energy in Movement", "subtitle": "TaichiKB Health Article EN-011 · Internal Alchemy, Energy Medicine, Neigong",
        "crosslink": "/vi/articles/vi/articles/ha-dan-dien-tu-khi/", "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-011-Neigong_Energy-lower-dantian-cultivation.md", "out": "vi/articles/ha-dan-dien-tu-khi", "lang": "vi",
        "title": "Phương Pháp Tụ Khí Hạ Đan Điền Trong Vận Động", "subtitle": "TaichiKB Health Article VI-011 · Nội Công, Y Học Năng Lượng",
        "crosslink": "/en/articles/en/articles/lower-dantian-cultivation/", "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-012-Neigong_Energy-microcosmic-orbit-meditation.md", "out": "en/articles/microcosmic-orbit-meditation", "lang": "en",
        "title": "Microcosmic Orbit Meditation: Unlocking the Spinal Channel", "subtitle": "TaichiKB Health Article EN-012 · Internal Alchemy, Energy Medicine, Neigong",
        "crosslink": "/vi/articles/vi/articles/tieu-chu-thien/", "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-012-Neigong_Energy-microcosmic-orbit-meditation.md", "out": "vi/articles/tieu-chu-thien", "lang": "vi",
        "title": "Vòng Tiểu Chu Thiên: Khai Thông Mạch Nhâm Đốc", "subtitle": "TaichiKB Health Article VI-012 · Nội Công, Y Học Năng Lượng",
        "crosslink": "/en/articles/en/articles/microcosmic-orbit-meditation/", "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-013-Neigong_Energy-biofield-physiology.md", "out": "en/articles/biofield-physiology", "lang": "en",
        "title": "Biofield Physiology: Modern Biophysics Meets Energy Medicine", "subtitle": "TaichiKB Health Article EN-013 · Internal Alchemy, Energy Medicine, Neigong",
        "crosslink": "/vi/articles/vi/articles/sinh-hoc-truong-biofield/", "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-013-Neigong_Energy-biofield-physiology.md", "out": "vi/articles/sinh-hoc-truong-biofield", "lang": "vi",
        "title": "Sinh Học Trường Biofield: Cầu Nối Giữa Y Học Hiện Đại và Năng Lượng", "subtitle": "TaichiKB Health Article VI-013 · Nội Công, Y Học Năng Lượng",
        "crosslink": "/en/articles/en/articles/biofield-physiology/", "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-014-Neigong_Energy-three-cavities-alignment.md", "out": "en/articles/three-cavities-alignment", "lang": "en",
        "title": "The Three Cavities: Skull, Thorax, and Pelvic Alignments", "subtitle": "TaichiKB Health Article EN-014 · Internal Alchemy, Energy Medicine, Neigong",
        "crosslink": "/vi/articles/vi/articles/dinh-truc-3-khang/", "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-014-Neigong_Energy-three-cavities-alignment.md", "out": "vi/articles/dinh-truc-3-khang", "lang": "vi",
        "title": "Định Trục 3 Khang: Định Tâm Đầu, Lồng Ngực và Khung Chậu", "subtitle": "TaichiKB Health Article VI-014 · Nội Công, Y Học Năng Lượng",
        "crosslink": "/en/articles/en/articles/three-cavities-alignment/", "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-015-Neigong_Energy-internal-heat-tummo-neigong.md", "out": "en/articles/internal-heat-tummo-neigong", "lang": "en",
        "title": "Internal Heat Generation (Tummo & Neigong Principles)", "subtitle": "TaichiKB Health Article EN-015 · Internal Alchemy, Energy Medicine, Neigong",
        "crosslink": "/vi/articles/vi/articles/sinh-nhiet-noi-boi/", "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-015-Neigong_Energy-internal-heat-tummo-neigong.md", "out": "vi/articles/sinh-nhiet-noi-boi", "lang": "vi",
        "title": "Nguyên Lý Sinh Nhiệt Nội Bội Của Nội Công và Khí Công", "subtitle": "TaichiKB Health Article VI-015 · Nội Công, Y Học Năng Lượng",
        "crosslink": "/en/articles/en/articles/internal-heat-tummo-neigong/", "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-016-Neigong_Energy-inner-smile-stress-vitality.md", "out": "en/articles/inner-smile-stress-vitality", "lang": "en",
        "title": "Transforming Stress into Vitality: The Inner Smile Technique", "subtitle": "TaichiKB Health Article EN-016 · Internal Alchemy, Energy Medicine, Neigong",
        "crosslink": "/vi/articles/vi/articles/nu-cuoi-noi-tam/", "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-016-Neigong_Energy-inner-smile-stress-vitality.md", "out": "vi/articles/nu-cuoi-noi-tam", "lang": "vi",
        "title": "Chuyển Hóa Căng Thắng Thành Năng Lượng Qua Nụ Cười Nội Tâm", "subtitle": "TaichiKB Health Article VI-016 · Nội Công, Y Học Năng Lượng",
        "crosslink": "/en/articles/en/articles/inner-smile-stress-vitality/", "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-017-Neigong_Energy-six-healing-sounds-liu-zi-jue.md", "out": "en/articles/six-healing-sounds-liu-zi-jue", "lang": "en",
        "title": "The Six Healing Sounds (Liu Zi Jue) for Detoxification", "subtitle": "TaichiKB Health Article EN-017 · Internal Alchemy, Energy Medicine, Neigong",
        "crosslink": "/vi/articles/vi/articles/luc-tu-khi-cong/", "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-017-Neigong_Energy-six-healing-sounds-liu-zi-jue.md", "out": "vi/articles/luc-tu-khi-cong", "lang": "vi",
        "title": "Lục Tự Khí Công: 6 Âm Thanh Chữa Lành Ngũ Tạng", "subtitle": "TaichiKB Health Article VI-017 · Nội Công, Y Học Năng Lượng",
        "crosslink": "/en/articles/en/articles/six-healing-sounds-liu-zi-jue/", "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-018-Neigong_Energy-fascial-energy-transmission.md", "out": "en/articles/fascial-energy-transmission", "lang": "en",
        "title": "Fascial Energy Transmission: Collagen Networks as Bio-Conductors", "subtitle": "TaichiKB Health Article EN-018 · Internal Alchemy, Energy Medicine, Neigong",
        "crosslink": "/vi/articles/vi/articles/can-mac-dan-truyen-nang-luong/", "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-018-Neigong_Energy-fascial-energy-transmission.md", "out": "vi/articles/can-mac-dan-truyen-nang-luong", "lang": "vi",
        "title": "Mạng Lưới Cân Mạc: Kênh Dẫn Truyền Năng Lượng Tự Nhiên", "subtitle": "TaichiKB Health Article VI-018 · Nội Công, Y Học Năng Lượng",
        "crosslink": "/en/articles/en/articles/fascial-energy-transmission/", "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-019-Neigong_Energy-bone-marrow-washing-xi-sui-jing.md", "out": "en/articles/bone-marrow-washing-xi-sui-jing", "lang": "en",
        "title": "Bone Marrow Washing (Xi Sui Jing) Fundamentals", "subtitle": "TaichiKB Health Article EN-019 · Internal Alchemy, Energy Medicine, Neigong",
        "crosslink": "/vi/articles/vi/articles/tay-tuy-kinh/", "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-019-Neigong_Energy-bone-marrow-washing-xi-sui-jing.md", "out": "vi/articles/tay-tuy-kinh", "lang": "vi",
        "title": "Tẩy Tủy Kinh: Phương Pháp Dưỡng Tủy và Tái Tạo Tế Bào", "subtitle": "TaichiKB Health Article VI-019 · Nội Công, Y Học Năng Lượng",
        "crosslink": "/en/articles/en/articles/bone-marrow-washing-xi-sui-jing/", "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-020-Neigong_Energy-shielding-emotional-energy.md", "out": "en/articles/shielding-emotional-energy", "lang": "en",
        "title": "Shielding Emotional Energy: Maintaining Boundary and Center", "subtitle": "TaichiKB Health Article EN-020 · Internal Alchemy, Energy Medicine, Neigong",
        "crosslink": "/vi/articles/vi/articles/bao-ve-truong-nang-luong/", "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-020-Neigong_Energy-shielding-emotional-energy.md", "out": "vi/articles/bao-ve-truong-nang-luong", "lang": "vi",
        "title": "Bảo Vệ Trường Năng Lượng Cá Nhân Trước Tác Động Ngoại Cảnh", "subtitle": "TaichiKB Health Article VI-020 · Nội Công, Y Học Năng Lượng",
        "crosslink": "/en/articles/en/articles/shielding-emotional-energy/", "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-021-Qigong_Longevity-ba-duan-jin-biomechanics.md", "out": "en/articles/ba-duan-jin-biomechanics", "lang": "en",
        "title": "Ba Duan Jin (Eight Brocades): Step-by-Step Biomechanical Breakdown", "subtitle": "TaichiKB Health Article EN-21 · Qigong, Organ Health",
        "crosslink": "/vi/articles/vi/articles/bat-doan-cam-co-hoc/", "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-021-Qigong_Longevity-ba-duan-jin-biomechanics.md", "out": "vi/articles/bat-doan-cam-co-hoc", "lang": "vi",
        "title": "Bát Đoạn Cẩm: Phân Tích Cơ Học 8 Động Tác Cốt Tủy", "subtitle": "TaichiKB Health Article VI-21 · Khí Công, Dưỡng Tạng",
        "crosslink": "/en/articles/en/articles/ba-duan-jin-biomechanics/", "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-022-Qigong_Longevity-wu-qin-xi-five-animals.md", "out": "en/articles/wu-qin-xi-five-animals", "lang": "en",
        "title": "Wu Qin Xi (Five Animal Frolics): Releasing Tension in Organs", "subtitle": "TaichiKB Health Article EN-22 · Qigong, Organ Health",
        "crosslink": "/vi/articles/vi/articles/ngu-cam-hi-ngu-tang/", "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-022-Qigong_Longevity-wu-qin-xi-five-animals.md", "out": "vi/articles/ngu-cam-hi-ngu-tang", "lang": "vi",
        "title": "Ngũ Cầm Hí: Phục Hồi Chức Năng Ngũ Tạng Theo Linh Vật", "subtitle": "TaichiKB Health Article VI-22 · Khí Công, Dưỡng Tạng",
        "crosslink": "/en/articles/en/articles/wu-qin-xi-five-animals/", "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-023-Qigong_Longevity-yi-jin-jing-tendon-changing.md", "out": "en/articles/yi-jin-jing-tendon-changing", "lang": "en",
        "title": "Yi Jin Jing (Tendon Changing Classic): Structural Reconditioning", "subtitle": "TaichiKB Health Article EN-23 · Qigong, Organ Health",
        "crosslink": "/vi/articles/vi/articles/dich-canh-kinh/", "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-023-Qigong_Longevity-yi-jin-jing-tendon-changing.md", "out": "vi/articles/dich-canh-kinh", "lang": "vi",
        "title": "Dịch Cân Kinh: Rèn Luyện Gân Cốt và Cấu Trúc Khung Xương", "subtitle": "TaichiKB Health Article VI-23 · Khí Công, Dưỡng Tạng",
        "crosslink": "/en/articles/en/articles/yi-jin-jing-tendon-changing/", "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-024-Qigong_Longevity-shibashi-18-cardiovascular.md", "out": "en/articles/shibashi-18-cardiovascular", "lang": "en",
        "title": "Shibashi 18 Movements: Flow States for Cardiovascular Health", "subtitle": "TaichiKB Health Article EN-24 · Qigong, Organ Health",
        "crosslink": "/vi/articles/vi/articles/thai-cuc-khi-cong-18-thuc/", "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-024-Qigong_Longevity-shibashi-18-cardiovascular.md", "out": "vi/articles/thai-cuc-khi-cong-18-thuc", "lang": "vi",
        "title": "Thái Cực Khí Công 18 Thức: Dòng Chảy Năng Lượng Cho Tim Mạch", "subtitle": "TaichiKB Health Article VI-24 · Khí Công, Dưỡng Tạng",
        "crosslink": "/en/articles/en/articles/shibashi-18-cardiovascular/", "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-025-Qigong_Longevity-crane-qigong-spine-lymph.md", "out": "en/articles/crane-qigong-spine-lymph", "lang": "en",
        "title": "Crane Qigong for Spine Mobility and Lymphatic Drainage", "subtitle": "TaichiKB Health Article EN-25 · Qigong, Organ Health",
        "crosslink": "/vi/articles/vi/articles/hac-khi-cong-cot-song/", "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-025-Qigong_Longevity-crane-qigong-spine-lymph.md", "out": "vi/articles/hac-khi-cong-cot-song", "lang": "vi",
        "title": "Hạc Khí Công: Nâng Cao Sự Linh Hoạt Cột Sống và Hệ Bạch Huyết", "subtitle": "TaichiKB Health Article VI-25 · Khí Công, Dưỡng Tạng",
        "crosslink": "/en/articles/en/articles/crane-qigong-spine-lymph/", "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-026-Qigong_Longevity-dragon-qigong-spinal-twist.md", "out": "en/articles/dragon-qigong-spinal-twist", "lang": "en",
        "title": "Dragon Qigong for Spinal Twisting and Core Vitality", "subtitle": "TaichiKB Health Article EN-26 · Qigong, Organ Health",
        "crosslink": "/vi/articles/vi/articles/long-khi-cong-xoan-cot-song/", "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-026-Qigong_Longevity-dragon-qigong-spinal-twist.md", "out": "vi/articles/long-khi-cong-xoan-cot-song", "lang": "vi",
        "title": "Long Khí Công: Xoắn Cột Sống và Khơi Thông Năng Lượng Lõi", "subtitle": "TaichiKB Health Article VI-26 · Khí Công, Dưỡng Tạng",
        "crosslink": "/en/articles/en/articles/dragon-qigong-spinal-twist/", "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-027-Qigong_Longevity-zhan-zhuang-immune.md", "out": "en/articles/zhan-zhuang-immune", "lang": "en",
        "title": "Standing Pole (Zhan Zhuang) for Immune System Enhancement", "subtitle": "TaichiKB Health Article EN-27 · Qigong, Organ Health",
        "crosslink": "/vi/articles/vi/articles/tru-the-khi-cong-mien-dich/", "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-027-Qigong_Longevity-zhan-zhuang-immune.md", "out": "vi/articles/tru-the-khi-cong-mien-dich", "lang": "vi",
        "title": "Trụ Thế Khí Công (Zhan Zhuang): Tăng Cường Hệ Miễn Dịch", "subtitle": "TaichiKB Health Article VI-27 · Khí Công, Dưỡng Tạng",
        "crosslink": "/en/articles/en/articles/zhan-zhuang-immune/", "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-028-Qigong_Longevity-kidney-qigong-lower-back.md", "out": "en/articles/kidney-qigong-lower-back", "lang": "en",
        "title": "Kidney Support Qigong: Strengthening Lower Back and Vital Will", "subtitle": "TaichiKB Health Article EN-28 · Qigong, Organ Health",
        "crosslink": "/vi/articles/vi/articles/khi-cong-bo-than/", "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-028-Qigong_Longevity-kidney-qigong-lower-back.md", "out": "vi/articles/khi-cong-bo-than", "lang": "vi",
        "title": "Khí Công Bổ Thận: Củng Cố Cột Sống Thắt Lưng và Nguyên Khí", "subtitle": "TaichiKB Health Article VI-28 · Khí Công, Dưỡng Tạng",
        "crosslink": "/en/articles/en/articles/kidney-qigong-lower-back/", "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-029-Qigong_Longevity-liver-detox-qigong-stress.md", "out": "en/articles/liver-detox-qigong-stress", "lang": "en",
        "title": "Liver Qi Detoxification Protocols for Stress Reduction", "subtitle": "TaichiKB Health Article EN-29 · Qigong, Organ Health",
        "crosslink": "/vi/articles/vi/articles/khi-cong-giai-doc-gan/", "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-029-Qigong_Longevity-liver-detox-qigong-stress.md", "out": "vi/articles/khi-cong-giai-doc-gan", "lang": "vi",
        "title": "Khí Công Giải Độc Gan: Tẩy Trừ Căng Thắng và Nóng Trong", "subtitle": "TaichiKB Health Article VI-29 · Khí Công, Dưỡng Tạng",
        "crosslink": "/en/articles/en/articles/liver-detox-qigong-stress/", "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-030-Qigong_Longevity-heart-qigong-sleep.md", "out": "en/articles/heart-qigong-sleep", "lang": "en",
        "title": "Heart-Centering Qigong: Emotional Balance and Sleep Quality", "subtitle": "TaichiKB Health Article EN-30 · Qigong, Organ Health",
        "crosslink": "/vi/articles/vi/articles/khi-cong-an-than/", "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-030-Qigong_Longevity-heart-qigong-sleep.md", "out": "vi/articles/khi-cong-an-than", "lang": "vi",
        "title": "Khí Công An Thần: Cân Bằng Cảm Xúc và Cải Thiện Giấc Ngủ", "subtitle": "TaichiKB Health Article VI-30 · Khí Công, Dưỡng Tạng",
        "crosslink": "/en/articles/en/articles/heart-qigong-sleep/", "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-031-Taichi_Biomechanics-ground-reaction-yongquan.md", "out": "en/articles/ground-reaction-yongquan", "lang": "en",
        "title": "Ground Reaction Force: Rooting Energy Through the Yongquan Point", "subtitle": "TaichiKB Health Article EN-31 · Taichi, Biomechanics",
        "crosslink": "/vi/articles/vi/articles/luc-phan-hoi-dung-tuyen/", "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-031-Taichi_Biomechanics-ground-reaction-yongquan.md", "out": "vi/articles/luc-phan-hoi-dung-tuyen", "lang": "vi",
        "title": "Lực Phản Hồi Từ Mặt Đất: Cắm Rễ Qua Huyệt Dũng Tuyền", "subtitle": "TaichiKB Health Article VI-31 · Thái Cực Quyền, Cơ Sinh Học",
        "crosslink": "/en/articles/en/articles/ground-reaction-yongquan/", "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-032-Taichi_Biomechanics-kua-integration-hip.md", "out": "en/articles/kua-integration-hip", "lang": "en",
        "title": "Kua Integration: Opening and Closing the Hip Joint", "subtitle": "TaichiKB Health Article EN-32 · Taichi, Biomechanics",
        "crosslink": "/vi/articles/vi/articles/kha-hop-vung-hang/", "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-032-Taichi_Biomechanics-kua-integration-hip.md", "out": "vi/articles/kha-hop-vung-hang", "lang": "vi",
        "title": "Mở và Đóng Khai Hợp Vùng Háng (Kua) Trong Di Chuyển", "subtitle": "TaichiKB Health Article VI-32 · Thái Cực Quyền, Cơ Sinh Học",
        "crosslink": "/en/articles/en/articles/kua-integration-hip/", "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-033-Taichi_Biomechanics-chan-si-gong-spiral.md", "out": "en/articles/chan-si-gong-spiral", "lang": "en",
        "title": "Silk-Reeling (Chan Si Gong): Spiral Dynamics of the Extremities", "subtitle": "TaichiKB Health Article EN-33 · Taichi, Biomechanics",
        "crosslink": "/vi/articles/vi/articles/tran-thi-trien-ty-cong/", "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-033-Taichi_Biomechanics-chan-si-gong-spiral.md", "out": "vi/articles/tran-thi-trien-ty-cong", "lang": "vi",
        "title": "Trần Thị Triền Ty Công: Động Học Xoắn Ốc Của Tay Chân", "subtitle": "TaichiKB Health Article VI-33 · Thái Cực Quyền, Cơ Sinh Học",
        "crosslink": "/en/articles/en/articles/chan-si-gong-spiral/", "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-034-Taichi_Biomechanics-baihui-crown-suspension.md", "out": "en/articles/baihui-crown-suspension", "lang": "en",
        "title": "Suspension from the Crown (Baihui): Gravity Neutralization", "subtitle": "TaichiKB Health Article EN-34 · Taichi, Biomechanics",
        "crosslink": "/vi/articles/vi/articles/treo-dinh-dau-bach-hoi/", "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-034-Taichi_Biomechanics-baihui-crown-suspension.md", "out": "vi/articles/treo-dinh-dau-bach-hoi", "lang": "vi",
        "title": "Treo Đỉnh Đầu (Bách Hội): Triệt Tiêu Căng Thắng Trọng Lực", "subtitle": "TaichiKB Health Article VI-34 · Thái Cực Quyền, Cơ Sinh Học",
        "crosslink": "/en/articles/en/articles/baihui-crown-suspension/", "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-035-Taichi_Biomechanics-song-relaxation-vs-sagging.md", "out": "en/articles/song-relaxation-vs-sagging", "lang": "en",
        "title": "Song (Relaxation) vs. Sagging: Functional Structural Integrity", "subtitle": "TaichiKB Health Article EN-35 · Taichi, Biomechanics",
        "crosslink": "/vi/articles/vi/articles/tung-song-tha-long/", "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-035-Taichi_Biomechanics-song-relaxation-vs-sagging.md", "out": "vi/articles/tung-song-tha-long", "lang": "vi",
        "title": "Thả Lỏng (Tùng - Sōng) Khác Với Bẹp Cấu Trúc Khung Xương", "subtitle": "TaichiKB Health Article VI-35 · Thái Cực Quyền, Cơ Sinh Học",
        "crosslink": "/en/articles/en/articles/song-relaxation-vs-sagging/", "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-036-Taichi_Biomechanics-pelvic-bowl-low-stances.md", "out": "en/articles/pelvic-bowl-low-stances", "lang": "en",
        "title": "Pelvic Bowl Stabilization in Low Stances", "subtitle": "TaichiKB Health Article EN-36 · Taichi, Biomechanics",
        "crosslink": "/vi/articles/vi/articles/khung-chau-ha-the/", "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-036-Taichi_Biomechanics-pelvic-bowl-low-stances.md", "out": "vi/articles/khung-chau-ha-the", "lang": "vi",
        "title": "Ổn Định Vùng Khung Chậu Trong Các Tư Thế Hạ Thấp", "subtitle": "TaichiKB Health Article VI-36 · Thái Cực Quyền, Cơ Sinh Học",
        "crosslink": "/en/articles/en/articles/pelvic-bowl-low-stances/", "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-037-Taichi_Biomechanics-knee-alignment-acl-safety.md", "out": "en/articles/knee-alignment-acl-safety", "lang": "en",
        "title": "Knee Alignment Rules: Preventing Shear Stress and ACL Damage", "subtitle": "TaichiKB Health Article EN-37 · Taichi, Biomechanics",
        "crosslink": "/vi/articles/vi/articles/bao-ve-khop-goi/", "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-037-Taichi_Biomechanics-knee-alignment-acl-safety.md", "out": "vi/articles/bao-ve-khop-goi", "lang": "vi",
        "title": "Bảo Vệ Khớp Gối: Quy Tắc Tránh Lệch Trục và Đau Khớp", "subtitle": "TaichiKB Health Article VI-37 · Thái Cực Quyền, Cơ Sinh Học",
        "crosslink": "/en/articles/en/articles/knee-alignment-acl-safety/", "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-038-Taichi_Biomechanics-spine-coiling-yang-chen.md", "out": "en/articles/spine-coiling-yang-chen", "lang": "en",
        "title": "Spine Coiling and Uncoiling in Yang and Chen Styles", "subtitle": "TaichiKB Health Article EN-38 · Taichi, Biomechanics",
        "crosslink": "/vi/articles/vi/articles/xoan-cot-song-duong-tran/", "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-038-Taichi_Biomechanics-spine-coiling-yang-chen.md", "out": "vi/articles/xoan-cot-song-duong-tran", "lang": "vi",
        "title": "Kỹ Thuật Xoắn Cột Sống Trong Thái Cực Quyền Dương Thị & Trần Thị", "subtitle": "TaichiKB Health Article VI-38 · Thái Cực Quyền, Cơ Sinh Học",
        "crosslink": "/en/articles/en/articles/spine-coiling-yang-chen/", "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-039-Taichi_Biomechanics-chen-jian-zhui-zhou.md", "out": "en/articles/chen-jian-zhui-zhou", "lang": "en",
        "title": "Shoulders Sinking and Elbows Dropping (Chen Jian Zhui Zhou)", "subtitle": "TaichiKB Health Article EN-39 · Taichi, Biomechanics",
        "crosslink": "/vi/articles/vi/articles/tram-vai-truy-cho/", "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-039-Taichi_Biomechanics-chen-jian-zhui-zhou.md", "out": "vi/articles/tram-vai-truy-cho", "lang": "vi",
        "title": "Trầm Vai Trụy Chỏ (Trầm Kiên Trụy Trữu): Giảm Tải Cổ Vai Gáy", "subtitle": "TaichiKB Health Article VI-39 · Thái Cực Quyền, Cơ Sinh Học",
        "crosslink": "/en/articles/en/articles/chen-jian-zhui-zhou/", "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-040-Taichi_Biomechanics-kinetic-chain-no-tension.md", "out": "en/articles/kinetic-chain-no-tension", "lang": "en",
        "title": "Kinetic Chain Continuity: Force Generation Without Muscular Tension", "subtitle": "TaichiKB Health Article EN-40 · Taichi, Biomechanics",
        "crosslink": "/vi/articles/vi/articles/chuoi-dong-hoc-lien-tuc/", "crosslabel": "🇻🇳 Tiếng Việt",
    },
    {
        "md": "vi/articles/VI-040-Taichi_Biomechanics-kinetic-chain-no-tension.md", "out": "vi/articles/chuoi-dong-hoc-lien-tuc", "lang": "vi",
        "title": "Chuỗi Động Học Liên Tục: Phát Lực Không Dùng Cơ Bắp Thô", "subtitle": "TaichiKB Health Article VI-40 · Thái Cực Quyền, Cơ Sinh Học",
        "crosslink": "/en/articles/en/articles/kinetic-chain-no-tension/", "crosslabel": "🇬🇧 English",
    },
    {
        "md": "en/articles/EN-041-Yoga_Taichi_Synergy-asana-holds-taichi-flow.md", "out": "en/articles/asana-holds-taichi-flow", "lang": "en",
        "title": "Asana Holds Meets Taichi Flow: Combining Static and Dynamic Stretch", "subtitle": "TaichiKB Health Article EN-41 · Yoga, Taichi, Flexibility",
        "crosslink": "/vi/articles/vi/articles/tinh-toa-luan-chuyen-thai-cuc/", "crosslabel": "\U0001F1FB\U0001F1F3 Ti\u1ebfng Vi\u1ec7t",
    },
    {
        "md": "vi/articles/VI-041-Yoga_Taichi_Synergy-asana-holds-taichi-flow.md", "out": "vi/articles/tinh-toa-luan-chuyen-thai-cuc", "lang": "vi",
        "title": "Tĩnh Tọa Yoga Kết Hợp Luân Chuyển Thái Cực: Giãn Cơ Toàn Diện", "subtitle": "TaichiKB Health Article VI-41 · Yoga, Thái Cực, Giãn Cơ",
        "crosslink": "/en/articles/en/articles/asana-holds-taichi-flow/", "crosslabel": "\U0001F1EC\U0001F1E7 English",
    },
    {
        "md": "en/articles/EN-042-Yoga_Taichi_Synergy-pranayama-tu-na-breathing.md", "out": "en/articles/pranayama-tu-na-breathing", "lang": "en",
        "title": "Pranayama and Tu Na Breathing: Comparative Respiratory Science", "subtitle": "TaichiKB Health Article EN-42 · Yoga, Taichi, Flexibility",
        "crosslink": "/vi/articles/vi/articles/pranayama-tho-nap/", "crosslabel": "\U0001F1FB\U0001F1F3 Ti\u1ebfng Vi\u1ec7t",
    },
    {
        "md": "vi/articles/VI-042-Yoga_Taichi_Synergy-pranayama-tu-na-breathing.md", "out": "vi/articles/pranayama-tho-nap", "lang": "vi",
        "title": "Pranayama và Thổ Nạp (Tu Na): Phân Tích Sinh Lý Hô Hấp", "subtitle": "TaichiKB Health Article VI-42 · Yoga, Thái Cực, Giãn Cơ",
        "crosslink": "/en/articles/en/articles/pranayama-tu-na-breathing/", "crosslabel": "\U0001F1EC\U0001F1E7 English",
    },
    {
        "md": "en/articles/EN-043-Yoga_Taichi_Synergy-backbends-taichi-back-safety.md", "out": "en/articles/backbends-taichi-back-safety", "lang": "en",
        "title": "Hatha Yoga Backbends and Taichi Back Extension Safety", "subtitle": "TaichiKB Health Article EN-43 · Yoga, Taichi, Flexibility",
        "crosslink": "/vi/articles/vi/articles/uon-lung-an-toan/", "crosslabel": "\U0001F1FB\U0001F1F3 Ti\u1ebfng Vi\u1ec7t",
    },
    {
        "md": "vi/articles/VI-043-Yoga_Taichi_Synergy-backbends-taichi-back-safety.md", "out": "vi/articles/uon-lung-an-toan", "lang": "vi",
        "title": "Uốn Lưng Yoga và Mở Ngực Thái Cực: An Toàn Cột Sống", "subtitle": "TaichiKB Health Article VI-43 · Yoga, Thái Cực, Giãn Cơ",
        "crosslink": "/en/articles/en/articles/backbends-taichi-back-safety/", "crosslabel": "\U0001F1EC\U0001F1E7 English",
    },
    {
        "md": "en/articles/EN-044-Yoga_Taichi_Synergy-hip-openers-pigeon-stepping.md", "out": "en/articles/hip-openers-pigeon-stepping", "lang": "en",
        "title": "Hip Openers: Pigeon Pose vs. Taichi Stepping Drills", "subtitle": "TaichiKB Health Article EN-44 · Yoga, Taichi, Flexibility",
        "crosslink": "/vi/articles/vi/articles/mo-hang-bo-phap/", "crosslabel": "\U0001F1FB\U0001F1F3 Ti\u1ebfng Vi\u1ec7t",
    },
    {
        "md": "vi/articles/VI-044-Yoga_Taichi_Synergy-hip-openers-pigeon-stepping.md", "out": "vi/articles/mo-hang-bo-phap", "lang": "vi",
        "title": "Mở Háng: So Sánh Tư Thế Chim Bồ Câu và Bộ Pháp Thái Cực", "subtitle": "TaichiKB Health Article VI-44 · Yoga, Thái Cực, Giãn Cơ",
        "crosslink": "/en/articles/en/articles/hip-openers-pigeon-stepping/", "crosslabel": "\U0001F1EC\U0001F1E7 English",
    },
    {
        "md": "en/articles/EN-045-Yoga_Taichi_Synergy-shoulder-mobility-gomukhasana-peng.md", "out": "en/articles/shoulder-mobility-gomukhasana-peng", "lang": "en",
        "title": "Shoulder Mobility: Gomukhasana Meets Ward Off (Peng)", "subtitle": "TaichiKB Health Article EN-45 · Yoga, Taichi, Flexibility",
        "crosslink": "/vi/articles/vi/articles/linh-hoat-khop-vai/", "crosslabel": "\U0001F1FB\U0001F1F3 Ti\u1ebfng Vi\u1ec7t",
    },
    {
        "md": "vi/articles/VI-045-Yoga_Taichi_Synergy-shoulder-mobility-gomukhasana-peng.md", "out": "vi/articles/linh-hoat-khop-vai", "lang": "vi",
        "title": "Linh Hoạt Khớp Vai: Gomukhasana và Thức Phòng (Peng)", "subtitle": "TaichiKB Health Article VI-45 · Yoga, Thái Cực, Giãn Cơ",
        "crosslink": "/en/articles/en/articles/shoulder-mobility-gomukhasana-peng/", "crosslabel": "\U0001F1EC\U0001F1E7 English",
    },
    {
        "md": "en/articles/EN-046-Yoga_Taichi_Synergy-core-uddiyana-dantian.md", "out": "en/articles/core-uddiyana-dantian", "lang": "en",
        "title": "Core Stability: Uddiyana Bandha and Dantian Compression", "subtitle": "TaichiKB Health Article EN-46 · Yoga, Taichi, Flexibility",
        "crosslink": "/vi/articles/vi/articles/uddiyana-dan-dien/", "crosslabel": "\U0001F1FB\U0001F1F3 Ti\u1ebfng Vi\u1ec7t",
    },
    {
        "md": "vi/articles/VI-046-Yoga_Taichi_Synergy-core-uddiyana-dantian.md", "out": "vi/articles/uddiyana-dan-dien", "lang": "vi",
        "title": "Core Stability: Uddiyana Bandha và Nén Đan Điền", "subtitle": "TaichiKB Health Article VI-46 · Yoga, Thái Cực, Giãn Cơ",
        "crosslink": "/en/articles/en/articles/core-uddiyana-dantian/", "crosslabel": "\U0001F1EC\U0001F1E7 English",
    },
    {
        "md": "en/articles/EN-047-Yoga_Taichi_Synergy-balance-tree-golden-rooster.md", "out": "en/articles/balance-tree-golden-rooster", "lang": "en",
        "title": "Balance Integration: Tree Pose vs. Golden Rooster", "subtitle": "TaichiKB Health Article EN-47 · Yoga, Taichi, Flexibility",
        "crosslink": "/vi/articles/vi/articles/can-bang-kim-ke/", "crosslabel": "\U0001F1FB\U0001F1F3 Ti\u1ebfng Vi\u1ec7t",
    },
    {
        "md": "vi/articles/VI-047-Yoga_Taichi_Synergy-balance-tree-golden-rooster.md", "out": "vi/articles/can-bang-kim-ke", "lang": "vi",
        "title": "Giữ Cân Bằng: Cái Cây Yoga và Kim Kê Độc Lập", "subtitle": "TaichiKB Health Article VI-47 · Yoga, Thái Cực, Giãn Cơ",
        "crosslink": "/en/articles/en/articles/balance-tree-golden-rooster/", "crosslabel": "\U0001F1EC\U0001F1E7 English",
    },
    {
        "md": "en/articles/EN-048-Yoga_Taichi_Synergy-hamstring-low-stance-health.md", "out": "en/articles/hamstring-low-stance-health", "lang": "en",
        "title": "Hamstring Lengthening for Low Stance Health", "subtitle": "TaichiKB Health Article EN-48 · Yoga, Taichi, Flexibility",
        "crosslink": "/vi/articles/vi/articles/duoi-co-dui-sau/", "crosslabel": "\U0001F1FB\U0001F1F3 Ti\u1ebfng Vi\u1ec7t",
    },
    {
        "md": "vi/articles/VI-048-Yoga_Taichi_Synergy-hamstring-low-stance-health.md", "out": "vi/articles/duoi-co-dui-sau", "lang": "vi",
        "title": "Duỗi Cơ Đùi Sau: Hỗ Trợ Đứng Đinh Tấn An Toàn", "subtitle": "TaichiKB Health Article VI-48 · Yoga, Thái Cực, Giãn Cơ",
        "crosslink": "/en/articles/en/articles/hamstring-low-stance-health/", "crosslabel": "\U0001F1EC\U0001F1E7 English",
    },
    {
        "md": "en/articles/EN-049-Yoga_Taichi_Synergy-vagus-inversions-sinking.md", "out": "en/articles/vagus-inversions-sinking", "lang": "en",
        "title": "Vagus Nerve Stimulation Through Inversions and Sinking", "subtitle": "TaichiKB Health Article EN-49 · Yoga, Taichi, Flexibility",
        "crosslink": "/vi/articles/vi/articles/than-kinh-me-tau/", "crosslabel": "\U0001F1FB\U0001F1F3 Ti\u1ebfng Vi\u1ec7t",
    },
    {
        "md": "vi/articles/VI-049-Yoga_Taichi_Synergy-vagus-inversions-sinking.md", "out": "vi/articles/than-kinh-me-tau", "lang": "vi",
        "title": "Kích Thích Dây Thần Kinh Mê Tẩu: Đảo Ngược và Trầm Khí", "subtitle": "TaichiKB Health Article VI-49 · Yoga, Thái Cực, Giãn Cơ",
        "crosslink": "/en/articles/en/articles/vagus-inversions-sinking/", "crosslabel": "\U0001F1EC\U0001F1E7 English",
    },
    {
        "md": "en/articles/EN-050-Yoga_Taichi_Synergy-restorative-yoga-zhan-zhuang.md", "out": "en/articles/restorative-yoga-zhan-zhuang", "lang": "en",
        "title": "Restorative Yoga and Zhan Zhuang for Burnout Recovery", "subtitle": "TaichiKB Health Article EN-50 · Yoga, Taichi, Flexibility",
        "crosslink": "/vi/articles/vi/articles/phuc-hoi-kiet-suc/", "crosslabel": "\U0001F1FB\U0001F1F3 Ti\u1ebfng Vi\u1ec7t",
    },
    {
        "md": "vi/articles/VI-050-Yoga_Taichi_Synergy-restorative-yoga-zhan-zhuang.md", "out": "vi/articles/phuc-hoi-kiet-suc", "lang": "vi",
        "title": "Phục Hồi Kiệt Sức: Yoga Phục Hồi và Đứng Trụ", "subtitle": "TaichiKB Health Article VI-50 · Yoga, Thái Cực, Giãn Cơ",
        "crosslink": "/en/articles/en/articles/restorative-yoga-zhan-zhuang/", "crosslabel": "\U0001F1EC\U0001F1E7 English",
    },
]

def read_base_template(lang):
    if lang == "en":
        cand = [REPO_ROOT / "index_clean.html", REPO_ROOT / "index.html"]
    else:
        cand = [REPO_ROOT / "vi" / "index.html"]
    for c in cand:
        if c.exists():
            return c.read_text(encoding="utf-8")
    raise FileNotFoundError("no base template found")

def inline_md(text):
    """Bold, italic, links, inline code."""
    t = html.escape(text, quote=False)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)', r'<em>\1</em>', t)
    t = re.sub(r'`([^`]+?)`', r'<code>\1</code>', t)
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank" rel="noopener">\1</a>', t)
    return t

def md_to_html(md):
    lines = md.split("\n")
    out, i, n = [], 0, len(lines)
    in_list = False
    def close_list():
        nonlocal in_list
        if in_list:
            out.append("</ol>" if out and out[-2 if len(out)>1 else 0].find("<ol")>=0 else "</ul>")
            nonlocal_flag = None
    list_stack = []
    def close_open_lists():
        while list_stack:
            out.append("</ul>" if list_stack.pop() == "ul" else "</ol>")
    while i < n:
        line = lines[i].rstrip()
        s = line.strip()
        if not s:
            close_open_lists(); i += 1; continue
        # code fence
        if s.startswith("```"):
            close_open_lists()
            lang = s[3:].strip()
            out.append('<div class="code-block"><pre><code>')
            i += 1
            buf = []
            while i < n and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1  # skip closing fence
            code = "\n".join(buf)
            # raw HTML embeds (video iframes) passthrough
            if lang.lower() == "html" and "<iframe" in code:
                out.pop()  # remove the code-block opener
                out.append('<div class="video-embed">')
                out.append(code)
                out.append("</div>")
            else:
                out.append(html.escape(code))
                out.append("</code></pre></div>")
            continue
        # headings
        m = re.match(r'^(#{1,3})\s+(.*)$', s)
        if m:
            close_open_lists()
            level = len(m.group(1))
            txt = inline_md(m.group(2))
            if level == 1: out.append(f'<h1 class="article-title">{txt}</h1>')
            elif level == 2: out.append(f'<h2 class="section-heading" id="sec-{len(out)}">{txt}</h2>')
            else: out.append(f'<h3 class="sub-heading">{txt}</h3>')
            i += 1; continue
        # horizontal rule
        if re.match(r'^-{3,}$', s):
            close_open_lists(); out.append('<hr class="art-hr">'); i += 1; continue
        # blockquote
        if s.startswith(">"):
            close_open_lists()
            quote = []
            while i < n and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip().lstrip(">").strip())
                i += 1
            out.append('<blockquote class="callout-box">' + inline_md(" ".join(quote)) + "</blockquote>")
            continue
        # table
        if "|" in s and i+1 < n and re.match(r'^\s*\|[\s:\-|]+\|\s*$', lines[i+1]):
            close_open_lists()
            header = [c.strip() for c in s.strip("|").split("|")]
            i += 2
            rows = []
            while i < n and "|" in lines[i] and lines[i].strip():
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            out.append('<div class="table-scroll"><table class="data-table"><thead><tr>')
            out += [f"<th>{inline_md(c)}</th>" for c in header]
            out.append("</tr></thead><tbody>")
            for r in rows:
                out.append("<tr>" + "".join(f"<td>{inline_md(c)}</td>" for c in r) + "</tr>")
            out.append("</tbody></table></div>")
            continue
        # ordered list
        m = re.match(r'^\s*(\d+)[.)]\s+(.*)$', line)
        if m:
            if not list_stack or list_stack[-1] != "ol":
                close_open_lists(); list_stack.append("ol"); out.append("<ol>")
            out.append(f"<li>{inline_md(m.group(2))}</li>")
            i += 1; continue
        # unordered list
        if re.match(r'^\s*[-*]\s+', line):
            if not list_stack or list_stack[-1] != "ul":
                close_open_lists(); list_stack.append("ul"); out.append("<ul>")
            item = re.sub(r'^\s*[-*]\s+', '', line)
            out.append(f"<li>{inline_md(item)}</li>")
            i += 1; continue
        close_open_lists()
        # video/iframe raw html passthrough
        if s.startswith("<"):
            out.append(line); i += 1; continue
        out.append(f"<p>{inline_md(s)}</p>")
        i += 1
    close_open_lists()
    return "\n".join(out)

def article_css():
    return """
<style>
.article-wrap { max-width: 900px; margin: 0 auto; padding: 24px 16px 60px; }
.article-title { font-size: 1.8em; line-height: 1.3; margin: .3em 0 .6em; }
.article-hero { text-align:center; padding: 30px 10px 6px; }
.article-hero .page-subtitle { color: var(--muted, #777); }
.section-heading { margin-top: 2em; padding-bottom: .3em; border-bottom: 2px solid var(--accent,#8b2635); color: var(--accent,#8b2635); font-size: 1.35em; }
.sub-heading { margin-top: 1.4em; font-size: 1.1em; }
.art-hr { border: 0; border-top: 1px solid var(--border,#ddd); margin: 2em 0; }
.callout-box { border-left: 4px solid var(--accent,#8b2635); background: rgba(139,38,53,.06); padding: 14px 18px; margin: 1.5em 0; border-radius: 0 8px 8px 0; }
.dark-mode .callout-box { background: rgba(217,138,149,.08); }
.table-scroll { overflow-x: auto; margin: 1.4em 0; }
.data-table { border-collapse: collapse; width: 100%; font-size: .95em; }
.data-table th { background: var(--accent,#8b2635); color: #fff; text-align: left; padding: 8px 12px; }
.data-table td { border: 1px solid var(--border,#ddd); padding: 8px 12px; vertical-align: top; }
.dark-mode .data-table td { border-color: #3a3a3a; }
.code-block { background: #181818; color: #f0f0f0; border: 1px solid rgba(255,255,255,.15); border-radius: 8px; padding: 14px 16px; overflow-x: auto; font-size: .88em; line-height: 1.5; margin: 1.2em 0; }
.code-block pre, .code-block code { color: #f0f0f0 !important; background: transparent !important; margin: 0; }
.video-embed { margin: 1.5em 0; }
.vault-note { text-align: center; font-size: .9em; color: var(--muted,#777); }
article p { margin: .8em 0; }
article ol, article ul { margin: .8em 0 .8em 1.4em; }
article li { margin: .35em 0; }
</style>
"""

def build_article(a):
    template = read_base_template(a["lang"])
    md = (REPO_ROOT / a["md"]).read_text(encoding="utf-8")
    # strip front matter
    md = re.sub(r'^---\n.*?\n---\n', '', md, count=1, flags=re.S)
    body_html = md_to_html(md)
    lang_sw = f'<a class="lang-switch" href="{a["crosslink"]}">{a["crosslabel"]}</a>'
    vault = f'<a href="{VAULT_URL}" target="_blank" rel="noopener">299 grounded sources</a>'
    main = f"""<main class="health-article" role="main">
{article_css()}
<article class="article-wrap">
    <header class="article-hero">
        <p class="page-subtitle">{html.escape(a["subtitle"])}</p>
        <h1 class="article-title">{html.escape(a["title"])}</h1>
        <p class="vault-note">Health, TCM, Energy Medicine, Yoga, Taichi & Qigong Vault · {vault}</p>
        <p>{lang_sw}</p>
    </header>
    {body_html}
    <footer class="page-footer">
        <p><a href="/{a["lang"]}/">← Back to {a["lang"].upper()} Home</a></p>
    </footer>
</article>
</main>"""
    # inject into template
    m = template.find("<main")
    if m == -1:
        m = template.find("<article")
    e = template.find("</main>")
    if e == -1:
        e = template.find("</article>")
    if m != -1 and e != -1:
        html_out = template[:m] + main + template[e+7:]
    else:
        html_out = template + main
    outdir = REPO_ROOT / a["out"]
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "index.html").write_text(html_out, encoding="utf-8")
    print(f"OK built {outdir / 'index.html'} ({len(html_out)//1024} KB)")

def main():
    for a in ARTICLES:
        build_article(a)

if __name__ == "__main__":
    main()
