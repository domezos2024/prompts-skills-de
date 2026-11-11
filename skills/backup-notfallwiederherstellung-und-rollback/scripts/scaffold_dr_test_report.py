#!/usr/bin/env python3
"""Scaffold DR/backup test report template.

Usage:
  python scaffold_dr_test_report.py --out artifacts/backup-dr --rpo 24h --rto 4h
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

TEMPLATE = """# DR Test Report

- Created (UTC): {ts}
- Target RPO: {rpo}
- Target RTO: {rto}
- Environment (must be isolated unless user approved prod):

## Assets in scope

| Asset | Location | Consistency notes |
|-------|----------|-------------------|
| | | |

## Backup run

| Job | Started | Finished | Size/Hash | Result |
|-----|---------|----------|-----------|--------|
| | | | | |

## Restore run

| Step | Result | Duration | Evidence |
|------|--------|----------|----------|
| | | | |

## Measured vs targets

- Achieved RPO evidence:
- Achieved RTO evidence:
- Gaps:

## Approvals

- [ ] User approval recorded for any prod-impacting restore
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--rpo", default="TBD")
    parser.add_argument("--rto", default="TBD")
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    path = args.out / "DR_TEST_REPORT.md"
    if not path.exists():
        path.write_text(
            TEMPLATE.format(
                ts=datetime.now(timezone.utc).isoformat(),
                rpo=args.rpo,
                rto=args.rto,
            ),
            encoding="utf-8",
        )
    print(f"Ready: {args.out.resolve()}")


if __name__ == "__main__":
    main()
