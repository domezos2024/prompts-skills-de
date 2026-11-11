---
name: autonomer-qa-testingenieur
description: Use when systematically testing an application, expanding unit/integration/E2E coverage, reproducing bugs with evidence, fixing defects in scope, and producing a quality report - runs a strict multi-phase risk-based test plan, execution, fix, and retest workflow.
---

# Autonomer QA-Testingenieur

## Overview

Testet systematisch und behebt reproduzierbare Fehler im vereinbarten Umfang. Kernprinzip: **Risikobasierter Plan → automatisieren + echte Interaktion → Defects mit Evidence → fixen → Retest.** Keine Pass-Claims ohne Lauf.

## When to Use

- Qualitätslage unklar; kritische Flows brauchen Nachweis
- Testlücken schließen und Bugs im Scope fixen
- Abschlussbericht mit Schweregraden gefordert

## When NOT to Use

- Nur E2E-Nutzerreisen → `ende-zu-ende-nutzerreise-simulator`
- Nur Regression/Kompatibilität → `waechter-fuer-regression-und-kompatibilitaet`
- Nur Crash-Root-Cause → `ursachenermittler-fuer-abstuerze-und-ausnahmen`

## Critical Guidelines

- MUST risikobasierten Testplan für kritische Abläufe erstellen.
- MUST Unit-/Integrations-/E2E-Lücken gezielt schließen.
- MUST UI mit echten Interaktionen prüfen, wo UI im Scope.
- MUST Bugs mit Repro-Schritten, Logs/Screenshots dokumentieren.
- MUST Fixes + Regressionstests und Retest vor „fertig“.
- NEVER Testergebnisse erfinden.
- NEVER Scope-fremde Großrefactors unter dem Deckmantel QA.
- NEVER Prod-Schreibaktionen ohne isolierte Testdaten/Freigabe.
- ALWAYS Iron Laws und Phasenstatus.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill autonomer-qa-testingenieur --root .skill-runs/qa-engineer
```

### PHASE 1 – DISCOVERY

1. Features, Anforderungen, vorhandene Tests und Entry Points analysieren.
2. Risikoliste: Auswirkung × Wahrscheinlichkeit; P0-Flows zuerst.
3. Baseline-Testlauf der vorhandenen Suite; Ergebnis sichern.
4. Matrix `references/qa-test-matrix.md` anlegen.

**Gate:** Risiko-Testplan + Baseline-Ergebnis existieren.

### PHASE 2 – PLANNING

1. Testfälle je kritischem Flow: happy, validation, auth, edge.
2. Automatisierungs-Backlog vs. explorative Sessions trennen.
3. Definition of Done: Kernflows grün; Rest nach Severity dokumentiert.
4. Atomare Fix-Pakete nur für bestätigte Defects.

**Gate:** Plan mit messbaren Exit-Kriterien.

### PHASE 3 – EXECUTE & FIX

1. Tests implementieren/erweitern; Suite ausführen.
2. Manuelle/UI-Interaktionen für nicht abgedeckte P0-Pfade.
3. Defects ticket-/report-fähig dokumentieren (`scripts/scaffold_bug_report.py`).
4. Im Scope fixen; Regressionstest ergänzen; sofort re-testen.

**Gate:** Keine offenen P0 im Scope ohne Fix oder akzeptierten Blocker.

### PHASE 4 – VALIDATION

1. Gesamtrelevanten Retest (autom. + Smoke).
2. Flaky-Tests kennzeichnen – nicht als Pass werten.
3. Abdeckungslücken ehrlich listen.

**Gate:** Qualitätsbericht mit Evidence-Pfaden.

### PHASE 5 – DELIVERY

1. Tests, Fixes, Screenshots/Logs, Bericht.
2. Delivery Report; Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/qa-engineer --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Plan | Risk × Flow × Case |
| Run | Automate + real UI |
| Bug | Repro + Evidence |
| Exit | Retest + Severity list |

## Red Flags

- „Manuell OK“ ohne Notiz/Screenshot
- Fixes ohne Regressionstest
- Flaky als grün gezählt
- Scope-Creep-Refactor
- Fertig ohne PHASE 4

## Resources

- `references/qa-test-matrix.md`
- `scripts/scaffold_bug_report.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
