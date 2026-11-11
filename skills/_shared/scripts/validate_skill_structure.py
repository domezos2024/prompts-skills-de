#!/usr/bin/env python3
"""Validate that each skills/<name>/SKILL.md meets repo conventions."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def check_skill(skill_dir: Path) -> list[str]:
    errs: list[str] = []
    skill = skill_dir / "SKILL.md"
    if not skill.exists():
        return [f"{skill_dir.name}: missing SKILL.md"]
    text = skill.read_text(encoding="utf-8")
    m = FRONTMATTER.match(text)
    if not m:
        errs.append(f"{skill_dir.name}: missing YAML frontmatter")
        return errs
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    if set(meta.keys()) - {"name", "description"}:
        errs.append(f"{skill_dir.name}: frontmatter may only contain name, description")
    name = meta.get("name", "")
    desc = meta.get("description", "")
    if not NAME_RE.match(name):
        errs.append(f"{skill_dir.name}: invalid name '{name}'")
    if name != skill_dir.name:
        errs.append(f"{skill_dir.name}: folder name != frontmatter name '{name}'")
    if not desc.lower().startswith("use when"):
        errs.append(f"{skill_dir.name}: description must start with 'Use when'")
    if len(name) + len(desc) > 1024:
        errs.append(f"{skill_dir.name}: name+description exceed 1024 chars")
    body = text[m.end() :]
    for heading in ("## Overview", "## Critical Guidelines", "## Workflow"):
        if heading not in body:
            errs.append(f"{skill_dir.name}: missing section {heading}")
    return errs


def main() -> int:
    skills_root = ROOT
    errors: list[str] = []
    for d in sorted(skills_root.iterdir()):
        if not d.is_dir() or d.name.startswith("_"):
            continue
        if not (d / "SKILL.md").exists():
            continue
        errors.extend(check_skill(d))
    if errors:
        print("FAIL")
        for e in errors:
            print(" -", e)
        return 1
    count = len([d for d in skills_root.iterdir() if d.is_dir() and not d.name.startswith("_") and (d / "SKILL.md").exists()])
    print(f"OK – {count} skills valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
