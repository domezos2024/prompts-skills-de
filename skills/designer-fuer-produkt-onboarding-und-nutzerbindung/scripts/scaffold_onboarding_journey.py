#!/usr/bin/env python3
"""Scaffold onboarding journey map and test scenarios.

Usage:
  python scaffold_onboarding_journey.py --out artifacts/onboarding
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

JOURNEY = """# Onboarding Journey Map

- Created (UTC): {ts}
- First-value action:
- Persona:

## Current path

| Step | Screen/Action | Required? | Friction | Severity |
|------|---------------|-----------|----------|----------|
| 1 | | | | P0/P1/P2/P3 |
| 2 | | | | |
| 3 | | | | |

## Target path

| Step | Screen/Action | Goal | Acceptance |
|------|---------------|------|------------|
| 1 | | | |
| 2 | | | |

## Hypotheses & metrics

| Hypothesis | Metric | Privacy notes |
|------------|--------|---------------|
| | | |
"""

SCENARIOS = """# First-user test scenarios

| ID | Scenario | Steps | Expected | Result | Evidence |
|----|----------|-------|----------|--------|----------|
| S1 | Happy path to first value | | | | |
| S2 | Skip optional setup | | | | |
| S3 | Invalid input / error | | | | |
| S4 | Empty state entry | | | | |
| S5 | Return visit (day 2) | | | | |
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).isoformat()
    for name, body in (("journey-map.md", JOURNEY), ("test-scenarios.md", SCENARIOS)):
        path = args.out / name
        if not path.exists():
            path.write_text(body.format(ts=ts), encoding="utf-8")
    print(f"Ready: {args.out.resolve()}")


if __name__ == "__main__":
    main()
