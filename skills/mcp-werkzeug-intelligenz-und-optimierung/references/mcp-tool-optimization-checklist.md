# MCP Tool Optimization Checklist

Jedes Item: `Pass` | `Fail` | `N/A` + Beweis.

## Baseline

- [ ] Tool-Katalog mit Descriptions/Schemas erfasst
- [ ] Repräsentative Agenten-Tasks definiert
- [ ] Calls/Task, Fehlerquote, Latenz, Payload-Größe gemessen oder aus Logs abgeleitet
- [ ] Redundante Call-Ketten identifiziert

## Contract Clarity

- [ ] Tool-Namen eindeutig und nicht kollidierend
- [ ] Description sagt Wann/Wann-nicht
- [ ] Required vs optional Felder korrekt
- [ ] Enums/Constraints wo Mehrdeutigkeit war
- [ ] Rückgabeform stabil und dokumentiert

## Efficiency

- [ ] Batch-Endpunkte für Mehrfach-Lookups
- [ ] Pagination/Filter/Field-Selection
- [ ] Keine unnötigen Roundtrips für Metadaten
- [ ] Caching nur mit klarer Invalidierung (falls eingeführt)

## Errors & Safety

- [ ] Strukturierte Fehlercodes
- [ ] AuthZ/Validierung nicht abgeschwächt
- [ ] Idempotenz-Hinweise für Write-Tools
- [ ] Deprecation-Pfad statt stiller Löschung

## Before/After

- [ ] Gleiche Tasks verglichen
- [ ] Qualitätsregression ausgeschlossen
- [ ] Breaking Changes versioniert/kommuniziert
