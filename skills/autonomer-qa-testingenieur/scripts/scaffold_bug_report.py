#!/usr/bin/env python3
"""Scaffold a structured bug report markdown file.

Usage:
  python scaffold_bug_report.py --out artifacts/qa/bugs --id BUG-001 --title "Login fails"
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

TEMPLATE = """# {id}: {title}

- Created (UTC): {ts}
- Severity: P0/P1/P2/P3
- Status: open
- Environment:
- Build/Commit:

## Summary

## Steps to reproduce

1.
2.
3.

## Expected

## Actual

## Evidence

- Logs:
- Screenshots:
- Test case:

## Suspected area

## Regression test added

- [ ] Yes – path:
- [ ] No – reason:
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
