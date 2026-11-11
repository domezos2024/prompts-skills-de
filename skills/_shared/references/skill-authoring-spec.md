# Skill Authoring Spec (dieses Repo)

## Pflichtstruktur jedes Skills

```
skills/<skill-name>/
  SKILL.md                 # required
  references/              # domain checklists, schemas (load on demand)
  scripts/                 # deterministic helpers (optional but preferred)
  assets/                  # templates for output (optional)
```

## SKILL.md Pflichtabschnitte

1. YAML frontmatter: nur `name`, `description`
2. `# Title`
3. `## Overview` – Kernprinzip in 2–4 Sätzen
4. `## When to Use` / `## When NOT to Use`
5. `## Critical Guidelines` – MUST/NEVER Regeln (imperativ)
6. `## Workflow` – nummerierte Multi-Phasen mit Unteraufgaben, Gates, Outputs
7. `## Quick Reference` – Tabelle
8. `## Red Flags`
9. `## Resources` – relative Pfade zu scripts/references + `_shared`

## Qualitätsanforderungen

- Sprache: Deutsch (wie Quellprompts), `description` auf Englisch mit "Use when..." (CSO)
- `name`: kebab-case, identisch mit Ordnername, nur a-z0-9-
- Strikt multi-task: Discovery → Plan → Implement → Validate → Deliver (domänenspezifisch erweitern)
- Weiter denken als Prompt: Checklisten, Anti-Rationalisierung, messbare Gates, Helper-Scripts
- Imperativ/Infinitiv, nicht "Du solltest"
- Keine erfundenen Tool-Erfolge in Beispielen ohne klaren Pseudo-Charakter
- SKILL.md ausgiebig aber fokussiert (~400–900 Wörter Body ok für Workflow-Skills); Details in references/

## Helper-Erwartung

Jeder Skill braucht mindestens:
- 1× `references/*-checklist.md` oder `*-matrix.md` mit domänenspezifischen Prüfpunkten
- Idealerweise 1× `scripts/*.py` oder `*.ps1` für wiederholbare Checks/Scaffolding

Shared immer referenzieren:
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
