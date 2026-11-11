# Asset-Produktions- & Rechte-Checkliste

Jedes Asset: Status `Need` | `Replace` | `Keep` | `N/A` + Beweis. Übertrifft Prompt: erzwingt Rechte, Exportmatrix und In-App-Verifikation.

## A. Inventar & Priorität

| ID | Typ | Kontext/Screen | Status | Prio | Ist-Pfad | Soll-Pfad | Lizenz/Quelle |
|----|-----|----------------|--------|------|----------|-----------|---------------|
| A1 | Icon | | | P0–P3 | | | |
| A2 | Logo | | | | | | |
| A3 | Illustration | | | | | | |
| A4 | Empty State | | | | | | |
| A5 | Preview/OG | | | | | | |
| A6 | Background | | | | | | |
| A7 | Store Art | | | | | | |

## B. Gestaltungsregeln (vor Produktion)

- [ ] Stil (Outline/Filled/Duotone/Illustration) festgelegt
- [ ] Strichstärke / Corner-Radius / Grid (z. B. 24px) dokumentiert
- [ ] Farbbindung an Brand/Tokens (keine wilden Hex pro Asset ohne System)
- [ ] Padding in ViewBox / Safe-Zone definiert
- [ ] Light/Dark-Varianten-Bedarf entschieden

## C. Exportmatrix (pro geliefertem Asset)

| ID | SVG | PNG 1x | PNG 2x | WebP | Sonstige Größen | Optimiert | Transparenz ok |
|----|-----|--------|--------|------|-----------------|-----------|----------------|
| | | | | | | Ja/Nein | Ja/Nein |

## D. Qualität

- [ ] Scharf auf Ziel-DPI; keine sichtbare Kompressionsartefakte an kritischen Kanten
- [ ] Dateigröße vertretbar relativ zum Nutzen
- [ ] Kontrast auf typischen Hintergründen ausreichend
- [ ] Naming-Konvention eingehalten
- [ ] Keine toten Imports/Referenzen

## E. Rechte & Integrität

- [ ] Quelle/Lizenz pro Asset dokumentiert
- [ ] Keine vorgetäuschten Dateien / leeren Placeholder als final
- [ ] Keep-Assets nur mit Begründung ersetzt
- [ ] Generierte Assets auf Marken-/Lizenzkonflikte stichprobenartig geprüft

## F. In-App-Verifikation

- [ ] Jedes P0/P1-Asset in laufender UI gesehen (Screenshot-Pfad)
- [ ] Broken-Image-Zustände nicht vorhanden
- [ ] Dark Mode / kontrastierende Surfaces geprüft wo relevant
