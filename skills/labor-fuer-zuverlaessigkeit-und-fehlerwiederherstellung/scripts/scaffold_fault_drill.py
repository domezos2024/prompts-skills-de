#!/usr/bin/env python3
"""Scaffold a fault-injection drill report for reliability lab work.

Usage:
  python scaffold_fault_drill.py --out artifacts/reliability/drills --id T1 --title "API timeout"
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

TEMPLATE = """# Fault Drill {id}: {title}

- Created (UTC): {ts}
- Environment: lab/stage (prod only with approved window)
- Dependency under test:
- Authorization / window notes:

## Injection method

- How fault is introduced:
- Duration:
- Traffic profile:

## Expected behavior

- User-visible:
- Internal (retry/breaker/degrade):

## Observations

| Time | Signal | Value |
|------|--------|-------|
| | success rate | |
| | p95 latency | |
| | error class | |
| | recovery time | |

## Integrity checks

- [ ] No duplicate side effects (or explained/compensated)
- [ ] No data corruption
- [ ] Compensating transactions / idempotency verified

## Hardening follow-ups

| Gap | Fix | Status |
|-----|-----|--------|
| | | |

## Result

- Pass/Fail:
- Residual SPOF:
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--id", required=True)
    parser.add_argument("--title", required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    safe = "".join(c if c.isalnum() or c in "-_" else "-" for c in args.id)
    path = args.out / f"{safe}.md"
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
