---
name: rettungsmission-fuer-altcode
description: Use when stabilizing poorly documented or legacy software - reconstructing entry points and behavior, restoring a reproducible build, adding characterization tests, fixing critical defects safely, and documenting operations for controlled future change.
---

# Rettungsmission für Altcode

## Overview

Stabilisiert schlecht dokumentierte oder veraltete Anwendungen und macht sie wieder zuverlässig wartbar. Kernprinzip: **Verstehen & Build wiederherstellen → Verhalten charakterisieren → kritische Defekte unter Tests sanieren → Betriebsdoku.** Keine Helden-Refactors ohne Sicherheitsnetz.

## When to Use

- Legacy-Code ohne verlässliche Doku, fragile Builds, unklare Einstiege
- Änderungen sind riskant, weil Verhalten unbekannt ist
- Ziel: reproduzierbarer Build + Kernfunktionen nachweisbar + kontrollierte Weiterarbeit

## When NOT to Use

- Saubere Codebase, nur Style-Refactor → `autonome-codebereinigung-und-refaktorierung`
- Geplante Architektur-Modernisierung auf stabilem Fundament → `modernisierung-der-softwarearchitektur`
- Nur Dependency-Bump auf grünem Build → `beseitigung-von-abhaengigkeiten-und-technischen-schulden`
- Greenfield-Feature ohne Legacy-Druck

## Critical Guidelines

- MUST Code, Config, Abhängigkeiten und tatsächliche Einstiegspunkte zuerst untersuchen.
- MUST wesentliche Funktionen und Datenflüsse rekonstruieren (belegt, nicht geraten).
- MUST reproduzierbare Dev-/Build-Umgebung herstellen bevor Großänderungen.
- MUST Charakterisierungstests für bestehendes Verhalten ergänzen bevor riskanter Umbau.
- MUST kritische Fehler und nicht unterstützte Interfaces identifizieren und priorisieren.
- MUST schrittweise unter Testabsicherung refaktorieren/modernisieren.
- MUST technische Betriebs- und Wartungsdokumentation erstellen.
- NEVER Big-Bang-Rewrite als ersten Schritt.
- NEVER „Tests später“ bei Verhaltensänderungen.
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill rettungsmission-fuer-altcode --root .skill-runs/legacy-rescue
```

### PHASE 1 – DISCOVERY

1. Einstiege (main, Server-Start, Jobs, UI-Hosts), Config, Deps, Runtime-Annahmen kartieren.
2. Funktionen/Datenflüsse nach `references/legacy-stabilization-checklist.md` rekonstruieren.
3. Risiko-Hotspots und „unbekanntes Verhalten“ markieren.
4. Notizen unter `artifacts/legacy-map/`.

**Gate:** Landkarte + Einstiegsnachweis + Risikoliste.

### PHASE 2 – PLANNING

1. Build-/Env-Wiederherstellung als erstes Inkrement planen.
2. Charakterisierungs-Testplan für Kernflows.
3. Danach erst: Defektfixes / vorsichtige Refactors mit Rollback.

**Gate:** Stabilisierungsplan mit Reihenfolge Build → Tests → Fix.

### PHASE 3 – IMPLEMENTATION

1. Reproduzierbaren Build/Dev-Setup herstellen (Scripts/Docs im Repo).
2. Charakterisierungstests für Ist-Verhalten schreiben (auch wenn „hässlich“).
3. Kritische Defekte und blockierende Schnittstellen unter Tests adressieren.
4. Kleine Refactors nur hinter grünen Charakterisierungstests.

**Gate:** Build reproduzierbar; Kernflows testgeschützt; P0-Blocker behoben oder begründet.

### PHASE 4 – VALIDATION

1. Kernfunktionen manuell + automatisiert verifizieren.
2. Checkliste abschließen; Rest-Risiken listen.
3. Keine unbelegten „stabil“-Claims.

**Gate:** Nachweisbare Kernfunktion + Test-/Build-Protokolle.

### PHASE 5 – DELIVERY

1. Delivery Report nach `_shared/references/delivery-report-template.md`.
2. Betriebs-/Wartungsdoku, Architekturübersicht, Teststatus, nächste sichere Schritte.
3. Checkpoint auf `done` setzen.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/legacy-rescue --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Verstehen | Einstiege + Flows kartieren |
| Boden | Build reproduzierbar machen |
| Netz | Charakterisierungstests |
| Retten | Kleine Fixes unter Tests |
| Stop | Umbau ohne Build/Tests → verboten |

## Red Flags

- Rewrite vor Build-Fix
- Verhalten „ich glaube…“ ohne Beweis
- Deps upgraden ohne Charakterisierung
- Doku nur mündlich
- Fertig ohne Kernflow-Nachweis

## Resources

- `references/legacy-stabilization-checklist.md`
- `scripts/scaffold_legacy_map.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
