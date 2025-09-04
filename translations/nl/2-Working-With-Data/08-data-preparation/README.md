<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "90a815d332aea41a222f4c6372e7186e",
  "translation_date": "2025-09-04T19:52:16+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "nl"
}
-->
# Werken met Data: Datavoorbereiding

|![ Sketchnote door [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|Datavoorbereiding - _Sketchnote door [@nitya](https://twitter.com/nitya)_ |

## [Pre-Lecture Quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/14)

Afhankelijk van de bron kan ruwe data inconsistenties bevatten die uitdagingen veroorzaken bij analyse en modellering. Met andere woorden, deze data kan worden gecategoriseerd als "vervuilde" data en moet worden opgeschoond. Deze les richt zich op technieken voor het opschonen en transformeren van data om uitdagingen zoals ontbrekende, onnauwkeurige of onvolledige data aan te pakken. Onderwerpen die in deze les worden behandeld maken gebruik van Python en de Pandas-bibliotheek en worden [gedemonstreerd in het notebook](notebook.ipynb) binnen deze map.

## Het belang van het opschonen van data

- **Gebruiksgemak en herbruikbaarheid**: Wanneer data goed georganiseerd en genormaliseerd is, is het gemakkelijker om te zoeken, te gebruiken en te delen met anderen.

- **Consistentie**: Datawetenschap vereist vaak het werken met meer dan één dataset, waarbij datasets uit verschillende bronnen moeten worden samengevoegd. Door ervoor te zorgen dat elke individuele dataset een gemeenschappelijke standaardisatie heeft, blijft de data bruikbaar wanneer ze worden samengevoegd tot één dataset.

- **Modelnauwkeurigheid**: Opschonen van data verbetert de nauwkeurigheid van modellen die ervan afhankelijk zijn.

## Veelvoorkomende doelen en strategieën voor opschonen

- **Een dataset verkennen**: Data-exploratie, wat wordt behandeld in een [latere les](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing), kan helpen om data te ontdekken die moet worden opgeschoond. Visueel observeren van waarden binnen een dataset kan verwachtingen scheppen over hoe de rest eruit zal zien, of een idee geven van de problemen die kunnen worden opgelost. Exploratie kan bestaan uit basisquery's, visualisaties en steekproeven.

- **Formatteren**: Afhankelijk van de bron kan data inconsistenties bevatten in hoe het wordt gepresenteerd. Dit kan problemen veroorzaken bij het zoeken naar en weergeven van waarden, waarbij ze wel zichtbaar zijn in de dataset maar niet correct worden weergegeven in visualisaties of queryresultaten. Veelvoorkomende formatteringsproblemen omvatten het oplossen van witruimte, datums en datatypes. Het oplossen van formatteringsproblemen is meestal de verantwoordelijkheid van de mensen die de data gebruiken. Bijvoorbeeld, standaarden voor hoe datums en getallen worden gepresenteerd kunnen per land verschillen.

- **Duplicaties**: Data met meer dan één voorkomen kan onnauwkeurige resultaten opleveren en moet meestal worden verwijderd. Dit komt vaak voor bij het samenvoegen van twee of meer datasets. Er zijn echter gevallen waarin duplicatie in samengevoegde datasets extra informatie kan bevatten en mogelijk moet worden behouden.

- **Ontbrekende data**: Ontbrekende data kan onnauwkeurigheden veroorzaken evenals zwakke of bevooroordeelde resultaten. Soms kunnen deze worden opgelost door de data opnieuw te laden, ontbrekende waarden in te vullen met berekeningen en code zoals Python, of simpelweg de waarde en bijbehorende data te verwijderen. Er zijn talloze redenen waarom data ontbreekt en de acties die worden ondernomen om deze ontbrekende waarden op te lossen kunnen afhankelijk zijn van hoe en waarom ze zijn verdwenen.

## Informatie over DataFrames verkennen
> **Leerdoel:** Aan het einde van deze subsectie moet je comfortabel zijn met het vinden van algemene informatie over de data die is opgeslagen in pandas DataFrames.

Zodra je je data hebt geladen in pandas, zal deze hoogstwaarschijnlijk in een DataFrame staan (zie de vorige [les](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe) voor een gedetailleerd overzicht). Maar als de dataset in je DataFrame 60.000 rijen en 400 kolommen bevat, hoe begin je dan een idee te krijgen van waar je mee werkt? Gelukkig biedt [pandas](https://pandas.pydata.org/) enkele handige tools om snel algemene informatie over een DataFrame te bekijken, naast de eerste en laatste paar rijen.

Om deze functionaliteit te verkennen, importeren we de Python scikit-learn bibliotheek en gebruiken we een iconische dataset: de **Iris dataset**.

```python
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
iris_df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
```
|                                        |sepal lengte (cm)|sepal breedte (cm)|petal lengte (cm)|petal breedte (cm)|
|----------------------------------------|-----------------|------------------|-----------------|------------------|
|0                                       |5.1              |3.5               |1.4              |0.2               |
|1                                       |4.9              |3.0               |1.4              |0.2               |
|2                                       |4.7              |3.2               |1.3              |0.2               |
|3                                       |4.6              |3.1               |1.5              |0.2               |
|4                                       |5.0              |3.6               |1.4              |0.2               |

- **DataFrame.info**: Om te beginnen wordt de `info()`-methode gebruikt om een samenvatting van de inhoud in een `DataFrame` af te drukken. Laten we deze dataset bekijken om te zien wat we hebben:
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
Hieruit weten we dat de *Iris* dataset 150 items heeft in vier kolommen zonder null-waarden. Alle data is opgeslagen als 64-bit floating-point getallen.

- **DataFrame.head()**: Vervolgens, om de daadwerkelijke inhoud van de `DataFrame` te controleren, gebruiken we de `head()`-methode. Laten we eens kijken naar de eerste paar rijen van onze `iris_df`:
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
- **DataFrame.tail()**: Omgekeerd, om de laatste paar rijen van de `DataFrame` te controleren, gebruiken we de `tail()`-methode:
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
> **Conclusie:** Alleen al door te kijken naar de metadata over de informatie in een DataFrame of de eerste en laatste paar waarden, kun je direct een idee krijgen van de grootte, vorm en inhoud van de data waarmee je werkt.

## Omgaan met ontbrekende data
> **Leerdoel:** Aan het einde van deze subsectie moet je weten hoe je null-waarden kunt vervangen of verwijderen uit DataFrames.

Meestal bevatten de datasets die je wilt gebruiken (of moet gebruiken) ontbrekende waarden. Hoe ontbrekende data wordt behandeld brengt subtiele afwegingen met zich mee die je uiteindelijke analyse en resultaten in de echte wereld kunnen beïnvloeden.

Pandas behandelt ontbrekende waarden op twee manieren. De eerste heb je eerder gezien in vorige secties: `NaN`, of Not a Number. Dit is eigenlijk een speciale waarde die deel uitmaakt van de IEEE floating-point specificatie en wordt alleen gebruikt om ontbrekende floating-point waarden aan te geven.

Voor ontbrekende waarden anders dan floats gebruikt pandas het Python `None`-object. Hoewel het verwarrend kan lijken dat je twee verschillende soorten waarden tegenkomt die in wezen hetzelfde zeggen, zijn er goede programmatische redenen voor deze ontwerpkeuze en, in de praktijk, maakt deze aanpak het mogelijk voor pandas om een goede compromis te bieden voor de overgrote meerderheid van de gevallen. Desondanks brengen zowel `None` als `NaN` beperkingen met zich mee waar je rekening mee moet houden met betrekking tot hoe ze kunnen worden gebruikt.

Lees meer over `NaN` en `None` in het [notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb)!

- **Detecteren van null-waarden**: In `pandas` zijn de `isnull()` en `notnull()`-methoden je primaire methoden voor het detecteren van null-data. Beide retourneren Booleaanse maskers over je data. We zullen `numpy` gebruiken voor `NaN`-waarden:
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
Kijk goed naar de output. Verrast iets je? Hoewel `0` een aritmetische null is, is het toch een perfect geldig geheel getal en pandas behandelt het als zodanig. `''` is iets subtieler. Hoewel we het in Sectie 1 gebruikten om een lege stringwaarde weer te geven, is het toch een stringobject en geen weergave van null volgens pandas.

Nu draaien we dit om en gebruiken we deze methoden op een manier zoals je ze in de praktijk zult gebruiken. Je kunt Booleaanse maskers direct gebruiken als een ``Series`` of ``DataFrame``-index, wat handig kan zijn bij het werken met geïsoleerde ontbrekende (of aanwezige) waarden.

> **Conclusie**: Zowel de `isnull()` als `notnull()`-methoden produceren vergelijkbare resultaten wanneer je ze gebruikt in `DataFrame`s: ze tonen de resultaten en de index van die resultaten, wat je enorm zal helpen bij het worstelen met je data.

- **Null-waarden verwijderen**: Naast het identificeren van ontbrekende waarden biedt pandas een handige manier om null-waarden te verwijderen uit `Series` en `DataFrame`s. (Met name bij grote datasets is het vaak verstandiger om ontbrekende [NA] waarden gewoon te verwijderen uit je analyse dan ze op andere manieren te behandelen.) Om dit in actie te zien, keren we terug naar `example1`:
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
Merk op dat dit eruit zou moeten zien als je output van `example3[example3.notnull()]`. Het verschil hier is dat, in plaats van alleen te indexeren op de gemaskeerde waarden, `dropna` die ontbrekende waarden heeft verwijderd uit de `Series` `example1`.

Omdat `DataFrame`s twee dimensies hebben, bieden ze meer opties voor het verwijderen van data.

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

(Heb je opgemerkt dat pandas twee van de kolommen heeft omgezet naar floats om de `NaN`s te accommoderen?)

Je kunt geen enkele waarde verwijderen uit een `DataFrame`, dus je moet volledige rijen of kolommen verwijderen. Afhankelijk van wat je doet, wil je misschien het een of het ander doen, en pandas geeft je opties voor beide. Omdat in datawetenschap kolommen meestal variabelen vertegenwoordigen en rijen observaties, ben je eerder geneigd om rijen data te verwijderen; de standaardinstelling voor `dropna()` is om alle rijen te verwijderen die null-waarden bevatten:

```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```
Indien nodig kun je NA-waarden uit kolommen verwijderen. Gebruik `axis=1` om dit te doen:
```python
example2.dropna(axis='columns')
```
```
	2
0	7
1	8
2	9
```
Merk op dat dit veel data kan verwijderen die je misschien wilt behouden, vooral in kleinere datasets. Wat als je alleen rijen of kolommen wilt verwijderen die meerdere of zelfs alle null-waarden bevatten? Je specificeert die instellingen in `dropna` met de parameters `how` en `thresh`.

Standaard is `how='any'` (als je dit zelf wilt controleren of wilt zien welke andere parameters de methode heeft, voer dan `example4.dropna?` uit in een codecel). Je kunt ook `how='all'` specificeren om alleen rijen of kolommen te verwijderen die alle null-waarden bevatten. Laten we ons voorbeeld `DataFrame` uitbreiden om dit in actie te zien.

```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

De parameter `thresh` geeft je fijnmazigere controle: je stelt het aantal *niet-null* waarden in dat een rij of kolom moet hebben om behouden te blijven:
```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```
Hier zijn de eerste en laatste rij verwijderd, omdat ze slechts twee niet-null waarden bevatten.

- **Null-waarden invullen**: Afhankelijk van je dataset kan het soms meer zin hebben om null-waarden in te vullen met geldige waarden in plaats van ze te verwijderen. Je zou `isnull` kunnen gebruiken om dit ter plekke te doen, maar dat kan arbeidsintensief zijn, vooral als je veel waarden moet invullen. Omdat dit zo'n veelvoorkomende taak is in datawetenschap, biedt pandas `fillna`, wat een kopie van de `Series` of `DataFrame` retourneert met de ontbrekende waarden vervangen door een van jouw keuze. Laten we een ander voorbeeld `Series` maken om te zien hoe dit in de praktijk werkt.
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
Je kunt alle null-items invullen met een enkele waarde, zoals `0`:
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
Je kunt null-waarden **voorwaarts invullen**, wat betekent dat je de laatste geldige waarde gebruikt om een null in te vullen:
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
Je kunt ook **achterwaarts invullen** om de volgende geldige waarde terug te propageren om een null in te vullen:
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
Zoals je misschien vermoedt, werkt dit hetzelfde met `DataFrame`s, maar je kunt ook een `axis` specificeren langs welke je null-waarden wilt invullen. Neem opnieuw het eerder gebruikte `example2`:
```python
example2.fillna(method='ffill', axis=1)
```
```
	0	1	2	3
0	1.0	1.0	7.0	7.0
1	2.0	5.0	8.0	8.0
2	NaN	6.0	9.0	9.0
```
Merk op dat wanneer een vorige waarde niet beschikbaar is voor voorwaarts invullen, de null-waarde blijft staan.
> **Belangrijk punt:** Er zijn meerdere manieren om om te gaan met ontbrekende waarden in je datasets. De specifieke strategie die je gebruikt (verwijderen, vervangen, of zelfs hoe je ze vervangt) moet worden bepaald door de specifieke kenmerken van die data. Hoe meer je met datasets werkt en interactie hebt, hoe beter je gevoel wordt voor het omgaan met ontbrekende waarden.

## Duplicaatgegevens verwijderen

> **Leerdoel:** Aan het einde van deze subsectie moet je comfortabel zijn met het identificeren en verwijderen van dubbele waarden uit DataFrames.

Naast ontbrekende data kom je vaak dubbele gegevens tegen in datasets uit de praktijk. Gelukkig biedt `pandas` een eenvoudige manier om dubbele invoer te detecteren en te verwijderen.

- **Duplicaten identificeren: `duplicated`**: Je kunt eenvoudig dubbele waarden opsporen met de `duplicated`-methode in pandas, die een Boolean-masker retourneert dat aangeeft of een invoer in een `DataFrame` een duplicaat is van een eerdere. Laten we een ander voorbeeld `DataFrame` maken om dit in actie te zien.
```python
example4 = pd.DataFrame({'letters': ['A','B'] * 2 + ['B'],
                         'numbers': [1, 2, 1, 3, 3]})
example4
```
|      |letters|numbers|
|------|-------|-------|
|0     |A      |1      |
|1     |B      |2      |
|2     |A      |1      |
|3     |B      |3      |
|4     |B      |3      |

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
- **Duplicaten verwijderen: `drop_duplicates`:** retourneert simpelweg een kopie van de data waarbij alle `duplicated`-waarden `False` zijn:
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
Zowel `duplicated` als `drop_duplicates` beschouwen standaard alle kolommen, maar je kunt specificeren dat ze alleen een subset van kolommen in je `DataFrame` onderzoeken:
```python
example4.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **Belangrijk punt:** Het verwijderen van dubbele gegevens is een essentieel onderdeel van bijna elk data-scienceproject. Dubbele gegevens kunnen de resultaten van je analyses veranderen en je onnauwkeurige resultaten geven!


## 🚀 Uitdaging

Alle besproken materialen worden aangeboden als een [Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb). Daarnaast zijn er oefeningen aanwezig na elke sectie, probeer ze eens uit!

## [Quiz na de les](https://ff-quizzes.netlify.app/en/ds/)



## Review & Zelfstudie

Er zijn veel manieren om te ontdekken en benaderen hoe je je data voorbereidt voor analyse en modellering, en het opschonen van data is een belangrijke stap die een "praktische" ervaring vereist. Probeer deze uitdagingen van Kaggle om technieken te verkennen die in deze les niet zijn behandeld.

- [Data Cleaning Challenge: Parsing Dates](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [Data Cleaning Challenge: Scale and Normalize Data](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)


## Opdracht

[Data evalueren vanuit een formulier](assignment.md)

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.