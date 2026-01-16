<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a33c5d4b4156a2b41788d8720b6f724c",
  "translation_date": "2025-08-26T23:02:59+00:00",
  "source_file": "3-Data-Visualization/R/12-visualization-relationships/README.md",
  "language_code": "fi"
}
-->
# Visualisoi suhteita: Kaikki hunajasta 🍯

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/12-Visualizing-Relationships.png)|
|:---:|
|Suhteiden visualisointi - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Jatkaen tutkimuksemme luontoteemaa, tutustutaan mielenkiintoisiin tapoihin visualisoida eri hunajatyyppeihin liittyviä suhteita Yhdysvaltain maatalousministeriön ([United States Department of Agriculture](https://www.nass.usda.gov/About_NASS/index.php)) tuottaman aineiston pohjalta.

Tämä noin 600 rivin datasetti kuvaa hunajantuotantoa useissa Yhdysvaltain osavaltioissa. Esimerkiksi voit tarkastella mehiläispesien määrää, tuottoa per pesä, kokonaistuotantoa, varastoja, hintaa per pauna ja hunajan arvoa osavaltioittain vuosina 1998–2012, yksi rivi per vuosi ja osavaltio.

Olisi mielenkiintoista visualisoida suhde tietyn osavaltion vuosituotannon ja esimerkiksi hunajan hinnan välillä kyseisessä osavaltiossa. Vaihtoehtoisesti voisit visualisoida osavaltioiden hunajantuoton per pesä. Tämä aikaväli kattaa myös tuhoisan 'CCD' eli 'Colony Collapse Disorder' -ilmiön, joka havaittiin ensimmäisen kerran vuonna 2006 (http://npic.orst.edu/envir/ccd.html), joten datasetti on erityisen merkityksellinen. 🐝

## [Esiluennon kysely](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/22)

Tässä oppitunnissa voit käyttää ggplot2-kirjastoa, jota olet käyttänyt aiemminkin, visualisoidaksesi muuttujien välisiä suhteita. Erityisen kiinnostavaa on käyttää ggplot2:n `geom_point`- ja `qplot`-toimintoja, jotka mahdollistavat hajontakaavioiden ja viivakaavioiden nopean luomisen. Näiden avulla data-analyytikko voi paremmin ymmärtää, miten muuttujat liittyvät toisiinsa. Lisätietoa löydät [täältä](https://ggplot2.tidyverse.org/).

## Hajontakaaviot

Käytä hajontakaaviota näyttääksesi, miten hunajan hinta on kehittynyt vuosittain osavaltioittain. ggplot2:n `ggplot` ja `geom_point` ryhmittelevät osavaltioiden tiedot kätevästi ja näyttävät datapisteet sekä kategoriselle että numeeriselle datalle.

Aloitetaan tuomalla data ja Seaborn:

```r
honey=read.csv('../../data/honey.csv')
head(honey)
```
Huomaat, että hunajadatasetissä on useita mielenkiintoisia sarakkeita, kuten vuosi ja hinta per pauna. Tutkitaan tätä dataa ryhmiteltynä Yhdysvaltain osavaltioiden mukaan:

| osavaltio | pesämäärä | tuotto/pesä | kokonaistuotanto | varastot | hinta/pauna | tuotannon arvo | vuosi |
| --------- | --------- | ----------- | ---------------- | -------- | ----------- | -------------- | ----- |
| AL        | 16000     | 71          | 1136000          | 159000   | 0.72        | 818000         | 1998  |
| AZ        | 55000     | 60          | 3300000          | 1485000  | 0.64        | 2112000        | 1998  |
| AR        | 53000     | 65          | 3445000          | 1688000  | 0.59        | 2033000        | 1998  |
| CA        | 450000    | 83          | 37350000         | 12326000 | 0.62        | 23157000       | 1998  |
| CO        | 27000     | 72          | 1944000          | 1594000  | 0.7         | 1361000        | 1998  |
| FL        | 230000    | 98          | 22540000         | 4508000  | 0.64        | 14426000       | 1998  |

Luo perushajontakaavio, joka näyttää suhteen hunajan hinnan ja sen alkuperäosavaltion välillä. Aseta `y`-akseli tarpeeksi korkeaksi, jotta kaikki osavaltiot näkyvät:

```r
library(ggplot2)
ggplot(honey, aes(x = priceperlb, y = state)) +
  geom_point(colour = "blue")
```
![hajontakaavio 1](../../../../../translated_images/fi/scatter1.86b8900674d88b26dd3353a83fe604e9ab3722c4680cc40ee9beb452ff02cdea.png)

Näytä nyt sama data hunajan värimaailmalla, joka havainnollistaa hinnan kehitystä vuosien varrella. Voit tehdä tämän lisäämällä 'scale_color_gradientn'-parametrin, joka näyttää muutoksen vuosi vuodelta:

> ✅ Lue lisää [scale_color_gradientn](https://www.rdocumentation.org/packages/ggplot2/versions/0.9.1/topics/scale_colour_gradientn) -toiminnosta ja kokeile kaunista sateenkaarivärimaailmaa!

```r
ggplot(honey, aes(x = priceperlb, y = state, color=year)) +
  geom_point()+scale_color_gradientn(colours = colorspace::heat_hcl(7))
```
![hajontakaavio 2](../../../../../translated_images/fi/scatter2.4d1cbc693bad20e2b563888747eb6bdf65b73ce449d903f7cd4068a78502dcff.png)

Tämän värimaailman avulla näet selvästi, että hunajan hinta per pauna on selvästi noussut vuosien varrella. Jos tarkastelet esimerkiksi Arizonan osavaltiota, voit havaita hintojen nousun vuosi vuodelta, muutamia poikkeuksia lukuun ottamatta:

| osavaltio | pesämäärä | tuotto/pesä | kokonaistuotanto | varastot | hinta/pauna | tuotannon arvo | vuosi |
| --------- | --------- | ----------- | ---------------- | -------- | ----------- | -------------- | ----- |
| AZ        | 55000     | 60          | 3300000          | 1485000  | 0.64        | 2112000        | 1998  |
| AZ        | 52000     | 62          | 3224000          | 1548000  | 0.62        | 1999000        | 1999  |
| AZ        | 40000     | 59          | 2360000          | 1322000  | 0.73        | 1723000        | 2000  |
| AZ        | 43000     | 59          | 2537000          | 1142000  | 0.72        | 1827000        | 2001  |
| AZ        | 38000     | 63          | 2394000          | 1197000  | 1.08        | 2586000        | 2002  |
| AZ        | 35000     | 72          | 2520000          | 983000   | 1.34        | 3377000        | 2003  |
| AZ        | 32000     | 55          | 1760000          | 774000   | 1.11        | 1954000        | 2004  |
| AZ        | 36000     | 50          | 1800000          | 720000   | 1.04        | 1872000        | 2005  |
| AZ        | 30000     | 65          | 1950000          | 839000   | 0.91        | 1775000        | 2006  |
| AZ        | 30000     | 64          | 1920000          | 902000   | 1.26        | 2419000        | 2007  |
| AZ        | 25000     | 64          | 1600000          | 336000   | 1.26        | 2016000        | 2008  |
| AZ        | 20000     | 52          | 1040000          | 562000   | 1.45        | 1508000        | 2009  |
| AZ        | 24000     | 77          | 1848000          | 665000   | 1.52        | 2809000        | 2010  |
| AZ        | 23000     | 53          | 1219000          | 427000   | 1.55        | 1889000        | 2011  |
| AZ        | 22000     | 46          | 1012000          | 253000   | 1.79        | 1811000        | 2012  |

Toinen tapa visualisoida tätä kehitystä on käyttää värin sijasta kokoa. Tämä voi olla parempi vaihtoehto värisokeille käyttäjille. Muokkaa visualisointiasi niin, että hinnan nousu näkyy pisteen koon kasvuna:

```r
ggplot(honey, aes(x = priceperlb, y = state)) +
  geom_point(aes(size = year),colour = "blue") +
  scale_size_continuous(range = c(0.25, 3))
```
Näet pisteiden koon kasvavan vähitellen.

![hajontakaavio 3](../../../../../translated_images/fi/scatter3.722d21e6f20b3ea2e18339bb9b10d75906126715eb7d5fdc88fe74dcb6d7066a.png)

Onko kyseessä yksinkertainen kysynnän ja tarjonnan laki? Ilmastonmuutoksen ja mehiläispesien romahtamisen vuoksi onko hunajaa vuosi vuodelta vähemmän saatavilla, mikä nostaa hintaa?

Tutkitaan korrelaatiota joidenkin muuttujien välillä viivakaavioiden avulla.

## Viivakaaviot

Kysymys: Onko hunajan hinnassa selkeä nousu vuosi vuodelta? Tämä on helpointa havaita luomalla yksittäinen viivakaavio:

```r
qplot(honey$year,honey$priceperlb, geom='smooth', span =0.5, xlab = "year",ylab = "priceperlb")
```
Vastaus: Kyllä, muutamia poikkeuksia lukuun ottamatta, kuten vuonna 2003:

![viivakaavio 1](../../../../../translated_images/fi/line1.299b576fbb2a59e60a59e7130030f59836891f90302be084e4e8d14da0562e2a.png)

Kysymys: Näkyykö vuonna 2003 myös piikki hunajan tarjonnassa? Entä jos tarkastelet kokonaistuotantoa vuosi vuodelta?

```python
qplot(honey$year,honey$totalprod, geom='smooth', span =0.5, xlab = "year",ylab = "totalprod")
```

![viivakaavio 2](../../../../../translated_images/fi/line2.3b18fcda7176ceba5b6689eaaabb817d49c965e986f11cac1ae3f424030c34d8.png)

Vastaus: Ei oikeastaan. Jos tarkastelet kokonaistuotantoa, se näyttää itse asiassa kasvaneen kyseisenä vuonna, vaikka yleisesti ottaen hunajantuotanto on ollut laskussa näinä vuosina.

Kysymys: Mikä sitten olisi voinut aiheuttaa hunajan hinnan piikin vuonna 2003?

Tämän selvittämiseksi voit käyttää facet grid -kaaviota.

## Facet grid -kaaviot

Facet grid -kaaviot ottavat yhden datasetin osa-alueen (tässä tapauksessa 'vuosi', jotta vältetään liian monien kaavioiden tuottaminen). Seaborn voi sitten luoda kaavion jokaiselle osa-alueelle valituilla x- ja y-koordinaateilla, mikä helpottaa visuaalista vertailua. Erottuuko vuosi 2003 tässä vertailussa?

Luo facet grid käyttämällä `facet_wrap`-toimintoa, kuten [ggplot2:n dokumentaatiossa](https://ggplot2.tidyverse.org/reference/facet_wrap.html) suositellaan.

```r
ggplot(honey, aes(x=yieldpercol, y = numcol,group = 1)) + 
  geom_line() + facet_wrap(vars(year))
```
Tässä visualisoinnissa voit verrata tuottoa per pesä ja pesien määrää vuosi vuodelta rinnakkain, sarakkeiden määrän ollessa 3:

![facet grid](../../../../../translated_images/fi/facet.491ad90d61c2a7cc69b50c929f80786c749e38217ccedbf1e22ed8909b65987c.png)

Tässä datasetissä mikään ei erityisesti erotu pesien määrän ja niiden tuoton osalta vuosi vuodelta ja osavaltioittain. Onko olemassa jokin toinen tapa löytää korrelaatio näiden kahden muuttujan välillä?

## Kaksoisviivakaaviot

Kokeile moniviivakaaviota piirtämällä kaksi viivakaaviota päällekkäin käyttäen R:n `par`- ja `plot`-toimintoja. Piirretään vuosi x-akselille ja näytetään kaksi y-akselia. Näytä tuotto per pesä ja pesien määrä päällekkäin:

```r
par(mar = c(5, 4, 4, 4) + 0.3)              
plot(honey$year, honey$numcol, pch = 16, col = 2,type="l")              
par(new = TRUE)                             
plot(honey$year, honey$yieldpercol, pch = 17, col = 3,              
     axes = FALSE, xlab = "", ylab = "",type="l")
axis(side = 4, at = pretty(range(y2)))      
mtext("colony yield", side = 4, line = 3)   
```
![päällekkäiset kaaviot](../../../../../translated_images/fi/dual-line.fc4665f360a54018d7df9bc6abcc26460112e17dcbda18d3b9ae6109b32b36c3.png)

Vaikka mikään ei erityisesti erotu vuoden 2003 kohdalla, tämä antaa meille mahdollisuuden päättää oppitunti hieman positiivisemmalla nuotilla: vaikka pesien määrä on yleisesti ottaen laskussa, niiden määrä näyttää vakiintuvan, vaikka tuotto per pesä onkin laskussa.

Hyvä mehiläiset, jatkakaa samaan malliin!

🐝❤️
## 🚀 Haaste

Tässä oppitunnissa opit lisää hajontakaavioiden ja viivaruudukkojen, kuten facet grid -kaavioiden, käytöstä. Haasta itsesi luomaan facet grid -kaavio eri datasetillä, ehkä sellaisella, jota käytit aiemmissa oppitunneissa. Huomaa, kuinka kauan niiden luominen kestää ja kuinka tarkkana sinun täytyy olla ruutujen määrän kanssa.

## [Jälkiluennon kysely](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/23)

## Kertaus ja itseopiskelu

Viivakaaviot voivat olla yksinkertaisia tai melko monimutkaisia. Lue lisää [ggplot2-dokumentaatiosta](https://ggplot2.tidyverse.org/reference/geom_path.html#:~:text=geom_line()%20connects%20them%20in,which%20cases%20are%20connected%20together) eri tavoista rakentaa niitä. Yritä parantaa tämän oppitunnin aikana luomiasi viivakaavioita dokumentaatiossa mainituilla muilla menetelmillä.

## Tehtävä

[Sukella mehiläispesään](assignment.md)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.