#!/usr/bin/env python3
"""Scaffold repository knowledge base folders and stubs.

Usage:
  python scaffold_knowledge_base.py --out knowledge
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

FILES = {
    "INDEX.md": """# Knowledge base index

- Created (UTC): {ts}

## Start here

1. [Architecture overview](architecture-overview.md)
2. [Data flows](data-flows.md)
3. [Project rules](project-rules.md)
4. [Boundaries](boundaries-and-constraints.md)
5. [Update rules](update-rules.md)
6. [Validation log](validation-log.md)

## Modules

- (add links under modules/)
""",
    "architecture-overview.md": """# Architecture overview

## System context

## Major components

## Key entry points

| Entry | Path | Notes | Verified |
|-------|------|-------|----------|
| | | | |
""",
    "data-flows.md": """# Data flows

```mermaid
flowchart LR
  A[Entry] --> B[Core]
  B --> C[Store]
```

## Flow notes

| Flow | Source files | Verified |
|------|--------------|----------|
| | | |
""",
    "boundaries-and-constraints.md": """# Boundaries and constraints

## In scope

## Out of scope / non-goals

## Hard constraints
""",
    "project-rules.md": """# Project rules summary

Link to AGENTS.md / CLAUDE.md / CI rules. Do not duplicate wholesale.

| Rule source | Path | Summary |
|-------------|------|---------|
| | | |
""",
    "update-rules.md": """# Knowledge base update rules

1. Update module pages when public APIs or ownership change.
2. Update data-flows when a cross-module path changes.
3. Add ADR when a significant decision is made.
4. Re-run validation samples after large refactors.
""",
    "validation-log.md": """# Validation log

- Created (UTC): {ts}

| Claim | Source doc | Code path | Result |
|-------|------------|-----------|--------|
| | | | Pass/Fail |
""",
    "modules/.gitkeep": "",
    "decisions/.gitkeep": "",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    ts = datetime.now(timezone.utc).isoformat()
    for name, body in FILES.items():
        path = args.out / name
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            path.write_text(body.format(ts=ts) if body else "", encoding="utf-8")
    print(f"Ready: {args.out.resolve()}")


if __name__ == "__main__":
    main()
