<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dc8f035ce92e4eaa078ab19caa68267a",
  "translation_date": "2025-08-26T21:07:16+00:00",
  "source_file": "2-Working-With-Data/07-python/assignment.md",
  "language_code": "sv"
}
-->
# Uppgift för Databehandling i Python

I denna uppgift kommer vi att be dig utveckla vidare på den kod vi har börjat skapa i våra utmaningar. Uppgiften består av två delar:

## Modellering av COVID-19 spridning

 - [ ] Rita *R* grafer för 5-6 olika länder på en graf för jämförelse, eller använd flera grafer sida vid sida.
 - [ ] Undersök hur antalet dödsfall och tillfrisknade korrelerar med antalet smittade fall.
 - [ ] Ta reda på hur länge en typisk sjukdom varar genom att visuellt korrelera infektionshastighet och dödsfallshastighet och leta efter vissa avvikelser. Du kan behöva titta på olika länder för att ta reda på detta.
 - [ ] Beräkna dödlighetsgraden och hur den förändras över tid. *Du kanske vill ta hänsyn till sjukdomens längd i dagar för att förskjuta en tidsserie innan du gör beräkningar.*

## Analys av COVID-19 artiklar

- [ ] Bygg en samförekomstmatris för olika mediciner och se vilka mediciner som ofta förekommer tillsammans (dvs. nämns i samma abstrakt). Du kan modifiera koden för att bygga en samförekomstmatris för mediciner och diagnoser.
- [ ] Visualisera denna matris med hjälp av en värmekarta.
- [ ] Som ett extra mål, visualisera samförekomsten av mediciner med hjälp av [chord diagram](https://en.wikipedia.org/wiki/Chord_diagram). [Detta bibliotek](https://pypi.org/project/chord/) kan hjälpa dig att rita ett chord diagram.
- [ ] Som ett annat extra mål, extrahera doseringar av olika mediciner (såsom **400mg** i *ta 400mg klorokin dagligen*) med hjälp av reguljära uttryck, och bygg en dataframe som visar olika doseringar för olika mediciner. **Obs**: överväg numeriska värden som är i nära textuell närhet till medicinens namn.

## Bedömningskriterier

Utmärkt | Tillräckligt | Behöver förbättras
--- | --- | -- |
Alla uppgifter är slutförda, grafiskt illustrerade och förklarade, inklusive minst ett av två extra mål | Mer än 5 uppgifter är slutförda, inga extra mål är försökte, eller resultaten är inte tydliga | Mindre än 5 (men mer än 3) uppgifter är slutförda, visualiseringar hjälper inte att demonstrera poängen

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.