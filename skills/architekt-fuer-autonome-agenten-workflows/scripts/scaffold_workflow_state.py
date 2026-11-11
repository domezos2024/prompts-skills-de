#!/usr/bin/env python3
"""Scaffold workflow state machine + checkpoint schema markdown.

Usage:
  python scaffold_workflow_state.py --out artifacts/agent-workflow-design.md
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

TEMPLATE = """# Autonomous Agent Workflow Design

- Created (UTC): {ts}
- Run / task id:
- Persistence store:

## Atomic Steps

| Step ID | Name | Inputs | Outputs | Side effects | Approval? | Idempotency key |
|---------|------|--------|---------|--------------|-----------|-----------------|
| S1 | | | | | yes/no | |

## State Machine

States: `planned` → `running` → `validating` → `succeeded` | `failed` | `waiting_approval` | `compensating`

| From | Event | To | Guard / notes |
|------|-------|----|---------------|
| planned | start | running | |
| running | step_ok | validating | |
| validating | accept | succeeded/next | |
| running | needs_approval | waiting_approval | |
| waiting_approval | approved | running | |
| running | retryable_error | running | retry budget |
| running | fatal_error | failed | |

## Checkpoint Schema (logical)

```json
{{
  "run_id": "",
  "step_id": "",
  "status": "",
  "inputs_hash": "",
  "effect_ids": [],
  "attempt": 0,
  "updated_at": ""
}}
```

## Policies

- Retry budget:
- Timeouts:
- Approval rules:
- Observability fields:
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
