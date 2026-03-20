---
trigger: always_on
---

# Aktionbutton - Farbregel für Zimmerei-Müller Webpage

- Wenn ein Aktion-Button erstellt werden soll, muss der Button immer die Hintergrundfarbe #D23526 haben
- Wenn ein Aktion-Button erstellt werden soll, muss die Schrift im Button immer die Schriftfarbe #FAE439 haben
- Wenn ein Aktion-Button erstellt werden soll, muss die Schrift mit einem halbtransparenten schwarzen Schatten-Effekt umrandet werden, der nur die Außenkontur betont:
  - CSS: text-shadow: -1px -1px 0 rgba(0,0,0,0.6), 1px -1px 0 rgba(0,0,0,0.6), -1px 1px 0 rgba(0,0,0,0.6), 1px 1px 0 rgba(0,0,0,0.6), 0 -1px 0 rgba(0,0,0,0.6), 0 1px 0 rgba(0,0,0,0.6), -1px 0 0 rgba(0,0,0,0.6), 1px 0 0 rgba(0,0,0,0.6)
- Die Schrift sollte fett sein (font-weight: bold) wie im Original-Logo
- NICHT text-stroke verwenden, da dies auch Innenflächen von Buchstaben ausfüllt