#!/usr/bin/env python3
"""Scaffold a privacy data-map markdown artifact.

Usage:
  python scaffold_data_map.py --out artifacts/privacy/data-map.md
  python scaffold_data_map.py --out artifacts/privacy/data-map.md --app "MyApp"
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

TEMPLATE = """# Data Map – {app}

- Created (UTC): {ts}
- Scope:
- Environment:
- Note: Technical inventory only – not legal advice. Do not paste real PII.

## Categories

| ID | Category | Purpose | Storage | Retention | Recipients | Minimization idea |
|----|----------|---------|---------|-----------|------------|-------------------|
| D1 | | | | | | |

## Flows

| ID | From | To | Channel | PII yes/no | Control gap |
|----|------|-----|---------|------------|-------------|
| F1 | | | | | |

## Rights endpoints / UI

| Right | Entry point | Persistence | Test status |
|-------|-------------|-------------|-------------|
| Consent | | | |
| Withdraw | | | |
| Access/Export | | | |
| Erasure | | | |

## Logging hotspots

| Location | Risk | Redaction status |
|----------|------|------------------|
| | | |

## Open legal questions (do not resolve as engineer alone)

| ID | Question | Owner |
|----|----------|-------|
| L1 | | |
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--app", default="Application")
    args = parser.parse_args()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    if not args.out.exists():
        args.out.write_text(
            TEMPLATE.format(app=args.app, ts=datetime.now(timezone.utc).isoformat()),
            encoding="utf-8",
        )
    print(f"Ready: {args.out.resolve()}")


if __name__ == "__main__":
    main()
