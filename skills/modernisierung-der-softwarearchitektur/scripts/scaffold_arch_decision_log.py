#!/usr/bin/env python3
"""Scaffold architecture-as-is notes and an ADR-style decision log.

Usage:
  python scaffold_arch_decision_log.py --out artifacts/arch-as-is
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

AS_IS = """# Architecture As-Is

- Created (UTC): {ts}
- System name:
- Runtime / stack:

## Modules

| Module | Responsibility | Owners/Notes |
|--------|----------------|--------------|
| | | |

## Critical data flows

1.
2.

## Known couplings / cycles

| ID | Description | Evidence |
|----|-------------|----------|
| | | |
"""

ADR = """# Architecture Decision Log

- Created (UTC): {ts}

## ADR-001 – Title

- Status: proposed
- Context:
- Options considered:
- Decision:
- Consequences:
- Rollback:
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).isoformat()
    as_is = args.out / "AS_IS.md"
    adr = args.out / "DECISION_LOG.md"
    if not as_is.exists():
        as_is.write_text(AS_IS.format(ts=ts), encoding="utf-8")
    if not adr.exists():
        adr.write_text(ADR.format(ts=ts), encoding="utf-8")
    print(f"Ready: {args.out.resolve()}")


if __name__ == "__main__":
    main()
