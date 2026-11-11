---
name: produktchancen-und-funktionsentdeckung
description: Use when discovering high-value product extensions for an existing app, ranking feature opportunities by evidence and effort, implementing one bounded improvement with tests/docs, and producing a prioritized roadmap - runs discovery, scoring, build, and validation.
---

# Produktchancen & Funktionsentdeckung

## Overview

Identifiziert die wertvollsten Erweiterungen für ein vorhandenes Produkt und setzt **eine** geeignete, begrenzte Verbesserung um. Kernprinzip: **nachweisbare Nutzerprobleme → scored Backlog → eine vollständige Funktion → Roadmap für Rest.** Keine künstliche Komplexität oder „KI-Feature um der KI willen“.

## When to Use

- Produkt braucht sinnvolle nächste Features, nicht nur Ideenliste
- Feedback/Wettbewerb deuten auf Lücken hin
- Auftrag: „wertvollste Erweiterung finden und umsetzen“

## When NOT to Use

- Nur Wettbewerbsvergleich ohne Feature-Build → `wettbewerbs-benchmark-und-produktverbesserung`
- Nur Onboarding/Retention → `designer-fuer-produkt-onboarding-und-nutzerbindung`
- Nur Monetarisierungsmodell → `faire-monetarisierung-und-spendenerlebnis`

## Critical Guidelines

- MUST Ist-Funktionen, Zielgruppe, Ziele und technische Grenzen vor Ideation erfassen.
- MUST ≥10 realistische Kandidaten mit Nutzwert/Aufwand/Wartung/Risiko bewerten.
- MUST Top-3 mit konkreten Use Cases beschreiben; genau einen Kandidaten vollständig implementieren.
- MUST Tests, nötige UI und Dokumentation zur Implementierung liefern.
- MUST Roadmap für verbleibende Vorschläge priorisieren (P0–P3).
- NEVER Features ohne Beleg für Nutzerproblem erfinden.
- NEVER unnötige KI-/Komplexitätsfeatures bevorzugen.
- NEVER „fertig“ ohne laufende/validierte Funktion und Tests (soweit möglich).
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill produktchancen-und-funktionsentdeckung --root .skill-runs/produktchancen
```

### PHASE 1 – DISCOVERY

1. Funktionen, Personas/Zielgruppe, Produktziele, Constraints und Tech-Debt erfassen.
2. Feedbackquellen, Support-Tickets, Analytics, Reviews und Wettbewerb sammeln (nur Verifiziertes).
3. Scoring-Vorlage mit `scripts/scaffold_feature_scorecard.py` anlegen.
4. Checkliste `references/feature-opportunity-checklist.md` abarbeiten.

**Gate:** Produktkurzprofil + Problem-/Chanceninventar existieren.

### PHASE 2 – PLANNING (Score & Auswahl)

1. ≥10 Erweiterungsmöglichkeiten formulieren (realistisch, begrenzt).
2. Nach Nutzwert, Aufwand, Wartungskosten, Risiko scoren; Top-3 auswählen.
3. Für Top-3 Use Cases, Akzeptanzkriterien und Abhängigkeiten schreiben.
4. Implementierungskandidat wählen; Scope und Rollback festlegen.

**Gate:** Scorecard + gewählter Kandidat mit Done-Definition.

### PHASE 3 – IMPLEMENTATION

1. Gewählte Funktion atomar umsetzen (Backend/UI nach Projektkonvention).
2. Tests und notwendige UI-Zustände (Empty/Error/Success) ergänzen.
3. Docs/README-Hinweise aktualisieren.
4. Nach Paketen Smoke der betroffenen Flows.

**Gate:** Funktion bedienbar; keine offenen P0-Bugs im Scope.

### PHASE 4 – VALIDATION

1. Akzeptanzkriterien abhaken; verfügbare Tests ausführen.
2. Manuelle Szenarien aus Use Cases prüfen; Ergebnisse protokollieren.
3. Selbst eingeführte Regressionen fixen.

**Gate:** Validierungsprotokoll ohne unbelegte Pass-Claims.

### PHASE 5 – DELIVERY

1. Priorisierte Roadmap für Restvorschläge.
2. Delivery Report nach `_shared/references/delivery-report-template.md`.
3. Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/produktchancen --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Ideation | ≥10 belegte Kandidaten |
| Score | Nutzen/Aufwand/Wartung/Risiko |
| Build | Genau 1 begrenzte Funktion + Tests |
| Deliver | Feature + Roadmap |
| Stop | Kein Nutzerproblem-Beleg → nicht bauen |

## Red Flags

- Feature-Liste ohne Quellen
- „AI-Feature“ ohne Problemfit
- Mehrere halbfertige Features statt einer vollständigen
- Roadmap ohne Aufwand/Risiko
- Fertigmeldung ohne PHASE 4

## Resources

- `references/feature-opportunity-checklist.md`
- `scripts/scaffold_feature_scorecard.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
