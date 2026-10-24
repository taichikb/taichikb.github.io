#!/usr/bin/env python3
"""Body of MD-to-HTML converter for the topic pages.

The split/{ch}.{lang}.md files contain:
- H2 chapter heading  (skipped, already in page <h1>)
- Body paragraphs containing **Bold:** lead-in
- A `### Drills for 3.0` heading followed by a table; we render each table as
  its own card
- Blockquote Master Cue lines (start with >) — render as inverted card
- A `### Chapter X Card` heading followed by ASCII art (skip)
"""
import re


def _render_paragraph(text):
    """Convert **bold** markdown to <strong>, normalise <p>."""
    t = text.strip()
    # Convert **...** to <strong>...</strong>
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    # Convert *...* to <em>...</em>
    t = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', t)
    return t


def md_to_html(md_text, lang):
    """Convert the bilingual-row-split MD to our technique-card markup."""
    lines = md_text.split('\n')
    out = []
    card_buffer = []   # current card body lines
    table_buffer = []  # current table rows
    cue_buffer = []    # current cue blockquote lines

    master_cue_label = "Master Cue" if lang == "en" else "Câu Nhắc Tổng"
    drills_label = "Drills" if lang == "en" else "Bài Tập"

    def flush_card():
        nonlocal card_buffer
        if not card_buffer:
            return
        # First non-empty line is the heading if it has **Bold:** prefix;
        # otherwise all lines belong to one paragraph-block card
        # Strategy: join into one <p>, with first line as <h3> if it begins with **
        first = card_buffer[0]
        m = re.match(r'^\*\*(.+?)\*\*\s*[:：\-]?\s*(.*)$', first)
        out.append('    <div class="technique-card">')
        if m:
            heading = _render_paragraph(m.group(1))
            rest = _render_paragraph(m.group(2))
            out.append(f'        <h3>{heading}</h3>')
            if rest:
                out.append(f'        <p>{rest}</p>')
            for ln in card_buffer[1:]:
                if ln.strip():
                    out.append(f'        <p>{_render_paragraph(ln.strip())}</p>')
        else:
            for ln in card_buffer:
                if ln.strip():
                    out.append(f'        <p>{_render_paragraph(ln.strip())}</p>')
        out.append('    </div>')
        card_buffer = []

    def flush_cue():
        nonlocal cue_buffer
        if not cue_buffer:
            return
        # Filter out VI bleed from EN (or vice versa) using simple heuristic:
        # Each cue line might contain both langs joined with ' / '.
        # In source they appear as:   *"\""EN"\"" *"\""VI"\""*
        # which after split may be both languages on one line.
        for ln in cue_buffer:
            t = ln.strip().lstrip('>').strip().lstrip('*').rstrip('*').strip()
            t = t.strip('"').strip()
            if not t:
                continue
            # Filter: keep lines that look like the target language.
            # Simple test: VI lines contain diacritics (ăâđêôơưĂÂĐÊÔƠƯáàảãạằẳẵặắấầậéèẻẽẹếềểễệíìỉĩịóòỏõọốồộỗớờởỡợúùủũụứừửữựýỳỷỹỵÁÀẢÃẠẰẲẴẶẮẤẦẬÉÈẺẼẸẾỀỂỄỆÍÌỈĨỊÓÒỎÕỌỐỒỘỖỚỜỞỠỢÚÙỦŨỤỨỪỬỮỰÝỲỶỸỴ) OR a common VN stopword.
            vi_chars = set("ăâđêôơưĂÂĐÊÔƠƯáàảãạằẳẵặắấầậéèẻẽẹếềểễệíìỉĩịóòỏõọốồộỗớờởỡợúùủũụứừửữựýỳỷỹỵÁÀẢÃẠẰẲẴẶẮẤẦẬÉÈẺẼẸẾỀỂỄỆÍÌỈĨỊÓÒỎÕỌỐỒỘỖỚỜỞỠỢÚÙỦŨỤỨỪỬỮỰÝỲỶỸỴ")
            if lang == "en":
                # Drop lines with diacritics or VN-specific stop words ("là","của","như","với","theo","bạn","đó")
                vn_words = (" là ", " của ", " như ", " với ", " theo ", " bạn ", " đó ", " thì ", " trong ", " được ", " không ", " một ", " cho ", " những ", " các ")
                if any(c in t for c in vi_chars) or any(w in f" {t} " for w in vn_words):
                    continue
            else:
                # Drop pure-EN lines (no diacritics AND VN-specific English stop words)
                en_phrases = ('like a ', 'press in', 'push back', 'is the ', 'is a ', 'of readiness', 'the energy', 'your arm', 'into your foot', 'imagined', 'partner', 'imagining an invisible')
                tl = t.lower()
                # If line has no diacritics but matches an EN phrase, skip
                if not any(c in t for c in vi_chars) and any(p in tl for p in en_phrases):
                    continue
                # Specifically also skip the marker lines from print-cards
                if t.startswith('"') and t.endswith('"'):
                    pass
            # Render
            out.append(
                '    <div class="technique-card" style="background:var(--ink); color:var(--card);">'
                f'<h3 style="color:var(--card);">{master_cue_label}</h3>'
                f'<p style="font-style:italic; font-family:Cormorant Garamond, serif; font-size:1.3rem;">{t}</p>'
                '</div>'
            )
        cue_buffer = []

    def flush_table():
        nonlocal table_buffer
        if not table_buffer:
            return
        # Skip header row + separator rows
        rows = [r for r in table_buffer if not re.match(r'^\|?[\s\-|]+\|?$', r.strip())]
        if not rows:
            table_buffer = []
            return
        out.append('    <div class="technique-card">')
        out.append(f'        <h3>{drills_label}</h3>')
        for r in rows:
            parts = [p.strip() for p in r.strip().strip('|').split('|')]
            parts = [p for p in parts if p]
            if not parts:
                continue
            label = _render_paragraph(parts[0])
            desc = ""
            if len(parts) > 1:
                desc = _render_paragraph(" — ".join(parts[1:]))
                # If alternate-language bleed: drop other-language content from desc
                if lang == "en":
                    desc = re.sub(r'\s+[A-ZĂÂĐÊÔƠƯ][a-zăâđêôơưáàảãạằẳẵặắấầậéèẻẽẹếềểễệíìỉĩịóòỏõọốồộỗớờởỡợúùủũụứừửữựýỳỷỹỵ]+\s+[a-zăâđêôơưáàảãạằẳẵặắấầậéèẻẽẹếềểễệíìỉĩịóòỏõọốồộỗớờởỡợúùủũụứừửữựýỳỷỹỵ]+\s+', ' ', desc)
            if desc:
                out.append(f'        <p><strong>{label}</strong> &mdash; {desc}</p>')
            else:
                out.append(f'        <p><strong>{label}</strong></p>')
        out.append('    </div>')
        table_buffer = []

    in_card_block = False
    in_drills_table = False
    in_cue = False

    for ln in lines:
        s = ln.strip()
        if not s:
            in_card_block = False
            in_drills_table = False
            continue

        # Skip page-level headings
        if s.startswith('# '):
            continue

        if s.startswith('### '):
            # New subsection
            flush_card(); flush_table(); flush_cue()
            h = s[4:].strip()
            h = re.split(r'\s*\|\s*', h)[0] if h else h
            h_low = h.lower()
            if 'card' in h_low and 'chapter' in h_low:
                # Skip ASCII printable card entirely
                continue
            if 'master cue' in h_low or 'câu nhắc tổng' in h_low:
                in_cue = True
                continue
            if 'drills' in h_low or 'bài tập' in h_low:
                in_drills_table = True
                continue
            # Generic subsection -> start a new card
            in_card_block = True
            card_buffer.append(f"**{h}**")
            continue

        if in_cue:
            if s.startswith('>'):
                cue_buffer.append(s)
            continue

        if in_drills_table:
            if s.startswith('|'):
                table_buffer.append(s)
            else:
                flush_table()
                in_drills_table = False
            continue

        # Skip the printable ASCII card block (boxed chars)
        if any(c in s for c in '║╔╚═╠╣╦╩╬'):
            continue

        # Skip leftover ### mini-header markers that came through inline
        if s.startswith('###'):
            continue

        # Skip orphan pipe-delimited header row labels
        if s.startswith('|') and s.endswith('|'):
            table_buffer.append(s)
            in_drills_table = True
            continue

        # Plain body line - collect into card
        in_card_block = True
        card_buffer.append(s)

    flush_card(); flush_table(); flush_cue()

    return '\n'.join(out)
