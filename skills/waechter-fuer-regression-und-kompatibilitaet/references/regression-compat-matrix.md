# Regression & Kompatibilitäts-Matrix

Jedes Ergebnis: `Pass` | `Fail` | `NotRun` | `Unsupported` + Evidence.

## Change Impact

| Change area | Direct modules | Downstream dependents | Risk | Required tests |
|-------------|----------------|------------------------|------|----------------|
| | | | P0–P3 | |

## Compatibility Matrix

| OS | Browser/Runtime | Version | Smoke | Critical flows | Notes | Evidence |
|----|-----------------|---------|-------|----------------|-------|----------|
| | | | | | | |

## Regression Suite Status

| Suite | Command | Result | Duration | Evidence |
|-------|---------|--------|----------|----------|
| | | | | |

## Classification Rules

| Signal | Treat as |
|--------|----------|
| Fail after related code change, repro local | Confirmed regression |
| Fail only on missing browser binary | Environment gap (`NotRun`) |
| Intermittent without code signal | Flake (not Pass) |
| Outside support policy | `Unsupported` |

## Anti-Rationalisierung

| Ausrede | Realität |
|---------|----------|
| „CI grün = alle Browser“ | Nur gelistete Targets zählen |
| „Kleine Diff, kein Test“ | Impact-Analyse trotzdem |
| „Unsupported aber ok“ | Als Unsupported markieren, nicht Pass |
| „Einmal geredet, reicht“ | Evidence speichern |
