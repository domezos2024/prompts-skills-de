#!/usr/bin/env python3
"""Scaffold master orchestration activation plan.

Usage:
  python scaffold_activation_plan.py --out artifacts/master-orchestration
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

PLAN = """# Master activation plan

- Created (UTC): {ts}
- Project path:
- Overall goal:

## Activated workflows

| # | Prompt/Title | Skill path | Depends on | Write scope | Approval gates | Status |
|---|--------------|------------|------------|-------------|----------------|--------|
| 1 | | | | | none/publish/pay/git | planned |

## Execution order

1.
2.
3.

## Shared baselines

- Build:
- Tests:
- Risks:

## Out of scope

-

## Status line template

`STATUS: PHASE {{N}} – {{Name}} | Workflow {{i}}/{{n}}: {{skill}} | Last validation: Pass|Fail|Skipped`
"""

VAL = """# Cross-cutting validation log

| Check | Related workflows | Result | Evidence |
|-------|-------------------|--------|----------|
| Build | | | |
| Tests | | | |
| UI smoke | | | |
| Docs consistency | | | |
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).isoformat()
    for name, body in (("activation-plan.md", PLAN), ("validation-log.md", VAL)):
        path = args.out / name
        if not path.exists():
            path.write_text(body.format(ts=ts), encoding="utf-8")
    print(f"Ready: {args.out.resolve()}")


if __name__ == "__main__":
    main()
