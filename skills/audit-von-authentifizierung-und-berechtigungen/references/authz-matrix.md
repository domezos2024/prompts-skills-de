# Authentifizierung & Berechtigungs-Matrix

Jedes Ergebnis: `Allow` | `Deny` | `N/A` + Evidence (Test/Log/Code). Defensiv – keine Angriffsanleitung.

## Rolleninventar

| Role | Beschreibung | Privileges (kurz) |
|------|--------------|-------------------|
| anonymous | | |
| user | | |
| admin | | |

## Ressourcen × Aktionen

| Resource | Action | anonymous | user | admin | Object-level check? | Evidence |
|----------|--------|-----------|------|-------|---------------------|----------|
| | read | | | | | |
| | write | | | | | |
| | delete | | | | | |

## Session / Token Checklist

- [ ] Login setzt Session/Token serverseitig nachvollziehbar
- [ ] Logout invalidiert Session/Refresh
- [ ] Absolute und Idle-Timeout definiert
- [ ] Password-Reset Tokens kurzlebig, einmalig, unschätzbar
- [ ] Brute-Force-/Rate-Limit an Login/Reset
- [ ] Keine Tokens in URLs/Logs

## Negativtest-Gate

| ID | Scenario | Expected | Result | Evidence |
|----|----------|----------|--------|----------|
| N1 | Unauthenticated access to protected resource | 401/403 | | |
| N2 | Authenticated but wrong role | 403 | | |
| N3 | Cross-tenant / foreign object ID | 403/404 | | |
| N4 | Expired token | 401 | | |
| N5 | Revoked/logged-out session | 401 | | |
| N6 | Privilege escalation via parameter tampering | Deny | | |

## Anti-Rationalisierung

| Ausrede | Realität |
|---------|----------|
| „UI blendet Button aus“ | Server muss deny |
| „Nur interne API“ | Trotzdem AuthZ |
| „Admin selten“ | Gerade Admin-Pfade härten |
| „Negativtest zu aufwendig“ | Ohne Deny-Beweis kein Gate-Pass |
