---
name: modernisierung-der-softwarearchitektur
description: Use when incrementally modernizing software architecture without a rewrite - mapping modules and couplings, choosing pragmatic target patterns, migrating with rollback plans, and validating builds, tests, and compatibility.
---

# Modernisierung der Softwarearchitektur

## Overview

Modernisiert die bestehende Architektur ohne unnötigen Komplettneubau. Kernprinzip: **Ist-Landschaft kartieren → Probleme & Optionen belegen → inkrementeller Plan mit Rollback → gezielte Umbauten → Build/Integration prüfen.** Keine Komplexität ohne nachweisbaren Nutzen.

## When to Use

- Enge Kopplung, Zyklen, fehlende Schichtentrennung, undurchsichtige Datenflüsse
- Dependency Injection / Modulgrenzen fehlen oder sind inkonsistent
- Schrittweise Modernisierung statt Big-Bang-Rewrite gewünscht

## When NOT to Use

- Nur lokale Code-Cleanup ohne Architekturziel → `autonome-codebereinigung-und-refaktorierung`
- Primär Dependency-/CVE-Arbeit → `beseitigung-von-abhaengigkeiten-und-technischen-schulden`
- Undokumentierter Totalschaden ohne Build → zuerst `rettungsmission-fuer-altcode`
- Rein UI-Designsystem → UI-Skills

## Critical Guidelines

- MUST Module, Datenflüsse, Schnittstellen und technische Abhängigkeiten zuerst erfassen.
- MUST Architekturprobleme (Kopplung, Zyklen, Verantwortungsdiffusion) mit Belegen listen.
- MUST Zielansätze am realen Projektbedarf vergleichen — nicht an Hype.
- MUST inkrementellen Migrationsplan mit Risiken und Rückfallstrategie erstellen.
- MUST Tests und technische Doku bei betroffenen Grenzen aktualisieren.
- NEVER Architekturkomplexität ohne nachweisbaren Nutzen einführen.
- NEVER Big-Bang-Rewrite als Default wählen.
- NEVER „fertig modernisiert“ ohne Build-/Integrationnachweis.
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill modernisierung-der-softwarearchitektur --root .skill-runs/arch-modernize
```

### PHASE 1 – DISCOVERY

1. Module, Einstiege, Datenflüsse, externe Interfaces inventarisieren.
2. Kopplung/Zyklen/Responsibility-Smells nach `references/architecture-migration-matrix.md` belegen.
3. Ist-Diagramm/Skizze unter `artifacts/arch-as-is/` ablegen.

**Gate:** Landschaftskarte + priorisierte Architekturprobleme.

### PHASE 2 – PLANNING

1. Zieloptionen vergleichen (Schichten, Hexagonal, Modulare Monolithe, klare Packages, DI …) — nur passende.
2. Inkremente mit Strangler/Anti-Corruption wo nötig; Risiko & Rollback pro Schritt.
3. Erfolgsmetriken: entkoppelte Grenzen, testbare Interfaces, stabile Builds.

**Gate:** Migrationsplan mit Entscheidungsprotokoll.

### PHASE 3 – IMPLEMENTATION

1. Gezielte Verbesserungen an Modulen, Interfaces, DI-Grenzen.
2. Aufrufer schrittweise umbiegen; Doppelpfade zeitlich begrenzen.
3. Tests für neue Grenzen; Doku/ADRs aktualisieren.

**Gate:** Geplante Inkremente integriert; Rollback-Pfad noch gangbar oder abgeschlossen dokumentiert.

### PHASE 4 – VALIDATION

1. Builds und Integrationstests; Kompatibilität und grobe Performance-Stichprobe.
2. Soll-Diagramm `artifacts/arch-to-be/`; offene Kopplungen listen.
3. Keine unbelegten „saubere Architektur“-Claims.

**Gate:** Validierungsprotokoll + aktualisierte Diagramme.

### PHASE 5 – DELIVERY

1. Delivery Report nach `_shared/references/delivery-report-template.md`.
2. Entscheidungsprotokoll, Migrationsergebnisse, Restschulden.
3. Checkpoint auf `done` setzen.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/arch-modernize --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Ist | Module, Flows, Zyklen kartieren |
| Soll | Nutzen-belegte Zielstruktur |
| Migrate | Inkremente + Rollback |
| Beweis | Build/IT + Diagramme |
| Stop | Komplexität ohne Nutzen → streichen |

## Red Flags

- Microservices „weil modern“ ohne Bedarf
- Kein Rollback
- Diagramme ohne Code-Bezug
- Tests nicht angepasst
- Fertig ohne Integrationstest

## Resources

- `references/architecture-migration-matrix.md`
- `scripts/scaffold_arch_decision_log.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
