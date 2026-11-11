# Skills – Strikte Multi-Workflow-Agenten

52 Agent Skills, abgeleitet aus den Prompts in `prompts/` plus Master- und STRICT-Prompt. Jeder Skill ist ein eigenständiger, phasenbasierter Workflow mit Gates, Checklisten und Helper-Scripts.

## Struktur

```
skills/
  _shared/                 # Iron Laws, Phase Protocol, Checkpoint, Validator
  <skill-name>/
    SKILL.md               # Hauptdatei (Frontmatter + Workflow)
    references/            # Domänen-Checklisten / Matrizen
    scripts/               # Deterministische Helper
```

## Verwendung

1. Passenden Skill-Ordner öffnen und `SKILL.md` laden (bzw. als Agent-Skill installieren).
2. Shared-Regeln beachten: `_shared/references/iron-laws.md`.
3. Checkpoint initialisieren:

```bash
python skills/_shared/scripts/checkpoint.py init --skill <skill-name> --root .skill-runs/<kurz>
```

4. Phasen 1→5 (bzw. skill-spezifisch) mit Gates durchlaufen; Delivery Report am Ende.

Validierung der Skill-Struktur:

```bash
python skills/_shared/scripts/validate_skill_structure.py
```

## Katalog

### Shared

| Ressource | Zweck |
|-----------|--------|
| `_shared/references/iron-laws.md` | Absolute Verbote & Pflichten |
| `_shared/references/phase-protocol.md` | Universelles 5-Phasen-Modell |
| `_shared/references/delivery-report-template.md` | Abschlussbericht |
| `_shared/scripts/checkpoint.py` | Phasen-Checkpoint JSON |
| `_shared/scripts/validate_skill_structure.py` | Struktur-Validator |

### 1. UI/UX & Grafikdesign

| Skill | Quelle |
|-------|--------|
| [vollstaendige-ui-ux-transformation](vollstaendige-ui-ux-transformation/) | `prompts/01-01-…` |
| [automatischer-designsystem-architekt](automatischer-designsystem-architekt/) | `prompts/01-02-…` |
| [mobile-first-erlebnisoptimierer](mobile-first-erlebnisoptimierer/) | `prompts/01-03-…` |
| [visuelle-asset-fabrik](visuelle-asset-fabrik/) | `prompts/01-04-…` |
| [conversion-orientiertes-oberflaechen-redesign](conversion-orientiertes-oberflaechen-redesign/) | `prompts/01-05-…` |

### 2. Codequalität & Refactoring

| Skill | Quelle |
|-------|--------|
| [autonome-codebereinigung-und-refaktorierung](autonome-codebereinigung-und-refaktorierung/) | `prompts/02-01-…` |
| [modernisierung-der-softwarearchitektur](modernisierung-der-softwarearchitektur/) | `prompts/02-02-…` |
| [performance-profiling-und-optimierung](performance-profiling-und-optimierung/) | `prompts/02-03-…` |
| [beseitigung-von-abhaengigkeiten-und-technischen-schulden](beseitigung-von-abhaengigkeiten-und-technischen-schulden/) | `prompts/02-04-…` |
| [rettungsmission-fuer-altcode](rettungsmission-fuer-altcode/) | `prompts/02-05-…` |

### 3. Cybersecurity & Datenschutz

| Skill | Quelle |
|-------|--------|
| [vollstaendige-sicherheitshaertung](vollstaendige-sicherheitshaertung/) | `prompts/03-01-…` |
| [datenschutz-durch-technikgestaltung-und-dsgvo-audit](datenschutz-durch-technikgestaltung-und-dsgvo-audit/) | `prompts/03-02-…` |
| [architekt-fuer-verschluesselung-und-schluesselverwaltung](architekt-fuer-verschluesselung-und-schluesselverwaltung/) | `prompts/03-03-…` |
| [audit-von-authentifizierung-und-berechtigungen](audit-von-authentifizierung-und-berechtigungen/) | `prompts/03-04-…` |
| [waechter-der-infrastruktursicherheit](waechter-der-infrastruktursicherheit/) | `prompts/03-05-…` |

### 4. Softwaretests & Qualitätssicherung

| Skill | Quelle |
|-------|--------|
| [autonomer-qa-testingenieur](autonomer-qa-testingenieur/) | `prompts/04-01-…` |
| [ende-zu-ende-nutzerreise-simulator](ende-zu-ende-nutzerreise-simulator/) | `prompts/04-02-…` |
| [waechter-fuer-regression-und-kompatibilitaet](waechter-fuer-regression-und-kompatibilitaet/) | `prompts/04-03-…` |
| [ursachenermittler-fuer-abstuerze-und-ausnahmen](ursachenermittler-fuer-abstuerze-und-ausnahmen/) | `prompts/04-04-…` |
| [labor-fuer-zuverlaessigkeit-und-fehlerwiederherstellung](labor-fuer-zuverlaessigkeit-und-fehlerwiederherstellung/) | `prompts/04-05-…` |

### 5. DevOps & Release Engineering

| Skill | Quelle |
|-------|--------|
| [vollstaendige-release-pipeline](vollstaendige-release-pipeline/) | `prompts/05-01-…` |
| [ci-cd-pipeline-architekt](ci-cd-pipeline-architekt/) | `prompts/05-02-…` |
| [docker-und-container-optimierung](docker-und-container-optimierung/) | `prompts/05-03-…` |
| [serverbereitstellung-und-reverse-proxy-orchestrierung](serverbereitstellung-und-reverse-proxy-orchestrierung/) | `prompts/05-04-…` |
| [backup-notfallwiederherstellung-und-rollback](backup-notfallwiederherstellung-und-rollback/) | `prompts/05-05-…` |

### 6. Webentwicklung & Optimierung

| Skill | Quelle |
|-------|--------|
| [vollstaendige-website-optimierung](vollstaendige-website-optimierung/) | `prompts/06-01-…` |
| [ingenieur-fuer-seo-und-inhaltsarchitektur](ingenieur-fuer-seo-und-inhaltsarchitektur/) | `prompts/06-02-…` |
| [ingenieur-fuer-web-barrierefreiheit-und-konformitaet](ingenieur-fuer-web-barrierefreiheit-und-konformitaet/) | `prompts/06-03-…` |
| [adsense-und-monetarisierungs-integration](adsense-und-monetarisierungs-integration/) | `prompts/06-04-…` |
| [umwandlung-in-eine-progressive-web-app](umwandlung-in-eine-progressive-web-app/) | `prompts/06-05-…` |

### 7. KI-Agenten & MCP-Systeme

| Skill | Quelle |
|-------|--------|
| [erweiterung-der-mcp-server-faehigkeiten](erweiterung-der-mcp-server-faehigkeiten/) | `prompts/07-01-…` |
| [architekt-fuer-autonome-agenten-workflows](architekt-fuer-autonome-agenten-workflows/) | `prompts/07-02-…` |
| [ingenieur-fuer-multi-agenten-zusammenarbeit](ingenieur-fuer-multi-agenten-zusammenarbeit/) | `prompts/07-03-…` |
| [intelligentes-modell-routing-und-failover](intelligentes-modell-routing-und-failover/) | `prompts/07-04-…` |
| [mcp-werkzeug-intelligenz-und-optimierung](mcp-werkzeug-intelligenz-und-optimierung/) | `prompts/07-05-…` |

### 8. Automatisierung & API-Integration

| Skill | Quelle |
|-------|--------|
| [ingenieur-fuer-rest-api-integration](ingenieur-fuer-rest-api-integration/) | `prompts/08-01-…` |
| [systemuebergreifende-workflow-automatisierung](systemuebergreifende-workflow-automatisierung/) | `prompts/08-02-…` |
| [architekt-fuer-datenpipelines-und-etl](architekt-fuer-datenpipelines-und-etl/) | `prompts/08-03-…` |
| [intelligentes-benachrichtigungs-und-ereignisverarbeitungssystem](intelligentes-benachrichtigungs-und-ereignisverarbeitungssystem/) | `prompts/08-04-…` |
| [intelligente-datei-und-dokumentenautomatisierung](intelligente-datei-und-dokumentenautomatisierung/) | `prompts/08-05-…` |

### 9. Produktentwicklung & Wachstum

| Skill | Quelle |
|-------|--------|
| [produktchancen-und-funktionsentdeckung](produktchancen-und-funktionsentdeckung/) | `prompts/09-01-…` |
| [app-store-release-und-listing-optimierung](app-store-release-und-listing-optimierung/) | `prompts/09-02-…` |
| [designer-fuer-produkt-onboarding-und-nutzerbindung](designer-fuer-produkt-onboarding-und-nutzerbindung/) | `prompts/09-03-…` |
| [faire-monetarisierung-und-spendenerlebnis](faire-monetarisierung-und-spendenerlebnis/) | `prompts/09-04-…` |
| [wettbewerbs-benchmark-und-produktverbesserung](wettbewerbs-benchmark-und-produktverbesserung/) | `prompts/09-05-…` |

### 10. Dokumentation & Wissensmanagement

| Skill | Quelle |
|-------|--------|
| [generator-fuer-vollstaendige-technische-dokumentation](generator-fuer-vollstaendige-technische-dokumentation/) | `prompts/10-01-…` |
| [architekt-fuer-repository-wissensdatenbanken](architekt-fuer-repository-wissensdatenbanken/) | `prompts/10-02-…` |
| [generator-fuer-ki-agenten-anweisungen-und-skills](generator-fuer-ki-agenten-anweisungen-und-skills/) | `prompts/10-03-…` |
| [changelog-und-release-dokumentation](changelog-und-release-dokumentation/) | `prompts/10-04-…` |
| [projektaudit-und-umsetzbare-roadmap](projektaudit-und-umsetzbare-roadmap/) | `prompts/10-05-…` |

### Orchestrierung & STRICT

| Skill | Quelle |
|-------|--------|
| [universeller-multi-workflow-master](universeller-multi-workflow-master/) | `master-prompt.md` |
| [strict-code-quality-refactoring-ui-ux](strict-code-quality-refactoring-ui-ux/) | `prompts/STRICT-…` |
