(function() {
  'use strict';

  // Only run on Vietnamese book pages
  var path = window.location.pathname;
  if (!path.includes('/vi/books/')) return;

  var books = [
    { title: 'Baguazhang Vol.1', url: '/vi/books/Baguazhang%20-%20the%20Complete%20System%20(Vol.1)%20by%20Erle%20Montaigue/Baguazhang%20-%20the%20Complete%20System%20(Vol.1)%20by%20Erle%20Montaigue_vi.html' },
    { title: 'Baguazhang Vol.2', url: '/vi/books/Baguazhang%20-%20the%20Complete%20System%20(Vol.2)/Baguazhang%20-%20the%20Complete%20System%20(Vol.2)_vi.html' },
    { title: 'Bản chất kình lực', url: '/vi/books/B%E1%BA%A3n%20ch%E1%BA%A5t%20k%C3%ACnh%20l%E1%BB%B1c%20trong%20v%C3%B5%20thu%E1%BA%ADt%20n%E1%BB%99i%20gia/B%E1%BA%A3n%20ch%E1%BA%A5t%20k%C3%ACnh%20l%E1%BB%B1c%20trong%20v%C3%B5%20thu%E1%BA%ADt%20n%E1%BB%99i%20gia_vi.html' },
    { title: 'Bát quái quyền chưởng', url: '/vi/books/b%C3%A1t%20qu%C3%A1i%20quy%E1%BB%81n%20ch%C6%B0%E1%BB%9Fng/b%C3%A1t%20qu%C3%A1i%20quy%E1%BB%81n%20ch%C6%B0%E1%BB%9Fng_vi.html' },
    { title: "Beginner's Guide Qigong", url: '/vi/books/Beginners-guide-to-understanding-qigong/Beginners-guide-to-understanding-qigong_vi.html' },
    { title: 'Chen-Style Handout', url: '/vi/books/Chen-Style-Tai-Chi-Handout-Jerry-Cheng/Chen-Style-Tai-Chi-Handout-Jerry-Cheng_vi.html' },
    { title: 'Chikung Bible', url: '/vi/books/Chikung%20bible/Chikung%20bible_vi.html' },
    { title: 'Xing Yi Nei Gong', url: '/vi/books/Dan%20Miller%20and%20Tim%20Cartmell%20-%20Xing%20Yi%20Nei%20Gong/Dan%20Miller%20and%20Tim%20Cartmell%20-%20Xing%20Yi%20Nei%20Gong_vi.html' },
    { title: 'How Stuff Works', url: '/vi/books/How%20Stuff%20Works/How%20Stuff%20Works_vi.html' }
  ];

  function init() {
    // Remove any existing sidebar-nav-bar
    var existingBars = document.querySelectorAll('.hh-nav-bar');
    existingBars.forEach(function(bar) { bar.remove(); });

    // Create sidebar container
    var sidebar = document.createElement('div');
    sidebar.className = 'hh-vi-sidebar';
    sidebar.innerHTML = '<div class="hh-vi-sidebar-header">📚 Sách đã dịch</div><ul class="hh-vi-sidebar-list"></ul>';
    var list = sidebar.querySelector('.hh-vi-sidebar-list');

    books.forEach(function(book) {
      var li = document.createElement('li');
      var a = document.createElement('a');
      a.href = book.url;
      a.textContent = book.title;
      if (path === book.url.replace(/%/g, '%')) {
        a.classList.add('hh-vi-sidebar-active');
      }
      // Check if current page matches this book
      if (window.location.pathname === book.url) {
        a.classList.add('hh-vi-sidebar-active');
      }
      li.appendChild(a);
      list.appendChild(li);
    });

    document.body.appendChild(sidebar);

    // Add toggle button for mobile
    var toggle = document.createElement('button');
    toggle.className = 'hh-vi-sidebar-toggle';
    toggle.textContent = '📚';
    toggle.onclick = function() {
      sidebar.classList.toggle('hh-vi-sidebar-open');
    };
    document.body.appendChild(toggle);
  }

  // Add sidebar styles
  var style = document.createElement('style');
  style.textContent = `
    .hh-vi-sidebar {
      position: fixed;
      left: 0;
      top: 0;
      width: 240px;
      height: 100vh;
      background: #0f172a;
      color: #fff;
      padding: 1rem 0;
      overflow-y: auto;
      z-index: 1000;
      transition: transform 0.3s ease;
    }
    .hh-vi-sidebar-header {
      font-size: 1rem;
      font-weight: 700;
      padding: 0.75rem 1.25rem;
      border-bottom: 1px solid #1e293b;
      margin-bottom: 0.5rem;
    }
    .hh-vi-sidebar-list {
      list-style: none;
      padding: 0;
      margin: 0;
    }
    .hh-vi-sidebar-list li a {
      display: block;
      padding: 0.6rem 1.25rem;
      color: #cbd5e1;
      text-decoration: none;
      font-size: 0.9rem;
      transition: background 0.2s, color 0.2s;
    }
    .hh-vi-sidebar-list li a:hover {
      background: #1e293b;
      color: #fff;
    }
    .hh-vi-sidebar-list li a.hh-vi-sidebar-active {
      background: #0284c7;
      color: #fff;
      font-weight: 600;
    }
    .hh-vi-sidebar-toggle {
      display: none;
      position: fixed;
      bottom: 1rem;
      left: 1rem;
      z-index: 1001;
      background: #0284c7;
      color: #fff;
      border: none;
      border-radius: 50%;
      width: 3rem;
      height: 3rem;
      font-size: 1.25rem;
      cursor: pointer;
      box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }
    @media (max-width: 768px) {
      .hh-vi-sidebar {
        transform: translateX(-100%);
      }
      .hh-vi-sidebar.hh-vi-sidebar-open {
        transform: translateX(0);
      }
      .hh-vi-sidebar-toggle {
        display: block;
      }
    }
    /* Shift content when sidebar is visible on desktop */
    @media (min-width: 769px) {
      .md-content, .reader-container {
        margin-left: 240px !important;
      }
      .md-header {
        padding-left: 240px;
      }
    }
  `;
  document.head.appendChild(style);

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
