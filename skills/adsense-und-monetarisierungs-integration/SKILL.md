---
name: adsense-und-monetarisierungs-integration
description: Use when integrating AdSense or similar ad placements with UX, performance, consent, and policy constraints - map layouts, wire approved slots, verify CMP/CSP, and never invent publisher IDs or claim live ads without confirmation.
---

# AdSense- & Monetarisierungs-Integration

## Overview

Integriert Werbeplätze unter Berücksichtigung von UX, Performance und Richtlinien. Kernprinzip: **Layout und Consent prüfen → freigegebene Slots platzieren → CMP/CSP/CLS testen.** Keine erfundenen IDs, keine Click-Manipulation, keine Live-Freischaltung ohne Bestätigung.

## When to Use

- AdSense/Ad-Slots technisch integrieren
- Consent- und Richtlinienanforderungen umsetzen
- CLS/Layout-Konflikte durch Ads vermeiden

## When NOT to Use

- Rein redaktionelle SEO-Arbeit → SEO-Skill
- Nur Performance ohne Ads → Website-Optimierung
- Payment/Checkout-Monetarisierung (nicht Ads)

## Critical Guidelines

- MUST Layouts, Content-Bereiche und bestehende Ad-Tags zuerst analysieren.
- MUST Publisher-IDs/Slots nur aus Nutzer-/Projektquellen übernehmen – nie erfinden.
- MUST Platzierung außerhalb kritischer Navigation/Bedienelemente wählen.
- MUST Consent/Widerruf, CSP und Ladeverhalten prüfen.
- MUST responsives Layout und Layoutverschiebungen testen.
- NEVER Nutzer absichtlich zu Klicks verleiten (dark patterns).
- NEVER Live-Freischaltung behaupten ohne Bestätigung.
- NEVER Deploy/Prod-Tag-Aktivierung ohne explizite Nutzerfreigabe.
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill adsense-und-monetarisierungs-integration --root .skill-runs/adsense
```

### PHASE 1 – DISCOVERY

1. Seitenlayouts und bestehende Integrationen inventarisieren.
2. Vorhandene Tags, IDs, Slot-Status erfassen (Quellen nennen).
3. Consent-Stack und Zielregionen prüfen.
4. Checklist `references/ads-monetization-checklist.md`.

**Gate:** Inventar + fehlende IDs als Blocker markiert (nicht raten).

### PHASE 2 – PLANNING

1. Zulässige Platzierungen und Dichten planen.
2. CMP-Events und Fallback ohne Consent definieren.
3. Performance-Budget (CLS) und CSP-Änderungen.
4. Freigabe-Gate für Prod-Aktivierung.

**Gate:** Platzierungsplan + Policy-/Consent-Notizen.

### PHASE 3 – IMPLEMENTATION

1. Freigegebene Container/Slots technisch korrekt einbauen.
2. Consent-gated Loading implementieren.
3. CSP/Script-Quellen anpassen wo nötig und dokumentieren.
4. Keine Fake-Publisher-IDs; Platzhalter klar kennzeichnen.

**Gate:** Code reviewfähig; Platzhalter vs. echte IDs transparent.

### PHASE 4 – VALIDATION

1. Consent accept/reject/revoke testen.
2. Layout/CLS auf Mobile/Desktop prüfen.
3. Konflikte mit Nav/Forms/Modals prüfen.
4. Network: Ads laden nur bei erlaubtem Consent.

**Gate:** Prüfprotokoll; Live-Status nur wenn bestätigt.

### PHASE 5 – DELIVERY

1. Platzierungsdokumentation + offene Policy-Punkte.
2. Prod-Go-Live nur nach User-Freigabe.
3. Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/adsense --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| IDs | Nur echte Quellen / sonst Blocker |
| UX | Keine kritische UI überdecken |
| Consent | Gate vor Ad-Load |
| Perf | CLS beobachten |
| Live | Nie ohne Bestätigung |

## Red Flags

- Erfundene `ca-pub` IDs
- Ads ohne Consent in regulierten Regionen
- Click-Anreize / überlappende CTAs
- „Live geschaltet“ ohne Nachweis
- Deploy ohne Freigabe

## Resources

- `references/ads-monetization-checklist.md`
- `scripts/scaffold_ad_placement_map.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
