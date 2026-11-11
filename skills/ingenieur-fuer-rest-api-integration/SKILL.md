---
name: ingenieur-fuer-rest-api-integration
description: Use when integrating an external REST API into an existing app, building a typed client with auth/timeouts/retries, handling pagination/errors/caching, or writing mock and integration tests from real docs - runs discovery against official docs only, client implementation, and validated delivery.
---

# Ingenieur für REST-API-Integration

## Overview

Integriert eine externe REST API **vollständig und zuverlässig** in die bestehende Anwendung. Kernprinzip: **Offizielle Docs → typisierter Client → sichere Credentials/Retries → Mocks + Integrationstests.** Keine erfundenen Endpunkte oder Felder.

## When to Use

- Neue externe REST-API anbinden
- Auth, Rate Limits, Pagination, Fehlercodes klären
- Client von Business-Logik trennen; Caching/Validierung nötig
- Mock- und Integrationstests fehlen

## When NOT to Use

- Event-/Notification-System → `intelligentes-benachrichtigungs-und-ereignisverarbeitungssystem`
- Multi-System-Business-Workflow → `systemuebergreifende-workflow-automatisierung`
- GraphQL/gRPC ohne REST-Anteil (anderen Integrationsskill nutzen)

## Critical Guidelines

- MUST Anforderungen, Architektur und **offizielle** API-Dokumentation analysieren.
- MUST Auth, Limits, Formate, Pagination und Fehlercodes aus Docs ableiten.
- MUST typisierten Client mit klarer Trennung zur Domänelogik bauen.
- MUST Secrets sicher verwalten; Timeouts und Retry nur für idempotente/sichere Fälle.
- MUST Validierung/Transformation; Caching nur mit TTL/Invalidierung.
- NEVER Endpunkte, Felder oder Statuscodes erfinden.
- NEVER Credentials committen oder loggen.
- NEVER unbegrenzte Retries gegen Rate Limits.
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill ingenieur-fuer-rest-api-integration --root .skill-runs/rest-api
```

### PHASE 1 – DISCOVERY

1. Use-Cases, bestehende Auth-/HTTP-Stack, Config-Muster erfassen.
2. Offizielle Docs lesen; Contract-Notiz mit `scripts/scaffold_api_contract.py`.
3. `references/rest-api-integration-checklist.md` abarbeiten.
4. Unklare Docs als Blocker markieren – nicht raten.

**Gate:** API-Contract-Notiz nur aus verifizierten Docs.

### PHASE 2 – PLANNING

1. Client-API (Methoden, DTOs, Error-Typen) spezifizieren.
2. Retry-/Timeout-/Idempotency-Policy; Auth-Token-Refresh.
3. Mapping auf Domänenmodelle; Cache-Strategie falls nötig.
4. Testplan: Mock unit + Integration (sandbox/real).

**Gate:** Plan mit Akzeptanzkriterien und Rollback.

### PHASE 3 – IMPLEMENTATION

1. Typed Client + Auth-Adapter + Error-Normalisierung.
2. Pagination-Helfer; Validierung der Responses.
3. Integration in App-Flows; Observability (correlation id, status, latency).
4. Config/Docs für Wartung.

**Gate:** Happy Path gegen Mock oder Sandbox belegt.

### PHASE 4 – VALIDATION

1. Mock-Tests für Erfolg und Fehlerantworten.
2. Integrationstests wo Zugang erlaubt; Rate-Limit-Verhalten prüfen.
3. Secret-Scan der Diffs; keine Leaks.
4. Regressions in abhängigen Flows fixen.

**Gate:** Testprotokoll ohne erfundene API-Shapes.

### PHASE 5 – DELIVERY

1. Delivery Report; Betriebs-/Wartungshinweise.
2. Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/rest-api --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Wahrheit | Nur offizielle Docs |
| Client | Typed + getrennt von Domain |
| Safety | Secrets, Timeouts, begrenzte Retries |
| Tests | Mock + Integration |
| Stop | Unklar in Docs → Blocker, nicht erfinden |

## Red Flags

- „Laut Erfahrung hat die API Feld X“
- Retries auf POST ohne Idempotency-Key
- Tokens in Logs
- Pagination ignoriert
- Fertig ohne Fehlerpfad-Tests

## Resources

- `references/rest-api-integration-checklist.md`
- `scripts/scaffold_api_contract.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
