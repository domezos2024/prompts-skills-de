---
name: intelligentes-benachrichtigungs-und-ereignisverarbeitungssystem
description: Use when building reliable event processing and notifications with durable queues, delivery state machines, retries/backoff/dead-letter, user preferences/opt-ins, or deduplicating duplicate events across email/push/in-app channels - runs event modeling, queue design, channel integration, and interruption-safe delivery tests.
---

# Intelligentes Benachrichtigungs- und Ereignisverarbeitungssystem

## Overview

Baut ein zuverlässiges System für **Ereignisverarbeitung, Queues und Benachrichtigungen**. Kernprinzip: **Ereignisvertrag → persistente Queue mit IDs → Zustell-State-Maschine → Retries/DLQ + Opt-in-Präferenzen.** Kein unkontrollierter Verlust, keine blinden Doppelzustellungen.

## When to Use

- Events sollen zuverlässig verarbeitet und benachrichtigt werden
- Mehrere Kanäle (E-Mail, Push, In-App…)
- Dedup, Offline, unterbrochene Zustellung
- User-Preferences / Opt-ins erforderlich

## When NOT to Use

- Reine ETL ohne Notification → `architekt-fuer-datenpipelines-und-etl`
- Cross-System Business-Workflow ohne Event-Focus → `systemuebergreifende-workflow-automatisierung`
- Nur REST-Client ohne Queue → `ingenieur-fuer-rest-api-integration`

## Critical Guidelines

- MUST Ereignistypen, Empfänger, Kanäle und Prioritäten vor Implementierung definieren.
- MUST persistente Queue mit eindeutigen Event- und Nachrichten-IDs.
- MUST Zustandsmodell für Verarbeitung/Zustellung (mindestens pending→processing→sent/failed/dead).
- MUST Retry + Backoff + Dead-Letter für dauerhafte Fehler.
- MUST Opt-ins/Preferences vor Kanalversand prüfen.
- NEVER Events bei normalen Unterbrechungen still verwerfen.
- NEVER Spam durch fehlende Dedup bei At-least-once.
- NEVER Marketing-/Push ohne rechtlich nötiges Opt-in (Kontext beachten).
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill intelligentes-benachrichtigungs-und-ereignisverarbeitungssystem --root .skill-runs/events-notify
```

### PHASE 1 – DISCOVERY

1. Event-Katalog, Producer, Consumer, SLAs, Compliance-Grenzen.
2. Kanäle und Provider-Limits inventarisieren.
3. `scripts/scaffold_event_catalog.py`.
4. `references/event-notification-checklist.md`.

**Gate:** Event-Katalog + Kanalmatrix.

### PHASE 2 – PLANNING

1. Event-/Notification-Verträge und ID-Strategien (idempotency keys).
2. Queue-/Outbox-Design und State-Maschine.
3. Retry/Backoff/DLQ-Policy; Preference-Modell.
4. Observability: delivery status, lag, fail reasons.

**Gate:** Design mit messbaren Delivery-Garantien (at-least-once + dedup).

### PHASE 3 – IMPLEMENTATION

1. Persistente Queue/Outbox + Worker.
2. Handler mit State-Transitions und Dedup.
3. Kanaladapter; Preference/Opt-in-Checks.
4. Monitoring-Dashboards/Logs für Zustellstatus.

**Gate:** End-to-end Event → Notification in Testumgebung.

### PHASE 4 – VALIDATION

1. Doppelte Events; Offline/Provider-Down; Worker-Crash mid-send.
2. Opt-out respektiert; DLQ erreichbar und replaybar.
3. Prioritäten/Backoff prüfen.
4. Audit-Trail Stichprobe.

**Gate:** Testprotokoll ohne „verlustfrei“-Claim ohne Beweis.

### PHASE 5 – DELIVERY

1. Delivery Report; Betriebs- und Replay-Runbook.
2. Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/events-notify --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| IDs | event_id + notification_id |
| State | pending→…→sent/failed/dead |
| Dedup | Idempotenz bei at-least-once |
| Prefs | Opt-in vor Send |
| Stop | Verlust/Doppel unklar → nicht prod |

## Red Flags

- Queue nur im Speicher
- Keine Dead-Letter
- Opt-in ignoriert
- Doppelte Mails nach Retry
- „Genau einmal“ behauptet ohne Dedup-Beweis

## Resources

- `references/event-notification-checklist.md`
- `scripts/scaffold_event_catalog.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
