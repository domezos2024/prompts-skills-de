#!/usr/bin/env python3
"""Find common dependency manifests and summarize them into a markdown inventory.

Usage:
  python summarize_manifests.py --root . --out artifacts/deps-baseline/MANIFESTS.md
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

CANDIDATES = [
    "package.json",
    "package-lock.json",
    "pnpm-lock.yaml",
    "yarn.lock",
    "requirements.txt",
    "pyproject.toml",
    "Pipfile",
    "Pipfile.lock",
    "go.mod",
    "go.sum",
    "Cargo.toml",
    "Cargo.lock",
    "pom.xml",
    "build.gradle",
    "build.gradle.kts",
    "packages.config",
    "*.csproj",
    "Directory.Packages.props",
    "composer.json",
    "Gemfile",
]

SKIP = {".git", "node_modules", "dist", "build", ".next", "vendor", "__pycache__", ".venv"}


def find_files(root: Path) -> list[Path]:
    found: list[Path] = []
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        if any(part in SKIP for part in p.parts):
            continue
        name = p.name
        if name in CANDIDATES or p.suffix.lower() == ".csproj":
            found.append(p)
    return sorted(found)


def summarize_package_json(path: Path) -> list[str]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        return [f"- parse error: {exc}"]
    lines = []
    for key in ("dependencies", "devDependencies", "peerDependencies", "optionalDependencies"):
        deps = data.get(key) or {}
        if deps:
            lines.append(f"- **{key}** ({len(deps)})")
            for name, ver in sorted(deps.items())[:80]:
                lines.append(f"  - `{name}`: `{ver}`")
            if len(deps) > 80:
                lines.append(f"  - … +{len(deps) - 80} more")
    return lines or ["- (no dependency keys)"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    files = find_files(root)

    lines = [
        "# Dependency Manifest Inventory",
        "",
        f"- Created (UTC): {datetime.now(timezone.utc).isoformat()}",
        f"- Root: `{root}`",
        f"- Files found: {len(files)}",
        "",
    ]
    for f in files:
        rel = f.relative_to(root)
        lines.append(f"## `{rel.as_posix()}`")
        if f.name == "package.json":
            lines.extend(summarize_package_json(f))
        else:
            lines.append(f"- size: {f.stat().st_size} bytes")
            lines.append("- (raw manifest present — review in upgrade matrix)")
        lines.append("")

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {args.out.resolve()} ({len(files)} manifests)")


if __name__ == "__main__":
    main()
