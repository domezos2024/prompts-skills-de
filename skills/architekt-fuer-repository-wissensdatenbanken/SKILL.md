---
name: architekt-fuer-repository-wissensdatenbanken
description: Use when building a structured project knowledge base for humans and AI agents - mapping modules, data flows, decisions, and source links, plus update rules - validated by sampling claims against real code.
---

# Architekt für Repository-Wissensdatenbanken

## Overview

Baut eine strukturierte Wissensbasis, damit Menschen und KI-Agenten ein Softwareprojekt schnell verstehen. Kernprinzip: **Code & Regeln analysieren → einheitliche Themenstruktur → Architektur/Module/Datenflüsse mit Dateiverweisen → Update-Regeln → Stichprobenvalidierung.** Erfolg: Einstieg ohne umfangreiche manuelle Recherche.

## When to Use

- Onboarding von Devs/Agents braucht navigierbares Projektwissen
- Architekturentscheidungen und Grenzen fehlen in zentraler Form
- Auftrag: „Repository-Knowledge-Base“

## When NOT to Use

- Klassische User-facing Tech-Docs only → `generator-fuer-vollstaendige-technische-dokumentation`
- Agent-Skill-Dateien erzeugen → `generator-fuer-ki-agenten-anweisungen-und-skills`
- Einmaliges README-Update ohne Wissensstruktur

## Critical Guidelines

- MUST Quellcode, Doku, Configs und Projektregeln (AGENTS/CLAUDE) analysieren.
- MUST zentrale Module, Datenmodelle, Schnittstellen und Abhängigkeiten identifizieren.
- MUST einheitliche Wissensstruktur mit Themenbereichen anlegen.
- MUST Architekturübersichten, Modulbeschreibungen und Datenflussdiagramme (textuell/ Mermaid ok) liefern.
- MUST technische Entscheidungen und Implementierungsgrenzen dokumentieren.
- MUST Navigation mit verlässlichen Quelldatei-Verweisen bauen.
- MUST Update-Regeln für zukünftige Codeänderungen definieren.
- MUST wichtige Aussagen stichprobenartig am Code validieren.
- NEVER unbelegte Architektur-Behauptungen.
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill architekt-fuer-repository-wissensdatenbanken --root .skill-runs/knowledge-base
```

### PHASE 1 – DISCOVERY

1. Code, Docs, Configs, Regeln inventarisieren.
2. Module, Models, APIs, Dependencies und kritische Pfade listen.
3. KB-Scaffold mit `scripts/scaffold_knowledge_base.py`.
4. `references/knowledge-base-structure.md` als Zielstruktur nutzen.

**Gate:** Inventar + Themenlandkarte.

### PHASE 2 – PLANNING

1. Themenbereiche und Navigationsbaum festlegen.
2. Schreibpakete: Overview, Modules, Dataflow, ADRs/Decisions, Boundaries, Update-Rules.
3. Validierungsstichproben planen (Claims → Dateien).

**Gate:** Strukturplan + Stichprobenliste.

### PHASE 3 – IMPLEMENTATION

1. Wissensdateien und Diagramme erstellen.
2. Querverweise auf Quelldateien setzen (relativ, prüfbar).
3. Entscheidungs- und Grenzdokumente schreiben.
4. Update-Konzept (wann/was/wer aktualisiert) ergänzen.

**Gate:** Navigierbare KB vorhanden.

### PHASE 4 – VALIDATION

1. Stichproben: Aussagen gegen Code prüfen; Fehler korrigieren.
2. Broken Links / tote Pfade fixen.
3. „Agent kann einsteigen“-Smoke: Einstiegspunkte in <N Hops erreichbar.

**Gate:** Validierungsprotokoll der Stichproben.

### PHASE 5 – DELIVERY

1. Index, Update-Regeln, Restlücken.
2. Delivery Report; Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/knowledge-base --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Map | Module + Flows + Boundaries |
| Link | Jede Kernaussage → Quelldatei |
| Decide | ADRs / Grenzen dokumentieren |
| Maintain | Update-Regeln festlegen |
| Stop | Unbelegte Claims |

## Red Flags

- Wiki ohne Dateiverweise
- Diagramme ohne Bezug zum Code
- Keine Update-Regeln
- Fertigmeldung ohne Stichproben

## Resources

- `references/knowledge-base-structure.md`
- `scripts/scaffold_knowledge_base.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
