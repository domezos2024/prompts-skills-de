---
name: autonome-codebereinigung-und-refaktorierung
description: Use when cleaning and refactoring a codebase for readability, maintainability, and safe structure - capturing build/test baselines, applying small verified change sets, removing dead code, and preventing unintended behavior changes.
---

# Autonome Codebereinigung und Refaktorierung

## Overview

Überarbeitet die Codebasis hinsichtlich Verständlichkeit, Wartbarkeit, Performance und Sicherheit — ohne Verhaltensdrift. Kernprinzip: **Baseline (Build/Tests/Analyse) → kleine Pakete → Regression nach jedem Paket → Restschulden benennen.** Korrektheit und Lesbarkeit schlagen Cleverness.

## When to Use

- Code ist schwer lesbar, stark dupliziert oder inkonsistent strukturiert
- Formatierung, Fehlerbehandlung, Logging oder Ressourcenverwaltung weichen wild ab
- Ungenutzter Code / überflüssige Abhängigkeiten sollen sicher entfernt werden

## When NOT to Use

- Große Architektur-Migration → `modernisierung-der-softwarearchitektur`
- Primär Dependency-Upgrades/CVE → `beseitigung-von-abhaengigkeiten-und-technischen-schulden`
- Messbare Runtime-Optimierung als Hauptziel → `performance-profiling-und-optimierung`
- Undokumentierter Legacy-Rescue inkl. Charakterisierungstests → `rettungsmission-fuer-altcode`

## Critical Guidelines

- MUST Architektur, Abhängigkeiten, Konventionen und vorhandene Tests vor Refactor analysieren.
- MUST Ausgangszustand durch Build, Tests und verfügbare statische Analyse erfassen.
- MUST in kleinen, nachvollziehbaren Änderungspaketen arbeiten; nach jedem Paket Regression.
- MUST Formatierung, Fehlerbehandlung, Logging und Ressourcenverwaltung vereinheitlichen wo angefasst.
- MUST ungenutzten Code und überflüssige Abhängigkeiten nur mit Nachweis entfernen.
- NEVER Verhalten unbeabsichtigt ändern; API-Verträge ohne Migration/Tests nicht brechen.
- NEVER „kurze Einzeiler“ auf Kosten der Lesbarkeit erzwingen.
- NEVER riesige Big-Bang-Refactors ohne Zwischen-Gates.
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill autonome-codebereinigung-und-refaktorierung --root .skill-runs/refactor
```

### PHASE 1 – DISCOVERY

1. Projektstruktur, Module, Konventionen, Testsetup und CI-Skripte erfassen.
2. Hotspots: Duplikate, Komplexität, Naming, ineffiziente Stellen — mit Pfaden.
3. Baseline: Build/Tests/Lint unter `artifacts/refactor-baseline/` protokollieren.
4. Befunde nach `references/refactor-risk-checklist.md` priorisieren.

**Gate:** Baseline-Protokolle + priorisierte Hotspot-Liste.

### PHASE 2 – PLANNING

1. Pakete schnüren (z. B. Extract Method, Naming, Dead-Code, Error-Handling-Vereinheitlichung).
2. Pro Paket: Scope, Nicht-Ziele, Akzeptanz (Tests grün), Rollback.
3. Sicherheitsrelevante Stellen separat und vorsichtiger behandeln.

**Gate:** Paketplan mit messbaren Done-Kriterien.

### PHASE 3 – IMPLEMENTATION

1. Paketweise refaktorieren; Diffs klein und reviewbar halten.
2. Format/Error/Logging/Resources nur im angefassten Bereich angleichen.
3. Dead Code / unused deps nur mit Nachweis (Referenzsuche/Tool) entfernen.
4. Nach jedem Paket: relevante Tests/Build; bei Rot fixen oder revertieren.

**Gate:** Geplante Pakete integriert; keine bekannten Test-Rots offen.

### PHASE 4 – VALIDATION

1. Volle verfügbare Test-/Lint-/Build-Suite erneut fahren.
2. Verhaltens-Stichproben kritischer Flows.
3. Änderungsübersicht vs. Restprobleme dokumentieren.

**Gate:** Validierungsprotokoll; keine unbelegten „alles grün“-Claims.

### PHASE 5 – DELIVERY

1. Delivery Report nach `_shared/references/delivery-report-template.md`.
2. Änderungsübersicht, Testresultate, Restschulden.
3. Checkpoint auf `done` setzen.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/refactor --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Baseline | Build + Tests + Analyse sichern |
| Schnitt | Kleine Pakete, ein Thema |
| Beweis | Tests nach jedem Paket |
| Dead Code | Nur mit Nachweis löschen |
| Stop | Rot/unklar → fix oder rollback |

## Red Flags

- Refactor ohne Test-/Build-Baseline
- Verhaltensänderung „nebenbei“
- 1000+ Zeilen ungetestet
- Unused entfernt ohne Referenzcheck
- Fertig ohne PHASE 4

## Resources

- `references/refactor-risk-checklist.md`
- `scripts/capture_quality_baseline.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
