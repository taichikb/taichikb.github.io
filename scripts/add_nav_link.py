#!/usr/bin/env python3
"""Add the 'All Articles' entry to every page's top nav.

The site has no nav include - the same <nav class="site-nav"> block is written
out in every page, in a couple of variants (English labels, Vietnamese labels,
and a few older subsets of the menu). So the link has to be inserted per file.

Insertion rules, in order:
  1. skip a page whose nav already links to /all-articles/  (idempotent)
  2. insert immediately before the language-switch link, so that link stays
     last in the menu
  3. if there is no language switch, insert before </nav>

The label follows the language of the nav block: "All Articles" for the English
menu, "Tất Cả Bài Viết" for the Vietnamese one.

Usage
-----
  python add_nav_link.py --repo D:\\path\\to\\taichinow.github.io --dry-run
  python add_nav_link.py --repo D:\\path\\to\\taichinow.github.io
"""

from __future__ import annotations

import argparse
import os
import re
import sys

NAV_OPEN = re.compile(r'<nav\s+class="site-nav"\s*>', re.I)
NAV_BLOCK = re.compile(r'(<nav\s+class="site-nav"\s*>)(.*?)(</nav>)', re.S | re.I)
LANG_SWITCH = re.compile(r'[ \t]*<a\s+href="/(?:en|vi)/"\s+class="lang-switch"[^>]*>.*?</a>',
                         re.S | re.I)
EXISTING = re.compile(r'href="/all-articles/"', re.I)
VI_MARKERS = ("Trang Chủ", "Kỹ Thuật", "Thư Viện Sách", "Triết Lý", "Liên Hệ")

HREF = "/all-articles/"
LABEL_EN = "All Articles"
LABEL_VI = "Tất Cả Bài Viết"


def is_vietnamese(nav_html: str) -> bool:
    return any(m in nav_html for m in VI_MARKERS)


def add_link(html: str) -> tuple[str, str]:
    """Return (new_html, status). status is one of: added-en, added-vi, has, none."""
    m = NAV_BLOCK.search(html)
    if not m:
        return html, "none"
    nav_html = m.group(2)
    if EXISTING.search(nav_html):
        return html, "has"

    label = LABEL_VI if is_vietnamese(nav_html) else LABEL_EN
    link = f'<a href="{HREF}" class="">{label}</a>'

    lang = LANG_SWITCH.search(nav_html)
    if lang:
        new_nav = nav_html[: lang.start()] + link + "\n" + nav_html[lang.start():]
    else:
        new_nav = nav_html.rstrip() + "\n" + link + "\n"

    new_html = html[: m.start(2)] + new_nav + html[m.end(2):]
    return new_html, ("added-vi" if label == LABEL_VI else "added-en")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo", required=True)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)

    repo = os.path.abspath(args.repo)
    counts = {"added-en": 0, "added-vi": 0, "has": 0, "none": 0}
    changed: list[str] = []

    for root, dirs, files in os.walk(repo):
        dirs[:] = [d for d in dirs if d != ".git"]
        for name in files:
            if not name.endswith((".html", ".htm")):
                continue
            path = os.path.join(root, name)
            try:
                with open(path, encoding="utf-8") as fh:
                    html = fh.read()
            except (UnicodeDecodeError, OSError):
                continue
            if not NAV_OPEN.search(html):
                continue
            new_html, status = add_link(html)
            counts[status] += 1
            if status in ("added-en", "added-vi"):
                changed.append(os.path.relpath(path, repo).replace("\\", "/"))
                if not args.dry_run:
                    with open(path, "w", encoding="utf-8", newline="") as fh:
                        fh.write(new_html)

    print("pages with a site-nav that already link /all-articles/ : %d" % counts["has"])
    print("pages updated (English label)                          : %d" % counts["added-en"])
    print("pages updated (Vietnamese label)                       : %d" % counts["added-vi"])
    if args.dry_run:
        print("dry run - nothing written")
    for p in changed[:15]:
        print("   " + p)
    if len(changed) > 15:
        print("   ... and %d more" % (len(changed) - 15))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
