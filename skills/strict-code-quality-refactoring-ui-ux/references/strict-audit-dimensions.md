# STRICT Audit Dimensions

Jedes Finding: Evidenzklasse `Confirmed` | `Hypothesis` | `Unknown` + Datei/Modul + P0–P3 + geplante Maßnahme.

## A. Codequalität

- [ ] Duplizierte Implementierungen
- [ ] Unnötige Klassen/Methoden/Variablen
- [ ] Ungenutzte Imports/Ressourcen/Abhängigkeiten
- [ ] Inkonsistente/unverständliche Namen
- [ ] Überlange Methoden/Klassen
- [ ] Zu tiefe Verschachtelung
- [ ] Magic Numbers/Strings
- [ ] Fragwürdige Globals/Static State
- [ ] Veraltete/überkomplizierte Patterns
- [ ] SOLID/DRY/KISS bzw. sprachübliche Best-Practice-Verletzungen

## B. Performance & Ressourcen

- [ ] Unnötige Allokationen / mögliche Leaks
- [ ] Ineffiziente Loops/Algorithmen / unnötige Kopien
- [ ] Redundante Network/File/DB-Ops
- [ ] Blocking auf UI/Main-Thread
- [ ] Überflüssige Renders/Updates
- [ ] Schlechte Async-Verarbeitung / Init-Kosten
- [ ] Zu große Assets/Libs / Ladezeiten
- [ ] Caching / Skalierbarkeit

## C. Funktionalität & Zuverlässigkeit

- [ ] Logikfehler / unvollständige Bedingungen
- [ ] Edge Cases / unbehandelte Exceptions
- [ ] Race Conditions / State-Fehler
- [ ] Validierung / Resource Cleanup
- [ ] Inkonsistente Daten / Retries / Abbruch
- [ ] Timeouts / potenzieller Datenverlust

## D. Security

- [ ] Unsichere Input-Verarbeitung
- [ ] Fehlende Berechtigungsprüfungen
- [ ] Unsichere Speicherung sensibler Daten
- [ ] Secrets/PII in Logs
- [ ] Unsichere Datei-/Pfadverarbeitung
- [ ] Veraltete Dependencies mit bekannten CVEs
- [ ] Unzureichende Fehlerisolierung
- [ ] Plattform-/Framework-spezifische Issues

## Priorität

| Prio | Bedeutung |
|------|-----------|
| P0 | Security, Datenverlust, Absturz, Broken Build |
| P1 | Schwere Funktions-/Perf-/UX-Mängel |
| P2 | Wartbarkeit, Komplexität, Konsistenz |
| P3 | Kosmetik / optional |
