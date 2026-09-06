/*
 * floating-nav.js
 *
 * A floating Home/Previous/Next bar that appears in the bottom-right
 * corner of the viewport once the user starts scrolling. Designed to
 * solve the problem of: "I've read to the bottom of a long deep-dive
 * page — now I have to scroll all the way back up to click Next."
 *
 * Behavior:
 *   - Hidden at page load (no JS-disclosure flicker)
 *   - Fades in once the user scrolls past 200px from the top
 *   - Fades out when at the very bottom of the page (where the
 *     sidebar-nav.js bottom bar already provides nav)
 *   - Fades out if the user scrolls back to the top
 *   - Three buttons: [⌂ Home] [← Prev] [Next →]
 *   - The two-page cheat sheet (last page) has Next disabled
 *   - The homepage has Prev disabled
 *   - On mobile/narrow screens, the FAB is more compact (icon-only)
 *   - All transitions use CSS — no layout thrash
 *
 * The prev/next is determined by walking the sidebar links in order,
 * same as sidebar-nav.js. The page list is shared logic but inlined
 * here so this file works standalone.
 */

(function() {
  'use strict';

  // Build a flat list of pages from the sidebar, in order.
  function buildPageList() {
    var items = document.querySelectorAll(
      '.md-nav--primary .md-nav__link[href]'
    );
    var pages = [];
    var seen = {};
    for (var i = 0; i < items.length; i++) {
      var link = items[i];
      var href = link.getAttribute('href');
      if (!href || href === '#') continue;
      if (/^(https?:|mailto:|tel:)/i.test(href)) continue;
      if (!/(\/|\.html|\.md)/i.test(href)) continue;
      var key = href.replace(/\.\//, '').replace(/\/$/, '').toLowerCase();
      if (seen[key]) continue;
      seen[key] = true;
      var ellipsis = link.querySelector('.md-ellipsis');
      var title = ellipsis ? ellipsis.textContent.trim() : key;
      if (title === 'Home' && pages.length > 0) continue;
      pages.push({ href: href, title: title });
    }
    return pages;
  }

  // Find the current page's index by matching the URL path.
  // Tries three strategies, in order of specificity:
  //   1. Exact last-2-segments match (most specific)
  //   2. First significant folder segment match (handles deep-dive pages
  //      that aren't in the sidebar — matches the folder they live in)
  //   3. document.title prefix match (last-resort heuristic)
  function findCurrentIndex(pages) {
    var currentPath = window.location.pathname
      .replace(/index\.html$/, '')
      .replace(/\/$/, '');
    var currentSegs = currentPath.split('/').filter(Boolean);
    // Strip /AI/ prefix if present (the repo name segment)
    if (currentSegs[0] === 'AI') currentSegs = currentSegs.slice(1);

    // Strategy 1: exact last-2-segments match
    var currentTail = currentSegs.slice(-2).join('/').toLowerCase();
    for (var i = 0; i < pages.length; i++) {
      var pageHref = normalizeHref(pages[i].href);
      var pageTail = pageHref.split('/').filter(Boolean).slice(-2).join('/').toLowerCase();
      if (pageTail && pageTail === currentTail) return i;
    }

    // Strategy 2: first significant folder segment match
    // If the current URL starts with /Forehand/, match any page whose
    // href is in the Forehand/ folder.
    var currentFolder = currentSegs.length > 0 ? currentSegs[0].toLowerCase() : '';
    if (currentFolder && currentFolder !== 'index.html') {
      var bestMatch = -1;
      var bestScore = -1;
      for (var j = 0; j < pages.length; j++) {
        var pHref = normalizeHref(pages[j].href);
        var pSegs = pHref.split('/').filter(Boolean);
        if (pSegs[0] && pSegs[0].toLowerCase() === currentFolder) {
          // Score: prefer pages whose 2nd segment matches current 2nd
          var score = (pSegs[1] && pSegs[1].toLowerCase() === (currentSegs[1] || '').toLowerCase()) ? 2 : 1;
          if (score > bestScore) {
            bestScore = score;
            bestMatch = j;
          }
        }
      }
      if (bestMatch >= 0) return bestMatch;
    }

    // Strategy 3: document.title prefix match
    var docTitle = (document.title || '').toLowerCase();
    if (docTitle) {
      for (var k = 0; k < pages.length; k++) {
        var pTitle = (pages[k].title || '').toLowerCase();
        if (pTitle && docTitle.indexOf(pTitle) >= 0) return k;
      }
    }

    return -1;
  }

  // Normalize a sidebar href by stripping prefixes and trailing slashes
  function normalizeHref(href) {
    return href
      .replace(/^\.\//, '')
      .replace(/^\//, '')
      .replace(/^(\.\.\/)+/, '')  // strip ../../  ../  etc.
      .replace(/index\.html$/, '')
      .replace(/\/$/, '');
  }

  // Truncate a title for the tooltip
  function shortTitle(title) {
    var parts = title.split(/\s+[—–-]\s+/);
    return parts[0] || title;
  }

  // Build a single button element
  function makeButton(cls, href, arrow, label, title, disabled) {
    var a = document.createElement('a');
    a.className = 'hh-fab-btn hh-fab-' + cls + (disabled ? ' hh-fab-btn--disabled' : '');
    a.href = disabled ? '#' : href;
    a.title = title;
    a.setAttribute('aria-label', title);
    if (disabled) a.setAttribute('aria-disabled', 'true');
    a.innerHTML =
      '<span class="hh-fab-icon">' + arrow + '</span>' +
      '<span class="hh-fab-label">' + label + '</span>';
    return a;
  }

  function init() {
    var pages = buildPageList();
    if (pages.length === 0) return;
    var idx = findCurrentIndex(pages);
    if (idx < 0) return;

    var home = { href: '.', title: 'Home' };
    var prev = idx > 0 ? pages[idx - 1] : null;
    var next = idx < pages.length - 1 ? pages[idx + 1] : null;

    // Build the FAB container
    var fab = document.createElement('div');
    fab.className = 'hh-fab';
    fab.setAttribute('aria-label', 'Page navigation');
    fab.setAttribute('role', 'navigation');

    // Add the three buttons (Home is always enabled, others disabled at edges)
    fab.appendChild(makeButton(
      'home', home.href, '⌂', 'Home',
      'Home — Complete Manual v2', false
    ));
    fab.appendChild(makeButton(
      'prev', prev ? prev.href : '#', '←', 'Previous',
      prev ? 'Previous: ' + prev.title : 'No previous page',
      !prev
    ));
    fab.appendChild(makeButton(
      'next', next ? next.href : '#', '→', 'Next',
      next ? 'Next: ' + next.title : 'No next page',
      !next
    ));

    document.body.appendChild(fab);

    // Show/hide the FAB based on scroll position.
    // Throttle with rAF to avoid layout thrash on long pages.
    var isVisible = false;
    var ticking = false;

    function update() {
      ticking = false;
      var scrollY = window.pageYOffset || document.documentElement.scrollTop;
      var docHeight = Math.max(
        document.body.scrollHeight,
        document.documentElement.scrollHeight
      );
      var winHeight = window.innerHeight;
      var atBottom = (scrollY + winHeight) >= (docHeight - 100);
      var shouldShow = scrollY > 200 && !atBottom;
      if (shouldShow !== isVisible) {
        isVisible = shouldShow;
        if (isVisible) {
          fab.classList.add('hh-fab--visible');
        } else {
          fab.classList.remove('hh-fab--visible');
        }
      }
    }

    function onScroll() {
      if (!ticking) {
        window.requestAnimationFrame(update);
        ticking = true;
      }
    }

    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll, { passive: true });
    // Initial check (in case the page is loaded already scrolled)
    update();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
