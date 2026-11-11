#!/usr/bin/env python3
"""Scaffold LLM provider inventory and routing policy matrix.

Usage:
  python scaffold_provider_matrix.py --out artifacts/provider-routing-matrix.md
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

TEMPLATE = """# Provider Routing Matrix

- Created (UTC): {ts}
- Environment:
- Inventory rule: only verified access

## Providers

| Provider | Access (API/CLI) | Auth verified | Models | Rate limit | Cost notes | ToS notes | Status |
|----------|------------------|---------------|--------|------------|------------|-----------|--------|
| | | yes/no | | | | | available/blocked |

## Unified Adapter Contract (logical)

- `complete(messages, tools?, params) -> result | normalized_error`
- Errors: `rate_limit` | `timeout` | `unavailable` | `auth` | `content_filter` | `unknown`

## Routing Policies

| Task type | Primary | Fallbacks | Budget cap | Notes |
|-----------|---------|-----------|------------|-------|
| coding | | | | |
| planning | | | | |
| cheap_classify | | | | |

## Checkpoint / Handoff

| Field | Purpose |
|-------|---------|
| run_id | correlation |
| step_id | resume point |
| context_digest | compact handoff |
| effect_ids | tool dedup |
| tokens_used | budget |

## Failover Test Plan

| Scenario | Expected behavior | Result |
|----------|-------------------|--------|
| rate_limit on primary | cooldown + fallback | |
| timeout | retry then fallback | |
| auth failure | hard-fail, no illegal bypass | |
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
