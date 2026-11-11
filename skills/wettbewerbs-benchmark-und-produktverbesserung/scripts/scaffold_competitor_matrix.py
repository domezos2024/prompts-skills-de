#!/usr/bin/env python3
"""Scaffold competitor benchmark artifact folder.

Usage:
  python scaffold_competitor_matrix.py --out artifacts/benchmark
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path
from shutil import copyfile

REF = Path(__file__).resolve().parents[1] / "references" / "competitive-benchmark-matrix.md"

NOTES = """# Benchmark working notes

- Created (UTC): {ts}
- Sources checked:
- Selected improvement:
- Test evidence paths:
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    target = args.out / "competitive-benchmark-matrix.md"
    if not target.exists() and REF.exists():
        copyfile(REF, target)
    notes = args.out / "NOTES.md"
    if not notes.exists():
        notes.write_text(
            NOTES.format(ts=datetime.now(timezone.utc).isoformat()),
            encoding="utf-8",
        )
    print(f"Ready: {args.out.resolve()}")


if __name__ == "__main__":
    main()
