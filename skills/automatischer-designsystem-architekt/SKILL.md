---
name: automatischer-designsystem-architekt
description: Use when extracting or building a scalable design system from an existing app - inventoring tokens/components, removing visual duplicates, migrating screens to a shared library, and validating states without visual regressions.
---

# Automatischer Designsystem-Architekt

## Overview

Extrahiert aus dem Ist-Projekt ein einheitliches, skalierbares Designsystem und integriert es vollständig. Kernprinzip: **Inventar beweisen → Tokens & Primitives definieren → Bibliothek bauen → Screens migrieren → Zustände validieren.** Kein Token-Katalog ohne Migrationsnachweis.

## When to Use

- Farben, Typo, Abstände und Komponenten sind inkonsistent oder dupliziert
- Neue Screens brauchen wiederverwendbare Bausteine statt Copy-Paste-Styles
- Light/Dark oder themingfähige Tokens fehlen
- Auftrag: „Designsystem aufbauen / vereinheitlichen“

## When NOT to Use

- Komplette UX-Neugestaltung inkl. Flows → `vollstaendige-ui-ux-transformation`
- Nur mobile Breakpoints/Touch → `mobile-first-erlebnisoptimierer`
- Nur fehlende Icons/Illustrationen → `visuelle-asset-fabrik`
- Rein Conversion-Funnel ohne Systemarbeit → `conversion-orientiertes-oberflaechen-redesign`

## Critical Guidelines

- MUST vor Token-Definition ein vollständiges Inventar (Fonts, Farben, Spacing, Komponenten, Icons) erfassen.
- MUST Duplikate und Inkonsistenzen mit Dateipfaden belegen, nicht schätzen.
- MUST Tokens für Farbe, Typografie, Abstand, Radius, Schatten und Zustände vor Screen-Migration etablieren.
- MUST Komponentenbibliothek mit dokumentierten Varianten (inkl. Hover/Focus/Disabled/Loading/Error) liefern.
- MUST bestehende Oberflächen migrieren ohne Funktionsverlust.
- MUST Komponentenübersicht mit visuellen Beispielen und Zustandsmatrix prüfen.
- NEVER neue UI-Libraries ohne klaren Mehrwert und Projektkonvention einführen.
- NEVER Hardcoded-Werte neben Tokens belassen, wenn Migration des Screens als „done“ gilt.
- NEVER ungenutzte Doppelimplementierungen als „Legacy ok“ stehen lassen ohne dokumentierte Ausnahme.
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill automatischer-designsystem-architekt --root .skill-runs/design-system
```

### PHASE 1 – DISCOVERY (Inventar)

1. Style-Quellen finden: CSS/SCSS, CSS-Variables, Theme-Dateien, Tailwind-Config, styled-components, Design-Tokens.
2. Komponentenordner, Storybook/Preview, Icon-Sets und Formularprimitive inventarisieren.
3. Inkonsistenzen und Duplikate nach `references/design-token-migration-matrix.md` erfassen.
4. Ist-Farben/Typo/Spacing als Rohliste unter `artifacts/ds-inventory/` speichern.

**Gate:** Inventarliste + priorisierte Duplikat-/Inkonsistenzliste existieren.

### PHASE 2 – PLANNING (Token- & Bibliotheksplan)

1. Token-Taxonomie festlegen: color, typography, space, radius, elevation, motion, state.
2. Primitive-Backlog: Button, Input, Select, Checkbox, Radio, Link, Badge, Card, Dialog, Toast, Nav.
3. Migrationspakete: Tokens → Primitives → zusammengesetzte Komponenten → Screens (atomar, mit Rollback).
4. Optional: Light/Dark und Breakpoint-Regeln nur wenn Projektbedarf nachgewiesen.

**Gate:** Plan mit messbaren Done-Kriterien und Migrationsreihenfolge.

### PHASE 3 – IMPLEMENTATION

1. Tokens/Theme zuerst implementieren; alte Hardcodes schrittweise ersetzen.
2. Komponentenbibliothek mit Varianten und Props-Dokumentation aufbauen.
3. Screens paketweise migrieren; Funktionen und Flows erhalten.
4. Nach jedem Paket: Smoke der betroffenen Views + Doppelimplementierungen entfernen.

**Gate:** Kritische Screens nutzen Tokens/Primitives; keine offenen P0-Doppelstyles.

### PHASE 4 – VALIDATION

1. Komponentenübersicht/Storybook oder Demo-Seite aller Varianten prüfen.
2. Zustandsmatrix (Idle/Hover/Focus/Disabled/Loading/Error/Success) abhaken.
3. Visuelle Regression: Vorher/Nachher unter `artifacts/ds-before/` und `artifacts/ds-after/`.
4. Selbst verursachte Brüche sofort fixen und re-testen.

**Gate:** Validierungsprotokoll ohne unbelegte Pass-Claims; QUALITÄTSGATE erfüllt.

### PHASE 5 – DELIVERY

1. Delivery Report nach `_shared/references/delivery-report-template.md`.
2. Token-Dokumentation, Komponentenliste, Restlücken und bewusste Ausnahmen nennen.
3. Checkpoint auf `done` setzen.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/design-system --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Inventar | Styles + Komponenten + Duplikate listen |
| System | Tokens → Primitives → Compounds → Screens |
| Zustände | Idle/Hover/Focus/Disabled/Loading/Error |
| Migration | Paketweise, Funktion erhalten, Hardcodes tilgen |
| Stop | Keine Zustandsprüfung → nicht als fertig melden |

## Red Flags

- Tokens ohne Inventar „aus dem Bauch“ erfunden
- Komponentenbibliothek ohne Varianten/Dokumentation
- Screens „migriert“, aber lokale Hex-Werte bleiben
- Dark Mode angekündigt ohne Theme-Schicht
- Fertigmeldung ohne Komponentenübersicht/Zustandscheck

## Resources

- `references/design-token-migration-matrix.md`
- `scripts/inventory_style_sources.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
