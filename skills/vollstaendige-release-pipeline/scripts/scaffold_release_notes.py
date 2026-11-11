#!/usr/bin/env python3
"""Scaffold release notes and checksums folder.

Usage:
  python scaffold_release_notes.py --out artifacts/release --version 1.2.3
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

NOTES = """# Release {version}

- Created (UTC): {ts}
- Previous version/tag:
- Target channel (needs user approval to publish):

## Highlights

-

## Changes

| Type | Description | Evidence |
|------|-------------|---------|
| feat/fix/chore | | |

## Artifacts

| File | SHA256 | Smoke |
|------|--------|-------|
| | | |

## Gates

- [ ] Tests/build green
- [ ] Checksums verified
- [ ] User approval for publish/tag/push
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--version", required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "checksums").mkdir(exist_ok=True)
    notes = args.out / "RELEASE_NOTES.md"
    if not notes.exists():
        notes.write_text(
            NOTES.format(version=args.version, ts=datetime.now(timezone.utc).isoformat()),
            encoding="utf-8",
        )
    print(f"Ready: {args.out.resolve()}")


if __name__ == "__main__":
    main()
