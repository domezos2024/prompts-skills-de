#!/usr/bin/env python3
"""Scaffold proxy/server change log and backup index.

Usage:
  python scaffold_proxy_change_log.py --out artifacts/server-proxy --service myapp
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

TEMPLATE = """# Proxy/Server Change Log – {service}

- Created (UTC): {ts}
- Host:
- Proxy engine (nginx/caddy/traefik/apache/other):

## Inventory snapshot

| Item | Value |
|------|-------|
| Domains | |
| Ports | |
| Existing routes | |
| TLS | |

## Backups

| File | Path | Restored? |
|------|------|-----------|
| | | |

## Planned diff

-

## Validation

| Check | Result | Evidence |
|-------|--------|----------|
| Syntax | | |
| New route | | |
| Legacy routes | | |
| TLS | | |

## Approvals

- [ ] User approved reload/deploy
- [ ] Rollback ready
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--service", required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "backups").mkdir(exist_ok=True)
    path = args.out / "CHANGE_LOG.md"
    if not path.exists():
        path.write_text(
            TEMPLATE.format(service=args.service, ts=datetime.now(timezone.utc).isoformat()),
            encoding="utf-8",
        )
    print(f"Ready: {args.out.resolve()}")


if __name__ == "__main__":
    main()
