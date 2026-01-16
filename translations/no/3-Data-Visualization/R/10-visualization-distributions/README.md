<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ea67c0c40808fd723594de6896c37ccf",
  "translation_date": "2025-08-26T22:58:11+00:00",
  "source_file": "3-Data-Visualization/R/10-visualization-distributions/README.md",
  "language_code": "no"
}
-->
# Visualisering av fordelinger

|![ Sketchnote av [(@sketchthedocs)](https://sketchthedocs.dev) ](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| Visualisering av fordelinger - _Sketchnote av [@nitya](https://twitter.com/nitya)_ |

I forrige leksjon lærte du noen interessante fakta om et datasett om fuglene i Minnesota. Du oppdaget feilaktige data ved å visualisere uteliggere og så på forskjellene mellom fuglekategorier basert på deres maksimale lengde.

## [Quiz før leksjonen](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/18)
## Utforsk fugledatasettet

En annen måte å grave i data på er ved å se på fordelingen, eller hvordan dataene er organisert langs en akse. Kanskje du for eksempel ønsker å lære om den generelle fordelingen i dette datasettet av maksimal vingespenn eller maksimal kroppsmasse for fuglene i Minnesota.

La oss oppdage noen fakta om fordelingen av data i dette datasettet. I din R-konsoll, importer `ggplot2` og databasen. Fjern uteliggere fra databasen slik som i forrige tema.

```r
library(ggplot2)

birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")

birds_filtered <- subset(birds, MaxWingspan < 500)
head(birds_filtered)
```
|      | Navn                        | VitenskapeligNavn      | Kategori              | Orden        | Familie  | Slekt       | Bevaringsstatus     | MinLengde | MaksLengde | MinKroppsmasse | MaksKroppsmasse | MinVingespenn | MaksVingespenn |
| ---: | :-------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ------------: | -------------: | ------------: | -------------: |
|    0 | Svartbukfløyteand           | Dendrocygna autumnalis | Ender/Gjess/Vannfugler | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |           652 |           1020 |            76 |            94 |
|    1 | Brunfløyteand               | Dendrocygna bicolor    | Ender/Gjess/Vannfugler | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |           712 |           1050 |            85 |            93 |
|    2 | Snøgås                      | Anser caerulescens     | Ender/Gjess/Vannfugler | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |          2050 |           4050 |           135 |           165 |
|    3 | Rossgås                     | Anser rossii           | Ender/Gjess/Vannfugler | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |          1066 |           1567 |           113 |           116 |
|    4 | Større hvitkinngås          | Anser albifrons        | Ender/Gjess/Vannfugler | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |          1930 |           3310 |           130 |           165 |

Generelt kan du raskt se hvordan data er fordelt ved å bruke et spredningsdiagram, slik vi gjorde i forrige leksjon:

```r
ggplot(data=birds_filtered, aes(x=Order, y=MaxLength,group=1)) +
  geom_point() +
  ggtitle("Max Length per order") + coord_flip()
```
![maks lengde per orden](../../../../../translated_images/no/max-length-per-order.e5b283d952c78c12b091307c5d3cf67132dad6fefe80a073353b9dc5c2bd3eb8.png)

Dette gir en oversikt over den generelle fordelingen av kroppslengde per fugleorden, men det er ikke den optimale måten å vise sanne fordelinger på. Den oppgaven håndteres vanligvis ved å lage et histogram.
## Arbeide med histogrammer

`ggplot2` tilbyr svært gode måter å visualisere datafordeling ved hjelp av histogrammer. Denne typen diagram ligner et stolpediagram hvor fordelingen kan sees gjennom stigning og fall av stolpene. For å lage et histogram trenger du numeriske data. For å lage et histogram kan du plotte et diagram og definere typen som 'hist' for histogram. Dette diagrammet viser fordelingen av MaksKroppsmasse for hele datasettets numeriske data. Ved å dele opp datasettet i mindre grupper kan det vise fordelingen av verdiene:

```r
ggplot(data = birds_filtered, aes(x = MaxBodyMass)) + 
  geom_histogram(bins=10)+ylab('Frequency')
```
![fordeling over hele datasettet](../../../../../translated_images/no/distribution-over-the-entire-dataset.d22afd3fa96be854e4c82213fedec9e3703cba753d07fad4606aadf58cf7e78e.png)

Som du kan se, faller de fleste av de 400+ fuglene i dette datasettet innenfor området under 2000 for deres Maks Kroppsmasse. Få mer innsikt i dataene ved å endre `bins`-parameteren til et høyere tall, for eksempel 30:

```r
ggplot(data = birds_filtered, aes(x = MaxBodyMass)) + geom_histogram(bins=30)+ylab('Frequency')
```

![fordeling-30bins](../../../../../translated_images/no/distribution-30bins.6a3921ea7a421bf71f06bf5231009e43d1146f1b8da8dc254e99b5779a4983e5.png)

Dette diagrammet viser fordelingen på en litt mer detaljert måte. Et diagram som er mindre skjevt mot venstre kan opprettes ved å sørge for at du bare velger data innenfor et gitt område:

Filtrer dataene dine for å få kun de fuglene som har kroppsmasse under 60, og vis 30 `bins`:

```r
birds_filtered_1 <- subset(birds_filtered, MaxBodyMass > 1 & MaxBodyMass < 60)
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_histogram(bins=30)+ylab('Frequency')
```

![filtrert histogram](../../../../../translated_images/no/filtered-histogram.6bf5d2bfd82533220e1bd4bc4f7d14308f43746ed66721d9ec8f460732be6674.png)

✅ Prøv noen andre filtre og datapunkter. For å se hele fordelingen av dataene, fjern `['MaxBodyMass']`-filteret for å vise merkede fordelinger.

Histogrammet tilbyr også noen fine farge- og merkeforbedringer å prøve:

Lag et 2D-histogram for å sammenligne forholdet mellom to fordelinger. La oss sammenligne `MaxBodyMass` vs. `MaxLength`. `ggplot2` tilbyr en innebygd måte å vise konvergens ved hjelp av lysere farger:

```r
ggplot(data=birds_filtered_1, aes(x=MaxBodyMass, y=MaxLength) ) +
  geom_bin2d() +scale_fill_continuous(type = "viridis")
```
Det ser ut til å være en forventet korrelasjon mellom disse to elementene langs en forventet akse, med ett spesielt sterkt punkt av konvergens:

![2d plot](../../../../../translated_images/no/2d-plot.c504786f439bd7ebceebf2465c70ca3b124103e06c7ff7214bf24e26f7aec21e.png)

Histogrammer fungerer godt som standard for numeriske data. Hva om du trenger å se fordelinger basert på tekstdata? 
## Utforsk datasettet for fordelinger ved hjelp av tekstdata 

Dette datasettet inkluderer også god informasjon om fuglekategori og dens slekt, art og familie, samt dens bevaringsstatus. La oss grave i denne bevaringsinformasjonen. Hva er fordelingen av fuglene i henhold til deres bevaringsstatus?

> ✅ I datasettet brukes flere forkortelser for å beskrive bevaringsstatus. Disse forkortelsene kommer fra [IUCN Red List Categories](https://www.iucnredlist.org/), en organisasjon som katalogiserer arters status.
> 
> - CR: Kritisk truet
> - EN: Truet
> - EX: Utdødd
> - LC: Livskraftig
> - NT: Nær truet
> - VU: Sårbar

Dette er tekstbaserte verdier, så du må gjøre en transformasjon for å lage et histogram. Bruk den filtrerteBirds-datarammen til å vise dens bevaringsstatus sammen med dens Minimum Vingespenn. Hva ser du? 

```r
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'EX'] <- 'x1' 
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'CR'] <- 'x2'
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'EN'] <- 'x3'
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'NT'] <- 'x4'
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'VU'] <- 'x5'
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'LC'] <- 'x6'

ggplot(data=birds_filtered_1, aes(x = MinWingspan, fill = ConservationStatus)) +
  geom_histogram(position = "identity", alpha = 0.4, bins = 20) +
  scale_fill_manual(name="Conservation Status",values=c("red","green","blue","pink"),labels=c("Endangered","Near Threathened","Vulnerable","Least Concern"))
```

![vingespenn og bevaringsstatus](../../../../../translated_images/no/wingspan-conservation-collation.4024e9aa6910866aa82f0c6cb6a6b4b925bd10079e6b0ef8f92eefa5a6792f76.png)

Det ser ikke ut til å være en god korrelasjon mellom minimum vingespenn og bevaringsstatus. Test andre elementer i datasettet ved hjelp av denne metoden. Du kan også prøve forskjellige filtre. Finner du noen korrelasjon?

## Tetthetsdiagrammer

Du har kanskje lagt merke til at histogrammene vi har sett på så langt er 'trappetrinnsformede' og ikke flyter jevnt i en bue. For å vise et jevnere tetthetsdiagram kan du prøve et tetthetsdiagram.

La oss jobbe med tetthetsdiagrammer nå!

```r
ggplot(data = birds_filtered_1, aes(x = MinWingspan)) + 
  geom_density()
```
![tetthetsdiagram](../../../../../translated_images/no/density-plot.675ccf865b76c690487fb7f69420a8444a3515f03bad5482886232d4330f5c85.png)

Du kan se hvordan diagrammet gjenspeiler det forrige for Minimum Vingespenn-data; det er bare litt jevnere. Hvis du ønsket å gå tilbake til den hakkete MaksKroppsmasse-linjen i det andre diagrammet du laget, kunne du jevne den ut veldig godt ved å gjenskape den ved hjelp av denne metoden:

```r
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_density()
```
![kroppsmasse tetthet](../../../../../translated_images/no/bodymass-smooth.d31ce526d82b0a1f19a073815dea28ecfbe58145ec5337e4ef7e8cdac81120b3.png)

Hvis du ønsket en jevn, men ikke for jevn linje, rediger `adjust`-parameteren: 

```r
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_density(adjust = 1/5)
```
![mindre jevn kroppsmasse](../../../../../translated_images/no/less-smooth-bodymass.10f4db8b683cc17d17b2d33f22405413142004467a1493d416608dafecfdee23.png)

✅ Les om parameterne som er tilgjengelige for denne typen diagram og eksperimenter!

Denne typen diagram tilbyr vakkert forklarende visualiseringer. Med noen få linjer kode kan du for eksempel vise maks kroppsmasse tetthet per fugleorden:

```r
ggplot(data=birds_filtered_1,aes(x = MaxBodyMass, fill = Order)) +
  geom_density(alpha=0.5)
```
![kroppsmasse per orden](../../../../../translated_images/no/bodymass-per-order.9d2b065dd931b928c839d8cdbee63067ab1ae52218a1b90717f4bc744354f485.png)

## 🚀 Utfordring

Histogrammer er en mer sofistikert type diagram enn grunnleggende spredningsdiagrammer, stolpediagrammer eller linjediagrammer. Gjør et søk på internett for å finne gode eksempler på bruk av histogrammer. Hvordan brukes de, hva viser de, og innen hvilke felt eller områder brukes de vanligvis?

## [Quiz etter leksjonen](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/19)

## Gjennomgang og selvstudium

I denne leksjonen brukte du `ggplot2` og begynte å jobbe med å vise mer sofistikerte diagrammer. Gjør litt research på `geom_density_2d()` en "kontinuerlig sannsynlighetstetthetskurve i en eller flere dimensjoner". Les gjennom [dokumentasjonen](https://ggplot2.tidyverse.org/reference/geom_density_2d.html) for å forstå hvordan det fungerer.

## Oppgave

[Bruk ferdighetene dine](assignment.md)

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.