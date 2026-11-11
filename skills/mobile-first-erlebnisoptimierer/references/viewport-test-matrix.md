# Viewport- & Touch-Testmatrix

Jedes Zelle: `Pass` | `Fail` | `N/A` + Screenshot-Pfad. Übertrifft Prompt: erzwingt Geräte × Flow × Interaktion × A11y.

## Pflicht-Viewports

| ID | Breite×Höhe | Orientierung | Typ |
|----|-------------|--------------|-----|
| V1 | 360×640 | Portrait | Klein-Phone |
| V2 | 390×844 | Portrait | Modern Phone |
| V3 | 428×926 | Portrait | Large Phone |
| V4 | 768×1024 | Portrait | Tablet |
| V5 | 360×640 | Landscape | Phone quer |
| V6 | 1024×768 | Landscape | Tablet quer |

## Kernflows × Viewport

| Flow | V1 | V2 | V3 | V4 | V5 | V6 | Notes/Evidence |
|------|----|----|----|----|----|----|----------------|
| Einstieg / Home | | | | | | | |
| Primäre Navigation | | | | | | | |
| Formular absenden | | | | | | | |
| Kritischer Detail-/Listenflow | | | | | | | |
| Fehlerzustand anzeigen | | | | | | | |

## Layout & Overflow

- [ ] Kein horizontaler Overflow auf V1–V4
- [ ] Keine abgeschnittenen CTAs/Buttons
- [ ] Sticky-Header/Footer verdecken keinen Inhalt dauerhaft
- [ ] Modals/Sheets auf schmalen Viewports vollständig bedienbar
- [ ] Safe-Area / Notch / Home-Indicator berücksichtigt (falls native/PWA)

## Touch & Interaktion

- [ ] Touch-Targets ≥ 44×44 CSS-px (oder nachweisbare Ausnahme)
- [ ] Ausreichend Abstand zwischen konkurrierenden Targets
- [ ] Scroll-Container ohne „scroll trap“ neben Parent-Scroll
- [ ] Swipe/Gesture-Alternativen haben sichtbare Controls

## Formulare & Tastatur

- [ ] Korrekte `inputmode`/Typen wo sinnvoll
- [ ] Fokus scrollt Feld sichtbar in den Viewport
- [ ] Fehlermeldungen lesbar ohne Zoom
- [ ] Submit erreichbar wenn Soft-Keyboard offen (Stichprobe)

## Medien & Typografie

- [ ] Bilder skalieren ohne Layoutbruch; keine riesigen unkomprimierten Mobile-Payloads unkritisch gelassen
- [ ] Typo lesbar ohne Pinch-Zoom für Body-Text
- [ ] Loading/Error/Empty auf Mobile vorhanden

## Accessibility (Mobile)

- [ ] Fokus sichtbar bei Tastatur/Switch-Steuerung
- [ ] Semantik/Labels für Icon-Buttons
- [ ] Information nicht nur über Farbe
- [ ] Screenreader-Stichprobe kritischer Controls

## Erfolgsgate

- [ ] Alle wesentlichen Kernabläufe mobil ohne Zoomzwang nutzbar
- [ ] Keine abgeschnittenen Bedienelemente auf Pflicht-Viewports
