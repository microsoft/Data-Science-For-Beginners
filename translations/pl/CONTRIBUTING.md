<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10f86fb29b5407088445ac803b3d0ed1",
  "translation_date": "2025-10-03T13:57:46+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "pl"
}
-->
# Współtworzenie Data Science dla Początkujących

Dziękujemy za zainteresowanie współtworzeniem programu nauczania Data Science dla Początkujących! Zapraszamy do współpracy całą społeczność.

## Spis Treści

- [Kodeks Postępowania](../..)
- [Jak Mogę Współtworzyć?](../..)
- [Pierwsze Kroki](../..)
- [Zasady Współtworzenia](../..)
- [Proces Pull Request](../..)
- [Zasady Stylu](../..)
- [Umowa Licencyjna Współtwórcy](../..)

## Kodeks Postępowania

Ten projekt przyjął [Kodeks Postępowania Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/).  
Więcej informacji znajdziesz w [FAQ dotyczących Kodeksu Postępowania](https://opensource.microsoft.com/codeofconduct/faq/)  
lub skontaktuj się z [opencode@microsoft.com](mailto:opencode@microsoft.com), jeśli masz dodatkowe pytania lub uwagi.

## Jak Mogę Współtworzyć?

### Zgłaszanie Błędów

Przed zgłoszeniem błędu sprawdź istniejące zgłoszenia, aby uniknąć duplikatów. Podczas zgłaszania błędu podaj jak najwięcej szczegółów:

- **Użyj jasnego i opisowego tytułu**
- **Opisz dokładne kroki prowadzące do wystąpienia problemu**
- **Podaj konkretne przykłady** (fragmenty kodu, zrzuty ekranu)
- **Opisz zaobserwowane zachowanie i oczekiwane rezultaty**
- **Podaj szczegóły dotyczące środowiska** (system operacyjny, wersja Pythona, przeglądarka)

### Proponowanie Ulepszeń

Sugestie dotyczące ulepszeń są mile widziane! Podczas ich zgłaszania:

- **Użyj jasnego i opisowego tytułu**
- **Podaj szczegółowy opis proponowanego ulepszenia**
- **Wyjaśnij, dlaczego to ulepszenie byłoby przydatne**
- **Wymień podobne funkcje w innych projektach, jeśli to możliwe**

### Współtworzenie Dokumentacji

Poprawki w dokumentacji są zawsze mile widziane:

- **Popraw literówki i błędy gramatyczne**
- **Zwiększ przejrzystość wyjaśnień**
- **Dodaj brakującą dokumentację**
- **Zaktualizuj przestarzałe informacje**
- **Dodaj przykłady lub przypadki użycia**

### Współtworzenie Kodów

Zapraszamy do współtworzenia kodu, w tym:

- **Nowych lekcji lub ćwiczeń**
- **Poprawek błędów**
- **Ulepszeń istniejących notebooków**
- **Nowych zestawów danych lub przykładów**
- **Ulepszeń aplikacji quizowej**

## Pierwsze Kroki

### Wymagania Wstępne

Przed rozpoczęciem współtworzenia upewnij się, że masz:

1. Konto GitHub
2. Zainstalowany Git na swoim systemie
3. Python 3.7+ i Jupyter zainstalowane
4. Node.js i npm (do współtworzenia aplikacji quizowej)
5. Znajomość struktury programu nauczania

Zobacz [INSTALLATION.md](INSTALLATION.md) dla szczegółowych instrukcji instalacji.

### Fork i Klonowanie

1. **Zrób fork repozytorium** na GitHub
2. **Sklonuj swój fork** lokalnie:  
   ```bash
   git clone https://github.com/YOUR-USERNAME/Data-Science-For-Beginners.git
   cd Data-Science-For-Beginners
   ```
  
3. **Dodaj upstream remote**:  
   ```bash
   git remote add upstream https://github.com/microsoft/Data-Science-For-Beginners.git
   ```
  

### Utwórz Gałąź

Utwórz nową gałąź dla swojej pracy:  
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```
  
Konwencje nazewnictwa gałęzi:  
- `feature/` - Nowe funkcje lub lekcje  
- `fix/` - Poprawki błędów  
- `docs/` - Zmiany w dokumentacji  
- `refactor/` - Refaktoryzacja kodu  

## Zasady Współtworzenia

### Dla Treści Lekcji

Podczas współtworzenia lekcji lub modyfikowania istniejących:

1. **Przestrzegaj istniejącej struktury**:
   - README.md z treścią lekcji
   - Notebook Jupyter z ćwiczeniami
   - Zadanie (jeśli dotyczy)
   - Linki do quizów przed i po lekcji

2. **Uwzględnij następujące elementy**:
   - Jasne cele nauczania
   - Wyjaśnienia krok po kroku
   - Przykłady kodu z komentarzami
   - Ćwiczenia do praktyki
   - Linki do dodatkowych zasobów

3. **Zapewnij dostępność**:
   - Używaj jasnego, prostego języka
   - Dodaj tekst alternatywny do obrazów
   - Uwzględnij komentarze w kodzie
   - Rozważ różne style uczenia się

### Dla Notebooków Jupyter

1. **Wyczyść wszystkie wyniki** przed zatwierdzeniem:  
   ```bash
   jupyter nbconvert --clear-output --inplace notebook.ipynb
   ```
  
2. **Dodaj komórki markdown** z wyjaśnieniami  

3. **Używaj spójnego formatowania**:  
   ```python
   # Import libraries at the top
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   
   # Use meaningful variable names
   # Add comments for complex operations
   # Follow PEP 8 style guidelines
   ```
  
4. **Przetestuj swój notebook** w całości przed przesłaniem  

### Dla Kodów Pythona

Przestrzegaj zasad stylu [PEP 8](https://www.python.org/dev/peps/pep-0008/):  
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
  

### Dla Współtworzenia Aplikacji Quizowej

Podczas modyfikowania aplikacji quizowej:

1. **Przetestuj lokalnie**:  
   ```bash
   cd quiz-app
   npm install
   npm run serve
   ```
  
2. **Uruchom linter**:  
   ```bash
   npm run lint
   ```
  
3. **Zbuduj pomyślnie**:  
   ```bash
   npm run build
   ```
  
4. **Przestrzegaj wytycznych stylu Vue.js** i istniejących wzorców  

### Dla Tłumaczeń

Podczas dodawania lub aktualizowania tłumaczeń:

1. Przestrzegaj struktury w folderze `translations/`  
2. Używaj kodu języka jako nazwy folderu (np. `fr` dla francuskiego)  
3. Zachowaj tę samą strukturę plików co wersja angielska  
4. Zaktualizuj linki do quizów, aby zawierały parametr języka: `?loc=fr`  
5. Przetestuj wszystkie linki i formatowanie  

## Proces Pull Request

### Przed Przesłaniem

1. **Zaktualizuj swoją gałąź** o najnowsze zmiany:  
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```
  
2. **Przetestuj swoje zmiany**:
   - Uruchom wszystkie zmodyfikowane notebooki
   - Przetestuj aplikację quizową, jeśli została zmodyfikowana
   - Zweryfikuj działanie wszystkich linków
   - Sprawdź błędy ortograficzne i gramatyczne

3. **Zatwierdź swoje zmiany**:  
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```
  
   Pisz jasne komunikaty zatwierdzeń:
   - Używaj czasu teraźniejszego ("Dodaj funkcję", a nie "Dodano funkcję")
   - Używaj trybu rozkazującego ("Przenieś kursor do...", a nie "Przenosi kursor do...")
   - Ogranicz pierwszą linię do 72 znaków
   - Odnoś się do zgłoszeń i pull requestów, jeśli to istotne

4. **Wypchnij do swojego forka**:  
   ```bash
   git push origin feature/your-feature-name
   ```
  

### Tworzenie Pull Request

1. Przejdź do [repozytorium](https://github.com/microsoft/Data-Science-For-Beginners)  
2. Kliknij "Pull requests" → "New pull request"  
3. Kliknij "compare across forks"  
4. Wybierz swój fork i gałąź  
5. Kliknij "Create pull request"  

### Format Tytułu PR

Używaj jasnych, opisowych tytułów w następującym formacie:  
```
[Component] Brief description
```
  
Przykłady:  
- `[Lesson 7] Fix Python notebook import error`  
- `[Quiz App] Add German translation`  
- `[Docs] Update README with new prerequisites`  
- `[Fix] Correct data path in visualization lesson`  

### Opis PR

W opisie PR uwzględnij:

- **Co**: Jakie zmiany wprowadziłeś?  
- **Dlaczego**: Dlaczego te zmiany są konieczne?  
- **Jak**: Jak zaimplementowałeś zmiany?  
- **Testowanie**: Jak przetestowałeś zmiany?  
- **Zrzuty ekranu**: Dodaj zrzuty ekranu dla zmian wizualnych  
- **Powiązane Zgłoszenia**: Podaj linki do powiązanych zgłoszeń (np. "Fixes #123")  

### Proces Przeglądu

1. **Automatyczne sprawdzenia** zostaną uruchomione na Twoim PR  
2. **Opiekunowie projektu przejrzą** Twój wkład  
3. **Odpowiedz na uwagi** poprzez dodanie kolejnych zatwierdzeń  
4. Po zatwierdzeniu, **opiekun projektu połączy** Twój PR  

### Po Połączeniu Twojego PR

1. Usuń swoją gałąź:  
   ```bash
   git branch -d feature/your-feature-name
   git push origin --delete feature/your-feature-name
   ```
  
2. Zaktualizuj swój fork:  
   ```bash
   git checkout main
   git pull upstream main
   git push origin main
   ```
  

## Zasady Stylu

### Markdown

- Używaj spójnych poziomów nagłówków  
- Dodawaj puste linie między sekcjami  
- Używaj bloków kodu ze specyfikacją języka:  
  ````markdown
  ```python
  import pandas as pd
  ```
  ````
  
- Dodawaj tekst alternatywny do obrazów: `![Alt text](../../translated_images/image.4ee84a82b5e4c9e6651b13fd27dcf615e427ec584929f2cef7167aa99151a77a.pl.png)`  
- Zachowuj rozsądną długość linii (około 80-100 znaków)  

### Python

- Przestrzegaj wytycznych stylu PEP 8  
- Używaj znaczących nazw zmiennych  
- Dodawaj docstringi do funkcji  
- Uwzględniaj wskazówki typów, jeśli to możliwe:  
  ```python
  def process_data(df: pd.DataFrame) -> pd.DataFrame:
      """Process the input dataframe."""
      return df
  ```
  

### JavaScript/Vue.js

- Przestrzegaj wytycznych stylu Vue.js 2  
- Używaj konfiguracji ESLint dostarczonej w projekcie  
- Pisz modułowe, wielokrotnego użytku komponenty  
- Dodawaj komentarze do złożonej logiki  

### Organizacja Plików

- Trzymaj powiązane pliki razem  
- Używaj opisowych nazw plików  
- Przestrzegaj istniejącej struktury katalogów  
- Nie zatwierdzaj niepotrzebnych plików (.DS_Store, .pyc, node_modules, itp.)  

## Umowa Licencyjna Współtwórcy

Ten projekt zaprasza do współtworzenia i składania sugestii. Większość wkładów wymaga od Ciebie  
zgody na Umowę Licencyjną Współtwórcy (CLA), która deklaruje, że masz prawo do  
i faktycznie udzielasz nam prawa do korzystania z Twojego wkładu. Szczegóły znajdziesz na  
https://cla.microsoft.com.  

Podczas przesyłania pull requestu, bot CLA automatycznie określi, czy musisz  
podpisać CLA i odpowiednio oznaczy PR (np. etykieta, komentarz). Wystarczy postępować zgodnie z  
instrukcjami podanymi przez bota. Musisz to zrobić tylko raz dla wszystkich repozytoriów korzystających z naszego CLA.  

## Pytania?

- Sprawdź nasz [Kanał Discord #data-science-for-beginners](https://aka.ms/ds4beginners/discord)  
- Dołącz do naszej [społeczności Discord](https://aka.ms/ds4beginners/discord)  
- Przejrzyj istniejące [zgłoszenia](https://github.com/microsoft/Data-Science-For-Beginners/issues) i [pull requesty](https://github.com/microsoft/Data-Science-For-Beginners/pulls)  

## Dziękujemy!

Twoje wkłady sprawiają, że ten program nauczania staje się lepszy dla wszystkich. Dziękujemy za poświęcony czas na współtworzenie!

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.