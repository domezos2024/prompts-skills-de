# Reliability & Fault Recovery Matrix

Jedes Ergebnis: `Pass` | `Fail` | `N/A` + Metrik/Evidence. **Kein Prod-Chaos ohne Freigabe.**

## Dependencies

| ID | Dependency | Failure modes | Timeout today | Retry/Backoff | Breaker | Idempotent client? |
|----|------------|---------------|---------------|---------------|---------|-------------------|
| D1 | | down/slow/reset | | | | |

## Fault Drill Plan

| Drill | Environment | Inject | Expected app behavior | Integrity check | Recovery metric | Result |
|-------|-------------|--------|----------------------|-----------------|-----------------|--------|
| T1 | lab/stage | dependency timeout | | | | |
| T2 | lab/stage | dependency down | | | | |
| T3 | lab/stage | connection reset | | | | |
| T4 | lab/stage | process restart mid-request | | | | |
| T5 | lab/stage | slow dependency | | | | |

## Hardening Checklist

- [ ] Timeouts an allen Remote-Calls gesetzt
- [ ] Retry nur für idempotente/safe Ops; Budget + Jitter
- [ ] Circuit Breaker / fail-fast wo sinnvoll
- [ ] Queue/Outbox oder Idempotency-Keys gegen Duplikate
- [ ] Graceful shutdown / drain
- [ ] Backup/Rollback vor destruktiven Lab-Schritten

## SPOF / Residual

| Component | SPOF? | Mitigation / accepted risk |
|-----------|-------|----------------------------|
| | | |

## Anti-Rationalisierung

| Ausrede | Realität |
|---------|----------|
| „Prod ist realistischer“ | Ohne Fenster verboten |
| „Retry härter = robuster“ | Storm-Risiko; Caps Pflicht |
| „Wieder da = Erfolg“ | Recovery-Zeit + Integrität messen |
| „Einmal manuell getestet“ | Automatisieren wo möglich |
