# Definiowanie danych

|![ Sketchnote autorstwa [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Definiowanie danych - _Sketchnote autorstwa [@nitya](https://twitter.com/nitya)_ |

Dane to fakty, informacje, obserwacje i pomiary, które są używane do dokonywania odkryć i wspierania świadomych decyzji. Punkt danych to pojedyncza jednostka danych w zbiorze danych, który jest kolekcją punktów danych. Zbiory danych mogą występować w różnych formatach i strukturach, zwykle zależnie od ich źródła, czyli miejsca, z którego pochodzą dane. Na przykład miesięczne przychody firmy mogą być w arkuszu kalkulacyjnym, ale dane o częstości akcji serca co godzinę z zegarka mogą być w formacie [JSON](https://stackoverflow.com/a/383699). Często naukowcy danych pracują z różnymi typami danych w obrębie jednego zbioru danych.

Ta lekcja skupia się na identyfikacji i klasyfikacji danych według ich cech i źródeł.

## [Quiz przed wykładem](https://ff-quizzes.netlify.app/en/ds/quiz/4)
## Jak opisujemy dane

### Surowe dane
Surowe dane to dane, które pochodzą ze swojego źródła w stanie pierwotnym i nie zostały jeszcze przeanalizowane ani zorganizowane. Aby zrozumieć, co się dzieje ze zbiorem danych, musi on zostać zorganizowany w formacie zrozumiałym dla ludzi oraz technologii, które mogą służyć do dalszej analizy. Struktura zbioru danych opisuje, jak jest on zorganizowany i może być sklasyfikowana jako strukturalna, niestrukturalna oraz półstrukturalna. Te rodzaje struktur będą się różnić w zależności od źródła, ale ostatecznie mieszczą się w tych trzech kategoriach.

### Dane ilościowe
Dane ilościowe to obserwacje numeryczne w zbiorze danych, które zazwyczaj mogą być analizowane, mierzone i wykorzystywane matematycznie. Przykładami danych ilościowych są: liczba ludności kraju, wzrost osoby lub kwartalne przychody firmy. Po dodatkowej analizie dane ilościowe mogą służyć do odkrywania sezonowych trendów Wskaźnika Jakości Powietrza (AQI) lub oszacowania prawdopodobieństwa wystąpienia korków w godzinach szczytu w zwykły dzień pracy.

### Dane jakościowe
Dane jakościowe, znane również jako dane kategoryczne, to dane, których nie da się obiektywnie zmierzyć, takich jak obserwacje danych ilościowych. Są to zazwyczaj różne formy subiektywnych danych, które odzwierciedlają jakość czegoś, np. produktu lub procesu. Czasami dane jakościowe mają formę liczbową, ale zwykle nie są wykorzystywane matematycznie, jak numery telefonów czy znaczniki czasu. Przykłady danych jakościowych to: komentarze wideo, marka i model samochodu lub ulubiony kolor najbliższych przyjaciół. Dane jakościowe mogą służyć do zrozumienia, które produkty konsumenci lubią najbardziej lub do identyfikacji popularnych słów kluczowych w życiorysach aplikacji o pracę.

### Dane strukturalne
Dane strukturalne to dane zorganizowane w wiersze i kolumny, gdzie każdy wiersz ma ten sam zestaw kolumn. Kolumny reprezentują wartość określonego typu i są oznaczone nazwą opisującą, co dana wartość reprezentuje, podczas gdy wiersze zawierają faktyczne wartości. Kolumny często mają określony zestaw zasad lub ograniczeń dotyczących wartości, aby upewnić się, że wartości dokładnie reprezentują kolumnę. Na przykład wyobraź sobie arkusz kalkulacyjny klientów, gdzie każdy wiersz musi mieć numer telefonu, a numery telefonów nigdy nie zawierają znaków alfabetycznych. W kolumnie z numerem telefonu mogą obowiązywać zasady, które zapewniają, że ta kolumna nigdy nie jest pusta i zawiera tylko cyfry.

Zaleta danych strukturalnych jest taka, że mogą być zorganizowane tak, aby można je było powiązać z innymi danymi strukturalnymi. Jednak ponieważ dane zaprojektowano tak, aby były zorganizowane w określony sposób, wprowadzanie zmian w ich ogólnej strukturze może wymagać dużego wysiłku. Na przykład dodanie kolumny z adresem e-mail do arkusza klientów, która nie może być pusta, oznacza, że trzeba będzie ustalić, jak dodać te wartości do istniejących wierszy klientów w zbiorze danych.

Przykłady danych strukturalnych: arkusze kalkulacyjne, relacyjne bazy danych, numery telefonów, wyciągi bankowe

### Dane niestrukturalne
Dane niestrukturalne zazwyczaj nie mogą być skategoryzowane w wiersze lub kolumny i nie zawierają ustalonego formatu lub zestawu zasad do przestrzegania. Ponieważ dane niestrukturalne mają mniej ograniczeń dotyczących struktury, łatwiej jest do nich dodawać nowe informacje w porównaniu do zbioru danych strukturalnych. Jeśli czujnik mierzący ciśnienie barometryczne co 2 minuty otrzyma aktualizację pozwalającą na pomiar i rejestrację temperatury, nie wymaga to zmieniania istniejących danych, jeśli są one niestrukturalne. Jednak może to wydłużyć czas analizowania lub badania tego typu danych. Na przykład naukowiec, który chce znaleźć średnią temperaturę z poprzedniego miesiąca na podstawie danych z czujników, odkrywa, że czujnik w niektórych zapisanych danych zanotował „e”, oznaczając uszkodzenie zamiast typowej liczby, co oznacza, że dane są niepełne.

Przykłady danych niestrukturalnych: pliki tekstowe, wiadomości tekstowe, pliki wideo

### Dane półstrukturalne
Dane półstrukturalne mają cechy łączące dane strukturalne i niestrukturalne. Zazwyczaj nie odpowiadają formatowi wierszy i kolumn, ale są zorganizowane w sposób uznawany za strukturalny i mogą mieć ustalony format lub zestaw zasad. Struktura będzie się różnić w zależności od źródeł, od dobrze określonej hierarchii do czegoś bardziej elastycznego, co ułatwia integrację nowych informacji. Metadane to wskaźniki pomagające zadecydować, jak dane są organizowane i przechowywane, i mają różne nazwy w zależności od rodzaju danych. Najczęstsze nazwy metadanych to tagi, elementy, jednostki i atrybuty. Na przykład typowa wiadomość e-mail ma temat, treść i zestaw odbiorców i może być zorganizowana według tego, kto lub kiedy ją wysłał.

Przykłady danych półstrukturalnych: HTML, pliki CSV, JavaScript Object Notation (JSON)

## Źródła danych

Źródło danych to pierwotna lokalizacja, w której dane zostały wygenerowane lub gdzie „mieszkają”, i różni się w zależności od sposobu i czasu ich zebrania. Dane generowane przez użytkownika(-ów) są znane jako dane pierwotne, podczas gdy dane wtórne pochodzą ze źródła, które zebrało dane do użytku ogólnego. Na przykład grupa naukowców zbierająca obserwacje w lesie deszczowym byłaby uznana za źródło pierwotne, a jeśli zdecydują się udostępnić je innym naukowcom, dla tych ostatnich będzie to źródło wtórne.

Bazy danych są powszechnym źródłem i opierają się na systemie zarządzania bazą danych do hostowania i utrzymywania danych, gdzie użytkownicy korzystają z poleceń zwanych zapytaniami, aby eksplorować dane. Pliki jako źródła danych mogą być plikami audio, obrazów, wideo, a także arkuszami kalkulacyjnymi, jak Excel. Źródła internetowe są powszechnym miejscem przechowywania danych, gdzie można znaleźć bazy danych i pliki. Interfejsy programistyczne aplikacji, znane jako API, pozwalają programistom tworzyć sposoby udostępniania danych zewnętrznym użytkownikom przez internet, podczas gdy proces web scrapingu wyodrębnia dane ze strony internetowej. [Lekcje z zakresu Pracy z danymi](../../../../../../../../../2-Working-With-Data) koncentrują się na tym, jak korzystać z różnych źródeł danych.

## Podsumowanie

Na tej lekcji dowiedzieliśmy się:

- Czym są dane
- Jak opisujemy dane
- Jak dane są klasyfikowane i kategoryzowane
- Gdzie można znaleźć dane

## 🚀 Wyzwanie

Kaggle to doskonałe źródło otwartych zbiorów danych. Użyj [narzędzia wyszukiwania zbiorów danych](https://www.kaggle.com/datasets), aby znaleźć ciekawe zbiory danych i sklasyfikuj 3-5 z nich według następujących kryteriów:

- Czy dane są ilościowe czy jakościowe?
- Czy dane są strukturalne, niestrukturalne czy półstrukturalne?

## [Quiz po wykładzie](https://ff-quizzes.netlify.app/en/ds/quiz/5)



## Przegląd i samodzielna nauka

- Ten moduł Microsoft Learn, zatytułowany [Identify data formats](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats?pivots=text), zawiera szczegółowe omówienie danych strukturalnych, półstrukturalnych oraz niestrukturalnych.

## Zadanie

[Klasyfikacja zbiorów danych](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->