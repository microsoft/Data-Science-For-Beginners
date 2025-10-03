<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10f86fb29b5407088445ac803b3d0ed1",
  "translation_date": "2025-10-03T13:55:29+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "it"
}
-->
# Contribuire a Data Science for Beginners

Grazie per il tuo interesse nel contribuire al curriculum di Data Science for Beginners! Accogliamo con piacere i contributi della comunità.

## Indice

- [Codice di Condotta](../..)
- [Come Posso Contribuire?](../..)
- [Per Iniziare](../..)
- [Linee Guida per i Contributi](../..)
- [Processo di Pull Request](../..)
- [Linee Guida di Stile](../..)
- [Accordo di Licenza per i Contributori](../..)

## Codice di Condotta

Questo progetto ha adottato il [Codice di Condotta Open Source di Microsoft](https://opensource.microsoft.com/codeofconduct/).  
Per ulteriori informazioni, consulta le [FAQ sul Codice di Condotta](https://opensource.microsoft.com/codeofconduct/faq/)  
o contatta [opencode@microsoft.com](mailto:opencode@microsoft.com) per eventuali domande o commenti.

## Come Posso Contribuire?

### Segnalare Bug

Prima di creare segnalazioni di bug, controlla i problemi esistenti per evitare duplicati. Quando crei una segnalazione di bug, includi il maggior numero di dettagli possibile:

- **Usa un titolo chiaro e descrittivo**
- **Descrivi i passaggi esatti per riprodurre il problema**
- **Fornisci esempi specifici** (frammenti di codice, screenshot)
- **Descrivi il comportamento osservato e quello atteso**
- **Includi i dettagli del tuo ambiente** (OS, versione di Python, browser)

### Suggerire Miglioramenti

I suggerimenti per miglioramenti sono benvenuti! Quando suggerisci miglioramenti:

- **Usa un titolo chiaro e descrittivo**
- **Fornisci una descrizione dettagliata del miglioramento suggerito**
- **Spiega perché questo miglioramento sarebbe utile**
- **Elenca eventuali funzionalità simili in altri progetti, se applicabile**

### Contribuire alla Documentazione

I miglioramenti alla documentazione sono sempre apprezzati:

- **Correggi errori di battitura e grammaticali**
- **Migliora la chiarezza delle spiegazioni**
- **Aggiungi documentazione mancante**
- **Aggiorna informazioni obsolete**
- **Aggiungi esempi o casi d'uso**

### Contribuire al Codice

Accogliamo contributi al codice, inclusi:

- **Nuove lezioni o esercizi**
- **Correzioni di bug**
- **Miglioramenti ai notebook esistenti**
- **Nuovi dataset o esempi**
- **Miglioramenti all'applicazione dei quiz**

## Per Iniziare

### Prerequisiti

Prima di contribuire, assicurati di avere:

1. Un account GitHub
2. Git installato sul tuo sistema
3. Python 3.7+ e Jupyter installati
4. Node.js e npm (per contributi all'app dei quiz)
5. Familiarità con la struttura del curriculum

Consulta [INSTALLATION.md](INSTALLATION.md) per istruzioni dettagliate sulla configurazione.

### Fork e Clone

1. **Fai il fork del repository** su GitHub  
2. **Clona il tuo fork** localmente:  
   ```bash
   git clone https://github.com/YOUR-USERNAME/Data-Science-For-Beginners.git
   cd Data-Science-For-Beginners
   ```
  
3. **Aggiungi il remote upstream**:  
   ```bash
   git remote add upstream https://github.com/microsoft/Data-Science-For-Beginners.git
   ```
  

### Crea un Branch

Crea un nuovo branch per il tuo lavoro:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```
  
Convenzioni per la denominazione dei branch:  
- `feature/` - Nuove funzionalità o lezioni  
- `fix/` - Correzioni di bug  
- `docs/` - Modifiche alla documentazione  
- `refactor/` - Refactoring del codice  

## Linee Guida per i Contributi

### Per il Contenuto delle Lezioni

Quando contribuisci con lezioni o modifichi quelle esistenti:

1. **Segui la struttura esistente**:  
   - README.md con il contenuto della lezione  
   - Notebook Jupyter con esercizi  
   - Compito (se applicabile)  
   - Link ai quiz pre e post lezione  

2. **Includi questi elementi**:  
   - Obiettivi di apprendimento chiari  
   - Spiegazioni passo-passo  
   - Esempi di codice con commenti  
   - Esercizi per la pratica  
   - Link a risorse aggiuntive  

3. **Garantisci l'accessibilità**:  
   - Usa un linguaggio chiaro e semplice  
   - Fornisci testo alternativo per le immagini  
   - Includi commenti nel codice  
   - Considera diversi stili di apprendimento  

### Per i Notebook Jupyter

1. **Cancella tutti gli output** prima di fare il commit:  
   ```bash
   jupyter nbconvert --clear-output --inplace notebook.ipynb
   ```
  
2. **Includi celle markdown** con spiegazioni  

3. **Usa una formattazione coerente**:  
   ```python
   # Import libraries at the top
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   
   # Use meaningful variable names
   # Add comments for complex operations
   # Follow PEP 8 style guidelines
   ```
  
4. **Testa completamente il tuo notebook** prima di inviarlo  

### Per il Codice Python

Segui le linee guida di stile [PEP 8](https://www.python.org/dev/peps/pep-0008/):  
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
  

### Per i Contributi all'App dei Quiz

Quando modifichi l'applicazione dei quiz:

1. **Testa localmente**:  
   ```bash
   cd quiz-app
   npm install
   npm run serve
   ```
  
2. **Esegui il linter**:  
   ```bash
   npm run lint
   ```
  
3. **Compila con successo**:  
   ```bash
   npm run build
   ```
  
4. **Segui la guida di stile Vue.js** e i modelli esistenti  

### Per le Traduzioni

Quando aggiungi o aggiorni traduzioni:

1. Segui la struttura nella cartella `translations/`  
2. Usa il codice della lingua come nome della cartella (es. `it` per italiano)  
3. Mantieni la stessa struttura dei file della versione inglese  
4. Aggiorna i link dei quiz per includere il parametro della lingua: `?loc=it`  
5. Testa tutti i link e la formattazione  

## Processo di Pull Request

### Prima di Inviare

1. **Aggiorna il tuo branch** con le modifiche più recenti:  
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```
  
2. **Testa le tue modifiche**:  
   - Esegui tutti i notebook modificati  
   - Testa l'app dei quiz se modificata  
   - Verifica che tutti i link funzionino  
   - Controlla errori di ortografia e grammatica  

3. **Fai il commit delle tue modifiche**:  
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```
  
   Scrivi messaggi di commit chiari:  
   - Usa il tempo presente ("Aggiungi funzionalità" non "Aggiunta funzionalità")  
   - Usa il modo imperativo ("Sposta il cursore su..." non "Sposta il cursore su...")  
   - Limita la prima riga a 72 caratteri  
   - Fai riferimento a problemi e pull request quando rilevante  

4. **Fai il push al tuo fork**:  
   ```bash
   git push origin feature/your-feature-name
   ```
  

### Creare la Pull Request

1. Vai al [repository](https://github.com/microsoft/Data-Science-For-Beginners)  
2. Clicca su "Pull requests" → "New pull request"  
3. Clicca su "compare across forks"  
4. Seleziona il tuo fork e branch  
5. Clicca su "Create pull request"  

### Formato del Titolo della PR

Usa titoli chiari e descrittivi seguendo questo formato:  
```
[Component] Brief description
```
  
Esempi:  
- `[Lesson 7] Fix errore di importazione notebook Python`  
- `[Quiz App] Aggiungi traduzione in tedesco`  
- `[Docs] Aggiorna README con nuovi prerequisiti`  
- `[Fix] Correggi percorso dati nella lezione di visualizzazione`  

### Descrizione della PR

Includi nella descrizione della PR:  

- **Cosa**: Quali modifiche hai apportato?  
- **Perché**: Perché queste modifiche sono necessarie?  
- **Come**: Come hai implementato le modifiche?  
- **Test**: Come hai testato le modifiche?  
- **Screenshot**: Includi screenshot per modifiche visive  
- **Problemi correlati**: Link ai problemi correlati (es. "Fixes #123")  

### Processo di Revisione

1. **Controlli automatici** verranno eseguiti sulla tua PR  
2. **I manutentori revisioneranno** il tuo contributo  
3. **Rispondi al feedback** facendo commit aggiuntivi  
4. Una volta approvata, un **manutentore unirà** la tua PR  

### Dopo che la tua PR è stata Unita

1. Elimina il tuo branch:  
   ```bash
   git branch -d feature/your-feature-name
   git push origin --delete feature/your-feature-name
   ```
  
2. Aggiorna il tuo fork:  
   ```bash
   git checkout main
   git pull upstream main
   git push origin main
   ```
  

## Linee Guida di Stile

### Markdown

- Usa livelli di intestazione coerenti  
- Includi righe vuote tra le sezioni  
- Usa blocchi di codice con specificatori di linguaggio:  
  ````markdown
  ```python
  import pandas as pd
  ```
  ````
  
- Aggiungi testo alternativo alle immagini: `![Testo alternativo](../../translated_images/image.4ee84a82b5e4c9e6651b13fd27dcf615e427ec584929f2cef7167aa99151a77a.it.png)`  
- Mantieni lunghezze di riga ragionevoli (circa 80-100 caratteri)  

### Python

- Segui la guida di stile PEP 8  
- Usa nomi di variabili significativi  
- Aggiungi docstring alle funzioni  
- Includi suggerimenti di tipo dove appropriato:  
  ```python
  def process_data(df: pd.DataFrame) -> pd.DataFrame:
      """Process the input dataframe."""
      return df
  ```
  

### JavaScript/Vue.js

- Segui la guida di stile Vue.js 2  
- Usa la configurazione ESLint fornita  
- Scrivi componenti modulari e riutilizzabili  
- Aggiungi commenti per la logica complessa  

### Organizzazione dei File

- Mantieni i file correlati insieme  
- Usa nomi di file descrittivi  
- Segui la struttura delle directory esistente  
- Non fare commit di file non necessari (.DS_Store, .pyc, node_modules, ecc.)  

## Accordo di Licenza per i Contributori

Questo progetto accoglie contributi e suggerimenti. La maggior parte dei contributi richiede che tu accetti un Accordo di Licenza per i Contributori (CLA) dichiarando che hai il diritto di, e effettivamente concedi, i diritti per utilizzare il tuo contributo. Per dettagli, visita  
https://cla.microsoft.com.

Quando invii una pull request, un bot CLA determinerà automaticamente se devi fornire un CLA e decorerà la PR di conseguenza (es. etichetta, commento). Segui semplicemente le istruzioni fornite dal bot. Dovrai farlo solo una volta per tutti i repository che utilizzano il nostro CLA.

## Domande?

- Controlla il nostro [Canale Discord #data-science-for-beginners](https://aka.ms/ds4beginners/discord)  
- Unisciti alla nostra [comunità Discord](https://aka.ms/ds4beginners/discord)  
- Consulta i [problemi esistenti](https://github.com/microsoft/Data-Science-For-Beginners/issues) e le [pull request](https://github.com/microsoft/Data-Science-For-Beginners/pulls)  

## Grazie!

I tuoi contributi rendono questo curriculum migliore per tutti. Grazie per dedicare il tuo tempo a contribuire!

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.