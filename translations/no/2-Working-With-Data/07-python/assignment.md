<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dc8f035ce92e4eaa078ab19caa68267a",
  "translation_date": "2025-08-26T21:07:37+00:00",
  "source_file": "2-Working-With-Data/07-python/assignment.md",
  "language_code": "no"
}
-->
# Oppgave for Databehandling i Python

I denne oppgaven vil vi be deg utdype koden vi har begynt å utvikle i våre utfordringer. Oppgaven består av to deler:

## Modellering av COVID-19 spredning

 - [ ] Plot *R* grafer for 5-6 forskjellige land på én graf for sammenligning, eller ved å bruke flere grafer side om side.
 - [ ] Se hvordan antall dødsfall og antall friskmeldte korrelerer med antall smittede tilfeller.
 - [ ] Finn ut hvor lenge en typisk sykdom varer ved å visuelt korrelere smitterate og dødsrate og se etter noen avvik. Du må kanskje se på forskjellige land for å finne dette ut.
 - [ ] Beregn dødelighetsraten og hvordan den endrer seg over tid. *Du kan vurdere å ta hensyn til sykdommens varighet i dager for å forskyve én tidsserie før du gjør beregningene.*

## Analyse av COVID-19 artikler

- [ ] Bygg en samforekomstmatrise for forskjellige medisiner, og se hvilke medisiner som ofte forekommer sammen (dvs. nevnt i samme sammendrag). Du kan modifisere koden for å bygge samforekomstmatrise for medisiner og diagnoser.
- [ ] Visualiser denne matrisen ved hjelp av et varmekart.
- [ ] Som et ekstra mål, visualiser samforekomsten av medisiner ved hjelp av [chord diagram](https://en.wikipedia.org/wiki/Chord_diagram). [Dette biblioteket](https://pypi.org/project/chord/) kan hjelpe deg med å tegne et chord diagram.
- [ ] Som et annet ekstra mål, trekk ut doseringer av forskjellige medisiner (slik som **400mg** i *ta 400mg klorokin daglig*) ved hjelp av regulære uttrykk, og bygg en dataframe som viser forskjellige doseringer for forskjellige medisiner. **Merk**: vurder numeriske verdier som er i nær tekstlig tilknytning til medisinens navn.

## Vurderingskriterier

Eksemplarisk | Tilfredsstillende | Trenger forbedring
--- | --- | -- |
Alle oppgaver er fullført, grafisk illustrert og forklart, inkludert minst ett av to ekstra mål | Mer enn 5 oppgaver er fullført, ingen ekstra mål er forsøkt, eller resultatene er ikke klare | Mindre enn 5 (men mer enn 3) oppgaver er fullført, visualiseringene hjelper ikke med å demonstrere poenget

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.