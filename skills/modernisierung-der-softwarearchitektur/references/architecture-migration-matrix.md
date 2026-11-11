# Architektur-Migrationsmatrix

Jedes Item: `Pass` | `Fail` | `N/A` + Beweis. Übertrifft Prompt: Optionenvergleich, Kopplungsnachweis, Inkrement-/Rollback-Gates.

## A. Ist-Landschaft

| Modul / Bounded Context | Verantwortung | Eingehende Deps | Ausgehende Deps | Datenhaltung | Einstiege |
|-------------------------|---------------|-----------------|-----------------|--------------|-----------|
| | | | | | |

## B. Problem-Belege

| ID | Problem (Kopplung/Zyklus/God-Module/leaky abstraction/…) | Evidence (Pfad/Tool) | Impact | Prio |
|----|------------------------------------------------------------|----------------------|--------|------|
| | | | | P0–P3 |

- [ ] Zyklische Referenzen identifiziert oder bewusst N/A
- [ ] Fehlende Verantwortlichkeitstrennung belegt
- [ ] Schnittstellen/Verträge katalogisiert

## C. Optionsvergleich (mind. 2 realistische Optionen)

| Option | Passt zu Bedarf? | Nutzen | Kosten/Komplexität | Risiko | Entscheidung |
|--------|------------------|--------|--------------------|--------|--------------|
| Beibehalten + lokale Grenzen schärfen | | | | | |
| Modulare Schichten / Packages | | | | | |
| Ports & Adapters / Hexagonal (teilweise) | | | | | |
| Andere (spezifizieren) | | | | | |

- [ ] Hype-Optionen ohne Nutzen explizit verworfen (Begründung)

## D. Inkrementplan

| Schritt | Änderung | Betroffene Module | Tests | Rollback | Done-Kriterium |
|---------|----------|-------------------|-------|----------|----------------|
| S1 | | | | | |
| S2 | | | | | |

## E. Implementierungs-Gates

- [ ] Interfaces/DI-Grenzen klar und testbar
- [ ] Keine neuen Zyklen eingeführt
- [ ] Doppelte Pfade terminiert oder mit Ablaufdatum dokumentiert
- [ ] Technische Doku/ADR aktualisiert

## F. Validation

- [ ] Build grün
- [ ] Integrationstests / kritische E2E-Stichprobe
- [ ] Kompatibilität externer Clients geprüft oder N/A
- [ ] Performance-Stichprobe ohne offensichtliche Regression
- [ ] Soll-Diagramm entspricht Code
