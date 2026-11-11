---
name: mcp-werkzeug-intelligenz-und-optimierung
description: Use when MCP tool calls are noisy, redundant, slow, or poorly selected by models, needing clearer tool descriptions/schemas, batch endpoints, structured errors, or before/after agent-task benchmarks - runs tool telemetry analysis, contract redesign, optimization, and measured comparison.
---

# MCP-Werkzeug-Intelligenz und Optimierung

## Overview

Verbessert MCP-Werkzeugnutzung für **weniger unnötige Calls, präzisere Auswahl und klarere Ergebnisse**. Kernprinzip: **Messung der Ist-Nutzung → Verträge schärfen → Batch/Errors → Before/After beweisen.** Keine Features entfernen hinter „Optimierung“.

## When to Use

- Agent wählt falsche Tools oder multipliziert Calls
- Tool-Namen/Descriptions/Schemas sind mehrdeutig
- Latenz, Payload-Größe oder Fehlerquote zu hoch
- Batch-Abfragen und strukturierte Fehlercodes fehlen

## When NOT to Use

- Neue MCP-Fähigkeiten hinzufügen → `erweiterung-der-mcp-server-faehigkeiten`
- Provider-/Modell-Failover → `intelligentes-modell-routing-und-failover`
- Kompletter Server-Rewrite ohne Nutzungsdaten

## Critical Guidelines

- MUST Tool-Definitionen, Schemas und typische Aufrufketten vor Änderungen erfassen.
- MUST Optimierungen an Messwerten oder reproduzierbaren Traces ausrichten.
- MUST Beschreibungen/Schemas so schärfen, dass Modellauswahl eindeutiger wird.
- MUST Batch-/Pagination-Optionen wo Call-Ketten redundant sind.
- MUST strukturierte Fehlercodes und stabile Return-Shapes.
- NEVER Funktionalität oder Safety „wegoptimieren“.
- NEVER Before/After-Gewinn ohne Vergleichsaufgaben behaupten.
- NEVER Breaking Schema-Changes ohne Migrationshinweis und Versionierung.
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill mcp-werkzeug-intelligenz-und-optimierung --root .skill-runs/mcp-optimize
```

### PHASE 1 – DISCOVERY

1. Tool-Katalog und Schemas inventarisieren.
2. Typische Agenten-Tasks und Call-Traces sammeln (vorhandene Logs/Messwerte).
3. Baseline mit `scripts/scaffold_tool_benchmark.py`.
4. `references/mcp-tool-optimization-checklist.md`: Duplikate, Ambiguität, Latenz, Payload.

**Gate:** Baseline-Bericht (Calls/Task, Fehler, Latenz) existiert.

### PHASE 2 – PLANNING

1. Description/Schema-Rewrite-Plan je problematischem Tool.
2. Batch-Kandidaten und Response-Shape-Verträge.
3. Fehlercode-Taxonomie; Idempotenz-Hinweise in Docs.
4. Repräsentative Benchmark-Tasks festnageln.

**Gate:** Änderungsplan mit messbaren Zielen (z. B. −X% Calls).

### PHASE 3 – IMPLEMENTATION

1. Descriptions/Schemas schärfen; Breaking Changes versionieren.
2. Batch-/Filter-/Field-Selection wo sinnvoll.
3. Strukturierte Errors; überflüssige Tools deprecaten (nicht hard-delete ohne Pfad).
4. Docs aktualisieren.

**Gate:** Geänderte Tools lauffähig; Safety unverändert oder verbessert.

### PHASE 4 – VALIDATION

1. Gleiche Benchmark-Tasks vor/nach ausführen.
2. Call-Count, Fehlerrate, Latenz, Ergebnisqualität vergleichen.
3. Security/Auth-Regression prüfen.
4. Restambiguitäten dokumentieren.

**Gate:** Benchmark-Bericht mit echten Zahlen.

### PHASE 5 – DELIVERY

1. Delivery Report + aktualisierte Tool-Doku.
2. Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/mcp-optimize --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Baseline | Traces + Calls/Task |
| Schärfen | Name/Description/Schema |
| Effizienz | Batch/Filter/Fields |
| Beweis | Before/After Benchmark |
| Stop | Kein Messvergleich → kein „schneller“ |

## Red Flags

- Optimierung ohne Baseline
- Schema-Break ohne Version
- Safety-Checks entfernt
- „Weniger Calls“ durch stilles Feature-Drop
- Erfundene Benchmark-Zahlen

## Resources

- `references/mcp-tool-optimization-checklist.md`
- `scripts/scaffold_tool_benchmark.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
