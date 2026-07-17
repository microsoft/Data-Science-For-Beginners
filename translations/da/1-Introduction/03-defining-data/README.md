# Definering af Data

|![ Sketchnote af [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Definering af Data - _Sketchnote af [@nitya](https://twitter.com/nitya)_ |

Data er fakta, information, observationer og målinger, der bruges til at gøre opdagelser og støtte informerede beslutninger. Et datapunkt er en enkelt enhed af data inden for et datasæt, som er en samling af datapunkter. Datasæt kan forekomme i forskellige formater og strukturer og vil normalt baseres på dets kilde, eller hvor dataene stammer fra. For eksempel kan en virksomheds månedlige indtjening være i et regneark, men timebaserede pulsmålinger fra et smartwatch kan være i [JSON](https://stackoverflow.com/a/383699) format. Det er almindeligt, at dataforskere arbejder med forskellige typer data inden for et datasæt.

Denne lektion fokuserer på at identificere og klassificere data efter deres karakteristika og deres kilder.

## [Quiz før forelæsningen](https://ff-quizzes.netlify.app/en/ds/quiz/4)
## Hvordan Data Beskrives

### Rå Data
Rå data er data, der er kommet fra sin kilde i sin oprindelige tilstand og ikke er blevet analyseret eller organiseret. For at kunne forstå, hvad der sker med et datasæt, skal det organiseres i et format, som kan forstås både af mennesker og den teknologi, de måtte bruge til at analysere det yderligere. Strukturen i et datasæt beskriver, hvordan det er organiseret og kan klassificeres som struktureret, ustruktureret og semi-struktureret. Disse typer af struktur vil variere afhængigt af kilden, men vil i sidste ende passe ind i disse tre kategorier.

### Kvantitativ Data
Kvantitativ data er numeriske observationer inden for et datasæt og kan typisk analyseres, måles og bruges matematisk. Nogle eksempler på kvantitativ data er: et lands befolkning, en persons højde eller en virksomheds kvartalsvise indtjening. Med yderligere analyse kunne kvantitativ data bruges til at opdage sæsonbestemte tendenser i Air Quality Index (AQI) eller estimere sandsynligheden for myldretidstrafik på en typisk arbejdsdag.

### Kvalitativ Data
Kvalitativ data, også kendt som kategoriske data, er data, der ikke kan måles objektivt som observationer af kvantitativ data. Det er generelt forskellige formater af subjektive data, som fanger kvaliteten af noget, såsom et produkt eller en proces. Nogle gange er kvalitativ data numerisk og ville normalt ikke blive brugt matematisk, som telefonnumre eller tidsstempler. Nogle eksempler på kvalitativ data er: videokommentarer, mærke og model af en bil eller din nærmeste vens yndlingsfarve. Kvalitativ data kunne bruges til at forstå, hvilke produkter forbrugere bedst kan lide eller til at identificere populære søgeord i jobansøgnings-CV'er.

### Struktureret Data
Struktureret data er data, der er organiseret i rækker og kolonner, hvor hver række har samme sæt kolonner. Kolonner repræsenterer en værdi af en bestemt type og identificeres med et navn, der beskriver, hvad værdien repræsenterer, mens rækker indeholder de faktiske værdier. Kolonner har ofte et specifikt sæt regler eller begrænsninger for værdierne for at sikre, at værdierne præcist repræsenterer kolonnen. For eksempel forestil dig et regneark med kunder, hvor hver række skal have et telefonnummer, og telefonnumrene aldrig indeholder alfabetiske tegn. Der kan være regler, der gælder for telefonnummerkolonnen for at sikre, at den aldrig er tom og kun indeholder tal.

En fordel ved struktureret data er, at det kan organiseres på en måde, så det kan relateres til andre strukturerede data. Men fordi dataene er designet til at blive organiseret på en bestemt måde, kan det kræve meget arbejde at ændre dens overordnede struktur. For eksempel betyder det, at hvis man tilføjer en e-mail-kolonne til kunderegnearket, der ikke må være tom, skal du finde ud af, hvordan du tilføjer disse værdier til de eksisterende rækker af kunder i datasættet.

Eksempler på struktureret data: regneark, relationelle databaser, telefonnumre, bankudtog

### Ustruktureret Data
Ustruktureret data kan typisk ikke kategoriseres i rækker eller kolonner og indeholder ikke et format eller et sæt regler, der skal følges. Fordi ustruktureret data har færre begrænsninger i sin struktur, er det nemmere at tilføje ny information sammenlignet med et struktureret datasæt. Hvis en sensor, der måler barometertryk hvert 2. minut, har modtaget en opdatering, der nu tillader den at måle og registrere temperatur, kræver det ikke at ændre de eksisterende data, hvis de er ustrukturerede. Dette kan dog betyde, at det tager længere tid at analysere eller undersøge denne type data. For eksempel en videnskabsmand, der vil finde gennemsnitstemperaturen for den foregående måned ud fra sensorens data, men opdager, at sensoren har registreret et "e" i nogle af sine registrerede data for at angive, at den var defekt i stedet for et typisk tal, hvilket betyder, at dataene er ufuldstændige.

Eksempler på ustruktureret data: tekstfiler, tekstbeskeder, videofiler

### Semi-struktureret
Semi-struktureret data har træk, der gør det til en kombination af struktureret og ustruktureret data. Det tilpasser sig typisk ikke et format med rækker og kolonner, men er organiseret på en måde, der betragtes som struktureret og kan følge et fast format eller et sæt regler. Strukturen vil variere mellem kilder, såsom en veldefineret hierarki til noget mere fleksibelt, der tillader nem integration af ny information. Metadata er indikatorer, der hjælper med at afgøre, hvordan dataene er organiseret og gemt og vil have forskellige navne, baseret på typen af data. Nogle almindelige navne til metadata er tags, elementer, enheder og attributter. For eksempel vil en typisk e-mail besked have et emne, brødtekst og et sæt modtagere og kan organiseres efter hvem eller hvornår den blev sendt.

Eksempler på semi-struktureret data: HTML, CSV-filer, JavaScript Object Notation (JSON)

## Kilder til Data

En datakilde er det oprindelige sted, hvor data blev genereret, eller hvor det "bor", og vil variere afhængigt af, hvordan og hvornår det blev indsamlet. Data genereret af dets bruger(e) kaldes primære data, mens sekundære data kommer fra en kilde, der har indsamlet data til generel brug. For eksempel ville en gruppe videnskabsmænd, der indsamler observationer i en regnskov, blive betragtet som primær, og hvis de beslutter at dele det med andre videnskabsmænd, vil det blive betragtet som sekundært for dem, der bruger det.

Databaser er en almindelig kilde og er afhængige af et databasehåndteringssystem til hosting og vedligeholdelse af data, hvor brugere bruger kommandoer kaldet forespørgsler til at udforske dataene. Filer som datakilder kan være lyd-, billed- og videofiler samt regneark som Excel. Internettets kilder er et almindeligt sted for hosting af data, hvor både databaser og filer kan findes. Application programming interfaces, også kendt som APIs, tillader programmører at skabe måder at dele data med eksterne brugere via internettet, mens processen med web scraping udtrækker data fra en webside. [Lektionen i Arbejde med Data](../../../../../../../../../2-Working-With-Data) fokuserer på, hvordan man bruger forskellige datakilder.

## Konklusion

I denne lektion har vi lært:

- Hvad data er
- Hvordan data beskrives
- Hvordan data klassificeres og kategoriseres
- Hvor data kan findes

## 🚀 Udfordring

Kaggle er en fremragende kilde til åbne datasæt. Brug [datasøgeværktøjet](https://www.kaggle.com/datasets) til at finde nogle interessante datasæt og klassificer 3-5 datasæt efter følgende kriterier:

- Er data kvantitativ eller kvalitativ?
- Er data struktureret, ustruktureret eller semi-struktureret?

## [Quiz efter forelæsningen](https://ff-quizzes.netlify.app/en/ds/quiz/5)



## Gennemgang & Selvstudium

- Denne Microsoft Learn enhed med titlen [Identify data formats](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats?pivots=text) har en detaljeret gennemgang af struktureret, semi-struktureret og ustruktureret data.

## Opgave

[Klassificering af Datasæt](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->