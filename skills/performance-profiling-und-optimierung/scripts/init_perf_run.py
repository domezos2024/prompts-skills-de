#!/usr/bin/env python3
"""Scaffold a performance run folder with environment and results stubs.

Usage:
  python init_perf_run.py --out artifacts/perf-baseline --label baseline
  python init_perf_run.py --out artifacts/perf-after --label after
"""
from __future__ import annotations

import argparse
import json
import platform
from datetime import datetime, timezone
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--label", default="run")
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    env = {
        "label": args.label,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "platform": platform.platform(),
        "python": platform.python_version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "notes": {
            "build_type": "",
            "dataset": "",
            "warmup": "",
            "iterations": "",
            "git_commit": "",
        },
    }
    (args.out / "env.json").write_text(json.dumps(env, indent=2), encoding="utf-8")

    results = args.out / "RESULTS.md"
    if not results.exists():
        results.write_text(
            f"""# Perf Results ({args.label})

- Created (UTC): {env['created_utc']}
- See env.json for machine metadata.

## Measurements

| Scenario | Metric | Value | Unit | Method | Notes |
|----------|--------|-------|------|--------|-------|
| | | | | | |

## Raw profiler outputs

Place profiler exports in this folder and link them from the matrix.
""",
            encoding="utf-8",
        )
    print(f"Ready: {args.out.resolve()}")


if __name__ == "__main__":
    main()
