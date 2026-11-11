---
name: intelligente-datei-und-dokumentenautomatisierung
description: Use when automating file/document intake, classification, renaming, conversion, metadata extraction, and safe organize/archive flows with dry-run, duplicate/corrupt checks, and recoverable moves - runs convention discovery, rule pipeline design, implementation, and conflict/interruption tests without silent overwrite or delete.
---

# Intelligente Datei- und Dokumentenautomatisierung

## Overview

Automatisiert Erfassen, Prüfen, Umwandeln und Organisieren von Dateien. Kernprinzip: **Konventionen & Regeln → Pipeline mit Validierung → Dry-Run zuerst → sichere Move/Copy/Archive mit Audit.** Kein stilles Überschreiben oder Löschen; Originale bei Konvertierung erhalten.

## When to Use

- Verzeichnischaos; Regeln für Name/Zielordner fehlen
- Formatkonvertierung + Metadatenextraktion
- Duplikat-/Korrupt-/Unvollständig-Checks nötig
- Dry-Run, Vorschau und Wiederherstellung gefordert

## When NOT to Use

- Tabellen-ETL über APIs/DBs → `architekt-fuer-datenpipelines-und-etl`
- Event-Notifications → `intelligentes-benachrichtigungs-und-ereignisverarbeitungssystem`
- Rein manuelle Einmal-Sortierung ohne Automatisierung

## Critical Guidelines

- MUST Verzeichnisstrukturen, Typen und Ablagekonventionen vor Rules erfassen.
- MUST Erkennungs-/Klassifizierungs-/Naming-/Zielregeln explizit machen.
- MUST Validierung gegen korrupt, dupliziert, unvollständig.
- MUST Dry-Run und Protokoll vor destruktiven Moves.
- MUST bei Konflikten fail-safe (rename-with-suffix / quarantine), nicht silent overwrite.
- NEVER löschen/überschreiben ohne nachvollziehbares Audit und Recovery-Pfad.
- NEVER Konvertierung ohne Erhalt der Originale (Copy-then-convert).
- NEVER Prod-Ordner ohne Dry-Run-Freigabe umbauen.
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill intelligente-datei-und-dokumentenautomatisierung --root .skill-runs/file-docs
```

### PHASE 1 – DISCOVERY

1. Quell-/Zielbäume, Typen, Volumina, Naming-Ist erfassen.
2. Risiken: Kollisionen, Sonderzeichen, große Dateien, Rechte.
3. `scripts/scaffold_file_rules.py` für Regelwerk.
4. `references/file-document-automation-checklist.md`.

**Gate:** Inventar + Regelentwurf (noch nicht angewandt).

### PHASE 2 – PLANNING

1. Pipeline: detect → validate → classify → convert? → name → place → audit.
2. Idempotenz (Hash/Content-ID); Quarantäne-Ordner.
3. Dry-Run-Report-Format; Rollback/Manifest.
4. Testfälle: unicode, huge, conflict, abort mid-run.

**Gate:** Regelwerk mit Safety-Defaults.

### PHASE 3 – IMPLEMENTATION

1. Pipeline-Skripte/Services; Config für Rules.
2. Validierungen + Dedup; Convert mit Original-Erhalt.
3. Safe move/copy/archive + Manifest/Log.
4. Vorschau-/Dry-Run-Modus verpflichtend exponieren.

**Gate:** Dry-Run auf Sample liefert vollständigen Plan.

### PHASE 4 – VALIDATION

1. Dry-Run dann Apply auf isolierte Testdaten.
2. Sonderzeichen, große Dateien, Namenskonflikte, Abbruch/Resume.
3. Kein Datenverlust; Manifest ermöglicht Undo/Restore.
4. Docs der Ergebnisse und Recovery.

**Gate:** Testprotokoll + Recovery-Nachweis.

### PHASE 5 – DELIVERY

1. Delivery Report; Ausführungsbericht.
2. Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/file-docs --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Rules | Classify/Name/Target explizit |
| Safety | Dry-Run → Manifest → Apply |
| Convert | Original behalten |
| Konflikt | Quarantäne/Suffix, nie silent overwrite |
| Stop | Delete/Overwrite ohne Audit → verboten |

## Red Flags

- Apply ohne Dry-Run
- Überschreiben bei Namenskollision
- Originale nach Convert gelöscht
- Kein Manifest/Log
- Abbruch hinterlässt inkonsistenten Baum ohne Recovery

## Resources

- `references/file-document-automation-checklist.md`
- `scripts/scaffold_file_rules.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
