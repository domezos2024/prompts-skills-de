#!/usr/bin/env python3
"""Write/read workflow checkpoints for multi-phase skills.

Usage:
  python checkpoint.py init --skill NAME --root PATH
  python checkpoint.py set  --root PATH --phase N --step TEXT --status running|blocked|done
  python checkpoint.py note --root PATH --text TEXT
  python checkpoint.py show --root PATH
  python checkpoint.py validate-gate --root PATH --require-phase N
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _path(root: Path) -> Path:
    return root / ".skill-checkpoint.json"


def load(root: Path) -> dict:
    p = _path(root)
    if not p.exists():
        return {
            "skill": None,
            "phase": 0,
            "step": "",
            "status": "idle",
            "notes": [],
            "history": [],
            "updated_at": None,
        }
    return json.loads(p.read_text(encoding="utf-8"))


def save(root: Path, data: dict) -> None:
    root.mkdir(parents=True, exist_ok=True)
    data["updated_at"] = _now()
    _path(root).write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def cmd_init(args: argparse.Namespace) -> None:
    data = load(args.root)
    data["skill"] = args.skill
    data["phase"] = 1
    data["step"] = "DISCOVERY start"
    data["status"] = "running"
    data["history"].append({"at": _now(), "event": "init", "skill": args.skill})
    save(args.root, data)
    print(f"Initialized checkpoint for {args.skill} at { _path(args.root) }")


def cmd_set(args: argparse.Namespace) -> None:
    data = load(args.root)
    data["phase"] = args.phase
    data["step"] = args.step
    data["status"] = args.status
    data["history"].append(
        {"at": _now(), "event": "set", "phase": args.phase, "step": args.step, "status": args.status}
    )
    save(args.root, data)
    print(f"STATUS: PHASE {args.phase} | {args.step} | {args.status}")


def cmd_note(args: argparse.Namespace) -> None:
    data = load(args.root)
    data["notes"].append({"at": _now(), "text": args.text})
    save(args.root, data)
    print("Note recorded.")


def cmd_show(args: argparse.Namespace) -> None:
    data = load(args.root)
    print(json.dumps(data, indent=2, ensure_ascii=False))


def cmd_validate_gate(args: argparse.Namespace) -> None:
    data = load(args.root)
    ok = data.get("phase", 0) >= args.require_phase and data.get("status") in {"running", "done"}
    if not ok:
        raise SystemExit(
            f"GATE FAIL: need phase>={args.require_phase} with active status; got phase={data.get('phase')} status={data.get('status')}"
        )
    print(f"GATE PASS: phase={data.get('phase')} status={data.get('status')}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Skill workflow checkpoint helper")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_init = sub.add_parser("init")
    p_init.add_argument("--skill", required=True)
    p_init.add_argument("--root", type=Path, required=True)
    p_init.set_defaults(func=cmd_init)

    p_set = sub.add_parser("set")
    p_set.add_argument("--root", type=Path, required=True)
    p_set.add_argument("--phase", type=int, required=True)
    p_set.add_argument("--step", required=True)
    p_set.add_argument("--status", choices=["running", "blocked", "done"], required=True)
    p_set.set_defaults(func=cmd_set)

    p_note = sub.add_parser("note")
    p_note.add_argument("--root", type=Path, required=True)
    p_note.add_argument("--text", required=True)
    p_note.set_defaults(func=cmd_note)

    p_show = sub.add_parser("show")
    p_show.add_argument("--root", type=Path, required=True)
    p_show.set_defaults(func=cmd_show)

    p_gate = sub.add_parser("validate-gate")
    p_gate.add_argument("--root", type=Path, required=True)
    p_gate.add_argument("--require-phase", type=int, required=True)
    p_gate.set_defaults(func=cmd_validate_gate)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
