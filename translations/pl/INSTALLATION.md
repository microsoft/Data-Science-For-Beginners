<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:20:04+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "pl"
}
-->
# Przewodnik instalacji

Ten przewodnik pomoże Ci skonfigurować środowisko do pracy z programem nauczania "Data Science for Beginners".

## Spis treści

- [Wymagania wstępne](../..)
- [Opcje szybkiego startu](../..)
- [Instalacja lokalna](../..)
- [Weryfikacja instalacji](../..)

## Wymagania wstępne

Przed rozpoczęciem powinieneś:

- Mieć podstawową znajomość pracy z wierszem poleceń/terminalem
- Posiadać konto GitHub (bezpłatne)
- Mieć stabilne połączenie internetowe do początkowej konfiguracji

## Opcje szybkiego startu

### Opcja 1: GitHub Codespaces (zalecane dla początkujących)

Najłatwiejszym sposobem na rozpoczęcie jest GitHub Codespaces, który oferuje kompletne środowisko programistyczne w przeglądarce.

1. Przejdź do [repozytorium](https://github.com/microsoft/Data-Science-For-Beginners)
2. Kliknij menu rozwijane **Code**
3. Wybierz zakładkę **Codespaces**
4. Kliknij **Create codespace on main**
5. Poczekaj na inicjalizację środowiska (2-3 minuty)

Twoje środowisko jest teraz gotowe z zainstalowanymi wszystkimi zależnościami!

### Opcja 2: Rozwój lokalny

Aby pracować na własnym komputerze, postępuj zgodnie z poniższymi szczegółowymi instrukcjami.

## Instalacja lokalna

### Krok 1: Zainstaluj Git

Git jest wymagany do sklonowania repozytorium i śledzenia zmian.

**Windows:**
- Pobierz z [git-scm.com](https://git-scm.com/download/win)
- Uruchom instalator z domyślnymi ustawieniami

**macOS:**
- Zainstaluj za pomocą Homebrew: `brew install git`
- Lub pobierz z [git-scm.com](https://git-scm.com/download/mac)

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

### Krok 2: Sklonuj repozytorium

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### Krok 3: Zainstaluj Python i Jupyter

Python w wersji 3.7 lub wyższej jest wymagany do lekcji z zakresu nauki o danych.

**Windows:**
1. Pobierz Python z [python.org](https://www.python.org/downloads/)
2. Podczas instalacji zaznacz opcję "Add Python to PATH"
3. Zweryfikuj instalację:
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

### Krok 4: Skonfiguruj środowisko Python

Zaleca się użycie wirtualnego środowiska, aby izolować zależności.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Krok 5: Zainstaluj pakiety Python

Zainstaluj wymagane biblioteki do nauki o danych:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Krok 6: Zainstaluj Node.js i npm (dla aplikacji quizowej)

Aplikacja quizowa wymaga Node.js i npm.

**Windows/macOS:**
- Pobierz z [nodejs.org](https://nodejs.org/) (zalecana wersja LTS)
- Uruchom instalator

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

### Krok 7: Zainstaluj zależności aplikacji quizowej

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### Krok 8: Zainstaluj Docsify (opcjonalne)

Dla dostępu offline do dokumentacji:

```bash
npm install -g docsify-cli
```

## Weryfikacja instalacji

### Test Python i Jupyter

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

Twoja przeglądarka powinna otworzyć interfejs Jupyter. Możesz teraz przejść do dowolnego pliku `.ipynb` z lekcji.

### Test aplikacji quizowej

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

Aplikacja quizowa powinna być dostępna pod adresem `http://localhost:8080` (lub innym, jeśli port 8080 jest zajęty).

### Test serwera dokumentacji

```bash
# From the root directory of the repository
docsify serve
```

Dokumentacja powinna być dostępna pod adresem `http://localhost:3000`.

## Korzystanie z kontenerów Dev w VS Code

Jeśli masz zainstalowany Docker, możesz użyć kontenerów Dev w VS Code:

1. Zainstaluj [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Zainstaluj [Visual Studio Code](https://code.visualstudio.com/)
3. Zainstaluj rozszerzenie [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. Otwórz repozytorium w VS Code
5. Naciśnij `F1` i wybierz "Remote-Containers: Reopen in Container"
6. Poczekaj na zbudowanie kontenera (tylko za pierwszym razem)

## Kolejne kroki

- Przeglądaj [README.md](README.md) dla ogólnego przeglądu programu nauczania
- Przeczytaj [USAGE.md](USAGE.md) dla typowych przepływów pracy i przykładów
- Sprawdź [TROUBLESHOOTING.md](TROUBLESHOOTING.md), jeśli napotkasz problemy
- Przejrzyj [CONTRIBUTING.md](CONTRIBUTING.md), jeśli chcesz wnieść swój wkład

## Uzyskiwanie pomocy

Jeśli napotkasz problemy:

1. Sprawdź przewodnik [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
2. Przeszukaj istniejące [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Dołącz do naszej [społeczności Discord](https://aka.ms/ds4beginners/discord)
4. Utwórz nowy problem, podając szczegółowe informacje o swoim problemie

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku źródłowym powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.