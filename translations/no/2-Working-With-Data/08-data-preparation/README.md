<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1b560955ff39a2bcf2a049fce474a951",
  "translation_date": "2025-09-05T22:18:48+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "no"
}
-->
# Arbeide med data: Datapreparering

|![ Sketchnote av [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|Datapreparering - _Sketchnote av [@nitya](https://twitter.com/nitya)_ |

## [Quiz før forelesning](https://ff-quizzes.netlify.app/en/ds/quiz/14)

Avhengig av kilden kan rådata inneholde noen inkonsistenser som skaper utfordringer i analyse og modellering. Med andre ord kan disse dataene kategoriseres som "skitne" og må rengjøres. Denne leksjonen fokuserer på teknikker for å rense og transformere data for å håndtere utfordringer som manglende, unøyaktige eller ufullstendige data. Temaene som dekkes i denne leksjonen bruker Python og Pandas-biblioteket og vil bli [demonstrert i notatboken](../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb) i denne katalogen.

## Viktigheten av å rense data

- **Enkel bruk og gjenbruk**: Når data er riktig organisert og normalisert, blir det enklere å søke, bruke og dele med andre.

- **Konsistens**: Dataanalyse krever ofte arbeid med flere datasett, der datasett fra ulike kilder må kombineres. Å sikre at hvert enkelt datasett har felles standardisering vil sørge for at dataene fortsatt er nyttige når de kombineres til ett datasett.

- **Modellnøyaktighet**: Rensede data forbedrer nøyaktigheten til modellene som er avhengige av dem.

## Vanlige mål og strategier for datarensing

- **Utforske et datasett**: Datautforskning, som dekkes i en [senere leksjon](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing), kan hjelpe deg med å oppdage data som må renses. Visuell observasjon av verdier i et datasett kan gi forventninger om hvordan resten av det vil se ut, eller gi en idé om problemer som kan løses. Utforskning kan innebære grunnleggende spørringer, visualiseringer og prøvetaking.

- **Formatering**: Avhengig av kilden kan data ha inkonsistenser i hvordan de presenteres. Dette kan skape problemer med å søke etter og representere verdier, der de er synlige i datasettet, men ikke riktig representert i visualiseringer eller spørringsresultater. Vanlige formateringsproblemer involverer å løse mellomrom, datoer og datatyper. Å løse formateringsproblemer er vanligvis opp til de som bruker dataene. For eksempel kan standarder for hvordan datoer og tall presenteres variere fra land til land.

- **Duplikasjoner**: Data som forekommer mer enn én gang kan gi unøyaktige resultater og bør vanligvis fjernes. Dette kan være en vanlig forekomst når man kombinerer to eller flere datasett. Imidlertid finnes det tilfeller der duplisering i kombinerte datasett inneholder deler som kan gi tilleggsinformasjon og kanskje må bevares.

- **Manglende data**: Manglende data kan føre til unøyaktigheter samt svake eller skjeve resultater. Noen ganger kan dette løses ved å "laste inn" dataene på nytt, fylle inn de manglende verdiene med beregninger og kode som Python, eller bare fjerne verdien og tilhørende data. Det finnes mange grunner til at data kan mangle, og handlingene som tas for å løse disse manglende verdiene kan avhenge av hvordan og hvorfor de manglet i utgangspunktet.

## Utforske informasjon i DataFrame
> **Læringsmål:** Etter denne delen skal du være komfortabel med å finne generell informasjon om data lagret i pandas DataFrames.

Når du har lastet inn dataene dine i pandas, vil de mest sannsynlig være i en DataFrame (se den forrige [leksjonen](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe) for en detaljert oversikt). Men hvis datasettet i din DataFrame har 60 000 rader og 400 kolonner, hvordan begynner du å få en forståelse av hva du jobber med? Heldigvis gir [pandas](https://pandas.pydata.org/) noen praktiske verktøy for raskt å se generell informasjon om en DataFrame i tillegg til de første og siste radene.

For å utforske denne funksjonaliteten, vil vi importere Python-biblioteket scikit-learn og bruke et ikonisk datasett: **Iris-datasettet**.

```python
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
iris_df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
```
|                                        |sepal lengde (cm)|sepal bredde (cm)|petal lengde (cm)|petal bredde (cm)|
|----------------------------------------|-----------------|-----------------|-----------------|----------------|
|0                                       |5.1              |3.5             |1.4              |0.2             |
|1                                       |4.9              |3.0             |1.4              |0.2             |
|2                                       |4.7              |3.2             |1.3              |0.2             |
|3                                       |4.6              |3.1             |1.5              |0.2             |
|4                                       |5.0              |3.6             |1.4              |0.2             |

- **DataFrame.info**: For å begynne, brukes `info()`-metoden til å skrive ut en oppsummering av innholdet i en `DataFrame`. La oss se på dette datasettet for å se hva vi har:
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
Fra dette vet vi at *Iris*-datasettet har 150 oppføringer i fire kolonner uten nullverdier. Alle dataene er lagret som 64-biters flyttall.

- **DataFrame.head()**: Deretter, for å sjekke det faktiske innholdet i `DataFrame`, bruker vi `head()`-metoden. La oss se hva de første radene i vår `iris_df` ser ut som:
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
- **DataFrame.tail()**: For å sjekke de siste radene i `DataFrame`, bruker vi `tail()`-metoden:
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
> **Oppsummering:** Bare ved å se på metadataene om informasjonen i en DataFrame eller de første og siste verdiene, kan du få en umiddelbar idé om størrelsen, formen og innholdet i dataene du jobber med.

## Håndtering av manglende data
> **Læringsmål:** Etter denne delen skal du vite hvordan du erstatter eller fjerner nullverdier fra DataFrames.

Ofte har datasettene du ønsker å bruke (eller må bruke) manglende verdier. Hvordan manglende data håndteres innebærer subtile avveininger som kan påvirke din endelige analyse og virkelige resultater.

Pandas håndterer manglende verdier på to måter. Den første har du sett før i tidligere seksjoner: `NaN`, eller Not a Number. Dette er faktisk en spesiell verdi som er en del av IEEE-flyttallspesifikasjonen og brukes kun til å indikere manglende flyttallsverdier.

For manglende verdier som ikke er flyttall, bruker pandas Python-objektet `None`. Selv om det kan virke forvirrende at du vil møte to forskjellige typer verdier som i hovedsak sier det samme, er det gode programmatiske grunner for dette designvalget, og i praksis gir denne tilnærmingen pandas en god balanse for de aller fleste tilfeller. Likevel har både `None` og `NaN` begrensninger som du må være oppmerksom på med hensyn til hvordan de kan brukes.

Les mer om `NaN` og `None` fra [notatboken](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb)!

- **Oppdage nullverdier**: I `pandas` er `isnull()` og `notnull()` dine primære metoder for å oppdage nullverdier. Begge returnerer boolske masker over dataene dine. Vi vil bruke `numpy` for `NaN`-verdier:
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
Se nøye på utdataene. Er noe av det overraskende? Selv om `0` er en aritmetisk null, er det likevel et heltall og pandas behandler det som sådan. `''` er litt mer subtilt. Selv om vi brukte det i seksjon 1 for å representere en tom strengverdi, er det likevel et strengobjekt og ikke en representasjon av null i pandas.

Nå, la oss snu dette rundt og bruke disse metodene på en måte som ligner mer på hvordan du vil bruke dem i praksis. Du kan bruke boolske masker direkte som en ``Series`` eller ``DataFrame``-indeks, noe som kan være nyttig når du prøver å jobbe med isolerte manglende (eller tilstedeværende) verdier.

> **Oppsummering**: Både `isnull()` og `notnull()` gir lignende resultater når du bruker dem i `DataFrame`s: de viser resultatene og indeksen til disse resultatene, noe som vil hjelpe deg enormt når du jobber med dataene dine.

- **Fjerne nullverdier**: Utover å identifisere manglende verdier, gir pandas en praktisk måte å fjerne nullverdier fra `Series` og `DataFrame`s. (Spesielt for store datasett er det ofte mer tilrådelig å bare fjerne manglende [NA] verdier fra analysen din enn å håndtere dem på andre måter.) For å se dette i praksis, la oss gå tilbake til `example1`:
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
Merk at dette bør se ut som utdataene fra `example3[example3.notnull()]`. Forskjellen her er at, i stedet for bare å indeksere på de maskerte verdiene, har `dropna` fjernet de manglende verdiene fra `Series` `example1`.

Siden `DataFrame`s har to dimensjoner, gir de flere alternativer for å fjerne data.

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

(La du merke til at pandas oppgraderte to av kolonnene til flyttall for å imøtekomme `NaN`-ene?)

Du kan ikke fjerne en enkelt verdi fra en `DataFrame`, så du må fjerne hele rader eller kolonner. Avhengig av hva du gjør, kan du ønske å gjøre det ene eller det andre, og pandas gir deg alternativer for begge. Siden kolonner generelt representerer variabler og rader representerer observasjoner i dataanalyse, er det mer sannsynlig at du fjerner rader med data; standardinnstillingen for `dropna()` er å fjerne alle rader som inneholder nullverdier:

```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```
Hvis nødvendig, kan du fjerne NA-verdier fra kolonner. Bruk `axis=1` for å gjøre dette:
```python
example2.dropna(axis='columns')
```
```
	2
0	7
1	8
2	9
```
Merk at dette kan fjerne mye data som du kanskje vil beholde, spesielt i mindre datasett. Hva om du bare vil fjerne rader eller kolonner som inneholder flere eller til og med bare alle nullverdier? Du spesifiserer disse innstillingene i `dropna` med parameterne `how` og `thresh`.

Som standard er `how='any'` (hvis du vil sjekke selv eller se hvilke andre parametere metoden har, kjør `example4.dropna?` i en kodecelle). Du kan alternativt spesifisere `how='all'` for å bare fjerne rader eller kolonner som inneholder alle nullverdier. La oss utvide vårt eksempel `DataFrame` for å se dette i praksis.

```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

Parameteren `thresh` gir deg mer detaljert kontroll: du angir antall *ikke-null* verdier som en rad eller kolonne må ha for å bli beholdt:
```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```
Her har den første og siste raden blitt fjernet, fordi de inneholder bare to ikke-null verdier.

- **Fylle nullverdier**: Avhengig av datasettet ditt, kan det noen ganger være mer fornuftig å fylle nullverdier med gyldige verdier i stedet for å fjerne dem. Du kan bruke `isnull` til å gjøre dette direkte, men det kan være arbeidskrevende, spesielt hvis du har mange verdier å fylle. Siden dette er en så vanlig oppgave i dataanalyse, gir pandas `fillna`, som returnerer en kopi av `Series` eller `DataFrame` med de manglende verdiene erstattet med en verdi du velger. La oss lage et annet eksempel `Series` for å se hvordan dette fungerer i praksis.
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
Du kan fylle alle nullverdiene med en enkelt verdi, som `0`:
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
Du kan **fremoverfylle** nullverdier, som vil bruke den siste gyldige verdien til å fylle en null:
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
Du kan også **bakoverfylle** for å propagere den neste gyldige verdien bakover for å fylle en null:
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
Som du kanskje gjetter, fungerer dette på samme måte med `DataFrame`s, men du kan også spesifisere en `axis` langs hvilken du fyller nullverdier. Ved å bruke det tidligere brukte `example2` igjen:
```python
example2.fillna(method='ffill', axis=1)
```
```
	0	1	2	3
0	1.0	1.0	7.0	7.0
1	2.0	5.0	8.0	8.0
2	NaN	6.0	9.0	9.0
```
Merk at når en tidligere verdi ikke er tilgjengelig for fremoverfylling, forblir nullverdien.
> **Hovedpoeng:** Det finnes flere måter å håndtere manglende verdier i datasettene dine. Den spesifikke strategien du velger (fjerne dem, erstatte dem, eller hvordan du erstatter dem) bør styres av de spesifikke egenskapene til dataene. Du vil utvikle en bedre forståelse for hvordan du håndterer manglende verdier jo mer du arbeider med og interagerer med datasett.
## Fjerne dupliserte data

> **Læringsmål:** Etter denne delen bør du være komfortabel med å identifisere og fjerne dupliserte verdier fra DataFrames.

I tillegg til manglende data vil du ofte støte på dupliserte data i virkelige datasett. Heldigvis gir `pandas` en enkel måte å oppdage og fjerne dupliserte oppføringer på.

- **Identifisere duplikater: `duplicated`**: Du kan enkelt finne dupliserte verdier ved å bruke `duplicated`-metoden i pandas, som returnerer en boolsk maske som indikerer om en oppføring i en `DataFrame` er en duplikat av en tidligere. La oss lage et annet eksempel på en `DataFrame` for å se dette i praksis.
```python
example4 = pd.DataFrame({'letters': ['A','B'] * 2 + ['B'],
                         'numbers': [1, 2, 1, 3, 3]})
example4
```
|      |bokstaver|tall   |
|------|----------|-------|
|0     |A         |1      |
|1     |B         |2      |
|2     |A         |1      |
|3     |B         |3      |
|4     |B         |3      |

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
- **Fjerne duplikater: `drop_duplicates`:** returnerer enkelt en kopi av dataene der alle `duplicated`-verdiene er `False`:
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
Både `duplicated` og `drop_duplicates` vurderer som standard alle kolonner, men du kan spesifisere at de kun skal undersøke et delsett av kolonner i din `DataFrame`:
```python
example4.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **Viktig å huske:** Å fjerne dupliserte data er en essensiell del av nesten alle dataanalyseprosjekter. Dupliserte data kan endre resultatene av analysene dine og gi deg unøyaktige resultater!


## 🚀 Utfordring

Alt materiale som er diskutert er tilgjengelig som en [Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb). I tillegg finnes det øvelser etter hver seksjon – prøv dem!

## [Quiz etter forelesning](https://ff-quizzes.netlify.app/en/ds/quiz/15)



## Gjennomgang og selvstudium

Det finnes mange måter å oppdage og tilnærme seg forberedelse av data for analyse og modellering, og rengjøring av data er et viktig steg som krever praktisk erfaring. Prøv disse utfordringene fra Kaggle for å utforske teknikker som ikke ble dekket i denne leksjonen.

- [Data Cleaning Challenge: Parsing Dates](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [Data Cleaning Challenge: Scale and Normalize Data](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)


## Oppgave

[Evaluering av data fra et skjema](assignment.md)

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.