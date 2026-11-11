---
name: serverbereitstellung-und-reverse-proxy-orchestrierung
description: Use when deploying an app onto an existing server behind a reverse proxy - inventory services/ports/TLS, backup configs, add routes safely, validate syntax, and preserve existing apps with an explicit rollback path.
---

# Serverbereitstellung & Reverse-Proxy-Orchestrierung

## Overview

Stellt eine Anwendung zuverlässig über vorhandenen Server und Reverse Proxy bereit. Kernprinzip: **Bestehende Dienste inventarisieren → Config sichern → minimal ändern → Syntax validieren → Erreichbarkeit und Alt-Routen testen.** Kein Blind-Reload gegen Produktion ohne Freigabe.

## When to Use

- App hinter Nginx/Caddy/Traefik/Apache anbinden
- Domain/TLS/Routing ohne Kollisionen erweitern
- Deployment inkl. Monitoring- und Rollback-Doku nötig

## When NOT to Use

- Nur Container-Build ohne Host-Proxy → `docker-und-container-optimierung`
- Nur CI-Deploy-Job ohne Serverarbeit → `ci-cd-pipeline-architekt`
- DR/Backup-Konzept → Backup-Skill

## Critical Guidelines

- MUST laufende Dienste, Domains, Ports, Routing und TLS zuerst erfassen.
- MUST relevante Server-/Proxy-Configs vor Änderung sichern.
- MUST Syntax validieren bevor Reload/Restart.
- MUST interne/externe Erreichbarkeit, TLS, Healthchecks und bestehende Routen testen.
- MUST Least Privilege für neue Dienste.
- NEVER bestehende Dienste/Routen brechen; bei Fail sofort Rollback.
- NEVER Reload/Deploy/DNS-Cutover ohne explizite Nutzerfreigabe.
- NEVER Secrets in Logs oder ungeschützte Config-Repos schreiben.
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill serverbereitstellung-und-reverse-proxy-orchestrierung --root .skill-runs/server-proxy
```

### PHASE 1 – DISCOVERY

1. Dienste, Listener, Domains, Zertifikate, Proxy-Chains inventarisieren.
2. Kollisionsrisiken (Ports, Pfade, Hostnames) markieren.
3. Baseline-Erreichbarkeit bestehender Apps notieren.
4. Audit nach `references/proxy-deploy-runbook.md`.

**Gate:** Inventar + Backup-Plan für Configs.

### PHASE 2 – PLANNING

1. Bereitstellungsoption ohne Konflikt wählen.
2. Diff der Proxy-Routen und Security-Header planen.
3. Validierungs- und Rollback-Schritte atomar formulieren.
4. Freigabe-Punkt für Reload/Cutover festlegen.

**Gate:** Change-Plan mit Rollback-Kommandos.

### PHASE 3 – IMPLEMENTATION

1. Config-Backups erstellen.
2. Dienst mit minimalen Rechten konfigurieren.
3. Proxy-Routen und Header ergänzen (noch kein Prod-Reload ohne Freigabe).
4. Syntax-Check der Config ausführen.

**Gate:** Diff + erfolgreicher Syntax-Check.

### PHASE 4 – VALIDATION

1. Nach Freigabe: Reload; sonst Staging/Dry-Run.
2. Neue Route, TLS, Healthcheck prüfen.
3. Alle dokumentierten Alt-Routen regressiv testen.
4. Bei Fail: Rollback aus Backup und erneut verifizieren.

**Gate:** Testprotokoll Alt+Neu grün oder Rollback nachgewiesen.

### PHASE 5 – DELIVERY

1. Deployment-, Monitoring- und Rollback-Doku.
2. Delivery Report; weitere Cutover nur mit Freigabe.
3. Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/server-proxy --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Inventar | Ports, Domains, TLS, Routen |
| Safety | Config-Backup vor Diff |
| Change | Minimal + Syntax-Check |
| Prove | Neu + Alt-Routen |
| Fail | Sofort Rollback |

## Red Flags

- Reload ohne Backup/Syntax-Check
- Bestehende Site down nach Change
- Deploy ohne User-Freigabe
- TLS „schon ok“ ohne Test
- Fertig ohne PHASE 4

## Resources

- `references/proxy-deploy-runbook.md`
- `scripts/scaffold_proxy_change_log.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
