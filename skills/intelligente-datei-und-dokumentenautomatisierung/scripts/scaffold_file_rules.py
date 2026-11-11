#!/usr/bin/env python3
"""Scaffold file/document automation rules and dry-run manifest template.

Usage:
  python scaffold_file_rules.py --out artifacts/file-automation-rules.md
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

TEMPLATE = """# File & Document Automation Rules

- Created (UTC): {ts}
- Source roots:
- Target roots:
- Safety default: dry-run first

## Classification Rules

| ID | Match (ext/pattern/content) | Class | Target dir template | Naming template |
|----|-----------------------------|-------|---------------------|-----------------|
| R1 | | | | |

## Validation Policy

| Check | Action on fail |
|-------|----------------|
| unreadable/corrupt | quarantine |
| duplicate hash | skip or link policy: |
| incomplete/temp | skip |
| path traversal / escape | reject |

## Conversion

| From | To | Keep original | Tool | Notes |
|------|----|---------------|------|-------|
| | | yes (required) | | |

## Conflict Policy

- On name collision: `suffix` | `quarantine` | `fail` (never silent overwrite)
- Chosen:

## Dry-Run Manifest Columns

`run_id, timestamp, action, src, dest, hash, bytes, rule_id, status`

## Test Matrix

| Case | Expected | Result |
|------|----------|--------|
| unicode name | preserved/safe mapped | |
| large file | streams, no truncate | |
| collision | no overwrite | |
| abort mid-run | resume/idempotent | |
| convert | original remains | |
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
