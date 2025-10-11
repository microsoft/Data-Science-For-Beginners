<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd4da10766c64fce4294a98f6479dfb0",
  "translation_date": "2025-10-11T15:27:36+00:00",
  "source_file": "5-Data-Science-In-Cloud/18-Low-Code/README.md",
  "language_code": "et"
}
-->
# Andmeteadus pilves: "Vähe koodi/Ilma koodita" lähenemine

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/18-DataScience-Cloud.png)|
|:---:|
| Andmeteadus pilves: Vähe koodi - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Sisukord:

- [Andmeteadus pilves: "Vähe koodi/Ilma koodita" lähenemine](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Eelloengu viktoriin](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [1. Sissejuhatus](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [1.1 Mis on Azure Machine Learning?](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [1.2 Südamepuudulikkuse ennustamise projekt:](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [1.3 Südamepuudulikkuse andmestik:](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [2. Mudeli treenimine Azure ML Studios vähe koodi/ilma koodita meetodil](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.1 Azure ML tööruumi loomine](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.2 Arvutusressursid](../../../../5-Data-Science-In-Cloud/18-Low-Code)
      - [2.2.1 Õigete arvutusressursside valimine](../../../../5-Data-Science-In-Cloud/18-Low-Code)
      - [2.2.2 Arvutusklastri loomine](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.3 Andmestiku laadimine](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.4 Vähe koodi/ilma koodita treenimine AutoML abil](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [3. Mudeli juurutamine ja tarbimine vähe koodi/ilma koodita meetodil](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [3.1 Mudeli juurutamine](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [3.2 Lõpp-punkti tarbimine](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [🚀 Väljakutse](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Järelloengu viktoriin](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Ülevaade ja iseseisev õppimine](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Kodutöö](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  
## [Eelloengu viktoriin](https://ff-quizzes.netlify.app/en/ds/quiz/34)

## 1. Sissejuhatus
### 1.1 Mis on Azure Machine Learning?

Azure pilveplatvorm koosneb enam kui 200 tootest ja pilveteenusest, mis on loodud selleks, et aidata teil ellu viia uusi lahendusi. Andmeteadlased kulutavad palju aega andmete uurimisele ja eeltöötlemisele ning erinevate mudeli treenimise algoritmide katsetamisele, et luua täpseid mudeleid. Need ülesanded on ajamahukad ja tihti ebaefektiivsed, kasutades kallist arvutusressurssi.

[Azure ML](https://docs.microsoft.com/azure/machine-learning/overview-what-is-azure-machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) on pilvepõhine platvorm masinõppe lahenduste loomiseks ja haldamiseks Azure'is. See sisaldab laia valikut funktsioone ja võimalusi, mis aitavad andmeteadlastel valmistada ette andmeid, treenida mudeleid, avaldada ennustusteenuseid ja jälgida nende kasutamist. Kõige olulisem on see, et see suurendab nende efektiivsust, automatiseerides paljusid ajamahukaid ülesandeid, mis on seotud mudelite treenimisega; ning võimaldab kasutada pilvepõhiseid arvutusressursse, mis skaleeruvad tõhusalt, et hallata suuri andmemahtusid, samal ajal kulusid tekitades ainult kasutamise ajal.

Azure ML pakub kõiki tööriistu, mida arendajad ja andmeteadlased vajavad oma masinõppe töövoogude jaoks. Nende hulka kuuluvad:

- **Azure Machine Learning Studio**: veebipõhine portaal Azure Machine Learningis, mis pakub vähe koodi ja ilma koodita võimalusi mudelite treenimiseks, juurutamiseks, automatiseerimiseks, jälgimiseks ja varade haldamiseks. Studio integreerub Azure Machine Learning SDK-ga, pakkudes sujuvat kogemust.
- **Jupyter Notebooks**: kiire prototüüpimine ja ML mudelite testimine.
- **Azure Machine Learning Designer**: võimaldab lohistada ja paigutada mooduleid eksperimentide loomiseks ning seejärel madala koodiga keskkonnas torujuhtmete juurutamiseks.
- **Automatiseeritud masinõppe kasutajaliides (AutoML)**: automatiseerib masinõppe mudeli arendamise iteratiivseid ülesandeid, võimaldades luua ML mudeleid suure ulatuse, efektiivsuse ja produktiivsusega, säilitades samal ajal mudeli kvaliteedi.
- **Andmete märgistamine**: abistatud ML tööriist andmete automaatseks märgistamiseks.
- **Masinõppe laiendus Visual Studio Code'ile**: pakub täisfunktsionaalset arenduskeskkonda ML projektide loomiseks ja haldamiseks.
- **Masinõppe CLI**: pakub käske Azure ML ressursside haldamiseks käsurealt.
- **Integreerimine avatud lähtekoodiga raamistikudega**, nagu PyTorch, TensorFlow, Scikit-learn ja paljud teised, treenimiseks, juurutamiseks ja masinõppe protsessi haldamiseks.
- **MLflow**: avatud lähtekoodiga teek masinõppe eksperimentide elutsükli haldamiseks. **MLFlow Tracking** on MLflow komponent, mis logib ja jälgib teie treeningu jooksu mõõdikuid ja mudeli artefakte, sõltumata teie eksperimendi keskkonnast.

### 1.2 Südamepuudulikkuse ennustamise projekt:

Pole kahtlust, et projektide loomine ja ehitamine on parim viis oma oskuste ja teadmiste proovile panemiseks. Selles õppetunnis uurime kahte erinevat viisi südamepuudulikkuse rünnakute ennustamise andmeteaduse projekti loomiseks Azure ML Studios: vähe koodi/ilma koodita meetodil ja Azure ML SDK abil, nagu on näidatud järgmisel skeemil:

![project-schema](../../../../translated_images/project-schema.736f6e403f321eb48d10242b3f4334dc6ccf0eabef8ff87daf52b89781389fcb.et.png)

Igal meetodil on oma plussid ja miinused. Vähe koodi/ilma koodita meetod on lihtsam alustada, kuna see hõlmab graafilise kasutajaliidese (GUI) kasutamist, ilma et oleks vaja eelnevaid teadmisi koodist. See meetod võimaldab projekti elujõulisust kiiresti testida ja luua POC (Proof Of Concept). Kuid kui projekt kasvab ja asjad peavad olema tootmisvalmis, ei ole GUI kaudu ressursside loomine teostatav. Siin muutub Azure ML SDK kasutamise oskus hädavajalikuks.

|                   | Vähe koodi/Ilma koodita | Azure ML SDK              |
|-------------------|-------------------------|---------------------------|
| Koodioskused      | Pole vajalik           | Vajalik                  |
| Arendusaeg        | Kiire ja lihtne        | Sõltub koodioskustest    |
| Tootmisvalmidus   | Ei                     | Jah                      |

### 1.3 Südamepuudulikkuse andmestik:

Kardiovaskulaarsed haigused (CVD-d) on ülemaailmselt peamine surmapõhjus, moodustades 31% kõigist surmadest. Keskkonna- ja käitumuslikud riskifaktorid, nagu tubaka kasutamine, ebatervislik toitumine ja rasvumine, füüsiline passiivsus ja kahjulik alkoholitarbimine, võiksid olla mudelite hinnangute jaoks kasutatavad tunnused. Võimalus hinnata CVD arengu tõenäosust oleks suureks abiks kõrge riskiga inimeste rünnakute ennetamisel.

Kaggle on teinud avalikult kättesaadavaks [Südamepuudulikkuse andmestiku](https://www.kaggle.com/andrewmvd/heart-failure-clinical-data), mida me selles projektis kasutame. Saate andmestiku kohe alla laadida. See on tabelandmestik, millel on 13 veergu (12 tunnust ja 1 sihtmuutuja) ja 299 rida.

|    | Muutuja nimi              | Tüüp            | Kirjeldus                                               | Näide             |
|----|---------------------------|-----------------|---------------------------------------------------------|-------------------|
| 1  | age                       | numbriline      | patsiendi vanus                                         | 25                |
| 2  | anaemia                   | boolean         | Punaste vereliblede või hemoglobiini vähenemine         | 0 või 1           |
| 3  | creatinine_phosphokinase  | numbriline      | CPK ensüümi tase veres                                  | 542               |
| 4  | diabetes                  | boolean         | Kas patsiendil on diabeet                               | 0 või 1           |
| 5  | ejection_fraction         | numbriline      | Südamest väljuva vere protsent iga kokkutõmbega         | 45                |
| 6  | high_blood_pressure       | boolean         | Kas patsiendil on hüpertensioon                         | 0 või 1           |
| 7  | platelets                 | numbriline      | Trombotsüütide arv veres                                | 149000            |
| 8  | serum_creatinine          | numbriline      | Seerumi kreatiniini tase veres                          | 0.5               |
| 9  | serum_sodium              | numbriline      | Seerumi naatriumi tase veres                            | jun               |
| 10 | sex                       | boolean         | naine või mees                                          | 0 või 1           |
| 11 | smoking                   | boolean         | Kas patsient suitsetab                                  | 0 või 1           |
| 12 | time                      | numbriline      | jälgimisperiood (päevad)                                | 4                 |
|----|---------------------------|-----------------|---------------------------------------------------------|-------------------|
| 21 | DEATH_EVENT [Sihtmuutuja] | boolean         | Kas patsient sureb jälgimisperioodi jooksul             | 0 või 1           |

Kui andmestik on olemas, saame alustada projekti Azure'is.

## 2. Mudeli treenimine Azure ML Studios vähe koodi/ilma koodita meetodil
### 2.1 Azure ML tööruumi loomine
Mudeli treenimiseks Azure ML-is peate esmalt looma Azure ML tööruumi. Tööruum on Azure Machine Learningi kõrgeim ressurss, mis pakub tsentraliseeritud kohta kõigi artefaktide haldamiseks, mida loote Azure Machine Learningi kasutamisel. Tööruum hoiab ajalugu kõigist treeningjooksudest, sealhulgas logisid, mõõdikuid, väljundeid ja teie skriptide hetktõmmiseid. Kasutate seda teavet, et määrata, milline treeningjooks annab parima mudeli. [Loe rohkem](https://docs.microsoft.com/azure/machine-learning/concept-workspace?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)

Soovitatav on kasutada kõige uuemat brauserit, mis sobib teie operatsioonisüsteemiga. Järgmised brauserid on toetatud:

- Microsoft Edge (uusim versioon, mitte Microsoft Edge legacy)
- Safari (uusim versioon, ainult Mac)
- Chrome (uusim versioon)
- Firefox (uusim versioon)

Azure Machine Learningi kasutamiseks looge tööruum oma Azure'i tellimuses. Seejärel saate seda tööruumi kasutada andmete, arvutusressursside, koodi, mudelite ja muude masinõppe töökoormustega seotud artefaktide haldamiseks.

> **_MÄRKUS:_** Teie Azure'i tellimusele rakendatakse väike tasu andmesalvestuse eest seni, kuni Azure Machine Learningi tööruum eksisteerib teie tellimuses, seega soovitame teil kustutada Azure Machine Learningi tööruum, kui te seda enam ei kasuta.

1. Logige sisse [Azure portaali](https://ms.portal.azure.com/) Microsofti mandaatidega, mis on seotud teie Azure'i tellimusega.
2. Valige **＋Loo ressurss**
   
   ![workspace-1](../../../../translated_images/workspace-1.ac8694d60b073ed1ae8333d71244dc8a9b3e439d54593724f98f1beefdd27b08.et.png)

   Otsige Machine Learning ja valige Machine Learningi plaat

   ![workspace-2](../../../../translated_images/workspace-2.ae7c486db8796147075e4a56566aa819827dd6c4c8d18d64590317c3be625f17.et.png)

   Klõpsake nuppu "Loo"

   ![workspace-3](../../../../translated_images/workspace-3.398ca4a5858132cce584db9df10c5a011cd9075eb182e647a77d5cac01771eea.et.png)

   Täitke seaded järgmiselt:
   - Tellimus: Teie Azure'i tellimus
   - Ressursside grupp: Looge või valige ressursside grupp
   - Tööruumi nimi: Sisestage oma tööruumile unikaalne nimi
   - Piirkond: Valige geograafiline piirkond, mis on teile kõige lähemal
   - Salvestuskonto: Märkige vaikimisi uus salvestuskonto, mis luuakse teie tööruumi jaoks
   - Võtmehoidla: Märkige vaikimisi uus võtmehoidla, mis luuakse teie tööruumi jaoks
   - Rakenduse ülevaated: Märkige vaikimisi uus rakenduse ülevaate ressurss, mis luuakse teie tööruumi jaoks
   - Konteineriregister: Puudub (üks luuakse automaatselt esimesel korral, kui juurutate mudeli konteinerisse)

    ![workspace-4](../../../../translated_images/workspace-4.bac87f6599c4df63e624fc2608990f965887bee551d9dedc71c687b43b986b6a.et.png)

   - Klõpsake nuppu "Loo + ülevaade" ja seejärel nuppu "Loo"
3. Oodake, kuni teie tööruum luuakse (see võib võtta paar minutit). Seejärel minge portaali. Leiate selle Machine Learning Azure'i teenuse kaudu.
4. Tööruumi ülevaate lehel käivitage Azure Machine Learning studio (või avage uus brauseri vahekaart ja navigeerige aadressile https://ml.azure.com) ning logige sisse Azure Machine Learning studio kasutades oma Microsofti kontot. Kui küsitakse, valige oma Azure'i kataloog ja tellimus ning Azure Machine Learningi tööruum.
   
![workspace-5](../../../../translated_images/workspace-5.a6eb17e0a5e6420018b08bdaf3755ce977f96f1df3ea363d2476a9dce7e15adb.et.png)

5. Azure Machine Learning studios lülitage ☰ ikooni ülaosas, et vaadata erinevaid lehti liideses. Saate neid lehti kasutada oma tööruumi ressursside haldamiseks.

![workspace-6](../../../../translated_images/workspace-6.8dd81fe841797ee17f8f73916769576260b16c4e17e850d277a49db35fd74a15.et.png)

Tööruumi saate hallata Azure'i portaali kaudu, kuid andmeteadlaste ja masinõppe operatsioonide inseneride jaoks pakub Azure Machine Learning Studio rohkem keskendunud kasutajaliidest tööruumi ressursside haldamiseks.

### 2.2 Arvutusressursid

Arvutusressursid on pilvepõhised ressursid, millel saate käivitada mudeli treenimise ja andmete uurimise protsesse. Saate luua nelja tüüpi arvutusressursse:

- **Arvutusinstantsid**: Arendustööjaamad, mida andmeteadlased saavad kasutada andmete ja mudelitega töötamiseks. See hõlmab virtuaalmasina (VM) loomist ja märkmiku instantsi käivitamist. Seejärel saate mudelit treenida, kutsudes märkmikust arvutusklastri.
- **Arvutusklastrid**: Skaleeritavad VM-klastrid eksperimentide koodi nõudmisel töötlemiseks. Vajate seda mudeli treenimiseks. Arvutusklastrid võivad kasutada ka spetsialiseeritud GPU- või CPU-ressursse.
- **Inference Clusters**: Ennustusteenuste juurutamise sihtkohad, mis kasutavad teie treenitud mudeleid.
- **Attached Compute**: Lingid olemasolevatele Azure'i arvutusressurssidele, nagu virtuaalmasinad või Azure Databricks klastrid.

#### 2.2.1 Õigete valikute tegemine arvutusressursside jaoks

Arvutusressursi loomisel tuleb arvestada mitmete oluliste teguritega, mis võivad olla kriitilised otsused.

**Kas vajate CPU-d või GPU-d?**

CPU (Central Processing Unit) on elektrooniline vooluring, mis täidab arvutiprogrammi juhiseid. GPU (Graphics Processing Unit) on spetsialiseeritud elektrooniline vooluring, mis suudab graafikaga seotud koodi täita väga suure kiirusega.

Peamine erinevus CPU ja GPU arhitektuuri vahel seisneb selles, et CPU on loodud mitmesuguste ülesannete kiireks täitmiseks (mõõdetuna CPU taktsagedusega), kuid sellel on piiratud samaaegselt töötavate ülesannete arv. GPU-d on loodud paralleelseks arvutamiseks ja seetõttu sobivad need paremini süvaõppe ülesannete jaoks.

| CPU                                     | GPU                         |
|-----------------------------------------|-----------------------------|
| Vähem kulukas                           | Kallim                     |
| Madalam samaaegsuse tase                | Kõrgem samaaegsuse tase    |
| Aeglasem süvaõppe mudelite treenimisel  | Optimaalne süvaõppe jaoks  |

**Klastri suurus**

Suuremad klastrid on kallimad, kuid tagavad parema reageerimisvõime. Seega, kui teil on aega, kuid mitte piisavalt raha, peaksite alustama väikese klastriga. Vastupidi, kui teil on raha, kuid mitte palju aega, peaksite alustama suurema klastriga.

**VM suurus**

Sõltuvalt teie aja- ja eelarvepiirangutest saate varieerida RAM-i, ketta, tuumade arvu ja taktsageduse suurust. Kõigi nende parameetrite suurendamine on kulukam, kuid tagab parema jõudluse.

**Dedikeeritud või madala prioriteediga instantsid?**

Madala prioriteediga instants tähendab, et see on katkestatav: Microsoft Azure võib need ressursid võtta ja määrata teisele ülesandele, katkestades seega töö. Dedikeeritud instants ehk mittekatkestatav tähendab, et töö lõpetatakse ainult teie loal. See on veel üks aja ja raha kaalutlus, kuna katkestatavad instantsid on odavamad kui dedikeeritud instantsid.

#### 2.2.2 Arvutusklastri loomine

[Azure ML tööruumis](https://ml.azure.com/), mille me varem lõime, minge arvutuse sektsiooni ja näete erinevaid arvutusressursse, mida me just arutasime (st arvutusinstantsid, arvutusklastrid, ennustusklastrid ja seotud arvutus). Selle projekti jaoks vajame mudeli treenimiseks arvutusklastrit. Studios klõpsake menüül "Compute", seejärel vahekaardil "Compute cluster" ja klõpsake nuppu "+ New", et luua arvutusklaster.

![22](../../../../translated_images/cluster-1.b78cb630bb543729b11f60c34d97110a263f8c27b516ba4dc47807b3cee5579f.et.png)

1. Valige oma valikud: Dedikeeritud vs Madala prioriteediga, CPU või GPU, VM suurus ja tuumade arv (võite selle projekti jaoks jätta vaikeseaded).
2. Klõpsake nupul Next.

![23](../../../../translated_images/cluster-2.ea30cdbc9f926bb9e05af3fdbc1f679811c796dc2a6847f935290aec15526e88.et.png)

3. Andke klastrile arvutusnimi.
4. Valige oma valikud: Minimaalne/maksimaalne sõlmede arv, tühikäigu sekundid enne vähendamist, SSH-juurdepääs. Pange tähele, et kui minimaalne sõlmede arv on 0, säästate raha, kui klaster on tühikäigul. Pange tähele, et mida suurem on maksimaalne sõlmede arv, seda lühem on treenimisaeg. Maksimaalne soovitatav sõlmede arv on 3.  
5. Klõpsake nupul "Create". See samm võib võtta paar minutit.

![29](../../../../translated_images/cluster-3.8a334bc070ec173a329ce5abd2a9d727542e83eb2347676c9af20f2c8870b3e7.et.png)

Suurepärane! Nüüd, kui meil on arvutusklaster, peame andmed Azure ML Studiosse laadima.

### 2.3 Andmestiku laadimine

1. [Azure ML tööruumis](https://ml.azure.com/), mille me varem lõime, klõpsake vasakpoolses menüüs "Datasets" ja klõpsake nuppu "+ Create dataset", et luua andmestik. Valige "From local files" ja valige varem alla laaditud Kaggle'i andmestik.

   ![24](../../../../translated_images/dataset-1.e86ab4e10907a6e9c2a72577b51db35f13689cb33702337b8b7032f2ef76dac2.et.png)

2. Andke oma andmestikule nimi, tüüp ja kirjeldus. Klõpsake Next. Laadige andmed failidest. Klõpsake Next.

   ![25](../../../../translated_images/dataset-2.f58de1c435d5bf9ccb16ccc5f5d4380eb2b50affca85cfbf4f97562bdab99f77.et.png)

3. Skeemis muutke andmetüüp Boolean järgnevate tunnuste jaoks: anaemia, diabeet, kõrge vererõhk, sugu, suitsetamine ja DEATH_EVENT. Klõpsake Next ja seejärel Create.

   ![26](../../../../translated_images/dataset-3.58db8c0eb783e89236a02bbce5bb4ba808d081a87d994d5284b1ae59928c95bf.et.png)

Suurepärane! Nüüd, kui andmestik on paigas ja arvutusklaster loodud, saame alustada mudeli treenimist!

### 2.4 Madala koodiga/koodivaba treenimine AutoML-iga

Traditsiooniline masinõppe mudeli arendamine on ressursimahukas, nõuab märkimisväärset valdkonna teadmisi ja aega, et toota ja võrrelda kümneid mudeleid. Automatiseeritud masinõpe (AutoML) on protsess, mis automatiseerib masinõppe mudeli arendamise aeganõudvaid ja korduvaid ülesandeid. See võimaldab andmeteadlastel, analüütikutel ja arendajatel luua ML-mudeleid suure ulatuse, tõhususe ja produktiivsusega, säilitades samal ajal mudeli kvaliteedi. See vähendab tootmisvalmis ML-mudelite loomise aega, pakkudes suurt lihtsust ja tõhusust. [Loe lähemalt](https://docs.microsoft.com/azure/machine-learning/concept-automated-ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)

1. [Azure ML tööruumis](https://ml.azure.com/), mille me varem lõime, klõpsake vasakpoolses menüüs "Automated ML" ja valige just üles laaditud andmestik. Klõpsake Next.

   ![27](../../../../translated_images/aml-1.67281a85d3a1e2f34eb367b2d0f74e1039d13396e510f363cd8766632106d1ec.et.png)

2. Sisestage uue eksperimendi nimi, sihtveerg (DEATH_EVENT) ja loodud arvutusklaster. Klõpsake Next.

   ![28](../../../../translated_images/aml-2.c9fb9cffb39ccbbe21ab9810ae937195d41a489744e15cff2b8477ed4dcae1ec.et.png)

3. Valige "Classification" ja klõpsake Finish. See samm võib võtta 30 minutist kuni 1 tunnini, sõltuvalt teie arvutusklastri suurusest.

   ![30](../../../../translated_images/aml-3.a7952e4295f38cc6cdb0c7ed6dc71ea756b7fb5697ec126bc1220f87c5fa9231.et.png)

4. Kui jooks on lõpetatud, klõpsake vahekaardil "Automated ML", klõpsake oma jooksul ja seejärel klõpsake "Best model summary" kaardil algoritmil.

   ![31](../../../../translated_images/aml-4.7a627e09cb6f16d0aa246059d9faee3d1725cc4258d0c8df15e801f73afc7e2c.et.png)

Siin näete üksikasjalikku kirjeldust parimast mudelist, mille AutoML genereeris. Samuti saate uurida teisi mudeleid vahekaardil Models. Võtke paar minutit, et uurida mudeleid selgituste (preview) nupul. Kui olete valinud mudeli, mida soovite kasutada (siin valime AutoML-i poolt valitud parima mudeli), näeme, kuidas seda juurutada.

## 3. Madala koodiga/koodivaba mudeli juurutamine ja lõpp-punkti tarbimine
### 3.1 Mudeli juurutamine

Automatiseeritud masinõppe liides võimaldab teil parima mudeli veebiteenusena juurutada mõne sammuga. Juurutamine tähendab mudeli integreerimist, et see saaks teha ennustusi uute andmete põhjal ja tuvastada potentsiaalseid võimalusi. Selle projekti puhul tähendab veebiteenuse juurutamine, et meditsiinirakendused saavad mudelit kasutada, et teha reaalajas ennustusi patsientide südameataki riski kohta.

Parima mudeli kirjelduses klõpsake nuppu "Deploy".

![deploy-1](../../../../translated_images/deploy-1.ddad725acadc84e34553c3d09e727160faeb32527a9fb8b904c0f99235a34bb6.et.png)

15. Andke sellele nimi, kirjeldus, arvutustüüp (Azure Container Instance), lubage autentimine ja klõpsake Deploy. See samm võib võtta umbes 20 minutit. Juurutamisprotsess hõlmab mitmeid samme, sealhulgas mudeli registreerimist, ressursside loomist ja nende konfigureerimist veebiteenuse jaoks. Juurutamise olek ilmub Deploy status all. Valige Refresh perioodiliselt, et kontrollida juurutamise olekut. Kui olek on "Healthy", on see juurutatud ja töötab.

![deploy-2](../../../../translated_images/deploy-2.94dbb13f239086473aa4bf814342fd40483d136849b080f02bafbb995383940e.et.png)

16. Kui see on juurutatud, klõpsake vahekaardil Endpoint ja klõpsake just juurutatud lõpp-punkti. Siit leiate kõik üksikasjad, mida peate lõpp-punkti kohta teadma.

![deploy-3](../../../../translated_images/deploy-3.fecefef070e8ef3b28e802326d107f61ac4e672d20bf82d05f78d025f9e6c611.et.png)

Vinge! Nüüd, kui meil on mudel juurutatud, saame alustada lõpp-punkti tarbimist.

### 3.2 Lõpp-punkti tarbimine

Klõpsake vahekaardil "Consume". Siit leiate REST-lõpp-punkti ja Python-skripti tarbimisvalikus. Võtke aega, et lugeda Python-koodi.

Seda skripti saab otse teie kohalikust masinast käivitada ja see tarbib teie lõpp-punkti.

![35](../../../../translated_images/consumption-1.700abd196452842a020c7d745908637a6e4c5c50494ad1217be80e283e0de154.et.png)

Võtke hetk, et vaadata neid kahte koodirida:

```python
url = 'http://98e3715f-xxxx-xxxx-xxxx-9ec22d57b796.centralus.azurecontainer.io/score'
api_key = '' # Replace this with the API key for the web service
```
Muutuja `url` on REST-lõpp-punkt, mis on leitav tarbimisvahekaardilt, ja muutuja `api_key` on esmane võti, mis on samuti leitav tarbimisvahekaardilt (ainult juhul, kui olete lubanud autentimise). Nii saab skript lõpp-punkti tarbida.

18. Skripti käivitamisel peaksite nägema järgmist väljundit:
    ```python
    b'"{\\"result\\": [true]}"'
    ```
See tähendab, et südamepuudulikkuse ennustus antud andmete põhjal on tõene. See on loogiline, sest kui vaadata skriptis automaatselt genereeritud andmeid, on kõik vaikimisi 0 ja vale. Saate andmeid muuta järgmise sisendi näidisega:

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
Skript peaks tagastama:
    ```python
    b'"{\\"result\\": [true, false]}"'
    ```

Palju õnne! Te just tarbisite juurutatud mudelit ja treenisite seda Azure ML-is!

> **_MÄRKUS:_** Kui olete projektiga lõpetanud, ärge unustage kõiki ressursse kustutada.
## 🚀 Väljakutse

Vaadake lähemalt AutoML-i poolt genereeritud mudeli selgitusi ja üksikasju parimate mudelite kohta. Proovige mõista, miks parim mudel on parem kui teised. Milliseid algoritme võrreldi? Millised on nende erinevused? Miks on parim mudel antud juhul paremini toimiv?

## [Loengu järgne viktoriin](https://ff-quizzes.netlify.app/en/ds/quiz/35)

## Ülevaade ja iseseisev õppimine

Selles õppetunnis õppisite, kuidas treenida, juurutada ja tarbida mudelit, et ennustada südamepuudulikkuse riski madala koodiga/koodivaba viisil pilves. Kui te pole seda veel teinud, süvenege AutoML-i poolt genereeritud mudeli selgitustesse ja proovige mõista, miks parim mudel on parem kui teised.

Saate minna kaugemale madala koodiga/koodivaba AutoML-i teemal, lugedes seda [dokumentatsiooni](https://docs.microsoft.com/azure/machine-learning/tutorial-first-experiment-automated-ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).

## Ülesanne

[Madala koodiga/koodivaba andmeteaduse projekt Azure ML-is](assignment.md)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.