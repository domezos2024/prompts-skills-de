---
name: faire-monetarisierung-und-spendenerlebnis
description: Use when adding a fair funding model to an existing app or site - comparing donations/one-time/premium options, building a transparent support page, integrating authorized payments with sandbox tests, and documenting ops/privacy without deceptive UX.
---

# Faire Monetarisierung & Spendenerlebnis

## Overview

Integriert ein seriöses Finanzierungsmodell in eine bestehende Anwendung oder Website. Kernprinzip: **Kosten & Zielgruppe verstehen → faires Modell wählen → transparente UI → autorisierte Integration → Sandbox-Tests.** Keine irreführenden Spendenaufrufe, versteckten Gebühren oder nicht autorisierten Live-Zahlungen.

## When to Use

- Freiwillige Unterstützung, Einmalkauf oder optionale Premium-Features geplant
- Bestehende Bezahlwege fehlen oder sind undurchsichtig
- Auftrag: „faire Finanzierung / Spende integrieren“

## When NOT to Use

- Aggressive Growth-/Dark-Pattern-Conversion
- Store-Listing ohne Payment-Thema → `app-store-release-und-listing-optimierung`
- Rein rechtliche Beratung ohne Implementierung

## Critical Guidelines

- MUST Produkt, Zielgruppe, laufende Kosten und vorhandene Bezahlwege analysieren.
- MUST Modelle (Spende/Einmal/Premium) inkl. Anbietergebühren und UX vergleichen.
- MUST transparente Finanzierungs-/Unterstützungsseite im bestehenden Designsystem bauen.
- MUST nur autorisierte Zahlungsintegration; Preise und Bedingungen klar zeigen.
- MUST Bestätigung, Fehlerfälle, Return-to-App und Webhooks (falls vorhanden) prüfen.
- MUST Sandbox-/Testtransaktionen nutzen, soweit verfügbar.
- NEVER irreführende Spendenaufrufe oder versteckte Gebühren.
- NEVER Live-Zahlungen ohne ausdrückliche Freigabe.
- NEVER Secrets/Keys in Repo committen.
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill faire-monetarisierung-und-spendenerlebnis --root .skill-runs/monetarisierung
```

### PHASE 1 – DISCOVERY

1. Produktwert, Kostenstruktur, Zielgruppe und bestehende Payments erfassen.
2. Anbieter/Optionen und Constraints (Plattform, Region, Steuern als offene Punkte) listen.
3. Vergleichsmatrix mit `scripts/scaffold_monetization_matrix.py`.
4. `references/fair-monetization-checklist.md` abarbeiten.

**Gate:** Kosten-/Modellinventar + Transparenzanforderungen.

### PHASE 2 – PLANNING

1. Modellwahl mit Begründung (Nutzen für Nutzer + Nachhaltigkeit).
2. UI-Plan: Support-Seite, Pricing-Klarheit, Fehler/Erfolg, AGB/Hinweisplatzhalter.
3. Integrationspakete inkl. Webhook/Return und Sandbox-Testplan.
4. Live-Go-Live als separates Freigabe-Gate markieren.

**Gate:** Plan mit Done-Kriterien und Freigabepunkten.

### PHASE 3 – IMPLEMENTATION

1. Unterstützungs-/Pricing-UI im Designsystem umsetzen.
2. Autorisierte Payment-Integration (Testmodus zuerst).
3. Bestätigung, Fehler, Cancel/Return und Webhooks verdrahten.
4. Betrieb/Datenschutz-Doku-Entwurf aktualisieren.

**Gate:** Testmodus-Flow end-to-end bedienbar; keine Live-Charges ohne Freigabe.

### PHASE 4 – VALIDATION

1. Sandbox-/Testtransaktionen (Erfolg, Abbruch, Fehler).
2. Preis-/Gebühren-Darstellung und Copy auf Fairness prüfen.
3. Protokoll; Regressionen fixen.

**Gate:** Validierungsprotokoll; Live-Status explizit.

### PHASE 5 – DELIVERY

1. Ops-/Privacy-Hinweise und offene rechtliche Punkte benennen.
2. Delivery Report; Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/monetarisierung --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Model | Spende / Einmal / Premium vergleichen |
| UI | Transparent, Designsystem, klare Preise |
| Pay | Nur autorisiert, Test zuerst |
| Test | Sandbox Erfolg/Fehler/Cancel |
| Stop | Live ohne Freigabe / Dark Patterns |

## Red Flags

- „Unterstütze uns“ ohne Kostenklarheit
- Versteckte recurring charges
- Live-Keys in Code/Chat
- Erfolg UI ohne bestätigte Zahlung
- Fertigmeldung ohne Sandbox-Test

## Resources

- `references/fair-monetization-checklist.md`
- `scripts/scaffold_monetization_matrix.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
