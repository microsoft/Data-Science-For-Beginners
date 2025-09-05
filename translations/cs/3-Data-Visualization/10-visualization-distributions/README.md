<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a20467e046d312809d008395051fc7",
  "translation_date": "2025-09-05T17:53:01+00:00",
  "source_file": "3-Data-Visualization/10-visualization-distributions/README.md",
  "language_code": "cs"
}
-->
# Vizualizace distribucí

|![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| Vizualizace distribucí - _Sketchnote od [@nitya](https://twitter.com/nitya)_ |

V předchozí lekci jste se dozvěděli zajímavé informace o datové sadě o ptácích z Minnesoty. Našli jste chybné údaje vizualizací odlehlých hodnot a podívali jste se na rozdíly mezi kategoriemi ptáků podle jejich maximální délky.

## [Kvíz před lekcí](https://ff-quizzes.netlify.app/en/ds/quiz/18)
## Prozkoumejte datovou sadu ptáků

Dalším způsobem, jak se ponořit do dat, je podívat se na jejich distribuci, tedy na to, jak jsou data uspořádána podél osy. Možná by vás například zajímalo, jaká je obecná distribuce maximálního rozpětí křídel nebo maximální tělesné hmotnosti ptáků z Minnesoty v této datové sadě.

Pojďme objevit některá fakta o distribucích dat v této datové sadě. V souboru _notebook.ipynb_ v kořenové složce této lekce importujte Pandas, Matplotlib a vaše data:

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```

|      | Název                        | VědeckýNázev           | Kategorie             | Řád          | Čeleď    | Rod         | StavOchrany         | MinDélka  | MaxDélka  | MinHmotnost | MaxHmotnost | MinRozpětí  | MaxRozpětí  |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Černobřichá pižmovka         | Dendrocygna autumnalis | Kachny/Husy/Vodní ptáci | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Pižmovka rezavá              | Dendrocygna bicolor    | Kachny/Husy/Vodní ptáci | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Sněžná husa                  | Anser caerulescens     | Kachny/Husy/Vodní ptáci | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Rossova husa                 | Anser rossii           | Kachny/Husy/Vodní ptáci | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Husa běločelá                | Anser albifrons        | Kachny/Husy/Vodní ptáci | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

Obecně můžete rychle zjistit, jak jsou data distribuována, pomocí bodového grafu, jak jsme to udělali v předchozí lekci:

```python
birds.plot(kind='scatter',x='MaxLength',y='Order',figsize=(12,8))

plt.title('Max Length per Order')
plt.ylabel('Order')
plt.xlabel('Max Length')

plt.show()
```
![max délka podle řádu](../../../../3-Data-Visualization/10-visualization-distributions/images/scatter-wb.png)

Toto poskytuje přehled o obecné distribuci délky těla podle řádu ptáků, ale není to optimální způsob zobrazení skutečných distribucí. Tento úkol obvykle řeší vytvoření histogramu.
## Práce s histogramy

Matplotlib nabízí velmi dobré způsoby vizualizace distribuce dat pomocí histogramů. Tento typ grafu je podobný sloupcovému grafu, kde distribuci lze vidět prostřednictvím vzestupu a poklesu sloupců. K vytvoření histogramu potřebujete číselná data. K vytvoření histogramu můžete vykreslit graf, kde definujete typ jako 'hist' pro histogram. Tento graf ukazuje distribuci MaxBodyMass pro celý rozsah číselných dat v datové sadě. Rozdělením pole dat na menší biny může zobrazit distribuci hodnot dat:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 10, figsize = (12,12))
plt.show()
```
![distribuce přes celou datovou sadu](../../../../3-Data-Visualization/10-visualization-distributions/images/dist1-wb.png)

Jak vidíte, většina z více než 400 ptáků v této datové sadě spadá do rozsahu pod 2000 pro jejich maximální tělesnou hmotnost. Získejte více informací o datech změnou parametru `bins` na vyšší číslo, například 30:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 30, figsize = (12,12))
plt.show()
```
![distribuce přes celou datovou sadu s větším parametrem bins](../../../../3-Data-Visualization/10-visualization-distributions/images/dist2-wb.png)

Tento graf ukazuje distribuci trochu podrobněji. Méně zkreslený graf doleva by mohl být vytvořen tím, že zajistíte, že vyberete pouze data v daném rozsahu:

Filtrovat data tak, aby obsahovala pouze ptáky, jejichž tělesná hmotnost je pod 60, a zobrazit 40 `bins`:

```python
filteredBirds = birds[(birds['MaxBodyMass'] > 1) & (birds['MaxBodyMass'] < 60)]      
filteredBirds['MaxBodyMass'].plot(kind = 'hist',bins = 40,figsize = (12,12))
plt.show()     
```
![filtrovaný histogram](../../../../3-Data-Visualization/10-visualization-distributions/images/dist3-wb.png)

✅ Vyzkoušejte některé další filtry a datové body. Chcete-li zobrazit plnou distribuci dat, odstraňte filtr `['MaxBodyMass']`, aby se zobrazily označené distribuce.

Histogram nabízí také některá pěkná vylepšení barev a označení, která můžete vyzkoušet:

Vytvořte 2D histogram pro porovnání vztahu mezi dvěma distribucemi. Porovnejme `MaxBodyMass` vs. `MaxLength`. Matplotlib nabízí vestavěný způsob zobrazení konvergence pomocí jasnějších barev:

```python
x = filteredBirds['MaxBodyMass']
y = filteredBirds['MaxLength']

fig, ax = plt.subplots(tight_layout=True)
hist = ax.hist2d(x, y)
```
Zdá se, že mezi těmito dvěma prvky existuje očekávaná korelace podél očekávané osy, s jedním obzvláště silným bodem konvergence:

![2D graf](../../../../3-Data-Visualization/10-visualization-distributions/images/2D-wb.png)

Histogramy fungují dobře ve výchozím nastavení pro číselná data. Co když potřebujete vidět distribuce podle textových dat? 
## Prozkoumejte datovou sadu pro distribuce pomocí textových dat 

Tato datová sada také obsahuje dobré informace o kategorii ptáků, jejich rodu, druhu a čeledi, stejně jako o jejich stavu ochrany. Pojďme se ponořit do těchto informací o ochraně. Jaká je distribuce ptáků podle jejich stavu ochrany?

> ✅ V datové sadě je použito několik zkratek k popisu stavu ochrany. Tyto zkratky pocházejí z [IUCN Red List Categories](https://www.iucnredlist.org/), organizace, která katalogizuje stav druhů.
> 
> - CR: Kriticky ohrožený
> - EN: Ohrožený
> - EX: Vyhynulý
> - LC: Nejmenší obavy
> - NT: Téměř ohrožený
> - VU: Zranitelný

Jedná se o textové hodnoty, takže budete muset provést transformaci, abyste vytvořili histogram. Pomocí dataframe `filteredBirds` zobrazte jeho stav ochrany vedle jeho minimálního rozpětí křídel. Co vidíte? 

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

![rozpětí křídel a kolace stavu ochrany](../../../../3-Data-Visualization/10-visualization-distributions/images/histogram-conservation-wb.png)

Zdá se, že mezi minimálním rozpětím křídel a stavem ochrany není dobrá korelace. Otestujte další prvky datové sady pomocí této metody. Můžete také vyzkoušet různé filtry. Najdete nějakou korelaci?

## Hustotní grafy

Možná jste si všimli, že histogramy, které jsme dosud viděli, jsou "krokové" a neplynou hladce v oblouku. Chcete-li zobrazit hladší hustotní graf, můžete zkusit hustotní graf.

Pro práci s hustotními grafy se seznamte s novou knihovnou pro vykreslování, [Seaborn](https://seaborn.pydata.org/generated/seaborn.kdeplot.html). 

Načtením Seaborn zkuste základní hustotní graf:

```python
import seaborn as sns
import matplotlib.pyplot as plt
sns.kdeplot(filteredBirds['MinWingspan'])
plt.show()
```
![Hustotní graf](../../../../3-Data-Visualization/10-visualization-distributions/images/density1.png)

Vidíte, jak graf odráží ten předchozí pro data o minimálním rozpětí křídel; je jen o něco hladší. Podle dokumentace Seaborn, "Ve srovnání s histogramem může KDE vytvořit graf, který je méně přeplněný a lépe interpretovatelný, zejména při vykreslování více distribucí. Ale má potenciál zavést zkreslení, pokud je základní distribuce ohraničená nebo není hladká. Stejně jako histogram kvalita reprezentace také závisí na výběru dobrých parametrů vyhlazení." [zdroj](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) Jinými slovy, odlehlé hodnoty jako vždy způsobí, že se vaše grafy budou chovat špatně.

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

✅ Přečtěte si o dostupných parametrech pro tento typ grafu a experimentujte!

Tento typ grafu nabízí krásně vysvětlující vizualizace. S několika řádky kódu můžete například zobrazit hustotu maximální tělesné hmotnosti podle řádu ptáků:

```python
sns.kdeplot(
   data=filteredBirds, x="MaxBodyMass", hue="Order",
   fill=True, common_norm=False, palette="crest",
   alpha=.5, linewidth=0,
)
```

![tělesná hmotnost podle řádu](../../../../3-Data-Visualization/10-visualization-distributions/images/density4.png)

Můžete také mapovat hustotu několika proměnných v jednom grafu. Otestujte maximální a minimální délku ptáka ve srovnání s jeho stavem ochrany:

```python
sns.kdeplot(data=filteredBirds, x="MinLength", y="MaxLength", hue="ConservationStatus")
```

![více hustot, překryté](../../../../3-Data-Visualization/10-visualization-distributions/images/multi.png)

Možná stojí za to prozkoumat, zda je shluk "zranitelných" ptáků podle jejich délek významný nebo ne.

## 🚀 Výzva

Histogramy jsou sofistikovanějším typem grafu než základní bodové grafy, sloupcové grafy nebo čárové grafy. Vyhledejte na internetu dobré příklady použití histogramů. Jak se používají, co ukazují a v jakých oborech nebo oblastech výzkumu se obvykle používají?

## [Kvíz po lekci](https://ff-quizzes.netlify.app/en/ds/quiz/19)

## Přehled & Samostudium

V této lekci jste použili Matplotlib a začali pracovat se Seabornem, abyste vytvořili sofistikovanější grafy. Proveďte výzkum o `kdeplot` v Seabornu, "kontinuální křivce hustoty pravděpodobnosti v jedné nebo více dimenzích". Přečtěte si [dokumentaci](https://seaborn.pydata.org/generated/seaborn.kdeplot.html), abyste pochopili, jak funguje.

## Úkol

[Uplatněte své dovednosti](assignment.md)

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.