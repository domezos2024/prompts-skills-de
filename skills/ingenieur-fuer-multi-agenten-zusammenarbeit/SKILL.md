---
name: ingenieur-fuer-multi-agenten-zusammenarbeit
description: Use when coordinating specialized AI agents on one project, defining agent roles and handoff contracts, detecting file/resource conflicts, adding review gates, or comparing multi-agent vs single-agent quality/cost - runs role design, orchestration, conflict control, and evaluation.
---

# Ingenieur für Multi-Agenten-Zusammenarbeit

## Overview

Baut ein System, in dem **spezialisierte Agenten** koordiniert an einem Projekt arbeiten. Kernprinzip: **Rollen + Handoff-Verträge + Review-Gates + Konfliktkontrolle.** Mehr Agenten nur bei nachweisbarem Nutzen.

## When to Use

- Planner/Developer/Reviewer/Tester sollen getrennt arbeiten
- Handoffs brauchen strukturierte Verträge und Validierung
- Parallele Arbeit riskiert Datei-/Ressourcenkonflikte
- Multi- vs. Einzelagenten-Vergleich gefordert

## When NOT to Use

- Einzelner resilienter Workflow ohne Rollen → `architekt-fuer-autonome-agenten-workflows`
- Nur Modell-Routing → `intelligentes-modell-routing-und-failover`
- Reine Menschen-Team-Prozessdoku ohne Agentenruntime

## Critical Guidelines

- MUST Aufgabenarten, Abhängigkeiten und Tool-/Modellfähigkeiten vor Rollenschnitt analysieren.
- MUST Handoff-Verträge (Input, Output, Acceptance, Owner) explizit machen.
- MUST Koordinator mit Statusverwaltung und klarer Ownership implementieren.
- MUST Konflikterkennung für gleichzeitige Datei-/Ressourcenänderungen.
- MUST Review-Gates vor jeder kritischen Übergabe.
- NEVER zusätzliche Agenten ohne Nutzen-Nachweis (Qualität/Laufzeit/Aufwand).
- NEVER ungeprüfte Outputs als „fertig“ in den nächsten Agenten durchreichen.
- NEVER parallele Writes ohne Lock-/Partitionierungsstrategie.
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill ingenieur-fuer-multi-agenten-zusammenarbeit --root .skill-runs/multi-agent
```

### PHASE 1 – DISCOVERY

1. Aufgabengraph, kritische Ressourcen, verfügbare Modelle/Tools erfassen.
2. Kandidatenrollen (Planner, Developer, Reviewer, Tester, Release) gegen echten Bedarf prüfen.
3. `scripts/scaffold_handoff_contract.py` für Vertragsvorlage nutzen.
4. Checkliste `references/multi-agent-orchestration-checklist.md`.

**Gate:** Abhängigkeitsgraph + Rollenbegründung (auch „nicht nötig“).

### PHASE 2 – PLANNING

1. Rollen-SLAs und erlaubte Tools je Rolle.
2. Handoff-Protokoll und Review-Gate-Kriterien.
3. Konfliktstrategie (Locks, Worktrees, Partition by path).
4. Evaluationsplan: Qualität, Laufzeit, Aufwand vs. Einzelagent.

**Gate:** Orchestrierungsplan mit messbaren Gates.

### PHASE 3 – IMPLEMENTATION

1. Koordinator: Task-Queue, Status, Ownership.
2. Handoff-Validierung (Schema + Acceptance Checks).
3. Konfliktwächter vor Merge/Write.
4. Observability: wer hat was wann übergeben.

**Gate:** Sequenzielle Pipeline läuft; parallele Pfade wo geplant.

### PHASE 4 – VALIDATION

1. Sequenzielle und parallele Abläufe testen.
2. Konfliktfall erzeugen und Auflösung prüfen.
3. Review-Reject-Pfad und Re-Work testen.
4. Vergleichsmessung Einzelagent vs. Multi dokumentieren.

**Gate:** Evaluationsbericht ohne unbelegte Vorteile.

### PHASE 5 – DELIVERY

1. Delivery Report; wann Multi-Agent lohnt / nicht lohnt.
2. Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/multi-agent --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Rollen | Nur bei nachweisbarem Nutzen |
| Handoff | Vertrag + Review-Gate |
| Konflikt | Lock/Partition vor parallelem Write |
| Eval | Qualität/Zeit/Kosten vs. Solo |
| Stop | Mehr Agenten ohne Nutzen → reduzieren |

## Red Flags

- Agenten ohne klare Ownership
- Handoff als Freitext ohne Schema
- Parallele Edits derselben Datei
- „Besser“ ohne Vergleichsmessung
- Review-Gate übersprungen

## Resources

- `references/multi-agent-orchestration-checklist.md`
- `scripts/scaffold_handoff_contract.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
