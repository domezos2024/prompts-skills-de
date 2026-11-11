# Cross-System Workflow Checklist

Jedes Item: `Pass` | `Fail` | `N/A` + Beweis.

## Ist-Prozess

- [ ] Schritte, Akteure, Systeme, Artefakte dokumentiert
- [ ] Medienbrüche und manuelle Copy-Paste-Punkte markiert
- [ ] Fehlerquellen und heutige Workarounds erfasst
- [ ] SLA / Häufigkeit / Volumen bekannt

## Design

- [ ] Trigger klar (Zeit/Event/Webhook/Manual)
- [ ] Schrittverträge (Input/Output/Errors)
- [ ] Idempotenz-Schlüssel je externem Write
- [ ] Persistenter State + Dead-letter
- [ ] Dry-Run / Approval für kritische Changes

## Integrationen

- [ ] Auth und Secrets sicher
- [ ] Timeouts/Retries budgetiert
- [ ] Partial-failure-Verhalten definiert
- [ ] Observability: run_id, step, external_ids

## Tests & Betrieb

- [ ] E2E mit isolierten Testdaten
- [ ] Doppeltrigger-/Retry-Test ohne Doppelwirkung
- [ ] Runbook: Start/Stop/Replay
- [ ] Voraussetzungen und Rollback dokumentiert
