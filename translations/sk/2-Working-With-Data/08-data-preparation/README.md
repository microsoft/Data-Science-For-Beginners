<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3ade580a06b5f04d57cc83a768a8fb77",
  "translation_date": "2025-08-26T14:38:05+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "sk"
}
-->
# Práca s dátami: Príprava dát

|![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|Príprava dát - _Sketchnote od [@nitya](https://twitter.com/nitya)_ |

## [Kvíz pred prednáškou](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/14)

V závislosti od zdroja môžu surové dáta obsahovať nekonzistencie, ktoré spôsobujú problémy pri analýze a modelovaní. Inými slovami, tieto dáta môžu byť označené ako „špinavé“ a bude ich potrebné vyčistiť. Táto lekcia sa zameriava na techniky čistenia a transformácie dát na riešenie problémov s chýbajúcimi, nepresnými alebo neúplnými dátami. Témy pokryté v tejto lekcii využívajú Python a knižnicu Pandas a budú [predvedené v notebooku](notebook.ipynb) v tomto adresári.

## Dôležitosť čistenia dát

- **Jednoduchosť použitia a opätovného použitia**: Keď sú dáta správne organizované a normalizované, je jednoduchšie ich vyhľadávať, používať a zdieľať s ostatnými.

- **Konzistentnosť**: Dátová veda často vyžaduje prácu s viacerými datasetmi, kde datasety z rôznych zdrojov musia byť spojené. Zabezpečenie, že každý jednotlivý dataset má spoločnú štandardizáciu, zaručí, že dáta budú stále užitočné, keď sa spoja do jedného datasetu.

- **Presnosť modelu**: Vyčistené dáta zlepšujú presnosť modelov, ktoré na nich závisia.

## Bežné ciele a stratégie čistenia

- **Preskúmanie datasetu**: Preskúmanie dát, ktoré je pokryté v [neskoršej lekcii](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing), vám môže pomôcť objaviť dáta, ktoré je potrebné vyčistiť. Vizualizácia hodnôt v datasete môže nastaviť očakávania, ako bude zvyšok vyzerať, alebo poskytnúť predstavu o problémoch, ktoré je možné vyriešiť. Preskúmanie môže zahŕňať základné dotazovanie, vizualizácie a vzorkovanie.

- **Formátovanie**: V závislosti od zdroja môžu dáta obsahovať nekonzistencie v tom, ako sú prezentované. To môže spôsobiť problémy pri vyhľadávaní a reprezentácii hodnôt, kde sú viditeľné v datasete, ale nie sú správne reprezentované vo vizualizáciách alebo výsledkoch dotazov. Bežné problémy s formátovaním zahŕňajú riešenie medzier, dátumov a typov dát. Riešenie problémov s formátovaním je zvyčajne na ľuďoch, ktorí dáta používajú. Napríklad štandardy, ako sú prezentované dátumy a čísla, sa môžu líšiť podľa krajiny.

- **Duplikácie**: Dáta, ktoré sa vyskytujú viac ako raz, môžu produkovať nepresné výsledky a zvyčajne by mali byť odstránené. Toto môže byť bežné pri spájaní dvoch alebo viacerých datasetov. Avšak existujú prípady, keď duplikácie v spojených datasetoch obsahujú časti, ktoré môžu poskytnúť dodatočné informácie a môžu byť potrebné zachovať.

- **Chýbajúce dáta**: Chýbajúce dáta môžu spôsobiť nepresnosti, ako aj slabé alebo zaujaté výsledky. Niekedy sa dajú vyriešiť „znovunačítaním“ dát, doplnením chýbajúcich hodnôt výpočtom a kódom, ako je Python, alebo jednoducho odstránením hodnoty a zodpovedajúcich dát. Existuje množstvo dôvodov, prečo môžu dáta chýbať, a kroky, ktoré sa podniknú na vyriešenie týchto chýbajúcich hodnôt, môžu závisieť od toho, ako a prečo zmizli.

## Preskúmanie informácií o DataFrame
> **Cieľ učenia:** Na konci tejto podsekcie by ste mali byť schopní nájsť všeobecné informácie o dátach uložených v pandas DataFrames.

Keď načítate svoje dáta do pandas, pravdepodobne budú vo forme DataFrame (pozrite si predchádzajúcu [lekciu](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe) pre podrobný prehľad). Ak však dataset vo vašom DataFrame obsahuje 60 000 riadkov a 400 stĺpcov, ako vôbec začnete získavať predstavu o tom, s čím pracujete? Našťastie, [pandas](https://pandas.pydata.org/) poskytuje niekoľko praktických nástrojov na rýchle zobrazenie celkových informácií o DataFrame, ako aj prvých a posledných niekoľkých riadkov.

Aby sme preskúmali túto funkcionalitu, importujeme knižnicu Python scikit-learn a použijeme ikonický dataset: **Iris dataset**.

```python
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
iris_df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
```
|                                        |dĺžka sepalu (cm)|šírka sepalu (cm)|dĺžka petalu (cm)|šírka petalu (cm)|
|----------------------------------------|-----------------|-----------------|-----------------|-----------------|
|0                                       |5.1              |3.5             |1.4              |0.2             |
|1                                       |4.9              |3.0             |1.4              |0.2             |
|2                                       |4.7              |3.2             |1.3              |0.2             |
|3                                       |4.6              |3.1             |1.5              |0.2             |
|4                                       |5.0              |3.6             |1.4              |0.2             |

- **DataFrame.info**: Na začiatok sa používa metóda `info()` na vytlačenie súhrnu obsahu prítomného v `DataFrame`. Pozrime sa na tento dataset, aby sme zistili, čo máme:
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
Z toho vieme, že dataset *Iris* má 150 záznamov v štyroch stĺpcoch bez nulových záznamov. Všetky dáta sú uložené ako 64-bitové čísla s pohyblivou desatinnou čiarkou.

- **DataFrame.head()**: Ďalej, na kontrolu skutočného obsahu `DataFrame`, používame metódu `head()`. Pozrime sa, ako vyzerá prvých pár riadkov nášho `iris_df`:
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
- **DataFrame.tail()**: Naopak, na kontrolu posledných pár riadkov `DataFrame` používame metódu `tail()`:
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
> **Záver:** Už len pohľad na metadáta o informáciách v DataFrame alebo na prvé a posledné hodnoty v ňom vám môže okamžite poskytnúť predstavu o veľkosti, tvare a obsahu dát, s ktorými pracujete.

## Riešenie chýbajúcich dát
> **Cieľ učenia:** Na konci tejto podsekcie by ste mali vedieť, ako nahradiť alebo odstrániť nulové hodnoty z DataFrames.

Väčšinou dataset, ktorý chcete použiť (alebo musíte použiť), obsahuje chýbajúce hodnoty. Spôsob, akým sa chýbajúce dáta riešia, nesie jemné kompromisy, ktoré môžu ovplyvniť vašu konečnú analýzu a výsledky v reálnom svete.

Pandas rieši chýbajúce hodnoty dvoma spôsobmi. Prvý ste už videli v predchádzajúcich sekciách: `NaN`, alebo Not a Number. Toto je vlastne špeciálna hodnota, ktorá je súčasťou špecifikácie IEEE pre čísla s pohyblivou desatinnou čiarkou a používa sa iba na označenie chýbajúcich hodnôt s pohyblivou desatinnou čiarkou.

Pre chýbajúce hodnoty okrem čísel s pohyblivou desatinnou čiarkou používa pandas objekt Python `None`. Aj keď sa môže zdať mätúce, že sa stretnete s dvoma rôznymi typmi hodnôt, ktoré v podstate hovoria to isté, existujú rozumné programové dôvody pre tento dizajn a v praxi tento prístup umožňuje pandas poskytnúť dobrý kompromis pre drvivú väčšinu prípadov. Napriek tomu majú `None` a `NaN` obmedzenia, na ktoré si musíte dávať pozor, pokiaľ ide o ich použitie.

Viac o `NaN` a `None` si môžete pozrieť v [notebooku](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb)!

- **Detekcia nulových hodnôt**: V `pandas` sú vaše primárne metódy na detekciu nulových dát `isnull()` a `notnull()`. Obe vracajú Booleovské masky nad vašimi dátami. Budeme používať `numpy` pre hodnoty `NaN`:
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
Pozorne si prezrite výstup. Prekvapilo vás niečo? Zatiaľ čo `0` je aritmetická nula, je to stále úplne dobré celé číslo a pandas ho takto aj považuje. `''` je trochu jemnejšie. Aj keď sme ho použili v sekcii 1 na reprezentáciu prázdnej hodnoty reťazca, je to stále objekt reťazca a nie reprezentácia nuly, pokiaľ ide o pandas.

Teraz to otočme a použime tieto metódy spôsobom, akým ich budete používať v praxi. Booleovské masky môžete použiť priamo ako index `Series` alebo `DataFrame`, čo môže byť užitočné pri práci s izolovanými chýbajúcimi (alebo prítomnými) hodnotami.

> **Záver:** Metódy `isnull()` a `notnull()` produkujú podobné výsledky, keď ich použijete v `DataFrame`: zobrazujú výsledky a index týchto výsledkov, čo vám nesmierne pomôže pri práci s vašimi dátami.

- **Odstránenie nulových hodnôt**: Okrem identifikácie chýbajúcich hodnôt poskytuje pandas pohodlný spôsob odstránenia nulových hodnôt zo `Series` a `DataFrame`. (Najmä pri veľkých datasetoch je často rozumnejšie jednoducho odstrániť chýbajúce [NA] hodnoty z vašej analýzy, než sa s nimi zaoberať inými spôsobmi.) Aby sme to videli v praxi, vráťme sa k `example1`:
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
Všimnite si, že toto by malo vyzerať ako váš výstup z `example3[example3.notnull()]`. Rozdiel je v tom, že namiesto indexovania na maskované hodnoty `dropna` odstránil tieto chýbajúce hodnoty zo `Series` `example1`.

Keďže `DataFrame` má dve dimenzie, poskytuje viac možností na odstránenie dát.

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

(Všimli ste si, že pandas pretypoval dva stĺpce na čísla s pohyblivou desatinnou čiarkou, aby vyhovovali `NaN`?)

Nemôžete odstrániť jednu hodnotu z `DataFrame`, takže musíte odstrániť celé riadky alebo stĺpce. V závislosti od toho, čo robíte, môžete chcieť urobiť jedno alebo druhé, a preto pandas poskytuje možnosti pre obe. Keďže v dátovej vede stĺpce zvyčajne reprezentujú premenné a riadky reprezentujú pozorovania, je pravdepodobnejšie, že odstránite riadky dát; predvolené nastavenie pre `dropna()` je odstrániť všetky riadky, ktoré obsahujú akékoľvek nulové hodnoty:

```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```
Ak je to potrebné, môžete odstrániť hodnoty NA zo stĺpcov. Použite `axis=1` na to:
```python
example2.dropna(axis='columns')
```
```
	2
0	7
1	8
2	9
```
Všimnite si, že to môže odstrániť veľa dát, ktoré by ste mohli chcieť zachovať, najmä v menších datasetoch. Čo ak chcete odstrániť iba riadky alebo stĺpce, ktoré obsahujú niekoľko alebo dokonca všetky nulové hodnoty? Tieto nastavenia môžete špecifikovať v `dropna` pomocou parametrov `how` a `thresh`.

Predvolene je `how='any'` (ak by ste si to chceli overiť alebo vidieť, aké ďalšie parametre má metóda, spustite `example4.dropna?` v kódovom bloku). Alternatívne môžete špecifikovať `how='all'`, aby ste odstránili iba riadky alebo stĺpce, ktoré obsahujú všetky nulové hodnoty. Rozšírme náš príklad `DataFrame`, aby sme to videli v praxi.

```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

Parameter `thresh` vám poskytuje jemnejšiu kontrolu: nastavíte počet *nenulových* hodnôt, ktoré musí riadok alebo stĺpec obsahovať, aby bol zachovaný:
```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```
Tu boli prvý a posledný riadok odstránené, pretože obsahovali iba dve nenulové hodnoty.

- **Doplnenie nulových hodnôt**: V závislosti od vášho datasetu môže niekedy dávať väčší zmysel doplniť nulové hodnoty platnými, než ich odstrániť. Mohli by ste použiť `isnull` na to, aby ste to urobili priamo, ale to môže byť pracné, najmä ak máte veľa hodnôt na doplnenie. Keďže ide o takú bežnú úlohu v dátovej vede, pandas poskytuje `fillna`, ktorý vráti kópiu `Series` alebo `DataFrame` s chýbajúcimi hodnotami nahradenými hodnotou podľa vášho výberu. Vytvorme ďalší príklad `Series`, aby sme videli, ako to funguje v praxi.
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
Môžete doplniť všetky nulové záznamy jednou hodnotou, napríklad `0`:
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
Môžete **dopĺňať dopredu** nulové hodnoty, čo znamená použiť poslednú platnú hodnotu na doplnenie nuly:
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
Môžete tiež **dopĺňať dozadu**, aby ste propagovali ďalšiu platnú hodnotu dozadu na doplnenie nuly:
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
Ako by ste mohli tušiť, toto funguje rovnako s `DataFrame`, ale môžete tiež špecifikovať `axis`, pozdĺž ktorého chcete doplniť nulové hodnoty. Použijeme opäť predtým použitý `example2`:
```python
example2.fillna(method='ffill', axis=1)
```
```
	0	1	2	3
0	1.0	1.0	7.0	7.0
1	2.0	5.0	8.0	8.0
2	NaN	6.0	9.0	9.0
```
Všimnite si, že keď predchádzajúca hodnota nie je dostupná na dopĺňanie dopredu, nulová hodnota zostáva.
> **Hlavná myšlienka:** Existuje viacero spôsobov, ako sa vysporiadať s chýbajúcimi hodnotami vo vašich datasetoch. Konkrétna stratégia, ktorú použijete (odstránenie, nahradenie alebo spôsob nahradenia), by mala byť určená špecifikami daných dát. Čím viac budete pracovať s datasetmi, tým lepšie pochopíte, ako riešiť chýbajúce hodnoty.

## Odstraňovanie duplicitných dát

> **Cieľ učenia:** Na konci tejto podsekcie by ste mali byť schopní identifikovať a odstrániť duplicitné hodnoty z DataFrames.

Okrem chýbajúcich dát sa často stretnete s duplicitnými dátami v datasetoch z reálneho sveta. Našťastie, `pandas` poskytuje jednoduchý spôsob na detekciu a odstránenie duplicitných záznamov.

- **Identifikácia duplicitných hodnôt: `duplicated`**: Duplicitné hodnoty môžete ľahko identifikovať pomocou metódy `duplicated` v pandas, ktorá vracia Boolean masku indikujúcu, či je záznam v `DataFrame` duplikátom skoršieho záznamu. Vytvorme ďalší príklad `DataFrame`, aby sme si to ukázali v praxi.
```python
example4 = pd.DataFrame({'letters': ['A','B'] * 2 + ['B'],
                         'numbers': [1, 2, 1, 3, 3]})
example4
```
|      |letters|numbers|
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
- **Odstraňovanie duplicitných hodnôt: `drop_duplicates`:** jednoducho vráti kópiu dát, kde všetky hodnoty označené ako `duplicated` sú `False`:
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
Metódy `duplicated` a `drop_duplicates` štandardne zohľadňujú všetky stĺpce, ale môžete špecifikovať, že majú skúmať iba podmnožinu stĺpcov vo vašom `DataFrame`:
```python
example4.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **Hlavná myšlienka:** Odstraňovanie duplicitných dát je nevyhnutnou súčasťou takmer každého projektu v oblasti dátovej vedy. Duplicitné dáta môžu ovplyvniť výsledky vašich analýz a poskytnúť nepresné výsledky!


## 🚀 Výzva

Všetky diskutované materiály sú dostupné ako [Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb). Navyše, po každej sekcii sú k dispozícii cvičenia, vyskúšajte ich!

## [Kvíz po prednáške](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/15)



## Prehľad & Samoštúdium

Existuje mnoho spôsobov, ako objaviť a pristupovať k príprave vašich dát na analýzu a modelovanie, pričom čistenie dát je dôležitým krokom, ktorý si vyžaduje praktickú skúsenosť. Vyskúšajte tieto výzvy na Kaggle, aby ste preskúmali techniky, ktoré táto lekcia nepokrývala.

- [Výzva na čistenie dát: Parsovanie dátumov](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [Výzva na čistenie dát: Škálovanie a normalizácia dát](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)


## Zadanie

[Vyhodnotenie dát z formulára](assignment.md)

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.