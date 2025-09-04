<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "39f3b3a9d873eaa522c2e792ce0ca503",
  "translation_date": "2025-09-04T22:21:16+00:00",
  "source_file": "5-Data-Science-In-Cloud/18-Low-Code/README.md",
  "language_code": "lt"
}
-->
# Duomenų mokslas debesyje: „Mažai kodo / Be kodo“ būdas

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/18-DataScience-Cloud.png)|
|:---:|
| Duomenų mokslas debesyje: Mažai kodo - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Turinys:

- [Duomenų mokslas debesyje: „Mažai kodo / Be kodo“ būdas](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Prieš paskaitą: testas](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [1. Įvadas](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [1.1 Kas yra Azure Machine Learning?](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [1.2 Širdies nepakankamumo prognozavimo projektas:](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [1.3 Širdies nepakankamumo duomenų rinkinys:](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [2. Mažai kodo / Be kodo modelio mokymas Azure ML Studio](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.1 Sukurkite Azure ML darbo sritį](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.2 Skaičiavimo ištekliai](../../../../5-Data-Science-In-Cloud/18-Low-Code)
      - [2.2.1 Tinkamų skaičiavimo išteklių pasirinkimas](../../../../5-Data-Science-In-Cloud/18-Low-Code)
      - [2.2.2 Skaičiavimo klasterio kūrimas](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.3 Duomenų rinkinio įkėlimas](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.4 Mažai kodo / Be kodo mokymas naudojant AutoML](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [3. Mažai kodo / Be kodo modelio diegimas ir galutinio taško naudojimas](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [3.1 Modelio diegimas](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [3.2 Galutinio taško naudojimas](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [🚀 Iššūkis](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Testas po paskaitos](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Apžvalga ir savarankiškas mokymasis](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Užduotis](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  
## [Prieš paskaitą: testas](https://ff-quizzes.netlify.app/en/ds/)

## 1. Įvadas
### 1.1 Kas yra Azure Machine Learning?

Azure debesų platforma apima daugiau nei 200 produktų ir debesų paslaugų, skirtų padėti jums kurti naujus sprendimus. Duomenų mokslininkai skiria daug pastangų duomenų tyrimui, išankstiniam apdorojimui ir įvairių modelio mokymo algoritmų bandymui, siekdami sukurti tikslius modelius. Šios užduotys užima daug laiko ir dažnai neefektyviai naudoja brangius skaičiavimo išteklius.

[Azure ML](https://docs.microsoft.com/azure/machine-learning/overview-what-is-azure-machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) yra debesų platforma, skirta kurti ir valdyti mašininio mokymosi sprendimus Azure aplinkoje. Ji apima daugybę funkcijų ir galimybių, kurios padeda duomenų mokslininkams paruošti duomenis, mokyti modelius, publikuoti prognozavimo paslaugas ir stebėti jų naudojimą. Svarbiausia, ji padeda padidinti efektyvumą automatizuojant daugelį laiko reikalaujančių užduočių, susijusių su modelių mokymu, ir leidžia naudoti debesų skaičiavimo išteklius, kurie efektyviai skalėja, kad apdorotų didelius duomenų kiekius, mokant tik už faktinį naudojimą.

Azure ML suteikia visus įrankius, kurių reikia kūrėjams ir duomenų mokslininkams jų mašininio mokymosi darbo eigoms. Tai apima:

- **Azure Machine Learning Studio**: tai yra internetinis portalas Azure Machine Learning, skirtas mažai kodo ir be kodo galimybėms modelių mokymui, diegimui, automatizavimui, stebėjimui ir turto valdymui. Studija integruojasi su Azure Machine Learning SDK, kad užtikrintų sklandžią patirtį.
- **Jupyter Notebooks**: greitai kurkite prototipus ir testuokite ML modelius.
- **Azure Machine Learning Designer**: leidžia vilkti ir mesti modulius, kad sukurtumėte eksperimentus ir diegtumėte procesus mažai kodo aplinkoje.
- **Automatizuotas mašininio mokymosi UI (AutoML)**: automatizuoja iteracines mašininio mokymosi modelio kūrimo užduotis, leidžiant kurti ML modelius su dideliu mastu, efektyvumu ir produktyvumu, išlaikant modelio kokybę.
- **Duomenų žymėjimas**: padedantis ML įrankis, skirtas automatiškai žymėti duomenis.
- **Mašininio mokymosi plėtinys Visual Studio Code**: suteikia pilnai funkcionalią kūrimo aplinką ML projektų kūrimui ir valdymui.
- **Mašininio mokymosi CLI**: suteikia komandas Azure ML išteklių valdymui iš komandinės eilutės.
- **Integracija su atvirojo kodo sistemomis**, tokiomis kaip PyTorch, TensorFlow, Scikit-learn ir daug kitų, skirtų mokymui, diegimui ir viso mašininio mokymosi proceso valdymui.
- **MLflow**: tai atvirojo kodo biblioteka, skirta valdyti jūsų mašininio mokymosi eksperimentų gyvavimo ciklą. **MLFlow Tracking** yra MLflow komponentas, kuris registruoja ir seka jūsų mokymo rezultatų metrikas ir modelio artefaktus, nepriklausomai nuo jūsų eksperimento aplinkos.

### 1.2 Širdies nepakankamumo prognozavimo projektas:

Nėra abejonių, kad projektų kūrimas ir įgyvendinimas yra geriausias būdas patikrinti savo įgūdžius ir žinias. Šioje pamokoje mes nagrinėsime du skirtingus būdus, kaip sukurti duomenų mokslų projektą, skirtą širdies nepakankamumo atakų prognozavimui Azure ML Studio, naudojant mažai kodo / be kodo ir Azure ML SDK, kaip parodyta šiame schematyje:

![project-schema](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/project-schema.PNG)

Kiekvienas būdas turi savo privalumų ir trūkumų. Mažai kodo / be kodo būdas yra lengvesnis pradėti, nes jis apima sąveiką su GUI (grafinė vartotojo sąsaja), nereikalaujant išankstinių kodavimo žinių. Šis metodas leidžia greitai išbandyti projekto gyvybingumą ir sukurti POC (Proof Of Concept). Tačiau, kai projektas auga ir reikia pasiruošti gamybai, neįmanoma kurti išteklių per GUI. Reikia programiškai automatizuoti viską – nuo išteklių kūrimo iki modelio diegimo. Čia tampa svarbu žinoti, kaip naudoti Azure ML SDK.

|                   | Mažai kodo / Be kodo | Azure ML SDK              |
|-------------------|----------------------|---------------------------|
| Kodavimo žinios   | Nereikalingos        | Reikalingos               |
| Kūrimo laikas     | Greitas ir lengvas   | Priklauso nuo kodavimo įgūdžių |
| Gamybos pasiruošimas | Ne                 | Taip                      |

### 1.3 Širdies nepakankamumo duomenų rinkinys: 

Širdies ir kraujagyslių ligos (CVDs) yra pagrindinė mirties priežastis pasaulyje, sudaranti 31% visų mirčių. Aplinkos ir elgesio rizikos veiksniai, tokie kaip tabako vartojimas, nesveika mityba ir nutukimas, fizinis neveiklumas ir žalingas alkoholio vartojimas, gali būti naudojami kaip modelių funkcijos. Gebėjimas įvertinti CVD išsivystymo tikimybę galėtų būti labai naudingas, siekiant užkirsti kelią atakoms žmonėms, kuriems yra didelė rizika.

Kaggle pateikė viešai prieinamą [Širdies nepakankamumo duomenų rinkinį](https://www.kaggle.com/andrewmvd/heart-failure-clinical-data), kurį naudosime šiame projekte. Galite atsisiųsti duomenų rinkinį dabar. Tai yra lentelinis duomenų rinkinys su 13 stulpelių (12 funkcijų ir 1 tikslinė kintamoji) ir 299 eilutėmis. 

|    | Kintamojo pavadinimas     | Tipas            | Aprašymas                                               | Pavyzdys          |
|----|---------------------------|------------------|---------------------------------------------------------|-------------------|
| 1  | amžius                    | skaitinis        | paciento amžius                                        | 25                |
| 2  | anemija                   | loginis          | Raudonųjų kraujo kūnelių ar hemoglobino sumažėjimas     | 0 arba 1          |
| 3  | kreatinino fosfokinazė    | skaitinis        | CPK fermento lygis kraujyje                            | 542               |
| 4  | diabetas                  | loginis          | Ar pacientas serga diabetu                             | 0 arba 1          |
| 5  | išstūmimo frakcija        | skaitinis        | Kraujo procentas, paliekantis širdį kiekvieno susitraukimo metu | 45                |
| 6  | aukštas kraujo spaudimas  | loginis          | Ar pacientas turi hipertenziją                         | 0 arba 1          |
| 7  | trombocitai               | skaitinis        | Trombocitų kiekis kraujyje                             | 149000            |
| 8  | serumo kreatininas        | skaitinis        | Serumo kreatinino lygis kraujyje                       | 0.5               |
| 9  | serumo natris             | skaitinis        | Serumo natrio lygis kraujyje                           | jun               |
| 10 | lytis                     | loginis          | moteris ar vyras                                       | 0 arba 1          |
| 11 | rūkymas                   | loginis          | Ar pacientas rūko                                      | 0 arba 1          |
| 12 | laikas                    | skaitinis        | stebėjimo laikotarpis (dienos)                         | 4                 |
|----|---------------------------|------------------|---------------------------------------------------------|-------------------|
| 21 | DEATH_EVENT [Tikslas]     | loginis          | Ar pacientas miršta stebėjimo laikotarpiu              | 0 arba 1          |

Kai turėsite duomenų rinkinį, galime pradėti projektą Azure aplinkoje.

## 2. Mažai kodo / Be kodo modelio mokymas Azure ML Studio
### 2.1 Sukurkite Azure ML darbo sritį
Norėdami mokyti modelį Azure ML, pirmiausia turite sukurti Azure ML darbo sritį. Darbo sritis yra aukščiausio lygio išteklius Azure Machine Learning, suteikiantis centralizuotą vietą dirbti su visais artefaktais, kuriuos sukuriate naudodami Azure Machine Learning. Darbo sritis saugo visų mokymo procesų istoriją, įskaitant žurnalus, metrikas, rezultatus ir jūsų scenarijų momentinę kopiją. Šią informaciją naudojate norėdami nustatyti, kuris mokymo procesas sukuria geriausią modelį. [Sužinokite daugiau](https://docs.microsoft.com/azure/machine-learning/concept-workspace?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)

Rekomenduojama naudoti naujausią naršyklę, suderinamą su jūsų operacine sistema. Palaikomos šios naršyklės:

- Microsoft Edge (Naujausia Microsoft Edge versija, ne Microsoft Edge legacy)
- Safari (naujausia versija, tik Mac)
- Chrome (naujausia versija)
- Firefox (naujausia versija)

Norėdami naudoti Azure Machine Learning, sukurkite darbo sritį savo Azure prenumeratoje. Tada galite naudoti šią darbo sritį duomenų, skaičiavimo išteklių, kodo, modelių ir kitų artefaktų, susijusių su jūsų mašininio mokymosi darbo krūviais, valdymui.

> **_PASTABA:_** Jūsų Azure prenumerata bus apmokestinta nedidele suma už duomenų saugojimą, kol Azure Machine Learning darbo sritis egzistuoja jūsų prenumeratoje, todėl rekomenduojame ištrinti Azure Machine Learning darbo sritį, kai jos nebenaudojate.

1. Prisijunkite prie [Azure portalo](https://ms.portal.azure.com/) naudodami Microsoft kredencialus, susijusius su jūsų Azure prenumerata.
2. Pasirinkite **＋Sukurti išteklių**
   
   ![workspace-1](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-1.PNG)

   Ieškokite „Machine Learning“ ir pasirinkite „Machine Learning“ plytelę

   ![workspace-2](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-2.PNG)

   Spustelėkite mygtuką „Sukurti“

   ![workspace-3](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-3.PNG)

   Užpildykite nustatymus taip:
   - Prenumerata: Jūsų Azure prenumerata
   - Išteklių grupė: Sukurkite arba pasirinkite išteklių grupę
   - Darbo srities pavadinimas: Įveskite unikalų darbo srities pavadinimą
   - Regionas: Pasirinkite geografinį regioną, artimiausią jums
   - Saugojimo paskyra: Atkreipkite dėmesį į numatytąją naują saugojimo paskyrą, kuri bus sukurta jūsų darbo sričiai
   - Raktų saugykla: Atkreipkite dėmesį į numatytąją naują raktų saugyklą, kuri bus sukurta jūsų darbo sričiai
   - Programos įžvalgos: Atkreipkite dėmesį į numatytąją naują programos įžvalgų išteklių, kuris bus sukurtas jūsų darbo sričiai
   - Konteinerių registras: Nėra (vienas bus automatiškai sukurtas pirmą kartą diegiant modelį į konteinerį)

    ![workspace-4](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-4.PNG)

   - Spustelėkite „Sukurti + peržiūrėti“, tada „Sukurti“
3. Palaukite, kol jūsų darbo sritis bus sukurta (tai gali užtrukti kelias minutes). Tada eikite į ją portale. Ją galite rasti per „Machine Learning“ Azure paslaugą.
4. Darbo srities apžvalgos puslapyje paleiskite Azure Machine Learning studiją (arba atidarykite naują naršyklės skirtuką ir eikite į https://ml.azure.com), ir prisijunkite prie Azure Machine Learning studijos naudodami savo Microsoft paskyrą. Jei paprašyta, pasirinkite savo Azure katalogą ir prenumeratą bei savo Azure Machine Learning darbo sritį.
   
![workspace-5](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-5.PNG)

5. Azure Machine Learning studijoje perjunkite ☰ piktogramą viršuje kairėje, kad peržiūrėtumėte įvairius puslapius sąsajoje. Šiuos puslapius galite naudoti savo darbo srities išteklių valdymui.

![workspace-6](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-6.PNG)

Darbo sritį galite valdyti naudodami Azure portalą, tačiau duomenų mokslininkams ir mašininio mokymosi operacijų inžinieriams Azure Machine Learning studija suteikia labiau orientuotą vartotojo sąsają darbo srities išteklių valdymui.

### 2.2 Skaičiavimo ištekliai

Skaičiavimo ištekliai yra debesų pagrindu ve
- **Prijungtas skaičiavimas**: Nuorodos į esamus Azure skaičiavimo išteklius, tokius kaip virtualios mašinos ar Azure Databricks klasteriai.

#### 2.2.1 Tinkamų skaičiavimo išteklių pasirinkimas

Kai kuriant skaičiavimo išteklius, svarbu atsižvelgti į keletą pagrindinių veiksnių, nes šie pasirinkimai gali būti kritiniai sprendimai.

**Ar jums reikia CPU ar GPU?**

CPU (Centrinis procesorius) yra elektroninė grandinė, vykdanti kompiuterio programos instrukcijas. GPU (Grafikos procesorius) yra specializuota elektroninė grandinė, galinti vykdyti su grafika susijusį kodą labai dideliu greičiu.

Pagrindinis skirtumas tarp CPU ir GPU architektūros yra tas, kad CPU yra sukurtas greitai atlikti įvairias užduotis (matuojama CPU laikrodžio greičiu), tačiau yra ribotas užduočių, kurios gali būti vykdomos vienu metu, skaičiumi. GPU yra sukurtas lygiagrečiam skaičiavimui, todėl jis daug geriau tinka giluminio mokymosi užduotims.

| CPU                                     | GPU                         |
|-----------------------------------------|-----------------------------|
| Mažiau brangus                          | Brangesnis                  |
| Mažesnis lygiagretumo lygis             | Didesnis lygiagretumo lygis |
| Lėtesnis mokant giluminio mokymosi modelius | Optimalus giluminiam mokymuisi |

**Klasterio dydis**

Didesni klasteriai yra brangesni, tačiau jie užtikrina geresnį atsaką. Todėl, jei turite laiko, bet ribotą biudžetą, turėtumėte pradėti nuo mažo klasterio. Priešingai, jei turite pinigų, bet mažai laiko, turėtumėte pradėti nuo didesnio klasterio.

**VM dydis**

Priklausomai nuo jūsų laiko ir biudžeto apribojimų, galite keisti RAM, disko, branduolių skaičių ir laikrodžio greitį. Visų šių parametrų didinimas bus brangesnis, tačiau užtikrins geresnį našumą.

**Dedikuoti ar mažo prioriteto egzemplioriai?**

Mažo prioriteto egzempliorius reiškia, kad jis yra pertraukiamas: iš esmės, Microsoft Azure gali paimti šiuos išteklius ir priskirti juos kitai užduočiai, taip nutraukdamas darbą. Dedikuotas egzempliorius, arba nepertraukiamas, reiškia, kad darbas niekada nebus nutrauktas be jūsų leidimo. Tai dar vienas laiko ir pinigų apsvarstymas, nes pertraukiami egzemplioriai yra pigesni nei dedikuoti.

#### 2.2.2 Skaičiavimo klasterio kūrimas

[Azure ML darbo aplinkoje](https://ml.azure.com/), kurią sukūrėme anksčiau, eikite į skaičiavimą ir pamatysite skirtingus skaičiavimo išteklius, kuriuos ką tik aptarėme (pvz., skaičiavimo egzempliorius, skaičiavimo klasterius, inferencijos klasterius ir prijungtą skaičiavimą). Šiam projektui mums reikės skaičiavimo klasterio modelio mokymui. Studijoje spustelėkite meniu „Compute“, tada skirtuką „Compute cluster“ ir spustelėkite mygtuką „+ New“, kad sukurtumėte skaičiavimo klasterį.

![22](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/cluster-1.PNG)

1. Pasirinkite savo parinktis: Dedikuotas vs Mažo prioriteto, CPU ar GPU, VM dydis ir branduolių skaičius (šiam projektui galite palikti numatytuosius nustatymus).
2. Spustelėkite mygtuką „Next“.

![23](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/cluster-2.PNG)

3. Suteikite klasteriui skaičiavimo pavadinimą.
4. Pasirinkite savo parinktis: Minimalus/Maksimalus mazgų skaičius, Neaktyvumo sekundės prieš sumažinimą, SSH prieiga. Atkreipkite dėmesį, kad jei minimalus mazgų skaičius yra 0, sutaupysite pinigų, kai klasteris bus neaktyvus. Atkreipkite dėmesį, kad kuo didesnis maksimalus mazgų skaičius, tuo trumpesnis mokymas. Rekomenduojamas maksimalus mazgų skaičius yra 3.  
5. Spustelėkite mygtuką „Create“. Šis žingsnis gali užtrukti kelias minutes.

![29](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/cluster-3.PNG)

Puiku! Dabar, kai turime skaičiavimo klasterį, turime įkelti duomenis į Azure ML Studio.

### 2.3 Duomenų rinkinio įkėlimas

1. [Azure ML darbo aplinkoje](https://ml.azure.com/), kurią sukūrėme anksčiau, spustelėkite „Datasets“ kairiajame meniu ir spustelėkite mygtuką „+ Create dataset“, kad sukurtumėte duomenų rinkinį. Pasirinkite parinktį „From local files“ ir pasirinkite anksčiau atsisiųstą Kaggle duomenų rinkinį.
   
   ![24](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/dataset-1.PNG)

2. Suteikite savo duomenų rinkiniui pavadinimą, tipą ir aprašymą. Spustelėkite „Next“. Įkelkite duomenis iš failų. Spustelėkite „Next“.
   
   ![25](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/dataset-2.PNG)

3. Schemoje pakeiskite duomenų tipą į Boolean šioms savybėms: anaemia, diabetes, high blood pressure, sex, smoking ir DEATH_EVENT. Spustelėkite „Next“ ir „Create“.
   
   ![26](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/dataset-3.PNG)

Puiku! Dabar, kai duomenų rinkinys yra vietoje ir skaičiavimo klasteris sukurtas, galime pradėti modelio mokymą!

### 2.4 Mokymas be kodo arba su minimaliu kodu naudojant AutoML

Tradicinis mašininio mokymosi modelių kūrimas reikalauja daug išteklių, reikšmingų žinių ir laiko, kad būtų galima sukurti ir palyginti daugybę modelių. Automatinis mašininis mokymasis (AutoML) yra procesas, automatizuojantis laiko reikalaujančias, pasikartojančias mašininio mokymosi modelių kūrimo užduotis. Jis leidžia duomenų mokslininkams, analitikams ir kūrėjams kurti ML modelius dideliu mastu, efektyvumu ir produktyvumu, išlaikant modelio kokybę. Tai sumažina laiką, reikalingą paruošti ML modelius gamybai, su dideliu paprastumu ir efektyvumu. [Sužinokite daugiau](https://docs.microsoft.com/azure/machine-learning/concept-automated-ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)

1. [Azure ML darbo aplinkoje](https://ml.azure.com/), kurią sukūrėme anksčiau, spustelėkite „Automated ML“ kairiajame meniu ir pasirinkite ką tik įkeltą duomenų rinkinį. Spustelėkite „Next“.

   ![27](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/aml-1.PNG)

2. Įveskite naują eksperimento pavadinimą, tikslinį stulpelį (DEATH_EVENT) ir sukurtą skaičiavimo klasterį. Spustelėkite „Next“.
   
   ![28](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/aml-2.PNG)

3. Pasirinkite „Classification“ ir spustelėkite „Finish“. Šis žingsnis gali užtrukti nuo 30 minučių iki 1 valandos, priklausomai nuo jūsų skaičiavimo klasterio dydžio.
    
    ![30](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/aml-3.PNG)

4. Kai vykdymas bus baigtas, spustelėkite „Automated ML“ skirtuką, spustelėkite savo vykdymą ir spustelėkite algoritmą kortelėje „Best model summary“.
    
    ![31](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/aml-4.PNG)

Čia galite matyti išsamų geriausio modelio, kurį sukūrė AutoML, aprašymą. Taip pat galite tyrinėti kitus modelius skirtuke „Models“. Skirkite kelias minutes modelių tyrinėjimui skirtuke „Explanations (preview)“. Kai pasirinksite modelį, kurį norite naudoti (čia pasirinkime geriausią modelį, kurį pasirinko AutoML), pamatysime, kaip jį galima diegti.

## 3. Modelio diegimas be kodo arba su minimaliu kodu ir galutinio taško naudojimas
### 3.1 Modelio diegimas

Automatinio mašininio mokymosi sąsaja leidžia geriausią modelį diegti kaip internetinę paslaugą keliais žingsniais. Diegimas yra modelio integravimas, kad jis galėtų atlikti prognozes pagal naujus duomenis ir identifikuoti galimas galimybių sritis. Šiame projekte diegimas kaip internetinė paslauga reiškia, kad medicinos programos galės naudoti modelį, kad galėtų atlikti tiesiogines pacientų širdies smūgio rizikos prognozes.

Geriausio modelio aprašyme spustelėkite mygtuką „Deploy“.
    
![deploy-1](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/deploy-1.PNG)

15. Suteikite pavadinimą, aprašymą, skaičiavimo tipą (Azure Container Instance), įgalinkite autentifikaciją ir spustelėkite „Deploy“. Šis žingsnis gali užtrukti apie 20 minučių. Diegimo procesas apima kelis žingsnius, įskaitant modelio registravimą, išteklių generavimą ir jų konfigūravimą internetinei paslaugai. Po diegimo statuso pasirodo pranešimas. Periodiškai spustelėkite „Refresh“, kad patikrintumėte diegimo statusą. Kai statusas yra „Healthy“, paslauga yra įdiegta ir veikia.

![deploy-2](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/deploy-2.PNG)

16. Kai paslauga bus įdiegta, spustelėkite skirtuką „Endpoint“ ir spustelėkite ką tik įdiegtą galutinį tašką. Čia rasite visą informaciją apie galutinį tašką.

![deploy-3](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/deploy-3.PNG)

Nuostabu! Dabar, kai turime įdiegtą modelį, galime pradėti galutinio taško naudojimą.

### 3.2 Galutinio taško naudojimas

Spustelėkite skirtuką „Consume“. Čia rasite REST galutinį tašką ir Python scenarijų naudojimo parinktyje. Skirkite laiko Python kodo peržiūrai.

Šį scenarijų galima paleisti tiesiai iš jūsų vietinio kompiuterio ir jis naudos jūsų galutinį tašką.

![35](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/consumption-1.PNG)

Skirkite laiko peržiūrėti šias 2 kodo eilutes:

```python
url = 'http://98e3715f-xxxx-xxxx-xxxx-9ec22d57b796.centralus.azurecontainer.io/score'
api_key = '' # Replace this with the API key for the web service
```
Kintamasis `url` yra REST galutinio taško adresas, rastas skirtuke „Consume“, o kintamasis `api_key` yra pirminis raktas, taip pat rastas skirtuke „Consume“ (tik tuo atveju, jei įgalinote autentifikaciją). Štai kaip scenarijus naudoja galutinį tašką.

18. Paleidus scenarijų, turėtumėte matyti šį rezultatą:
    ```python
    b'"{\\"result\\": [true]}"'
    ```
Tai reiškia, kad širdies nepakankamumo prognozė pagal pateiktus duomenis yra teisinga. Tai logiška, nes jei atidžiau pažvelgsite į scenarijuje automatiškai sugeneruotus duomenis, viskas yra 0 ir klaidinga pagal numatytuosius nustatymus. Galite pakeisti duomenis naudodami šį pavyzdinį įvestį:

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
Scenarijus turėtų grąžinti:
    ```python
    b'"{\\"result\\": [true, false]}"'
    ```

Sveikiname! Jūs ką tik panaudojote įdiegtą modelį ir jį apmokėte Azure ML!

> **_PASTABA:_** Baigę projektą, nepamirškite ištrinti visų išteklių.
## 🚀 Iššūkis

Atidžiai peržiūrėkite modelio paaiškinimus ir detales, kurias AutoML sugeneravo geriausiems modeliams. Pabandykite suprasti, kodėl geriausias modelis yra geresnis už kitus. Kokie algoritmai buvo palyginti? Kokie jų skirtumai? Kodėl geriausias modelis šiuo atveju veikia geriau?

## [Po paskaitos testas](https://ff-quizzes.netlify.app/en/ds/)

## Apžvalga ir savarankiškas mokymasis

Šioje pamokoje išmokote, kaip apmokyti, įdiegti ir naudoti modelį, kad prognozuotumėte širdies nepakankamumo riziką, naudojant mažai kodo arba be kodo debesyje. Jei dar to nepadarėte, gilinkitės į modelio paaiškinimus, kuriuos AutoML sugeneravo geriausiems modeliams, ir pabandykite suprasti, kodėl geriausias modelis yra geresnis už kitus.

Galite gilintis į mažai kodo arba be kodo AutoML, skaitydami šią [dokumentaciją](https://docs.microsoft.com/azure/machine-learning/tutorial-first-experiment-automated-ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).

## Užduotis

[Mažai kodo arba be kodo duomenų mokslų projektas Azure ML](assignment.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.