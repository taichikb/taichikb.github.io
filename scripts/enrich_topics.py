#!/usr/bin/env python3
"""Enrich all New-Topics pages with 2 additional substantive cards each.

Data lives in enrich_topics_data.py (ALL_DATA dict: slug -> [(en,vi), ...]).
This script is a runner: it inserts those cards before each page's
master-cue section.
"""
from pathlib import Path
import re, sys

REPO = Path("D:/Taichi-Health-Finance/Intranet/taichikb_repo")
sys.path.insert(0, str(REPO / "scripts"))
from enrich_topics_data import ALL_DATA

# Regex: find the master-cue heading. It appears in two shapes:
#  - on the <section> wrapper (older topics):  <section ... background:var(--ink); ...><h3 ...>Master Cue|Câu Nhắc Tổng</h3>
#  - on the <h3> itself (newer topics):         <h3 style="background:var(--ink); ...">Master Cue|Câu Nhắc Tổng</h3>
# In both cases the cue block begins with one of two strings; we anchor on the <h3> heading.
PATTERN = re.compile(
    r'(<h3[^>]*>(?:Master Cue|Câu Nhắc Tổng)</h3>)'
)


def insert_new_cards():
    inserted = 0
    skipped = 0
    for slug, pairs in ALL_DATA.items():
        for lang in ("en", "vi"):
            page = REPO / lang / "techniques" / slug / "index.html"
            if not page.exists():
                skipped += 1
                continue
            text = page.read_text(encoding="utf-8")
            m = PATTERN.search(text)
            if not m:
                print(f"  WARN: no master-cue in {lang}/{slug}")
                skipped += 1
                continue
            # Walk backward from the <h3> to find the start of the enclosing <section>
            h3_start = m.start()
            section_start = text.rfind('    <section class="technique-card"', 0, h3_start)
            if section_start < 0:
                # The cue is in a different shape; just insert before the <h3>
                section_start = h3_start
            if lang == "en":
                cards_html = "".join(
                    f'    <section class="technique-card">\n  {ec}\n    </section>\n'
                    for ec, _ in pairs
                )
            else:
                cards_html = "".join(
                    f'    <section class="technique-card">\n  {vc}\n    </section>\n'
                    for _, vc in pairs
                )
            new_text = text[:section_start] + cards_html + "\n" + text[section_start:]
            page.write_text(new_text, encoding="utf-8")
            inserted += 1
    print(f"\nupdated {inserted} files, skipped {skipped}")


if __name__ == "__main__":
    print(f"--- Enriching {len(ALL_DATA)} topics with 2 new cards each ---")
    insert_new_cards()
