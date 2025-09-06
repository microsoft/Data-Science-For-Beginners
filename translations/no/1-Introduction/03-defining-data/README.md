<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "12339119c0165da569a93ddba05f9339",
  "translation_date": "2025-09-05T22:29:39+00:00",
  "source_file": "1-Introduction/03-defining-data/README.md",
  "language_code": "no"
}
-->
# Definere Data

|![ Sketchnote av [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Definere Data - _Sketchnote av [@nitya](https://twitter.com/nitya)_ |

Data er fakta, informasjon, observasjoner og målinger som brukes til å gjøre oppdagelser og støtte informerte beslutninger. Et datapunkt er en enkelt enhet av data innenfor et datasett, som er en samling av datapunkter. Datasett kan komme i ulike formater og strukturer, og vil vanligvis være basert på kilden, eller hvor dataene kommer fra. For eksempel kan en bedrifts månedlige inntekter være i et regneark, mens timebaserte pulsdata fra en smartklokke kan være i [JSON](https://stackoverflow.com/a/383699)-format. Det er vanlig for dataforskere å jobbe med ulike typer data innenfor et datasett.

Denne leksjonen fokuserer på å identifisere og klassifisere data basert på deres egenskaper og kilder.

## [Quiz før forelesning](https://ff-quizzes.netlify.app/en/ds/quiz/4)

## Hvordan Data Beskrives

### Rådata
Rådata er data som kommer fra kilden i sin opprinnelige tilstand og som ikke har blitt analysert eller organisert. For å forstå hva som skjer med et datasett, må det organiseres i et format som kan forstås av mennesker så vel som av teknologien de bruker for videre analyse. Strukturen til et datasett beskriver hvordan det er organisert og kan klassifiseres som strukturert, ustrukturert og semi-strukturert. Disse strukturtypene vil variere avhengig av kilden, men vil til slutt passe inn i disse tre kategoriene.

### Kvantitative Data
Kvantitative data er numeriske observasjoner innenfor et datasett og kan vanligvis analyseres, måles og brukes matematisk. Noen eksempler på kvantitative data er: et lands befolkning, en persons høyde eller en bedrifts kvartalsvise inntekter. Med litt ekstra analyse kan kvantitative data brukes til å oppdage sesongtrender i luftkvalitetsindeksen (AQI) eller estimere sannsynligheten for rushtidstrafikk på en typisk arbeidsdag.

### Kvalitative Data
Kvalitative data, også kjent som kategoriske data, er data som ikke kan måles objektivt som observasjoner av kvantitative data. Det er generelt ulike formater av subjektive data som fanger kvaliteten på noe, som et produkt eller en prosess. Noen ganger er kvalitative data numeriske, men brukes vanligvis ikke matematisk, som telefonnumre eller tidsstempler. Noen eksempler på kvalitative data er: videokommentarer, merke og modell på en bil eller din nærmeste venns favorittfarge. Kvalitative data kan brukes til å forstå hvilke produkter forbrukere liker best eller identifisere populære nøkkelord i jobbsøknader.

### Strukturert Data
Strukturert data er data som er organisert i rader og kolonner, hvor hver rad har det samme settet med kolonner. Kolonner representerer en verdi av en bestemt type og identifiseres med et navn som beskriver hva verdien representerer, mens rader inneholder de faktiske verdiene. Kolonner vil ofte ha et spesifikt sett med regler eller begrensninger på verdiene for å sikre at verdiene nøyaktig representerer kolonnen. For eksempel, tenk deg et regneark med kunder der hver rad må ha et telefonnummer, og telefonnumrene aldri inneholder alfabetiske tegn. Det kan være regler som sikrer at telefonnummerkolonnen aldri er tom og kun inneholder tall.

En fordel med strukturert data er at det kan organiseres på en måte som gjør det mulig å relatere det til andre strukturerte data. Men fordi dataene er designet for å være organisert på en spesifikk måte, kan det være tidkrevende å gjøre endringer i den overordnede strukturen. For eksempel, hvis du legger til en e-postkolonne i kunderegnearket som ikke kan være tom, må du finne ut hvordan du skal legge til disse verdiene i de eksisterende radene i datasettet.

Eksempler på strukturert data: regneark, relasjonsdatabaser, telefonnumre, kontoutskrifter.

### Ustrukturert Data
Ustrukturert data kan vanligvis ikke kategoriseres i rader eller kolonner og inneholder ikke et format eller sett med regler å følge. Fordi ustrukturert data har færre begrensninger på strukturen, er det enklere å legge til ny informasjon sammenlignet med et strukturert datasett. Hvis en sensor som registrerer data om barometrisk trykk hvert 2. minutt får en oppdatering som nå lar den måle og registrere temperatur, krever det ikke endring av eksisterende data hvis det er ustrukturert. Men dette kan gjøre analyser eller undersøkelser av denne typen data mer tidkrevende. For eksempel, en forsker som ønsker å finne gjennomsnittstemperaturen for forrige måned fra sensorens data, men oppdager at sensoren har registrert en "e" i noen av sine data for å indikere at den var ødelagt, i stedet for et typisk tall, noe som betyr at dataene er ufullstendige.

Eksempler på ustrukturert data: tekstfiler, tekstmeldinger, videofiler.

### Semi-strukturert Data
Semi-strukturert data har egenskaper som gjør det til en kombinasjon av strukturert og ustrukturert data. Det følger vanligvis ikke et format med rader og kolonner, men er organisert på en måte som anses som strukturert og kan følge et fast format eller sett med regler. Strukturen vil variere mellom kilder, fra en veldefinert hierarki til noe mer fleksibelt som tillater enkel integrering av ny informasjon. Metadata er indikatorer som hjelper til med å bestemme hvordan dataene er organisert og lagret, og vil ha ulike navn basert på typen data. Noen vanlige navn for metadata er tagger, elementer, enheter og attributter. For eksempel vil en typisk e-postmelding ha et emne, en tekst og et sett med mottakere og kan organiseres etter hvem eller når den ble sendt.

Eksempler på semi-strukturert data: HTML, CSV-filer, JavaScript Object Notation (JSON).

## Datakilder

En datakilde er det opprinnelige stedet hvor dataene ble generert, eller hvor de "bor", og vil variere basert på hvordan og når de ble samlet inn. Data generert av brukeren(e) kalles primærdata, mens sekundærdata kommer fra en kilde som har samlet inn data for generell bruk. For eksempel, en gruppe forskere som samler observasjoner i en regnskog vil bli betraktet som primærdata, og hvis de deler det med andre forskere, vil det bli betraktet som sekundærdata for de som bruker det.

Databaser er en vanlig kilde og er avhengige av et databaseadministrasjonssystem for å være vert for og vedlikeholde dataene, hvor brukere bruker kommandoer kalt spørringer for å utforske dataene. Filer som datakilder kan være lyd-, bilde- og videofiler, samt regneark som Excel. Internettkilder er et vanlig sted for hosting av data, hvor databaser så vel som filer kan finnes. Application programming interfaces, også kjent som API-er, lar programmerere lage måter å dele data med eksterne brukere via internett, mens prosessen med webskraping trekker ut data fra en nettside. [Leksjonene i Arbeide med Data](../../../../../../../../../2-Working-With-Data) fokuserer på hvordan man bruker ulike datakilder.

## Konklusjon

I denne leksjonen har vi lært:

- Hva data er
- Hvordan data beskrives
- Hvordan data klassifiseres og kategoriseres
- Hvor data kan finnes

## 🚀 Utfordring

Kaggle er en utmerket kilde til åpne datasett. Bruk [verktøyet for datasett-søk](https://www.kaggle.com/datasets) for å finne noen interessante datasett og klassifiser 3-5 datasett med følgende kriterier:

- Er dataene kvantitative eller kvalitative?
- Er dataene strukturerte, ustrukturerte eller semi-strukturerte?

## [Quiz etter forelesning](https://ff-quizzes.netlify.app/en/ds/quiz/5)

## Gjennomgang & Selvstudium

- Denne Microsoft Learn-enheten, kalt [Classify your Data](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/2-classify-data), har en detaljert oversikt over strukturert, semi-strukturert og ustrukturert data.

## Oppgave

[Classifying Datasets](assignment.md)

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.