---
name: backup-notfallwiederherstellung-und-rollback
description: Use when designing or implementing verifiable backup, disaster recovery, and rollback procedures - define RPO/RTO, encrypted versioned backups, integrity checks, and prove restore with an isolated test instead of assuming backups work.
---

# Backup, Notfallwiederherstellung & Rollback

## Overview

Entwickelt und implementiert ein überprüfbares Backup- und Wiederherstellungskonzept. Kernprinzip: **Kritische Assets inventarisieren → RPO/RTO setzen → Backups bauen → Restore isoliert beweisen.** Ein vorhandenes Backup allein ist kein Nachweis.

## When to Use

- Backup-/DR-Konzept fehlt oder ist ungetestet
- Rollback-Prozeduren für Releases/Deploys nötig
- Integrität, Aufbewahrung, Alerting für Sicherungen

## When NOT to Use

- Nur Release-Notes/Artefakte → `vollstaendige-release-pipeline`
- Nur Proxy-Deploy ohne DR → Server-Skill
- Reines Monitoring ohne Daten-Backup

## Critical Guidelines

- MUST kritische Dateien, DBs, Configs und Abhängigkeiten inventarisieren.
- MUST realistische RPO/RTO definieren und dokumentieren.
- MUST versionierte, nach Möglichkeit verschlüsselte Backups implementieren.
- MUST Aufbewahrung, Integritätschecks und Fehlerbenachrichtigung ergänzen.
- MUST Restore/Rollback isoliert an Testdaten oder Kopien nachweisen.
- NEVER Produktivdaten bei Restore-Tests überschreiben ohne explizite Freigabe.
- NEVER ungeprüfte Backups als „DR ready“ melden.
- NEVER Push/Deploy von Restore auf Prod ohne explizite Nutzerfreigabe.
- ALWAYS Phasenstatus anzeigen und `_shared` Iron Laws befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill backup-notfallwiederherstellung-und-rollback --root .skill-runs/backup-dr
```

### PHASE 1 – DISCOVERY

1. Datenklassifikation: was ist kritisch, wo liegt es, welche Konsistenz nötig.
2. Bestehende Backup-Jobs, Speicherorte, Schlüsselverwaltung prüfen.
3. Baseline: letzte erfolgreiche Sicherung, bekannte Lücken.
4. Audit nach `references/dr-restore-checklist.md`.

**Gate:** Asset-Inventar + vorläufige RPO/RTO.

### PHASE 2 – PLANNING

1. Backup-Strategie (voll/inkrementell), Verschlüsselung, Retention.
2. Restore-Runbooks und Rollback-Pfade je Szenario.
3. Isolierte Testumgebung für Restore festlegen.
4. Alerting bei Fail.

**Gate:** DR-Plan mit messbaren Zielen und Testmethode.

### PHASE 3 – IMPLEMENTATION

1. Backup-Scripts/Jobs implementieren oder härten.
2. Integritätsprüfungen und Retention einbauen.
3. Restore-/Rollback-Prozeduren als Runbook + Script.
4. Keine Prod-Overwrite-Defaults.

**Gate:** Jobs/Scripts reviewfähig; Dry-Run dokumentiert.

### PHASE 4 – VALIDATION

1. Backup erzeugen; Checksumme/Größe/Log prüfen.
2. Isolierten Restore durchführen; Erfolg beweisen.
3. Zeitmessung gegen RTO; Datenstand gegen RPO bewerten.
4. Rollback-Übung wo relevant.

**Gate:** Restore-Testprotokoll mit gemessenen Ergebnissen.

### PHASE 5 – DELIVERY

1. Betriebsdoku, Kontakte, Eskalation.
2. Delivery Report; Prod-Restore nur mit Freigabe.
3. Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/backup-dr --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Inventar | Daten, Config, Secrets-Refs |
| Ziele | RPO/RTO realistisch |
| Backup | versioniert + integrität |
| Beweis | isolierter Restore |
| Prod | nie ohne Freigabe überschreiben |

## Red Flags

- „Backup existiert“ ohne Restore-Test
- Prod bei Übung überschrieben
- Unverschlüsselte sensible Offsite-Kopien ohne Begründung
- Retention fehlt
- Fertig ohne PHASE 4

## Resources

- `references/dr-restore-checklist.md`
- `scripts/scaffold_dr_test_report.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
