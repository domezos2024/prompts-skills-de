# Infrastruktur-Härtungs-Checkliste

Jedes Item: `Pass` | `Fail` | `N/A` + Evidence. Nur autorisierte Systeme. Backup vor Change.

## Inventar

- [ ] Hosts/Services/Ports erfasst
- [ ] Container/Orchestration-Objekte erfasst
- [ ] Reverse Proxy / Ingress Regeln erfasst
- [ ] Öffentliche vs. interne Exposure getrennt

## TLS & Edge

- [ ] Gültige Zertifikate / Ketten
- [ ] HTTPS erzwungen wo vorgesehen
- [ ] Veraltete Protokolle/Ciphers abgeschaltet (lab/stage first)
- [ ] Security-Header (CSP/HSTS/XFO/Referrer/… kontextabhängig)
- [ ] Admin-Interfaces nicht unnötig öffentlich

## Netzwerk & Zugriff

- [ ] Unnötige Ports geschlossen oder gebunden
- [ ] Management-Zugang eingeschränkt
- [ ] Rate limits / WAF-Regeln wo vorhanden geprüft
- [ ] Rollback für Firewall/DNS/Proxy dokumentiert

## Host & Container

- [ ] Dienstkonten Least Privilege
- [ ] Dateirechte für Keys/Configs restriktiv
- [ ] Container non-root / dropped capabilities wo möglich
- [ ] Secrets nicht in Images/ENV-History
- [ ] Read-only mounts wo praktikabel

## Change Gate

| Change | Backup path | Verify | Rollback | Result |
|--------|-------------|--------|----------|--------|
| | | | | |

## Anti-Rationalisierung

| Ausrede | Realität |
|---------|----------|
| „Kurz ohne Backup“ | Kein Gate-Pass |
| „Firewall hart zu = sicher“ | Lockout = Failure |
| „Nur Dev-Compose“ | Patterns trotzdem härten |
| „Header reichen allein“ | Exposure + Auth + Patching mitdenken |
