<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "39f3b3a9d873eaa522c2e792ce0ca503",
  "translation_date": "2025-09-04T21:50:40+00:00",
  "source_file": "5-Data-Science-In-Cloud/18-Low-Code/README.md",
  "language_code": "hr"
}
-->
# Data Science u oblaku: "Low code/No code" pristup

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/18-DataScience-Cloud.png)|
|:---:|
| Data Science u oblaku: Low Code - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Sadržaj:

- [Data Science u oblaku: "Low code/No code" pristup](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Pre-ispitni kviz](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [1. Uvod](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [1.1 Što je Azure Machine Learning?](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [1.2 Projekt predviđanja srčanog zatajenja:](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [1.3 Skup podataka o srčanom zatajenju:](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [2. Low code/No code treniranje modela u Azure ML Studio](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.1 Kreiranje Azure ML radnog prostora](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.2 Resursi za računalnu obradu](../../../../5-Data-Science-In-Cloud/18-Low-Code)
      - [2.2.1 Odabir pravih opcija za resurse za računalnu obradu](../../../../5-Data-Science-In-Cloud/18-Low-Code)
      - [2.2.2 Kreiranje klastera za računalnu obradu](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.3 Učitavanje skupa podataka](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.4 Low code/No Code treniranje s AutoML](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [3. Low code/No Code implementacija modela i korištenje krajnjih točaka](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [3.1 Implementacija modela](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [3.2 Korištenje krajnjih točaka](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [🚀 Izazov](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Post-ispitni kviz](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Pregled i samostalno učenje](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Zadatak](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  
## [Pre-ispitni kviz](https://ff-quizzes.netlify.app/en/ds/)

## 1. Uvod
### 1.1 Što je Azure Machine Learning?

Azure cloud platforma obuhvaća više od 200 proizvoda i usluga u oblaku osmišljenih kako bi vam pomogli u stvaranju novih rješenja. Data znanstvenici troše puno vremena na istraživanje i predobradu podataka te isprobavanje različitih algoritama za treniranje modela kako bi proizveli točne modele. Ovi zadaci su vremenski zahtjevni i često neefikasno koriste skupe računalne resurse.

[Azure ML](https://docs.microsoft.com/azure/machine-learning/overview-what-is-azure-machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) je platforma u oblaku za izgradnju i upravljanje rješenjima za strojno učenje u Azureu. Pruža širok raspon značajki koje pomažu data znanstvenicima u pripremi podataka, treniranju modela, objavljivanju prediktivnih usluga i praćenju njihove upotrebe. Najvažnije, povećava njihovu učinkovitost automatizacijom mnogih vremenski zahtjevnih zadataka povezanih s treniranjem modela te omogućuje korištenje računalnih resursa u oblaku koji se skaliraju kako bi obradili velike količine podataka, uz troškove samo kada se resursi stvarno koriste.

Azure ML pruža sve alate potrebne za radne procese strojnog učenja, uključujući:

- **Azure Machine Learning Studio**: web portal u Azure Machine Learningu za opcije s malo ili bez koda za treniranje modela, implementaciju, automatizaciju, praćenje i upravljanje resursima. Studio se integrira s Azure Machine Learning SDK-om za besprijekorno iskustvo.
- **Jupyter Notebooks**: brzo prototipiranje i testiranje ML modela.
- **Azure Machine Learning Designer**: omogućuje povlačenje i ispuštanje modula za izgradnju eksperimenata i implementaciju cjevovoda u okruženju s malo koda.
- **Automatizirani UI za strojno učenje (AutoML)**: automatizira iterativne zadatke razvoja ML modela, omogućujući izgradnju modela s visokom skalabilnošću, učinkovitošću i produktivnošću, uz održavanje kvalitete modela.
- **Označavanje podataka**: alat za asistirano ML označavanje podataka.
- **Ekstenzija za strojno učenje u Visual Studio Codeu**: pruža potpuno opremljeno razvojno okruženje za izgradnju i upravljanje ML projektima.
- **CLI za strojno učenje**: omogućuje upravljanje resursima Azure ML-a putem naredbenog retka.
- **Integracija s open-source okvirima** poput PyTorch, TensorFlow, Scikit-learn i mnogih drugih za treniranje, implementaciju i upravljanje procesom strojnog učenja od početka do kraja.
- **MLflow**: otvorena biblioteka za upravljanje životnim ciklusom vaših eksperimenata strojnog učenja. **MLFlow Tracking** je komponenta MLflowa koja bilježi i prati metrike vaših treninga i artefakte modela, bez obzira na okruženje vašeg eksperimenta.

### 1.2 Projekt predviđanja srčanog zatajenja:

Nema sumnje da je izrada projekata najbolji način za testiranje vaših vještina i znanja. U ovoj lekciji istražit ćemo dva različita načina izrade projekta za predviđanje srčanog zatajenja u Azure ML Studio, kroz Low code/No code pristup i kroz Azure ML SDK, kao što je prikazano u sljedećem shematskom prikazu:

![project-schema](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/project-schema.PNG)

Svaki način ima svoje prednosti i nedostatke. Low code/No code pristup je lakši za početak jer uključuje interakciju s grafičkim korisničkim sučeljem (GUI), bez potrebe za prethodnim znanjem kodiranja. Ova metoda omogućuje brzo testiranje izvedivosti projekta i stvaranje POC-a (Proof Of Concept). Međutim, kako projekt raste i postaje spreman za produkciju, nije izvedivo stvarati resurse putem GUI-ja. Potrebno je programatski automatizirati sve, od stvaranja resursa do implementacije modela. Tu postaje ključno znanje o korištenju Azure ML SDK-a.

|                   | Low code/No code | Azure ML SDK              |
|-------------------|------------------|---------------------------|
| Znanje kodiranja  | Nije potrebno    | Potrebno                  |
| Vrijeme razvoja   | Brzo i jednostavno | Ovisi o znanju kodiranja |
| Spremnost za produkciju | Ne               | Da                       |

### 1.3 Skup podataka o srčanom zatajenju:

Kardiovaskularne bolesti (CVD) su vodeći uzrok smrti u svijetu, odgovorne za 31% svih smrti globalno. Ekološki i ponašajni čimbenici rizika poput upotrebe duhana, nezdrave prehrane i pretilosti, tjelesne neaktivnosti i štetne upotrebe alkohola mogu se koristiti kao značajke za modele procjene. Mogućnost procjene vjerojatnosti razvoja CVD-a mogla bi biti od velike koristi za prevenciju napada kod osoba visokog rizika.

Kaggle je učinio [skup podataka o srčanom zatajenju](https://www.kaggle.com/andrewmvd/heart-failure-clinical-data) javno dostupnim, koji ćemo koristiti za ovaj projekt. Možete ga preuzeti sada. Ovo je tablični skup podataka s 13 stupaca (12 značajki i 1 ciljana varijabla) i 299 redaka.

|    | Naziv varijable           | Tip             | Opis                                                      | Primjer           |
|----|---------------------------|-----------------|-----------------------------------------------------------|-------------------|
| 1  | age                       | numerički       | dob pacijenta                                             | 25                |
| 2  | anaemia                   | logički         | Smanjenje crvenih krvnih stanica ili hemoglobina          | 0 ili 1           |
| 3  | creatinine_phosphokinase  | numerički       | Razina CPK enzima u krvi                                  | 542               |
| 4  | diabetes                  | logički         | Ima li pacijent dijabetes                                 | 0 ili 1           |
| 5  | ejection_fraction         | numerički       | Postotak krvi koja napušta srce pri svakoj kontrakciji    | 45                |
| 6  | high_blood_pressure       | logički         | Ima li pacijent hipertenziju                              | 0 ili 1           |
| 7  | platelets                 | numerički       | Trombociti u krvi                                         | 149000            |
| 8  | serum_creatinine          | numerički       | Razina serumskog kreatinina u krvi                        | 0.5               |
| 9  | serum_sodium              | numerički       | Razina serumskog natrija u krvi                           | jun               |
| 10 | sex                       | logički         | žena ili muškarac                                         | 0 ili 1           |
| 11 | smoking                   | logički         | Puši li pacijent                                          | 0 ili 1           |
| 12 | time                      | numerički       | razdoblje praćenja (dani)                                 | 4                 |
|----|---------------------------|-----------------|-----------------------------------------------------------|-------------------|
| 21 | DEATH_EVENT [Cilj]        | logički         | Umire li pacijent tijekom razdoblja praćenja              | 0 ili 1           |

Nakon što preuzmete skup podataka, možemo započeti projekt u Azureu.

## 2. Low code/No code treniranje modela u Azure ML Studio
### 2.1 Kreiranje Azure ML radnog prostora
Za treniranje modela u Azure ML-u prvo morate kreirati Azure ML radni prostor. Radni prostor je glavni resurs za Azure Machine Learning, koji pruža centralizirano mjesto za rad sa svim artefaktima koje kreirate kada koristite Azure Machine Learning. Radni prostor čuva povijest svih treninga, uključujući zapise, metrike, izlaz i snimke vaših skripti. Koristite ove informacije kako biste odredili koji trening daje najbolji model. [Saznajte više](https://docs.microsoft.com/azure/machine-learning/concept-workspace?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)

Preporučuje se korištenje najnovijeg preglednika kompatibilnog s vašim operativnim sustavom. Podržani su sljedeći preglednici:

- Microsoft Edge (novi Microsoft Edge, najnovija verzija. Ne Microsoft Edge legacy)
- Safari (najnovija verzija, samo Mac)
- Chrome (najnovija verzija)
- Firefox (najnovija verzija)

Za korištenje Azure Machine Learninga, kreirajte radni prostor u svojoj Azure pretplati. Zatim možete koristiti ovaj radni prostor za upravljanje podacima, resursima za računalnu obradu, kodom, modelima i drugim artefaktima povezanim s vašim radnim procesima strojnog učenja.

> **_NAPOMENA:_** Vaša Azure pretplata će biti naplaćena malim iznosom za pohranu podataka dok Azure Machine Learning radni prostor postoji u vašoj pretplati, pa preporučujemo da izbrišete radni prostor kada ga više ne koristite.

1. Prijavite se na [Azure portal](https://ms.portal.azure.com/) koristeći Microsoft vjerodajnice povezane s vašom Azure pretplatom.
2. Odaberite **＋Kreiraj resurs**
   
   ![workspace-1](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-1.PNG)

   Potražite Machine Learning i odaberite pločicu Machine Learning

   ![workspace-2](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-2.PNG)

   Kliknite na gumb za kreiranje

   ![workspace-3](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-3.PNG)

   Ispunite postavke kako slijedi:
   - Pretplata: Vaša Azure pretplata
   - Grupa resursa: Kreirajte ili odaberite grupu resursa
   - Naziv radnog prostora: Unesite jedinstveni naziv za vaš radni prostor
   - Regija: Odaberite geografsku regiju najbližu vama
   - Račun za pohranu: Zabilježite zadani novi račun za pohranu koji će biti kreiran za vaš radni prostor
   - Key vault: Zabilježite zadani novi key vault koji će biti kreiran za vaš radni prostor
   - Application insights: Zabilježite zadani novi resurs za application insights koji će biti kreiran za vaš radni prostor
   - Registry za kontejnere: Nijedan (jedan će biti automatski kreiran prvi put kada implementirate model u kontejner)

    ![workspace-4](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-4.PNG)

   - Kliknite na gumb za pregled i kreiranje, a zatim na gumb za kreiranje
3. Pričekajte da se vaš radni prostor kreira (to može potrajati nekoliko minuta). Zatim idite na njega u portalu. Možete ga pronaći putem Azure Machine Learning usluge.
4. Na stranici Pregled za vaš radni prostor, pokrenite Azure Machine Learning studio (ili otvorite novu karticu preglednika i idite na https://ml.azure.com), i prijavite se u Azure Machine Learning studio koristeći svoj Microsoft račun. Ako se od vas zatraži, odaberite svoj Azure direktorij i pretplatu te svoj Azure Machine Learning radni prostor.
   
![workspace-5](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-5.PNG)

5. U Azure Machine Learning studiju, prebacite ☰ ikonu u gornjem lijevom kutu kako biste vidjeli različite stranice u sučelju. Možete koristiti ove stranice za upravljanje resursima u vašem radnom prostoru.

![workspace-6](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-6.PNG)

Možete upravljati svojim radnim prostorom koristeći Azure portal, ali za data znanstvenike i inženjere operacija strojnog učenja, Azure Machine Learning Studio pruža fokusiranije korisničko sučelje za upravljanje resursima radnog prostora.

### 2.2 Resursi za računalnu obradu

Resursi za računalnu obradu su resursi u oblaku na kojima možete pokretati procese treniranja modela i istraživanja podataka. Postoje četiri vrste resursa za računalnu obradu koje možete kreirati:

- **Instancije za računalnu obradu**: Radne stanice za razvoj koje data znanstvenici mogu koristiti za rad s podacima i modelima. Ovo uključuje kreiranje virtualnog stroja (VM) i pokretanje instance bilježnice. Zatim možete trenirati model pozivanjem klastera za računalnu obradu iz bilježnice.
- **Klasteri za računalnu obradu**: Skalabilni klasteri VM-ova za obradu eksperimentalnog koda na zahtjev. Trebat će vam kada trenirate model. Klasteri za računalnu obradu također mogu koristiti specijalizirane GPU ili CPU resurse.
- **Klasteri za inferenciju**: Ciljevi za implementaciju prediktivnih usluga koje koriste vaše trenirane modele.
- **Povezani resursi za računalstvo**: Povezuje postojeće Azure resurse za računalstvo, poput virtualnih strojeva ili Azure Databricks klastera.

#### 2.2.1 Odabir pravih opcija za vaše resurse za računalstvo

Neki ključni faktori koje treba uzeti u obzir prilikom stvaranja resursa za računalstvo mogu biti kritične odluke.

**Trebate li CPU ili GPU?**

CPU (Central Processing Unit) je elektronički sklop koji izvršava upute koje čine računalni program. GPU (Graphics Processing Unit) je specijalizirani elektronički sklop koji može izvoditi grafički povezani kod vrlo velikom brzinom.

Glavna razlika između arhitekture CPU-a i GPU-a je u tome što je CPU dizajniran za brzo obavljanje širokog spektra zadataka (mjereno brzinom takta CPU-a), ali je ograničen u paralelnosti zadataka koji se mogu izvoditi. GPU-ovi su dizajnirani za paralelno računanje i stoga su mnogo bolji za zadatke dubokog učenja.

| CPU                                     | GPU                         |
|-----------------------------------------|-----------------------------|
| Manje skup                             | Skuplji                    |
| Niža razina paralelnosti               | Viša razina paralelnosti   |
| Sporiji u treniranju modela dubokog učenja | Optimalan za duboko učenje |

**Veličina klastera**

Veći klasteri su skuplji, ali rezultiraju boljom responzivnošću. Stoga, ako imate vremena, ali ne i dovoljno novca, trebali biste započeti s manjim klasterom. Suprotno tome, ako imate novca, ali ne i puno vremena, trebali biste započeti s većim klasterom.

**Veličina VM-a**

Ovisno o vašim vremenskim i financijskim ograničenjima, možete varirati veličinu RAM-a, diska, broj jezgri i brzinu takta. Povećanje svih tih parametara bit će skuplje, ali će rezultirati boljim performansama.

**Namjenske ili niskoprioritetne instance?**

Niskoprioritetna instanca znači da je prekinjiva: Microsoft Azure može preuzeti te resurse i dodijeliti ih drugom zadatku, čime prekida posao. Namjenska instanca, ili neprekinjiva, znači da posao nikada neće biti prekinut bez vašeg dopuštenja. Ovo je još jedno razmatranje vremena naspram novca, budući da su prekinjive instance jeftinije od namjenskih.

#### 2.2.2 Stvaranje klastera za računalstvo

U [Azure ML radnom prostoru](https://ml.azure.com/) koji smo ranije stvorili, idite na "Compute" i moći ćete vidjeti različite resurse za računalstvo o kojima smo upravo razgovarali (npr. instance za računalstvo, klasteri za računalstvo, klasteri za inferenciju i povezano računalstvo). Za ovaj projekt, trebat će nam klaster za računalstvo za treniranje modela. U Studiju kliknite na izbornik "Compute", zatim karticu "Compute cluster" i kliknite na gumb "+ New" za stvaranje klastera za računalstvo.

![22](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/cluster-1.PNG)

1. Odaberite svoje opcije: Namjensko naspram niskog prioriteta, CPU ili GPU, veličina VM-a i broj jezgri (možete zadržati zadane postavke za ovaj projekt).
2. Kliknite na gumb "Next".

![23](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/cluster-2.PNG)

3. Dajte klasteru ime za računalstvo.
4. Odaberite svoje opcije: Minimalni/maksimalni broj čvorova, sekunde neaktivnosti prije smanjenja, SSH pristup. Imajte na umu da ako je minimalni broj čvorova 0, uštedjet ćete novac kada je klaster neaktivan. Imajte na umu da što je veći broj maksimalnih čvorova, to će treniranje biti kraće. Preporučeni maksimalni broj čvorova je 3.  
5. Kliknite na gumb "Create". Ovaj korak može potrajati nekoliko minuta.

![29](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/cluster-3.PNG)

Odlično! Sada kada imamo klaster za računalstvo, trebamo učitati podatke u Azure ML Studio.

### 2.3 Učitavanje skupa podataka

1. U [Azure ML radnom prostoru](https://ml.azure.com/) koji smo ranije stvorili, kliknite na "Datasets" u lijevom izborniku i kliknite na gumb "+ Create dataset" za stvaranje skupa podataka. Odaberite opciju "From local files" i odaberite Kaggle skup podataka koji smo ranije preuzeli.
   
   ![24](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/dataset-1.PNG)

2. Dajte svom skupu podataka ime, vrstu i opis. Kliknite "Next". Učitajte podatke iz datoteka. Kliknite "Next".
   
   ![25](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/dataset-2.PNG)

3. U shemi promijenite vrstu podataka u Boolean za sljedeće značajke: anaemia, diabetes, high blood pressure, sex, smoking i DEATH_EVENT. Kliknite "Next" i zatim "Create".
   
   ![26](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/dataset-3.PNG)

Odlično! Sada kada je skup podataka na mjestu i klaster za računalstvo je stvoren, možemo započeti treniranje modela!

### 2.4 Treniranje s malo ili bez koda pomoću AutoML-a

Tradicionalni razvoj modela strojnog učenja zahtijeva puno resursa, značajno domenno znanje i vrijeme za proizvodnju i usporedbu desetaka modela. Automatizirano strojno učenje (AutoML) proces je automatizacije vremenski zahtjevnih, iterativnih zadataka razvoja modela strojnog učenja. Omogućuje znanstvenicima podataka, analitičarima i programerima izradu ML modela s velikom skalabilnošću, učinkovitošću i produktivnošću, uz održavanje kvalitete modela. Smanjuje vrijeme potrebno za dobivanje modela spremnih za proizvodnju, uz veliku lakoću i učinkovitost. [Saznajte više](https://docs.microsoft.com/azure/machine-learning/concept-automated-ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)

1. U [Azure ML radnom prostoru](https://ml.azure.com/) koji smo ranije stvorili kliknite na "Automated ML" u lijevom izborniku i odaberite skup podataka koji ste upravo učitali. Kliknite "Next".

   ![27](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/aml-1.PNG)

2. Unesite novo ime eksperimenta, ciljni stupac (DEATH_EVENT) i klaster za računalstvo koji smo stvorili. Kliknite "Next".
   
   ![28](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/aml-2.PNG)

3. Odaberite "Classification" i kliknite "Finish". Ovaj korak može trajati između 30 minuta i 1 sat, ovisno o veličini vašeg klastera za računalstvo.
    
    ![30](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/aml-3.PNG)

4. Kada je pokretanje završeno, kliknite na karticu "Automated ML", kliknite na svoje pokretanje i kliknite na algoritam u kartici "Best model summary".
    
    ![31](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/aml-4.PNG)

Ovdje možete vidjeti detaljan opis najboljeg modela koji je AutoML generirao. Također možete istražiti druge modele generirane u kartici "Models". Odvojite nekoliko minuta za istraživanje modela u kartici "Explanations (preview)". Kada odaberete model koji želite koristiti (ovdje ćemo odabrati najbolji model koji je odabrao AutoML), vidjet ćemo kako ga možemo implementirati.

## 3. Implementacija modela s malo ili bez koda i konzumacija krajnje točke
### 3.1 Implementacija modela

Sučelje za automatizirano strojno učenje omogućuje vam implementaciju najboljeg modela kao web usluge u nekoliko koraka. Implementacija je integracija modela kako bi mogao davati predviđanja na temelju novih podataka i identificirati potencijalna područja prilika. Za ovaj projekt, implementacija u web uslugu znači da će medicinske aplikacije moći koristiti model za davanje predviđanja o riziku pacijenata od srčanog udara.

U opisu najboljeg modela kliknite na gumb "Deploy".
    
![deploy-1](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/deploy-1.PNG)

15. Dajte mu ime, opis, vrstu računalstva (Azure Container Instance), omogućite autentifikaciju i kliknite na "Deploy". Ovaj korak može trajati oko 20 minuta. Proces implementacije uključuje nekoliko koraka, uključujući registraciju modela, generiranje resursa i njihovu konfiguraciju za web uslugu. Statusna poruka pojavljuje se pod "Deploy status". Povremeno odaberite "Refresh" kako biste provjerili status implementacije. Implementirano je i radi kada je status "Healthy".

![deploy-2](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/deploy-2.PNG)

16. Kada je implementacija završena, kliknite na karticu "Endpoint" i kliknite na krajnju točku koju ste upravo implementirali. Ovdje možete pronaći sve detalje koje trebate znati o krajnjoj točki.

![deploy-3](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/deploy-3.PNG)

Nevjerojatno! Sada kada imamo implementiran model, možemo započeti konzumaciju krajnje točke.

### 3.2 Konzumacija krajnje točke

Kliknite na karticu "Consume". Ovdje možete pronaći REST krajnju točku i Python skriptu u opciji konzumacije. Odvojite malo vremena za čitanje Python koda.

Ova skripta može se izravno pokrenuti s vašeg lokalnog računala i konzumirat će vašu krajnju točku.

![35](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/consumption-1.PNG)

Odvojite trenutak da provjerite ove dvije linije koda:

```python
url = 'http://98e3715f-xxxx-xxxx-xxxx-9ec22d57b796.centralus.azurecontainer.io/score'
api_key = '' # Replace this with the API key for the web service
```  
Varijabla `url` je REST krajnja točka pronađena u kartici "Consume", a varijabla `api_key` je primarni ključ također pronađen u kartici "Consume" (samo u slučaju da ste omogućili autentifikaciju). Ovo je način na koji skripta može konzumirati krajnju točku.

18. Pokretanjem skripte trebali biste vidjeti sljedeći izlaz:  
    ```python
    b'"{\\"result\\": [true]}"'
    ```  
To znači da je predviđanje srčanog zatajenja za dane podatke točno. Ovo ima smisla jer ako pažljivije pogledate podatke automatski generirane u skripti, sve je postavljeno na 0 i false prema zadanim postavkama. Možete promijeniti podatke s ovim uzorkom unosa:

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
Skripta bi trebala vratiti:  
    ```python
    b'"{\\"result\\": [true, false]}"'
    ```  

Čestitamo! Upravo ste konzumirali implementirani model i trenirali ga na Azure ML-u!

> **_NAPOMENA:_** Kada završite s projektom, ne zaboravite izbrisati sve resurse.  
## 🚀 Izazov

Pogledajte detaljno objašnjenja modela i detalje koje je AutoML generirao za najbolje modele. Pokušajte razumjeti zašto je najbolji model bolji od ostalih. Koji su algoritmi uspoređeni? Koje su razlike među njima? Zašto je najbolji model u ovom slučaju bolji?

## [Kviz nakon predavanja](https://ff-quizzes.netlify.app/en/ds/)

## Pregled i samostalno učenje

U ovoj lekciji naučili ste kako trenirati, implementirati i konzumirati model za predviđanje rizika od srčanog zatajenja na način s malo ili bez koda u oblaku. Ako to još niste učinili, dublje istražite objašnjenja modela koja je AutoML generirao za najbolje modele i pokušajte razumjeti zašto je najbolji model bolji od ostalih.

Možete dodatno istražiti AutoML s malo ili bez koda čitajući ovu [dokumentaciju](https://docs.microsoft.com/azure/machine-learning/tutorial-first-experiment-automated-ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).

## Zadatak

[Projekt Data Science s malo ili bez koda na Azure ML-u](assignment.md)

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane stručnjaka. Ne preuzimamo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije proizašle iz korištenja ovog prijevoda.