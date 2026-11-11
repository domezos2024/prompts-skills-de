# Event & Notification System Checklist

Jedes Item: `Pass` | `Fail` | `N/A` + Beweis.

## Event-Vertrag

- [ ] Ereignistypen, Payload-Schema, Priorität definiert
- [ ] Eindeutige `event_id` / Idempotenzschlüssel
- [ ] Producer und Schema-Version dokumentiert
- [ ] PII-Minimierung im Payload

## Queue & State

- [ ] Persistente Queue/Outbox
- [ ] States: pending/processing/sent/failed/dead (oder äquivalent)
- [ ] At-least-once Verarbeitung + Dedup auf Notification-Ebene
- [ ] Visibility timeout / lease gegen Doppelworker-Kollisionen

## Delivery

- [ ] Retry + exponentielles Backoff + Max-Attempts
- [ ] Dead-letter + Replay-Pfad
- [ ] Kanaladapter mit Timeout und Fehlerklassifikation
- [ ] Zustellstatus auditierbar

## Preferences & Safety

- [ ] Opt-in/Opt-out je Kanal geprüft vor Send
- [ ] Quiet hours / Rate limits wo gefordert
- [ ] Keine Secrets in Notification-Bodies/Logs

## Tests

- [ ] Duplicate event → eine logische Notification
- [ ] Worker crash mid-send → sichere Fortsetzung
- [ ] Provider down → retry dann DLQ
- [ ] Opt-out → kein Send
