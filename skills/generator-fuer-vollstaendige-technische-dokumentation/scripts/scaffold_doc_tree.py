#!/usr/bin/env python3
"""Scaffold a technical documentation tree with placeholders.

Usage:
  python scaffold_doc_tree.py --out docs
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

FILES = {
    "README.md": """# Project documentation index

- Created (UTC): {ts}
- Status: draft

## Sections

- [Architecture](architecture.md)
- [Configuration](configuration.md)
- [API / Tools](api-reference.md)
- [Development](development.md)
- [Troubleshooting](troubleshooting.md)
- [Verification log](verification-log.md)
""",
    "architecture.md": """# Architecture

## Overview

## Modules

## Data / control flow

## Boundaries & constraints
""",
    "configuration.md": """# Configuration

## Required settings

## Optional settings

## Environment variables

| Name | Required | Description | Verified |
|------|----------|-------------|----------|
| | | | |
""",
    "api-reference.md": """# API / Tool reference

Document only surfaces that exist in code.

| Surface | Entry | Auth | Notes | Verified |
|---------|-------|------|-------|----------|
| | | | | |
""",
    "development.md": """# Development guide

## Setup

## Common tasks

## Tests
""",
    "troubleshooting.md": """# Troubleshooting

| Symptom | Likely cause | Fix | Verified |
|---------|--------------|-----|----------|
| | | | |
""",
    "verification-log.md": """# Documentation verification log

- Created (UTC): {ts}

| Command / step | Result | Notes |
|----------------|--------|-------|
| | Pass/Fail/Skipped | |
""",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).isoformat()
    for name, body in FILES.items():
        path = args.out / name
        if not path.exists():
            path.write_text(body.format(ts=ts), encoding="utf-8")
    print(f"Ready: {args.out.resolve()}")


if __name__ == "__main__":
    main()
