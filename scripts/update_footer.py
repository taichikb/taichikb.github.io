#!/usr/bin/env python3
"""Footer-text migration across all generated HTML + the build script."""
from pathlib import Path

REPO = Path("D:/Taichi-Health-Finance/Intranet/taichikb_repo")

# Three independent substitutions
SUBS = [
    # 1. Thái Cực Quyền Việt Nam → Thái Cực Quyền Việt Nam
    ("Thái Cực Quyền Việt Nam", "Thái Cực Quyền Việt Nam"),
    # 2. <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="20" height="20" style="vertical-align:-3px;display:inline-block;"><circle cx="100" cy="100" r="98" fill="#ffffff" stroke="#000000" stroke-width="4"/><path d="M 100,2 A 98,98 0 0,1 100,198 A 49,49 0 0,1 100,100 A 49,49 0 0,0 100,2 Z" fill="#000000"/><circle cx="100" cy="51" r="12" fill="#ffffff"/><circle cx="100" cy="149" r="12" fill="#000000"/></svg> (tennis ball emoji) → taichi logo SVG
    ("<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="20" height="20" style="vertical-align:-3px;display:inline-block;"><circle cx="100" cy="100" r="98" fill="#ffffff" stroke="#000000" stroke-width="4"/><path d="M 100,2 A 98,98 0 0,1 100,198 A 49,49 0 0,1 100,100 A 49,49 0 0,0 100,2 Z" fill="#000000"/><circle cx="100" cy="51" r="12" fill="#ffffff"/><circle cx="100" cy="149" r="12" fill="#000000"/></svg>", '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="20" height="20" style="vertical-align:-3px;display:inline-block;"><circle cx="100" cy="100" r="98" fill="#ffffff" stroke="#000000" stroke-width="4"/><path d="M 100,2 A 98,98 0 0,1 100,198 A 49,49 0 0,1 100,100 A 49,49 0 0,0 100,2 Z" fill="#000000"/><circle cx="100" cy="51" r="12" fill="#ffffff"/><circle cx="100" cy="149" r="12" fill="#000000"/></svg>'),
    # 3. "bởi Phạm Đức Hải" / "bởi Henry Phạm" → "bởi Phạm Đức Hải"
    ("bởi Phạm Đức Hải", "bởi Phạm Đức Hải"),
]

# Walk all HTML files in the repo
html_files = []
for p in REPO.rglob("*.html"):
    # Skip the deploy/ and docs/ areas that are not part of the live site
    rel = p.relative_to(REPO).as_posix()
    if rel.startswith("deploy/"):
        continue
    html_files.append(p)

# Also include Python build scripts that emit the same footer (so future
# rebuilds don't reintroduce the old text).
for p in REPO.rglob("*.py"):
    rel = p.relative_to(REPO).as_posix()
    if rel.startswith("deploy/"):
        continue
    html_files.append(p)

changed = 0
for f in html_files:
    try:
        text = f.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    new = text
    for old, replacement in SUBS:
        if old in new:
            new = new.replace(old, replacement)
    if new != text:
        f.write_text(new, encoding="utf-8")
        changed += 1

print(f"updated {changed} files")

# Patch the build script with the same substitutions
build_script = REPO / "scripts" / "build_topics.py"
text = build_script.read_text(encoding="utf-8")
# Use placeholders since the SVG string is identical and would self-match
new_text = text
for old, replacement in SUBS:
    new_text = new_text.replace(old, replacement)
if new_text != text:
    build_script.write_text(new_text, encoding="utf-8")
    print("patched scripts/build_topics.py")
else:
    print("scripts/build_topics.py: no change")
