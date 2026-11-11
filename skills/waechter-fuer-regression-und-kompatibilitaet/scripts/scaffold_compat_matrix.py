#!/usr/bin/env python3
"""Scaffold a regression/compatibility matrix markdown.

Usage:
  python scaffold_compat_matrix.py --out artifacts/regression/compat-matrix.md
  python scaffold_compat_matrix.py --out artifacts/regression/compat-matrix.md --targets "win-chrome,win-firefox,linux-node20"
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument(
        "--targets",
        default="win-chrome,linux-node20",
        help="Comma-separated target labels",
    )
    args = parser.parse_args()
    targets = [t.strip() for t in args.targets.split(",") if t.strip()]
    rows = "\n".join(f"| {t} | | NotRun | | |" for t in targets)
    content = f"""# Compatibility Matrix

- Created (UTC): {datetime.now(timezone.utc).isoformat()}
- Baseline commit/tag:
- Change summary:

## Targets

| Target | Version details | Result | Critical flows | Evidence |
|--------|-----------------|--------|----------------|----------|
{rows}

## Impact

| Area | Modules | Risk | Tests |
|------|---------|------|-------|
| | | | |

## Notes

- Use Pass/Fail/NotRun/Unsupported only.
- Do not claim untested targets as Pass.
"""
    args.out.parent.mkdir(parents=True, exist_ok=True)
    if not args.out.exists():
        args.out.write_text(content, encoding="utf-8")
    print(f"Ready: {args.out.resolve()}")


if __name__ == "__main__":
    main()
