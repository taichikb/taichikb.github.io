#!/usr/bin/env python3
"""Merge the 4 batch-1 entries from enrich_batch1_extra.py into enrich_topics_data.py."""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "extra",
    Path("D:/Taichi-Health-Finance/Intranet/taichikb_repo/scripts/enrich_batch1_extra.py")
)
extra = importlib.util.module_from_spec(spec)
spec.loader.exec_module(extra)

data_path = Path("D:/Taichi-Health-Finance/Intranet/taichikb_repo/scripts/enrich_topics_data.py")
text = data_path.read_text(encoding="utf-8")

# Find ALL_DATA = { and inject new keys after the opening brace
marker = "ALL_DATA = {"
idx = text.find(marker)
if idx < 0:
    raise SystemExit("marker ALL_DATA = { not found")

# Build the new key-value pairs
pairs = []
for slug in ("peng", "ji", "an", "xu-thuc"):
    entries = extra.DATA[slug]
    pairs.append(f'    "{slug}": [\n')
    for en, vi in entries:
        pairs.append(f'        (\n')
        pairs.append(f'            {en!r}\n')
        pairs.append(f'            ,\n')
        pairs.append(f'            {vi!r}\n')
        pairs.append(f'        ),\n')
    pairs.append(f'    ],\n')

insertion = "".join(pairs)
new_text = text[:idx + len(marker)] + "\n" + insertion + text[idx + len(marker):]
data_path.write_text(new_text, encoding="utf-8")
print(f"merged 4 batch-1 topics, new file size: {len(new_text)} bytes")

# Verify
import sys
sys.path.insert(0, str(data_path.parent))
import enrich_topics_data as etd
for slug in ("peng", "ji", "an", "xu-thuc"):
    entries = etd.ALL_DATA.get(slug, [])
    print(f"  {slug}: {len(entries)} entries")
    for i, e in enumerate(entries):
        if len(e) != 2:
            print(f"    BAD: entry {i} has {len(e)} items")
