---
name: app-store-release-und-listing-optimierung
description: Use when preparing a mobile app for store release, optimizing listing copy/assets, checking SDK/privacy/package requirements, producing a signed release build, and validating install/core flows before an explicitly approved publish.
---

# App-Store-Release & Listing-Optimierung

## Overview

Bereitet eine mobile App technisch und visuell auf eine professionelle Store-Veröffentlichung vor. Kernprinzip: **Anforderungen prüfen → Listing & Assets → signierter Release-Build → Install/Smoke → nur freigegebenes Publish.** Keine erfundenen Features, keine fremden Signaturschlüssel.

## When to Use

- iOS/Android/Store-Release steht an
- Listing-Texte, Icons, Screenshots oder Lokalisierung fehlen/mangelhaft
- Release-Track / Signatur / Paketformat müssen geprüft werden

## When NOT to Use

- Nur allgemeines Changelog → `changelog-und-release-dokumentation`
- Nur UI-Redesign ohne Store → `vollstaendige-ui-ux-transformation`
- Web-Deploy ohne Stores

## Critical Guidelines

- MUST Funktionen, Version, Zielgruppe und bestehende Store-Metadaten erfassen.
- MUST offizielle Anforderungen (Paketformat, Ziel-SDK, Datenschutz, Assets) gegen Checkliste prüfen.
- MUST Kurz-/Langbeschreibung, Versionshinweise und Assets im Branding liefern.
- MUST Übersetzungen auf Qualität, Vollständigkeit und Längenlimits prüfen.
- MUST signierten Release-Build nur mit vorhandener autorisierter Signaturkonfiguration erzeugen.
- MUST Installationspaket und Kernfunktionen testen; Publish nur nach ausdrücklicher Freigabe.
- NEVER nicht vorhandene Features bewerben.
- NEVER unbekannte Signaturschlüssel ersetzen oder Secrets committen.
- NEVER ungeprüftes Live-Publish ohne Freigabe.
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill app-store-release-und-listing-optimierung --root .skill-runs/app-store-release
```

### PHASE 1 – DISCOVERY

1. App-Funktionen, Versionsstand, Bundle-IDs, Zielplattformen und bestehende Listings erfassen.
2. Privacy/Permissions, Target-SDK, Paketformat und Asset-Specs prüfen.
3. Scaffold mit `scripts/scaffold_store_listing.py` anlegen.
4. `references/store-release-checklist.md` abarbeiten.

**Gate:** Release-Readiness-Inventar + Anforderungslückenliste.

### PHASE 2 – PLANNING

1. Listing-Copy-Plan (Kurz/Lang/WhatsNew) und Keyword-Grenzen.
2. Asset-Plan: Icon, Screenshots, Feature-Grafik – Größen und Geräte.
3. Lokalisierungsplan und Längenlimits.
4. Build-/Signatur-/Track-Plan inkl. Rollback und Freigabe-Gate.

**Gate:** Plan mit messbaren Done-Kriterien und Publish-Freigabepunkt.

### PHASE 3 – IMPLEMENTATION

1. Store-Texte und Lokalisierungen erstellen/aktualisieren (nur echte Features).
2. Icons/Screenshots/Feature-Grafiken konsistent produzieren.
3. Release-Build über vorhandene autorisierte Signaturkonfiguration erzeugen.
4. Release-Track vorbereiten; **Publish nur bei ausdrücklicher Freigabe**.

**Gate:** Artefakte + Texte + Assets vorhanden; Publish-Status dokumentiert.

### PHASE 4 – VALIDATION

1. Installationspaket installieren/testen; Kernflows smoke-testen.
2. Asset-Maße und Textlängen gegen Spec prüfen.
3. Prüfprotokoll ohne unbelegte Pass-Claims.

**Gate:** Install/Smoke ok oder Blocker mit nächstem Schritt.

### PHASE 5 – DELIVERY

1. Release-Artefaktpfade, Listing-Paket, Prüfprotokoll und Restlücken.
2. Delivery Report; Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/app-store-release --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Specs | SDK, Privacy, Asset-Größen prüfen |
| Copy | Kurz/Lang/WhatsNew – nur echte Features |
| Build | Autorisierte Signatur, kein Key-Replace |
| Publish | Nur mit expliziter Freigabe |
| Stop | Erfundene Features / unbekannte Keys |

## Red Flags

- Features im Listing, die die App nicht hat
- Screenshots von Mockups als „Live“ verkauft
- Signaturkeys neu generiert ohne Auftrag
- Publish ohne Freigabe und ohne Install-Test
- Fertigmeldung ohne PHASE 4

## Resources

- `references/store-release-checklist.md`
- `scripts/scaffold_store_listing.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
