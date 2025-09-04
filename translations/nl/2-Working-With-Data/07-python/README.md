<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "57f7db1f4c3ae3361c1d1fbafcdd690c",
  "translation_date": "2025-09-04T19:50:43+00:00",
  "source_file": "2-Working-With-Data/07-python/README.md",
  "language_code": "nl"
}
-->
# Werken met Data: Python en de Pandas-bibliotheek

| ![ Sketchnote door [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/07-WorkWithPython.png) |
| :-------------------------------------------------------------------------------------------------------: |
|                 Werken met Python - _Sketchnote door [@nitya](https://twitter.com/nitya)_                 |

[![Intro Video](../../../../translated_images/video-ds-python.245247dc811db8e4d5ac420246de8a118c63fd28f6a56578d08b630ae549f260.nl.png)](https://youtu.be/dZjWOGbsN4Y)

Hoewel databases zeer efficiënte manieren bieden om gegevens op te slaan en te raadplegen met behulp van querytalen, is de meest flexibele manier van gegevensverwerking het schrijven van je eigen programma om gegevens te manipuleren. In veel gevallen is een databasequery een effectievere aanpak. Maar in sommige gevallen, wanneer complexere gegevensverwerking nodig is, kan dit niet eenvoudig worden gedaan met SQL. 
Gegevensverwerking kan worden geprogrammeerd in elke programmeertaal, maar er zijn bepaalde talen die beter geschikt zijn voor het werken met data. Datawetenschappers geven meestal de voorkeur aan een van de volgende talen:

* **[Python](https://www.python.org/)**, een algemene programmeertaal die vaak wordt beschouwd als een van de beste opties voor beginners vanwege de eenvoud. Python heeft veel extra bibliotheken die je kunnen helpen bij het oplossen van praktische problemen, zoals het extraheren van gegevens uit een ZIP-archief of het converteren van een afbeelding naar grijstinten. Naast datawetenschap wordt Python ook vaak gebruikt voor webontwikkeling. 
* **[R](https://www.r-project.org/)** is een traditionele toolbox die is ontwikkeld met statistische gegevensverwerking in gedachten. Het bevat ook een grote bibliotheekrepository (CRAN), waardoor het een goede keuze is voor gegevensverwerking. R is echter geen algemene programmeertaal en wordt zelden buiten het domein van datawetenschap gebruikt.
* **[Julia](https://julialang.org/)** is een andere taal die specifiek is ontwikkeld voor datawetenschap. Het is bedoeld om betere prestaties te leveren dan Python, waardoor het een geweldig hulpmiddel is voor wetenschappelijke experimenten.

In deze les richten we ons op het gebruik van Python voor eenvoudige gegevensverwerking. We gaan ervan uit dat je basiskennis hebt van de taal. Als je een diepgaande introductie tot Python wilt, kun je een van de volgende bronnen raadplegen:

* [Leer Python op een leuke manier met Turtle Graphics en Fractals](https://github.com/shwars/pycourse) - Een snelle introductiecursus op GitHub over Python-programmering
* [Zet je eerste stappen met Python](https://docs.microsoft.com/en-us/learn/paths/python-first-steps/?WT.mc_id=academic-77958-bethanycheum) Leerpad op [Microsoft Learn](http://learn.microsoft.com/?WT.mc_id=academic-77958-bethanycheum)

Gegevens kunnen in veel vormen voorkomen. In deze les behandelen we drie vormen van gegevens: **tabulaire gegevens**, **tekst** en **afbeeldingen**.

We richten ons op een paar voorbeelden van gegevensverwerking, in plaats van een volledig overzicht te geven van alle gerelateerde bibliotheken. Dit stelt je in staat om een goed idee te krijgen van wat mogelijk is en laat je begrijpen waar je oplossingen kunt vinden voor je problemen wanneer je ze nodig hebt.

> **Meest nuttige advies**. Wanneer je een bepaalde bewerking op gegevens moet uitvoeren en niet weet hoe je dit moet doen, probeer er dan naar te zoeken op internet. [Stackoverflow](https://stackoverflow.com/) bevat vaak veel nuttige codevoorbeelden in Python voor veelvoorkomende taken.



## [Pre-lecture quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/12)

## Tabulaire gegevens en Dataframes

Je hebt al kennisgemaakt met tabulaire gegevens toen we het hadden over relationele databases. Wanneer je veel gegevens hebt die in verschillende gekoppelde tabellen zijn opgeslagen, is het zeker zinvol om SQL te gebruiken om ermee te werken. Er zijn echter veel gevallen waarin we een tabel met gegevens hebben en we **inzicht** of **begrip** willen krijgen over deze gegevens, zoals de verdeling, correlatie tussen waarden, enz. In datawetenschap zijn er veel gevallen waarin we enkele transformaties van de oorspronkelijke gegevens moeten uitvoeren, gevolgd door visualisatie. Beide stappen kunnen eenvoudig worden uitgevoerd met Python.

Er zijn twee zeer nuttige bibliotheken in Python die je kunnen helpen bij het werken met tabulaire gegevens:
* **[Pandas](https://pandas.pydata.org/)** stelt je in staat om zogenaamde **Dataframes** te manipuleren, die vergelijkbaar zijn met relationele tabellen. Je kunt kolommen benoemen en verschillende bewerkingen uitvoeren op rijen, kolommen en dataframes in het algemeen. 
* **[Numpy](https://numpy.org/)** is een bibliotheek voor het werken met **tensors**, oftewel multidimensionale **arrays**. Een array heeft waarden van hetzelfde onderliggende type en is eenvoudiger dan een dataframe, maar biedt meer wiskundige bewerkingen en creëert minder overhead.

Er zijn ook een paar andere bibliotheken die je moet kennen:
* **[Matplotlib](https://matplotlib.org/)** is een bibliotheek die wordt gebruikt voor gegevensvisualisatie en het plotten van grafieken
* **[SciPy](https://www.scipy.org/)** is een bibliotheek met enkele aanvullende wetenschappelijke functies. We zijn deze bibliotheek al tegengekomen toen we het hadden over kansberekening en statistiek

Hier is een stukje code dat je meestal gebruikt om deze bibliotheken te importeren aan het begin van je Python-programma:
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import ... # you need to specify exact sub-packages that you need
``` 

Pandas draait om een paar basisconcepten.

### Series 

**Series** is een reeks waarden, vergelijkbaar met een lijst of numpy-array. Het belangrijkste verschil is dat een series ook een **index** heeft, en wanneer we bewerkingen uitvoeren op series (bijv. optellen), wordt rekening gehouden met de index. De index kan zo eenvoudig zijn als een geheel getal (dit is de standaardindex bij het maken van een series vanuit een lijst of array), of het kan een complexe structuur hebben, zoals een datumbereik.

> **Opmerking**: Er is wat introductiecode voor Pandas in het bijbehorende notebook [`notebook.ipynb`](notebook.ipynb). We schetsen hier slechts enkele voorbeelden, en je bent van harte welkom om het volledige notebook te bekijken.

Laten we een voorbeeld bekijken: we willen de verkoop van onze ijssalon analyseren. Laten we een reeks verkoopcijfers genereren (aantal verkochte items per dag) voor een bepaalde periode:

```python
start_date = "Jan 1, 2020"
end_date = "Mar 31, 2020"
idx = pd.date_range(start_date,end_date)
print(f"Length of index is {len(idx)}")
items_sold = pd.Series(np.random.randint(25,50,size=len(idx)),index=idx)
items_sold.plot()
```
![Tijdreeksplot](../../../../translated_images/timeseries-1.80de678ab1cf727e50e00bcf24009fa2b0a8b90ebc43e34b99a345227d28e467.nl.png)

Stel nu dat we elke week een feestje organiseren voor vrienden en we nemen extra 10 pakken ijs mee voor het feestje. We kunnen een andere series maken, geïndexeerd per week, om dat te laten zien:
```python
additional_items = pd.Series(10,index=pd.date_range(start_date,end_date,freq="W"))
```
Wanneer we twee series optellen, krijgen we het totale aantal:
```python
total_items = items_sold.add(additional_items,fill_value=0)
total_items.plot()
```
![Tijdreeksplot](../../../../translated_images/timeseries-2.aae51d575c55181ceda81ade8c546a2fc2024f9136934386d57b8a189d7570ff.nl.png)

> **Opmerking** dat we niet de eenvoudige syntaxis `total_items+additional_items` gebruiken. Als we dat deden, zouden we veel `NaN` (*Not a Number*) waarden krijgen in de resulterende series. Dit komt omdat er ontbrekende waarden zijn voor sommige indexpunten in de `additional_items` series, en het optellen van `NaN` met iets resulteert in `NaN`. Daarom moeten we de parameter `fill_value` specificeren tijdens het optellen.

Met tijdreeksen kunnen we ook **herbemonsteren** met verschillende tijdsintervallen. Bijvoorbeeld, stel dat we het gemiddelde verkoopvolume maandelijks willen berekenen. We kunnen de volgende code gebruiken:
```python
monthly = total_items.resample("1M").mean()
ax = monthly.plot(kind='bar')
```
![Maandelijkse tijdreeks gemiddelden](../../../../translated_images/timeseries-3.f3147cbc8c624881008564bc0b5d9fcc15e7374d339da91766bd0e1c6bd9e3af.nl.png)

### DataFrame

Een DataFrame is in wezen een verzameling series met dezelfde index. We kunnen meerdere series combineren tot een DataFrame:
```python
a = pd.Series(range(1,10))
b = pd.Series(["I","like","to","play","games","and","will","not","change"],index=range(0,9))
df = pd.DataFrame([a,b])
```
Dit zal een horizontale tabel maken zoals deze:
|     | 0   | 1    | 2   | 3   | 4      | 5   | 6      | 7    | 8    |
| --- | --- | ---- | --- | --- | ------ | --- | ------ | ---- | ---- |
| 0   | 1   | 2    | 3   | 4   | 5      | 6   | 7      | 8    | 9    |
| 1   | I   | like | to  | use | Python | and | Pandas | very | much |

We kunnen ook series gebruiken als kolommen en kolomnamen specificeren met behulp van een dictionary:
```python
df = pd.DataFrame({ 'A' : a, 'B' : b })
```
Dit geeft ons een tabel zoals deze:

|     | A   | B      |
| --- | --- | ------ |
| 0   | 1   | I      |
| 1   | 2   | like   |
| 2   | 3   | to     |
| 3   | 4   | use    |
| 4   | 5   | Python |
| 5   | 6   | and    |
| 6   | 7   | Pandas |
| 7   | 8   | very   |
| 8   | 9   | much   |

**Opmerking** dat we deze tabelindeling ook kunnen krijgen door de vorige tabel te transponeren, bijvoorbeeld door te schrijven 
```python
df = pd.DataFrame([a,b]).T..rename(columns={ 0 : 'A', 1 : 'B' })
```
Hier betekent `.T` de operatie van het transponeren van het DataFrame, d.w.z. het wisselen van rijen en kolommen, en de `rename`-operatie stelt ons in staat om kolommen te hernoemen om overeen te komen met het vorige voorbeeld.

Hier zijn een paar van de belangrijkste bewerkingen die we kunnen uitvoeren op DataFrames:

**Kolomselectie**. We kunnen individuele kolommen selecteren door `df['A']` te schrijven - deze operatie retourneert een Series. We kunnen ook een subset van kolommen selecteren in een ander DataFrame door `df[['B','A']]` te schrijven - dit retourneert een ander DataFrame.

**Filteren** van alleen bepaalde rijen op basis van criteria. Bijvoorbeeld, om alleen rijen met kolom `A` groter dan 5 te behouden, kunnen we schrijven `df[df['A']>5]`.

> **Opmerking**: De manier waarop filteren werkt is als volgt. De expressie `df['A']<5` retourneert een booleaanse series, die aangeeft of de expressie `True` of `False` is voor elk element van de oorspronkelijke series `df['A']`. Wanneer een booleaanse series wordt gebruikt als index, retourneert het een subset van rijen in het DataFrame. Het is dus niet mogelijk om willekeurige Python-booleaanse expressies te gebruiken, bijvoorbeeld door `df[df['A']>5 and df['A']<7]` te schrijven, wat fout zou zijn. In plaats daarvan moet je een speciale `&`-operatie gebruiken op booleaanse series, door te schrijven `df[(df['A']>5) & (df['A']<7)]` (*haakjes zijn hier belangrijk*).

**Nieuwe berekenbare kolommen maken**. We kunnen eenvoudig nieuwe berekenbare kolommen maken voor ons DataFrame door intuïtieve expressies te gebruiken zoals deze:
```python
df['DivA'] = df['A']-df['A'].mean() 
``` 
Dit voorbeeld berekent de afwijking van A ten opzichte van de gemiddelde waarde. Wat hier eigenlijk gebeurt, is dat we een series berekenen en deze vervolgens toewijzen aan de linkerzijde, waardoor een nieuwe kolom wordt gemaakt. Daarom kunnen we geen bewerkingen gebruiken die niet compatibel zijn met series, bijvoorbeeld de onderstaande code is fout:
```python
# Wrong code -> df['ADescr'] = "Low" if df['A'] < 5 else "Hi"
df['LenB'] = len(df['B']) # <- Wrong result
``` 
Het laatste voorbeeld, hoewel syntactisch correct, geeft ons een fout resultaat, omdat het de lengte van de series `B` toewijst aan alle waarden in de kolom, en niet de lengte van individuele elementen zoals we bedoeld hadden.

Als we complexe expressies zoals deze moeten berekenen, kunnen we de `apply`-functie gebruiken. Het laatste voorbeeld kan als volgt worden geschreven:
```python
df['LenB'] = df['B'].apply(lambda x : len(x))
# or 
df['LenB'] = df['B'].apply(len)
```

Na bovenstaande bewerkingen eindigen we met het volgende DataFrame:

|     | A   | B      | DivA | LenB |
| --- | --- | ------ | ---- | ---- |
| 0   | 1   | I      | -4.0 | 1    |
| 1   | 2   | like   | -3.0 | 4    |
| 2   | 3   | to     | -2.0 | 2    |
| 3   | 4   | use    | -1.0 | 3    |
| 4   | 5   | Python | 0.0  | 6    |
| 5   | 6   | and    | 1.0  | 3    |
| 6   | 7   | Pandas | 2.0  | 6    |
| 7   | 8   | very   | 3.0  | 4    |
| 8   | 9   | much   | 4.0  | 4    |

**Rijen selecteren op basis van nummers** kan worden gedaan met behulp van de `iloc`-constructie. Bijvoorbeeld, om de eerste 5 rijen uit het DataFrame te selecteren:
```python
df.iloc[:5]
```

**Groeperen** wordt vaak gebruikt om een resultaat te krijgen dat lijkt op *draaitabellen* in Excel. Stel dat we de gemiddelde waarde van kolom `A` willen berekenen voor elk gegeven aantal `LenB`. Dan kunnen we ons DataFrame groeperen op `LenB` en `mean` aanroepen:
```python
df.groupby(by='LenB').mean()
```
Als we het gemiddelde en het aantal elementen in de groep willen berekenen, kunnen we een meer complexe `aggregate`-functie gebruiken:
```python
df.groupby(by='LenB') \
 .aggregate({ 'DivA' : len, 'A' : lambda x: x.mean() }) \
 .rename(columns={ 'DivA' : 'Count', 'A' : 'Mean'})
```
Dit geeft ons de volgende tabel:

| LenB | Count | Mean     |
| ---- | ----- | -------- |
| 1    | 1     | 1.000000 |
| 2    | 1     | 3.000000 |
| 3    | 2     | 5.000000 |
| 4    | 3     | 6.333333 |
| 6    | 2     | 6.000000 |

### Gegevens verkrijgen
We hebben gezien hoe eenvoudig het is om Series en DataFrames te maken vanuit Python-objecten. Data komt echter meestal in de vorm van een tekstbestand of een Excel-tabel. Gelukkig biedt Pandas ons een eenvoudige manier om data vanaf de schijf te laden. Bijvoorbeeld, het lezen van een CSV-bestand is zo simpel als dit:
```python
df = pd.read_csv('file.csv')
```
We zullen meer voorbeelden zien van het laden van data, inclusief het ophalen van data van externe websites, in de sectie "Challenge".

### Printen en Plotten

Een Data Scientist moet vaak data verkennen, dus het is belangrijk om deze te kunnen visualiseren. Wanneer een DataFrame groot is, willen we vaak alleen controleren of we alles correct doen door de eerste paar rijen af te drukken. Dit kan worden gedaan door `df.head()` aan te roepen. Als je dit uitvoert vanuit Jupyter Notebook, wordt het DataFrame weergegeven in een mooie tabelvorm.

We hebben ook het gebruik van de `plot`-functie gezien om enkele kolommen te visualiseren. Hoewel `plot` erg nuttig is voor veel taken en verschillende grafiektypen ondersteunt via de `kind=`-parameter, kun je altijd de ruwe `matplotlib`-bibliotheek gebruiken om iets complexers te plotten. We zullen datavisualisatie in detail behandelen in aparte cursuslessen.

Dit overzicht behandelt de belangrijkste concepten van Pandas, maar de bibliotheek is zeer uitgebreid en er zijn geen grenzen aan wat je ermee kunt doen! Laten we nu deze kennis toepassen om een specifiek probleem op te lossen.

## 🚀 Challenge 1: Analyse van COVID-verspreiding

Het eerste probleem waarop we ons zullen richten, is het modelleren van de epidemische verspreiding van COVID-19. Om dat te doen, gebruiken we de gegevens over het aantal geïnfecteerde personen in verschillende landen, verstrekt door het [Center for Systems Science and Engineering](https://systems.jhu.edu/) (CSSE) van [Johns Hopkins University](https://jhu.edu/). De dataset is beschikbaar in [deze GitHub-repository](https://github.com/CSSEGISandData/COVID-19).

Omdat we willen demonstreren hoe je met data omgaat, nodigen we je uit om [`notebook-covidspread.ipynb`](notebook-covidspread.ipynb) te openen en deze van boven naar beneden te lezen. Je kunt ook cellen uitvoeren en enkele uitdagingen aangaan die we aan het einde voor je hebben achtergelaten.

![COVID Spread](../../../../translated_images/covidspread.f3d131c4f1d260ab0344d79bac0abe7924598dd754859b165955772e1bd5e8a2.nl.png)

> Als je niet weet hoe je code uitvoert in Jupyter Notebook, bekijk dan [dit artikel](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## Werken met ongestructureerde data

Hoewel data vaak in tabelvorm komt, moeten we in sommige gevallen werken met minder gestructureerde data, zoals tekst of afbeeldingen. In dat geval moeten we, om de dataverwerkingstechnieken die we hierboven hebben gezien toe te passen, op de een of andere manier **gestructureerde** data **extraheren**. Hier zijn enkele voorbeelden:

* Het extraheren van trefwoorden uit tekst en bekijken hoe vaak die trefwoorden voorkomen
* Het gebruik van neurale netwerken om informatie over objecten op een afbeelding te extraheren
* Het verkrijgen van informatie over emoties van mensen via een videofeed van een camera

## 🚀 Challenge 2: Analyse van COVID-papers

In deze uitdaging blijven we bij het onderwerp van de COVID-pandemie en richten we ons op het verwerken van wetenschappelijke papers over het onderwerp. Er is een [CORD-19 Dataset](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) met meer dan 7000 (op het moment van schrijven) papers over COVID, beschikbaar met metadata en samenvattingen (en voor ongeveer de helft is ook de volledige tekst beschikbaar).

Een volledig voorbeeld van het analyseren van deze dataset met behulp van de [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health/?WT.mc_id=academic-77958-bethanycheum) cognitieve service wordt beschreven [in deze blogpost](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/). We zullen een vereenvoudigde versie van deze analyse bespreken.

> **NOTE**: We bieden geen kopie van de dataset als onderdeel van deze repository. Je moet mogelijk eerst het bestand [`metadata.csv`](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge?select=metadata.csv) downloaden van [deze dataset op Kaggle](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge). Registratie bij Kaggle kan vereist zijn. Je kunt de dataset ook zonder registratie downloaden [van hier](https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/historical_releases.html), maar deze bevat alle volledige teksten naast het metadata-bestand.

Open [`notebook-papers.ipynb`](notebook-papers.ipynb) en lees deze van boven naar beneden. Je kunt ook cellen uitvoeren en enkele uitdagingen aangaan die we aan het einde voor je hebben achtergelaten.

![Covid Medical Treatment](../../../../translated_images/covidtreat.b2ba59f57ca45fbcda36e0ddca3f8cfdddeeed6ca879ea7f866d93fa6ec65791.nl.png)

## Verwerken van afbeeldingsdata

Recent zijn zeer krachtige AI-modellen ontwikkeld die ons in staat stellen afbeeldingen te begrijpen. Er zijn veel taken die kunnen worden opgelost met behulp van vooraf getrainde neurale netwerken of clouddiensten. Enkele voorbeelden zijn:

* **Afbeeldingsclassificatie**, waarmee je een afbeelding kunt categoriseren in een van de vooraf gedefinieerde klassen. Je kunt eenvoudig je eigen afbeeldingsclassificators trainen met diensten zoals [Custom Vision](https://azure.microsoft.com/services/cognitive-services/custom-vision-service/?WT.mc_id=academic-77958-bethanycheum)
* **Objectdetectie** om verschillende objecten in een afbeelding te detecteren. Diensten zoals [computer vision](https://azure.microsoft.com/services/cognitive-services/computer-vision/?WT.mc_id=academic-77958-bethanycheum) kunnen een aantal veelvoorkomende objecten detecteren, en je kunt een [Custom Vision](https://azure.microsoft.com/services/cognitive-services/custom-vision-service/?WT.mc_id=academic-77958-bethanycheum)-model trainen om specifieke objecten van interesse te detecteren.
* **Gezichtsdetectie**, inclusief leeftijds-, geslachts- en emotiedetectie. Dit kan worden gedaan via [Face API](https://azure.microsoft.com/services/cognitive-services/face/?WT.mc_id=academic-77958-bethanycheum).

Al deze clouddiensten kunnen worden aangeroepen met behulp van [Python SDKs](https://docs.microsoft.com/samples/azure-samples/cognitive-services-python-sdk-samples/cognitive-services-python-sdk-samples/?WT.mc_id=academic-77958-bethanycheum) en kunnen dus eenvoudig worden geïntegreerd in je workflow voor data-exploratie.

Hier zijn enkele voorbeelden van het verkennen van data uit afbeeldingsbronnen:
* In de blogpost [Hoe leer je Data Science zonder te programmeren](https://soshnikov.com/azure/how-to-learn-data-science-without-coding/) verkennen we Instagram-foto's om te begrijpen wat mensen ertoe brengt meer likes te geven aan een foto. We extraheren eerst zoveel mogelijk informatie uit afbeeldingen met behulp van [computer vision](https://azure.microsoft.com/services/cognitive-services/computer-vision/?WT.mc_id=academic-77958-bethanycheum) en gebruiken vervolgens [Azure Machine Learning AutoML](https://docs.microsoft.com/azure/machine-learning/concept-automated-ml/?WT.mc_id=academic-77958-bethanycheum) om een interpreteerbaar model te bouwen.
* In [Facial Studies Workshop](https://github.com/CloudAdvocacy/FaceStudies) gebruiken we [Face API](https://azure.microsoft.com/services/cognitive-services/face/?WT.mc_id=academic-77958-bethanycheum) om emoties van mensen op foto's van evenementen te extraheren, om te proberen te begrijpen wat mensen gelukkig maakt.

## Conclusie

Of je nu gestructureerde of ongestructureerde data hebt, met Python kun je alle stappen uitvoeren die verband houden met dataverwerking en -begrip. Het is waarschijnlijk de meest flexibele manier van dataverwerking, en daarom gebruiken de meeste data scientists Python als hun primaire tool. Python diepgaand leren is waarschijnlijk een goed idee als je serieus bent over je reis in data science!

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/)

## Review & Zelfstudie

**Boeken**
* [Wes McKinney. Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython](https://www.amazon.com/gp/product/1491957662)

**Online bronnen**
* Officiële [10 minuten naar Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html) tutorial
* [Documentatie over Pandas-visualisatie](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html)

**Python leren**
* [Leer Python op een leuke manier met Turtle Graphics en fractals](https://github.com/shwars/pycourse)
* [Zet je eerste stappen met Python](https://docs.microsoft.com/learn/paths/python-first-steps/?WT.mc_id=academic-77958-bethanycheum) Leerpad op [Microsoft Learn](http://learn.microsoft.com/?WT.mc_id=academic-77958-bethanycheum)

## Opdracht

[Voer een meer gedetailleerde datastudie uit voor de bovenstaande uitdagingen](assignment.md)

## Credits

Deze les is met ♥️ geschreven door [Dmitry Soshnikov](http://soshnikov.com)

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.