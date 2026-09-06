/*
 * open-external-links.js
 *
 * Auto-adds target="_blank" (and rel="noopener noreferrer" for security) to
 * any link whose href starts with http:// or https://. mailto:, tel:,
 * anchor, and internal links are left alone.
 *
 * Why: MkDocs nav YAML supports external URLs as values but does NOT
 * support HTML attributes like target="_blank". This 2KB JS is the
 * verified fix. Hook via extra_javascript in mkdocs.yml.
 */
(function() {
  'use strict';

  function openExternalLinksInNewTab() {
    var links = document.querySelectorAll(
      '.md-tabs__link, .md-nav__link, .md-content a'
    );
    for (var i = 0; i < links.length; i++) {
      var link = links[i];
      var href = link.getAttribute('href');
      if (!href) continue;
      // Skip mailto:, tel:, anchor, and internal links
      if (
        href.indexOf('mailto:') === 0 ||
        href.indexOf('tel:') === 0 ||
        href.indexOf('#') === 0 ||
        href.indexOf('/') === 0 ||
        href.indexOf('./') === 0 ||
        href.indexOf('../') === 0
      ) continue;
      // If full URL, mark as external
      if (href.indexOf('http://') === 0 || href.indexOf('https://') === 0) {
        link.setAttribute('target', '_blank');
        var rel = link.getAttribute('rel') || '';
        if (rel.indexOf('noopener') === -1) {
          link.setAttribute('rel', (rel + ' noopener noreferrer').trim());
        }
      }
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', openExternalLinksInNewTab);
  } else {
    openExternalLinksInNewTab();
  }
})();