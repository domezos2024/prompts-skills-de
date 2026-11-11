#!/usr/bin/env python3
"""Create a filled-out-ready viewport test matrix markdown for a run.

Usage:
  python scaffold_viewport_matrix.py --out artifacts/mobile-baseline/VIEWPORT_MATRIX.md
  python scaffold_viewport_matrix.py --out artifacts/mobile-after/VIEWPORT_MATRIX.md --title "After"
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

TEMPLATE = """# {title} – Viewport Matrix

- Created (UTC): {ts}
- App URL / entry:
- Build / commit:

## Viewports

| ID | Size | Orientation | Result | Screenshot | Notes |
|----|------|-------------|--------|------------|-------|
| V1 | 360×640 | Portrait | | | |
| V2 | 390×844 | Portrait | | | |
| V3 | 428×926 | Portrait | | | |
| V4 | 768×1024 | Portrait | | | |
| V5 | 360×640 | Landscape | | | |
| V6 | 1024×768 | Landscape | | | |

## Flows

| Flow | Worst viewport | Pass/Fail | Evidence | Fix ref |
|------|----------------|-----------|----------|---------|
| Home | | | | |
| Navigation | | | | |
| Primary form | | | | |
| Critical list/detail | | | | |

## Defects

| ID | Severity | Description | Viewport | Evidence |
|----|----------|-------------|----------|----------|
| | P0/P1/P2/P3 | | | |
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--title", default="Mobile Baseline")
    args = parser.parse_args()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    if not args.out.exists():
        args.out.write_text(
            TEMPLATE.format(title=args.title, ts=datetime.now(timezone.utc).isoformat()),
            encoding="utf-8",
        )
    print(f"Ready: {args.out.resolve()}")


if __name__ == "__main__":
    main()
