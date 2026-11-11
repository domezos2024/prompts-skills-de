#!/usr/bin/env python3
"""Scaffold conversion audit notes and measurement plan stubs.

Usage:
  python scaffold_conversion_notes.py --out artifacts/conversion-baseline
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

NOTES = """# Conversion Audit Notes

- Created (UTC): {ts}
- Page type (landing/signup/download/checkout):
- Primary CTA:
- Audience:

## Current funnel hurdles

| Step | Friction | Severity | Evidence |
|------|----------|----------|----------|
| | | P0/P1/P2/P3 | |

## Hypotheses (not results)

| ID | Change | Expected effect | How to measure |
|----|--------|-----------------|----------------|
| H1 | | | |

## Measurement plan

| Metric | Definition | Source | Baseline | Target (optional) | Notes |
|--------|------------|--------|----------|-------------------|-------|
| | | | unknown/known | | Do not invent lifts |

## Dark-pattern review

- [ ] Reviewed – no dark patterns introduced
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    path = args.out / "CONVERSION_NOTES.md"
    if not path.exists():
        path.write_text(
            NOTES.format(ts=datetime.now(timezone.utc).isoformat()),
            encoding="utf-8",
        )
    print(f"Ready: {args.out.resolve()}")


if __name__ == "__main__":
    main()
