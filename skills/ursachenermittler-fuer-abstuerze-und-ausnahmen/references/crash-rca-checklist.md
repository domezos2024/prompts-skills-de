# Crash / Exception RCA Checklist

Jedes Item: `Pass` | `Fail` | `N/A` + Evidence. Keine Secrets/PII in Artefakten.

## Evidence Pack

- [ ] Stacktrace/Signature gespeichert
- [ ] App-/Runtime-Version notiert
- [ ] Häufigkeit / erster/letzter Seen
- [ ] Betroffene Funktion/User-Impact
- [ ] Logs ohne Secret-Leak kuratiert

## Classification

| ID | Signature | Freq | Severity | Impact area | Repro? |
|----|-----------|------|----------|-------------|--------|
| C1 | | | P0–P3 | | yes/no/flake |

## Reproduction Gate

- [ ] Controlled environment identified
- [ ] Minimal steps written
- [ ] Deterministic or characterized flake
- [ ] Failing test or scripted repro attached

## Root Cause Analysis

- [ ] Failing invariant stated
- [ ] Why now / trigger conditions
- [ ] Concurrency/resources/state considered
- [ ] Rejected alternative hypotheses listed

## Fix Quality

- [ ] Addresses root cause (not only message)
- [ ] No broad swallow of exceptions
- [ ] Regression test added
- [ ] Diagnostics improved without PII/secrets
- [ ] Same repro steps pass after fix

## Anti-Rationalisierung

| Ausrede | Realität |
|---------|----------|
| „try/catch drumherum“ | Root Cause Pflicht |
| „Nur einmal aufgetreten“ | Signature + Telemetrie prüfen |
| „Logging später“ | Diagnose jetzt, aber redaktiert |
| „Nicht repro → closed“ | Open/Blocked mit nächstem Messpunkt |
