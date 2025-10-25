<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80d80300002ef4e77cc7631d5904bd6e",
  "translation_date": "2025-10-25T18:50:49+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "pl"
}
-->
# Praca z danymi: Relacyjne bazy danych

|![ Sketchnote autorstwa [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Praca z danymi: Relacyjne bazy danych - _Sketchnote autorstwa [@nitya](https://twitter.com/nitya)_ |

Prawdopodobnie używałeś kiedyś arkusza kalkulacyjnego do przechowywania informacji. Miałeś zestaw wierszy i kolumn, gdzie wiersze zawierały informacje (lub dane), a kolumny opisywały te informacje (czasami nazywane metadanymi). Relacyjna baza danych opiera się na tej podstawowej zasadzie kolumn i wierszy w tabelach, co pozwala na przechowywanie informacji w wielu tabelach. Dzięki temu można pracować z bardziej złożonymi danymi, unikać ich duplikacji i mieć większą elastyczność w eksploracji danych. Przyjrzyjmy się koncepcjom relacyjnej bazy danych.

## [Quiz przed wykładem](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## Wszystko zaczyna się od tabel

Relacyjna baza danych opiera się na tabelach. Podobnie jak w przypadku arkusza kalkulacyjnego, tabela to zbiór kolumn i wierszy. Wiersz zawiera dane lub informacje, z którymi chcemy pracować, takie jak nazwa miasta czy ilość opadów. Kolumny opisują dane, które przechowują.

Zacznijmy naszą eksplorację od utworzenia tabeli do przechowywania informacji o miastach. Możemy zacząć od ich nazw i krajów. Można to przechowywać w tabeli w następujący sposób:

| Miasto   | Kraj          |
| -------- | ------------- |
| Tokio    | Japonia       |
| Atlanta  | Stany Zjednoczone |
| Auckland | Nowa Zelandia |

Zauważ, że nazwy kolumn **miasto**, **kraj** i **populacja** opisują przechowywane dane, a każdy wiersz zawiera informacje o jednym mieście.

## Ograniczenia podejścia z jedną tabelą

Prawdopodobnie powyższa tabela wydaje się dość znajoma. Zacznijmy dodawać dodatkowe dane do naszej rozwijającej się bazy danych - roczne opady (w milimetrach). Skupimy się na latach 2018, 2019 i 2020. Jeśli mielibyśmy dodać dane dla Tokio, mogłoby to wyglądać tak:

| Miasto | Kraj   | Rok  | Ilość  |
| ------ | ------ | ---- | ------ |
| Tokio  | Japonia| 2020 | 1690   |
| Tokio  | Japonia| 2019 | 1874   |
| Tokio  | Japonia| 2018 | 1445   |

Co zauważasz w naszej tabeli? Możesz zauważyć, że powtarzamy nazwę i kraj miasta wielokrotnie. Może to zajmować sporo miejsca i w dużej mierze jest niepotrzebne, ponieważ Tokio ma tylko jedną nazwę, która nas interesuje.

OK, spróbujmy czegoś innego. Dodajmy nowe kolumny dla każdego roku:

| Miasto   | Kraj          | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokio    | Japonia       | 1445 | 1874 | 1690 |
| Atlanta  | Stany Zjednoczone | 1779 | 1111 | 1683 |
| Auckland | Nowa Zelandia | 1386 | 942  | 1176 |

Chociaż to unika duplikacji wierszy, dodaje kilka innych wyzwań. Musielibyśmy zmieniać strukturę naszej tabeli za każdym razem, gdy pojawi się nowy rok. Dodatkowo, gdy nasze dane się rozrosną, posiadanie lat jako kolumn utrudni ich pobieranie i obliczanie wartości.

Dlatego potrzebujemy wielu tabel i relacji. Rozdzielając nasze dane, możemy uniknąć duplikacji i mieć większą elastyczność w pracy z nimi.

## Koncepcje relacji

Wróćmy do naszych danych i zdecydujmy, jak je podzielić. Wiemy, że chcemy przechowywać nazwę i kraj naszych miast, więc prawdopodobnie najlepiej będzie to zrobić w jednej tabeli.

| Miasto   | Kraj          |
| -------- | ------------- |
| Tokio    | Japonia       |
| Atlanta  | Stany Zjednoczone |
| Auckland | Nowa Zelandia |

Ale zanim stworzymy następną tabelę, musimy ustalić, jak odwoływać się do każdego miasta. Potrzebujemy jakiejś formy identyfikatora, ID lub (w technicznych terminach baz danych) klucza głównego. Klucz główny to wartość używana do identyfikacji jednego konkretnego wiersza w tabeli. Chociaż może być oparty na samej wartości (na przykład moglibyśmy użyć nazwy miasta), prawie zawsze powinien być liczbą lub innym identyfikatorem. Nie chcemy, aby identyfikator kiedykolwiek się zmienił, ponieważ złamałoby to relację. W większości przypadków klucz główny lub ID będzie automatycznie generowaną liczbą.

> ✅ Klucz główny często jest skracany jako PK

### miasta

| city_id | Miasto   | Kraj          |
| ------- | -------- | ------------- |
| 1       | Tokio    | Japonia       |
| 2       | Atlanta  | Stany Zjednoczone |
| 3       | Auckland | Nowa Zelandia |

> ✅ Zauważysz, że używamy terminów "id" i "klucz główny" zamiennie w trakcie tej lekcji. Koncepcje te mają zastosowanie do DataFrames, które będziesz eksplorować później. DataFrames nie używają terminologii "klucz główny", jednak zauważysz, że działają w bardzo podobny sposób.

Po utworzeniu tabeli miast, przechowajmy dane o opadach. Zamiast duplikować pełne informacje o mieście, możemy użyć ID. Powinniśmy również upewnić się, że nowo utworzona tabela ma kolumnę *id*, ponieważ wszystkie tabele powinny mieć ID lub klucz główny.

### opady

| rainfall_id | city_id | Rok  | Ilość  |
| ----------- | ------- | ---- | ------ |
| 1           | 1       | 2018 | 1445   |
| 2           | 1       | 2019 | 1874   |
| 3           | 1       | 2020 | 1690   |
| 4           | 2       | 2018 | 1779   |
| 5           | 2       | 2019 | 1111   |
| 6           | 2       | 2020 | 1683   |
| 7           | 3       | 2018 | 1386   |
| 8           | 3       | 2019 | 942    |
| 9           | 3       | 2020 | 1176   |

Zauważ kolumnę **city_id** w nowo utworzonej tabeli **opady**. Ta kolumna zawiera wartości, które odnoszą się do ID w tabeli **miasta**. W technicznych terminach relacyjnych danych nazywa się to **kluczem obcym**; jest to klucz główny z innej tabeli. Możesz po prostu myśleć o tym jako o odwołaniu lub wskaźniku. **city_id** 1 odnosi się do Tokio.

> [!NOTE] 
> Klucz obcy często jest skracany jako FK

## Pobieranie danych

Mając nasze dane podzielone na dwie tabele, możesz się zastanawiać, jak je pobrać. Jeśli używamy relacyjnej bazy danych, takiej jak MySQL, SQL Server lub Oracle, możemy użyć języka o nazwie Structured Query Language, czyli SQL. SQL (czasami wymawiane jako "sequel") to standardowy język używany do pobierania i modyfikowania danych w relacyjnej bazie danych.

Aby pobrać dane, używasz polecenia `SELECT`. W swojej istocie **wybierasz** kolumny, które chcesz zobaczyć **z** tabeli, w której się znajdują. Jeśli chcesz wyświetlić tylko nazwy miast, możesz użyć następującego zapytania:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` to miejsce, gdzie wymieniasz kolumny, a `FROM` to miejsce, gdzie wymieniasz tabele.

> [!NOTE] 
> Składnia SQL jest niewrażliwa na wielkość liter, co oznacza, że `select` i `SELECT` oznaczają to samo. Jednak w zależności od rodzaju używanej bazy danych, kolumny i tabele mogą być wrażliwe na wielkość liter. W związku z tym najlepszą praktyką jest zawsze traktowanie wszystkiego w programowaniu tak, jakby było wrażliwe na wielkość liter. Podczas pisania zapytań SQL powszechną konwencją jest używanie słów kluczowych zapisanych wielkimi literami.

Powyższe zapytanie wyświetli wszystkie miasta. Wyobraźmy sobie, że chcemy wyświetlić tylko miasta w Nowej Zelandii. Potrzebujemy jakiejś formy filtra. Słowem kluczowym SQL dla tego jest `WHERE`, czyli "gdzie coś jest prawdziwe".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Łączenie danych

Do tej pory pobieraliśmy dane z jednej tabeli. Teraz chcemy połączyć dane z obu tabel **miasta** i **opady**. Robi się to poprzez *łączenie* ich ze sobą. W efekcie tworzysz połączenie między dwiema tabelami, dopasowując wartości z kolumny z każdej tabeli.

W naszym przykładzie dopasujemy kolumnę **city_id** w **opady** z kolumną **city_id** w **miasta**. To dopasuje wartość opadów do odpowiedniego miasta. Typ połączenia, który wykonamy, nazywa się *wewnętrznym* połączeniem, co oznacza, że jeśli jakiekolwiek wiersze nie pasują do niczego z drugiej tabeli, nie będą wyświetlane. W naszym przypadku każde miasto ma dane o opadach, więc wszystko zostanie wyświetlone.

Pobierzmy dane o opadach za rok 2019 dla wszystkich naszych miast.

Zrobimy to krok po kroku. Pierwszym krokiem jest połączenie danych, wskazując kolumny dla połączenia - **city_id**, jak podkreślono wcześniej.

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

Relacyjne bazy danych opierają się na podziale informacji między wiele tabel, które następnie są łączone w celu wyświetlenia i analizy. Zapewnia to wysoki stopień elastyczności w wykonywaniu obliczeń i innych operacji na danych. Poznałeś podstawowe koncepcje relacyjnej bazy danych oraz sposób łączenia dwóch tabel.

## 🚀 Wyzwanie

Istnieje wiele relacyjnych baz danych dostępnych w Internecie. Możesz eksplorować dane, korzystając z umiejętności, które zdobyłeś powyżej.

## Quiz po wykładzie

## [Quiz po wykładzie](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Przegląd i samodzielna nauka

Na [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) dostępnych jest kilka zasobów, które pozwolą Ci kontynuować eksplorację SQL i koncepcji relacyjnych baz danych:

- [Opis koncepcji relacyjnych danych](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Rozpocznij pracę z zapytaniami w Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL to wersja SQL)
- [Treści SQL na Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Zadanie

[Temat zadania](assignment.md)

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.