<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b29e427401499e81f4af55a8c4afea76",
  "translation_date": "2025-09-04T22:16:54+00:00",
  "source_file": "3-Data-Visualization/12-visualization-relationships/README.md",
  "language_code": "hu"
}
-->
# Kapcsolatok vizualizálása: Minden a mézről 🍯

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/12-Visualizing-Relationships.png)|
|:---:|
|Kapcsolatok vizualizálása - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Folytatva kutatásunk természetközpontú fókuszát, fedezzünk fel érdekes vizualizációkat, amelyek bemutatják a különböző mézfajták közötti kapcsolatokat egy, az [Egyesült Államok Mezőgazdasági Minisztériuma](https://www.nass.usda.gov/About_NASS/index.php) által származtatott adathalmaz alapján.

Ez az adathalmaz körülbelül 600 elemet tartalmaz, és az Egyesült Államok számos államában a méztermelést mutatja be. Például megvizsgálhatjuk az államok méhkolóniáinak számát, a kolóniánkénti hozamot, a teljes termelést, a készleteket, az árakat fontonként, valamint az adott államban 1998-2012 között előállított méz értékét, évente egy sorral minden államra vonatkozóan.

Érdekes lehet vizualizálni az adott állam éves termelése és például az állambeli méz ára közötti kapcsolatot. Alternatívaként vizualizálhatjuk az államok kolóniánkénti mézhozamának kapcsolatát. Ez az időszak magában foglalja a pusztító 'CCD' vagy 'Colony Collapse Disorder' (http://npic.orst.edu/envir/ccd.html) első megjelenését 2006-ban, így ez egy szívszorító adathalmaz a tanulmányozáshoz. 🐝

## [Előadás előtti kvíz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/22)

Ebben a leckében használhatod a Seaborn könyvtárat, amelyet korábban már használtál, hogy vizualizáld a változók közötti kapcsolatokat. Különösen érdekes a Seaborn `relplot` függvényének használata, amely lehetővé teszi szórásdiagramok és vonaldiagramok gyors létrehozását a '[statisztikai kapcsolatok](https://seaborn.pydata.org/tutorial/relational.html?highlight=relationships)' vizualizálásához, amelyek segítenek az adatelemzőnek jobban megérteni, hogyan kapcsolódnak egymáshoz a változók.

## Szórásdiagramok

Használj szórásdiagramot annak bemutatására, hogyan alakult a méz ára évről évre, államonként. A Seaborn `relplot` függvényével kényelmesen csoportosíthatod az államok adatait, és megjelenítheted az adatpontokat mind kategóriális, mind numerikus adatok esetében.

Kezdjük az adatok és a Seaborn importálásával:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
honey = pd.read_csv('../../data/honey.csv')
honey.head()
```
Láthatod, hogy a méz adathalmaz számos érdekes oszlopot tartalmaz, például az évet és az árakat fontonként. Fedezzük fel ezeket az adatokat, csoportosítva az Egyesült Államok államai szerint:

| állam | numcol | yieldpercol | totalprod | stocks   | priceperlb | prodvalue | év   |
| ----- | ------ | ----------- | --------- | -------- | ---------- | --------- | ---- |
| AL    | 16000  | 71          | 1136000   | 159000   | 0.72       | 818000    | 1998 |
| AZ    | 55000  | 60          | 3300000   | 1485000  | 0.64       | 2112000   | 1998 |
| AR    | 53000  | 65          | 3445000   | 1688000  | 0.59       | 2033000   | 1998 |
| CA    | 450000 | 83          | 37350000  | 12326000 | 0.62       | 23157000  | 1998 |
| CO    | 27000  | 72          | 1944000   | 1594000  | 0.7        | 1361000   | 1998 |

Hozz létre egy alapvető szórásdiagramot, amely bemutatja a méz fontonkénti ára és az Egyesült Államok államai közötti kapcsolatot. Állítsd be az `y` tengelyt elég magasra, hogy minden állam látható legyen:

```python
sns.relplot(x="priceperlb", y="state", data=honey, height=15, aspect=.5);
```
![szórásdiagram 1](../../../../3-Data-Visualization/12-visualization-relationships/images/scatter1.png)

Most mutasd meg ugyanazokat az adatokat méz színvilággal, hogy bemutasd, hogyan változik az ár az évek során. Ezt úgy teheted meg, hogy hozzáadsz egy 'hue' paramétert, amely megmutatja az évről évre történő változást:

> ✅ Tudj meg többet a [Seaborn színpalettáiról](https://seaborn.pydata.org/tutorial/color_palettes.html) - próbálj ki egy gyönyörű szivárvány színvilágot!

```python
sns.relplot(x="priceperlb", y="state", hue="year", palette="YlOrBr", data=honey, height=15, aspect=.5);
```
![szórásdiagram 2](../../../../3-Data-Visualization/12-visualization-relationships/images/scatter2.png)

Ezzel a színvilág változtatással látható, hogy az évek során egyértelműen erős növekedés tapasztalható a méz fontonkénti ára tekintetében. Valóban, ha az adatok egy mintáját megvizsgálod (például Arizona államot), láthatod az árak évről évre történő növekedésének mintázatát, néhány kivétellel:

| állam | numcol | yieldpercol | totalprod | stocks  | priceperlb | prodvalue | év   |
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

Egy másik módja ennek a változásnak a vizualizálására a méret használata a szín helyett. Színvak felhasználók számára ez jobb opció lehet. Módosítsd a vizualizációt úgy, hogy az ár növekedését a pontok körméretének növekedésével mutasd:

```python
sns.relplot(x="priceperlb", y="state", size="year", data=honey, height=15, aspect=.5);
```
Láthatod, hogy a pontok mérete fokozatosan növekszik.

![szórásdiagram 3](../../../../3-Data-Visualization/12-visualization-relationships/images/scatter3.png)

Ez egyszerűen a kereslet és kínálat esete? Az olyan tényezők, mint az éghajlatváltozás és a kolóniák összeomlása miatt kevesebb méz áll rendelkezésre évről évre, és így az árak növekednek?

Ahhoz, hogy felfedezzük az adathalmazban lévő változók közötti korrelációt, nézzünk meg néhány vonaldiagramot.

## Vonaldiagramok

Kérdés: Van-e egyértelmű növekedés a méz fontonkénti ára tekintetében évről évre? Ezt legegyszerűbben egyetlen vonaldiagram létrehozásával fedezheted fel:

```python
sns.relplot(x="year", y="priceperlb", kind="line", data=honey);
```
Válasz: Igen, néhány kivétellel 2003 körül:

![vonaldiagram 1](../../../../3-Data-Visualization/12-visualization-relationships/images/line1.png)

✅ Mivel a Seaborn egyetlen vonal köré aggregálja az adatokat, "az x értékeknél lévő több mérést az átlag és az átlag körüli 95%-os konfidencia intervallum ábrázolásával jeleníti meg". [Forrás](https://seaborn.pydata.org/tutorial/relational.html). Ez az időigényes viselkedés kikapcsolható a `ci=None` hozzáadásával.

Kérdés: Nos, 2003-ban láthatunk-e egy ugrást a mézkínálatban? Mi történik, ha megnézzük az éves össztermelést?

```python
sns.relplot(x="year", y="totalprod", kind="line", data=honey);
```

![vonaldiagram 2](../../../../3-Data-Visualization/12-visualization-relationships/images/line2.png)

Válasz: Nem igazán. Ha megnézzük az össztermelést, úgy tűnik, hogy az adott évben valójában növekedett, bár általánosságban véve a méztermelés csökkenő tendenciát mutat ezekben az években.

Kérdés: Ebben az esetben mi okozhatta a méz árának ugrását 2003 körül?

Ennek felfedezéséhez használhatunk egy facet gridet.

## Facet grid-ek

A facet grid-ek az adathalmaz egy aspektusát veszik alapul (esetünkben választhatjuk az 'év'-et, hogy elkerüljük túl sok facet létrehozását). A Seaborn ezután egy diagramot készít az adott x és y koordináták alapján minden facet számára, megkönnyítve az összehasonlítást. Kitűnik-e 2003 ebben a típusú összehasonlításban?

Hozz létre egy facet grid-et a `relplot` használatával, ahogy azt a [Seaborn dokumentációja](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html?highlight=facetgrid#seaborn.FacetGrid) ajánlja.

```python
sns.relplot(
    data=honey, 
    x="yieldpercol", y="numcol",
    col="year", 
    col_wrap=3,
    kind="line"
```
Ebben a vizualizációban összehasonlíthatod a kolóniánkénti hozamot és a kolóniák számát évről évre, egymás mellett, 3 oszlopra állított wrap beállítással:

![facet grid](../../../../3-Data-Visualization/12-visualization-relationships/images/facet.png)

Ebben az adathalmazban semmi különös nem tűnik ki a kolóniák számát és hozamát illetően évről évre és államonként. Van-e más módja annak, hogy korrelációt találjunk e két változó között?

## Kettős vonaldiagramok

Próbálj ki egy többsoros diagramot, amely két vonaldiagramot helyez egymásra, a Seaborn 'despine' funkciójával eltávolítva a felső és jobb oldali gerinceket, valamint az `ax.twinx` használatával [a Matplotlibből származtatva](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.twinx.html). A Twinx lehetővé teszi, hogy egy diagram megossza az x tengelyt, és két y tengelyt jelenítsen meg. Tehát jelenítsd meg a kolóniánkénti hozamot és a kolóniák számát, egymásra helyezve:

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
![egymásra helyezett diagramok](../../../../3-Data-Visualization/12-visualization-relationships/images/dual-line.png)

Bár semmi különös nem tűnik ki 2003 körül, ez lehetővé teszi, hogy egy kicsit boldogabb hangon zárjuk ezt a leckét: bár a kolóniák száma általánosságban csökken, a kolóniák száma stabilizálódik, még ha a kolóniánkénti hozam csökken is.

Hajrá, méhek, hajrá!

🐝❤️
## 🚀 Kihívás

Ebben a leckében többet tanultál a szórásdiagramok és vonalhálók, köztük a facet grid-ek használatáról. Kihívásként hozz létre egy facet grid-et egy másik adathalmazzal, talán olyannal, amelyet korábban használtál ezekben a leckékben. Jegyezd meg, mennyi időbe telik létrehozni őket, és légy óvatos, hány gridet kell rajzolnod ezekkel a technikákkal.

## [Előadás utáni kvíz](https://ff-quizzes.netlify.app/en/ds/)

## Áttekintés és önálló tanulás

A vonaldiagramok lehetnek egyszerűek vagy meglehetősen összetettek. Olvass egy kicsit a [Seaborn dokumentációjában](https://seaborn.pydata.org/generated/seaborn.lineplot.html) a különböző módokról, ahogyan ezeket felépítheted. Próbáld meg fejleszteni az ebben a leckében létrehozott vonaldiagramokat a dokumentációban felsorolt egyéb módszerekkel.
## Feladat

[Merülj el a méhkasban](assignment.md)

---

**Felelősségkizárás**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális, emberi fordítást igénybe venni. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.