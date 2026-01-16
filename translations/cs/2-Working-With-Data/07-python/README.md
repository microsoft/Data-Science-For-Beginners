<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7bfec050f4717dcc2dfd028aca9d21f3",
  "translation_date": "2025-09-06T15:56:55+00:00",
  "source_file": "2-Working-With-Data/07-python/README.md",
  "language_code": "cs"
}
-->
# Práce s daty: Python a knihovna Pandas

| ![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/07-WorkWithPython.png) |
| :-------------------------------------------------------------------------------------------------------: |
|                 Práce s Pythonem - _Sketchnote od [@nitya](https://twitter.com/nitya)_                   |

[![Úvodní video](../../../../translated_images/cs/video-ds-python.245247dc811db8e4d5ac420246de8a118c63fd28f6a56578d08b630ae549f260.png)](https://youtu.be/dZjWOGbsN4Y)

Databáze nabízejí velmi efektivní způsoby ukládání dat a jejich dotazování pomocí dotazovacích jazyků, ale nejflexibilnějším způsobem zpracování dat je napsání vlastního programu pro manipulaci s daty. V mnoha případech by bylo efektivnější použít dotaz na databázi. Nicméně v některých situacích, kdy je potřeba složitější zpracování dat, to nelze snadno provést pomocí SQL. 
Zpracování dat lze naprogramovat v jakémkoli programovacím jazyce, ale existují určité jazyky, které jsou na vyšší úrovni, pokud jde o práci s daty. Datoví vědci obvykle preferují jeden z následujících jazyků:

* **[Python](https://www.python.org/)**, univerzální programovací jazyk, který je často považován za jednu z nejlepších možností pro začátečníky díky své jednoduchosti. Python má mnoho dalších knihoven, které vám mohou pomoci vyřešit praktické problémy, jako je extrakce dat ze ZIP archivu nebo převod obrázku na odstíny šedi. Kromě datové vědy se Python často používá i pro vývoj webových aplikací. 
* **[R](https://www.r-project.org/)** je tradiční nástroj vyvinutý s ohledem na statistické zpracování dat. Obsahuje také rozsáhlé úložiště knihoven (CRAN), což z něj činí dobrou volbu pro zpracování dat. Nicméně R není univerzální programovací jazyk a mimo oblast datové vědy se používá jen zřídka.
* **[Julia](https://julialang.org/)** je další jazyk vyvinutý speciálně pro datovou vědu. Je navržen tak, aby poskytoval lepší výkon než Python, což z něj činí skvělý nástroj pro vědecké experimentování.

V této lekci se zaměříme na použití Pythonu pro jednoduché zpracování dat. Předpokládáme základní znalost tohoto jazyka. Pokud chcete hlubší úvod do Pythonu, můžete se podívat na některý z následujících zdrojů:

* [Naučte se Python zábavným způsobem pomocí grafiky Turtle a fraktálů](https://github.com/shwars/pycourse) - rychlý úvodní kurz programování v Pythonu na GitHubu
* [Udělejte své první kroky s Pythonem](https://docs.microsoft.com/en-us/learn/paths/python-first-steps/?WT.mc_id=academic-77958-bethanycheum) - vzdělávací cesta na [Microsoft Learn](http://learn.microsoft.com/?WT.mc_id=academic-77958-bethanycheum)

Data mohou mít mnoho podob. V této lekci se zaměříme na tři formy dat - **tabulková data**, **text** a **obrázky**.

Zaměříme se na několik příkladů zpracování dat, místo abychom vám poskytli kompletní přehled všech souvisejících knihoven. To vám umožní získat hlavní představu o tom, co je možné, a zanechá vás s pochopením, kde najít řešení vašich problémů, když je budete potřebovat.

> **Nejužitečnější rada**. Když potřebujete provést určitou operaci na datech, kterou nevíte, jak provést, zkuste ji vyhledat na internetu. [Stackoverflow](https://stackoverflow.com/) obvykle obsahuje mnoho užitečných ukázek kódu v Pythonu pro mnoho typických úkolů. 

## [Kvíz před lekcí](https://ff-quizzes.netlify.app/en/ds/quiz/12)

## Tabulková data a DataFrame

S tabulkovými daty jste se již setkali, když jsme mluvili o relačních databázích. Když máte hodně dat, která jsou obsažena v mnoha různých propojených tabulkách, rozhodně má smysl použít SQL pro práci s nimi. Nicméně existuje mnoho případů, kdy máme tabulku dat a potřebujeme získat nějaké **pochopení** nebo **poznatky** o těchto datech, jako je rozložení, korelace mezi hodnotami atd. V datové vědě existuje mnoho situací, kdy potřebujeme provést nějaké transformace původních dat, následované vizualizací. Oba tyto kroky lze snadno provést pomocí Pythonu.

Existují dvě nejdůležitější knihovny v Pythonu, které vám mohou pomoci pracovat s tabulkovými daty:
* **[Pandas](https://pandas.pydata.org/)** umožňuje manipulovat s tzv. **DataFrame**, což jsou analogie relačních tabulek. Můžete mít pojmenované sloupce a provádět různé operace na řádcích, sloupcích a DataFrame obecně. 
* **[Numpy](https://numpy.org/)** je knihovna pro práci s **tensory**, tj. vícerozměrnými **poli**. Pole má hodnoty stejného základního typu a je jednodušší než DataFrame, ale nabízí více matematických operací a vytváří menší režii.

Existuje také několik dalších knihoven, které byste měli znát:
* **[Matplotlib](https://matplotlib.org/)** je knihovna používaná pro vizualizaci dat a vykreslování grafů
* **[SciPy](https://www.scipy.org/)** je knihovna s některými dalšími vědeckými funkcemi. Již jsme se s touto knihovnou setkali, když jsme mluvili o pravděpodobnosti a statistice

Zde je kousek kódu, který byste obvykle použili k importu těchto knihoven na začátku svého programu v Pythonu:
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import ... # you need to specify exact sub-packages that you need
``` 

Pandas je založen na několika základních konceptech.

### Series 

**Series** je sekvence hodnot, podobná seznamu nebo numpy poli. Hlavní rozdíl je v tom, že Series má také **index**, a když s nimi pracujeme (např. je sčítáme), index se bere v úvahu. Index může být tak jednoduchý jako číslo řádku (je to výchozí index při vytváření Series ze seznamu nebo pole), nebo může mít složitou strukturu, jako je časový interval.

> **Poznámka**: V doprovodném notebooku [`notebook.ipynb`](notebook.ipynb) je úvodní kód pro Pandas. Zde uvádíme pouze některé příklady, ale určitě se podívejte na celý notebook.

Představme si příklad: chceme analyzovat prodeje našeho stánku se zmrzlinou. Vygenerujeme sérii čísel prodejů (počet prodaných položek každý den) za určité časové období:

```python
start_date = "Jan 1, 2020"
end_date = "Mar 31, 2020"
idx = pd.date_range(start_date,end_date)
print(f"Length of index is {len(idx)}")
items_sold = pd.Series(np.random.randint(25,50,size=len(idx)),index=idx)
items_sold.plot()
```
![Graf časové řady](../../../../translated_images/cs/timeseries-1.80de678ab1cf727e50e00bcf24009fa2b0a8b90ebc43e34b99a345227d28e467.png)

Předpokládejme, že každý týden pořádáme večírek pro přátele a bereme dalších 10 balení zmrzliny na večírek. Můžeme vytvořit další sérii, indexovanou podle týdne, abychom to ukázali:
```python
additional_items = pd.Series(10,index=pd.date_range(start_date,end_date,freq="W"))
```
Když sečteme dvě série dohromady, získáme celkový počet:
```python
total_items = items_sold.add(additional_items,fill_value=0)
total_items.plot()
```
![Graf časové řady](../../../../translated_images/cs/timeseries-2.aae51d575c55181ceda81ade8c546a2fc2024f9136934386d57b8a189d7570ff.png)

> **Poznámka**: Nepoužíváme jednoduchou syntaxi `total_items+additional_items`. Pokud bychom to udělali, dostali bychom mnoho hodnot `NaN` (*Not a Number*) v výsledné sérii. To je proto, že některé hodnoty indexu v sérii `additional_items` chybí, a přičtení `NaN` k čemukoli vede k `NaN`. Proto musíme při sčítání specifikovat parametr `fill_value`.

U časových řad můžeme také **převzorkovat** sérii na různé časové intervaly. Například pokud chceme vypočítat průměrný objem prodeje měsíčně, můžeme použít následující kód:
```python
monthly = total_items.resample("1M").mean()
ax = monthly.plot(kind='bar')
```
![Měsíční průměry časové řady](../../../../translated_images/cs/timeseries-3.f3147cbc8c624881008564bc0b5d9fcc15e7374d339da91766bd0e1c6bd9e3af.png)

### DataFrame

DataFrame je v podstatě kolekce sérií se stejným indexem. Můžeme spojit několik sérií dohromady do DataFrame:
```python
a = pd.Series(range(1,10))
b = pd.Series(["I","like","to","play","games","and","will","not","change"],index=range(0,9))
df = pd.DataFrame([a,b])
```
To vytvoří horizontální tabulku jako tuto:
|     | 0   | 1    | 2   | 3   | 4      | 5   | 6      | 7    | 8    |
| --- | --- | ---- | --- | --- | ------ | --- | ------ | ---- | ---- |
| 0   | 1   | 2    | 3   | 4   | 5      | 6   | 7      | 8    | 9    |
| 1   | I   | like | to  | use | Python | and | Pandas | very | much |

Můžeme také použít Series jako sloupce a specifikovat názvy sloupců pomocí slovníku:
```python
df = pd.DataFrame({ 'A' : a, 'B' : b })
```
To nám dá tabulku jako tuto:

|     | A   | B      |
| --- | --- | ------ |
| 0   | 1   | I      |
| 1   | 2   | like   |
| 2   | 3   | to     |
| 3   | 4   | use    |
| 4   | 5   | Python |
| 5   | 6   | and    |
| 6   | 7   | Pandas |
| 7   | 8   | very   |
| 8   | 9   | much   |

**Poznámka**: Tuto tabulku můžeme také získat transpozicí předchozí tabulky, např. napsáním 
```python
df = pd.DataFrame([a,b]).T..rename(columns={ 0 : 'A', 1 : 'B' })
```
Zde `.T` znamená operaci transpozice DataFrame, tj. změnu řádků a sloupců, a operace `rename` nám umožňuje přejmenovat sloupce tak, aby odpovídaly předchozímu příkladu.

Zde je několik nejdůležitějších operací, které můžeme provádět na DataFrame:

**Výběr sloupců**. Můžeme vybrat jednotlivé sloupce napsáním `df['A']` - tato operace vrací Series. Můžeme také vybrat podmnožinu sloupců do jiného DataFrame napsáním `df[['B','A']]` - to vrací další DataFrame.

**Filtrování** pouze určitých řádků podle kritérií. Například, abychom ponechali pouze řádky se sloupcem `A` větším než 5, můžeme napsat `df[df['A']>5]`.

> **Poznámka**: Způsob, jakým filtrování funguje, je následující. Výraz `df['A']<5` vrací booleovskou sérii, která označuje, zda je výraz `True` nebo `False` pro každý prvek původní série `df['A']`. Když je booleovská série použita jako index, vrací podmnožinu řádků v DataFrame. Proto není možné použít libovolný booleovský výraz v Pythonu, například napsání `df[df['A']>5 and df['A']<7]` by bylo špatné. Místo toho byste měli použít speciální operaci `&` na booleovské sérii, napsáním `df[(df['A']>5) & (df['A']<7)]` (*závorky jsou zde důležité*).

**Vytváření nových vypočitatelných sloupců**. Můžeme snadno vytvořit nové vypočitatelné sloupce pro náš DataFrame pomocí intuitivního výrazu jako tento:
```python
df['DivA'] = df['A']-df['A'].mean() 
``` 
Tento příklad vypočítává odchylku A od její průměrné hodnoty. Co se zde vlastně děje, je to, že počítáme sérii a poté tuto sérii přiřazujeme na levou stranu, čímž vytváříme další sloupec. Proto nemůžeme použít žádné operace, které nejsou kompatibilní se sériemi, například následující kód je špatný:
```python
# Wrong code -> df['ADescr'] = "Low" if df['A'] < 5 else "Hi"
df['LenB'] = len(df['B']) # <- Wrong result
``` 
Poslední příklad, i když je syntakticky správný, nám dává špatný výsledek, protože přiřazuje délku série `B` všem hodnotám ve sloupci, a ne délku jednotlivých prvků, jak jsme zamýšleli.

Pokud potřebujeme vypočítat složité výrazy jako tento, můžeme použít funkci `apply`. Poslední příklad lze napsat takto:
```python
df['LenB'] = df['B'].apply(lambda x : len(x))
# or 
df['LenB'] = df['B'].apply(len)
```

Po výše uvedených operacích skončíme s následujícím DataFrame:

|     | A   | B      | DivA | LenB |
| --- | --- | ------ | ---- | ---- |
| 0   | 1   | I      | -4.0 | 1    |
| 1   | 2   | like   | -3.0 | 4    |
| 2   | 3   | to     | -2.0 | 2    |
| 3   | 4   | use    | -1.0 | 3    |
| 4   | 5   | Python | 0.0  | 6    |
| 5   | 6   | and    | 1.0  | 3    |
| 6   | 7   | Pandas | 2.0  | 6    |
| 7   | 8   | very   | 3.0  | 4    |
| 8   | 9   | much   | 4.0  | 4    |

**Výběr řádků podle čísel** lze provést pomocí konstruktu `iloc`. Například, abychom vybrali prvních 5 řádků z DataFrame:
```python
df.iloc[:5]
```

**Seskupování** se často používá k získání výsledku podobného *kontingenčním tabulkám* v Excelu. Předpokládejme, že chceme vypočítat průměrnou hodnotu sloupce `A` pro každé dané číslo `LenB`. Poté můžeme seskupit náš DataFrame podle `LenB` a zavolat `mean`:
```python
df.groupby(by='LenB')[['A','DivA']].mean()
```
Pokud potřebujeme vypočítat průměr a počet prvků ve skupině, můžeme použít složitější funkci `aggregate`:
```python
df.groupby(by='LenB') \
 .aggregate({ 'DivA' : len, 'A' : lambda x: x.mean() }) \
 .rename(columns={ 'DivA' : 'Count', 'A' : 'Mean'})
```
To nám dá následující tabulku:

| LenB | Count | Mean     |
| ---- | ----- | -------- |
| 1    | 1     | 1.000000 |
| 2    | 1     | 3.000000 |
| 3    | 2     | 5.000000 |
| 4    | 3     | 6.333333 |
| 6    | 2     | 6.000000 |

### Získávání dat
Viděli jsme, jak snadné je vytvořit Series a DataFrames z objektů v Pythonu. Nicméně, data obvykle přicházejí ve formě textového souboru nebo tabulky v Excelu. Naštěstí nám Pandas nabízí jednoduchý způsob, jak načíst data z disku. Například čtení CSV souboru je tak jednoduché:
```python
df = pd.read_csv('file.csv')
```
V sekci "Výzva" uvidíme více příkladů načítání dat, včetně jejich získávání z externích webových stránek.

### Tisk a Vizualizace

Datový vědec často musí prozkoumat data, a proto je důležité být schopen je vizualizovat. Když je DataFrame velký, často chceme jen ověřit, že vše děláme správně, tím, že si vytiskneme prvních pár řádků. To lze provést voláním `df.head()`. Pokud to spustíte z Jupyter Notebooku, vytiskne se DataFrame v pěkné tabulkové podobě.

Také jsme viděli použití funkce `plot` k vizualizaci některých sloupců. Zatímco `plot` je velmi užitečný pro mnoho úkolů a podporuje různé typy grafů pomocí parametru `kind=`, vždy můžete použít knihovnu `matplotlib` k vytvoření něčeho složitějšího. Vizualizaci dat se budeme podrobně věnovat v samostatných lekcích kurzu.

Tento přehled pokrývá nejdůležitější koncepty Pandas, nicméně knihovna je velmi bohatá a neexistují žádné limity, co s ní můžete dělat! Pojďme nyní aplikovat tyto znalosti na řešení konkrétního problému.

## 🚀 Výzva 1: Analýza šíření COVID

Prvním problémem, na který se zaměříme, je modelování epidemického šíření COVID-19. K tomu použijeme data o počtu nakažených jednotlivců v různých zemích, která poskytuje [Center for Systems Science and Engineering](https://systems.jhu.edu/) (CSSE) na [Johns Hopkins University](https://jhu.edu/). Dataset je dostupný v [tomto GitHub repozitáři](https://github.com/CSSEGISandData/COVID-19).

Protože chceme ukázat, jak pracovat s daty, zveme vás k otevření [`notebook-covidspread.ipynb`](notebook-covidspread.ipynb) a jeho přečtení od začátku do konce. Můžete také spustit buňky a vyzkoušet některé výzvy, které jsme pro vás nechali na konci.

![COVID Spread](../../../../translated_images/cs/covidspread.f3d131c4f1d260ab0344d79bac0abe7924598dd754859b165955772e1bd5e8a2.png)

> Pokud nevíte, jak spustit kód v Jupyter Notebooku, podívejte se na [tento článek](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## Práce s nestrukturovanými daty

Zatímco data často přicházejí v tabulkové podobě, v některých případech musíme pracovat s méně strukturovanými daty, například textem nebo obrázky. V takovém případě, abychom mohli použít techniky zpracování dat, které jsme viděli výše, musíme nějakým způsobem **extrahovat** strukturovaná data. Zde je několik příkladů:

* Extrakce klíčových slov z textu a sledování, jak často se tato klíčová slova objevují
* Použití neuronových sítí k extrakci informací o objektech na obrázku
* Získání informací o emocích lidí na záznamu z kamery

## 🚀 Výzva 2: Analýza COVID publikací

V této výzvě budeme pokračovat v tématu pandemie COVID a zaměříme se na zpracování vědeckých publikací na toto téma. Existuje [CORD-19 Dataset](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) s více než 7000 (v době psaní) publikacemi o COVID, dostupný s metadaty a abstrakty (a u přibližně poloviny z nich je k dispozici také celý text).

Kompletní příklad analýzy tohoto datasetu pomocí [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health/?WT.mc_id=academic-77958-bethanycheum) kognitivní služby je popsán [v tomto blogovém příspěvku](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/). Budeme diskutovat zjednodušenou verzi této analýzy.

> **NOTE**: Kopii datasetu neposkytujeme jako součást tohoto repozitáře. Možná budete muset nejprve stáhnout soubor [`metadata.csv`](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge?select=metadata.csv) z [tohoto datasetu na Kaggle](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge). Registrace na Kaggle může být vyžadována. Dataset můžete také stáhnout bez registrace [zde](https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/historical_releases.html), ale bude zahrnovat všechny plné texty kromě souboru s metadaty.

Otevřete [`notebook-papers.ipynb`](notebook-papers.ipynb) a přečtěte si jej od začátku do konce. Můžete také spustit buňky a vyzkoušet některé výzvy, které jsme pro vás nechali na konci.

![Covid Medical Treatment](../../../../translated_images/cs/covidtreat.b2ba59f57ca45fbcda36e0ddca3f8cfdddeeed6ca879ea7f866d93fa6ec65791.png)

## Zpracování obrazových dat

V poslední době byly vyvinuty velmi výkonné AI modely, které nám umožňují porozumět obrázkům. Existuje mnoho úkolů, které lze řešit pomocí předtrénovaných neuronových sítí nebo cloudových služeb. Některé příklady zahrnují:

* **Klasifikace obrázků**, která vám může pomoci kategorizovat obrázek do jedné z předdefinovaných tříd. Svůj vlastní klasifikátor obrázků můžete snadno vytrénovat pomocí služeb jako [Custom Vision](https://azure.microsoft.com/services/cognitive-services/custom-vision-service/?WT.mc_id=academic-77958-bethanycheum)
* **Detekce objektů** k identifikaci různých objektů na obrázku. Služby jako [computer vision](https://azure.microsoft.com/services/cognitive-services/computer-vision/?WT.mc_id=academic-77958-bethanycheum) mohou detekovat řadu běžných objektů a můžete vytrénovat model [Custom Vision](https://azure.microsoft.com/services/cognitive-services/custom-vision-service/?WT.mc_id=academic-77958-bethanycheum) k detekci specifických objektů.
* **Detekce obličeje**, včetně věku, pohlaví a emocí. To lze provést pomocí [Face API](https://azure.microsoft.com/services/cognitive-services/face/?WT.mc_id=academic-77958-bethanycheum).

Všechny tyto cloudové služby lze volat pomocí [Python SDKs](https://docs.microsoft.com/samples/azure-samples/cognitive-services-python-sdk-samples/cognitive-services-python-sdk-samples/?WT.mc_id=academic-77958-bethanycheum), a tak je lze snadno začlenit do vašeho workflow pro průzkum dat.

Zde jsou některé příklady průzkumu dat z obrazových zdrojů:
* V blogovém příspěvku [Jak se naučit datovou vědu bez programování](https://soshnikov.com/azure/how-to-learn-data-science-without-coding/) zkoumáme fotografie z Instagramu, snažíme se pochopit, co způsobuje, že lidé dávají více lajků na fotografii. Nejprve extrahujeme co nejvíce informací z obrázků pomocí [computer vision](https://azure.microsoft.com/services/cognitive-services/computer-vision/?WT.mc_id=academic-77958-bethanycheum), a poté použijeme [Azure Machine Learning AutoML](https://docs.microsoft.com/azure/machine-learning/concept-automated-ml/?WT.mc_id=academic-77958-bethanycheum) k vytvoření interpretovatelného modelu.
* V [Workshopu o studiu obličejů](https://github.com/CloudAdvocacy/FaceStudies) používáme [Face API](https://azure.microsoft.com/services/cognitive-services/face/?WT.mc_id=academic-77958-bethanycheum) k extrakci emocí lidí na fotografiích z událostí, abychom se pokusili pochopit, co dělá lidi šťastnými.

## Závěr

Ať už máte strukturovaná nebo nestrukturovaná data, pomocí Pythonu můžete provést všechny kroky související se zpracováním a porozuměním dat. Je to pravděpodobně nejflexibilnější způsob zpracování dat, a to je důvod, proč většina datových vědců používá Python jako svůj primární nástroj. Naučit se Python do hloubky je pravděpodobně dobrý nápad, pokud to s vaší cestou v datové vědě myslíte vážně!

## [Kvíz po přednášce](https://ff-quizzes.netlify.app/en/ds/quiz/13)

## Recenze a samostudium

**Knihy**
* [Wes McKinney. Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython](https://www.amazon.com/gp/product/1491957662)

**Online zdroje**
* Oficiální [10 minutový Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html) tutoriál
* [Dokumentace k vizualizaci v Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html)

**Učení Pythonu**
* [Naučte se Python zábavným způsobem s Turtle Graphics a fraktály](https://github.com/shwars/pycourse)
* [Uděláte své první kroky s Pythonem](https://docs.microsoft.com/learn/paths/python-first-steps/?WT.mc_id=academic-77958-bethanycheum) Learning Path na [Microsoft Learn](http://learn.microsoft.com/?WT.mc_id=academic-77958-bethanycheum)

## Zadání

[Proveďte podrobnější studii dat pro výzvy výše](assignment.md)

## Poděkování

Tuto lekci vytvořil s ♥️ [Dmitry Soshnikov](http://soshnikov.com)

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.