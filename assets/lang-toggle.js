(function() {
  'use strict';

  function getToggleUrl() {
    var path = window.location.pathname;
    // If we are in /vi/, switch to root. Otherwise switch to /vi/
    if (path.startsWith('/vi/') || path === '/vi' || path === '/vi.html') {
      return path.replace(/^\/vi\//, '/').replace(/^\/vi$/, '/').replace('/vi.html', '/index.html');
    } else {
      return '/vi/' + path.replace(/^\//, '');
    }
  }

  function getLabel() {
    var path = window.location.pathname;
    if (path.startsWith('/vi/') || path === '/vi' || path === '/vi.html') {
      return 'English';
    }
    return 'Tiếng Việt';
  }

  function init() {
    // Material for MkDocs top bar container
    var topBar = document.querySelector('.md-header__inner');
    if (!topBar) return;

    var toggle = document.createElement('a');
    toggle.className = 'hh-lang-toggle';
    toggle.href = getToggleUrl();
    toggle.textContent = getLabel();
    toggle.title = 'Switch Language / Chuyển Ngôn Ngữ';

    // Inject into the top bar
    topBar.appendChild(toggle);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
