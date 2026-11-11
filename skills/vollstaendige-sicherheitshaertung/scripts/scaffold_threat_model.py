#!/usr/bin/env python3
"""Scaffold a threat-model markdown for security hardening runs.

Usage:
  python scaffold_threat_model.py --out artifacts/security/threat-model.md
  python scaffold_threat_model.py --out artifacts/security/threat-model.md --app "MyApp"
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

TEMPLATE = """# Threat Model – {app}

- Created (UTC): {ts}
- Authorized scope:
- Environment (dev/stage/lab – never silent prod chaos):
- Analyst:

## Assets

| ID | Asset | Data sensitivity | Trust boundary |
|----|-------|------------------|----------------|
| A1 | | | |

## Entry points

| ID | Entry | Auth required | Notes |
|----|-------|---------------|-------|
| E1 | | | |

## Actors

| ID | Actor | Capabilities |
|----|-------|--------------|
| T1 | Anonymous | |
| T2 | Authenticated user | |
| T3 | Privileged / admin | |

## Risks (prioritized)

| ID | Threat | Asset | Likelihood | Impact | Severity | Proposed control | Status |
|----|--------|-------|------------|--------|----------|------------------|--------|
| R1 | | | | | P0/P1/P2/P3 | | open |

## Hardening packages

| Package | Controls | Acceptance test | Rollback |
|---------|----------|-----------------|----------|
| | | | |

## Retest log

| Risk ID | Test | Result | Evidence |
|---------|------|--------|----------|
| | | Pass/Fail | |

## Residual risks

| ID | Description | Owner / next step |
|----|-------------|-------------------|
| | | |
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--app", default="Application")
    args = parser.parse_args()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    if not args.out.exists():
        args.out.write_text(
            TEMPLATE.format(app=args.app, ts=datetime.now(timezone.utc).isoformat()),
            encoding="utf-8",
        )
    print(f"Ready: {args.out.resolve()}")


if __name__ == "__main__":
    main()
