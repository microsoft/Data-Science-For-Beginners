<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a49d78e32e280c410f04e5f2a2068e77",
  "translation_date": "2025-09-05T22:23:31+00:00",
  "source_file": "3-Data-Visualization/09-visualization-quantities/README.md",
  "language_code": "no"
}
-->
# Visualisering av Mengder

|![ Sketchnote av [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| Visualisering av Mengder - _Sketchnote av [@nitya](https://twitter.com/nitya)_ |

I denne leksjonen skal du utforske hvordan du kan bruke et av de mange tilgjengelige Python-bibliotekene for å lære å lage interessante visualiseringer rundt konseptet mengde. Ved å bruke et renset datasett om fugler i Minnesota, kan du lære mange interessante fakta om det lokale dyrelivet.  
## [Quiz før leksjonen](https://ff-quizzes.netlify.app/en/ds/quiz/16)

## Observer vingespenn med Matplotlib

Et utmerket bibliotek for å lage både enkle og avanserte diagrammer og grafer av ulike slag er [Matplotlib](https://matplotlib.org/stable/index.html). Generelt sett innebærer prosessen med å plotte data ved hjelp av disse bibliotekene å identifisere hvilke deler av dataframen du vil fokusere på, utføre nødvendige transformasjoner på dataene, tilordne verdier til x- og y-aksene, bestemme hvilken type diagram som skal vises, og deretter vise diagrammet. Matplotlib tilbyr et stort utvalg av visualiseringer, men i denne leksjonen skal vi fokusere på de som er mest egnet for å visualisere mengder: linjediagrammer, spredningsdiagrammer og stolpediagrammer.

> ✅ Bruk det diagrammet som passer best til datastrukturen og historien du vil fortelle.  
> - For å analysere trender over tid: linje  
> - For å sammenligne verdier: stolpe, kolonne, kakediagram, spredningsdiagram  
> - For å vise hvordan deler forholder seg til helheten: kakediagram  
> - For å vise fordeling av data: spredningsdiagram, stolpe  
> - For å vise trender: linje, kolonne  
> - For å vise relasjoner mellom verdier: linje, spredningsdiagram, boblediagram  

Hvis du har et datasett og trenger å finne ut hvor mye av en gitt vare som er inkludert, vil en av de første oppgavene dine være å inspisere verdiene.

✅ Det finnes veldig gode "jukseark" for Matplotlib [her](https://matplotlib.org/cheatsheets/cheatsheets.pdf).

## Lag et linjediagram over vingespennverdier for fugler

Åpne `notebook.ipynb`-filen i roten av denne leksjonsmappen og legg til en celle.

> Merk: Dataene er lagret i roten av dette repoet i `/data`-mappen.

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```  
Disse dataene er en blanding av tekst og tall:

|      | Navn                         | VitenskapeligNavn      | Kategori              | Orden        | Familie  | Slekt       | Bevaringsstatus     | MinLengde | MaksLengde | MinKroppsmasse | MaksKroppsmasse | MinVingespenn | MaksVingespenn |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ------------: | ------------: | ------------: | ------------: |
|    0 | Svartbukfløyteand            | Dendrocygna autumnalis | Ender/Gjess/Vannfugler | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |           652 |          1020 |            76 |            94 |
|    1 | Brunfløyteand                | Dendrocygna bicolor    | Ender/Gjess/Vannfugler | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |           712 |          1050 |            85 |            93 |
|    2 | Snøgås                       | Anser caerulescens     | Ender/Gjess/Vannfugler | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |          2050 |          4050 |           135 |           165 |
|    3 | Rossgås                      | Anser rossii           | Ender/Gjess/Vannfugler | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |          1066 |          1567 |           113 |           116 |
|    4 | Tundragås                    | Anser albifrons        | Ender/Gjess/Vannfugler | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |          1930 |          3310 |           130 |           165 |

La oss starte med å plotte noen av de numeriske dataene ved hjelp av et grunnleggende linjediagram. Anta at du ønsker en oversikt over det maksimale vingespennet for disse interessante fuglene.

```python
wingspan = birds['MaxWingspan'] 
wingspan.plot()
```  
![Maks Vingespenn](../../../../3-Data-Visualization/09-visualization-quantities/images/max-wingspan-02.png)

Hva legger du merke til med en gang? Det ser ut til å være minst én uteligger – det er et ganske stort vingespenn! Et vingespenn på 2300 centimeter tilsvarer 23 meter – er det Pterodaktyler som flyr rundt i Minnesota? La oss undersøke.

Selv om du raskt kunne sortert i Excel for å finne disse uteliggerne, som sannsynligvis er skrivefeil, fortsett visualiseringsprosessen ved å jobbe fra diagrammet.

Legg til etiketter på x-aksen for å vise hvilke fugler det er snakk om:

```
plt.title('Max Wingspan in Centimeters')
plt.ylabel('Wingspan (CM)')
plt.xlabel('Birds')
plt.xticks(rotation=45)
x = birds['Name'] 
y = birds['MaxWingspan']

plt.plot(x, y)

plt.show()
```  
![vingespenn med etiketter](../../../../3-Data-Visualization/09-visualization-quantities/images/max-wingspan-labels-02.png)

Selv med rotasjonen av etikettene satt til 45 grader, er det for mange til å lese. La oss prøve en annen strategi: merk bare uteliggerne og sett etikettene i diagrammet. Du kan bruke et spredningsdiagram for å få mer plass til merkingen:

```python
plt.title('Max Wingspan in Centimeters')
plt.ylabel('Wingspan (CM)')
plt.tick_params(axis='both',which='both',labelbottom=False,bottom=False)

for i in range(len(birds)):
    x = birds['Name'][i]
    y = birds['MaxWingspan'][i]
    plt.plot(x, y, 'bo')
    if birds['MaxWingspan'][i] > 500:
        plt.text(x, y * (1 - 0.05), birds['Name'][i], fontsize=12)
    
plt.show()
```  
Hva skjer her? Du brukte `tick_params` for å skjule etikettene nederst og opprettet deretter en løkke over fugledatasettet ditt. Ved å plotte diagrammet med små runde blå prikker ved hjelp av `bo`, sjekket du etter fugler med et maksimalt vingespenn over 500 og viste etiketten deres ved siden av prikken hvis det var tilfelle. Du forskjøv etikettene litt på y-aksen (`y * (1 - 0.05)`) og brukte fuglenavnet som etikett.

Hva oppdaget du?

![uteliggerne](../../../../3-Data-Visualization/09-visualization-quantities/images/labeled-wingspan-02.png)  
## Filtrer dataene dine

Både Hvitthodeørn og Præriefalk, som sannsynligvis er veldig store fugler, ser ut til å være feilmerket, med en ekstra `0` lagt til deres maksimale vingespenn. Det er usannsynlig at du møter en Hvitthodeørn med et vingespenn på 25 meter, men hvis du gjør det, gi oss beskjed! La oss lage en ny dataframe uten disse to uteliggerne:

```python
plt.title('Max Wingspan in Centimeters')
plt.ylabel('Wingspan (CM)')
plt.xlabel('Birds')
plt.tick_params(axis='both',which='both',labelbottom=False,bottom=False)
for i in range(len(birds)):
    x = birds['Name'][i]
    y = birds['MaxWingspan'][i]
    if birds['Name'][i] not in ['Bald eagle', 'Prairie falcon']:
        plt.plot(x, y, 'bo')
plt.show()
```  

Ved å filtrere ut uteliggerne er dataene dine nå mer sammenhengende og forståelige.

![spredningsdiagram av vingespenn](../../../../3-Data-Visualization/09-visualization-quantities/images/scatterplot-wingspan-02.png)

Nå som vi har et renere datasett, i det minste når det gjelder vingespenn, la oss oppdage mer om disse fuglene.

Mens linje- og spredningsdiagrammer kan vise informasjon om dataverdier og deres fordeling, ønsker vi å tenke på verdiene som ligger i dette datasettet. Du kan lage visualiseringer for å svare på følgende spørsmål om mengder:

> Hvor mange kategorier av fugler finnes det, og hva er antallet deres?  
> Hvor mange fugler er utryddet, truet, sjeldne eller vanlige?  
> Hvor mange finnes det av de ulike slektene og ordenene i Linnés terminologi?  
## Utforsk stolpediagrammer

Stolpediagrammer er praktiske når du trenger å vise grupperinger av data. La oss utforske kategoriene av fugler som finnes i dette datasettet for å se hvilken som er den vanligste.

I notebook-filen, lag et grunnleggende stolpediagram.

✅ Merk, du kan enten filtrere ut de to uteliggerfuglene vi identifiserte i forrige seksjon, rette skrivefeilen i vingespennet deres, eller la dem være med for disse øvelsene som ikke avhenger av vingespennverdier.

Hvis du vil lage et stolpediagram, kan du velge dataene du vil fokusere på. Stolpediagrammer kan lages fra rådata:

```python
birds.plot(x='Category',
        kind='bar',
        stacked=True,
        title='Birds of Minnesota')

```  
![full data som stolpediagram](../../../../3-Data-Visualization/09-visualization-quantities/images/full-data-bar-02.png)

Dette stolpediagrammet er imidlertid uleselig fordi det er for mye ugruppert data. Du må velge bare dataene du vil plotte, så la oss se på lengden av fugler basert på deres kategori.

Filtrer dataene dine til å inkludere bare fuglens kategori.

✅ Legg merke til at du bruker Pandas for å håndtere dataene, og deretter lar Matplotlib lage diagrammet.

Siden det er mange kategorier, kan du vise dette diagrammet vertikalt og justere høyden for å ta hensyn til alle dataene:

```python
category_count = birds.value_counts(birds['Category'].values, sort=True)
plt.rcParams['figure.figsize'] = [6, 12]
category_count.plot.barh()
```  
![kategori og lengde](../../../../3-Data-Visualization/09-visualization-quantities/images/category-counts-02.png)

Dette stolpediagrammet gir en god oversikt over antall fugler i hver kategori. Med et øyekast ser du at det største antallet fugler i denne regionen tilhører kategorien Ender/Gjess/Vannfugler. Minnesota er tross alt "landet med 10 000 innsjøer", så dette er ikke overraskende!

✅ Prøv noen andre tellinger på dette datasettet. Er det noe som overrasker deg?

## Sammenligne data

Du kan prøve ulike sammenligninger av grupperte data ved å lage nye akser. Prøv en sammenligning av MaksLengde for en fugl, basert på dens kategori:

```python
maxlength = birds['MaxLength']
plt.barh(y=birds['Category'], width=maxlength)
plt.rcParams['figure.figsize'] = [6, 12]
plt.show()
```  
![sammenligne data](../../../../3-Data-Visualization/09-visualization-quantities/images/category-length-02.png)

Ingenting er overraskende her: kolibrier har minst MaksLengde sammenlignet med Pelikaner eller Gjess. Det er bra når data gir logisk mening!

Du kan lage mer interessante visualiseringer av stolpediagrammer ved å legge data oppå hverandre. La oss legge Minimum og Maksimum Lengde oppå hverandre for en gitt fuglekategori:

```python
minLength = birds['MinLength']
maxLength = birds['MaxLength']
category = birds['Category']

plt.barh(category, maxLength)
plt.barh(category, minLength)

plt.show()
```  
I dette diagrammet kan du se området per fuglekategori for Minimum Lengde og Maksimum Lengde. Du kan trygt si at, gitt disse dataene, jo større fuglen er, desto større er lengdeområdet dens. Fascinerende!

![overlappende verdier](../../../../3-Data-Visualization/09-visualization-quantities/images/superimposed-02.png)

## 🚀 Utfordring

Dette fugledatasettet tilbyr en mengde informasjon om ulike typer fugler innenfor et bestemt økosystem. Søk rundt på internett og se om du kan finne andre fugleorienterte datasett. Øv deg på å lage diagrammer og grafer rundt disse fuglene for å oppdage fakta du ikke visste.

## [Quiz etter leksjonen](https://ff-quizzes.netlify.app/en/ds/quiz/17)

## Gjennomgang og Selvstudium

Denne første leksjonen har gitt deg noe informasjon om hvordan du kan bruke Matplotlib til å visualisere mengder. Gjør litt research rundt andre måter å jobbe med datasett for visualisering. [Plotly](https://github.com/plotly/plotly.py) er et verktøy vi ikke dekker i disse leksjonene, så ta en titt på hva det kan tilby.  
## Oppgave

[Linjer, Spredning og Stolper](assignment.md)  

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.