<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "43c402d9d90ae6da55d004519ada5033",
  "translation_date": "2025-08-26T17:24:12+00:00",
  "source_file": "3-Data-Visualization/09-visualization-quantities/README.md",
  "language_code": "sk"
}
-->
# Vizualizácia množstiev

|![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| Vizualizácia množstiev - _Sketchnote od [@nitya](https://twitter.com/nitya)_ |

V tejto lekcii preskúmate, ako používať jednu z mnohých dostupných knižníc Pythonu na vytváranie zaujímavých vizualizácií založených na koncepte množstva. Pomocou vyčisteného datasetu o vtákoch z Minnesoty sa môžete dozvedieť veľa zaujímavých faktov o miestnej faune.  
## [Kvíz pred prednáškou](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/16)

## Pozorovanie rozpätia krídel pomocou Matplotlib

Vynikajúcou knižnicou na vytváranie jednoduchých aj sofistikovaných grafov a diagramov rôznych typov je [Matplotlib](https://matplotlib.org/stable/index.html). Vo všeobecnosti proces vykresľovania údajov pomocou týchto knižníc zahŕňa identifikáciu častí vášho dataframe, ktoré chcete zacieliť, vykonanie potrebných transformácií na týchto údajoch, priradenie hodnôt osi x a y, rozhodnutie o type grafu a následné zobrazenie grafu. Matplotlib ponúka širokú škálu vizualizácií, ale v tejto lekcii sa zameriame na tie najvhodnejšie na vizualizáciu množstva: čiarové grafy, bodové grafy a stĺpcové grafy.

> ✅ Použite najlepší typ grafu podľa štruktúry vašich údajov a príbehu, ktorý chcete rozprávať.  
> - Na analýzu trendov v čase: čiarový graf  
> - Na porovnanie hodnôt: stĺpcový, koláčový, bodový graf  
> - Na zobrazenie vzťahu častí k celku: koláčový graf  
> - Na zobrazenie distribúcie údajov: bodový, stĺpcový graf  
> - Na zobrazenie trendov: čiarový, stĺpcový graf  
> - Na zobrazenie vzťahov medzi hodnotami: čiarový, bodový, bublinový graf  

Ak máte dataset a potrebujete zistiť, koľko konkrétnej položky je zahrnuté, jednou z prvých úloh bude preskúmať jeho hodnoty.  

✅ Existujú veľmi dobré 'cheat sheets' pre Matplotlib [tu](https://matplotlib.org/cheatsheets/cheatsheets.pdf).

## Vytvorenie čiarového grafu o hodnotách rozpätia krídel vtákov

Otvorte súbor `notebook.ipynb` v koreňovom adresári tejto lekcie a pridajte bunku.

> Poznámka: údaje sú uložené v koreňovom adresári tohto repozitára v priečinku `/data`.

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```  
Tieto údaje sú kombináciou textu a čísel:

|      | Názov                        | Vedecký názov          | Kategória             | Rad          | Rodina   | Rod         | Stav ochrany         | MinDĺžka | MaxDĺžka | MinHmotnosť | MaxHmotnosť | MinRozpätie | MaxRozpätie |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :------------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Black-bellied whistling-duck | Dendrocygna autumnalis | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                   |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Fulvous whistling-duck       | Dendrocygna bicolor    | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                   |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Snow goose                   | Anser caerulescens     | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                   |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Ross's goose                 | Anser rossii           | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                   |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Greater white-fronted goose  | Anser albifrons        | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                   |        64 |        81 |        1930 |        3310 |         130 |         165 |

Začnime vykreslením niektorých číselných údajov pomocou základného čiarového grafu. Predpokladajme, že chcete zobraziť maximálne rozpätie krídel týchto zaujímavých vtákov.

```python
wingspan = birds['MaxWingspan'] 
wingspan.plot()
```  
![Max Rozpätie](../../../../translated_images/max-wingspan-02.e79fd847b2640b89e21e340a3a9f4c5d4b224c4fcd65f54385e84f1c9ed26d52.sk.png)

Čo si všimnete okamžite? Zdá sa, že existuje aspoň jeden extrémny údaj - to je dosť veľké rozpätie krídel! Rozpätie krídel 2300 centimetrov sa rovná 23 metrom - potulujú sa v Minnesote pterodaktyly? Poďme to preskúmať.

Aj keď by ste mohli rýchlo zoradiť údaje v Exceli, aby ste našli tieto extrémne údaje, ktoré sú pravdepodobne preklepy, pokračujte vo vizualizačnom procese priamo z grafu.

Pridajte štítky na os x, aby ste ukázali, o aké vtáky ide:

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
![rozpätie krídel so štítkami](../../../../translated_images/max-wingspan-labels-02.aa90e826ca49a9d1dde78075e9755c1849ef56a4e9ec60f7e9f3806daf9283e2.sk.png)

Aj keď sú štítky otočené o 45 stupňov, je ich príliš veľa na čítanie. Skúsme inú stratégiu: označte iba tie extrémne údaje a nastavte štítky priamo v grafe. Môžete použiť bodový graf, aby ste získali viac miesta na označovanie:

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
Čo sa tu deje? Použili ste `tick_params` na skrytie spodných štítkov a potom ste vytvorili slučku nad datasetom vtákov. Vykreslením grafu s malými modrými bodkami pomocou `bo` ste skontrolovali, či má nejaký vták maximálne rozpätie krídel nad 500, a ak áno, zobrazili ste jeho štítok vedľa bodky. Štítky ste trochu posunuli na osi y (`y * (1 - 0.05)`) a použili názov vtáka ako štítok.

Čo ste zistili?

![extrémne údaje](../../../../translated_images/labeled-wingspan-02.6110e2d2401cd5238ccc24dfb6d04a6c19436101f6cec151e3992e719f9f1e1f.sk.png)  
## Filtrovanie údajov

Orol skalný a sokol prériový, aj keď sú pravdepodobne veľmi veľké vtáky, sa zdajú byť nesprávne označené, s pridanou `0` v ich maximálnom rozpätí krídel. Je nepravdepodobné, že by ste stretli orla skalného s rozpätím krídel 25 metrov, ale ak áno, dajte nám vedieť! Vytvorme nový dataframe bez týchto dvoch extrémnych údajov:

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

Odstránením extrémnych údajov sú vaše údaje teraz súdržnejšie a zrozumiteľnejšie.

![bodový graf rozpätí krídel](../../../../translated_images/scatterplot-wingspan-02.1c33790094ce36a75f5fb45b25ed2cf27f0356ea609e43c11e97a2cedd7011a4.sk.png)

Teraz, keď máme čistejší dataset aspoň z hľadiska rozpätia krídel, poďme objaviť viac o týchto vtákoch.

Aj keď čiarové a bodové grafy môžu zobrazovať informácie o hodnotách údajov a ich distribúciách, chceme premýšľať o hodnotách obsiahnutých v tomto datasete. Mohli by ste vytvoriť vizualizácie na zodpovedanie nasledujúcich otázok o množstve:

> Koľko kategórií vtákov existuje a aké sú ich počty?  
> Koľko vtákov je vyhynutých, ohrozených, vzácnych alebo bežných?  
> Koľko je rôznych rodov a radov podľa Linnaeusovej terminológie?  
## Preskúmanie stĺpcových grafov

Stĺpcové grafy sú praktické, keď potrebujete zobraziť skupiny údajov. Preskúmajme kategórie vtákov, ktoré existujú v tomto datasete, aby sme zistili, ktorá je najbežnejšia podľa počtu.

V súbore notebooku vytvorte základný stĺpcový graf.

✅ Poznámka: Môžete buď filtrovať dva extrémne údaje vtákov, ktoré sme identifikovali v predchádzajúcej časti, upraviť preklep v ich rozpätí krídel, alebo ich ponechať pre tieto cvičenia, ktoré nezávisia od hodnôt rozpätia krídel.

Ak chcete vytvoriť stĺpcový graf, môžete vybrať údaje, na ktoré sa chcete zamerať. Stĺpcové grafy môžu byť vytvorené z nespracovaných údajov:

```python
birds.plot(x='Category',
        kind='bar',
        stacked=True,
        title='Birds of Minnesota')

```  
![celé údaje ako stĺpcový graf](../../../../translated_images/full-data-bar-02.aaa3fda71c63ed564b917841a1886c177dd9a26424142e510c0c0498fd6ca160.sk.png)

Tento stĺpcový graf je však nečitateľný, pretože je tu príliš veľa nezhromaždených údajov. Musíte vybrať iba údaje, ktoré chcete vykresliť, takže sa pozrime na dĺžku vtákov podľa ich kategórie.

Filtrovanie údajov na zahrnutie iba kategórie vtákov.

✅ Všimnite si, že používate Pandas na správu údajov a potom necháte Matplotlib vykresliť graf.

Keďže existuje veľa kategórií, môžete tento graf zobraziť vertikálne a upraviť jeho výšku, aby ste zohľadnili všetky údaje:

```python
category_count = birds.value_counts(birds['Category'].values, sort=True)
plt.rcParams['figure.figsize'] = [6, 12]
category_count.plot.barh()
```  
![kategória a dĺžka](../../../../translated_images/category-counts-02.0b9a0a4de42275ae5096d0f8da590d8bf520d9e7e40aad5cc4fc8d276480cc32.sk.png)

Tento stĺpcový graf poskytuje dobrý prehľad o počte vtákov v každej kategórii. Na prvý pohľad vidíte, že najväčší počet vtákov v tomto regióne patrí do kategórie Ducks/Geese/Waterfowl. Minnesota je 'krajina 10 000 jazier', takže to nie je prekvapujúce!

✅ Skúste niektoré ďalšie počty v tomto datasete. Prekvapilo vás niečo?

## Porovnávanie údajov

Môžete skúsiť rôzne porovnania zoskupených údajov vytvorením nových osí. Skúste porovnanie MaxDĺžky vtákov podľa ich kategórie:

```python
maxlength = birds['MaxLength']
plt.barh(y=birds['Category'], width=maxlength)
plt.rcParams['figure.figsize'] = [6, 12]
plt.show()
```  
![porovnávanie údajov](../../../../translated_images/category-length-02.7304bf519375c9807d8165cc7ec60dd2a60f7b365b23098538e287d89adb7d76.sk.png)

Tu nie je nič prekvapujúce: kolibríky majú najmenšiu MaxDĺžku v porovnaní s pelikánmi alebo husami. Je dobré, keď údaje dávajú logický zmysel!

Môžete vytvoriť zaujímavejšie vizualizácie stĺpcových grafov prekrytím údajov. Prekryme Minimálnu a Maximálnu Dĺžku na danej kategórii vtákov:

```python
minLength = birds['MinLength']
maxLength = birds['MaxLength']
category = birds['Category']

plt.barh(category, maxLength)
plt.barh(category, minLength)

plt.show()
```  
V tomto grafe môžete vidieť rozsah pre kategóriu vtákov Minimálnej Dĺžky a Maximálnej Dĺžky. Môžete bezpečne povedať, že podľa týchto údajov, čím väčší vták, tým väčší rozsah jeho dĺžky. Fascinujúce!

![prekryté hodnoty](../../../../translated_images/superimposed-02.f03058536baeb2ed7864f01102538464d4c2fd7ade881ddd7d5ba74dc5d2fdae.sk.png)

## 🚀 Výzva

Tento dataset vtákov ponúka množstvo informácií o rôznych typoch vtákov v konkrétnom ekosystéme. Vyhľadajte na internete ďalšie datasety zamerané na vtáky. Precvičte si vytváranie grafov a diagramov o týchto vtákoch, aby ste objavili fakty, ktoré ste si neuvedomovali.  
## [Kvíz po prednáške](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/17)

## Prehľad a samostatné štúdium

Táto prvá lekcia vám poskytla niekoľko informácií o tom, ako používať Matplotlib na vizualizáciu množstiev. Urobte si výskum o iných spôsoboch práce s datasetmi na vizualizáciu. [Plotly](https://github.com/plotly/plotly.py) je jedna z možností, ktorú v týchto lekciách nebudeme pokrývať, takže sa pozrite, čo môže ponúknuť.  
## Zadanie

[Čiary, bodky a stĺpce](assignment.md)

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.