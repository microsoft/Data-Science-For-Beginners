<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:14:09+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "de"
}
-->
# Installationsanleitung

Diese Anleitung hilft Ihnen, Ihre Umgebung für die Arbeit mit dem Data Science for Beginners-Lehrplan einzurichten.

## Inhaltsverzeichnis

- [Voraussetzungen](../..)
- [Schnellstart-Optionen](../..)
- [Lokale Installation](../..)
- [Installation überprüfen](../..)

## Voraussetzungen

Bevor Sie beginnen, sollten Sie Folgendes haben:

- Grundkenntnisse im Umgang mit der Kommandozeile/Terminal
- Ein GitHub-Konto (kostenlos)
- Stabile Internetverbindung für die Ersteinrichtung

## Schnellstart-Optionen

### Option 1: GitHub Codespaces (Empfohlen für Anfänger)

Der einfachste Weg, um zu starten, ist GitHub Codespaces, das eine vollständige Entwicklungsumgebung direkt in Ihrem Browser bereitstellt.

1. Gehen Sie zum [Repository](https://github.com/microsoft/Data-Science-For-Beginners)
2. Klicken Sie auf das Dropdown-Menü **Code**
3. Wählen Sie den Tab **Codespaces**
4. Klicken Sie auf **Create codespace on main**
5. Warten Sie, bis die Umgebung initialisiert ist (2-3 Minuten)

Ihre Umgebung ist jetzt bereit mit allen vorinstallierten Abhängigkeiten!

### Option 2: Lokale Entwicklung

Wenn Sie auf Ihrem eigenen Computer arbeiten möchten, folgen Sie den detaillierten Anweisungen unten.

## Lokale Installation

### Schritt 1: Git installieren

Git wird benötigt, um das Repository zu klonen und Ihre Änderungen zu verfolgen.

**Windows:**
- Herunterladen von [git-scm.com](https://git-scm.com/download/win)
- Führen Sie den Installer mit den Standardeinstellungen aus

**macOS:**
- Installation über Homebrew: `brew install git`
- Oder herunterladen von [git-scm.com](https://git-scm.com/download/mac)

**Linux:**
```bash
# Debian/Ubuntu
sudo apt-get update
sudo apt-get install git

# Fedora
sudo dnf install git

# Arch
sudo pacman -S git
```

### Schritt 2: Repository klonen

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### Schritt 3: Python und Jupyter installieren

Python 3.7 oder höher wird für die Data-Science-Lektionen benötigt.

**Windows:**
1. Laden Sie Python von [python.org](https://www.python.org/downloads/) herunter
2. Aktivieren Sie während der Installation die Option "Add Python to PATH"
3. Installation überprüfen:
```bash
python --version
```

**macOS:**
```bash
# Using Homebrew
brew install python3

# Verify installation
python3 --version
```

**Linux:**
```bash
# Most Linux distributions come with Python pre-installed
python3 --version

# If not installed:
# Debian/Ubuntu
sudo apt-get install python3 python3-pip

# Fedora
sudo dnf install python3 python3-pip
```

### Schritt 4: Python-Umgebung einrichten

Es wird empfohlen, eine virtuelle Umgebung zu verwenden, um Abhängigkeiten isoliert zu halten.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Schritt 5: Python-Pakete installieren

Installieren Sie die erforderlichen Data-Science-Bibliotheken:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Schritt 6: Node.js und npm installieren (für Quiz-App)

Die Quiz-Anwendung benötigt Node.js und npm.

**Windows/macOS:**
- Herunterladen von [nodejs.org](https://nodejs.org/) (LTS-Version empfohlen)
- Führen Sie den Installer aus

**Linux:**
```bash
# Debian/Ubuntu
# WARNING: Piping scripts from the internet directly into bash can be a security risk.
# It is recommended to review the script before running it:
#   curl -fsSL https://deb.nodesource.com/setup_lts.x -o setup_lts.x
#   less setup_lts.x
# Then run:
#   sudo -E bash setup_lts.x
#
# Alternatively, you can use the one-liner below at your own risk:
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs

# Fedora
sudo dnf install nodejs

# Verify installation
node --version
npm --version
```

### Schritt 7: Abhängigkeiten der Quiz-App installieren

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### Schritt 8: Docsify installieren (Optional)

Für den Offline-Zugriff auf die Dokumentation:

```bash
npm install -g docsify-cli
```

## Installation überprüfen

### Python und Jupyter testen

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

Ihr Browser sollte mit der Jupyter-Oberfläche geöffnet werden. Sie können nun zu einer beliebigen `.ipynb`-Datei einer Lektion navigieren.

### Quiz-Anwendung testen

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

Die Quiz-App sollte unter `http://localhost:8080` (oder einem anderen Port, falls 8080 belegt ist) verfügbar sein.

### Dokumentationsserver testen

```bash
# From the root directory of the repository
docsify serve
```

Die Dokumentation sollte unter `http://localhost:3000` verfügbar sein.

## Verwendung von VS Code Dev Containers

Wenn Sie Docker installiert haben, können Sie VS Code Dev Containers verwenden:

1. Installieren Sie [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Installieren Sie [Visual Studio Code](https://code.visualstudio.com/)
3. Installieren Sie die [Remote - Containers-Erweiterung](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. Öffnen Sie das Repository in VS Code
5. Drücken Sie `F1` und wählen Sie "Remote-Containers: Reopen in Container"
6. Warten Sie, bis der Container erstellt wird (nur beim ersten Mal)

## Nächste Schritte

- Erkunden Sie die [README.md](README.md) für einen Überblick über den Lehrplan
- Lesen Sie [USAGE.md](USAGE.md) für häufige Workflows und Beispiele
- Überprüfen Sie [TROUBLESHOOTING.md](TROUBLESHOOTING.md), falls Sie auf Probleme stoßen
- Sehen Sie sich [CONTRIBUTING.md](CONTRIBUTING.md) an, wenn Sie beitragen möchten

## Hilfe erhalten

Falls Sie auf Probleme stoßen:

1. Überprüfen Sie die [TROUBLESHOOTING.md](TROUBLESHOOTING.md)-Anleitung
2. Durchsuchen Sie bestehende [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Treten Sie unserer [Discord-Community](https://aka.ms/ds4beginners/discord) bei
4. Erstellen Sie ein neues Issue mit detaillierten Informationen zu Ihrem Problem

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.