# Agent & Skill Authoring Checklist

Jedes Item: `Pass` | `Fail` | `N/A` + Beweis.

## Discovery

- [ ] Tatsächlich genutzte KI-Tools erfasst
- [ ] Vorhandene Rules/Skills inventarisiert
- [ ] Backup/Diff-Strategie vor Änderungen

## Central rules

- [ ] Eine zentrale Regelquelle
- [ ] Imperativ, kurz, ohne Duplikate
- [ ] Keine Secrets

## Skills / Agents

- [ ] Jeder Skill: kebab-name, EN description „Use when…“
- [ ] Trigger, Inputs, Erfolgskriterien klar
- [ ] Multi-phase Workflow mit Gates
- [ ] Keine dekorativen Rollen ohne Taskfit
- [ ] Shared refs (_shared) wo sinnvoll

## Validation

- [ ] Frontmatter/Struktur ok
- [ ] Relative Links auflösbar
- [ ] Sample task geprüft
- [ ] Kein unbeabsichtigtes Überschreiben
