---
name: vollstaendige-ui-ux-transformation
description: Use when transforming an existing app UI/UX end-to-end, redesigning screens, fixing visual inconsistency, accessibility gaps, or needing before/after UI proof - runs a strict multi-phase audit, design-system build, implementation, and validated visual QA workflow.
---

# Vollständige UI/UX-Transformation

## Overview

Verwandelt eine vorhandene Anwendung in ein konsistentes, barrierearmes, professionelles Produkt. Kernprinzip: **Istzustand beweisen → Designsystem definieren → implementieren → Vorher/Nachher validieren.** Keine Cosmetik-ohne-Beweis.

## When to Use

- UI wirkt inkonsistent, veraltet oder unprofessionell
- Nutzerführung ist unklar; mobile/Desktop bricht
- Accessibility/Kontrast/Fokus fehlen
- Auftrag: „komplette UI/UX-Transformation“

## When NOT to Use

- Nur einzelnes Icon/Farbschema ohne UX-Audit → `visuelle-asset-fabrik` oder Designsystem-Skill
- Nur Conversion-Funnel-Optimierung → `conversion-orientiertes-oberflaechen-redesign`
- Rein backend/API-Arbeit ohne UI

## Critical Guidelines

- MUST Baseline mit realen Screenshots/Build vor Änderungen erfassen.
- MUST Design-Tokens und wiederverwendbare Komponenten vor Einzel-Screen-Tweaks etablieren.
- MUST Lade-, Fehler-, Leer- und Erfolgszustände für relevante Interaktionen abdecken.
- MUST Accessibility (Kontrast, Fokus, Semantik, Tastatur) mitprüfen.
- MUST Vorher/Nachher und Interaktionstests nach Implementierung ausführen.
- NEVER „sieht besser aus“ ohne Nachweis behaupten.
- NEVER neue UI-Libraries ohne klaren Mehrwert und Projektkonvention.
- NEVER bestehende Flows brechen; Regressionen sofort beheben.
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill vollstaendige-ui-ux-transformation --root .skill-runs/ui-ux
```

### PHASE 1 – DISCOVERY (Istzustand)

1. Projektstruktur, UI-Einstiege, Style-Systeme, Komponentenordner, Router/Navigation erfassen.
2. App starten (oder Storybook/Preview). Relevante Screens dokumentieren.
3. Screenshots der kritischen Flows speichern unter `artifacts/ui-baseline/`.
4. Audit nach `references/ui-ux-audit-checklist.md` (Layout, Typo, Farbe, Kontrast, Responsiveness, Interaction, A11y).
5. Befunde als P0–P3 listen; nur Verifiziertes.

**Gate:** Baseline-Artefakte + priorisierte Mängelliste existieren.

### PHASE 2 – PLANNING (Designrichtung)

1. Designprinzipien und visuelle Hierarchie festlegen (klar, schlicht, funktional).
2. Token-Plan: Farbe, Typo, Spacing, Radii, Elevation, Motion (sparsam).
3. Komponenten-Backlog: Buttons, Inputs, Nav, Dialoge, Feedback.
4. Atomare Implementierungspakete mit Akzeptanzkriterien und Rollback.

**Gate:** Plan mit messbaren Done-Kriterien pro Paket.

### PHASE 3 – IMPLEMENTATION

1. Tokens/Theme zuerst, dann Primitive, dann Screens.
2. Navigation, mobile Breakpoints, Loading/Error/Empty/Success nachziehen.
3. Icons/Assets nur wo nötig; konsistente Größen und Labels.
4. Nach jedem Paket: Smoke der betroffenen Screens.

**Gate:** Kritische Flows bedienbar; keine bekannten P0-UI-Bugs offen.

### PHASE 4 – VALIDATION

1. App erneut starten; Vorher/Nachher-Screenshots `artifacts/ui-after/`.
2. Interaktionen testen (Klick, Tastatur, Fehlerpfade).
3. Verfügbare UI-/A11y-Tests ausführen; Ergebnisse protokollieren.
4. Selbst verursachte Regressions fixen und re-testen.

**Gate:** Validierungsprotokoll ohne unbelegte Pass-Claims.

### PHASE 5 – DELIVERY

1. Delivery Report nach `_shared/references/delivery-report-template.md`.
2. Auditbericht priorisiert; Restlücken benennen.
3. Checkpoint auf `done` setzen.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/ui-ux --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Baseline | Start + Screenshots + Checklist |
| System | Tokens → Primitives → Screens |
| Zustände | Idle/Hover/Focus/Loading/Error/Empty/Success |
| Beweis | Before/After + Tests |
| Stop | Kein Nachweis → nicht als fertig melden |

## Red Flags

- Redesign ohne Baseline-Screenshots
- Neue Farben pro Screen statt Tokens
- „A11y ok“ ohne Prüfung
- Nur Desktop getestet
- Fertigmeldung ohne PHASE 4

## Resources

- `references/ui-ux-audit-checklist.md`
- `scripts/capture_baseline_notes.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
