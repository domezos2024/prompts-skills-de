#!/usr/bin/env python3
"""Scaffold Docker measurement notes (does not run docker by itself).

Usage:
  python measure_image_notes.py --out artifacts/docker --image app:local
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

TEMPLATE = """# Container Metrics – {image}

- Created (UTC): {ts}
- Host context (dev/ci/prod-sim):

## Commands (run manually / with approval)

```bash
docker image inspect {image} --format 'Size={{{{.Size}}}}'
docker compose config
# NEVER: docker system prune --volumes on shared/prod without explicit approval
```

## Results

| Check | Result | Evidence |
|-------|--------|----------|
| Build | | |
| Start | | |
| Healthcheck | | |
| Restart | | |
| Persist (test volume) | | |
| Image size | | |
| Start time | | |

## Risks

-
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--image", default="app:local")
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    path = args.out / "METRICS.md"
    if not path.exists():
        path.write_text(
            TEMPLATE.format(image=args.image, ts=datetime.now(timezone.utc).isoformat()),
            encoding="utf-8",
        )
    print(f"Ready: {args.out.resolve()}")


if __name__ == "__main__":
    main()
