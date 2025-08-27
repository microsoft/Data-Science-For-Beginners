<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d92f57eb110dc7f765c05cbf0f837c77",
  "translation_date": "2025-08-26T22:29:38+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "da"
}
-->
# Data Science Livscyklus: Analyse

|![ Sketchnote af [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Data Science Livscyklus: Analyse - _Sketchnote af [@nitya](https://twitter.com/nitya)_ |

## Quiz før lektionen

## [Quiz før lektionen](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/28)

Analysen i dataens livscyklus bekræfter, at dataene kan besvare de stillede spørgsmål eller løse et specifikt problem. Dette trin fokuserer også på at sikre, at en model korrekt adresserer disse spørgsmål og problemer. Denne lektion handler om Exploratory Data Analysis (EDA), som er teknikker til at definere egenskaber og relationer inden for dataene og kan bruges til at forberede dataene til modellering.

Vi vil bruge et eksempel-datasæt fra [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1) for at vise, hvordan dette kan anvendes med Python og Pandas-biblioteket. Dette datasæt indeholder en optælling af nogle almindelige ord, der findes i e-mails, hvor kilderne til disse e-mails er anonyme. Brug [notebook](notebook.ipynb) i denne mappe til at følge med.

## Exploratory Data Analysis

Indfangningsfasen i livscyklussen er, hvor dataene erhverves, samt de problemer og spørgsmål, der skal adresseres. Men hvordan ved vi, om dataene kan understøtte det ønskede resultat? 
Husk, at en dataforsker kan stille følgende spørgsmål, når de erhverver dataene:
-   Har jeg nok data til at løse dette problem?
-   Er dataene af acceptabel kvalitet til dette problem?
-   Hvis jeg opdager yderligere information gennem disse data, bør vi så overveje at ændre eller omdefinere målene?

Exploratory Data Analysis er processen med at lære dataene at kende og kan bruges til at besvare disse spørgsmål samt identificere udfordringerne ved at arbejde med datasættet. Lad os fokusere på nogle af de teknikker, der bruges til at opnå dette.

## Data Profiling, Deskriptiv Statistik og Pandas
Hvordan vurderer vi, om vi har nok data til at løse dette problem? Data profiling kan opsummere og indsamle nogle generelle oplysninger om vores datasæt gennem teknikker inden for deskriptiv statistik. Data profiling hjælper os med at forstå, hvad der er tilgængeligt for os, og deskriptiv statistik hjælper os med at forstå, hvor mange ting der er tilgængelige for os.

I nogle af de tidligere lektioner har vi brugt Pandas til at levere deskriptiv statistik med [`describe()` funktionen](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html). Den giver optælling, maksimum- og minimumværdier, gennemsnit, standardafvigelse og kvantiler for de numeriske data. Ved at bruge deskriptiv statistik som `describe()` funktionen kan du vurdere, hvor meget du har, og om du har brug for mere.

## Sampling og Forespørgsler
At udforske alt i et stort datasæt kan være meget tidskrævende og en opgave, der normalt overlades til en computer. Sampling er dog et nyttigt værktøj til at forstå dataene og giver os en bedre forståelse af, hvad der er i datasættet, og hvad det repræsenterer. Med en prøve kan du anvende sandsynlighed og statistik for at komme frem til nogle generelle konklusioner om dine data. Selvom der ikke er nogen fast regel for, hvor meget data du bør sample, er det vigtigt at bemærke, at jo mere data du sample, desto mere præcis kan din generalisering om dataene være.

Pandas har [`sample()` funktionen i sit bibliotek](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html), hvor du kan angive, hvor mange tilfældige prøver du ønsker at modtage og bruge.

Generelle forespørgsler om dataene kan hjælpe dig med at besvare nogle generelle spørgsmål og teorier, du måtte have. I modsætning til sampling giver forespørgsler dig mulighed for at have kontrol og fokusere på specifikke dele af dataene, som du har spørgsmål om. 
[`query()` funktionen](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) i Pandas-biblioteket giver dig mulighed for at vælge kolonner og modtage enkle svar om dataene gennem de rækker, der hentes.

## Udforskning med Visualiseringer
Du behøver ikke vente, indtil dataene er grundigt renset og analyseret, før du begynder at lave visualiseringer. Faktisk kan det at have en visuel repræsentation under udforskningen hjælpe med at identificere mønstre, relationer og problemer i dataene. Desuden giver visualiseringer en måde at kommunikere med dem, der ikke er involveret i håndteringen af dataene, og kan være en mulighed for at dele og afklare yderligere spørgsmål, der ikke blev adresseret i indfangningsfasen. Se [sektionen om Visualiseringer](../../../../../../../../../3-Data-Visualization) for at lære mere om nogle populære måder at udforske visuelt.

## Udforskning for at identificere inkonsistenser
Alle emnerne i denne lektion kan hjælpe med at identificere manglende eller inkonsekvente værdier, men Pandas tilbyder funktioner til at tjekke for nogle af disse. [isna() eller isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) kan tjekke for manglende værdier. En vigtig del af udforskningen af disse værdier i dine data er at undersøge, hvorfor de endte sådan i første omgang. Dette kan hjælpe dig med at beslutte, hvilke [handlinger der skal tages for at løse dem](/2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Quiz før lektionen](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/27)

## Opgave

[Udforskning for svar](assignment.md)

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på at sikre nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.