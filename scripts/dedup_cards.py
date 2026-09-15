#!/usr/bin/env python3
"""Dedup technique cards across all 30 topics (EN + VI) based on heading key.

Uses string-level processing to avoid lxml dependency. Each technique-card
block is delimited by <section class="technique-card"> tags.
"""
import re
from pathlib import Path

REPO = Path("D:/Taichi-Health-Finance/Intranet/taichikb_repo")

def extract_cards(text):
    """Split text into (prefix, [card_blocks]).

    Cards are contiguous <section class="technique-card">...</section> blocks.
    The prefix is everything before the first card.
    """
    pattern = re.compile(r'<section class="technique-card"', re.IGNORECASE)
    positions = [m.start() for m in pattern.finditer(text)]
    if not positions:
        return "", []

    prefix = text[:positions[0]]
    cards = []
    for i, start in enumerate(positions):
        end = positions[i + 1] if i + 1 < len(positions) else len(text)
        cards.append(text[start:end])
    return prefix, cards

def get_heading_key(card_html):
    """Extract the heading text from a card (used for dedup key)."""
    m = re.search(r'<h3[^>]*>(.*?)</h3>', card_html, re.DOTALL | re.IGNORECASE)
    if m:
        inner = m.group(1)
        text = re.sub(r'<[^>]+>', '', inner).strip()
        return text
    return card_html[:200]

def dedup_page(page_path: Path):
    text = page_path.read_text(encoding="utf-8")
    prefix, cards = extract_cards(text)
    seen = set()
    unique_cards = []
    removed = 0
    for card in cards:
        key = get_heading_key(card)
        if key in seen:
            removed += 1
        else:
            seen.add(key)
            unique_cards.append(card)

    if removed > 0:
        new_text = prefix + "".join(unique_cards)
        page_path.write_text(new_text, encoding="utf-8")
        print(f"  {page_path.relative_to(REPO)}: removed {removed} dupes, kept {len(unique_cards)}")
    return removed

total_removed = 0
for lang in ("en", "vi"):
    techniques_dir = REPO / lang / "techniques"
    if not techniques_dir.exists():
        continue
    for slug_dir in sorted(techniques_dir.iterdir()):
        if not slug_dir.is_dir():
            continue
        page = slug_dir / "index.html"
        if page.exists():
            total_removed += dedup_page(page)

print(f"\nTotal duplicate cards removed: {total_removed}")
