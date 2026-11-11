# Proxy Deploy Runbook

Jedes Item: `Pass` | `Fail` | `N/A` + Beweis.

## Pre-Change Inventar

- [ ] Laufende Dienste und Owner erfasst
- [ ] Ports und Konflikte geprüft
- [ ] Domains / Server-Namen erfasst
- [ ] TLS-Zertifikate und Ablauf notiert
- [ ] Bestehende Proxy-Routen gelistet
- [ ] Baseline-URL-Checks bestehender Apps gespeichert

## Change Safety

- [ ] Config-Backup mit Timestamp abgelegt
- [ ] Diff reviewt (minimaler Scope)
- [ ] Syntax-Validation vor Reload
- [ ] Explizite Nutzerfreigabe für Reload/Cutover
- [ ] Rollback-Kommandos vorbereitet und getestet (wo möglich)

## Post-Change Checks

| Check | Neu | Alt-Routen | Evidence |
|-------|-----|------------|----------|
| HTTP→HTTPS | | | |
| Host/Path Routing | | | |
| Upstream Health | | | |
| Security Headers | | | |
| Latency Smoke | | | |

## Rollback

1. Backup-Config wiederherstellen
2. Syntax prüfen
3. Reload
4. Alt-Routen verifizieren
5. Incident-Notiz schreiben
