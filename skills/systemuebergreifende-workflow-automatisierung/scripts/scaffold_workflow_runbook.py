#!/usr/bin/env python3
"""Scaffold cross-system workflow runbook and idempotency map.

Usage:
  python scaffold_workflow_runbook.py --out artifacts/cross-system-runbook.md
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

TEMPLATE = """# Cross-System Workflow Runbook

- Created (UTC): {ts}
- Workflow name:
- Environments: dev/test/prod

## As-Is Steps

| # | Actor | System | Action | Pain / risk |
|---|-------|--------|--------|-------------|
| 1 | | | | |

## To-Be Flow

| Step | Trigger/dep | Integration | Idempotency key | Approval | State |
|------|-------------|-------------|-----------------|----------|-------|
| | | | | yes/no | |

## Controls

- Dry-run flag:
- Kill switch:
- Dedup store:
- DLQ / replay:

## E2E Test Data

| Case | Systems touched | Expected | Result |
|------|-----------------|----------|--------|
| happy | | | |
| retry storm | | no duplicate writes | |
| partial failure | | | |

## Ops

- How to start/stop:
- How to replay a run:
- Rollback:
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    if not args.out.exists():
        args.out.write_text(
            TEMPLATE.format(ts=datetime.now(timezone.utc).isoformat()),
            encoding="utf-8",
        )
    print(f"Ready: {args.out.resolve()}")


if __name__ == "__main__":
    main()
