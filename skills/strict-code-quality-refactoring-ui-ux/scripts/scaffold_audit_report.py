#!/usr/bin/env python3
"""Scaffold AUDIT-REFACTOR-UIUX-REPORT.md for STRICT workflow.

Usage:
  python scaffold_audit_report.py --out AUDIT-REFACTOR-UIUX-REPORT.md
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

TEMPLATE = """# AUDIT-REFACTOR-UIUX-REPORT

- Created (UTC): {ts}
- Project:
- STRICT skill run root: `.skill-runs/strict`

## 1. Projektübersicht

- Architektur:
- Technologie-Stack:
- Analysierte Bereiche:

## 2. Ursprüngliche Probleme

| Fundstelle | Beschreibung | Schwere | Begründung / Evidence |
|------------|--------------|---------|------------------------|
| | | P0-P3 | |

## 3. Durchgeführte Verbesserungen

| Dateien | Behobenes Problem | Konkreter Vorteil |
|---------|-------------------|-------------------|
| | | |

## 4. Refactoring

- Entfernte Redundanzen:
- Vereinfachte Strukturen:
- Architekturverbesserungen:
- Bereinigte Abhängigkeiten:

## 5. UI/UX

- Usability-Probleme behoben:
- Navigation:
- Statusanzeigen:
- Fehler-/Erfolgsrückmeldungen:
- Accessibility:

## 6. Tests

| Test / Check | Result | Notes |
|--------------|--------|-------|
| Build | | |
| Unit | | |
| Integration | | |
| UI / manual | | |
| A11y | | |
| Security | | |

Nicht ausführbar = `NICHT GETESTET` + Grund.

## 7. Performance

| Metric | Before | After | Method | Verified? |
|--------|--------|-------|--------|-----------|
| | | | | |

Unbelegte Prozentangaben verboten.

## 8. Restprobleme

| Issue | Warum offen | Nächster Schritt |
|-------|-------------|------------------|
| | | |

## 9. Strenge Qualitätsbewertung (0–100)

| Kategorie | Punkte | Begründung / Evidence |
|-----------|--------|------------------------|
| Codequalität | | |
| Architektur | | |
| Performance | | |
| Sicherheit | | |
| Wartbarkeit | | |
| Funktionalität | | |
| UI-Design | | |
| UX/Usability | | |
| Accessibility | | |
| Testabdeckung und Testqualität | | |

**Gesamtbewertung:**
**Nicht ausreichend prüfbare Kategorien:** (keine Fantasiezahlen)

## Definition of Done

Siehe `skills/strict-code-quality-refactoring-ui-ux/references/definition-of-done.md` – nur mit Nachweis abhaken.
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    if not args.out.exists():
        args.out.write_text(
            TEMPLATE.format(ts=datetime.now(timezone.utc).isoformat()),
            encoding="utf-8",
        )
    print(f"Ready: {args.out.resolve()}")


if __name__ == "__main__":
    main()
