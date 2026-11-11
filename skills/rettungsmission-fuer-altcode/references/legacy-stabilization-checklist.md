# Legacy-Stabilisierungs-Checkliste

Jedes Item: `Pass` | `Fail` | `N/A` + Beweis. Übertrifft Prompt: Build-Repro-Gate, Charakterisierungsmatrix, Risikoregister und Betriebsübergabe.

## A. Landschaft & Einstiege

| Einstieg | Typ (CLI/API/UI/Job) | Pfad/Kommando | Runtime-Annahme | Status |
|----------|----------------------|---------------|-----------------|--------|
| | | | | läuft/unklar/gebrochen |

- [ ] Config-Quellen katalogisiert (Env, Files, Secrets-Stellen ohne Secret-Werte)
- [ ] Abhängigkeiten/Toolversions grob erfasst
- [ ] Datenflüsse der Top-Funktionen skizziert

## B. Funktionsrekonstruktion

| Feature / Flow | Beobachtetes Verhalten | Evidence | Datenstores | Kritikalität |
|----------------|------------------------|----------|-------------|--------------|
| | | | | P0–P3 |

## C. Build- & Env-Repro-Gate (vor Umbau)

- [ ] Sauberer Checkout baut mit dokumentierten Schritten
- [ ] Toolchain-Versionen notiert (oder Container/Devcontainer)
- [ ] Bekannte Flakiness/Env-Fallen dokumentiert
- [ ] Artefakt: `BUILD.md` oder gleichwertig im Lieferumfang

## D. Charakterisierungs-Testmatrix

| Flow | Testart (unit/integration/e2e/golden) | Abgedecktes Ist-Verhalten | Datei | Grün? |
|------|----------------------------------------|---------------------------|-------|-------|
| | | | | |

- [ ] Mindestens Kern-P0-Flows haben Charakterisierung bevor riskanter Refactor
- [ ] Bekanntes „falsches aber produktives“ Verhalten bewusst festgehalten (nicht still „repariert“)

## E. Defekt- & Risiko-Register

| ID | Problem | Impact | Ausbeut-/Ausfallrisiko | Fix unter Tests? | Status |
|----|---------|--------|------------------------|------------------|--------|
| | | | | Ja/Nein | |

- [ ] Nicht mehr unterstützte Interfaces markiert
- [ ] Riskante Module (Auth, Money, Sync, Filesystem) extra abgesichert

## F. Umbau-Disziplin

- [ ] Keine Big-Bang-Rewrite-Schritte ohne explizite Entscheidung
- [ ] Jede Verhaltensänderung an Tests gekoppelt
- [ ] Rollback-Pfad für riskante Schritte notiert

## G. Betriebs- & Wartungsübergabe

- [ ] Architekturübersicht (auch grob) vorhanden
- [ ] Start/Stop/Build/Test dokumentiert
- [ ] Bekannte Schulden & nächste sichere Schritte gelistet
- [ ] Kernfunktionen überprüfbar funktionsfähig
