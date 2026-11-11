# REST API Integration Checklist

Jedes Item: `Pass` | `Fail` | `N/A` + Beweis (Doc-URL/Datei/Test).

## Discovery

- [ ] Offizielle Basis-URL(s) und Versionierung
- [ ] Auth-Flow (API key/OAuth/mTLS) dokumentiert und getestet
- [ ] Rate Limits und Quota-Header verstanden
- [ ] Pagination-Schema (cursor/offset) aus Docs
- [ ] Fehlercode-/Problem-Details-Format aus Docs
- [ ] Keine erfundenen Felder in DTOs

## Client-Vertrag

- [ ] Typisierte Request/Response-Modelle
- [ ] Trennung Client ↔ Domain-Services
- [ ] Timeouts gesetzt
- [ ] Retry nur retryable + budgetiert; Idempotency-Key wo nötig
- [ ] Token-Refresh/Expiry behandelt

## Daten & Cache

- [ ] Response-Validierung vor Domänennutzung
- [ ] Transformation dokumentiert
- [ ] Cache TTL/Invalidierung oder bewusst kein Cache

## Observability & Safety

- [ ] Correlation-/Request-IDs
- [ ] Latenz/Status metrisiert oder geloggt
- [ ] Secrets nicht geloggt/committet
- [ ] PII-Minimierung in Logs

## Tests

- [ ] Mock: 2xx, 4xx, 5xx, timeout
- [ ] Pagination-Edge-Cases
- [ ] Integration gegen Sandbox/erlaubte Umgebung
- [ ] App-Flow-Regression
