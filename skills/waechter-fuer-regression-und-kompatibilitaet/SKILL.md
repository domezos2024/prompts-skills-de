---
name: waechter-fuer-regression-und-kompatibilitaet
description: Use when preventing regressions from recent changes, mapping impacted modules, building OS/browser/runtime compatibility matrices, adding regression tests, and documenting tested vs untested environments - runs a strict multi-phase change-impact, matrix execution, fix, and evidence workflow.
---

# Wächter für Regression & Kompatibilität

## Overview

Verhindert, dass Änderungen bestehende Funktionen oder Plattformkompatibilität beschädigen. Kernprinzip: **Diff-Impact → Matrix → Tests in verfügbaren Targets → bestätigte Regressionen fixen → getestet vs. ungetestet ehrlich melden.**

## When to Use

- Nach Features/Refactors Regressionen absichern
- Browser/OS/Runtime-Kompatibilität nachweisen
- CI-Regressionssuite erweitern

## When NOT to Use

- Erste explorative QA ohne Change-Fokus → `autonomer-qa-testingenieur`
- Nur neue E2E-Journeys → `ende-zu-ende-nutzerreise-simulator`
- Chaos/Resilience → `labor-fuer-zuverlaessigkeit-und-fehlerwiederherstellung`

## Critical Guidelines

- MUST Änderungen ggü. letztem bekannten Gut-Stand analysieren.
- MUST betroffene Module, APIs und indirekte Abhängigkeiten bestimmen.
- MUST Kompatibilitätsmatrix mit relevanten OS/Browser/Runtime-Versionen führen.
- MUST kritische Regressionstests ergänzen und ausführen.
- MUST getestete, nicht getestete und unsupported Environments trennen.
- NEVER „überall grün“ ohne Matrix-Evidence.
- NEVER unbestätigte Umweltprobleme als App-Regression labeln (oder umgekehrt).
- NEVER fehlgeschlagene kritische Regressionen ignorieren.
- ALWAYS Iron Laws und Phasenstatus.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill waechter-fuer-regression-und-kompatibilitaet --root .skill-runs/regression-compat
```

### PHASE 1 – DISCOVERY (Impact)

1. Diff/Changelog seit Baseline analysieren.
2. Impact-Graph: direkte Module + Consumer + Shared Contracts.
3. Bestehende Regressionssuites inventarisieren.
4. Matrix `references/regression-compat-matrix.md` vorbereiten.

**Gate:** Impact-Liste + Baseline-Referenz existieren.

### PHASE 2 – PLANNING

1. Target-Environments aus Projekt-Support-Policy ableiten.
2. Pflicht-Tests für P0-Funktionen; Lücken schließen.
3. Ausführungsreihenfolge: unit → integration → e2e/compat smoke.
4. Rollback-/Fix-Strategie bei roten P0.

**Gate:** Matrix + Ausführungplan mit Exit-Kriterien.

### PHASE 3 – EXECUTE & FIX

1. Vorhandene und neue Tests in verfügbaren Targets laufen lassen.
2. Failures triage: echte Regression vs. Env-Limit vs. Flake.
3. Bestätigte Regressionen fixen; Tests ergänzen.
4. Re-run der betroffenen Suite.

**Gate:** Keine bekannten kritischen Regressionen in getesteten Configs.

### PHASE 4 – VALIDATION

1. Gesamtrelevanten Retest nach Fixes.
2. Matrix-Zellen mit Evidence füllen.
3. Untested/Unsupported explizit ausweisen.

**Gate:** Bericht ohne unbelegte Universal-Claims.

### PHASE 5 – DELIVERY

1. Suite, Matrix, Ergebnisbericht.
2. Delivery Report; Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/regression-compat --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Impact | Diff → modules → contracts |
| Matrix | OS × Browser × Runtime |
| Fix | Confirmed regressions only |
| Report | Tested vs untested |

## Red Flags

- „Sollte überall laufen“
- Nur Chromium getestet, alle Browser grün gemeldet
- Flake als Produktbug ohne Nachweis
- Fertig ohne MATRIX-Evidence
- Fertig ohne PHASE 4

## Resources

- `references/regression-compat-matrix.md`
- `scripts/scaffold_compat_matrix.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
