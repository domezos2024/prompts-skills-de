---
name: strict-code-quality-refactoring-ui-ux
description: Use when running a strict end-to-end code quality, refactoring, UI/UX, accessibility, performance, and re-audit workflow on the open project - identify, prioritize, implement, test, measure, re-audit, and document with hard phase gates and evidence.
---

# STRICT Code Quality, Refactoring & UI/UX Engineering

## Overview

Führt als interdisziplinäres Senior-Engineering-Team einen **kompromisslosen** Verbesserungszyklus über das geöffnete Projekt aus. Kernprinzip: **Identifizieren → Priorisieren → Implementieren → Testen → Messen → Erneut auditieren → Dokumentieren.** Nicht loben, nicht nur vorschlagen – nachweisbar beheben. Keine kosmetischen Scheinerfolge.

## When to Use

- Gesamtprojekt soll streng auf Qualität, Architektur, Security, UI/UX, A11y, Tests und Performance gehärtet werden
- Auftrag entspricht STRICT-/„extrem strenger Audit+Refactor“-Charakter
- Zweiter unabhängiger Audit nach eigenen Änderungen gefordert

## When NOT to Use

- Nur schlankes Projektaudit + Roadmap → `projektaudit-und-umsetzbare-roadmap`
- Nur UI-Transformation ohne Code-Audit-Tiefe → `vollstaendige-ui-ux-transformation`
- Master-Orchestrierung mehrerer fachlicher Prompts → `universeller-multi-workflow-master`

## Critical Guidelines

- MUST alle Phasen 1–9 sequentiell mit **harten Gates** durchlaufen; Status `PHASE X/9`.
- MUST verifizierte Fehler, Qualitätsmängel, Risiken und optionale Verbesserungen strikt trennen.
- MUST jedem bestätigten relevanten Mangel eine Maßnahme + P0–P3 zuordnen.
- MUST Refactorings nur bei erkennbarem Mehrwert (Verständlichkeit, Komplexität, Speed, Ressourcen, Reliability, Testbarkeit, Security, Wartung).
- MUST UI nicht nur im Code prüfen: Build/Start, Screens, Interaktionen, Zustandsmatrix.
- MUST fehlende Zustände (Idle→…→Empty/Offline/…) und verständliche Fehler-/Erfolgsmeldungen ergänzen.
- MUST nach Implementierung testen, Performance messen (keine Fantasieprozente), dann **zweiten** Audit machen.
- MUST `AUDIT-REFACTOR-UIUX-REPORT.md` mit Bewertungen 0–100 je Kategorie (begründet) liefern.
- NEVER loben statt fixen; NEVER erfundenen Tests/Metriken; NEVER destruktives Git/Secrets/Push ohne Freigabe.
- NEVER parallele Schreibagenten auf dieselben Dateien.
- ALWAYS `_shared` Iron Laws; Qualität vor Schein-Kürze; bestehende Fremdänderungen erhalten.

## Workflow

### PHASE 0 – Checkpoint & Tooling

```bash
python skills/_shared/scripts/checkpoint.py init --skill strict-code-quality-refactoring-ui-ux --root .skill-runs/strict
python skills/strict-code-quality-refactoring-ui-ux/scripts/scaffold_priority_matrix.py --out artifacts/strict/priority-matrix.md
python skills/strict-code-quality-refactoring-ui-ux/scripts/scaffold_audit_report.py --out AUDIT-REFACTOR-UIUX-REPORT.md
```

1. Git-Status, CLAUDE/AGENTS, verfügbare Skills/MCP/Build/Test/UI-Tools prüfen.
2. Referenzen laden: `references/strict-audit-dimensions.md`, `references/ui-state-matrix.md`, `references/definition-of-done.md`.

**Gate:** Checkpoint + Matrix- + Report-Scaffold existieren.

---

### PHASE 1/9 – VOLLSTÄNDIGE PROJEKTANALYSE (DISCOVERY)

**Status: PHASE 1/9 – Projekt verstehen und Ausgangszustand erfassen.**

1. Struktur, Sprache, Frameworks, Build-System.
2. Architektur, Module, Abhängigkeiten, zentrale Pfade, Datenflüsse, State.
3. Tests, Build-Varianten, QS-Tools, Docs/Regeln.
4. TODO/FIXME/HACK und vergleichbare Markierungen.
5. Initialer Build + vorhandene Tests; messbare Baseline (Größe/Build/Speed/Ressourcen) soweit möglich.

**Output:** Architekturübersicht + Ausgangszustand; Evidenzklassen getrennt.

**Gate:** Baseline dokumentiert; keine unbelegten Behauptungen. Sonst STOP/nachziehen.

---

### PHASE 2/9 – EXTREM STRENGER CODE-AUDIT

**Status: PHASE 2/9 – Kompromisslose technische Qualitätskontrolle.**

Audit nach `references/strict-audit-dimensions.md`:

- **A Codequalität:** Duplikate, Dead code, Naming, Länge, Nesting, Magic values, Globals, Smells, SOLID/DRY/KISS-Verletzungen.
- **B Performance/Ressourcen:** Allokationen, Leaks, Loops, Copies, IO, Main-Thread-Blocks, Render, Async, Assets, Caching, Skalierung.
- **C Funktionalität/Zuverlässigkeit:** Logik, Edge cases, Exceptions, Races, State, Validation, Resource lifetime, Retries, Timeouts, Datenverlust.
- **D Security:** Input, AuthZ, Sensitive storage, Log leakage, Path traversal, Vulnerable deps, Error isolation, Platform issues.

Jeder bestätigte Mangel → Maßnahme in Priority-Matrix (P0–P3).

**Gate:** Matrix mit Evidenz; P0/P1 vollständig zugeordnet. Keine leere „alles ok“-Aussage ohne Prüfung.

---

### PHASE 3/9 – STRENGES REFACTORING

**Status: PHASE 3/9 – Architektur und Implementierung verbessern.**

1. Toten/ungenutzten Code entfernen; Redundanzen zusammenführen.
2. SoC verbessern; Kontrollflüsse vereinfachen; unnötige Deps reduzieren.
3. Fehlerbehandlung/Logging/State vereinheitlichen; Modelle/APIs vereinfachen wenn sinnvoll.
4. Engpässe gezielt optimieren; Parallelität/Async verbessern; Ressourcen bereinigen.
5. Format/Konventionen; Testbarkeit/Modularität; **keine unnötigen Breaking Changes**; Funktionen erhalten.

**Qualitätsregel:** Jedes Refactoring braucht erkennbaren Vorteil (siehe Overview-Liste). Sonst unterlassen.

**Gate:** Diffs nachvollziehbar; P0/P1-Refactor-Pakete validiert (Smoke/Tests); Rollback bei Regression.

---

### PHASE 4/9 – EXTREM STRENGER UI/UX-AUDIT

**Status: PHASE 4/9 – UI und UX untersuchen.**

App bauen/starten soweit möglich. Screenshots/Emulator/Browser/A11y-Tools nutzen.

Prüfen laut STRICT-Abschnitten 4.1–4.7 und `references/ui-state-matrix.md`:

- Übersichtlichkeit, Designqualität, Interaktionszustände, Fehler-UX, Erfolgsfeedback, Bedienbarkeit, Accessibility (WCAG 2.2 AA wo anwendbar).

Befunde → Matrix (P0–P3), Evidenz (Screenshot/Notiz/Datei).

**Gate:** UI-Audit-Protokoll existiert; „nur Code gelesen“ reicht **nicht**, wenn Start möglich war (sonst `NICHT GETESTET` + Grund).

---

### PHASE 5/9 – UI/UX-VERBESSERUNGEN IMPLEMENTIEREN

**Status: PHASE 5/9 – Oberfläche professionell überarbeiten.**

1. Komponenten vereinheitlichen; Navigation/Anordnung verbessern.
2. Progress, Success/Error/Warning, Form-Validation, Empty States, Confirmations.
3. Button-Zustände; visuelle Inkonsistenzen; Touch/Keyboard; A11y.
4. Unnötige Interaktionen entfernen; konsistente Rückmeldungen.
5. Designsprache erhalten; Full-Redesign nur bei erheblichen Strukturmängeln.

**Gate:** Kritische UI-P0/P1 im Scope behoben; Flows bedienbar.

---

### PHASE 6/9 – FUNKTIONALITÄT, ROBUSTHEIT UND TESTS

**Status: PHASE 6/9 – Geänderte und bestehende Funktionen validieren.**

Ausführen soweit möglich: Build, Linter, SCA, Unit, Integration, UI, Navigation, Regression, Fehlerfälle, Grenzwerte, Perf, Memory, A11y, Security.

Interaktive Prüfung: Start → Kernfunktionen → Inputs → gültig/ungültig → Loading → Success → Cancel → Navigation → Wiederholung/Grenzen.

**Regel:** Funktion erst verifiziert nach Test oder nachvollziehbarer manueller Prüfung. Sonst `NICHT GETESTET`.

**Gate:** Validierungsprotokoll mit Pass/Fail/Skipped; neue Regressionen gefixt oder blockiert dokumentiert.

---

### PHASE 7/9 – PERFORMANCE- UND GRÖSSENOPTIMIERUNG

**Status: PHASE 7/9 – Effizienz anhand messbarer Ergebnisse.**

Baseline vs. danach: Build-/App-Größe, Start, Latency, Memory, CPU, Render, IO/DB, Hintergrundaktivität.

Nur reale Engpässe; keine „30 % schneller“ ohne Messung; keine Optimierung zulasten von Korrektheit/Security/Verständlichkeit.

**Gate:** Messprotokoll oder ehrliches `nicht messbar` mit Grund; Änderungen begründet.

---

### PHASE 8/9 – ZWEITER UNABHÄNGIGER QUALITÄTSAUDIT

**Status: PHASE 8/9 – Eigene Verbesserungen streng kontrollieren.**

Code wie von Fremden reviewen. Prüffragen:

1. Neue Fehler? 2. Funktionen erhalten? 3. Neue Smells? 4. Änderungen nötig? 5. Verständlicher? 6. Architektur konsistenter? 7. Error/State vollständig? 8. UI-Feedback zuverlässig? 9. Neue Deps gerechtfertigt? 10. Perf belegt? 11. Offene P0/P1? 12. Testumfang ok?

Gefundene Issues fixen und betroffene Tests wiederholen, bis keine sicher behebbaren kritischen Probleme im Auftrag offen sind.

**Gate:** Re-Audit-Protokoll; P0/P1 im Auftrag geschlossen oder mit Freigabe-Blocker.

---

### PHASE 9/9 – ABSCHLUSSBERICHT UND QUALITÄTSBEWERTUNG

**Status: PHASE 9/9 – Ergebnisse dokumentieren und bewerten.**

Report `AUDIT-REFACTOR-UIUX-REPORT.md` (Scaffold-Script) vollständig füllen:

1. Projektübersicht 2. Ursprüngliche Probleme 3. Verbesserungen 4. Refactoring 5. UI/UX 6. Tests 7. Performance 8. Restprobleme 9. Scores 0–100 je Kategorie mit Begründung + Gesamtbewertung (streng).

Definition of Done: `references/definition-of-done.md` abhaken.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/strict --phase 9 --step "delivery complete" --status done
```

**Gate:** Report existiert; DoD-Checkboxen nur mit Nachweis; unvermeidbare Lücken dokumentiert.

## Quick Reference

| Phase | Gate-Kurzform |
|-------|----------------|
| 1 | Baseline + Architektur |
| 2 | Audit-Matrix P0–P3 |
| 3 | Refactor mit Mehrwert + Smoke |
| 4 | UI-Audit mit Laufzeit-Evidenz |
| 5 | UI-Fixes P0/P1 |
| 6 | Testprotokoll |
| 7 | Messungen oder ehrlich skipped |
| 8 | Re-Audit clean/blocked |
| 9 | Report + DoD |

## Red Flags

- Analyse ohne Implementierung beendet
- Refactor ohne Vorteil / Breaking ohne Migration
- UI „verbessert“ ohne Start/Screenshot
- Scores ohne Befunde
- PHASE 8 übersprungen
- Erfundene Metriken/Tests

## Resources

- `references/strict-audit-dimensions.md`
- `references/ui-state-matrix.md`
- `references/definition-of-done.md`
- `scripts/scaffold_priority_matrix.py`
- `scripts/scaffold_audit_report.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
