---
name: designer-fuer-produkt-onboarding-und-nutzerbindung
description: Use when improving first-run onboarding and long-term retention UX, removing friction to first value, adding contextual help/empty states, fixing feedback messages, and validating with first-user scenarios without dark patterns.
---

# Designer für Produkt-Onboarding & Nutzerbindung

## Overview

Verbessert den Einstieg neuer Nutzer und senkt unnötige Hürden bei der langfristigen Nutzung. Kernprinzip: **Pfad zur ersten Kernaktion verkürzen → kontextuelle Hilfe → klare Feedbackzustände → datensparsame Messung.** Keine aufdringlichen Pop-ups, erzwungenen Bewertungen oder manipulativen Bindungsmechanismen.

## When to Use

- Erstanwender scheitern vor dem ersten Erfolg
- Empty States / Fehlermeldungen / Guided Setup fehlen oder verwirren
- Retention leidet durch Reibung, nicht durch fehlende Features

## When NOT to Use

- Komplettes UI-Redesign → `vollstaendige-ui-ux-transformation`
- Conversion-Funnel-Optimierung mit Pricing-Fokus → Monetarisierungs-/Conversion-Skills
- Nur Feature-Ideation → `produktchancen-und-funktionsentdeckung`

## Critical Guidelines

- MUST Journey vom ersten Öffnen bis zur ersten erfolgreichen Kernaktion mappen.
- MUST unklare Erklärungen, unnötige Settings und vermeidbare Eingaben identifizieren.
- MUST schlanken Onboarding-Flow mit klaren Nutzerzielen implementieren.
- MUST kontextuelle Hilfen, Empty States und optionales Guided Setup liefern.
- MUST Fehler-/Erfolgs-/Feedbackzustände überarbeiten.
- MUST datensparsame Erfolgsmessungen ergänzen (nur wenn sinnvoll und erlaubt).
- NEVER Dark Patterns, erzwungene Reviews, manipulative Nudges.
- NEVER Onboarding, das Kernwert verzögert statt ermöglicht.
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill designer-fuer-produkt-onboarding-und-nutzerbindung --root .skill-runs/onboarding
```

### PHASE 1 – DISCOVERY

1. First-Open → First-Value-Pfad erfassen; Drop-off-Stellen dokumentieren.
2. Einstellungen, Pflichtfelder, Erklärungen und bestehende Tours inventarisieren.
3. Journey-Scaffold mit `scripts/scaffold_onboarding_journey.py`.
4. `references/onboarding-retention-checklist.md` abarbeiten.

**Gate:** Journey-Map + priorisierte Reibungspunkte (P0–P3).

### PHASE 2 – PLANNING

1. Schlanken Ziel-Flow mit messbaren Nutzerzielen definieren.
2. Pakete: Copy/Help, Empty States, Guided Setup (optional), Feedbackzustände, Metrics.
3. Anti-Dark-Pattern-Review in den Plan aufnehmen.
4. Akzeptanzkriterien und Rollback je Paket.

**Gate:** Plan mit Done-Kriterien und Hypothesen/Kennzahlen.

### PHASE 3 – IMPLEMENTATION

1. Onboarding-Schritte reduzieren/klären; Kernaktion früher erreichbar machen.
2. Kontextuelle Hilfe, Empty States, optionales Guided Setup implementieren.
3. Fehler-/Erfolgsmeldungen und Feedbackzustände vereinheitlichen.
4. Datensparsame Event-/Erfolgsmessung nur mit klarer Zweckbindung.

**Gate:** First-Value-Pfad bedienbar; keine Dark Patterns eingeführt.

### PHASE 4 – VALIDATION

1. Realistische Erstanwender-Szenarien durchspielen; Protokoll führen.
2. Abbruch, Skip, Fehler und Erfolgspfad prüfen.
3. Verfügbare UI-/Flow-Tests; Regressionen fixen.

**Gate:** Testbericht ohne unbelegte Pass-Claims.

### PHASE 5 – DELIVERY

1. Hypothesen, Kennzahlen und Restlücken dokumentieren.
2. Delivery Report; Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/onboarding --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Map | First open → first value |
| Cut | Unnötige Steps/Settings entfernen |
| Help | Kontextuell, Empty, optional Guide |
| Measure | Datensparsam, zweckgebunden |
| Stop | Dark Patterns / Forced Review |

## Red Flags

- Langer Wizard vor erstem Nutzen
- Nicht überspringbares Onboarding ohne Not
- Bewertungs-Dialoge als „Retention“
- Metrics ohne Privacy-Klarheit
- Fertigmeldung ohne Erstanwender-Test

## Resources

- `references/onboarding-retention-checklist.md`
- `scripts/scaffold_onboarding_journey.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
