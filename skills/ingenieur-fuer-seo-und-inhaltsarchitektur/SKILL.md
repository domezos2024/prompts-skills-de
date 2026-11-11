---
name: ingenieur-fuer-seo-und-inhaltsarchitektur
description: Use when improving technical SEO and content information architecture - fix duplicate content, metadata, headings, internal links, sitemaps, canonicals, and justified structured data without inventing ratings or ranking promises.
---

# Ingenieur für SEO & Inhaltsarchitektur

## Overview

Verbessert technische Auffindbarkeit und inhaltliche Struktur. Kernprinzip: **Hierarchie und Intention analysieren → IA und Metadaten planen → implementieren → Crawlbarkeit prüfen.** Keine erfundenen Bewertungen oder SERP-Versprechen.

## When to Use

- Schwache Titles/Descriptions/Headings
- Unklare Seitenhierarchie, Duplicate Content
- Canonicals, Sitemap, Indexierung, Structured Data

## When NOT to Use

- Breite Perf+A11y-Website-Optimierung → `vollstaendige-website-optimierung`
- Reine WCAG-Arbeit → A11y-Skill
- AdSense/Monetarisierung → AdSense-Skill

## Critical Guidelines

- MUST Seitenhierarchie, Suchintentionen und Inhalte zuerst analysieren.
- MUST Duplicate Content, fehlende Metas und unklare Seitenziele priorisieren.
- MUST Structured Data nur bei tatsächlich gerechtfertigten Inhalten.
- MUST Canonicals, Sitemap und Indexierungsregeln aktualisieren und prüfen.
- MUST Rendering/Crawlbarkeit technisch verifizieren.
- NEVER erfundene AggregateRating/Organization-Properties oder Ranking-Garantien.
- NEVER Live-Index-Änderungen/Deploy ohne explizite Nutzerfreigabe.
- NEVER Keywords stuffing oder irreführende Titles.
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill ingenieur-fuer-seo-und-inhaltsarchitektur --root .skill-runs/seo-ia
```

### PHASE 1 – DISCOVERY

1. Sitemap/Nav/URL-Muster und Content-Typen erfassen.
2. Metadaten, Headings, Canonicals, Index-Signale auditieren.
3. Duplicate/Thin/Conflicting Intent finden.
4. Matrix nach `references/seo-ia-matrix.md`.

**Gate:** SEO-Befundliste P0–P3.

### PHASE 2 – PLANNING

1. Ziel-Informationsarchitektur und URL-Policy.
2. Metadata-Standards und Internal-Link-Muster.
3. Structured-Data-Kandidaten nur mit Inhaltsnachweis.
4. Redirect-/Canonical-Plan.

**Gate:** IA-Plan + Akzeptanzkriterien.

### PHASE 3 – IMPLEMENTATION

1. Titles, Descriptions, Headings, interne Links umsetzen.
2. Canonicals, robots, Sitemap aktualisieren.
3. Structured Data validierbar einbauen wo gerechtfertigt.
4. Templates konsistent halten.

**Gate:** Diffs reviewfähig; keine Fake-Schema-Fakten.

### PHASE 4 – VALIDATION

1. HTML-Rendering und Meta-Ausgabe prüfen.
2. Sitemap/robots/Canonical-Konsistenz testen.
3. Structured Data nur mit Validator-Beweis.
4. Crawl-Simulation/Link-Check wo verfügbar.

**Gate:** Technisches SEO-Protokoll ohne SERP-Claims.

### PHASE 5 – DELIVERY

1. SEO-Auditbericht + offene Content-Lücken.
2. Deploy/Search-Console-Einreichung nur mit Freigabe.
3. Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/seo-ia --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| IA | Hierarchie + Intent |
| Meta | Unique Title/Description |
| Links | Interne Kohärenz |
| Schema | Nur echte Inhalte |
| Index | Canonical/Sitemap/robots |

## Red Flags

- Fake Reviews/Ratings im Schema
- Ranking-Versprechen
- Sitemap ≠ echte URLs
- Duplicate Titles ignoriert
- Fertig ohne Crawl-Check

## Resources

- `references/seo-ia-matrix.md`
- `scripts/scaffold_seo_audit.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
