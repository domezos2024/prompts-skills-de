---
name: changelog-und-release-dokumentation
description: Use when producing accurate changelogs and release notes from real commits/PRs/diffs - classifying changes, verifying against implementation, documenting migrations and known limits, and marking unpublished work clearly.
---

# Changelog- & Release-Dokumentation

## Overview

Erzeugt präzise Versionshinweise und technische Release-Dokumentation aus **tatsächlichen** Projektänderungen. Kernprinzip: **Versionsspanne bestimmen → Commits/PRs/Diffs analysieren → gegen Code verifizieren → User Notes + Tech Changelog + Migrationen.** Keine Features behaupten, die nicht prüfbar sind.

## When to Use

- Release Notes / CHANGELOG fehlen oder sind ungenau
- Migrationen/Breaking Changes müssen kommuniziert werden
- Auftrag: „Changelog & Release-Doku“

## When NOT to Use

- Store-Listing-ASO → `app-store-release-und-listing-optimierung`
- Vollständige Tech-Docs → `generator-fuer-vollstaendige-technische-dokumentation`
- Git-History umschreiben

## Critical Guidelines

- MUST letzten veröffentlichten Stand und aktuellen Repo-Zustand ermitteln.
- MUST relevante Commits, PRs und Dateiänderungen analysieren.
- MUST nach Features, Fixes, Perf, Security, Breaking Changes ordnen.
- MUST Commit-Messages mit tatsächlicher Implementierung abgleichen.
- MUST Endnutzer-Versionshinweise und technisches Changelog erstellen.
- MUST Migrationen, Config-Änderungen und bekannte Limits dokumentieren.
- NEVER nicht implementierte Features behaupten.
- NEVER unveröffentlichte Änderungen als released kennzeichnen.
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill changelog-und-release-dokumentation --root .skill-runs/changelog
```

### PHASE 1 – DISCOVERY

1. Letzte Release-Version/Tag und HEAD bestimmen.
2. Commits/PRs/Diffs im Range sammeln.
3. Scaffold mit `scripts/scaffold_changelog.py`.
4. `references/changelog-taxonomy.md` anwenden.

**Gate:** Versionsspanne + Rohänderungsliste.

### PHASE 2 – PLANNING

1. Klassifikation der Änderungen; Dubletten mergen.
2. Verifikationsstichproben (Message ↔ Diff) planen.
3. Zielartefakte: USER notes, TECH changelog, MIGRATION, KNOWN ISSUES.

**Gate:** Klassifizierter Draft-Plan.

### PHASE 3 – IMPLEMENTATION

1. Nutzerverständliche Release Notes schreiben.
2. Technisches Changelog mit Pfaden/Modulen ergänzen.
3. Migrationen/Config/Breaking dokumentieren.
4. Bestehende Release-Docs konsistent aktualisieren.

**Gate:** Dokumente vorhanden; Claims verankert.

### PHASE 4 – VALIDATION

1. Stichproben gegen Diff/Code; falsche Claims entfernen.
2. Unpublished klar markieren.
3. Protokoll.

**Gate:** Keine ungeprüften Feature-Claims.

### PHASE 5 – DELIVERY

1. Finales Paket + Restunsicherheiten.
2. Delivery Report; Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/changelog --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Range | Last release → HEAD |
| Sort | Feat/Fix/Perf/Sec/Breaking |
| Verify | Message ↔ Diff |
| Split | User notes vs tech log |
| Stop | Unverified feature claims |

## Red Flags

- Release Notes nur aus Commit-Titeln ohne Diff
- Breaking Changes verschwiegen
- „Released“ ohne Tag/Publish
- Fertigmeldung ohne Verifikation

## Resources

- `references/changelog-taxonomy.md`
- `scripts/scaffold_changelog.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
