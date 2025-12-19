<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11739c7b40e7c6b16ad29e3df4e65862",
  "translation_date": "2025-12-19T11:19:35+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "pl"
}
-->
# Praca z danymi: bazy danych relacyjne

|![ Sketchnote autorstwa [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Praca z danymi: bazy danych relacyjne - _Sketchnote autorstwa [@nitya](https://twitter.com/nitya)_ |

Prawdopodobnie w przeszłości korzystałeś z arkusza kalkulacyjnego do przechowywania informacji. Miałeś zestaw wierszy i kolumn, gdzie wiersze zawierały informacje (lub dane), a kolumny opisywały te informacje (czasem nazywane metadanymi). Baza danych relacyjnych opiera się na tej podstawowej zasadzie kolumn i wierszy w tabelach, pozwalając na rozproszenie informacji na wiele tabel. Umożliwia to pracę z bardziej złożonymi danymi, unikanie duplikacji oraz elastyczność w eksploracji danych. Przyjrzyjmy się koncepcjom bazy danych relacyjnych.

## [Quiz przed wykładem](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## Wszystko zaczyna się od tabel

Baza danych relacyjnych opiera się na tabelach. Podobnie jak w arkuszu kalkulacyjnym, tabela to zbiór kolumn i wierszy. Wiersz zawiera dane lub informacje, z którymi chcemy pracować, takie jak nazwa miasta czy ilość opadów. Kolumny opisują przechowywane dane.

Zacznijmy naszą eksplorację od utworzenia tabeli do przechowywania informacji o miastach. Możemy zacząć od ich nazwy i kraju. Można to przechować w tabeli w następujący sposób:

| Miasto   | Kraj          |
| -------- | ------------- |
| Tokyo    | Japonia       |
| Atlanta  | Stany Zjednoczone |
| Auckland | Nowa Zelandia |

Zauważ, że nazwy kolumn **Miasto**, **Kraj** i **Populacja** opisują przechowywane dane, a każdy wiersz zawiera informacje o jednym mieście.

## Wady podejścia z jedną tabelą

Prawdopodobnie powyższa tabela wydaje się Ci dość znajoma. Dodajmy teraz dodatkowe dane do naszej rozwijającej się bazy danych - roczne opady (w milimetrach). Skupimy się na latach 2018, 2019 i 2020. Gdybyśmy dodali je dla Tokio, mogłoby to wyglądać tak:

| Miasto | Kraj    | Rok  | Ilość  |
| ------ | ------- | ---- | ------ |
| Tokyo  | Japonia | 2020 | 1690   |
| Tokyo  | Japonia | 2019 | 1874   |
| Tokyo  | Japonia | 2018 | 1445   |

Co zauważasz w naszej tabeli? Możesz zauważyć, że powielamy nazwę i kraj miasta wielokrotnie. To może zajmować sporo miejsca i jest w dużej mierze niepotrzebne, aby mieć wiele kopii. W końcu Tokio ma tylko jedną nazwę, która nas interesuje.

OK, spróbujmy czegoś innego. Dodajmy nowe kolumny dla każdego roku:

| Miasto   | Kraj          | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Japonia       | 1445 | 1874 | 1690 |
| Atlanta  | Stany Zjednoczone | 1779 | 1111 | 1683 |
| Auckland | Nowa Zelandia | 1386 | 942  | 1176 |

Chociaż unika to powielania wierszy, wprowadza kilka innych wyzwań. Musielibyśmy modyfikować strukturę tabeli za każdym razem, gdy pojawia się nowy rok. Dodatkowo, gdy nasze dane rosną, posiadanie lat jako kolumn utrudni pobieranie i obliczanie wartości.

Dlatego potrzebujemy wielu tabel i relacji. Dzieląc dane, możemy uniknąć duplikacji i mieć większą elastyczność w pracy z danymi.

## Koncepcje relacji

Wróćmy do naszych danych i zdecydujmy, jak chcemy je podzielić. Wiemy, że chcemy przechowywać nazwę i kraj naszych miast, więc najlepiej będzie to w jednej tabeli.

| Miasto   | Kraj          |
| -------- | ------------- |
| Tokyo    | Japonia       |
| Atlanta  | Stany Zjednoczone |
| Auckland | Nowa Zelandia |

Ale zanim utworzymy kolejną tabelę, musimy ustalić, jak odwołać się do każdego miasta. Potrzebujemy jakiegoś identyfikatora, ID lub (w technicznych terminach baz danych) klucza głównego. Klucz główny to wartość używana do identyfikacji jednego konkretnego wiersza w tabeli. Chociaż może to być oparty na samej wartości (na przykład nazwa miasta), powinien to być prawie zawsze numer lub inny identyfikator. Nie chcemy, aby id kiedykolwiek się zmieniło, ponieważ złamałoby to relację. W większości przypadków klucz główny lub id będzie automatycznie generowanym numerem.

> ✅ Klucz główny jest często skracany jako PK

### cities

| city_id | Miasto   | Kraj          |
| ------- | -------- | ------------- |
| 1       | Tokyo    | Japonia       |
| 2       | Atlanta  | Stany Zjednoczone |
| 3       | Auckland | Nowa Zelandia |

> ✅ Zauważysz, że w trakcie lekcji używamy zamiennie terminów "id" i "klucz główny". Koncepcje te odnoszą się również do DataFrame'ów, które poznasz później. DataFrame'y nie używają terminologii "klucz główny", ale zauważysz, że zachowują się podobnie.

Po utworzeniu tabeli miast, przechowajmy dane o opadach. Zamiast powielać pełne informacje o mieście, możemy użyć id. Powinniśmy również upewnić się, że nowo utworzona tabela ma kolumnę *id*, ponieważ wszystkie tabele powinny mieć id lub klucz główny.

### rainfall

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

Zauważ kolumnę **city_id** w nowo utworzonej tabeli **rainfall**. Ta kolumna zawiera wartości, które odwołują się do ID w tabeli **cities**. W technicznych terminach relacyjnych danych nazywa się to **kluczem obcym**; jest to klucz główny z innej tabeli. Możesz myśleć o tym jako o odniesieniu lub wskaźniku. **city_id** 1 odnosi się do Tokio.

> [!NOTE] 
> Klucz obcy jest często skracany jako FK

## Pobieranie danych

Mając dane podzielone na dwie tabele, możesz się zastanawiać, jak je pobrać. Jeśli używamy bazy danych relacyjnej takiej jak MySQL, SQL Server czy Oracle, możemy użyć języka zwanego Structured Query Language lub SQL. SQL (czasem wymawiany jako sequel) to standardowy język używany do pobierania i modyfikowania danych w bazie danych relacyjnej.

Aby pobrać dane, używasz polecenia `SELECT`. W swojej istocie **wybierasz** kolumny, które chcesz zobaczyć, **z** tabeli, w której się znajdują. Jeśli chcesz wyświetlić tylko nazwy miast, możesz użyć następującego zapytania:

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
> Składnia SQL jest nieczuła na wielkość liter, co oznacza, że `select` i `SELECT` znaczą to samo. Jednak w zależności od typu bazy danych, której używasz, kolumny i tabele mogą być czułe na wielkość liter. W związku z tym najlepszą praktyką jest traktowanie wszystkiego w programowaniu jak czułego na wielkość liter. Podczas pisania zapytań SQL powszechną konwencją jest pisanie słów kluczowych wielkimi literami.

Powyższe zapytanie wyświetli wszystkie miasta. Załóżmy, że chcemy wyświetlić tylko miasta w Nowej Zelandii. Potrzebujemy jakiegoś filtra. Słowem kluczowym SQL do tego jest `WHERE`, czyli "gdzie coś jest prawdziwe".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Łączenie danych

Do tej pory pobieraliśmy dane z jednej tabeli. Teraz chcemy połączyć dane z obu tabel: **cities** i **rainfall**. Robi się to przez *łączenie* ich razem. W praktyce tworzysz połączenie między dwiema tabelami i dopasowujesz wartości z kolumny z każdej tabeli.

W naszym przykładzie dopasujemy kolumnę **city_id** w tabeli **rainfall** do kolumny **city_id** w tabeli **cities**. To dopasuje wartość opadów do odpowiedniego miasta. Typ łączenia, który wykonamy, nazywa się *inner* join, co oznacza, że jeśli jakieś wiersze nie mają dopasowania w drugiej tabeli, nie zostaną wyświetlone. W naszym przypadku każde miasto ma dane o opadach, więc wszystko zostanie wyświetlone.

Pobierzmy opady za rok 2019 dla wszystkich naszych miast.

Zrobimy to krok po kroku. Pierwszym krokiem jest połączenie danych, wskazując kolumny do połączenia - **city_id**, jak wcześniej podkreślono.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Podkreśliliśmy dwie kolumny, które chcemy, oraz fakt, że chcemy połączyć tabele przez **city_id**. Teraz możemy dodać instrukcję `WHERE`, aby przefiltrować tylko rok 2019.

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

Bazy danych relacyjne opierają się na dzieleniu informacji na wiele tabel, które następnie są łączone do wyświetlania i analizy. Zapewnia to dużą elastyczność w wykonywaniu obliczeń i manipulacji danymi. Poznałeś podstawowe koncepcje bazy danych relacyjnych oraz jak wykonać łączenie między dwiema tabelami.

## 🚀 Wyzwanie

Istnieje wiele baz danych relacyjnych dostępnych w internecie. Możesz eksplorować dane, korzystając z umiejętności, które poznałeś powyżej.

## Quiz po wykładzie

## [Quiz po wykładzie](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Przegląd i samodzielna nauka

Na [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) dostępnych jest kilka zasobów, które pozwolą Ci kontynuować eksplorację SQL i koncepcji baz danych relacyjnych

- [Opis koncepcji danych relacyjnych](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Pierwsze kroki z zapytaniami Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL to wersja SQL)
- [Zawartość SQL na Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Zadanie

[Wyświetlanie danych lotnisk](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->