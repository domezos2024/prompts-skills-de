# Knowledge Base Structure

Empfohlene Top-Level-Themen (anpassen, nicht aufblasen).

```
knowledge/
  INDEX.md                 # Navigation & Einstiege
  architecture-overview.md
  modules/
    <module>.md            # Zweck, APIs, Abhängigkeiten, Pfade
  data-flows.md            # Mermaid/Text + Dateiverweise
  decisions/
    ADR-XXXX.md
  boundaries-and-constraints.md
  project-rules.md         # AGENTS/CLAUDE Zusammenfassung + Links
  update-rules.md
  validation-log.md
```

## Pflicht je Modulseite

- [ ] Zweck in 2–4 Sätzen
- [ ] Einstiegspfad(e) mit Dateilinks
- [ ] Öffentliche Surfaces
- [ ] Abhängigkeiten inbound/outbound
- [ ] Bekannte Grenzen / Non-goals

## Validierung

- [ ] Mind. 5 Claims stichprobenartig am Code geprüft
- [ ] Keine toten relativen Links
- [ ] Update-Regeln vorhanden
