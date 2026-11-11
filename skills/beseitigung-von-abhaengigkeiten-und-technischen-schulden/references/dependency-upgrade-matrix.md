# Dependency-Upgrade- & Debt-Matrix

Jedes Package: Entscheidung `Upgrade` | `Remove` | `Keep` | `Defer` + Beweis. Übertrifft Prompt: Batch-Disziplin, Breaking-Change-Gate, Security- und Unused-Nachweis.

## A. Inventar

| Ecosystem | Manifest(e) | Lockfile | Toolchain (Node/Java/Dotnet/…) |
|-----------|-------------|----------|--------------------------------|
| | | | |

| Package | Ist-Version | Latest relevant | Typ (direct/transitive) | Unused? | Advisory/CVE | Entscheidung |
|---------|-------------|-----------------|-------------------------|---------|--------------|--------------|
| | | | | Ja/Nein/Unklar | | Upgrade/Remove/Keep/Defer |

## B. Risikoklassen

- [ ] Security-critical (CVE/Advisory) priorisiert
- [ ] Major-Version-Lag markiert
- [ ] Abandoned / unmaintained markiert
- [ ] Duplicate / overlapping libraries markiert
- [ ] Build-tool / SDK-Drift notiert

## C. Batch-Plan

| Batch-ID | Inhalt (Packages) | Level (patch/minor/major) | Breaking notes gelesen? | Rollback | Test-Fokus | Status |
|----------|-------------------|---------------------------|-------------------------|----------|------------|--------|
| B1 | | | Ja/Nein | Lock revert | | |
| B2 | | | | | | |

## D. Breaking-Change-Gate (pro Major oder riskantem Minor)

- [ ] Changelog/Migration Guide gelesen (Link/Notiz)
- [ ] Betroffene Call-Sites gelistet
- [ ] API-Anpassungen umgesetzt oder Batch deferred
- [ ] Config/Peer-Dependencies geprüft

## E. Removal-Gate

- [ ] Referenzsuche ohne Treffer (oder nur Docs/Comments)
- [ ] Lockfile/Manifest bereinigt
- [ ] Build ohne Package grün

## F. Validation

- [ ] Build grün
- [ ] Unit/Integration/Regression ausgeführt (verfügbar = Pflicht)
- [ ] Security-Check ausgeführt oder begründet N/A
- [ ] Deferred-Items mit Owner/Follow-up versehen

## G. Policy

- [ ] Keine unkontrollierten Multi-Major-Batches
- [ ] Problematische Upgrades nachvollziehbar zurückgestellt (nicht verschwiegen)
