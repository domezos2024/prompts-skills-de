#!/usr/bin/env python3
"""Scaffold REST API contract notes from official documentation (manual fill).

Usage:
  python scaffold_api_contract.py --out artifacts/rest-api-contract.md
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

TEMPLATE = """# REST API Contract Notes

- Created (UTC): {ts}
- Official docs URL(s):
- API version:
- Rule: no invented endpoints/fields

## Auth

| Mechanism | Details | Secret location | Notes |
|-----------|---------|-----------------|-------|
| | | | |

## Endpoints in Scope

| Method | Path | Purpose | Idempotent | Pagination | Doc anchor |
|--------|------|---------|------------|------------|------------|
| | | | yes/no | | |

## Error Model

| Status / code | Meaning | Retryable | Source |
|---------------|---------|-----------|--------|
| | | yes/no | docs |

## Client Method Plan

| Client method | Maps to | DTO in | DTO out | Timeout | Retry policy |
|---------------|---------|--------|---------|---------|--------------|
| | | | | | |

## Test Matrix

| Case | Expected | Type (mock/integration) | Result |
|------|----------|-------------------------|--------|
| | | | |
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
