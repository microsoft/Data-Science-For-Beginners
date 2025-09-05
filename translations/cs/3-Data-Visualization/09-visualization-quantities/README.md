<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a49d78e32e280c410f04e5f2a2068e77",
  "translation_date": "2025-09-05T17:51:16+00:00",
  "source_file": "3-Data-Visualization/09-visualization-quantities/README.md",
  "language_code": "cs"
}
-->
# Vizualizace množství

|![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| Vizualizace množství - _Sketchnote od [@nitya](https://twitter.com/nitya)_ |

V této lekci se naučíte používat jednu z mnoha dostupných knihoven Pythonu k vytváření zajímavých vizualizací zaměřených na koncept množství. Pomocí vyčištěného datasetu o ptácích z Minnesoty můžete objevit mnoho zajímavých faktů o místní fauně.  
## [Kvíz před lekcí](https://ff-quizzes.netlify.app/en/ds/quiz/16)

## Pozorování rozpětí křídel pomocí Matplotlib

Skvělou knihovnou pro vytváření jednoduchých i sofistikovaných grafů a diagramů různých typů je [Matplotlib](https://matplotlib.org/stable/index.html). Obecně proces vykreslování dat pomocí těchto knihoven zahrnuje identifikaci částí vašeho dataframe, které chcete cílit, provedení potřebných transformací na tato data, přiřazení hodnot osy x a y, rozhodnutí o typu grafu, který chcete zobrazit, a následné vykreslení grafu. Matplotlib nabízí širokou škálu vizualizací, ale v této lekci se zaměříme na ty nejvhodnější pro vizualizaci množství: čárové grafy, bodové grafy a sloupcové grafy.

> ✅ Použijte nejlepší typ grafu podle struktury vašich dat a příběhu, který chcete vyprávět.  
> - Pro analýzu trendů v čase: čárový graf  
> - Pro porovnání hodnot: sloupcový, koláčový, bodový graf  
> - Pro zobrazení, jak části tvoří celek: koláčový graf  
> - Pro zobrazení distribuce dat: bodový graf, sloupcový graf  
> - Pro zobrazení trendů: čárový, sloupcový graf  
> - Pro zobrazení vztahů mezi hodnotami: čárový graf, bodový graf, bublinový graf  

Pokud máte dataset a potřebujete zjistit, kolik určité položky je zahrnuto, jedním z prvních úkolů bude prozkoumání jeho hodnot.

✅ Existují velmi dobré 'cheat sheets' pro Matplotlib [zde](https://matplotlib.org/cheatsheets/cheatsheets.pdf).

## Vytvoření čárového grafu hodnot rozpětí křídel ptáků

Otevřete soubor `notebook.ipynb` v kořenové složce této lekce a přidejte buňku.

> Poznámka: data jsou uložena v kořenové složce tohoto repozitáře ve složce `/data`.

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```  
Tato data jsou směsí textu a čísel:

|      | Název                        | Vědecký název          | Kategorie             | Řád          | Čeleď    | Rod         | Stav ochrany         | MinDélka | MaxDélka | MinHmotnost | MaxHmotnost | MinRozpětí | MaxRozpětí |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :------------------- | --------:| --------:| ----------: | ----------: | ----------:| ----------:|
|    0 | Černobřichá pižmovka         | Dendrocygna autumnalis | Kachny/Husy/Vodní ptáci| Anseriformes | Anatidae | Dendrocygna | LC                   |        47|        56|         652 |        1020 |          76|          94|
|    1 | Pižmovka rezavá              | Dendrocygna bicolor    | Kachny/Husy/Vodní ptáci| Anseriformes | Anatidae | Dendrocygna | LC                   |        45|        53|         712 |        1050 |          85|          93|
|    2 | Sněžná husa                  | Anser caerulescens     | Kachny/Husy/Vodní ptáci| Anseriformes | Anatidae | Anser       | LC                   |        64|        79|        2050 |        4050 |         135|         165|
|    3 | Rossova husa                 | Anser rossii           | Kachny/Husy/Vodní ptáci| Anseriformes | Anatidae | Anser       | LC                   |      57.3|        64|        1066 |        1567 |         113|         116|
|    4 | Husa běločelá                | Anser albifrons        | Kachny/Husy/Vodní ptáci| Anseriformes | Anatidae | Anser       | LC                   |        64|        81|        1930 |        3310 |         130|         165|

Začněme vykreslením některých číselných dat pomocí základního čárového grafu. Předpokládejme, že chcete zobrazit maximální rozpětí křídel těchto zajímavých ptáků.

```python
wingspan = birds['MaxWingspan'] 
wingspan.plot()
```  
![Max Rozpětí](../../../../3-Data-Visualization/09-visualization-quantities/images/max-wingspan-02.png)

Co si všimnete okamžitě? Zdá se, že existuje alespoň jeden extrémní údaj - to je opravdu velké rozpětí křídel! Rozpětí křídel 2300 centimetrů odpovídá 23 metrům - potulují se v Minnesotě pterodaktylové? Pojďme to prozkoumat.

Zatímco byste mohli rychle seřadit data v Excelu a najít tyto extrémní údaje, které jsou pravděpodobně překlepy, pokračujte ve vizualizačním procesu přímo z grafu.

Přidejte popisky na osu x, aby bylo vidět, o jaké ptáky se jedná:

```
plt.title('Max Wingspan in Centimeters')
plt.ylabel('Wingspan (CM)')
plt.xlabel('Birds')
plt.xticks(rotation=45)
x = birds['Name'] 
y = birds['MaxWingspan']

plt.plot(x, y)

plt.show()
```  
![Rozpětí s popisky](../../../../3-Data-Visualization/09-visualization-quantities/images/max-wingspan-labels-02.png)

I při otočení popisků o 45 stupňů je jich příliš mnoho na čtení. Zkusme jinou strategii: označte pouze ty extrémní údaje a nastavte popisky přímo v grafu. Můžete použít bodový graf, abyste vytvořili více prostoru pro popisky:

```python
plt.title('Max Wingspan in Centimeters')
plt.ylabel('Wingspan (CM)')
plt.tick_params(axis='both',which='both',labelbottom=False,bottom=False)

for i in range(len(birds)):
    x = birds['Name'][i]
    y = birds['MaxWingspan'][i]
    plt.plot(x, y, 'bo')
    if birds['MaxWingspan'][i] > 500:
        plt.text(x, y * (1 - 0.05), birds['Name'][i], fontsize=12)
    
plt.show()
```  
Co se zde děje? Použili jste `tick_params` k skrytí spodních popisků a poté vytvořili smyčku přes dataset ptáků. Vykreslením grafu s malými modrými tečkami pomocí `bo` jste zkontrolovali, zda má nějaký pták maximální rozpětí křídel přes 500, a pokud ano, zobrazili jeho popisek vedle tečky. Popisky jste mírně posunuli na ose y (`y * (1 - 0.05)`) a použili název ptáka jako popisek.

Co jste objevili?

![Extrémní údaje](../../../../3-Data-Visualization/09-visualization-quantities/images/labeled-wingspan-02.png)  
## Filtrování dat

Jak Orel bělohlavý, tak Sokol prériový, i když pravděpodobně velmi velcí ptáci, se zdají být chybně označeni, s přidanou `0` v jejich maximálním rozpětí křídel. Je nepravděpodobné, že byste potkali Orla bělohlavého s rozpětím křídel 25 metrů, ale pokud ano, dejte nám vědět! Vytvořme nový dataframe bez těchto dvou extrémních údajů:

```python
plt.title('Max Wingspan in Centimeters')
plt.ylabel('Wingspan (CM)')
plt.xlabel('Birds')
plt.tick_params(axis='both',which='both',labelbottom=False,bottom=False)
for i in range(len(birds)):
    x = birds['Name'][i]
    y = birds['MaxWingspan'][i]
    if birds['Name'][i] not in ['Bald eagle', 'Prairie falcon']:
        plt.plot(x, y, 'bo')
plt.show()
```  

Filtrováním extrémních údajů jsou vaše data nyní soudržnější a srozumitelnější.

![Bodový graf rozpětí křídel](../../../../3-Data-Visualization/09-visualization-quantities/images/scatterplot-wingspan-02.png)

Nyní, když máme čistší dataset alespoň co se týče rozpětí křídel, pojďme objevit více o těchto ptácích.

Zatímco čárové a bodové grafy mohou zobrazovat informace o hodnotách dat a jejich distribuci, chceme se zaměřit na hodnoty obsažené v tomto datasetu. Mohli byste vytvořit vizualizace, které odpoví na následující otázky o množství:

> Kolik kategorií ptáků existuje a jaké jsou jejich počty?  
> Kolik ptáků je vyhynulých, ohrožených, vzácných nebo běžných?  
> Kolik je různých rodů a řádů podle Linnaeusovy terminologie?  
## Prozkoumání sloupcových grafů

Sloupcové grafy jsou praktické, když potřebujete zobrazit seskupení dat. Pojďme prozkoumat kategorie ptáků, které existují v tomto datasetu, abychom zjistili, která je nejběžnější podle počtu.

V souboru notebook vytvořte základní sloupcový graf.

✅ Poznámka: Můžete buď odfiltrovat dva extrémní ptáky, které jsme identifikovali v předchozí části, upravit překlep v jejich rozpětí křídel, nebo je ponechat pro tyto cvičení, která nezávisí na hodnotách rozpětí křídel.

Pokud chcete vytvořit sloupcový graf, můžete vybrat data, na která se chcete zaměřit. Sloupcové grafy lze vytvořit z neupravených dat:

```python
birds.plot(x='Category',
        kind='bar',
        stacked=True,
        title='Birds of Minnesota')

```  
![Celá data jako sloupcový graf](../../../../3-Data-Visualization/09-visualization-quantities/images/full-data-bar-02.png)

Tento sloupcový graf je však nečitelný, protože je zde příliš mnoho neseskupených dat. Musíte vybrat pouze data, která chcete vykreslit, takže se podívejme na délku ptáků podle jejich kategorie.

Filtrovat data tak, aby zahrnovala pouze kategorii ptáků.

✅ Všimněte si, že používáte Pandas k práci s daty a poté necháte Matplotlib vykreslit graf.

Protože existuje mnoho kategorií, můžete tento graf zobrazit vertikálně a upravit jeho výšku, aby zahrnoval všechna data:

```python
category_count = birds.value_counts(birds['Category'].values, sort=True)
plt.rcParams['figure.figsize'] = [6, 12]
category_count.plot.barh()
```  
![Kategorie a délka](../../../../3-Data-Visualization/09-visualization-quantities/images/category-counts-02.png)

Tento sloupcový graf poskytuje dobrý přehled o počtu ptáků v každé kategorii. Na první pohled vidíte, že největší počet ptáků v této oblasti patří do kategorie Kachny/Husy/Vodní ptáci. Minnesota je 'země 10 000 jezer', takže to není překvapivé!

✅ Vyzkoušejte další počty v tomto datasetu. Překvapí vás něco?

## Porovnání dat

Můžete zkusit různé porovnání seskupených dat vytvořením nových os. Zkuste porovnání MaxDélky ptáka podle jeho kategorie:

```python
maxlength = birds['MaxLength']
plt.barh(y=birds['Category'], width=maxlength)
plt.rcParams['figure.figsize'] = [6, 12]
plt.show()
```  
![Porovnání dat](../../../../3-Data-Visualization/09-visualization-quantities/images/category-length-02.png)

Nic překvapivého zde: kolibříci mají nejmenší MaxDélku ve srovnání s pelikány nebo husami. Je dobré, když data dávají logický smysl!

Můžete vytvořit zajímavější vizualizace sloupcových grafů překrytím dat. Pojďme překrýt Minimální a Maximální délku na dané kategorii ptáků:

```python
minLength = birds['MinLength']
maxLength = birds['MaxLength']
category = birds['Category']

plt.barh(category, maxLength)
plt.barh(category, minLength)

plt.show()
```  
V tomto grafu vidíte rozsah pro každou kategorii ptáků mezi Minimální délkou a Maximální délkou. Můžete bezpečně říci, že podle těchto dat platí, že čím větší pták, tím větší rozsah jeho délky. Fascinující!

![Překryté hodnoty](../../../../3-Data-Visualization/09-visualization-quantities/images/superimposed-02.png)

## 🚀 Výzva

Tento dataset ptáků nabízí bohatství informací o různých typech ptáků v konkrétním ekosystému. Prohledejte internet a zjistěte, zda můžete najít další dataset zaměřený na ptáky. Procvičte si vytváření grafů a diagramů kolem těchto ptáků, abyste objevili fakta, která jste si neuvědomovali.

## [Kvíz po lekci](https://ff-quizzes.netlify.app/en/ds/quiz/17)

## Přehled & Samostudium

Tato první lekce vám poskytla informace o tom, jak používat Matplotlib k vizualizaci množství. Proveďte výzkum dalších způsobů práce s datovými sadami pro vizualizaci. [Plotly](https://github.com/plotly/plotly.py) je jedna z možností, kterou v těchto lekcích nebudeme pokrývat, takže se podívejte, co může nabídnout.  
## Úkol

[Čáry, body a sloupce](assignment.md)

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádné nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.