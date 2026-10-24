/*
 * lang-toggle.js
 * Language toggle button injected into the top navigation bar.
 * Runs on window.load to ensure MkDocs Material JS has finished.
 */
(function() {
  'use strict';

  function getToggleUrl() {
    var path = window.location.pathname;
    if (path.indexOf('/vi/') === 0 || path === '/vi' || path === '/vi.html') {
      return path.replace(/^\/vi\//, '/').replace(/^\/vi$/, '/').replace('/vi.html', '/index.html');
    } else {
      return '/vi/' + path.replace(/^\//, '');
    }
  }

  function getLabel() {
    var path = window.location.pathname;
    if (path.indexOf('/vi/') === 0 || path === '/vi' || path === '/vi.html') {
      return 'English';
    }
    return 'Tiếng Việt';
  }

  function init() {
    var topBar = document.querySelector('.md-header__inner');
    if (!topBar) {
      topBar = document.querySelector('.md-header');
    }
    if (!topBar) return;

    // Remove existing toggle if present
    var existing = document.querySelector('#hh-lang-toggle');
    if (existing) existing.remove();

    var toggle = document.createElement('a');
    toggle.id = 'hh-lang-toggle';
    toggle.href = getToggleUrl();
    toggle.textContent = getLabel();
    toggle.title = 'Switch Language / Chuyển Ngôn Ngữ';
    toggle.style.cssText = [
      'display:inline-flex',
      'align-items:center',
      'justify-content:center',
      'padding:4px 12px',
      'margin-left:16px',
      'border-radius:4px',
      'background:var(--md-primary-fg-color,#009688)',
      'color:var(--md-primary-bg-color,#fff)',
      'text-decoration:none',
      'font-size:13px',
      'font-weight:700',
      'cursor:pointer',
      'border:none',
      'line-height:1',
      'white-space:nowrap',
      'flex-shrink:0'
    ].join(';');

    toggle.onmouseover = function() { this.style.opacity = '0.85'; };
    toggle.onmouseout = function() { this.style.opacity = '1'; };

    topBar.appendChild(toggle);
  }

  if (document.readyState === 'complete') {
    setTimeout(init, 100);
  } else {
    window.addEventListener('load', function() {
      setTimeout(init, 100);
    });
  }
})();
