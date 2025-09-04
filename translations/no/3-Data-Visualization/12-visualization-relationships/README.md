<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b29e427401499e81f4af55a8c4afea76",
  "translation_date": "2025-09-04T19:31:04+00:00",
  "source_file": "3-Data-Visualization/12-visualization-relationships/README.md",
  "language_code": "no"
}
-->
# Visualisering av relasjoner: Alt om honning 🍯

|![ Sketchnote av [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/12-Visualizing-Relationships.png)|
|:---:|
|Visualisering av relasjoner - _Sketchnote av [@nitya](https://twitter.com/nitya)_ |

Vi fortsetter med naturfokuset i vår forskning og utforsker interessante visualiseringer for å vise relasjoner mellom ulike typer honning, basert på et datasett fra [United States Department of Agriculture](https://www.nass.usda.gov/About_NASS/index.php).

Dette datasettet, som inneholder rundt 600 elementer, viser honningproduksjon i mange amerikanske stater. For eksempel kan du se på antall kolonier, avkastning per koloni, total produksjon, lagerbeholdning, pris per pund og verdien av honningen produsert i en gitt stat fra 1998-2012, med én rad per år for hver stat.

Det kan være interessant å visualisere relasjonen mellom en stats produksjon per år og for eksempel prisen på honning i den staten. Alternativt kan du visualisere relasjonen mellom statenes honningavkastning per koloni. Denne tidsperioden dekker den ødeleggende 'CCD' eller 'Colony Collapse Disorder', som først ble observert i 2006 (http://npic.orst.edu/envir/ccd.html), så det er et tankevekkende datasett å studere. 🐝

## [Quiz før leksjonen](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/22)

I denne leksjonen kan du bruke Seaborn, som du har brukt tidligere, som et godt bibliotek for å visualisere relasjoner mellom variabler. Spesielt interessant er bruken av Seaborns `relplot`-funksjon, som lar deg lage scatterplots og linjediagrammer for raskt å visualisere '[statistiske relasjoner](https://seaborn.pydata.org/tutorial/relational.html?highlight=relationships)', som hjelper dataforskere med å forstå hvordan variabler henger sammen.

## Scatterplots

Bruk et scatterplot for å vise hvordan prisen på honning har utviklet seg år for år, per stat. Seaborn, ved bruk av `relplot`, grupperer praktisk nok dataene fra statene og viser datapunkter for både kategoriske og numeriske data.

La oss starte med å importere dataene og Seaborn:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
honey = pd.read_csv('../../data/honey.csv')
honey.head()
```
Du vil legge merke til at honningdataene har flere interessante kolonner, inkludert år og pris per pund. La oss utforske disse dataene, gruppert etter amerikansk stat:

| state | numcol | yieldpercol | totalprod | stocks   | priceperlb | prodvalue | year |
| ----- | ------ | ----------- | --------- | -------- | ---------- | --------- | ---- |
| AL    | 16000  | 71          | 1136000   | 159000   | 0.72       | 818000    | 1998 |
| AZ    | 55000  | 60          | 3300000   | 1485000  | 0.64       | 2112000   | 1998 |
| AR    | 53000  | 65          | 3445000   | 1688000  | 0.59       | 2033000   | 1998 |
| CA    | 450000 | 83          | 37350000  | 12326000 | 0.62       | 23157000  | 1998 |
| CO    | 27000  | 72          | 1944000   | 1594000  | 0.7        | 1361000   | 1998 |

Lag et enkelt scatterplot for å vise relasjonen mellom prisen per pund honning og dens opprinnelsesstat i USA. Gjør `y`-aksen høy nok til å vise alle statene:

```python
sns.relplot(x="priceperlb", y="state", data=honey, height=15, aspect=.5);
```
![scatterplot 1](../../../../translated_images/scatter1.5e1aa5fd6706c5d12b5e503ccb77f8a930f8620f539f524ddf56a16c039a5d2f.no.png)

Vis nå de samme dataene med et honningfarget fargetema for å vise hvordan prisen utvikler seg over årene. Du kan gjøre dette ved å legge til en 'hue'-parameter for å vise endringen år for år:

> ✅ Lær mer om [fargepalettene du kan bruke i Seaborn](https://seaborn.pydata.org/tutorial/color_palettes.html) - prøv et vakkert regnbuefargetema!

```python
sns.relplot(x="priceperlb", y="state", hue="year", palette="YlOrBr", data=honey, height=15, aspect=.5);
```
![scatterplot 2](../../../../translated_images/scatter2.c0041a58621ca702990b001aa0b20cd68c1e1814417139af8a7211a2bed51c5f.no.png)

Med denne fargeendringen kan du tydelig se en sterk progresjon over årene når det gjelder honningpris per pund. Faktisk, hvis du ser på et utvalg av dataene for å verifisere (velg en gitt stat, for eksempel Arizona), kan du se et mønster med prisøkninger år for år, med få unntak:

| state | numcol | yieldpercol | totalprod | stocks  | priceperlb | prodvalue | year |
| ----- | ------ | ----------- | --------- | ------- | ---------- | --------- | ---- |
| AZ    | 55000  | 60          | 3300000   | 1485000 | 0.64       | 2112000   | 1998 |
| AZ    | 52000  | 62          | 3224000   | 1548000 | 0.62       | 1999000   | 1999 |
| AZ    | 40000  | 59          | 2360000   | 1322000 | 0.73       | 1723000   | 2000 |
| AZ    | 43000  | 59          | 2537000   | 1142000 | 0.72       | 1827000   | 2001 |
| AZ    | 38000  | 63          | 2394000   | 1197000 | 1.08       | 2586000   | 2002 |
| AZ    | 35000  | 72          | 2520000   | 983000  | 1.34       | 3377000   | 2003 |
| AZ    | 32000  | 55          | 1760000   | 774000  | 1.11       | 1954000   | 2004 |
| AZ    | 36000  | 50          | 1800000   | 720000  | 1.04       | 1872000   | 2005 |
| AZ    | 30000  | 65          | 1950000   | 839000  | 0.91       | 1775000   | 2006 |
| AZ    | 30000  | 64          | 1920000   | 902000  | 1.26       | 2419000   | 2007 |
| AZ    | 25000  | 64          | 1600000   | 336000  | 1.26       | 2016000   | 2008 |
| AZ    | 20000  | 52          | 1040000   | 562000  | 1.45       | 1508000   | 2009 |
| AZ    | 24000  | 77          | 1848000   | 665000  | 1.52       | 2809000   | 2010 |
| AZ    | 23000  | 53          | 1219000   | 427000  | 1.55       | 1889000   | 2011 |
| AZ    | 22000  | 46          | 1012000   | 253000  | 1.79       | 1811000   | 2012 |

En annen måte å visualisere denne progresjonen på er å bruke størrelse i stedet for farge. For fargeblinde brukere kan dette være et bedre alternativ. Rediger visualiseringen din for å vise en økning i pris ved en økning i prikkens omkrets:

```python
sns.relplot(x="priceperlb", y="state", size="year", data=honey, height=15, aspect=.5);
```
Du kan se at størrelsen på prikkene gradvis øker.

![scatterplot 3](../../../../translated_images/scatter3.3c160a3d1dcb36b37900ebb4cf97f34036f28ae2b7b8e6062766c7c1dfc00853.no.png)

Er dette et enkelt tilfelle av tilbud og etterspørsel? På grunn av faktorer som klimaendringer og kollaps av kolonier, er det mindre honning tilgjengelig for kjøp år for år, og dermed øker prisen?

For å oppdage en korrelasjon mellom noen av variablene i dette datasettet, la oss utforske noen linjediagrammer.

## Linjediagrammer

Spørsmål: Er det en klar økning i prisen på honning per pund år for år? Du kan enklest oppdage dette ved å lage et enkelt linjediagram:

```python
sns.relplot(x="year", y="priceperlb", kind="line", data=honey);
```
Svar: Ja, med noen unntak rundt året 2003:

![line chart 1](../../../../translated_images/line1.f36eb465229a3b1fe385cdc93861aab3939de987d504b05de0b6cd567ef79f43.no.png)

✅ Fordi Seaborn aggregerer data rundt én linje, viser den "de flere målingene ved hver x-verdi ved å plotte gjennomsnittet og 95 % konfidensintervallet rundt gjennomsnittet". [Kilde](https://seaborn.pydata.org/tutorial/relational.html). Denne tidkrevende oppførselen kan deaktiveres ved å legge til `ci=None`.

Spørsmål: Vel, i 2003 kan vi også se en topp i honningtilførselen? Hva hvis du ser på total produksjon år for år?

```python
sns.relplot(x="year", y="totalprod", kind="line", data=honey);
```

![line chart 2](../../../../translated_images/line2.a5b3493dc01058af6402e657aaa9ae1125fafb5e7d6630c777aa60f900a544e4.no.png)

Svar: Ikke egentlig. Hvis du ser på total produksjon, ser det faktisk ut til å ha økt det året, selv om mengden honning som produseres generelt sett er i nedgang i disse årene.

Spørsmål: I så fall, hva kan ha forårsaket den toppen i prisen på honning rundt 2003?

For å oppdage dette kan du utforske et facet grid.

## Facet grids

Facet grids tar én fasett av datasettet ditt (i vårt tilfelle kan du velge 'år' for å unngå å produsere for mange fasetter). Seaborn kan deretter lage et diagram for hver av disse fasettene av dine valgte x- og y-koordinater for enklere visuell sammenligning. Skiller 2003 seg ut i denne typen sammenligning?

Lag et facet grid ved å fortsette å bruke `relplot` som anbefalt av [Seaborns dokumentasjon](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html?highlight=facetgrid#seaborn.FacetGrid).

```python
sns.relplot(
    data=honey, 
    x="yieldpercol", y="numcol",
    col="year", 
    col_wrap=3,
    kind="line"
```
I denne visualiseringen kan du sammenligne avkastning per koloni og antall kolonier år for år, side om side med en wrap satt til 3 for kolonnene:

![facet grid](../../../../translated_images/facet.6a34851dcd540050dcc0ead741be35075d776741668dd0e42f482c89b114c217.no.png)

For dette datasettet skiller ingenting seg spesielt ut med hensyn til antall kolonier og deres avkastning, år for år og stat for stat. Er det en annen måte å se på korrelasjonen mellom disse to variablene?

## Dual-line Plots

Prøv et multiline-diagram ved å legge to linjediagrammer oppå hverandre, ved å bruke Seaborns 'despine' for å fjerne deres øvre og høyre ryggrad, og bruke `ax.twinx` [avledet fra Matplotlib](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.twinx.html). Twinx lar et diagram dele x-aksen og vise to y-akser. Så, vis avkastning per koloni og antall kolonier, lagt oppå hverandre:

```python
fig, ax = plt.subplots(figsize=(12,6))
lineplot = sns.lineplot(x=honey['year'], y=honey['numcol'], data=honey, 
                        label = 'Number of bee colonies', legend=False)
sns.despine()
plt.ylabel('# colonies')
plt.title('Honey Production Year over Year');

ax2 = ax.twinx()
lineplot2 = sns.lineplot(x=honey['year'], y=honey['yieldpercol'], ax=ax2, color="r", 
                         label ='Yield per colony', legend=False) 
sns.despine(right=False)
plt.ylabel('colony yield')
ax.figure.legend();
```
![superimposed plots](../../../../translated_images/dual-line.a4c28ce659603fab2c003f4df816733df2bf41d1facb7de27989ec9afbf01b33.no.png)

Selv om ingenting skiller seg ut rundt året 2003, lar det oss avslutte denne leksjonen på en litt gladere tone: selv om det generelt er et synkende antall kolonier, stabiliserer antallet kolonier seg, selv om deres avkastning per koloni synker.

Heia, bier, heia!

🐝❤️
## 🚀 Utfordring

I denne leksjonen lærte du litt mer om andre bruksområder for scatterplots og linjediagrammer, inkludert facet grids. Utfordre deg selv til å lage et facet grid ved å bruke et annet datasett, kanskje et du brukte tidligere i disse leksjonene. Legg merke til hvor lang tid det tar å lage dem og hvordan du må være forsiktig med hvor mange grids du trenger å tegne ved bruk av disse teknikkene.

## [Quiz etter leksjonen](https://ff-quizzes.netlify.app/en/ds/)

## Gjennomgang & Selvstudium

Linjediagrammer kan være enkle eller ganske komplekse. Les litt i [Seaborns dokumentasjon](https://seaborn.pydata.org/generated/seaborn.lineplot.html) om de ulike måtene du kan bygge dem på. Prøv å forbedre linjediagrammene du bygde i denne leksjonen med andre metoder som er oppført i dokumentasjonen.
## Oppgave

[Dykk inn i bikuben](assignment.md)

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.