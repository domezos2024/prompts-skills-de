---
name: visuelle-asset-fabrik
description: Use when creating or replacing missing/low-quality visual assets - icons, logos, illustrations, empty states, store art - with a rights-aware pipeline, format exports, optimization, and in-app visual verification.
---

# Visuelle Asset-Fabrik

## Overview

Erstellt und integriert fehlende oder qualitativ unzureichende visuelle Assets. Kernprinzip: **Bedarf inventarisieren → Gestaltungsregeln fixieren → produzieren/exportieren/optimieren → in der laufenden App prüfen.** Keine Schein-Dateien, keine Rechte-Blindflüge.

## When to Use

- Icons, Logos, Illustrationen, Empty States oder Store-Grafiken fehlen/sind minderwertig
- Asset-Formate/Größen inkonsistent; Dateien zu groß oder unscharf
- Einheitliche visuelle Regeln für neue Grafiken nötig

## When NOT to Use

- Vollständiges UI/UX-Redesign → `vollstaendige-ui-ux-transformation`
- Design-Tokens/Komponentenbibliothek → `automatischer-designsystem-architekt`
- Nur Conversion-Texte/CTAs → `conversion-orientiertes-oberflaechen-redesign`
- Kein visueller Bedarf (reine Code-Refaktorierung)

## Critical Guidelines

- MUST Branding, vorhandene Grafiken, Zielplattformen und Asset-Typen zuerst analysieren.
- MUST priorisierte Asset-Liste führen (Icons, Logos, Illustrationen, Previews, Hintergründe, Empty States, Store).
- MUST einheitliche Gestaltungsregeln vor Massenproduktion festlegen.
- MUST passende Formate exportieren (SVG/PNG/WebP u. a.) und Dateigröße/Schärfe/Transparenz prüfen.
- MUST Assets in der laufenden Anwendung visuell verifizieren.
- MUST Nutzungsrechte und Lizenzstatus dokumentieren.
- NEVER Dateien als vorhanden vortäuschen oder Platzhalter als finales Asset ausgeben.
- NEVER funktionierende Assets ohne nachvollziehbaren Grund ersetzen.
- NEVER urheberrechtlich unklare Quellen ungeprüft übernehmen.
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill visuelle-asset-fabrik --root .skill-runs/asset-factory
```

### PHASE 1 – DISCOVERY

1. Branding, Asset-Ordner, Naming, Plattformen (Web/App/Store) erfassen.
2. Fehlende/mangelhafte Assets nach `references/asset-production-checklist.md` listen.
3. Priorität P0–P3; Ist-Qualität und Lizenzstatus notieren.

**Gate:** Priorisierte Asset-Liste + Regel-Skizze existieren.

### PHASE 2 – PLANNING

1. Visuelle Regeln: Stil, Strichstärke, Farbbindung an Tokens/Brand, Ecken, Padding in ViewBox.
2. Produktionsplan: Quelle (Eigenzeichnung/Generierung/Lizenzbibliothek), Exportgrößen, Zielpfade.
3. Integrationspakete mit Rollback (alte Datei behalten bis Verifikation).

**Gate:** Plan mit Done-Kriterien und Rechte-Status pro Asset-Gruppe.

### PHASE 3 – IMPLEMENTATION

1. Assets produzieren; Namenskonvention und Ordnerstruktur einhalten.
2. Export SVG/PNG/WebP (und plattformspezifische Größen); optimieren.
3. In Code/Manifeste einbinden; Referenzen aktualisieren.
4. Manifest unter `artifacts/assets/ASSET_MANIFEST.md` pflegen.

**Gate:** P0/P1-Assets integriert; keine toten Referenzen bekannt.

### PHASE 4 – VALIDATION

1. App/Preview starten; jedes neue Asset visuell prüfen (Light/Dark, 1x/2x wo relevant).
2. Checkliste abhaken: Schärfe, Transparenz, Kontrast auf Hintergrund, Dateigröße.
3. Rechte-Spalte vollständig; keine Scheinpfade.

**Gate:** Visuelle Verifikation + Manifest ohne Lücken bei gelieferten Assets.

### PHASE 5 – DELIVERY

1. Delivery Report nach `_shared/references/delivery-report-template.md`.
2. Asset-Bibliothek, Dateiliste, Vorschauhinweise, Restbedarf nennen.
3. Checkpoint auf `done` setzen.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/asset-factory --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Inventar | Fehlt / mangelhaft / ersetzen? + Lizenz |
| Regeln | Stil vor Produktion fixieren |
| Pipeline | Produzieren → Export → Optimieren → Integrieren |
| Beweis | In-App-Screenshot + Manifestzeile |
| Stop | Rechte unklar oder Datei fingiert → nicht liefern |

## Red Flags

- „Asset erstellt“ ohne Datei im Repo
- Store-Grafiken ohne Größen-Spec
- SVG mit eingebetteten Riesen-PNGs
- Ersatz funktionierender Icons ohne Begründung
- Fertig ohne In-App-Check

## Resources

- `references/asset-production-checklist.md`
- `scripts/init_asset_manifest.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
