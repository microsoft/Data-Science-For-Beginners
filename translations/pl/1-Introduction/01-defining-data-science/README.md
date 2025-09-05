<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a0516588d172f82f35f7a0d4a001e5d0",
  "translation_date": "2025-09-05T14:44:32+00:00",
  "source_file": "1-Introduction/01-defining-data-science/README.md",
  "language_code": "pl"
}
-->
## Rodzaje danych

Jak już wspomniano, dane są wszędzie. Wystarczy je odpowiednio uchwycić! Warto rozróżnić dane **ustrukturyzowane** i **nieustrukturyzowane**. Dane ustrukturyzowane są zazwyczaj przedstawiane w dobrze zorganizowanej formie, często jako tabela lub zestaw tabel, podczas gdy dane nieustrukturyzowane to po prostu zbiór plików. Czasami możemy również mówić o danych **półustrukturyzowanych**, które mają pewien rodzaj struktury, ale może ona znacznie się różnić.

| Ustrukturyzowane                                                             | Półustrukturyzowane                                                                           | Nieustrukturyzowane                     |
| ----------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------- |
| Lista osób z ich numerami telefonów                                          | Strony Wikipedii z linkami                                                                    | Tekst Encyklopedii Britannica           |
| Temperatura we wszystkich pomieszczeniach budynku co minutę przez ostatnie 20 lat | Zbiór artykułów naukowych w formacie JSON z autorami, datą publikacji i streszczeniem         | Udostępnione pliki z dokumentami firmowymi |
| Dane o wieku i płci wszystkich osób wchodzących do budynku                   | Strony internetowe                                                                            | Surowy materiał wideo z kamery monitoringu |

## Skąd pozyskiwać dane

Istnieje wiele możliwych źródeł danych, i niemożliwe jest wymienienie wszystkich! Jednak warto wspomnieć o kilku typowych miejscach, z których można pozyskać dane:

* **Ustrukturyzowane**
  - **Internet rzeczy** (IoT), w tym dane z różnych czujników, takich jak czujniki temperatury czy ciśnienia, dostarcza wiele użytecznych informacji. Na przykład, jeśli budynek biurowy jest wyposażony w czujniki IoT, możemy automatycznie kontrolować ogrzewanie i oświetlenie, aby zminimalizować koszty.
  - **Ankiety**, które prosimy użytkowników o wypełnienie po zakupie lub po odwiedzeniu strony internetowej.
  - **Analiza zachowań** może pomóc nam zrozumieć, jak głęboko użytkownik zagłębia się w stronę internetową i jakie są typowe powody opuszczenia strony.
* **Nieustrukturyzowane**
  - **Teksty** mogą być bogatym źródłem informacji, takich jak ogólny **wskaźnik nastroju** lub wyodrębnienie słów kluczowych i znaczenia semantycznego.
  - **Obrazy** lub **wideo**. Na przykład wideo z kamery monitoringu może być użyte do oszacowania ruchu na drodze i informowania ludzi o potencjalnych korkach.
  - **Logi** serwera internetowego mogą być użyte do zrozumienia, które strony naszej witryny są najczęściej odwiedzane i jak długo.
* **Półustrukturyzowane**
  - **Grafy sieci społecznościowych** mogą być świetnym źródłem danych o osobowościach użytkowników i potencjalnej skuteczności w rozpowszechnianiu informacji.
  - Kiedy mamy zbiór zdjęć z imprezy, możemy spróbować wyodrębnić dane o **dynamice grupy**, budując graf osób robiących sobie zdjęcia nawzajem.

Znając różne możliwe źródła danych, możesz spróbować pomyśleć o różnych scenariuszach, w których techniki nauki o danych mogą być zastosowane, aby lepiej zrozumieć sytuację i poprawić procesy biznesowe.

## Co można zrobić z danymi

W nauce o danych skupiamy się na następujących etapach pracy z danymi:

Oczywiście, w zależności od rodzaju danych, niektóre etapy mogą być pominięte (np. gdy dane są już w bazie danych lub gdy nie potrzebujemy trenowania modelu), a niektóre etapy mogą być powtarzane wielokrotnie (np. przetwarzanie danych).

## Cyfryzacja i transformacja cyfrowa

W ostatniej dekadzie wiele firm zaczęło dostrzegać znaczenie danych w podejmowaniu decyzji biznesowych. Aby zastosować zasady nauki o danych w prowadzeniu biznesu, najpierw trzeba zebrać dane, czyli przekształcić procesy biznesowe w formę cyfrową. To nazywa się **cyfryzacją**. Zastosowanie technik nauki o danych do tych danych w celu podejmowania decyzji może prowadzić do znacznego wzrostu produktywności (lub nawet zmiany kierunku działalności), co nazywa się **transformacją cyfrową**.

Rozważmy przykład. Załóżmy, że mamy kurs nauki o danych (taki jak ten), który prowadzimy online dla studentów, i chcemy go ulepszyć za pomocą nauki o danych. Jak możemy to zrobić?

Możemy zacząć od pytania "Co można cyfryzować?" Najprostszym sposobem byłoby zmierzenie czasu, jaki każdy student potrzebuje na ukończenie każdego modułu, oraz zmierzenie zdobytej wiedzy poprzez test wielokrotnego wyboru na końcu każdego modułu. Średnia czasu ukończenia dla wszystkich studentów pozwoli nam zidentyfikować moduły, które sprawiają największe trudności, i pracować nad ich uproszczeniem.
Można argumentować, że takie podejście nie jest idealne, ponieważ moduły mogą mieć różne długości. Prawdopodobnie bardziej sprawiedliwe byłoby podzielenie czasu przez długość modułu (w liczbie znaków) i porównanie tych wartości zamiast tego.
Kiedy zaczynamy analizować wyniki testów wielokrotnego wyboru, możemy spróbować określić, które pojęcia sprawiają trudność uczniom, i wykorzystać te informacje do ulepszenia treści. Aby to zrobić, musimy zaprojektować testy w taki sposób, aby każde pytanie odnosiło się do konkretnego pojęcia lub fragmentu wiedzy.

Jeśli chcemy podejść do tego jeszcze bardziej szczegółowo, możemy zestawić czas potrzebny na ukończenie każdego modułu z kategorią wiekową uczniów. Możemy odkryć, że dla niektórych grup wiekowych ukończenie modułu zajmuje nieproporcjonalnie dużo czasu lub że uczniowie rezygnują przed jego ukończeniem. To może pomóc nam w określeniu zaleceń wiekowych dla modułu i zminimalizowaniu niezadowolenia wynikającego z niewłaściwych oczekiwań.

## 🚀 Wyzwanie

W tym wyzwaniu spróbujemy znaleźć pojęcia związane z dziedziną Data Science, analizując teksty. Weźmiemy artykuł z Wikipedii na temat Data Science, pobierzemy i przetworzymy tekst, a następnie stworzymy chmurę słów, taką jak ta:

![Chmura słów dla Data Science](../../../../1-Introduction/01-defining-data-science/images/ds_wordcloud.png)

Odwiedź [`notebook.ipynb`](../../../../../../../../../1-Introduction/01-defining-data-science/notebook.ipynb ':ignore'), aby przejrzeć kod. Możesz również uruchomić kod i zobaczyć, jak w czasie rzeczywistym wykonuje wszystkie transformacje danych.

> Jeśli nie wiesz, jak uruchomić kod w Jupyter Notebook, zapoznaj się z [tym artykułem](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## [Quiz po wykładzie](https://ff-quizzes.netlify.app/en/ds/quiz/1)

## Zadania

* **Zadanie 1**: Zmodyfikuj powyższy kod, aby znaleźć powiązane pojęcia dla dziedzin **Big Data** i **Machine Learning**
* **Zadanie 2**: [Przemyśl scenariusze związane z Data Science](assignment.md)

## Podziękowania

Ta lekcja została stworzona z ♥️ przez [Dmitry Soshnikov](http://soshnikov.com)

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.