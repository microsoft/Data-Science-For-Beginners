<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2baeafe1db4d58ee5b8ec85db9de728a",
  "translation_date": "2025-09-05T22:20:05+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "no"
}
-->
# Livssyklusen for datavitenskap: Analyse

|![ Sketchnote av [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Livssyklusen for datavitenskap: Analyse - _Sketchnote av [@nitya](https://twitter.com/nitya)_ |

## Quiz før forelesning

## [Quiz før forelesning](https://ff-quizzes.netlify.app/en/ds/quiz/28)

Analysestadiet i datalivssyklusen bekrefter at dataene kan svare på de foreslåtte spørsmålene eller løse et spesifikt problem. Dette trinnet kan også fokusere på å bekrefte at en modell adresserer disse spørsmålene og problemene korrekt. Denne leksjonen handler om utforskende dataanalyse, eller EDA, som er teknikker for å definere egenskaper og relasjoner i dataene og som kan brukes til å forberede dataene for modellering.

Vi skal bruke et eksempel-datasett fra [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1) for å vise hvordan dette kan brukes med Python og Pandas-biblioteket. Dette datasettet inneholder en opptelling av noen vanlige ord som finnes i e-poster, og kildene til disse e-postene er anonyme. Bruk [notatboken](../../../../4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb) i denne mappen for å følge med.

## Utforskende dataanalyse

Innsamlingsfasen i livssyklusen er der dataene hentes inn, samt problemene og spørsmålene som skal løses, men hvordan vet vi at dataene kan bidra til å støtte sluttresultatet? 
Husk at en datavitenskapsmann kan stille følgende spørsmål når de får tilgang til dataene:
-   Har jeg nok data til å løse dette problemet?
-   Er dataene av akseptabel kvalitet for dette problemet?
-   Hvis jeg oppdager tilleggsinformasjon gjennom disse dataene, bør vi vurdere å endre eller omdefinere målene?
Utforskende dataanalyse er prosessen med å bli kjent med dataene og kan brukes til å svare på disse spørsmålene, samt identifisere utfordringene ved å jobbe med datasettet. La oss fokusere på noen av teknikkene som brukes for å oppnå dette.

## Dataprofilering, beskrivende statistikk og Pandas
Hvordan vurderer vi om vi har nok data til å løse dette problemet? Dataprofilering kan oppsummere og samle generell informasjon om datasettet vårt gjennom teknikker innen beskrivende statistikk. Dataprofilering hjelper oss med å forstå hva som er tilgjengelig for oss, og beskrivende statistikk hjelper oss med å forstå hvor mye som er tilgjengelig.

I noen av de tidligere leksjonene har vi brukt Pandas til å gi noen beskrivende statistikker med [`describe()`-funksjonen](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html). Den gir antall, maks- og minverdier, gjennomsnitt, standardavvik og kvantiler for numeriske data. Ved å bruke beskrivende statistikk som `describe()`-funksjonen kan du vurdere hvor mye data du har og om du trenger mer.

## Utvalg og spørringer
Å utforske alt i et stort datasett kan være svært tidkrevende og en oppgave som vanligvis overlates til en datamaskin. Imidlertid er utvalg et nyttig verktøy for å forstå dataene og gir oss en bedre forståelse av hva som finnes i datasettet og hva det representerer. Med et utvalg kan du bruke sannsynlighet og statistikk for å trekke generelle konklusjoner om dataene dine. Selv om det ikke finnes noen fast regel for hvor mye data du bør ta ut, er det viktig å merke seg at jo mer data du tar ut, desto mer presise generaliseringer kan du gjøre om dataene. 
Pandas har [`sample()`-funksjonen i sitt bibliotek](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html), der du kan angi et argument for hvor mange tilfeldige utvalg du ønsker å motta og bruke.

Generelle spørringer av dataene kan hjelpe deg med å svare på noen generelle spørsmål og teorier du måtte ha. I motsetning til utvalg gir spørringer deg kontroll og lar deg fokusere på spesifikke deler av dataene du har spørsmål om. 
[`query()`-funksjonen](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) i Pandas-biblioteket lar deg velge kolonner og få enkle svar om dataene gjennom radene som hentes ut.

## Utforsking med visualiseringer
Du trenger ikke vente til dataene er grundig renset og analysert før du begynner å lage visualiseringer. Faktisk kan det å ha en visuell fremstilling under utforskningen hjelpe med å identifisere mønstre, relasjoner og problemer i dataene. Videre gir visualiseringer en måte å kommunisere med de som ikke er involvert i håndteringen av dataene, og kan være en mulighet til å dele og klargjøre ytterligere spørsmål som ikke ble adressert i innsamlingsfasen. Se [seksjonen om visualiseringer](../../../../../../../../../3-Data-Visualization) for å lære mer om noen populære måter å utforske visuelt.

## Utforsking for å identifisere inkonsekvenser
Alle temaene i denne leksjonen kan hjelpe med å identifisere manglende eller inkonsekvente verdier, men Pandas gir funksjoner for å sjekke noen av disse. [isna() eller isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) kan sjekke etter manglende verdier. En viktig del av å utforske disse verdiene i dataene dine er å undersøke hvorfor de oppsto i utgangspunktet. Dette kan hjelpe deg med å bestemme hvilke [tiltak som skal tas for å løse dem](../../../../../../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Quiz etter forelesning](https://ff-quizzes.netlify.app/en/ds/quiz/29)

## Oppgave

[Utforske for svar](assignment.md)

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.