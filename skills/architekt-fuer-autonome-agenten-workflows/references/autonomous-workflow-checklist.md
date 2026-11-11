# Autonomer Agenten-Workflow Checklist

Jedes Item: `Pass` | `Fail` | `N/A` + Beweis.

## Zerlegung & Verträge

- [ ] Atomare Schritte mit Input/Output-Schema
- [ ] Abhängigkeiten und Parallelitätsgrenzen klar
- [ ] Akzeptanzkriterien je Schritt messbar

## Zustand & Checkpoints

- [ ] Explizite States (z. B. planned/running/waiting_approval/succeeded/failed/compensating)
- [ ] Persistenter Checkpoint nach jedem erfolgreichen Schritt
- [ ] Inputs-Hash / Effect-IDs gespeichert
- [ ] Resume lädt letzten gültigen Checkpoint

## Idempotenz & Safety

- [ ] Side-Effects mit Dedup-Schlüssel
- [ ] Approval-Gate für irreversible Aktionen
- [ ] Timeout + Retry-Budget + Dead-letter/Fail-stop
- [ ] Compensating Action oder klarer Manual-Runbook-Pfad

## Observability

- [ ] Strukturierte Statusmeldungen (phase/step/status)
- [ ] Fehlerklassifikation (retryable vs fatal)
- [ ] Trace-/Run-ID durchgängig

## Recovery-Tests

- [ ] Kill während Step → sauberer Resume
- [ ] Doppelter Resume → keine doppelten Effects
- [ ] Approval-Reject-Pfad
- [ ] Exhausted-Retry-Pfad
