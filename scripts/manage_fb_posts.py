#!/usr/bin/env python3
"""List and delete posts on the TaichiNOW Facebook Page via the Graph API.

Why this exists
---------------
The TaichiNOW page still carries the posts published by the old pipeline
("Published by TaichiNOW"). Those are not the new illustrated articles, and the
page should be cleaned so the new queue owns the timeline.

Safety model - read this before running anything
------------------------------------------------
Deleting a Page post is public and irreversible. So:

  * `--list` and `--plan` are READ-ONLY. Always start there.
  * A delete needs BOTH a selector (`--ids-file`, `--ids`, `--before`) AND
    `--confirm`. Neither alone will delete anything.
  * Every candidate is printed with its post ID, date and message excerpt
    BEFORE anything is removed.
  * Posts created on/after `--protect-from` (default: 2026-10-01, when the new
    queue started) are NEVER deleted unless you pass `--allow-new`.
  * `--limit` (default 25) caps one run, so a mistake cannot wipe the page.
  * Each deletion is verified with a follow-up GET, and every action is
    appended to `logs/fb_delete_log.jsonl`.

Credentials
-----------
Needs a Page access token with `pages_read_engagement` + `pages_manage_posts`:

    export FB_PAGE_TOKEN='EAAG...'      # long-lived Page token
    export FB_PAGE_ID='1234567890'      # optional; --whoami resolves it

Usage
-----
  python manage_fb_posts.py --whoami
  python manage_fb_posts.py --list --out fb_posts.json
  python manage_fb_posts.py --plan --before 2026-10-01
  python manage_fb_posts.py --before 2026-10-01 --confirm
  python manage_fb_posts.py --ids-file old_ids.txt --confirm
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

GRAPH = "https://graph.facebook.com/v21.0"
HERE = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(os.path.dirname(HERE), "logs", "fb_delete_log.jsonl")
PIPELINE_START = "2026-10-01"          # the day the new queue began posting
FIELDS = "id,created_time,message,permalink_url,is_published"


# --------------------------------------------------------------------------- #
# http
# --------------------------------------------------------------------------- #
def api(method: str, path: str, token: str, params: dict | None = None):
    """Return (ok, payload). Never raises on an API error - returns the body."""
    params = dict(params or {})
    params["access_token"] = token
    url = f"{GRAPH}/{path.lstrip('/')}"
    if method == "GET":
        url += "?" + urllib.parse.urlencode(params)
        req = urllib.request.Request(url, method="GET")
    else:
        req = urllib.request.Request(url, data=urllib.parse.urlencode(params).encode(),
                                     method=method)
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            return True, json.loads(resp.read().decode("utf-8", "replace") or "{}")
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", "replace")
        try:
            return False, json.loads(body)
        except Exception:
            return False, {"error": {"message": body[:400], "code": exc.code}}
    except Exception as exc:                                   # network etc.
        return False, {"error": {"message": str(exc)}}


def err_text(payload) -> str:
    e = (payload or {}).get("error") or {}
    if isinstance(e, dict):
        return "%s (code %s, subcode %s)" % (e.get("message", "?"),
                                             e.get("code", "?"),
                                             e.get("error_subcode", "?"))
    return str(e)


def token_from_env() -> str:
    tok = os.environ.get("FB_PAGE_TOKEN", "").strip()
    if not tok:
        print("error: FB_PAGE_TOKEN is not set.", file=sys.stderr)
        print("       Get a long-lived Page token with pages_read_engagement +",
              file=sys.stderr)
        print("       pages_manage_posts from the Graph API Explorer, then export it.",
              file=sys.stderr)
        raise SystemExit(2)
    return tok


# --------------------------------------------------------------------------- #
# posts
# --------------------------------------------------------------------------- #
def fetch_posts(page_id: str, token: str, cap: int = 1000) -> list[dict]:
    posts, url_path, params = [], f"{page_id}/published_posts", {
        "fields": FIELDS, "limit": 100}
    while len(posts) < cap:
        ok, body = api("GET", url_path, token, params)
        if not ok:
            print("error: %s" % err_text(body), file=sys.stderr)
            raise SystemExit(3)
        posts.extend(body.get("data") or [])
        nxt = ((body.get("paging") or {}).get("next")) or ""
        if not nxt:
            break
        # the paging cursor already carries the token; re-send path + cursor
        q = urllib.parse.parse_qs(urllib.parse.urlparse(nxt).query)
        url_path = f"{page_id}/published_posts"
        params = {k: v[0] for k, v in q.items() if k != "access_token"}
    return posts


def created_date(post: dict) -> str:
    return (post.get("created_time") or "")[:10]


def one_line(post: dict, width: int = 78) -> str:
    msg = (post.get("message") or "").replace("\n", " ").strip()
    if not msg:
        msg = "(no text — photo or link post)"
    return msg[:width] + ("…" if len(msg) > width else "")


def describe(posts: list[dict]) -> None:
    print("%-22s  %-10s  %s" % ("POST ID", "DATE", "MESSAGE"))
    print("-" * 110)
    for p in posts:
        print("%-22s  %-10s  %s" % (p.get("id", "?"), created_date(p) or "?",
                                    one_line(p)))


def log_action(entry: dict) -> None:
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    entry = dict(entry, at=datetime.now(timezone.utc).isoformat(timespec="seconds"))
    with open(LOG_PATH, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(entry, ensure_ascii=False) + "\n")


def select_posts(posts: list[dict], ids: list[str] | None = None,
                 before: str | None = None, protect_from: str | None = None,
                 allow_new: bool = False) -> tuple[list[dict], list[dict], list[str]]:
    """Pick the posts a delete would target.

    Returns (selected, protected, notes). `protected` holds posts that matched
    the selector but sit on/after `protect_from` - they are reported and then
    dropped, so a date typo cannot wipe the new queue's output.
    """
    notes: list[str] = []
    if ids:
        by_id = {p["id"]: p for p in posts}
        selected = []
        for i in ids:
            if i in by_id:
                selected.append(by_id[i])
            else:
                notes.append("id %s is not among the Page's published posts" % i)
    elif before:
        selected = [p for p in posts
                    if created_date(p) and created_date(p) < before]
    else:
        return [], [], ["no selector given"]

    protected: list[dict] = []
    if not allow_new and protect_from:
        protected = [p for p in selected if created_date(p) >= protect_from]
        selected = [p for p in selected if created_date(p) < protect_from]
    return selected, protected, notes


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #
def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--whoami", action="store_true",
                    help="resolve the Page behind FB_PAGE_TOKEN and exit")
    ap.add_argument("--list", action="store_true", help="list Page posts (read-only)")
    ap.add_argument("--plan", action="store_true",
                    help="list what a delete WOULD remove, then stop (read-only)")
    ap.add_argument("--out", help="write the fetched posts to this JSON file")
    ap.add_argument("--ids", help="comma-separated post ids to delete")
    ap.add_argument("--ids-file", help="file with one post id per line")
    ap.add_argument("--before", metavar="YYYY-MM-DD",
                    help="select posts created before this date")
    ap.add_argument("--protect-from", default=PIPELINE_START, metavar="YYYY-MM-DD",
                    help=f"never delete posts from this date on (default {PIPELINE_START})")
    ap.add_argument("--allow-new", action="store_true",
                    help="lift --protect-from. Deletes recent posts too. Dangerous.")
    ap.add_argument("--limit", type=int, default=25,
                    help="max posts to delete in one run (default 25)")
    ap.add_argument("--confirm", action="store_true",
                    help="actually delete. Without it nothing is removed.")
    ap.add_argument("--page-id", default=os.environ.get("FB_PAGE_ID", ""))
    ap.add_argument("--sleep", type=float, default=0.4,
                    help="pause between deletes, seconds (default 0.4)")
    args = ap.parse_args(argv)

    token = token_from_env()

    page_id = args.page_id.strip()
    if not page_id:
        ok, body = api("GET", "me", token, {"fields": "id,name,username"})
        if not ok:
            print("error resolving the page: %s" % err_text(body), file=sys.stderr)
            return 3
        page_id = body.get("id", "")
        if args.whoami or not page_id:
            print("page id   : %s" % page_id)
            print("page name : %s" % body.get("name", "?"))
            print("username  : %s" % body.get("username", "?"))
    elif args.whoami:
        ok, body = api("GET", page_id, token, {"fields": "id,name,username"})
        print("page id   : %s" % page_id)
        if ok:
            print("page name : %s" % body.get("name", "?"))
            print("username  : %s" % body.get("username", "?"))

    if args.whoami and not (args.list or args.plan or args.before or args.ids
                            or args.ids_file):
        return 0
    if not page_id:
        print("error: could not determine the Page id; pass --page-id", file=sys.stderr)
        return 3

    print("page: %s" % page_id)
    print()
    posts = fetch_posts(page_id, token)
    posts.sort(key=lambda p: p.get("created_time") or "")
    print("%d post(s) on the Page." % len(posts))
    print()

    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            json.dump(posts, fh, ensure_ascii=False, indent=2)
        print("wrote %s" % args.out)
        print()

    if args.list and not (args.plan or args.before or args.ids or args.ids_file):
        describe(posts)
        return 0

    # ---- select ----------------------------------------------------------- #
    wanted: list[str] = []
    if args.ids:
        wanted += [i.strip() for i in args.ids.split(",") if i.strip()]
    if args.ids_file:
        with open(args.ids_file, encoding="utf-8") as fh:
            wanted += [ln.strip() for ln in fh
                       if ln.strip() and not ln.startswith("#")]

    selected, protected, notes = select_posts(
        posts, ids=wanted or None, before=args.before,
        protect_from=args.protect_from, allow_new=args.allow_new)

    for n in notes:
        print("  note: %s" % n)
    if notes and not selected and not protected:
        print("nothing to do.")
        return 0

    if protected:
        print("%d selected post(s) are on/after %s and are PROTECTED:"
              % (len(protected), args.protect_from))
        for p in protected:
            print("   %-22s %s  %s" % (p["id"], created_date(p), one_line(p, 50)))
        print("   (pass --allow-new to include them)")
        print()

    if not selected:
        print("nothing selected — no post matches the selector after protection.")
        return 0

    print("WOULD DELETE %d post(s):" % len(selected))
    describe(selected)
    print()

    if args.plan:
        print("plan only — nothing deleted. Re-run with --confirm to delete.")
        return 0

    if not args.confirm:
        print("refusing to delete: --confirm was not given.")
        print("This is a public, irreversible action. Re-run with --confirm.")
        return 1

    todo = selected[: max(0, args.limit)]
    if len(selected) > len(todo):
        print("capped at --limit %d; %d post(s) left for a later run."
              % (args.limit, len(selected) - len(todo)))
        print()

    deleted = failed = 0
    for i, post in enumerate(todo, 1):
        pid = post["id"]
        ok, body = api("DELETE", pid, token)
        if not ok:
            print("  [%d/%d] FAILED %s — %s" % (i, len(todo), pid, err_text(body)))
            log_action({"id": pid, "date": created_date(post), "ok": False,
                        "detail": err_text(body), "message": one_line(post, 200)})
            failed += 1
            continue
        # verify it is really gone
        chk_ok, _ = api("GET", pid, token, {"fields": "id"})
        print("  [%d/%d] deleted %s  %s  %s"
              % (i, len(todo), pid, created_date(post), one_line(post, 50)))
        log_action({"id": pid, "date": created_date(post), "ok": True,
                    "verified_gone": not chk_ok, "message": one_line(post, 200)})
        deleted += 1
        time.sleep(max(0.0, args.sleep))

    print()
    print("deleted %d, failed %d, remaining in selection %d"
          % (deleted, failed, max(0, len(selected) - deleted - failed)))
    print("log: %s" % LOG_PATH)
    return 0 if not failed else 4


if __name__ == "__main__":
    raise SystemExit(main())
