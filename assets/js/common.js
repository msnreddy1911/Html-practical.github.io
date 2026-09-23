/**
 * Common JavaScript functionality for HTML, CSS & JavaScript Practical Portal
 */

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initCodeDrawer();
  initSearchFilter();
  initKeyNav();
});

// Theme Management
function initTheme() {
  const savedTheme = localStorage.getItem('app-theme') || 'dark';
  document.documentElement.setAttribute('data-theme', savedTheme);
  updateThemeButton(savedTheme);

  const toggleBtn = document.getElementById('themeToggleBtn');
  if (toggleBtn) {
    toggleBtn.addEventListener('click', () => {
      const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('app-theme', newTheme);
      updateThemeButton(newTheme);
    });
  }
}

function updateThemeButton(theme) {
  const toggleBtn = document.getElementById('themeToggleBtn');
  if (toggleBtn) {
    toggleBtn.innerHTML = theme === 'dark' ? '☀️ Light Mode' : '🌙 Dark Mode';
  }
}

// Code Drawer Toggle
function initCodeDrawer() {
  const headers = document.querySelectorAll('.code-header');
  headers.forEach(header => {
    header.addEventListener('click', () => {
      header.classList.toggle('expanded');
      const content = header.nextElementSibling;
      if (content && content.classList.contains('code-content')) {
        content.classList.toggle('show');
        const arrow = header.querySelector('.code-arrow');
        if (arrow) {
          arrow.textContent = content.classList.contains('show') ? '▲ Hide Code' : '▼ View Code';
        }
      }
    });
  });
}

// Program Search and Filtering
function initSearchFilter() {
  const searchInput = document.getElementById('programSearch');
  const filterTags = document.querySelectorAll('.filter-tag');
  const programCards = document.querySelectorAll('.program-card');

  if (!searchInput && filterTags.length === 0) return;

  function filterCards() {
    const query = searchInput ? searchInput.value.toLowerCase().trim() : '';
    const activeTag = document.querySelector('.filter-tag.active');
    const selectedCategory = activeTag ? activeTag.getAttribute('data-filter') : 'all';

    programCards.forEach(card => {
      const title = card.querySelector('.program-title')?.textContent.toLowerCase() || '';
      const desc = card.querySelector('.program-desc')?.textContent.toLowerCase() || '';
      const number = card.querySelector('.program-number')?.textContent.toLowerCase() || '';
      const category = card.getAttribute('data-category') || 'all';

      const matchesQuery = !query || title.includes(query) || desc.includes(query) || number.includes(query);
      const matchesCategory = selectedCategory === 'all' || category === selectedCategory;

      if (matchesQuery && matchesCategory) {
        card.style.display = 'flex';
      } else {
        card.style.display = 'none';
      }
    });
  }

  if (searchInput) {
    searchInput.addEventListener('input', filterCards);
  }

  filterTags.forEach(tag => {
    tag.addEventListener('click', () => {
      filterTags.forEach(t => t.classList.remove('active'));
      tag.classList.add('active');
      filterCards();
    });
  });
}

// Keyboard shortcuts for previous / next navigation
function initKeyNav() {
  document.addEventListener('keydown', (e) => {
    // Only trigger if not typing in an input or textarea
    if (['INPUT', 'TEXTAREA', 'SELECT'].includes(document.activeElement.tagName)) return;

    if (e.key === 'ArrowLeft' || e.key === '[') {
      const prevBtn = document.querySelector('.btn-prev');
      if (prevBtn && prevBtn.getAttribute('href') && prevBtn.getAttribute('href') !== '#') {
        window.location.href = prevBtn.getAttribute('href');
      }
    } else if (e.key === 'ArrowRight' || e.key === ']') {
      const nextBtn = document.querySelector('.btn-next');
      if (nextBtn && nextBtn.getAttribute('href') && nextBtn.getAttribute('href') !== '#') {
        window.location.href = nextBtn.getAttribute('href');
      }
    }
  });
}

// Copy Code to Clipboard helper
function copySnippet(codeId, btnElement) {
  const codeEl = document.getElementById(codeId);
  if (!codeEl) return;
  navigator.clipboard.writeText(codeEl.innerText).then(() => {
    const originalText = btnElement.innerText;
    btnElement.innerText = 'Copied!';
    setTimeout(() => {
      btnElement.innerText = originalText;
    }, 2000);
  });
}
