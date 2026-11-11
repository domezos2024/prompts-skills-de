#!/usr/bin/env python3
"""Scaffold accessibility test report.

Usage:
  python scaffold_a11y_report.py --out artifacts/a11y
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

TEMPLATE = """# Accessibility Report

- Created (UTC): {ts}
- Scope / URLs:
- Target guidance (e.g. WCAG 2.2 AA):
- Tools:

## Inventory

| Template/Component | Interactive? | Critical flow |
|--------------------|--------------|---------------|
| | | |

## Findings

| ID | WCAG-ish | Severity | Description | Evidence | Status |
|----|----------|----------|-------------|----------|--------|
| | | P0/P1/P2/P3 | | | |

## Manual tests

| Flow | Keyboard | Screen reader | Viewport | Pass? |
|------|----------|---------------|----------|-------|
| | | | | |

## Statement

Automated scores alone do **not** prove conformance. Remaining barriers are listed above.
Live deploy requires explicit user approval.
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    path = args.out / "A11Y_REPORT.md"
    if not path.exists():
        path.write_text(
            TEMPLATE.format(ts=datetime.now(timezone.utc).isoformat()),
            encoding="utf-8",
        )
    print(f"Ready: {args.out.resolve()}")


if __name__ == "__main__":
    main()
