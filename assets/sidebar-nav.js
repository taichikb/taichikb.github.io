/*
 * sidebar-nav.js
 *
 * Builds browser-style Home / Previous / Next navigation bars by walking
 * the rendered sidebar DOM at runtime. Two bars are injected:
 *   1. At the top of the sidebar (sticky)
 *   2. At the bottom of the article
 * No per-page config needed — adding a new DD to nav: automatically
 * updates the prev/next ordering on next build.
 *
 * Verified pattern from the tennis-coach-system library.
 */
(function() {
  'use strict';

  function buildPageList() {
    var items = document.querySelectorAll('.md-nav--primary .md-nav__link[href]');
    var pages = [], seen = {};
    for (var i = 0; i < items.length; i++) {
      var link = items[i];
      var href = link.getAttribute('href');
      if (!href || href === '#') continue;
      if (/^(https?:|mailto:|tel:)/i.test(href)) continue;
      // Skip non-page links (anchors only)
      var key = href.replace(/^\.\//, '').replace(/\/$/, '').toLowerCase();
      if (seen[key]) continue;
      seen[key] = true;
      var ellipsis = link.querySelector('.md-ellipsis');
      var title = ellipsis ? ellipsis.textContent.trim() : key;
      pages.push({ href: href, title: title });
    }
    return pages;
  }

  function findCurrentIndex(pages) {
    var currentPath = window.location.pathname
      .replace(/index\.html$/, '').replace(/\/$/, '');
    var currentSegs = currentPath.split('/').filter(Boolean);
    if (currentSegs.length === 0) {
      // We're at root; match the homepage (index.html)
      for (var i = 0; i < pages.length; i++) {
        var h = pages[i].href.replace(/^\.\//, '').replace(/\/$/, '');
        if (h === '' || h === 'index' || h === 'index.html') return i;
      }
      return -1;
    }
    // Strip /tennis/ or /AI/ prefix if present
    if (currentSegs[0] === 'tennis' || currentSegs[0] === 'AI') {
      currentSegs = currentSegs.slice(1);
    }
    // Strategy 1: exact last-2-segments match
    var currentTail = currentSegs.slice(-2).join('/').toLowerCase();
    for (var j = 0; j < pages.length; j++) {
      var pageHref = normalizeHref(pages[j].href);
      var pageTail = pageHref.split('/').filter(Boolean).slice(-2).join('/');
      if (pageTail && pageTail === currentTail) return j;
    }
    // Strategy 2: last-segment match (filenames like DD1_The_Player_in_Motion.md)
    var currentFile = currentSegs.slice(-1)[0].toLowerCase();
    for (var k = 0; k < pages.length; k++) {
      var h2 = normalizeHref(pages[k].href);
      var h2File = h2.split('/').filter(Boolean).slice(-1)[0].toLowerCase();
      if (h2File && h2File === currentFile) return k;
    }
    return -1;
  }

  function normalizeHref(href) {
    return href
      .replace(/^\.\//, '')
      .replace(/^\//, '')
      .replace(/^(\.\.\/)+/, '')
      .replace(/index\.html$/, '')
      .replace(/\/$/, '');
  }

  function buildBar(home, prev, next, position) {
    var bar = document.createElement('nav');
    bar.className = 'hh-nav-bar hh-nav-bar--' + position;
    bar.setAttribute('aria-label', position === 'top' ? 'Top navigation' : 'Bottom navigation');

    function makeBtn(target, label, title, isHome, isDisabled) {
      var a = document.createElement('a');
      a.className = 'hh-nav-btn' + (isHome ? ' hh-nav-home' : '') + (isDisabled ? ' hh-nav-btn--disabled' : '');
      if (target) a.setAttribute('href', target);
      else a.setAttribute('aria-disabled', 'true');
      a.setAttribute('title', title);
      var eyebrow = document.createElement('span');
      eyebrow.className = 'hh-nav-eyebrow';
      eyebrow.textContent = label;
      var labelSpan = document.createElement('span');
      labelSpan.className = 'hh-nav-label';
      labelSpan.textContent = title;
      var titleEl = document.createElement('span');
      titleEl.className = 'hh-nav-title';
      titleEl.textContent = title;
      a.appendChild(eyebrow);
      a.appendChild(labelSpan);
      a.appendChild(titleEl);
      return a;
    }

    // Left button: Home (always present)
    bar.appendChild(makeBtn(home ? home.href : '.', 'Home', 'Home', true, !home));
    // Middle button: Previous
    if (prev) {
      bar.appendChild(makeBtn(prev.href, '← Previous', prev.title, false, false));
    } else {
      bar.appendChild(makeBtn(null, '← Previous', 'First page', false, true));
    }
    // Right button: Next
    if (next) {
      bar.appendChild(makeBtn(next.href, 'Next →', next.title, false, false));
    } else {
      bar.appendChild(makeBtn(null, 'Next →', 'Last page', false, true));
    }
    return bar;
  }

  function init() {
    var pages = buildPageList();
    if (pages.length === 0) return;
    var idx = findCurrentIndex(pages);
    if (idx < 0) return;
    var home = { href: '.', title: 'Home' };
    var prev = idx > 0 ? pages[idx - 1] : null;
    var next = idx < pages.length - 1 ? pages[idx + 1] : null;
    // Top bar in sidebar
    var sidebar = document.querySelector('.md-sidebar--primary .md-sidebar__inner');
    if (sidebar) {
      var topBar = buildBar(home, prev, next, 'top');
      sidebar.insertBefore(topBar, sidebar.firstChild);
    }
    // Bottom bar in article
    var content = document.querySelector('.md-content__inner');
    if (content) {
      var bottomBar = buildBar(home, prev, next, 'bottom');
      content.appendChild(bottomBar);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();