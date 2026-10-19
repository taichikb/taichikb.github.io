/* ============================================================
   TaichiNOW — Circadian Organ Clock · desktop dashboard engine
   Expects window.ORGAN_CLOCK = { lang, t, data } from the page.
   ============================================================ */
(function () {
  'use strict';

  var CFG = window.ORGAN_CLOCK;
  if (!CFG || !CFG.data || !CFG.data.length) { return; }

  var T = CFG.t || {};
  var DATA = CFG.data;
  var NS = 'http://www.w3.org/2000/svg';

  var CX = 374, CY = 374;
  var R_OUT = 252, R_IN = 166, R_LABEL = 292, R_PROG = 259;
  var GAP = 1.4;
  var IDLE_MS = 120000;

  var state = {
    liveIdx: 0,
    selected: null,
    saver: false,
    lastArm: 0
  };

  /* ---------- helpers ---------- */

  function pad(n) { return (n < 10 ? '0' : '') + n; }
  function f(n) { return Math.round(n * 100) / 100; }

  function svgEl(name, attrs) {
    var node = document.createElementNS(NS, name);
    if (attrs) {
      Object.keys(attrs).forEach(function (k) {
        node.setAttribute(k, attrs[k]);
      });
    }
    return node;
  }

  function pt(r, a) {
    var rad = a * Math.PI / 180;
    return [CX + r * Math.cos(rad), CY + r * Math.sin(rad)];
  }

  function sector(a1, a2, r1, r2) {
    var A = pt(r2, a1), B = pt(r2, a2), C = pt(r1, a2), D = pt(r1, a1);
    var large = (a2 - a1) > 180 ? 1 : 0;
    return 'M' + f(A[0]) + ' ' + f(A[1]) +
      ' A' + r2 + ' ' + r2 + ' 0 ' + large + ' 1 ' + f(B[0]) + ' ' + f(B[1]) +
      ' L' + f(C[0]) + ' ' + f(C[1]) +
      ' A' + r1 + ' ' + r1 + ' 0 ' + large + ' 0 ' + f(D[0]) + ' ' + f(D[1]) + ' Z';
  }

  function arc(r, a1, a2) {
    var A = pt(r, a1), B = pt(r, a2);
    var large = (a2 - a1) > 180 ? 1 : 0;
    return 'M' + f(A[0]) + ' ' + f(A[1]) + ' A' + r + ' ' + r + ' 0 ' + large + ' 1 ' + f(B[0]) + ' ' + f(B[1]);
  }

  /* ---------- time model ---------- */

  // 23:00-01:00 => 0, 01:00-03:00 => 1 ... 21:00-23:00 => 11
  function nowIndex(d) {
    return Math.floor((((d.getHours() + 1) % 24)) / 2);
  }

  function windowStartHour(i) {
    return (i * 2 + 23) % 24;
  }

  function elapsedMinutes(i, d) {
    var start = windowStartHour(i) * 60;
    var now = d.getHours() * 60 + d.getMinutes() + d.getSeconds() / 60;
    var diff = now - start;
    if (diff < 0) { diff += 1440; }
    return diff;
  }

  function remainingMinutes(i, d) {
    var left = 120 - elapsedMinutes(i, d);
    return Math.max(0, Math.min(120, left));
  }

  function humanLeft(mins) {
    var m = Math.max(1, Math.round(mins));
    var uh = T.unitH || 'h';
    var um = T.unitM || 'm';
    if (m >= 60) {
      var h = Math.floor(m / 60);
      var r = m % 60;
      return r === 0 ? h + uh : h + uh + ' ' + pad(r) + um;
    }
    return m + um;
  }

  function leftText(mins) {
    return (T.leftTpl || '{t} left').replace('{t}', humanLeft(mins));
  }

  function clockTime(d) { return pad(d.getHours()) + ':' + pad(d.getMinutes()); }

  function shortRange(range) {
    var p = range.split(' - ');
    return p[0].slice(0, 2) + '\u2013' + p[1].slice(0, 2);
  }
  function clockFull(d) { return clockTime(d) + ':' + pad(d.getSeconds()); }

  /* ---------- ring ---------- */

  var segNodes = [];

  function buildRing() {
    var host = document.getElementById('oc-segments');
    var progHost = document.getElementById('oc-progress');
    if (!host) { return; }

    DATA.forEach(function (item, i) {
      var a1 = -90 + i * 30 + GAP / 2;
      var a2 = -90 + (i + 1) * 30 - GAP / 2;
      var mid = (a1 + a2) / 2;
      var rad = mid * Math.PI / 180;
      var cos = Math.cos(rad);

      var g = svgEl('g', {
        'class': 'seg',
        'tabindex': '0',
        'role': 'button',
        'data-i': String(i),
        'aria-label': item.branch + ', ' + item.range + ', ' + item.organ
      });
      g.style.setProperty('--seg-tint', 'var(--' + (item.element || 'emerald') + ')');

      var fill = svgEl('path', { d: sector(a1, a2, R_IN, R_OUT), 'class': 'seg-fill' });
      g.appendChild(fill);

      var lx = CX + R_LABEL * Math.cos(rad);
      var ly = CY + R_LABEL * Math.sin(rad);
      var anchor = cos > 0.35 ? 'start' : (cos < -0.35 ? 'end' : 'middle');

      var t1 = svgEl('text', { x: f(lx), y: f(ly - 6), 'text-anchor': anchor, 'class': 'lbl-branch' });
      t1.textContent = item.branch;
      g.appendChild(t1);

      var t2 = svgEl('text', { x: f(lx), y: f(ly + 10), 'text-anchor': anchor, 'class': 'lbl-time' });
      t2.textContent = item.range;
      g.appendChild(t2);

      var t3 = svgEl('text', { x: f(lx), y: f(ly + 25), 'text-anchor': anchor, 'class': 'lbl-organ' });
      t3.textContent = item.short || item.organ;
      g.appendChild(t3);

      g.addEventListener('click', function () { select(i); });
      g.addEventListener('keydown', function (ev) {
        if (ev.key === 'Enter' || ev.key === ' ') {
          ev.preventDefault();
          select(i);
        }
      });

      host.appendChild(g);
      segNodes.push(g);
    });

    var prog = svgEl('path', {
      id: 'oc-prog-arc',
      'class': 'prog-arc',
      opacity: '0'
    });
    if (progHost) { progHost.appendChild(prog); }
  }

  function updateProgressArc(i, frac) {
    var p = document.getElementById('oc-prog-arc');
    if (!p) { return; }
    if (frac <= 0.002 || frac >= 0.999) {
      p.setAttribute('opacity', '0');
      return;
    }
    var a1 = -90 + i * 30 + GAP / 2;
    var a2 = -90 + (i + 1) * 30 - GAP / 2;
    p.setAttribute('d', arc(R_PROG, a1, a1 + (a2 - a1) * frac));
    p.setAttribute('opacity', '1');
  }

  /* ---------- strip ---------- */

  var cells = [];

  function buildStrip() {
    var host = document.getElementById('oc-strip');
    if (!host) { return; }
    DATA.forEach(function (item, i) {
      var b = document.createElement('button');
      b.type = 'button';
      b.className = 'cell';
      b.style.setProperty('--tint', 'var(--' + (item.element || 'emerald') + ')');
      b.setAttribute('aria-label', item.branch + ', ' + item.range + ', ' + item.organ);

      var o = document.createElement('span');
      o.className = 'c-organ';
      o.textContent = item.short || item.organ;

      var t = document.createElement('span');
      t.className = 'c-range';
      t.textContent = item.range.replace(' - ', '–');

      var fill = document.createElement('i');
      fill.className = 'c-fill';

      b.appendChild(o);
      b.appendChild(t);
      b.appendChild(fill);
      b.addEventListener('click', function () { select(i); });
      host.appendChild(b);
      cells.push({ btn: b, fill: fill });
    });
  }

  /* ---------- panel ---------- */

  function setText(id, value) {
    var node = document.getElementById(id);
    if (node) { node.textContent = value; }
  }

  function staticLabels() {
    setText('hScience', T.lblScience);
    setText('hClassical', T.lblClassical);
    setText('hDrill', T.lblDrill);
    setText('hLifestyle', T.lblLifestyle);
    setText('nLbl', T.lblNext);
    setText('pBack', T.backToNow);
    setText('drillEyebrow', T.lblDrill);
    setText('saverDrill', '');
    setText('saverHint', T.saverHint);
    var fsLabel = document.getElementById('fsLabel');
    if (fsLabel) { fsLabel.textContent = T.fullscreen; }
    var saverLabel = document.getElementById('saverLabel');
    if (saverLabel) { saverLabel.textContent = T.saver; }
    var drillReset = document.getElementById('drillReset');
    if (drillReset) { drillReset.textContent = T.reset; }
  }

  function paintPanel(item, isNow, frac, left) {
    var eyebrow = document.getElementById('pEyebrow');
    var eyebrowTxt = document.getElementById('pEyebrowTxt');
    var back = document.getElementById('pBack');
    var leftPill = document.getElementById('pLeft');

    if (eyebrow) { eyebrow.className = 'p-eyebrow' + (isNow ? '' : ' is-preview'); }
    if (eyebrowTxt) { eyebrowTxt.textContent = isNow ? T.live : T.preview; }

    setText('pOrgan', item.organ);
    setText('pSub', item.sub || '');
    setText('pRange', item.range.replace(' - ', ' → '));
    setText('pBranch', item.branch);

    if (leftPill) {
      leftPill.hidden = !isNow;
      leftPill.textContent = isNow ? leftText(left) : '';
    }
    if (back) { back.hidden = isNow; }

    setText('bScience', item.science);
    setText('bClassical', item.classical);
    setText('bDrill', item.drill);
    setText('bLifestyle', item.lifestyle);

    var bar = document.getElementById('pBar');
    if (bar) { bar.style.width = (isNow ? Math.round(frac * 1000) / 10 : 0) + '%'; }

    var guide = document.getElementById('lnkGuide');
    if (guide) {
      guide.href = item.url;
      guide.textContent = (T.guideLabel || 'Open guide').replace('{id}', item.id);
    }

    var btn = document.getElementById('btnDrill');
    if (btn) { btn.textContent = T.startDrill; }

    var meta = document.getElementById('pFootMeta');
    if (meta) {
      var n = DATA.indexOf(item) + 1;
      var elName = (T.elements && T.elements[item.element]) || item.element;
      meta.textContent = (T.elementLabel || 'Element') + ': ' + elName + '  ·  ' +
        (T.windowLabel || 'Window {n} of 12').replace('{n}', n);
    }

    var host = document.getElementById('nItems');
    if (host) {
      host.innerHTML = '';
      var base = DATA.indexOf(item);
      for (var k = 1; k <= 2; k++) {
        (function (idx) {
          var nx = DATA[idx];
          var s = document.createElement('button');
          s.type = 'button';
          s.className = 'n-item';
          var dot = document.createElement('i');
          dot.style.background = 'var(--' + (nx.element || 'emerald') + ')';
          s.appendChild(dot);
          s.appendChild(document.createTextNode(nx.range.split(' - ')[0] + ' ' + (nx.short || nx.organ)));
          s.addEventListener('click', function () { select(idx); });
          host.appendChild(s);
          host.appendChild(document.createTextNode(' '));
        })((base + k) % DATA.length);
      }
    }

    setText('saverDrill', item.drill);
  }

  function paint(i, isNow) {
    var item = DATA[i];
    var d = new Date();
    var frac = isNow ? Math.max(0, Math.min(1, elapsedMinutes(i, d) / 120)) : 0;
    var left = isNow ? remainingMinutes(i, d) : 0;

    segNodes.forEach(function (g, k) {
      g.classList.toggle('is-now', isNow && k === i);
      g.classList.toggle('is-selected', !isNow && k === i);
    });

    cells.forEach(function (c, k) {
      c.btn.classList.toggle('now', isNow && k === i);
      c.btn.classList.toggle('is-selected', !isNow && k === i);
      c.fill.style.width = (isNow && k === i) ? (frac * 100) + '%' : '0%';
    });

    setText('ocTime', isNow ? clockTime(d) : shortRange(item.range));
    setText('ocBranch', item.branch);
    setText('ocOrgan', item.center || item.organ);
    setText('ocRemain', isNow ? leftText(left) : T.previewSub);

    paintPanel(item, isNow, frac, left);
    updateProgressArc(i, frac);
    document.body.classList.toggle('previewing', !isNow);
  }

  function select(i) {
    if (i === state.liveIdx) {
      state.selected = null;
      paint(state.liveIdx, true);
    } else {
      state.selected = i;
      paint(i, false);
    }
  }

  function backToNow() {
    state.selected = null;
    paint(state.liveIdx, true);
  }

  /* ---------- ticking ---------- */

  function tick() {
    var d = new Date();
    setText('liveClock', clockFull(d));

    var idx = nowIndex(d);
    if (idx !== state.liveIdx) {
      state.liveIdx = idx;
      if (state.selected === null) {
        paint(idx, true);
        return;
      }
    }

    if (state.selected === null) {
      var frac = Math.max(0, Math.min(1, elapsedMinutes(idx, d) / 120));
      var left = remainingMinutes(idx, d);
      setText('ocTime', clockTime(d));
      setText('ocRemain', leftText(left));
      var bar = document.getElementById('pBar');
      if (bar) { bar.style.width = (Math.round(frac * 1000) / 10) + '%'; }
      var lp = document.getElementById('pLeft');
      if (lp) { lp.textContent = leftText(left); }
      var cf = cells[idx] && cells[idx].fill;
      if (cf) { cf.style.width = (frac * 100) + '%'; }
      updateProgressArc(idx, frac);
    }
  }

  /* ---------- drill timer ---------- */

  var tmr = { total: 180, left: 180, running: false, endAt: 0, handle: null, item: null };

  function fmtTimer(sec) {
    var s = Math.max(0, Math.ceil(sec));
    return pad(Math.floor(s / 60)) + ':' + pad(s % 60);
  }

  function paintTimer() {
    var node = document.getElementById('drillTime');
    if (!node) { return; }
    node.textContent = fmtTimer(tmr.left);
    node.classList.toggle('done', tmr.left <= 0);
    var btn = document.getElementById('drillToggle');
    if (btn) { btn.textContent = tmr.running ? T.pause : (tmr.left <= 0 ? T.reset : (tmr.left < tmr.total ? T.resume : T.start)); }
    Array.prototype.forEach.call(document.querySelectorAll('.ov-preset'), function (p) {
      p.classList.toggle('active', Number(p.getAttribute('data-min')) * 60 === tmr.total);
    });
  }

  function stopTimer() {
    if (tmr.handle) { clearInterval(tmr.handle); tmr.handle = null; }
    tmr.running = false;
  }

  function runTimer() {
    stopTimer();
    tmr.endAt = Date.now() + tmr.left * 1000;
    tmr.running = true;
    tmr.handle = setInterval(function () {
      var left = (tmr.endAt - Date.now()) / 1000;
      tmr.left = Math.max(0, left);
      paintTimer();
      if (tmr.left <= 0) {
        stopTimer();
        chime();
        paintTimer();
      }
    }, 200);
  }

  function toggleTimer() {
    if (tmr.running) {
      tmr.left = Math.max(0, (tmr.endAt - Date.now()) / 1000);
      stopTimer();
      paintTimer();
      return;
    }
    if (tmr.left <= 0) { tmr.left = tmr.total; }
    runTimer();
  }

  function setPreset(min) {
    stopTimer();
    tmr.total = min * 60;
    tmr.left = tmr.total;
    paintTimer();
  }

  function chime() {
    try {
      var AC = window.AudioContext || window.webkitAudioContext;
      if (!AC) { return; }
      var ac = new AC();
      var t0 = ac.currentTime;
      [523.25, 659.25, 783.99].forEach(function (freq, i) {
        var o = ac.createOscillator();
        var g = ac.createGain();
        o.type = 'sine';
        o.frequency.value = freq;
        g.gain.setValueAtTime(0.0001, t0 + i * 0.32);
        g.gain.linearRampToValueAtTime(0.16, t0 + i * 0.32 + 0.05);
        g.gain.exponentialRampToValueAtTime(0.0001, t0 + i * 0.32 + 1.5);
        o.connect(g);
        g.connect(ac.destination);
        o.start(t0 + i * 0.32);
        o.stop(t0 + i * 0.32 + 1.6);
      });
      setTimeout(function () { ac.close(); }, 3200);
    } catch (e) { /* silent */ }
  }

  function openDrill() {
    var item = DATA[state.selected === null ? state.liveIdx : state.selected];
    tmr.item = item;
    setText('drillTitle', item.organ);
    setText('drillBody', item.drill);
    setText('drillEyebrow', T.lblDrill);
    tmr.total = 180;
    tmr.left = 180;
    stopTimer();
    paintTimer();
    var ov = document.getElementById('drillOverlay');
    if (ov) {
      ov.classList.add('open');
      ov.setAttribute('aria-hidden', 'false');
    }
    clearTimeout(idleHandle);
  }

  function closeDrill() {
    stopTimer();
    var ov = document.getElementById('drillOverlay');
    if (ov) {
      ov.classList.remove('open');
      ov.setAttribute('aria-hidden', 'true');
    }
    armIdle();
  }

  /* ---------- screensaver ---------- */

  var idleHandle = null;

  function armIdle() {
    clearTimeout(idleHandle);
    if (state.saver) { return; }
    idleHandle = setTimeout(function () {
      var ov = document.getElementById('drillOverlay');
      if (ov && ov.classList.contains('open')) { return; }
      enterSaver();
    }, IDLE_MS);
  }

  function enterSaver() {
    state.saver = true;
    document.body.classList.add('saver');
  }

  function exitSaver() {
    if (!state.saver) { return; }
    state.saver = false;
    document.body.classList.remove('saver');
  }

  function onActivity() {
    if (state.saver) {
      exitSaver();
      state.lastArm = Date.now();
      armIdle();
      return;
    }
    if (Date.now() - state.lastArm > 1500) {
      state.lastArm = Date.now();
      armIdle();
    }
  }

  /* ---------- fullscreen ---------- */

  function toggleFullscreen() {
    if (!document.fullscreenElement) {
      var p = document.documentElement.requestFullscreen();
      if (p && p.catch) { p.catch(function () {}); }
    } else if (document.exitFullscreen) {
      document.exitFullscreen();
    }
  }

  function syncFullscreen() {
    var b = document.getElementById('btnFullscreen');
    if (!b) { return; }
    var on = !!document.fullscreenElement;
    b.setAttribute('aria-pressed', on ? 'true' : 'false');
    var label = document.getElementById('fsLabel');
    if (label) { label.textContent = on ? T.exitFullscreen : T.fullscreen; }
  }

  /* ---------- boot ---------- */

  function init() {
    buildRing();
    buildStrip();
    staticLabels();

    state.liveIdx = nowIndex(new Date());
    paint(state.liveIdx, true);

    var d = new Date();
    setText('liveClock', clockFull(d));

    setInterval(tick, 1000);

    var back = document.getElementById('pBack');
    if (back) { back.addEventListener('click', backToNow); }

    var bd = document.getElementById('btnDrill');
    if (bd) { bd.addEventListener('click', openDrill); }

    var x = document.getElementById('drillClose');
    if (x) { x.addEventListener('click', closeDrill); }

    var ov = document.getElementById('drillOverlay');
    if (ov) {
      ov.addEventListener('click', function (ev) {
        if (ev.target === ov) { closeDrill(); }
      });
    }

    var tg = document.getElementById('drillToggle');
    if (tg) { tg.addEventListener('click', toggleTimer); }

    var rs = document.getElementById('drillReset');
    if (rs) {
      rs.addEventListener('click', function () {
        stopTimer();
        tmr.left = tmr.total;
        paintTimer();
      });
    }

    Array.prototype.forEach.call(document.querySelectorAll('.ov-preset'), function (p) {
      p.addEventListener('click', function () {
        setPreset(Number(p.getAttribute('data-min')));
      });
    });

    var fb = document.getElementById('btnFullscreen');
    if (fb) { fb.addEventListener('click', toggleFullscreen); }
    document.addEventListener('fullscreenchange', syncFullscreen);

    var sb = document.getElementById('btnSaver');
    if (sb) {
      sb.addEventListener('click', function () {
        if (state.saver) { exitSaver(); } else { enterSaver(); }
      });
    }

    document.addEventListener('keydown', function (ev) {
      if (state.saver) {
        exitSaver();
        state.lastArm = Date.now();
        armIdle();
        return;
      }
      if (ev.key === 'Escape') {
        var o = document.getElementById('drillOverlay');
        if (o && o.classList.contains('open')) { closeDrill(); return; }
        if (state.saver) { exitSaver(); return; }
        if (state.selected !== null) { backToNow(); }
        return;
      }
      if (ev.target && /^(INPUT|TEXTAREA)$/.test(ev.target.tagName)) { return; }
      var ovEl = document.getElementById('drillOverlay');
      if (ovEl && ovEl.classList.contains('open')) { return; }
      if (ev.key === 'f' || ev.key === 'F') { toggleFullscreen(); }
      if (ev.key === 's' || ev.key === 'S') {
        if (state.saver) { exitSaver(); } else { enterSaver(); }
      }
      if (ev.key === 'n' || ev.key === 'N') { backToNow(); }
      if (ev.key === 'ArrowRight') {
        var cur = state.selected === null ? state.liveIdx : state.selected;
        select((cur + 1) % DATA.length);
      }
      if (ev.key === 'ArrowLeft') {
        var cur2 = state.selected === null ? state.liveIdx : state.selected;
        select((cur2 + DATA.length - 1) % DATA.length);
      }
    });

    ['pointermove', 'pointerdown', 'wheel', 'touchstart'].forEach(function (evt) {
      document.addEventListener(evt, onActivity, { passive: true });
    });

    syncFullscreen();
    state.lastArm = Date.now();
    armIdle();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
