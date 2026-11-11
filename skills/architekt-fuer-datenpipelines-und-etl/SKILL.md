---
name: architekt-fuer-datenpipelines-und-etl
description: Use when building or hardening multi-source ETL/data pipelines, defining unified schemas and data-quality checks, adding incremental loads with checkpoints, or testing restart/partial failure and idempotent re-runs - runs source discovery, model design, pipeline implementation, and quality-gated delivery without mutating originals unless required.
---

# Architekt für Datenpipelines und ETL

## Overview

Baut Pipelines, die Daten aus mehreren Quellen **zuverlässig vereinheitlichen**. Kernprinzip: **Quellen & Qualität verstehen → kanonisches Modell → idempotente ETL mit Checkpoints → DQ-Gates.** Originale nicht ungefragt mutieren; PII schützen.

## When to Use

- Mehrere Quellen → einheitliches Zielmodell
- Inkrementelle Loads, Wiederanlauf, Teilfehler
- Datenqualität (Vollständigkeit, Duplikate, Integrität) sichern
- Lineage/Betriebsdoku gefordert

## When NOT to Use

- Cross-App Business-Automation ohne analytisches Modell → `systemuebergreifende-workflow-automatisierung`
- Reine API-Client-Integration → `ingenieur-fuer-rest-api-integration`
- Dokumenten-Datei-Sorting ohne tabellarische ETL → `intelligente-datei-und-dokumentenautomatisierung`

## Critical Guidelines

- MUST Quellen, Formate, Intervalle und Zielstruktur vor Coding erfassen.
- MUST Qualitätsprobleme (Missing, Duplikate, Inkonsistenzen) analysieren.
- MUST kanonisches Modell mit Validierungsregeln definieren.
- MUST inkrementelle Aktualisierung, Fehlerbehandlung und Checkpoints.
- MUST DQ-Checks für Vollständigkeit/Integrität vor „Publish“.
- NEVER Originalquellen ohne Anforderung überschreiben.
- NEVER PII ungeschützt loggen/exportieren.
- NEVER Re-Runs mit Doppelzählung ohne Idempotenzstrategie.
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill architekt-fuer-datenpipelines-und-etl --root .skill-runs/etl
```

### PHASE 1 – DISCOVERY

1. Quellen, Schemas, SLAs, Volumina, PII-Felder inventarisieren.
2. DQ-Stichprobe; Befunde priorisieren.
3. `scripts/scaffold_pipeline_spec.py` für Pipeline-Spec.
4. `references/etl-pipeline-checklist.md`.

**Gate:** Quelleninventar + DQ-Befundliste.

### PHASE 2 – PLANNING

1. Kanonisches Modell + Mapping je Quelle.
2. Extract/Transform/Load-Schritte; Incremental Keys/Watermarks.
3. Checkpoint-/Retry-/Quarantäne-Strategie.
4. DQ-Gate-Metriken und Lineage-Felder.

**Gate:** Spec mit messbaren DQ-Schwellen.

### PHASE 3 – IMPLEMENTATION

1. Extract → Transform → Validate → Load.
2. Incremental + Idempotent Upserts/Partition Overwrites.
3. Quarantäne für Bad Records; strukturierte Logs.
4. Observability: rows in/out, lag, fail rate.

**Gate:** Pipeline läuft auf Test-/Sample-Daten.

### PHASE 4 – VALIDATION

1. Wiederanlauf nach Abbruch.
2. Teilfehler und wiederholte Ausführungen ohne Duplikat-Effekt.
3. DQ-Gates Pass/Fail belegen.
4. PII-/Rechte-Check der Outputs.

**Gate:** Validierungsprotokoll + Lineage-Notiz.

### PHASE 5 – DELIVERY

1. Delivery Report; Betriebsanleitung und Herkunft.
2. Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/etl --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Modell | Kanonisch + Validierung |
| Load | Incremental + idempotent |
| DQ | Gate vor Publish |
| Safety | Originale/PII schützen |
| Stop | Re-Run verdoppelt Daten → Fail |

## Red Flags

- Full-Load als einziges Modell ohne Bedarf
- Originale überschrieben
- Keine Quarantäne für Bad Rows
- „Qualität ok“ ohne Metriken
- Secrets/PII in Pipeline-Logs

## Resources

- `references/etl-pipeline-checklist.md`
- `scripts/scaffold_pipeline_spec.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
