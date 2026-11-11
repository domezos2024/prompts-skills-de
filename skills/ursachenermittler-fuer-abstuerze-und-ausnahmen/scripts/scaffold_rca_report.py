#!/usr/bin/env python3
"""Scaffold a root-cause analysis report for crashes/exceptions.

Usage:
  python scaffold_rca_report.py --out artifacts/rca --id C1 --title "NullRef in checkout"
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

TEMPLATE = """# RCA {id}: {title}

- Created (UTC): {ts}
- Severity: P0/P1/P2/P3
- Status: investigating
- Version:
- Signature / stack top:
- Do not paste secrets, tokens, or raw PII.

## Impact

## Evidence

- Logs:
- Stacktrace file:
- Metrics/frequency:

## Reproduction

1.
2.
3.

- Determinism: always / intermittent
- Environment:

## Hypotheses

| Hypothesis | Test | Result |
|------------|------|--------|
| | | |

## Root cause

## Fix

- PR/Commit:
- Why this fixes the invariant:

## Regression

- Test path:
- Retest of original steps: Pass/Fail

## Residual risk
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--id", required=True)
    parser.add_argument("--title", required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    safe = "".join(c if c.isalnum() or c in "-_" else "-" for c in args.id)
    path = args.out / f"{safe}-rca.md"
    if not path.exists():
        path.write_text(
            TEMPLATE.format(
                id=args.id,
                title=args.title,
                ts=datetime.now(timezone.utc).isoformat(),
            ),
            encoding="utf-8",
        )
    print(f"Ready: {path.resolve()}")


if __name__ == "__main__":
    main()
