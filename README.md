# HTML, CSS & JavaScript – Practical Assignment

A production-grade, fully functional frontend laboratory website containing all **212 practical programs** specified in the curriculum assignment.

---

## Student Information

- **Student Name:** M.Surya Nivas Reddy
- **Register Number:** *(Enter Register Number here)*
- **Class / Section:** *(Enter Class / Section here)*
- **Subject:** HTML, CSS & JavaScript
- **Assignment:** Practical Assignment
- **Total Programs Completed:** **212 Programs** (15 HTML + 75 CSS + 122 JavaScript)

---

## Project Summary & Statistics

| Module | Category | Folder | Program Range | Count |
|---|---|---|---|---|
| **01** | **HTML Programs** | `html/` | `html-01.html` to `html-15.html` | **15** |
| **02** | **CSS Programs** | `css/` | `css-01.html` to `css-75.html` | **75** |
| **03** | **Core JavaScript & Algorithms** | `javascript/core/` | `js-01.html` to `js-67.html` | **67** |
| **04** | **DOM Manipulation** | `javascript/dom-manipulation/` | `dom-01.html` to `dom-15.html` | **15** |
| **05** | **JavaScript Events** | `javascript/events/` | `event-01.html` to `event-08.html` | **8** |
| **06** | **Forms & Validation** | `javascript/forms-validation/` | `form-01.html` to `form-07.html` | **7** |
| **07** | **Browser Objects & Web Storage** | `javascript/browser-storage/` | `storage-01.html` to `storage-08.html` | **8** |
| **08** | **Mini Projects** | `javascript/mini-projects/` | `project-01.html` to `project-17.html` | **17** |
| **TOTAL** | **All Categories** | - | - | **212** |

---

## Directory Hierarchy

```
htmlcss/
├── index.html                                 # Main Dashboard (3 Primary Section Cards)
├── README.md                                  # Complete Project Documentation & Index
├── assets/
│   ├── css/
│   │   └── style.css                          # Modern Unified Design System & Themes
│   └── js/
│       └── common.js                          # Theme Toggle, Code Drawer, Search Filter
├── html/
│   ├── index.html                             # HTML Suite Catalog (15 Programs)
│   ├── html-01.html ... html-15.html          # Individual HTML Program Pages
├── css/
│   ├── index.html                             # CSS Suite Catalog (75 Programs)
│   ├── css-01.html ... css-75.html            # Individual CSS Program Pages
└── javascript/
    ├── index.html                             # Master JavaScript Hub (6 Categories)
    ├── core/
    │   ├── index.html                         # Core JS & Algorithms Listing (67 Programs)
    │   ├── js-01.html ... js-67.html          # Individual Algorithmic Pages
    ├── dom-manipulation/
    │   ├── index.html                         # DOM Manipulation Listing (15 Programs)
    │   ├── dom-01.html ... dom-15.html        # Individual DOM Pages
    ├── events/
    │   ├── index.html                         # Events Listing (8 Programs)
    │   ├── event-01.html ... event-08.html    # Individual Event Pages
    ├── forms-validation/
    │   ├── index.html                         # Forms & Validation Listing (7 Programs)
    │   ├── form-01.html ... form-07.html      # Individual Validation Pages
    ├── browser-storage/
    │   ├── index.html                         # Browser & Storage Listing (8 Programs)
    │   ├── storage-01.html ... storage-08.html# Individual Storage Pages
    └── mini-projects/
        ├── index.html                         # Mini Projects Listing (17 Applications)
        ├── project-01.html ... project-17.html # 17 Standalone Mini Applications
```

---

## Key Features

1. **Dashboard Architecture**:
   - The home page (`index.html`) prominently displays the 3 required section cards: **HTML Programs**, **CSS Programs**, and **JavaScript Programs**, each with immediate navigation buttons.
2. **Every Program as a Standalone Page**:
   - Exactly 212 separate `.html` files have been created. None are combined or skipped.
3. **Interactive Demonstrations**:
   - Every program provides live, working interactive UI elements (calculators, timers, form validators, draggable boards, games, styling visualizers).
4. **Built-in Source Code Inspector**:
   - Every program page includes a collapsible **"Source Code Inspector"** drawer allowing immediate inspection of the HTML/CSS/JS source code directly inside the browser.
5. **Bidirectional Navigation**:
   - Every single program includes header breadcrumbs, a `[ 🏠 Home ]` link, a `[ 📋 Back to Programs ]` link, and `[ ⬅ Previous ]` / `[ Next ➡ ]` sequential browsing controls. Keyboard shortcuts (`[` / `]`) are also supported.
6. **Dark / Light Mode**:
   - Seamless palette switching powered by CSS custom properties and persisted in `localStorage`.
7. **Zero Broken Links**:
   - All internal links resolve to valid relative paths across directories.

---

## Verification & Execution

To view and execute the project:
1. Double-click `index.html` in any modern web browser (Google Chrome, Microsoft Edge, Mozilla Firefox, Safari).
2. Alternatively, serve via any local development server:
   ```bash
   python -m http.server 8000
   ```
   and navigate to `http://localhost:8000`.

---
*Created as part of the Web Technologies Laboratory Practical Assignment.*
