#!/usr/bin/env python3
"""Scaffold monetization model comparison and test plan.

Usage:
  python scaffold_monetization_matrix.py --out artifacts/monetization
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

MATRIX = """# Monetization Model Matrix

- Created (UTC): {ts}
- Product:
- Cost drivers:
- Existing payments:

| Model | Fit (1-5) | Fees | Tech effort | UX risk | Fairness notes | Decision |
|-------|-----------|------|-------------|---------|----------------|----------|
| Voluntary support / donation | | | | | | |
| One-time purchase | | | | | | |
| Optional premium | | | | | | |
| Hybrid | | | | | | |

## Selected model

- Choice:
- Why:
- Provider (authorized):
- Live approval: pending | granted | denied
"""

TESTS = """# Payment test plan

| ID | Case | Mode | Steps | Expected | Result | Evidence |
|----|------|------|-------|----------|--------|----------|
| P1 | Successful payment | sandbox | | | | |
| P2 | User cancel | sandbox | | | | |
| P3 | Provider error | sandbox | | | | |
| P4 | Return-to-app | sandbox | | | | |
| P5 | Webhook / confirm | sandbox | | | | |
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).isoformat()
    for name, body in (("model-matrix.md", MATRIX), ("payment-test-plan.md", TESTS)):
        path = args.out / name
        if not path.exists():
            path.write_text(body.format(ts=ts), encoding="utf-8")
    print(f"Ready: {args.out.resolve()}")


if __name__ == "__main__":
    main()
