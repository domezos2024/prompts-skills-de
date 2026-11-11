---
name: architekt-fuer-autonome-agenten-workflows
description: Use when designing resilient autonomous or semi-autonomous agent workflows, needing checkpoints, retries, approval gates, interrupt/resume without duplicate side effects, or turning a complex task into a state-machine workflow - runs decomposition, state design, implementation, and recovery validation.
---

# Architekt für autonome Agenten-Workflows

## Overview

Baut aus einem komplexen Auftrag einen **belastbaren Agentenworkflow** mit Zustandsmaschine, Checkpoints und Recovery. Kernprinzip: **atomare Schritte → persistenter State → idempotente Fortsetzung nach Unterbrechung.** Keine „Fire-and-forget“-Autonomie ohne Grenzen.

## When to Use

- Lange/mehrstufige Agentenaufträge sollen unterbrechbar fortsetzbar sein
- Retry, Timeouts, Approval für irreversible Aktionen nötig
- Doppelte Side-Effects nach Crash/Reconnect vermeiden
- Auftrag: „autonomen Agentenworkflow entwerfen/bauen“

## When NOT to Use

- Multi-Agent-Rollen/Orchestrierung → `ingenieur-fuer-multi-agenten-zusammenarbeit`
- Nur Modell-Failover → `intelligentes-modell-routing-und-failover`
- Einmalige manuelle Einzelschritte ohne Automation

## Critical Guidelines

- MUST Auftrag in atomare Schritte mit prüfbaren Outputs zerlegen.
- MUST Zustandsmaschine (Plan → Execute → Validate → Recover) und persistente Checkpoints implementieren.
- MUST Idempotenz-Schlüssel oder „exactly-once effect / at-least-once compute“-Strategie je Side-Effect definieren.
- MUST Retry-Budget, Timeouts und Circuit-Grenzen setzen.
- MUST Approval-Gates für irreversible/sensible Aktionen.
- NEVER Fortsetzung ohne State-Reload und Effect-Dedup annehmen.
- NEVER unbegrenzte Retries oder stille Endlosschleifen.
- NEVER Erfolg ohne Unterbrechungs-/Resume-Simulation behaupten.
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill architekt-fuer-autonome-agenten-workflows --root .skill-runs/agent-workflow
```

### PHASE 1 – DISCOVERY

1. Auftrag, Tools, Eingaben, Abhängigkeiten und Failure-Modi erfassen.
2. Manuelle vs. automatisierbare Schritte trennen; irreversible Aktionen markieren.
3. Vorlage mit `scripts/scaffold_workflow_state.py` anlegen.
4. Prüfpunkte nach `references/autonomous-workflow-checklist.md`.

**Gate:** Atomare Schrittliste + Risiko-/Approval-Markierungen.

### PHASE 2 – PLANNING

1. Zustandsmaschine und Transitions inkl. Fehlerzustände spezifizieren.
2. Checkpoint-Schema (Schritt-ID, Step, Inputs-Hash, Effect-IDs, Status).
3. Retry/Backoff/Timeout-Policy und Compensating Actions skizzieren.
4. Observability: strukturierte Statusmeldungen und Metriken.

**Gate:** State-Diagramm/Schema + Policies dokumentiert.

### PHASE 3 – IMPLEMENTATION

1. Orchestrator mit persistenter Fortschrittsablage.
2. Step-Runner: Validierung In → Execute → Validate Out → Checkpoint.
3. Approval-Hooks und Idempotenz-Guards für Side-Effects.
4. Status-API/Logs für Menschen lesbar.

**Gate:** Happy Path läuft; Checkpoints werden geschrieben.

### PHASE 4 – VALIDATION

1. Unterbrechung mitten im Schritt und nach Checkpoint simulieren.
2. Resume ohne doppelte Effects prüfen.
3. Timeout-/Retry-/Approval-Pfade testen.
4. Fehlerszenarien dokumentieren und re-testen.

**Gate:** Recovery-Protokoll ohne unbelegte Claims.

### PHASE 5 – DELIVERY

1. Delivery Report; Betriebsgrenzen und bekannte Failure-Modes.
2. Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/agent-workflow --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Zerlegung | Atomare Schritte + prüfbare Outputs |
| State | Persistenter Checkpoint + Transitions |
| Safety | Approval + Idempotenz |
| Recovery | Interrupt/Resume-Simulation |
| Stop | Kein Resume-Beweis → nicht fertig |

## Red Flags

- State nur im Speicher
- Side-Effect ohne Idempotenz
- Unbegrenzte Retries
- „Autonom“ ohne Approval für destruktive Schritte
- Fertig ohne Crash-Resume-Test

## Resources

- `references/autonomous-workflow-checklist.md`
- `scripts/scaffold_workflow_state.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
