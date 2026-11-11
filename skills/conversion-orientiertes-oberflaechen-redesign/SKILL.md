---
name: conversion-orientiertes-oberflaechen-redesign
description: Use when improving landing, signup, download, or checkout surfaces for clarity and conversion - auditing friction, redesigning hierarchy/CTAs, implementing responsive changes, and defining honest metrics without dark patterns or invented lift claims.
---

# Conversion-orientiertes Oberflächen-Redesign

## Overview

Verbessert Verständlichkeit und Wirksamkeit von Landingpages, Registrierung, Download- oder Kaufstrecken. Kernprinzip: **Ziel & Hürden beweisen → Hierarchie/CTA schärfen → implementieren → Flows prüfen → ehrlichen Messplan liefern.** Keine Dark Patterns, keine erfundenen Uplifts.

## When to Use

- Landing/Signup/Checkout/Download konvertiert schlecht oder wirkt unklar
- CTAs, Headlines oder Vertrauenselemente sind schwach/widersprüchlich
- Formular-Friction (Validierung, Fehler, Schritte) blockiert Abschlüsse

## When NOT to Use

- Ganzes App-UI-System → `vollstaendige-ui-ux-transformation` / `automatischer-designsystem-architekt`
- Nur Mobile-Breakpoints ohne Conversion-Fokus → `mobile-first-erlebnisoptimierer`
- Nur Asset-Produktion → `visuelle-asset-fabrik`
- Rein backend Pricing/A-B-Infra ohne UI-Auftrag

## Critical Guidelines

- MUST Zielgruppe, Seitenzweck und primäre Aktion vor Redesign klar festhalten.
- MUST Ist-Funnel und Hürden dokumentieren (Screenshots/Notizen).
- MUST Headlines, CTAs, Informationshierarchie und Trust-Elemente prüfen und verbessern.
- MUST responsive Umsetzung und vollständige Nutzerabläufe inkl. Formularfehler testen.
- MUST messbare Erfolgsmetriken und ggf. datenschutzkonformen A/B-Ansatz definieren.
- NEVER Dark Patterns (Irreführung, erzwungene Opt-ins, Fake-Knappheit, versteckte Kosten).
- NEVER Conversion-Steigerungen oder Testergebnisse erfinden.
- NEVER „fertig“ ohne Vorher/Nachher und Messplan.
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill conversion-orientiertes-oberflaechen-redesign --root .skill-runs/conversion-ui
```

### PHASE 1 – DISCOVERY

1. Zielgruppe, Job-to-be-done, Primär-CTA und Sekundärziele erfassen.
2. Ist-Führung und Hürden nach `references/conversion-friction-checklist.md` dokumentieren.
3. Baseline-Screenshots `artifacts/conversion-baseline/`.

**Gate:** Funnel-Ist + Hürdenliste + Baseline existieren.

### PHASE 2 – PLANNING

1. Neue Seitenstruktur mit klarer visueller Priorisierung entwerfen.
2. Copy-/CTA-Hypothesen formulieren (was sich warum ändern soll).
3. Implementierungspakete + Metrikdefinition (z. B. CTA-Click, Complete-Rate) ohne Fake-Zahlen.
4. A/B nur wenn Instrumentierung/DSGVO-Rahmen realistisch.

**Gate:** Strukturplan + Hypothesen + Messplan-Skizze.

### PHASE 3 – IMPLEMENTATION

1. Redesign umsetzen (Hierarchie, CTA, Trust, Spacing, responsive).
2. Formulare: Labels, Validierung, Fehlermeldungen, Erfolgspfad.
3. Tracking-Hooks nur wenn vorhanden/erlaubt; sonst Messplan als manuell/analytisch markieren.

**Gate:** Zielseite bedienbar; Kernflow ohne Blocker.

### PHASE 4 – VALIDATION

1. Komplette Nutzerabläufe inkl. Fehlerpfade testen.
2. Vorher/Nachher `artifacts/conversion-after/`.
3. Friction-Checkliste erneut; Dark-Pattern-Review.
4. Metriken/A-B-Plan finalisieren — ohne erfundene Results.

**Gate:** Validierung + ehrlicher Messplan; keine unbelegten Lift-Claims.

### PHASE 5 – DELIVERY

1. Delivery Report nach `_shared/references/delivery-report-template.md`.
2. Vorher/Nachher, Hypothesen, Messplan, offene Risiken.
3. Checkpoint auf `done` setzen.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/conversion-ui --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Ist | Zweck, CTA, Hürden, Baseline |
| Soll | Hierarchie, Copy, Trust, Form-UX |
| Beweis | Before/After + Flow-Test |
| Messung | Metriken planen, keine Fake-Lifts |
| Stop | Dark Pattern oder erfundene Zahlen → ablehnen |

## Red Flags

- Mehr CTAs ohne Primärfokus
- Trust-Logos ohne Substanz/Rechte
- Formular „optimiert“ ohne Fehlertest
- „+40% Conversion“ ohne Daten
- Fertig ohne Messplan

## Resources

- `references/conversion-friction-checklist.md`
- `scripts/scaffold_conversion_notes.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
