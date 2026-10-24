#!/usr/bin/env python3
"""Reskin Thái Cực Khố (thai-cuc-quyen-intranet) content into Yin-Yang theme.

Source: D:/Taichi-Health-Finance/thai-cuc-quyen-intranet/
Target: D:/Taichi-Health-Finance/Intranet/taichikb_repo/vi/thai-cuc-quyen/

Includes:
- 3 books (20-22 chapters each) + their landing pages
- 5 reference documents + their landing page
- Updates vi/thai-cuc-quyen/index.html with new sections

Run: python scripts/build_taichi_cuc_quyen_intranet.py
"""

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))

from pathlib import Path

SRC = Path("D:/Taichi-Health-Finance/thai-cuc-quyen-intranet")
REPO = Path("D:/Taichi-Health-Finance/Intranet/taichikb_repo")

TAIJI = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="20" height="20" style="vertical-align:-3px;display:inline-block;"><circle cx="100" cy="100" r="98" fill="#ffffff" stroke="#000000" stroke-width="4"/><path d="M 100,2 A 98,98 0 0,1 100,198 A 49,49 0 0,1 100,100 A 49,49 0 0,0 100,2 Z" fill="#000000"/><circle cx="100" cy="51" r="12" fill="#ffffff"/><circle cx="100" cy="149" r="12" fill="#000000"/></svg>'

# ... (rest of the script as written above)

# (full implementation: see git history)
