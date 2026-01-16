<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a33c5d4b4156a2b41788d8720b6f724c",
  "translation_date": "2025-08-26T23:01:28+00:00",
  "source_file": "3-Data-Visualization/R/12-visualization-relationships/README.md",
  "language_code": "sv"
}
-->
# Visualisera relationer: Allt om honung 🍯

|![ Sketchnote av [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/12-Visualizing-Relationships.png)|
|:---:|
|Visualisera relationer - _Sketchnote av [@nitya](https://twitter.com/nitya)_ |

Fortsätt med naturfokuset i vår forskning och upptäck intressanta visualiseringar för att visa relationerna mellan olika typer av honung, baserat på en dataset från [United States Department of Agriculture](https://www.nass.usda.gov/About_NASS/index.php).

Denna dataset med cirka 600 poster visar honungsproduktion i många amerikanska delstater. Du kan till exempel se antalet kolonier, avkastning per koloni, total produktion, lager, pris per pund och värdet av den producerade honungen i en given delstat från 1998-2012, med en rad per år för varje delstat.

Det kan vara intressant att visualisera relationen mellan en given delstats produktion per år och till exempel priset på honung i den delstaten. Alternativt kan du visualisera relationen mellan delstaters honungsavkastning per koloni. Denna tidsperiod täcker den förödande 'CCD' eller 'Colony Collapse Disorder' som först observerades 2006 (http://npic.orst.edu/envir/ccd.html), vilket gör det till en gripande dataset att studera. 🐝

## [Quiz före lektionen](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/22)

I denna lektion kan du använda ggplot2, som du har använt tidigare, som ett bra bibliotek för att visualisera relationer mellan variabler. Särskilt intressant är användningen av ggplot2:s `geom_point` och `qplot`-funktion som möjliggör spridningsdiagram och linjediagram för att snabbt visualisera '[statistiska relationer](https://ggplot2.tidyverse.org/)', vilket hjälper dataforskaren att bättre förstå hur variabler relaterar till varandra.

## Spridningsdiagram

Använd ett spridningsdiagram för att visa hur priset på honung har utvecklats år för år, per delstat. ggplot2, med hjälp av `ggplot` och `geom_point`, grupperar bekvämt delstatsdata och visar datapunkter för både kategoriska och numeriska data.

Låt oss börja med att importera data och Seaborn:

```r
honey=read.csv('../../data/honey.csv')
head(honey)
```
Du märker att honungsdatan har flera intressanta kolumner, inklusive år och pris per pund. Låt oss utforska denna data, grupperad efter amerikansk delstat:

| state | numcol | yieldpercol | totalprod | stocks   | priceperlb | prodvalue | year |
| ----- | ------ | ----------- | --------- | -------- | ---------- | --------- | ---- |
| AL    | 16000  | 71          | 1136000   | 159000   | 0.72       | 818000    | 1998 |
| AZ    | 55000  | 60          | 3300000   | 1485000  | 0.64       | 2112000   | 1998 |
| AR    | 53000  | 65          | 3445000   | 1688000  | 0.59       | 2033000   | 1998 |
| CA    | 450000 | 83          | 37350000  | 12326000 | 0.62       | 23157000  | 1998 |
| CO    | 27000  | 72          | 1944000   | 1594000  | 0.7        | 1361000   | 1998 |
| FL    | 230000 | 98          |22540000   | 4508000  | 0.64       | 14426000  | 1998 |

Skapa ett grundläggande spridningsdiagram för att visa relationen mellan priset per pund honung och dess ursprungsdelstat i USA. Gör `y`-axeln tillräckligt hög för att visa alla delstater:

```r
library(ggplot2)
ggplot(honey, aes(x = priceperlb, y = state)) +
  geom_point(colour = "blue")
```
![spridningsdiagram 1](../../../../../translated_images/sv/scatter1.86b8900674d88b26dd3353a83fe604e9ab3722c4680cc40ee9beb452ff02cdea.png)

Visa nu samma data med ett honungsfärgschema för att visa hur priset utvecklas över åren. Du kan göra detta genom att lägga till en 'scale_color_gradientn'-parameter för att visa förändringen år för år:

> ✅ Läs mer om [scale_color_gradientn](https://www.rdocumentation.org/packages/ggplot2/versions/0.9.1/topics/scale_colour_gradientn) - prova ett vackert regnbågsfärgschema!

```r
ggplot(honey, aes(x = priceperlb, y = state, color=year)) +
  geom_point()+scale_color_gradientn(colours = colorspace::heat_hcl(7))
```
![spridningsdiagram 2](../../../../../translated_images/sv/scatter2.4d1cbc693bad20e2b563888747eb6bdf65b73ce449d903f7cd4068a78502dcff.png)

Med denna färgschemaändring kan du tydligt se en stark utveckling över åren när det gäller honungspriset per pund. Om du tittar på ett urval av data för att verifiera (välj en given delstat, till exempel Arizona) kan du se ett mönster av prisökningar år för år, med få undantag:

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

Ett annat sätt att visualisera denna utveckling är att använda storlek istället för färg. För färgblinda användare kan detta vara ett bättre alternativ. Redigera din visualisering för att visa en ökning av priset genom en ökning av punktens omkrets:

```r
ggplot(honey, aes(x = priceperlb, y = state)) +
  geom_point(aes(size = year),colour = "blue") +
  scale_size_continuous(range = c(0.25, 3))
```
Du kan se att storleken på punkterna gradvis ökar.

![spridningsdiagram 3](../../../../../translated_images/sv/scatter3.722d21e6f20b3ea2e18339bb9b10d75906126715eb7d5fdc88fe74dcb6d7066a.png)

Är detta ett enkelt fall av utbud och efterfrågan? På grund av faktorer som klimatförändringar och kolonikollaps, finns det mindre honung tillgänglig för köp år för år, och därmed ökar priset?

För att upptäcka en korrelation mellan några av variablerna i denna dataset, låt oss utforska några linjediagram.

## Linjediagram

Fråga: Finns det en tydlig ökning av priset på honung per pund år för år? Du kan enklast upptäcka detta genom att skapa ett enda linjediagram:

```r
qplot(honey$year,honey$priceperlb, geom='smooth', span =0.5, xlab = "year",ylab = "priceperlb")
```
Svar: Ja, med vissa undantag runt år 2003:

![linjediagram 1](../../../../../translated_images/sv/line1.299b576fbb2a59e60a59e7130030f59836891f90302be084e4e8d14da0562e2a.png)

Fråga: Kan vi också se en topp i honungstillgången år 2003? Vad händer om du tittar på total produktion år för år?

```python
qplot(honey$year,honey$totalprod, geom='smooth', span =0.5, xlab = "year",ylab = "totalprod")
```

![linjediagram 2](../../../../../translated_images/sv/line2.3b18fcda7176ceba5b6689eaaabb817d49c965e986f11cac1ae3f424030c34d8.png)

Svar: Inte riktigt. Om du tittar på total produktion verkar det faktiskt ha ökat det året, även om mängden honung som produceras generellt sett minskar under dessa år.

Fråga: I så fall, vad kan ha orsakat den prisökningen på honung runt år 2003?

För att upptäcka detta kan du utforska ett facet grid.

## Facet grids

Facet grids tar en aspekt av din dataset (i vårt fall kan du välja 'år' för att undvika att skapa för många facetter). Seaborn kan sedan skapa en plot för varje av dessa facetter av dina valda x- och y-koordinater för enklare visuell jämförelse. Sticker år 2003 ut i denna typ av jämförelse?

Skapa ett facet grid genom att använda `facet_wrap` som rekommenderas av [ggplot2:s dokumentation](https://ggplot2.tidyverse.org/reference/facet_wrap.html).

```r
ggplot(honey, aes(x=yieldpercol, y = numcol,group = 1)) + 
  geom_line() + facet_wrap(vars(year))
```
I denna visualisering kan du jämföra avkastning per koloni och antal kolonier år för år, sida vid sida med en wrap inställd på 3 för kolumnerna:

![facet grid](../../../../../translated_images/sv/facet.491ad90d61c2a7cc69b50c929f80786c749e38217ccedbf1e22ed8909b65987c.png)

För denna dataset sticker inget särskilt ut när det gäller antalet kolonier och deras avkastning, år för år och delstat för delstat. Finns det ett annat sätt att hitta en korrelation mellan dessa två variabler?

## Dubbel-linjediagram

Prova ett flerlinjediagram genom att lägga två linjediagram ovanpå varandra, med hjälp av R:s `par` och `plot`-funktion. Vi kommer att plotta året på x-axeln och visa två y-axlar. Visa avkastning per koloni och antal kolonier, överlagrade:

```r
par(mar = c(5, 4, 4, 4) + 0.3)              
plot(honey$year, honey$numcol, pch = 16, col = 2,type="l")              
par(new = TRUE)                             
plot(honey$year, honey$yieldpercol, pch = 17, col = 3,              
     axes = FALSE, xlab = "", ylab = "",type="l")
axis(side = 4, at = pretty(range(y2)))      
mtext("colony yield", side = 4, line = 3)   
```
![överlagrade diagram](../../../../../translated_images/sv/dual-line.fc4665f360a54018d7df9bc6abcc26460112e17dcbda18d3b9ae6109b32b36c3.png)

Även om inget sticker ut runt år 2003, låter det oss avsluta denna lektion med en lite gladare ton: även om det totalt sett är ett minskande antal kolonier, stabiliseras antalet kolonier även om deras avkastning per koloni minskar.

Heja bina, heja!

🐝❤️
## 🚀 Utmaning

I denna lektion lärde du dig lite mer om andra användningar av spridningsdiagram och linjediagram, inklusive facet grids. Utmana dig själv att skapa ett facet grid med en annan dataset, kanske en du använde tidigare i dessa lektioner. Notera hur lång tid det tar att skapa och hur du behöver vara försiktig med hur många grids du behöver rita med dessa tekniker.
## [Quiz efter lektionen](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/23)

## Granskning & Självstudier

Linjediagram kan vara enkla eller ganska komplexa. Läs lite i [ggplot2-dokumentationen](https://ggplot2.tidyverse.org/reference/geom_path.html#:~:text=geom_line()%20connects%20them%20in,which%20cases%20are%20connected%20together) om de olika sätten du kan bygga dem. Försök att förbättra de linjediagram du byggde i denna lektion med andra metoder som listas i dokumentationen.
## Uppgift

[Dyk in i bikupan](assignment.md)

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.