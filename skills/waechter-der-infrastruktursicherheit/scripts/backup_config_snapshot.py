#!/usr/bin/env python3
"""Copy config files into a timestamped backup folder before infra hardening.

Usage:
  python backup_config_snapshot.py --out artifacts/infra/backups --files nginx.conf,docker-compose.yml
  python backup_config_snapshot.py --out artifacts/infra/backups --files C:/path/to/Caddyfile
"""
from __future__ import annotations

import argparse
import shutil
from datetime import datetime, timezone
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument(
        "--files",
        required=True,
        help="Comma-separated paths to config files to snapshot",
    )
    args = parser.parse_args()
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    dest_root = args.out / stamp
    dest_root.mkdir(parents=True, exist_ok=True)
    manifest = ["# Infra config backup", f"- UTC: {stamp}", ""]
    for raw in args.files.split(","):
        src = Path(raw.strip())
        if not src.exists() or not src.is_file():
            manifest.append(f"- MISSING: {src}")
            continue
        target = dest_root / src.name
        # Avoid overwrite collisions
        if target.exists():
            target = dest_root / f"{src.stem}__{abs(hash(str(src.resolve())))}{src.suffix}"
        shutil.copy2(src, target)
        manifest.append(f"- {src.resolve()} -> {target.name}")
    (dest_root / "MANIFEST.md").write_text("\n".join(manifest) + "\n", encoding="utf-8")
    print(f"Backup ready: {dest_root.resolve()}")


if __name__ == "__main__":
    main()
