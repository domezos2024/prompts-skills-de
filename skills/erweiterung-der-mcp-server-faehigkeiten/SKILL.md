---
name: erweiterung-der-mcp-server-faehigkeiten
description: Use when extending an existing MCP server with missing tools/resources/prompts, auditing redundant or unsafe MCP capabilities, or implementing high-value MCP tool additions with schemas, auth checks, and tests - runs inventory, gap analysis, prioritized implementation, and capability-matrix validation.
---

# Erweiterung der MCP-Server-Fähigkeiten

## Overview

Erweitert einen bestehenden MCP-Server um **nachweislich fehlende, nützliche** Fähigkeiten. Kernprinzip: **Inventar beweisen → Lücken priorisieren → top-N implementieren → mit Contract-/Safety-Tests absichern.** Keine Duplikate ohne Verbesserung.

## When to Use

- MCP-Server hat Tools, aber wichtige Service-Methoden fehlen als Tools
- Redundante/unsichere Tools bereinigen und gezielt erweitern
- Capability-Matrix, Schemas und Integrationstests fehlen
- Auftrag: „MCP-Server erweitern / neue MCP-Tools“

## When NOT to Use

- Nur Tool-Beschreibungen/Schemas optimieren → `mcp-werkzeug-intelligenz-und-optimierung`
- Neuen MCP-Server von Null → MCP-Builder-/Scaffold-Skill
- Modell-Routing/Failover → `intelligentes-modell-routing-und-failover`

## Critical Guidelines

- MUST vollständiges Inventar (Tools, Resources, Prompts) vor Design erstellen.
- MUST neue Tools gegen bestehende Fähigkeiten prüfen; Duplikate nur bei messbarer Verbesserung.
- MUST Input-Schema, Validierung, AuthZ und strukturierte Fehler für jedes neue Tool liefern.
- MUST Idempotenz/Safety für side-effecting Tools (Dry-Run, Confirm-Flag oder Gate) spezifizieren.
- MUST gültige, ungültige und Grenzwert-Eingaben testen; Ergebnisse protokollieren.
- NEVER Tools erfinden, die der Server nicht technisch bedienen kann.
- NEVER destruktive Aktionen ohne Berechtigungsprüfung und Observability (Audit-Log).
- NEVER „fertig“ ohne aktualisierte Capability-Matrix und Docs.
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill erweiterung-der-mcp-server-faehigkeiten --root .skill-runs/mcp-extend
```

### PHASE 1 – DISCOVERY (Inventar)

1. MCP-Server-Einstieg, Tool-/Resource-/Prompt-Registrierung und Auth-Modell erfassen.
2. Inventar mit `scripts/scaffold_capability_matrix.py` anlegen; Ist-Tools auflisten.
3. Interne Service-Methoden und öffentliche APIs gegen exponierte Tools mappen.
4. Redundanzen, unsichere Surface, fehlende Validierung nach `references/mcp-capability-checklist.md` markieren.

**Gate:** Capability-Inventar + Gap-Liste (verifiziert) existieren.

### PHASE 2 – PLANNING (Priorisierung)

1. Kandidaten nach Nutzen × Aufwand × Sicherheitsrisiko bewerten (P0–P3).
2. Top-5 technisch realisierbare Erweiterungen wählen; Verträge (Input/Output/Errors) skizzieren.
3. Idempotenz-, AuthZ- und Observability-Anforderungen je Tool festlegen.
4. Atomare Implementierungspakete mit Akzeptanzkriterien und Rollback.

**Gate:** Priorisierte Top-5-Liste mit messbaren Done-Kriterien.

### PHASE 3 – IMPLEMENTATION

1. Pro Tool: Schema → Handler → Validierung → AuthZ → Fehlercodes.
2. Side-effects: Confirm/Dry-Run oder Approval-Gate; Audit-Events schreiben.
3. Docs/Integrationsbeispiele parallel aktualisieren.
4. Nach jedem Tool: Smoke mit gültigen Eingaben.

**Gate:** Fünf Tools (oder dokumentiert weniger bei Blockern) lauffähig; keine offenen P0-Safety-Lücken.

### PHASE 4 – VALIDATION

1. Jedes Tool: valid / invalid / boundary Cases.
2. Capability-Matrix aktualisieren; Duplikat-Claim prüfen.
3. Regression bestehender Tools; Fehlerpfade und Auth-Deny prüfen.
4. Selbst verursachte Brüche fixen und re-testen.

**Gate:** Testprotokoll + Matrix ohne unbelegte Pass-Claims.

### PHASE 5 – DELIVERY

1. Delivery Report nach `_shared/references/delivery-report-template.md`.
2. Restlücken und bewusst nicht gebaute Kandidaten benennen.
3. Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/mcp-extend --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Inventar | Tools/Resources/Prompts + Service-Map |
| Priorität | Nutzen × Aufwand × Risiko |
| Vertrag | Schema + Errors + AuthZ + Idempotenz |
| Beweis | Tests + Capability-Matrix |
| Stop | Duplikat ohne Verbesserung → nicht bauen |

## Red Flags

- Neues Tool ohne Schema/Validierung
- Destruktives Tool ohne AuthZ/Audit
- „Schon ähnlich vorhanden“ ignoriert
- Fertigmeldung ohne PHASE-4-Tests
- Erfundene Backend-Fähigkeiten

## Resources

- `references/mcp-capability-checklist.md`
- `scripts/scaffold_capability_matrix.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
