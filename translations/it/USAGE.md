<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T15:01:37+00:00",
  "source_file": "USAGE.md",
  "language_code": "it"
}
-->
# Guida all'Uso

Questa guida fornisce esempi e flussi di lavoro comuni per utilizzare il curriculum "Data Science for Beginners".

## Indice

- [Come Utilizzare Questo Curriculum](../..)
- [Lavorare con le Lezioni](../..)
- [Lavorare con i Jupyter Notebook](../..)
- [Utilizzare l'Applicazione Quiz](../..)
- [Flussi di Lavoro Comuni](../..)
- [Consigli per Studenti Autodidatti](../..)
- [Consigli per Insegnanti](../..)

## Come Utilizzare Questo Curriculum

Questo curriculum è progettato per essere flessibile e può essere utilizzato in diversi modi:

- **Apprendimento autonomo**: Segui le lezioni indipendentemente, al tuo ritmo
- **Istruzione in aula**: Utilizzalo come corso strutturato con istruzione guidata
- **Gruppi di studio**: Impara collaborando con i tuoi pari
- **Formato workshop**: Sessioni di apprendimento intensive a breve termine

## Lavorare con le Lezioni

Ogni lezione segue una struttura coerente per massimizzare l'apprendimento:

### Struttura della Lezione

1. **Quiz preliminare**: Metti alla prova le tue conoscenze iniziali
2. **Sketchnote** (Opzionale): Riassunto visivo dei concetti chiave
3. **Video** (Opzionale): Contenuti video supplementari
4. **Lezione scritta**: Concetti principali e spiegazioni
5. **Jupyter Notebook**: Esercizi pratici di programmazione
6. **Compito**: Metti in pratica ciò che hai imparato
7. **Quiz finale**: Rafforza la tua comprensione

### Esempio di Flusso di Lavoro per una Lezione

```bash
# 1. Navigate to the lesson directory
cd 1-Introduction/01-defining-data-science

# 2. Read the README.md
# Open README.md in your browser or editor

# 3. Take the pre-lesson quiz
# Click the quiz link in the README

# 4. Open the Jupyter notebook (if available)
jupyter notebook

# 5. Complete the exercises in the notebook

# 6. Work on the assignment

# 7. Take the post-lesson quiz
```

## Lavorare con i Jupyter Notebook

### Avviare Jupyter

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### Eseguire le Celle del Notebook

1. **Esegui una cella**: Premi `Shift + Enter` o clicca sul pulsante "Run"
2. **Esegui tutte le celle**: Seleziona "Cell" → "Run All" dal menu
3. **Riavvia il kernel**: Seleziona "Kernel" → "Restart" se riscontri problemi

### Esempio: Lavorare con i Dati in un Notebook

```python
# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load a dataset
df = pd.read_csv('data/sample.csv')

# Explore the data
df.head()
df.info()
df.describe()

# Create a visualization
plt.figure(figsize=(10, 6))
plt.plot(df['column_name'])
plt.title('Sample Visualization')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.show()
```

### Salvare il Lavoro

- Jupyter salva automaticamente a intervalli regolari
- Salva manualmente: Premi `Ctrl + S` (o `Cmd + S` su macOS)
- I tuoi progressi vengono salvati nel file `.ipynb`

## Utilizzare l'Applicazione Quiz

### Eseguire l'App Quiz Localmente

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### Svolgere i Quiz

1. I quiz preliminari sono collegati all'inizio di ogni lezione
2. I quiz finali sono collegati alla fine di ogni lezione
3. Ogni quiz contiene 3 domande
4. I quiz sono progettati per rafforzare l'apprendimento, non per testare in modo esaustivo

### Numerazione dei Quiz

- I quiz sono numerati da 0 a 39 (40 quiz in totale)
- Ogni lezione ha generalmente un quiz preliminare e uno finale
- Gli URL dei quiz includono il numero del quiz: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## Flussi di Lavoro Comuni

### Flusso di Lavoro 1: Percorso per Principianti Completo

```bash
# 1. Set up your environment (see INSTALLATION.md)

# 2. Start with Lesson 1
cd 1-Introduction/01-defining-data-science

# 3. For each lesson:
#    - Take pre-lesson quiz
#    - Read the lesson content
#    - Work through the notebook
#    - Complete the assignment
#    - Take post-lesson quiz

# 4. Progress through all 20 lessons sequentially
```

### Flusso di Lavoro 2: Apprendimento Specifico per Argomento

Se sei interessato a un argomento specifico:

```bash
# Example: Focus on Data Visualization
cd 3-Data-Visualization

# Explore lessons 9-13:
# - Lesson 9: Visualizing Quantities
# - Lesson 10: Visualizing Distributions
# - Lesson 11: Visualizing Proportions
# - Lesson 12: Visualizing Relationships
# - Lesson 13: Meaningful Visualizations
```

### Flusso di Lavoro 3: Apprendimento Basato su Progetti

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### Flusso di Lavoro 4: Data Science su Cloud

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## Consigli per Studenti Autodidatti

### Organizzati

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### Pratica Regolarmente

- Dedica tempo specifico ogni giorno o settimana
- Completa almeno una lezione a settimana
- Rivedi periodicamente le lezioni precedenti

### Interagisci con la Comunità

- Unisciti alla [comunità Discord](https://aka.ms/ds4beginners/discord)
- Partecipa al canale #Data-Science-for-Beginners su Discord [Discussioni Discord](https://aka.ms/ds4beginners/discord)
- Condividi i tuoi progressi e fai domande

### Crea i Tuoi Progetti

Dopo aver completato le lezioni, applica i concetti a progetti personali:

```python
# Example: Analyze your own dataset
import pandas as pd

# Load your own data
my_data = pd.read_csv('my-project/data.csv')

# Apply techniques learned
# - Data cleaning (Lesson 8)
# - Exploratory data analysis (Lesson 7)
# - Visualization (Lessons 9-13)
# - Analysis (Lesson 15)
```

## Consigli per Insegnanti

### Configurazione della Classe

1. Consulta [for-teachers.md](for-teachers.md) per una guida dettagliata
2. Configura un ambiente condiviso (GitHub Classroom o Codespaces)
3. Stabilisci un canale di comunicazione (Discord, Slack o Teams)

### Pianificazione delle Lezioni

**Programma Suggerito di 10 Settimane:**

- **Settimana 1-2**: Introduzione (Lezioni 1-4)
- **Settimana 3-4**: Lavorare con i Dati (Lezioni 5-8)
- **Settimana 5-6**: Visualizzazione dei Dati (Lezioni 9-13)
- **Settimana 7-8**: Ciclo di Vita della Data Science (Lezioni 14-16)
- **Settimana 9**: Data Science su Cloud (Lezioni 17-19)
- **Settimana 10**: Applicazioni Reali & Progetti Finali (Lezione 20)

### Eseguire Docsify per Accesso Offline

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### Valutazione dei Compiti

- Esamina i notebook degli studenti per verificare gli esercizi completati
- Controlla la comprensione attraverso i punteggi dei quiz
- Valuta i progetti finali utilizzando i principi del ciclo di vita della data science

### Creare Compiti

```python
# Example custom assignment template
"""
Assignment: [Topic]

Objective: [Learning goal]

Dataset: [Provide or have students find one]

Tasks:
1. Load and explore the dataset
2. Clean and prepare the data
3. Create at least 3 visualizations
4. Perform analysis
5. Communicate findings

Deliverables:
- Jupyter notebook with code and explanations
- Written summary of findings
"""
```

## Lavorare Offline

### Scaricare le Risorse

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### Eseguire la Documentazione Localmente

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### Eseguire l'App Quiz Localmente

```bash
cd quiz-app
npm run serve
```

## Accesso ai Contenuti Tradotti

Le traduzioni sono disponibili in oltre 40 lingue:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

Ogni traduzione mantiene la stessa struttura della versione in inglese.

## Risorse Aggiuntive

### Continua a Imparare

- [Microsoft Learn](https://docs.microsoft.com/learn/) - Percorsi di apprendimento aggiuntivi
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - Risorse per studenti
- [Azure AI Foundry](https://aka.ms/foundry/forum) - Forum della comunità

### Curricula Correlati

- [AI for Beginners](https://aka.ms/ai-beginners)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [Generative AI for Beginners](https://aka.ms/genai-beginners)

## Ottenere Aiuto

- Consulta [TROUBLESHOOTING.md](TROUBLESHOOTING.md) per problemi comuni
- Cerca [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
- Unisciti al nostro [Discord](https://aka.ms/ds4beginners/discord)
- Consulta [CONTRIBUTING.md](CONTRIBUTING.md) per segnalare problemi o contribuire

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.