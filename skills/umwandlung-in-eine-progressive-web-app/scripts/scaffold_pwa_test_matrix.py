#!/usr/bin/env python3
"""Scaffold PWA test matrix and strategy notes.

Usage:
  python scaffold_pwa_test_matrix.py --out artifacts/pwa
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

TEMPLATE = """# PWA Test Matrix

- Created (UTC): {ts}
- App URL:
- Manifest path:
- Service worker path:

## Cache strategy

| Resource type | Strategy | Versioned? | Notes |
|---------------|----------|------------|-------|
| App shell | | | |
| Static assets | | | |
| API/Auth | network-only / no-cache | | must not leak |

## Tests

| Browser | Install | Offline | Reconnect | Update | Evidence |
|---------|---------|---------|-----------|--------|----------|
| | | | | | |

## Privacy exclusions

-

## Approvals

- [ ] User approval for production deploy
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    path = args.out / "PWA_TEST_MATRIX.md"
    if not path.exists():
        path.write_text(
            TEMPLATE.format(ts=datetime.now(timezone.utc).isoformat()),
            encoding="utf-8",
        )
    print(f"Ready: {args.out.resolve()}")


if __name__ == "__main__":
    main()
