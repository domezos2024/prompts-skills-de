#!/usr/bin/env python3
"""Scaffold an asset manifest and folder structure for the asset factory skill.

Usage:
  python init_asset_manifest.py --out artifacts/assets
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

MANIFEST = """# Asset Manifest

- Created (UTC): {ts}
- Brand / style notes:
- License policy:

## Assets

| ID | Type | Priority | Source/License | Source file | Exported paths | Integrated | In-app verified | Notes |
|----|------|----------|----------------|-------------|----------------|------------|-----------------|-------|
| A1 | | P0/P1/P2/P3 | | | | no | no | |

## Rejected / deferred

| ID | Reason | Follow-up |
|----|--------|-----------|
| | | |
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    for sub in ("icons", "logos", "illustrations", "empty-states", "store", "exports"):
        (args.out / sub).mkdir(parents=True, exist_ok=True)
    manifest = args.out / "ASSET_MANIFEST.md"
    if not manifest.exists():
        manifest.write_text(
            MANIFEST.format(ts=datetime.now(timezone.utc).isoformat()),
            encoding="utf-8",
        )
    print(f"Ready: {args.out.resolve()}")


if __name__ == "__main__":
    main()
