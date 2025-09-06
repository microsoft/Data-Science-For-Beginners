<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a20467e046d312809d008395051fc7",
  "translation_date": "2025-09-05T18:11:39+00:00",
  "source_file": "3-Data-Visualization/10-visualization-distributions/README.md",
  "language_code": "sk"
}
-->
# Vizualizácia distribúcií

|![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| Vizualizácia distribúcií - _Sketchnote od [@nitya](https://twitter.com/nitya)_ |

V predchádzajúcej lekcii ste sa dozvedeli niekoľko zaujímavých faktov o dátach týkajúcich sa vtákov z Minnesoty. Objavili ste chybné údaje vizualizáciou odľahlých hodnôt a pozreli ste sa na rozdiely medzi kategóriami vtákov podľa ich maximálnej dĺžky.

## [Kvíz pred prednáškou](https://ff-quizzes.netlify.app/en/ds/quiz/18)
## Preskúmajte dataset vtákov

Ďalším spôsobom, ako sa ponoriť do dát, je pozrieť sa na ich distribúciu, teda na to, ako sú údaje usporiadané pozdĺž osi. Možno by ste napríklad chceli zistiť všeobecnú distribúciu maximálneho rozpätia krídel alebo maximálnej telesnej hmotnosti vtákov z Minnesoty v tomto datasete.

Poďme objaviť niekoľko faktov o distribúciách dát v tomto datasete. V súbore _notebook.ipynb_ v koreňovom adresári tejto lekcie importujte Pandas, Matplotlib a vaše dáta:

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```

|      | Názov                        | Vedecký názov          | Kategória             | Rad          | Čeľaď    | Rod         | Stav ochrany         | MinDĺžka | MaxDĺžka | MinHmotnosť | MaxHmotnosť | MinRozpätie | MaxRozpätie |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :------------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Čiernobruchá pískajúca kačica | Dendrocygna autumnalis | Kačice/Husi/Vodné vtáky | Anseriformes | Anatidae | Dendrocygna | LC                   |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Hnedá pískajúca kačica        | Dendrocygna bicolor    | Kačice/Husi/Vodné vtáky | Anseriformes | Anatidae | Dendrocygna | LC                   |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Snežná hus                   | Anser caerulescens     | Kačice/Husi/Vodné vtáky | Anseriformes | Anatidae | Anser       | LC                   |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Rossova hus                  | Anser rossii           | Kačice/Husi/Vodné vtáky | Anseriformes | Anatidae | Anser       | LC                   |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Veľká bieločelá hus          | Anser albifrons        | Kačice/Husi/Vodné vtáky | Anseriformes | Anatidae | Anser       | LC                   |        64 |        81 |        1930 |        3310 |         130 |         165 |

Vo všeobecnosti môžete rýchlo pozrieť na spôsob, akým sú dáta distribuované, pomocou bodového grafu, ako sme to urobili v predchádzajúcej lekcii:

```python
birds.plot(kind='scatter',x='MaxLength',y='Order',figsize=(12,8))

plt.title('Max Length per Order')
plt.ylabel('Order')
plt.xlabel('Max Length')

plt.show()
```
![max dĺžka podľa radu](../../../../3-Data-Visualization/10-visualization-distributions/images/scatter-wb.png)

Toto poskytuje prehľad o všeobecnej distribúcii dĺžky tela podľa radu vtákov, ale nie je to optimálny spôsob zobrazenia skutočných distribúcií. Na tento účel sa zvyčajne používa histogram.
## Práca s histogramami

Matplotlib ponúka veľmi dobré spôsoby vizualizácie distribúcie dát pomocou histogramov. Tento typ grafu je podobný stĺpcovému grafu, kde distribúciu možno vidieť prostredníctvom stúpania a klesania stĺpcov. Na vytvorenie histogramu potrebujete numerické údaje. Na vytvorenie histogramu môžete nakresliť graf, kde definujete typ ako 'hist' pre histogram. Tento graf ukazuje distribúciu MaxBodyMass pre celý rozsah numerických dát v datasete. Rozdelením poľa dát na menšie intervaly (bins) môže zobraziť distribúciu hodnôt dát:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 10, figsize = (12,12))
plt.show()
```
![distribúcia v celom datasete](../../../../3-Data-Visualization/10-visualization-distributions/images/dist1-wb.png)

Ako vidíte, väčšina z viac ako 400 vtákov v tomto datasete spadá do rozsahu pod 2000 pre ich maximálnu telesnú hmotnosť. Získajte viac informácií o dátach zmenou parametra `bins` na vyššie číslo, napríklad 30:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 30, figsize = (12,12))
plt.show()
```
![distribúcia v celom datasete s väčším parametrom bins](../../../../3-Data-Visualization/10-visualization-distributions/images/dist2-wb.png)

Tento graf ukazuje distribúciu trochu podrobnejšie. Graf menej skreslený doľava by sa dal vytvoriť tým, že by ste vybrali iba dáta v danom rozsahu:

Filtrovať svoje dáta tak, aby ste získali iba tie vtáky, ktorých telesná hmotnosť je pod 60, a zobraziť 40 `bins`:

```python
filteredBirds = birds[(birds['MaxBodyMass'] > 1) & (birds['MaxBodyMass'] < 60)]      
filteredBirds['MaxBodyMass'].plot(kind = 'hist',bins = 40,figsize = (12,12))
plt.show()     
```
![filtrovaný histogram](../../../../3-Data-Visualization/10-visualization-distributions/images/dist3-wb.png)

✅ Vyskúšajte niektoré ďalšie filtre a dátové body. Ak chcete vidieť celú distribúciu dát, odstráňte filter `['MaxBodyMass']`, aby ste zobrazili označené distribúcie.

Histogram ponúka aj niektoré pekné farebné a označovacie vylepšenia, ktoré môžete vyskúšať:

Vytvorte 2D histogram na porovnanie vzťahu medzi dvoma distribúciami. Porovnajme `MaxBodyMass` vs. `MaxLength`. Matplotlib ponúka zabudovaný spôsob zobrazenia konvergencie pomocou jasnejších farieb:

```python
x = filteredBirds['MaxBodyMass']
y = filteredBirds['MaxLength']

fig, ax = plt.subplots(tight_layout=True)
hist = ax.hist2d(x, y)
```
Zdá sa, že existuje očakávaná korelácia medzi týmito dvoma prvkami pozdĺž očakávanej osi, s jedným obzvlášť silným bodom konvergencie:

![2D graf](../../../../3-Data-Visualization/10-visualization-distributions/images/2D-wb.png)

Histogramy fungujú dobre predvolene pre numerické údaje. Čo ak potrebujete vidieť distribúcie podľa textových údajov? 
## Preskúmajte dataset pre distribúcie pomocou textových údajov 

Tento dataset obsahuje aj dobré informácie o kategórii vtákov, ich rode, druhu, čeľadi, ako aj o ich stave ochrany. Poďme sa ponoriť do informácií o stave ochrany. Aká je distribúcia vtákov podľa ich stavu ochrany?

> ✅ V datasete sa používajú rôzne skratky na opis stavu ochrany. Tieto skratky pochádzajú z [IUCN Red List Categories](https://www.iucnredlist.org/), organizácie, ktorá katalogizuje stav druhov.
> 
> - CR: Kriticky ohrozený
> - EN: Ohrozený
> - EX: Vyhynutý
> - LC: Najmenšie obavy
> - NT: Takmer ohrozený
> - VU: Zraniteľný

Tieto hodnoty sú textové, takže budete musieť vykonať transformáciu na vytvorenie histogramu. Pomocou dataframe `filteredBirds` zobrazte jeho stav ochrany spolu s minimálnym rozpätím krídel. Čo vidíte? 

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

![rozpätie krídel a stav ochrany](../../../../3-Data-Visualization/10-visualization-distributions/images/histogram-conservation-wb.png)

Zdá sa, že neexistuje dobrá korelácia medzi minimálnym rozpätím krídel a stavom ochrany. Otestujte ďalšie prvky datasetu pomocou tejto metódy. Môžete vyskúšať rôzne filtre. Nájdete nejakú koreláciu?

## Hustotné grafy

Možno ste si všimli, že histogramy, ktoré sme doteraz videli, sú "krokové" a neplynú hladko v oblúku. Na zobrazenie hladšieho hustotného grafu môžete vyskúšať hustotný graf.

Na prácu s hustotnými grafmi sa oboznámte s novou knižnicou na tvorbu grafov, [Seaborn](https://seaborn.pydata.org/generated/seaborn.kdeplot.html). 

Načítajte Seaborn a vyskúšajte základný hustotný graf:

```python
import seaborn as sns
import matplotlib.pyplot as plt
sns.kdeplot(filteredBirds['MinWingspan'])
plt.show()
```
![Hustotný graf](../../../../3-Data-Visualization/10-visualization-distributions/images/density1.png)

Vidíte, ako graf odráža ten predchádzajúci pre údaje o minimálnom rozpätí krídel; je len trochu hladší. Podľa dokumentácie Seaborn, "V porovnaní s histogramom môže KDE vytvoriť graf, ktorý je menej preplnený a ľahšie interpretovateľný, najmä pri kreslení viacerých distribúcií. Ale má potenciál zaviesť skreslenia, ak je základná distribúcia ohraničená alebo nie je hladká. Podobne ako histogram, kvalita reprezentácie tiež závisí od výberu dobrých parametrov vyhladzovania." [zdroj](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) Inými slovami, odľahlé hodnoty ako vždy spôsobia, že vaše grafy budú zle fungovať.

Ak by ste chceli znovu navštíviť tú zubatú čiaru MaxBodyMass v druhom grafe, ktorý ste vytvorili, mohli by ste ju veľmi dobre vyhladiť tým, že ju znovu vytvoríte pomocou tejto metódy:

```python
sns.kdeplot(filteredBirds['MaxBodyMass'])
plt.show()
```
![hladká čiara telesnej hmotnosti](../../../../3-Data-Visualization/10-visualization-distributions/images/density2.png)

Ak by ste chceli hladkú, ale nie príliš hladkú čiaru, upravte parameter `bw_adjust`: 

```python
sns.kdeplot(filteredBirds['MaxBodyMass'], bw_adjust=.2)
plt.show()
```
![menej hladká čiara telesnej hmotnosti](../../../../3-Data-Visualization/10-visualization-distributions/images/density3.png)

✅ Prečítajte si o dostupných parametroch pre tento typ grafu a experimentujte!

Tento typ grafu ponúka krásne vysvetľujúce vizualizácie. S niekoľkými riadkami kódu môžete napríklad zobraziť hustotu maximálnej telesnej hmotnosti podľa radu vtákov:

```python
sns.kdeplot(
   data=filteredBirds, x="MaxBodyMass", hue="Order",
   fill=True, common_norm=False, palette="crest",
   alpha=.5, linewidth=0,
)
```

![telesná hmotnosť podľa radu](../../../../3-Data-Visualization/10-visualization-distributions/images/density4.png)

Môžete tiež mapovať hustotu viacerých premenných v jednom grafe. Skúste porovnať MaxLength a MinLength vtákov podľa ich stavu ochrany:

```python
sns.kdeplot(data=filteredBirds, x="MinLength", y="MaxLength", hue="ConservationStatus")
```

![viac hustôt, prekryté](../../../../3-Data-Visualization/10-visualization-distributions/images/multi.png)

Možno stojí za to preskúmať, či je zhluk "Zraniteľných" vtákov podľa ich dĺžok významný alebo nie.

## 🚀 Výzva

Histogramy sú sofistikovanejší typ grafu ako základné bodové grafy, stĺpcové grafy alebo čiarové grafy. Vyhľadajte na internete dobré príklady použitia histogramov. Ako sa používajú, čo demonštrujú a v akých oblastiach alebo oblastiach výskumu sa zvyčajne používajú?

## [Kvíz po prednáške](https://ff-quizzes.netlify.app/en/ds/quiz/19)

## Prehľad a samostatné štúdium

V tejto lekcii ste použili Matplotlib a začali pracovať so Seaborn na zobrazenie sofistikovanejších grafov. Urobte si výskum o `kdeplot` v Seaborn, "kontinuálna krivka hustoty pravdepodobnosti v jednej alebo viacerých dimenziách". Prečítajte si [dokumentáciu](https://seaborn.pydata.org/generated/seaborn.kdeplot.html), aby ste pochopili, ako funguje.

## Zadanie

[Uplatnite svoje zručnosti](assignment.md)

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.