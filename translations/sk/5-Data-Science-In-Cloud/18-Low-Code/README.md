<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd4da10766c64fce4294a98f6479dfb0",
  "translation_date": "2025-09-05T18:00:08+00:00",
  "source_file": "5-Data-Science-In-Cloud/18-Low-Code/README.md",
  "language_code": "sk"
}
-->
# Data Science v cloude: Cesta "Low code/No code"

|![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/18-DataScience-Cloud.png)|
|:---:|
| Data Science v cloude: Low Code - _Sketchnote od [@nitya](https://twitter.com/nitya)_ |

Obsah:

- [Data Science v cloude: Cesta "Low code/No code"](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Kvíz pred prednáškou](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [1. Úvod](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [1.1 Čo je Azure Machine Learning?](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [1.2 Projekt predikcie zlyhania srdca:](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [1.3 Dataset zlyhania srdca:](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [2. Tréning modelu v Azure ML Studio pomocou Low code/No code](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.1 Vytvorenie pracovného priestoru Azure ML](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.2 Výpočtové zdroje](../../../../5-Data-Science-In-Cloud/18-Low-Code)
      - [2.2.1 Výber správnych možností pre vaše výpočtové zdroje](../../../../5-Data-Science-In-Cloud/18-Low-Code)
      - [2.2.2 Vytvorenie výpočtového klastru](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.3 Načítanie datasetu](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.4 Tréning pomocou AutoML s Low code/No code](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [3. Nasadenie modelu a využitie endpointov pomocou Low code/No code](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [3.1 Nasadenie modelu](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [3.2 Využitie endpointov](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [🚀 Výzva](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Kvíz po prednáške](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Recenzia a samostatné štúdium](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Úloha](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  
## [Kvíz pred prednáškou](https://ff-quizzes.netlify.app/en/ds/quiz/34)

## 1. Úvod
### 1.1 Čo je Azure Machine Learning?

Platforma Azure cloud obsahuje viac ako 200 produktov a cloudových služieb navrhnutých na to, aby vám pomohli priniesť nové riešenia do života. 
Dátoví vedci vynakladajú veľké úsilie na skúmanie a predspracovanie dát, ako aj na testovanie rôznych algoritmov na tréning modelov, aby dosiahli presné výsledky. Tieto úlohy sú časovo náročné a často neefektívne využívajú drahé výpočtové zdroje.

[Azure ML](https://docs.microsoft.com/azure/machine-learning/overview-what-is-azure-machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) je cloudová platforma na vytváranie a prevádzkovanie riešení strojového učenia v Azure. Obsahuje širokú škálu funkcií a možností, ktoré pomáhajú dátovým vedcom pripravovať dáta, trénovať modely, publikovať prediktívne služby a monitorovať ich používanie. Najdôležitejšie je, že zvyšuje ich efektivitu automatizáciou mnohých časovo náročných úloh spojených s tréningom modelov; a umožňuje im využívať cloudové výpočtové zdroje, ktoré sa efektívne škálujú na spracovanie veľkých objemov dát, pričom náklady vznikajú iba pri ich skutočnom použití.

Azure ML poskytuje všetky nástroje, ktoré vývojári a dátoví vedci potrebujú pre svoje pracovné postupy strojového učenia. Patria sem:

- **Azure Machine Learning Studio**: webový portál v Azure Machine Learning pre možnosti tréningu modelov, nasadenia, automatizácie, sledovania a správy aktív s nízkym alebo žiadnym kódom. Studio sa integruje s Azure Machine Learning SDK pre bezproblémový zážitok.
- **Jupyter Notebooks**: rýchle prototypovanie a testovanie ML modelov.
- **Azure Machine Learning Designer**: umožňuje vytvárať experimenty pomocou drag-and-drop modulov a nasadzovať pipeline v prostredí s nízkym kódom.
- **Automatizované strojové učenie (AutoML)**: automatizuje iteratívne úlohy vývoja modelov strojového učenia, umožňuje vytvárať ML modely s vysokou škálou, efektivitou a produktivitou, pričom zachováva kvalitu modelu.
- **Označovanie dát**: asistovaný nástroj ML na automatické označovanie dát.
- **Rozšírenie strojového učenia pre Visual Studio Code**: poskytuje plnohodnotné vývojové prostredie na vytváranie a správu ML projektov.
- **CLI pre strojové učenie**: poskytuje príkazy na správu zdrojov Azure ML z príkazového riadku.
- **Integrácia s open-source frameworkmi** ako PyTorch, TensorFlow, Scikit-learn a mnoho ďalších na tréning, nasadenie a správu celého procesu strojového učenia.
- **MLflow**: open-source knižnica na správu životného cyklu vašich experimentov strojového učenia. **MLFlow Tracking** je komponent MLflow, ktorý zaznamenáva a sleduje metriky tréningových behov a artefakty modelov, bez ohľadu na prostredie vášho experimentu.

### 1.2 Projekt predikcie zlyhania srdca:

Niet pochýb o tom, že vytváranie projektov je najlepší spôsob, ako otestovať svoje schopnosti a znalosti. V tejto lekcii preskúmame dva rôzne spôsoby vytvárania projektu dátovej vedy na predikciu zlyhania srdca v Azure ML Studio, pomocou Low code/No code a pomocou Azure ML SDK, ako je znázornené na nasledujúcej schéme:

![project-schema](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/project-schema.PNG)

Každý spôsob má svoje výhody a nevýhody. Cesta Low code/No code je jednoduchšia na začiatok, pretože zahŕňa interakciu s GUI (grafické užívateľské rozhranie) bez potreby predchádzajúcich znalostí kódu. Táto metóda umožňuje rýchle testovanie životaschopnosti projektu a vytvorenie POC (Proof Of Concept). Avšak, keď projekt rastie a veci musia byť pripravené na produkciu, nie je možné vytvárať zdroje cez GUI. Je potrebné programovo automatizovať všetko, od vytvárania zdrojov až po nasadenie modelu. Tu sa stáva dôležitým ovládanie Azure ML SDK.

|                   | Low code/No code | Azure ML SDK              |
|-------------------|------------------|---------------------------|
| Znalosť kódu      | Nie je potrebná  | Potrebná                  |
| Čas na vývoj      | Rýchly a jednoduchý | Závisí od znalostí kódu   |
| Pripravenosť na produkciu | Nie               | Áno                       |

### 1.3 Dataset zlyhania srdca: 

Kardiovaskulárne ochorenia (CVDs) sú hlavnou príčinou úmrtí na celom svete, predstavujú 31% všetkých úmrtí. Environmentálne a behaviorálne rizikové faktory, ako je používanie tabaku, nezdravá strava a obezita, fyzická nečinnosť a škodlivé používanie alkoholu, by mohli byť použité ako vlastnosti pre odhadové modely. Schopnosť odhadnúť pravdepodobnosť vývoja CVD by mohla byť veľmi užitočná na prevenciu útokov u ľudí s vysokým rizikom.

Kaggle sprístupnil [dataset zlyhania srdca](https://www.kaggle.com/andrewmvd/heart-failure-clinical-data), ktorý použijeme v tomto projekte. Dataset si môžete stiahnuť teraz. Ide o tabuľkový dataset s 13 stĺpcami (12 vlastností a 1 cieľová premenná) a 299 riadkami. 

|    | Názov premennej           | Typ             | Popis                                                    | Príklad           |
|----|---------------------------|-----------------|----------------------------------------------------------|-------------------|
| 1  | age                       | numerický       | vek pacienta                                             | 25                |
| 2  | anaemia                   | boolean         | Zníženie červených krviniek alebo hemoglobínu            | 0 alebo 1         |
| 3  | creatinine_phosphokinase  | numerický       | Hladina enzýmu CPK v krvi                                | 542               |
| 4  | diabetes                  | boolean         | Či má pacient cukrovku                                   | 0 alebo 1         |
| 5  | ejection_fraction         | numerický       | Percento krvi opúšťajúcej srdce pri každej kontrakcii    | 45                |
| 6  | high_blood_pressure       | boolean         | Či má pacient hypertenziu                                | 0 alebo 1         |
| 7  | platelets                 | numerický       | Počet krvných doštičiek v krvi                           | 149000            |
| 8  | serum_creatinine          | numerický       | Hladina sérového kreatinínu v krvi                       | 0.5               |
| 9  | serum_sodium              | numerický       | Hladina sérového sodíka v krvi                           | jun               |
| 10 | sex                       | boolean         | žena alebo muž                                           | 0 alebo 1         |
| 11 | smoking                   | boolean         | Či pacient fajčí                                         | 0 alebo 1         |
| 12 | time                      | numerický       | obdobie sledovania (dni)                                 | 4                 |
|----|---------------------------|-----------------|----------------------------------------------------------|-------------------|
| 21 | DEATH_EVENT [Cieľ]        | boolean         | Či pacient zomrie počas obdobia sledovania               | 0 alebo 1         |

Keď máte dataset, môžeme začať projekt v Azure.

## 2. Tréning modelu v Azure ML Studio pomocou Low code/No code
### 2.1 Vytvorenie pracovného priestoru Azure ML
Na tréning modelu v Azure ML musíte najskôr vytvoriť pracovný priestor Azure ML. Pracovný priestor je najvyšší zdroj pre Azure Machine Learning, ktorý poskytuje centralizované miesto na prácu so všetkými artefaktmi, ktoré vytvoríte pri používaní Azure Machine Learning. Pracovný priestor uchováva históriu všetkých tréningových behov, vrátane logov, metrík, výstupov a snímok vašich skriptov. Tieto informácie používate na určenie, ktorý tréningový beh produkuje najlepší model. [Viac informácií](https://docs.microsoft.com/azure/machine-learning/concept-workspace?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)

Odporúča sa používať najaktuálnejší prehliadač kompatibilný s vaším operačným systémom. Podporované sú nasledujúce prehliadače:

- Microsoft Edge (nový Microsoft Edge, najnovšia verzia. Nie Microsoft Edge legacy)
- Safari (najnovšia verzia, iba Mac)
- Chrome (najnovšia verzia)
- Firefox (najnovšia verzia)

Na používanie Azure Machine Learning vytvorte pracovný priestor vo vašom Azure predplatnom. Tento pracovný priestor môžete potom použiť na správu dát, výpočtových zdrojov, kódu, modelov a ďalších artefaktov súvisiacich s vašimi pracovnými záťažami strojového učenia.

> **_POZNÁMKA:_** Vaše Azure predplatné bude účtované malou sumou za ukladanie dát, pokiaľ pracovný priestor Azure Machine Learning existuje vo vašom predplatnom, preto odporúčame odstrániť pracovný priestor Azure Machine Learning, keď ho už nebudete používať.

1. Prihláste sa do [Azure portálu](https://ms.portal.azure.com/) pomocou Microsoft prihlasovacích údajov spojených s vaším Azure predplatným.
2. Vyberte **＋Vytvoriť zdroj**
   
   ![workspace-1](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-1.PNG)

   Vyhľadajte Machine Learning a vyberte dlaždicu Machine Learning

   ![workspace-2](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-2.PNG)

   Kliknite na tlačidlo vytvoriť

   ![workspace-3](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-3.PNG)

   Vyplňte nastavenia nasledovne:
   - Predplatné: Vaše Azure predplatné
   - Skupina zdrojov: Vytvorte alebo vyberte skupinu zdrojov
   - Názov pracovného priestoru: Zadajte jedinečný názov pre váš pracovný priestor
   - Región: Vyberte geografický región najbližší k vám
   - Účet úložiska: Poznámka k predvolenému novému účtu úložiska, ktorý bude vytvorený pre váš pracovný priestor
   - Key vault: Poznámka k predvolenému novému key vaultu, ktorý bude vytvorený pre váš pracovný priestor
   - Application insights: Poznámka k predvolenému novému zdroju application insights, ktorý bude vytvorený pre váš pracovný priestor
   - Container registry: Žiadny (bude automaticky vytvorený pri prvom nasadení modelu do kontajnera)

    ![workspace-4](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-4.PNG)

   - Kliknite na tlačidlo vytvoriť + recenzia a potom na tlačidlo vytvoriť
3. Počkajte, kým sa váš pracovný priestor vytvorí (môže to trvať niekoľko minút). Potom prejdite naň v portáli. Nájdete ho cez službu Machine Learning Azure.
4. Na stránke Prehľad vášho pracovného priestoru spustite Azure Machine Learning studio (alebo otvorte nový prehliadač a prejdite na https://ml.azure.com), a prihláste sa do Azure Machine Learning studio pomocou vášho Microsoft účtu. Ak budete vyzvaní, vyberte váš Azure adresár a predplatné, a váš pracovný priestor Azure Machine Learning.
   
![workspace-5](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-5.PNG)

5. V Azure Machine Learning studio, prepnite ikonu ☰ v ľavom hornom rohu na zobrazenie rôznych stránok v rozhraní. Tieto stránky môžete použiť na správu zdrojov vo vašom pracovnom priestore.

![workspace-6](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-6.PNG)

Pracovný priestor môžete spravovať pomocou Azure portálu, ale pre dátových vedcov a inžinierov operácií strojového učenia poskytuje Azure Machine Learning Studio viac zamerané užívateľské rozhranie na správu zdrojov pracovného priestoru.

### 2.2 Výpočtové zdroje

Výpočtové zdroje sú cloudové zdroje, na ktorých môžete spúšťať procesy tréningu modelov a skúmania dát. Existujú štyri typy výpočtových zdrojov, ktoré môžete vytvoriť:

- **Výpočtové inštancie**: Vývojové pracovné stanice, ktoré môžu dátoví vedci používať na prácu s dátami a modelmi. To zahŕňa vytvorenie virtuálneho stroja (VM) a spustenie notebookovej inštancie. Potom môžete trénovať model volaním výpočtového klastru z notebooku.
- **Výpočtové klastry**: Škálovateľné klastry VM na požiadanie na spracovanie experimentálneho kódu. Budete ich potrebovať pri tréningu modelu. Výpočtové klastry môžu tiež využívať špecializované GPU alebo CPU zdroje.
- **Inferenčné klastry**: Ciele nasadenia pre prediktívne služby, ktoré používajú vaše trénované modely.
- **Pripojený výpočet**: Odkazuje na existujúce výpočtové zdroje Azure, ako sú virtuálne počítače alebo klastre Azure Databricks.

#### 2.2.1 Výber správnych možností pre vaše výpočtové zdroje

Pri vytváraní výpočtového zdroja je potrebné zvážiť niekoľko kľúčových faktorov, ktoré môžu byť rozhodujúce.

**Potrebujete CPU alebo GPU?**

CPU (Central Processing Unit) je elektronický obvod, ktorý vykonáva inštrukcie tvoriace počítačový program. GPU (Graphics Processing Unit) je špecializovaný elektronický obvod, ktorý dokáže vykonávať graficky orientovaný kód veľmi vysokou rýchlosťou.

Hlavný rozdiel medzi architektúrou CPU a GPU je v tom, že CPU je navrhnuté na rýchle spracovanie širokého spektra úloh (merané rýchlosťou hodín CPU), ale má obmedzenú paralelitu úloh, ktoré môžu bežať. GPU sú navrhnuté na paralelné výpočty, a preto sú oveľa lepšie na úlohy hlbokého učenia.

| CPU                                     | GPU                         |
|-----------------------------------------|-----------------------------|
| Menej nákladné                          | Viac nákladné               |
| Nižšia úroveň paralelnosti              | Vyššia úroveň paralelnosti  |
| Pomalšie pri trénovaní modelov hlbokého učenia | Optimálne pre hlboké učenie |

**Veľkosť klastru**

Väčšie klastre sú drahšie, ale poskytujú lepšiu odozvu. Ak máte čas, ale obmedzený rozpočet, mali by ste začať s malým klastrom. Naopak, ak máte peniaze, ale málo času, mali by ste začať s väčším klastrom.

**Veľkosť virtuálneho počítača (VM)**

V závislosti od vašich časových a rozpočtových obmedzení môžete meniť veľkosť RAM, disku, počet jadier a rýchlosť hodín. Zvýšenie všetkých týchto parametrov bude drahšie, ale zlepší výkon.

**Dedikované alebo nízko-prioritné inštancie?**

Nízko-prioritná inštancia znamená, že je prerušená: Microsoft Azure môže tieto zdroje použiť na inú úlohu, čím preruší vašu úlohu. Dedikovaná inštancia, alebo neprerušiteľná, znamená, že úloha nebude nikdy ukončená bez vášho povolenia. Toto je ďalší aspekt rozhodovania medzi časom a peniazmi, pretože prerušiteľné inštancie sú lacnejšie ako dedikované.

#### 2.2.2 Vytvorenie výpočtového klastru

V [Azure ML workspace](https://ml.azure.com/), ktorý sme vytvorili skôr, prejdite na sekciu Compute, kde uvidíte rôzne výpočtové zdroje, o ktorých sme práve diskutovali (t.j. výpočtové inštancie, výpočtové klastre, inferenčné klastre a pripojené výpočty). Pre tento projekt budeme potrebovať výpočtový klaster na trénovanie modelu. V Studio kliknite na menu "Compute", potom na záložku "Compute cluster" a kliknite na tlačidlo "+ New" na vytvorenie výpočtového klastru.

![22](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/cluster-1.PNG)

1. Vyberte svoje možnosti: Dedikované vs nízko-prioritné, CPU alebo GPU, veľkosť VM a počet jadier (pre tento projekt môžete ponechať predvolené nastavenia).
2. Kliknite na tlačidlo Next.

![23](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/cluster-2.PNG)

3. Dajte klastru názov.
4. Vyberte svoje možnosti: Minimálny/maximálny počet uzlov, nečinné sekundy pred zmenšením, SSH prístup. Upozorňujeme, že ak je minimálny počet uzlov 0, ušetríte peniaze, keď je klaster nečinný. Upozorňujeme, že čím vyšší je maximálny počet uzlov, tým kratšie bude trénovanie. Odporúčaný maximálny počet uzlov je 3.  
5. Kliknite na tlačidlo "Create". Tento krok môže trvať niekoľko minút.

![29](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/cluster-3.PNG)

Skvelé! Teraz, keď máme výpočtový klaster, musíme nahrať dáta do Azure ML Studio.

### 2.3 Nahrávanie datasetu

1. V [Azure ML workspace](https://ml.azure.com/), ktorý sme vytvorili skôr, kliknite na "Datasets" v ľavom menu a kliknite na tlačidlo "+ Create dataset" na vytvorenie datasetu. Vyberte možnosť "From local files" a vyberte Kaggle dataset, ktorý sme stiahli skôr.
   
   ![24](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/dataset-1.PNG)

2. Dajte datasetu názov, typ a popis. Kliknite na Next. Nahrajte dáta zo súborov. Kliknite na Next.
   
   ![25](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/dataset-2.PNG)

3. V schéme zmeňte typ dát na Boolean pre nasledujúce vlastnosti: anaemia, diabetes, high blood pressure, sex, smoking a DEATH_EVENT. Kliknite na Next a potom na Create.
   
   ![26](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/dataset-3.PNG)

Výborne! Teraz, keď je dataset pripravený a výpočtový klaster vytvorený, môžeme začať trénovanie modelu!

### 2.4 Trénovanie s AutoML bez kódu alebo s minimálnym kódom

Tradičný vývoj modelov strojového učenia je náročný na zdroje, vyžaduje značné odborné znalosti a čas na vytvorenie a porovnanie desiatok modelov. Automatizované strojové učenie (AutoML) je proces automatizácie časovo náročných, iteratívnych úloh vývoja modelov strojového učenia. Umožňuje dátovým vedcom, analytikom a vývojárom vytvárať ML modely vo veľkom rozsahu, efektívne a produktívne, pričom zachováva kvalitu modelov. Skracuje čas potrebný na získanie modelov pripravených na produkciu s veľkou ľahkosťou a efektivitou. [Viac informácií](https://docs.microsoft.com/azure/machine-learning/concept-automated-ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)

1. V [Azure ML workspace](https://ml.azure.com/), ktorý sme vytvorili skôr, kliknite na "Automated ML" v ľavom menu a vyberte dataset, ktorý ste práve nahrali. Kliknite na Next.

   ![27](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/aml-1.PNG)

2. Zadajte nový názov experimentu, cieľový stĺpec (DEATH_EVENT) a výpočtový klaster, ktorý sme vytvorili. Kliknite na Next.
   
   ![28](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/aml-2.PNG)

3. Vyberte "Classification" a kliknite na Finish. Tento krok môže trvať medzi 30 minútami až 1 hodinou, v závislosti od veľkosti vášho výpočtového klastru.
    
    ![30](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/aml-3.PNG)

4. Po dokončení behu kliknite na záložku "Automated ML", kliknite na váš beh a kliknite na algoritmus v karte "Best model summary".
    
    ![31](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/aml-4.PNG)

Tu môžete vidieť podrobný popis najlepšieho modelu, ktorý AutoML vygeneroval. Môžete tiež preskúmať ďalšie modely v záložke Models. Strávte niekoľko minút skúmaním modelov v sekcii Explanations (preview button). Keď si vyberiete model, ktorý chcete použiť (tu vyberieme najlepší model vybraný AutoML), uvidíme, ako ho môžeme nasadiť.

## 3. Nasadenie modelu bez kódu alebo s minimálnym kódom a spotreba endpointu
### 3.1 Nasadenie modelu

Rozhranie automatizovaného strojového učenia umožňuje nasadiť najlepší model ako webovú službu v niekoľkých krokoch. Nasadenie je integrácia modelu tak, aby mohol robiť predikcie na základe nových dát a identifikovať potenciálne oblasti príležitostí. Pre tento projekt nasadenie do webovej služby znamená, že medicínske aplikácie budú môcť využívať model na živé predikcie rizika infarktu u pacientov.

V popise najlepšieho modelu kliknite na tlačidlo "Deploy".
    
![deploy-1](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/deploy-1.PNG)

15. Dajte mu názov, popis, typ výpočtu (Azure Container Instance), povolte autentifikáciu a kliknite na Deploy. Tento krok môže trvať približne 20 minút. Proces nasadenia zahŕňa niekoľko krokov vrátane registrácie modelu, generovania zdrojov a ich konfigurácie pre webovú službu. Stavová správa sa zobrazí pod stavom nasadenia. Pravidelne kliknite na Refresh, aby ste skontrolovali stav nasadenia. Je nasadený a beží, keď je stav "Healthy".

![deploy-2](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/deploy-2.PNG)

16. Po nasadení kliknite na záložku Endpoint a kliknite na endpoint, ktorý ste práve nasadili. Tu nájdete všetky detaily, ktoré potrebujete vedieť o endpointe. 

![deploy-3](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/deploy-3.PNG)

Úžasné! Teraz, keď máme model nasadený, môžeme začať spotrebu endpointu.

### 3.2 Spotreba endpointu

Kliknite na záložku "Consume". Tu nájdete REST endpoint a python skript v možnosti spotreby. Strávte chvíľu čítaním python kódu.

Tento skript môže byť spustený priamo z vášho lokálneho počítača a bude spotrebovávať váš endpoint.

![35](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/consumption-1.PNG)

Pozrite sa na tieto 2 riadky kódu:

```python
url = 'http://98e3715f-xxxx-xxxx-xxxx-9ec22d57b796.centralus.azurecontainer.io/score'
api_key = '' # Replace this with the API key for the web service
```
Premenná `url` je REST endpoint nájdený v záložke consume a premenná `api_key` je primárny kľúč tiež nájdený v záložke consume (iba v prípade, že ste povolili autentifikáciu). Takto skript môže spotrebovávať endpoint.

18. Po spustení skriptu by ste mali vidieť nasledujúci výstup:
    ```python
    b'"{\\"result\\": [true]}"'
    ```
To znamená, že predikcia zlyhania srdca pre dané dáta je pravdivá. To dáva zmysel, pretože ak sa pozriete bližšie na dáta automaticky generované v skripte, všetko je nastavené na 0 a false ako predvolené. Môžete zmeniť dáta na nasledujúci vstupný vzor:

```python
data = {
    "data":
    [
        {
            'age': "0",
            'anaemia': "false",
            'creatinine_phosphokinase': "0",
            'diabetes': "false",
            'ejection_fraction': "0",
            'high_blood_pressure': "false",
            'platelets': "0",
            'serum_creatinine': "0",
            'serum_sodium': "0",
            'sex': "false",
            'smoking': "false",
            'time': "0",
        },
        {
            'age': "60",
            'anaemia': "false",
            'creatinine_phosphokinase': "500",
            'diabetes': "false",
            'ejection_fraction': "38",
            'high_blood_pressure': "false",
            'platelets': "260000",
            'serum_creatinine': "1.40",
            'serum_sodium': "137",
            'sex': "false",
            'smoking': "false",
            'time': "130",
        },
    ],
}
```
Skript by mal vrátiť:
    ```python
    b'"{\\"result\\": [true, false]}"'
    ```

Gratulujeme! Práve ste spotrebovali model nasadený a trénovaný na Azure ML!

> **_POZNÁMKA:_** Po dokončení projektu nezabudnite vymazať všetky zdroje.
## 🚀 Výzva

Pozrite sa bližšie na vysvetlenia modelu a detaily, ktoré AutoML vygeneroval pre najlepšie modely. Pokúste sa pochopiť, prečo je najlepší model lepší ako ostatné. Aké algoritmy boli porovnávané? Aké sú rozdiely medzi nimi? Prečo je najlepší model v tomto prípade výkonnejší?

## [Kvíz po prednáške](https://ff-quizzes.netlify.app/en/ds/quiz/35)

## Prehľad a samostatné štúdium

V tejto lekcii ste sa naučili, ako trénovať, nasadiť a spotrebovať model na predikciu rizika zlyhania srdca bez kódu alebo s minimálnym kódom v cloude. Ak ste to ešte neurobili, ponorte sa hlbšie do vysvetlení modelu, ktoré AutoML vygeneroval pre najlepšie modely, a pokúste sa pochopiť, prečo je najlepší model lepší ako ostatné.

Môžete ísť ďalej do AutoML bez kódu alebo s minimálnym kódom čítaním tejto [dokumentácie](https://docs.microsoft.com/azure/machine-learning/tutorial-first-experiment-automated-ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).

## Zadanie

[Projekt Data Science bez kódu alebo s minimálnym kódom na Azure ML](assignment.md)

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.