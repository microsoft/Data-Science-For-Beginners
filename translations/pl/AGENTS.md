<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:19:07+00:00",
  "source_file": "AGENTS.md",
  "language_code": "pl"
}
-->
# AGENTS.md

## Przegląd projektu

Data Science for Beginners to kompleksowy, 10-tygodniowy kurs składający się z 20 lekcji, stworzony przez Microsoft Azure Cloud Advocates. Repozytorium jest zasobem edukacyjnym, który uczy podstawowych pojęć z zakresu nauki o danych poprzez lekcje oparte na projektach, w tym notatniki Jupyter, interaktywne quizy i zadania praktyczne.

**Kluczowe technologie:**
- **Notatniki Jupyter**: Główne medium nauki z użyciem Python 3
- **Biblioteki Python**: pandas, numpy, matplotlib do analizy danych i wizualizacji
- **Vue.js 2**: Aplikacja quizowa (folder quiz-app)
- **Docsify**: Generator strony dokumentacji do użytku offline
- **Node.js/npm**: Zarządzanie pakietami dla komponentów JavaScript
- **Markdown**: Cała treść lekcji i dokumentacja

**Architektura:**
- Repozytorium edukacyjne w wielu językach z obszernymi tłumaczeniami
- Struktura podzielona na moduły lekcji (1-Introduction do 6-Data-Science-In-Wild)
- Każda lekcja zawiera README, notatniki, zadania i quizy
- Samodzielna aplikacja quizowa Vue.js do oceny przed/po lekcji
- Wsparcie dla GitHub Codespaces i kontenerów deweloperskich VS Code

## Polecenia konfiguracji

### Konfiguracja repozytorium
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### Konfiguracja środowiska Python
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Konfiguracja aplikacji quizowej
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

### Serwer dokumentacji Docsify
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### Konfiguracja projektów wizualizacyjnych
Dla projektów wizualizacyjnych, takich jak meaningful-visualizations (lekcja 13):
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


## Przebieg pracy deweloperskiej

### Praca z notatnikami Jupyter
1. Uruchom Jupyter w katalogu głównym repozytorium: `jupyter notebook`
2. Przejdź do odpowiedniego folderu lekcji
3. Otwórz pliki `.ipynb`, aby przejść przez ćwiczenia
4. Notatniki są samodzielne, zawierają wyjaśnienia i komórki kodu
5. Większość notatników używa pandas, numpy i matplotlib - upewnij się, że są zainstalowane

### Struktura lekcji
Każda lekcja zazwyczaj zawiera:
- `README.md` - Główna treść lekcji z teorią i przykładami
- `notebook.ipynb` - Ćwiczenia praktyczne w notatniku Jupyter
- `assignment.ipynb` lub `assignment.md` - Zadania praktyczne
- Folder `solution/` - Notatniki z rozwiązaniami i kod
- Folder `images/` - Materiały wizualne wspierające

### Rozwój aplikacji quizowej
- Aplikacja Vue.js 2 z funkcją hot-reload podczas rozwoju
- Quizy przechowywane w `quiz-app/src/assets/translations/`
- Każdy język ma własny folder tłumaczeń (en, fr, es, itd.)
- Numeracja quizów zaczyna się od 0 i kończy na 39 (łącznie 40 quizów)

### Dodawanie tłumaczeń
- Tłumaczenia umieszczane w folderze `translations/` w katalogu głównym repozytorium
- Każdy język ma pełną strukturę lekcji odzwierciedloną z angielskiego
- Automatyczne tłumaczenie za pomocą GitHub Actions (co-op-translator.yml)

## Instrukcje testowania

### Testowanie aplikacji quizowej
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### Testowanie notatników
- Nie istnieje automatyczny framework testowy dla notatników
- Walidacja ręczna: Uruchom wszystkie komórki w kolejności, aby upewnić się, że nie ma błędów
- Sprawdź dostępność plików danych i poprawność generowanych wyników
- Upewnij się, że wizualizacje renderują się poprawnie

### Testowanie dokumentacji
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### Kontrola jakości kodu
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## Wytyczne dotyczące stylu kodu

### Python (Notatniki Jupyter)
- Przestrzegaj wytycznych stylu PEP 8 dla kodu Python
- Używaj jasnych nazw zmiennych, które opisują analizowane dane
- Dodawaj komórki markdown z wyjaśnieniami przed komórkami kodu
- Skup komórki kodu na pojedynczych koncepcjach lub operacjach
- Używaj pandas do manipulacji danymi, matplotlib do wizualizacji
- Typowy wzorzec importu:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- Przestrzegaj wytycznych stylu Vue.js 2 i najlepszych praktyk
- Konfiguracja ESLint w `quiz-app/package.json`
- Używaj komponentów Vue w pojedynczych plikach (.vue)
- Utrzymuj architekturę opartą na komponentach
- Uruchom `npm run lint` przed zatwierdzeniem zmian

### Dokumentacja Markdown
- Używaj jasnej hierarchii nagłówków (# ## ### itd.)
- Dodawaj bloki kodu ze specyfikatorami języka
- Dodawaj tekst alternatywny dla obrazów
- Linkuj do powiązanych lekcji i zasobów
- Zachowaj rozsądną długość linii dla czytelności

### Organizacja plików
- Treść lekcji w ponumerowanych folderach (01-defining-data-science, itd.)
- Rozwiązania w dedykowanych podfolderach `solution/`
- Tłumaczenia odzwierciedlają strukturę angielską w folderze `translations/`
- Pliki danych w folderze `data/` lub specyficznych dla lekcji

## Budowa i wdrożenie

### Wdrożenie aplikacji quizowej
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Wdrożenie Azure Static Web Apps
Aplikacja quizowa może być wdrożona na Azure Static Web Apps:
1. Utwórz zasób Azure Static Web App
2. Połącz z repozytorium GitHub
3. Skonfiguruj ustawienia budowy:
   - Lokalizacja aplikacji: `quiz-app`
   - Lokalizacja wynikowa: `dist`
4. Workflow GitHub Actions automatycznie wdroży zmiany po ich przesłaniu

### Strona dokumentacji
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- Repozytorium zawiera konfigurację kontenera deweloperskiego
- Codespaces automatycznie konfiguruje środowisko Python i Node.js
- Otwórz repozytorium w Codespace za pomocą interfejsu GitHub
- Wszystkie zależności instalują się automatycznie

## Wytyczne dotyczące pull requestów

### Przed przesłaniem
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### Format tytułu PR
- Używaj jasnych, opisowych tytułów
- Format: `[Komponent] Krótki opis`
- Przykłady:
  - `[Lekcja 7] Napraw błąd importu w notatniku Python`
  - `[Aplikacja Quizowa] Dodaj tłumaczenie na niemiecki`
  - `[Dokumentacja] Zaktualizuj README o nowe wymagania wstępne`

### Wymagane kontrole
- Upewnij się, że cały kod działa bez błędów
- Zweryfikuj, że notatniki wykonują się w całości
- Potwierdź, że aplikacje Vue.js budują się poprawnie
- Sprawdź, czy linki w dokumentacji działają
- Przetestuj aplikację quizową, jeśli została zmodyfikowana
- Zweryfikuj, że tłumaczenia zachowują spójną strukturę

### Wytyczne dotyczące wkładu
- Przestrzegaj istniejącego stylu kodu i wzorców
- Dodawaj wyjaśniające komentarze dla złożonej logiki
- Aktualizuj odpowiednią dokumentację
- Testuj zmiany w różnych modułach lekcji, jeśli to możliwe
- Przejrzyj plik CONTRIBUTING.md

## Dodatkowe uwagi

### Często używane biblioteki
- **pandas**: Manipulacja i analiza danych
- **numpy**: Obliczenia numeryczne
- **matplotlib**: Wizualizacja danych i wykresy
- **seaborn**: Wizualizacja danych statystycznych (niektóre lekcje)
- **scikit-learn**: Uczenie maszynowe (lekcje zaawansowane)

### Praca z plikami danych
- Pliki danych znajdują się w folderze `data/` lub w katalogach specyficznych dla lekcji
- Większość notatników oczekuje plików danych w ścieżkach względnych
- Pliki CSV są głównym formatem danych
- Niektóre lekcje używają JSON dla przykładów danych nierelacyjnych

### Wsparcie wielojęzyczne
- Ponad 40 tłumaczeń językowych za pomocą automatycznych GitHub Actions
- Workflow tłumaczeń w `.github/workflows/co-op-translator.yml`
- Tłumaczenia w folderze `translations/` z kodami języków
- Tłumaczenia quizów w `quiz-app/src/assets/translations/`

### Opcje środowiska deweloperskiego
1. **Rozwój lokalny**: Zainstaluj Python, Jupyter, Node.js lokalnie
2. **GitHub Codespaces**: Środowisko rozwoju w chmurze
3. **Kontenery deweloperskie VS Code**: Lokalny rozwój oparty na kontenerach
4. **Binder**: Uruchamianie notatników w chmurze (jeśli skonfigurowane)

### Wytyczne dotyczące treści lekcji
- Każda lekcja jest samodzielna, ale buduje na poprzednich koncepcjach
- Quizy przed lekcją sprawdzają wcześniejszą wiedzę
- Quizy po lekcji wzmacniają naukę
- Zadania zapewniają praktykę
- Sketchnotes oferują wizualne podsumowania

### Rozwiązywanie typowych problemów

**Problemy z Jupyter Kernel:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**Problemy z instalacją npm:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**Błędy importu w notatnikach:**
- Upewnij się, że wszystkie wymagane biblioteki są zainstalowane
- Sprawdź zgodność wersji Python (zalecany Python 3.7+)
- Upewnij się, że środowisko wirtualne jest aktywowane

**Docsify nie ładuje się:**
- Upewnij się, że serwujesz z katalogu głównego repozytorium
- Sprawdź, czy istnieje plik `index.html`
- Upewnij się, że masz odpowiedni dostęp do sieci (port 3000)

### Uwagi dotyczące wydajności
- Duże zestawy danych mogą długo się ładować w notatnikach
- Renderowanie wizualizacji może być wolne dla złożonych wykresów
- Serwer deweloperski Vue.js umożliwia szybkie iteracje dzięki hot-reload
- Kompilacje produkcyjne są zoptymalizowane i zminimalizowane

### Uwagi dotyczące bezpieczeństwa
- Nie należy przesyłać danych wrażliwych ani poświadczeń
- Używaj zmiennych środowiskowych dla kluczy API w lekcjach chmurowych
- Lekcje związane z Azure mogą wymagać poświadczeń konta Azure
- Aktualizuj zależności dla poprawek bezpieczeństwa

## Wkład w tłumaczenia
- Automatyczne tłumaczenia zarządzane za pomocą GitHub Actions
- Mile widziane ręczne poprawki dla dokładności tłumaczeń
- Przestrzegaj istniejącej struktury folderów tłumaczeń
- Aktualizuj linki do quizów, aby zawierały parametr języka: `?loc=fr`
- Testuj przetłumaczone lekcje pod kątem poprawnego renderowania

## Powiązane zasoby
- Główna ścieżka nauczania: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- Student Hub: https://docs.microsoft.com/learn/student-hub
- Forum dyskusyjne: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- Inne kursy Microsoft: ML for Beginners, AI for Beginners, Web Dev for Beginners

## Utrzymanie projektu
- Regularne aktualizacje, aby treść była aktualna
- Mile widziane wkłady społeczności
- Problemy śledzone na GitHub
- PR-y przeglądane przez opiekunów programu nauczania
- Miesięczne przeglądy i aktualizacje treści

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.