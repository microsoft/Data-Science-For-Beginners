<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd4da10766c64fce4294a98f6479dfb0",
  "translation_date": "2025-09-05T17:42:30+00:00",
  "source_file": "5-Data-Science-In-Cloud/18-Low-Code/README.md",
  "language_code": "cs"
}
-->
# Data Science v cloudu: Cesta "Low code/No code"

|![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/18-DataScience-Cloud.png)|
|:---:|
| Data Science v cloudu: Low Code - _Sketchnote od [@nitya](https://twitter.com/nitya)_ |

Obsah:

- [Data Science v cloudu: Cesta "Low code/No code"](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Kvíz před lekcí](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [1. Úvod](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [1.1 Co je Azure Machine Learning?](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [1.2 Projekt predikce srdečního selhání:](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [1.3 Dataset srdečního selhání:](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [2. Trénování modelu v Azure ML Studio pomocí Low code/No code](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.1 Vytvoření pracovního prostoru Azure ML](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.2 Výpočetní zdroje](../../../../5-Data-Science-In-Cloud/18-Low-Code)
      - [2.2.1 Výběr správných možností pro vaše výpočetní zdroje](../../../../5-Data-Science-In-Cloud/18-Low-Code)
      - [2.2.2 Vytvoření výpočetního clusteru](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.3 Načtení datasetu](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.4 Trénování pomocí AutoML v režimu Low code/No code](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [3. Nasazení modelu a využití endpointu v režimu Low code/No code](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [3.1 Nasazení modelu](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [3.2 Využití endpointu](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [🚀 Výzva](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Kvíz po lekci](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Revize a samostudium](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Úkol](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  
## [Kvíz před lekcí](https://ff-quizzes.netlify.app/en/ds/quiz/34)

## 1. Úvod
### 1.1 Co je Azure Machine Learning?

Platforma Azure cloud zahrnuje více než 200 produktů a cloudových služeb navržených tak, aby vám pomohly přivést nové řešení k životu. Datoví vědci věnují značné úsilí průzkumu a předzpracování dat a zkoušení různých typů algoritmů pro trénování modelů, aby vytvořili přesné modely. Tyto úkoly jsou časově náročné a často neefektivně využívají drahý výpočetní hardware.

[Azure ML](https://docs.microsoft.com/azure/machine-learning/overview-what-is-azure-machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) je cloudová platforma pro vytváření a provozování řešení strojového učení v Azure. Nabízí širokou škálu funkcí a možností, které pomáhají datovým vědcům připravovat data, trénovat modely, publikovat prediktivní služby a monitorovat jejich využití. Největší výhodou je automatizace mnoha časově náročných úkolů spojených s trénováním modelů a možnost využívat cloudové výpočetní zdroje, které se efektivně škálují, aby zvládly velké objemy dat, přičemž náklady vznikají pouze při jejich skutečném využití.

Azure ML poskytuje všechny nástroje, které vývojáři a datoví vědci potřebují pro své pracovní postupy strojového učení. Patří sem:

- **Azure Machine Learning Studio**: webový portál v Azure Machine Learning pro možnosti trénování modelů, nasazení, automatizace, sledování a správy aktiv v režimu Low code/No code. Studio se integruje s Azure Machine Learning SDK pro bezproblémový zážitek.
- **Jupyter Notebooks**: rychlé prototypování a testování ML modelů.
- **Azure Machine Learning Designer**: umožňuje přetahování modulů pro vytváření experimentů a následné nasazení pipeline v prostředí Low code.
- **Automatizované uživatelské rozhraní strojového učení (AutoML)**: automatizuje iterativní úkoly vývoje modelů strojového učení, což umožňuje vytvářet ML modely s vysokou škálovatelností, efektivitou a produktivitou, přičemž je zachována kvalita modelu.
- **Označování dat**: asistovaný nástroj ML pro automatické označování dat.
- **Rozšíření strojového učení pro Visual Studio Code**: poskytuje plně vybavené vývojové prostředí pro vytváření a správu ML projektů.
- **CLI strojového učení**: poskytuje příkazy pro správu zdrojů Azure ML z příkazového řádku.
- **Integrace s open-source frameworky** jako PyTorch, TensorFlow, Scikit-learn a mnoho dalších pro trénování, nasazení a správu celého procesu strojového učení.
- **MLflow**: open-source knihovna pro správu životního cyklu vašich experimentů strojového učení. **MLFlow Tracking** je komponenta MLflow, která zaznamenává a sleduje metriky trénování a artefakty modelu bez ohledu na prostředí vašeho experimentu.

### 1.2 Projekt predikce srdečního selhání:

Není pochyb o tom, že vytváření projektů je nejlepší způsob, jak otestovat své dovednosti a znalosti. V této lekci prozkoumáme dva různé způsoby, jak vytvořit projekt datové vědy pro predikci srdečních selhání v Azure ML Studio, a to pomocí Low code/No code a pomocí Azure ML SDK, jak je znázorněno na následujícím schématu:

![project-schema](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/project-schema.PNG)

Každý způsob má své výhody a nevýhody. Cesta Low code/No code je jednodušší na začátek, protože zahrnuje práci s grafickým uživatelským rozhraním (GUI) bez nutnosti předchozích znalostí kódu. Tento způsob umožňuje rychlé testování životaschopnosti projektu a vytvoření POC (Proof Of Concept). Jakmile však projekt roste a je potřeba jej připravit na produkční prostředí, není možné vytvářet zdroje pouze prostřednictvím GUI. Je nutné vše programově automatizovat, od vytvoření zdrojů až po nasazení modelu. Zde se stává klíčovým umět používat Azure ML SDK.

|                   | Low code/No code | Azure ML SDK              |
|-------------------|------------------|---------------------------|
| Znalost kódu      | Není nutná       | Nutná                     |
| Doba vývoje       | Rychlá a snadná  | Závisí na znalostech kódu |
| Připravenost na produkci | Ne         | Ano                       |

### 1.3 Dataset srdečního selhání: 

Kardiovaskulární onemocnění (CVD) jsou hlavní příčinou úmrtí na celém světě, představují 31 % všech úmrtí. Environmentální a behaviorální rizikové faktory, jako je užívání tabáku, nezdravá strava a obezita, fyzická nečinnost a škodlivé užívání alkoholu, mohou být použity jako vlastnosti pro odhadové modely. Schopnost odhadnout pravděpodobnost vývoje CVD by mohla být velmi užitečná pro prevenci útoků u lidí s vysokým rizikem.

Kaggle zpřístupnil veřejně [dataset srdečního selhání](https://www.kaggle.com/andrewmvd/heart-failure-clinical-data), který použijeme pro tento projekt. Dataset si můžete stáhnout nyní. Jedná se o tabulkový dataset s 13 sloupci (12 vlastností a 1 cílová proměnná) a 299 řádky. 

|    | Název proměnné            | Typ             | Popis                                                    | Příklad           |
|----|---------------------------|-----------------|----------------------------------------------------------|-------------------|
| 1  | age                       | numerický       | věk pacienta                                             | 25                |
| 2  | anaemia                   | boolean         | Snížení počtu červených krvinek nebo hemoglobinu         | 0 nebo 1          |
| 3  | creatinine_phosphokinase  | numerický       | Hladina enzymu CPK v krvi                                | 542               |
| 4  | diabetes                  | boolean         | Zda má pacient diabetes                                  | 0 nebo 1          |
| 5  | ejection_fraction         | numerický       | Procento krve opouštějící srdce při každé kontrakci      | 45                |
| 6  | high_blood_pressure       | boolean         | Zda má pacient hypertenzi                                | 0 nebo 1          |
| 7  | platelets                 | numerický       | Počet krevních destiček v krvi                           | 149000            |
| 8  | serum_creatinine          | numerický       | Hladina sérového kreatininu v krvi                       | 0.5               |
| 9  | serum_sodium              | numerický       | Hladina sérového sodíku v krvi                           | jun               |
| 10 | sex                       | boolean         | žena nebo muž                                            | 0 nebo 1          |
| 11 | smoking                   | boolean         | Zda pacient kouří                                        | 0 nebo 1          |
| 12 | time                      | numerický       | období sledování (dny)                                   | 4                 |
|----|---------------------------|-----------------|----------------------------------------------------------|-------------------|
| 21 | DEATH_EVENT [Cíl]         | boolean         | zda pacient zemře během období sledování                 | 0 nebo 1          |

Jakmile máte dataset, můžeme začít projekt v Azure.

## 2. Trénování modelu v Azure ML Studio pomocí Low code/No code
### 2.1 Vytvoření pracovního prostoru Azure ML
Pro trénování modelu v Azure ML je nejprve nutné vytvořit pracovní prostor Azure ML. Pracovní prostor je nejvyšší úroveň zdroje pro Azure Machine Learning, která poskytuje centralizované místo pro práci se všemi artefakty, které vytvoříte při používání Azure Machine Learning. Pracovní prostor uchovává historii všech trénovacích běhů, včetně logů, metrik, výstupů a snímků vašich skriptů. Tyto informace využíváte k určení, který trénovací běh produkuje nejlepší model. [Zjistěte více](https://docs.microsoft.com/azure/machine-learning/concept-workspace?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)

Doporučuje se používat nejaktuálnější prohlížeč kompatibilní s vaším operačním systémem. Podporované prohlížeče jsou:

- Microsoft Edge (nový Microsoft Edge, nejnovější verze. Ne Microsoft Edge legacy)
- Safari (nejnovější verze, pouze Mac)
- Chrome (nejnovější verze)
- Firefox (nejnovější verze)

Pro použití Azure Machine Learning vytvořte pracovní prostor ve svém předplatném Azure. Tento pracovní prostor pak můžete použít ke správě dat, výpočetních zdrojů, kódu, modelů a dalších artefaktů souvisejících s vašimi pracovními postupy strojového učení.

> **_POZNÁMKA:_** Vaše předplatné Azure bude účtováno malou částkou za úložiště dat, dokud pracovní prostor Azure Machine Learning existuje ve vašem předplatném, takže doporučujeme pracovní prostor Azure Machine Learning smazat, když jej již nebudete používat.

1. Přihlaste se do [Azure portálu](https://ms.portal.azure.com/) pomocí Microsoft přihlašovacích údajů spojených s vaším předplatným Azure.
2. Vyberte **＋Vytvořit zdroj**
   
   ![workspace-1](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-1.PNG)

   Vyhledejte Machine Learning a vyberte dlaždici Machine Learning

   ![workspace-2](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-2.PNG)

   Klikněte na tlačítko vytvořit

   ![workspace-3](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-3.PNG)

   Vyplňte nastavení následovně:
   - Předplatné: Vaše předplatné Azure
   - Skupina zdrojů: Vytvořte nebo vyberte skupinu zdrojů
   - Název pracovního prostoru: Zadejte jedinečný název pro váš pracovní prostor
   - Region: Vyberte geografický region nejblíže k vám
   - Účet úložiště: Poznamenejte si výchozí nový účet úložiště, který bude vytvořen pro váš pracovní prostor
   - Key vault: Poznamenejte si výchozí nový key vault, který bude vytvořen pro váš pracovní prostor
   - Application insights: Poznamenejte si výchozí nový zdroj Application Insights, který bude vytvořen pro váš pracovní prostor
   - Container registry: Žádný (bude vytvořen automaticky při prvním nasazení modelu do kontejneru)

    ![workspace-4](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-4.PNG)

   - Klikněte na vytvořit + recenze a poté na tlačítko vytvořit
3. Počkejte, až bude váš pracovní prostor vytvořen (může to trvat několik minut). Poté do něj přejděte v portálu. Najdete jej prostřednictvím služby Machine Learning Azure.
4. Na stránce Přehled vašeho pracovního prostoru spusťte Azure Machine Learning studio (nebo otevřete novou kartu prohlížeče a přejděte na https://ml.azure.com) a přihlaste se do Azure Machine Learning studio pomocí svého Microsoft účtu. Pokud budete vyzváni, vyberte svůj Azure adresář a předplatné a svůj pracovní prostor Azure Machine Learning.
   
![workspace-5](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-5.PNG)

5. V Azure Machine Learning studio přepněte ikonu ☰ v levém horním rohu, abyste si zobrazili různé stránky v rozhraní. Tyto stránky můžete použít ke správě zdrojů ve vašem pracovním prostoru.

![workspace-6](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-6.PNG)

Pracovní prostor můžete spravovat pomocí Azure portálu, ale pro datové vědce a inženýry operací strojového učení poskytuje Azure Machine Learning Studio více zaměřené uživatelské rozhraní pro správu zdrojů pracovního prostoru.

### 2.2 Výpočetní zdroje

Výpočetní zdroje jsou cloudové zdroje, na kterých můžete spouštět procesy trénování modelů a průzkumu dat. Existují čtyři druhy výpočetních zdrojů, které můžete vytvořit:

- **Výpočetní instance**: Vývojové pracovní stanice, které mohou datoví vědci používat k práci s daty a modely. To zahrnuje vytvoření virtuálního stroje (VM) a spuštění instance notebooku. Poté můžete trénovat model voláním výpočetního clusteru z notebooku.
- **Výpočetní clustery**: Škálovatelné clustery VM pro zpracování experimentálního kódu na vyžádání. Budete je potřebovat při trénování modelu. Výpočetní clustery mohou také využívat specializované GPU nebo CPU zdroje.
- **Inference clustery**: Cíle nasazení pro prediktivní služby, které využívají vaše trénované modely.
- **Připojené výpočetní prostředky**: Odkazy na existující výpočetní prostředky Azure, jako jsou virtuální počítače nebo clustery Azure Databricks.

#### 2.2.1 Výběr správných možností pro vaše výpočetní prostředky

Při vytváření výpočetního prostředku je třeba zvážit několik klíčových faktorů, které mohou být zásadními rozhodnutími.

**Potřebujete CPU nebo GPU?**

CPU (Central Processing Unit) je elektronický obvod, který provádí instrukce tvořící počítačový program. GPU (Graphics Processing Unit) je specializovaný elektronický obvod, který dokáže provádět graficky orientovaný kód velmi rychle.

Hlavní rozdíl mezi architekturou CPU a GPU je v tom, že CPU je navrženo pro rychlé zpracování široké škály úkolů (měřeno rychlostí hodin CPU), ale má omezenou schopnost paralelního zpracování. GPU je navrženo pro paralelní výpočty, a proto je mnohem lepší pro úlohy hlubokého učení.

| CPU                                     | GPU                         |
|-----------------------------------------|-----------------------------|
| Méně nákladné                          | Více nákladné              |
| Nižší úroveň paralelismu               | Vyšší úroveň paralelismu   |
| Pomalejší při trénování modelů hlubokého učení | Optimální pro hluboké učení |

**Velikost clusteru**

Větší clustery jsou dražší, ale poskytují lepší odezvu. Pokud máte čas, ale omezený rozpočet, měli byste začít s malým clusterem. Naopak, pokud máte peníze, ale málo času, měli byste začít s větším clusterem.

**Velikost virtuálního počítače**

V závislosti na vašich časových a rozpočtových omezeních můžete měnit velikost RAM, disku, počet jader a rychlost hodin. Zvýšení všech těchto parametrů bude dražší, ale povede k lepšímu výkonu.

**Dedikované nebo nízko-prioritní instance?**

Nízko-prioritní instance znamená, že je přerušitelná: Microsoft Azure může tyto prostředky převzít a přiřadit je jinému úkolu, čímž přeruší běžící úlohu. Dedikovaná instance, nebo nepřerušitelná, znamená, že úloha nebude nikdy ukončena bez vašeho svolení. Toto je další úvaha mezi časem a penězi, protože přerušitelné instance jsou levnější než dedikované.

#### 2.2.2 Vytvoření výpočetního clusteru

V [Azure ML workspace](https://ml.azure.com/), který jsme vytvořili dříve, přejděte na výpočetní prostředky a uvidíte různé výpočetní prostředky, o kterých jsme právě diskutovali (tj. výpočetní instance, výpočetní clustery, inference clustery a připojené výpočetní prostředky). Pro tento projekt budeme potřebovat výpočetní cluster pro trénování modelu. Ve Studio klikněte na nabídku "Compute", poté na záložku "Compute cluster" a klikněte na tlačítko "+ New" pro vytvoření výpočetního clusteru.

![22](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/cluster-1.PNG)

1. Vyberte své možnosti: Dedikované vs nízko-prioritní, CPU nebo GPU, velikost virtuálního počítače a počet jader (pro tento projekt můžete ponechat výchozí nastavení).
2. Klikněte na tlačítko Next.

![23](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/cluster-2.PNG)

3. Pojmenujte cluster.
4. Vyberte své možnosti: Minimální/maximální počet uzlů, počet nečinných sekund před zmenšením, přístup SSH. Všimněte si, že pokud je minimální počet uzlů 0, ušetříte peníze, když je cluster nečinný. Všimněte si, že čím vyšší je počet maximálních uzlů, tím kratší bude trénování. Doporučený maximální počet uzlů je 3.  
5. Klikněte na tlačítko "Create". Tento krok může trvat několik minut.

![29](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/cluster-3.PNG)

Skvělé! Nyní, když máme výpočetní cluster, musíme nahrát data do Azure ML Studio.

### 2.3 Nahrání datasetu

1. V [Azure ML workspace](https://ml.azure.com/), který jsme vytvořili dříve, klikněte na "Datasets" v levém menu a klikněte na tlačítko "+ Create dataset" pro vytvoření datasetu. Vyberte možnost "From local files" a vyberte dataset Kaggle, který jsme stáhli dříve.
   
   ![24](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/dataset-1.PNG)

2. Pojmenujte dataset, zadejte typ a popis. Klikněte na Next. Nahrajte data ze souborů. Klikněte na Next.
   
   ![25](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/dataset-2.PNG)

3. Ve schématu změňte datový typ na Boolean pro následující atributy: anaemia, diabetes, high blood pressure, sex, smoking a DEATH_EVENT. Klikněte na Next a poté na Create.
   
   ![26](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/dataset-3.PNG)

Skvělé! Nyní, když je dataset na místě a výpočetní cluster je vytvořen, můžeme začít trénovat model!

### 2.4 Trénování s nízkým kódem/bez kódu pomocí AutoML

Tradiční vývoj modelů strojového učení je náročný na zdroje, vyžaduje značné odborné znalosti a čas na vytvoření a porovnání desítek modelů. Automatizované strojové učení (AutoML) je proces automatizace časově náročných, iterativních úkolů vývoje modelů strojového učení. Umožňuje datovým vědcům, analytikům a vývojářům vytvářet modely ML s vysokou škálovatelností, efektivitou a produktivitou, přičemž zachovává kvalitu modelu. Snižuje čas potřebný k získání modelů ML připravených pro produkci, s velkou lehkostí a efektivitou. [Více informací](https://docs.microsoft.com/azure/machine-learning/concept-automated-ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)

1. V [Azure ML workspace](https://ml.azure.com/), který jsme vytvořili dříve, klikněte na "Automated ML" v levém menu a vyberte dataset, který jste právě nahráli. Klikněte na Next.

   ![27](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/aml-1.PNG)

2. Zadejte nový název experimentu, cílový sloupec (DEATH_EVENT) a výpočetní cluster, který jsme vytvořili. Klikněte na Next.
   
   ![28](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/aml-2.PNG)

3. Vyberte "Classification" a klikněte na Finish. Tento krok může trvat mezi 30 minutami až 1 hodinou, v závislosti na velikosti vašeho výpočetního clusteru.
    
    ![30](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/aml-3.PNG)

4. Jakmile je běh dokončen, klikněte na záložku "Automated ML", klikněte na svůj běh a klikněte na algoritmus v kartě "Best model summary".
    
    ![31](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/aml-4.PNG)

Zde můžete vidět podrobný popis nejlepšího modelu, který AutoML vytvořil. Můžete také prozkoumat další modely v záložce Models. Věnujte několik minut prozkoumání modelů v sekci Explanations (preview button). Jakmile si vyberete model, který chcete použít (zde vybereme nejlepší model vybraný AutoML), podíváme se, jak jej můžeme nasadit.

## 3. Nasazení modelu s nízkým kódem/bez kódu a spotřeba endpointu
### 3.1 Nasazení modelu

Rozhraní automatizovaného strojového učení umožňuje nasadit nejlepší model jako webovou službu v několika krocích. Nasazení je integrace modelu tak, aby mohl provádět predikce na základě nových dat a identifikovat potenciální oblasti příležitostí. Pro tento projekt nasazení na webovou službu znamená, že lékařské aplikace budou schopny využívat model k provádění živých predikcí rizika srdečního infarktu u pacientů.

V popisu nejlepšího modelu klikněte na tlačítko "Deploy".
    
![deploy-1](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/deploy-1.PNG)

15. Zadejte název, popis, typ výpočtu (Azure Container Instance), povolte autentizaci a klikněte na Deploy. Tento krok může trvat asi 20 minut. Proces nasazení zahrnuje několik kroků, včetně registrace modelu, generování prostředků a jejich konfigurace pro webovou službu. Stavová zpráva se objeví pod stavem nasazení. Pravidelně klikněte na Refresh pro kontrolu stavu nasazení. Je nasazen a běží, když je stav "Healthy".

![deploy-2](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/deploy-2.PNG)

16. Jakmile je nasazen, klikněte na záložku Endpoint a klikněte na endpoint, který jste právě nasadili. Zde najdete všechny podrobnosti, které potřebujete vědět o endpointu.

![deploy-3](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/deploy-3.PNG)

Úžasné! Nyní, když máme model nasazený, můžeme začít spotřebovávat endpoint.

### 3.2 Spotřeba endpointu

Klikněte na záložku "Consume". Zde najdete REST endpoint a python skript v možnosti spotřeby. Věnujte chvíli čtení python kódu.

Tento skript lze spustit přímo z vašeho lokálního počítače a bude spotřebovávat váš endpoint.

![35](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/consumption-1.PNG)

Věnujte chvíli pozornost těmto dvěma řádkům kódu:

```python
url = 'http://98e3715f-xxxx-xxxx-xxxx-9ec22d57b796.centralus.azurecontainer.io/score'
api_key = '' # Replace this with the API key for the web service
```
Proměnná `url` je REST endpoint nalezený v záložce consume a proměnná `api_key` je primární klíč také nalezený v záložce consume (pouze v případě, že jste povolili autentizaci). Takto skript může spotřebovávat endpoint.

18. Při spuštění skriptu byste měli vidět následující výstup:
    ```python
    b'"{\\"result\\": [true]}"'
    ```
To znamená, že predikce srdečního selhání pro zadaná data je pravdivá. To dává smysl, protože pokud se podíváte blíže na data automaticky generovaná ve skriptu, vše je ve výchozím nastavení na 0 a false. Můžete změnit data na následující vzorový vstup:

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
Skript by měl vrátit:
    ```python
    b'"{\\"result\\": [true, false]}"'
    ```

Gratulujeme! Právě jste spotřebovali nasazený model a trénovali jej na Azure ML!

> **_POZNÁMKA:_** Jakmile dokončíte projekt, nezapomeňte smazat všechny prostředky.
## 🚀 Výzva

Podívejte se podrobně na vysvětlení modelu a detaily, které AutoML vytvořil pro nejlepší modely. Pokuste se pochopit, proč je nejlepší model lepší než ostatní. Jaké algoritmy byly porovnány? Jaké jsou mezi nimi rozdíly? Proč je nejlepší model v tomto případě výkonnější?

## [Kvíz po přednášce](https://ff-quizzes.netlify.app/en/ds/quiz/35)

## Přehled & Samostudium

V této lekci jste se naučili, jak trénovat, nasazovat a spotřebovávat model pro predikci rizika srdečního selhání s nízkým kódem/bez kódu v cloudu. Pokud jste to ještě neudělali, ponořte se hlouběji do vysvětlení modelu, které AutoML vytvořil pro nejlepší modely, a pokuste se pochopit, proč je nejlepší model lepší než ostatní.

Můžete se dále ponořit do AutoML s nízkým kódem/bez kódu přečtením této [dokumentace](https://docs.microsoft.com/azure/machine-learning/tutorial-first-experiment-automated-ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).

## Zadání

[Projekt Data Science s nízkým kódem/bez kódu na Azure ML](assignment.md)

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádné nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.