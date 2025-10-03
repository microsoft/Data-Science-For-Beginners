<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T14:52:27+00:00",
  "source_file": "USAGE.md",
  "language_code": "de"
}
-->
# Gebrauchsanleitung

Diese Anleitung bietet Beispiele und typische Arbeitsabläufe für die Nutzung des Lehrplans "Data Science für Anfänger".

## Inhaltsverzeichnis

- [Wie man diesen Lehrplan nutzt](../..)
- [Arbeiten mit Lektionen](../..)
- [Arbeiten mit Jupyter Notebooks](../..)
- [Verwendung der Quiz-Anwendung](../..)
- [Typische Arbeitsabläufe](../..)
- [Tipps für Selbstlerner](../..)
- [Tipps für Lehrkräfte](../..)

## Wie man diesen Lehrplan nutzt

Dieser Lehrplan ist flexibel gestaltet und kann auf verschiedene Arten genutzt werden:

- **Selbstgesteuertes Lernen**: Arbeiten Sie die Lektionen eigenständig in Ihrem eigenen Tempo durch.
- **Unterricht im Klassenzimmer**: Nutzen Sie den Lehrplan als strukturierten Kurs mit geführtem Unterricht.
- **Lerngruppen**: Lernen Sie gemeinsam mit anderen.
- **Workshop-Format**: Intensives Lernen in kurzen Sitzungen.

## Arbeiten mit Lektionen

Jede Lektion folgt einer konsistenten Struktur, um das Lernen zu maximieren:

### Struktur der Lektionen

1. **Quiz vor der Lektion**: Testen Sie Ihr vorhandenes Wissen.
2. **Sketchnote** (Optional): Visuelle Zusammenfassung der wichtigsten Konzepte.
3. **Video** (Optional): Ergänzende Videoinhalte.
4. **Geschriebene Lektion**: Kernkonzepte und Erklärungen.
5. **Jupyter Notebook**: Praktische Programmierübungen.
6. **Aufgabe**: Üben Sie das Gelernte.
7. **Quiz nach der Lektion**: Festigen Sie Ihr Verständnis.

### Beispielablauf für eine Lektion

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

## Arbeiten mit Jupyter Notebooks

### Jupyter starten

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### Ausführen von Notebook-Zellen

1. **Eine Zelle ausführen**: Drücken Sie `Shift + Enter` oder klicken Sie auf die Schaltfläche "Run".
2. **Alle Zellen ausführen**: Wählen Sie im Menü "Cell" → "Run All".
3. **Kernel neu starten**: Wählen Sie "Kernel" → "Restart", falls Probleme auftreten.

### Beispiel: Arbeiten mit Daten in einem Notebook

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

### Speichern Ihrer Arbeit

- Jupyter speichert automatisch in regelmäßigen Abständen.
- Manuelles Speichern: Drücken Sie `Ctrl + S` (oder `Cmd + S` auf macOS).
- Ihr Fortschritt wird in der `.ipynb`-Datei gespeichert.

## Verwendung der Quiz-Anwendung

### Quiz-App lokal ausführen

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### Quiz durchführen

1. Quiz vor der Lektion sind oben in jeder Lektion verlinkt.
2. Quiz nach der Lektion sind unten in jeder Lektion verlinkt.
3. Jedes Quiz enthält 3 Fragen.
4. Die Quiz sind darauf ausgelegt, das Lernen zu unterstützen, nicht umfassend zu testen.

### Nummerierung der Quiz

- Quiz sind von 0-39 nummeriert (insgesamt 40 Quiz).
- Jede Lektion hat in der Regel ein Quiz vor und nach der Lektion.
- Quiz-URLs enthalten die Quiznummer: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## Typische Arbeitsabläufe

### Arbeitsablauf 1: Pfad für absolute Anfänger

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

### Arbeitsablauf 2: Lernen zu spezifischen Themen

Falls Sie sich für ein bestimmtes Thema interessieren:

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

### Arbeitsablauf 3: Projektbasiertes Lernen

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### Arbeitsablauf 4: Cloud-basierte Datenwissenschaft

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## Tipps für Selbstlerner

### Organisiert bleiben

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### Regelmäßig üben

- Reservieren Sie täglich oder wöchentlich feste Lernzeiten.
- Schließen Sie mindestens eine Lektion pro Woche ab.
- Wiederholen Sie regelmäßig vorherige Lektionen.

### Mit der Community interagieren

- Treten Sie der [Discord-Community](https://aka.ms/ds4beginners/discord) bei.
- Nehmen Sie am #Data-Science-for-Beginners-Kanal in Discord teil [Discord-Diskussionen](https://aka.ms/ds4beginners/discord).
- Teilen Sie Ihren Fortschritt und stellen Sie Fragen.

### Eigene Projekte erstellen

Nachdem Sie die Lektionen abgeschlossen haben, wenden Sie die Konzepte auf persönliche Projekte an:

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

## Tipps für Lehrkräfte

### Einrichtung des Klassenzimmers

1. Lesen Sie [for-teachers.md](for-teachers.md) für detaillierte Anleitungen.
2. Richten Sie eine gemeinsame Umgebung ein (GitHub Classroom oder Codespaces).
3. Etablieren Sie einen Kommunikationskanal (Discord, Slack oder Teams).

### Unterrichtsplanung

**Vorgeschlagener 10-Wochen-Plan:**

- **Woche 1-2**: Einführung (Lektionen 1-4)
- **Woche 3-4**: Arbeiten mit Daten (Lektionen 5-8)
- **Woche 5-6**: Datenvisualisierung (Lektionen 9-13)
- **Woche 7-8**: Lebenszyklus der Datenwissenschaft (Lektionen 14-16)
- **Woche 9**: Cloud-Datenwissenschaft (Lektionen 17-19)
- **Woche 10**: Anwendungen in der Praxis & Abschlussprojekte (Lektion 20)

### Docsify für Offline-Zugriff ausführen

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### Bewertung von Aufgaben

- Überprüfen Sie die Notebooks der Schüler auf abgeschlossene Übungen.
- Prüfen Sie das Verständnis anhand der Quiz-Ergebnisse.
- Bewerten Sie Abschlussprojekte anhand der Prinzipien des Lebenszyklus der Datenwissenschaft.

### Aufgaben erstellen

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

## Offline arbeiten

### Ressourcen herunterladen

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### Dokumentation lokal ausführen

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### Quiz-App lokal ausführen

```bash
cd quiz-app
npm run serve
```

## Zugriff auf übersetzte Inhalte

Übersetzungen sind in über 40 Sprachen verfügbar:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

Jede Übersetzung behält die gleiche Struktur wie die englische Version bei.

## Zusätzliche Ressourcen

### Weiterlernen

- [Microsoft Learn](https://docs.microsoft.com/learn/) - Weitere Lernpfade
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - Ressourcen für Studierende
- [Azure AI Foundry](https://aka.ms/foundry/forum) - Community-Forum

### Verwandte Lehrpläne

- [KI für Anfänger](https://aka.ms/ai-beginners)
- [ML für Anfänger](https://aka.ms/ml-beginners)
- [Webentwicklung für Anfänger](https://aka.ms/webdev-beginners)
- [Generative KI für Anfänger](https://aka.ms/genai-beginners)

## Hilfe erhalten

- Lesen Sie [TROUBLESHOOTING.md](TROUBLESHOOTING.md) für häufige Probleme.
- Suchen Sie in [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues).
- Treten Sie unserem [Discord](https://aka.ms/ds4beginners/discord) bei.
- Überprüfen Sie [CONTRIBUTING.md](CONTRIBUTING.md), um Probleme zu melden oder beizutragen.

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.