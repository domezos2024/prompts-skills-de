---
name: beseitigung-von-abhaengigkeiten-und-technischen-schulden
description: Use when reducing dependency and technical debt - auditing packages and toolchains, planning safe upgrade batches, removing obsolete libraries, applying API fixes, and verifying with builds, security checks, and regression tests without uncontrolled majors.
---

# Beseitigung von Abhängigkeiten und technischen Schulden

## Overview

Reduziert technische Schulden, veraltete Abhängigkeiten und unnötige Projektkomplexität. Kernprinzip: **Inventar & Risiken → kleine Upgrade-Gruppen → Anpassen → Build/Security/Regression → problematische Majors bewusst zurückstellen.** Keine unkontrollierten Major-Upgrades.

## When to Use

- Veraltete, ungenutzte, inkompatible oder sicherheitskritische Packages
- Lockfiles/Toolchains driften; Obsolete Libraries belasten Builds
- Gezielter Debt-Abbau bei Dependencies und Konfiguration

## When NOT to Use

- Reines Code-Refactor ohne Dep-Fokus → `autonome-codebereinigung-und-refaktorierung`
- Architektur-Neuzuschnitt → `modernisierung-der-softwarearchitektur`
- Legacy ohne lauffähigen Build → zuerst `rettungsmission-fuer-altcode`
- UI-only Cosmetik → UI-Skills

## Critical Guidelines

- MUST Pakete, Frameworks, SDKs, Build-Tools und Versionsstände vollständig erfassen.
- MUST unused/outdated/incompatible/security-critical Abhängigkeiten identifizieren und belegen.
- MUST Release Notes / Breaking Changes vor Upgrades prüfen.
- MUST in kleinen, kontrollierbaren Gruppen aktualisieren.
- MUST obsolete Libraries entfernen und Konfiguration bereinigen; APIs anpassen.
- MUST Builds, Sicherheitsprüfungen und Regressionstests ausführen.
- NEVER unkontrollierte Major-Upgrades „auf gut Glück“.
- NEVER problematische Updates vertuschen — nachvollziehbar zurückstellen.
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill beseitigung-von-abhaengigkeiten-und-technischen-schulden --root .skill-runs/deps-debt
```

### PHASE 1 – DISCOVERY

1. Manifeste/Lockfiles/Toolchains inventarisieren.
2. Risiken nach `references/dependency-upgrade-matrix.md` (CVE, unused, major lag).
3. Baseline-Build/Test unter `artifacts/deps-baseline/`.

**Gate:** Inventar + Risikoliste + Baseline.

### PHASE 2 – PLANNING

1. Upgrade-Batches (patch/minor zuerst; majors isoliert).
2. Pro Batch: Breaking-Change-Notiz, betroffene Module, Rollback (Lockfile pin).
3. Entfernungs-Kandidaten ungenutzter Deps separat planen.

**Gate:** Batch-Plan mit expliziten Zurückstellungen.

### PHASE 3 – IMPLEMENTATION

1. Batches anwenden; Lockfiles commit-fähig halten.
2. API-Anpassungen und Config-Cleanup.
3. Obsolete Deps entfernen nach Nachweis.
4. Nach jedem Batch: Build + relevante Tests.

**Gate:** Geplante Batches integriert oder begründet deferred.

### PHASE 4 – VALIDATION

1. Volle Regression; Security-Scan falls verfügbar.
2. Matrix aktualisieren (Before/After-Versionen).
3. Deferred Majors mit Begründung und Follow-up.

**Gate:** Validierungsprotokoll; keine stillen Major-Sprünge.

### PHASE 5 – DELIVERY

1. Delivery Report nach `_shared/references/delivery-report-template.md`.
2. Bereinigte Abhängigkeiten, Lockfiles, Migrationsbericht, Deferred-Liste.
3. Checkpoint auf `done` setzen.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/deps-debt --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Inventar | Manifest + Lock + Toolchain |
| Batch | Klein, patch/minor first |
| Major | Isoliert + Notes + Rollback |
| Beweis | Build/Test/Security |
| Stop | Unkontrollierter Major → zurückstellen |

## Red Flags

- `latest` ohne Pin/Lock
- Mehrere Majors in einem Batch
- CVE ignoriert ohne Ticket/Defer-Begründung
- Unused „entfernt“ aber Import bleibt
- Fertig ohne Regression

## Resources

- `references/dependency-upgrade-matrix.md`
- `scripts/summarize_manifests.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
