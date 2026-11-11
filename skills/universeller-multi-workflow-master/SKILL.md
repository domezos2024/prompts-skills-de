---
name: universeller-multi-workflow-master
description: Use when orchestrating multiple specialized skills/prompts toward one project outcome - running discovery, planning, sequenced implementation, cross-cutting validation, and delivery with an explicit activation list, checkpoints, and no invented tool successes.
---

# Universeller Multi-Workflow-Master

## Overview

Koordiniert als interdisziplinärer Principal Engineer mehrere spezialisierte Workflows zu **einem** Gesamtergebnis. Kernprinzip: **Aktivierungsliste festlegen → Discovery über das Gesamtprojekt → abhängigkeitsgeordnete Orchestrierung → Implementierung je aktiviertem Skill → gemeinsame Validation → Delivery.** Unnötige Komplexität und parallele Schreibkonflikte vermeiden.

## When to Use

- Mehrere Prompt-/Skill-Nummern/Titel sollen in einem Auftrag zusammenlaufen
- Gesamtziel ist klar, Teilaufgaben sind domänenübergreifend
- Orchestrierung mit Checkpoints statt isolierter Einzelläufe

## When NOT to Use

- Nur ein einzelner Domänen-Skill reicht (direkt diesen Skill nutzen)
- Voller STRICT 9-Phasen-Audit/Refactor → `strict-code-quality-refactoring-ui-ux`
- Rein spekulative Strategie ohne Ausführungsauftrag

## Critical Guidelines

- MUST `PROJEKT`, `GESAMTZIEL` und `AKTIVIERTE WORKFLOWS` zu Beginn explizit machen.
- MUST Aktivierungsliste gegen vorhandene Skills/Prompts mappen (`references/activation-catalog.md`).
- MUST Phasen 1–5 aus Master-Prompt strikt einhalten; Statuszeile führen.
- MUST Teilaufgaben atomar, abhängigkeitsgeordnet und mit messbaren Akzeptanzkriterien planen.
- MUST vorhandene Tools/Konventionen nutzen; keine Doppelimplementierungen.
- MUST Builds/Tests/UI-Checks soweit möglich ausführen; keine erfundenen Erfolge.
- MUST gefährliche/irreversible Aktionen ohne Freigabe stoppen.
- NEVER Workflow als abgeschlossen melden ohne Validation (oder dokumentierten Blocker).
- NEVER parallele Agenten auf dieselben Dateien schreiben lassen.
- ALWAYS `_shared` Iron Laws und Phase Protocol befolgen.

## Workflow

### PHASE 0 – Checkpoint & Aktivierung

```bash
python skills/_shared/scripts/checkpoint.py init --skill universeller-multi-workflow-master --root .skill-runs/master
python skills/universeller-multi-workflow-master/scripts/scaffold_activation_plan.py --out artifacts/master-orchestration
```

1. Projektpfad, Gesamtziel, aktivierte Workflow-Nummern/Titel erfassen.
2. Mapping auf Skills via `references/activation-catalog.md` schreiben.
3. Out-of-scope und Freigabe-Gates (Publish, Live-Pay, destruktives Git) notieren.

**Gate:** Aktivierungsliste + Orchestrierungsordner existieren.

### PHASE 1 – DISCOVERY

1. Projekt und Umgebung untersuchen (Struktur, Stack, Tools, Regeln).
2. Abhängigkeiten, bestehende Funktionen, Build-/Teststatus erfassen.
3. Risiken und vorhandene Projektregeln (AGENTS/CLAUDE/CI) lesen.
4. Pro aktiviertem Workflow: kurze Domänen-Baseline (was fehlt / was blockiert).

**Gate:** Architekturkurzüberblick + Baseline + Risiko-/Abhängigkeitsliste.

### PHASE 2 – PLANNING

1. Alle Teilaufgaben atomar zerlegen; Abhängigkeitsgraph bilden.
2. Reihenfolge der aktivierten Skills festlegen (keine Schreibkonflikte).
3. Messbare Akzeptanzkriterien, Checkpoints und Rollback je Paket.
4. Parallelisierung nur für unabhängige Lese-/Analysearbeit.

**Gate:** Geordneter Ausführungsplan mit Done-Definitionen.

### PHASE 3 – IMPLEMENTATION

1. Aktivierte Skills nacheinander (oder konfliktfrei parallel lesend) ausführen.
2. Pro Skill: dessen Phasen/Gates respektieren; Master-Statuszeile aktualisieren.
3. Änderungen direkt im Projekt; Konventionen wahren; Nutzerdaten erhalten.
4. Blocker konkret melden; unabhängig davon ausführbare Pakete weiterführen.

**Gate:** Geplante ausführbare Pakete umgesetzt oder mit Blocker dokumentiert.

### PHASE 4 – VALIDATION

1. Builds, Tests, statische Analysen ausführen (soweit vorhanden).
2. UI-Interaktionen prüfen, wenn UI-Workflows aktiv waren.
3. Security-/Kompatibilitätsaspekte der Änderungen kontrollieren.
4. Fehler reproduzieren, fixen, relevante Tests wiederholen.
5. Querschnitt: Widersprüche zwischen Workflow-Outputs bereinigen.

**Gate:** Validierungsprotokoll; keine unbelegten Pass-Claims.

### PHASE 5 – DELIVERY

1. Erforderliche Dokumentation aktualisieren.
2. Änderungsübersicht: erledigt / erreicht / Rest / nicht geprüft.
3. Release-Artefakte nur wenn aktivierte Workflows und User das verlangen.
4. Master Delivery Report; Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/master --phase 5 --step "delivery complete" --status done
```

**Abschlusskriterium:** Alle ausführbaren Aufgaben implementiert und geprüft. Nicht Ausführbares mit Grund und nächstem Schritt dokumentiert.

## Operative Regeln (verbindlich)

1. Autonom innerhalb Berechtigungen und Sicherheitsgrenzen.
2. Immer Phase + Arbeitsschritt anzeigen.
3. Keine unnötigen Rückfragen bei sicheren Entscheidungen.
4. Kritische Fakten an Projektdateien/offiziellen Quellen verifizieren.
5. Keine erfundenen Tests, Dateien, Versionen, Tool-Erfolge.
6. Gefährliche/irreversible Aktionen ohne Freigabe stoppen.
7. Checkpoints bei umfangreichen Arbeiten.
8. Blocker konkret; parallel ausführbare Arbeit fortsetzen.
9. Erst nach Validation als abgeschlossen melden.

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Activate | Liste → Skill-Mapping |
| Order | Dependencies first |
| Execute | Skill gates + master status |
| Validate | Cross-cutting evidence |
| Stop | Unvalidated „done“ |

## Red Flags

- Aktivierungsliste fehlt oder ist vage
- Skills parallel auf gleiche Dateien
- Master „fertig“ obwohl Kind-Skill PHASE 4 übersprungen
- Erfundene Tool-Outputs
- Publish/Push ohne Freigabe

## Resources

- `references/activation-catalog.md`
- `scripts/scaffold_activation_plan.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
