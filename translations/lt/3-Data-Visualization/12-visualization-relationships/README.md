<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cad419b574d5c35eaa417e9abfdcb0c8",
  "translation_date": "2025-08-31T05:53:30+00:00",
  "source_file": "3-Data-Visualization/12-visualization-relationships/README.md",
  "language_code": "lt"
}
-->
# Vizualizuojant ryšius: Viskas apie medų 🍯

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/12-Visualizing-Relationships.png)|
|:---:|
|Ryšių vizualizavimas - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Tęsdami mūsų tyrimų dėmesį į gamtą, atraskime įdomius vizualizacijos būdus, kaip parodyti ryšius tarp įvairių medaus rūšių, remiantis duomenų rinkiniu, gautu iš [JAV Žemės ūkio departamento](https://www.nass.usda.gov/About_NASS/index.php).

Šis duomenų rinkinys, apimantis apie 600 elementų, rodo medaus gamybą daugelyje JAV valstijų. Pavyzdžiui, galite peržiūrėti kolonijų skaičių, derlių vienai kolonijai, bendrą gamybą, atsargas, kainą už svarą ir medaus vertę tam tikroje valstijoje nuo 1998 iki 2012 metų, su viena eilute per metus kiekvienai valstijai.

Būtų įdomu vizualizuoti ryšį tarp tam tikros valstijos gamybos per metus ir, pavyzdžiui, medaus kainos toje valstijoje. Arba galite vizualizuoti ryšį tarp valstijų medaus derliaus vienai kolonijai. Šis laikotarpis apima niokojantį „CCD“ arba „Kolonijų žlugimo sutrikimą“, pirmą kartą pastebėtą 2006 m. (http://npic.orst.edu/envir/ccd.html), todėl tai yra prasmingas duomenų rinkinys tyrimui. 🐝

## [Prieš paskaitą: testas](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/22)

Šioje pamokoje galite naudoti Seaborn, kurį jau naudojote anksčiau, kaip puikią biblioteką vizualizuoti ryšius tarp kintamųjų. Ypač įdomi yra Seaborn funkcija `relplot`, kuri leidžia greitai kurti sklaidos diagramas ir linijines diagramas, vizualizuojant '[statistinius ryšius](https://seaborn.pydata.org/tutorial/relational.html?highlight=relationships)', padedančius duomenų mokslininkui geriau suprasti, kaip kintamieji tarpusavyje susiję.

## Sklaidos diagramos

Naudokite sklaidos diagramą, kad parodytumėte, kaip medaus kaina keitėsi metai iš metų, kiekvienoje valstijoje. Seaborn, naudodamas `relplot`, patogiai grupuoja valstijų duomenis ir rodo duomenų taškus tiek kategoriniams, tiek skaitiniams duomenims.

Pradėkime nuo duomenų ir Seaborn importavimo:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
honey = pd.read_csv('../../data/honey.csv')
honey.head()
```
Pastebėsite, kad medaus duomenyse yra keletas įdomių stulpelių, įskaitant metus ir kainą už svarą. Išnagrinėkime šiuos duomenis, suskirstytus pagal JAV valstijas:

| valstija | kolonijų skaičius | derlius/kolonija | bendra gamyba | atsargos | kaina/svaras | gamybos vertė | metai |
| -------- | ----------------- | ---------------- | ------------- | -------- | ------------ | ------------- | ----- |
| AL       | 16000            | 71              | 1136000       | 159000   | 0.72         | 818000        | 1998  |
| AZ       | 55000            | 60              | 3300000       | 1485000  | 0.64         | 2112000       | 1998  |
| AR       | 53000            | 65              | 3445000       | 1688000  | 0.59         | 2033000       | 1998  |
| CA       | 450000           | 83              | 37350000      | 12326000 | 0.62         | 23157000      | 1998  |
| CO       | 27000            | 72              | 1944000       | 1594000  | 0.7          | 1361000       | 1998  |

Sukurkite paprastą sklaidos diagramą, kad parodytumėte ryšį tarp medaus kainos už svarą ir jo kilmės valstijos. Padarykite `y` ašį pakankamai aukštą, kad būtų matomos visos valstijos:

```python
sns.relplot(x="priceperlb", y="state", data=honey, height=15, aspect=.5);
```
![sklaidos diagrama 1](../../../../translated_images/scatter1.5e1aa5fd6706c5d12b5e503ccb77f8a930f8620f539f524ddf56a16c039a5d2f.lt.png)

Dabar parodykite tuos pačius duomenis su medaus spalvų schema, kad pavaizduotumėte, kaip kaina keičiasi metai iš metų. Tai galite padaryti pridėdami 'hue' parametrą, kuris parodys pokyčius per metus:

> ✅ Sužinokite daugiau apie [spalvų paletes, kurias galite naudoti Seaborn](https://seaborn.pydata.org/tutorial/color_palettes.html) - išbandykite gražią vaivorykštės spalvų schemą!

```python
sns.relplot(x="priceperlb", y="state", hue="year", palette="YlOrBr", data=honey, height=15, aspect=.5);
```
![sklaidos diagrama 2](../../../../translated_images/scatter2.c0041a58621ca702990b001aa0b20cd68c1e1814417139af8a7211a2bed51c5f.lt.png)

Naudodami šią spalvų schemą, galite pastebėti, kad per metus medaus kaina už svarą akivaizdžiai kyla. Iš tiesų, jei pažiūrėsite į duomenų pavyzdį (pasirinkite tam tikrą valstiją, pavyzdžiui, Arizoną), galite pastebėti kainų kilimo tendenciją metai iš metų, su keliomis išimtimis:

| valstija | kolonijų skaičius | derlius/kolonija | bendra gamyba | atsargos | kaina/svaras | gamybos vertė | metai |
| -------- | ----------------- | ---------------- | ------------- | -------- | ------------ | ------------- | ----- |
| AZ       | 55000            | 60              | 3300000       | 1485000  | 0.64         | 2112000       | 1998  |
| AZ       | 52000            | 62              | 3224000       | 1548000  | 0.62         | 1999000       | 1999  |
| AZ       | 40000            | 59              | 2360000       | 1322000  | 0.73         | 1723000       | 2000  |
| AZ       | 43000            | 59              | 2537000       | 1142000  | 0.72         | 1827000       | 2001  |
| AZ       | 38000            | 63              | 2394000       | 1197000  | 1.08         | 2586000       | 2002  |
| AZ       | 35000            | 72              | 2520000       | 983000   | 1.34         | 3377000       | 2003  |
| AZ       | 32000            | 55              | 1760000       | 774000   | 1.11         | 1954000       | 2004  |
| AZ       | 36000            | 50              | 1800000       | 720000   | 1.04         | 1872000       | 2005  |
| AZ       | 30000            | 65              | 1950000       | 839000   | 0.91         | 1775000       | 2006  |
| AZ       | 30000            | 64              | 1920000       | 902000   | 1.26         | 2419000       | 2007  |
| AZ       | 25000            | 64              | 1600000       | 336000   | 1.26         | 2016000       | 2008  |
| AZ       | 20000            | 52              | 1040000       | 562000   | 1.45         | 1508000       | 2009  |
| AZ       | 24000            | 77              | 1848000       | 665000   | 1.52         | 2809000       | 2010  |
| AZ       | 23000            | 53              | 1219000       | 427000   | 1.55         | 1889000       | 2011  |
| AZ       | 22000            | 46              | 1012000       | 253000   | 1.79         | 1811000       | 2012  |

Kitas būdas vizualizuoti šią progresiją yra naudoti dydį, o ne spalvą. Spalvų aklumo turintiems vartotojams tai gali būti geresnis pasirinkimas. Redaguokite savo vizualizaciją, kad parodytumėte kainos didėjimą, didinant taško apskritimo dydį:

```python
sns.relplot(x="priceperlb", y="state", size="year", data=honey, height=15, aspect=.5);
```
Galite matyti, kaip taškų dydis palaipsniui didėja.

![sklaidos diagrama 3](../../../../translated_images/scatter3.3c160a3d1dcb36b37900ebb4cf97f34036f28ae2b7b8e6062766c7c1dfc00853.lt.png)

Ar tai paprastas pasiūlos ir paklausos atvejis? Dėl tokių veiksnių kaip klimato kaita ir kolonijų žlugimas, ar medaus kiekis, kurį galima įsigyti, mažėja metai iš metų, todėl kaina kyla?

Norėdami atrasti koreliaciją tarp kai kurių šio duomenų rinkinio kintamųjų, panagrinėkime keletą linijinių diagramų.

## Linijinės diagramos

Klausimas: Ar yra aiškus medaus kainos už svarą kilimas metai iš metų? Tai galite lengviausiai atrasti, sukurdami vieną linijinę diagramą:

```python
sns.relplot(x="year", y="priceperlb", kind="line", data=honey);
```
Atsakymas: Taip, su kai kuriomis išimtimis apie 2003 metus:

![linijinė diagrama 1](../../../../translated_images/line1.f36eb465229a3b1fe385cdc93861aab3939de987d504b05de0b6cd567ef79f43.lt.png)

✅ Kadangi Seaborn agreguoja duomenis aplink vieną liniją, jis rodo „kelis matavimus kiekvienoje x reikšmėje, braižydamas vidurkį ir 95% pasitikėjimo intervalą aplink vidurkį“. [Šaltinis](https://seaborn.pydata.org/tutorial/relational.html). Šį laiko reikalaujantį elgesį galima išjungti, pridėjus `ci=None`.

Klausimas: Na, o 2003 metais ar galime pastebėti medaus pasiūlos šuolį? Kas, jei pažvelgtumėte į bendrą gamybą metai iš metų?

```python
sns.relplot(x="year", y="totalprod", kind="line", data=honey);
```

![linijinė diagrama 2](../../../../translated_images/line2.a5b3493dc01058af6402e657aaa9ae1125fafb5e7d6630c777aa60f900a544e4.lt.png)

Atsakymas: Ne visai. Jei pažvelgsite į bendrą gamybą, atrodo, kad ji iš tikrųjų padidėjo tais metais, nors apskritai medaus gamybos kiekis mažėja per šiuos metus.

Klausimas: Tokiu atveju, kas galėjo sukelti medaus kainos šuolį apie 2003 metus?

Norėdami tai išsiaiškinti, galite panagrinėti facet grid.

## Facet grid

Facet grid leidžia pasirinkti vieną duomenų rinkinio aspektą (mūsų atveju galite pasirinkti 'metus', kad išvengtumėte per daug facetų). Seaborn tada gali sukurti diagramą kiekvienam iš šių aspektų, pasirinktų x ir y koordinatėms, kad būtų lengviau vizualiai palyginti. Ar 2003 metai išsiskiria tokio tipo palyginime?

Sukurkite facet grid, toliau naudodami `relplot`, kaip rekomenduoja [Seaborn dokumentacija](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html?highlight=facetgrid#seaborn.FacetGrid).

```python
sns.relplot(
    data=honey, 
    x="yieldpercol", y="numcol",
    col="year", 
    col_wrap=3,
    kind="line"
```
Šioje vizualizacijoje galite palyginti derlių vienai kolonijai ir kolonijų skaičių metai iš metų, šalia vienas kito, su wrap nustatytu 3 stulpeliams:

![facet grid](../../../../translated_images/facet.6a34851dcd540050dcc0ead741be35075d776741668dd0e42f482c89b114c217.lt.png)

Šiame duomenų rinkinyje niekas ypatingai neišsiskiria, kalbant apie kolonijų skaičių ir jų derlių, metai iš metų ir valstija po valstijos. Ar yra kitoks būdas ieškoti koreliacijos tarp šių dviejų kintamųjų?

## Dvigubos linijos diagramos

Išbandykite daugiagubą linijinę diagramą, uždėdami dvi linijines diagramas viena ant kitos, naudodami Seaborn 'despine', kad pašalintumėte jų viršutines ir dešines linijas, ir naudodami `ax.twinx` [gautą iš Matplotlib](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.twinx.html). Twinx leidžia diagramai dalintis x ašimi ir rodyti dvi y ašis. Taigi, parodykite derlių vienai kolonijai ir kolonijų skaičių, uždėtus vienas ant kito:

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
![superimposed plots](../../../../translated_images/dual-line.a4c28ce659603fab2c003f4df816733df2bf41d1facb7de27989ec9afbf01b33.lt.png)

Nors niekas akivaizdžiai neišsiskiria apie 2003 metus, tai leidžia mums užbaigti šią pamoką šiek tiek laimingesne nata: nors kolonijų skaičius apskritai mažėja, kolonijų skaičius stabilizuojasi, net jei jų derlius vienai kolonijai mažėja.

Pirmyn, bitės, pirmyn!

🐝❤️
## 🚀 Iššūkis

Šioje pamokoje sužinojote šiek tiek daugiau apie kitus sklaidos diagramų ir linijinių gridų naudojimo būdus, įskaitant facet grid. Išbandykite save, sukurdami facet grid naudodami kitą duomenų rinkinį, galbūt tą, kurį naudojote prieš šias pamokas. Atkreipkite dėmesį, kiek laiko užtrunka jų kūrimas ir kaip reikia būti atsargiems dėl to, kiek gridų reikia piešti naudojant šiuos metodus.
## [Po paskaitos: testas](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/23)

## Apžvalga ir savarankiškas mokymasis

Linijinės diagramos gali būti paprastos arba gana sudėtingos. Šiek tiek pasiskaitykite [Seaborn dokumentacijoje](https://seaborn.pydata.org/generated/seaborn.lineplot.html) apie įvairius būdus, kaip jas kurti. Pabandykite patobulinti linijines diagramas, kurias sukūrėte šioje pamokoje, naudodami kitus dokumentacijoje išvardytus metodus.
## Užduotis

[Pasinerkite į avilį](assignment.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipiame dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudotis profesionalių vertėjų paslaugomis. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus aiškinimus, kylančius dėl šio vertimo naudojimo.