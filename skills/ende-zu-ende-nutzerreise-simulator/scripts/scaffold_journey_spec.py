#!/usr/bin/env python3
"""Scaffold an E2E journey specification markdown.

Usage:
  python scaffold_journey_spec.py --out artifacts/e2e/journeys --id J1 --title "Checkout"
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

TEMPLATE = """# Journey {id}: {title}

- Created (UTC): {ts}
- Priority: P0/P1/P2/P3
- Role(s):
- Viewport(s):
- Isolated data set:
- Side-effect guards confirmed: yes/no

## Goal

## Steps

1.
2.
3.

## Expected result

## Negative / interrupt cases

| Case | Steps | Expected |
|------|-------|----------|
| invalid input | | |
| mid-flow refresh | | |
| double submit | | |

## Checkpoints

| Name | Assertion | Screenshot |
|------|-----------|------------|
| entry | | |
| critical | | |
| done | | |

## Automation notes

- Framework:
- Spec file:
- Last run result:
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
