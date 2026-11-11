# Refactor-Risiko- & Paket-Checkliste

Jedes Item: `Pass` | `Fail` | `N/A` + Beweis. Übertrifft Prompt: Risikoklassen, Verhaltensvertrag und Dead-Code-Nachweispflicht.

## A. Baseline (vor erstem Diff)

- [ ] Build-Befehl dokumentiert und ausgeführt (Log-Pfad)
- [ ] Tests ausgeführt oder begründet nicht vorhanden
- [ ] Lint/Formatter/Static Analysis falls vorhanden ausgeführt
- [ ] Branch/Commit-Hash der Baseline notiert

## B. Hotspot-Inventar

| ID | Typ (Duplikat/Komplexität/Naming/Algo/Error/Logging) | Pfad | Risiko | Geplantes Paket |
|----|------------------------------------------------------|------|--------|-----------------|
| | | | P0–P3 | |

## C. Paket-Gate (pro Änderungspaket)

| Paket | Scope klar? | Tests vorher | Diff reviewbar? | Tests nachher | Verhalten unverändert belegt? |
|-------|-------------|--------------|-----------------|---------------|-------------------------------|
| | Ja/Nein | | | | |

## D. Qualitätsdimensionen

- [ ] Lesbarkeit verbessert oder gleichwertig (keine cleveren Einzeiler-Regressionen)
- [ ] Fehlerbehandlung konsistent im angefassten Bereich
- [ ] Logging ohne Secrets; sinnvolle Levels
- [ ] Ressourcen (Handles/Streams/Connections) korrekt geschlossen
- [ ] Formatierung nur projektkonform (kein Formatter-Krieg)

## E. Dead Code / Dependencies

- [ ] Ungenutzter Code: Referenzsuche/Tool-Output als Beweis abgelegt
- [ ] Keine „vielleicht später“-Löschung kritischer Public APIs ohne Migration
- [ ] Dependency-Entfernung mit Import-/Lockfile-Nachweis

## F. Sicherheits- & Verhaltensrisiken

- [ ] Auth/Payment/Crypto/Concurrency nur mit Extra-Tests angefasst
- [ ] Öffentliche APIs unverändert oder bewusst versioniert
- [ ] Keine stillen Default-Änderungen

## G. Abschluss

- [ ] Gesamte Suite erneut grün (oder Gaps explizit)
- [ ] Restschuldenliste aktualisiert
- [ ] Keine unbeabsichtigte Verhaltensänderung bekannt
