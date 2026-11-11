# Crypto & Key Management Checklist

Jedes Item: `Pass` | `Fail` | `N/A` + Evidence. Defensive Prüfung – keine Angriffsanleitungen.

## Inventar

- [ ] Algorithmen/Modi/KDFs dokumentiert
- [ ] Key-IDs und Speicherorte erfasst
- [ ] Ciphertext-Versionierung vorhanden oder geplant
- [ ] Klartext-Zwischenpfade bekannt

## Primitive & Nutzung

- [ ] Authentifizierte Verschlüsselung (AEAD) wo Vertraulichkeit+Integrität nötig
- [ ] Kein ECB für vertrauliche Daten
- [ ] Nonce/IV: eindeutig pro Key; Generierung zentral
- [ ] AAD gebunden an Kontext (Tenant/User/Object-ID) wo sinnvoll
- [ ] KDF-Parameter zeitgemäß (kein unsicheres MD5/SHA1-Password-Hashing)

## Schlüsselverwaltung

- [ ] Keys nicht im Repo / Client-Bundle
- [ ] Trennung Enc vs. Sign vs. MAC Keys
- [ ] Zugriff Least Privilege auf Key Material
- [ ] Rotation geplant (Zeit/Event)
- [ ] Wrapping / KMS/HSM wo verfügbar genutzt

## Migration & Recovery

- [ ] Backup vor Massen-Reencrypt
- [ ] Dual-read oder Version-Marker
- [ ] Rollback-Pfad dokumentiert
- [ ] Lab-Probe: Decrypt mit alter Key-Version
- [ ] Key-Loss-Szenario: akzeptiertes Risiko oder Recovery-Runbook

## Testmatrix

| Case | Expected | Result | Evidence |
|------|----------|--------|----------|
| Encrypt→Decrypt roundtrip | Success | | |
| Tampered ciphertext | Fail closed | | |
| Wrong key / wrong key-id | Fail closed | | |
| Nonce reuse guard (if enforceable) | Detect/prevent | | |
| Rotation dual-read | Old+new readable | | |

## Anti-Rationalisierung

| Ausrede | Realität |
|---------|----------|
| „AES reicht, Modus egal“ | Modus/AEAD entscheidet Sicherheit |
| „IV fixed is fine for demos“ | Auch in Dev keine schlechten Patterns committen |
| „Rotation bricht Prod“ | Dual-read + Lab zuerst |
| „Eigenes XOR ist simpler“ | Verboten |
