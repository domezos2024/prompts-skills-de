#!/usr/bin/env python3
"""Scaffold multi-agent handoff contract template.

Usage:
  python scaffold_handoff_contract.py --out artifacts/multi-agent-handoffs.md
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

TEMPLATE = """# Multi-Agent Handoff Contracts

- Created (UTC): {ts}
- Project / run:

## Roles

| Role | Responsibility | Allowed tools | Not allowed |
|------|----------------|---------------|-------------|
| Planner | | | |
| Developer | | | |
| Reviewer | | | |
| Tester | | | |
| Release Manager | | | |

## Handoff Contract Template

```yaml
handoff_id: ""
from_role: ""
to_role: ""
task_id: ""
inputs:
  artifacts: []
  context_summary: ""
acceptance_criteria:
  - ""
outputs_expected:
  - ""
review_gate: required|optional
conflict_scope:
  paths: []
status: draft|ready|accepted|rejected
```

## Conflict Rules

- One writer per path set
- Lock / claim before edit
- Reject handoff if overlapping dirty paths

## Evaluation Matrix

| Metric | Single agent | Multi agent | Notes |
|--------|--------------|-------------|-------|
| Quality | | | |
| Duration | | | |
| Cost / tokens | | | |
| Coordination overhead | | | |
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
