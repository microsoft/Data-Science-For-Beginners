<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a33c5d4b4156a2b41788d8720b6f724c",
  "translation_date": "2025-08-30T18:47:37+00:00",
  "source_file": "3-Data-Visualization/R/12-visualization-relationships/README.md",
  "language_code": "hr"
}
-->
# Vizualizacija odnosa: Sve o medu 🍯

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/12-Visualizing-Relationships.png)|
|:---:|
|Vizualizacija odnosa - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Nastavljajući s prirodnim fokusom našeg istraživanja, otkrijmo zanimljive vizualizacije koje prikazuju odnose između različitih vrsta meda, prema skupu podataka dobivenom od [Ministarstva poljoprivrede Sjedinjenih Američkih Država](https://www.nass.usda.gov/About_NASS/index.php).

Ovaj skup podataka, koji sadrži oko 600 stavki, prikazuje proizvodnju meda u mnogim američkim saveznim državama. Na primjer, možete pogledati broj kolonija, prinos po koloniji, ukupnu proizvodnju, zalihe, cijenu po funti i vrijednost proizvedenog meda u određenoj državi od 1998. do 2012., s jednim redom po godini za svaku državu.

Bit će zanimljivo vizualizirati odnos između proizvodnje određene države po godini i, na primjer, cijene meda u toj državi. Alternativno, mogli biste vizualizirati odnos između prinosa meda po koloniji u različitim državama. Ovo vremensko razdoblje obuhvaća razarajući 'CCD' ili 'Colony Collapse Disorder', prvi put zabilježen 2006. (http://npic.orst.edu/envir/ccd.html), što čini ovaj skup podataka dirljivim za proučavanje. 🐝

## [Kviz prije predavanja](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/22)

U ovoj lekciji možete koristiti ggplot2, koji ste već koristili, kao dobru biblioteku za vizualizaciju odnosa između varijabli. Posebno je zanimljiva upotreba ggplot2 funkcija `geom_point` i `qplot`, koje omogućuju scatter plotove i linijske grafove za brzu vizualizaciju '[statističkih odnosa](https://ggplot2.tidyverse.org/)', što omogućuje data znanstveniku bolje razumijevanje kako se varijable međusobno odnose.

## Scatterplotovi

Koristite scatterplot za prikaz kako se cijena meda razvijala iz godine u godinu, po državama. ggplot2, koristeći `ggplot` i `geom_point`, praktično grupira podatke po državama i prikazuje točke za kategorijske i numeričke podatke.

Započnimo s uvozom podataka i Seaborn-a:

```r
honey=read.csv('../../data/honey.csv')
head(honey)
```
Primijetit ćete da podaci o medu imaju nekoliko zanimljivih stupaca, uključujući godinu i cijenu po funti. Istražimo ove podatke, grupirane po američkim državama:

| država | brojkol | prinospokol | ukupnaprod | zalihe   | cijenapofunti | vrijednostprod | godina |
| ------ | ------- | ----------- | ---------- | -------- | ------------- | -------------- | ------ |
| AL     | 16000   | 71          | 1136000    | 159000   | 0.72          | 818000         | 1998   |
| AZ     | 55000   | 60          | 3300000    | 1485000  | 0.64          | 2112000        | 1998   |
| AR     | 53000   | 65          | 3445000    | 1688000  | 0.59          | 2033000        | 1998   |
| CA     | 450000  | 83          | 37350000   | 12326000 | 0.62          | 23157000       | 1998   |
| CO     | 27000   | 72          | 1944000    | 1594000  | 0.7           | 1361000        | 1998   |
| FL     | 230000  | 98          | 22540000   | 4508000  | 0.64          | 14426000       | 1998   |

Napravite osnovni scatterplot za prikaz odnosa između cijene po funti meda i države podrijetla. Napravite `y` os dovoljno visokom da prikaže sve države:

```r
library(ggplot2)
ggplot(honey, aes(x = priceperlb, y = state)) +
  geom_point(colour = "blue")
```
![scatterplot 1](../../../../../translated_images/hr/scatter1.86b8900674d88b26dd3353a83fe604e9ab3722c4680cc40ee9beb452ff02cdea.png)

Sada prikažite iste podatke s paletom boja meda kako biste pokazali kako se cijena razvija tijekom godina. To možete učiniti dodavanjem parametra 'scale_color_gradientn' za prikaz promjena iz godine u godinu:

> ✅ Saznajte više o [scale_color_gradientn](https://www.rdocumentation.org/packages/ggplot2/versions/0.9.1/topics/scale_colour_gradientn) - isprobajte prekrasnu paletu boja duge!

```r
ggplot(honey, aes(x = priceperlb, y = state, color=year)) +
  geom_point()+scale_color_gradientn(colours = colorspace::heat_hcl(7))
```
![scatterplot 2](../../../../../translated_images/hr/scatter2.4d1cbc693bad20e2b563888747eb6bdf65b73ce449d903f7cd4068a78502dcff.png)

S ovom promjenom palete boja možete vidjeti očigledan snažan napredak tijekom godina u smislu cijene meda po funti. Doista, ako pogledate uzorak podataka za provjeru (odaberite određenu državu, na primjer Arizonu), možete vidjeti obrazac povećanja cijene iz godine u godinu, s nekoliko iznimaka:

| država | brojkol | prinospokol | ukupnaprod | zalihe  | cijenapofunti | vrijednostprod | godina |
| ------ | ------- | ----------- | ---------- | ------- | ------------- | -------------- | ------ |
| AZ     | 55000   | 60          | 3300000    | 1485000 | 0.64          | 2112000        | 1998   |
| AZ     | 52000   | 62          | 3224000    | 1548000 | 0.62          | 1999000        | 1999   |
| AZ     | 40000   | 59          | 2360000    | 1322000 | 0.73          | 1723000        | 2000   |
| AZ     | 43000   | 59          | 2537000    | 1142000 | 0.72          | 1827000        | 2001   |
| AZ     | 38000   | 63          | 2394000    | 1197000 | 1.08          | 2586000        | 2002   |
| AZ     | 35000   | 72          | 2520000    | 983000  | 1.34          | 3377000        | 2003   |
| AZ     | 32000   | 55          | 1760000    | 774000  | 1.11          | 1954000        | 2004   |
| AZ     | 36000   | 50          | 1800000    | 720000  | 1.04          | 1872000        | 2005   |
| AZ     | 30000   | 65          | 1950000    | 839000  | 0.91          | 1775000        | 2006   |
| AZ     | 30000   | 64          | 1920000    | 902000  | 1.26          | 2419000        | 2007   |
| AZ     | 25000   | 64          | 1600000    | 336000  | 1.26          | 2016000        | 2008   |
| AZ     | 20000   | 52          | 1040000    | 562000  | 1.45          | 1508000        | 2009   |
| AZ     | 24000   | 77          | 1848000    | 665000  | 1.52          | 2809000        | 2010   |
| AZ     | 23000   | 53          | 1219000    | 427000  | 1.55          | 1889000        | 2011   |
| AZ     | 22000   | 46          | 1012000    | 253000  | 1.79          | 1811000        | 2012   |

Drugi način za vizualizaciju ovog napretka je korištenje veličine, umjesto boje. Za korisnike s poteškoćama u razlikovanju boja, ovo bi mogla biti bolja opcija. Uredite svoju vizualizaciju kako biste prikazali povećanje cijene povećanjem opsega točaka:

```r
ggplot(honey, aes(x = priceperlb, y = state)) +
  geom_point(aes(size = year),colour = "blue") +
  scale_size_continuous(range = c(0.25, 3))
```
Možete vidjeti kako se veličina točaka postupno povećava.

![scatterplot 3](../../../../../translated_images/hr/scatter3.722d21e6f20b3ea2e18339bb9b10d75906126715eb7d5fdc88fe74dcb6d7066a.png)

Je li ovo jednostavan slučaj ponude i potražnje? Zbog faktora poput klimatskih promjena i kolapsa kolonija, je li dostupno manje meda za kupnju iz godine u godinu, pa cijena raste?

Kako biste otkrili korelaciju između nekih varijabli u ovom skupu podataka, istražimo neke linijske grafove.

## Linijski grafovi

Pitanje: Postoji li jasan porast cijene meda po funti iz godine u godinu? To možete najlakše otkriti stvaranjem jednog linijskog grafova:

```r
qplot(honey$year,honey$priceperlb, geom='smooth', span =0.5, xlab = "year",ylab = "priceperlb")
```
Odgovor: Da, s nekim iznimkama oko 2003. godine:

![line chart 1](../../../../../translated_images/hr/line1.299b576fbb2a59e60a59e7130030f59836891f90302be084e4e8d14da0562e2a.png)

Pitanje: Pa, možemo li 2003. također vidjeti skok u zalihama meda? Što ako pogledate ukupnu proizvodnju iz godine u godinu?

```python
qplot(honey$year,honey$totalprod, geom='smooth', span =0.5, xlab = "year",ylab = "totalprod")
```

![line chart 2](../../../../../translated_images/hr/line2.3b18fcda7176ceba5b6689eaaabb817d49c965e986f11cac1ae3f424030c34d8.png)

Odgovor: Ne baš. Ako pogledate ukupnu proizvodnju, čini se da je zapravo porasla te godine, iako općenito količina proizvedenog meda opada tijekom tih godina.

Pitanje: U tom slučaju, što je moglo uzrokovati taj skok u cijeni meda oko 2003. godine?

Kako biste to otkrili, možete istražiti facet grid.

## Facet gridovi

Facet gridovi uzimaju jedan aspekt vašeg skupa podataka (u našem slučaju, možete odabrati 'godinu' kako biste izbjegli previše proizvedenih faceta). Seaborn zatim može napraviti graf za svaki od tih aspekata vaših odabranih x i y koordinata za lakšu vizualnu usporedbu. Ističe li se 2003. u ovoj vrsti usporedbe?

Napravite facet grid koristeći `facet_wrap` kako preporučuje [ggplot2 dokumentacija](https://ggplot2.tidyverse.org/reference/facet_wrap.html).

```r
ggplot(honey, aes(x=yieldpercol, y = numcol,group = 1)) + 
  geom_line() + facet_wrap(vars(year))
```
U ovoj vizualizaciji možete usporediti prinos po koloniji i broj kolonija iz godine u godinu, usporedno s wrap postavljenim na 3 za stupce:

![facet grid](../../../../../translated_images/hr/facet.491ad90d61c2a7cc69b50c929f80786c749e38217ccedbf1e22ed8909b65987c.png)

Za ovaj skup podataka, ništa posebno ne ističe se u vezi s brojem kolonija i njihovim prinosom, iz godine u godinu i iz države u državu. Postoji li drugačiji način za pronalaženje korelacije između ove dvije varijable?

## Dvostruki linijski grafovi

Isprobajte višelinijski graf superponiranjem dvaju linijskih grafova jedan na drugi, koristeći R-ove funkcije `par` i `plot`. Grafirat ćemo godinu na x osi i prikazati dvije y osi. Dakle, prikazat ćemo prinos po koloniji i broj kolonija, superponirano:

```r
par(mar = c(5, 4, 4, 4) + 0.3)              
plot(honey$year, honey$numcol, pch = 16, col = 2,type="l")              
par(new = TRUE)                             
plot(honey$year, honey$yieldpercol, pch = 17, col = 3,              
     axes = FALSE, xlab = "", ylab = "",type="l")
axis(side = 4, at = pretty(range(y2)))      
mtext("colony yield", side = 4, line = 3)   
```
![superimposed plots](../../../../../translated_images/hr/dual-line.fc4665f360a54018d7df9bc6abcc26460112e17dcbda18d3b9ae6109b32b36c3.png)

Iako ništa ne iskače oko 2003. godine, ovo nam omogućuje da završimo ovu lekciju na malo sretnijoj noti: iako ukupno broj kolonija opada, broj kolonija se stabilizira čak i ako njihov prinos po koloniji opada.

Naprijed, pčele, naprijed!

🐝❤️
## 🚀 Izazov

U ovoj lekciji naučili ste nešto više o drugim upotrebama scatterplotova i linijskih gridova, uključujući facet gridove. Izazovite se da napravite facet grid koristeći drugačiji skup podataka, možda onaj koji ste koristili prije ovih lekcija. Zabilježite koliko dugo traje njihovo stvaranje i kako morate biti oprezni s brojem gridova koje trebate nacrtati koristeći ove tehnike.
## [Kviz nakon predavanja](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/23)

## Pregled i samostalno učenje

Linijski grafovi mogu biti jednostavni ili prilično složeni. Malo istražite [ggplot2 dokumentaciju](https://ggplot2.tidyverse.org/reference/geom_path.html#:~:text=geom_line()%20connects%20them%20in,which%20cases%20are%20connected%20together) o raznim načinima na koje ih možete izgraditi. Pokušajte poboljšati linijske grafove koje ste izradili u ovoj lekciji koristeći druge metode navedene u dokumentaciji.
## Zadatak

[Zaronite u košnicu](assignment.md)

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane stručnjaka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.