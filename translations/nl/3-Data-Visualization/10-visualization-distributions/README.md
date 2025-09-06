<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a20467e046d312809d008395051fc7",
  "translation_date": "2025-09-05T23:03:19+00:00",
  "source_file": "3-Data-Visualization/10-visualization-distributions/README.md",
  "language_code": "nl"
}
-->
# Visualiseren van Distributies

|![ Sketchnote door [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| Visualiseren van Distributies - _Sketchnote door [@nitya](https://twitter.com/nitya)_ |

In de vorige les heb je enkele interessante feiten geleerd over een dataset over de vogels van Minnesota. Je ontdekte foutieve gegevens door uitschieters te visualiseren en bekeek de verschillen tussen vogelcategorieën op basis van hun maximale lengte.

## [Quiz voorafgaand aan de les](https://ff-quizzes.netlify.app/en/ds/quiz/18)
## Verken de vogeldataset

Een andere manier om gegevens te onderzoeken is door te kijken naar de verdeling ervan, of hoe de gegevens langs een as zijn georganiseerd. Misschien wil je bijvoorbeeld meer te weten komen over de algemene verdeling van de maximale spanwijdte of het maximale lichaamsgewicht van de vogels in Minnesota in deze dataset.

Laten we enkele feiten ontdekken over de verdelingen van gegevens in deze dataset. Importeer in het bestand _notebook.ipynb_ in de hoofdmap van deze lesmap Pandas, Matplotlib en je gegevens:

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```

|      | Naam                         | WetenschappelijkeNaam  | Categorie             | Orde         | Familie  | Geslacht    | Beschermingsstatus  | MinLengte | MaxLengte | MinLichaamsgewicht | MaxLichaamsgewicht | MinSpanwijdte | MaxSpanwijdte |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | -----------------: | -----------------: | ------------: | ------------: |
|    0 | Zwartbuikfluiteend           | Dendrocygna autumnalis | Eenden/Ganzen/Watervogels | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |               652  |              1020  |            76 |            94 |
|    1 | Rosse fluiteend              | Dendrocygna bicolor    | Eenden/Ganzen/Watervogels | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |               712  |              1050  |            85 |            93 |
|    2 | Sneeuwgans                   | Anser caerulescens     | Eenden/Ganzen/Watervogels | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |              2050  |              4050  |           135 |           165 |
|    3 | Ross' gans                   | Anser rossii           | Eenden/Ganzen/Watervogels | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |              1066  |              1567  |           113 |           116 |
|    4 | Grote rietgans               | Anser albifrons        | Eenden/Ganzen/Watervogels | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |              1930  |              3310  |           130 |           165 |

Over het algemeen kun je snel naar de verdeling van gegevens kijken door een scatterplot te gebruiken, zoals we in de vorige les deden:

```python
birds.plot(kind='scatter',x='MaxLength',y='Order',figsize=(12,8))

plt.title('Max Length per Order')
plt.ylabel('Order')
plt.xlabel('Max Length')

plt.show()
```
![max lengte per orde](../../../../3-Data-Visualization/10-visualization-distributions/images/scatter-wb.png)

Dit geeft een overzicht van de algemene verdeling van lichaamslengte per vogelorde, maar het is niet de optimale manier om echte verdelingen weer te geven. Die taak wordt meestal uitgevoerd door een histogram te maken.

## Werken met histogrammen

Matplotlib biedt uitstekende manieren om gegevensverdelingen te visualiseren met behulp van histogrammen. Dit type grafiek lijkt op een staafdiagram waarbij de verdeling zichtbaar is via een stijging en daling van de staven. Om een histogram te maken, heb je numerieke gegevens nodig. Om een histogram te maken, kun je een grafiek plotten waarbij je het type instelt op 'hist' voor histogram. Deze grafiek toont de verdeling van MaxBodyMass voor het volledige bereik van numerieke gegevens in de dataset. Door de gegevensreeks op te splitsen in kleinere intervallen (bins), kan het de verdeling van de waarden weergeven:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 10, figsize = (12,12))
plt.show()
```
![verdeling over de hele dataset](../../../../3-Data-Visualization/10-visualization-distributions/images/dist1-wb.png)

Zoals je kunt zien, valt het merendeel van de 400+ vogels in deze dataset in het bereik van minder dan 2000 voor hun maximale lichaamsgewicht. Krijg meer inzicht in de gegevens door de parameter `bins` te verhogen naar bijvoorbeeld 30:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 30, figsize = (12,12))
plt.show()
```
![verdeling over de hele dataset met grotere bins](../../../../3-Data-Visualization/10-visualization-distributions/images/dist2-wb.png)

Deze grafiek toont de verdeling op een iets meer gedetailleerde manier. Een grafiek die minder naar links is scheefgetrokken, kan worden gemaakt door ervoor te zorgen dat je alleen gegevens binnen een bepaald bereik selecteert:

Filter je gegevens om alleen die vogels te krijgen waarvan het lichaamsgewicht onder de 60 ligt, en toon 40 `bins`:

```python
filteredBirds = birds[(birds['MaxBodyMass'] > 1) & (birds['MaxBodyMass'] < 60)]      
filteredBirds['MaxBodyMass'].plot(kind = 'hist',bins = 40,figsize = (12,12))
plt.show()     
```
![gefilterd histogram](../../../../3-Data-Visualization/10-visualization-distributions/images/dist3-wb.png)

✅ Probeer enkele andere filters en gegevenspunten. Om de volledige verdeling van de gegevens te zien, verwijder je de `['MaxBodyMass']`-filter om gelabelde verdelingen te tonen.

Het histogram biedt ook enkele leuke kleur- en labelverbeteringen om uit te proberen:

Maak een 2D-histogram om de relatie tussen twee verdelingen te vergelijken. Laten we `MaxBodyMass` vergelijken met `MaxLength`. Matplotlib biedt een ingebouwde manier om convergentie te tonen met behulp van helderdere kleuren:

```python
x = filteredBirds['MaxBodyMass']
y = filteredBirds['MaxLength']

fig, ax = plt.subplots(tight_layout=True)
hist = ax.hist2d(x, y)
```
Er lijkt een verwachte correlatie te zijn tussen deze twee elementen langs een verwachte as, met één bijzonder sterk convergentiepunt:

![2D-plot](../../../../3-Data-Visualization/10-visualization-distributions/images/2D-wb.png)

Histogrammen werken standaard goed voor numerieke gegevens. Wat als je verdelingen wilt zien op basis van tekstgegevens? 
## Verken de dataset voor verdelingen met tekstgegevens 

Deze dataset bevat ook goede informatie over de vogelcategorie en zijn geslacht, soort en familie, evenals zijn beschermingsstatus. Laten we deze beschermingsinformatie onderzoeken. Wat is de verdeling van de vogels volgens hun beschermingsstatus?

> ✅ In de dataset worden verschillende acroniemen gebruikt om de beschermingsstatus te beschrijven. Deze acroniemen komen van de [IUCN Rode Lijst Categorieën](https://www.iucnredlist.org/), een organisatie die de status van soorten catalogiseert.
> 
> - CR: Kritiek Bedreigd
> - EN: Bedreigd
> - EX: Uitgestorven
> - LC: Minste Zorg
> - NT: Bijna Bedreigd
> - VU: Kwetsbaar

Dit zijn tekstgebaseerde waarden, dus je moet een transformatie uitvoeren om een histogram te maken. Gebruik de gefilterdeBirds-dataraam om de beschermingsstatus samen met de minimale spanwijdte weer te geven. Wat zie je?

```python
x1 = filteredBirds.loc[filteredBirds.ConservationStatus=='EX', 'MinWingspan']
x2 = filteredBirds.loc[filteredBirds.ConservationStatus=='CR', 'MinWingspan']
x3 = filteredBirds.loc[filteredBirds.ConservationStatus=='EN', 'MinWingspan']
x4 = filteredBirds.loc[filteredBirds.ConservationStatus=='NT', 'MinWingspan']
x5 = filteredBirds.loc[filteredBirds.ConservationStatus=='VU', 'MinWingspan']
x6 = filteredBirds.loc[filteredBirds.ConservationStatus=='LC', 'MinWingspan']

kwargs = dict(alpha=0.5, bins=20)

plt.hist(x1, **kwargs, color='red', label='Extinct')
plt.hist(x2, **kwargs, color='orange', label='Critically Endangered')
plt.hist(x3, **kwargs, color='yellow', label='Endangered')
plt.hist(x4, **kwargs, color='green', label='Near Threatened')
plt.hist(x5, **kwargs, color='blue', label='Vulnerable')
plt.hist(x6, **kwargs, color='gray', label='Least Concern')

plt.gca().set(title='Conservation Status', ylabel='Min Wingspan')
plt.legend();
```

![spanwijdte en beschermingsstatus](../../../../3-Data-Visualization/10-visualization-distributions/images/histogram-conservation-wb.png)

Er lijkt geen goede correlatie te zijn tussen minimale spanwijdte en beschermingsstatus. Test andere elementen van de dataset met deze methode. Je kunt ook verschillende filters proberen. Vind je enige correlatie?

## Dichtheidsplots

Je hebt misschien gemerkt dat de histogrammen die we tot nu toe hebben bekeken 'getrapt' zijn en niet soepel in een boog verlopen. Om een vloeiender dichtheidsgrafiek te tonen, kun je een dichtheidsplot proberen.

Om met dichtheidsplots te werken, kun je jezelf vertrouwd maken met een nieuwe plotbibliotheek, [Seaborn](https://seaborn.pydata.org/generated/seaborn.kdeplot.html). 

Laad Seaborn en probeer een eenvoudige dichtheidsplot:

```python
import seaborn as sns
import matplotlib.pyplot as plt
sns.kdeplot(filteredBirds['MinWingspan'])
plt.show()
```
![Dichtheidsplot](../../../../3-Data-Visualization/10-visualization-distributions/images/density1.png)

Je kunt zien hoe de plot de vorige voor minimale spanwijdte-gegevens weerspiegelt; het is alleen iets vloeiender. Volgens de documentatie van Seaborn: "In vergelijking met een histogram kan KDE een plot produceren die minder rommelig en beter interpreteerbaar is, vooral bij het tekenen van meerdere verdelingen. Maar het heeft het potentieel om vervormingen te introduceren als de onderliggende verdeling begrensd of niet vloeiend is. Net als een histogram hangt de kwaliteit van de representatie ook af van de selectie van goede gladheidsparameters." [bron](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) Met andere woorden, uitschieters zullen, zoals altijd, je grafieken negatief beïnvloeden.

Als je die grillige MaxBodyMass-lijn in de tweede grafiek die je hebt gemaakt opnieuw wilt bekijken, kun je deze heel goed gladstrijken door deze opnieuw te maken met deze methode:

```python
sns.kdeplot(filteredBirds['MaxBodyMass'])
plt.show()
```
![gladde lichaamsgewichtlijn](../../../../3-Data-Visualization/10-visualization-distributions/images/density2.png)

Als je een gladde, maar niet te gladde lijn wilt, pas je de parameter `bw_adjust` aan: 

```python
sns.kdeplot(filteredBirds['MaxBodyMass'], bw_adjust=.2)
plt.show()
```
![minder gladde lichaamsgewichtlijn](../../../../3-Data-Visualization/10-visualization-distributions/images/density3.png)

✅ Lees over de beschikbare parameters voor dit type plot en experimenteer!

Dit type grafiek biedt prachtig verklarende visualisaties. Met een paar regels code kun je bijvoorbeeld de dichtheid van het maximale lichaamsgewicht per vogelorde tonen:

```python
sns.kdeplot(
   data=filteredBirds, x="MaxBodyMass", hue="Order",
   fill=True, common_norm=False, palette="crest",
   alpha=.5, linewidth=0,
)
```

![lichaamsgewicht per orde](../../../../3-Data-Visualization/10-visualization-distributions/images/density4.png)

Je kunt ook de dichtheid van meerdere variabelen in één grafiek weergeven. Test de MaxLength en MinLength van een vogel in vergelijking met hun beschermingsstatus:

```python
sns.kdeplot(data=filteredBirds, x="MinLength", y="MaxLength", hue="ConservationStatus")
```

![meerdere dichtheden, over elkaar heen gelegd](../../../../3-Data-Visualization/10-visualization-distributions/images/multi.png)

Misschien is het de moeite waard om te onderzoeken of de cluster van 'Kwetsbare' vogels op basis van hun lengtes betekenisvol is of niet.

## 🚀 Uitdaging

Histogrammen zijn een geavanceerder type grafiek dan eenvoudige scatterplots, staafdiagrammen of lijndiagrammen. Zoek op internet naar goede voorbeelden van het gebruik van histogrammen. Hoe worden ze gebruikt, wat laten ze zien, en in welke vakgebieden of onderzoeksgebieden worden ze vaak gebruikt?

## [Quiz na de les](https://ff-quizzes.netlify.app/en/ds/quiz/19)

## Herziening & Zelfstudie

In deze les heb je Matplotlib gebruikt en ben je begonnen met Seaborn om meer geavanceerde grafieken te maken. Doe wat onderzoek naar `kdeplot` in Seaborn, een "continue waarschijnlijkheidsdichtheidscurve in één of meer dimensies". Lees de [documentatie](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) om te begrijpen hoe het werkt.

## Opdracht

[Pas je vaardigheden toe](assignment.md)

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, willen we u erop wijzen dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.