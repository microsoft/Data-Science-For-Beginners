<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "870a0086adbc313a8eea5489bdcb2522",
  "translation_date": "2025-08-23T23:23:54+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "pl"
}
-->
# Praca z danymi: Relacyjne bazy danych

|![ Sketchnote autorstwa [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Praca z danymi: Relacyjne bazy danych - _Sketchnote autorstwa [@nitya](https://twitter.com/nitya)_ |

Prawdopodobnie w przeszłości korzystałeś z arkusza kalkulacyjnego do przechowywania informacji. Miałeś zestaw wierszy i kolumn, gdzie wiersze zawierały informacje (lub dane), a kolumny opisywały te informacje (czasami nazywane metadanymi). Relacyjna baza danych opiera się na tej podstawowej zasadzie kolumn i wierszy w tabelach, umożliwiając rozproszenie informacji na wiele tabel. Dzięki temu możesz pracować z bardziej złożonymi danymi, unikać duplikacji i mieć większą elastyczność w eksploracji danych. Przyjrzyjmy się koncepcjom relacyjnej bazy danych.

## [Quiz przed wykładem](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/8)

## Wszystko zaczyna się od tabel

Relacyjna baza danych opiera się na tabelach. Podobnie jak w arkuszu kalkulacyjnym, tabela to zbiór kolumn i wierszy. Wiersz zawiera dane lub informacje, z którymi chcemy pracować, takie jak nazwa miasta czy ilość opadów. Kolumny opisują dane, które przechowują.

Zacznijmy naszą eksplorację od stworzenia tabeli do przechowywania informacji o miastach. Możemy zacząć od ich nazwy i kraju. Możesz przechowywać to w tabeli w następujący sposób:

| Miasto   | Kraj          |
| -------- | ------------- |
| Tokio    | Japonia       |
| Atlanta  | Stany Zjednoczone |
| Auckland | Nowa Zelandia |

Zwróć uwagę, że nazwy kolumn **miasto**, **kraj** i **populacja** opisują przechowywane dane, a każdy wiersz zawiera informacje o jednym mieście.

## Ograniczenia podejścia z jedną tabelą

Prawdopodobnie powyższa tabela wydaje się dość znajoma. Dodajmy teraz dodatkowe dane do naszej rozwijającej się bazy danych - roczne opady (w milimetrach). Skupimy się na latach 2018, 2019 i 2020. Jeśli mielibyśmy dodać dane dla Tokio, mogłoby to wyglądać tak:

| Miasto | Kraj    | Rok  | Ilość |
| ------ | ------- | ---- | ----- |
| Tokio  | Japonia | 2020 | 1690  |
| Tokio  | Japonia | 2019 | 1874  |
| Tokio  | Japonia | 2018 | 1445  |

Co zauważasz w naszej tabeli? Możesz zauważyć, że powtarzamy nazwę i kraj miasta wielokrotnie. Może to zajmować sporo miejsca i jest w dużej mierze niepotrzebne. W końcu Tokio ma tylko jedną nazwę, która nas interesuje.

OK, spróbujmy czegoś innego. Dodajmy nowe kolumny dla każdego roku:

| Miasto   | Kraj          | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokio    | Japonia       | 1445 | 1874 | 1690 |
| Atlanta  | Stany Zjednoczone | 1779 | 1111 | 1683 |
| Auckland | Nowa Zelandia | 1386 | 942  | 1176 |

Chociaż unika to duplikacji wierszy, wprowadza kilka innych wyzwań. Musielibyśmy modyfikować strukturę naszej tabeli za każdym razem, gdy pojawi się nowy rok. Dodatkowo, w miarę wzrostu danych, posiadanie lat jako kolumn utrudniłoby ich pobieranie i obliczanie wartości.

Dlatego potrzebujemy wielu tabel i relacji. Dzieląc nasze dane, możemy unikać duplikacji i mieć większą elastyczność w pracy z nimi.

## Koncepcje relacji

Wróćmy do naszych danych i zdecydujmy, jak je podzielić. Wiemy, że chcemy przechowywać nazwę i kraj naszych miast, więc najlepiej będzie to zrobić w jednej tabeli.

| Miasto   | Kraj          |
| -------- | ------------- |
| Tokio    | Japonia       |
| Atlanta  | Stany Zjednoczone |
| Auckland | Nowa Zelandia |

Ale zanim stworzymy następną tabelę, musimy ustalić, jak odwoływać się do każdego miasta. Potrzebujemy jakiejś formy identyfikatora, ID lub (w technicznych terminach baz danych) klucza głównego. Klucz główny to wartość używana do identyfikacji jednego konkretnego wiersza w tabeli. Chociaż może to być oparte na samej wartości (moglibyśmy na przykład użyć nazwy miasta), powinien to być prawie zawsze numer lub inny identyfikator. Nie chcemy, aby identyfikator kiedykolwiek się zmieniał, ponieważ złamałoby to relację. W większości przypadków klucz główny lub identyfikator będzie automatycznie generowanym numerem.

> ✅ Klucz główny jest często skracany jako PK

### miasta

| city_id | Miasto   | Kraj          |
| ------- | -------- | ------------- |
| 1       | Tokio    | Japonia       |
| 2       | Atlanta  | Stany Zjednoczone |
| 3       | Auckland | Nowa Zelandia |

> ✅ Zauważysz, że w tej lekcji używamy zamiennie terminów "id" i "klucz główny". Koncepcje te mają zastosowanie do DataFrames, które poznasz później. DataFrames nie używają terminologii "klucz główny", jednak zauważysz, że zachowują się w bardzo podobny sposób.

Po utworzeniu tabeli **miasta**, przechowajmy dane o opadach. Zamiast duplikować pełne informacje o mieście, możemy użyć identyfikatora. Powinniśmy również upewnić się, że nowo utworzona tabela ma kolumnę *id*, ponieważ wszystkie tabele powinny mieć identyfikator lub klucz główny.

### opady

| rainfall_id | city_id | Rok  | Ilość |
| ----------- | ------- | ---- | ----- |
| 1           | 1       | 2018 | 1445  |
| 2           | 1       | 2019 | 1874  |
| 3           | 1       | 2020 | 1690  |
| 4           | 2       | 2018 | 1779  |
| 5           | 2       | 2019 | 1111  |
| 6           | 2       | 2020 | 1683  |
| 7           | 3       | 2018 | 1386  |
| 8           | 3       | 2019 | 942   |
| 9           | 3       | 2020 | 1176  |

Zwróć uwagę na kolumnę **city_id** w nowo utworzonej tabeli **opady**. Ta kolumna zawiera wartości, które odnoszą się do identyfikatorów w tabeli **miasta**. W technicznych terminach relacyjnych danych nazywa się to **kluczem obcym**; jest to klucz główny z innej tabeli. Możesz myśleć o tym jako o odniesieniu lub wskaźniku. **city_id** 1 odnosi się do Tokio.

> [!NOTE] Klucz obcy jest często skracany jako FK

## Pobieranie danych

Mając dane podzielone na dwie tabele, możesz się zastanawiać, jak je pobrać. Jeśli używamy relacyjnej bazy danych, takiej jak MySQL, SQL Server lub Oracle, możemy użyć języka o nazwie Structured Query Language lub SQL. SQL (czasami wymawiane jako "sequel") to standardowy język używany do pobierania i modyfikowania danych w relacyjnej bazie danych.

Aby pobrać dane, używasz polecenia `SELECT`. W swojej podstawowej formie **wybierasz** kolumny, które chcesz zobaczyć **z** tabeli, w której się znajdują. Jeśli chciałbyś wyświetlić tylko nazwy miast, możesz użyć następującego zapytania:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` to miejsce, gdzie wymieniasz kolumny, a `FROM` to miejsce, gdzie wymieniasz tabele.

> [NOTE] Składnia SQL nie rozróżnia wielkości liter, co oznacza, że `select` i `SELECT` oznaczają to samo. Jednak w zależności od typu bazy danych, której używasz, kolumny i tabele mogą być wrażliwe na wielkość liter. W rezultacie najlepszą praktyką jest zawsze traktowanie wszystkiego w programowaniu tak, jakby było wrażliwe na wielkość liter. Podczas pisania zapytań SQL powszechną konwencją jest używanie słów kluczowych wielkimi literami.

Powyższe zapytanie wyświetli wszystkie miasta. Wyobraźmy sobie, że chcemy wyświetlić tylko miasta w Nowej Zelandii. Potrzebujemy jakiejś formy filtra. Słowem kluczowym SQL do tego celu jest `WHERE`, czyli "gdzie coś jest prawdziwe".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Łączenie danych

Do tej pory pobieraliśmy dane z jednej tabeli. Teraz chcemy połączyć dane z tabel **miasta** i **opady**. Robi się to poprzez *łączenie* ich razem. W efekcie tworzysz "szew" między dwiema tabelami i dopasowujesz wartości z kolumny z każdej tabeli.

W naszym przykładzie dopasujemy kolumnę **city_id** w tabeli **opady** do kolumny **city_id** w tabeli **miasta**. To dopasuje wartość opadów do odpowiedniego miasta. Typ łączenia, który wykonamy, to tzw. *łączenie wewnętrzne* (inner join), co oznacza, że jeśli jakiekolwiek wiersze nie pasują do niczego z drugiej tabeli, nie zostaną wyświetlone. W naszym przypadku każde miasto ma dane o opadach, więc wszystko zostanie wyświetlone.

Pobierzmy dane o opadach z 2019 roku dla wszystkich naszych miast.

Zrobimy to krokami. Pierwszym krokiem jest połączenie danych, wskazując kolumny dla "szwu" - **city_id**, jak podkreślono wcześniej.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Podkreśliliśmy dwie kolumny, które chcemy, oraz fakt, że chcemy połączyć tabele za pomocą **city_id**. Teraz możemy dodać instrukcję `WHERE`, aby odfiltrować tylko rok 2019.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
WHERE rainfall.year = 2019

-- Output

-- city     | amount
-- -------- | ------
-- Tokyo    | 1874
-- Atlanta  | 1111
-- Auckland |  942
```

## Podsumowanie

Relacyjne bazy danych opierają się na podziale informacji między wiele tabel, które następnie są łączone w celu wyświetlania i analizy. Zapewnia to dużą elastyczność w wykonywaniu obliczeń i manipulowaniu danymi. Poznałeś podstawowe koncepcje relacyjnej bazy danych oraz sposób wykonywania łączenia między dwiema tabelami.

## 🚀 Wyzwanie

W internecie dostępnych jest wiele relacyjnych baz danych. Możesz eksplorować dane, korzystając z umiejętności, które zdobyłeś powyżej.

## Quiz po wykładzie

## [Quiz po wykładzie](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/9)

## Przegląd i samodzielna nauka

Na [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) dostępnych jest wiele zasobów, które pozwolą Ci kontynuować eksplorację SQL i koncepcji relacyjnych baz danych.

- [Opis koncepcji danych relacyjnych](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Rozpocznij pracę z zapytaniami w Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL to wersja SQL)
- [Treści SQL na Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Zadanie

[Temat zadania](assignment.md)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.