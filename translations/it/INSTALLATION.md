<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:19:47+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "it"
}
-->
# Guida all'Installazione

Questa guida ti aiuterà a configurare l'ambiente per lavorare con il curriculum "Data Science for Beginners".

## Indice

- [Prerequisiti](../..)
- [Opzioni di Avvio Rapido](../..)
- [Installazione Locale](../..)
- [Verifica dell'Installazione](../..)

## Prerequisiti

Prima di iniziare, dovresti avere:

- Familiarità di base con la riga di comando/terminale
- Un account GitHub (gratuito)
- Connessione internet stabile per la configurazione iniziale

## Opzioni di Avvio Rapido

### Opzione 1: GitHub Codespaces (Consigliato per Principianti)

Il modo più semplice per iniziare è con GitHub Codespaces, che offre un ambiente di sviluppo completo direttamente nel browser.

1. Vai al [repository](https://github.com/microsoft/Data-Science-For-Beginners)
2. Clicca sul menu a discesa **Code**
3. Seleziona la scheda **Codespaces**
4. Clicca su **Create codespace on main**
5. Attendi l'inizializzazione dell'ambiente (2-3 minuti)

Il tuo ambiente è ora pronto con tutte le dipendenze pre-installate!

### Opzione 2: Sviluppo Locale

Per lavorare sul tuo computer, segui le istruzioni dettagliate qui sotto.

## Installazione Locale

### Passo 1: Installa Git

Git è necessario per clonare il repository e tracciare le modifiche.

**Windows:**
- Scarica da [git-scm.com](https://git-scm.com/download/win)
- Esegui l'installer con le impostazioni predefinite

**macOS:**
- Installa tramite Homebrew: `brew install git`
- Oppure scarica da [git-scm.com](https://git-scm.com/download/mac)

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

### Passo 2: Clona il Repository

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### Passo 3: Installa Python e Jupyter

Python 3.7 o superiore è richiesto per le lezioni di data science.

**Windows:**
1. Scarica Python da [python.org](https://www.python.org/downloads/)
2. Durante l'installazione, seleziona "Add Python to PATH"
3. Verifica l'installazione:
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

### Passo 4: Configura l'Ambiente Python

Si consiglia di utilizzare un ambiente virtuale per mantenere le dipendenze isolate.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Passo 5: Installa i Pacchetti Python

Installa le librerie necessarie per la data science:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Passo 6: Installa Node.js e npm (Per l'App Quiz)

L'app quiz richiede Node.js e npm.

**Windows/macOS:**
- Scarica da [nodejs.org](https://nodejs.org/) (versione LTS consigliata)
- Esegui l'installer

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

### Passo 7: Installa le Dipendenze dell'App Quiz

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### Passo 8: Installa Docsify (Opzionale)

Per accedere alla documentazione offline:

```bash
npm install -g docsify-cli
```

## Verifica dell'Installazione

### Test Python e Jupyter

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

Il tuo browser dovrebbe aprirsi con l'interfaccia Jupyter. Ora puoi navigare verso qualsiasi file `.ipynb` delle lezioni.

### Test dell'App Quiz

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

L'app quiz dovrebbe essere disponibile su `http://localhost:8080` (o un'altra porta se 8080 è occupata).

### Test del Server di Documentazione

```bash
# From the root directory of the repository
docsify serve
```

La documentazione dovrebbe essere disponibile su `http://localhost:3000`.

## Utilizzo dei Contenitori Dev di VS Code

Se hai Docker installato, puoi utilizzare i Contenitori Dev di VS Code:

1. Installa [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Installa [Visual Studio Code](https://code.visualstudio.com/)
3. Installa l'estensione [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. Apri il repository in VS Code
5. Premi `F1` e seleziona "Remote-Containers: Reopen in Container"
6. Attendi la costruzione del contenitore (solo la prima volta)

## Prossimi Passi

- Esplora il [README.md](README.md) per una panoramica del curriculum
- Leggi [USAGE.md](USAGE.md) per flussi di lavoro comuni ed esempi
- Controlla [TROUBLESHOOTING.md](TROUBLESHOOTING.md) se incontri problemi
- Consulta [CONTRIBUTING.md](CONTRIBUTING.md) se vuoi contribuire

## Ottenere Aiuto

Se incontri problemi:

1. Controlla la guida [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
2. Cerca tra i [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) esistenti
3. Unisciti alla nostra [community su Discord](https://aka.ms/ds4beginners/discord)
4. Crea un nuovo issue con informazioni dettagliate sul tuo problema

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un esperto umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.