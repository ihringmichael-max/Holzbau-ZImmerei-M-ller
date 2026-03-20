# Footer-Konsistenz-Regeln

- Alle Seiten (Frontpage, Unterseiten, Leistungsseiten, rechtliche Seiten) müssen einen identischen Footer haben
- Der Footer der Frontpage (`zimmerei-mueller-frontpage.html`) ist die Vorlage
- Footer-Elemente müssen exakt gleich sein:
  - Container (`.footer`, `.footer-container`)
    - Padding: `var(--space-xl) var(--space-lg)`
    - **Background: `#D23526`** (Rot aus Firmenfarben)
    - **Color: `#FAE439`** (Gelb aus Firmenfarben)
  - Container-Layout (`.footer-container`)
    - Max-width: `1200px`
    - Display: `flex`
    - Justify-content: `space-between`
    - Align-items: `center`
  - Footer-Left (`.footer-left`)
    - Font-size: `14px`
    - Color: `#FAE439`
  - Footer-Links (`.footer-links`, `.footer-link`)
    - Display: `flex`
    - Gap: `var(--space-lg)`
    - Font-size: `14px`
    - Color: `#FAE439`
    - Font-weight: `500`
    - Hover: `color: #FFFFFF`, `text-decoration: underline`
  - Responsive-Verhalten
    - @media (max-width: 768px): Column-Layout mit Center-Alignment
- Alle Footer müssen die drei Links haben: Impressum, Datenschutz, AGB
- Bei Änderungen am Footer: ALLE Seiten müssen gleichzeitig angepasst werden
- Keine Abweichungen in Farben, Größen oder Layout erlaubt

