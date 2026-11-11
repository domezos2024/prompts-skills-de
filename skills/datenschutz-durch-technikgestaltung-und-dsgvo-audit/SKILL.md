---
name: datenschutz-durch-technikgestaltung-und-dsgvo-audit
description: Use when auditing technical privacy architecture, GDPR-style data minimization, consent/export/erasure flows, PII logging, or third-party transfers - runs a strict multi-phase data-map, Privacy-by-Design hardening, and validated privacy-flow test workflow. Not legal advice.
---

# Datenschutz durch Technikgestaltung & DSGVO-Audit

## Overview

Prüft und verbessert die **technische** Datenschutzarchitektur. Kernprinzip: **Datenkarte beweisen → Minimierung/Rechtepfade härten → Abläufe testen → technische Findings von Rechtsberatung trennen.** Keine Konformitätsbehauptung ohne entsprechende Prüfung.

## When to Use

- PII-Flüsse, Logging, Drittanbieter, Speicherdauer unklar
- Einwilligung, Widerruf, Auskunft, Export, Löschung technisch umsetzen/prüfen
- Privacy-by-Design / Datenminimierung im Code

## When NOT to Use

- Rein rechtliche Vertrags-/DPIA-Beratung ohne Code
- Nur Crypto-at-Rest → `architekt-fuer-verschluesselung-und-schluesselverwaltung`
- Nur allgemeine AppSec → `vollstaendige-sicherheitshaertung`

## Critical Guidelines

- MUST personenbezogene Daten, Zwecke, Speicherorte, Retention und Empfänger kartieren.
- MUST unnötige Erhebung, übermäßiges Logging und problematische Transfers kennzeichnen.
- MUST technische Unterstützung für Consent, Widerruf, Auskunft, Export, Löschung prüfen/implementieren.
- MUST kritische Privacy-Flows inkl. Ablehnung/Widerruf testen.
- MUST in Reports klar trennen: technische Findings vs. offene Rechtsfragen.
- NEVER „DSGVO-konform“ ohne rechtliche Prüfung behaupten.
- NEVER Produktivdaten für Tests ohne Freigabe/Anonymisierung nutzen.
- NEVER PII oder Secrets in Artefakte/Logs der Prüfung schreiben.
- ALWAYS Iron Laws und Phasenstatus.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill datenschutz-durch-technikgestaltung-und-dsgvo-audit --root .skill-runs/privacy-dsgvo
```

### PHASE 1 – DISCOVERY (Datenkarte)

1. Datenkategorien, Quellen, Speicher, Logs, Analytics, Drittanbieter erfassen.
2. Retention, Zweckbindung und Zugriffsrollen pro Datensatz notieren.
3. Matrix `references/privacy-dsgvo-matrix.md` befüllen; Evidence pflicht.

**Gate:** Datenflusskarte + Inventar existieren.

### PHASE 2 – PLANNING (Privacy-by-Design)

1. Minimierungs- und Pseudonymisierungsoptionen priorisieren (P0 Leaks zuerst).
2. Rechtepfade: Consent UI/API, Widerruf, Export, Löschkaskade planen.
3. Logging-Policy: was nie geloggt wird; Redaction-Stellen.
4. Atomare Pakete mit Akzeptanztests (Ablehnung, Widerruf, Löschbestätigung).

**Gate:** Plan mit messbaren Done-Kriterien; Rechtsfragen separat gelistet.

### PHASE 3 – IMPLEMENTATION

1. Datenerhebung kürzen; Defaults datenschutzfreundlich.
2. Consent-/Widerruf-Speicherung nachvollziehbar machen.
3. Export/Löschung inkl. abhängiger Stores so weit technisch machbar.
4. PII aus Logs/Errors entfernen oder maskieren.
5. Nach jedem Paket: Privacy-Smoke der betroffenen Flows.

**Gate:** P0-Datenlecks/Tech-Lücken geschlossen oder risk-accepted dokumentiert.

### PHASE 4 – VALIDATION

1. Consent annehmen/ablehnen/widerrufen; Export und Löschung durchspielen.
2. Negativ: Verarbeitung ohne Consent wo Consent Pflichtpfad ist.
3. Prüfen, dass Testartefakte keine echten PII enthalten.
4. Ergebnisse gegen Matrix abhaken.

**Gate:** Testprotokoll ohne Konformitäts-Claim; offene Rechtsfragen markiert.

### PHASE 5 – DELIVERY

1. Datenflussdokumentation, technische Maßnahmen, Testbericht.
2. Delivery Report; Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/privacy-dsgvo --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Map | Kategorien → Flüsse → Retention → Empfänger |
| Design | Minimize → Consent → Erasure |
| Test | Ablehnung / Widerruf / Export / Delete |
| Claim | Nur technische Findings, kein Rechtsurteil |

## Red Flags

- „DSGVO ok“ ohne Rechtsprüfung
- Prod-PII in Testlogs
- Consent nur clientseitig
- Löschung löscht UI-Flag aber nicht Storage
- Fertig ohne PHASE 4

## Resources

- `references/privacy-dsgvo-matrix.md`
- `scripts/scaffold_data_map.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
