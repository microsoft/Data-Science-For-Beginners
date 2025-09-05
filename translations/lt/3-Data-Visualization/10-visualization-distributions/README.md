<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a20467e046d312809d008395051fc7",
  "translation_date": "2025-09-05T16:11:22+00:00",
  "source_file": "3-Data-Visualization/10-visualization-distributions/README.md",
  "language_code": "lt"
}
-->
# Vizualizuojame pasiskirstymus

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| Vizualizuojame pasiskirstymus - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Ankstesnėje pamokoje sužinojote keletą įdomių faktų apie Minesotos paukščių duomenų rinkinį. Aptikote klaidingų duomenų vizualizuodami išskirtis ir išanalizavote paukščių kategorijų skirtumus pagal jų maksimalų ilgį.

## [Prieš paskaitą vykdomas testas](https://ff-quizzes.netlify.app/en/ds/quiz/18)
## Tyrinėjame paukščių duomenų rinkinį

Kitas būdas gilintis į duomenis yra pažvelgti į jų pasiskirstymą arba kaip duomenys yra organizuoti pagal ašį. Pavyzdžiui, galbūt norėtumėte sužinoti apie bendrą maksimalios sparnų amplitudės ar maksimalios kūno masės pasiskirstymą Minesotos paukščių duomenų rinkinyje.

Atraskime keletą faktų apie šio duomenų rinkinio pasiskirstymus. _notebook.ipynb_ faile, esančiame šios pamokos aplanko šaknyje, importuokite Pandas, Matplotlib ir savo duomenis:

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```

|      | Pavadinimas                  | MokslinisPavadinimas   | Kategorija            | Būrys        | Šeima    | Gentis      | ApsaugosStatusas    | MinIlgis | MaxIlgis | MinKūnoMasa | MaxKūnoMasa | MinSparnųAmplitudė | MaxSparnųAmplitudė |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | -----------------: | -----------------: |
|    0 | Juodapilvė švilpiko antis    | Dendrocygna autumnalis | Antys/Žąsys/Vandenspaukščiai | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76        |          94        |
|    1 | Rudašvilpė antis             | Dendrocygna bicolor    | Antys/Žąsys/Vandenspaukščiai | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85        |          93        |
|    2 | Snieginė žąsis               | Anser caerulescens     | Antys/Žąsys/Vandenspaukščiai | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135        |         165        |
|    3 | Roso žąsis                   | Anser rossii           | Antys/Žąsys/Vandenspaukščiai | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113        |         116        |
|    4 | Didžioji baltakaktė žąsis    | Anser albifrons        | Antys/Žąsys/Vandenspaukščiai | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130        |         165        |

Apskritai, greitai galite pažvelgti į duomenų pasiskirstymą naudodami sklaidos diagramą, kaip darėme ankstesnėje pamokoje:

```python
birds.plot(kind='scatter',x='MaxLength',y='Order',figsize=(12,8))

plt.title('Max Length per Order')
plt.ylabel('Order')
plt.xlabel('Max Length')

plt.show()
```
![maksimalus ilgis pagal būrį](../../../../3-Data-Visualization/10-visualization-distributions/images/scatter-wb.png)

Tai suteikia bendrą paukščių kūno ilgio pasiskirstymo pagal būrį apžvalgą, tačiau tai nėra optimalus būdas tikriems pasiskirstymams parodyti. Šią užduotį paprastai atlieka histograma.

## Darbas su histogramomis

Matplotlib siūlo puikius būdus vizualizuoti duomenų pasiskirstymą naudojant histogramas. Šio tipo diagrama yra panaši į stulpelinę diagramą, kur pasiskirstymas matomas per stulpelių kilimą ir kritimą. Norint sukurti histogramą, reikia skaitinių duomenų. Histogramą galite sukurti, nurodydami diagramos tipą kaip 'hist'. Ši diagrama rodo MaxBodyMass pasiskirstymą visame duomenų rinkinyje. Padalindama jai pateiktą duomenų masyvą į mažesnius intervalus, ji gali parodyti duomenų reikšmių pasiskirstymą:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 10, figsize = (12,12))
plt.show()
```
![pasiskirstymas visame duomenų rinkinyje](../../../../3-Data-Visualization/10-visualization-distributions/images/dist1-wb.png)

Kaip matote, dauguma iš 400+ paukščių šiame duomenų rinkinyje patenka į mažesnę nei 2000 Max Kūno Masės ribą. Gaukite daugiau įžvalgų apie duomenis pakeisdami `bins` parametrą į didesnį skaičių, pavyzdžiui, 30:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 30, figsize = (12,12))
plt.show()
```
![pasiskirstymas su didesniu bins parametru](../../../../3-Data-Visualization/10-visualization-distributions/images/dist2-wb.png)

Ši diagrama rodo pasiskirstymą šiek tiek detaliau. Mažiau į kairę pasvirusią diagramą galima sukurti užtikrinant, kad pasirinktumėte tik duomenis tam tikrame diapazone:

Filtruokite savo duomenis, kad gautumėte tik tuos paukščius, kurių kūno masė yra mažesnė nei 60, ir parodykite 40 `bins`:

```python
filteredBirds = birds[(birds['MaxBodyMass'] > 1) & (birds['MaxBodyMass'] < 60)]      
filteredBirds['MaxBodyMass'].plot(kind = 'hist',bins = 40,figsize = (12,12))
plt.show()     
```
![filtruota histograma](../../../../3-Data-Visualization/10-visualization-distributions/images/dist3-wb.png)

✅ Išbandykite kitus filtrus ir duomenų taškus. Norėdami pamatyti visą duomenų pasiskirstymą, pašalinkite `['MaxBodyMass']` filtrą, kad parodytumėte pažymėtus pasiskirstymus.

Histogramoje taip pat galima išbandyti spalvų ir žymėjimo patobulinimus:

Sukurkite 2D histogramą, kad palygintumėte dviejų pasiskirstymų santykį. Palyginkime `MaxBodyMass` ir `MaxLength`. Matplotlib siūlo įmontuotą būdą parodyti susiliejimą naudojant ryškesnes spalvas:

```python
x = filteredBirds['MaxBodyMass']
y = filteredBirds['MaxLength']

fig, ax = plt.subplots(tight_layout=True)
hist = ax.hist2d(x, y)
```
Atrodo, kad tarp šių dviejų elementų yra tikėtinas koreliavimas pagal numatomą ašį, su viena ypač stipria susiliejimo vieta:

![2D diagrama](../../../../3-Data-Visualization/10-visualization-distributions/images/2D-wb.png)

Histogramos gerai veikia pagal nutylėjimą su skaitiniais duomenimis. O kas, jei reikia pamatyti pasiskirstymus pagal tekstinius duomenis? 
## Tyrinėjame duomenų rinkinį pagal tekstinius duomenis

Šiame duomenų rinkinyje taip pat yra naudinga informacija apie paukščių kategoriją, jų gentį, rūšį, šeimą ir apsaugos statusą. Pažvelkime į šią apsaugos informaciją. Koks yra paukščių pasiskirstymas pagal jų apsaugos statusą?

> ✅ Duomenų rinkinyje naudojami keli akronimai, apibūdinantys apsaugos statusą. Šie akronimai yra iš [IUCN Raudonojo sąrašo kategorijų](https://www.iucnredlist.org/), organizacijos, kataloguojančios rūšių statusą.
> 
> - CR: Kritiškai nykstantis
> - EN: Nykstantis
> - EX: Išnykęs
> - LC: Mažiausiai susirūpinimą keliantis
> - NT: Beveik nykstantis
> - VU: Pažeidžiamas

Tai yra tekstinės reikšmės, todėl norint sukurti histogramą reikės atlikti transformaciją. Naudodami `filteredBirds` duomenų rėmelį, parodykite jo apsaugos statusą kartu su minimaliu sparnų amplitudės dydžiu. Ką pastebite?

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

![sparnų amplitudė ir apsaugos statusas](../../../../3-Data-Visualization/10-visualization-distributions/images/histogram-conservation-wb.png)

Atrodo, kad nėra gero ryšio tarp minimalaus sparnų amplitudės dydžio ir apsaugos statuso. Išbandykite kitus duomenų rinkinio elementus naudodami šį metodą. Taip pat galite išbandyti skirtingus filtrus. Ar pastebite kokį nors ryšį?

## Tankio diagramos

Galbūt pastebėjote, kad iki šiol nagrinėtos histogramos yra „laiptinės“ ir nesudaro sklandžios kreivės. Norėdami parodyti sklandesnę tankio diagramą, galite išbandyti tankio diagramą.

Norėdami dirbti su tankio diagramomis, susipažinkite su nauja braižymo biblioteka, [Seaborn](https://seaborn.pydata.org/generated/seaborn.kdeplot.html). 

Įkėlę Seaborn, išbandykite paprastą tankio diagramą:

```python
import seaborn as sns
import matplotlib.pyplot as plt
sns.kdeplot(filteredBirds['MinWingspan'])
plt.show()
```
![Tankio diagrama](../../../../3-Data-Visualization/10-visualization-distributions/images/density1.png)

Galite matyti, kaip ši diagrama atspindi ankstesnę minimalaus sparnų amplitudės duomenų diagramą; ji tiesiog yra šiek tiek sklandesnė. Pasak Seaborn dokumentacijos, „Palyginti su histograma, KDE gali sukurti diagramą, kuri yra mažiau užgriozdinta ir lengviau interpretuojama, ypač kai braižomos kelios pasiskirstymo kreivės. Tačiau ji gali sukelti iškraipymus, jei pagrindinis pasiskirstymas yra ribotas arba nesudaro sklandžios kreivės. Kaip ir histograma, atvaizdavimo kokybė taip pat priklauso nuo gerų lyginimo parametrų pasirinkimo.“ [šaltinis](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) Kitaip tariant, išskirtys, kaip visada, gali iškreipti jūsų diagramas.

Jei norėtumėte peržiūrėti tą dantytą MaxBodyMass liniją antroje sukurtoje diagramoje, galėtumėte ją labai gerai išlyginti naudodami šį metodą:

```python
sns.kdeplot(filteredBirds['MaxBodyMass'])
plt.show()
```
![lyginta kūno masės linija](../../../../3-Data-Visualization/10-visualization-distributions/images/density2.png)

Jei norėtumėte sklandžios, bet ne per daug sklandžios linijos, redaguokite `bw_adjust` parametrą:

```python
sns.kdeplot(filteredBirds['MaxBodyMass'], bw_adjust=.2)
plt.show()
```
![mažiau lyginta kūno masės linija](../../../../3-Data-Visualization/10-visualization-distributions/images/density3.png)

✅ Perskaitykite apie šio tipo diagramos parametrus ir eksperimentuokite!

Šio tipo diagrama siūlo puikiai paaiškinančias vizualizacijas. Pavyzdžiui, keliais kodo eilutėmis galite parodyti maksimalios kūno masės tankį pagal paukščių būrį:

```python
sns.kdeplot(
   data=filteredBirds, x="MaxBodyMass", hue="Order",
   fill=True, common_norm=False, palette="crest",
   alpha=.5, linewidth=0,
)
```

![kūno masė pagal būrį](../../../../3-Data-Visualization/10-visualization-distributions/images/density4.png)

Taip pat galite vienoje diagramoje pavaizduoti kelių kintamųjų tankį. Palyginkite paukščio MaxLength ir MinLength su jų apsaugos statusu:

```python
sns.kdeplot(data=filteredBirds, x="MinLength", y="MaxLength", hue="ConservationStatus")
```

![kelios tankio kreivės, uždengtos viena ant kitos](../../../../3-Data-Visualization/10-visualization-distributions/images/multi.png)

Galbūt verta ištirti, ar „Pažeidžiamų“ paukščių grupė pagal jų ilgius yra reikšminga.

## 🚀 Iššūkis

Histogramos yra sudėtingesnis diagramos tipas nei paprastos sklaidos, stulpelinės ar linijinės diagramos. Ieškokite internete gerų histogramų naudojimo pavyzdžių. Kaip jos naudojamos, ką jos demonstruoja ir kokiose srityse ar tyrimų srityse jos dažniausiai naudojamos?

## [Po paskaitos vykdomas testas](https://ff-quizzes.netlify.app/en/ds/quiz/19)

## Peržiūra ir savarankiškas mokymasis

Šioje pamokoje naudojote Matplotlib ir pradėjote dirbti su Seaborn, kad sukurtumėte sudėtingesnes diagramas. Atlikite tyrimą apie `kdeplot` Seaborn bibliotekoje, „nepertraukiamą tikimybių tankio kreivę vienoje ar keliose dimensijose“. Perskaitykite [dokumentaciją](https://seaborn.pydata.org/generated/seaborn.kdeplot.html), kad suprastumėte, kaip ji veikia.

## Užduotis

[Praktikuokite savo įgūdžius](assignment.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.