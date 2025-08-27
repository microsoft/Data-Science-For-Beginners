<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3ade580a06b5f04d57cc83a768a8fb77",
  "translation_date": "2025-08-26T20:55:54+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "sv"
}
-->
# Arbeta med data: Datapreparation

|![ Sketchnote av [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|Datapreparation - _Sketchnote av [@nitya](https://twitter.com/nitya)_ |

## [Quiz före föreläsning](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/14)

Beroende på dess källa kan rådata innehålla vissa inkonsekvenser som skapar utmaningar vid analys och modellering. Med andra ord kan denna data kategoriseras som "smutsig" och behöver rengöras. Denna lektion fokuserar på tekniker för att rengöra och transformera data för att hantera utmaningar som saknad, felaktig eller ofullständig data. Ämnen som tas upp i denna lektion använder Python och Pandas-biblioteket och kommer att [demonstreras i notebooken](notebook.ipynb) inom denna katalog.

## Vikten av att rengöra data

- **Enkel användning och återanvändning**: När data är korrekt organiserad och normaliserad blir det enklare att söka, använda och dela med andra.

- **Konsistens**: Dataanalys kräver ofta arbete med flera dataset, där dataset från olika källor behöver kombineras. Att säkerställa att varje dataset har gemensam standardisering gör att data fortfarande är användbar när de kombineras till ett dataset.

- **Modellens noggrannhet**: Rengjord data förbättrar noggrannheten hos modeller som är beroende av den.

## Vanliga mål och strategier för datarengöring

- **Utforska ett dataset**: Datautforskning, som tas upp i en [senare lektion](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing), kan hjälpa dig att identifiera data som behöver rengöras. Att visuellt observera värden inom ett dataset kan ge en förväntan om hur resten av det ser ut eller ge en idé om problem som kan lösas. Utforskning kan involvera grundläggande frågor, visualiseringar och sampling.

- **Formatering**: Beroende på källan kan data ha inkonsekvenser i hur den presenteras. Detta kan orsaka problem vid sökning och representation av värden, där de syns inom datasetet men inte är korrekt representerade i visualiseringar eller frågeresultat. Vanliga formateringsproblem inkluderar att lösa problem med blanksteg, datum och datatyper. Att lösa formateringsproblem är vanligtvis upp till de som använder datan. Till exempel kan standarder för hur datum och siffror presenteras skilja sig mellan länder.

- **Dupliceringar**: Data som förekommer mer än en gång kan ge felaktiga resultat och bör vanligtvis tas bort. Detta är vanligt när man kombinerar två eller fler dataset. Det finns dock tillfällen då duplicering i kombinerade dataset innehåller delar som kan ge ytterligare information och kan behöva bevaras.

- **Saknad data**: Saknad data kan orsaka felaktigheter samt svaga eller partiska resultat. Ibland kan detta lösas genom att "ladda om" datan, fylla i de saknade värdena med beräkningar och kod som Python, eller helt enkelt ta bort värdet och motsvarande data. Det finns många anledningar till varför data kan saknas, och de åtgärder som vidtas för att lösa dessa saknade värden kan bero på hur och varför de försvann.

## Utforska DataFrame-information
> **Lärandemål:** I slutet av denna del ska du känna dig bekväm med att hitta generell information om data som lagras i pandas DataFrames.

När du har laddat din data i pandas kommer den troligen att vara i en DataFrame (se den tidigare [lektionen](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe) för en detaljerad översikt). Men om datasetet i din DataFrame har 60 000 rader och 400 kolumner, hur börjar du ens få en känsla för vad du arbetar med? Lyckligtvis erbjuder [pandas](https://pandas.pydata.org/) några praktiska verktyg för att snabbt titta på övergripande information om en DataFrame, samt de första och sista raderna.

För att utforska denna funktionalitet kommer vi att importera Python-biblioteket scikit-learn och använda ett ikoniskt dataset: **Iris-datasetet**.

```python
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
iris_df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
```
|                                        |sepal length (cm)|sepal width (cm)|petal length (cm)|petal width (cm)|
|----------------------------------------|-----------------|----------------|-----------------|----------------|
|0                                       |5.1              |3.5             |1.4              |0.2             |
|1                                       |4.9              |3.0             |1.4              |0.2             |
|2                                       |4.7              |3.2             |1.3              |0.2             |
|3                                       |4.6              |3.1             |1.5              |0.2             |
|4                                       |5.0              |3.6             |1.4              |0.2             |

- **DataFrame.info**: För att börja används metoden `info()` för att skriva ut en sammanfattning av innehållet i en `DataFrame`. Låt oss titta på detta dataset för att se vad vi har:
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
Från detta vet vi att *Iris*-datasetet har 150 poster i fyra kolumner utan några null-poster. All data lagras som 64-bitars flyttal.

- **DataFrame.head()**: För att kontrollera det faktiska innehållet i `DataFrame` använder vi metoden `head()`. Låt oss se hur de första raderna i vår `iris_df` ser ut:
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
- **DataFrame.tail()**: För att kontrollera de sista raderna i `DataFrame` använder vi metoden `tail()`:
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
> **Slutsats:** Genom att bara titta på metadata om informationen i en DataFrame eller de första och sista värdena kan du få en omedelbar uppfattning om storlek, form och innehåll i datan du arbetar med.

## Hantera saknad data
> **Lärandemål:** I slutet av denna del ska du veta hur du ersätter eller tar bort null-värden från DataFrames.

Oftast har de dataset du vill använda (eller måste använda) saknade värden. Hur saknad data hanteras innebär subtila kompromisser som kan påverka din slutliga analys och verkliga resultat.

Pandas hanterar saknade värden på två sätt. Det första har du sett tidigare i tidigare avsnitt: `NaN`, eller Not a Number. Detta är faktiskt ett specialvärde som är en del av IEEE-flyttalspecifikationen och används endast för att indikera saknade flyttalsvärden.

För saknade värden utöver flyttal använder pandas Python-objektet `None`. Även om det kan verka förvirrande att du kommer att stöta på två olika typer av värden som i princip säger samma sak, finns det goda programmatiska skäl för detta designval och i praktiken möjliggör detta att pandas levererar en bra kompromiss för de allra flesta fall. Trots detta har både `None` och `NaN` begränsningar som du måste vara medveten om när det gäller hur de kan användas.

Läs mer om `NaN` och `None` från [notebooken](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb)!

- **Upptäcka null-värden**: I `pandas` är metoderna `isnull()` och `notnull()` dina primära metoder för att upptäcka null-data. Båda returnerar Boolean-masker över din data. Vi kommer att använda `numpy` för `NaN`-värden:
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
Titta noga på utdata. Överraskar något dig? Även om `0` är en aritmetisk null är det ändå ett heltal och pandas behandlar det som sådant. `''` är lite mer subtilt. Även om vi använde det i avsnitt 1 för att representera ett tomt strängvärde, är det ändå ett strängobjekt och inte en representation av null enligt pandas.

Nu ska vi vända på detta och använda dessa metoder på ett sätt som liknar hur du kommer att använda dem i praktiken. Du kan använda Boolean-masker direkt som ett ``Series`` eller ``DataFrame``-index, vilket kan vara användbart när du försöker arbeta med isolerade saknade (eller befintliga) värden.

> **Slutsats**: Både metoderna `isnull()` och `notnull()` ger liknande resultat när du använder dem i `DataFrame`s: de visar resultaten och indexet för dessa resultat, vilket kommer att hjälpa dig enormt när du arbetar med din data.

- **Ta bort null-värden**: Utöver att identifiera saknade värden erbjuder pandas ett bekvämt sätt att ta bort null-värden från `Series` och `DataFrame`s. (Särskilt för stora dataset är det ofta mer tillrådligt att helt enkelt ta bort saknade [NA] värden från din analys än att hantera dem på andra sätt.) För att se detta i praktiken, låt oss återgå till `example1`:
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
Observera att detta bör se ut som din utdata från `example3[example3.notnull()]`. Skillnaden här är att istället för att bara indexera på de maskerade värdena har `dropna` tagit bort dessa saknade värden från `Series` `example1`.

Eftersom `DataFrame`s har två dimensioner erbjuder de fler alternativ för att ta bort data.

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

(Lade du märke till att pandas uppgraderade två av kolumnerna till flyttal för att rymma `NaN`s?)

Du kan inte ta bort ett enskilt värde från en `DataFrame`, så du måste ta bort hela rader eller kolumner. Beroende på vad du gör kanske du vill göra det ena eller det andra, och därför ger pandas dig alternativ för båda. Eftersom kolumner i data science generellt representerar variabler och rader representerar observationer är det mer sannolikt att du tar bort rader av data; standardinställningen för `dropna()` är att ta bort alla rader som innehåller några null-värden:

```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```
Om det behövs kan du ta bort NA-värden från kolumner. Använd `axis=1` för att göra det:
```python
example2.dropna(axis='columns')
```
```
	2
0	7
1	8
2	9
```
Observera att detta kan ta bort mycket data som du kanske vill behålla, särskilt i mindre dataset. Vad händer om du bara vill ta bort rader eller kolumner som innehåller flera eller till och med bara alla null-värden? Du specificerar dessa inställningar i `dropna` med parametrarna `how` och `thresh`.

Som standard är `how='any'` (om du vill kontrollera själv eller se vilka andra parametrar metoden har, kör `example4.dropna?` i en kodcell). Du kan alternativt specificera `how='all'` för att endast ta bort rader eller kolumner som innehåller alla null-värden. Låt oss utöka vårt exempel `DataFrame` för att se detta i praktiken.

```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

Parametern `thresh` ger dig mer detaljerad kontroll: du anger antalet *icke-null* värden som en rad eller kolumn behöver ha för att behållas:
```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```
Här har den första och sista raden tagits bort eftersom de endast innehåller två icke-null-värden.

- **Fylla null-värden**: Beroende på ditt dataset kan det ibland vara mer logiskt att fylla null-värden med giltiga värden istället för att ta bort dem. Du kan använda `isnull` för att göra detta direkt, men det kan vara arbetskrävande, särskilt om du har många värden att fylla. Eftersom detta är en så vanlig uppgift inom data science erbjuder pandas `fillna`, som returnerar en kopia av `Series` eller `DataFrame` med de saknade värdena ersatta med ett av ditt val. Låt oss skapa ett annat exempel `Series` för att se hur detta fungerar i praktiken.
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
Du kan fylla alla null-poster med ett enda värde, som `0`:
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
Du kan **framåt-fylla** null-värden, vilket innebär att använda det senaste giltiga värdet för att fylla ett null:
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
Du kan också **bakåt-fylla** för att sprida nästa giltiga värde bakåt för att fylla ett null:
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
Som du kanske gissar fungerar detta på samma sätt med `DataFrame`s, men du kan också specificera en `axis` längs vilken du fyller null-värden. Genom att använda det tidigare använda `example2` igen:
```python
example2.fillna(method='ffill', axis=1)
```
```
	0	1	2	3
0	1.0	1.0	7.0	7.0
1	2.0	5.0	8.0	8.0
2	NaN	6.0	9.0	9.0
```
Observera att när ett tidigare värde inte är tillgängligt för framåt-fyllning, förblir null-värdet kvar.
> **Viktig insikt:** Det finns flera sätt att hantera saknade värden i dina dataset. Den specifika strategi du använder (ta bort dem, ersätta dem, eller hur du ersätter dem) bör styras av detaljerna i datan. Du kommer att utveckla en bättre känsla för hur du hanterar saknade värden ju mer du arbetar med och interagerar med dataset.

## Ta bort duplicerad data

> **Lärandemål:** Efter denna del ska du känna dig bekväm med att identifiera och ta bort duplicerade värden från DataFrames.

Förutom saknade data kommer du ofta att stöta på duplicerad data i verkliga dataset. Lyckligtvis erbjuder `pandas` ett enkelt sätt att upptäcka och ta bort duplicerade poster.

- **Identifiera duplicat: `duplicated`**: Du kan enkelt hitta duplicerade värden med metoden `duplicated` i pandas, som returnerar en Boolean-mask som indikerar om en post i en `DataFrame` är en kopia av en tidigare. Låt oss skapa ett annat exempel på en `DataFrame` för att se detta i praktiken.
```python
example4 = pd.DataFrame({'letters': ['A','B'] * 2 + ['B'],
                         'numbers': [1, 2, 1, 3, 3]})
example4
```
|      |bokstäver|nummer|
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
- **Ta bort duplicat: `drop_duplicates`:** returnerar helt enkelt en kopia av datan där alla värden som är `duplicated` är `False`:
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
Både `duplicated` och `drop_duplicates` undersöker som standard alla kolumner, men du kan specificera att de endast ska granska en delmängd av kolumnerna i din `DataFrame`:
```python
example4.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **Viktig insikt:** Att ta bort duplicerad data är en viktig del av nästan alla dataanalysprojekt. Duplicerad data kan förändra resultaten av dina analyser och ge dig felaktiga resultat!


## 🚀 Utmaning

Allt material som diskuterats finns tillgängligt som en [Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb). Dessutom finns det övningar efter varje avsnitt, prova dem!

## [Quiz efter föreläsningen](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/15)



## Granskning & Självstudier

Det finns många sätt att upptäcka och närma sig förberedelse av data för analys och modellering, och att rengöra data är ett viktigt steg som kräver praktisk erfarenhet. Prova dessa utmaningar från Kaggle för att utforska tekniker som inte täcktes i denna lektion.

- [Data Cleaning Challenge: Parsing Dates](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [Data Cleaning Challenge: Scale and Normalize Data](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)


## Uppgift

[Utvärdera data från ett formulär](assignment.md)

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.