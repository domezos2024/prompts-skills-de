---
name: vollstaendige-website-optimierung
description: Use when optimizing an entire website for performance, technical SEO, UX, and accessibility across pages - inventory, audit, fix assets/metadata/links, then re-measure with before/after proof without inventing ranking gains.
---

# Vollständige Website-Optimierung

## Overview

Optimiert die gesamte Website inkl. Unterseiten für Technik, Geschwindigkeit, Nutzbarkeit und Auffindbarkeit. Kernprinzip: **Inventar → Audits → gezielte Fixes → Audits wiederholen mit Messwerten.** Keine Ranking-Behauptungen ohne Daten.

## When to Use

- Site-weite Performance-/SEO-/A11y-Schwächen
- Assets, Caching, Metadaten, Links, Sitemap reparieren
- Vorher/Nachher-Bericht gefordert

## When NOT to Use

- Nur SEO-Inhaltsarchitektur → `ingenieur-fuer-seo-und-inhaltsarchitektur`
- Nur WCAG-Fokus → `ingenieur-fuer-web-barrierefreiheit-und-konformitaet`
- Nur PWA → `umwandlung-in-eine-progressive-web-app`

## Critical Guidelines

- MUST Seiten, Templates, Assets und interne Links inventarisieren.
- MUST Audits für Performance, SEO, Accessibility und Best Practices ausführen und speichern.
- MUST URLs und bestehende Funktionen möglichst erhalten.
- MUST Bilder/Fonts/CSS/JS/Caching und Layout-/A11y-Probleme priorisiert beheben.
- MUST Audits wiederholen und deltas dokumentieren.
- NEVER verbesserte Rankings ohne Messdaten behaupten.
- NEVER Deploy/Publish der Live-Site ohne explizite Nutzerfreigabe.
- NEVER unbelegte Lighthouse-„100“-Claims.
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill vollstaendige-website-optimierung --root .skill-runs/website-opt
```

### PHASE 1 – DISCOVERY

1. Erreichbare Seiten/Templates/Assets/Linkgraph erfassen.
2. Baseline-Audits (Perf/SEO/A11y/Best Practices) speichern.
3. HTML-Struktur, Metas, Canonicals, Headings, Structured Data prüfen.
4. Audit nach `references/website-optimization-checklist.md`.

**Gate:** Inventar + Baseline-Artefakte.

### PHASE 2 – PLANNING

1. P0–P3 Maßnahmenpakete mit Akzeptanzmetriken.
2. URL-Erhalt und Redirect-Strategie festhalten.
3. Rollback für Template/Asset-Änderungen.

**Gate:** Priorisierter Plan mit Done-Kriterien.

### PHASE 3 – IMPLEMENTATION

1. Critical Rendering Path / Assets optimieren.
2. Metadaten, Sitemap, robots, interne Links/Redirects.
3. Layout- und Tastatur-/Screenreader-Barrieren schließen.
4. Smoke betroffener Seiten nach jedem Paket.

**Gate:** P0/P1 umgesetzt; keine bekannten Breakages.

### PHASE 4 – VALIDATION

1. Audits wiederholen; Vorher/Nachher tabellieren.
2. Link-Checker/Sitemap/robots verifizieren.
3. Regressions fixen und re-messen.

**Gate:** Messbericht ohne unbelegte Claims.

### PHASE 5 – DELIVERY

1. Vorher/Nachher-Bericht + Restlücken.
2. Live-Deploy nur nach User-Freigabe.
3. Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/website-opt --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Inventar | Seiten + Assets + Links |
| Baseline | Audits speichern |
| Fix | Perf → Tech SEO → A11y |
| Beweis | Re-Audit Deltas |
| Stop | Keine Ranking-Fantasie |

## Red Flags

- Fixes ohne Baseline
- URL-Brüche ohne Redirect
- „SEO besser“ ohne Daten
- Deploy ohne Freigabe
- Fertig ohne Re-Audit

## Resources

- `references/website-optimization-checklist.md`
- `scripts/scaffold_audit_comparison.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
