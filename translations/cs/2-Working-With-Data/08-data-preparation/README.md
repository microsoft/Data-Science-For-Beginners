<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1b560955ff39a2bcf2a049fce474a951",
  "translation_date": "2025-09-05T17:47:16+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "cs"
}
-->
# Práce s daty: Příprava dat

|![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|Příprava dat - _Sketchnote od [@nitya](https://twitter.com/nitya)_ |

## [Kvíz před lekcí](https://ff-quizzes.netlify.app/en/ds/quiz/14)

V závislosti na zdroji mohou surová data obsahovat určité nesrovnalosti, které způsobí problémy při analýze a modelování. Jinými slovy, tato data mohou být označena jako „špinavá“ a bude je třeba vyčistit. Tato lekce se zaměřuje na techniky čištění a transformace dat, aby bylo možné řešit problémy s chybějícími, nepřesnými nebo neúplnými daty. Témata probíraná v této lekci využívají Python a knihovnu Pandas a budou [demonstrována v notebooku](../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb) v tomto adresáři.

## Důležitost čištění dat

- **Snadné použití a opětovné použití**: Když jsou data správně organizována a normalizována, je snazší je vyhledávat, používat a sdílet s ostatními.

- **Konzistence**: Datová věda často vyžaduje práci s více datovými sadami, kde je třeba spojit datové sady z různých zdrojů. Zajištění, že každá jednotlivá datová sada má společnou standardizaci, zajistí, že data budou stále užitečná, když budou sloučena do jedné datové sady.

- **Přesnost modelu**: Vyčištěná data zlepšují přesnost modelů, které na nich závisí.

## Běžné cíle a strategie čištění

- **Prozkoumání datové sady**: Prozkoumání dat, které je pokryto v [pozdější lekci](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing), vám může pomoci objevit data, která je třeba vyčistit. Vizualizace hodnot v datové sadě může nastavit očekávání, jak bude vypadat zbytek, nebo poskytnout představu o problémech, které lze vyřešit. Prozkoumání může zahrnovat základní dotazování, vizualizace a vzorkování.

- **Formátování**: V závislosti na zdroji mohou data obsahovat nesrovnalosti v tom, jak jsou prezentována. To může způsobit problémy při hledání a reprezentaci hodnoty, kde je vidět v datové sadě, ale není správně reprezentována ve vizualizacích nebo výsledcích dotazů. Běžné problémy s formátováním zahrnují řešení mezer, dat a typů dat. Řešení problémů s formátováním obvykle závisí na lidech, kteří data používají. Například standardy, jak jsou prezentována data a čísla, se mohou lišit podle země.

- **Duplicitní data**: Data, která se vyskytují vícekrát, mohou produkovat nepřesné výsledky a obvykle by měla být odstraněna. To může být běžné při spojování dvou nebo více datových sad dohromady. Existují však případy, kdy duplikace v spojených datových sadách obsahují části, které mohou poskytovat další informace a mohou být zachovány.

- **Chybějící data**: Chybějící data mohou způsobit nepřesnosti, slabé nebo zaujaté výsledky. Někdy je možné je vyřešit „znovunačtením“ dat, doplněním chybějících hodnot výpočtem a kódem, například v Pythonu, nebo jednoduše odstraněním hodnoty a odpovídajících dat. Existuje mnoho důvodů, proč data mohou chybět, a kroky, které jsou podniknuty k jejich vyřešení, mohou záviset na tom, jak a proč chyběla.

## Prozkoumání informací o DataFrame
> **Cíl učení:** Na konci této podsekce byste měli být schopni najít obecné informace o datech uložených v pandas DataFrames.

Jakmile načtete svá data do pandas, pravděpodobně budou ve formátu DataFrame (viz předchozí [lekce](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe) pro podrobný přehled). Pokud však datová sada ve vašem DataFrame obsahuje 60 000 řádků a 400 sloupců, jak vůbec začít získávat představu o tom, s čím pracujete? Naštěstí [pandas](https://pandas.pydata.org/) poskytuje několik praktických nástrojů, jak rychle získat celkové informace o DataFrame, kromě prvních a posledních několika řádků.

Abychom prozkoumali tuto funkčnost, importujeme knihovnu Python scikit-learn a použijeme ikonickou datovou sadu: **Iris data set**.

```python
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
iris_df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
```
|                                        |sepal length (cm)|sepal width (cm)|petal length (cm)|petal width (cm)|
|----------------------------------------|-----------------|----------------|-----------------|----------------|
|0                                       |5.1              |3.5             |1.4              |0.2             |
|1                                       |4.9              |3.0             |1.4              |0.2             |
|2                                       |4.7              |3.2             |1.3              |0.2             |
|3                                       |4.6              |3.1             |1.5              |0.2             |
|4                                       |5.0              |3.6             |1.4              |0.2             |

- **DataFrame.info**: Na začátek se používá metoda `info()` k vytištění souhrnu obsahu přítomného v `DataFrame`. Podívejme se na tuto datovou sadu, abychom zjistili, co máme:
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
Z toho víme, že datová sada *Iris* má 150 záznamů ve čtyřech sloupcích bez nulových záznamů. Všechna data jsou uložena jako 64bitová čísla s plovoucí desetinnou čárkou.

- **DataFrame.head()**: Dále, abychom zkontrolovali skutečný obsah `DataFrame`, použijeme metodu `head()`. Podívejme se, jak vypadají první řádky našeho `iris_df`:
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
- **DataFrame.tail()**: Naopak, abychom zkontrolovali poslední řádky `DataFrame`, použijeme metodu `tail()`:
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
> **Shrnutí:** Už jen pohledem na metadata o informacích v DataFrame nebo na první a poslední hodnoty v něm můžete okamžitě získat představu o velikosti, tvaru a obsahu dat, se kterými pracujete.

## Řešení chybějících dat
> **Cíl učení:** Na konci této podsekce byste měli vědět, jak nahradit nebo odstranit nulové hodnoty z DataFrames.

Většinou datové sady, které chcete použít (nebo musíte použít), obsahují chybějící hodnoty. Způsob, jakým se chybějící data řeší, s sebou nese jemné kompromisy, které mohou ovlivnit vaši konečnou analýzu a výsledky v reálném světě.

Pandas řeší chybějící hodnoty dvěma způsoby. První jste již viděli v předchozích sekcích: `NaN`, neboli Not a Number. Toto je speciální hodnota, která je součástí specifikace IEEE pro čísla s plovoucí desetinnou čárkou a používá se pouze k označení chybějících hodnot s plovoucí desetinnou čárkou.

Pro chybějící hodnoty kromě čísel s plovoucí desetinnou čárkou používá pandas objekt Python `None`. I když se může zdát matoucí, že narazíte na dva různé typy hodnot, které říkají v podstatě totéž, existují rozumné programové důvody pro toto designové rozhodnutí a v praxi tento přístup umožňuje pandas nabídnout dobrý kompromis pro drtivou většinu případů. Přesto obě `None` a `NaN` mají omezení, která je třeba mít na paměti, pokud jde o jejich použití.

Podívejte se na více informací o `NaN` a `None` v [notebooku](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb)!

- **Detekce nulových hodnot**: V `pandas` jsou vaše primární metody pro detekci nulových dat `isnull()` a `notnull()`. Obě vracejí Booleovské masky nad vašimi daty. Budeme používat `numpy` pro hodnoty `NaN`:
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
Pozorně se podívejte na výstup. Překvapilo vás něco? Zatímco `0` je aritmetická nula, je to přesto zcela platné celé číslo a pandas ho takto považuje. `''` je trochu jemnější. I když jsme ho použili v sekci 1 k reprezentaci prázdné hodnoty řetězce, je to přesto objekt řetězce a není to reprezentace nuly, pokud jde o pandas.

Nyní to otočme a použijme tyto metody způsobem, jakým je budete používat v praxi. Booleovské masky můžete použít přímo jako index `Series` nebo `DataFrame`, což může být užitečné při práci s izolovanými chybějícími (nebo přítomnými) hodnotami.

> **Shrnutí**: Metody `isnull()` a `notnull()` produkují podobné výsledky, když je použijete v `DataFrame`: zobrazují výsledky a index těchto výsledků, což vám velmi pomůže při práci s vašimi daty.

- **Odstranění nulových hodnot**: Kromě identifikace chybějících hodnot poskytuje pandas pohodlný způsob, jak odstranit nulové hodnoty z `Series` a `DataFrame`. (Zvláště u velkých datových sad je často vhodnější jednoduše odstranit chybějící [NA] hodnoty z vaší analýzy než se s nimi vypořádávat jinými způsoby.) Abychom to viděli v praxi, vraťme se k `example1`:
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
Všimněte si, že by to mělo vypadat jako váš výstup z `example3[example3.notnull()]`. Rozdíl zde je, že místo indexování na maskované hodnoty `dropna` odstranil tyto chybějící hodnoty z `Series` `example1`.

Protože `DataFrame` má dvě dimenze, nabízí více možností pro odstranění dat.

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

(Všimli jste si, že pandas převedl dva sloupce na čísla s plovoucí desetinnou čárkou, aby vyhověl hodnotám `NaN`?)

Nemůžete odstranit jednu hodnotu z `DataFrame`, takže musíte odstranit celé řádky nebo sloupce. V závislosti na tom, co děláte, můžete chtít udělat jedno nebo druhé, a pandas vám dává možnosti pro obojí. Protože ve vědě o datech sloupce obecně představují proměnné a řádky představují pozorování, je pravděpodobnější, že odstraníte řádky dat; výchozí nastavení pro `dropna()` je odstranit všechny řádky, které obsahují jakékoli nulové hodnoty:

```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```
Pokud je to nutné, můžete odstranit hodnoty NA ze sloupců. Použijte `axis=1` k tomu:
```python
example2.dropna(axis='columns')
```
```
	2
0	7
1	8
2	9
```
Všimněte si, že to může odstranit hodně dat, která byste chtěli zachovat, zejména v menších datových sadách. Co když chcete odstranit pouze řádky nebo sloupce, které obsahují několik nebo dokonce všechny nulové hodnoty? Tyto nastavení můžete specifikovat v `dropna` pomocí parametrů `how` a `thresh`.

Ve výchozím nastavení je `how='any'` (pokud byste si to chtěli ověřit nebo zjistit, jaké další parametry metoda má, spusťte `example4.dropna?` v buňce kódu). Můžete alternativně specifikovat `how='all'`, abyste odstranili pouze řádky nebo sloupce, které obsahují všechny nulové hodnoty. Rozšiřme náš příklad `DataFrame`, abychom to viděli v praxi.

```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

Parametr `thresh` vám poskytuje jemnější kontrolu: nastavíte počet *nenulových* hodnot, které řádek nebo sloupec musí mít, aby byl zachován:
```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```
Zde byly první a poslední řádek odstraněny, protože obsahují pouze dvě nenulové hodnoty.

- **Vyplnění nulových hodnot**: V závislosti na vaší datové sadě může někdy dávat větší smysl vyplnit nulové hodnoty platnými než je odstranit. Mohli byste použít `isnull` k tomu, abyste to udělali na místě, ale to může být pracné, zejména pokud máte hodně hodnot k vyplnění. Protože se jedná o tak běžný úkol ve vědě o datech, pandas poskytuje `fillna`, který vrací kopii `Series` nebo `DataFrame` s chybějícími hodnotami nahrazenými jednou z vašich volby. Vytvořme další příklad `Series`, abychom viděli, jak to funguje v praxi.
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
Můžete vyplnit všechny nulové záznamy jednou hodnotou, například `0`:
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
Můžete **dopředně vyplnit** nulové hodnoty, což znamená použít poslední platnou hodnotu k vyplnění nuly:
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
Můžete také **zpětně vyplnit**, aby se propagovala další platná hodnota zpět k vyplnění nuly:
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
Jak asi tušíte, funguje to stejně s `DataFrame`, ale můžete také specifikovat `axis`, podél kterého chcete vyplnit nulové hodnoty. Použijeme znovu dříve použitý `example2`:
```python
example2.fillna(method='ffill', axis=1)
```
```
	0	1	2	3
0	1.0	1.0	7.0	7.0
1	2.0	5.0	8.0	8.0
2	NaN	6.0	9.0	9.0
```
Všimněte si, že když není k dispozici předchozí hodnota pro dopředné vyplnění, nulová hodnota zůstává.
> **Hlavní myšlenka:** Existuje několik způsobů, jak se vypořádat s chybějícími hodnotami ve vašich datových souborech. Konkrétní strategie, kterou použijete (odstranění, nahrazení nebo způsob, jakým je nahradíte), by měla být určena specifiky těchto dat. Lepší smysl pro práci s chybějícími hodnotami si vyvinete tím více, čím častěji budete s datovými soubory pracovat a interagovat.
## Odstranění duplicitních dat

> **Cíl učení:** Na konci této podsekce byste měli být schopni identifikovat a odstranit duplicitní hodnoty z DataFrame.

Kromě chybějících dat se v reálných datových sadách často setkáte s duplicitními daty. Naštěstí `pandas` poskytuje jednoduchý způsob, jak detekovat a odstranit duplicitní záznamy.

- **Identifikace duplicit: `duplicated`**: Duplicitní hodnoty můžete snadno odhalit pomocí metody `duplicated` v pandas, která vrací masku typu Boolean, jež označuje, zda je záznam v `DataFrame` duplicitou dřívějšího záznamu. Vytvořme další příklad `DataFrame`, abychom si to ukázali v praxi.
```python
example4 = pd.DataFrame({'letters': ['A','B'] * 2 + ['B'],
                         'numbers': [1, 2, 1, 3, 3]})
example4
```
|      |písmena|čísla  |
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
- **Odstranění duplicit: `drop_duplicates`:** jednoduše vrátí kopii dat, u kterých jsou všechny hodnoty označené jako `duplicated` `False`:
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
Metody `duplicated` a `drop_duplicates` standardně zohledňují všechny sloupce, ale můžete specifikovat, že mají zkoumat pouze podmnožinu sloupců ve vašem `DataFrame`:
```python
example4.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **Shrnutí:** Odstranění duplicitních dat je nezbytnou součástí téměř každého projektu v oblasti datové vědy. Duplicitní data mohou ovlivnit výsledky vašich analýz a poskytnout nepřesné výsledky!


## 🚀 Výzva

Všechny probírané materiály jsou k dispozici jako [Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb). Navíc jsou po každé sekci k dispozici cvičení, zkuste je vyřešit!

## [Kvíz po přednášce](https://ff-quizzes.netlify.app/en/ds/quiz/15)



## Přehled & Samostudium

Existuje mnoho způsobů, jak objevit a přistoupit k přípravě dat pro analýzu a modelování, a čištění dat je důležitým krokem, který vyžaduje praktické zkušenosti. Vyzkoušejte tyto výzvy na Kaggle, abyste prozkoumali techniky, které tato lekce nepokryla.

- [Výzva čištění dat: Parsování dat](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [Výzva čištění dat: Škálování a normalizace dat](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)


## Zadání

[Hodnocení dat z formuláře](assignment.md)

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.