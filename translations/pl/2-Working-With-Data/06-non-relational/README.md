<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "32ddfef8121650f2ca2f3416fd283c37",
  "translation_date": "2025-08-23T23:41:15+00:00",
  "source_file": "2-Working-With-Data/06-non-relational/README.md",
  "language_code": "pl"
}
-->
# Praca z danymi: Dane nierelacyjne

|![ Sketchnote autorstwa [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/06-NoSQL.png)|
|:---:|
|Praca z danymi NoSQL - _Sketchnote autorstwa [@nitya](https://twitter.com/nitya)_ |

## [Quiz przed wykładem](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/10)

Dane nie ograniczają się tylko do baz relacyjnych. Ta lekcja skupia się na danych nierelacyjnych i obejmuje podstawy arkuszy kalkulacyjnych oraz NoSQL.

## Arkusze kalkulacyjne

Arkusze kalkulacyjne są popularnym sposobem przechowywania i eksploracji danych, ponieważ wymagają mniej pracy przy konfiguracji i rozpoczęciu pracy. W tej lekcji poznasz podstawowe elementy arkusza kalkulacyjnego, a także formuły i funkcje. Przykłady będą ilustrowane za pomocą Microsoft Excel, ale większość elementów i tematów będzie miała podobne nazwy i kroki w porównaniu z innym oprogramowaniem do arkuszy kalkulacyjnych.

![Pusty skoroszyt Microsoft Excel z dwoma arkuszami](../../../../2-Working-With-Data/06-non-relational/images/parts-of-spreadsheet.png)

Arkusz kalkulacyjny to plik, który będzie dostępny w systemie plików komputera, urządzenia lub w chmurowym systemie plików. Samo oprogramowanie może być przeglądarkowe lub aplikacją, którą należy zainstalować na komputerze lub pobrać jako aplikację. W Excelu te pliki są również definiowane jako **skoroszyty**, i to określenie będzie używane w dalszej części tej lekcji.

Skoroszyt zawiera jeden lub więcej **arkuszy**, z których każdy jest oznaczony zakładkami. W arkuszu znajdują się prostokąty zwane **komórkami**, które zawierają rzeczywiste dane. Komórka to przecięcie wiersza i kolumny, gdzie kolumny są oznaczone literami alfabetu, a wiersze numerami. Niektóre arkusze kalkulacyjne zawierają nagłówki w pierwszych kilku wierszach, które opisują dane w komórce.

Z tymi podstawowymi elementami skoroszytu Excel, użyjemy przykładu z [Microsoft Templates](https://templates.office.com/) dotyczącego inwentarza, aby przejść przez dodatkowe elementy arkusza kalkulacyjnego.

### Zarządzanie inwentarzem

Plik arkusza kalkulacyjnego o nazwie "InventoryExample" to sformatowany arkusz z przedmiotami w inwentarzu, który zawiera trzy arkusze, oznaczone zakładkami "Inventory List", "Inventory Pick List" i "Bin Lookup". Wiersz 4 arkusza Inventory List to nagłówek, który opisuje wartość każdej komórki w kolumnie nagłówka.

![Podświetlona formuła z przykładowej listy inwentarza w Microsoft Excel](../../../../2-Working-With-Data/06-non-relational/images/formula-excel.png)

Są przypadki, gdy wartość komórki zależy od wartości innych komórek, aby wygenerować swoją wartość. Arkusz Inventory List śledzi koszt każdego przedmiotu w inwentarzu, ale co, jeśli chcemy znać wartość całego inwentarza? [**Formuły**](https://support.microsoft.com/en-us/office/overview-of-formulas-34519a4e-1e8d-4f4b-84d4-d642c4f63263) wykonują operacje na danych w komórkach i są używane do obliczania kosztu inwentarza w tym przykładzie. Ten arkusz używa formuły w kolumnie Inventory Value, aby obliczyć wartość każdego przedmiotu, mnożąc ilość pod nagłówkiem QTY przez koszt pod nagłówkiem COST. Podwójne kliknięcie lub zaznaczenie komórki pokaże formułę. Zauważysz, że formuły zaczynają się od znaku równości, po którym następuje obliczenie lub operacja.

![Podświetlona funkcja z przykładowej listy inwentarza w Microsoft Excel](../../../../2-Working-With-Data/06-non-relational/images/function-excel.png)

Możemy użyć innej formuły, aby dodać wszystkie wartości kolumny Inventory Value i uzyskać jej całkowitą wartość. Można to obliczyć, dodając każdą komórkę, aby uzyskać sumę, ale to może być żmudne zadanie. Excel posiada [**funkcje**](https://support.microsoft.com/en-us/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89), czyli predefiniowane formuły do wykonywania obliczeń na wartościach komórek. Funkcje wymagają argumentów, czyli wartości potrzebnych do wykonania obliczeń. Gdy funkcje wymagają więcej niż jednego argumentu, muszą być one wymienione w określonej kolejności, w przeciwnym razie funkcja może nie obliczyć poprawnej wartości. W tym przykładzie użyto funkcji SUM, która wykorzystuje wartości z kolumny Inventory Value jako argument, aby dodać je i wygenerować sumę podaną w wierszu 3, kolumnie B (znanej również jako B3).

## NoSQL

NoSQL to ogólny termin dla różnych sposobów przechowywania danych nierelacyjnych i może być interpretowany jako "non-SQL", "nierelacyjny" lub "nie tylko SQL". Tego typu systemy baz danych można podzielić na 4 kategorie.

![Graficzna reprezentacja bazy danych klucz-wartość pokazująca 4 unikalne klucze numeryczne powiązane z 4 różnymi wartościami](../../../../2-Working-With-Data/06-non-relational/images/kv-db.png)
> Źródło: [Blog Michała Białeckiego](https://www.michalbialecki.com/2018/03/18/azure-cosmos-db-key-value-database-cloud/)

Bazy danych [klucz-wartość](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#keyvalue-data-stores) łączą unikalne klucze, które są unikalnym identyfikatorem powiązanym z wartością. Te pary są przechowywane za pomocą [tablicy mieszającej](https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/) z odpowiednią funkcją mieszającą.

![Graficzna reprezentacja bazy danych grafowej pokazująca relacje między ludźmi, ich zainteresowaniami i lokalizacjami](../../../../2-Working-With-Data/06-non-relational/images/graph-db.png)
> Źródło: [Microsoft](https://docs.microsoft.com/en-us/azure/cosmos-db/graph/graph-introduction#graph-database-by-example)

Bazy danych [grafowe](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#graph-data-stores) opisują relacje w danych i są reprezentowane jako zbiór węzłów i krawędzi. Węzeł reprezentuje jednostkę, coś, co istnieje w rzeczywistości, na przykład studenta lub wyciąg bankowy. Krawędzie reprezentują relacje między dwiema jednostkami. Każdy węzeł i krawędź mają właściwości, które dostarczają dodatkowych informacji o każdym węźle i krawędzi.

![Graficzna reprezentacja bazy danych kolumnowej pokazująca bazę danych klientów z dwiema rodzinami kolumn nazwanymi Identity i Contact Info](../../../../2-Working-With-Data/06-non-relational/images/columnar-db.png)

Bazy danych [kolumnowe](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#columnar-data-stores) organizują dane w kolumny i wiersze, podobnie jak struktura danych relacyjnych, ale każda kolumna jest podzielona na grupy zwane rodzinami kolumn, gdzie wszystkie dane w jednej kolumnie są powiązane i mogą być pobierane oraz zmieniane jako jedna jednostka.

### Bazy danych dokumentów z Azure Cosmos DB

Bazy danych [dokumentów](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#document-data-stores) opierają się na koncepcji bazy danych klucz-wartość i składają się z serii pól i obiektów. W tej sekcji zbadamy bazy danych dokumentów za pomocą emulatora Cosmos DB.

Baza danych Cosmos DB spełnia definicję "Nie tylko SQL", gdzie baza danych dokumentów Cosmos DB opiera się na SQL do zapytań o dane. [Poprzednia lekcja](../05-relational-databases/README.md) dotycząca SQL obejmuje podstawy języka, a tutaj będziemy mogli zastosować niektóre z tych samych zapytań do bazy danych dokumentów. Użyjemy emulatora Cosmos DB, który pozwala na tworzenie i eksplorację bazy danych dokumentów lokalnie na komputerze. Przeczytaj więcej o emulatorze [tutaj](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21).

Dokument to zbiór pól i wartości obiektów, gdzie pola opisują, co reprezentuje wartość obiektu. Poniżej znajduje się przykład dokumentu.

```json
{
    "firstname": "Eva",
    "age": 44,
    "id": "8c74a315-aebf-4a16-bb38-2430a9896ce5",
    "_rid": "bHwDAPQz8s0BAAAAAAAAAA==",
    "_self": "dbs/bHwDAA==/colls/bHwDAPQz8s0=/docs/bHwDAPQz8s0BAAAAAAAAAA==/",
    "_etag": "\"00000000-0000-0000-9f95-010a691e01d7\"",
    "_attachments": "attachments/",
    "_ts": 1630544034
}
```

Pola, które nas interesują w tym dokumencie, to: `firstname`, `id` i `age`. Pozostałe pola z podkreśleniami zostały wygenerowane przez Cosmos DB.

#### Eksploracja danych za pomocą emulatora Cosmos DB

Możesz pobrać i zainstalować emulator [dla systemu Windows tutaj](https://aka.ms/cosmosdb-emulator). Odwołaj się do tej [dokumentacji](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21#run-on-linux-macos) w celu uzyskania opcji uruchamiania emulatora na macOS i Linux.

Emulator uruchamia okno przeglądarki, gdzie widok Explorer pozwala na eksplorację dokumentów.

![Widok Explorer emulatora Cosmos DB](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-explorer.png)

Jeśli podążasz za instrukcjami, kliknij "Start with Sample", aby wygenerować przykładową bazę danych o nazwie SampleDB. Jeśli rozwiniesz SampleDB, klikając strzałkę, znajdziesz kontener o nazwie `Persons`. Kontener przechowuje kolekcję elementów, które są dokumentami w kontenerze. Możesz eksplorować cztery indywidualne dokumenty w sekcji `Items`.

![Eksploracja przykładowych danych w emulatorze Cosmos DB](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-persons.png)

#### Zapytania o dane dokumentów za pomocą emulatora Cosmos DB

Możemy również wykonywać zapytania o przykładowe dane, klikając przycisk nowego zapytania SQL (drugi przycisk od lewej).

`SELECT * FROM c` zwraca wszystkie dokumenty w kontenerze. Dodajmy klauzulę WHERE i znajdźmy wszystkich, którzy mają mniej niż 40 lat.

`SELECT * FROM c where c.age < 40`

![Wykonywanie zapytania SELECT na przykładowych danych w emulatorze Cosmos DB, aby znaleźć dokumenty, których pole age ma wartość mniejszą niż 40](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-persons-query.png)

Zapytanie zwraca dwa dokumenty, zauważ, że wartość pola age w każdym dokumencie jest mniejsza niż 40.

#### JSON i dokumenty

Jeśli znasz JavaScript Object Notation (JSON), zauważysz, że dokumenty wyglądają podobnie do JSON. W tym katalogu znajduje się plik `PersonsData.json` z większą ilością danych, które możesz przesłać do kontenera Persons w emulatorze za pomocą przycisku `Upload Item`.

W większości przypadków API zwracające dane w formacie JSON mogą być bezpośrednio przenoszone i przechowywane w bazach danych dokumentów. Poniżej znajduje się kolejny dokument, który reprezentuje tweety z konta Microsoft na Twitterze, pobrane za pomocą API Twittera, a następnie wstawione do Cosmos DB.

```json
{
    "created_at": "2021-08-31T19:03:01.000Z",
    "id": "1432780985872142341",
    "text": "Blank slate. Like this tweet if you’ve ever painted in Microsoft Paint before. https://t.co/cFeEs8eOPK",
    "_rid": "dhAmAIUsA4oHAAAAAAAAAA==",
    "_self": "dbs/dhAmAA==/colls/dhAmAIUsA4o=/docs/dhAmAIUsA4oHAAAAAAAAAA==/",
    "_etag": "\"00000000-0000-0000-9f84-a0958ad901d7\"",
    "_attachments": "attachments/",
    "_ts": 1630537000
```

Pola, które nas interesują w tym dokumencie, to: `created_at`, `id` i `text`.

## 🚀 Wyzwanie

W katalogu znajduje się plik `TwitterData.json`, który możesz przesłać do bazy danych SampleDB. Zaleca się dodanie go do osobnego kontenera. Można to zrobić, wykonując następujące kroki:

1. Kliknij przycisk nowego kontenera w prawym górnym rogu.
2. Wybierz istniejącą bazę danych (SampleDB), utwórz identyfikator kontenera.
3. Ustaw klucz partycji na `/id`.
4. Kliknij OK (możesz zignorować resztę informacji w tym widoku, ponieważ jest to mały zestaw danych uruchamiany lokalnie na twoim komputerze).
5. Otwórz nowy kontener i prześlij plik Twitter Data za pomocą przycisku `Upload Item`.

Spróbuj wykonać kilka zapytań SELECT, aby znaleźć dokumenty, które zawierają słowo "Microsoft" w polu text. Wskazówka: spróbuj użyć [słowa kluczowego LIKE](https://docs.microsoft.com/en-us/azure/cosmos-db/sql/sql-query-keywords#using-like-with-the--wildcard-character).

## [Quiz po wykładzie](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/11)

## Przegląd i samodzielna nauka

- W tym arkuszu kalkulacyjnym dodano dodatkowe formatowanie i funkcje, które nie są omawiane w tej lekcji. Microsoft posiada [obszerną bibliotekę dokumentacji i filmów](https://support.microsoft.com/excel) na temat Excela, jeśli chcesz dowiedzieć się więcej.

- Ta dokumentacja architektoniczna szczegółowo opisuje cechy różnych typów danych nierelacyjnych: [Dane nierelacyjne i NoSQL](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data).

- Cosmos DB to chmurowa baza danych nierelacyjnych, która może również przechowywać różne typy NoSQL wspomniane w tej lekcji. Dowiedz się więcej o tych typach w tym [moduł Microsoft Learn dotyczący Cosmos DB](https://docs.microsoft.com/en-us/learn/paths/work-with-nosql-data-in-azure-cosmos-db/).

## Zadanie

[Soda Profits](assignment.md)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.