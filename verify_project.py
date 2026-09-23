"""
Automated Verification Script for HTML, CSS & JavaScript Practical Programs Website
Verifies:
1. Exact program counts across all categories
2. All index.html dashboards
3. Relative link resolution (zero 404 broken links)
4. Assets integrity (style.css, common.js)
"""
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))

EXPECTED_COUNTS = {
    os.path.join("html"): 15,
    os.path.join("css"): 75,
    os.path.join("javascript", "core"): 67,
    os.path.join("javascript", "dom-manipulation"): 15,
    os.path.join("javascript", "events"): 8,
    os.path.join("javascript", "forms-validation"): 7,
    os.path.join("javascript", "browser-storage"): 8,
    os.path.join("javascript", "mini-projects"): 17,
}

INDEX_FILES = [
    "index.html",
    os.path.join("html", "index.html"),
    os.path.join("css", "index.html"),
    os.path.join("javascript", "index.html"),
    os.path.join("javascript", "core", "index.html"),
    os.path.join("javascript", "dom-manipulation", "index.html"),
    os.path.join("javascript", "events", "index.html"),
    os.path.join("javascript", "forms-validation", "index.html"),
    os.path.join("javascript", "browser-storage", "index.html"),
    os.path.join("javascript", "mini-projects", "index.html"),
]

def verify_counts():
    print("=" * 60)
    print("1. VERIFYING PROGRAM COUNTS")
    print("=" * 60)
    grand_total = 0
    all_passed = True
    for folder, expected in EXPECTED_COUNTS.items():
        full_dir = os.path.join(ROOT, folder)
        files = [f for f in os.listdir(full_dir) if f.endswith(".html") and f != "index.html"]
        count = len(files)
        status = "PASSED" if count == expected else "FAILED"
        print(f"[{status}] {folder:35s}: Found {count:02d} / Expected {expected:02d}")
        if count != expected:
            all_passed = False
        grand_total += count
    
    print("-" * 60)
    print(f"GRAND TOTAL PROGRAMS: {grand_total} / 212 Expected")
    assert grand_total == 212, f"Expected 212 total programs, got {grand_total}"
    assert all_passed, "Some category counts did not match!"
    print("All program counts verified successfully!\n")

def verify_indexes():
    print("=" * 60)
    print("2. VERIFYING INDEX DASHBOARDS")
    print("=" * 60)
    for idx in INDEX_FILES:
        path = os.path.join(ROOT, idx)
        exists = os.path.isfile(path)
        status = "PASSED" if exists else "FAILED"
        print(f"[{status}] Index File: {idx}")
        assert exists, f"Missing index file: {path}"
    print("All 10 index dashboards verified successfully!\n")

def verify_links():
    print("=" * 60)
    print("3. VERIFYING INTERNAL LINK INTEGRITY (ZERO BROKEN LINKS)")
    print("=" * 60)
    broken_links = []
    total_links_checked = 0

    link_pattern = re.compile(r'(?:href|src)=["\']([^"\'#]+)["\']')

    for root_dir, _, files in os.walk(ROOT):
        for f in files:
            if not f.endswith(".html"):
                continue
            html_path = os.path.join(root_dir, f)
            with open(html_path, "r", encoding="utf-8") as file_obj:
                content = file_obj.read()
            
            for match in link_pattern.finditer(content):
                target = match.group(1).strip()
                # Skip external protocols, data URLs, anchors, mailto, tel
                if target.startswith(("http://", "https://", "mailto:", "tel:", "data:", "javascript:")):
                    continue
                if not target:
                    continue
                
                # Resolve target relative to html_path's directory
                file_dir = os.path.dirname(html_path)
                resolved_path = os.path.normpath(os.path.join(file_dir, target))
                total_links_checked += 1

                if not os.path.exists(resolved_path):
                    broken_links.append((html_path, target, resolved_path))

    print(f"Checked {total_links_checked} internal relative links across all files.")
    if broken_links:
        print(f"ERROR: Found {len(broken_links)} broken links:")
        for src, tgt, res in broken_links[:10]:
            print(f"  In {os.path.relpath(src, ROOT)} -> '{tgt}' not found at '{os.path.relpath(res, ROOT)}'")
        assert False, f"Broken links detected ({len(broken_links)} total)"
    else:
        print("PASSED: 100% of internal links resolved with 0 broken links!\n")

def main():
    verify_counts()
    verify_indexes()
    verify_links()
    print("=" * 60)
    print("ALL PROJECT VERIFICATION CHECKS PASSED PERFECTLY!")
    print("=" * 60)

if __name__ == "__main__":
    main()
