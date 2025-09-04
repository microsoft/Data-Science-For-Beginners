<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1228edf3572afca7d7cdcd938b6b4984",
  "translation_date": "2025-09-04T14:49:11+00:00",
  "source_file": "1-Introduction/03-defining-data/README.md",
  "language_code": "pl"
}
-->
# Definiowanie danych

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Definiowanie danych - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Dane to fakty, informacje, obserwacje i pomiary, które są wykorzystywane do dokonywania odkryć i podejmowania świadomych decyzji. Punkt danych to pojedyncza jednostka danych w zbiorze danych, który jest kolekcją punktów danych. Zbiory danych mogą mieć różne formaty i struktury, zazwyczaj zależne od ich źródła, czyli miejsca, z którego pochodzą dane. Na przykład miesięczne dochody firmy mogą być zapisane w arkuszu kalkulacyjnym, ale dane o godzinowym tętnie z smartwatcha mogą być w formacie [JSON](https://stackoverflow.com/a/383699). Często zdarza się, że naukowcy zajmujący się danymi pracują z różnymi typami danych w jednym zbiorze danych.

Ta lekcja koncentruje się na identyfikacji i klasyfikacji danych według ich cech i źródeł.

## [Quiz przed wykładem](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/4)

## Jak opisuje się dane

### Surowe dane
Surowe dane to dane, które pochodzą ze swojego źródła w pierwotnym stanie i nie zostały jeszcze przeanalizowane ani zorganizowane. Aby zrozumieć, co dzieje się w zbiorze danych, muszą one zostać zorganizowane w formacie, który będzie zrozumiały zarówno dla ludzi, jak i dla technologii, które mogą być używane do ich dalszej analizy. Struktura zbioru danych opisuje, jak jest on zorganizowany i może być sklasyfikowana jako strukturalna, niestrukturalna lub półstrukturalna. Te typy struktur będą się różnić w zależności od źródła, ale ostatecznie pasują do jednej z tych trzech kategorii.

### Dane ilościowe
Dane ilościowe to obserwacje numeryczne w zbiorze danych, które można zazwyczaj analizować, mierzyć i wykorzystywać matematycznie. Przykłady danych ilościowych to: populacja kraju, wzrost osoby czy kwartalne dochody firmy. Przy dodatkowej analizie dane ilościowe mogą być używane do odkrywania sezonowych trendów wskaźnika jakości powietrza (AQI) lub szacowania prawdopodobieństwa korków w godzinach szczytu w typowy dzień roboczy.

### Dane jakościowe
Dane jakościowe, znane również jako dane kategoryczne, to dane, których nie można mierzyć obiektywnie, jak w przypadku obserwacji danych ilościowych. Zazwyczaj są to różne formaty danych subiektywnych, które uchwytują jakość czegoś, na przykład produktu lub procesu. Czasami dane jakościowe są numeryczne, ale nie są zazwyczaj wykorzystywane matematycznie, jak numery telefonów czy znaczniki czasu. Przykłady danych jakościowych to: komentarze wideo, marka i model samochodu czy ulubiony kolor najbliższych przyjaciół. Dane jakościowe mogą być używane do zrozumienia, które produkty konsumenci lubią najbardziej lub do identyfikacji popularnych słów kluczowych w życiorysach aplikacji o pracę.

### Dane strukturalne
Dane strukturalne to dane zorganizowane w wiersze i kolumny, gdzie każdy wiersz ma ten sam zestaw kolumn. Kolumny reprezentują wartość określonego typu i są identyfikowane nazwą opisującą, co dana wartość reprezentuje, podczas gdy wiersze zawierają rzeczywiste wartości. Kolumny często mają określony zestaw reguł lub ograniczeń dotyczących wartości, aby zapewnić, że wartości dokładnie reprezentują kolumnę. Na przykład wyobraź sobie arkusz kalkulacyjny klientów, gdzie każdy wiersz musi zawierać numer telefonu, a numery telefonów nigdy nie zawierają znaków alfabetycznych. Mogą być zastosowane reguły dotyczące kolumny numeru telefonu, aby upewnić się, że nigdy nie jest pusta i zawiera tylko liczby.

Zaletą danych strukturalnych jest to, że mogą być zorganizowane w sposób umożliwiający ich powiązanie z innymi danymi strukturalnymi. Jednakże, ponieważ dane są zaprojektowane tak, aby były zorganizowane w określony sposób, wprowadzenie zmian w ich ogólnej strukturze może wymagać dużego wysiłku. Na przykład dodanie kolumny e-mail do arkusza kalkulacyjnego klientów, która nie może być pusta, oznacza, że trzeba będzie ustalić, jak dodać te wartości do istniejących wierszy klientów w zbiorze danych.

Przykłady danych strukturalnych: arkusze kalkulacyjne, relacyjne bazy danych, numery telefonów, wyciągi bankowe.

### Dane niestrukturalne
Dane niestrukturalne zazwyczaj nie mogą być kategoryzowane w wiersze lub kolumny i nie zawierają formatu ani zestawu reguł do przestrzegania. Ponieważ dane niestrukturalne mają mniej ograniczeń dotyczących swojej struktury, łatwiej jest dodawać nowe informacje w porównaniu do zbioru danych strukturalnych. Jeśli czujnik rejestrujący dane o ciśnieniu barometrycznym co 2 minuty otrzyma aktualizację, która pozwala mu mierzyć i rejestrować temperaturę, nie wymaga to zmiany istniejących danych, jeśli są one niestrukturalne. Jednakże, może to sprawić, że analiza lub badanie tego typu danych zajmie więcej czasu. Na przykład naukowiec, który chce znaleźć średnią temperaturę z poprzedniego miesiąca na podstawie danych z czujnika, ale odkrywa, że czujnik zarejestrował "e" w niektórych swoich danych, aby zaznaczyć, że był uszkodzony, zamiast typowej liczby, co oznacza, że dane są niekompletne.

Przykłady danych niestrukturalnych: pliki tekstowe, wiadomości tekstowe, pliki wideo.

### Dane półstrukturalne
Dane półstrukturalne mają cechy, które sprawiają, że są kombinacją danych strukturalnych i niestrukturalnych. Zazwyczaj nie odpowiadają formatowi wierszy i kolumn, ale są zorganizowane w sposób uważany za strukturalny i mogą przestrzegać ustalonego formatu lub zestawu reguł. Struktura będzie się różnić w zależności od źródła, od dobrze zdefiniowanej hierarchii do czegoś bardziej elastycznego, co pozwala na łatwą integrację nowych informacji. Metadane to wskaźniki, które pomagają zdecydować, jak dane są zorganizowane i przechowywane, i mają różne nazwy w zależności od rodzaju danych. Niektóre popularne nazwy metadanych to tagi, elementy, jednostki i atrybuty. Na przykład typowa wiadomość e-mail będzie miała temat, treść i zestaw odbiorców i może być zorganizowana według tego, kto ją wysłał lub kiedy została wysłana.

Przykłady danych półstrukturalnych: HTML, pliki CSV, JavaScript Object Notation (JSON).

## Źródła danych

Źródło danych to początkowe miejsce, w którym dane zostały wygenerowane lub gdzie "żyją" i będzie się różnić w zależności od tego, jak i kiedy zostały zebrane. Dane generowane przez użytkownika są znane jako dane pierwotne, podczas gdy dane wtórne pochodzą ze źródła, które zebrało dane do ogólnego użytku. Na przykład grupa naukowców zbierająca obserwacje w lesie deszczowym byłaby uważana za dane pierwotne, a jeśli zdecydują się je udostępnić innym naukowcom, byłyby one uważane za dane wtórne dla tych, którzy je wykorzystują.

Bazy danych są powszechnym źródłem i polegają na systemie zarządzania bazami danych, który hostuje i utrzymuje dane, gdzie użytkownicy używają poleceń zwanych zapytaniami do eksploracji danych. Pliki jako źródła danych mogą być plikami audio, obrazami, plikami wideo, a także arkuszami kalkulacyjnymi, takimi jak Excel. Źródła internetowe są powszechnym miejscem hostowania danych, gdzie można znaleźć zarówno bazy danych, jak i pliki. Interfejsy programowania aplikacji, znane również jako API, pozwalają programistom tworzyć sposoby udostępniania danych zewnętrznym użytkownikom przez internet, podczas gdy proces web scrapingu polega na wyodrębnianiu danych ze strony internetowej. [Lekcje w Praca z danymi](../../../../../../../../../2-Working-With-Data) koncentrują się na tym, jak korzystać z różnych źródeł danych.

## Podsumowanie

W tej lekcji nauczyliśmy się:

- Czym są dane
- Jak opisuje się dane
- Jak klasyfikuje się i kategoryzuje dane
- Gdzie można znaleźć dane

## 🚀 Wyzwanie

Kaggle to doskonałe źródło otwartych zbiorów danych. Skorzystaj z [narzędzia wyszukiwania zbiorów danych](https://www.kaggle.com/datasets), aby znaleźć kilka interesujących zbiorów danych i sklasyfikować 3-5 zbiorów danych według tych kryteriów:

- Czy dane są ilościowe czy jakościowe?
- Czy dane są strukturalne, niestrukturalne czy półstrukturalne?

## [Quiz po wykładzie](https://ff-quizzes.netlify.app/en/ds/)

## Przegląd i samodzielna nauka

- Jednostka Microsoft Learn zatytułowana [Klasyfikowanie danych](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/2-classify-data) zawiera szczegółowy podział danych strukturalnych, półstrukturalnych i niestrukturalnych.

## Zadanie

[Klasyfikowanie zbiorów danych](assignment.md)

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.