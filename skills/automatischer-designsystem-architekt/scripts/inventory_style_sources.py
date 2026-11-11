#!/usr/bin/env python3
"""Scan a project tree for likely style/token/component sources.

Usage:
  python inventory_style_sources.py --root . --out artifacts/ds-inventory/SOURCES.md
"""
from __future__ import annotations

import argparse
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

PATTERNS = {
    "css": ("*.css", "*.scss", "*.sass", "*.less"),
    "tokens": ("*token*", "*theme*", "*design-system*"),
    "tailwind": ("tailwind.config.*",),
    "styled": ("*.styles.ts", "*.styles.tsx", "*.styled.ts", "*.styled.tsx"),
}

SKIP_DIRS = {".git", "node_modules", "dist", "build", ".next", "coverage", "vendor", "__pycache__"}


def iter_files(root: Path):
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        yield p


def match_category(path: Path) -> str | None:
    name = path.name.lower()
    rel = str(path).lower()
    if name.endswith((".css", ".scss", ".sass", ".less")):
        return "css"
    if "tailwind.config" in name:
        return "tailwind"
    if re.search(r"(token|theme|design[-_]?system)", name) or re.search(
        r"(token|theme|design[-_]?system)", rel
    ):
        return "tokens"
    if name.endswith((".styles.ts", ".styles.tsx", ".styled.ts", ".styled.tsx")):
        return "styled"
    if path.suffix.lower() in {".tsx", ".jsx", ".vue", ".svelte"} and re.search(
        r"(button|input|select|modal|dialog|badge|card)", name
    ):
        return "components"
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    buckets: dict[str, list[str]] = defaultdict(list)
    for f in iter_files(args.root.resolve()):
        cat = match_category(f)
        if cat:
            try:
                rel = f.relative_to(args.root.resolve())
            except ValueError:
                rel = f
            buckets[cat].append(str(rel).replace("\\", "/"))

    lines = [
        "# Design-System Style Sources",
        "",
        f"- Created (UTC): {datetime.now(timezone.utc).isoformat()}",
        f"- Root: `{args.root.resolve()}`",
        "",
    ]
    for cat in sorted(buckets):
        lines.append(f"## {cat} ({len(buckets[cat])})")
        for item in sorted(buckets[cat])[:200]:
            lines.append(f"- `{item}`")
        if len(buckets[cat]) > 200:
            lines.append(f"- … +{len(buckets[cat]) - 200} more")
        lines.append("")

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {args.out.resolve()} ({sum(len(v) for v in buckets.values())} files)")


if __name__ == "__main__":
    main()
