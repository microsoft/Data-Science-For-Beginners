<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10f86fb29b5407088445ac803b3d0ed1",
  "translation_date": "2025-10-03T14:35:31+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "ro"
}
-->
# Contribuind la Data Science pentru Începători

Mulțumim pentru interesul de a contribui la curriculumul Data Science pentru Începători! Salutăm contribuțiile din partea comunității.

## Cuprins

- [Cod de Conduită](../..)
- [Cum Pot Contribui?](../..)
- [Începutul](../..)
- [Ghid de Contribuție](../..)
- [Procesul de Pull Request](../..)
- [Ghiduri de Stil](../..)
- [Acord de Licență pentru Contribuitori](../..)

## Cod de Conduită

Acest proiect a adoptat [Codul de Conduită Open Source Microsoft](https://opensource.microsoft.com/codeofconduct/).  
Pentru mai multe informații, consultați [FAQ-ul Codului de Conduită](https://opensource.microsoft.com/codeofconduct/faq/)  
sau contactați [opencode@microsoft.com](mailto:opencode@microsoft.com) pentru întrebări sau comentarii suplimentare.

## Cum Pot Contribui?

### Raportarea Bug-urilor

Înainte de a crea rapoarte de bug-uri, verificați problemele existente pentru a evita duplicatele. Când creați un raport de bug, includeți cât mai multe detalii:

- **Folosiți un titlu clar și descriptiv**
- **Descrieți pașii exacți pentru a reproduce problema**
- **Furnizați exemple specifice** (fragmente de cod, capturi de ecran)
- **Descrieți comportamentul observat și cel așteptat**
- **Includeți detalii despre mediul dvs.** (OS, versiunea Python, browser)

### Sugestii de Îmbunătățiri

Sugestiile de îmbunătățiri sunt binevenite! Când propuneți îmbunătățiri:

- **Folosiți un titlu clar și descriptiv**
- **Furnizați o descriere detaliată a îmbunătățirii sugerate**
- **Explicați de ce această îmbunătățire ar fi utilă**
- **Listați funcționalități similare din alte proiecte, dacă este cazul**

### Contribuind la Documentație

Îmbunătățirile documentației sunt mereu apreciate:

- **Corectați greșelile de ortografie și gramatică**
- **Îmbunătățiți claritatea explicațiilor**
- **Adăugați documentație lipsă**
- **Actualizați informațiile învechite**
- **Adăugați exemple sau cazuri de utilizare**

### Contribuind Cod

Salutăm contribuțiile de cod, inclusiv:

- **Lecții sau exerciții noi**
- **Corectarea bug-urilor**
- **Îmbunătățiri ale notebook-urilor existente**
- **Seturi de date sau exemple noi**
- **Îmbunătățiri ale aplicației de quiz**

## Începutul

### Cerințe Prealabile

Înainte de a contribui, asigurați-vă că aveți:

1. Un cont GitHub
2. Git instalat pe sistemul dvs.
3. Python 3.7+ și Jupyter instalat
4. Node.js și npm (pentru contribuții la aplicația de quiz)
5. Familiaritate cu structura curriculumului

Consultați [INSTALLATION.md](INSTALLATION.md) pentru instrucțiuni detaliate de configurare.

### Fork și Clone

1. **Fork-uiți repository-ul** pe GitHub  
2. **Clonați fork-ul** local:  
   ```bash
   git clone https://github.com/YOUR-USERNAME/Data-Science-For-Beginners.git
   cd Data-Science-For-Beginners
   ```
  
3. **Adăugați upstream remote**:  
   ```bash
   git remote add upstream https://github.com/microsoft/Data-Science-For-Beginners.git
   ```
  

### Creați un Branch

Creați un branch nou pentru munca dvs.:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```
  
Convenții pentru denumirea branch-urilor:  
- `feature/` - Funcționalități sau lecții noi  
- `fix/` - Corectarea bug-urilor  
- `docs/` - Modificări ale documentației  
- `refactor/` - Refactorizarea codului  

## Ghid de Contribuție

### Pentru Conținutul Lecțiilor

Când contribuiți lecții sau modificați lecții existente:

1. **Respectați structura existentă**:  
   - README.md cu conținutul lecției  
   - Notebook Jupyter cu exerciții  
   - Temă (dacă este cazul)  
   - Link către quiz-uri pre și post  

2. **Includeți aceste elemente**:  
   - Obiective clare de învățare  
   - Explicații pas cu pas  
   - Exemple de cod cu comentarii  
   - Exerciții pentru practică  
   - Link-uri către resurse suplimentare  

3. **Asigurați accesibilitatea**:  
   - Folosiți un limbaj clar și simplu  
   - Furnizați text alternativ pentru imagini  
   - Includeți comentarii în cod  
   - Luați în considerare stiluri diferite de învățare  

### Pentru Notebook-uri Jupyter

1. **Ștergeți toate output-urile** înainte de a face commit:  
   ```bash
   jupyter nbconvert --clear-output --inplace notebook.ipynb
   ```
  
2. **Includeți celule markdown** cu explicații  

3. **Folosiți un format consistent**:  
   ```python
   # Import libraries at the top
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   
   # Use meaningful variable names
   # Add comments for complex operations
   # Follow PEP 8 style guidelines
   ```
  
4. **Testați complet notebook-ul** înainte de a-l trimite  

### Pentru Cod Python

Respectați ghidul de stil [PEP 8](https://www.python.org/dev/peps/pep-0008/):  

```python
# Good practices
import pandas as pd

def calculate_mean(data):
    """Calculate the mean of a dataset.
    
    Args:
        data (list): List of numerical values
        
    Returns:
        float: Mean of the dataset
    """
    return sum(data) / len(data)
```
  

### Pentru Contribuții la Aplicația de Quiz

Când modificați aplicația de quiz:

1. **Testați local**:  
   ```bash
   cd quiz-app
   npm install
   npm run serve
   ```
  
2. **Rulați linter-ul**:  
   ```bash
   npm run lint
   ```
  
3. **Construiți cu succes**:  
   ```bash
   npm run build
   ```
  
4. **Respectați ghidul de stil Vue.js** și modelele existente  

### Pentru Traduceri

Când adăugați sau actualizați traduceri:

1. Respectați structura din folderul `translations/`  
2. Folosiți codul limbii ca nume de folder (de exemplu, `fr` pentru franceză)  
3. Mențineți aceeași structură de fișiere ca versiunea în engleză  
4. Actualizați link-urile quiz-urilor pentru a include parametrul limbii: `?loc=fr`  
5. Testați toate link-urile și formatările  

## Procesul de Pull Request

### Înainte de a Trimite

1. **Actualizați branch-ul dvs.** cu cele mai recente modificări:  
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```
  
2. **Testați modificările dvs.**:  
   - Rulați toate notebook-urile modificate  
   - Testați aplicația de quiz dacă a fost modificată  
   - Verificați toate link-urile  
   - Verificați greșelile de ortografie și gramatică  

3. **Faceți commit modificărilor dvs.**:  
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```
  
   Scrieți mesaje de commit clare:  
   - Folosiți timpul prezent ("Adaugă funcționalitate" nu "Am adăugat funcționalitate")  
   - Folosiți modul imperativ ("Mută cursorul la..." nu "Mută cursorul la...")  
   - Limitați prima linie la 72 de caractere  
   - Faceți referire la probleme și pull request-uri relevante  

4. **Faceți push la fork-ul dvs.**:  
   ```bash
   git push origin feature/your-feature-name
   ```
  

### Crearea Pull Request-ului

1. Accesați [repository-ul](https://github.com/microsoft/Data-Science-For-Beginners)  
2. Click pe "Pull requests" → "New pull request"  
3. Click pe "compare across forks"  
4. Selectați fork-ul și branch-ul dvs.  
5. Click pe "Create pull request"  

### Formatul Titlului PR

Folosiți titluri clare și descriptive urmând acest format:

```
[Component] Brief description
```
  
Exemple:  
- `[Lesson 7] Fix Python notebook import error`  
- `[Quiz App] Add German translation`  
- `[Docs] Update README with new prerequisites`  
- `[Fix] Correct data path in visualization lesson`  

### Descrierea PR

Includeți în descrierea PR-ului:

- **Ce**: Ce modificări ați făcut?  
- **De ce**: De ce sunt necesare aceste modificări?  
- **Cum**: Cum ați implementat modificările?  
- **Testare**: Cum ați testat modificările?  
- **Capturi de ecran**: Includeți capturi de ecran pentru modificările vizuale  
- **Probleme asociate**: Link către problemele asociate (de exemplu, "Fixes #123")  

### Procesul de Revizuire

1. **Verificările automate** vor rula pe PR-ul dvs.  
2. **Maintainerii vor revizui** contribuția dvs.  
3. **Adresați feedback-ul** făcând commit-uri suplimentare  
4. După aprobare, un **maintainer va face merge** PR-ul dvs.  

### După ce PR-ul dvs. este Fuzionat

1. Ștergeți branch-ul dvs.:  
   ```bash
   git branch -d feature/your-feature-name
   git push origin --delete feature/your-feature-name
   ```
  
2. Actualizați fork-ul dvs.:  
   ```bash
   git checkout main
   git pull upstream main
   git push origin main
   ```
  

## Ghiduri de Stil

### Markdown

- Folosiți niveluri consistente de titluri  
- Includeți linii goale între secțiuni  
- Folosiți blocuri de cod cu specificatori de limbaj:  
  ````markdown
  ```python
  import pandas as pd
  ```
  ````
  
- Adăugați text alternativ la imagini: `![Alt text](../../translated_images/image.4ee84a82b5e4c9e6651b13fd27dcf615e427ec584929f2cef7167aa99151a77a.ro.png)`  
- Mențineți lungimea liniilor rezonabilă (aproximativ 80-100 de caractere)  

### Python

- Respectați ghidul de stil PEP 8  
- Folosiți nume de variabile semnificative  
- Adăugați docstrings la funcții  
- Includeți indicii de tip acolo unde este cazul:  
  ```python
  def process_data(df: pd.DataFrame) -> pd.DataFrame:
      """Process the input dataframe."""
      return df
  ```
  

### JavaScript/Vue.js

- Respectați ghidul de stil Vue.js 2  
- Folosiți configurația ESLint furnizată  
- Scrieți componente modulare, reutilizabile  
- Adăugați comentarii pentru logica complexă  

### Organizarea Fișierelor

- Mențineți fișierele asociate împreună  
- Folosiți nume de fișiere descriptive  
- Respectați structura existentă a directoarelor  
- Nu faceți commit fișierelor inutile (.DS_Store, .pyc, node_modules, etc.)  

## Acord de Licență pentru Contribuitori

Acest proiect salută contribuțiile și sugestiile. Majoritatea contribuțiilor necesită să  
fiți de acord cu un Acord de Licență pentru Contribuitori (CLA) care declară că aveți dreptul de a,  
și chiar acordați drepturile de utilizare a contribuției dvs. Pentru detalii, vizitați  
https://cla.microsoft.com.  

Când trimiteți un pull request, un bot CLA va determina automat dacă trebuie  
să furnizați un CLA și va decora PR-ul corespunzător (de exemplu, etichetă, comentariu). Pur și simplu urmați  
instrucțiunile furnizate de bot. Va trebui să faceți acest lucru o singură dată pentru toate repository-urile care folosesc CLA-ul nostru.

## Întrebări?

- Verificați [Canalul nostru Discord #data-science-for-beginners](https://aka.ms/ds4beginners/discord)  
- Alăturați-vă [comunității noastre Discord](https://aka.ms/ds4beginners/discord)  
- Revizuiți problemele [existente](https://github.com/microsoft/Data-Science-For-Beginners/issues) și [pull request-urile](https://github.com/microsoft/Data-Science-For-Beginners/pulls)  

## Mulțumim!

Contribuțiile dvs. fac acest curriculum mai bun pentru toată lumea. Mulțumim că v-ați luat timpul să contribuiți!

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.