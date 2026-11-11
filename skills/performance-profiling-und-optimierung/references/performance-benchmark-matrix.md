# Performance-Benchmark-Matrix

Jedes Szenario: Zahlen + Methode + Umgebung. Übertrifft Prompt: Vergleichbarkeitsregeln, Hypothesen-Tracking, Regressions-Spalten.

## A. Umgebung (MUSS identisch für Before/After sein)

| Feld | Wert |
|------|------|
| Maschine / CI-Runner | |
| OS / Runtime-Version | |
| Build-Typ (Debug/Release) | |
| Datensatz / Fixture | |
| Warmup / Iterationen | |
| Parallele Last | |
| Commit Before | |
| Commit After | |

## B. Szenarien & Metriken

| ID | Szenario | Metrik | Einheit | Tool/Methode | Baseline | Nachher | Δ | Signifikant? | Notes |
|----|----------|--------|---------|--------------|----------|---------|---|--------------|-------|
| S1 | Startzeit | cold start | ms | | | | | Ja/Nein/Unklar | |
| S2 | Primärer Userflow | latency p50/p95 | ms | | | | | | |
| S3 | CPU-Hotspot | CPU % / samples | | | | | | | |
| S4 | Speicher | RSS / heap peak | MB | | | | | | |
| S5 | I/O | reads/writes / time | | | | | | | |

## C. Hotspot-Analyse

| Hotspot | Evidence (Profil-Datei) | Ursache (Hypothese) | Geplante Fix | Risiko |
|---------|-------------------------|---------------------|-------------|--------|
| | | | | |

## D. Optimierungs-Log

| Change-ID | Hypothese | Implementiert in | Messung danach | Behalten? | Begründung |
|-----------|-----------|------------------|----------------|-----------|------------|
| | | | | Ja/Nein | |

## E. Vergleichbarkeits-Gate

- [ ] Gleiche Hardware/Runner-Klasse
- [ ] Gleicher Datensatz
- [ ] Gleicher Build-Modus
- [ ] Warmup-Politik dokumentiert und gleich
- [ ] Ausreißer / Varianz notiert (nicht nur Best-Run cherrypicken)

## F. Korrektheit & Regression

- [ ] Funktionale Tests/Smoke der betroffenen Pfade grün
- [ ] Keine neuen offensichtlichen Latenzregressionen in Sekundärszenarien
- [ ] Cache-Kohärenz / Thread-Safety bedacht wo relevant

## G. Claim-Regeln

- [ ] Jede „Optimierung“-Aussage referenziert eine Matrixzeile
- [ ] Unklare Δ als „unklar/nicht signifikant“ markiert — nicht als Erfolg verkauft
