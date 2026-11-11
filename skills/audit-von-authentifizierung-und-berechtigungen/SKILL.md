---
name: audit-von-authentifizierung-und-berechtigungen
description: Use when auditing or improving authentication, sessions/tokens, RBAC/ABAC, least-privilege authorization, password-reset/logout/revocation, or privilege-escalation negative tests - runs a strict multi-phase access inventory, authZ design, server-side enforcement, and validated denial-path workflow.
---

# Audit von Authentifizierung & Berechtigungen

## Overview

Entwickelt oder härtet AuthN/AuthZ zuverlässig. Kernprinzip: **Rollen/Ressourcen inventarisieren → Least Privilege spezifizieren → serverseitig erzwingen → Negativtests gegen Escalation.** Jeder geschützte Zugriff wird serverseitig geprüft.

## When to Use

- Login, Sessions, Tokens, RBAC/ABAC unsicher oder unklar
- Privilege Escalation / IDOR-Verdacht defensiv prüfen
- Passwort-Reset, Logout, Revocation, Brute-Force-Schutz

## When NOT to Use

- Nur Infra/TLS → `waechter-der-infrastruktursicherheit`
- Nur allgemeine OWASP-Härtung → `vollstaendige-sicherheitshaertung`
- Unautorisierte Accounts fremder Systeme angreifen

## Critical Guidelines

- MUST Rollen, Permissions, Sessions und geschützte Ressourcen inventarisieren.
- MUST Autorisierung serverseitig an jeder geschützten Grenze prüfen.
- MUST Least Privilege und Deny-by-default als Default.
- MUST Negativtests: unauth, wrong role, cross-tenant, escalated action.
- MUST Token-Lebensdauer, Revocation, Reset und Session-Ende prüfen.
- NEVER client-only AuthZ als ausreichend akzeptieren.
- NEVER Exploit-Playbooks liefern; defensive Deny-Assertions und Fix-Pfade.
- NEVER Prod-Accounts sperren/zerstören ohne Freigabe; Lab/Stage bevorzugen.
- NEVER Secrets/Session-Tokens in Reports im Klartext.
- ALWAYS Iron Laws und Phasenstatus.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill audit-von-authentifizierung-und-berechtigungen --root .skill-runs/authz-audit
```

### PHASE 1 – DISCOVERY

1. User-Modell, Rollen, Permissions, Policies, Middleware/Guards erfassen.
2. Geschützte APIs/UI-Routen und Objektzugriffe (IDOR-Flächen) listen.
3. Session-/Token-Mechanik (Cookie, JWT, Refresh) dokumentieren.
4. Matrix `references/authz-matrix.md` initial befüllen.

**Gate:** Inventar + Matrix-Entwurf existieren.

### PHASE 2 – DESIGN

1. Rollen-/Permission-Konzept mit Least Privilege schärfen.
2. Policy-Entscheidungsstellen (central guard vs. scattered checks) vereinheitlichen.
3. Brute-Force-, Lockout-, Reset- und Logout-Flows spezifizieren.
4. Atomare Pakete + Negativtest-Akzeptanzkriterien.

**Gate:** AuthZ-Spec und Testmatrix freigegeben (intern).

### PHASE 3 – IMPLEMENTATION

1. Server-side Checks für alle P0-Ressourcen; Deny-by-default.
2. Session hardening: HttpOnly/Secure/SameSite wo Cookie; Rotation bei Login.
3. Revocation/Logout/Reset konsistent machen.
4. Nach jedem Paket: positive + negative Tests.

**Gate:** Keine bekannten P0 AuthZ-Lücken offen.

### PHASE 4 – VALIDATION

1. Matrix-Zellen ausführen: allow und deny.
2. Privilege-Escalation- und Cross-Tenant-Negativpfade.
3. Expired/revoked Token → 401/403 wie spezifiziert.
4. Ergebnisse protokollieren; Lücken fixen und re-testen.

**Gate:** Kritische Deny-Pfade belegt; Restlücken dokumentiert.

### PHASE 5 – DELIVERY

1. Berechtigungsmatrix, Annahmen, Tests, Restrisiken.
2. Delivery Report; Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/authz-audit --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Map | Roles × Resources × Actions |
| Enforce | Server-side, deny-by-default |
| Test | Unauth / Wrong role / Cross-tenant |
| Stop | UI-Hide als Security |

## Red Flags

- „Frontend prüft Rolle“
- Fehlende Object-Level AuthZ
- Refresh ohne Revocation
- Tests nur Happy Path
- Fertig ohne PHASE 4

## Resources

- `references/authz-matrix.md`
- `scripts/scaffold_authz_matrix.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
