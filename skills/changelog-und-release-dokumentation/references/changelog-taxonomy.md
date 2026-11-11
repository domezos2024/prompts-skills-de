# Changelog Taxonomy

## Categories

| Category | Use for | User-facing? |
|----------|---------|--------------|
| Features | Neue Fähigkeiten | Ja, klar und begrenzt |
| Bugfixes | Korrekturen | Ja, wenn spürbar |
| Performance | Messbare/begründete Verbesserungen | Kurz |
| Security | Sicherheitsfixes | Ohne Exploit-Details |
| Breaking | Inkompatible Änderungen | Pflicht + Migration |
| Docs | Reine Doku | Optional im Tech-Log |
| Internal | Refactors ohne User-Impact | Tech-Log only |

## Verification rules

- [ ] Jeder Feature-Bullet hat Diff-/PR-Bezug
- [ ] Breaking Changes mit Migrationshinweis
- [ ] Unpublished als `Unreleased` markiert
- [ ] Keine erfundenen Versionsnummern

## Suggested files

- `CHANGELOG.md` (Keep-a-Changelog-ähnlich)
- `docs/releases/vX.Y.Z.md` (User notes)
- `docs/migrations/vX.Y.Z.md` (falls nötig)
