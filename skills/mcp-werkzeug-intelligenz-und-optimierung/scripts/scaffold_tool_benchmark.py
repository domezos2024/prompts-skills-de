#!/usr/bin/env python3
"""Scaffold MCP tool usage benchmark report.

Usage:
  python scaffold_tool_benchmark.py --out artifacts/mcp-tool-benchmark.md --phase before
  python scaffold_tool_benchmark.py --out artifacts/mcp-tool-benchmark-after.md --phase after
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

TEMPLATE = """# MCP Tool Benchmark ({phase})

- Created (UTC): {ts}
- Environment / server:
- Trace source:

## Representative Tasks

| Task ID | Description | Success criteria |
|---------|-------------|------------------|
| T1 | | |

## Metrics

| Task ID | Tool call count | Unique tools | Errors | p50 latency | Payload bytes | Notes |
|---------|-----------------|--------------|--------|-------------|---------------|-------|
| T1 | | | | | | |

## Ambiguity / Redundancy Findings

| Issue | Tools involved | Impact | Proposed fix |
|-------|----------------|--------|--------------|
| | | | |

## Targets

- Call count delta goal:
- Error rate goal:
- Safety constraints unchanged: yes/no
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--phase", choices=["before", "after"], default="before")
    args = parser.parse_args()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    if not args.out.exists():
        args.out.write_text(
            TEMPLATE.format(
                phase=args.phase,
                ts=datetime.now(timezone.utc).isoformat(),
            ),
            encoding="utf-8",
        )
    print(f"Ready: {args.out.resolve()}")


if __name__ == "__main__":
    main()
