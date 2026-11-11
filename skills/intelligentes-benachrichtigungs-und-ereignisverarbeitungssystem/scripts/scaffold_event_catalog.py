#!/usr/bin/env python3
"""Scaffold event catalog and notification delivery matrix.

Usage:
  python scaffold_event_catalog.py --out artifacts/event-notification-catalog.md
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

TEMPLATE = """# Event & Notification Catalog

- Created (UTC): {ts}
- System:
- Delivery goal: at-least-once process + deduped notify

## Event Types

| Event type | Schema/version | Priority | Producers | PII | Notes |
|------------|----------------|----------|-----------|-----|-------|
| | | P0-P3 | | yes/no | |

## Channels

| Channel | Provider | Opt-in required | Rate limits | Adapter status |
|---------|----------|-----------------|-------------|----------------|
| email | | yes/no | | |
| web_push | | | | |
| in_app | | | | |

## State Machine

`pending` → `processing` → `sent` | `failed` → (retry) | `dead`

| Transition | Guard | Side effects |
|------------|-------|--------------|
| | | |

## Idempotency

| Key | Scope | Store |
|-----|-------|-------|
| event_id | ingest | |
| notification_id | per user+channel+event | |

## Test Plan

| Scenario | Expected | Result |
|----------|----------|--------|
| duplicate event | single notification | |
| crash mid-send | resume / no silent drop | |
| opt-out | skip channel | |
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
