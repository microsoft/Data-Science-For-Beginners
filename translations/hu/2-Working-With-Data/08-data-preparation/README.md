<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1b560955ff39a2bcf2a049fce474a951",
  "translation_date": "2025-09-05T17:28:40+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "hu"
}
-->
# Adatokkal való munka: Adatelőkészítés

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|Adatelőkészítés - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## [Előadás előtti kvíz](https://ff-quizzes.netlify.app/en/ds/quiz/14)

Az adatok forrásától függően a nyers adatok tartalmazhatnak olyan inkonzisztenciákat, amelyek nehézségeket okoznak az elemzésben és modellezésben. Más szóval, ezek az adatok „piszkosnak” minősíthetők, és tisztításra szorulnak. Ez a lecke az adatok tisztítására és átalakítására szolgáló technikákra összpontosít, hogy kezelje a hiányzó, pontatlan vagy hiányos adatok problémáit. A lecke témái Python és Pandas könyvtár használatával kerülnek bemutatásra, és [a notebookban](../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb) találhatók ebben a könyvtárban.

## Az adatok tisztításának fontossága

- **Egyszerű használat és újrafelhasználás**: Ha az adatok megfelelően szervezettek és normalizáltak, könnyebb keresni, használni és megosztani másokkal.

- **Konzisztencia**: Az adatelemzés gyakran több adatállománnyal való munkát igényel, ahol különböző forrásokból származó adatállományokat kell összeilleszteni. Az egyes adatállományok közös szabványosítása biztosítja, hogy az adatok továbbra is hasznosak maradjanak, amikor egyetlen adatállományba egyesítik őket.

- **Modellek pontossága**: A tisztított adatok javítják az azokra támaszkodó modellek pontosságát.

## Gyakori tisztítási célok és stratégiák

- **Adatállomány feltérképezése**: Az adatok feltérképezése, amelyet egy [későbbi leckében](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing) tárgyalunk, segíthet azonosítani azokat az adatokat, amelyeket tisztítani kell. Az értékek vizuális megfigyelése az adatállományban elvárásokat állíthat fel arról, hogy a többi adat hogyan fog kinézni, vagy ötletet adhat a megoldandó problémákról. A feltérképezés magában foglalhat alapvető lekérdezéseket, vizualizációkat és mintavételezést.

- **Formázás**: Az adatok forrásától függően előfordulhatnak inkonzisztenciák az adatok megjelenítésében. Ez problémákat okozhat az értékek keresésében és megjelenítésében, ahol az értékek láthatók az adatállományban, de nem megfelelően jelennek meg a vizualizációkban vagy lekérdezési eredményekben. Gyakori formázási problémák közé tartozik a szóközök, dátumok és adattípusok kezelése. A formázási problémák megoldása általában az adatok felhasználóira hárul. Például a dátumok és számok megjelenítésére vonatkozó szabványok országonként eltérhetnek.

- **Duplikációk**: Az adatok többszöri előfordulása pontatlan eredményeket hozhat, és általában el kell távolítani. Ez gyakran előfordulhat, amikor két vagy több adatállományt egyesítenek. Azonban vannak olyan esetek, amikor az egyesített adatállományok duplikációi további információkat tartalmazhatnak, és megőrzésük szükséges lehet.

- **Hiányzó adatok**: A hiányzó adatok pontatlanságokat, valamint gyenge vagy elfogult eredményeket okozhatnak. Ezeket néha meg lehet oldani az adatok „újratöltésével”, a hiányzó értékek számítással és kóddal, például Python segítségével történő kitöltésével, vagy egyszerűen az értékek és a hozzájuk tartozó adatok eltávolításával. Számos oka lehet annak, hogy az adatok miért hiányoznak, és a hiányzó értékek megoldására tett lépések attól függhetnek, hogy hogyan és miért tűntek el.

## Adatkeret információinak feltérképezése
> **Tanulási cél:** A szakasz végére képesnek kell lenned általános információkat találni a pandas DataFrame-ekben tárolt adatokról.

Miután betöltötted az adataidat a pandas-ba, valószínűleg DataFrame formátumban lesznek (lásd az előző [leckét](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe) a részletes áttekintésért). Azonban ha a DataFrame-edben lévő adatállomány 60,000 sorból és 400 oszlopból áll, hogyan kezdhetsz el egyáltalán képet kapni arról, hogy mivel dolgozol? Szerencsére a [pandas](https://pandas.pydata.org/) kényelmes eszközöket kínál, amelyekkel gyorsan áttekintheted a DataFrame általános információit, valamint az első és utolsó néhány sort.

Ennek a funkciónak a feltérképezéséhez importáljuk a Python scikit-learn könyvtárat, és használjunk egy ikonikus adatállományt: az **Iris adatállományt**.

```python
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
iris_df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
```
|                                        |csészelevél hossza (cm)|csészelevél szélessége (cm)|sziromlevél hossza (cm)|sziromlevél szélessége (cm)|
|----------------------------------------|-----------------------|---------------------------|-----------------------|---------------------------|
|0                                       |5.1                   |3.5                       |1.4                   |0.2                       |
|1                                       |4.9                   |3.0                       |1.4                   |0.2                       |
|2                                       |4.7                   |3.2                       |1.3                   |0.2                       |
|3                                       |4.6                   |3.1                       |1.5                   |0.2                       |
|4                                       |5.0                   |3.6                       |1.4                   |0.2                       |

- **DataFrame.info**: Kezdésként az `info()` metódust használjuk, hogy összefoglalót nyomtassunk a `DataFrame` tartalmáról. Nézzük meg ezt az adatállományt, hogy lássuk, mivel dolgozunk:
```python
iris_df.info()
```
```
RangeIndex: 150 entries, 0 to 149
Data columns (total 4 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   sepal length (cm)  150 non-null    float64
 1   sepal width (cm)   150 non-null    float64
 2   petal length (cm)  150 non-null    float64
 3   petal width (cm)   150 non-null    float64
dtypes: float64(4)
memory usage: 4.8 KB
```
Ebből tudjuk, hogy az *Iris* adatállomány 150 bejegyzést tartalmaz négy oszlopban, és nincs benne null érték. Az összes adat 64 bites lebegőpontos számként van tárolva.

- **DataFrame.head()**: Ezután, hogy ellenőrizzük a `DataFrame` tényleges tartalmát, használjuk a `head()` metódust. Nézzük meg, hogyan néz ki az `iris_df` első néhány sora:
```python
iris_df.head()
```
```
   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
0                5.1               3.5                1.4               0.2
1                4.9               3.0                1.4               0.2
2                4.7               3.2                1.3               0.2
3                4.6               3.1                1.5               0.2
4                5.0               3.6                1.4               0.2
```
- **DataFrame.tail()**: Ezzel szemben, hogy ellenőrizzük a `DataFrame` utolsó néhány sorát, használjuk a `tail()` metódust:
```python
iris_df.tail()
```
```
     sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
145                6.7               3.0                5.2               2.3
146                6.3               2.5                5.0               1.9
147                6.5               3.0                5.2               2.0
148                6.2               3.4                5.4               2.3
149                5.9               3.0                5.1               1.8
```
> **Tanulság:** Már csak a DataFrame-ben lévő információk metaadatainak vagy az első és utolsó néhány értékének megtekintésével azonnali képet kaphatsz az adatok méretéről, alakjáról és tartalmáról, amelyekkel dolgozol.

## Hiányzó adatok kezelése
> **Tanulási cél:** A szakasz végére tudnod kell, hogyan cserélj vagy távolíts el null értékeket a DataFrame-ekből.

A legtöbb esetben az általad használt (vagy használnod kell) adatállományok hiányzó értékeket tartalmaznak. A hiányzó adatok kezelése finom kompromisszumokat hordoz magában, amelyek befolyásolhatják a végső elemzést és a valós eredményeket.

A pandas kétféleképpen kezeli a hiányzó értékeket. Az elsőt már láttad korábbi szakaszokban: `NaN`, vagyis Not a Number. Ez valójában egy speciális érték, amely az IEEE lebegőpontos specifikáció része, és csak hiányzó lebegőpontos értékek jelzésére használják.

A lebegőpontokon kívüli hiányzó értékek esetében a pandas a Python `None` objektumát használja. Bár zavarónak tűnhet, hogy két különböző típusú értékkel találkozol, amelyek lényegében ugyanazt jelentik, ennek a tervezési döntésnek programozási okai vannak, és a gyakorlatban ez a megközelítés a legtöbb esetben jó kompromisszumot kínál. Mindazonáltal a `None` és `NaN` korlátozásokat hordoz magában, amelyeket figyelembe kell venni a használatuk során.

További információt a `NaN`-ról és `None`-ról a [notebookban](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb) találsz!

- **Null értékek észlelése**: A `pandas`-ban az `isnull()` és `notnull()` metódusok az elsődleges eszközeid a null adatok észlelésére. Mindkettő logikai maszkokat ad vissza az adataid felett. A `numpy`-t fogjuk használni a `NaN` értékekhez:
```python
import numpy as np

example1 = pd.Series([0, np.nan, '', None])
example1.isnull()
```
```
0    False
1     True
2    False
3     True
dtype: bool
```
Nézd meg alaposan a kimenetet. Meglepett valami? Bár a `0` aritmetikailag null, mégis tökéletesen jó egész szám, és a pandas így is kezeli. A `''` egy kicsit finomabb. Bár az 1. szakaszban üres sztring értékként használtuk, mégis sztring objektum, és nem null reprezentáció a pandas szerint.

Most fordítsuk meg ezt, és használjuk ezeket a metódusokat úgy, ahogy a gyakorlatban fogod. A logikai maszkokat közvetlenül használhatod `Series` vagy `DataFrame` indexként, ami hasznos lehet, amikor elszigetelt hiányzó (vagy meglévő) értékekkel dolgozol.

> **Tanulság:** Az `isnull()` és `notnull()` metódusok hasonló eredményeket adnak, amikor `DataFrame`-ekben használod őket: megmutatják az eredményeket és azok indexét, ami óriási segítséget nyújt az adatokkal való küzdelem során.

- **Null értékek eltávolítása**: A hiányzó értékek azonosításán túl a pandas kényelmes eszközt kínál a null értékek eltávolítására `Series`-ekből és `DataFrame`-ekből. (Különösen nagy adatállományok esetén gyakran tanácsosabb egyszerűen eltávolítani a hiányzó [NA] értékeket az elemzésből, mint más módon kezelni őket.) Nézzük meg ezt a gyakorlatban az `example1`-re visszatérve:
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
Figyeld meg, hogy ez hasonlít az `example3[example3.notnull()]` kimenetére. A különbség itt az, hogy a maszkolt értékek indexelése helyett a `dropna` eltávolította a hiányzó értékeket az `example1` `Series`-ből.

Mivel a `DataFrame`-eknek két dimenziója van, több lehetőséget kínálnak az adatok eltávolítására.

```python
example2 = pd.DataFrame([[1,      np.nan, 7], 
                         [2,      5,      8], 
                         [np.nan, 6,      9]])
example2
```
|      | 0 | 1 | 2 |
|------|---|---|---|
|0     |1.0|NaN|7  |
|1     |2.0|5.0|8  |
|2     |NaN|6.0|9  |

(Észrevetted, hogy a pandas két oszlopot lebegőpontokká alakított, hogy kezelje a `NaN`-okat?)

Egyetlen értéket nem tudsz eltávolítani egy `DataFrame`-ből, így teljes sorokat vagy oszlopokat kell eltávolítanod. Attól függően, hogy mit csinálsz, lehet, hogy az egyiket vagy a másikat szeretnéd, és a pandas mindkettőre lehetőséget kínál. Mivel az adatelemzésben az oszlopok általában változókat, a sorok pedig megfigyeléseket képviselnek, valószínűbb, hogy sorokat távolítasz el; a `dropna()` alapértelmezett beállítása az összes null értéket tartalmazó sorok eltávolítása:

```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```
Ha szükséges, eltávolíthatod az NA értékeket az oszlopokból. Használd az `axis=1` beállítást ehhez:
```python
example2.dropna(axis='columns')
```
```
	2
0	7
1	8
2	9
```
Figyeld meg, hogy ez sok olyan adatot eltávolíthat, amelyet meg szeretnél tartani, különösen kisebb adatállományok esetén. Mi van, ha csak azokat a sorokat vagy oszlopokat szeretnéd eltávolítani, amelyek több vagy akár minden null értéket tartalmaznak? Ezeket a beállításokat a `dropna` metódusban a `how` és `thresh` paraméterekkel adhatod meg.

Alapértelmezés szerint `how='any'` (ha szeretnéd ellenőrizni magad, vagy megnézni, milyen más paraméterek vannak a metódusban, futtasd az `example4.dropna?` parancsot egy kódcellában). Alternatívaként megadhatod a `how='all'` beállítást, hogy csak azokat a sorokat vagy oszlopokat távolítsd el, amelyek minden null értéket tartalmaznak. Bővítsük ki az `example` `DataFrame`-et, hogy ezt gyakorlatban lássuk.

```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

A `thresh` paraméter finomabb vezérlést biztosít: beállíthatod a sor vagy oszlop megtartásához szükséges *nem null* értékek számát:
```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```
Itt az első és utolsó sorokat eltávolították, mert csak két nem null értéket tartalmaztak.

- **Null értékek kitöltése**: Az adatállománytól függően néha értelmesebb lehet a null értékeket érvényesekkel kitölteni, mint eltávolítani őket. Az `isnull` segítségével helyben is megteheted ezt, de ez fárasztó lehet, különösen, ha sok értéket kell kitöltened. Mivel ez az adatelemzésben gyakori feladat, a pandas biztosítja a `fillna` metódust, amely visszaadja a `Series` vagy `DataFrame` másolatát, amelyben a hiányzó értékek az általad választott értékkel vannak helyettesítve. Hozzunk létre egy másik `Series` példát, hogy lássuk, hogyan működik ez a gyakorlatban.
```python
example3 = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
example3
```
```
a    1.0
b    NaN
c    2.0
d    NaN
e    3.0
dtype: float64
```
Kitöltheted az összes null bejegyzést egyetlen értékkel, például `0`-val:
```python
example3.fillna(0)
```
```
a    1.0
b    0.0
c    2.0
d    0.0
e    3.0
dtype: float64
```
Kitöltheted a null értékeket **előre kitöltéssel**, azaz az utolsó érvényes értékkel:
```python
example3.fillna(method='ffill')
```
```
a    1.0
b    1.0
c    2.0
d    2.0
e    3.0
dtype: float64
```
Kitöltheted **hátra kitöltéssel** is, azaz a következő érvényes értéket visszafelé propagálva:
```python
example3.fillna(method='bfill')
```
```
a    1.0
b    2.0
c    2.0
d    3.0
e    3.0
dtype: float64
```
Ahogy sejtheted, ez ugyanígy működik a `DataFrame`-ekkel, de megadhatod az `axis`-t is, amely mentén kitöltöd a null értékeket.
> **Tanulság:** Számos módja van annak, hogy kezeljük a hiányzó értékeket az adatállományainkban. Az alkalmazott konkrét stratégia (eltávolítás, helyettesítés, vagy akár a helyettesítés módja) az adott adatok sajátosságaitól függ. Minél többet dolgozol és foglalkozol adatállományokkal, annál jobb érzéket fejlesztesz ki a hiányzó értékek kezelésére.
## Duplikált adatok eltávolítása

> **Tanulási cél:** Ennek az alfejezetnek a végére képesnek kell lenned azonosítani és eltávolítani a duplikált értékeket a DataFrame-ekből.

A hiányzó adatok mellett gyakran találkozhatsz duplikált adatokkal is a valós adatállományokban. Szerencsére a `pandas` egyszerű eszközt biztosít a duplikált bejegyzések felismerésére és eltávolítására.

- **Duplikátumok azonosítása: `duplicated`**: A `duplicated` metódus segítségével könnyen felismerheted a duplikált értékeket. Ez egy logikai maszkot ad vissza, amely jelzi, hogy egy `DataFrame` bejegyzése megegyezik-e egy korábbi bejegyzéssel. Hozzunk létre egy újabb példát egy `DataFrame`-re, hogy lássuk ezt működés közben.
```python
example4 = pd.DataFrame({'letters': ['A','B'] * 2 + ['B'],
                         'numbers': [1, 2, 1, 3, 3]})
example4
```
|      |betűk  |számok |
|------|-------|-------|
|0     |A      |1      |
|1     |B      |2      |
|2     |A      |1      |
|3     |B      |3      |
|4     |B      |3      |

```python
example4.duplicated()
```
```
0    False
1    False
2     True
3    False
4     True
dtype: bool
```
- **Duplikátumok eltávolítása: `drop_duplicates`:** egyszerűen visszaadja azokat az adatokat, amelyeknél az összes `duplicated` érték `False`:
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
Mind a `duplicated`, mind a `drop_duplicates` alapértelmezés szerint az összes oszlopot figyelembe veszi, de megadhatod, hogy csak az `DataFrame` egy részhalmazát vizsgálják:
```python
example4.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **Fontos tanulság:** A duplikált adatok eltávolítása szinte minden adat-tudományi projekt alapvető része. A duplikált adatok megváltoztathatják az elemzéseid eredményeit, és pontatlan eredményeket adhatnak!


## 🚀 Kihívás

Az összes tárgyalt anyag elérhető egy [Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb) formájában. Ezenkívül minden szakasz után találhatók gyakorlatok, próbáld ki őket!

## [Előadás utáni kvíz](https://ff-quizzes.netlify.app/en/ds/quiz/15)



## Áttekintés és önálló tanulás

Számos módja van annak, hogy felfedezd és megközelítsd az adatok előkészítését elemzéshez és modellezéshez, és az adatok tisztítása egy fontos lépés, amely "gyakorlati" tapasztalatot igényel. Próbáld ki ezeket a Kaggle kihívásokat, hogy felfedezd azokat a technikákat, amelyeket ez a lecke nem tárgyalt.

- [Adattisztítási kihívás: Dátumok elemzése](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [Adattisztítási kihívás: Adatok skálázása és normalizálása](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)


## Feladat

[Adatok értékelése egy űrlapról](assignment.md)

---

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális, emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.