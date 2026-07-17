# Definere Data

|![ Sketchnote av [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Definere Data - _Sketchnote av [@nitya](https://twitter.com/nitya)_ |

Data er fakta, informasjon, observasjoner og målinger som brukes til å gjøre oppdagelser og støtte velinformerte beslutninger. Et datapunkt er en enkelt enhet med data innenfor et datasett, som er en samling av datapunkter. Dataset kan komme i forskjellige formater og strukturer, og vil vanligvis være basert på sin kilde, eller hvor dataene kom fra. For eksempel kan et selskaps månedlige inntjening være i et regneark, men timebaserte pulsmålinger fra en smartklokke kan være i [JSON](https://stackoverflow.com/a/383699) format. Det er vanlig at dataforskere jobber med ulike typer data innenfor et datasett.

Denne leksjonen fokuserer på å identifisere og klassifisere data etter deres egenskaper og kilder.

## [Pre-forelesningsquiz](https://ff-quizzes.netlify.app/en/ds/quiz/4)
## Hvordan Data Beskrives

### Rå Data
Rå data er data som har kommet fra sin kilde i sin opprinnelige tilstand og som ikke er analysert eller organisert. For å forstå hva som skjer med et datasett, må det organiseres i et format som kan forstås av mennesker så vel som teknologien de kan bruke til å analysere det videre. Strukturen til et datasett beskriver hvordan det er organisert og kan klassifiseres som strukturert, ustrukturert og semi-strukturert. Disse typene strukturer vil variere, avhengig av kilden, men vil til slutt passe inn i disse tre kategoriene.

### Kvantitativ Data
Kvantitativ data er numeriske observasjoner innenfor et datasett og kan vanligvis analyseres, måles og brukes matematisk. Noen eksempler på kvantitativ data er: et lands befolkning, en persons høyde eller et selskaps kvartalsvise inntekter. Med noe ekstra analyse kan kvantitativ data brukes til å oppdage sesongtrender i luftkvalitetsindeksen (AQI) eller estimere sannsynligheten for rushtrafikk på en vanlig arbeidsdag.

### Kvalitativ Data
Kvalitativ data, også kjent som kategorisk data, er data som ikke kan måles objektivt som observasjoner av kvantitativ data. Det er generelt ulike former av subjektiv data som fanger kvaliteten på noe, som et produkt eller en prosess. Noen ganger er kvalitativ data numerisk og brukes vanligvis ikke matematisk, for eksempel telefonnumre eller tidsstempler. Noen eksempler på kvalitativ data er: videokommentarer, merke og modell av en bil, eller favorittfargen til dine nærmeste venner. Kvalitativ data kan brukes for å forstå hvilke produkter forbrukerne liker best eller for å identifisere populære nøkkelord i jobbsøknader.

### Strukturert Data
Strukturert data er data som er organisert i rader og kolonner, hvor hver rad har samme sett med kolonner. Kolonner representerer en verdi av en bestemt type og vil bli identifisert med et navn som beskriver hva verdien representerer, mens rader inneholder de faktiske verdiene. Kolonner har ofte et spesifikt sett med regler eller begrensninger på verdiene, for å sikre at verdiene nøyaktig representerer kolonnen. For eksempel, forestill deg et regneark med kunder hvor hver rad må ha et telefonnummer og telefonnumrene aldri inneholder bokstaver. Det kan være regler for telefonnummer-kolonnen for å sørge for at den aldri er tom og bare inneholder tall.

En fordel med strukturert data er at den kan organiseres på en måte som gjør at det kan relateres til andre strukturerte data. Men fordi dataene er designet for å organiseres på en spesifikk måte, kan det være mye arbeid å endre den overordnede strukturen. For eksempel, hvis du legger til en e-postkolonne til kunderegnearket som ikke kan være tom, må du finne ut hvordan disse verdiene skal legges til i de eksisterende kunderradene i datasettet.

Eksempler på strukturert data: regneark, relasjonsdatabaser, telefonnumre, kontoutskrifter

### Ustrukturert Data
Ustrukturert data kan vanligvis ikke kategoriseres i rader eller kolonner og inneholder ikke et format eller sett med regler å følge. Fordi ustrukturert data har færre begrensninger på sin struktur, er det enklere å legge til ny informasjon sammenlignet med et strukturert datasett. Hvis en sensor som fanger data om barometertrykk hvert annet minutt har fått en oppdatering som nå lar den måle og registrere temperatur, kreves det ikke endringer i den eksisterende dataen hvis den er ustrukturert. Dette kan imidlertid gjøre det vanskeligere å analysere eller undersøke denne typen data. For eksempel, en forsker som vil finne gjennomsnittstemperaturen fra forrige måned basert på sensors data, men oppdager at sensoren har registrert en "e" i noen av dataene for å indikere at den var ødelagt i stedet for et typisk tall, noe som betyr at dataene er ufullstendige.

Eksempler på ustrukturert data: tekstfiler, tekstmeldinger, videofiler

### Semi-strukturert
Semi-strukturert data har egenskaper som gjør at det er en kombinasjon av strukturert og ustrukturert data. Det følger vanligvis ikke et format av rader og kolonner, men er organisert på en måte som anses som strukturert og kan følge et fast format eller sett med regler. Strukturen vil variere mellom kilder, fra en veldefinert hierarki til noe mer fleksibelt som tillater enkel integrering av ny informasjon. Metadata er indikatorer som hjelper med å avgjøre hvordan data er organisert og lagret, og vil ha ulike navn basert på hvilken type data det er. Noen vanlige navn for metadata er tagger, elementer, enheter og attributter. For eksempel har en vanlig e-postmelding et emne, innhold og et sett mottakere, og kan organiseres etter hvem som sendte den eller når.

Eksempler på semi-strukturert data: HTML, CSV-filer, JavaScript Object Notation (JSON)

## Datakilder

En datakilde er det opprinnelige stedet hvor dataene ble generert, eller hvor de "bor", og vil variere basert på hvordan og når de ble samlet inn. Data som genereres av bruker(e) kalles primærdata, mens sekundærdata kommer fra en kilde som har samlet data for generell bruk. For eksempel vil en gruppe forskere som samler observasjoner i en regnskog betraktes som primær, og hvis de bestemmer seg for å dele det med andre forskere, vil det betraktes som sekundært for de som bruker det.

Databaser er en vanlig kilde og bruker et databasesystem for å være vert og opprettholde dataene hvor brukere bruker kommandoer kalt spørringer for å utforske dataene. Filer som datakilder kan være lyd-, bilde- og videofiler samt regneark som Excel. Internettkilder er et vanlig sted for hosting av data hvor både databaser og filer kan finnes. Programmeringsgrensesnitt, også kjent som API-er, gjør det mulig for programmerere å lage måter å dele data med eksterne brukere gjennom internett, mens prosessen med webskraping henter data fra en nettside. [Leksjonene i Working with Data](../../../../../../../../../2-Working-With-Data) fokuserer på hvordan bruke ulike datakilder.

## Konklusjon

I denne leksjonen har vi lært:

- Hva data er
- Hvordan data beskrives
- Hvordan data klassifiseres og kategoriseres
- Hvor data kan finnes

## 🚀 Utfordring

Kaggle er en utmerket kilde til åpne datasett. Bruk [datasett-søkverktøyet](https://www.kaggle.com/datasets) for å finne noen interessante datasett og klassifiser 3-5 datasett med dette kriteriet:

- Er dataene kvantitative eller kvalitative?
- Er dataene strukturerte, ustrukturerte, eller semi-strukturerte?

## [Quiz etter forelesningen](https://ff-quizzes.netlify.app/en/ds/quiz/5)



## Gjennomgang & Selvstudium

- Denne Microsoft Learn-enheten, med tittelen [Identify data formats](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats?pivots=text) har en detaljert gjennomgang av strukturert, semi-strukturert og ustrukturert data.

## Oppgave

[Klassifisering av Datasett](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->