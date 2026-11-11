# Phase Protocol – Universelles 5-Phasen-Modell

Jeder Skill mappt seine Domänenarbeit auf dieses Gerüst. Domänenphasen dürfen untergliedern, aber nie Phasen überspringen.

## PHASE 1 – DISCOVERY

**Ziel:** Verifizierter Istzustand.

Pflicht:
- Projektstruktur, Stack, Build, Tests, Konventionen erfassen
- Relevante Einstiegspunkte und kritische Pfade finden
- Risiken, Blocker, vorhandene Regeln (AGENTS.md, CLAUDE.md, CI) lesen
- Ausgangsmetriken notieren (Build, Tests, Größe, Perf, Coverage – was verfügbar ist)

Output: Architekturkurzüberblick + Baseline + offene Fragen (nur wenn wirklich blockierend)

## PHASE 2 – PLANNING

**Ziel:** Atomarer, priorisierter Ausführungsplan.

Pflicht:
- Arbeit in abhängigkeitsgeordnete Pakete zerlegen
- Akzeptanzkriterien messbar formulieren
- Checkpoints und Rollback-Strategie festlegen
- Out-of-scope explizit nennen

Output: Geordnete Taskliste mit P0–P3 und Done-Definition pro Paket

## PHASE 3 – IMPLEMENTATION

**Ziel:** Direkte, minimale, korrekte Änderungen im Projekt.

Pflicht:
- Vorhandene Konventionen und Tools nutzen
- Keine Doppelimplementierungen, keine unnötigen Dependencies
- Bestehende Funktionalität und Nutzerdaten bewahren
- Pro Paket: ändern → kurz validieren → erst dann weiter

Output: Diffs/Commits-würdiges Arbeitsergebnis (Commit nur auf Anweisung)

## PHASE 4 – VALIDATION

**Ziel:** Nachweis, dass Ziele erreicht sind.

Pflicht:
- Build, Tests, Linters/SCA ausführen soweit vorhanden
- Domänenspezifische Checks (UI, Security, A11y, Perf, …)
- Selbst eingeführte Fehler beheben und erneut prüfen
- Nicht geprüfte Bereiche ehrlich benennen

Output: Validierungsprotokoll mit Pass/Fail/Skipped + Gründen

## PHASE 5 – DELIVERY

**Ziel:** Übergabefähiges Paket.

Pflicht:
- Dokumentation aktualisieren wo nötig
- Änderungsübersicht (was/warum/Risiken)
- Restprobleme und nächste Schritte
- Release-Artefakte nur wenn Skill/User das verlangt

Output: Delivery-Report gemäß Skill-Template

## Statuszeile (immer)

```
STATUS: PHASE {N} – {Name} | Paket {i}/{n}: {kurz} | Letzte Validierung: {Pass|Fail|Skipped}
```
