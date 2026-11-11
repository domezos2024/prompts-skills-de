#!/usr/bin/env python3
"""Create a quality baseline notes file and optionally record command outputs.

Usage:
  python capture_quality_baseline.py --out artifacts/refactor-baseline
  python capture_quality_baseline.py --out artifacts/refactor-baseline --run "npm test"
"""
from __future__ import annotations

import argparse
import subprocess
from datetime import datetime, timezone
from pathlib import Path

TEMPLATE = """# Quality Baseline

- Created (UTC): {ts}
- Git commit / branch:
- Environment notes:

## Commands

| Command | Exit code | Log file | Notes |
|---------|-----------|----------|-------|
| | | | |

## Hotspots (initial)

| ID | Severity | Description | Path |
|----|----------|-------------|------|
| | P0/P1/P2/P3 | | |
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--run", action="append", default=[], help="Command to run and capture")
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    notes = args.out / "BASELINE.md"
    if not notes.exists():
        notes.write_text(
            TEMPLATE.format(ts=datetime.now(timezone.utc).isoformat()),
            encoding="utf-8",
        )

    for i, cmd in enumerate(args.run, start=1):
        log = args.out / f"cmd-{i}.log"
        proc = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        log.write_text(
            f"$ {cmd}\nexit={proc.returncode}\n\n[stdout]\n{proc.stdout}\n[stderr]\n{proc.stderr}\n",
            encoding="utf-8",
        )
        print(f"Captured exit={proc.returncode} -> {log}")

    print(f"Ready: {args.out.resolve()}")


if __name__ == "__main__":
    main()
