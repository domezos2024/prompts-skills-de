---
name: docker-und-container-optimierung
description: Use when containerizing or optimizing Docker images and Compose setups for secure, lean runtime - multi-stage builds, least privilege, healthchecks, volumes, and measured image size without destructive prune on production data.
---

# Docker- & Container-Optimierung

## Overview

Containerisiert oder optimiert die Anwendung für sicheren, ressourcenschonenden Betrieb. Kernprinzip: **Laufzeit analysieren → Multi-Stage/schlanke Bases → Härten → Build/Start/Persistenz testen → messen.** Produktive Volumes bleiben unangetastet.

## When to Use

- Dockerfile/Compose fehlt oder ist aufgebläht/unsicher
- Imagegröße, Startzeit oder Privilegien optimieren
- Healthchecks, Netzgrenzen, Persistenz definieren

## When NOT to Use

- Nur CI ohne Container → `ci-cd-pipeline-architekt`
- Server/Proxy-Orchestrierung jenseits Container → Server-Skill
- Backup/DR-Konzept → Backup-Skill

## Critical Guidelines

- MUST Laufzeit, Abhängigkeiten, Ports und Persistenzanforderungen zuerst erfassen.
- MUST Multi-Stage-Builds und geeignete schlanke Base Images nutzen, wo sinnvoll.
- MUST Privilegien minimieren; keine eingebetteten Secrets.
- MUST Healthchecks, Netzwerkgrenzen und Volumes explizit definieren.
- MUST Build, Start, Neustart, Update und Datenpersistenz testen und messen.
- NEVER bestehende Volumes oder produktive Daten löschen/ersetzen.
- NEVER unkontrollierte `docker system prune` / volume prune auf Prod/Shared Hosts.
- NEVER Images pushen oder Cluster-Deploy ohne explizite Nutzerfreigabe.
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill docker-und-container-optimierung --root .skill-runs/docker
```

### PHASE 1 – DISCOVERY

1. App-Start, Ports, Env-Vars, Persistenzpfade dokumentieren.
2. Bestehende Dockerfiles/Compose prüfen.
3. Baseline: Imagegröße, Startzeit, bekannte Risiken.
4. Audit nach `references/container-hardening-checklist.md`.

**Gate:** Ist-Inventar + Baseline-Metriken.

### PHASE 2 – PLANNING

1. Target-Images, Stages, User, Networks, Volumes planen.
2. Secrets-Strategie (Build-Args meiden; Runtime-Secrets).
3. Testmatrix: build/run/restart/upgrade/persist.
4. Rollback: vorherige Tags/Compose behalten.

**Gate:** Plan mit messbaren Größen-/Sicherheitszielen.

### PHASE 3 – IMPLEMENTATION

1. Dockerfile/Compose umsetzen (Multi-Stage, non-root wo möglich).
2. Healthchecks und Resource-Limits setzen.
3. `.dockerignore` und Layer-Caching optimieren.
4. Lokale Builds iterieren; keine Prod-Daten mounten ohne Freigabe.

**Gate:** Build erfolgreich; Konfig reviewfähig.

### PHASE 4 – VALIDATION

1. Container starten, Healthcheck, Restart-Policy prüfen.
2. Persistenz mit Testdaten verifizieren.
3. Imagegröße und Startverhalten messen; Vorher/Nachher notieren.
4. Security-Basics: User, Ports, Secrets-Scan der Config.

**Gate:** Messergebnisse + Testprotokoll.

### PHASE 5 – DELIVERY

1. Deployment-Anleitung + Risiken.
2. Registry-Push/Deploy nur nach User-Freigabe.
3. Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/docker --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Build | Multi-Stage, schlanke Base |
| Security | non-root, no secrets in image |
| Ops | Healthcheck, Limits, Networks |
| Data | Volumes schützen, kein Blind-Prune |
| Proof | Größe/Start/Restart gemessen |

## Red Flags

- Root + Secrets im Image
- `prune -a --volumes` auf Shared Host
- Prod-Volume überschrieben
- Push ohne Freigabe
- „Optimiert“ ohne Messwerte

## Resources

- `references/container-hardening-checklist.md`
- `scripts/measure_image_notes.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
