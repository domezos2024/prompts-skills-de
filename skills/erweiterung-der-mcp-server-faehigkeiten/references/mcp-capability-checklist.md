# MCP Capability Checklist

Jedes Item: `Pass` | `Fail` | `N/A` + Beweis (Datei/Log/Test).

## Inventar

- [ ] Alle Tools mit Name, Beschreibung, Input-Schema erfasst
- [ ] Resources und Prompts vollständig gelistet
- [ ] Service-/Backend-Methoden gegen Tools gemappt
- [ ] Auth-Modell (Scopes/Roles) dokumentiert

## Duplikate & Gaps

- [ ] Funktional äquivalente Tools markiert
- [ ] Fehlende High-Value-Fähigkeiten priorisiert (P0–P3)
- [ ] Ineffiziente Multi-Call-Ketten als Batch-Kandidaten notiert

## Verträge & Safety

- [ ] JSON-Schema/Zod o. Ä. für Inputs
- [ ] Strukturierte Fehlercodes (nicht nur Strings)
- [ ] Side-effecting Tools: Dry-Run/Confirm oder Approval
- [ ] Idempotenz-Schlüssel oder „safe retry“-Semantik dokumentiert
- [ ] Sensible Felder nicht in Logs/Responses geleakt

## Observability

- [ ] Tool-Aufrufe auditierbar (wer/was/wann/Ergebnis)
- [ ] Latenz/Fehlerzähler oder mindestens strukturierte Logs
- [ ] Rate-/Abuse-Grenzen wo relevant

## Tests

- [ ] Gültige Eingaben
- [ ] Ungültige Eingaben (Schema-Reject)
- [ ] Grenzwert/Empty/Large-Payload
- [ ] Auth-Deny-Pfad
- [ ] Regression bestehender Tools
