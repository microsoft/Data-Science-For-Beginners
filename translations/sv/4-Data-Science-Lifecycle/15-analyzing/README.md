<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2baeafe1db4d58ee5b8ec85db9de728a",
  "translation_date": "2025-09-05T21:46:17+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "sv"
}
-->
# Livscykeln för datavetenskap: Analysera

|![ Sketchnote av [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Livscykeln för datavetenskap: Analysera - _Sketchnote av [@nitya](https://twitter.com/nitya)_ |

## Förquiz före föreläsning

## [Förquiz före föreläsning](https://ff-quizzes.netlify.app/en/ds/quiz/28)

Att analysera i datalivscykeln bekräftar att datan kan besvara de frågor som ställts eller lösa ett specifikt problem. Detta steg kan också fokusera på att säkerställa att en modell korrekt adresserar dessa frågor och problem. Den här lektionen fokuserar på Exploratory Data Analysis (EDA), som är tekniker för att definiera egenskaper och relationer inom datan och kan användas för att förbereda datan för modellering.

Vi kommer att använda ett exempeldata från [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1) för att visa hur detta kan tillämpas med Python och Pandas-biblioteket. Detta dataset innehåller en räkning av några vanliga ord som finns i e-postmeddelanden, där källorna till dessa e-postmeddelanden är anonyma. Använd [notebook](../../../../4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb) i denna katalog för att följa med.

## Exploratory Data Analysis

Fasen för insamling i livscykeln är där datan samlas in samt problemen och frågorna identifieras, men hur vet vi att datan kan hjälpa till att stödja slutresultatet? 
Kom ihåg att en datavetare kan ställa följande frågor när de samlar in data:
-   Har jag tillräckligt med data för att lösa detta problem?
-   Är datan av acceptabel kvalitet för detta problem?
-   Om jag upptäcker ytterligare information genom denna data, bör vi överväga att ändra eller omdefiniera målen?

Exploratory Data Analysis är processen att lära känna datan och kan användas för att besvara dessa frågor, samt identifiera utmaningar med att arbeta med datasetet. Låt oss fokusera på några av de tekniker som används för att uppnå detta.

## Dataprofilering, beskrivande statistik och Pandas
Hur utvärderar vi om vi har tillräckligt med data för att lösa detta problem? Dataprofilering kan sammanfatta och samla in viss generell information om vårt dataset genom tekniker för beskrivande statistik. Dataprofilering hjälper oss att förstå vad som finns tillgängligt för oss, och beskrivande statistik hjälper oss att förstå hur mycket som finns tillgängligt.

I några av de tidigare lektionerna har vi använt Pandas för att tillhandahålla viss beskrivande statistik med funktionen [`describe()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html). Den ger räkning, max- och minvärden, medelvärde, standardavvikelse och kvantiler för den numeriska datan. Att använda beskrivande statistik som funktionen `describe()` kan hjälpa dig att bedöma hur mycket du har och om du behöver mer.

## Sampling och frågeställningar
Att utforska allt i ett stort dataset kan vara mycket tidskrävande och en uppgift som vanligtvis lämnas till en dator att utföra. Dock är sampling ett användbart verktyg för att förstå datan och ger oss en bättre förståelse för vad som finns i datasetet och vad det representerar. Med ett urval kan du tillämpa sannolikhet och statistik för att dra vissa generella slutsatser om din data. Även om det inte finns någon definierad regel för hur mycket data du bör sampla är det viktigt att notera att ju mer data du samplar, desto mer exakt kan du generalisera om datan.

Pandas har funktionen [`sample()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html) där du kan ange hur många slumpmässiga prover du vill få och använda.

Generella frågeställningar om datan kan hjälpa dig att besvara vissa generella frågor och teorier du kan ha. Till skillnad från sampling tillåter frågor dig att ha kontroll och fokusera på specifika delar av datan som du har frågor om. 
Funktionen [`query()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) i Pandas-biblioteket låter dig välja kolumner och få enkla svar om datan genom de rader som hämtas.

## Utforska med visualiseringar
Du behöver inte vänta tills datan är noggrant rengjord och analyserad för att börja skapa visualiseringar. Faktum är att ha en visuell representation medan du utforskar kan hjälpa till att identifiera mönster, relationer och problem i datan. Dessutom ger visualiseringar ett sätt att kommunicera med dem som inte är involverade i att hantera datan och kan vara en möjlighet att dela och klargöra ytterligare frågor som inte adresserades i insamlingsfasen. Se [avsnittet om visualiseringar](../../../../../../../../../3-Data-Visualization) för att lära dig mer om några populära sätt att utforska visuellt.

## Utforska för att identifiera inkonsekvenser
Alla ämnen i denna lektion kan hjälpa till att identifiera saknade eller inkonsekventa värden, men Pandas tillhandahåller funktioner för att kontrollera några av dessa. [isna() eller isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) kan kontrollera saknade värden. En viktig del av att utforska dessa värden inom din data är att undersöka varför de hamnade så från början. Detta kan hjälpa dig att besluta om vilka [åtgärder som ska vidtas för att lösa dem](../../../../../../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Efterquiz efter föreläsning](https://ff-quizzes.netlify.app/en/ds/quiz/29)

## Uppgift

[Utforska för svar](assignment.md)

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen notera att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.