# File & Document Automation Checklist

Jedes Item: `Pass` | `Fail` | `N/A` + Beweis.

## Discovery & Rules

- [ ] Quell-/Zielstrukturen dokumentiert
- [ ] Dateitypen und Konventionen definiert
- [ ] Klassifizierungsregeln testbar formuliert
- [ ] Naming-Template und Kollisionsstrategie festgelegt

## Pipeline Safety

- [ ] Dry-Run-Modus vorhanden und Default vor erstem Apply
- [ ] Manifest/Audit je Lauf (src, dest, hash, action)
- [ ] Kein silent overwrite; Konflikt → suffix/quarantine
- [ ] Kein Delete ohne explizite Policy + Recovery
- [ ] Convert: Original erhalten (copy-then-convert)

## Validation

- [ ] Corrupt/unreadable Detection
- [ ] Duplikat-Erkennung (Hash/Größe+Name-Policy)
- [ ] Unvollständige Downloads/temp files ausgeschlossen
- [ ] Rechte/Pfad-Traversal-Schutz

## Edge Cases

- [ ] Unicode/Sonderzeichen
- [ ] Sehr große Dateien
- [ ] Lange Pfade (OS-Limits)
- [ ] Abbruch mitten im Lauf + sichere Fortsetzung
- [ ] Parallel-Lauf / Doppelstart verhindert oder idempotent

## Recovery

- [ ] Undo/Restore aus Manifest dokumentiert und getestet
- [ ] Quarantäne reviewbar
