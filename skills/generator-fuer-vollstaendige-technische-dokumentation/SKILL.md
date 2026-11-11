---
name: generator-fuer-vollstaendige-technische-dokumentation
description: Use when creating or updating complete technical docs from the real codebase - README, install/quickstart, architecture, API/tool refs, examples, troubleshooting - and verifying documented commands instead of inventing features.
---

# Generator für vollständige technische Dokumentation

## Overview

Erzeugt aktuelle, verständliche technische Dokumentation **ausschließlich aus der tatsächlichen Implementierung**. Kernprinzip: **Repo lesen → Doku-Gaps finden → schreiben → dokumentierte Befehle testen → Widersprüche tilgen.** Nicht überprüfbare Schritte explizit kennzeichnen.

## When to Use

- README/Architektur/API-Docs fehlen oder sind veraltet
- Onboarding neuer Entwickler stockt an der Doku
- Auftrag: „vollständige technische Dokumentation“

## When NOT to Use

- Wissensdatenbank/Diagramm-first für Agents → `architekt-fuer-repository-wissensdatenbanken`
- Nur Changelog/Release Notes → `changelog-und-release-dokumentation`
- Agent-Skills erzeugen → `generator-fuer-ki-agenten-anweisungen-und-skills`

## Critical Guidelines

- MUST Struktur, Einstiege, Configs und öffentliche Schnittstellen analysieren.
- MUST bestehende Doku mit Ist-Zustand vergleichen; nur Vorhandenes dokumentieren.
- MUST README, Install, Schnellstart, Architektur, Module, Config, Dependencies liefern/aktualisieren.
- MUST API-/Tool-Referenzen aus realer Implementierung ableiten.
- MUST Beispiele, Troubleshooting und Dev-Anleitungen ergänzen.
- MUST dokumentierte Befehle in geeigneter Umgebung testen; Failures korrigieren.
- NEVER Features dokumentieren, die nicht existieren.
- NEVER ungeprüfte Schritte als „verifiziert“ markieren.
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill generator-fuer-vollstaendige-technische-dokumentation --root .skill-runs/tech-docs
```

### PHASE 1 – DISCOVERY

1. Repo-Struktur, Entry Points, Configs, public APIs/CLIs inventarisieren.
2. Vorhandene Docs listen und Drift markieren.
3. Doc-Tree mit `scripts/scaffold_doc_tree.py` anlegen.
4. `references/tech-docs-checklist.md` abarbeiten.

**Gate:** Inventar + Drift-Liste.

### PHASE 2 – PLANNING

1. Zielstruktur der Doku festlegen (README + tiefergehende Docs).
2. Schreibpakete priorisieren (P0: Install/Quickstart, P1: Architektur/API, …).
3. Befehlsliste für Verifikation definieren.
4. Out-of-scope und „nicht verifizierbar“-Policy.

**Gate:** Doc-Plan mit Verifikationsliste.

### PHASE 3 – IMPLEMENTATION

1. README / Install / Quickstart aktualisieren oder erstellen.
2. Architektur, Module, Config, Dependencies dokumentieren.
3. API-/Tool-Refs und Beispiele schreiben.
4. Widersprüche und tote Links entfernen.

**Gate:** Doc-Paket vorhanden; Claims an Code gebunden.

### PHASE 4 – VALIDATION

1. Dokumentierte Befehle ausführen; Ergebnisse protokollieren.
2. Stichproben: Abschnitte ↔ Quellcode.
3. Nicht Ausführbares als solches kennzeichnen.

**Gate:** Verifikationsprotokoll ohne Fake-Pass.

### PHASE 5 – DELIVERY

1. Doc-Index, Restlücken, bekannte Einschränkungen.
2. Delivery Report; Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/tech-docs --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Source | Code > Wishful docs |
| Core | README + Install + Architecture |
| API | Nur reale Surfaces |
| Verify | Befehle wirklich ausführen |
| Stop | Ungeprüft als „fertig“ |

## Red Flags

- Copy aus alten Docs ohne Code-Check
- Beispielcommands die failen
- „Coming soon“ als existierende Feature-Doku
- Fertigmeldung ohne PHASE 4

## Resources

- `references/tech-docs-checklist.md`
- `scripts/scaffold_doc_tree.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
