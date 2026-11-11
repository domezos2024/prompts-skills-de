#!/usr/bin/env python3
"""Scaffold a CI workflow stub and runbook notes (no secrets, no deploy).

Usage:
  python scaffold_workflow_stub.py --out artifacts/cicd --name ci
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

WORKFLOW = """# Pseudo-stub – copy into .github/workflows/ only after review
name: {name}

on:
  pull_request:
  push:
    branches: [main]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install / restore deps
        run: echo "replace with project install"
      - name: Lint
        run: echo "replace with lint"
      - name: Test
        run: echo "replace with tests"
      - name: Build
        run: echo "replace with build"
  # deploy:
  #   needs: validate
  #   environment: production  # requires approval
  #   if: false  # enable only with explicit user approval
"""

NOTES = """# CI/CD Notes

- Created (UTC): {ts}
- Existing workflows:
- Required secret *names* (no values):
- Prod gate:

## Test runs

| Branch | Run ID/URL | Result | Notes |
|--------|------------|--------|-------|
| | | | |
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--name", default="ci")
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    stub = args.out / f"{args.name}.workflow.stub.yml"
    if not stub.exists():
        stub.write_text(WORKFLOW.format(name=args.name), encoding="utf-8")
    notes = args.out / "CICD_NOTES.md"
    if not notes.exists():
        notes.write_text(
            NOTES.format(ts=datetime.now(timezone.utc).isoformat()),
            encoding="utf-8",
        )
    print(f"Ready: {args.out.resolve()}")


if __name__ == "__main__":
    main()
