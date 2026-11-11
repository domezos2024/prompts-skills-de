# QA Test Matrix

Jedes Ergebnis: `Pass` | `Fail` | `Blocked` | `Skipped` + Evidence.

## Risikobasierte Flows

| ID | Flow | Risk (P0–P3) | Unit | Integration | E2E/UI | Exploratory | Owner |
|----|------|--------------|------|-------------|--------|-------------|-------|
| F1 | | | | | | | |

## Case-Typen pro Flow

| Flow | Happy | Validation | AuthZ | Edge/Empty | Error handling | Evidence |
|------|-------|------------|-------|------------|----------------|----------|
| | | | | | | |

## Defect Severity Gate

| Sev | Bedeutung | Exit-Regel |
|-----|-----------|------------|
| P0 | Blocker/Datenverlust/Security | Muss fix oder offizieller Blocker |
| P1 | Kernfunktion gebrochen | Muss fix oder akzeptiertes Risiko |
| P2 | Workaround möglich | Dokumentieren + optional fix |
| P3 | Kosmetik | Backlog |

## Anti-Rationalisierung

| Ausrede | Realität |
|---------|----------|
| „Build war grün gestern“ | Heute erneut laufen lassen |
| „Offensichtlich kaputt, kein Repro nötig“ | Ohne Repro kein stabiler Fix |
| „E2E deckt Unit ab“ | Schichten ergänzen, nicht ersetzen |
| „Flaky aber meist grün“ | Nicht als Pass melden |
