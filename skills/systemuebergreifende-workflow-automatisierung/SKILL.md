---
name: systemuebergreifende-workflow-automatisierung
description: Use when automating a recurring business or engineering process across multiple apps, eliminating manual handoffs, adding event/schedule triggers with idempotency and durable state, or preventing duplicate external side effects - runs as-is capture, workflow design, integration, and controlled end-to-end tests.
---

# Systemübergreifende Workflow-Automatisierung

## Overview

Automatisiert einen wiederkehrenden Prozess **über mehrere Systeme** hinweg. Kernprinzip: **Ist-Ablauf erfassen → Medienbrüche entfernen → event-/zeitgesteuert orchestrieren → Idempotenz + kontrollierte Side-Effects.** Keine stillen Mehrfachaktionen.

## When to Use

- Manueller Cross-App-Prozess (Tickets, Dateien, APIs, Chat, CRM…)
- Zeit- oder Event-Trigger gewünscht
- Duplikatschutz, Retries und persistenter Zustand nötig
- Kritische externe Änderungen müssen auditierbar sein

## When NOT to Use

- Reine Einzel-API-Anbindung → `ingenieur-fuer-rest-api-integration`
- Daten-ETL/Pipelines → `architekt-fuer-datenpipelines-und-etl`
- Nur Agenten-State-Maschine ohne Business-Systeme → `architekt-fuer-autonome-agenten-workflows`

## Critical Guidelines

- MUST manuellen Ist-Ablauf, Datenquellen und Zielsysteme vor Design dokumentieren.
- MUST Idempotenz und Dedup für alle externen Writes.
- MUST persistente Zustände, Fehlerbehandlung und begrenzte Retries.
- MUST kritische externe Änderungen hinter Confirm/Feature-Flag/Approval steuerbar machen.
- MUST E2E mit isolierten Testdaten prüfen.
- NEVER Produktivdaten als erstes Testziel ohne Freigabe.
- NEVER Mehrfach-Posts bei Retry ohne Dedup-Schlüssel.
- NEVER Erfolg ohne Zeitersparnis-/Voraussetzungsdoku behaupten, wenn Messung fehlt – dann als Schätzung kennzeichnen.
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill systemuebergreifende-workflow-automatisierung --root .skill-runs/cross-workflow
```

### PHASE 1 – DISCOVERY

1. Ist-Ablauf Schritt für Schritt erfassen (Menschen, Systeme, Artefakte).
2. Medienbrüche, Fehlerquellen, SLAs markieren.
3. `scripts/scaffold_workflow_runbook.py` für Runbook-Gerüst.
4. `references/cross-system-workflow-checklist.md`.

**Gate:** Ist-Prozesskarte + Risikoliste.

### PHASE 2 – PLANNING

1. Trigger (Cron/Event/Webhook) und Ziel-Architektur.
2. Integrationspunkte (API/Datei/MCP); Verträge je Schritt.
3. Idempotenz-Schlüssel, State-Store, Dead-letter.
4. Safety: Dry-Run, Approval für P0-Writes.

**Gate:** Workflow-Plan mit messbaren Done-Kriterien.

### PHASE 3 – IMPLEMENTATION

1. Orchestrator + Integrationen.
2. Validierung Eingaben; Dedup-Store; Retries mit Backoff.
3. Logging/Audit für externe Changes.
4. Bedien-/Config-Oberfläche oder CLI-Dokumentation.

**Gate:** Happy Path in Testumgebung ausführbar.

### PHASE 4 – VALIDATION

1. E2E mit isolierten Testdaten.
2. Retry-/Crash-Resume ohne Doppelwirkung.
3. Failure injection an Integrationen.
4. Voraussetzungen und Bedienung verifizieren.

**Gate:** Testprotokoll + bekannte Grenzen.

### PHASE 5 – DELIVERY

1. Delivery Report; Zeitersparnis gemessen oder klar als Schätzung.
2. Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/cross-workflow --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Ist | Prozesskarte + Brüche |
| Trigger | Event oder Schedule |
| Safety | Idempotenz + Approval |
| State | Persistent + DLQ |
| Stop | Doppel-Write-Risiko offen → nicht live |

## Red Flags

- Retry ohne Dedup
- Prod-Writes im ersten Test
- Kein State bei Mehrschritt
- Unkontrollierbare externe Side-Effects
- „Automatisiert“ ohne E2E-Beweis

## Resources

- `references/cross-system-workflow-checklist.md`
- `scripts/scaffold_workflow_runbook.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
