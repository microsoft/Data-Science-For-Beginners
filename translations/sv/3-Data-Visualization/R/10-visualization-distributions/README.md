<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ea67c0c40808fd723594de6896c37ccf",
  "translation_date": "2025-08-26T22:57:19+00:00",
  "source_file": "3-Data-Visualization/R/10-visualization-distributions/README.md",
  "language_code": "sv"
}
-->
# Visualisera distributioner

|![ Sketchnote av [(@sketchthedocs)](https://sketchthedocs.dev) ](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| Visualisera distributioner - _Sketchnote av [@nitya](https://twitter.com/nitya)_ |

I den föregående lektionen lärde du dig några intressanta fakta om en dataset om fåglar i Minnesota. Du hittade felaktiga data genom att visualisera avvikare och tittade på skillnaderna mellan fågelkategorier baserat på deras maximala längd.

## [Quiz före föreläsningen](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/18)
## Utforska datasetet om fåglar

Ett annat sätt att gräva i data är att titta på dess distribution, eller hur datan är organiserad längs en axel. Kanske vill du till exempel lära dig om den generella distributionen, för detta dataset, av den maximala vingbredden eller den maximala kroppsmassan för fåglarna i Minnesota.

Låt oss upptäcka några fakta om distributionerna av data i detta dataset. I din R-konsol, importera `ggplot2` och databasen. Ta bort avvikare från databasen precis som i det föregående ämnet.

```r
library(ggplot2)

birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")

birds_filtered <- subset(birds, MaxWingspan < 500)
head(birds_filtered)
```
|      | Namn                         | VetenskapligtNamn      | Kategori              | Ordning      | Familj   | Släkte      | Bevarandestatus    | MinLängd  | MaxLängd  | MinKroppsmassa | MaxKroppsmassa | MinVingbredd | MaxVingbredd |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | -------------: | -------------: | -----------: | -----------: |
|    0 | Svartbukig visselanka         | Dendrocygna autumnalis | Änder/Gäss/Vattenfåglar | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |           652  |          1020  |          76  |          94  |
|    1 | Rödbrun visselanka            | Dendrocygna bicolor    | Änder/Gäss/Vattenfåglar | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |           712  |          1050  |          85  |          93  |
|    2 | Snögås                       | Anser caerulescens     | Änder/Gäss/Vattenfåglar | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |          2050  |          4050  |         135  |         165  |
|    3 | Ross' gås                    | Anser rossii           | Änder/Gäss/Vattenfåglar | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |          1066  |          1567  |         113  |         116  |
|    4 | Större vitkindad gås         | Anser albifrons        | Änder/Gäss/Vattenfåglar | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |          1930  |          3310  |         130  |         165  |

Generellt kan du snabbt se hur data är fördelad genom att använda ett spridningsdiagram, som vi gjorde i den föregående lektionen:

```r
ggplot(data=birds_filtered, aes(x=Order, y=MaxLength,group=1)) +
  geom_point() +
  ggtitle("Max Length per order") + coord_flip()
```
![max längd per ordning](../../../../../translated_images/sv/max-length-per-order.e5b283d952c78c12b091307c5d3cf67132dad6fefe80a073353b9dc5c2bd3eb8.png)

Detta ger en översikt över den generella fördelningen av kroppslängd per fågelordning, men det är inte det optimala sättet att visa verkliga fördelningar. Den uppgiften hanteras vanligtvis genom att skapa ett histogram.
## Arbeta med histogram

`ggplot2` erbjuder mycket bra sätt att visualisera datafördelning med hjälp av histogram. Denna typ av diagram liknar ett stapeldiagram där fördelningen kan ses via en uppgång och nedgång av staplarna. För att bygga ett histogram behöver du numerisk data. För att skapa ett histogram kan du plotta ett diagram och definiera typen som 'hist' för histogram. Detta diagram visar fördelningen av MaxKroppsmassa för hela datasetets numeriska data. Genom att dela upp datamängden i mindre fack kan det visa fördelningen av datavärdena:

```r
ggplot(data = birds_filtered, aes(x = MaxBodyMass)) + 
  geom_histogram(bins=10)+ylab('Frequency')
```
![fördelning över hela datasetet](../../../../../translated_images/sv/distribution-over-the-entire-dataset.d22afd3fa96be854e4c82213fedec9e3703cba753d07fad4606aadf58cf7e78e.png)

Som du kan se, faller de flesta av de 400+ fåglarna i detta dataset inom intervallet under 2000 för deras Max Kroppsmassa. Få mer insikt i datan genom att ändra `bins`-parametern till ett högre nummer, något som 30:

```r
ggplot(data = birds_filtered, aes(x = MaxBodyMass)) + geom_histogram(bins=30)+ylab('Frequency')
```

![fördelning-30bins](../../../../../translated_images/sv/distribution-30bins.6a3921ea7a421bf71f06bf5231009e43d1146f1b8da8dc254e99b5779a4983e5.png)

Detta diagram visar fördelningen på ett lite mer detaljerat sätt. Ett diagram som är mindre snedvridet åt vänster kan skapas genom att säkerställa att du endast väljer data inom ett visst intervall:

Filtrera din data för att få endast de fåglar vars kroppsmassa är under 60, och visa 30 `bins`:

```r
birds_filtered_1 <- subset(birds_filtered, MaxBodyMass > 1 & MaxBodyMass < 60)
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_histogram(bins=30)+ylab('Frequency')
```

![filtrerat histogram](../../../../../translated_images/sv/filtered-histogram.6bf5d2bfd82533220e1bd4bc4f7d14308f43746ed66721d9ec8f460732be6674.png)

✅ Prova några andra filter och datapunkter. För att se den fullständiga fördelningen av datan, ta bort `['MaxBodyMass']`-filtret för att visa märkta fördelningar.

Histogrammet erbjuder också några trevliga färg- och märkningsförbättringar att prova:

Skapa ett 2D-histogram för att jämföra relationen mellan två fördelningar. Låt oss jämföra `MaxBodyMass` vs. `MaxLength`. `ggplot2` erbjuder ett inbyggt sätt att visa konvergens med hjälp av ljusare färger:

```r
ggplot(data=birds_filtered_1, aes(x=MaxBodyMass, y=MaxLength) ) +
  geom_bin2d() +scale_fill_continuous(type = "viridis")
```
Det verkar finnas en förväntad korrelation mellan dessa två element längs en förväntad axel, med en särskilt stark konvergenspunkt:

![2d diagram](../../../../../translated_images/sv/2d-plot.c504786f439bd7ebceebf2465c70ca3b124103e06c7ff7214bf24e26f7aec21e.png)

Histogram fungerar bra som standard för numerisk data. Vad händer om du behöver se fördelningar enligt textdata? 
## Utforska datasetet för fördelningar med hjälp av textdata 

Detta dataset innehåller också bra information om fågelkategorin och dess släkte, art och familj samt dess bevarandestatus. Låt oss gräva i denna bevarandestatusinformation. Hur ser fördelningen ut för fåglarna enligt deras bevarandestatus?

> ✅ I datasetet används flera akronymer för att beskriva bevarandestatus. Dessa akronymer kommer från [IUCN Red List Categories](https://www.iucnredlist.org/), en organisation som katalogiserar arters status.
> 
> - CR: Kritiskt hotad
> - EN: Hotad
> - EX: Utdöd
> - LC: Minst bekymrad
> - NT: Nära hotad
> - VU: Sårbar

Dessa är textbaserade värden så du behöver göra en transformering för att skapa ett histogram. Använd den filtreradeBirds-databasen och visa dess bevarandestatus tillsammans med dess Minsta Vingbredd. Vad ser du?

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

![vingbredd och bevarande](../../../../../translated_images/sv/wingspan-conservation-collation.4024e9aa6910866aa82f0c6cb6a6b4b925bd10079e6b0ef8f92eefa5a6792f76.png)

Det verkar inte finnas någon bra korrelation mellan minsta vingbredd och bevarandestatus. Testa andra element i datasetet med denna metod. Du kan prova olika filter också. Hittar du någon korrelation?

## Täthetsdiagram

Du kanske har märkt att histogrammen vi har tittat på hittills är "stegade" och inte flödar smidigt i en båge. För att visa ett smidigare täthetsdiagram kan du prova ett täthetsdiagram.

Låt oss arbeta med täthetsdiagram nu!

```r
ggplot(data = birds_filtered_1, aes(x = MinWingspan)) + 
  geom_density()
```
![täthetsdiagram](../../../../../translated_images/sv/density-plot.675ccf865b76c690487fb7f69420a8444a3515f03bad5482886232d4330f5c85.png)

Du kan se hur diagrammet speglar det tidigare för Minsta Vingbredd-data; det är bara lite smidigare. Om du ville återbesöka den hackiga MaxKroppsmassa-linjen i det andra diagrammet du byggde, kunde du jämna ut den mycket väl genom att återskapa den med denna metod:

```r
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_density()
```
![kroppsmassa täthet](../../../../../translated_images/sv/bodymass-smooth.d31ce526d82b0a1f19a073815dea28ecfbe58145ec5337e4ef7e8cdac81120b3.png)

Om du ville ha en smidig, men inte alltför smidig linje, redigera `adjust`-parametern: 

```r
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_density(adjust = 1/5)
```
![mindre smidig kroppsmassa](../../../../../translated_images/sv/less-smooth-bodymass.10f4db8b683cc17d17b2d33f22405413142004467a1493d416608dafecfdee23.png)

✅ Läs om de parametrar som finns tillgängliga för denna typ av diagram och experimentera!

Denna typ av diagram erbjuder vackert förklarande visualiseringar. Med några få rader kod kan du till exempel visa max kroppsmassa täthet per fågelordning:

```r
ggplot(data=birds_filtered_1,aes(x = MaxBodyMass, fill = Order)) +
  geom_density(alpha=0.5)
```
![kroppsmassa per ordning](../../../../../translated_images/sv/bodymass-per-order.9d2b065dd931b928c839d8cdbee63067ab1ae52218a1b90717f4bc744354f485.png)

## 🚀 Utmaning

Histogram är en mer sofistikerad typ av diagram än grundläggande spridningsdiagram, stapeldiagram eller linjediagram. Gör en sökning på internet för att hitta bra exempel på användningen av histogram. Hur används de, vad visar de, och inom vilka områden eller forskningsfält tenderar de att användas?

## [Quiz efter föreläsningen](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/19)

## Granskning & Självstudier

I denna lektion använde du `ggplot2` och började arbeta med att visa mer sofistikerade diagram. Gör lite forskning om `geom_density_2d()` en "kontinuerlig sannolikhetstäthetskurva i en eller flera dimensioner". Läs igenom [dokumentationen](https://ggplot2.tidyverse.org/reference/geom_density_2d.html) för att förstå hur det fungerar.

## Uppgift

[Använd dina färdigheter](assignment.md)

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiserade översättningar kan innehålla fel eller inexaktheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.