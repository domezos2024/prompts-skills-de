#!/usr/bin/env python3
"""Scaffold an MCP capability matrix markdown file.

Usage:
  python scaffold_capability_matrix.py --out artifacts/mcp-capability-matrix.md
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

TEMPLATE = """# MCP Capability Matrix

- Created (UTC): {ts}
- Server / package:
- Auth model:

## Tools (Ist)

| Name | Purpose | Side effects | AuthZ | Schema | Tests | Notes |
|------|---------|--------------|-------|--------|-------|-------|
| | | none/read/write/destructive | | yes/no | | |

## Resources / Prompts

| Kind | Name | Purpose | Notes |
|------|------|---------|-------|
| | | | |

## Gaps (Soll)

| ID | Capability | Benefit | Effort | Risk | Priority | Decision |
|----|------------|---------|--------|------|----------|----------|
| G1 | | | S/M/L | L/M/H | P0-P3 | build/skip |

## Top-5 Implementation Plan

| Rank | Tool | Contract summary | Idempotency | Done criteria |
|------|------|------------------|-------------|---------------|
| 1 | | | | |
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
