---
name: umwandlung-in-eine-progressive-web-app
description: Use when adding Progressive Web App capabilities to an existing web app - web app manifest, icons, service worker caching with safe invalidation, offline fallbacks, and install/update tests without caching sensitive data uncontrolled.
---

# Umwandlung in eine Progressive Web App

## Overview

Erweitert eine bestehende Webanwendung um sinnvolle PWA-Funktionen. Kernprinzip: **Eignung prüfen → Manifest/Icons → Service Worker mit klarer Cache-Strategie → Install/Offline/Update testen.** Keine unkontrollierte Zwischenspeicherung sensibler Daten.

## When to Use

- Installierbarkeit / Offline-Grundfunktionen fehlen
- Manifest, Icons, Service Worker einführen oder härten
- Update-Hinweise und Cache-Invalidierung nötig

## When NOT to Use

- Nur SEO/Content → SEO-Skill
- Nur Performance ohne Offline-Scope → Website-Optimierung
- Native App-Store-Release ohne Web-PWA

## Critical Guidelines

- MUST Architektur, Assets und Browseranforderungen zuerst analysieren.
- MUST Eignung von Offline, Installation und Notifications bewusst entscheiden.
- MUST Web App Manifest und Icons korrekt implementieren.
- MUST Cache-Strategie und Invalidierung klar definieren und testen.
- MUST Offline-Fallbacks und Update-Erkennung absichern.
- NEVER sensible Inhalte unkontrolliert cachen.
- NEVER Push-Notifications ohne Nutzeraktion und Berechtigung erzwingen.
- NEVER Deploy der PWA-Prod-Version ohne explizite Nutzerfreigabe.
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill umwandlung-in-eine-progressive-web-app --root .skill-runs/pwa
```

### PHASE 1 – DISCOVERY

1. App-Shell, Asset-Pipeline, HTTPS/Hosting-Voraussetzungen prüfen.
2. Bestehende SW/Manifest-Reste inventarisieren.
3. Offline-Scope und Ausschlusslisten (Auth/API/Privacy) festlegen.
4. Checklist `references/pwa-readiness-checklist.md`.

**Gate:** PWA-Scope und No-Cache-Liste dokumentiert.

### PHASE 2 – PLANNING

1. Manifest-Felder, Icon-Größen, Display-Mode.
2. Cache-Strategien je Asset-Typ (cache-first/network-first etc.).
3. Update-UX und Rollback (SW unregister / version bump).
4. Optional: Notifications nur opt-in.

**Gate:** Strategiepapier mit Testfällen.

### PHASE 3 – IMPLEMENTATION

1. Manifest + Icons einbinden.
2. Service Worker mit versionierten Caches.
3. Offline-Fallback-Seiten/Routen.
4. Sichere Invalidierung bei Deploy-Version.

**Gate:** SW registriert in Dev/Test; keine Secrets im Cache-Plan.

### PHASE 4 – VALIDATION

1. Installierbarkeit (unterstützte Browser) testen.
2. Offline-Modus und Reconnect prüfen.
3. Update-Pfad (neue Version ersetzt Cache) verifizieren.
4. Privacy: sensible URLs nicht im Cache.

**Gate:** PWA-Testprotokoll mit Browserangaben.

### PHASE 5 – DELIVERY

1. Testdoku + Browser-Matrix + Restlücken.
2. Prod-Deploy nur nach User-Freigabe.
3. Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/pwa --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Manifest | Name, icons, display, start_url |
| SW | Klare Strategie + Version |
| Offline | Fallback + Scope |
| Privacy | Sensibles nicht cachen |
| Update | Invalidierung beweisen |

## Red Flags

- SW cached Auth-Responses blind
- Kein HTTPS in Zielumgebung
- Update bricht App durch Alt-Cache
- Notifications ohne Opt-in
- Fertig ohne Offline-Test

## Resources

- `references/pwa-readiness-checklist.md`
- `scripts/scaffold_pwa_test_matrix.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
