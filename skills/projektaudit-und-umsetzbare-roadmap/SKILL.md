---
name: projektaudit-und-umsetzbare-roadmap
description: Use when auditing a real project's code, architecture, tests, docs, and build health, separating confirmed issues from speculation, scoring findings, producing an actionable roadmap, and implementing low-risk quick wins with test evidence.
---

# Projektaudit & umsetzbare Roadmap

## Overview

Untersucht den tatsächlichen Projektzustand und liefert einen realistischen Verbesserungsplan mit überprüfbaren Schritten. Kernprinzip: **Istzustand beweisen → bestätigte vs. vermutete Befunde trennen → scoren → Roadmap mit Akzeptanzkriterien → risikoarme Quick Wins umsetzen & testen.** Keine pauschalen Ratschläge; nichts „done“ ohne Umsetzung + Prüfung.

## When to Use

- Projektzustand unklar; Prioritäten fehlen
- Tech-Debt/Risiken sollen in eine umsetzbare Roadmap
- Auftrag: „Audit + Roadmap (+ Quick Wins)“

## When NOT to Use

- Voller STRICT Refactor/UI-Durchlauf → `strict-code-quality-refactoring-ui-ux`
- Nur Feature-Ideation → `produktchancen-und-funktionsentdeckung`
- Nur Docs → Doku-Skills

## Critical Guidelines

- MUST Code, Architektur, Tests, Doku und Buildfähigkeit analysieren.
- MUST Risiken, fehlende Funktionen, Bugs und Wartungsprobleme mit Belegen listen.
- MUST bestätigte Probleme von Vermutungen/Unprüfbarem trennen.
- MUST Schwere, Aufwand, Nutzen, Abhängigkeiten bewerten.
- MUST Roadmap mit atomaren Tasks und Akzeptanzkriterien liefern.
- MUST Quick Wins, Blocker und Vorarbeiten markieren; risikoarme Quick Wins umsetzen.
- MUST Änderungen testen und Roadmap aktualisieren.
- NEVER pauschale Verbesserungen ohne Projektbezug.
- NEVER Tasks als erledigt ohne Umsetzung+Prüfung.
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill projektaudit-und-umsetzbare-roadmap --root .skill-runs/projektaudit
```

### PHASE 1 – DISCOVERY

1. Struktur, Stack, Build, Tests, CI, Docs erfassen; Baseline-Metriken.
2. Befunde sammeln; Evidenzpflicht.
3. Audit-Scaffold mit `scripts/scaffold_audit_roadmap.py`.
4. `references/project-audit-priority-matrix.md` füllen.

**Gate:** Baseline + Befundliste mit Evidenzklassen.

### PHASE 2 – PLANNING

1. Score nach Schwere/Aufwand/Nutzen/Abhängigkeiten.
2. Roadmap: Quick Wins, Blocker, Vorarbeiten, Wellen.
3. Akzeptanzkriterien je Task; Out-of-scope.
4. Quick-Win-Auswahl (risikoarm, belegt).

**Gate:** Priorisierte Roadmap + Quick-Win-Plan.

### PHASE 3 – IMPLEMENTATION

1. Ausgewählte Quick Wins umsetzen.
2. Nach jedem Win kurz validieren.
3. Roadmap-Status aktualisieren (nicht spekulativ).

**Gate:** Quick Wins implementiert oder Blocker dokumentiert.

### PHASE 4 – VALIDATION

1. Build/Tests für geänderte Bereiche.
2. Audit-Claims stichprobenartig gegen Code re-checken.
3. Protokoll.

**Gate:** Keine „done“-Tasks ohne Nachweis.

### PHASE 5 – DELIVERY

1. Auditbericht, Roadmap, Testnachweise, RestRisiken.
2. Delivery Report; Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/projektaudit --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Evidence | Confirmed vs Hypothesis vs Unknown |
| Score | Severity × Impact / Effort |
| Roadmap | Atomic + acceptance |
| Wins | Low-risk only, then test |
| Stop | Done without proof |

## Red Flags

- Generische Best-Practice-Listen ohne Pfade
- Alles als P0
- Quick Wins ohne Tests
- Roadmap ohne Akzeptanzkriterien
- Fertigmeldung ohne PHASE 4

## Resources

- `references/project-audit-priority-matrix.md`
- `scripts/scaffold_audit_roadmap.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
