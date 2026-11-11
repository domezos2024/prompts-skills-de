# Design-Token- & Migrationsmatrix

Jedes Item: `Pass` | `Fail` | `N/A` + Beweis (Datei/Zeile/Screenshot). Übertrifft reines Inventar: erzwingt Quellen→Token→Konsument-Nachweis.

## A. Inventar (Quellen)

| Kategorie | Gefundene Quellen (Pfad) | Varianten / Werte | Duplikate? | Schwere |
|-----------|--------------------------|-------------------|------------|---------|
| Farben | | | Ja/Nein | P0–P3 |
| Typografie | | | | |
| Spacing | | | | |
| Radii | | | | |
| Schatten/Elevation | | | | |
| Motion | | | | |
| Icons | | | | |
| Buttons | | | | |
| Formulare | | | | |
| Navigation | | | | |
| Feedback (Toast/Alert) | | | | |

## B. Token-Definition (Soll)

- [ ] Farbtokens semantisch (bg/fg/border/accent/danger/success/warning/info), nicht nur Palette
- [ ] Typo-Tokens: family, size-scale, weight, line-height, letter-spacing
- [ ] Spacing-Skala dokumentiert (z. B. 4er-Raster) und in Code verdrahtet
- [ ] Radius- und Elevation-Tokens vorhanden
- [ ] State-Tokens oder klare State-Varianten (hover/focus/disabled/error)
- [ ] Light/Dark nur wenn Theme-Schicht existiert und Screens angebunden sind

## C. Komponentenbibliothek

| Komponente | Varianten | States geprüft | Docs/Story | Migrierte Konsumenten | Doppel-Impl entfernt |
|------------|-----------|----------------|------------|----------------------|----------------------|
| Button | | | | | |
| Input | | | | | |
| Select | | | | | |
| Dialog | | | | | |
| Nav | | | | | |
| … | | | | | |

## D. Screen-Migration

- [ ] Jeder kritische Screen referenziert Tokens/Primitives statt lokaler Magic Values
- [ ] Keine unbeabsichtigte visuelle Regression (Before/After belegt)
- [ ] Funktionen unverändert (Smoke der Kernflows)
- [ ] Ungenutzte Style-Duplikate gelöscht oder als Ausnahme begründet

## E. QUALITÄTSGATE

- [ ] Keine unbeabsichtigten visuellen Regressionen
- [ ] Keine ungenutzten Doppelimplementierungen offen ohne Ausnahme
- [ ] Keine fehlerhaften Komponenten in der Übersicht
