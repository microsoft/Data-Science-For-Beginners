<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f2d7693f28e4b2675f275e489dc5aac",
  "translation_date": "2025-08-23T23:25:53+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "pl"
}
-->
# Wyświetlanie danych o lotniskach

Otrzymałeś [bazę danych](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) opartą na [SQLite](https://sqlite.org/index.html), która zawiera informacje o lotniskach. Schemat bazy danych jest przedstawiony poniżej. Użyjesz [rozszerzenia SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) w [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum), aby wyświetlić informacje o lotniskach w różnych miastach.

## Instrukcje

Aby rozpocząć zadanie, musisz wykonać kilka kroków. Będziesz musiał zainstalować odpowiednie narzędzia i pobrać przykładową bazę danych.

### Przygotowanie systemu

Możesz użyć Visual Studio Code i rozszerzenia SQLite, aby pracować z bazą danych.

1. Przejdź na stronę [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) i postępuj zgodnie z instrukcjami, aby zainstalować Visual Studio Code
1. Zainstaluj [rozszerzenie SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) zgodnie z instrukcjami na stronie Marketplace

### Pobierz i otwórz bazę danych

Następnie pobierz i otwórz bazę danych.

1. Pobierz [plik bazy danych z GitHuba](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) i zapisz go w wybranym katalogu
1. Otwórz Visual Studio Code
1. Otwórz bazę danych w rozszerzeniu SQLite, wybierając **Ctl-Shift-P** (lub **Cmd-Shift-P** na Macu) i wpisując `SQLite: Open database`
1. Wybierz **Choose database from file** i otwórz plik **airports.db**, który wcześniej pobrałeś
1. Po otwarciu bazy danych (nie zobaczysz żadnej zmiany na ekranie), utwórz nowe okno zapytań, wybierając **Ctl-Shift-P** (lub **Cmd-Shift-P** na Macu) i wpisując `SQLite: New query`

Po otwarciu nowego okna zapytań możesz używać go do wykonywania instrukcji SQL na bazie danych. Aby uruchomić zapytania, możesz użyć polecenia **Ctl-Shift-Q** (lub **Cmd-Shift-Q** na Macu).

> [!NOTE] Aby uzyskać więcej informacji o rozszerzeniu SQLite, możesz zapoznać się z [dokumentacją](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## Schemat bazy danych

Schemat bazy danych to jej projekt i struktura tabel. Baza danych **airports** zawiera dwie tabele: `cities`, która zawiera listę miast w Wielkiej Brytanii i Irlandii, oraz `airports`, która zawiera listę wszystkich lotnisk. Ponieważ niektóre miasta mogą mieć wiele lotnisk, utworzono dwie tabele do przechowywania tych informacji. W tym ćwiczeniu użyjesz połączeń (joins), aby wyświetlić informacje o różnych miastach.

| Cities           |
| ---------------- |
| id (PK, integer) |
| city (text)      |
| country (text)   |

| Airports                         |
| -------------------------------- |
| id (PK, integer)                 |
| name (text)                      |
| code (text)                      |
| city_id (FK to id in **Cities**) |

## Zadanie

Utwórz zapytania, które zwrócą następujące informacje:

1. wszystkie nazwy miast w tabeli `Cities`
1. wszystkie miasta w Irlandii w tabeli `Cities`
1. wszystkie nazwy lotnisk wraz z ich miastem i krajem
1. wszystkie lotniska w Londynie, Wielka Brytania

## Kryteria oceny

| Wzorowe       | Wystarczające | Wymaga poprawy |
| ------------- | ------------- | --------------- |

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby zapewnić poprawność tłumaczenia, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.