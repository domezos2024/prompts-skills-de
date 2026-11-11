---
name: vollstaendige-release-pipeline
description: Use when preparing a verified software release from the current project state, bumping versions, building distribution packages, writing changelogs, or needing a gated publish-ready release workflow without accidental overwrite.
---

# Vollständige Release-Pipeline

## Overview

Erzeugt aus dem aktuellen Projektstand ein überprüftes, veröffentlichungsfähiges Release. Kernprinzip: **Istzustand und Version beweisen → bauen → Artefakte prüfen → Notes schreiben → nur mit Freigabe publizieren.** Kein Release bei kritischen Fehlern.

## When to Use

- Release vorbereiten (Version, Build, Pakete, Notes)
- Distributionsartefakte inkl. Prüfsummen erzeugen
- Veröffentlichungsprotokoll und Freigabe-Gate nötig

## When NOT to Use

- Nur CI-Pipeline-Design ohne Release-Artefakt → `ci-cd-pipeline-architekt`
- Nur Container-Image-Optimierung → `docker-und-container-optimierung`
- Hotfix-Deploy auf Server ohne Release-Paket → Server-/Backup-Skills

## Critical Guidelines

- MUST Repository-Zustand, Tags, Abhängigkeiten und Build-Anforderungen vor Versionierung erfassen.
- MUST Versionsbump nach bestehenden Projektregeln (SemVer/Changelog-Konvention).
- MUST Codeprüfung, automatisierte Tests und Release-Build vor Artefaktfreigabe ausführen.
- MUST Artefakte auf Vollständigkeit, Integrität (Checksummen) und Startfähigkeit prüfen.
- MUST Changelog und Release Notes aus tatsächlichen Änderungen ableiten.
- NEVER bei kritischen Fehlern oder roten Tests veröffentlichen.
- NEVER vorhandene Tags/Releases unbeabsichtigt überschreiben.
- NEVER Push, Tag-Push, Deploy oder Registry-Publish ohne explizite Nutzerfreigabe.
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill vollstaendige-release-pipeline --root .skill-runs/release
```

### PHASE 1 – DISCOVERY (Istzustand)

1. Git-Status, Branch, letzte Tags/Releases, dirty worktree erfassen.
2. Buildsystem, Abhängigkeiten, Release-Scripts, Zielkanäle dokumentieren.
3. Baseline: vorhandene Version, bekannte Blocker, CI-Status notieren.
4. Audit nach `references/release-checklist.md`.

**Gate:** Baseline + Freigabe-Zielkanal klar; keine unklaren Secrets nötig ohne Nutzer.

### PHASE 2 – PLANNING (Version & Pakete)

1. Neue Version nach Projektregeln bestimmen; Begründung dokumentieren.
2. Release-Pakete (Installer, Archives, Images) und Akzeptanzkriterien festlegen.
3. Rollback: Tag/Artefakt-Plan bei Fehlschlag.
4. Out-of-scope: Kanäle ohne Freigabe.

**Gate:** Versionsplan + Paketliste + Done-Kriterien.

### PHASE 3 – IMPLEMENTATION

1. Abhängigkeiten und Release-Metadaten kontrolliert aktualisieren.
2. Lint/Tests/Build ausführen; Fehler sofort beheben oder Release stoppen.
3. Distributionspakete erzeugen; Checksummen schreiben.
4. Changelog/Release Notes erstellen.

**Gate:** Artefakte + Checksummen vorhanden; kritische Checks grün.

### PHASE 4 – VALIDATION

1. Artefakte entpacken/installieren (Sandbox) und Startfähigkeit prüfen.
2. Checksummen verifizieren; Manifest gegen Checklist abgleichen.
3. Notes auf Vollständigkeit und Faktentreue prüfen.
4. Publish-Dry-Run nur wenn Tooling es ohne Side-Effects erlaubt.

**Gate:** Validierungsprotokoll ohne unbelegte Pass-Claims.

### PHASE 5 – DELIVERY

1. Delivery Report; Veröffentlichungsprotokoll vorbereiten.
2. Publish/Tag/Push **nur nach expliziter Nutzerfreigabe**.
3. Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/release --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Baseline | Tags, Version, Build, Tests |
| Version | Projektregeln, kein Blind-Bump |
| Artefakte | Build + Checksummen + Smoke |
| Publish | Nur mit User-Freigabe |
| Stop | Kritischer Fehler → kein Release |

## Red Flags

- Publish ohne Freigabe oder bei roten Tests
- Tag überschreiben / force-push
- Checksummen fehlen
- Release Notes ohne reale Diff-Basis
- Fertigmeldung ohne PHASE 4

## Resources

- `references/release-checklist.md`
- `scripts/scaffold_release_notes.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
