---
name: ci-cd-pipeline-architekt
description: Use when designing or hardening CI/CD pipelines, adding lint/test/security/build stages, caching, artifact handling, or gated release automation that keeps production deploys controlled.
---

# CI/CD-Pipeline-Architekt

## Overview

Baut eine robuste Pipeline, die Änderungen automatisch validiert und kontrolliert bereitstellt. Kernprinzip: **Ist-Workflows analysieren → Stufen definieren → implementieren → auf Branch testen → Secrets/Gates dokumentieren.** Produktionsdeploys bleiben freigabepflichtig.

## When to Use

- CI/CD fehlt, ist fragil oder unvollständig
- Lint/Test/Security/Build sollen automatisiert werden
- Release-Automation mit klaren Freigaberegeln nötig

## When NOT to Use

- Einmaliges manuelles Release-Paket → `vollstaendige-release-pipeline`
- Nur Dockerfile-Tuning → `docker-und-container-optimierung`
- Server/Proxy-Konfiguration ohne Pipeline → Server-Skill

## Critical Guidelines

- MUST Repo-Struktur, Buildsystem, Zielplattformen und vorhandene Workflows zuerst erfassen.
- MUST Stufen für Format, Lint, Tests, Security-Checks und Build definieren.
- MUST Caching und Artefaktverwaltung nachvollziehbar einrichten.
- MUST Pipeline auf geeignetem Branch/Testlauf verifizieren; Logs als Beweis.
- MUST benötigte Secrets und Berechtigungen dokumentieren – Werte nie committen.
- NEVER Produktions-Deploy oder Push zu geschützten Branches ohne explizite Nutzerfreigabe.
- NEVER Secrets in Logs, YAML-Klartext oder Tickets schreiben.
- NEVER flaky Steps als „grün“ werten ohne Reproduktion.
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill ci-cd-pipeline-architekt --root .skill-runs/cicd
```

### PHASE 1 – DISCOVERY

1. Vorhandene Workflows (Actions/GitLab/Azure/Jenkins) inventarisieren.
2. Build-/Test-Befehle lokal oder aus Docs ableiten.
3. Zielplattformen, Runner, Matrix-Bedarf, Deploy-Ziele notieren.
4. Audit nach `references/cicd-pipeline-matrix.md`.

**Gate:** Pipeline-Istzustand + Lückenliste P0–P3.

### PHASE 2 – PLANNING

1. Stufenreihenfolge und Fail-Fast-Regeln festlegen.
2. Caching-Schlüssel, Artefakt-Retention, Branch-Trigger planen.
3. Freigabemodell: Environment Protection / manual approval für Prod.
4. Rollback: Workflow-Revert-Pfad.

**Gate:** Architekturplan mit messbaren Done-Kriterien.

### PHASE 3 – IMPLEMENTATION

1. CI-Konfiguration implementieren (z. B. GitHub Actions).
2. Dependency-Caching und Artefakt-Upload einbauen.
3. Versions-/Release-Jobs nur hinter Freigabe-Gates.
4. Fehlermeldungen und required checks dokumentieren.

**Gate:** Konfigurationsdateien reviewfähig; keine Secrets im Repo.

### PHASE 4 – VALIDATION

1. Pipeline auf Feature-/Testbranch anstoßen (kein Prod-Deploy).
2. Fehlgeschlagene Steps beheben und erneut laufen lassen.
3. Matrix/Cache-Verhalten und Artefakt-Download prüfen.
4. Gate-Verhalten (Approval nötig) dokumentieren.

**Gate:** Nachweisbarer grüner oder bewusst geblockter Lauf mit Log-Referenz.

### PHASE 5 – DELIVERY

1. CI/CD-Dokumentation + Secret-Liste (Namen only).
2. Delivery Report; Prod-Enablement nur nach User-Freigabe.
3. Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/cicd --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Stufen | Format → Lint → Test → Security → Build |
| Cache | Deterministische Keys |
| Artefakte | Upload + Retention |
| Prod | Manual/Environment Gate |
| Secrets | Namen dokumentieren, Werte nie committen |

## Red Flags

- Deploy-on-push nach main ohne Freigabe
- Secrets im Klartext
- „Pipeline ok“ ohne Lauf-Log
- Nur Build, keine Tests bei vorhandener Testsuite
- Fertig ohne PHASE 4

## Resources

- `references/cicd-pipeline-matrix.md`
- `scripts/scaffold_workflow_stub.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
