---
name: waechter-der-infrastruktursicherheit
description: Use when hardening authorized servers, containers, reverse proxies, TLS, security headers, network exposure, service accounts, or infra secrets - runs a strict multi-phase inventory, backup-first hardening, reachability validation, and rollback-documented workflow. No lockout without fallback.
---

# Wächter der Infrastruktursicherheit

## Overview

Härtet Server, Container, Reverse Proxy und öffentlich erreichbare Dienste. Kernprinzip: **Inventar → Backup → risikominimierende Hardening → Erreichbarkeit/Funktion validieren → Rollback bereit.** Keine Änderung, die Dienste ohne Rückfallweg aussperrt.

## When to Use

- TLS, Security-Header, Proxy-Regeln, offene Ports härten
- Container-Privilegien, Dateirechte, Dienstkonten, Secrets
- Öffentliche Angriffsfläche der Infra reduzieren

## When NOT to Use

- App-Code OWASP ohne Infra → `vollstaendige-sicherheitshaertung`
- AuthZ-Logik in der App → `audit-von-authentifizierung-und-berechtigungen`
- Unautorisierte Fremdsysteme scannen/ändern

## Critical Guidelines

- MUST Inventar von Diensten, Ports, Containern und Security-Configs erstellen.
- MUST vor Änderungen Config-Backups und Rollback-Schritte sichern.
- MUST TLS, Header, Proxy und Netzwerkfreigaben defensiv härten.
- MUST Least Privilege für Dienstkonten und Container (non-root wo möglich).
- MUST nach Änderungen Erreichbarkeit und Kernfunktion prüfen.
- NEVER Firewall/DNS/Proxy-Änderungen ohne abgesicherten Rückfallweg.
- NEVER destruktive Prod-Tests oder DoS; nur autorisierte Systeme.
- NEVER Secrets in Klartext-Commits/Tickets; Rotation über Secret Store.
- NEVER Exploit-PoCs; nur Baseline-Vergleich und sichere Defaults.
- ALWAYS Iron Laws und Phasenstatus.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill waechter-der-infrastruktursicherheit --root .skill-runs/infra-security
```

### PHASE 1 – DISCOVERY

1. Erreichbare Dienste, Ports, Container, Ingress/Proxy inventarisieren.
2. TLS-Zertifikate, Cipher/Header, Auth an der Edge prüfen.
3. Dateirechte, Service-User, Secrets-Mounts, Capabilities erfassen.
4. Checkliste `references/infra-hardening-checklist.md` abarbeiten.

**Gate:** Inventar + Risiko-Priorisierung existieren.

### PHASE 2 – PLANNING

1. Hardening-Pakete priorisieren (Exposure/P0 zuerst).
2. Pro Paket: Backup-Pfad, Change, Verify, Rollback.
3. Wartungsfenster/Autorisierung bestätigen falls Prod-nah.
4. Messbare Done-Kriterien (Header vorhanden, Port closed, Health OK).

**Gate:** Change-Plan mit Rollback freigegeben.

### PHASE 3 – HARDENING

1. Config-Backups anlegen (`scripts/backup_config_snapshot.py` oder äquivalent).
2. Unnötige Exposure schließen; Headers/TLS/Proxy-Regeln verschärfen.
3. Container: read-only rootfs, drop caps, non-root – schrittweise.
4. Nach jedem Paket: Health-/Reachability-Smoke.

**Gate:** Keine Self-Lockouts; P0-Exposure adressiert.

### PHASE 4 – VALIDATION

1. Erreichbarkeit kritischer Endpunkte und Admin-Zugangswege prüfen.
2. Security-Config gegen Checkliste verifizieren.
3. Fehlschläge sofort rollbacken und Ursache dokumentieren.
4. Nicht getestete Hosts/Umgebungen explizit markieren.

**Gate:** Verify-Protokoll + funktionierender Rollback-Nachweis oder ungenutzt dokumentiert.

### PHASE 5 – DELIVERY

1. Gehärtete Diffs, Prüfergebnisse, Rollback-Runbook.
2. Delivery Report; Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/infra-security --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Vorher | Inventar + Backup |
| Härten | Least exposure / privilege |
| Nachher | Health + Security verify |
| Stop | Änderung ohne Rollback |

## Red Flags

- SSH/Firewall zu ohne Break-Glass
- Prod-Chaos ohne Fenster
- Secrets in Image-Layers
- „Header gesetzt“ ohne Response-Check
- Fertig ohne PHASE 4

## Resources

- `references/infra-hardening-checklist.md`
- `scripts/backup_config_snapshot.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
