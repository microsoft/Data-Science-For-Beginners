<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1b560955ff39a2bcf2a049fce474a951",
  "translation_date": "2025-09-05T21:59:34+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "da"
}
-->
# Arbejde med data: Dataklargøring

|![ Sketchnote af [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|Dataklargøring - _Sketchnote af [@nitya](https://twitter.com/nitya)_ |

## [Quiz før lektion](https://ff-quizzes.netlify.app/en/ds/quiz/14)

Afhængigt af kilden kan rådata indeholde nogle uoverensstemmelser, der skaber udfordringer i analyse og modellering. Med andre ord kan disse data kategoriseres som "beskidte" og skal renses. Denne lektion fokuserer på teknikker til at rense og transformere data for at håndtere udfordringer med manglende, unøjagtige eller ufuldstændige data. Emnerne i denne lektion vil benytte Python og Pandas-biblioteket og vil blive [demonstreret i notebooken](../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb) i denne mappe.

## Vigtigheden af at rense data

- **Lettere at bruge og genbruge**: Når data er korrekt organiseret og normaliseret, bliver det nemmere at søge, bruge og dele med andre.

- **Konsistens**: Data science kræver ofte arbejde med flere datasæt, hvor datasæt fra forskellige kilder skal kombineres. At sikre, at hvert enkelt datasæt har fælles standardisering, gør det muligt at bruge dataene, når de samles i ét datasæt.

- **Modelnøjagtighed**: Rensede data forbedrer nøjagtigheden af de modeller, der er afhængige af dem.

## Almindelige mål og strategier for datarensning

- **Udforskning af et datasæt**: Dataudforskning, som dækkes i en [senere lektion](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing), kan hjælpe dig med at identificere data, der skal renses. Visuel observation af værdier i et datasæt kan give en idé om, hvordan resten ser ud, eller hvilke problemer der kan løses. Udforskning kan involvere grundlæggende forespørgsler, visualiseringer og sampling.

- **Formatering**: Afhængigt af kilden kan data have uoverensstemmelser i, hvordan de præsenteres. Dette kan skabe problemer med at søge efter og repræsentere værdier, hvor de ses i datasættet, men ikke vises korrekt i visualiseringer eller forespørgselsresultater. Almindelige formateringsproblemer involverer fjernelse af mellemrum, datoer og datatyper. Løsning af formateringsproblemer afhænger typisk af dem, der bruger dataene. For eksempel kan standarder for, hvordan datoer og tal præsenteres, variere fra land til land.

- **Duplikationer**: Data med flere forekomster kan give unøjagtige resultater og bør normalt fjernes. Dette kan ofte ske, når man kombinerer to eller flere datasæt. Dog kan der være tilfælde, hvor duplikationer indeholder ekstra information, der skal bevares.

- **Manglende data**: Manglende data kan føre til unøjagtigheder samt svage eller forudindtagede resultater. Nogle gange kan dette løses ved at genindlæse dataene, udfylde de manglende værdier med beregninger og kode som Python, eller blot fjerne værdien og de tilhørende data. Der er mange grunde til, at data kan mangle, og de handlinger, der tages for at løse dette, afhænger af, hvordan og hvorfor de mangler.

## Udforskning af DataFrame-information
> **Læringsmål:** Ved slutningen af dette afsnit bør du være komfortabel med at finde generel information om data, der er gemt i pandas DataFrames.

Når du har indlæst dine data i pandas, vil de sandsynligvis være i en DataFrame (se den tidligere [lektion](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe) for en detaljeret oversigt). Men hvis datasættet i din DataFrame har 60.000 rækker og 400 kolonner, hvordan begynder du så at få en fornemmelse af, hvad du arbejder med? Heldigvis giver [pandas](https://pandas.pydata.org/) nogle praktiske værktøjer til hurtigt at få et overblik over en DataFrame samt de første og sidste rækker.

For at udforske denne funktionalitet vil vi importere Python scikit-learn biblioteket og bruge et ikonisk datasæt: **Iris-datasættet**.

```python
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
iris_df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
```
|                                        |sepal længde (cm)|sepal bredde (cm)|petal længde (cm)|petal bredde (cm)|
|----------------------------------------|-----------------|-----------------|-----------------|----------------|
|0                                       |5.1              |3.5             |1.4              |0.2             |
|1                                       |4.9              |3.0             |1.4              |0.2             |
|2                                       |4.7              |3.2             |1.3              |0.2             |
|3                                       |4.6              |3.1             |1.5              |0.2             |
|4                                       |5.0              |3.6             |1.4              |0.2             |

- **DataFrame.info**: For at starte bruges `info()`-metoden til at udskrive en oversigt over indholdet i en `DataFrame`. Lad os se på dette datasæt for at se, hvad vi har:
```python
iris_df.info()
```
```
RangeIndex: 150 entries, 0 to 149
Data columns (total 4 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   sepal length (cm)  150 non-null    float64
 1   sepal width (cm)   150 non-null    float64
 2   petal length (cm)  150 non-null    float64
 3   petal width (cm)   150 non-null    float64
dtypes: float64(4)
memory usage: 4.8 KB
```
Ud fra dette ved vi, at *Iris*-datasættet har 150 poster i fire kolonner uden null-værdier. Alle data er gemt som 64-bit floating-point tal.

- **DataFrame.head()**: For at kontrollere det faktiske indhold af `DataFrame` bruger vi `head()`-metoden. Lad os se, hvordan de første par rækker af vores `iris_df` ser ud:
```python
iris_df.head()
```
```
   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
0                5.1               3.5                1.4               0.2
1                4.9               3.0                1.4               0.2
2                4.7               3.2                1.3               0.2
3                4.6               3.1                1.5               0.2
4                5.0               3.6                1.4               0.2
```
- **DataFrame.tail()**: Omvendt, for at kontrollere de sidste par rækker af `DataFrame`, bruger vi `tail()`-metoden:
```python
iris_df.tail()
```
```
     sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
145                6.7               3.0                5.2               2.3
146                6.3               2.5                5.0               1.9
147                6.5               3.0                5.2               2.0
148                6.2               3.4                5.4               2.3
149                5.9               3.0                5.1               1.8
```
> **Konklusion:** Bare ved at kigge på metadata om informationen i en DataFrame eller de første og sidste værdier, kan du hurtigt få en idé om størrelsen, formen og indholdet af de data, du arbejder med.

## Håndtering af manglende data
> **Læringsmål:** Ved slutningen af dette afsnit bør du vide, hvordan du erstatter eller fjerner null-værdier fra DataFrames.

Ofte har de datasæt, du vil bruge (eller skal bruge), manglende værdier. Hvordan manglende data håndteres indebærer subtile afvejninger, der kan påvirke din endelige analyse og virkelige resultater.

Pandas håndterer manglende værdier på to måder. Den første har du set før i tidligere afsnit: `NaN`, eller Not a Number. Dette er faktisk en speciel værdi, der er en del af IEEE floating-point specifikationen og bruges kun til at indikere manglende floating-point værdier.

For manglende værdier udover floats bruger pandas Python-objektet `None`. Selvom det kan virke forvirrende at støde på to forskellige typer værdier, der i bund og grund betyder det samme, er der gode programmatiske grunde til dette designvalg. I praksis giver det pandas mulighed for at levere en god kompromisløsning for de fleste tilfælde. Ikke desto mindre har både `None` og `NaN` begrænsninger, som du skal være opmærksom på med hensyn til, hvordan de kan bruges.

Læs mere om `NaN` og `None` i [notebooken](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb)!

- **Detektering af null-værdier**: I `pandas` er `isnull()` og `notnull()` dine primære metoder til at detektere null-data. Begge returnerer Boolean-masker over dine data. Vi vil bruge `numpy` til `NaN`-værdier:
```python
import numpy as np

example1 = pd.Series([0, np.nan, '', None])
example1.isnull()
```
```
0    False
1     True
2    False
3     True
dtype: bool
```
Se nøje på outputtet. Overrasker noget dig? Mens `0` er en aritmetisk null, er det stadig en gyldig integer, og pandas behandler det som sådan. `''` er lidt mere subtil. Selvom vi brugte det i afsnit 1 til at repræsentere en tom strengværdi, er det stadig et strengobjekt og ikke en repræsentation af null ifølge pandas.

Nu vender vi dette rundt og bruger disse metoder på en måde, der ligner, hvordan du vil bruge dem i praksis. Du kan bruge Boolean-masker direkte som en ``Series`` eller ``DataFrame``-indeks, hvilket kan være nyttigt, når du arbejder med isolerede manglende (eller tilstedeværende) værdier.

> **Konklusion**: Både `isnull()` og `notnull()` giver lignende resultater, når du bruger dem i `DataFrame`s: de viser resultaterne og indekset for disse resultater, hvilket vil hjælpe dig enormt, når du arbejder med dine data.

- **Fjernelse af null-værdier**: Ud over at identificere manglende værdier giver pandas en praktisk metode til at fjerne null-værdier fra `Series` og `DataFrame`s. (Især med store datasæt er det ofte mere tilrådeligt blot at fjerne manglende [NA] værdier fra din analyse end at håndtere dem på andre måder.) For at se dette i praksis vender vi tilbage til `example1`:
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
Bemærk, at dette bør ligne dit output fra `example3[example3.notnull()]`. Forskellen her er, at `dropna` har fjernet de manglende værdier fra `Series` `example1`.

Fordi `DataFrame`s har to dimensioner, giver de flere muligheder for at fjerne data.

```python
example2 = pd.DataFrame([[1,      np.nan, 7], 
                         [2,      5,      8], 
                         [np.nan, 6,      9]])
example2
```
|      | 0 | 1 | 2 |
|------|---|---|---|
|0     |1.0|NaN|7  |
|1     |2.0|5.0|8  |
|2     |NaN|6.0|9  |

(Har du bemærket, at pandas opgraderede to af kolonnerne til floats for at rumme `NaN`?)

Du kan ikke fjerne en enkelt værdi fra en `DataFrame`, så du skal fjerne hele rækker eller kolonner. Afhængigt af hvad du laver, kan du vælge det ene eller det andet, og pandas giver dig muligheder for begge dele. Fordi kolonner generelt repræsenterer variabler og rækker repræsenterer observationer i data science, er det mere sandsynligt, at du fjerner rækker af data; standardindstillingen for `dropna()` er at fjerne alle rækker, der indeholder null-værdier:

```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```
Hvis nødvendigt kan du fjerne NA-værdier fra kolonner. Brug `axis=1` for at gøre dette:
```python
example2.dropna(axis='columns')
```
```
	2
0	7
1	8
2	9
```
Bemærk, at dette kan fjerne mange data, som du måske vil beholde, især i mindre datasæt. Hvad hvis du kun vil fjerne rækker eller kolonner, der indeholder flere eller alle null-værdier? Du kan angive disse indstillinger i `dropna` med parametrene `how` og `thresh`.

Som standard er `how='any'` (hvis du vil kontrollere dette selv eller se, hvilke andre parametre metoden har, kan du køre `example4.dropna?` i en kodecelle). Du kan alternativt angive `how='all'` for kun at fjerne rækker eller kolonner, der indeholder alle null-værdier. Lad os udvide vores eksempel `DataFrame` for at se dette i praksis.

```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

Parameteren `thresh` giver dig mere præcis kontrol: du angiver antallet af *ikke-null* værdier, som en række eller kolonne skal have for at blive bevaret:
```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```
Her er den første og sidste række blevet fjernet, fordi de kun indeholder to ikke-null værdier.

- **Udfyldning af null-værdier**: Afhængigt af dit datasæt kan det nogle gange give mere mening at udfylde null-værdier med gyldige værdier i stedet for at fjerne dem. Du kunne bruge `isnull` til at gøre dette direkte, men det kan være besværligt, især hvis du har mange værdier at udfylde. Fordi dette er en så almindelig opgave i data science, giver pandas `fillna`, som returnerer en kopi af `Series` eller `DataFrame` med de manglende værdier erstattet med en af dine valg. Lad os oprette et andet eksempel `Series` for at se, hvordan dette fungerer i praksis.
```python
example3 = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
example3
```
```
a    1.0
b    NaN
c    2.0
d    NaN
e    3.0
dtype: float64
```
Du kan udfylde alle null-poster med en enkelt værdi, såsom `0`:
```python
example3.fillna(0)
```
```
a    1.0
b    0.0
c    2.0
d    0.0
e    3.0
dtype: float64
```
Du kan **forward-fill** null-værdier, hvilket betyder at bruge den sidste gyldige værdi til at udfylde en null:
```python
example3.fillna(method='ffill')
```
```
a    1.0
b    1.0
c    2.0
d    2.0
e    3.0
dtype: float64
```
Du kan også **back-fill** for at propagere den næste gyldige værdi bagud for at udfylde en null:
```python
example3.fillna(method='bfill')
```
```
a    1.0
b    2.0
c    2.0
d    3.0
e    3.0
dtype: float64
```
Som du måske gætter, fungerer dette på samme måde med `DataFrame`s, men du kan også angive en `axis` langs hvilken null-værdier skal udfyldes. Brug igen det tidligere anvendte `example2`:
```python
example2.fillna(method='ffill', axis=1)
```
```
	0	1	2	3
0	1.0	1.0	7.0	7.0
1	2.0	5.0	8.0	8.0
2	NaN	6.0	9.0	9.0
```
Bemærk, at når en tidligere værdi ikke er tilgængelig til forward-filling, forbliver null-værdien.
> **Vigtig pointe:** Der er flere måder at håndtere manglende værdier i dine datasæt. Den specifikke strategi, du vælger (at fjerne dem, erstatte dem eller endda hvordan du erstatter dem), bør afhænge af de specifikke detaljer i dataene. Du vil få en bedre forståelse af, hvordan man håndterer manglende værdier, jo mere du arbejder med og interagerer med datasæt.
## Fjernelse af duplikerede data

> **Læringsmål:** Ved slutningen af dette afsnit bør du være komfortabel med at identificere og fjerne duplikerede værdier fra DataFrames.

Ud over manglende data vil du ofte støde på duplikerede data i virkelige datasæt. Heldigvis tilbyder `pandas` en nem måde at opdage og fjerne duplikerede poster.

- **Identificering af duplikater: `duplicated`**: Du kan nemt finde duplikerede værdier ved hjælp af metoden `duplicated` i pandas, som returnerer en Boolean-maske, der angiver, om en post i en `DataFrame` er en duplikat af en tidligere. Lad os oprette et andet eksempel på en `DataFrame` for at se dette i praksis.
```python
example4 = pd.DataFrame({'letters': ['A','B'] * 2 + ['B'],
                         'numbers': [1, 2, 1, 3, 3]})
example4
```
|      |bogstaver|tal   |
|------|---------|------|
|0     |A        |1     |
|1     |B        |2     |
|2     |A        |1     |
|3     |B        |3     |
|4     |B        |3     |

```python
example4.duplicated()
```
```
0    False
1    False
2     True
3    False
4     True
dtype: bool
```
- **Fjernelse af duplikater: `drop_duplicates`:** returnerer simpelthen en kopi af dataene, hvor alle `duplicated` værdier er `False`:
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
Både `duplicated` og `drop_duplicates` tager som standard alle kolonner i betragtning, men du kan specificere, at de kun skal undersøge et delmængde af kolonner i din `DataFrame`:
```python
example4.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **Vigtig pointe:** Fjernelse af duplikerede data er en essentiel del af næsten alle data science-projekter. Duplikerede data kan ændre resultaterne af dine analyser og give dig unøjagtige resultater!


## 🚀 Udfordring

Alt det diskuterede materiale er tilgængeligt som en [Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb). Derudover er der øvelser efter hver sektion – prøv dem!

## [Quiz efter forelæsning](https://ff-quizzes.netlify.app/en/ds/quiz/15)



## Gennemgang & Selvstudie

Der er mange måder at opdage og nærme sig forberedelsen af dine data til analyse og modellering, og rengøring af data er et vigtigt skridt, der kræver praktisk erfaring. Prøv disse udfordringer fra Kaggle for at udforske teknikker, som denne lektion ikke dækkede.

- [Data Cleaning Challenge: Parsing Dates](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [Data Cleaning Challenge: Scale and Normalize Data](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)


## Opgave

[Evaluering af data fra en formular](assignment.md)

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.