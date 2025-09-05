<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "02ce904bc1e2bfabb7dc05c25aae375c",
  "translation_date": "2025-09-04T22:17:29+00:00",
  "source_file": "3-Data-Visualization/10-visualization-distributions/README.md",
  "language_code": "hu"
}
-->
# Az eloszlások vizualizálása

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| Az eloszlások vizualizálása - _Sketchnote készítette: [@nitya](https://twitter.com/nitya)_ |

Az előző leckében érdekes tényeket tanultál a Minnesotában élő madarakról szóló adathalmazról. Vizualizációval azonosítottál hibás adatokat, és megvizsgáltad a madárkategóriák közötti különbségeket a maximális hosszuk alapján.

## [Előadás előtti kvíz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/18)
## Fedezd fel a madarak adathalmazát

Egy másik módja az adatok elemzésének, ha megvizsgáljuk azok eloszlását, vagyis azt, hogy az adatok hogyan rendeződnek el egy tengely mentén. Például szeretnéd megtudni, hogy ebben az adathalmazban hogyan oszlik el a madarak maximális szárnyfesztávolsága vagy maximális testtömege Minnesotában.

Fedezzünk fel néhány tényt az adathalmaz eloszlásairól. Az _notebook.ipynb_ fájlban, amely a lecke mappájának gyökerében található, importáld a Pandas-t, a Matplotlib-et és az adataidat:

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```

|      | Név                          | TudományosNév          | Kategória             | Rend         | Család   | Nemzetség   | VédettségiStátusz | MinHossz | MaxHossz | MinTesttömeg | MaxTesttömeg | MinSzárnyfesztáv | MaxSzárnyfesztáv |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :---------------- | --------: | --------: | ------------: | ------------: | ---------------: | ---------------: |
|    0 | Feketehasú fütyülőlúd        | Dendrocygna autumnalis | Kacsák/Ludak/Vízimadarak | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652   |        1020   |              76  |              94  |
|    1 | Barna fütyülőlúd             | Dendrocygna bicolor    | Kacsák/Ludak/Vízimadarak | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712   |        1050   |              85  |              93  |
|    2 | Hóliba                      | Anser caerulescens     | Kacsák/Ludak/Vízimadarak | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050   |        4050   |             135  |             165  |
|    3 | Kis lúd                     | Anser rossii           | Kacsák/Ludak/Vízimadarak | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066   |        1567   |             113  |             116  |
|    4 | Nagy lilik                  | Anser albifrons        | Kacsák/Ludak/Vízimadarak | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930   |        3310   |             130  |             165  |

Általánosságban gyorsan megvizsgálhatod az adatok eloszlását egy szórásdiagram segítségével, ahogy az előző leckében is tettük:

```python
birds.plot(kind='scatter',x='MaxLength',y='Order',figsize=(12,8))

plt.title('Max Length per Order')
plt.ylabel('Order')
plt.xlabel('Max Length')

plt.show()
```
![max hossz rendenként](../../../../3-Data-Visualization/10-visualization-distributions/images/scatter-wb.png)

Ez egy általános áttekintést ad a madarak testhosszának eloszlásáról rendenként, de nem a legjobb módja az igazi eloszlások megjelenítésének. Ezt a feladatot általában hisztogramokkal oldják meg.

## Hisztogramok használata

A Matplotlib kiváló eszközöket kínál az adatok eloszlásának vizualizálására hisztogramok segítségével. Ez a diagramtípus hasonlít az oszlopdiagramhoz, ahol az eloszlás a sávok emelkedésén és csökkenésén keresztül látható. Hisztogram készítéséhez numerikus adatokra van szükség. Egy hisztogram létrehozásához állítsd be a diagram típusát 'hist'-re. Ez a diagram az egész adathalmaz MaxBodyMass értékeinek eloszlását mutatja. Az adatok tömbjét kisebb részekre osztva megjeleníti az értékek eloszlását:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 10, figsize = (12,12))
plt.show()
```
![eloszlás az egész adathalmazon](../../../../3-Data-Visualization/10-visualization-distributions/images/dist1-wb.png)

Ahogy látható, a több mint 400 madár többsége ebben az adathalmazban 2000 alatti Max Body Mass tartományba esik. További betekintést nyerhetsz az adatokba, ha a `bins` paramétert magasabb értékre, például 30-ra állítod:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 30, figsize = (12,12))
plt.show()
```
![eloszlás nagyobb bins paraméterrel](../../../../3-Data-Visualization/10-visualization-distributions/images/dist2-wb.png)

Ez a diagram kicsit részletesebb képet ad az eloszlásról. Egy kevésbé balra torzított diagramot hozhatsz létre, ha csak egy adott tartományba eső adatokat választasz ki:

Szűrd az adatokat úgy, hogy csak azokat a madarakat kapd meg, amelyek testtömege 60 alatt van, és állítsd be a `bins` értékét 40-re:

```python
filteredBirds = birds[(birds['MaxBodyMass'] > 1) & (birds['MaxBodyMass'] < 60)]      
filteredBirds['MaxBodyMass'].plot(kind = 'hist',bins = 40,figsize = (12,12))
plt.show()     
```
![szűrt hisztogram](../../../../3-Data-Visualization/10-visualization-distributions/images/dist3-wb.png)

✅ Próbálj ki más szűrőket és adatpontokat. Az adatok teljes eloszlásának megtekintéséhez távolítsd el a `['MaxBodyMass']` szűrőt, hogy címkézett eloszlásokat láss.

A hisztogram további szín- és címkézési lehetőségeket is kínál:

Hozz létre egy 2D hisztogramot, hogy összehasonlítsd két eloszlás kapcsolatát. Hasonlítsuk össze a `MaxBodyMass` és a `MaxLength` értékeket. A Matplotlib beépített módot kínál az összefüggések megjelenítésére élénkebb színek használatával:

```python
x = filteredBirds['MaxBodyMass']
y = filteredBirds['MaxLength']

fig, ax = plt.subplots(tight_layout=True)
hist = ax.hist2d(x, y)
```
Úgy tűnik, hogy van egy várható korreláció e két elem között egy előre látható tengely mentén, egy különösen erős konvergenciaponttal:

![2D diagram](../../../../3-Data-Visualization/10-visualization-distributions/images/2D-wb.png)

A hisztogramok alapértelmezés szerint jól működnek numerikus adatokkal. Mi a helyzet akkor, ha szöveges adatok szerinti eloszlásokat szeretnél látni?

## Az adathalmaz vizsgálata szöveges adatok eloszlása alapján

Ez az adathalmaz jó információkat tartalmaz a madarak kategóriájáról, nemzetségéről, fajáról és családjáról, valamint a védettségi státuszukról. Vizsgáljuk meg ezt a védettségi információt. Hogyan oszlanak meg a madarak a védettségi státuszuk szerint?

> ✅ Az adathalmazban több rövidítés található, amelyek a védettségi státuszt írják le. Ezek a rövidítések az [IUCN Vörös Lista Kategóriáiból](https://www.iucnredlist.org/) származnak, amely egy szervezet, amely a fajok státuszát katalogizálja.
> 
> - CR: Kihalás szélén álló
> - EN: Veszélyeztetett
> - EX: Kihalt
> - LC: Nem fenyegetett
> - NT: Mérsékelten fenyegetett
> - VU: Sebezhető

Ezek szöveges értékek, így egy átalakítást kell végezned, hogy hisztogramot készíthess. A szűrtBirds adathalmazt használva jelenítsd meg a védettségi státuszt a minimális szárnyfesztávolsággal együtt. Mit látsz?

```python
x1 = filteredBirds.loc[filteredBirds.ConservationStatus=='EX', 'MinWingspan']
x2 = filteredBirds.loc[filteredBirds.ConservationStatus=='CR', 'MinWingspan']
x3 = filteredBirds.loc[filteredBirds.ConservationStatus=='EN', 'MinWingspan']
x4 = filteredBirds.loc[filteredBirds.ConservationStatus=='NT', 'MinWingspan']
x5 = filteredBirds.loc[filteredBirds.ConservationStatus=='VU', 'MinWingspan']
x6 = filteredBirds.loc[filteredBirds.ConservationStatus=='LC', 'MinWingspan']

kwargs = dict(alpha=0.5, bins=20)

plt.hist(x1, **kwargs, color='red', label='Extinct')
plt.hist(x2, **kwargs, color='orange', label='Critically Endangered')
plt.hist(x3, **kwargs, color='yellow', label='Endangered')
plt.hist(x4, **kwargs, color='green', label='Near Threatened')
plt.hist(x5, **kwargs, color='blue', label='Vulnerable')
plt.hist(x6, **kwargs, color='gray', label='Least Concern')

plt.gca().set(title='Conservation Status', ylabel='Min Wingspan')
plt.legend();
```

![szárnyfesztáv és védettségi státusz](../../../../3-Data-Visualization/10-visualization-distributions/images/histogram-conservation-wb.png)

Úgy tűnik, hogy nincs jó korreláció a minimális szárnyfesztávolság és a védettségi státusz között. Tesztelj más elemeket az adathalmazból ezzel a módszerrel. Próbálj ki különböző szűrőket is. Találsz bármilyen összefüggést?

## Sűrűségdiagramok

Észrevehetted, hogy az eddig vizsgált hisztogramok "lépcsőzetesek", és nem folynak simán egy ívben. Egy simább sűrűségdiagram megjelenítéséhez próbálj ki egy sűrűségdiagramot.

A sűrűségdiagramokkal való munkához ismerkedj meg egy új ábrázolási könyvtárral, a [Seaborn](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) könyvtárral.

A Seaborn betöltése után próbálj ki egy alapvető sűrűségdiagramot:

```python
import seaborn as sns
import matplotlib.pyplot as plt
sns.kdeplot(filteredBirds['MinWingspan'])
plt.show()
```
![Sűrűségdiagram](../../../../3-Data-Visualization/10-visualization-distributions/images/density1.png)

Láthatod, hogy a diagram visszatükrözi a korábbi minimális szárnyfesztávolság adatait; csak egy kicsit simább. A Seaborn dokumentációja szerint: "A hisztogramhoz képest a KDE egy kevésbé zsúfolt és könnyebben értelmezhető diagramot készíthet, különösen több eloszlás ábrázolásakor. Azonban torzításokat vezethet be, ha az alapul szolgáló eloszlás korlátozott vagy nem sima. Mint a hisztogram esetében, a reprezentáció minősége is a jó simítási paraméterek kiválasztásától függ." [forrás](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) Más szavakkal, az outlierek, mint mindig, rossz viselkedést okozhatnak a diagramjaidban.

Ha újra szeretnéd vizsgálni azt a szaggatott MaxBodyMass vonalat, amelyet a második diagramon készítettél, nagyon jól kisimíthatod, ha ezt a módszert használod:

```python
sns.kdeplot(filteredBirds['MaxBodyMass'])
plt.show()
```
![simított testtömeg vonal](../../../../3-Data-Visualization/10-visualization-distributions/images/density2.png)

Ha sima, de nem túl sima vonalat szeretnél, szerkeszd a `bw_adjust` paramétert:

```python
sns.kdeplot(filteredBirds['MaxBodyMass'], bw_adjust=.2)
plt.show()
```
![kevésbé sima testtömeg vonal](../../../../3-Data-Visualization/10-visualization-distributions/images/density3.png)

✅ Olvass a rendelkezésre álló paraméterekről ehhez a diagramtípushoz, és kísérletezz!

Ez a diagramtípus gyönyörűen magyarázó vizualizációkat kínál. Például néhány kódsorral megjelenítheted a madarak rendenkénti maximális testtömegének sűrűségét:

```python
sns.kdeplot(
   data=filteredBirds, x="MaxBodyMass", hue="Order",
   fill=True, common_norm=False, palette="crest",
   alpha=.5, linewidth=0,
)
```

![testtömeg rendenként](../../../../3-Data-Visualization/10-visualization-distributions/images/density4.png)

Egy diagramon több változó sűrűségét is ábrázolhatod. Vizsgáld meg a madarak MaxLength és MinLength értékeit a védettségi státuszukhoz viszonyítva:

```python
sns.kdeplot(data=filteredBirds, x="MinLength", y="MaxLength", hue="ConservationStatus")
```

![több sűrűség, egymásra helyezve](../../../../3-Data-Visualization/10-visualization-distributions/images/multi.png)

Talán érdemes kutatni, hogy a "Sebezhető" madarak hosszúság szerinti csoportosulása jelentőséggel bír-e vagy sem.

## 🚀 Kihívás

A hisztogramok fejlettebb diagramtípusok, mint az alapvető szórásdiagramok, oszlopdiagramok vagy vonaldiagramok. Keress az interneten jó példákat a hisztogramok használatára. Hogyan használják őket, mit mutatnak be, és milyen területeken vagy kutatási területeken alkalmazzák őket?

## [Előadás utáni kvíz](https://ff-quizzes.netlify.app/en/ds/)

## Áttekintés és önálló tanulás

Ebben a leckében a Matplotlib-et használtad, és elkezdtél dolgozni a Seaborn-nal, hogy fejlettebb diagramokat készíts. Kutass a Seaborn `kdeplot` funkciójáról, amely "folytonos valószínűségi sűrűséggörbét" készít egy vagy több dimenzióban. Olvasd el a [dokumentációt](https://seaborn.pydata.org/generated/seaborn.kdeplot.html), hogy megértsd, hogyan működik.

## Feladat

[Alkalmazd a készségeidet](assignment.md)

---

**Felelősségkizárás**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális, emberi fordítást igénybe venni. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.