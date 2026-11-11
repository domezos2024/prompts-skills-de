---
name: architekt-fuer-verschluesselung-und-schluesselverwaltung
description: Use when reviewing or improving application encryption, authenticated encryption (e.g. AES-GCM), key derivation, key storage/rotation, nonce handling, or encrypted-data migration - runs a strict multi-phase crypto inventory, threat-backed design, defensive implementation, and recovery-tested validation workflow.
---

# Architekt für Verschlüsselung & Schlüsselverwaltung

## Overview

Prüft und verbessert Verschlüsselung und Schlüsselverwaltung. Kernprinzip: **Ist-Krypto inventarisieren → Garantien/Threats festlegen → etablierte Primitive korrekt einsetzen → Rotation/Migration mit Recovery testen.** Keine Eigenbau-Algorithmen; bestehende Ciphertexte nicht unkontrolliert zerstören.

## When to Use

- Daten at-rest/in-transit kryptografisch absichern oder refactorn
- Key Storage, Rotation, KDF, Nonce/IV, AEAD prüfen
- Migration versionierter verschlüsselter Payloads

## When NOT to Use

- Allgemeine AppSec ohne Krypto-Fokus → `vollstaendige-sicherheitshaertung`
- Nur TLS/Infra-Zertifikate → `waechter-der-infrastruktursicherheit`
- Homegrown-Cipher „zum Spaß“ erfinden

## Critical Guidelines

- MUST bestehende Algorithmen, Schlüsselorte, Datenwege und Versionierung erfassen.
- MUST Threat Model und Sicherheitsgarantien (Vertraulichkeit, Integrität, Authentizität) definieren.
- MUST nur etablierte Primitive (z. B. AES-256-GCM, XChaCha20-Poly1305, HKDF/Argon2 wo passend) korrekt verwenden.
- MUST Nonce-/IV-Uniqueness, Associated Data und Key Separation absichern.
- MUST Rotation und Migration mit Rollback/Recovery planen und testen.
- NEVER selbst erfundene Algorithmen oder „AES-ECB weil einfach“.
- NEVER Keys in Repo, Logs, Tickets oder Client-Bundles hardcoden.
- NEVER Bestandsdaten entschlüsselbar machen ohne Migrations-/Backup-Strategie.
- NEVER Exploit-PoCs als Angriffsanleitung; nur defensive Tests (Tamper → fail, wrong key → fail).
- ALWAYS Iron Laws und Phasenstatus.

## Workflow

### PHASE 0 – Checkpoint

```bash
python skills/_shared/scripts/checkpoint.py init --skill architekt-fuer-verschluesselung-und-schluesselverwaltung --root .skill-runs/crypto-keys
```

### PHASE 1 – DISCOVERY

1. Cipher, Modi, KDFs, Key-IDs, Speicherorte (KMS/HSM/env/file) inventarisieren.
2. Klartext-Pfade, Backup-/Log-Leaks, Client-seitige Key-Nutzung suchen.
3. Checkliste `references/crypto-key-checklist.md` abarbeiten.

**Gate:** Crypto-Inventar + bekannte Anti-Patterns gelistet.

### PHASE 2 – DESIGN

1. Bedrohungsmodell: Key compromise, ciphertext tampering, nonce reuse, rollback attacks.
2. Target-Design: AEAD, Key hierarchy, wrapping, versionierte Envelope-Struktur.
3. Rotations- und Migrationsplan inkl. Dual-Read/ Dual-Write wo nötig.
4. Testmatrix: decrypt ok, tamper fail, wrong key fail, key loss recovery drill (lab).

**Gate:** Spec mit Garantien, Key-Lifecycle und Migrationsschritten.

### PHASE 3 – IMPLEMENTATION

1. Library-APIs korrekt verdrahten; Parameter (Nonce, Tag, AAD) zentralisieren.
2. Key-Loading nur aus Secret Store/KMS; Trennung von Enc-/Mac-/Signing-Keys.
3. Envelope-Versionierung und Key-ID im Ciphertext-Metadatenfeld.
4. Nach jedem Paket: Unit-Tests für Roundtrip und Negative Cases.

**Gate:** Keine bekannten Nonce-/Key-Anti-Patterns offen; Migration dry-run dokumentiert.

### PHASE 4 – VALIDATION

1. Roundtrip, Tamper-Detection, Key-Rotation-Probe in Lab/Stage.
2. Recovery-Drill: Restore alter Key-Version / Backup-Decrypt.
3. Performance-Smoke nur soweit nötig; keine Prod-Lastzerstörung.
4. Results gegen Checkliste.

**Gate:** Validierungsprotokoll; kein Datenverlust-Risiko unadressiert.

### PHASE 5 – DELIVERY

1. Technische Spec, Tests, Rotations-/Rollback-Runbook.
2. Delivery Report; Checkpoint `done`.

```bash
python skills/_shared/scripts/checkpoint.py set --root .skill-runs/crypto-keys --phase 5 --step "delivery complete" --status done
```

## Quick Reference

| Aufgabe | Aktion |
|---------|--------|
| Inventar | Algo, Keys, Paths, Versions |
| Design | AEAD + Key hierarchy + Rotation |
| Test | Roundtrip / Tamper / Wrong key |
| Stop | Eigenbau-Crypto / Blind-Migration |

## Red Flags

- ECB, statische IVs, Key im Git
- „Wir rotieren später“
- Migration ohne Backup-Decrypt-Probe
- Custom Hash-Chains statt AEAD
- Fertig ohne PHASE 4

## Resources

- `references/crypto-key-checklist.md`
- `scripts/scaffold_crypto_inventory.py`
- `../_shared/references/iron-laws.md`
- `../_shared/references/phase-protocol.md`
- `../_shared/references/delivery-report-template.md`
- `../_shared/scripts/checkpoint.py`
