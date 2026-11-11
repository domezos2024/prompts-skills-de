# DR Restore Checklist

Jedes Item: `Pass` | `Fail` | `N/A` + Beweis.

## Inventar & Ziele

- [ ] Kritische Assets gelistet (Files, DB, Config, Volumes)
- [ ] Abhängigkeiten (Runtime, Keys, DNS) erfasst
- [ ] RPO definiert und begründet
- [ ] RTO definiert und begründet
- [ ] Verantwortlichkeiten / Eskalation klar

## Backup-Qualität

- [ ] Versionierung vorhanden
- [ ] Verschlüsselung wo erforderlich
- [ ] Retention-Regeln aktiv
- [ ] Integritätscheck (Hash/Verify) läuft
- [ ] Fehlerbenachrichtigung getestet oder geplant
- [ ] Speicherort und Zugriffsrechte dokumentiert

## Restore-Beweis

| Szenario | Isoliert? | Dauer | Daten-OK | Evidence |
|----------|-----------|-------|----------|----------|
| File restore | | | | |
| DB restore | | | | |
| Config rollback | | | | |
| App start after restore | | | | |

## Verbote

- [ ] Kein Prod-Overwrite ohne explizite Nutzerfreigabe
- [ ] Keine Secrets in Klartext-Reports
