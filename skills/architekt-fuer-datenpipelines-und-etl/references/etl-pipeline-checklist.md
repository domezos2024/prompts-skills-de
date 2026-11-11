# ETL / Data Pipeline Checklist

Jedes Item: `Pass` | `Fail` | `N/A` + Beweis.

## Quellen & Modell

- [ ] Quellen, Formate, Refresh-Intervalle erfasst
- [ ] PII-/Sensitivitätsklassifikation
- [ ] Kanonisches Zielschema versioniert
- [ ] Mapping Quelle → Ziel dokumentiert
- [ ] Originale unverändert (außer explizit gefordert)

## Pipeline-Vertrag

- [ ] Extract/Transform/Load Schritte getrennt und nachvollziehbar
- [ ] Incremental Key / Watermark definiert
- [ ] Idempotente Re-Runs (Upsert/Partition-Replace)
- [ ] Checkpoints für Wiederanlauf
- [ ] Quarantäne für invalid records

## Datenqualität

- [ ] Vollständigkeit (row counts / required fields)
- [ ] Uniqueness wo business key gilt
- [ ] Referentielle Integrität / Domain-Checks
- [ ] DQ-Gate blockt Publish bei Fail

## Observability & Safety

- [ ] Lineage (source → transform → sink)
- [ ] Metriken: in/out/quarantine/lag
- [ ] Keine PII in Klartext-Logs
- [ ] Zugriffsbeschränkung auf Outputs

## Tests

- [ ] Sample happy path
- [ ] Restart mid-run
- [ ] Partial source failure
- [ ] Repeated run ohne Duplikate
