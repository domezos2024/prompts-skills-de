# Project Audit Priority Matrix

## Evidence classes

| Class | Meaning | Allowed actions |
|-------|---------|-----------------|
| Confirmed | Reproduced or directly observed in code/build/tests | Fix / schedule |
| Hypothesis | Plausible but not verified | Investigate task only |
| Unknown | Not checked | Explicitly mark untested |

## Finding row template

| ID | Area | Finding | Evidence class | Evidence | Severity P0-P3 | Effort | Benefit | Deps | Wave | Status |
|----|------|---------|----------------|----------|----------------|--------|---------|------|------|--------|
| A01 | | | Confirmed/Hypothesis/Unknown | path/log | | S/M/L | | | W0/W1/… | open |

## Waves

- **W0 Quick Wins:** low risk, high confidence, small effort
- **W1:** important fixes needing short prep
- **W2:** structural / multi-module
- **W3:** optional / long-term

## Done rule

A roadmap item is `done` only if implemented **and** validated (or blocked with next step).
