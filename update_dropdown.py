#!/usr/bin/env python3
"""
Script to add Leistungen dropdown menu to all subpages.
Adds CSS, HTML, and JavaScript modifications based on the frontpage template.
"""

import re
from pathlib import Path

# List of files to modify
FILES_TO_MODIFY = [
    "ueber-uns.html",
    "referenzen.html",
    "holzrahmenbau.html",
    "neubau.html",
    "dachsanierung.html",
    "dachfenster.html",
    "treppenbau.html",
    "asbestsanierung.html",
    "aufstockungen.html",
    "dachgauben.html",
    "massivholzhaus.html",
    "impressum.html",
    "datenschutz.html",
]

BASE_DIR = Path(__file__).parent

# CSS for Dropdown (to be inserted after .nav-cta:hover)
DROPDOWN_CSS = """
        /* ===================== DROPDOWN MENU ===================== */

        .nav-dropdown {
            position: relative;
        }

        .nav-dropdown-toggle {
            display: flex;
            align-items: center;
            gap: 4px;
            cursor: pointer;
        }

        .dropdown-icon {
            width: 12px;
            height: 12px;
            transition: transform 0.2s;
        }

        .nav-dropdown:hover .dropdown-icon {
            transform: rotate(180deg);
        }

        .nav-dropdown-menu {
            position: absolute;
            top: calc(100% + 12px);
            left: 0;
            background: var(--white);
            border-radius: 8px;
            box-shadow: 0 4px 24px rgba(0, 0, 0, 0.1), 0 0 0 1px rgba(0, 0, 0, 0.05);
            min-width: 200px;
            padding: var(--space-xs) 0;
            opacity: 0;
            visibility: hidden;
            transform: translateY(-8px);
            transition: opacity 0.2s, transform 0.2s, visibility 0.2s;
            z-index: 1000;
        }

        .nav-dropdown:hover .nav-dropdown-menu {
            opacity: 1;
            visibility: visible;
            transform: translateY(0);
        }

        .nav-dropdown-menu a {
            display: block;
            padding: 10px 20px;
            color: var(--gray-700);
            text-decoration: none;
            font-size: 14px;
            font-weight: 500;
            transition: all 0.2s;
        }

        .nav-dropdown-menu a:hover {
            background: var(--gray-50);
            color: var(--brand-red);
            padding-left: 24px;
        }

        /* Mobile Dropdown */
        .mobile-dropdown {
            display: flex;
            flex-direction: column;
        }

        .mobile-dropdown-toggle {
            text-decoration: none;
            color: var(--gray-900);
            font-size: 18px;
            font-weight: 600;
            padding: var(--space-md);
            border-radius: 8px;
            transition: background 0.2s;
            background: none;
            border: none;
            text-align: left;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .mobile-dropdown-toggle::after {
            content: '▼';
            font-size: 12px;
            transition: transform 0.2s;
        }

        .mobile-dropdown-toggle.active::after {
            transform: rotate(180deg);
        }

        .mobile-dropdown-toggle:hover {
            background: var(--gray-100);
        }

        .mobile-dropdown-menu {
            display: none;
            flex-direction: column;
            padding-left: var(--space-md);
            gap: 4px;
        }

        .mobile-dropdown-menu.active {
            display: flex;
        }

        .mobile-dropdown-menu a {
            text-decoration: none;
            color: var(--gray-700);
            font-size: 16px;
            font-weight: 500;
            padding: 10px var(--space-md);
            border-radius: 6px;
            transition: background 0.2s;
        }

        .mobile-dropdown-menu a:hover {
            background: var(--gray-100);
            color: var(--brand-red);
        }
"""

# Desktop navigation dropdown HTML
DESKTOP_DROPDOWN_HTML = """                <div class="nav-dropdown">
                    <a href="index.html#leistungen" class="nav-link nav-dropdown-toggle">
                        Leistungen
                        <svg class="dropdown-icon" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M2 4L6 8L10 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"
                                stroke-linejoin="round" />
                        </svg>
                    </a>
                    <div class="nav-dropdown-menu">
                        <a href="massivholzhaus.html">Massivholzhaus</a>
                        <a href="neubau.html">Neubau</a>
                        <a href="dachsanierung.html">Dachsanierung</a>
                        <a href="holzrahmenbau.html">Holzrahmenbau</a>
                        <a href="dachfenster.html">Dachfenster</a>
                        <a href="aufstockungen.html">Aufstockungen</a>
                        <a href="asbestsanierung.html">Asbestsanierung</a>
                        <a href="treppenbau.html">Treppenbau</a>
                        <a href="dachgauben.html">Dachgauben</a>
                    </div>
                </div>"""

# Mobile menu dropdown HTML
MOBILE_DROPDOWN_HTML = """        <div class="mobile-dropdown">
            <button class="mobile-dropdown-toggle" id="mobileDropdownToggle">Leistungen</button>
            <div class="mobile-dropdown-menu" id="mobileDropdownMenu">
                <a href="massivholzhaus.html" onclick="closeMenu()">Massivholzhaus</a>
                <a href="neubau.html" onclick="closeMenu()">Neubau</a>
                <a href="dachsanierung.html" onclick="closeMenu()">Dachsanierung</a>
                <a href="holzrahmenbau.html" onclick="closeMenu()">Holzrahmenbau</a>
                <a href="dachfenster.html" onclick="closeMenu()">Dachfenster</a>
                <a href="aufstockungen.html" onclick="closeMenu()">Aufstockungen</a>
                <a href="asbestsanierung.html" onclick="closeMenu()">Asbestsanierung</a>
                <a href="treppenbau.html" onclick="closeMenu()">Treppenbau</a>
                <a href="dachgauben.html" onclick="closeMenu()">Dachgauben</a>
            </div>
        </div>"""

# JavaScript for mobile dropdown
MOBILE_DROPDOWN_JS = """
        // Mobile dropdown toggle
        const mobileDropdownToggle = document.getElementById('mobileDropdownToggle');
        const mobileDropdownMenu = document.getElementById('mobileDropdownMenu');

        if (mobileDropdownToggle) {
            mobileDropdownToggle.addEventListener('click', function () {
                mobileDropdownToggle.classList.toggle('active');
                mobileDropdownMenu.classList.toggle('active');
            });
        }
"""


def add_css_dropdown(content: str) -> str:
    """Add dropdown CSS after .nav-cta:hover block."""
    # Find the .nav-cta:hover block and insert after it
    pattern = r'(\.nav-cta:hover\s*{[^}]+})'
    
    def replacement(match):
        return match.group(1) + "\n" + DROPDOWN_CSS
    
    # Only add if not already present
    if ".nav-dropdown {" not in content:
        content = re.sub(pattern, replacement, content, count=1)
    
    return content


def replace_desktop_nav(content: str) -> str:
    """Replace simple Leistungen link with dropdown in navigation."""
    # Pattern to match the current Leistungen link
    pattern = r'<a href="[^"]*#leistungen" class="nav-link">Leistungen</a>'
    
    # Only replace if dropdown not already present
    if '<div class="nav-dropdown">' not in content:
        content = re.sub(pattern, DESKTOP_DROPDOWN_HTML, content, count=1)
    
    return content


def replace_mobile_nav(content: str) -> str:
    """Replace simple Leistungen link with dropdown in mobile menu."""
    # Pattern to match the current mobile Leistungen link
    pattern = r'<a href="[^"]*#leistungen"[^>]*>Leistungen</a>'
    
    # Only replace if mobile dropdown not already present
    if '<div class="mobile-dropdown">' not in content:
        # Find the mobile menu section and replace
        content = re.sub(pattern, MOBILE_DROPDOWN_HTML, content, count=1)
    
    return content


def add_javascript(content: str) -> str:
    """Add JavaScript for mobile dropdown toggle."""
    # Find the closeMenu function and add dropdown logic before it
    pattern = r'(function closeMenu\(\) {)'
    
    def replacement(match):
        return MOBILE_DROPDOWN_JS + "\n        " + match.group(1)
    
    # Only add if not already present
    if "mobileDropdownToggle" not in content:
        content = re.sub(pattern, replacement, content, count=1)
        
        # Also update closeMenu function to handle dropdown
        old_close = r'(mobileMenu\.classList\.remove\(\'active\'\);)'
        new_close = r"""\1
            if (mobileDropdownToggle) {
                mobileDropdownToggle.classList.remove('active');
                mobileDropdownMenu.classList.remove('active');
            }"""
        content = re.sub(old_close, new_close, content, count=1)
    
    return content


def process_file(filepath: Path) -> bool:
    """Process a single HTML file to add dropdown functionality."""
    print(f"Processing {filepath.name}...")
    
    try:
        # Read file
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Apply transformations
        content = add_css_dropdown(content)
        content = replace_desktop_nav(content)
        content = replace_mobile_nav(content)
        content = add_javascript(content)
        
        # Write back if changed
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ {filepath.name} updated successfully")
            return True
        else:
            print(f"  ⊘ {filepath.name} already has dropdown")
            return False
            
    except Exception as e:
        print(f"  ✗ Error processing {filepath.name}: {e}")
        return False


def main():
    """Main function to process all files."""
    print("=" * 60)
    print("Adding Leistungen Dropdown to all subpages")
    print("=" * 60)
    print()
    
    updated_count = 0
    skipped_count = 0
    
    for filename in FILES_TO_MODIFY:
        filepath = BASE_DIR / filename
        
        if not filepath.exists():
            print(f"  ⚠ {filename} not found, skipping")
            continue
        
        if process_file(filepath):
            updated_count += 1
        else:
            skipped_count += 1
        print()
    
    print("=" * 60)
    print(f"Summary: {updated_count} files updated, {skipped_count} files skipped")
    print("=" * 60)


if __name__ == "__main__":
    main()
