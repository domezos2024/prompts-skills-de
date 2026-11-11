#!/usr/bin/env python3
"""Scaffold baseline/after artifact folders and a notes markdown file.

Usage:
  python capture_baseline_notes.py --out artifacts/ui-baseline --title "Baseline"
  python capture_baseline_notes.py --out artifacts/ui-after --title "After"
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

TEMPLATE = """# {title}

- Created (UTC): {ts}
- App URL / entry:
- Viewport(s):
- Critical flows covered:

## Screenshots

| Flow | File | Notes |
|------|------|-------|
| | | |

## Issues spotted

| ID | Severity | Description | Evidence |
|----|----------|-------------|----------|
| | P0/P1/P2/P3 | | |
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--title", required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    notes = args.out / "NOTES.md"
    if not notes.exists():
        notes.write_text(
            TEMPLATE.format(title=args.title, ts=datetime.now(timezone.utc).isoformat()),
            encoding="utf-8",
        )
    print(f"Ready: {args.out.resolve()}")


if __name__ == "__main__":
    main()
