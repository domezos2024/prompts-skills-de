# UI State Matrix (STRICT)

Für jede relevante interaktive Komponente / jeden kritischen Flow.

| Zustand | Erwartung | Pass/Fail/N/A | Evidence |
|---------|-----------|---------------|----------|
| Idle | Ausgangszustand eindeutig | | |
| Hover | Interaktivität erkennbar (falls zutreffend) | | |
| Focus | Sichtbarer Tastaturfokus | | |
| Pressed | Reaktion auf Betätigung | | |
| Loading | Sichtbare Verarbeitung | | |
| Progress | Fortschritt, sofern bestimmbar | | |
| Success | Eindeutige Erfolgsbestätigung | | |
| Error | Verständliche Fehlermeldung + nächster Schritt | | |
| Warning | Erkennbare Warnung | | |
| Disabled | Klar unterscheidbar | | |
| Empty | Hilfreicher Leerzustand | | |
| Offline | Verständlicher Verbindungsstatus | | |
| Cancelled | Nachvollziehbare Abbruchbestätigung | | |

## Usability / A11y Kurzchecks

- [ ] Primäre Aktion auffindbar; Hierarchie klar
- [ ] Labels verständlich; keine unnötigen Klicks
- [ ] Abstände/Alignment konsistent; Navigation vorhersehbar
- [ ] Kontrast WCAG 2.2 AA (soweit anwendbar)
- [ ] Touch-Ziele / Tastatur / Screenreader-Labels
- [ ] Fehler nicht nur über Farbe; `prefers-reduced-motion` berücksichtigt
- [ ] Keine Fake-Success-Meldungen
- [ ] Destruktive Aktionen: Confirm oder Undo
