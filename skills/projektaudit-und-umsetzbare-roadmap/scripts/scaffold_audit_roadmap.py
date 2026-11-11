#!/usr/bin/env python3
"""Scaffold project audit + roadmap artifacts.

Usage:
  python scaffold_audit_roadmap.py --out artifacts/projektaudit
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

AUDIT = """# Project audit

- Created (UTC): {ts}
- Repo:
- Stack:
- Build baseline:
- Test baseline:

## Findings

| ID | Area | Finding | Evidence class | Evidence | P | Effort | Benefit | Deps | Wave | Status |
|----|------|---------|----------------|----------|---|--------|---------|------|------|--------|
| A01 | | | Confirmed | | P1 | S | | | W0 | open |

## Notes

- Confirmed vs Hypothesis vs Unknown must stay strict.
"""

ROADMAP = """# Actionable roadmap

## W0 – Quick wins

| ID | Task | Acceptance criteria | Status | Validation |
|----|------|---------------------|--------|------------|
| | | | | |

## W1 – Near term

| ID | Task | Acceptance criteria | Status | Validation |
|----|------|---------------------|--------|------------|
| | | | | |

## W2 – Structural

| ID | Task | Acceptance criteria | Status | Validation |
|----|------|---------------------|--------|------------|
| | | | | |

## Blockers / prep work

| ID | Blocker | Needed before | Next step |
|----|---------|---------------|-----------|
| | | | |
"""

VAL = """# Validation log

| Change / task | Command or check | Result | Notes |
|---------------|------------------|--------|-------|
| | | Pass/Fail/Skipped | |
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).isoformat()
    for name, body in (
        ("AUDIT.md", AUDIT),
        ("ROADMAP.md", ROADMAP),
        ("validation-log.md", VAL),
    ):
        path = args.out / name
        if not path.exists():
            path.write_text(body.format(ts=ts), encoding="utf-8")
    print(f"Ready: {args.out.resolve()}")


if __name__ == "__main__":
    main()
