# CI/CD Pipeline Matrix

Jedes Item: `Pass` | `Fail` | `N/A` + Beweis (Workflow-Datei/Lauf-URL/Log).

## Trigger & Scope

- [ ] Push/PR-Trigger korrekt und nicht zu breit
- [ ] Path-Filter sinnvoll (falls nötig)
- [ ] Schedule nur wo begründet
- [ ] Fork-PRs ohne Secret-Exfiltration abgesichert

## Qualitätsstufen

| Stufe | Vorhanden | Fail-Fast | Hinweis |
|-------|-----------|-----------|---------|
| Format/Lint | | | |
| Unit Tests | | | |
| Integration/E2E | | | |
| Security (SAST/deps) | | | |
| Build | | | |
| Publish/Deploy | | | nur hinter Freigabe |

## Effizienz & Artefakte

- [ ] Dependency-Cache konfiguriert
- [ ] Cache-Keys stabil und korrekt invalidierend
- [ ] Build-Artefakte hochgeladen
- [ ] Retention dokumentiert

## Sicherheit & Freigabe

- [ ] Secrets nur über Secret-Store referenziert
- [ ] Least Privilege für Tokens/Permissions
- [ ] Production Deploy braucht manuelle Freigabe / Environment Gate
- [ ] Kein unkontrolliertes `workflow_dispatch` auf Prod ohne Schutz

## Nachweis

- [ ] Mindestens ein erfolgreicher oder bewusst geblockter Testlauf protokolliert
- [ ] Bekannte Flakes dokumentiert, nicht vertuscht
