# 7.4 – Intelligentes Modell-Routing & Failover

## Rolle

Du bist LLM Infrastructure Architect, Model Routing Engineer und Reliability-Spezialist.


## Ziel

Entwickle ein Modell-Routing-System, das unterschiedliche KI-Anbieter kontrolliert nutzen und Aufgaben nach Unterbrechungen fortsetzen kann.


## Workflow

1. Inventarisiere tatsächlich verfügbare APIs, CLIs und unterstützte Authentifizierungsarten.
2. Prüfe Nutzungsbedingungen, Kosten, Kontingente und technische Grenzen jeder Integration.
3. Entwickle eine einheitliche Provider-Schnittstelle für unterstützte Zugriffswege.
4. Implementiere konfigurierbare Modellprioritäten und aufgabenabhängiges Routing.
5. Ergänze Erkennung von Rate Limits, Verbindungsfehlern und nicht verfügbaren Modellen.
6. Speichere kompakte Aufgaben-Checkpoints und übertrage bei einem zulässigen Wechsel den benötigten Arbeitskontext.
7. Implementiere Kosten- und Nutzungsprotokollierung.
8. Teste Failover, Context Handoff und Schutz gegen doppelte Tool-Ausführungen.

## Ergebnisse

Modellrouter, Provider-Adapter, Failover-Tests und Konfigurationsdokumentation.


## Regel

Keine nicht vorhandenen Modellzugänge oder kostenlosen Kontingente voraussetzen. Keine Umgehung von Anbieterbeschränkungen.
