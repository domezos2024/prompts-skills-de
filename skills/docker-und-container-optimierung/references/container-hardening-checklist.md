# Container Hardening Checklist

Jedes Item: `Pass` | `Fail` | `N/A` + Beweis.

## Image & Build

- [ ] Multi-Stage wo sinnvoll
- [ ] Schlanke/ gepinnte Base Images
- [ ] `.dockerignore` vorhanden und wirksam
- [ ] Keine Secrets in Layers/ENV/ARG persistiert
- [ ] Image-Tags nachvollziehbar (kein blindes `latest` in Prod-Docs)

## Runtime Security

- [ ] Non-root User wo möglich
- [ ] Read-only Root-FS erwogen/begründet
- [ ] Capabilities/Privileges minimiert
- [ ] Nur benötigte Ports exponiert
- [ ] Secrets via Runtime-Mechanismus, nicht Image

## Ops & Persistenz

- [ ] Healthcheck definiert und getestet
- [ ] Restart-Policy gesetzt
- [ ] Networks begrenzt
- [ ] Volumes benannt und dokumentiert
- [ ] Kein destruktives Prune geplant

## Messung

| Metrik | Vorher | Nachher | Methode |
|--------|--------|---------|---------|
| Imagegröße | | | |
| Cold start | | | |
| Memory (Smoke) | | | |
