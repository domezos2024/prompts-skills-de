#!/usr/bin/env python3
"""Scaffold STRICT priority matrix for audit findings.

Usage:
  python scaffold_priority_matrix.py --out artifacts/strict/priority-matrix.md
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

TEMPLATE = """# STRICT Priority Matrix

- Created (UTC): {ts}
- Project:
- Baseline build/tests:

## Findings

| ID | Phase | Dimension (A/B/C/D/UI) | Finding | Evidence class | Evidence | P0-P3 | Action | Status | Validation |
|----|-------|------------------------|---------|----------------|----------|-------|--------|--------|------------|
| S01 | 2 | A | | Confirmed | | P1 | | open | |
| S02 | 2 | B | | | | | | open | |
| S03 | 2 | C | | | | | | open | |
| S04 | 2 | D | | | | | | open | |
| S05 | 4 | UI | | | | | | open | |

## Priority rules

- P0: Security, data loss, crash, broken build
- P1: Severe functional / perf / UX
- P2: Maintainability / complexity / consistency
- P3: Cosmetic / optional

## Ordering

1. Close all actionable P0
2. Close actionable P1
3. Then P2/P3 within scope
4. Re-audit (PHASE 8) before claiming done
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
