# PWA Readiness Checklist

Jedes Item: `Pass` | `Fail` | `N/A` + Beweis.

## Voraussetzungen

- [ ] HTTPS / sicherer Kontext in Zielumgebung
- [ ] App-Shell und kritische Assets identifiziert
- [ ] Offline-Scope bewusst begrenzt
- [ ] No-cache Liste für sensible/API/Auth-Routen

## Manifest & Icons

- [ ] `name` / `short_name` / `start_url` / `display`
- [ ] Icons in benötigten Größen
- [ ] Theme/Background color gesetzt oder begründet weggelassen
- [ ] Manifest verlinkt und erreichbar

## Service Worker

- [ ] Registrierung nur wo unterstützt
- [ ] Cache-Versionierung vorhanden
- [ ] Strategie je Ressourcentyp dokumentiert
- [ ] Invalidierung / Update getestet
- [ ] Offline-Fallback definiert

## UX & Privacy

- [ ] Install-Prompt nicht aufdringlich
- [ ] Update-Hinweis verständlich
- [ ] Notifications nur nach Opt-in (falls genutzt)
- [ ] Keine unkontrollierte Speicherung sensibler Daten

## Testmatrix

| Browser | Install | Offline | Update | Notes |
|---------|---------|---------|--------|-------|
| | | | | |
