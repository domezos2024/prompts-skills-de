---
name: performance-profiling-und-optimierung
description: Use when reducing runtime, memory, or system load with measured evidence - establishing reproducible benchmarks, profiling bottlenecks, applying behavior-preserving optimizations, and comparing before/after metrics without unverified claims.
---

# Performance-Profiling und Optimierung

## Overview

Reduziert Laufzeit, Speicherverbrauch und unnötige Systemlast anhand messbarer Ergebnisse. Kernprinzip: **Szenarien fixieren → reproduzierbare Baseline → Engpässe belegen → gezielt optimieren → Vorher/Nachher vergleichen.** Keine Optimierung ohne Messung.

## When to Use

- App/API ist langsam, speicherhungrig oder I/O-lastig
- Startzeiten oder Latenz kritisch
- Vermutete Hotspots sollen datengetrieben bestätigt/widerlegt werden

## When NOT to Use

- Refactor nur für Lesbarkeit ohne Perf-Ziel → `autonome-codebereinigung-und-refaktorierung`
- Architekturumbau als Selbstzweck → `modernisierung-der-softwarearchitektur`
- UI-Cosmetik ohne Messziel → UI-Skills
- Keine Möglichkeit zu messen und trotzdem „schneller“ behaupten — dann Skill nicht als Erfolg schließen

## Critical Guidelines

- MUST wichtige Nutzungsszenarien und performancekritische Komponenten zuerst identifizieren.
- MUST reproduzierbare Benchmarks/Profiling vor Änderungen einrichten.
- MUST CPU, RAM, I/O, Startzeiten und relevante Latenzen messen (was im Kontext greifbar ist).
- MUST Engpässe in Algo/Datenzugriff/Sync/Caching analysieren und belegen.
- MUST Verhalten erhalten; nach jeder größeren Änderung neu messen.
- NEVER Leistungsversprechen ohne Messwerte.
- NEVER Mikro-Optimierungen ohne Hotspot-Beweis priorisieren.
- NEVER „xx% schneller“ ohne vergleichbare Bedingungen (Hardware, Daten, Warmup).
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill performance-profiling-und-optimierung --root .skill-runs/perf
```

### PHASE 1 – DISCOVERY

1. Kritische Szenarien und SLAs/Ziele (falls vorhanden) festhalten.
2. Messmethode wählen (Profiler, Benchmark-Harness, Browser-Perf, load test — projektpassend).
3. Baseline unter `artifacts/perf-baseline/` nach `references/performance-benchmark-matrix.md`.

**Gate:** Reproduzierbare Baseline + Szenarioliste.

### PHASE 2 – PLANNING

1. Hotspots aus Profilen priorisieren (P0 = klarer Engpass mit Impact).
2. Optimierungsoptionen mit Aufwand/Risiko; Hypothesen formulieren.
3. Abbruchkriterien: kein messbarer Gewinn → Revert erwägen.

**Gate:** Plan mit Hypothesen und Messpunkten.

### PHASE 3 – IMPLEMENTATION

1. Gezielte Optimierungen (Algorithmus, Batching, Caching, I/O, Sync) umsetzen.
2. Verhaltenstests/Smoke parallel halten.
3. Nach größerem Schritt: Messung wiederholen und speichern.

**Gate:** Änderungen integriert; Zwischenmessungen dokumentiert.

### PHASE 4 – VALIDATION

1. Vorher/Nachher unter vergleichbaren Bedingungen.
2. Regressions (Korrektheit + andere Szenarien) prüfen.
3. Verbleibende Engpässe ehrlich listen.

**Gate:** Performancebericht mit Zahlen; keine unbelegten Claims.

### PHASE 5 – DELIVERY

1. Delivery Report nach `_shared/references/delivery-report-template.md`.
2. Benchmark-Ergebnisse, Methodik, Restengpässe.
3. Checkpoint auf `done` setzen.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/perf --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Baseline | Reproduzierbar messen |
| Fokus | Hotspot zuerst |
| Change | Verhalten erhalten |
| Beweis | Before/After gleiche Konditionen |
| Stop | Keine Zahl → kein Optimierungs-Claim |

## Red Flags

- Optimieren ohne Profiler/Benchmark
- Cache ohne Invalidierungsstrategie
- Vergleich Warm vs. Cold vermischt
- „Gefühlt schneller“
- Fertig ohne Matrix

## Resources

- `references/performance-benchmark-matrix.md`
- `scripts/init_perf_run.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
