<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10f86fb29b5407088445ac803b3d0ed1",
  "translation_date": "2025-10-03T13:20:00+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "de"
}
-->
# Beitrag zu Data Science für Anfänger

Vielen Dank für Ihr Interesse, zum Lehrplan "Data Science für Anfänger" beizutragen! Wir freuen uns über Beiträge aus der Community.

## Inhaltsverzeichnis

- [Verhaltenskodex](../..)
- [Wie kann ich beitragen?](../..)
- [Erste Schritte](../..)
- [Richtlinien für Beiträge](../..)
- [Ablauf für Pull Requests](../..)
- [Stilrichtlinien](../..)
- [Contributor License Agreement](../..)

## Verhaltenskodex

Dieses Projekt hat den [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) übernommen.  
Weitere Informationen finden Sie in den [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/)  
oder kontaktieren Sie [opencode@microsoft.com](mailto:opencode@microsoft.com) bei weiteren Fragen oder Kommentaren.

## Wie kann ich beitragen?

### Fehler melden

Bevor Sie Fehlerberichte erstellen, überprüfen Sie bitte die vorhandenen Issues, um Duplikate zu vermeiden. Wenn Sie einen Fehler melden, geben Sie so viele Details wie möglich an:

- **Verwenden Sie einen klaren und beschreibenden Titel**
- **Beschreiben Sie die genauen Schritte, um das Problem zu reproduzieren**
- **Geben Sie konkrete Beispiele an** (Code-Snippets, Screenshots)
- **Beschreiben Sie das beobachtete Verhalten und was Sie erwartet haben**
- **Fügen Sie Details zu Ihrer Umgebung hinzu** (Betriebssystem, Python-Version, Browser)

### Verbesserungsvorschläge

Vorschläge zur Verbesserung sind willkommen! Wenn Sie Verbesserungen vorschlagen:

- **Verwenden Sie einen klaren und beschreibenden Titel**
- **Geben Sie eine detaillierte Beschreibung der vorgeschlagenen Verbesserung**
- **Erklären Sie, warum diese Verbesserung nützlich wäre**
- **Listen Sie ähnliche Funktionen in anderen Projekten auf, falls zutreffend**

### Beitrag zur Dokumentation

Verbesserungen der Dokumentation sind immer willkommen:

- **Korrigieren Sie Rechtschreib- und Grammatikfehler**
- **Verbessern Sie die Klarheit von Erklärungen**
- **Fügen Sie fehlende Dokumentation hinzu**
- **Aktualisieren Sie veraltete Informationen**
- **Fügen Sie Beispiele oder Anwendungsfälle hinzu**

### Beitrag zum Code

Wir freuen uns über Code-Beiträge, einschließlich:

- **Neue Lektionen oder Übungen**
- **Fehlerbehebungen**
- **Verbesserungen an bestehenden Notebooks**
- **Neue Datensätze oder Beispiele**
- **Erweiterungen der Quiz-Anwendung**

## Erste Schritte

### Voraussetzungen

Bevor Sie beitragen, stellen Sie sicher, dass Sie Folgendes haben:

1. Ein GitHub-Konto
2. Git auf Ihrem System installiert
3. Python 3.7+ und Jupyter installiert
4. Node.js und npm (für Beiträge zur Quiz-App)
5. Vertrautheit mit der Struktur des Lehrplans

Siehe [INSTALLATION.md](INSTALLATION.md) für detaillierte Installationsanweisungen.

### Fork und Klonen

1. **Forken Sie das Repository** auf GitHub  
2. **Klonen Sie Ihren Fork** lokal:  
   ```bash
   git clone https://github.com/YOUR-USERNAME/Data-Science-For-Beginners.git
   cd Data-Science-For-Beginners
   ```
  
3. **Fügen Sie das Upstream-Remote hinzu**:  
   ```bash
   git remote add upstream https://github.com/microsoft/Data-Science-For-Beginners.git
   ```
  

### Erstellen eines Branches

Erstellen Sie einen neuen Branch für Ihre Arbeit:  
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```
  
Branch-Namenskonventionen:  
- `feature/` - Neue Funktionen oder Lektionen  
- `fix/` - Fehlerbehebungen  
- `docs/` - Änderungen an der Dokumentation  
- `refactor/` - Code-Refaktorierung  

## Richtlinien für Beiträge

### Für Lektionen

Wenn Sie Lektionen beitragen oder bestehende ändern:

1. **Folgen Sie der bestehenden Struktur**:
   - README.md mit Lektioneninhalt
   - Jupyter-Notebook mit Übungen
   - Aufgabe (falls zutreffend)
   - Link zu Vor- und Nachtests

2. **Fügen Sie diese Elemente hinzu**:
   - Klare Lernziele
   - Schritt-für-Schritt-Erklärungen
   - Code-Beispiele mit Kommentaren
   - Übungen zum Üben
   - Links zu zusätzlichen Ressourcen

3. **Stellen Sie Barrierefreiheit sicher**:
   - Verwenden Sie klare, einfache Sprache
   - Geben Sie Alt-Text für Bilder an
   - Fügen Sie Code-Kommentare hinzu
   - Berücksichtigen Sie unterschiedliche Lernstile

### Für Jupyter-Notebooks

1. **Löschen Sie alle Ausgaben**, bevor Sie Änderungen einreichen:  
   ```bash
   jupyter nbconvert --clear-output --inplace notebook.ipynb
   ```
  
2. **Fügen Sie Markdown-Zellen** mit Erklärungen hinzu  

3. **Verwenden Sie einheitliche Formatierung**:  
   ```python
   # Import libraries at the top
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   
   # Use meaningful variable names
   # Add comments for complex operations
   # Follow PEP 8 style guidelines
   ```
  
4. **Testen Sie Ihr Notebook** vollständig, bevor Sie es einreichen  

### Für Python-Code

Befolgen Sie die [PEP 8](https://www.python.org/dev/peps/pep-0008/) Stilrichtlinien:  
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
  

### Für Beiträge zur Quiz-App

Wenn Sie die Quiz-Anwendung ändern:

1. **Testen Sie lokal**:  
   ```bash
   cd quiz-app
   npm install
   npm run serve
   ```
  
2. **Führen Sie den Linter aus**:  
   ```bash
   npm run lint
   ```
  
3. **Erfolgreich bauen**:  
   ```bash
   npm run build
   ```
  
4. **Befolgen Sie die Vue.js-Stilrichtlinien** und bestehende Muster  

### Für Übersetzungen

Wenn Sie Übersetzungen hinzufügen oder aktualisieren:

1. Folgen Sie der Struktur im `translations/`-Ordner  
2. Verwenden Sie den Sprachcode als Ordnernamen (z. B. `fr` für Französisch)  
3. Behalten Sie die gleiche Dateistruktur wie die englische Version bei  
4. Aktualisieren Sie Quiz-Links, um den Sprachparameter einzuschließen: `?loc=fr`  
5. Testen Sie alle Links und die Formatierung  

## Ablauf für Pull Requests

### Vor dem Einreichen

1. **Aktualisieren Sie Ihren Branch** mit den neuesten Änderungen:  
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```
  
2. **Testen Sie Ihre Änderungen**:
   - Führen Sie alle geänderten Notebooks aus
   - Testen Sie die Quiz-App, falls geändert
   - Überprüfen Sie, ob alle Links funktionieren
   - Prüfen Sie auf Rechtschreib- und Grammatikfehler

3. **Committen Sie Ihre Änderungen**:  
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```
  
   Schreiben Sie klare Commit-Nachrichten:
   - Verwenden Sie die Gegenwartsform ("Füge Funktion hinzu" statt "Funktion hinzugefügt")
   - Verwenden Sie den Imperativ ("Bewege Cursor zu..." statt "Bewegt Cursor zu...")
   - Begrenzen Sie die erste Zeile auf 72 Zeichen
   - Verweisen Sie auf Issues und Pull Requests, wenn relevant

4. **Pushen Sie zu Ihrem Fork**:  
   ```bash
   git push origin feature/your-feature-name
   ```
  

### Erstellen des Pull Requests

1. Gehen Sie zum [Repository](https://github.com/microsoft/Data-Science-For-Beginners)  
2. Klicken Sie auf "Pull requests" → "New pull request"  
3. Klicken Sie auf "compare across forks"  
4. Wählen Sie Ihren Fork und Branch aus  
5. Klicken Sie auf "Create pull request"  

### Format des PR-Titels

Verwenden Sie klare, beschreibende Titel nach diesem Format:  
```
[Component] Brief description
```
  
Beispiele:  
- `[Lesson 7] Fix Python notebook import error`  
- `[Quiz App] Add German translation`  
- `[Docs] Update README with new prerequisites`  
- `[Fix] Correct data path in visualization lesson`  

### PR-Beschreibung

Fügen Sie Ihrer PR-Beschreibung Folgendes hinzu:

- **Was**: Welche Änderungen haben Sie vorgenommen?  
- **Warum**: Warum sind diese Änderungen notwendig?  
- **Wie**: Wie haben Sie die Änderungen implementiert?  
- **Tests**: Wie haben Sie die Änderungen getestet?  
- **Screenshots**: Fügen Sie Screenshots für visuelle Änderungen hinzu  
- **Verwandte Issues**: Verlinken Sie verwandte Issues (z. B. "Fixes #123")  

### Überprüfungsprozess

1. **Automatische Checks** werden für Ihre PR ausgeführt  
2. **Maintainer überprüfen** Ihren Beitrag  
3. **Feedback bearbeiten** durch zusätzliche Commits  
4. Nach Genehmigung wird Ihre PR von einem **Maintainer gemergt**  

### Nach dem Merge Ihrer PR

1. Löschen Sie Ihren Branch:  
   ```bash
   git branch -d feature/your-feature-name
   git push origin --delete feature/your-feature-name
   ```
  
2. Aktualisieren Sie Ihren Fork:  
   ```bash
   git checkout main
   git pull upstream main
   git push origin main
   ```
  

## Stilrichtlinien

### Markdown

- Verwenden Sie konsistente Überschriftenebenen  
- Fügen Sie Leerzeilen zwischen Abschnitten ein  
- Verwenden Sie Code-Blöcke mit Sprachspezifikatoren:  
  ````markdown
  ```python
  import pandas as pd
  ```
  ````
  
- Fügen Sie Alt-Text zu Bildern hinzu: `![Alt-Text](../../translated_images/image.4ee84a82b5e4c9e6651b13fd27dcf615e427ec584929f2cef7167aa99151a77a.de.png)`  
- Halten Sie die Zeilenlänge vernünftig (ca. 80-100 Zeichen)  

### Python

- Befolgen Sie die PEP 8 Stilrichtlinien  
- Verwenden Sie aussagekräftige Variablennamen  
- Fügen Sie Docstrings zu Funktionen hinzu  
- Fügen Sie Typ-Hinweise hinzu, wo angebracht:  
  ```python
  def process_data(df: pd.DataFrame) -> pd.DataFrame:
      """Process the input dataframe."""
      return df
  ```
  

### JavaScript/Vue.js

- Befolgen Sie die Vue.js 2 Stilrichtlinien  
- Verwenden Sie die bereitgestellte ESLint-Konfiguration  
- Schreiben Sie modulare, wiederverwendbare Komponenten  
- Fügen Sie Kommentare für komplexe Logik hinzu  

### Dateiorganisation

- Halten Sie zusammengehörige Dateien zusammen  
- Verwenden Sie beschreibende Dateinamen  
- Folgen Sie der bestehenden Verzeichnisstruktur  
- Committen Sie keine unnötigen Dateien (.DS_Store, .pyc, node_modules, etc.)  

## Contributor License Agreement

Dieses Projekt begrüßt Beiträge und Vorschläge. Die meisten Beiträge erfordern, dass Sie einer Contributor License Agreement (CLA) zustimmen, die erklärt, dass Sie das Recht haben und tatsächlich die Rechte gewähren, Ihren Beitrag zu nutzen. Weitere Details finden Sie unter  
https://cla.microsoft.com.

Wenn Sie einen Pull Request einreichen, wird ein CLA-Bot automatisch feststellen, ob Sie eine CLA bereitstellen müssen, und den PR entsprechend kennzeichnen (z. B. Label, Kommentar). Folgen Sie einfach den Anweisungen des Bots. Sie müssen dies nur einmal für alle Repositories tun, die unsere CLA verwenden.

## Fragen?

- Besuchen Sie unseren [Discord-Kanal #data-science-for-beginners](https://aka.ms/ds4beginners/discord)  
- Treten Sie unserer [Discord-Community](https://aka.ms/ds4beginners/discord) bei  
- Überprüfen Sie vorhandene [Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) und [Pull Requests](https://github.com/microsoft/Data-Science-For-Beginners/pulls)  

## Vielen Dank!

Ihre Beiträge machen diesen Lehrplan für alle besser. Vielen Dank, dass Sie sich die Zeit nehmen, beizutragen!

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.