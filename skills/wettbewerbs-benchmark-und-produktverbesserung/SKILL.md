---
name: wettbewerbs-benchmark-und-produktverbesserung
description: Use when benchmarking an existing product against real competitors with verifiable sources, identifying true gaps and differentiators, scoring improvements, implementing one feasible upgrade, and updating the product roadmap with test evidence.
---

# Wettbewerbs-Benchmark & Produktverbesserung

## Overview

Vergleicht die vorhandene Anwendung mit relevanten Alternativen und leitet **konkrete, umsetzbare** Verbesserungen ab. Kernprinzip: **eigene Position belegen → 5 echte Wettbewerber mit Quellen → Lücken scoren → eine machbare Verbesserung bauen → Roadmap updaten.** Keine erfundenen Features/Preise/Reviews; kein Copy fremder Designs/Code.

## When to Use

- Produktstrategie braucht evidenzbasierten Wettbewerbsblick
- Feature-Gaps sollen priorisiert und mindestens ein Gap geschlossen werden
- Auftrag: „Benchmark + Verbesserung“

## When NOT to Use

- Nur interne Feature-Ideation ohne Wettbewerb → `produktchancen-und-funktionsentdeckung`
- Nur Store-Listing-ASO → `app-store-release-und-listing-optimierung`
- Competitor-Code/Design klonen (verboten)

## Critical Guidelines

- MUST eigenen Funktionsumfang und Positionierung zuerst dokumentieren.
- MUST genau fünf vergleichbare, tatsächlich existierende Produkte mit überprüfbaren Quellen recherchieren.
- MUST Features, UX, Plattformen und nachvollziehbare Preismodelle vergleichen.
- MUST echte Lücken vs. mögliche Differenziatoren trennen.
- MUST Verbesserungen nach Nutzen/Aufwand/Folgekosten bewerten und eine machbare Verbesserung implementieren.
- NEVER Wettbewerber-Features, Preise oder Bewertungen erfinden.
- NEVER geschützte Designs oder fremden Quellcode übernehmen.
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill wettbewerbs-benchmark-und-produktverbesserung --root .skill-runs/benchmark
```

### PHASE 1 – DISCOVERY

1. Eigenes Produkt: Features, Positionierung, Plattformen, Pricing (falls vorhanden).
2. Kandidatenliste potenzieller Wettbewerber; Existenz prüfen.
3. Benchmark-Scaffold mit `scripts/scaffold_competitor_matrix.py`.
4. `references/competitive-benchmark-matrix.md` füllen.

**Gate:** Eigenprofil + 5 Wettbewerber mit Quellenangaben.

### PHASE 2 – PLANNING

1. Vergleichsmatrix fertigstellen; Lücken und Differenziatoren markieren.
2. Maßnahmen scoren (Nutzen, Aufwand, Folgekosten, Risiko).
3. Eine Verbesserung mit klarer Abgrenzung zu Wettbewerbern wählen.
4. Implementierungsplan mit Akzeptanzkriterien und Rollback.

**Gate:** Priorisierte Maßnahmen + gewählter Implementierungsschritt.

### PHASE 3 – IMPLEMENTATION

1. Gewählte Verbesserung technisch umsetzen (eigene Lösung, kein Clone).
2. Tests/UI nach Bedarf; Produkt-Roadmap aktualisieren.
3. Smoke der betroffenen Flows.

**Gate:** Verbesserung bedienbar; keine offenen P0 im Scope.

### PHASE 4 – VALIDATION

1. Akzeptanzkriterien und verfügbare Tests.
2. Quellenliste der Wettbewerbsclaims erneut gegenprüfen.
3. Regressionen fixen; Protokoll.

**Gate:** Validierungsprotokoll + Quellentreue.

### PHASE 5 – DELIVERY

1. Benchmark-Report, Roadmap, Testnachweise.
2. Delivery Report; Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/benchmark --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Own | Features & Position belegen |
| Comp | 5 echte Produkte + Quellen |
| Gap | Lücken vs. Differenziatoren |
| Build | 1 machbare Verbesserung |
| Stop | Erfundene Competitor-Daten |

## Red Flags

- Wettbewerber ohne URL/Quelle
- Preise „geschätzt“ als Fakt dargestellt
- UI 1:1 nachgebaut
- Viele Vorschläge, null Implementierung
- Fertigmeldung ohne PHASE 4

## Resources

- `references/competitive-benchmark-matrix.md`
- `scripts/scaffold_competitor_matrix.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
