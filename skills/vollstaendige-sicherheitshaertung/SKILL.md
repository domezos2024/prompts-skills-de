---
name: vollstaendige-sicherheitshaertung
description: Use when hardening an authorized application against realistic threats, building threat models, fixing OWASP-class issues, reviewing secrets/deps/config, or adding security regression tests - runs a strict multi-phase discovery, threat modeling, defensive hardening, and validated retest workflow.
---

# Vollständige Sicherheitshärtung

## Overview

Härtet eine autorisierte Anwendung gegen realistische Bedrohungen. Kernprinzip: **Angriffsfläche beweisen → Threat Model priorisieren → defensive Fixes → Security-Regression validieren.** Keine Exploit-PoCs als Angriffsanleitung; Fokus auf Nachweis und Härtung.

## When to Use

- Security-Review oder Secure-Code-Review der gesamten App
- OWASP-/Auth-/Input-/Secret-/Dependency-Risiken beheben
- Security-Regressionstests und Restrisiko-Dokumentation nötig

## When NOT to Use

- Nur AuthZ/AuthN-Audit → `audit-von-authentifizierung-und-berechtigungen`
- Nur Krypto/Key-Mgmt → `architekt-fuer-verschluesselung-und-schluesselverwaltung`
- Nur Infra/TLS/Container → `waechter-der-infrastruktursicherheit`
- Unautorisierte Systeme, Red-Team gegen Dritte, produktive Chaos-/DoS-Tests

## Critical Guidelines

- MUST nur autorisierte Systeme und vereinbarte Umgebungen prüfen.
- MUST Threat Model mit Assets, Actors, Trust Boundaries und priorisierten Risiken erstellen.
- MUST Findings mit Evidence (Datei, Config, Test) und Schwere P0–P3 belegen.
- MUST Schutzmaßnahmen defensiv umsetzen (Validierung, AuthZ, Secure Defaults, Least Privilege).
- MUST Security-Regressionstests für behobene Klassen ergänzen und ausführen.
- NEVER destruktive oder produktionsgefährdende Tests ohne Freigabe.
- NEVER Exploit-/Payload-Anleitungen liefern; nur defensive Nachweise (Fail-closed, Deny-by-default).
- NEVER Secrets committen, loggen oder in Reports im Klartext belassen.
- NEVER „sicher“ ohne Retest und dokumentierte Restrisiken behaupten.
- ALWAYS `_shared` Iron Laws und Phasenstatus befolgen.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill vollstaendige-sicherheitshaertung --root .skill-runs/security-hardening
```

### PHASE 1 – DISCOVERY (Angriffsfläche)

1. Architektur, Einstiegspunkte, APIs, Admin-Flächen, Uploads, Webhooks, Jobs erfassen.
2. Trust Boundaries, externe Abhängigkeiten, Datenspeicher und Secret-Quellen inventarisieren.
3. Baseline: vorhandene Security-Tests, Scanner, Config-Hardening dokumentieren.
4. Checkliste `references/threat-hardening-checklist.md` abarbeiten; nur Verifiziertes.

**Gate:** Asset-/Entry-Inventar + Baseline-Notizen existieren.

### PHASE 2 – THREAT MODEL & PLAN

1. Threat Model: Spoofing, Tampering, Repudiation, Information Disclosure, DoS, Elevation (STRIDE-artig).
2. Risiken nach Schwere × Ausnutzbarkeit priorisieren; Top-Risiken mit Angriffspfad (defensiv beschrieben).
3. Härteplan in atomare Pakete: Auth, Input, Session, Secrets, Dependencies, Error Handling, Logging.
4. Messbare Akzeptanzkriterien und Rollback pro Paket.

**Gate:** Priorisierte Risikomatrix + Implementierungspakete mit Done-Kriterien.

### PHASE 3 – HARDENING (Implement)

1. P0/P1 zuerst: serverseitige AuthZ, Input-Validierung, Secret-Handling, sichere Defaults.
2. Dependencies/Configs prüfen; unsichere Defaults und bekannte CVE-relevante Libs behandeln.
3. Fehlerantworten ohne Leak von Stacktraces/Interna; Rate Limits wo sinnvoll.
4. Nach jedem Paket: relevante Unit/Integration/Security-Smoke.

**Gate:** Keine offenen P0; P1 entweder behoben oder mit akzeptiertem Risiko dokumentiert.

### PHASE 4 – VALIDATION (Retest)

1. Behobene Schwachstellenklassen gezielt retesten (Negativtests, Deny-Pfade).
2. Automatisierte Security-Regression ausführen; Ergebnisse protokollieren.
3. Restrisiken und nicht getestete Flächen explizit listen.
4. Anti-Rationalisierung: kein „vermutlich sicher“ ohne Lauf.

**Gate:** Validierungsprotokoll mit Pass/Fail/Evidence; keine unbelegten Claims.

### PHASE 5 – DELIVERY

1. Sicherheitsbericht: Threat Model, Fixes, Tests, Restrisikomatrix.
2. Delivery Report nach `_shared/references/delivery-report-template.md`.
3. Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/security-hardening --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Scope | Nur autorisierte Targets |
| Modell | Assets → Boundaries → Risiken |
| Fix | Defensive Controls + Least Privilege |
| Beweis | Retest + Regression |
| Stop | Kein Retest → nicht fertig |

## Red Flags

- Exploit-PoC statt Fix/Härtung
- Prod-Scan ohne Autorisierung
- Secrets in Issues/Commits
- „OWASP abgehakt“ ohne Evidence
- Fertigmeldung ohne PHASE 4

## Resources

- `references/threat-hardening-checklist.md`
- `scripts/scaffold_threat_model.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
