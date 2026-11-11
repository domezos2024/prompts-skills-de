#!/usr/bin/env python3
"""Scaffold ETL pipeline specification and DQ gate sheet.

Usage:
  python scaffold_pipeline_spec.py --out artifacts/etl-pipeline-spec.md
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

TEMPLATE = """# ETL Pipeline Spec

- Created (UTC): {ts}
- Pipeline name:
- Owner:

## Sources

| Source | Format | Cadence | Watermark/key | PII | Notes |
|--------|--------|---------|---------------|-----|-------|
| | | | | yes/no | |

## Canonical Model

| Field | Type | Required | Validation | Lineage |
|-------|------|----------|------------|---------|
| | | | | |

## Stages

| Stage | Input | Output | Idempotency | Checkpoint |
|-------|-------|--------|-------------|------------|
| Extract | | | | |
| Transform | | | | |
| DQ Gate | | | | |
| Load | | | | |

## DQ Thresholds

| Check | Metric | Threshold | On fail |
|-------|--------|-----------|---------|
| completeness | | | quarantine/block |
| uniqueness | | | |
| freshness | | | |

## Restart / Re-run Tests

| Scenario | Expected | Result |
|----------|----------|--------|
| kill after extract | resume without dup load | |
| bad rows | quarantine, good rows load | |
| re-run same watermark | no duplicate facts | |
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
