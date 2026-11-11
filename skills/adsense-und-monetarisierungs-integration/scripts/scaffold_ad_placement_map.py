#!/usr/bin/env python3
"""Scaffold ad placement map and validation notes.

Usage:
  python scaffold_ad_placement_map.py --out artifacts/adsense
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

TEMPLATE = """# Ad Placement Map

- Created (UTC): {ts}
- Publisher ID source (must be real or BLOCKED):
- CMP:

## Placements

| Page | Zone | Slot ID | Away from critical UI? | Consent gated? |
|------|------|---------|--------------------------|----------------|
| | | | | |

## Validation

| Check | Result | Evidence |
|-------|--------|----------|
| Consent accept | | |
| Consent reject | | |
| Revoke | | |
| Mobile layout / CLS | | |
| CSP | | |

## Policy

- No invented IDs
- No click baiting
- No live-activation claim without confirmation
- Prod deploy requires explicit user approval
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    path = args.out / "AD_PLACEMENT_MAP.md"
    if not path.exists():
        path.write_text(
            TEMPLATE.format(ts=datetime.now(timezone.utc).isoformat()),
            encoding="utf-8",
        )
    print(f"Ready: {args.out.resolve()}")


if __name__ == "__main__":
    main()
