<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "43212cc1ac137b7bb1dcfb37ca06b0f4",
  "translation_date": "2025-10-25T18:51:10+00:00",
  "source_file": "1-Introduction/01-defining-data-science/README.md",
  "language_code": "pl"
}
-->
# Definiowanie Data Science

| ![ Sketchnote autorstwa [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/01-Definitions.png) |
| :----------------------------------------------------------------------------------------------------------: |
|              Definiowanie Data Science - _Sketchnote autorstwa [@nitya](https://twitter.com/nitya)_           |

---

[![Film o definicji Data Science](../../../../translated_images/pl/video-def-ds.6623ee2392ef1abf6d7faf3fad10a4163642811749da75f44e35a5bb121de15c.png)](https://youtu.be/beZ7Mb_oz9I)

## [Quiz przed wykładem](https://ff-quizzes.netlify.app/en/ds/quiz/0)

## Co to jest dane?
W naszym codziennym życiu jesteśmy nieustannie otoczeni danymi. Tekst, który teraz czytasz, to dane. Lista numerów telefonów twoich znajomych w smartfonie to dane, podobnie jak aktualny czas wyświetlany na zegarku. Jako ludzie naturalnie operujemy danymi, licząc pieniądze, które posiadamy, czy pisząc listy do przyjaciół.

Jednak dane stały się znacznie bardziej istotne wraz z powstaniem komputerów. Główną rolą komputerów jest wykonywanie obliczeń, ale potrzebują one danych, aby na nich operować. Dlatego musimy zrozumieć, jak komputery przechowują i przetwarzają dane.

Wraz z pojawieniem się Internetu rola komputerów jako urządzeń do obsługi danych wzrosła. Jeśli się nad tym zastanowisz, obecnie coraz częściej używamy komputerów do przetwarzania danych i komunikacji, a nie do samych obliczeń. Kiedy piszemy e-mail do przyjaciela lub szukamy informacji w Internecie, w istocie tworzymy, przechowujemy, przesyłamy i manipulujemy danymi.
> Czy pamiętasz, kiedy ostatni raz używałeś komputera do faktycznego wykonywania obliczeń?

## Co to jest Data Science?

Na [Wikipedii](https://en.wikipedia.org/wiki/Data_science) **Data Science** jest definiowane jako *dziedzina naukowa, która wykorzystuje metody naukowe do wydobywania wiedzy i wniosków z danych strukturalnych i niestrukturalnych oraz stosowania wiedzy i praktycznych wniosków z danych w szerokim zakresie dziedzin zastosowań*.

Ta definicja podkreśla następujące ważne aspekty data science:

* Głównym celem data science jest **wydobywanie wiedzy** z danych, innymi słowy - **zrozumienie** danych, znalezienie ukrytych zależności i budowanie **modelu**.
* Data science wykorzystuje **metody naukowe**, takie jak prawdopodobieństwo i statystyka. W rzeczywistości, gdy po raz pierwszy wprowadzono termin *data science*, niektórzy twierdzili, że jest to tylko nowa, modna nazwa dla statystyki. Obecnie stało się jasne, że dziedzina ta jest znacznie szersza.
* Uzyskana wiedza powinna być stosowana do tworzenia **praktycznych wniosków**, czyli wniosków, które można zastosować w rzeczywistych sytuacjach biznesowych.
* Powinniśmy być w stanie operować zarówno na danych **strukturalnych**, jak i **niestrukturalnych**. Wrócimy do omówienia różnych typów danych później w kursie.
* **Dziedzina zastosowania** to ważne pojęcie, a specjaliści od data science często potrzebują przynajmniej pewnego stopnia wiedzy w danej dziedzinie, na przykład: finanse, medycyna, marketing itp.

> Kolejnym istotnym aspektem Data Science jest badanie, w jaki sposób dane mogą być zbierane, przechowywane i przetwarzane za pomocą komputerów. Podczas gdy statystyka dostarcza nam podstaw matematycznych, data science stosuje koncepcje matematyczne, aby faktycznie wyciągać wnioski z danych.

Jednym ze sposobów (przypisywanym [Jimowi Grayowi](https://en.wikipedia.org/wiki/Jim_Gray_(computer_scientist))) spojrzenia na data science jest uznanie jej za odrębny paradygmat nauki:
* **Empiryczny**, w którym opieramy się głównie na obserwacjach i wynikach eksperymentów
* **Teoretyczny**, gdzie nowe koncepcje wyłaniają się z istniejącej wiedzy naukowej
* **Obliczeniowy**, gdzie odkrywamy nowe zasady na podstawie eksperymentów obliczeniowych
* **Oparty na danych**, bazujący na odkrywaniu relacji i wzorców w danych  

## Powiązane dziedziny

Ponieważ dane są wszechobecne, data science samo w sobie jest również szeroką dziedziną, dotykającą wielu innych dyscyplin.

<dl>
<dt>Bazy danych</dt>
<dd>
Kluczowym zagadnieniem jest <b>jak przechowywać</b> dane, czyli jak je strukturyzować w sposób umożliwiający szybsze przetwarzanie. Istnieją różne typy baz danych, które przechowują dane strukturalne i niestrukturalne, co <a href="../../2-Working-With-Data/README.md">rozważymy w naszym kursie</a>.
</dd>
<dt>Big Data</dt>
<dd>
Często musimy przechowywać i przetwarzać bardzo duże ilości danych o stosunkowo prostej strukturze. Istnieją specjalne podejścia i narzędzia do przechowywania tych danych w sposób rozproszony na klastrze komputerowym i ich efektywnego przetwarzania.
</dd>
<dt>Uczenie maszynowe</dt>
<dd>
Jednym ze sposobów zrozumienia danych jest <b>budowanie modelu</b>, który będzie w stanie przewidzieć pożądany wynik. Opracowywanie modeli na podstawie danych nazywa się <b>uczeniem maszynowym</b>. Możesz zapoznać się z naszym <a href="https://aka.ms/ml-beginners">Kurs Uczenia Maszynowego dla Początkujących</a>, aby dowiedzieć się więcej na ten temat.
</dd>
<dt>Sztuczna inteligencja</dt>
<dd>
Dziedzina uczenia maszynowego znana jako sztuczna inteligencja (AI) również opiera się na danych i obejmuje budowanie modeli o wysokiej złożoności, które naśladują procesy myślowe człowieka. Metody AI często pozwalają nam przekształcić dane niestrukturalne (np. język naturalny) w uporządkowane wnioski.
</dd>
<dt>Wizualizacja</dt>
<dd>
Ogromne ilości danych są niezrozumiałe dla człowieka, ale gdy stworzymy przydatne wizualizacje z tych danych, możemy lepiej je zrozumieć i wyciągnąć wnioski. Dlatego ważne jest, aby znać wiele sposobów wizualizacji informacji - coś, co omówimy w <a href="../../3-Data-Visualization/README.md">Sekcji 3</a> naszego kursu. Powiązane dziedziny obejmują również <b>Infografikę</b> oraz ogólnie <b>Interakcję Człowiek-Komputer</b>.
</dd>
</dl>

## Typy danych

Jak już wspomnieliśmy, dane są wszędzie. Wystarczy je odpowiednio uchwycić! Warto rozróżnić dane **strukturalne** i **niestrukturalne**. Te pierwsze są zazwyczaj przedstawiane w dobrze zorganizowanej formie, często jako tabela lub zestaw tabel, podczas gdy te drugie to po prostu zbiór plików. Czasami możemy również mówić o danych **półstrukturalnych**, które mają pewien rodzaj struktury, ale może się ona znacznie różnić.

| Strukturalne                                                               | Półstrukturalne                                                                                  | Niestrukturalne                        |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | -------------------------------------- |
| Lista osób z ich numerami telefonów                                        | Strony Wikipedii z linkami                                                                       | Tekst Encyklopedii Britannica          |
| Temperatura we wszystkich pomieszczeniach budynku co minutę przez ostatnie 20 lat | Zbiór artykułów naukowych w formacie JSON z autorami, datą publikacji i streszczeniem            | Udostępnione pliki z dokumentami firmowymi |
| Dane dotyczące wieku i płci wszystkich osób wchodzących do budynku         | Strony internetowe                                                                               | Surowy materiał wideo z kamery monitoringu |

## Skąd pozyskiwać dane

Istnieje wiele możliwych źródeł danych i niemożliwe jest wymienienie ich wszystkich! Jednak wspomnijmy o kilku typowych miejscach, z których można pozyskać dane:

* **Strukturalne**
  - **Internet rzeczy** (IoT), w tym dane z różnych czujników, takich jak czujniki temperatury czy ciśnienia, dostarcza wiele przydatnych informacji. Na przykład, jeśli budynek biurowy jest wyposażony w czujniki IoT, możemy automatycznie kontrolować ogrzewanie i oświetlenie, aby zminimalizować koszty.
  - **Ankiety**, które prosimy użytkowników o wypełnienie po zakupie lub po odwiedzeniu strony internetowej.
  - **Analiza zachowań** może na przykład pomóc nam zrozumieć, jak głęboko użytkownik zagłębia się w stronę i jaki jest typowy powód opuszczenia strony.
* **Niestrukturalne**
  - **Teksty** mogą być bogatym źródłem wniosków, takich jak ogólny **wskaźnik nastroju** czy wyodrębnianie słów kluczowych i znaczenia semantycznego.
  - **Obrazy** lub **wideo**. Film z kamery monitoringu może być użyty do oszacowania ruchu na drodze i informowania ludzi o potencjalnych korkach.
  - **Logi serwera internetowego** mogą być używane do zrozumienia, które strony naszej witryny są najczęściej odwiedzane i jak długo.
* Półstrukturalne
  - **Grafy sieci społecznościowych** mogą być doskonałym źródłem danych o osobowościach użytkowników i potencjalnej skuteczności w rozpowszechnianiu informacji.
  - Gdy mamy zbiór zdjęć z imprezy, możemy spróbować wyodrębnić dane o **dynamice grupy**, budując graf osób robiących sobie zdjęcia nawzajem.

Znając różne możliwe źródła danych, możesz spróbować pomyśleć o różnych scenariuszach, w których techniki data science mogą być zastosowane, aby lepiej zrozumieć sytuację i poprawić procesy biznesowe.

## Co można zrobić z danymi

W Data Science skupiamy się na następujących etapach podróży danych:

<dl>
<dt>1) Pozyskiwanie danych</dt>
<dd>
Pierwszym krokiem jest zebranie danych. Chociaż w wielu przypadkach może to być prosty proces, jak dane trafiające do bazy danych z aplikacji internetowej, czasami musimy użyć specjalnych technik. Na przykład dane z czujników IoT mogą być przytłaczające, dlatego dobrą praktyką jest użycie punktów buforowych, takich jak IoT Hub, do zbierania wszystkich danych przed dalszym przetwarzaniem.
</dd>
<dt>2) Przechowywanie danych</dt>
<dd>
Przechowywanie danych może być wyzwaniem, zwłaszcza jeśli mówimy o dużych zbiorach danych. Decydując, jak przechowywać dane, warto przewidzieć sposób, w jaki będziemy chcieli je później przeszukiwać. Istnieje kilka sposobów przechowywania danych:
<ul>
<li>Relacyjna baza danych przechowuje zbiór tabel i używa specjalnego języka o nazwie SQL do ich przeszukiwania. Zazwyczaj tabele są organizowane w różne grupy zwane schematami. W wielu przypadkach musimy przekształcić dane z ich pierwotnej formy, aby pasowały do schematu.</li>
<li><a href="https://en.wikipedia.org/wiki/NoSQL">Baza danych NoSQL</a>, taka jak <a href="https://azure.microsoft.com/services/cosmos-db/?WT.mc_id=academic-77958-bethanycheum">CosmosDB</a>, nie narzuca schematów na dane i pozwala na przechowywanie bardziej złożonych danych, na przykład hierarchicznych dokumentów JSON lub grafów. Jednak bazy danych NoSQL nie mają tak bogatych możliwości zapytań jak SQL i nie mogą wymuszać integralności referencyjnej, czyli zasad dotyczących struktury danych w tabelach i relacji między nimi.</li>
<li><a href="https://en.wikipedia.org/wiki/Data_lake">Magazyn Data Lake</a> jest używany do dużych zbiorów danych w surowej, niestrukturalnej formie. Data lakes są często używane w przypadku big data, gdzie wszystkie dane nie mogą zmieścić się na jednej maszynie i muszą być przechowywane i przetwarzane przez klaster serwerów. <a href="https://en.wikipedia.org/wiki/Apache_Parquet">Parquet</a> to format danych, który jest często używany w połączeniu z big data.</li> 
</ul>
</dd>
<dt>3) Przetwarzanie danych</dt>
<dd>
To najbardziej ekscytująca część podróży danych, która polega na przekształceniu danych z ich pierwotnej formy w formę, która może być użyta do wizualizacji lub trenowania modelu. W przypadku danych niestrukturalnych, takich jak tekst czy obrazy, możemy potrzebować użyć technik AI, aby wyodrębnić <b>cechy</b> z danych, przekształcając je w formę strukturalną.
</dd>
<dt>4) Wizualizacja / Wnioski ludzkie</dt>
<dd>
Często, aby zrozumieć dane, musimy je zwizualizować. Mając wiele różnych technik wizualizacji w naszym arsenale, możemy znaleźć odpowiedni sposób, aby uzyskać wgląd. Często specjalista od data science musi "bawić się danymi", wielokrotnie je wizualizując i szukając relacji. Możemy również używać technik statystycznych, aby testować hipotezy lub udowadniać korelacje między różnymi elementami danych.
</dd>
<dt>5) Trenowanie modelu predykcyjnego</dt>
<dd>
Ponieważ ostatecznym celem data science jest podejmowanie decyzji na podstawie danych, możemy chcieć użyć technik <a href="http://github.com/microsoft/ml-for-beginners">Uczenia Maszynowego</a>, aby zbudować model predykcyjny. Możemy go następnie używać do przewidywania na podstawie nowych zestawów danych o podobnej strukturze.
</dd>
</dl>

Oczywiście, w zależności od rzeczywistych danych, niektóre kroki mogą być pominięte (np. gdy dane są już w bazie danych lub gdy nie potrzebujemy trenowania modelu), lub niektóre kroki mogą być powtarzane wielokrotnie (takie jak przetwarzanie danych).

## Cyfryzacja i transformacja cyfrowa

W ostatniej dekadzie wiele firm zaczęło rozumieć znaczenie danych przy podejmowaniu decyzji biznesowych. Aby zastosować zasady data science w prowadzeniu biznesu, najpierw trzeba zebrać dane, czyli przekształcić procesy biznesowe w formę cyfrową. Nazywa się to **cyfryzacją**. Zastosowanie technik data science do tych danych w celu podejmowania decyzji może prowadzić do znacznego wzrostu produktywności (a nawet zmiany kierunku działalności), co nazywa się **transformacją cyfrową**.

Rozważmy przykład. Załóżmy, że mamy kurs data science (taki jak ten), który prowadzimy online dla studentów i chcemy użyć data science, aby go ulepszyć. Jak możemy to zrobić?

Możemy zacząć od pytania "Co można zdigitalizować?" Najprostszym sposobem byłoby zmierzenie czasu, jaki zajmuje każdemu studentowi ukończenie każdego modułu, oraz zmierzenie zdobytej wiedzy poprzez przeprowadzenie testu wielokrotnego wyboru na końcu każdego modułu. Średnia czasu ukończenia dla wszystkich studentów pozwoli nam dowiedzieć się, które moduły sprawiają studentom największe trudności i nad którymi warto popracować, aby je uprościć.
> Możesz argumentować, że takie podejście nie jest idealne, ponieważ moduły mogą mieć różną długość. Prawdopodobnie bardziej sprawiedliwe byłoby podzielenie czasu przez długość modułu (w liczbie znaków) i porównanie tych wartości.

Kiedy zaczynamy analizować wyniki testów wielokrotnego wyboru, możemy spróbować określić, które koncepcje sprawiają trudności w zrozumieniu uczniom, i wykorzystać te informacje do ulepszenia treści. Aby to zrobić, musimy zaprojektować testy w taki sposób, aby każde pytanie odnosiło się do konkretnej koncepcji lub fragmentu wiedzy.

Jeśli chcemy podejść do tego jeszcze bardziej szczegółowo, możemy zestawić czas potrzebny na ukończenie każdego modułu z kategorią wiekową uczniów. Możemy odkryć, że dla niektórych grup wiekowych ukończenie modułu zajmuje nieproporcjonalnie dużo czasu lub że uczniowie rezygnują przed jego ukończeniem. Może to pomóc nam w określeniu zaleceń wiekowych dla modułu i zminimalizowaniu niezadowolenia wynikającego z niewłaściwych oczekiwań.

## 🚀 Wyzwanie

W tym wyzwaniu spróbujemy znaleźć koncepcje związane z dziedziną Data Science, analizując teksty. Weźmiemy artykuł z Wikipedii na temat Data Science, pobierzemy i przetworzymy tekst, a następnie stworzymy chmurę słów, taką jak ta:

![Chmura słów dla Data Science](../../../../translated_images/pl/ds_wordcloud.664a7c07dca57de017c22bf0498cb40f898d48aa85b3c36a80620fea12fadd42.png)

Odwiedź [`notebook.ipynb`](../../../../1-Introduction/01-defining-data-science/notebook.ipynb ':ignore'), aby zapoznać się z kodem. Możesz również uruchomić kod i zobaczyć, jak w czasie rzeczywistym wykonuje wszystkie transformacje danych.

> Jeśli nie wiesz, jak uruchomić kod w Jupyter Notebook, zapoznaj się z [tym artykułem](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## [Quiz po wykładzie](https://ff-quizzes.netlify.app/en/ds/quiz/1)

## Zadania

* **Zadanie 1**: Zmodyfikuj powyższy kod, aby znaleźć powiązane koncepcje dla dziedzin **Big Data** i **Machine Learning**.
* **Zadanie 2**: [Przemyśl scenariusze związane z Data Science](assignment.md)

## Podziękowania

Ta lekcja została stworzona z ♥️ przez [Dmitry Soshnikov](http://soshnikov.com)

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.