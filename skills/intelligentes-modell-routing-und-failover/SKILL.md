---
name: intelligentes-modell-routing-und-failover
description: Use when routing tasks across multiple LLM providers, implementing model failover after rate limits or outages, unifying provider adapters, checkpointing work for context handoff, or logging cost/usage safely - runs inventory, adapter design, routing policies, and failover tests without inventing access.
---

# Intelligentes Modell-Routing und Failover

## Overview

Baut ein Routing-System, das **tatsächlich verfügbare** LLM-Anbieter nutzt, bei Fehlern failovers und Arbeit fortsetzt. Kernprinzip: **Inventar der echten Zugänge → einheitliche Adapter → policy-basiertes Routing → idempotenter Context-Handoff.** Keine erfundenen Kontingente.

## When to Use

- Mehrere Provider/CLIs; Aufgaben sollen priorisiert geroutet werden
- Rate-Limits/Outages brauchen Failover
- Kosten-/Nutzungsprotokollierung und Checkpoints nötig
- Context bei Provider-Wechsel übertragen

## When NOT to Use

- Agenten-Rollenorchestrierung → `ingenieur-fuer-multi-agenten-zusammenarbeit`
- MCP-Tool-Optimierung → `mcp-werkzeug-intelligenz-und-optimierung`
- Einzelprovider ohne Failover-Bedarf

## Critical Guidelines

- MUST nur inventarisierte, verifizierte APIs/CLIs/Auth-Methoden verwenden.
- MUST Nutzungsbedingungen, Kosten, Quotas und Limits dokumentieren.
- MUST einheitliche Provider-Schnittstelle und aufgabenabhängige Prioritäten.
- MUST Rate-Limit-/Netz-/Unavailable-Erkennung und Failover-Policy.
- MUST kompakte Checkpoints; Context-Handoff ohne doppelte Tool-Effects.
- NEVER nicht vorhandene Modellzugänge oder „kostenlose Unlimited“-Kontingente annehmen.
- NEVER Anbieterbeschränkungen umgehen.
- NEVER Secrets in Logs; Kostenlogs aggregiert/redaktiert.
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill intelligentes-modell-routing-und-failover --root .skill-runs/model-routing
```

### PHASE 1 – DISCOVERY

1. Verfügbare Provider, Auth, Modelle, Regionen, Limits inventarisieren (wirklich testen/prüfen).
2. ToS/Kosten/Quotas notieren; fehlende Zugänge als Blocker markieren.
3. Matrix mit `scripts/scaffold_provider_matrix.py`.
4. `references/model-routing-checklist.md`.

**Gate:** Provider-Matrix nur mit verifizierten Einträgen.

### PHASE 2 – PLANNING

1. Unified Adapter-Contract (chat/complete/tools/embed – je nach Bedarf).
2. Routing-Policies (task-type → priority list) und Budget-Caps.
3. Failover-Klassifikation (retryable vs hard-fail) + Checkpoint-Schema.
4. Observability: usage, latency, error class, cost estimate.

**Gate:** Policy-Dokument + Adapter-API spezifiziert.

### PHASE 3 – IMPLEMENTATION

1. Provider-Adapter hinter einheitlicher Schnittstelle.
2. Router mit Prioritäten, Health/Cooldown, Budget-Guards.
3. Checkpoint + Context-Pack für Handoff; Effect-Dedup bei Tool-Loops.
4. Usage-/Cost-Logging (ohne Secrets).

**Gate:** Mindestens ein Failover-Pfad in Staging/Dev demonstrierbar.

### PHASE 4 – VALIDATION

1. Rate-Limit-/Timeout-/Unavailable-Simulation.
2. Context-Handoff und Schutz gegen doppelte Tool-Ausführung.
3. Kostenlog-Stichproben; Policy-Respect (kein verbotener Fallback).
4. Doku der Konfiguration aktualisieren.

**Gate:** Failover-Testprotokoll ohne erfundene Provider.

### PHASE 5 – DELIVERY

1. Delivery Report + Config-Doku.
2. Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/model-routing --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Inventar | Nur verifizierte Zugänge |
| Adapter | Einheitliche Provider-API |
| Routing | Task → Prioritätsliste + Budget |
| Failover | Error-Klasse → nächster Provider |
| Stop | Kein Zugang → Blocker, nicht faken |

## Red Flags

- „Provider X ist sicher gratis/verfügbar“ ohne Check
- Failover umgeht ToS/Region-Limits
- Context-Handoff ohne Checkpoint
- Doppelte Tool-Calls nach Switch
- Secrets in Usage-Logs

## Resources

- `references/model-routing-checklist.md`
- `scripts/scaffold_provider_matrix.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
