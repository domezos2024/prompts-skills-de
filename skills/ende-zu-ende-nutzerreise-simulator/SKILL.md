---
name: ende-zu-ende-nutzerreise-simulator
description: Use when simulating real user journeys end-to-end, automating browser flows with checkpoints/screenshots, covering roles and viewports, and fixing journey-breaking defects with isolated test data - runs a strict multi-phase journey map, automation, failure-path validation, and evidence workflow.
---

# Ende-zu-Ende-Nutzerreise-Simulator

## Overview

Simuliert reale Benutzer vom Einstieg bis zum Ergebnis. Kernprinzip: **Top-Journeys definieren → automatisieren inkl. Fehlerpfade → Rollen/Viewports → Evidence an Checkpoints → Ursachen im Code beheben.** Schreibende Tests nur mit isolierten Testdaten.

## When to Use

- Kritische User Journeys brauchen reproduzierbare E2E-Nachweise
- Flaky manuelle Abnahmen ersetzen
- Multi-Viewport/Rollen-Verhalten prüfen

## When NOT to Use

- Nur Unit-/API-QA ohne Journey → `autonomer-qa-testingenieur`
- Nur Kompatibilitätsmatrix → `waechter-fuer-regression-und-kompatibilitaet`
- Produktiv Käufe/Nachrichten/Payments auslösen

## Critical Guidelines

- MUST 5–10 wichtigste Nutzerreisen priorisieren.
- MUST erwartete Ergebnisse, Testdaten und Fehlerszenarien je Journey definieren.
- MUST Interaktionen automatisieren (Klick, Input, Navigation, Submit).
- MUST Loading, ungültige Eingaben, Unterbrechungen, Wiederholungen prüfen.
- MUST isolierte Testdaten; keine echten Prod-Side-Effects.
- NEVER echte Käufe, Mails an echte Nutzer, Live-Zahlungen.
- NEVER Pass ohne Screenshot/Trace an Kontrollpunkten.
- NEVER selektoren-fragile Suites ohne Stabilisierungsstrategie als fertig melden.
- ALWAYS Iron Laws und Phasenstatus.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill ende-zu-ende-nutzerreise-simulator --root .skill-runs/e2e-journeys
```

### PHASE 1 – DISCOVERY

1. Top-Journeys aus Produktzielen/Analytics/Nav ableiten.
2. Rollen und abhängige Backend-Voraussetzungen erfassen.
3. Vorhandene E2E-Frameworks (Playwright/Cypress/…) nutzen, nicht parallel erfinden.
4. Journey-Matrix `references/journey-test-matrix.md` skizzieren.

**Gate:** Journey-Liste + Datastrategie (isoliert) existieren.

### PHASE 2 – PLANNING

1. Pro Journey: Steps, Assertions, Negative Branches, Viewports.
2. Checkpoint-Screenshots-Plan (Entry, kritische Form, Success).
3. Stabilität: waits auf UI-State, nicht fixed sleep-only.
4. Atomare Fix-Pakete für Journey-Breaks.

**Gate:** Spezifizierte Cases mit Done-Kriterien.

### PHASE 3 – AUTOMATION & FIX

1. Suites implementieren; Seeds/Fixtures für Testdaten.
2. Happy + Validation + Interrupt/Retry-Pfade.
3. Fehler analysieren; Ursachen im Projektcode beheben.
4. Nach Fix: betroffene Journey sofort re-laufen.

**Gate:** P0-Journeys automatisiert und lokal/CI-ausführbar.

### PHASE 4 – VALIDATION

1. Journeys über relevante Rollen/Viewports laufen lassen.
2. Evidence unter `artifacts/e2e/` ablegen.
3. Flakes isolieren; nicht als grün melden.
4. Restlücken dokumentieren.

**Gate:** Protokoll mit Pass/Fail + Artifact-Pfaden.

### PHASE 5 – DELIVERY

1. E2E-Suite, Fixes, Ablaufprotokolle.
2. Delivery Report; Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/e2e-journeys --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Map | 5–10 Journeys |
| Data | Isolated fixtures only |
| Assert | Checkpoints + screenshots |
| Stop | Live side effects |

## Red Flags

- Prod-Checkout „zum Test“
- Nur Happy Path
- Sleep-only Waits
- Keine Screenshots
- Fertig ohne PHASE 4

## Resources

- `references/journey-test-matrix.md`
- `scripts/scaffold_journey_spec.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
