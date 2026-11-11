#!/usr/bin/env python3
"""Scaffold a draft agent/skill pack for a project.

Usage:
  python scaffold_agent_skill_pack.py --out artifacts/agent-skill-pack
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

FILES = {
    "INVENTORY.md": """# AI tooling inventory

- Created (UTC): {ts}
- Tools in use:
- Existing rule files:
- Existing skills:
- Recurring tasks:
- Overwrite risk notes:
""",
    "PROJECT_RULES.draft.md": """# Project rules (draft)

Keep central. Imperative. No secrets.

## Must

- …

## Never

- …
""",
    "skills/_template/SKILL.md": """---
name: example-skill
description: Use when <trigger> - runs <workflow summary>.
---

# Example Skill

## Overview

## When to Use

## When NOT to Use

## Critical Guidelines

- MUST …
- NEVER …

## Workflow

### PHASE 1 – DISCOVERY
### PHASE 2 – PLANNING
### PHASE 3 – IMPLEMENTATION
### PHASE 4 – VALIDATION
### PHASE 5 – DELIVERY

## Resources

- `../_shared/references/iron-laws.md`
""",
    "validation-notes.md": """# Validation notes

| Check | Result | Evidence |
|-------|--------|----------|
| Structure | | |
| Sample task | | |
| No accidental overwrite | | |
""",
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
            path.write_text(body.format(ts=ts), encoding="utf-8")
    print(f"Ready: {args.out.resolve()}")


if __name__ == "__main__":
    main()
