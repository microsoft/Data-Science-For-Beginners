<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a33c5d4b4156a2b41788d8720b6f724c",
  "translation_date": "2025-08-26T23:01:58+00:00",
  "source_file": "3-Data-Visualization/R/12-visualization-relationships/README.md",
  "language_code": "da"
}
-->
# Visualisering af relationer: Alt om honning 🍯

|![ Sketchnote af [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/12-Visualizing-Relationships.png)|
|:---:|
|Visualisering af relationer - _Sketchnote af [@nitya](https://twitter.com/nitya)_ |

Med fokus på naturen i vores forskning, lad os udforske interessante visualiseringer, der viser relationerne mellem forskellige typer honning, baseret på et datasæt fra [United States Department of Agriculture](https://www.nass.usda.gov/About_NASS/index.php).

Dette datasæt med omkring 600 poster viser honningproduktion i mange amerikanske stater. For eksempel kan du se på antallet af kolonier, udbytte pr. koloni, total produktion, lagre, pris pr. pund og værdien af den producerede honning i en given stat fra 1998-2012, med én række pr. år for hver stat.

Det vil være interessant at visualisere relationen mellem en given stats produktion pr. år og f.eks. prisen på honning i den stat. Alternativt kunne du visualisere relationen mellem staters honningudbytte pr. koloni. Denne tidsperiode dækker den ødelæggende 'CCD' eller 'Colony Collapse Disorder', som først blev observeret i 2006 (http://npic.orst.edu/envir/ccd.html), så det er et tankevækkende datasæt at studere. 🐝

## [Quiz før lektionen](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/22)

I denne lektion kan du bruge ggplot2, som du har brugt før, som et godt bibliotek til at visualisere relationer mellem variabler. Særligt interessant er brugen af ggplot2's `geom_point` og `qplot` funktion, der tillader scatterplots og linjediagrammer til hurtigt at visualisere '[statistiske relationer](https://ggplot2.tidyverse.org/)', hvilket giver dataforskeren en bedre forståelse af, hvordan variabler relaterer til hinanden.

## Scatterplots

Brug et scatterplot til at vise, hvordan prisen på honning har udviklet sig år for år pr. stat. ggplot2, ved brug af `ggplot` og `geom_point`, grupperer bekvemt data fra staterne og viser datapunkter for både kategoriske og numeriske data.

Lad os starte med at importere data og Seaborn:

```r
honey=read.csv('../../data/honey.csv')
head(honey)
```
Du bemærker, at honningdataene har flere interessante kolonner, inklusive år og pris pr. pund. Lad os udforske disse data, grupperet efter amerikanske stater:

| stat | numcol | yieldpercol | totalprod | stocks   | priceperlb | prodvalue | år   |
| ---- | ------ | ----------- | --------- | -------- | ---------- | --------- | ---- |
| AL   | 16000  | 71          | 1136000   | 159000   | 0.72       | 818000    | 1998 |
| AZ   | 55000  | 60          | 3300000   | 1485000  | 0.64       | 2112000   | 1998 |
| AR   | 53000  | 65          | 3445000   | 1688000  | 0.59       | 2033000   | 1998 |
| CA   | 450000 | 83          | 37350000  | 12326000 | 0.62       | 23157000  | 1998 |
| CO   | 27000  | 72          | 1944000   | 1594000  | 0.7        | 1361000   | 1998 |
| FL   | 230000 | 98          |22540000   | 4508000  | 0.64       | 14426000  | 1998 |

Lav et grundlæggende scatterplot for at vise relationen mellem prisen pr. pund honning og dens oprindelsesstat i USA. Gør `y`-aksen høj nok til at vise alle staterne:

```r
library(ggplot2)
ggplot(honey, aes(x = priceperlb, y = state)) +
  geom_point(colour = "blue")
```
![scatterplot 1](../../../../../translated_images/da/scatter1.86b8900674d88b26dd3353a83fe604e9ab3722c4680cc40ee9beb452ff02cdea.png)

Vis nu de samme data med et honningfarvetema for at vise, hvordan prisen udvikler sig over årene. Du kan gøre dette ved at tilføje en 'scale_color_gradientn'-parameter for at vise ændringen år for år:

> ✅ Lær mere om [scale_color_gradientn](https://www.rdocumentation.org/packages/ggplot2/versions/0.9.1/topics/scale_colour_gradientn) - prøv et smukt regnbuefarvetema!

```r
ggplot(honey, aes(x = priceperlb, y = state, color=year)) +
  geom_point()+scale_color_gradientn(colours = colorspace::heat_hcl(7))
```
![scatterplot 2](../../../../../translated_images/da/scatter2.4d1cbc693bad20e2b563888747eb6bdf65b73ce449d903f7cd4068a78502dcff.png)

Med denne farveskemaændring kan du se, at der tydeligvis er en stærk progression over årene i forhold til honningprisen pr. pund. Faktisk, hvis du ser på et eksempel fra datasættet for at verificere (vælg en given stat, f.eks. Arizona), kan du se et mønster af prisstigninger år for år, med få undtagelser:

| stat | numcol | yieldpercol | totalprod | stocks  | priceperlb | prodvalue | år   |
| ---- | ------ | ----------- | --------- | ------- | ---------- | --------- | ---- |
| AZ   | 55000  | 60          | 3300000   | 1485000 | 0.64       | 2112000   | 1998 |
| AZ   | 52000  | 62          | 3224000   | 1548000 | 0.62       | 1999000   | 1999 |
| AZ   | 40000  | 59          | 2360000   | 1322000 | 0.73       | 1723000   | 2000 |
| AZ   | 43000  | 59          | 2537000   | 1142000 | 0.72       | 1827000   | 2001 |
| AZ   | 38000  | 63          | 2394000   | 1197000 | 1.08       | 2586000   | 2002 |
| AZ   | 35000  | 72          | 2520000   | 983000  | 1.34       | 3377000   | 2003 |
| AZ   | 32000  | 55          | 1760000   | 774000  | 1.11       | 1954000   | 2004 |
| AZ   | 36000  | 50          | 1800000   | 720000  | 1.04       | 1872000   | 2005 |
| AZ   | 30000  | 65          | 1950000   | 839000  | 0.91       | 1775000   | 2006 |
| AZ   | 30000  | 64          | 1920000   | 902000  | 1.26       | 2419000   | 2007 |
| AZ   | 25000  | 64          | 1600000   | 336000  | 1.26       | 2016000   | 2008 |
| AZ   | 20000  | 52          | 1040000   | 562000  | 1.45       | 1508000   | 2009 |
| AZ   | 24000  | 77          | 1848000   | 665000  | 1.52       | 2809000   | 2010 |
| AZ   | 23000  | 53          | 1219000   | 427000  | 1.55       | 1889000   | 2011 |
| AZ   | 22000  | 46          | 1012000   | 253000  | 1.79       | 1811000   | 2012 |

En anden måde at visualisere denne progression på er at bruge størrelse i stedet for farve. For farveblinde brugere kan dette være en bedre mulighed. Rediger din visualisering for at vise en stigning i prisen ved en stigning i prikstørrelse:

```r
ggplot(honey, aes(x = priceperlb, y = state)) +
  geom_point(aes(size = year),colour = "blue") +
  scale_size_continuous(range = c(0.25, 3))
```
Du kan se, at prikkerne gradvist bliver større.

![scatterplot 3](../../../../../translated_images/da/scatter3.722d21e6f20b3ea2e18339bb9b10d75906126715eb7d5fdc88fe74dcb6d7066a.png)

Er dette et simpelt tilfælde af udbud og efterspørgsel? På grund af faktorer som klimaforandringer og kolonikollaps, er der mindre honning tilgængelig for køb år for år, og derfor stiger prisen?

For at finde en korrelation mellem nogle af variablerne i dette datasæt, lad os udforske nogle linjediagrammer.

## Linjediagrammer

Spørgsmål: Er der en klar stigning i prisen på honning pr. pund år for år? Du kan nemmest opdage det ved at lave et enkelt linjediagram:

```r
qplot(honey$year,honey$priceperlb, geom='smooth', span =0.5, xlab = "year",ylab = "priceperlb")
```
Svar: Ja, med nogle undtagelser omkring året 2003:

![line chart 1](../../../../../translated_images/da/line1.299b576fbb2a59e60a59e7130030f59836891f90302be084e4e8d14da0562e2a.png)

Spørgsmål: Nå, i 2003 kan vi også se en stigning i honningforsyningen? Hvad hvis du ser på den totale produktion år for år?

```python
qplot(honey$year,honey$totalprod, geom='smooth', span =0.5, xlab = "year",ylab = "totalprod")
```

![line chart 2](../../../../../translated_images/da/line2.3b18fcda7176ceba5b6689eaaabb817d49c965e986f11cac1ae3f424030c34d8.png)

Svar: Ikke rigtig. Hvis du ser på den totale produktion, ser det faktisk ud til at være steget i det pågældende år, selvom mængden af produceret honning generelt er faldende i disse år.

Spørgsmål: I så fald, hvad kunne have forårsaget den stigning i prisen på honning omkring 2003?

For at finde ud af dette kan du udforske et facet grid.

## Facet grids

Facet grids tager én facet af dit datasæt (i vores tilfælde kan du vælge 'år' for at undgå at få for mange facetter). Seaborn kan derefter lave et plot for hver af disse facetter af dine valgte x- og y-koordinater for lettere visuel sammenligning. Skiller 2003 sig ud i denne type sammenligning?

Lav et facet grid ved at bruge `facet_wrap` som anbefalet af [ggplot2's dokumentation](https://ggplot2.tidyverse.org/reference/facet_wrap.html).

```r
ggplot(honey, aes(x=yieldpercol, y = numcol,group = 1)) + 
  geom_line() + facet_wrap(vars(year))
```
I denne visualisering kan du sammenligne udbytte pr. koloni og antal kolonier år for år, side om side med en wrap sat til 3 for kolonnerne:

![facet grid](../../../../../translated_images/da/facet.491ad90d61c2a7cc69b50c929f80786c749e38217ccedbf1e22ed8909b65987c.png)

For dette datasæt skiller intet sig særligt ud med hensyn til antallet af kolonier og deres udbytte år for år og stat for stat. Er der en anden måde at finde en korrelation mellem disse to variabler?

## Dual-line plots

Prøv et multiline plot ved at overlejre to linjediagrammer oven på hinanden, ved brug af R's `par` og `plot` funktion. Vi vil plotte året på x-aksen og vise to y-akser. Så vis udbytte pr. koloni og antal kolonier, overlejret:

```r
par(mar = c(5, 4, 4, 4) + 0.3)              
plot(honey$year, honey$numcol, pch = 16, col = 2,type="l")              
par(new = TRUE)                             
plot(honey$year, honey$yieldpercol, pch = 17, col = 3,              
     axes = FALSE, xlab = "", ylab = "",type="l")
axis(side = 4, at = pretty(range(y2)))      
mtext("colony yield", side = 4, line = 3)   
```
![superimposed plots](../../../../../translated_images/da/dual-line.fc4665f360a54018d7df9bc6abcc26460112e17dcbda18d3b9ae6109b32b36c3.png)

Mens intet springer i øjnene omkring året 2003, giver det os mulighed for at afslutte denne lektion på en lidt gladere note: selvom der generelt er et faldende antal kolonier, stabiliserer antallet af kolonier sig, selvom deres udbytte pr. koloni falder.

Kom så, bier, kom så!

🐝❤️
## 🚀 Udfordring

I denne lektion lærte du lidt mere om andre anvendelser af scatterplots og linjediagrammer, inklusive facet grids. Udfordr dig selv til at lave et facet grid ved brug af et andet datasæt, måske et du brugte tidligere i disse lektioner. Bemærk, hvor lang tid det tager at lave, og hvordan du skal være forsigtig med, hvor mange grids du skal tegne ved brug af disse teknikker.
## [Quiz efter lektionen](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/23)

## Gennemgang & Selvstudie

Linjediagrammer kan være simple eller ret komplekse. Læs lidt i [ggplot2 dokumentationen](https://ggplot2.tidyverse.org/reference/geom_path.html#:~:text=geom_line()%20connects%20them%20in,which%20cases%20are%20connected%20together) om de forskellige måder, du kan bygge dem på. Prøv at forbedre de linjediagrammer, du byggede i denne lektion, med andre metoder, der er nævnt i dokumentationen.
## Opgave

[Dyk ned i bikuben](assignment.md)

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.