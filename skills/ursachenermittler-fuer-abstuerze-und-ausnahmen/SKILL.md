---
name: ursachenermittler-fuer-abstuerze-und-ausnahmen
description: Use when investigating recurring crashes and exceptions, classifying by severity/frequency, reproducing in a controlled environment, fixing true root causes (not swallowing errors), and adding regression tests plus safer diagnostics - runs a strict multi-phase collect, reproduce, root-cause, fix, and retest workflow.
---

# Ursachenermittler für Abstürze & Ausnahmen

## Overview

Findet und behebt tatsächliche Ursachen wiederkehrender Abstürze/Exceptions. Kernprinzip: **Evidence sammeln → klassifizieren → kontrolliert reproduzieren → Root Cause fixen → Regression + besseres Logging → gleiche Steps retesten.** Kein pauschales Verschlucken von Exceptions; keine sensiblen Daten in Diagnoselogs.

## When to Use

- Wiederkehrende Crashes, Unhandled Exceptions, Fatal Errors
- Stacktraces vorhanden, Ursache unklar
- Stabilitätsbugs statt Feature-Arbeit

## When NOT to Use

- Allgemeine QA ohne Crash-Fokus → `autonomer-qa-testingenieur`
- Infra-Chaos/Dependency-Outages → `labor-fuer-zuverlaessigkeit-und-fehlerwiederherstellung`
- Security-Exploit-Analyse → Security-Skills

## Critical Guidelines

- MUST Logs, Stacktraces, Repro-Szenarien und Versionen sammeln.
- MUST nach Häufigkeit/Schwere/Impact klassifizieren (P0 zuerst).
- MUST in kontrollierter Umgebung reproduzieren bevor „fix“.
- MUST Root Cause adressieren (Zustände, Concurrency, Ressourcen) – nicht nur Message ändern.
- MUST Regressionstests und sinnvolle Diagnose-Logs ergänzen.
- NEVER leere catch-Blöcke / pauschal schlucken.
- NEVER Secrets/PII/Tokens in Logs schreiben.
- NEVER Symptome als fertig melden, wenn Crash noch reproduzierbar.
- ALWAYS Iron Laws und Phasenstatus.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill ursachenermittler-fuer-abstuerze-und-ausnahmen --root .skill-runs/crash-rca
```

### PHASE 1 – COLLECT

1. Logs, Stacktraces, Crash-Dumps, Fehlermeldungen, betroffene Versionen sichern.
2. Cluster bilden: gleiche Signature → ein Incident.
3. Checkliste `references/crash-rca-checklist.md` starten.
4. Hypothesenliste ohne Fix-Aktion.

**Gate:** Incident-Backlog mit Top-P0/P1 und Evidence-Pfaden.

### PHASE 2 – REPRODUCE

1. Kontrollierte Env mit möglichst gleicher Version/Config.
2. Minimale Repro-Steps; Flakiness notieren (Timing/Race).
3. Bei Nicht-Repro: Telemetrie erweitern (ohne PII) und Scope ehrlich setzen.
4. Gate nur für reproduzierbare oder klar telemetrie-belegte Cases weiter.

**Gate:** Repro-Skript/Steps für Top-Incidents oder dokumentierter Blocker.

### PHASE 3 – ROOT CAUSE & FIX

1. Kontrollfluss, Nebenläufigkeit, Lifecycle, Ressourcen, Null/State prüfen.
2. Ursache belegen (warum crash; warum Fix korrekt).
3. Fix implementieren; kein generisches catch-all.
4. Logging: hilfreiche Kontextfelder, redaktiert.
5. Regressionstest der Repro-Steps.

**Gate:** Fix + Test für jeden bearbeiteten P0.

### PHASE 4 – VALIDATION

1. Dieselben Repro-Steps erneut; Crash darf nicht auftreten.
2. Nahe Verwandte Signatures smoke-testen.
3. Log-Proben auf Secret/PII-Leaks prüfen.

**Gate:** Retest-Protokoll mit vorher/nachher Evidence.

### PHASE 5 – DELIVERY

1. Root-Cause-Bericht, Fixes, Tests, Rest-Incidents.
2. Delivery Report; Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/crash-rca --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Collect | Logs + signatures |
| Repro | Controlled env |
| Fix | Root cause + test |
| Stop | Swallow-all catch |

## Red Flags

- `catch (Exception) {}`
- Fix ohne Retest der Repro-Steps
- Tokens in Crash-Logs
- „Nicht reproduzierbar“ als Erfolg
- Fertig ohne PHASE 4

## Resources

- `references/crash-rca-checklist.md`
- `scripts/scaffold_rca_report.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
