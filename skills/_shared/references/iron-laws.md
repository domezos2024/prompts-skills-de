# Iron Laws – Verbindliche Regeln für alle Workflow-Skills

Diese Regeln gelten für jeden Skill in diesem Repository. Verstöße sind Failures, keine Stilfragen.

## Absolute Verbote

1. **Keine erfundenen Ergebnisse.** Behaupte niemals bestandene Tests, erfolgreiche Builds, Screenshots, Metriken oder Tool-Ausgaben ohne tatsächliche Ausführung.
2. **Keine destruktiven Git-Aktionen** ohne ausdrückliche Nutzerfreigabe (force-push, hard reset, clean -fdx, amend gepushter Commits).
3. **Keine Secrets anfassen.** Keine Credentials ändern, committen, loggen oder in Tickets/Chats posten.
4. **Kein Push/Deploy/Release** ohne explizite Anweisung.
5. **Keine parallel fremden Änderungen überschreiben.** Unrelated dirty worktree erhalten.
6. **Keine destruktiven Produktionstests** ohne Autorisierung.
7. **Keine Breaking Changes** ohne dokumentierte Begründung und Migrationspfad.

## Pflichtverhalten

1. **Phasenstatus anzeigen:** Immer `PHASE N – Kurzname` und aktuellen Arbeitsschritt nennen.
2. **Atomare Schritte:** Eine logische Änderungseinheit pro Paket; nach jedem Paket validieren.
3. **Messbarer Ausgangszustand:** Vor Änderungen Build/Tests/Metriken erfassen, soweit möglich.
4. **Priorisierung:** P0 → P1 → P2 → P3. P0/P1 vor Kosmetik.
5. **Regression nach jedem Paket:** Mindestens relevante Tests/Smoke; bei Fehler sofort fixen oder revertieren.
6. **Abschlusskriterium:** Workflow gilt erst als fertig, wenn implementiert **und** validiert – oder Blocker mit konkretem nächsten Schritt dokumentiert sind.
7. **Progressive Disclosure:** Schwere Referenzen und Scripts erst laden/ausführen, wenn die Phase sie braucht.

## Prioritäten

| Prio | Bedeutung | Beispiele |
|------|-----------|-----------|
| P0 | Kritisch | Sicherheit, Datenverlust, Absturz, Broken Build |
| P1 | Hoch | Schwere Funktionsfehler, große Perf-/UX-Lücken |
| P2 | Mittel | Wartbarkeit, Duplikate, Konsistenz |
| P3 | Niedrig | Kosmetik, optionale Nice-to-haves |

## Rationalisierungs-Tabelle (Anti-Ausreden)

| Ausrede | Realität |
|---------|----------|
| „Nur Analyse reicht“ | Skills verlangen Umsetzung + Validierung |
| „Tests später“ | Kein Paket ohne passende Prüfung abschließen |
| „Zu einfach zum Prüfen“ | Smoke/Build ist Minimum |
| „Zeitdruck → shortcut“ | Qualität vor Schein-Fortschritt |
| „Ich hab’s manuell gesehen“ | Reproduzierbarer Nachweis nötig |
| „Spirit statt Ritual“ | Phasen und Checkpoints sind das Ritual |

## Red Flags – STOP

- Ergebnis behauptet ohne Tool-/Testlauf
- Großes Refactor ohne Ausgangsmetrik
- UI „verbessert“ ohne Vorher/Nachher-Beweis
- Security-Fix ohne Regressionstest
- „Fertig“ obwohl Validierungsphase fehlt
