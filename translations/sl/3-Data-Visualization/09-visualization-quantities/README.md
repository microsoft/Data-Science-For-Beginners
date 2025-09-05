<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "69b32b6789a91f796ebc7a02f5575e03",
  "translation_date": "2025-09-05T06:02:21+00:00",
  "source_file": "3-Data-Visualization/09-visualization-quantities/README.md",
  "language_code": "sl"
}
-->
# Vizualizacija količin

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| Vizualizacija količin - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

V tej lekciji boste raziskali, kako uporabiti eno izmed številnih Python knjižnic za ustvarjanje zanimivih vizualizacij, povezanih s konceptom količine. Z uporabo očiščenega nabora podatkov o pticah iz Minnesote lahko odkrijete številna zanimiva dejstva o lokalni divjini.  
## [Predlekcijski kviz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/16)

## Opazovanje razpona kril z Matplotlib

Odlična knjižnica za ustvarjanje tako preprostih kot tudi kompleksnih grafov in diagramov različnih vrst je [Matplotlib](https://matplotlib.org/stable/index.html). Na splošno proces risanja podatkov s temi knjižnicami vključuje identifikacijo delov vašega dataframe-a, ki jih želite obdelati, izvedbo potrebnih transformacij podatkov, dodelitev vrednosti za osi x in y, odločitev o vrsti grafa ter prikaz grafa. Matplotlib ponuja širok nabor vizualizacij, vendar se bomo v tej lekciji osredotočili na tiste, ki so najbolj primerni za vizualizacijo količin: črtni grafi, razpršeni diagrami in stolpčni diagrami.

> ✅ Uporabite najboljši graf glede na strukturo vaših podatkov in zgodbo, ki jo želite povedati.  
> - Za analizo trendov skozi čas: črtni graf  
> - Za primerjavo vrednosti: stolpčni, vrstični, tortni graf, razpršeni diagram  
> - Za prikaz, kako deli sestavljajo celoto: tortni graf  
> - Za prikaz porazdelitve podatkov: razpršeni diagram, stolpčni graf  
> - Za prikaz trendov: črtni, vrstični graf  
> - Za prikaz odnosov med vrednostmi: črtni graf, razpršeni diagram, mehurčasti graf  

Če imate nabor podatkov in želite ugotoviti, koliko določenega elementa je vključenega, bo ena izmed prvih nalog pregled njegovih vrednosti.  

✅ Na voljo so odlični 'cheat sheets' za Matplotlib [tukaj](https://matplotlib.org/cheatsheets/cheatsheets.pdf).

## Ustvarite črtni graf za vrednosti razpona kril ptic

Odprite datoteko `notebook.ipynb` v korenskem direktoriju te lekcije in dodajte celico.

> Opomba: podatki so shranjeni v korenskem direktoriju tega repozitorija v mapi `/data`.

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```  
Ti podatki so mešanica besedila in številk:

|      | Ime                          | ZnanstvenoIme          | Kategorija            | Red          | Družina  | Rod         | StatusOhranjanja   | MinDolžina | MaxDolžina | MinTeža     | MaxTeža     | MinRazponKril | MaxRazponKril |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Črno-trebušna piščalka       | Dendrocygna autumnalis | Race/Gosi/Vodne ptice | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Rjava piščalka               | Dendrocygna bicolor    | Race/Gosi/Vodne ptice | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Snežna gos                   | Anser caerulescens     | Race/Gosi/Vodne ptice | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Rossova gos                  | Anser rossii           | Race/Gosi/Vodne ptice | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Velika bela-frontna gos      | Anser albifrons        | Race/Gosi/Vodne ptice | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

Začnimo z risanjem nekaterih numeričnih podatkov z osnovnim črtnim grafom. Recimo, da želite pogled na največji razpon kril teh zanimivih ptic.

```python
wingspan = birds['MaxWingspan'] 
wingspan.plot()
```  
![Max Wingspan](../../../../3-Data-Visualization/09-visualization-quantities/images/max-wingspan-02.png)

Kaj takoj opazite? Zdi se, da obstaja vsaj en odstopajoč podatek - to je precejšen razpon kril! Razpon kril 2300 centimetrov pomeni 23 metrov - ali v Minnesoti živijo pterodaktili? Raziščimo.

Medtem ko bi lahko hitro razvrstili podatke v Excelu, da bi našli te odstopajoče podatke, nadaljujte proces vizualizacije z delom znotraj grafa.

Dodajte oznake na os x, da pokažete, za katere ptice gre:

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
![wingspan with labels](../../../../3-Data-Visualization/09-visualization-quantities/images/max-wingspan-labels-02.png)

Tudi z rotacijo oznak na 45 stopinj je preveč podatkov, da bi jih lahko prebrali. Poskusimo drugačno strategijo: označimo samo odstopajoče podatke in postavimo oznake znotraj grafa. Uporabite razpršeni diagram, da ustvarite več prostora za označevanje:

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
Kaj se tukaj dogaja? Uporabili ste `tick_params`, da skrijete spodnje oznake, nato pa ustvarili zanko nad vašim naborom podatkov o pticah. Z risanjem grafa z majhnimi modrimi pikami z uporabo `bo` ste preverili, ali ima katera ptica največji razpon kril nad 500, in če je tako, prikazali njeno oznako poleg pike. Oznake ste nekoliko premaknili na osi y (`y * (1 - 0.05)`) in uporabili ime ptice kot oznako.

Kaj ste odkrili?

![outliers](../../../../3-Data-Visualization/09-visualization-quantities/images/labeled-wingspan-02.png)  
## Filtrirajte svoje podatke

Tako plešasti orel kot prerijski sokol, čeprav verjetno zelo velike ptice, se zdita napačno označena, z dodatno `0` pri največjem razponu kril. Malo verjetno je, da boste srečali plešastega orla z razponom kril 25 metrov, vendar če ga, nas prosimo obvestite! Ustvarimo nov dataframe brez teh dveh odstopajočih podatkov:

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

Z odstranitvijo odstopajočih podatkov so vaši podatki zdaj bolj skladni in razumljivi.

![scatterplot of wingspans](../../../../3-Data-Visualization/09-visualization-quantities/images/scatterplot-wingspan-02.png)

Zdaj, ko imamo bolj čist nabor podatkov vsaj glede razpona kril, odkrijmo več o teh pticah.

Medtem ko črtni in razpršeni diagrami lahko prikazujejo informacije o vrednostih podatkov in njihovih porazdelitvah, želimo razmisliti o vrednostih, ki so inherentne temu naboru podatkov. Lahko bi ustvarili vizualizacije za odgovore na naslednja vprašanja o količinah:

> Koliko kategorij ptic obstaja in kakšno je njihovo število?  
> Koliko ptic je izumrlih, ogroženih, redkih ali pogostih?  
> Koliko jih je v različnih rodovih in redih po Linnaeusovi terminologiji?  
## Raziskovanje stolpčnih diagramov

Stolpčni diagrami so praktični, ko želite prikazati skupine podatkov. Raziskujmo kategorije ptic, ki obstajajo v tem naboru podatkov, da vidimo, katera je najpogostejša po številu.

V datoteki zvezka ustvarite osnovni stolpčni diagram.

✅ Opomba, lahko odstranite dve odstopajoči ptici, ki smo ju identificirali v prejšnjem razdelku, popravite napako v njihovem razponu kril ali ju pustite v teh vajah, ki ne temeljijo na vrednostih razpona kril.

Če želite ustvariti stolpčni diagram, lahko izberete podatke, na katere se želite osredotočiti. Stolpčni diagrami se lahko ustvarijo iz surovih podatkov:

```python
birds.plot(x='Category',
        kind='bar',
        stacked=True,
        title='Birds of Minnesota')

```  
![full data as a bar chart](../../../../3-Data-Visualization/09-visualization-quantities/images/full-data-bar-02.png)

Ta stolpčni diagram pa je neberljiv, ker je preveč nepovezanih podatkov. Izbrati morate samo podatke, ki jih želite prikazati, zato si oglejmo dolžino ptic glede na njihovo kategorijo.

Filtrirajte svoje podatke, da vključite samo kategorijo ptic.

✅ Opazite, da uporabljate Pandas za upravljanje podatkov, nato pa Matplotlib za risanje grafa.

Ker je veliko kategorij, lahko ta graf prikažete vertikalno in prilagodite njegovo višino, da upoštevate vse podatke:

```python
category_count = birds.value_counts(birds['Category'].values, sort=True)
plt.rcParams['figure.figsize'] = [6, 12]
category_count.plot.barh()
```  
![category and length](../../../../3-Data-Visualization/09-visualization-quantities/images/category-counts-02.png)

Ta stolpčni diagram prikazuje dober pregled števila ptic v vsaki kategoriji. Na prvi pogled vidite, da je največ ptic v tej regiji v kategoriji Race/Gosi/Vodne ptice. Minnesota je 'dežela 10.000 jezer', zato to ni presenetljivo!

✅ Poskusite nekaj drugih štetij na tem naboru podatkov. Vas kaj preseneti?

## Primerjava podatkov

Lahko poskusite različne primerjave skupin podatkov z ustvarjanjem novih osi. Poskusite primerjavo največje dolžine ptice glede na njeno kategorijo:

```python
maxlength = birds['MaxLength']
plt.barh(y=birds['Category'], width=maxlength)
plt.rcParams['figure.figsize'] = [6, 12]
plt.show()
```  
![comparing data](../../../../3-Data-Visualization/09-visualization-quantities/images/category-length-02.png)

Tukaj ni nič presenetljivega: kolibriji imajo najmanjšo največjo dolžino v primerjavi s pelikani ali gosmi. Dobro je, ko podatki logično ustrezajo!

Lahko ustvarite bolj zanimive vizualizacije stolpčnih diagramov z nadgradnjo podatkov. Nadgradimo minimalno in maksimalno dolžino glede na kategorijo ptic:

```python
minLength = birds['MinLength']
maxLength = birds['MaxLength']
category = birds['Category']

plt.barh(category, maxLength)
plt.barh(category, minLength)

plt.show()
```  
Na tem grafu lahko vidite razpon za vsako kategorijo ptic glede na minimalno in maksimalno dolžino. Lahko varno rečete, da je glede na te podatke večja ptica, večji je njen razpon dolžine. Fascinantno!

![superimposed values](../../../../3-Data-Visualization/09-visualization-quantities/images/superimposed-02.png)

## 🚀 Izziv

Ta nabor podatkov o pticah ponuja bogastvo informacij o različnih vrstah ptic znotraj določenega ekosistema. Poiščite po internetu in preverite, ali lahko najdete druge nabore podatkov o pticah. Vadite ustvarjanje grafov in diagramov o teh pticah, da odkrijete dejstva, ki jih niste poznali.

## [Po-lekcijski kviz](https://ff-quizzes.netlify.app/en/ds/)

## Pregled in samostojno učenje

Ta prva lekcija vam je dala nekaj informacij o tem, kako uporabiti Matplotlib za vizualizacijo količin. Raziskujte druge načine dela z nabori podatkov za vizualizacijo. [Plotly](https://github.com/plotly/plotly.py) je ena izmed knjižnic, ki je ne bomo obravnavali v teh lekcijah, zato si oglejte, kaj lahko ponudi.  
## Naloga

[Črte, razpršeni diagrami in stolpci](assignment.md)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna napačna razumevanja ali napačne interpretacije, ki bi nastale zaradi uporabe tega prevoda.