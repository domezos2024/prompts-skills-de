# Release Checklist

Jedes Item: `Pass` | `Fail` | `N/A` + Beweis (Befehl/Log/Datei).

## Repository & Version

- [ ] Working tree für Release-Scope bekannt (clean oder dokumentiert)
- [ ] Aktuelle Version / letzter Tag erfasst
- [ ] Neue Version nach Projektregeln gewählt
- [ ] Kein unbeabsichtigtes Überschreiben bestehender Tags/Releases geplant
- [ ] Changelog-Quellen (Commits/PRs) erfasst

## Qualitätstore

- [ ] Lint/Format (falls vorhanden) grün
- [ ] Unit-/Integrationstests grün oder Failures begründet geblockt
- [ ] Security-/SAST-Hinweise für P0 geprüft
- [ ] Release-Build reproduzierbar dokumentiert

## Artefakte

- [ ] Alle erwarteten Pakete erzeugt
- [ ] Checksummen (z. B. SHA256) vorhanden
- [ ] Manifest/Dateiliste vollständig
- [ ] Sandbox-Start / Smoke der Artefakte erfolgreich
- [ ] Keine Secrets in Artefakten

## Notes & Freigabe

- [ ] Release Notes faktisch korrekt
- [ ] Breaking Changes und Migrationen genannt
- [ ] Zielkanal und Berechtigungen geklärt
- [ ] Explizite Nutzerfreigabe für Push/Tag/Publish dokumentiert
- [ ] Rollback-Pfad beschrieben
