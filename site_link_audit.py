#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
site_link_audit.py -- resolve every relative link/asset in a set of HTML pages
against the local repo tree and report broken ones.

Usage:
    python site_link_audit.py <repo> <page> [<page> ...]
    python site_link_audit.py <repo> --all
"""
import os
import re
import sys
from urllib.parse import unquote

LINK_RE = re.compile(r'(?:href|src)="([^"]+)"')
SKIP = ('http', '//', '#', 'mailto:', 'data:', 'javascript:', 'tel:')
# JS template fragments are not real URLs (e.g. href="/'+l.href+'" )
JS_LIKE = ("'", '"', '+', '.', '{', '}', ' ')


def resolve(repo, page, href):
    """Return (ok, resolved_path_or_reason)."""
    if href.startswith(SKIP):
        return True, None
    if any(ch in href for ch in JS_LIKE):
        return True, None          # JS template fragment, not a URL
    tgt = href.split('#')[0].split('?')[0]
    if not tgt:
        return True, None
    tgt = unquote(tgt)
    if href.startswith('/'):
        p = os.path.join(repo, tgt.lstrip('/'))
    else:
        p = os.path.normpath(os.path.join(os.path.dirname(page), tgt))
    if os.path.exists(p):
        return True, None
    # a directory-style link /foo/ resolves to /foo/index.html
    if href.endswith('/') and os.path.exists(os.path.join(p, 'index.html')):
        return True, None
    return False, p


def audit(repo, pages):
    broken = []
    checked = 0
    for page in pages:
        with open(page, encoding='utf-8', errors='replace') as f:
            h = f.read()
        for href in LINK_RE.findall(h):
            checked += 1
            ok, p = resolve(repo, page, href)
            if not ok:
                broken.append((os.path.relpath(page, repo), href, p))
    return checked, broken


def main():
    repo = os.path.abspath(sys.argv[1])
    args = sys.argv[2:]
    if args == ['--all']:
        pages = []
        for root, dirs, files in os.walk(repo):
            dirs[:] = [d for d in dirs if d not in ('.git', 'node_modules', '.workbuddy-ai')]
            for f in files:
                if f.endswith('.html'):
                    pages.append(os.path.join(root, f))
    else:
        pages = []
        for a in args:
            p = os.path.join(repo, a)
            if os.path.isdir(p):
                for root, dirs, files in os.walk(p):
                    dirs[:] = [d for d in dirs if d not in ('.git', 'node_modules')]
                    for f in files:
                        if f.endswith('.html'):
                            pages.append(os.path.join(root, f))
            else:
                pages.append(p)
    checked, broken = audit(repo, pages)
    print('checked %d links in %d pages' % (checked, len(pages)))
    if not broken:
        print('ALL LINKS OK')
        return 0
    print('BROKEN: %d' % len(broken))
    for page, href, p in broken[:80]:
        print('  %-42s -> %s' % (page, href))
    if len(broken) > 80:
        print('  ... and %d more' % (len(broken) - 80))
    return 1


if __name__ == '__main__':
    sys.exit(main())
