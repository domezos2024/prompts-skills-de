# Multi-Agent Orchestration Checklist

Jedes Item: `Pass` | `Fail` | `N/A` + Beweis.

## Rollen & Nutzen

- [ ] Jede Rolle hat klaren Scope und erlaubte Tools
- [ ] Nutzen vs. Einzelagent begründet (Qualität/Zeit/Kosten)
- [ ] Keine dekorativen Agenten ohne Arbeitspaket

## Handoff-Verträge

- [ ] Input-Schema und erforderliche Artefakte
- [ ] Output-Schema und Acceptance Criteria
- [ ] Owner, Reviewer, Deadline/Budget
- [ ] Fehler-/Reject-Protokoll

## Koordination

- [ ] Zentraler Status (queued/in_progress/in_review/done/blocked)
- [ ] Nur ein Writer pro Ressource zur Zeit oder Partition
- [ ] Konfliktfrüherkennung (Pfad-/Lock-Check)
- [ ] Eskalation bei Deadlock/Blocker

## Gates & Qualität

- [ ] Review vor Merge in shared branch/artefakt
- [ ] Tester-Gate vor Release-Agent
- [ ] Observability: Run-ID, Agent-ID, Handoff-ID

## Evaluation

- [ ] Gleiche Aufgabe Solo vs. Multi gemessen
- [ ] Qualitätskriterien vorab definiert
- [ ] Overhead (Tokens/Zeit/Koordination) erfasst
