#!/usr/bin/env python3
"""Scaffold a feature opportunity scorecard markdown.

Usage:
  python scaffold_feature_scorecard.py --out artifacts/feature-scorecard.md
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

TEMPLATE = """# Feature Opportunity Scorecard

- Created (UTC): {ts}
- Product / repo:
- Evidence sources:

## Candidates (≥10)

| ID | Idea | Evidence | Nutzen (1-5) | Aufwand (1-5) | Wartung (1-5) | Risiko (1-5) | Score* | Notes |
|----|------|----------|--------------|---------------|---------------|--------------|--------|-------|
| F01 | | | | | | | | |
| F02 | | | | | | | | |
| F03 | | | | | | | | |
| F04 | | | | | | | | |
| F05 | | | | | | | | |
| F06 | | | | | | | | |
| F07 | | | | | | | | |
| F08 | | | | | | | | |
| F09 | | | | | | | | |
| F10 | | | | | | | | |

\\*Score-Vorschlag: `Nutzen*2 - Aufwand - Wartung - Risiko` (anpassen und dokumentieren).

## Top 3 Use Cases

### T1 –
- Actor / Goal / Flow:
- Acceptance criteria:
- Dependencies:

### T2 –
- Actor / Goal / Flow:
- Acceptance criteria:
- Dependencies:

### T3 –
- Actor / Goal / Flow:
- Acceptance criteria:
- Dependencies:

## Selected for implementation

- ID:
- Why:
- Scope / Out-of-scope:
- Rollback:
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    if not args.out.exists():
        args.out.write_text(
            TEMPLATE.format(ts=datetime.now(timezone.utc).isoformat()),
            encoding="utf-8",
        )
    print(f"Ready: {args.out.resolve()}")


if __name__ == "__main__":
    main()
