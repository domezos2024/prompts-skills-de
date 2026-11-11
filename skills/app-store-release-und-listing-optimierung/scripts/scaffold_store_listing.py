#!/usr/bin/env python3
"""Scaffold store listing draft files.

Usage:
  python scaffold_store_listing.py --out artifacts/store-listing
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

FILES = {
    "README.md": """# Store Listing Package

- Created (UTC): {ts}
- App name:
- Platforms:
- Version / build:
- Track:
- Publish approval: pending | granted | denied

## Artifacts

- Release binary path:
- Icon path(s):
- Screenshot path(s):
""",
    "short-description.txt": """# Short description (respect store length limits)

""",
    "full-description.txt": """# Full description (only real features)

""",
    "whats-new.txt": """# What's new

""",
    "checklist-notes.md": """# Validation notes

| Check | Result | Evidence |
|-------|--------|----------|
| Install | | |
| Core flows | | |
| Asset sizes | | |
| Privacy | | |
""",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).isoformat()
    for name, body in FILES.items():
        path = args.out / name
        if not path.exists():
            path.write_text(body.format(ts=ts), encoding="utf-8")
    print(f"Ready: {args.out.resolve()}")


if __name__ == "__main__":
    main()
