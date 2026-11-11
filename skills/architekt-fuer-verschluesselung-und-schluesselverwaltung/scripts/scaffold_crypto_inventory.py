#!/usr/bin/env python3
"""Scaffold crypto/key inventory markdown for encryption architecture work.

Usage:
  python scaffold_crypto_inventory.py --out artifacts/crypto/inventory.md
  python scaffold_crypto_inventory.py --out artifacts/crypto/inventory.md --app "MyApp"
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

TEMPLATE = """# Crypto Inventory – {app}

- Created (UTC): {ts}
- Authorized scope:
- Environment:
- Warning: never paste raw key material into this file.

## Algorithms in use

| Location | Purpose | Algorithm/Mode | Library | Key ID / source | Versioned? | Risk notes |
|----------|---------|----------------|---------|-----------------|------------|------------|
| | | | | | | |

## Key hierarchy

| Key | Type | Storage | Access | Rotation | Status |
|-----|------|---------|--------|----------|--------|
| | DEK/KEK/signing | | | | |

## Envelope format (target)

```
version | key_id | nonce | aad_context | ciphertext+tag
```

## Threat guarantees

| Guarantee | Required yes/no | Mechanism |
|-----------|-----------------|-----------|
| Confidentiality | | |
| Integrity/Authenticity | | |
| Key separation | | |
| Forward secrecy (if applicable) | | |

## Migration plan

| Step | Action | Rollback |
|------|--------|----------|
| 1 | Backup | |
| 2 | Dual-read deploy | |
| 3 | Reencrypt batch (lab first) | |
| 4 | Retire old key (after verify) | |

## Test log

| Case | Result | Evidence |
|------|--------|----------|
| Roundtrip | | |
| Tamper | | |
| Wrong key | | |
| Rotation probe | | |
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--app", default="Application")
    args = parser.parse_args()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    if not args.out.exists():
        args.out.write_text(
            TEMPLATE.format(app=args.app, ts=datetime.now(timezone.utc).isoformat()),
            encoding="utf-8",
        )
    print(f"Ready: {args.out.resolve()}")


if __name__ == "__main__":
    main()
