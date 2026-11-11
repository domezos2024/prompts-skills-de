---
name: generator-fuer-ki-agenten-anweisungen-und-skills
description: Use when creating project AI instructions, reusable agent roles, and installable skills for the tools actually used in the repo - with shared central rules, validation of structure/syntax, and no decorative agents or accidental overwrites.
---

# Generator für KI-Agenten-Anweisungen & Skills

## Overview

Erstellt professionelle Projektanweisungen, wiederverwendbare Agentenrollen und installierbare Skills für die **tatsächlich verwendeten** KI-Entwicklungswerkzeuge. Kernprinzip: **Ist-Tools & Tasks → zentrale Regeln → Rollen/Skills mit Triggern & Erfolgskriterien → Format validieren → repräsentativ testen.** Keine dekorativen Agenten; vorhandene Anweisungen nicht unbeabsichtigt überschreiben.

## When to Use

- CLAUDE.md / AGENTS.md / Skills fehlen oder sind inkonsistent
- Wiederkehrende Agentenaufgaben brauchen klaren Trigger und Done-Definition
- Auftrag: „Agent Instructions & Skills generieren“

## When NOT to Use

- Nur Knowledge-Base ohne Agent-Packaging → `architekt-fuer-repository-wissensdatenbanken`
- Orchestrierung vieler Workflows → `universeller-multi-workflow-master`
- Skill-Authoring-Spec dieses Repos selbst erweitern ohne Bedarf

## Critical Guidelines

- MUST Stack, Tools und vorhandene Agent-/Skill-Definitionen analysieren.
- MUST wiederkehrende Aufgaben und Gaps identifizieren.
- MUST schlanke zentrale Regeldatei pflegen (Single Source of Truth).
- MUST Rollen für Implementierung, Review, Testing, Docs nur bei Bedarf.
- MUST Skills mit klaren Auslösern, Inputs und Erfolgskriterien liefern.
- MUST zieltool-kompatible Dateiformate erzeugen; Syntax/Struktur/Verweise validieren.
- MUST repräsentative Aufgaben testen und Anweisungen nachschärfen.
- NEVER bloß dekorative Agenten.
- NEVER vorhandene Anweisungen unbeabsichtigt überschreiben (Backup/Diff zuerst).
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws / skill-authoring-spec befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill generator-fuer-ki-agenten-anweisungen-und-skills --root .skill-runs/agent-skills
```

### PHASE 1 – DISCOVERY

1. Sprachen, Tools (Claude/Cursor/Codex/…), vorhandene Rules/Skills inventarisieren.
2. Wiederkehrende Tasks und Schmerzpunkte listen.
3. Scaffold mit `scripts/scaffold_agent_skill_pack.py`.
4. `references/agent-skill-authoring-checklist.md` nutzen.

**Gate:** Tool-Inventar + Task-/Gap-Liste + Backup-Plan für bestehende Files.

### PHASE 2 – PLANNING

1. Zentrale Regeln vs. rollenspezifische Ergänzungen trennen.
2. Skill-Backlog: Name, Trigger („Use when…“), Inputs, Gates, Outputs.
3. Zielpfade und Formate je Tool festlegen; Merge-Strategie gegen Existierendes.
4. Validierungs- und Testfälle planen.

**Gate:** Plan ohne Überschreibungsrisiko.

### PHASE 3 – IMPLEMENTATION

1. Zentrale Projektregeln schreiben/aktualisieren (minimal, imperativ).
2. Agentenrollen und Skills erzeugen (SKILL.md + references/scripts wo nötig).
3. Install-/Pfad-Doku für Zielwerkzeuge.
4. Keine Secrets in Instructions.

**Gate:** Dateien im Ziel-Format vorhanden; Diff zu Altbestand reviewt.

### PHASE 4 – VALIDATION

1. Struktur/Syntax/Frontmatter/Links prüfen (`validate_skill_structure.py` falls anwendbar).
2. Repräsentative Aufgabe je Skill/Rolle dry-run / Review.
3. Überschreibungs- und Duplikat-Check.

**Gate:** Validierungsprotokoll; keine Fake-Kompatibilität.

### PHASE 5 – DELIVERY

1. Installationsdoku, Aktivierungshinweise, Restlücken.
2. Delivery Report; Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/agent-skills --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Center | Eine Regelquelle |
| Skill | Trigger + Gates + Outputs |
| Safety | Backup before overwrite |
| Validate | Structure + sample task |
| Stop | Decorative agents |

## Red Flags

- Skills ohne „Use when“
- Agenten ohne Erfolgskriterien
- Blindes Überschreiben von CLAUDE.md
- Fertigmeldung ohne Strukturcheck

## Resources

- `references/agent-skill-authoring-checklist.md`
- `scripts/scaffold_agent_skill_pack.py`
- `../_shared/references/skill-authoring-spec.md`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
- `../_shared/scripts/validate_skill_structure.py`
