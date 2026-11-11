#!/usr/bin/env python3
"""Scaffold an RBAC/ABAC authorization matrix markdown file.

Usage:
  python scaffold_authz_matrix.py --out artifacts/authz/matrix.md
  python scaffold_authz_matrix.py --out artifacts/authz/matrix.md --roles anonymous,user,admin
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path


def build(roles: list[str]) -> str:
    role_cols = " | ".join(roles)
    role_sep = " | ".join(["------"] * len(roles))
    empty_role_cells = " | ".join([""] * len(roles))
    return f"""# AuthZ Matrix

- Created (UTC): {datetime.now(timezone.utc).isoformat()}
- Roles: {", ".join(roles)}
- Note: fill Allow/Deny with evidence; never paste live session tokens.

## Matrix

| Resource | Action | {role_cols} | Object-level | Evidence |
|----------|--------|-{role_sep}-|--------------|----------|
| example  | read   | {empty_role_cells} | | |

## Negative tests

| ID | Scenario | Expected | Result | Evidence |
|----|----------|----------|--------|----------|
| N1 | unauthenticated | 401/403 | | |
| N2 | wrong role | 403 | | |
| N3 | cross-tenant object | 403/404 | | |

## Assumptions

|
|
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--roles", default="anonymous,user,admin")
    args = parser.parse_args()
    roles = [r.strip() for r in args.roles.split(",") if r.strip()]
    if not roles:
        raise SystemExit("At least one role required")
    args.out.parent.mkdir(parents=True, exist_ok=True)
    if not args.out.exists():
        args.out.write_text(build(roles), encoding="utf-8")
    print(f"Ready: {args.out.resolve()}")


if __name__ == "__main__":
    main()
