#!/usr/bin/env python3
"""Split bilingual side-by-side MD chapters into separate EN and VI files.
Source layout is per-row "| EN | VI |". Output keeps headings, cues, drills split."""
import re, sys
from pathlib import Path

SRC_DIR = Path("D:/Taichi-Health-Finance/Intranet/taichikb_repo/scripts/chapters")
OUT_DIR = Path("D:/Taichi-Health-Finance/Intranet/taichikb_repo/scripts/split")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Strip the in-line EN/VN markers from headings
def clean(s, lang):
    s = s.strip()
    # Remove trailing "| VN ..." part for EN
    m = re.match(r'^(.*?)\s*\|\s*(.+)$', s)
    if m:
        if lang == "en":
            return m.group(1).strip()
        else:
            return m.group(2).strip()
    return s

def split_table_row(line):
    """Split `| EN | VN |` into 2 strings (without leading/trailing pipes)."""
    parts = [p.strip() for p in line.strip().strip('|').split('|')]
    if len(parts) >= 2:
        return parts[0], parts[1]
    return line, line

def split_doc(content):
    """Yields (en_line, vi_line) tuples."""
    lines = content.split('\n')
    out_en, out_vi = [], []
    in_table = False
    for ln in lines:
        s = ln.strip()
        if not s:
            out_en.append(''); out_vi.append(''); in_table = False; continue
        if s.startswith('|'):
            in_table = True
            # Table separator / divider (---)
            if re.match(r'^\|[\s\-|]+\|$', s):
                out_en.append(ln); out_vi.append(ln); continue
            en, vi = split_table_row(ln)
            # For table rows, rebuild as single-lang lines
            out_en.append(f"| {en} |")
            out_vi.append(f"| {vi} |")
        elif s.startswith('#'):
            # Heading - split into both languages
            en = clean(s, "en")
            vi = clean(s, "vi")
            out_en.append(en); out_vi.append(vi)
        else:
            # Blockquote / paragraph / card lines may contain " | " separator
            if ' | ' in s and (s.startswith('>') or s.startswith('*') or s.startswith('- ')):
                # inline separator
                try:
                    en, vi = s.split(' | ', 1)
                    out_en.append(en); out_vi.append(vi); continue
                except ValueError:
                    pass
            out_en.append(ln); out_vi.append(ln)
    return ('\n'.join(out_en).strip(), '\n'.join(out_vi).strip())

for src in sorted(SRC_DIR.glob("ch*.md")):
    content = src.read_text(encoding='utf-8')
    en, vi = split_doc(content)
    n = src.stem  # e.g. "ch06"
    (OUT_DIR / f"{n}.en.md").write_text(en, encoding='utf-8')
    (OUT_DIR / f"{n}.vi.md").write_text(vi, encoding='utf-8')
    print(f"{n}: en={len(en)} chars, vi={len(vi)} chars")
