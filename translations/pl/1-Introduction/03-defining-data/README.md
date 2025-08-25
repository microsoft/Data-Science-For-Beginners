<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "356d12cffc3125db133a2d27b827a745",
  "translation_date": "2025-08-24T21:34:15+00:00",
  "source_file": "1-Introduction/03-defining-data/README.md",
  "language_code": "pl"
}
-->
# Definiowanie Danych

|![ Sketchnote autorstwa [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Definiowanie Danych - _Sketchnote autorstwa [@nitya](https://twitter.com/nitya)_ |

Dane to fakty, informacje, obserwacje i pomiary, które są wykorzystywane do dokonywania odkryć i podejmowania świadomych decyzji. Punkt danych to pojedyncza jednostka danych w zbiorze danych, który jest kolekcją punktów danych. Zbiory danych mogą mieć różne formaty i struktury, zazwyczaj zależne od ich źródła, czyli miejsca, z którego pochodzą dane. Na przykład miesięczne przychody firmy mogą być zapisane w arkuszu kalkulacyjnym, ale dane o tętnie zebrane co godzinę przez smartwatch mogą być w formacie [JSON](https://stackoverflow.com/a/383699). Często zdarza się, że naukowcy zajmujący się danymi pracują z różnymi typami danych w jednym zbiorze danych.

Ta lekcja koncentruje się na identyfikacji i klasyfikacji danych według ich cech i źródeł.

## [Quiz przed wykładem](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/4)
## Jak Opisywane Są Dane

### Surowe Dane
Surowe dane to dane, które pochodzą bezpośrednio ze swojego źródła w pierwotnym stanie i nie zostały jeszcze przeanalizowane ani zorganizowane. Aby zrozumieć, co dzieje się w zbiorze danych, muszą one zostać zorganizowane w formacie, który będzie zrozumiały zarówno dla ludzi, jak i technologii, które mogą być używane do ich dalszej analizy. Struktura zbioru danych opisuje, jak jest on zorganizowany, i może być sklasyfikowana jako strukturalna, niestrukturalna lub półstrukturalna. Te typy struktur różnią się w zależności od źródła, ale ostatecznie mieszczą się w tych trzech kategoriach.

### Dane Ilościowe
Dane ilościowe to obserwacje liczbowe w zbiorze danych, które można zazwyczaj analizować, mierzyć i wykorzystywać matematycznie. Przykłady danych ilościowych to: populacja kraju, wzrost osoby lub kwartalne przychody firmy. Po dodatkowej analizie dane ilościowe mogą być używane do odkrywania sezonowych trendów w indeksie jakości powietrza (AQI) lub szacowania prawdopodobieństwa korków w godzinach szczytu w typowy dzień roboczy.

### Dane Jakościowe
Dane jakościowe, znane również jako dane kategoryczne, to dane, których nie można mierzyć obiektywnie, jak w przypadku obserwacji danych ilościowych. Są to zazwyczaj różne formaty danych subiektywnych, które uchwytują jakość czegoś, na przykład produktu lub procesu. Czasami dane jakościowe są liczbowe, ale nie są zazwyczaj wykorzystywane matematycznie, jak numery telefonów czy znaczniki czasu. Przykłady danych jakościowych to: komentarze wideo, marka i model samochodu lub ulubiony kolor najbliższych przyjaciół. Dane jakościowe mogą być używane do zrozumienia, które produkty konsumenci lubią najbardziej, lub do identyfikacji popularnych słów kluczowych w życiorysach aplikacji o pracę.

### Dane Strukturalne
Dane strukturalne to dane zorganizowane w wiersze i kolumny, gdzie każdy wiersz ma ten sam zestaw kolumn. Kolumny reprezentują wartość określonego typu i są identyfikowane nazwą opisującą, co dana wartość reprezentuje, podczas gdy wiersze zawierają rzeczywiste wartości. Kolumny często mają określony zestaw reguł lub ograniczeń dotyczących wartości, aby upewnić się, że wartości dokładnie reprezentują kolumnę. Na przykład wyobraź sobie arkusz kalkulacyjny klientów, gdzie każdy wiersz musi zawierać numer telefonu, a numery telefonów nigdy nie zawierają znaków alfabetycznych. Mogą być zastosowane reguły dotyczące kolumny numeru telefonu, aby upewnić się, że nigdy nie jest pusta i zawiera tylko liczby.

Zaletą danych strukturalnych jest to, że mogą być zorganizowane w sposób umożliwiający ich powiązanie z innymi danymi strukturalnymi. Jednak ze względu na to, że dane są zaprojektowane w określony sposób, wprowadzenie zmian w ich ogólnej strukturze może wymagać dużego wysiłku. Na przykład dodanie kolumny e-mail do arkusza kalkulacyjnego klientów, która nie może być pusta, oznacza, że trzeba będzie ustalić, jak dodać te wartości do istniejących wierszy klientów w zbiorze danych.

Przykłady danych strukturalnych: arkusze kalkulacyjne, relacyjne bazy danych, numery telefonów, wyciągi bankowe.

### Dane Niestrukturalne
Dane niestrukturalne zazwyczaj nie mogą być kategoryzowane w wiersze lub kolumny i nie zawierają formatu ani zestawu reguł do przestrzegania. Ponieważ dane niestrukturalne mają mniej ograniczeń dotyczących swojej struktury, łatwiej jest dodać nowe informacje w porównaniu do zbioru danych strukturalnych. Jeśli czujnik rejestrujący dane o ciśnieniu barometrycznym co 2 minuty otrzyma aktualizację, która pozwala mu mierzyć i rejestrować temperaturę, nie wymaga to zmiany istniejących danych, jeśli są one niestrukturalne. Jednak analiza lub badanie tego typu danych może zająć więcej czasu. Na przykład naukowiec, który chce znaleźć średnią temperaturę z poprzedniego miesiąca na podstawie danych z czujnika, może odkryć, że czujnik zapisał "e" w niektórych swoich danych, aby zaznaczyć, że był uszkodzony, zamiast typowej liczby, co oznacza, że dane są niekompletne.

Przykłady danych niestrukturalnych: pliki tekstowe, wiadomości tekstowe, pliki wideo.

### Dane Półstrukturalne
Dane półstrukturalne mają cechy, które sprawiają, że są połączeniem danych strukturalnych i niestrukturalnych. Zazwyczaj nie odpowiadają formatowi wierszy i kolumn, ale są zorganizowane w sposób uznawany za strukturalny i mogą przestrzegać ustalonego formatu lub zestawu reguł. Struktura będzie się różnić w zależności od źródła, od dobrze zdefiniowanej hierarchii po coś bardziej elastycznego, co pozwala na łatwą integrację nowych informacji. Metadane to wskaźniki, które pomagają zdecydować, jak dane są zorganizowane i przechowywane, i będą miały różne nazwy w zależności od typu danych. Niektóre popularne nazwy dla metadanych to tagi, elementy, jednostki i atrybuty. Na przykład typowa wiadomość e-mail będzie miała temat, treść i zestaw odbiorców i może być zorganizowana według tego, kto lub kiedy ją wysłał.

Przykłady danych półstrukturalnych: HTML, pliki CSV, JavaScript Object Notation (JSON).

## Źródła Danych

Źródło danych to początkowe miejsce, w którym dane zostały wygenerowane lub gdzie "żyją" i różni się w zależności od tego, jak i kiedy zostały zebrane. Dane generowane przez ich użytkowników są znane jako dane pierwotne, podczas gdy dane wtórne pochodzą ze źródła, które zebrało dane do ogólnego użytku. Na przykład grupa naukowców zbierających obserwacje w lesie deszczowym byłaby uznawana za dane pierwotne, a jeśli zdecydują się je udostępnić innym naukowcom, będą one uznawane za dane wtórne dla tych, którzy z nich korzystają.

Bazy danych są powszechnym źródłem i opierają się na systemie zarządzania bazami danych, aby hostować i utrzymywać dane, gdzie użytkownicy używają poleceń zwanych zapytaniami do eksploracji danych. Pliki jako źródła danych mogą obejmować pliki audio, obrazy, wideo, a także arkusze kalkulacyjne, takie jak Excel. Internet jest powszechnym miejscem przechowywania danych, gdzie można znaleźć zarówno bazy danych, jak i pliki. Interfejsy programowania aplikacji, znane również jako API, pozwalają programistom tworzyć sposoby udostępniania danych zewnętrznym użytkownikom przez internet, podczas gdy proces web scrapingu polega na wyodrębnianiu danych ze strony internetowej. [Lekcje w sekcji Praca z Danymi](../../../../../../../../../2-Working-With-Data) koncentrują się na tym, jak korzystać z różnych źródeł danych.

## Podsumowanie

W tej lekcji dowiedzieliśmy się:

- Czym są dane
- Jak dane są opisywane
- Jak dane są klasyfikowane i kategoryzowane
- Gdzie można znaleźć dane

## 🚀 Wyzwanie

Kaggle to doskonałe źródło otwartych zbiorów danych. Skorzystaj z [narzędzia wyszukiwania zbiorów danych](https://www.kaggle.com/datasets), aby znaleźć kilka interesujących zbiorów danych i sklasyfikować 3-5 z nich według następujących kryteriów:

- Czy dane są ilościowe czy jakościowe?
- Czy dane są strukturalne, niestrukturalne czy półstrukturalne?

## [Quiz po wykładzie](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/5)

## Przegląd i Samodzielna Nauka

- Jednostka Microsoft Learn zatytułowana [Klasyfikowanie Twoich Danych](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/2-classify-data) zawiera szczegółowy podział danych strukturalnych, półstrukturalnych i niestrukturalnych.

## Zadanie

[Klasyfikowanie Zbiorów Danych](assignment.md)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.