#!/usr/bin/env python3
"""Scaffold changelog / release note artifacts.

Usage:
  python scaffold_changelog.py --out artifacts/release-notes --version Unreleased
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

CHANGELOG = """# Changelog

## [{version}] - TBD

### Features

### Bugfixes

### Performance

### Security

### Breaking Changes

### Internal
"""

USER = """# Release notes {version}

- Created (UTC): {ts}
- Range: <tag>..<commit>

## Highlights

-

## Fixes

-

## Notes / known limits

-
"""

MIGRATION = """# Migration guide {version}

## Breaking changes

## Config changes

## Data / DB steps

## Rollback
"""

VERIFY = """# Verification log

| Claim | Source commit/PR | Diff evidence | Result |
|-------|------------------|---------------|--------|
| | | | Pass/Fail |
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--version", default="Unreleased")
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).isoformat()
    mapping = {
        "CHANGELOG.md": CHANGELOG.format(version=args.version),
        f"release-notes-{args.version}.md": USER.format(version=args.version, ts=ts),
        f"migration-{args.version}.md": MIGRATION.format(version=args.version),
        "verification-log.md": VERIFY,
    }
    for name, body in mapping.items():
        path = args.out / name
        if not path.exists():
            path.write_text(body, encoding="utf-8")
    print(f"Ready: {args.out.resolve()}")


if __name__ == "__main__":
    main()
