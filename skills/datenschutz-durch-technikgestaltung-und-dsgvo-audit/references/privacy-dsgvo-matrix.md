# Privacy / DSGVO Technical Matrix

Jedes Item: `Pass` | `Fail` | `N/A` | `Legal-Review` + Evidence.  
**Hinweis:** Technische Prüfung ≠ verbindliche Rechtsberatung.

## Dateninventar

| ID | Datenkategorie | Zweck | Rechtsgrundlage (falls bekannt) | Speicher | Retention | Empfänger | Minimierbar? |
|----|----------------|-------|----------------------------------|----------|-----------|-----------|--------------|
| D1 | | | | | | | |

## Datenflüsse

| From | To | Mechanism | PII | Encrypted in transit | Encrypted at rest | Notes |
|------|-----|-----------|-----|----------------------|-------------------|-------|
| | | | | | | |

## Betroffenenrechte (technisch)

- [ ] Einwilligung einholen und speichern (nachvollziehbar)
- [ ] Widerruf wirkt auf nachfolgende Verarbeitung
- [ ] Auskunft/Export der relevanten Daten möglich
- [ ] Löschung/Anonymisierung inkl. abhängiger Systeme geplant
- [ ] Ablehnungspfad ohne Dark Patterns getestet

## Logging & Observability

- [ ] Keine Secrets in Logs
- [ ] PII in Logs minimiert/redaktiert
- [ ] Error-Payloads ohne unnötige Personendaten
- [ ] Analytics-Events datensparsam

## Drittanbieter

- [ ] Liste aller Processor/Subprocessor im Scope
- [ ] Transfers und Zwecke dokumentiert
- [ ] Opt-out/Consent-Gate wo technisch vorgesehen
- [ ] Keine ungeplanten Beacons/Tracker im Build

## Speicherung & Minimierung

- [ ] Default: nur notwendige Felder
- [ ] Soft-Delete vs. Hard-Delete dokumentiert
- [ ] Backup-/Queue-Restlaufzeiten bedacht
- [ ] Test-/Staging-Daten anonymisiert oder synthetisch

## Testmatrix Privacy-Flows

| Flow | Happy | Deny/Reject | Withdraw | Evidence |
|------|-------|-------------|----------|----------|
| Consent | | | | |
| Export | | | | |
| Erasure | | | | |

## Anti-Rationalisierung

| Ausrede | Realität |
|---------|----------|
| „Marketing braucht alle Felder“ | Zweck + Minimierung nachweisen |
| „Löschen = User.deactivated=true“ | Storage/Queues/Backups prüfen |
| „Wir sind DSGVO-konform“ | Nur technische Measures melden |
| „Logs sind intern“ | PII-Redaction trotzdem Pflicht |
