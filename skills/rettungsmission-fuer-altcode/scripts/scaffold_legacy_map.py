#!/usr/bin/env python3
"""Scaffold legacy mapping docs: entry points, risks, and characterization plan.

Usage:
  python scaffold_legacy_map.py --out artifacts/legacy-map
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

MAP = """# Legacy System Map

- Created (UTC): {ts}
- App / repo:
- Suspected runtime:

## Entry points

| Name | How to start | Path | Status | Notes |
|------|--------------|------|--------|-------|
| | | | unknown/broken/ok | |

## Top data flows

1.
2.
3.

## Config sources

| Source | Path / key pattern | Required? | Notes |
|--------|--------------------|-----------|-------|
| | | | |

## Risk register

| ID | Severity | Description | Evidence | Next step |
|----|----------|-------------|----------|-----------|
| | P0/P1/P2/P3 | | | |
"""

CHARS = """# Characterization Test Plan

- Created (UTC): {ts}

| Flow | Behavior to freeze | Test type | Owner file | Status |
|------|--------------------|-----------|------------|--------|
| | | | | planned |

## Build reproduction

- [ ] Documented in BUILD.md
- [ ] Verified on clean environment
"""

BUILD = """# BUILD (Legacy Rescue)

- Created (UTC): {ts}

## Prerequisites

-

## Steps

1.
2.

## Verify

- Command:
- Expected:
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).isoformat()
    for name, content in (
        ("SYSTEM_MAP.md", MAP),
        ("CHARACTERIZATION_PLAN.md", CHARS),
        ("BUILD.md", BUILD),
    ):
        path = args.out / name
        if not path.exists():
            path.write_text(content.format(ts=ts), encoding="utf-8")
    print(f"Ready: {args.out.resolve()}")


if __name__ == "__main__":
    main()
