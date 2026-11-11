# Threat & Hardening Checklist

Jedes Item: `Pass` | `Fail` | `N/A` + Evidence (Datei/Test/Config). Nur autorisierte Systeme.

## Scope & Autorisierung

- [ ] Zielsystem/Umgebung schriftlich autorisiert
- [ ] Keine destruktiven Prod-Tests geplant
- [ ] Secret-Handling-Regel für Reports klar

## Angriffsfläche

- [ ] Öffentliche Endpunkte inventarisiert
- [ ] Admin/Debug/Internal-Routen erfasst
- [ ] Uploads, Webhooks, Jobs, Queues erfasst
- [ ] Trust Boundaries dokumentiert

## AuthN / AuthZ (defensiv)

- [ ] Geschützte Ressourcen serverseitig geprüft
- [ ] Session/Token-Lebensdauer und Widerruf geprüft
- [ ] Privilege Escalation-Negativpfade getestet
- [ ] Keine clientseitige-only Autorisierung

## Input & Daten

- [ ] Validierung an Trust Boundary
- [ ] Output-Encoding / Template-Sicherheit wo relevant
- [ ] Path-/Injection-relevante APIs abgesichert
- [ ] Datei-Uploads: Typ/Größe/Speicherort geprüft

## Secrets & Config

- [ ] Keine Secrets im Repo/Klartext-Config
- [ ] Env/Secret-Store Nutzung verifiziert
- [ ] Debug-Flags in Prod aus
- [ ] Fehlerantworten ohne interne Leaks

## Dependencies

- [ ] Dependency-Inventar vorhanden
- [ ] Kritische bekannte Schwachstellen adressiert oder risk-accepted
- [ ] Lockfiles konsistent

## Logging & Abuse

- [ ] Security-relevante Events geloggt (ohne PII/Secrets)
- [ ] Rate Limiting / Lockout wo sinnvoll
- [ ] CSRF/CORS-Policies geprüft (falls Web)

## Threat-Model-Matrix (Auszug)

| Asset | Threat | Control | Severity | Retest |
|-------|--------|---------|----------|--------|
| | | | P0–P3 | Pass/Fail |

## Anti-Rationalisierung

| Ausrede | Realität |
|---------|----------|
| „Nur Scanner reicht“ | Threat Model + manuelle Review der kritischen Pfade |
| „PoC zum Beweis nötig“ | Defensiver Negativtest / Deny-Assertion reicht |
| „Prod schneller“ | Nur freigegebene nicht-destruktive Checks |
| „Fix ohne Test“ | Security-Regression Pflicht |
