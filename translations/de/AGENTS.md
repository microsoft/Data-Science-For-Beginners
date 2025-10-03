<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:00:36+00:00",
  "source_file": "AGENTS.md",
  "language_code": "de"
}
-->
# AGENTS.md

## Projektübersicht

Data Science for Beginners ist ein umfassender 10-wöchiger, 20-teiliger Lehrplan, der von den Microsoft Azure Cloud Advocates erstellt wurde. Das Repository dient als Lernressource, die grundlegende Konzepte der Datenwissenschaft durch projektbasierte Lektionen vermittelt, einschließlich Jupyter-Notebooks, interaktiver Quizze und praktischer Aufgaben.

**Wichtige Technologien:**
- **Jupyter-Notebooks**: Hauptmedium für das Lernen mit Python 3
- **Python-Bibliotheken**: pandas, numpy, matplotlib für Datenanalyse und Visualisierung
- **Vue.js 2**: Quiz-Anwendung (Ordner quiz-app)
- **Docsify**: Generator für Dokumentationsseiten für den Offline-Zugriff
- **Node.js/npm**: Paketverwaltung für JavaScript-Komponenten
- **Markdown**: Alle Lektionen und Dokumentationen

**Architektur:**
- Mehrsprachiges Bildungs-Repository mit umfangreichen Übersetzungen
- In Lektionenmodule strukturiert (1-Introduction bis 6-Data-Science-In-Wild)
- Jede Lektion enthält README, Notebooks, Aufgaben und Quizze
- Eigenständige Vue.js-Quiz-Anwendung für Vor-/Nach-Lektionsbewertungen
- Unterstützung durch GitHub Codespaces und VS Code Dev-Container

## Setup-Befehle

### Repository-Setup
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### Python-Umgebung einrichten
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Quiz-Anwendung einrichten
```bash
# Navigate to quiz app
cd quiz-app

# Install dependencies
npm install

# Start development server
npm run serve

# Build for production
npm run build

# Lint and fix files
npm run lint
```

### Docsify-Dokumentationsserver
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### Setup für Visualisierungsprojekte
Für Visualisierungsprojekte wie meaningful-visualizations (Lektion 13):
```bash
# Navigate to starter or solution folder
cd 3-Data-Visualization/13-meaningful-visualizations/starter

# Install dependencies
npm install

# Start development server
npm run serve

# Build for production
npm run build

# Lint files
npm run lint
```


## Entwicklungsworkflow

### Arbeiten mit Jupyter-Notebooks
1. Starten Sie Jupyter im Repository-Stammverzeichnis: `jupyter notebook`
2. Navigieren Sie zum gewünschten Lektionenordner
3. Öffnen Sie `.ipynb`-Dateien, um die Übungen durchzuarbeiten
4. Notebooks sind eigenständig mit Erklärungen und Codezellen
5. Die meisten Notebooks verwenden pandas, numpy und matplotlib – stellen Sie sicher, dass diese installiert sind

### Struktur der Lektionen
Jede Lektion enthält typischerweise:
- `README.md` - Hauptinhalt der Lektion mit Theorie und Beispielen
- `notebook.ipynb` - Praktische Übungen in Jupyter-Notebooks
- `assignment.ipynb` oder `assignment.md` - Übungsaufgaben
- `solution/`-Ordner - Lösungen und Code
- `images/`-Ordner - Unterstützende visuelle Materialien

### Entwicklung der Quiz-Anwendung
- Vue.js 2-Anwendung mit Hot-Reload während der Entwicklung
- Quizze gespeichert in `quiz-app/src/assets/translations/`
- Jede Sprache hat ihren eigenen Übersetzungsordner (en, fr, es usw.)
- Die Nummerierung der Quizze beginnt bei 0 und geht bis 39 (insgesamt 40 Quizze)

### Hinzufügen von Übersetzungen
- Übersetzungen befinden sich im `translations/`-Ordner im Repository-Stammverzeichnis
- Jede Sprache hat eine vollständige Lektionenstruktur, die der englischen Version entspricht
- Automatische Übersetzung über GitHub Actions (co-op-translator.yml)

## Testanweisungen

### Testen der Quiz-Anwendung
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### Testen der Notebooks
- Es gibt kein automatisiertes Testframework für Notebooks
- Manuelle Validierung: Führen Sie alle Zellen der Reihe nach aus, um sicherzustellen, dass keine Fehler auftreten
- Überprüfen Sie, ob die Datendateien zugänglich sind und die Ausgaben korrekt generiert werden
- Stellen Sie sicher, dass Visualisierungen ordnungsgemäß gerendert werden

### Testen der Dokumentation
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### Überprüfung der Codequalität
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## Richtlinien für den Programmierstil

### Python (Jupyter-Notebooks)
- Befolgen Sie die PEP 8-Stilrichtlinien für Python-Code
- Verwenden Sie klare Variablennamen, die die analysierten Daten beschreiben
- Fügen Sie Markdown-Zellen mit Erklärungen vor den Codezellen ein
- Halten Sie Codezellen auf einzelne Konzepte oder Operationen fokussiert
- Verwenden Sie pandas für Datenmanipulation, matplotlib für Visualisierungen
- Übliches Importmuster:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- Befolgen Sie den Vue.js 2-Stilguide und Best Practices
- ESLint-Konfiguration in `quiz-app/package.json`
- Verwenden Sie Vue-Single-File-Komponenten (.vue-Dateien)
- Beibehalten einer komponentenbasierten Architektur
- Führen Sie `npm run lint` aus, bevor Sie Änderungen einreichen

### Markdown-Dokumentation
- Verwenden Sie eine klare Überschriftenhierarchie (# ## ### usw.)
- Fügen Sie Codeblöcke mit Sprachspezifikatoren hinzu
- Fügen Sie Alt-Texte für Bilder hinzu
- Verlinken Sie auf verwandte Lektionen und Ressourcen
- Halten Sie die Zeilenlängen für die Lesbarkeit angemessen

### Dateiorganisation
- Lektioneninhalte in nummerierten Ordnern (01-defining-data-science usw.)
- Lösungen in dedizierten `solution/`-Unterordnern
- Übersetzungen spiegeln die englische Struktur im `translations/`-Ordner wider
- Datendateien in `data/` oder lektionenspezifischen Ordnern aufbewahren

## Build und Deployment

### Deployment der Quiz-Anwendung
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Deployment von Azure Static Web Apps
Die Quiz-App kann auf Azure Static Web Apps bereitgestellt werden:
1. Erstellen Sie eine Azure Static Web App-Ressource
2. Verbinden Sie sich mit dem GitHub-Repository
3. Konfigurieren Sie die Build-Einstellungen:
   - App-Standort: `quiz-app`
   - Ausgabe-Standort: `dist`
4. GitHub Actions-Workflow wird bei Push automatisch bereitgestellt

### Dokumentationsseite
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- Das Repository enthält eine Dev-Container-Konfiguration
- Codespaces richtet automatisch die Python- und Node.js-Umgebung ein
- Öffnen Sie das Repository in Codespaces über die GitHub-Benutzeroberfläche
- Alle Abhängigkeiten werden automatisch installiert

## Richtlinien für Pull Requests

### Vor dem Einreichen
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### Format des PR-Titels
- Verwenden Sie klare, beschreibende Titel
- Format: `[Komponente] Kurze Beschreibung`
- Beispiele:
  - `[Lektion 7] Fehler beim Import von Python-Notebook beheben`
  - `[Quiz-App] Deutsche Übersetzung hinzufügen`
  - `[Dokumentation] README mit neuen Voraussetzungen aktualisieren`

### Erforderliche Überprüfungen
- Stellen Sie sicher, dass der gesamte Code fehlerfrei ausgeführt wird
- Überprüfen Sie, ob Notebooks vollständig ausgeführt werden
- Bestätigen Sie, dass Vue.js-Anwendungen erfolgreich gebaut werden
- Überprüfen Sie, ob Dokumentationslinks funktionieren
- Testen Sie die Quiz-Anwendung, falls Änderungen vorgenommen wurden
- Stellen Sie sicher, dass Übersetzungen eine konsistente Struktur beibehalten

### Richtlinien für Beiträge
- Befolgen Sie den bestehenden Programmierstil und die Muster
- Fügen Sie erklärende Kommentare für komplexe Logik hinzu
- Aktualisieren Sie relevante Dokumentationen
- Testen Sie Änderungen in verschiedenen Lektionenmodulen, falls zutreffend
- Lesen Sie die Datei CONTRIBUTING.md

## Zusätzliche Hinweise

### Häufig verwendete Bibliotheken
- **pandas**: Datenmanipulation und -analyse
- **numpy**: Numerisches Rechnen
- **matplotlib**: Datenvisualisierung und -darstellung
- **seaborn**: Statistische Datenvisualisierung (einige Lektionen)
- **scikit-learn**: Maschinelles Lernen (fortgeschrittene Lektionen)

### Arbeiten mit Datendateien
- Datendateien befinden sich im Ordner `data/` oder in lektionenspezifischen Verzeichnissen
- Die meisten Notebooks erwarten Datendateien in relativen Pfaden
- CSV-Dateien sind das primäre Datenformat
- Einige Lektionen verwenden JSON für Beispiele mit nicht-relationalen Daten

### Mehrsprachige Unterstützung
- Über 40 Sprachübersetzungen über automatisierte GitHub Actions
- Übersetzungsworkflow in `.github/workflows/co-op-translator.yml`
- Übersetzungen im `translations/`-Ordner mit Sprachcodes
- Quiz-Übersetzungen in `quiz-app/src/assets/translations/`

### Optionen für Entwicklungsumgebungen
1. **Lokale Entwicklung**: Installieren Sie Python, Jupyter, Node.js lokal
2. **GitHub Codespaces**: Cloud-basierte, sofortige Entwicklungsumgebung
3. **VS Code Dev-Container**: Lokale containerbasierte Entwicklung
4. **Binder**: Starten Sie Notebooks in der Cloud (falls konfiguriert)

### Richtlinien für Lektioneninhalte
- Jede Lektion ist eigenständig, baut jedoch auf vorherigen Konzepten auf
- Vor-Lektions-Quizze testen Vorwissen
- Nach-Lektions-Quizze festigen das Gelernte
- Aufgaben bieten praktische Übungen
- Sketchnotes bieten visuelle Zusammenfassungen

### Behebung häufiger Probleme

**Probleme mit dem Jupyter-Kernel:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**Fehler bei npm-Installationen:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**Importfehler in Notebooks:**
- Überprüfen Sie, ob alle erforderlichen Bibliotheken installiert sind
- Prüfen Sie die Kompatibilität der Python-Version (Python 3.7+ empfohlen)
- Stellen Sie sicher, dass die virtuelle Umgebung aktiviert ist

**Docsify lädt nicht:**
- Überprüfen Sie, ob Sie vom Repository-Stamm aus bedienen
- Stellen Sie sicher, dass `index.html` vorhanden ist
- Überprüfen Sie den ordnungsgemäßen Netzwerkzugriff (Port 3000)

### Leistungshinweise
- Große Datensätze können in Notebooks Ladezeit beanspruchen
- Die Visualisierungsdarstellung kann bei komplexen Diagrammen langsam sein
- Der Vue.js-Entwicklungsserver ermöglicht Hot-Reload für schnelle Iterationen
- Produktions-Builds sind optimiert und minimiert

### Sicherheitshinweise
- Keine sensiblen Daten oder Anmeldedaten sollten eingecheckt werden
- Verwenden Sie Umgebungsvariablen für API-Schlüssel in Cloud-Lektionen
- Azure-bezogene Lektionen erfordern möglicherweise Azure-Kontoanmeldedaten
- Halten Sie Abhängigkeiten für Sicherheitspatches aktuell

## Beitrag zu Übersetzungen
- Automatische Übersetzungen werden über GitHub Actions verwaltet
- Manuelle Korrekturen zur Verbesserung der Übersetzungsgenauigkeit sind willkommen
- Befolgen Sie die bestehende Struktur der Übersetzungsordner
- Aktualisieren Sie Quiz-Links, um den Sprachparameter einzuschließen: `?loc=fr`
- Testen Sie übersetzte Lektionen auf korrekte Darstellung

## Verwandte Ressourcen
- Hauptlehrplan: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- Student Hub: https://docs.microsoft.com/learn/student-hub
- Diskussionsforum: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- Weitere Microsoft-Lehrpläne: ML for Beginners, AI for Beginners, Web Dev for Beginners

## Projektwartung
- Regelmäßige Updates, um Inhalte aktuell zu halten
- Beiträge aus der Community sind willkommen
- Probleme werden auf GitHub verfolgt
- PRs werden von Lehrplanbetreuern überprüft
- Monatliche Inhaltsüberprüfungen und -aktualisierungen

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.