#!/usr/bin/env python3
"""
Minimalistische Kopie der Dropdown-Implementierung von neubau.html zu allen anderen Seiten.
"""
import re
from pathlib import Path

# Verzeichnis
BASE = Path("/Users/michael-ihring/Documents/Zimmrei-Müller/Webpage/Antigravity")

# Seiten die bearbeitet werden müssen (ohne neubau.html, ueber-uns.html, index.html)
FILES = [
    "holzrahmenbau.html",
    "dachsanierung.html",
    "dachfenster.html",
    "treppenbau.html",
    "asbestsanierung.html",
    "aufstockungen.html",
    "dachgauben.html",
    "massivholzhaus.html",
    "referenzen. html",
    "impressum.html",
    "datenschutz.html",
]

# Lese neubau.html als Template
with open(BASE / "neubau.html", "r", encoding="utf-8") as f:
    template = f.read()

# Extrahiere die Dropdown-CSS (von "/* ===================== DROPDOWN MENU ===================== */" bis vor "/* ===================== DETAIL PAGE LAYOUT ===================== */")
css_start = template.find("/* ===================== DROPDOWN MENU ===================== */")
css_end = template.find("/* ===================== DETAIL PAGE LAYOUT ===================== */", css_start)
dropdown_css = template[css_start:css_end]

# Extrahiere Desktop Nav Dropdown
desktop_nav_start = template.find('<div class="nav-dropdown">')
desktop_nav_end = template.find('</div>', desktop_nav_start) + len('</div>')
desktop_dropdown = template[desktop_nav_start:desktop_nav_end]

# Extrahiere Mobile Dropdown
mobile_start = template.find('<div class="mobile-dropdown">')
mobile_end = template.find('</div>', template.find('</div>', template.find('</div>', mobile_start) + 1) + 1) + len('</div>')
mobile_dropdown = template[mobile_start:mobile_end]

print(f"CSS Block: {len(dropdown_css)} chars")
print(f"Desktop Nav: {len(desktop_dropdown)} chars")
print(f"Mobile Nav: {len(mobile_dropdown)} chars")
print()

# Bearbeite jede Datei
for filename in FILES:
    filepath = BASE / filename
    if not filepath.exists():
        print(f"⚠ {filename} nicht gefunden")
        continue
    
    print(f"Bearbeite {filename}...")
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Prüfe ob schon vorhanden
    if ".nav-dropdown {" in content:
        print(f"  ⊘ Hat bereits Dropdown, überspringe")
        continue
    
    # 1. CSS hinzufügen (nach .nav-cta:hover)
    nav_cta_hover_match = re.search(r'(\.nav-cta:hover\s*{[^}]+})', content)
    if nav_cta_hover_match:
        insert_pos = nav_cta_hover_match.end()
        content = content[:insert_pos] + "\n\n" + dropdown_css + content[insert_pos:]
        print("  ✓ CSS hinzugefügt")
    
    # 2. Desktop Nav ersetzen
    desktop_link_pattern = r'<a href="[^"]*#leistungen"[^>]*class="nav-link"[^>]*>Leistungen</a>'
    if re.search(desktop_link_pattern, content):
        content = re.sub(desktop_link_pattern, desktop_dropdown, content, count=1)
        print("  ✓ Desktop Nav ersetzt")
    
    # 3. Mobile Nav ersetzen
    mobile_link_pattern = r'<a href="[^"]*#leistungen"[^>]*onclick="closeMenu\(\)"[^>]*>Leistungen</a>'
    if re.search(mobile_link_pattern, content):
        content = re.sub(mobile_link_pattern, mobile_dropdown, content, count=1)
        print("  ✓ Mobile Nav ersetzt")
    
    # 4. JavaScript aktualisieren
    # Finde const hamburger Zeile und füge Dropdown Variablen hinzu
    hamburger_pattern = r'(const hamburger = document\.getElementById\(.*?\);\s*const mobileMenu = document\.getElementById\(.*?\);)'
    if re.search(hamburger_pattern, content):
        replacement = r"\1\n        const mobileDropdownToggle = document.getElementById('mobileDropdownToggle');\n        const mobileDropdownMenu = document.getElementById('mobileDropdownMenu');"
        content = re.sub(hamburger_pattern, replacement, content, count=1)
        
        # Füge Dropdown-Listener hinzu (nach hamburger.addEventListener)
        listener_pattern = r'(hamburger\.addEventListener\([^}]+}\);)'
        listener_replacement = r"""\1

        // Mobile dropdown toggle
        if (mobileDropdownToggle) {
            mobileDropdownToggle.addEventListener('click', function () {
                mobileDropdownToggle.classList.toggle('active');
                mobileDropdownMenu.classList.toggle('active');
            });
        }"""
        content = re.sub(listener_pattern, listener_replacement, content, count=1)
        
        # Aktualisiere closeMenu Funktion
        close_menu_pattern = r'(function closeMenu\(\) {\s*hamburger\.classList\.remove\(.*?\);\s*mobileMenu\.classList\.remove\(.*?\);)'
        close_menu_replacement = r"""\1
            if (mobileDropdownToggle) {
                mobileDropdownToggle.classList.remove('active');
                mobileDropdownMenu.classList.remove('active');
            }"""
        content = re.sub(close_menu_pattern, close_menu_replacement, content, count=1)
        
        print("  ✓ JavaScript aktualisiert")
    
    # Schreibe zurück
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"  ✅ {filename} fertig!\n")

print("=" * 60)
print("FERTIG! Alle Seiten wurden aktualisiert.")
print("="*60)
