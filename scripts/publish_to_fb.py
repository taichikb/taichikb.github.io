# -*- coding: utf-8 -*-
"""
publish_to_fb.py — TaichiNow -> Facebook Page publisher.

Reads a page from the local taichinow.github.io clone, builds a clean Facebook
post (title + excerpt + live link + optional image), and pushes it to a
Make.com "Custom Webhook" that is wired to Facebook Pages -> Create a Post.

    local repo  ->  this script  ->  Make.com webhook  ->  TaichiNow FB Page

Optionally it can bypass Make and publish straight through the Meta Graph API
when FB_PAGE_ID + FB_PAGE_TOKEN are provided (--direct).

Nothing is sent unless --send is passed. Without it you get a preview.

Usage
-----
  python publish_to_fb.py --list
  python publish_to_fb.py --slug thái-cực-quyền-luận-bản-nguyên-vô-cực
  python publish_to_fb.py --slug <slug> --send
  python publish_to_fb.py --latest --send
  python publish_to_fb.py --file vi/articles/foo/index.html --send
  python publish_to_fb.py --slug <slug> --send --direct      # Graph API
"""

import argparse
import html as html_mod
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from html.parser import HTMLParser

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
# The site repo this script lives in (scripts/ is always one level below the
# root). Derived from __file__ on purpose: GitHub Actions checks the site out
# to a different absolute path on Linux, and a hardcoded Windows path made
# content_paths() walk a directory that does not exist - so --emit silently
# reported "no unpublished posts found" in CI.
REPO_DEFAULT = os.path.dirname(HERE)
SITE_BASE_DEFAULT = "https://taichinow.github.io"
CONFIG_PATH = os.path.join(HERE, "fb_publish_config.json")
LOG_PATH = os.path.join(REPO_DEFAULT, "logs", "fb_publish_log.jsonl")

# Make.com webhook zones. A token only lives in one zone; we try them in order
# and stop at the first one that answers. A 404 means nothing was published,
# so falling through to the next zone is safe (no duplicate posts).
MAKE_ZONES = ["us1", "us2", "eu1", "eu2"]

DEFAULT_CONFIG = {
    # Credentials are deliberately NOT baked in: this file is committed to a
    # public repo. Supply them via the MAKE_WEBHOOK_URL / MAKE_WEBHOOK_KEY
    # environment variables (GitHub Actions secret, or scripts/fb_publish_config.json
    # which stays out of git).
    "make_webhook_key": "",
    "make_webhook_url": "",
    "make_zone": "",
    "repo": REPO_DEFAULT,
    "site_base": SITE_BASE_DEFAULT,
    "hashtags": "#ThaiCucQuyen #TaichiNow #SucKhoe",
    # Facebook cannot label a Page post with a person's name, so a signature
    # line is the only way to put a name in front of readers.
    "signature": "— Phạm Đức Hải",
    "max_chars": 600,
    # facebook/posts is the TaichiNOW page archive: never a source, only the
    # "already published" reference used for de-duplication.
    "source_dirs": ["vi/articles", "techniques", "articles"],
    "default_image": "",
    "fb_page_id": "",
}


# --------------------------------------------------------------------------- #
# config
# --------------------------------------------------------------------------- #
def load_config():
    cfg = dict(DEFAULT_CONFIG)
    if os.path.exists(CONFIG_PATH):
        try:
            with open(CONFIG_PATH, "r", encoding="utf-8") as fh:
                cfg.update(json.load(fh))
        except Exception as exc:
            print("[warn] could not read %s (%s); using defaults" % (CONFIG_PATH, exc))
    # environment wins over the file
    cfg["make_webhook_key"] = os.environ.get("MAKE_WEBHOOK_KEY", cfg["make_webhook_key"])
    cfg["make_webhook_url"] = os.environ.get("MAKE_WEBHOOK_URL", cfg["make_webhook_url"])
    cfg["make_zone"] = os.environ.get("MAKE_ZONE", cfg["make_zone"])
    cfg["fb_page_id"] = os.environ.get("FB_PAGE_ID", cfg["fb_page_id"])
    cfg["fb_page_token"] = os.environ.get("FB_PAGE_TOKEN", "")
    return cfg


# --------------------------------------------------------------------------- #
# extraction
# --------------------------------------------------------------------------- #
class TextExtractor(HTMLParser):
    """Collect visible text + image sources, skipping non-content blocks."""

    # figcaption is deliberately here: attach_og_to_pages.py injects a
    # <figure> with the caption "Minh họa — TaichiNOW" right under the <h1>,
    # so without this the caption becomes the first line of every post body.
    SKIP_TAGS = {"script", "style", "svg", "nav", "header", "footer", "form",
                 "noscript", "figcaption"}
    BLOCK_TAGS = {
        "p", "div", "br", "li", "tr", "section", "article", "h1", "h2", "h3",
        "h4", "h5", "h6", "blockquote", "pre", "ul", "ol", "table", "hr",
    }

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.chunks = []
        self.images = []
        self._skip_depth = 0

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP_TAGS:
            self._skip_depth += 1
            return
        if self._skip_depth:
            return
        if tag == "img":
            src = dict(attrs).get("src", "")
            if src:
                self.images.append(src)
            return
        if tag in self.BLOCK_TAGS:
            self.chunks.append("\n")

    def handle_endtag(self, tag):
        if tag in self.SKIP_TAGS:
            self._skip_depth = max(0, self._skip_depth - 1)
            return
        if self._skip_depth:
            return
        if tag in self.BLOCK_TAGS:
            self.chunks.append("\n")

    def handle_data(self, data):
        if self._skip_depth:
            return
        self.chunks.append(data)

    def text(self):
        raw = "".join(self.chunks)
        raw = raw.replace("\u00a0", " ")
        lines = []
        for line in raw.split("\n"):
            line = re.sub(r"[ \t]+", " ", line).strip()
            if line:
                lines.append(line)
        return "\n".join(lines)


NOISE_PATTERNS = [
    r"^←",
    r"^Quay lại",
    r"^Back to",
    r"Trang web này được xây dựng",
    r"^Home$",
    r"^⌂",
    r"Bài viết Facebook",
    r"danh sách bài viết",
    r"^Kho Vault",                       # notebook/vault metadata
    r"^[0-9a-f]{8}-[0-9a-f]{4}-",        # raw UUIDs
    r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-",
    r"^\d+\s*nguồn$",
]
NOISE_RE = re.compile("|".join(NOISE_PATTERNS), re.IGNORECASE)


def clean_lines(text):
    out = []
    for line in text.split("\n"):
        line = line.strip()
        # drop leftover markdown heading markers: "## Title ##" -> "Title"
        line = re.sub(r"^#{1,6}\s*", "", line)
        line = re.sub(r"\s*#+\s*$", "", line).strip()
        if not line:
            continue
        if NOISE_RE.search(line):
            continue
        # date / attachment metadata block: "📅 Thứ Tư 27/05/2026 06:55 · 📸 1 ảnh"
        if line.startswith("📅") or line.startswith("📸"):
            continue
        out.append(line)
    return out


def strip_front_matter(text):
    """Return (meta_dict, body) for markdown with optional YAML front matter."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    raw = text[3:end]
    body = text[end + 4:]
    meta = {}
    for line in raw.splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            meta[key.strip()] = val.strip().strip("\"'")
    return meta, body.lstrip("\n")


def md_to_text(md):
    meta, body = strip_front_matter(md)
    body = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", body)          # images
    body = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", body)      # links -> text
    body = re.sub(r"^\s{0,3}#{1,6}\s*", "", body, flags=re.MULTILINE)
    body = re.sub(r"^\s{0,3}>\s?", "", body, flags=re.MULTILINE)
    body = re.sub(r"[*_`]{1,3}", "", body)
    return meta, body


def extract_from_html(raw):
    """Return dict(title, lines, images) from an HTML page."""
    title = ""
    m = re.search(r"<title[^>]*>(.*?)</title>", raw, re.S | re.I)
    if m:
        title = html_mod.unescape(m.group(1)).strip()
        title = re.sub(r"\s*(?:—|–|\|)\s*TaichiKB\s*$", "", title).strip()
        title = re.sub(r"\s*(?:—|–|\|)\s*Taichi\s*NOW.*$", "", title).strip()

    # narrow to the article body when possible so nav/footer never leak in
    body = raw
    for pattern in (
        r"<article\b[^>]*>(.*?)</article>",
        r"<main\b[^>]*>(.*?)</main>",
    ):
        m = re.search(pattern, body, re.S | re.I)
        if m:
            body = m.group(1)
            break

    if not title:
        m = re.search(r"<h1[^>]*>(.*?)</h1>", body, re.S | re.I)
        if m:
            title = re.sub(r"<[^>]+>", "", m.group(1)).strip()

    parser = TextExtractor()
    parser.feed(body)
    lines = clean_lines(parser.text())

    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", body, re.S | re.I)
    if h1:
        heading = html_mod.unescape(re.sub(r"<[^>]+>", "", h1.group(1))).strip()
        if heading and heading not in lines:
            # <title> is sometimes truncated; the <h1> is the fuller version
            if not title or (len(heading) > len(title)
                             and heading.startswith(title[:15])):
                title = heading
    title = re.sub(r"\s*#+\s*$", "", title).strip()   # markdown leftovers
    return {"title": title, "lines": lines, "images": parser.images}


def extract(path):
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        raw = fh.read()
    ext = os.path.splitext(path)[1].lower()
    if ext in (".md", ".markdown", ".txt"):
        meta, body = md_to_text(raw)
        lines = clean_lines(body)
        title = meta.get("title", "")
        if not title and lines:
            title = lines[0]
            lines = lines[1:]
        return {"title": title, "lines": lines, "images": [], "meta": meta}
    info = extract_from_html(raw)
    info["meta"] = {}
    return info


def make_excerpt(lines, max_chars):
    """Take whole paragraphs up to max_chars, then cut on a sentence."""
    picked, total = [], 0
    for line in lines:
        if total and total + len(line) + 2 > max_chars:
            break
        picked.append(line)
        total += len(line) + 2
        if total >= max_chars:
            break
    # verse-style posts (one short line per <p>) read better with single
    # newlines; prose gets a blank line between paragraphs
    longest = max((len(p) for p in picked), default=0)
    joiner = "\n" if longest <= 60 else "\n\n"
    text = joiner.join(picked).strip()
    if len(text) > max_chars:
        cut = text[:max_chars]
        for sep in ("。", ". ", "! ", "? ", "…"):
            idx = cut.rfind(sep)
            if idx > max_chars * 0.5:
                cut = cut[: idx + len(sep)].rstrip()
                break
        text = cut.rstrip() + "…"
    return text


def to_live_url(file_path, repo, site_base):
    rel = os.path.relpath(file_path, repo).replace("\\", "/")
    rel = re.sub(r"index\.html?$", "", rel)
    rel = re.sub(r"\.md$", "/", rel)
    rel = rel.rstrip("/")
    return site_base.rstrip("/") + "/" + rel.lstrip("/")


def absolutise(src, file_path, repo, site_base):
    if src.startswith("http://") or src.startswith("https://"):
        return src
    if src.startswith("/"):
        return site_base.rstrip("/") + src
    resolved = os.path.normpath(os.path.join(os.path.dirname(file_path), src))
    return to_live_url(resolved, repo, site_base)


# --------------------------------------------------------------------------- #
# repository helpers
# --------------------------------------------------------------------------- #
def posts_dir(repo):
    return os.path.join(repo, "facebook", "posts")


def list_slugs(repo):
    d = posts_dir(repo)
    if not os.path.isdir(d):
        return []
    return sorted(s for s in os.listdir(d) if os.path.isdir(os.path.join(d, s)))


def resolve_slug(repo, slug):
    """A slug is a folder under facebook/posts containing index.html."""
    for candidate in (
        os.path.join(posts_dir(repo), slug, "index.html"),
        os.path.join(posts_dir(repo), slug),
    ):
        if os.path.isfile(candidate):
            return candidate
    # loose match, useful when the shell mangles diacritics
    target = slug.lower()
    for s in list_slugs(repo):
        if s.lower() == target:
            p = os.path.join(posts_dir(repo), s, "index.html")
            if os.path.isfile(p):
                return p
    return None


def latest_post(repo):
    """Newest facebook post page by mtime."""
    best, best_mt = None, -1
    d = posts_dir(repo)
    for root, _dirs, files in os.walk(d):
        for name in files:
            if not name.endswith((".html", ".md")):
                continue
            p = os.path.join(root, name)
            mt = os.path.getmtime(p)
            if mt > best_mt:
                best, best_mt = p, mt
    return best


# --------------------------------------------------------------------------- #
# payload + transport
# --------------------------------------------------------------------------- #
IMAGE_EXTS = (".png", ".jpg", ".jpeg", ".webp")


def _safe_slug(slug):
    return re.sub(r"[^0-9A-Za-z_-]", "_", (slug or "").replace("/", "__"))[:80]


def generated_image(repo, site_base, slug):
    """URL of a generated illustration for this post, if one exists on the site."""
    if not slug:
        return ""
    rel = os.path.join("facebook", "media", "generated", _safe_slug(slug))
    for ext in IMAGE_EXTS:
        if os.path.isfile(os.path.join(repo, rel + ext)):
            return "%s/%s%s" % (site_base.rstrip("/"), rel.replace("\\", "/"), ext)
    return ""


def cfg_default_image():
    try:
        return (load_config().get("default_image") or "")
    except Exception:
        return ""


def build_payload(repo, site_base, file_path, slug, max_chars, hashtags, with_image,
                  signature=""):
    info = extract(file_path)
    lines = info["lines"]
    # the first line often repeats the title
    if lines and info["title"] and lines[0].strip() == info["title"].strip():
        lines = lines[1:]
    excerpt = make_excerpt(lines, max_chars)
    link = to_live_url(file_path, repo, site_base)

    image_url = ""
    if with_image and info["images"]:
        image_url = absolutise(info["images"][0], file_path, repo, site_base)
    if not image_url:
        image_url = generated_image(repo, site_base, slug)
    if not image_url:
        image_url = cfg_default_image()

    parts = []
    if info["title"]:
        parts.append("📌 " + info["title"])
    if excerpt:
        parts.append(excerpt)
    parts.append("🔗 " + link)
    if hashtags:
        parts.append(hashtags)
    if signature:
        # Facebook cannot label a Page post with a person's name, so a
        # signature line is the only way to put a name in front of readers.
        parts.append(signature)
    message = "\n\n".join(parts).strip()

    queued_at = datetime.now().isoformat(timespec="seconds")
    return {
        "message": message,
        "title": info["title"],
        "excerpt": excerpt,
        "link": link,
        "image_url": image_url,
        "slug": slug or "",
        "source_file": os.path.relpath(file_path, repo).replace("\\", "/"),
        "site": urllib.parse.urlparse(site_base).netloc or site_base,
        "queued_at": queued_at,
        # --- aliases -------------------------------------------------------- #
        # The Make scenario that is already live maps post_text / status /
        # created_at, while the webhook feeder maps message / link / image_url.
        # Emit both names so neither route needs re-mapping by hand.
        "post_text": message,
        "post_url": link,
        "photo_url": image_url,
        "created_at": queued_at,
    }, info


def http_post_json(url, payload, timeout=30):
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        url, data=data, method="POST",
        headers={"Content-Type": "application/json; charset=utf-8",
                 "Accept": "application/json, text/plain, */*",
                 "User-Agent": "TaichiNowPublisher/1.0 (+https://taichinow.github.io)"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read().decode("utf-8", "replace")[:2000]
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", "replace")[:2000]
    except Exception as exc:
        return 0, str(exc)


def send_to_make(payload, cfg, verbose=True, url=None):
    """POST to Make.com, trying zones until one answers (404 => try next)."""
    if url or cfg.get("make_webhook_url"):
        zones = [None]
    elif cfg.get("make_zone"):
        zones = [cfg["make_zone"]] + [z for z in MAKE_ZONES if z != cfg["make_zone"]]
    else:
        zones = list(MAKE_ZONES)

    key = cfg.get("make_webhook_key", "")
    attempts = []
    for zone in zones:
        url = url or cfg.get("make_webhook_url") or "https://hook.%s.make.com/%s" % (zone, key)
        if not key and not cfg.get("make_webhook_url"):
            return False, "no webhook key configured", attempts
        status, body = http_post_json(url, payload)
        attempts.append({"url": url, "status": status, "body": body[:200]})
        if verbose:
            print("  -> %-46s HTTP %s" % (url, status))
            if status != 200 and body:
                print("     %s" % body.strip().replace("\n", " ")[:300])
        if status == 200:
            return True, body, attempts
    return False, "no Make.com zone accepted the payload", attempts


def send_direct_graph(payload, cfg):
    """Publish straight to the page with the Meta Graph API."""
    page_id = cfg.get("fb_page_id") or os.environ.get("FB_PAGE_ID", "")
    token = os.environ.get("FB_PAGE_TOKEN", "")
    if not (page_id and token):
        return False, "FB_PAGE_ID / FB_PAGE_TOKEN not set"
    if payload.get("image_url"):
        endpoint = "https://graph.facebook.com/v21.0/%s/photos" % page_id
        params = {"url": payload["image_url"], "caption": payload["message"],
                  "access_token": token}
    else:
        endpoint = "https://graph.facebook.com/v21.0/%s/feed" % page_id
        params = {"message": payload["message"], "link": payload.get("link", ""),
                  "access_token": token}
    status, body = http_post_json(endpoint + "?" + urllib.parse.urlencode(params), {})
    if status == 200:
        return True, body
    return False, "HTTP %s: %s" % (status, body[:300])


def append_log(entry):
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(entry, ensure_ascii=False) + "\n")


def state_path(repo):
    return os.path.join(repo, "facebook", "publish_state.json")


def load_state(repo):
    """Slugs already published, as tracked inside the repo (survives CI)."""
    p = state_path(repo)
    if os.path.exists(p):
        try:
            with open(p, "r", encoding="utf-8") as fh:
                data = json.load(fh)
            if isinstance(data.get("published"), list):
                return data
        except Exception:
            pass
    return {"published": [], "enqueued": []}


def save_state(repo, state):
    p = state_path(repo)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as fh:
        json.dump(state, fh, ensure_ascii=False, indent=2)
        fh.write("\n")


_ARCHIVE_INDEX = {}


def fingerprint(text):
    """Coarse content key: normalised text, first 240 chars."""
    t = re.sub(r"[^\w\s]", " ", (text or "").lower())
    t = re.sub(r"\s+", " ", t).strip()
    return t[:240]


def archive_index(repo):
    """slug -> (title fingerprint, body fingerprint) for every archived post.

    facebook/posts/ is an archive of what has already been on the page, so it
    doubles as the "already published" list. Cached because it reads 70+ files.
    """
    if repo in _ARCHIVE_INDEX:
        return _ARCHIVE_INDEX[repo]
    index = {}
    d = posts_dir(repo)
    for root, _dirs, files in os.walk(d):
        if "index.html" not in files:
            continue
        path = os.path.join(root, "index.html")
        try:
            info = extract(path)
        except Exception:
            continue
        index[os.path.basename(root)] = (
            fingerprint(info["title"]),
            fingerprint(" ".join(info["lines"])),
        )
    _ARCHIVE_INDEX[repo] = index
    return index


def find_duplicate(repo, slug, title, body):
    """Return the slug of an already-existing twin, or None.

    A post is a duplicate if its normalised body or its normalised title
    matches a DIFFERENT entry in the archive. This catches the repeat posts
    in the export (e.g. tiep-chuong-7 vs chuong-7-...).
    """
    tf, bf = fingerprint(title), fingerprint(body)
    if not tf and not bf:
        return None
    for other, (otf, obf) in archive_index(repo).items():
        if other == slug:
            continue
        if bf and bf == obf:
            return other
        if tf and tf == otf:
            return other
    # also guard against anything we have published before
    state = load_state(repo)
    for other, fp in (state.get("fingerprints") or {}).items():
        if other != slug and fp and fp == bf:
            return other
    return None


def mark_published(repo, slug, text=None):
    """Record a slug as published in the repo state file.

    The local log does not exist in CI, so without this the scheduled run
    would happily repost anything published from a laptop.
    """
    if not slug:
        return
    state = load_state(repo)
    state.setdefault("published", [])
    if slug not in state["published"]:
        state["published"].append(slug)
    if text:
        state.setdefault("fingerprints", {})[slug] = fingerprint(text)
    state["last_published"] = datetime.now(SITE_TZ).isoformat(timespec="seconds")
    save_state(repo, state)


def mark_skipped(repo, slug):
    """Exclude a post from the queue without deleting it from the site."""
    if not slug:
        return
    state = load_state(repo)
    state.setdefault("skipped", [])
    if slug not in state["skipped"]:
        state["skipped"].append(slug)
    if isinstance(state.get("schedule"), dict):
        state["schedule"].pop(slug, None)
    save_state(repo, state)


def reset_schedule(repo):
    """Park the current schedule under 'schedule_legacy' and start clean.

    Needed whenever the source set changes: the stale dates would otherwise be
    the cursor for the new posts, pushing the first one months into the future.
    """
    state = load_state(repo)
    old = state.get("schedule") or {}
    if old:
        legacy = state.setdefault("schedule_legacy", {})
        legacy.update(old)
    state["schedule"] = {}
    save_state(repo, state)
    print("[reset] %d stale schedule entry(ies) moved to 'schedule_legacy'" % len(old))
    return 0


def published_slugs(repo):
    """Union of the repo state file and the local log (successful sends only).

    'enqueued' counts too: once a post has been handed to Make's Data Store,
    Make owns it and we must not publish it again locally.
    """
    state = load_state(repo)
    slugs = (set(state.get("published", [])) | set(state.get("enqueued", []))
             | set(state.get("skipped", [])))
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH, "r", encoding="utf-8") as fh:
            for line in fh:
                try:
                    entry = json.loads(line)
                    if entry.get("ok") and entry.get("slug"):
                        slugs.add(entry["slug"])
                except Exception:
                    continue
    return slugs


def already_published(slug):
    if not slug or not os.path.exists(LOG_PATH):
        return False
    with open(LOG_PATH, "r", encoding="utf-8") as fh:
        for line in fh:
            try:
                entry = json.loads(line)
                # only successful sends count as "already published";
                # failed attempts must stay retryable
                if entry.get("slug") == slug and entry.get("ok"):
                    return True
            except Exception:
                continue
    return False


HOOK_MARKER = "taichinow-facebook autopost"
HOOK_END_MARKER = "# --- end " + HOOK_MARKER + " ---"
HOOK_BLOCK = """
# ---------------------------------------------------------------------------
# {marker} (managed by scripts/publish_to_fb.py --install-hook)
# Publishes new facebook posts to the TaichiNow page on `git push`.
# - only on the main branch
# - never blocks the push (failures are printed, not fatal)
# - disable a single push with: TAICHINOW_FB_AUTOPOST=0 git push
# ---------------------------------------------------------------------------
if [[ "${{TAICHINOW_FB_AUTOPOST:-1}}" == "1" ]]; then
  _fb_branch="$(git symbolic-ref --quiet --short HEAD || echo '')"
  if [[ "$_fb_branch" == "main" ]]; then
    _fb_py="{python}"
    [[ -x "$_fb_py" ]] || _fb_py="python"
    "$_fb_py" "scripts/publish_to_fb.py" --hook --repo "$PWD" 2>&1 \\
      | sed 's/^/[fb-autopost] /' || true
  fi
fi
{end}
""".lstrip()


def install_hook(repo, python_exe=None):
    """Append the autopost block to the repo's existing pre-push hook."""
    hook_path = os.path.join(repo, ".git", "hooks", "pre-push")
    # linked worktrees keep hooks in the common git dir
    if not os.path.exists(hook_path):
        dot = os.path.join(repo, ".git")
        if os.path.isfile(dot):
            with open(dot, "r", encoding="utf-8") as fh:
                ref = fh.read().strip()
            if ref.startswith("gitdir:"):
                hook_path = os.path.join(ref.split(":", 1)[1].strip(), "hooks", "pre-push")
    if not os.path.isdir(os.path.dirname(hook_path)):
        print("[error] no git hooks dir at %s" % os.path.dirname(hook_path))
        return 2

    existing = ""
    if os.path.exists(hook_path):
        with open(hook_path, "r", encoding="utf-8", errors="replace") as fh:
            existing = fh.read()
    if HOOK_MARKER in existing:
        print("[ok] pre-push hook already contains the autopost block")
        print("     %s" % hook_path)
        return 0

    py = python_exe or sys.executable.replace("\\", "/")
    block = HOOK_BLOCK.format(marker=HOOK_MARKER, python=py, end=HOOK_END_MARKER)
    if existing.strip():
        # keep whatever guard is already there; append just before its exit
        if re.search(r"\nexit 0\s*$", existing):
            new = re.sub(r"\nexit 0\s*$", "\n" + block + "\nexit 0\n", existing)
        else:
            new = existing.rstrip() + "\n\n" + block + "\nexit 0\n"
    else:
        new = "#!/usr/bin/env bash\nset -uo pipefail\n\n" + block + "\nexit 0\n"

    with open(hook_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(new)
    try:
        os.chmod(hook_path, 0o755)
    except Exception:
        pass
    print("[ok] autopost block appended to %s" % hook_path)
    print("     existing hook content left untouched; block runs only on branch 'main'")
    return 0


def uninstall_hook(repo):
    """Remove the autopost block, leaving the rest of the hook intact."""
    hook_path = os.path.join(repo, ".git", "hooks", "pre-push")
    if not os.path.exists(hook_path):
        print("[info] no pre-push hook")
        return 0
    with open(hook_path, "r", encoding="utf-8", errors="replace") as fh:
        existing = fh.read()
    if HOOK_MARKER not in existing:
        print("[info] autopost block not present")
        return 0
    start = existing.index("# " + HOOK_MARKER)
    start = existing.rindex("# ------", 0, start)          # include the rule line
    end = existing.index(HOOK_END_MARKER, start) + len(HOOK_END_MARKER)
    while end < len(existing) and existing[end] == "\n":
        end += 1
    new = existing[:start] + existing[end:]
    new = re.sub(r"\n{3,}", "\n\n", new)
    with open(hook_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(new)
    print("[ok] autopost block removed from %s" % hook_path)
    return 0


# Vietnam is UTC+7 with no DST - a fixed offset avoids needing tzdata on Windows
SITE_TZ = timezone(timedelta(hours=7))


def today_local():
    return datetime.now(SITE_TZ).date()


def ping_mode(repo, cfg):
    """Trigger the Make scenario whose start module is a Custom Webhook.

    Make then does its own thing: Search records -> Facebook Pages Create a
    Post -> Data store Update. We only supply the kick.
    """
    url = (os.environ.get("MAKE_POST_URL")
           or cfg.get("make_post_url")
           or cfg.get("make_webhook_url") or "")
    if not url and not cfg.get("make_webhook_key"):
        print("[error] no posting webhook configured "
              "(MAKE_POST_URL / make_post_url / make_webhook_url)")
        return 2
    payload = {
        "trigger": "workbuddy",
        "requested_at": datetime.now(SITE_TZ).isoformat(timespec="seconds"),
        "timezone": "Asia/Ho_Chi_Minh (UTC+7)",
    }
    ok, detail, _ = send_to_make(payload, cfg, verbose=False, url=url or None)
    print("[ping] %s" % ("scenario triggered" if ok else "FAILED: %s" % detail))
    return 0 if ok else 4


def emit_mode(repo, cfg):
    """Write the public JSON endpoints that Make's Custom API module reads.

    Produces, inside the site so GitHub Pages serves them:
      facebook/queue/queue.json  - every scheduled post, with its date
      facebook/queue/next.json   - today's single post (or found:false)

    Each post gets one fixed date; Make filters `date = today`. That makes the
    whole thing idempotent - a missed run skips a post, it never double-posts.

    The candidate set is the SAME one the poster uses (content_paths), never
    facebook/posts - that archive is the "already on the page" reference, so
    scheduling from it would repost the page's own archive back to itself.
    """
    base = cfg.get("site_base", SITE_BASE_DEFAULT)
    state = load_state(repo)
    schedule = state.setdefault("schedule", {})

    candidates = collect_candidates(repo, cfg, oldest_first=True)
    if not candidates:
        print("[emit] no unpublished posts found")
        return 2

    today = today_local()
    if schedule:
        cursor = max(datetime.strptime(v, "%Y-%m-%d").date()
                     for v in schedule.values())
        cursor = max(cursor, today - timedelta(days=1))
    else:
        cursor = today - timedelta(days=1)

    items = []
    for payload in candidates:
        slug = payload["slug"]
        if slug not in schedule:
            cursor = cursor + timedelta(days=1)
            schedule[slug] = cursor.isoformat()
        item = dict(payload)
        item["key"] = slug
        item["date"] = schedule[slug]
        item["status"] = "queued" if schedule[slug] >= today.isoformat() else "past"
        items.append(item)

    state["generated"] = datetime.now(SITE_TZ).isoformat(timespec="seconds")
    save_state(repo, state)

    items.sort(key=lambda it: it["date"])
    queue_dir = os.path.join(repo, "facebook", "queue")
    os.makedirs(queue_dir, exist_ok=True)

    queue_doc = {
        "generated": state["generated"],
        "timezone": "Asia/Ho_Chi_Minh (UTC+7)",
        "count": len(items),
        "items": items,
    }
    with open(os.path.join(queue_dir, "queue.json"), "w", encoding="utf-8") as fh:
        json.dump(queue_doc, fh, ensure_ascii=False, indent=2)

    due = next((it for it in items if it["date"] == today.isoformat()), None)
    next_doc = {
        "generated": state["generated"],
        "date": today.isoformat(),
        "timezone": "Asia/Ho_Chi_Minh (UTC+7)",
        "found": due is not None,
        "item": due,
    }
    with open(os.path.join(queue_dir, "next.json"), "w", encoding="utf-8") as fh:
        json.dump(next_doc, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    print("[emit] %d post(s) scheduled" % len(items))
    print("[emit] today (%s): %s" % (today.isoformat(),
                                     due["slug"] if due else "nothing due"))
    print("[emit] %s/facebook/queue/next.json" % base.rstrip("/"))
    print("[emit] %s/facebook/queue/queue.json" % base.rstrip("/"))
    return 0


def content_paths(repo, cfg):
    """Pages eligible for posting.

    Deliberately NOT facebook/posts - that folder is an export of what is
    already on the TaichiNOW page, so reposting it just duplicates the page.
    It still has a job: archive_index() uses it as the "already published"
    list. New posts come from the site's own article sections.
    """
    dirs = cfg.get("source_dirs") or ["vi/articles", "techniques", "articles"]
    paths = []
    for rel in dirs:
        root_dir = os.path.join(repo, rel.replace("/", os.sep))
        if not os.path.isdir(root_dir):
            # Loud on purpose: a wrong --repo used to make this fail silently
            # and surface only as "no unpublished posts found".
            print("[warn] source dir missing, skipping: %s" % root_dir)
            continue
        for root, _dirs, files in os.walk(root_dir):
            if "index.html" in files:
                paths.append(os.path.join(root, "index.html"))
    return sorted(set(paths))


def collect_candidates(repo, cfg, oldest_first=True):
    """Unpublished post pages in the repo, with payloads attached."""
    paths = content_paths(repo, cfg)
    paths.sort(key=lambda p: os.path.getmtime(p), reverse=not oldest_first)

    base = cfg.get("site_base", SITE_BASE_DEFAULT)
    done = published_slugs(repo)
    out = []
    for path in paths:
        slug = os.path.relpath(path, repo).replace("\\", "/")
        slug = re.sub(r"/?index\.html$", "", slug)
        if slug in done:
            continue
        info = extract(path)
        twin = find_duplicate(repo, slug, info["title"], " ".join(info["lines"]))
        if twin:
            print("  [dup] %s matches already-posted %s - skipping" % (slug, twin))
            continue
        payload, _ = build_payload(repo, base, path, slug,
                                   cfg.get("max_chars", 600),
                                   cfg.get("hashtags", ""), True,
                                   cfg.get("signature", ""))
        out.append(payload)
    return out


def enqueue_mode(repo, cfg, limit):
    """Hand posts to Make's Data Store. Make does the actual posting.

    One POST per post -> one record per post. The record `key` is the slug,
    so re-sending a post updates its row instead of duplicating it.
    """
    url = (os.environ.get("MAKE_ENQUEUE_URL")
           or cfg.get("make_enqueue_url")
           or cfg.get("make_webhook_url") or "")
    if not url and not cfg.get("make_webhook_key"):
        print("[error] no enqueue webhook configured "
              "(MAKE_ENQUEUE_URL / make_enqueue_url)")
        return 2

    items = collect_candidates(repo, cfg)
    if not items:
        print("[enqueue] nothing left to queue")
        return 0
    if limit and limit > 0:
        items = items[:limit]

    print("[enqueue] %d post(s) -> Make Data Store" % len(items))
    state = load_state(repo)
    sent = 0
    for payload in items:
        record = dict(payload)
        record["key"] = payload["slug"]          # Data Store key: dedupe on slug
        record["status"] = "queued"
        ok, detail, _ = send_to_make(record, cfg, verbose=False, url=url or None)
        append_log(dict(payload, ok=bool(ok), mode="enqueue",
                        detail=str(detail)[:500]))
        print("  %-8s %s" % ("queued" if ok else "FAILED", payload["slug"]))
        if not ok:
            print("     %s" % str(detail)[:200])
            continue
        if payload["slug"] not in state.setdefault("enqueued", []):
            state["enqueued"].append(payload["slug"])
        state["last_enqueued"] = payload["queued_at"]
        sent += 1
        time.sleep(0.2)                          # stay well under Make's rate limit

    save_state(repo, state)
    print("[enqueue] %d/%d handed to Make; Make publishes them on its schedule"
          % (sent, len(items)))
    return 0 if sent else 4


def queue_mode(repo, cfg, direct):
    """Publish exactly one unpublished post, oldest first. Used by the cron."""
    items = collect_candidates(repo, cfg, oldest_first=True)
    if not items:
        print("[queue] nothing left to publish")
        return 0

    payload = items[0]
    slug = payload["slug"]
    path = os.path.join(repo, payload["source_file"].replace("/", os.sep))
    print("[queue] next in queue: %s  (%d remaining after this)"
          % (slug, len(items) - 1))
    if direct:
        ok, detail = send_direct_graph(payload, cfg)
    else:
        ok, detail, _ = send_to_make(payload, cfg, verbose=False)
    append_log(dict(payload, ok=bool(ok), mode="graph" if direct else "queue",
                    detail=str(detail)[:500]))
    if ok:
        mark_published(repo, slug, payload.get("message"))
        print("[queue] published -> %s" % payload["link"])
        return 0
    print("[queue] FAILED: %s" % detail)
    return 4


def hook_mode(repo, cfg, limit, direct):
    """Publish posts that are not in the log yet. Never fails the push."""
    candidates = []
    d = posts_dir(repo)
    for root, _dirs, files in os.walk(d):
        if "index.html" in files:
            candidates.append(os.path.join(root, "index.html"))
    candidates.sort(key=lambda p: os.path.getmtime(p), reverse=True)

    done = published_slugs(repo)
    todo = [p for p in candidates
            if os.path.basename(os.path.dirname(p)) not in done]
    if not todo:
        print("[hook] no new posts to publish (%d already logged)" % len(candidates))
        return 0
    todo = todo[:limit]
    print("[hook] %d new post(s) to publish" % len(todo))

    ok_count = 0
    for path in todo:
        slug = os.path.basename(os.path.dirname(path))
        payload, _ = build_payload(repo, cfg.get("site_base", SITE_BASE_DEFAULT), path,
                                   slug, cfg.get("max_chars", 600),
                                   cfg.get("hashtags", ""), True,
                                   cfg.get("signature", ""))
        print("[hook] %s" % slug)
        if direct:
            ok, detail = send_direct_graph(payload, cfg)
        else:
            ok, detail, _ = send_to_make(payload, cfg, verbose=False)
        append_log(dict(payload, ok=bool(ok),
                        mode="graph" if direct else "hook",
                        detail=str(detail)[:500]))
        print("[hook]   %s" % ("published" if ok else "FAILED: %s" % detail))
        ok_count += bool(ok)
    print("[hook] done: %d/%d published" % (ok_count, len(todo)))
    return 0


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #
def main():
    cfg = load_config()

    ap = argparse.ArgumentParser(description="Publish a TaichiNow page to Facebook via Make.com")
    ap.add_argument("--repo", default=cfg.get("repo", REPO_DEFAULT),
                    help="local clone of taichinow.github.io")
    ap.add_argument("--slug", help="post folder under facebook/posts/")
    ap.add_argument("--file", help="explicit file (html/md) relative to repo or absolute")
    ap.add_argument("--latest", action="store_true", help="use the most recently edited post")
    ap.add_argument("--list", action="store_true", help="list available slugs and exit")
    ap.add_argument("--send", action="store_true", help="actually publish (default = preview)")
    ap.add_argument("--direct", action="store_true", help="use Meta Graph API instead of Make")
    ap.add_argument("--max-chars", type=int, default=cfg.get("max_chars", 600))
    ap.add_argument("--hashtags", default=cfg.get("hashtags", ""))
    ap.add_argument("--no-image", action="store_true", help="do not attach the first image")
    ap.add_argument("--retry", type=int, default=0, metavar="SECONDS",
                    help="keep retrying for this long when Make is not listening "
                         "(404/410 are rejected outright, so no duplicate risk)")
    ap.add_argument("--retry-every", type=int, default=5, metavar="SECONDS",
                    help="gap between retries (default 5)")
    ap.add_argument("--allow-duplicate", action="store_true",
                    help="publish even if this slug is already in the log")
    ap.add_argument("--install-hook", action="store_true",
                    help="append the autopost block to the repo's pre-push hook "
                         "(main branch only, never blocks the push)")
    ap.add_argument("--uninstall-hook", action="store_true",
                    help="remove the autopost block from the pre-push hook")
    ap.add_argument("--hook", action="store_true",
                    help="hook mode: publish every post not yet in the log")
    ap.add_argument("--queue", action="store_true",
                    help="queue mode: publish the next unpublished post (oldest "
                         "first) and record it in facebook/publish_state.json")
    ap.add_argument("--ping", action="store_true",
                    help="kick the Make scenario that starts with a Custom "
                         "Webhook; Make then searches, posts and updates itself")
    ap.add_argument("--skip-slug", metavar="SLUG",
                    help="exclude a post from the queue without deleting it "
                         "from the site (e.g. a bare link-share)")
    ap.add_argument("--emit", action="store_true",
                    help="write facebook/queue/queue.json + next.json, the public "
                         "JSON endpoints Make's Custom API module reads")
    ap.add_argument("--enqueue", action="store_true",
                    help="hand posts to Make's Data Store instead of publishing; "
                         "Make's scheduled scenario does the posting")
    ap.add_argument("--reset-schedule", action="store_true",
                    help="move facebook/publish_state.json's 'schedule' to "
                         "'schedule_legacy' so the next --emit re-dates every "
                         "post from today. Use when the source set changed and "
                         "the old dates would push new posts months out")
    ap.add_argument("--limit", type=int, default=1,
                    help="max posts to publish in --hook mode (default 1)")
    args = ap.parse_args()

    repo = os.path.abspath(args.repo)
    if args.install_hook:
        return install_hook(repo)
    if args.uninstall_hook:
        return uninstall_hook(repo)
    if args.reset_schedule:
        return reset_schedule(repo)
    if args.skip_slug:
        mark_skipped(repo, args.skip_slug)
        print("[skip] '%s' excluded from the queue" % args.skip_slug)
        return 0
    if args.ping:
        return ping_mode(repo, cfg)
    if args.emit:
        return emit_mode(repo, cfg)
    if args.enqueue:
        return enqueue_mode(repo, cfg, args.limit)
    if args.queue:
        return queue_mode(repo, cfg, args.direct)
    if args.hook:
        return hook_mode(repo, cfg, args.limit, args.direct)

    repo = os.path.abspath(args.repo)
    site_base = cfg.get("site_base", SITE_BASE_DEFAULT)

    if args.list:
        slugs = list_slugs(repo)
        print("%d post(s) under facebook/posts:" % len(slugs))
        for s in slugs:
            print("  " + s)
        return 0

    if args.file:
        file_path = args.file if os.path.isabs(args.file) else os.path.join(repo, args.file)
        slug = os.path.basename(os.path.dirname(file_path))
    elif args.slug:
        file_path = resolve_slug(repo, args.slug)
        if not file_path:
            print("[error] no post found for slug: %s" % args.slug)
            print("        run --list to see valid slugs")
            return 2
        slug = args.slug
    elif args.latest:
        file_path = latest_post(repo)
        if not file_path:
            print("[error] no posts found under %s" % posts_dir(repo))
            return 2
        slug = os.path.basename(os.path.dirname(file_path))
    else:
        ap.print_help()
        print("\n[info] nothing to do: pass --slug, --file or --latest "
              "(or --list to browse)")
        return 1

    if not os.path.isfile(file_path):
        print("[error] file not found: %s" % file_path)
        return 2

    payload, _info = build_payload(
        repo, site_base, file_path, slug, args.max_chars,
        args.hashtags, not args.no_image, cfg.get("signature", ""),
    )

    print("=" * 72)
    print("SOURCE : %s" % payload["source_file"])
    print("TITLE  : %s" % payload["title"])
    print("LINK   : %s" % payload["link"])
    print("IMAGE  : %s" % (payload["image_url"] or "(none)"))
    print("-" * 72)
    print(payload["message"])
    print("-" * 72)
    print("length : %d chars" % len(payload["message"]))

    if not args.send:
        print("\n[dry-run] nothing was published. Re-run with --send to publish.")
        return 0

    if not args.allow_duplicate and already_published(slug):
        print("\n[skip] '%s' is already in %s (use --allow-duplicate to override)"
              % (slug, LOG_PATH))
        return 3

    print("\nsending...")
    ok, detail = (send_direct_graph(payload, cfg) if args.direct
                  else send_to_make(payload, cfg)[:2])

    # Safe to retry: 404/410 mean Make rejected the payload outright, so a
    # retry can never produce a duplicate post. Only a 200 stops the loop.
    if not ok and args.retry > 0:
        deadline = time.time() + args.retry
        attempt = 0
        while not ok and time.time() < deadline:
            attempt += 1
            time.sleep(args.retry_every)
            print("  retry %d (Make not listening yet) ..." % attempt)
            ok, detail = (send_direct_graph(payload, cfg) if args.direct
                          else send_to_make(payload, cfg, verbose=False)[:2])
        if ok:
            print("  caught it on retry %d" % attempt)

    append_log(dict(payload, ok=bool(ok), mode="graph" if args.direct else "make",
                    detail=str(detail)[:500]))
    if ok:
        mark_published(repo, slug)      # so CI does not repost this one
        print("\n[ok] published to the TaichiNow page. Logged -> %s" % LOG_PATH)
        return 0
    print("\n[fail] %s" % detail)
    print("       Check the Make.com scenario is ON and the webhook key is right.")
    return 4


if __name__ == "__main__":
    sys.exit(main())
