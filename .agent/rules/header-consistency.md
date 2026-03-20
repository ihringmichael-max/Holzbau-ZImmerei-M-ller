---
trigger: always_on
---

# Header-Konsistenz-Regeln

- Alle Seiten (Frontpage, Unterseiten, Leistungsseiten) müssen einen identischen Header haben
- Der Header der Frontpage (`zimmerei-mueller-frontpage.html`) ist die Vorlage
- Header-Elemente müssen exakt gleich sein:
  - Navigation-Container (`.nav`, `.nav-container`)
  - Logo (`.nav-logo`, `.nav-logo-img`)
    - Größe: `height: 54px`
    - Border-radius: `4px`
    - Gap: `var(--space-sm)`
    - Hover-Effekt mit transform und drop-shadow
  - Navigation-Links (`.nav-links`, `.nav-link`)
  - CTA-Button (`.nav-cta`)
    - Farben: Background `#D23526`, Text `#FAE439`
    - Text-shadow für schwarze Kontur
  - Mobile-Menu (`.nav-hamburger`, `.mobile-menu`)
- Bei Änderungen am Header: ALLE Seiten müssen gleichzeitig angepasst werden
- Keine Abweichungen in Größen, Abstände, Farben oder Positionierung erlaubt
s