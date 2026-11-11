---
name: ingenieur-fuer-web-barrierefreiheit-und-konformitaet
description: Use when improving website accessibility toward WCAG - combine automated and manual tests for contrast, keyboard, focus, semantics, forms, and dialogs, and never treat automated scores alone as full compliance proof.
---

# Ingenieur für Web-Barrierefreiheit & Konformität

## Overview

Verbessert Barrierefreiheit anhand einschlägiger WCAG-Anforderungen. Kernprinzip: **Flows inventarisieren → auto+manuell testen → semantisch fixen → mit Tastatur/Screenreader erneut prüfen.** Automatisierte Scores allein sind kein Konformitätsnachweis.

## When to Use

- WCAG-Lücken (Kontrast, Fokus, Semantik, Formulare, Dialoge)
- Tastatur- und Screenreader-Probleme
- Accessibility-Bericht mit Restbarrieren gefordert

## When NOT to Use

- Nur visualles Redesign ohne A11y-Scope → UI/UX-Skill
- Nur SEO-Metadaten → SEO-Skill
- Nur Performance ohne Semantik → Website-Optimierung ergänzend

## Critical Guidelines

- MUST Templates, interaktive Elemente und kritische Abläufe inventarisieren.
- MUST automatisierte und manuelle Tests kombinieren.
- MUST native HTML-Semantik bevorzugen; ARIA nur wenn nötig.
- MUST Formulare, Fehler, Live-Regions und Dialoge prüfen.
- MUST Restbarrieren ehrlich dokumentieren.
- NEVER „WCAG AA erfüllt“ allein aufgrund eines Tool-Scores behaupten.
- NEVER Deploy ohne explizite Nutzerfreigabe.
- NEVER Tastaturfallen oder Fokusverlust als kosmetisch abtun.
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill ingenieur-fuer-web-barrierefreiheit-und-konformitaet --root .skill-runs/a11y
```

### PHASE 1 – DISCOVERY

1. Templates und kritische User-Flows erfassen.
2. Automatisierte Scans + manuelle Stichproben Baseline.
3. Kontrast, Tastatur, Fokus, Semantik auditieren.
4. Checklist `references/wcag-conformance-checklist.md`.

**Gate:** Priorisierte Barrierenliste mit Evidence.

### PHASE 2 – PLANNING

1. Fixes nach Impact (P0 Blocker zuerst).
2. Komponenten vs. Seiten-Fixes trennen.
3. Testplan: Tastatur, Screenreader, Viewport.
4. Done = reproduzierbarer Nachweis, kein Score-Ziel allein.

**Gate:** Implementierungsplan + Testmatrix.

### PHASE 3 – IMPLEMENTATION

1. Semantik, Labels, Kontrast, Fokusreihenfolge umsetzen.
2. Formulare/Fehler/Dialoge zugänglich machen.
3. ARIA sparsam und korrekt.
4. Smoke der betroffenen Flows.

**Gate:** P0-Barrieren geschlossen oder mit Blocker begründet.

### PHASE 4 – VALIDATION

1. Auto-Scan wiederholen.
2. Manuelle Tastaturtests kritischer Flows.
3. Verfügbare Screenreader-Checks; Ergebnisse protokollieren.
4. Verbliebene Barrieren listen (keine Vollständigkeitsfiktion).

**Gate:** A11y-Bericht mit Methodenmix.

### PHASE 5 – DELIVERY

1. Accessibility-Bericht + Restliste.
2. Deploy nur nach User-Freigabe.
3. Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/a11y --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Inventar | Templates + Flows |
| Test | Auto + manuell |
| Fix | Semantik first |
| ARIA | Nur wenn nötig |
| Claim | Nie Score-only |

## Red Flags

- „AA compliant“ nur via Lighthouse
- Div-Buttons ohne Keyboard
- Modals ohne Fokus-Trap/Return
- Farbe als einzige Info
- Fertig ohne manuelle Prüfung

## Resources

- `references/wcag-conformance-checklist.md`
- `scripts/scaffold_a11y_report.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
