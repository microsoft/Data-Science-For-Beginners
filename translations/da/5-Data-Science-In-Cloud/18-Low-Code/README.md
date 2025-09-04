<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "39f3b3a9d873eaa522c2e792ce0ca503",
  "translation_date": "2025-09-04T19:08:33+00:00",
  "source_file": "5-Data-Science-In-Cloud/18-Low-Code/README.md",
  "language_code": "da"
}
-->
# Data Science i skyen: Den "Low code/No code" tilgang

|![ Sketchnote af [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/18-DataScience-Cloud.png)|
|:---:|
| Data Science i skyen: Low Code - _Sketchnote af [@nitya](https://twitter.com/nitya)_ |

Indholdsfortegnelse:

- [Data Science i skyen: Den "Low code/No code" tilgang](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Quiz før lektionen](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [1. Introduktion](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [1.1 Hvad er Azure Machine Learning?](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [1.2 Projektet om forudsigelse af hjertesvigt:](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [1.3 Hjertesvigt-datasættet:](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [2. Low code/No code træning af en model i Azure ML Studio](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.1 Opret et Azure ML-arbejdsområde](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.2 Compute-ressourcer](../../../../5-Data-Science-In-Cloud/18-Low-Code)
      - [2.2.1 Valg af de rigtige muligheder for dine compute-ressourcer](../../../../5-Data-Science-In-Cloud/18-Low-Code)
      - [2.2.2 Oprettelse af en compute-klynge](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.3 Indlæsning af datasættet](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.4 Low code/No code træning med AutoML](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [3. Low code/No code modeludrulning og forbrug af endpoints](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [3.1 Modeludrulning](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [3.2 Forbrug af endpoints](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [🚀 Udfordring](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Quiz efter lektionen](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Gennemgang & Selvstudie](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Opgave](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  
## [Quiz før lektionen](https://ff-quizzes.netlify.app/en/ds/)

## 1. Introduktion
### 1.1 Hvad er Azure Machine Learning?

Azure cloud-platformen består af mere end 200 produkter og cloud-tjenester designet til at hjælpe dig med at bringe nye løsninger til live. Dataforskere bruger meget tid på at udforske og forbehandle data samt afprøve forskellige typer modeltræningsalgoritmer for at producere præcise modeller. Disse opgaver er tidskrævende og udnytter ofte dyr hardware ineffektivt.

[Azure ML](https://docs.microsoft.com/azure/machine-learning/overview-what-is-azure-machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) er en cloud-baseret platform til opbygning og drift af machine learning-løsninger i Azure. Den indeholder en bred vifte af funktioner og kapaciteter, der hjælper dataforskere med at forberede data, træne modeller, offentliggøre forudsigelsestjenester og overvåge deres brug. Mest vigtigt er, at den øger effektiviteten ved at automatisere mange af de tidskrævende opgaver, der er forbundet med modeltræning, og gør det muligt at bruge cloud-baserede compute-ressourcer, der skalerer effektivt til at håndtere store datamængder, mens omkostninger kun påløber, når de faktisk bruges.

Azure ML tilbyder alle de værktøjer, udviklere og dataforskere har brug for til deres machine learning-arbejdsgange. Disse inkluderer:

- **Azure Machine Learning Studio**: En webportal i Azure Machine Learning til low-code og no-code muligheder for modeltræning, udrulning, automatisering, sporing og asset management. Studio integreres med Azure Machine Learning SDK for en problemfri oplevelse.
- **Jupyter Notebooks**: Hurtig prototyping og test af ML-modeller.
- **Azure Machine Learning Designer**: Mulighed for at trække og slippe moduler for at opbygge eksperimenter og derefter udrulle pipelines i et low-code miljø.
- **Automated machine learning UI (AutoML)**: Automatiserer iterative opgaver i udviklingen af machine learning-modeller, hvilket gør det muligt at bygge ML-modeller med høj skala, effektivitet og produktivitet, samtidig med at modelkvaliteten opretholdes.
- **Data Labelling**: Et assisteret ML-værktøj til automatisk mærkning af data.
- **Machine learning extension for Visual Studio Code**: Tilbyder et fuldt udviklingsmiljø til opbygning og styring af ML-projekter.
- **Machine learning CLI**: Giver kommandoer til styring af Azure ML-ressourcer fra kommandolinjen.
- **Integration med open-source frameworks** som PyTorch, TensorFlow, Scikit-learn og mange flere til træning, udrulning og styring af den end-to-end machine learning-proces.
- **MLflow**: Et open-source bibliotek til styring af livscyklussen for dine machine learning-eksperimenter. **MLFlow Tracking** er en komponent af MLflow, der logger og sporer dine træningskørselsmetrikker og modelartefakter, uanset eksperimentets miljø.

### 1.2 Projektet om forudsigelse af hjertesvigt:

Der er ingen tvivl om, at opbygning af projekter er den bedste måde at teste dine færdigheder og viden på. I denne lektion vil vi udforske to forskellige måder at opbygge et data science-projekt til forudsigelse af hjertesvigt i Azure ML Studio, gennem Low code/No code og gennem Azure ML SDK som vist i følgende skema:

![projekt-skema](../../../../translated_images/project-schema.736f6e403f321eb48d10242b3f4334dc6ccf0eabef8ff87daf52b89781389fcb.da.png)

Hver metode har sine egne fordele og ulemper. Low code/No code-metoden er nemmere at starte med, da den involverer interaktion med en GUI (Graphical User Interface) uden behov for forudgående kendskab til kode. Denne metode gør det muligt hurtigt at teste projektets levedygtighed og skabe POC (Proof Of Concept). Men når projektet vokser, og tingene skal være produktionsklare, er det ikke praktisk at oprette ressourcer gennem GUI. Vi skal programmere og automatisere alt, fra oprettelse af ressourcer til udrulning af en model. Her bliver det afgørende at kunne bruge Azure ML SDK.

|                   | Low code/No code | Azure ML SDK              |
|-------------------|------------------|---------------------------|
| Ekspertise i kode | Ikke påkrævet    | Påkrævet                  |
| Udviklingstid     | Hurtig og nem    | Afhænger af kodeekspertise |
| Produktionsklar   | Nej              | Ja                        |

### 1.3 Hjertesvigt-datasættet:

Kardiovaskulære sygdomme (CVD'er) er den største dødsårsag globalt og står for 31% af alle dødsfald verden over. Miljømæssige og adfærdsmæssige risikofaktorer som tobaksbrug, usund kost og fedme, fysisk inaktivitet og skadelig brug af alkohol kan bruges som features i estimationsmodeller. At kunne estimere sandsynligheden for udviklingen af en CVD kan være meget nyttigt til at forebygge angreb hos personer med høj risiko.

Kaggle har gjort et [hjertesvigt-datasæt](https://www.kaggle.com/andrewmvd/heart-failure-clinical-data) offentligt tilgængeligt, som vi vil bruge til dette projekt. Du kan downloade datasættet nu. Det er et tabulært datasæt med 13 kolonner (12 features og 1 målvariabel) og 299 rækker.

|    | Variabelnavn              | Type            | Beskrivelse                                                | Eksempel          |
|----|---------------------------|-----------------|-----------------------------------------------------------|-------------------|
| 1  | age                       | numerisk        | Patientens alder                                          | 25                |
| 2  | anaemia                   | boolean         | Reduktion af røde blodlegemer eller hæmoglobin            | 0 eller 1         |
| 3  | creatinine_phosphokinase  | numerisk        | Niveau af CPK-enzym i blodet                              | 542               |
| 4  | diabetes                  | boolean         | Om patienten har diabetes                                 | 0 eller 1         |
| 5  | ejection_fraction         | numerisk        | Procentdel af blod, der forlader hjertet ved hver sammentrækning | 45                |
| 6  | high_blood_pressure       | boolean         | Om patienten har forhøjet blodtryk                        | 0 eller 1         |
| 7  | platelets                 | numerisk        | Blodplader i blodet                                       | 149000            |
| 8  | serum_creatinine          | numerisk        | Niveau af serumkreatinin i blodet                         | 0.5               |
| 9  | serum_sodium              | numerisk        | Niveau af serumnatrium i blodet                           | jun               |
| 10 | sex                       | boolean         | Kvinde eller mand                                         | 0 eller 1         |
| 11 | smoking                   | boolean         | Om patienten ryger                                        | 0 eller 1         |
| 12 | time                      | numerisk        | Opfølgningsperiode (dage)                                | 4                 |
|----|---------------------------|-----------------|-----------------------------------------------------------|-------------------|
| 21 | DEATH_EVENT [Målvariabel] | boolean         | Om patienten dør i opfølgningsperioden                   | 0 eller 1         |

Når du har datasættet, kan vi starte projektet i Azure.

## 2. Low code/No code træning af en model i Azure ML Studio
### 2.1 Opret et Azure ML-arbejdsområde
For at træne en model i Azure ML skal du først oprette et Azure ML-arbejdsområde. Arbejdsområdet er den øverste ressource for Azure Machine Learning og giver et centralt sted at arbejde med alle de artefakter, du opretter, når du bruger Azure Machine Learning. Arbejdsområdet holder styr på alle træningskørsler, inklusive logfiler, metrikker, output og en snapshot af dine scripts. Du bruger disse oplysninger til at afgøre, hvilken træningskørsel der producerer den bedste model. [Lær mere](https://docs.microsoft.com/azure/machine-learning/concept-workspace?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)

Det anbefales at bruge den mest opdaterede browser, der er kompatibel med dit operativsystem. Følgende browsere understøttes:

- Microsoft Edge (Den nye Microsoft Edge, seneste version. Ikke Microsoft Edge legacy)
- Safari (seneste version, kun Mac)
- Chrome (seneste version)
- Firefox (seneste version)

For at bruge Azure Machine Learning skal du oprette et arbejdsområde i din Azure-abonnement. Du kan derefter bruge dette arbejdsområde til at administrere data, compute-ressourcer, kode, modeller og andre artefakter relateret til dine machine learning-arbejdsbelastninger.

> **_NOTE:_** Dit Azure-abonnement vil blive opkrævet et mindre beløb for datalagring, så længe Azure Machine Learning-arbejdsområdet eksisterer i dit abonnement. Vi anbefaler derfor, at du sletter arbejdsområdet, når du ikke længere bruger det.

1. Log ind på [Azure-portalen](https://ms.portal.azure.com/) med de Microsoft-legitimationsoplysninger, der er knyttet til dit Azure-abonnement.
2. Vælg **＋Opret en ressource**
   
   ![arbejdsområde-1](../../../../translated_images/workspace-1.ac8694d60b073ed1ae8333d71244dc8a9b3e439d54593724f98f1beefdd27b08.da.png)

   Søg efter Machine Learning og vælg Machine Learning-flisen

   ![arbejdsområde-2](../../../../translated_images/workspace-2.ae7c486db8796147075e4a56566aa819827dd6c4c8d18d64590317c3be625f17.da.png)

   Klik på opret-knappen

   ![arbejdsområde-3](../../../../translated_images/workspace-3.398ca4a5858132cce584db9df10c5a011cd9075eb182e647a77d5cac01771eea.da.png)

   Udfyld indstillingerne som følger:
   - Abonnement: Dit Azure-abonnement
   - Ressourcegruppe: Opret eller vælg en ressourcegruppe
   - Arbejdsområdenavn: Indtast et unikt navn til dit arbejdsområde
   - Region: Vælg den geografiske region, der er tættest på dig
   - Lagringskonto: Bemærk den nye standardlagringskonto, der vil blive oprettet til dit arbejdsområde
   - Key vault: Bemærk den nye standard key vault, der vil blive oprettet til dit arbejdsområde
   - Application insights: Bemærk den nye standard Application Insights-ressource, der vil blive oprettet til dit arbejdsområde
   - Container registry: Ingen (en vil blive oprettet automatisk første gang du udruller en model til en container)

    ![arbejdsområde-4](../../../../translated_images/workspace-4.bac87f6599c4df63e624fc2608990f965887bee551d9dedc71c687b43b986b6a.da.png)

   - Klik på opret + gennemse og derefter på opret-knappen
3. Vent på, at dit arbejdsområde bliver oprettet (dette kan tage et par minutter). Gå derefter til det i portalen. Du kan finde det via Machine Learning Azure-tjenesten.
4. På oversigtssiden for dit arbejdsområde skal du starte Azure Machine Learning Studio (eller åbne en ny browserfane og navigere til https://ml.azure.com) og logge ind på Azure Machine Learning Studio med din Microsoft-konto. Hvis du bliver bedt om det, skal du vælge din Azure-directory og abonnement samt dit Azure Machine Learning-arbejdsområde.
   
![arbejdsområde-5](../../../../translated_images/workspace-5.a6eb17e0a5e6420018b08bdaf3755ce977f96f1df3ea363d2476a9dce7e15adb.da.png)

5. I Azure Machine Learning Studio skal du skifte ☰-ikonet øverst til venstre for at se de forskellige sider i grænsefladen. Du kan bruge disse sider til at administrere ressourcerne i dit arbejdsområde.

![arbejdsområde-6](../../../../translated_images/workspace-6.8dd81fe841797ee17f8f73916769576260b16c4e17e850d277a49db35fd74a15.da.png)

Du kan administrere dit arbejdsområde via Azure-portalen, men for dataforskere og Machine Learning operations-ingeniører giver Azure Machine Learning Studio en mere fokuseret brugergrænseflade til styring af arbejdsområderessourcer.

### 2.2 Compute-ressourcer

Compute-ressourcer er cloud-baserede ressourcer, hvor du kan køre modeltræning og dataudforskningsprocesser. Der er fire typer compute-ressourcer, du kan oprette:

- **Compute-instanser**: Udviklingsarbejdsstationer, som dataforskere kan bruge til at arbejde med data og modeller. Dette involverer oprettelse af en virtuel maskine (VM) og lancering af en notebook-instans. Du kan derefter træne en model ved at kalde en compute-klynge fra notebooken.
- **Compute-klynger**: Skalerbare klynger af VM'er til on-demand behandling af eksperimentkode. Du vil have brug for det, når du træner en model. Compute-klynger kan også anvende specialiserede GPU- eller CPU-ressourcer.
- **Inference-klynger**: Udrulningsmål for forudsigelsestjenester, der bruger dine trænede modeller.
- **Tilsluttet Compute**: Forbinder til eksisterende Azure compute-ressourcer, såsom virtuelle maskiner eller Azure Databricks-klynger.

#### 2.2.1 Valg af de rigtige muligheder for dine compute-ressourcer

Nogle vigtige faktorer skal overvejes, når du opretter en compute-ressource, og disse valg kan være afgørende beslutninger.

**Har du brug for CPU eller GPU?**

En CPU (Central Processing Unit) er den elektroniske kredsløbsenhed, der udfører instruktioner i et computerprogram. En GPU (Graphics Processing Unit) er et specialiseret elektronisk kredsløb, der kan udføre grafikrelateret kode med meget høj hastighed.

Den primære forskel mellem CPU- og GPU-arkitektur er, at en CPU er designet til hurtigt at håndtere en bred vifte af opgaver (målt ved CPU-klokkehastighed), men er begrænset i antallet af samtidige opgaver, der kan køre. GPU'er er designet til parallel computing og er derfor meget bedre til dyb læring-opgaver.

| CPU                                     | GPU                         |
|-----------------------------------------|-----------------------------|
| Mindre dyr                              | Mere dyr                   |
| Lavere niveau af samtidighed            | Højere niveau af samtidighed |
| Langsommere i træning af dyb læringsmodeller | Optimal til dyb læring      |

**Klynge Størrelse**

Større klynger er dyrere, men giver bedre responsivitet. Derfor, hvis du har tid, men ikke nok penge, bør du starte med en lille klynge. Omvendt, hvis du har penge, men ikke meget tid, bør du starte med en større klynge.

**VM Størrelse**

Afhængigt af dine tids- og budgetmæssige begrænsninger kan du variere størrelsen på din RAM, disk, antal kerner og klokkehastighed. At øge alle disse parametre vil være dyrere, men vil resultere i bedre ydeevne.

**Dedikerede eller Lav-prioritets Instanser?**

En lav-prioritets instans betyder, at den kan afbrydes: Microsoft Azure kan i princippet tage disse ressourcer og tildele dem til en anden opgave, hvilket afbryder et job. En dedikeret instans, eller ikke-afbrydelig, betyder, at jobbet aldrig vil blive afsluttet uden din tilladelse. Dette er endnu en overvejelse mellem tid og penge, da afbrydelige instanser er billigere end dedikerede.

#### 2.2.2 Oprettelse af en compute-klynge

I [Azure ML workspace](https://ml.azure.com/), som vi oprettede tidligere, gå til compute, og du vil kunne se de forskellige compute-ressourcer, vi lige har diskuteret (dvs. compute-instanser, compute-klynger, inferens-klynger og tilsluttet compute). Til dette projekt skal vi bruge en compute-klynge til modeltræning. I Studio skal du klikke på "Compute"-menuen, derefter fanen "Compute cluster" og klikke på "+ Ny"-knappen for at oprette en compute-klynge.

![22](../../../../translated_images/cluster-1.b78cb630bb543729b11f60c34d97110a263f8c27b516ba4dc47807b3cee5579f.da.png)

1. Vælg dine muligheder: Dedikeret vs Lav prioritet, CPU eller GPU, VM-størrelse og antal kerner (du kan beholde standardindstillingerne for dette projekt).
2. Klik på knappen Næste.

![23](../../../../translated_images/cluster-2.ea30cdbc9f926bb9e05af3fdbc1f679811c796dc2a6847f935290aec15526e88.da.png)

3. Giv klyngen et compute-navn.
4. Vælg dine muligheder: Minimum/Maksimum antal noder, Idle sekunder før nedskalering, SSH-adgang. Bemærk, at hvis minimumsantallet af noder er 0, vil du spare penge, når klyngen er inaktiv. Bemærk, at jo højere antallet af maksimale noder er, jo kortere vil træningen være. Det anbefalede maksimale antal noder er 3.  
5. Klik på "Opret"-knappen. Dette trin kan tage et par minutter.

![29](../../../../translated_images/cluster-3.8a334bc070ec173a329ce5abd2a9d727542e83eb2347676c9af20f2c8870b3e7.da.png)

Fantastisk! Nu hvor vi har en Compute-klynge, skal vi indlæse dataene til Azure ML Studio.

### 2.3 Indlæsning af datasættet

1. I [Azure ML workspace](https://ml.azure.com/), som vi oprettede tidligere, klik på "Datasæt" i venstre menu og klik på "+ Opret datasæt"-knappen for at oprette et datasæt. Vælg "Fra lokale filer"-muligheden og vælg det Kaggle-datasæt, vi downloadede tidligere.
   
   ![24](../../../../translated_images/dataset-1.e86ab4e10907a6e9c2a72577b51db35f13689cb33702337b8b7032f2ef76dac2.da.png)

2. Giv dit datasæt et navn, en type og en beskrivelse. Klik på Næste. Upload dataene fra filer. Klik på Næste.
   
   ![25](../../../../translated_images/dataset-2.f58de1c435d5bf9ccb16ccc5f5d4380eb2b50affca85cfbf4f97562bdab99f77.da.png)

3. I skemaet skal du ændre datatype til Boolean for følgende funktioner: anaemia, diabetes, high blood pressure, sex, smoking og DEATH_EVENT. Klik på Næste og klik på Opret.
   
   ![26](../../../../translated_images/dataset-3.58db8c0eb783e89236a02bbce5bb4ba808d081a87d994d5284b1ae59928c95bf.da.png)

Super! Nu hvor datasættet er på plads, og compute-klyngen er oprettet, kan vi begynde træningen af modellen!

### 2.4 Lav kode/Ingen kode træning med AutoML

Traditionel udvikling af maskinlæringsmodeller er ressourcekrævende, kræver betydelig domæneviden og tid til at producere og sammenligne dusinvis af modeller. 
Automatiseret maskinlæring (AutoML) er processen med at automatisere de tidskrævende, iterative opgaver i udviklingen af maskinlæringsmodeller. Det giver dataforskere, analytikere og udviklere mulighed for at bygge ML-modeller med høj skala, effektivitet og produktivitet, samtidig med at modelkvaliteten opretholdes. Det reducerer den tid, det tager at få produktionsklare ML-modeller, med stor lethed og effektivitet. [Lær mere](https://docs.microsoft.com/azure/machine-learning/concept-automated-ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)

1. I [Azure ML workspace](https://ml.azure.com/), som vi oprettede tidligere, klik på "Automated ML" i venstre menu og vælg det datasæt, du lige har uploadet. Klik på Næste.

   ![27](../../../../translated_images/aml-1.67281a85d3a1e2f34eb367b2d0f74e1039d13396e510f363cd8766632106d1ec.da.png)

2. Indtast et nyt eksperimentnavn, målkolonnen (DEATH_EVENT) og den compute-klynge, vi oprettede. Klik på Næste.
   
   ![28](../../../../translated_images/aml-2.c9fb9cffb39ccbbe21ab9810ae937195d41a489744e15cff2b8477ed4dcae1ec.da.png)

3. Vælg "Klassifikation" og klik på Udfør. Dette trin kan tage mellem 30 minutter og 1 time, afhængigt af størrelsen på din compute-klynge.
    
    ![30](../../../../translated_images/aml-3.a7952e4295f38cc6cdb0c7ed6dc71ea756b7fb5697ec126bc1220f87c5fa9231.da.png)

4. Når kørslen er færdig, klik på fanen "Automated ML", klik på din kørsel, og klik på algoritmen i kortet "Best model summary".
    
    ![31](../../../../translated_images/aml-4.7a627e09cb6f16d0aa246059d9faee3d1725cc4258d0c8df15e801f73afc7e2c.da.png)

Her kan du se en detaljeret beskrivelse af den bedste model, som AutoML genererede. Du kan også udforske andre modeller, der er genereret, i fanen Modeller. Brug et par minutter på at udforske modellerne i forklaringer (preview-knappen). Når du har valgt den model, du vil bruge (her vælger vi den bedste model, der er valgt af AutoML), vil vi se, hvordan vi kan implementere den.

## 3. Lav kode/Ingen kode modelimplementering og endpoint-forbrug
### 3.1 Modelimplementering

Den automatiserede maskinlæringsgrænseflade giver dig mulighed for at implementere den bedste model som en webtjeneste i nogle få trin. Implementering er integrationen af modellen, så den kan lave forudsigelser baseret på nye data og identificere potentielle muligheder. For dette projekt betyder implementering til en webtjeneste, at medicinske applikationer vil kunne bruge modellen til at lave live-forudsigelser af deres patienters risiko for at få et hjerteanfald.

I den bedste modelbeskrivelse skal du klikke på knappen "Deploy".
    
![deploy-1](../../../../translated_images/deploy-1.ddad725acadc84e34553c3d09e727160faeb32527a9fb8b904c0f99235a34bb6.da.png)

15. Giv den et navn, en beskrivelse, computertype (Azure Container Instance), aktiver godkendelse og klik på Deploy. Dette trin kan tage omkring 20 minutter at fuldføre. Implementeringsprocessen indebærer flere trin, herunder registrering af modellen, generering af ressourcer og konfiguration af dem til webtjenesten. En statusmeddelelse vises under Deploy-status. Vælg Opdater periodisk for at kontrollere implementeringsstatus. Det er implementeret og kører, når status er "Healthy".

![deploy-2](../../../../translated_images/deploy-2.94dbb13f239086473aa4bf814342fd40483d136849b080f02bafbb995383940e.da.png)

16. Når det er implementeret, skal du klikke på fanen Endpoint og klikke på det endpoint, du lige har implementeret. Her kan du finde alle de detaljer, du skal vide om endpointet.

![deploy-3](../../../../translated_images/deploy-3.fecefef070e8ef3b28e802326d107f61ac4e672d20bf82d05f78d025f9e6c611.da.png)

Fantastisk! Nu hvor vi har en model implementeret, kan vi begynde forbruget af endpointet.

### 3.2 Endpoint-forbrug

Klik på fanen "Consume". Her kan du finde REST-endpointet og et Python-script i forbrugsindstillingen. Brug lidt tid på at læse Python-koden.

Dette script kan køres direkte fra din lokale maskine og vil forbruge dit endpoint.

![35](../../../../translated_images/consumption-1.700abd196452842a020c7d745908637a6e4c5c50494ad1217be80e283e0de154.da.png)

Tag et øjeblik til at tjekke disse 2 linjer kode:

```python
url = 'http://98e3715f-xxxx-xxxx-xxxx-9ec22d57b796.centralus.azurecontainer.io/score'
api_key = '' # Replace this with the API key for the web service
```
Variablen `url` er REST-endpointet, der findes i fanen Consume, og variablen `api_key` er den primære nøgle, der også findes i fanen Consume (kun hvis du har aktiveret godkendelse). Dette er, hvordan scriptet kan forbruge endpointet.

18. Når du kører scriptet, bør du se følgende output:
    ```python
    b'"{\\"result\\": [true]}"'
    ```
Dette betyder, at forudsigelsen af hjertesvigt for de givne data er sand. Dette giver mening, fordi hvis du ser nærmere på de data, der automatisk genereres i scriptet, er alt sat til 0 og falsk som standard. Du kan ændre dataene med følgende inputeksempel:

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
Scriptet bør returnere:
    ```python
    b'"{\\"result\\": [true, false]}"'
    ```

Tillykke! Du har lige forbrugt den model, der blev implementeret og trænet på Azure ML!

> **_NOTE:_** Når du er færdig med projektet, skal du huske at slette alle ressourcer.
## 🚀 Udfordring

Se nærmere på model-forklaringerne og detaljerne, som AutoML genererede for de bedste modeller. Prøv at forstå, hvorfor den bedste model er bedre end de andre. Hvilke algoritmer blev sammenlignet? Hvad er forskellene mellem dem? Hvorfor klarer den bedste sig bedre i dette tilfælde?

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/)

## Gennemgang & Selvstudie

I denne lektion lærte du, hvordan du træner, implementerer og forbruger en model til at forudsige risikoen for hjertesvigt på en Lav kode/Ingen kode-måde i skyen. Hvis du ikke har gjort det endnu, så dyk dybere ned i model-forklaringerne, som AutoML genererede for de bedste modeller, og prøv at forstå, hvorfor den bedste model er bedre end de andre.

Du kan gå videre med Lav kode/Ingen kode AutoML ved at læse denne [dokumentation](https://docs.microsoft.com/azure/machine-learning/tutorial-first-experiment-automated-ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).

## Opgave

[Low code/No code Data Science projekt på Azure ML](assignment.md)

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.