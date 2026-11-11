---
name: mobile-first-erlebnisoptimierer
description: Use when optimizing an app for phones and tablets - fixing overflow, touch targets, mobile navigation, responsive typography/images, and validating core flows across viewports without zoom or clipped controls.
---

# Mobile-First-Erlebnisoptimierer

## Overview

Optimiert die Anwendung konsequent für Smartphones, Tablets und wechselnde Bildschirmgrößen. Kernprinzip: **Viewport-Fehler beweisen → Navigation/Touch/Formulare sanieren → responsive Medien & A11y → Matrix validieren.** Kein „responsive“-Claim ohne Testmatrix.

## When to Use

- Mobile Layouts brechen, Overflow, abgeschnittene Buttons
- Touch-Ziele zu klein; Navigation auf schmalen Viewports unbrauchbar
- Formulare/Keyboard auf Mobile problematisch
- Auftrag: „Mobile-First / Responsive UX“

## When NOT to Use

- Vollständiges Designsystem aufbauen → `automatischer-designsystem-architekt`
- Nur Conversion-Landingpage → `conversion-orientiertes-oberflaechen-redesign`
- Rein visuelle Asset-Produktion → `visuelle-asset-fabrik`
- Kein UI vorhanden (reine API/Backend-Arbeit)

## Critical Guidelines

- MUST repräsentative Viewport-Größen testen und Layoutfehler mit Screenshots belegen.
- MUST Touch-Ziele, Abstände, mobile Navigation und Formulare priorisieren.
- MUST responsive Bilder, typografische Skalierung sowie Lade-/Fehlerzustände absichern.
- MUST Tastaturbedienung, Screenreader-Semantik und Touch-Zielgröße prüfen.
- MUST Hoch- und Querformat sowie typische Gerätebreiten in der Matrix abdecken.
- MUST Überläufe, verdeckte Buttons und unzugängliche Controls beheben.
- NEVER Desktop-only als „fertig mobil“ deklarieren.
- NEVER Zoomzwang oder horizontales Scrollen als akzeptabel belassen.
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill mobile-first-erlebnisoptimierer --root .skill-runs/mobile-first
```

### PHASE 1 – DISCOVERY

1. Ansichten, Navigation, Inputs, Scrollverhalten und Touch-Ziele analysieren.
2. Viewports aus `references/viewport-test-matrix.md` durchspielen; Fehler dokumentieren.
3. Baseline-Screenshots unter `artifacts/mobile-baseline/` ablegen.
4. P0–P3-Befunde nur mit Beweis (Screenshot/Pfad).

**Gate:** Baseline + priorisierte Mängelliste + begonnene Testmatrix.

### PHASE 2 – PLANNING

1. Mobile-Nav-Konzept (Bottom-Nav, Drawer, Collapse) und Breakpoint-Strategie festlegen.
2. Pakete: Overflow-Fixes → Touch/Spacing → Forms → Media/Typo → A11y.
3. Akzeptanz: Kernflows ohne Zoom/Clipping auf definierten Viewports.

**Gate:** Plan mit messbaren Done-Kriterien pro Paket.

### PHASE 3 – IMPLEMENTATION

1. Navigation, Abstände, Touch-Interaktionen und Formulare überarbeiten.
2. Responsive Images, fluid Typography, Loading/Error/Empty nachziehen.
3. Verdeckte Controls und Overflows beseitigen; Safe-Area/Notch beachten wo relevant.
4. Nach jedem Paket: Smoke auf engstem Ziel-Viewport.

**Gate:** Kernflows mobil bedienbar; keine offenen P0-Layout-Bugs.

### PHASE 4 – VALIDATION

1. Vollständige Viewport-Matrix inkl. Portrait/Landscape abarbeiten.
2. After-Screenshots `artifacts/mobile-after/`; Interaktionen und Tastatur testen.
3. A11y-Stichprobe: Fokus, Labels, Target-Größe.
4. Regressionen fixen und Matrix aktualisieren.

**Gate:** Matrix ohne unbelegte Pass-Claims; Erfolgskriterium erfüllt.

### PHASE 5 – DELIVERY

1. Delivery Report nach `_shared/references/delivery-report-template.md`.
2. Testmatrix, Restlücken und Geräte-Annahmen dokumentieren.
3. Checkpoint auf `done` setzen.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/mobile-first --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Baseline | Viewports + Screenshots + Overflow-Liste |
| Fix-Reihenfolge | Nav → Touch/Spacing → Forms → Media → A11y |
| Beweis | Matrix Pass/Fail + Before/After |
| Erfolg | Kernflows ohne Zoom/Clipping |
| Stop | Nur Desktop getestet → nicht delivern |

## Red Flags

- „Mobile ok“ ohne Matrix
- Touch-Targets geschätzt, nicht geprüft
- Querformat ignoriert
- Fixed-Width-Layouts unverändert
- Fertigmeldung ohne PHASE 4

## Resources

- `references/viewport-test-matrix.md`
- `scripts/scaffold_viewport_matrix.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
