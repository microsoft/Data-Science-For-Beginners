<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a33c5d4b4156a2b41788d8720b6f724c",
  "translation_date": "2025-08-31T05:49:03+00:00",
  "source_file": "3-Data-Visualization/R/12-visualization-relationships/README.md",
  "language_code": "lt"
}
-->
# Vizualizuojame ryšius: Viskas apie medų 🍯

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/12-Visualizing-Relationships.png)|
|:---:|
|Ryšių vizualizavimas - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Tęsdami gamtos tematiką mūsų tyrimuose, atraskime įdomius vizualizacijos būdus, kaip parodyti ryšius tarp įvairių medaus rūšių, remiantis duomenų rinkiniu, gautu iš [Jungtinių Valstijų Žemės ūkio departamento](https://www.nass.usda.gov/About_NASS/index.php).

Šis maždaug 600 elementų duomenų rinkinys rodo medaus gamybą daugelyje JAV valstijų. Pavyzdžiui, galite peržiūrėti kolonijų skaičių, derlių vienai kolonijai, bendrą gamybą, atsargas, kainą už svarą ir medaus vertę tam tikroje valstijoje nuo 1998 iki 2012 metų, su viena eilute kiekvieniems metams kiekvienai valstijai.

Būtų įdomu vizualizuoti ryšį tarp tam tikros valstijos gamybos per metus ir, pavyzdžiui, medaus kainos toje valstijoje. Arba galite vizualizuoti ryšį tarp valstijų medaus derliaus vienai kolonijai. Šis laikotarpis apima niokojantį „CCD“ arba „Kolonijų žlugimo sutrikimą“, pirmą kartą pastebėtą 2006 m. (http://npic.orst.edu/envir/ccd.html), todėl tai yra reikšmingas duomenų rinkinys tyrimui. 🐝

## [Prieš paskaitą: testas](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/22)

Šioje pamokoje galite naudoti ggplot2, kurį jau naudojote anksčiau, kaip puikią biblioteką vizualizuoti ryšius tarp kintamųjų. Ypač įdomu naudoti ggplot2 `geom_point` ir `qplot` funkcijas, kurios leidžia greitai kurti sklaidos ir linijų diagramas, kad būtų galima vizualizuoti '[statistinius ryšius](https://ggplot2.tidyverse.org/)', padedančius duomenų mokslininkui geriau suprasti, kaip kintamieji yra susiję.

## Sklaidos diagramos

Naudokite sklaidos diagramą, kad parodytumėte, kaip medaus kaina keitėsi metai iš metų kiekvienoje valstijoje. ggplot2, naudojant `ggplot` ir `geom_point`, patogiai grupuoja valstijų duomenis ir rodo duomenų taškus tiek kategoriniams, tiek skaitiniams duomenims.

Pradėkime importuodami duomenis ir Seaborn:

```r
honey=read.csv('../../data/honey.csv')
head(honey)
```
Pastebėsite, kad medaus duomenyse yra keletas įdomių stulpelių, įskaitant metus ir kainą už svarą. Išnagrinėkime šiuos duomenis, suskirstytus pagal JAV valstijas:

| valstija | kolonijų skaičius | derlius vienai kolonijai | bendra gamyba | atsargos | kaina už svarą | gamybos vertė | metai |
| -------- | ----------------- | ------------------------ | ------------- | -------- | ------------- | ------------- | ----- |
| AL       | 16000            | 71                      | 1136000       | 159000   | 0.72          | 818000        | 1998  |
| AZ       | 55000            | 60                      | 3300000       | 1485000  | 0.64          | 2112000       | 1998  |
| AR       | 53000            | 65                      | 3445000       | 1688000  | 0.59          | 2033000       | 1998  |
| CA       | 450000           | 83                      | 37350000      | 12326000 | 0.62          | 23157000      | 1998  |
| CO       | 27000            | 72                      | 1944000       | 1594000  | 0.7           | 1361000       | 1998  |
| FL       | 230000           | 98                      | 22540000      | 4508000  | 0.64          | 14426000      | 1998  |

Sukurkite paprastą sklaidos diagramą, kad parodytumėte ryšį tarp medaus kainos už svarą ir jo kilmės valstijos. Padarykite `y` ašį pakankamai aukštą, kad būtų rodomos visos valstijos:

```r
library(ggplot2)
ggplot(honey, aes(x = priceperlb, y = state)) +
  geom_point(colour = "blue")
```
![sklaidos diagrama 1](../../../../../translated_images/lt/scatter1.86b8900674d88b26dd3353a83fe604e9ab3722c4680cc40ee9beb452ff02cdea.png)

Dabar parodykite tuos pačius duomenis su medaus spalvų schema, kad parodytumėte, kaip kaina keičiasi metai iš metų. Tai galite padaryti pridėdami 'scale_color_gradientn' parametrą, kad parodytumėte pokyčius:

> ✅ Sužinokite daugiau apie [scale_color_gradientn](https://www.rdocumentation.org/packages/ggplot2/versions/0.9.1/topics/scale_colour_gradientn) - išbandykite gražią vaivorykštės spalvų schemą!

```r
ggplot(honey, aes(x = priceperlb, y = state, color=year)) +
  geom_point()+scale_color_gradientn(colours = colorspace::heat_hcl(7))
```
![sklaidos diagrama 2](../../../../../translated_images/lt/scatter2.4d1cbc693bad20e2b563888747eb6bdf65b73ce449d903f7cd4068a78502dcff.png)

Naudodami šią spalvų schemą, galite pastebėti, kad per metus medaus kaina už svarą akivaizdžiai kyla. Iš tiesų, jei patikrinsite duomenų pavyzdį (pavyzdžiui, Arizonos valstiją), galite pastebėti kainų kilimo modelį metai iš metų, su keliomis išimtimis:

| valstija | kolonijų skaičius | derlius vienai kolonijai | bendra gamyba | atsargos | kaina už svarą | gamybos vertė | metai |
| -------- | ----------------- | ------------------------ | ------------- | -------- | ------------- | ------------- | ----- |
| AZ       | 55000            | 60                      | 3300000       | 1485000  | 0.64          | 2112000       | 1998  |
| AZ       | 52000            | 62                      | 3224000       | 1548000  | 0.62          | 1999000       | 1999  |
| AZ       | 40000            | 59                      | 2360000       | 1322000  | 0.73          | 1723000       | 2000  |
| AZ       | 43000            | 59                      | 2537000       | 1142000  | 0.72          | 1827000       | 2001  |
| AZ       | 38000            | 63                      | 2394000       | 1197000  | 1.08          | 2586000       | 2002  |
| AZ       | 35000            | 72                      | 2520000       | 983000   | 1.34          | 3377000       | 2003  |
| AZ       | 32000            | 55                      | 1760000       | 774000   | 1.11          | 1954000       | 2004  |
| AZ       | 36000            | 50                      | 1800000       | 720000   | 1.04          | 1872000       | 2005  |
| AZ       | 30000            | 65                      | 1950000       | 839000   | 0.91          | 1775000       | 2006  |
| AZ       | 30000            | 64                      | 1920000       | 902000   | 1.26          | 2419000       | 2007  |
| AZ       | 25000            | 64                      | 1600000       | 336000   | 1.26          | 2016000       | 2008  |
| AZ       | 20000            | 52                      | 1040000       | 562000   | 1.45          | 1508000       | 2009  |
| AZ       | 24000            | 77                      | 1848000       | 665000   | 1.52          | 2809000       | 2010  |
| AZ       | 23000            | 53                      | 1219000       | 427000   | 1.55          | 1889000       | 2011  |
| AZ       | 22000            | 46                      | 1012000       | 253000   | 1.79          | 1811000       | 2012  |

Kitas būdas parodyti šį progresą yra naudoti dydį, o ne spalvą. Spalvų neskiriantiems vartotojams tai gali būti geresnis pasirinkimas. Redaguokite savo vizualizaciją, kad kainos padidėjimas būtų parodytas didesniu taško apskritimu:

```r
ggplot(honey, aes(x = priceperlb, y = state)) +
  geom_point(aes(size = year),colour = "blue") +
  scale_size_continuous(range = c(0.25, 3))
```
Matote, kaip taškų dydis palaipsniui didėja.

![sklaidos diagrama 3](../../../../../translated_images/lt/scatter3.722d21e6f20b3ea2e18339bb9b10d75906126715eb7d5fdc88fe74dcb6d7066a.png)

Ar tai paprastas pasiūlos ir paklausos atvejis? Dėl tokių veiksnių kaip klimato kaita ir kolonijų žlugimas, ar medaus kiekis, kurį galima įsigyti, mažėja metai iš metų, todėl kaina kyla?

Norėdami atrasti koreliaciją tarp kai kurių šio duomenų rinkinio kintamųjų, išnagrinėkime keletą linijinių diagramų.

## Linijinės diagramos

Klausimas: Ar yra aiškus medaus kainos už svarą kilimas metai iš metų? Tai galite lengviausiai atrasti sukurdami vieną linijinę diagramą:

```r
qplot(honey$year,honey$priceperlb, geom='smooth', span =0.5, xlab = "year",ylab = "priceperlb")
```
Atsakymas: Taip, su keliomis išimtimis apie 2003 metus:

![linijinė diagrama 1](../../../../../translated_images/lt/line1.299b576fbb2a59e60a59e7130030f59836891f90302be084e4e8d14da0562e2a.png)

Klausimas: Na, o 2003 metais, ar taip pat matome medaus tiekimo šuolį? Ką, jei pažvelgtume į bendrą gamybą metai iš metų?

```python
qplot(honey$year,honey$totalprod, geom='smooth', span =0.5, xlab = "year",ylab = "totalprod")
```

![linijinė diagrama 2](../../../../../translated_images/lt/line2.3b18fcda7176ceba5b6689eaaabb817d49c965e986f11cac1ae3f424030c34d8.png)

Atsakymas: Ne visai. Jei pažvelgsite į bendrą gamybą, atrodo, kad ji iš tikrųjų padidėjo tais metais, nors apskritai medaus gamybos kiekis mažėja per šiuos metus.

Klausimas: Tokiu atveju, kas galėjo sukelti tą medaus kainos šuolį apie 2003 metus?

Norėdami tai atrasti, galite išnagrinėti facet grid.

## Facet grid

Facet grid leidžia pasirinkti vieną duomenų rinkinio aspektą (mūsų atveju galite pasirinkti 'metus', kad išvengtumėte per daug facetų). Tada Seaborn gali sukurti diagramą kiekvienam iš šių aspektų, pasirinktoms x ir y koordinatėms, kad būtų lengviau palyginti. Ar 2003 metai išsiskiria tokiame palyginime?

Sukurkite facet grid naudodami `facet_wrap`, kaip rekomenduoja [ggplot2 dokumentacija](https://ggplot2.tidyverse.org/reference/facet_wrap.html).

```r
ggplot(honey, aes(x=yieldpercol, y = numcol,group = 1)) + 
  geom_line() + facet_wrap(vars(year))
```
Šioje vizualizacijoje galite palyginti derlių vienai kolonijai ir kolonijų skaičių metai iš metų, šalia vienas kito, su wrap nustatytu 3 stulpeliams:

![facet grid](../../../../../translated_images/lt/facet.491ad90d61c2a7cc69b50c929f80786c749e38217ccedbf1e22ed8909b65987c.png)

Šiam duomenų rinkiniui niekas ypatingai neišsiskiria, kalbant apie kolonijų skaičių ir jų derlių, metai iš metų ir valstija po valstijos. Ar yra kitoks būdas ieškoti koreliacijos tarp šių dviejų kintamųjų?

## Dvigubos linijos diagramos

Išbandykite daugiagubą linijinę diagramą, uždėdami dvi linijines diagramas vieną ant kitos, naudodami R `par` ir `plot` funkcijas. Mes braižysime metus x ašyje ir rodysime dvi y ašis. Taigi, parodykite derlių vienai kolonijai ir kolonijų skaičių, uždėtus vieną ant kito:

```r
par(mar = c(5, 4, 4, 4) + 0.3)              
plot(honey$year, honey$numcol, pch = 16, col = 2,type="l")              
par(new = TRUE)                             
plot(honey$year, honey$yieldpercol, pch = 17, col = 3,              
     axes = FALSE, xlab = "", ylab = "",type="l")
axis(side = 4, at = pretty(range(y2)))      
mtext("colony yield", side = 4, line = 3)   
```
![uždėtos diagramos](../../../../../translated_images/lt/dual-line.fc4665f360a54018d7df9bc6abcc26460112e17dcbda18d3b9ae6109b32b36c3.png)

Nors niekas ypatingai neišsiskiria apie 2003 metus, tai leidžia mums užbaigti šią pamoką šiek tiek linksmesne nata: nors kolonijų skaičius apskritai mažėja, jų skaičius stabilizuojasi, net jei jų derlius vienai kolonijai mažėja.

Pirmyn, bitės, pirmyn!

🐝❤️
## 🚀 Iššūkis

Šioje pamokoje sužinojote daugiau apie kitus sklaidos diagramų ir linijinių tinklų, įskaitant facet grid, naudojimo būdus. Išbandykite save, sukurdami facet grid naudodami kitą duomenų rinkinį, galbūt tą, kurį naudojote prieš šias pamokas. Atkreipkite dėmesį, kiek laiko užtrunka jų kūrimas ir kaip reikia būti atsargiems dėl to, kiek tinklų reikia piešti naudojant šiuos metodus.
## [Po paskaitos: testas](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/23)

## Peržiūra ir savarankiškas mokymasis

Linijinės diagramos gali būti paprastos arba gana sudėtingos. Šiek tiek pasiskaitykite [ggplot2 dokumentacijoje](https://ggplot2.tidyverse.org/reference/geom_path.html#:~:text=geom_line()%20connects%20them%20in,which%20cases%20are%20connected%20together) apie įvairius būdus, kaip jas kurti. Pabandykite patobulinti linijines diagramas, kurias sukūrėte šioje pamokoje, naudodami kitus dokumentacijoje išvardytus metodus.
## Užduotis

[Pasinerkite į avilį](assignment.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipkite dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus aiškinimus, kylančius dėl šio vertimo naudojimo.