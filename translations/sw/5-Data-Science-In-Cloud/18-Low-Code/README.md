<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "39f3b3a9d873eaa522c2e792ce0ca503",
  "translation_date": "2025-09-05T06:24:09+00:00",
  "source_file": "5-Data-Science-In-Cloud/18-Low-Code/README.md",
  "language_code": "sw"
}
-->
# Sayansi ya Takwimu katika Wingu: Njia ya "Low code/No code"

|![ Sketchnote na [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/18-DataScience-Cloud.png)|
|:---:|
| Sayansi ya Takwimu Katika Wingu: Low Code - _Sketchnote na [@nitya](https://twitter.com/nitya)_ |

Yaliyomo:

- [Sayansi ya Takwimu katika Wingu: Njia ya "Low code/No code"](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Maswali ya awali ya somo](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [1. Utangulizi](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [1.1 Azure Machine Learning ni nini?](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [1.2 Mradi wa Utabiri wa Mshuko wa Moyo:](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [1.3 Seti ya Takwimu ya Mshuko wa Moyo:](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [2. Mafunzo ya modeli kwa njia ya Low code/No code katika Azure ML Studio](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.1 Kuunda eneo la kazi la Azure ML](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.2 Rasilimali za Kompyuta](../../../../5-Data-Science-In-Cloud/18-Low-Code)
      - [2.2.1 Kuchagua chaguo sahihi kwa rasilimali zako za kompyuta](../../../../5-Data-Science-In-Cloud/18-Low-Code)
      - [2.2.2 Kuunda klasta ya kompyuta](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.3 Kupakia Seti ya Takwimu](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.4 Mafunzo ya Low code/No code kwa AutoML](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [3. Utekelezaji wa modeli kwa njia ya Low code/No code na matumizi ya endpoint](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [3.1 Utekelezaji wa modeli](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [3.2 Matumizi ya endpoint](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [🚀 Changamoto](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Maswali ya baada ya somo](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Mapitio na Kujisomea](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Kazi ya Nyumbani](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  
## [Maswali ya awali ya somo](https://ff-quizzes.netlify.app/en/ds/)

## 1. Utangulizi
### 1.1 Azure Machine Learning ni nini?

Jukwaa la wingu la Azure lina zaidi ya bidhaa 200 na huduma za wingu zilizoundwa kusaidia kuleta suluhisho mpya. Wanasayansi wa takwimu hutumia juhudi nyingi kuchunguza na kuandaa takwimu, na kujaribu aina mbalimbali za algorithimu za mafunzo ya modeli ili kuzalisha modeli sahihi. Kazi hizi zinachukua muda mwingi na mara nyingi hutumia rasilimali za kompyuta kwa njia isiyo na ufanisi.

[Azure ML](https://docs.microsoft.com/azure/machine-learning/overview-what-is-azure-machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) ni jukwaa la wingu kwa ajili ya kujenga na kuendesha suluhisho za kujifunza kwa mashine katika Azure. Inajumuisha vipengele na uwezo mbalimbali vinavyosaidia wanasayansi wa takwimu kuandaa takwimu, kufundisha modeli, kuchapisha huduma za utabiri, na kufuatilia matumizi yao. Muhimu zaidi, inawasaidia kuongeza ufanisi wao kwa kugeuza kiotomatiki kazi nyingi zinazochukua muda zinazohusiana na mafunzo ya modeli; na inawawezesha kutumia rasilimali za kompyuta za wingu zinazoweza kupanuka kwa ufanisi, kushughulikia kiasi kikubwa cha takwimu huku wakipata gharama tu wanapozitumia.

Azure ML inatoa zana zote zinazohitajika na watengenezaji na wanasayansi wa takwimu kwa ajili ya mchakato wao wa kujifunza kwa mashine. Hizi ni pamoja na:

- **Azure Machine Learning Studio**: ni portal ya wavuti katika Azure Machine Learning kwa chaguo za low-code na no-code kwa mafunzo ya modeli, utekelezaji, kiotomatiki, ufuatiliaji, na usimamizi wa mali. Studio inaunganishwa na Azure Machine Learning SDK kwa uzoefu usio na mshono.
- **Jupyter Notebooks**: kuunda haraka na kujaribu modeli za ML.
- **Azure Machine Learning Designer**: inaruhusu kuburuta na kuachia moduli ili kujenga majaribio na kisha kutekeleza mabomba katika mazingira ya low-code.
- **Automated machine learning UI (AutoML)**: inageuza kiotomatiki kazi za kurudia za maendeleo ya modeli za kujifunza kwa mashine, ikiruhusu kujenga modeli za ML kwa kiwango kikubwa, ufanisi, na uzalishaji, huku ikidumisha ubora wa modeli.
- **Data Labelling**: zana ya ML inayosaidia kuweka lebo kiotomatiki kwa takwimu.
- **Kiendelezi cha kujifunza kwa mashine kwa Visual Studio Code**: kinatoa mazingira kamili ya maendeleo kwa ajili ya kujenga na kusimamia miradi ya ML.
- **CLI ya kujifunza kwa mashine**: inatoa amri za kusimamia rasilimali za Azure ML kutoka kwa mstari wa amri.
- **Ujumuishaji na mifumo ya chanzo huria** kama PyTorch, TensorFlow, Scikit-learn na mingine mingi kwa mafunzo, utekelezaji, na usimamizi wa mchakato wa kujifunza kwa mashine kutoka mwanzo hadi mwisho.
- **MLflow**: ni maktaba ya chanzo huria kwa usimamizi wa mzunguko wa maisha wa majaribio yako ya kujifunza kwa mashine. **MLFlow Tracking** ni sehemu ya MLflow inayorekodi na kufuatilia vipimo vya mafunzo yako na vifaa vya modeli, bila kujali mazingira ya majaribio yako.

### 1.2 Mradi wa Utabiri wa Mshuko wa Moyo:

Hakuna shaka kwamba kutengeneza na kujenga miradi ni njia bora ya kujaribu ujuzi na maarifa yako. Katika somo hili, tutachunguza njia mbili tofauti za kujenga mradi wa sayansi ya takwimu kwa utabiri wa mshuko wa moyo katika Azure ML Studio, kupitia Low code/No code na kupitia Azure ML SDK kama inavyoonyeshwa kwenye mpangilio ufuatao:

![project-schema](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/project-schema.PNG)

Kila njia ina faida na hasara zake. Njia ya Low code/No code ni rahisi kuanza nayo kwani inahusisha kuingiliana na GUI (Graphical User Interface), bila ujuzi wa awali wa programu kuhitajika. Njia hii inawezesha majaribio ya haraka ya uwezekano wa mradi na kuunda POC (Proof Of Concept). Hata hivyo, mradi unapokua na mambo yanapohitaji kuwa tayari kwa uzalishaji, si rahisi kuunda rasilimali kupitia GUI. Tunahitaji kugeuza kiotomatiki kila kitu kwa njia ya programu, kuanzia uundaji wa rasilimali hadi utekelezaji wa modeli. Hapa ndipo ujuzi wa kutumia Azure ML SDK unakuwa muhimu.

|                   | Low code/No code | Azure ML SDK              |
|-------------------|------------------|---------------------------|
| Ujuzi wa programu | Hauhitajiki      | Unahitajika               |
| Muda wa kuendeleza| Haraka na rahisi | Inategemea ujuzi wa programu |
| Tayari kwa uzalishaji | Hapana          | Ndio                      |

### 1.3 Seti ya Takwimu ya Mshuko wa Moyo: 

Magonjwa ya moyo na mishipa (CVDs) ni sababu kuu ya vifo duniani, yakichangia 31% ya vifo vyote duniani. Sababu za hatari za mazingira na tabia kama matumizi ya tumbaku, lishe isiyo bora na unene kupita kiasi, kutofanya mazoezi, na matumizi mabaya ya pombe zinaweza kutumika kama vipengele vya modeli za makadirio. Uwezo wa kukadiria uwezekano wa maendeleo ya CVD unaweza kuwa na manufaa makubwa katika kuzuia mshuko wa moyo kwa watu walio katika hatari kubwa.

Kaggle imeweka [Seti ya Takwimu ya Mshuko wa Moyo](https://www.kaggle.com/andrewmvd/heart-failure-clinical-data) kwa matumizi ya umma, ambayo tutatumia kwa mradi huu. Unaweza kupakua seti ya takwimu sasa. Hii ni seti ya takwimu ya tabular yenye safu 13 (vipengele 12 na kipengele 1 cha lengo) na mistari 299. 

|    | Jina la kipengele          | Aina            | Maelezo                                                  | Mfano             |
|----|---------------------------|-----------------|---------------------------------------------------------|-------------------|
| 1  | umri                      | nambari         | umri wa mgonjwa                                         | 25                |
| 2  | anemia                    | boolean         | Kupungua kwa seli nyekundu za damu au hemoglobini       | 0 au 1            |
| 3  | creatinine_phosphokinase  | nambari         | Kiwango cha enzyme ya CPK katika damu                   | 542               |
| 4  | kisukari                  | boolean         | Ikiwa mgonjwa ana kisukari                               | 0 au 1            |
| 5  | ejection_fraction         | nambari         | Asilimia ya damu inayotoka moyoni kwa kila mkazo        | 45                |
| 6  | shinikizo la damu         | boolean         | Ikiwa mgonjwa ana shinikizo la damu                     | 0 au 1            |
| 7  | platelets                 | nambari         | Platelets katika damu                                   | 149000            |
| 8  | serum_creatinine          | nambari         | Kiwango cha serum creatinine katika damu               | 0.5               |
| 9  | serum_sodium              | nambari         | Kiwango cha serum sodium katika damu                   | jun               |
| 10 | jinsia                    | boolean         | mwanamke au mwanaume                                   | 0 au 1            |
| 11 | uvutaji sigara            | boolean         | Ikiwa mgonjwa anavuta sigara                            | 0 au 1            |
| 12 | muda                      | nambari         | kipindi cha ufuatiliaji (siku)                         | 4                 |
|----|---------------------------|-----------------|---------------------------------------------------------|-------------------|
| 21 | DEATH_EVENT [Lengo]       | boolean         | Ikiwa mgonjwa hufa wakati wa kipindi cha ufuatiliaji    | 0 au 1            |

Baada ya kuwa na seti ya takwimu, tunaweza kuanza mradi katika Azure.

## 2. Mafunzo ya modeli kwa njia ya Low code/No code katika Azure ML Studio
### 2.1 Kuunda eneo la kazi la Azure ML
Ili kufundisha modeli katika Azure ML, unahitaji kwanza kuunda eneo la kazi la Azure ML. Eneo la kazi ni rasilimali ya kiwango cha juu kwa Azure Machine Learning, ikitoa mahali pa kati pa kufanya kazi na mali zote unazounda unapotumia Azure Machine Learning. Eneo la kazi linahifadhi historia ya mafunzo yote, ikiwa ni pamoja na kumbukumbu, vipimo, matokeo, na picha ya maandishi yako. Unatumia taarifa hii kuamua ni mafunzo gani yanazalisha modeli bora. [Jifunze zaidi](https://docs.microsoft.com/azure/machine-learning/concept-workspace?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)

Inapendekezwa kutumia kivinjari cha kisasa zaidi kinacholingana na mfumo wako wa uendeshaji. Vivinjari vifuatavyo vinasaidiwa:

- Microsoft Edge (Microsoft Edge mpya, toleo la kisasa. Sio Microsoft Edge legacy)
- Safari (toleo la kisasa, Mac pekee)
- Chrome (toleo la kisasa)
- Firefox (toleo la kisasa)

Ili kutumia Azure Machine Learning, unda eneo la kazi katika usajili wako wa Azure. Unaweza kisha kutumia eneo hili la kazi kusimamia takwimu, rasilimali za kompyuta, maandishi, modeli, na mali nyingine zinazohusiana na mzigo wako wa kazi wa kujifunza kwa mashine.

> **_KUMBUKA:_** Usajili wako wa Azure utatozwa kiasi kidogo kwa uhifadhi wa takwimu mradi eneo la kazi la Azure Machine Learning lipo katika usajili wako, kwa hivyo tunapendekeza kufuta eneo la kazi la Azure Machine Learning ikiwa hautalitumia tena.

1. Ingia kwenye [portal ya Azure](https://ms.portal.azure.com/) ukitumia maelezo ya Microsoft yanayohusiana na usajili wako wa Azure.
2. Chagua **＋Unda rasilimali**
   
   ![workspace-1](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-1.PNG)

   Tafuta Machine Learning na uchague tile ya Machine Learning

   ![workspace-2](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-2.PNG)

   Bonyeza kitufe cha kuunda

   ![workspace-3](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-3.PNG)

   Jaza mipangilio kama ifuatavyo:
   - Usajili: Usajili wako wa Azure
   - Kikundi cha rasilimali: Unda au chagua kikundi cha rasilimali
   - Jina la eneo la kazi: Ingiza jina la kipekee kwa eneo lako la kazi
   - Eneo: Chagua eneo la kijiografia lililo karibu nawe
   - Akaunti ya uhifadhi: Kumbuka akaunti mpya ya uhifadhi itakayoundwa kwa eneo lako la kazi
   - Key vault: Kumbuka key vault mpya itakayoundwa kwa eneo lako la kazi
   - Application insights: Kumbuka rasilimali mpya ya application insights itakayoundwa kwa eneo lako la kazi
   - Container registry: Hakuna (moja itaundwa kiotomatiki mara ya kwanza unapotekeleza modeli kwenye kontena)

    ![workspace-4](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-4.PNG)

   - Bonyeza kuunda + hakiki na kisha kitufe cha kuunda
3. Subiri eneo lako la kazi liundwe (hii inaweza kuchukua dakika chache). Kisha nenda kwenye portal. Unaweza kulipata kupitia huduma ya Azure Machine Learning.
4. Kwenye ukurasa wa Muhtasari wa eneo lako la kazi, fungua Azure Machine Learning studio (au fungua tabo mpya ya kivinjari na nenda kwenye https://ml.azure.com), na ingia kwenye Azure Machine Learning studio ukitumia akaunti yako ya Microsoft. Ikiwa utaulizwa, chagua saraka yako ya Azure na usajili, na eneo lako la kazi la Azure Machine Learning.
   
![workspace-5](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-5.PNG)

5. Katika Azure Machine Learning studio, geuza icon ya ☰ juu kushoto ili kuona kurasa mbalimbali katika kiolesura. Unaweza kutumia kurasa hizi kusimamia rasilimali katika eneo lako la kazi.

![workspace-6](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-6.PNG)

Unaweza kusimamia eneo lako la kazi ukitumia portal ya Azure, lakini kwa wanasayansi wa takwimu na wahandisi wa operesheni za kujifunza kwa mashine, Azure Machine Learning Studio inatoa kiolesura kilicholenga zaidi kwa usimamizi wa rasilimali za eneo la kazi.

### 2.2 Rasilimali za Kompyuta

Rasilimali za Kompyuta ni rasilimali za wingu ambazo unaweza kutumia kuendesha mchakato wa mafunzo ya modeli na uchunguzi wa takwimu. Kuna aina nne za rasilimali za kompyuta unazoweza kuunda:

- **Compute Instances**: Vituo vya kazi vya maendeleo ambavyo wanasayansi wa takwimu wanaweza kutumia kufanya kazi na takwimu na modeli. Hii inahusisha uundaji wa Mashine ya Virtual (VM) na kuzindua mfano wa daftari. Unaweza kisha kufundisha modeli kwa kuita klasta ya kompyuta kutoka kwenye daftari.
- **Compute Clusters**: Klasta zinazoweza kupanuka za VM kwa usindikaji wa majaribio ya msimbo kwa mahitaji. Utahitaji klasta ya kompyuta unapofundisha modeli. Klasta za kompyuta zinaweza pia kutumia rasilimali maalum za GPU au CPU.
- **Inference Clusters**: Malengo ya utekelezaji kwa huduma za utabiri zinazotumia modeli zako zilizofundishwa.
- **Compute Iliyounganishwa**: Inaunganisha na rasilimali za kompyuta zilizopo za Azure, kama vile Mashine za Kawaida (Virtual Machines) au vikundi vya Azure Databricks.

#### 2.2.1 Kuchagua chaguo sahihi kwa rasilimali zako za kompyuta

Kuna mambo muhimu ya kuzingatia unapounda rasilimali ya kompyuta, na chaguo hizo zinaweza kuwa maamuzi muhimu.

**Je, unahitaji CPU au GPU?**

CPU (Central Processing Unit) ni mzunguko wa kielektroniki unaotekeleza maagizo yanayounda programu ya kompyuta. GPU (Graphics Processing Unit) ni mzunguko maalum wa kielektroniki unaoweza kutekeleza msimbo unaohusiana na michoro kwa kasi ya juu sana.

Tofauti kuu kati ya usanifu wa CPU na GPU ni kwamba CPU imeundwa kushughulikia kazi mbalimbali kwa haraka (kama inavyopimwa na kasi ya saa ya CPU), lakini ina mipaka katika idadi ya kazi zinazoweza kuendeshwa kwa wakati mmoja. GPU zimeundwa kwa ajili ya kompyuta sambamba na kwa hivyo ni bora zaidi kwa kazi za kujifunza kwa kina.

| CPU                                     | GPU                         |
|-----------------------------------------|-----------------------------|
| Gharama nafuu                           | Gharama kubwa               |
| Kiwango cha chini cha ushirikiano       | Kiwango cha juu cha ushirikiano |
| Polepole katika kufundisha mifano ya kujifunza kwa kina | Bora kwa kujifunza kwa kina |

**Ukubwa wa Klasta**

Vikundi vikubwa ni vya gharama kubwa zaidi lakini vitatoa majibu bora. Kwa hivyo, ikiwa una muda lakini bajeti ndogo, unapaswa kuanza na kikundi kidogo. Kinyume chake, ikiwa una bajeti kubwa lakini muda mfupi, unapaswa kuanza na kikundi kikubwa.

**Ukubwa wa VM**

Kulingana na muda wako na vikwazo vya bajeti, unaweza kubadilisha ukubwa wa RAM, diski, idadi ya cores na kasi ya saa. Kuongeza vigezo vyote hivyo kutakuwa na gharama kubwa zaidi, lakini kutatoa utendaji bora.

**Matukio ya Kujitolea au ya Kipaumbele cha Chini?**

Tukio la kipaumbele cha chini linamaanisha kuwa linaweza kusitishwa: kimsingi, Microsoft Azure inaweza kuchukua rasilimali hizo na kuzitumia kwa kazi nyingine, hivyo kusitisha kazi. Tukio la kujitolea, au lisiloweza kusitishwa, linamaanisha kuwa kazi haitasitishwa bila ruhusa yako. 
Hili ni jambo jingine la kuzingatia kati ya muda na pesa, kwani matukio yanayoweza kusitishwa ni ya gharama nafuu kuliko yale ya kujitolea.

#### 2.2.2 Kuunda klasta ya kompyuta

Katika [Azure ML workspace](https://ml.azure.com/) tuliyounda awali, nenda kwenye sehemu ya kompyuta na utaweza kuona rasilimali tofauti za kompyuta tulizojadili (yaani, compute instances, compute clusters, inference clusters na attached compute). Kwa mradi huu, tutahitaji klasta ya kompyuta kwa ajili ya kufundisha mfano. Katika Studio, bonyeza menyu ya "Compute", kisha kichupo cha "Compute cluster" na bonyeza kitufe cha "+ New" ili kuunda klasta ya kompyuta.

![22](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/cluster-1.PNG)

1. Chagua chaguo zako: Dedicated vs Low priority, CPU au GPU, ukubwa wa VM na idadi ya cores (unaweza kuweka mipangilio ya chaguo-msingi kwa mradi huu).
2. Bonyeza kitufe cha Next.

![23](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/cluster-2.PNG)

3. Pea klasta jina la kompyuta.
4. Chagua chaguo zako: Idadi ya chini/jumla ya nodes, sekunde za kusubiri kabla ya kupunguza ukubwa, ufikiaji wa SSH. Kumbuka kuwa ikiwa idadi ya chini ya nodes ni 0, utaokoa pesa wakati klasta haifanyi kazi. Kumbuka kuwa idadi kubwa ya nodes inamaanisha mafunzo yatakuwa mafupi zaidi. Idadi ya juu ya nodes inayopendekezwa ni 3.  
5. Bonyeza kitufe cha "Create". Hatua hii inaweza kuchukua dakika chache.

![29](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/cluster-3.PNG)

Hongera! Sasa kwa kuwa tuna klasta ya kompyuta, tunahitaji kupakia data kwenye Azure ML Studio.

### 2.3 Kupakia Dataset

1. Katika [Azure ML workspace](https://ml.azure.com/) tuliyounda awali, bonyeza "Datasets" kwenye menyu ya kushoto na bonyeza kitufe cha "+ Create dataset" ili kuunda dataset. Chagua chaguo la "From local files" na uchague dataset ya Kaggle tuliyopakua awali.
   
   ![24](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/dataset-1.PNG)

2. Pea dataset jina, aina na maelezo. Bonyeza Next. Pakia data kutoka kwa faili. Bonyeza Next.
   
   ![25](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/dataset-2.PNG)

3. Katika Schema, badilisha aina ya data kuwa Boolean kwa sifa zifuatazo: anaemia, diabetes, high blood pressure, sex, smoking, na DEATH_EVENT. Bonyeza Next na Bonyeza Create.
   
   ![26](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/dataset-3.PNG)

Nzuri! Sasa kwa kuwa dataset ipo na klasta ya kompyuta imeundwa, tunaweza kuanza mafunzo ya mfano!

### 2.4 Mafunzo ya Low code/No Code kwa AutoML 

Maendeleo ya jadi ya mifano ya kujifunza mashine yanahitaji rasilimali nyingi, maarifa makubwa ya uwanja na muda wa kuzalisha na kulinganisha mifano kadhaa. 
Mafunzo ya mashine yaliyojiendesha (AutoML), ni mchakato wa kujiendesha kazi za kurudia-rudia za maendeleo ya mifano ya kujifunza mashine. Inawawezesha wanasayansi wa data, wachambuzi, na watengenezaji kujenga mifano ya ML kwa kiwango kikubwa, ufanisi, na uzalishaji, huku ikidumisha ubora wa mfano. Inapunguza muda unaohitajika kupata mifano ya ML tayari kwa uzalishaji, kwa urahisi mkubwa na ufanisi. [Jifunze zaidi](https://docs.microsoft.com/azure/machine-learning/concept-automated-ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)

1. Katika [Azure ML workspace](https://ml.azure.com/) tuliyounda awali bonyeza "Automated ML" kwenye menyu ya kushoto na uchague dataset uliyoipakia. Bonyeza Next.

   ![27](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/aml-1.PNG)

2. Ingiza jina jipya la jaribio, safu lengwa (DEATH_EVENT) na klasta ya kompyuta tuliyounda. Bonyeza Next.
   
   ![28](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/aml-2.PNG)

3. Chagua "Classification" na Bonyeza Finish. Hatua hii inaweza kuchukua kati ya dakika 30 hadi saa 1, kulingana na ukubwa wa klasta yako ya kompyuta.
    
    ![30](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/aml-3.PNG)

4. Mara tu mchakato unapokamilika, bonyeza kichupo cha "Automated ML", bonyeza jaribio lako, na bonyeza Algorithm kwenye kadi ya "Best model summary".
    
    ![31](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/aml-4.PNG)

Hapa unaweza kuona maelezo ya kina ya mfano bora ambao AutoML ilitengeneza. Unaweza pia kuchunguza mifano mingine kwenye kichupo cha Models. Chukua dakika chache kuchunguza mifano kwenye kitufe cha Explanations (preview). Mara tu unapochagua mfano unaotaka kutumia (hapa tutachagua mfano bora ulioteuliwa na AutoML), tutaona jinsi ya kuutumia.

## 3. Utekelezaji wa mfano wa Low code/No Code na matumizi ya endpoint
### 3.1 Utekelezaji wa mfano

Kiolesura cha mafunzo ya mashine yaliyojiendesha kinakuwezesha kutekeleza mfano bora kama huduma ya wavuti kwa hatua chache. Utekelezaji ni ujumuishaji wa mfano ili uweze kutoa utabiri kulingana na data mpya na kutambua maeneo ya fursa. Kwa mradi huu, utekelezaji kama huduma ya wavuti unamaanisha kuwa programu za matibabu zitaweza kutumia mfano kufanya utabiri wa moja kwa moja wa hatari ya wagonjwa wao kupata mshtuko wa moyo.

Katika maelezo ya mfano bora, bonyeza kitufe cha "Deploy".
    
![deploy-1](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/deploy-1.PNG)

15. Pea jina, maelezo, aina ya kompyuta (Azure Container Instance), wezesha uthibitishaji na bonyeza Deploy. Hatua hii inaweza kuchukua takriban dakika 20 kukamilika. Mchakato wa utekelezaji unajumuisha hatua kadhaa ikiwa ni pamoja na kusajili mfano, kuzalisha rasilimali, na kuziandaa kwa huduma ya wavuti. Ujumbe wa hali utaonekana chini ya Deploy status. Chagua Refresh mara kwa mara ili kuangalia hali ya utekelezaji. Imewekwa na inafanya kazi wakati hali ni "Healthy".

![deploy-2](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/deploy-2.PNG)

16. Mara tu imewekwa, bonyeza kichupo cha Endpoint na bonyeza endpoint uliyoitekeleza. Hapa unaweza kupata maelezo yote unayohitaji kujua kuhusu endpoint.

![deploy-3](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/deploy-3.PNG)

Ajabu! Sasa kwa kuwa tuna mfano uliowekwa, tunaweza kuanza matumizi ya endpoint.

### 3.2 Matumizi ya Endpoint

Bonyeza kichupo cha "Consume". Hapa unaweza kupata endpoint ya REST na script ya Python katika chaguo la matumizi. Chukua muda kusoma msimbo wa Python.

Script hii inaweza kuendeshwa moja kwa moja kutoka kwa mashine yako ya ndani na itatumia endpoint yako.

![35](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/consumption-1.PNG)

Chukua muda kuangalia mistari hii miwili ya msimbo:

```python
url = 'http://98e3715f-xxxx-xxxx-xxxx-9ec22d57b796.centralus.azurecontainer.io/score'
api_key = '' # Replace this with the API key for the web service
```
Kigezo cha `url` ni endpoint ya REST inayopatikana kwenye kichupo cha consume na kigezo cha `api_key` ni ufunguo wa msingi pia unaopatikana kwenye kichupo cha consume (ikiwa tu umewezesha uthibitishaji). Hivi ndivyo script inaweza kutumia endpoint.

18. Ukiendesha script, unapaswa kuona matokeo yafuatayo:
    ```python
    b'"{\\"result\\": [true]}"'
    ```
Hii inamaanisha kuwa utabiri wa mshtuko wa moyo kwa data iliyotolewa ni kweli. Hii inaeleweka kwa sababu ukitazama kwa karibu data iliyotengenezwa kiotomatiki kwenye script, kila kitu kiko 0 na si kweli kwa chaguo-msingi. Unaweza kubadilisha data kwa sampuli ifuatayo:

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
Script inapaswa kurudisha:
    ```python
    b'"{\\"result\\": [true, false]}"'
    ```

Hongera! Umetumia mfano uliowekwa na kuufundisha kwenye Azure ML!

> **_NOTE:_** Mara tu unapomaliza mradi, usisahau kufuta rasilimali zote.
## 🚀 Changamoto

Angalia kwa karibu maelezo na maelezo ambayo AutoML ilitengeneza kwa mifano bora. Jaribu kuelewa kwa nini mfano bora ni bora kuliko mingine. Ni algoriti gani zililinganishwa? Tofauti ni zipi kati yao? Kwa nini bora zaidi inafanya kazi vizuri zaidi katika kesi hii?

## [Jaribio la baada ya somo](https://ff-quizzes.netlify.app/en/ds/)

## Mapitio na Kujisomea

Katika somo hili, umejifunza jinsi ya kufundisha, kutekeleza na kutumia mfano wa kutabiri hatari ya mshtuko wa moyo kwa njia ya Low code/No Code kwenye wingu. Ikiwa bado hujafanya hivyo, chunguza kwa kina maelezo ya mfano ambayo AutoML ilitengeneza kwa mifano bora na jaribu kuelewa kwa nini mfano bora ni bora kuliko mingine.

Unaweza kwenda mbali zaidi katika AutoML ya Low code/No Code kwa kusoma [hati hii](https://docs.microsoft.com/azure/machine-learning/tutorial-first-experiment-automated-ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).

## Kazi

[Mradi wa Data Science wa Low code/No Code kwenye Azure ML](assignment.md)

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia huduma ya tafsiri ya kitaalamu ya binadamu. Hatutawajibika kwa maelewano mabaya au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.