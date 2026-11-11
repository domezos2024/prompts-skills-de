---
name: labor-fuer-zuverlaessigkeit-und-fehlerwiederherstellung
description: Use when improving resilience to network faults, dependency outages, timeouts, retries/backoff/circuit breakers, restart recovery, and idempotency under failure - runs a strict multi-phase dependency mapping, controlled fault injection in non-prod, hardening, integrity checks, and recovery-metrics workflow. No prod chaos without an approved window.
---

# Labor für Zuverlässigkeit & Fehlerwiederherstellung

## Overview

Macht Anwendungen widerstandsfähiger gegen Netzprobleme, Dienstausfälle und Ressourcenengpässe. Kernprinzip: **Abhängigkeiten kartieren → kontrollierte Fault Injection (Lab/Stage) → Timeouts/Retry/Backoff/Breaker härten → Integrität/Idempotenz prüfen → Recovery-Metriken und SPOFs dokumentieren.** Kein Chaos auf Prod ohne freigegebenes Wartungsfenster.

## When to Use

- Timeouts, Partial Outages, Retry-Stürme, Restart-Recovery
- Circuit Breaker / Bulkhead / Backoff fehlen oder greifen falsch
- Doppelte Verarbeitung / Datenintegrität unter Fehlerbedingungen

## When NOT to Use

- Funktionale QA ohne Fault Injection → `autonomer-qa-testingenieur`
- Crash-Root-Cause ohne Resilience-Fokus → `ursachenermittler-fuer-abstuerze-und-ausnahmen`
- Produktiv-Chaos ohne Autorisierung

## Critical Guidelines

- MUST externe Abhängigkeiten und Ausfallszenarien inventarisieren.
- MUST kontrollierte Testumgebung mit realistischen Faults nutzen.
- MUST Timeouts, Retries, Backoff, Circuit Breaker, Restart-Verhalten prüfen/implementieren.
- MUST Datenintegrität und Idempotenz unter Fehlern verifizieren.
- MUST Recovery-Zeiten, Grenzen und SPOFs dokumentieren.
- NEVER Chaos-Tests auf Prod ohne ausdrücklich freigegebenes Fenster.
- NEVER unbegrenzte Retries ohne Jitter/Budget (Retry-Storms).
- NEVER destruktive Datenexperimente ohne Backup/Rollback.
- ALWAYS Iron Laws und Phasenstatus.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill labor-fuer-zuverlaessigkeit-und-fehlerwiederherstellung --root .skill-runs/reliability-lab
```

### PHASE 1 – DISCOVERY

1. Dependencies (DB, APIs, Queues, Storage, DNS) und Failure Modes listen.
2. Bestehende Timeout/Retry/Breaker-Configs erfassen.
3. SLO/SLI falls vorhanden; sonst pragmatische Lab-Ziele setzen.
4. Matrix `references/reliability-fault-matrix.md` anlegen.

**Gate:** Dependency- + Fault-Inventar existieren.

### PHASE 2 – LAB SETUP & PLAN

1. Isolierte Stage/Lab-Umgebung; Synthetische Last wo nötig.
2. Fault-Plan: timeout, connection reset, dependency down, slow-dep, process restart.
3. Messgrößen: success rate, latency, recovery time, duplicate side effects.
4. Hardening-Pakete mit Rollback.

**Gate:** Freigabe der Lab-Targets; Prod explizit out-of-scope oder Fenster dokumentiert.

### PHASE 3 – INJECT & HARDEN

1. Faults einzeln injizieren; Beobachtungen protokollieren.
2. Timeouts/Backoff/Breaker/Idempotency Keys implementieren.
3. Graceful Degradation wo spezifiziert.
4. Nach jedem Paket: Fault-Szenario erneut.

**Gate:** P0-Failure-Modes beherrscht oder als SPOF akzeptiert dokumentiert.

### PHASE 4 – VALIDATION

1. Integrität: keine stillen Datenkorruptionen; keine unerwünschten Doppelbuchungen.
2. Recovery-Zeiten messen; Grenzen notieren.
3. Automatisierte Fault-Simulationen committen, soweit machbar.
4. Ergebnisse gegen Matrix.

**Gate:** Reliability-Bericht mit Metriken und Rest-SPOFs.

### PHASE 5 – DELIVERY

1. Code-Härte, Simulationsskripte/-tests, Bericht.
2. Delivery Report; Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/reliability-lab --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Map | Dependencies × faults |
| Inject | Lab/Stage only |
| Harden | Timeout/Retry/Breaker/Idempotency |
| Prove | Integrity + recovery metrics |

## Red Flags

- Prod-Chaos ohne Fenster
- Retry ohne Cap/Jitter
- „Irgendwie wieder da“ ohne Metrik
- Doppelte Side Effects ignoriert
- Fertig ohne PHASE 4

## Resources

- `references/reliability-fault-matrix.md`
- `scripts/scaffold_fault_drill.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
