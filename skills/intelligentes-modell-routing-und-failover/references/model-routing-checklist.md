# Model Routing & Failover Checklist

Jedes Item: `Pass` | `Fail` | `N/A` + Beweis.

## Inventar (nur Verifiziertes)

- [ ] API/CLI-Endpunkt erreichbar oder explizit als unavailable markiert
- [ ] Auth-Methode getestet (ohne Secret-Leak)
- [ ] Modelle/Capabilities gelistet
- [ ] Rate limits, quotas, pricing, ToS-Grenzen dokumentiert

## Adapter-Vertrag

- [ ] Einheitliche Request/Response-Typen
- [ ] Error-Normalisierung (rate_limit, timeout, unavailable, auth, content_filter)
- [ ] Timeout-Defaults und Cancel-Support
- [ ] Keine provider-spezifischen Leaks in Caller-Code (außer Policy-Hints)

## Routing & Failover

- [ ] Task-type → priority list konfigurierbar
- [ ] Cooldown nach rate_limit
- [ ] Budget-/Token-Caps enforced
- [ ] Kein Fallback auf nicht inventarisierte Provider
- [ ] ToS-konforme Region/Model-Wahl

## Checkpoints & Idempotenz

- [ ] Kompakter Task-Checkpoint vor/nach Modellcalls
- [ ] Context-Pack für Handoff definiert
- [ ] Tool-Effect-IDs verhindern Doppelausführung

## Observability & Safety

- [ ] Usage/Cost-Logs ohne Secrets/PII-Rohdaten
- [ ] Latency und Error-Class metrisiert
- [ ] Failover-Ereignisse auditierbar
