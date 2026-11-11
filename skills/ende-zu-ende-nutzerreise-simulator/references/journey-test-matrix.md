# E2E Nutzerreise-Matrix

Jedes Ergebnis: `Pass` | `Fail` | `Blocked` | `Skipped` + Evidence (Trace/Screenshot).

## Journey Backlog

| ID | Journey | Role | Priority | Data set | Happy | Validation | Interrupt/Retry | Mobile | Desktop | Evidence |
|----|---------|------|----------|----------|-------|------------|-----------------|--------|---------|----------|
| J1 | | | P0–P3 | isolated | | | | | | |

## Checkpoint Plan

| Journey | Checkpoint | Assertion | Screenshot path |
|---------|------------|-----------|-----------------|
| | Entry | | |
| | Mid critical step | | |
| | Success / terminal error | | |

## Side-Effect Guards

- [ ] Keine echten Payments/Käufe
- [ ] Keine echten Outbound-Messages an Kunden
- [ ] Testuser/Tenant isoliert
- [ ] Cleanup/Reset nach Suite definiert

## Anti-Rationalisierung

| Ausrede | Realität |
|---------|----------|
| „Ein Browser reicht“ | Viewports laut Plan |
| „Screenshot später“ | Checkpoint ohne Evidence = Fail |
| „Prod-Daten realistischer“ | Isolierte Daten Pflicht |
| „Flaky CI, lokal grün“ | Als unsicher dokumentieren |
