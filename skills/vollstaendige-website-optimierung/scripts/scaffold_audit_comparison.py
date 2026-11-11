#!/usr/bin/env python3
"""Scaffold before/after website audit comparison notes.

Usage:
  python scaffold_audit_comparison.py --out artifacts/website-opt
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

TEMPLATE = """# Website Audit Comparison

- Created (UTC): {ts}
- Site / entry URL:
- Tools used (Lighthouse, axe, link checker, …):

## Inventory

| Page/Template | Priority | Notes |
|---------------|----------|-------|
| | | |

## Baseline

| Page | Perf | SEO | A11y | BP | Evidence |
|------|------|-----|------|----|----------|
| | | | | | |

## After

| Page | Perf | SEO | A11y | BP | Evidence |
|------|------|-----|------|----|----------|
| | | | | | |

## Changes shipped

| ID | Prio | Change | Result |
|----|------|--------|--------|
| | | | |

## Claims policy

- Do not claim ranking improvements without Search Console / ranking data.
- Live deploy requires explicit user approval.
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "baseline").mkdir(exist_ok=True)
    (args.out / "after").mkdir(exist_ok=True)
    path = args.out / "COMPARISON.md"
    if not path.exists():
        path.write_text(
            TEMPLATE.format(ts=datetime.now(timezone.utc).isoformat()),
            encoding="utf-8",
        )
    print(f"Ready: {args.out.resolve()}")


if __name__ == "__main__":
    main()
