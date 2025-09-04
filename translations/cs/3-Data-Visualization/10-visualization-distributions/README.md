<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "02ce904bc1e2bfabb7dc05c25aae375c",
  "translation_date": "2025-09-04T21:47:27+00:00",
  "source_file": "3-Data-Visualization/10-visualization-distributions/README.md",
  "language_code": "cs"
}
-->
# Vizualizace distribucí

|![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| Vizualizace distribucí - _Sketchnote od [@nitya](https://twitter.com/nitya)_ |

V předchozí lekci jste se dozvěděli několik zajímavých faktů o datasetu o ptácích z Minnesoty. Objevili jste chybná data vizualizací odlehlých hodnot a podívali jste se na rozdíly mezi kategoriemi ptáků podle jejich maximální délky.

## [Kvíz před lekcí](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/18)
## Prozkoumejte dataset ptáků

Dalším způsobem, jak se ponořit do dat, je podívat se na jejich distribuci, tedy jak jsou data uspořádána podél osy. Možná byste například chtěli zjistit obecnou distribuci maximálního rozpětí křídel nebo maximální tělesné hmotnosti ptáků z Minnesoty v tomto datasetu.

Pojďme objevit některá fakta o distribucích dat v tomto datasetu. V souboru _notebook.ipynb_ v kořenové složce této lekce importujte Pandas, Matplotlib a svá data:

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```

|      | Název                        | VědeckýNázev           | Kategorie             | Řád          | Čeleď    | Rod         | StavOchrany         | MinDélka | MaxDélka | MinHmotnost | MaxHmotnost | MinRozpětí | MaxRozpětí |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :------------------ | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Čírka černobřichá            | Dendrocygna autumnalis | Kachny/Husy/Vodní ptáci | Anseriformes | Anatidae | Dendrocygna | LC                  |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Čírka rezavá                 | Dendrocygna bicolor    | Kachny/Husy/Vodní ptáci | Anseriformes | Anatidae | Dendrocygna | LC                  |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Husa sněžní                  | Anser caerulescens     | Kachny/Husy/Vodní ptáci | Anseriformes | Anatidae | Anser       | LC                  |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Husa Rossova                 | Anser rossii           | Kachny/Husy/Vodní ptáci | Anseriformes | Anatidae | Anser       | LC                  |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Husa běločelá                | Anser albifrons        | Kachny/Husy/Vodní ptáci | Anseriformes | Anatidae | Anser       | LC                  |        64 |        81 |        1930 |        3310 |         130 |         165 |

Obecně můžete rychle nahlédnout na způsob, jakým jsou data distribuována, pomocí bodového grafu, jak jsme to udělali v předchozí lekci:

```python
birds.plot(kind='scatter',x='MaxLength',y='Order',figsize=(12,8))

plt.title('Max Length per Order')
plt.ylabel('Order')
plt.xlabel('Max Length')

plt.show()
```
![maximální délka podle řádu](../../../../3-Data-Visualization/10-visualization-distributions/images/scatter-wb.png)

Tento graf poskytuje přehled o obecné distribuci délky těla podle řádu ptáků, ale není to optimální způsob, jak zobrazit skutečné distribuce. Tento úkol obvykle řeší histogram.

## Práce s histogramy

Matplotlib nabízí velmi dobré způsoby vizualizace distribuce dat pomocí histogramů. Tento typ grafu je podobný sloupcovému grafu, kde distribuci lze vidět prostřednictvím růstu a poklesu sloupců. Pro vytvoření histogramu potřebujete číselná data. Pro vytvoření histogramu můžete vykreslit graf s definovaným typem 'hist' pro histogram. Tento graf ukazuje distribuci MaxBodyMass pro celý rozsah číselných dat v datasetu. Rozdělením pole dat na menší intervaly (bins) může zobrazit distribuci hodnot dat:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 10, figsize = (12,12))
plt.show()
```
![distribuce v celém datasetu](../../../../3-Data-Visualization/10-visualization-distributions/images/dist1-wb.png)

Jak vidíte, většina z více než 400 ptáků v tomto datasetu spadá do rozsahu pod 2000 pro jejich maximální tělesnou hmotnost. Získejte více informací o datech změnou parametru `bins` na vyšší číslo, například 30:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 30, figsize = (12,12))
plt.show()
```
![distribuce v celém datasetu s větším parametrem bins](../../../../3-Data-Visualization/10-visualization-distributions/images/dist2-wb.png)

Tento graf ukazuje distribuci trochu podrobněji. Méně zkreslený graf by mohl být vytvořen tím, že vyberete pouze data v daném rozsahu:

Filtrovat data tak, aby obsahovala pouze ptáky s tělesnou hmotností pod 60, a zobrazit 40 `bins`:

```python
filteredBirds = birds[(birds['MaxBodyMass'] > 1) & (birds['MaxBodyMass'] < 60)]      
filteredBirds['MaxBodyMass'].plot(kind = 'hist',bins = 40,figsize = (12,12))
plt.show()     
```
![filtrovaný histogram](../../../../3-Data-Visualization/10-visualization-distributions/images/dist3-wb.png)

✅ Vyzkoušejte další filtry a datové body. Chcete-li zobrazit úplnou distribuci dat, odstraňte filtr `['MaxBodyMass']`, abyste zobrazili označené distribuce.

Histogram nabízí také pěkná vylepšení barev a popisků:

Vytvořte 2D histogram pro porovnání vztahu mezi dvěma distribucemi. Porovnejme `MaxBodyMass` vs. `MaxLength`. Matplotlib nabízí vestavěný způsob, jak zobrazit konvergenci pomocí jasnějších barev:

```python
x = filteredBirds['MaxBodyMass']
y = filteredBirds['MaxLength']

fig, ax = plt.subplots(tight_layout=True)
hist = ax.hist2d(x, y)
```
Zdá se, že mezi těmito dvěma prvky existuje očekávaná korelace podél očekávané osy, s jedním obzvláště silným bodem konvergence:

![2D graf](../../../../3-Data-Visualization/10-visualization-distributions/images/2D-wb.png)

Histogramy fungují dobře pro číselná data. Co když ale potřebujete vidět distribuce podle textových dat? 
## Prozkoumejte dataset pro distribuce pomocí textových dat 

Tento dataset také obsahuje dobré informace o kategorii ptáků, jejich rodu, druhu, čeledi a stavu ochrany. Pojďme se ponořit do těchto informací o ochraně. Jaká je distribuce ptáků podle jejich stavu ochrany?

> ✅ V datasetu je použito několik zkratek k popisu stavu ochrany. Tyto zkratky pocházejí z [IUCN Red List Categories](https://www.iucnredlist.org/), organizace, která katalogizuje stav druhů.
> 
> - CR: Kriticky ohrožený
> - EN: Ohrožený
> - EX: Vyhynulý
> - LC: Nejmenší obavy
> - NT: Téměř ohrožený
> - VU: Zranitelný

Jedná se o textové hodnoty, takže budete muset provést transformaci, abyste vytvořili histogram. Pomocí dataframe `filteredBirds` zobrazte jeho stav ochrany spolu s minimálním rozpětím křídel. Co vidíte? 

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

![rozpětí křídel a stav ochrany](../../../../3-Data-Visualization/10-visualization-distributions/images/histogram-conservation-wb.png)

Zdá se, že mezi minimálním rozpětím křídel a stavem ochrany není dobrá korelace. Otestujte další prvky datasetu pomocí této metody. Můžete také vyzkoušet různé filtry. Najdete nějakou korelaci?

## Hustotní grafy

Možná jste si všimli, že histogramy, které jsme dosud viděli, jsou „schodovité“ a nepřecházejí plynule do oblouku. Pro zobrazení hladšího hustotního grafu můžete vyzkoušet hustotní graf.

Pro práci s hustotními grafy se seznamte s novou knihovnou pro vykreslování, [Seaborn](https://seaborn.pydata.org/generated/seaborn.kdeplot.html). 

Načtením Seaborn zkuste základní hustotní graf:

```python
import seaborn as sns
import matplotlib.pyplot as plt
sns.kdeplot(filteredBirds['MinWingspan'])
plt.show()
```
![Hustotní graf](../../../../3-Data-Visualization/10-visualization-distributions/images/density1.png)

Vidíte, jak graf odráží ten předchozí pro data o minimálním rozpětí křídel; je jen trochu hladší. Podle dokumentace Seaborn: „Ve srovnání s histogramem může KDE vytvořit graf, který je méně přeplněný a lépe interpretovatelný, zejména při vykreslování více distribucí. Ale má potenciál zavádět zkreslení, pokud je základní distribuce ohraničená nebo není hladká. Stejně jako histogram kvalita reprezentace také závisí na výběru dobrých parametrů vyhlazování." [zdroj](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) Jinými slovy, odlehlé hodnoty, jako vždy, způsobí, že se vaše grafy budou chovat špatně.

Pokud byste chtěli znovu navštívit tu zubatou linii MaxBodyMass v druhém grafu, který jste vytvořili, mohli byste ji velmi dobře vyhladit tím, že ji znovu vytvoříte pomocí této metody:

```python
sns.kdeplot(filteredBirds['MaxBodyMass'])
plt.show()
```
![hladká linie tělesné hmotnosti](../../../../3-Data-Visualization/10-visualization-distributions/images/density2.png)

Pokud byste chtěli hladkou, ale ne příliš hladkou linii, upravte parametr `bw_adjust`: 

```python
sns.kdeplot(filteredBirds['MaxBodyMass'], bw_adjust=.2)
plt.show()
```
![méně hladká linie tělesné hmotnosti](../../../../3-Data-Visualization/10-visualization-distributions/images/density3.png)

✅ Přečtěte si o parametrech dostupných pro tento typ grafu a experimentujte!

Tento typ grafu nabízí krásně vysvětlující vizualizace. S několika řádky kódu můžete například zobrazit hustotu maximální tělesné hmotnosti podle řádu ptáků:

```python
sns.kdeplot(
   data=filteredBirds, x="MaxBodyMass", hue="Order",
   fill=True, common_norm=False, palette="crest",
   alpha=.5, linewidth=0,
)
```

![tělesná hmotnost podle řádu](../../../../3-Data-Visualization/10-visualization-distributions/images/density4.png)

Můžete také mapovat hustotu několika proměnných v jednom grafu. Otestujte maximální a minimální délku ptáka ve srovnání s jejich stavem ochrany:

```python
sns.kdeplot(data=filteredBirds, x="MinLength", y="MaxLength", hue="ConservationStatus")
```

![více hustot, překryté](../../../../3-Data-Visualization/10-visualization-distributions/images/multi.png)

Možná stojí za to prozkoumat, zda je shluk „zranitelných“ ptáků podle jejich délek významný nebo ne.

## 🚀 Výzva

Histogramy jsou sofistikovanější typ grafu než základní bodové grafy, sloupcové grafy nebo čárové grafy. Vyhledejte na internetu dobré příklady použití histogramů. Jak se používají, co ukazují a v jakých oborech nebo oblastech výzkumu se obvykle používají?

## [Kvíz po lekci](https://ff-quizzes.netlify.app/en/ds/)

## Přehled a samostudium

V této lekci jste použili Matplotlib a začali pracovat se Seaborn pro zobrazení sofistikovanějších grafů. Proveďte výzkum o `kdeplot` v Seaborn, „kontinuální křivce hustoty pravděpodobnosti v jedné nebo více dimenzích“. Přečtěte si [dokumentaci](https://seaborn.pydata.org/generated/seaborn.kdeplot.html), abyste pochopili, jak funguje.

## Zadání

[Uplatněte své dovednosti](assignment.md)

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o co největší přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Za autoritativní zdroj by měl být považován původní dokument v jeho původním jazyce. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.