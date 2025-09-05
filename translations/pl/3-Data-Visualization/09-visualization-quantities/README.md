<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a49d78e32e280c410f04e5f2a2068e77",
  "translation_date": "2025-09-05T14:38:56+00:00",
  "source_file": "3-Data-Visualization/09-visualization-quantities/README.md",
  "language_code": "pl"
}
-->
# Wizualizacja ilości

|![ Sketchnote autorstwa [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| Wizualizacja ilości - _Sketchnote autorstwa [@nitya](https://twitter.com/nitya)_ |

W tej lekcji dowiesz się, jak korzystać z jednej z wielu dostępnych bibliotek Pythona, aby tworzyć ciekawe wizualizacje związane z pojęciem ilości. Korzystając z oczyszczonego zestawu danych o ptakach z Minnesoty, możesz poznać wiele interesujących faktów o lokalnej faunie.

## [Quiz przed wykładem](https://ff-quizzes.netlify.app/en/ds/quiz/16)

## Obserwacja rozpiętości skrzydeł za pomocą Matplotlib

Doskonałą biblioteką do tworzenia zarówno prostych, jak i zaawansowanych wykresów oraz diagramów różnego rodzaju jest [Matplotlib](https://matplotlib.org/stable/index.html). Ogólnie rzecz biorąc, proces tworzenia wykresów za pomocą tych bibliotek obejmuje identyfikację części ramki danych, które chcesz wykorzystać, przeprowadzenie niezbędnych transformacji danych, przypisanie wartości osi x i y, wybór rodzaju wykresu, a następnie jego wyświetlenie. Matplotlib oferuje szeroką gamę wizualizacji, ale w tej lekcji skupimy się na tych najbardziej odpowiednich do wizualizacji ilości: wykresach liniowych, wykresach punktowych i wykresach słupkowych.

> ✅ Wybierz najlepszy typ wykresu, który pasuje do struktury Twoich danych i historii, którą chcesz opowiedzieć.  
> - Aby analizować trendy w czasie: linia  
> - Aby porównywać wartości: słupki, kolumny, koło, wykres punktowy  
> - Aby pokazać, jak części odnoszą się do całości: koło  
> - Aby pokazać rozkład danych: wykres punktowy, słupki  
> - Aby pokazać trendy: linia, kolumny  
> - Aby pokazać relacje między wartościami: linia, wykres punktowy, bąbelkowy  

Jeśli masz zestaw danych i chcesz dowiedzieć się, ile danego elementu jest zawarte, jednym z pierwszych zadań będzie inspekcja jego wartości.

✅ Dostępne są bardzo dobre 'ściągi' dla Matplotlib [tutaj](https://matplotlib.org/cheatsheets/cheatsheets.pdf).

## Tworzenie wykresu liniowego dotyczącego rozpiętości skrzydeł ptaków

Otwórz plik `notebook.ipynb` znajdujący się w głównym folderze tej lekcji i dodaj komórkę.

> Uwaga: dane są przechowywane w głównym folderze tego repozytorium w katalogu `/data`.

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```  
Te dane to mieszanka tekstu i liczb:

|      | Nazwa                        | NazwaNaukowa           | Kategoria             | Rząd         | Rodzina  | Rodzaj      | StatusOchrony       | MinDługość | MaxDługość | MinMasaCiała | MaxMasaCiała | MinRozpiętość | MaxRozpiętość |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Czarnobrzuchy gwizduś        | Dendrocygna autumnalis | Kaczki/Gęsi/Wodne     | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Płowy gwizduś                | Dendrocygna bicolor    | Kaczki/Gęsi/Wodne     | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Gęś śnieżna                  | Anser caerulescens     | Kaczki/Gęsi/Wodne     | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Gęś Ross'a                   | Anser rossii           | Kaczki/Gęsi/Wodne     | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Gęś białoczelna              | Anser albifrons        | Kaczki/Gęsi/Wodne     | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

Zacznijmy od wykreślenia niektórych danych liczbowych za pomocą podstawowego wykresu liniowego. Załóżmy, że chcesz zobaczyć maksymalną rozpiętość skrzydeł tych interesujących ptaków.

```python
wingspan = birds['MaxWingspan'] 
wingspan.plot()
```  
![Max Rozpiętość](../../../../3-Data-Visualization/09-visualization-quantities/images/max-wingspan-02.png)

Co zauważasz od razu? Wydaje się, że jest co najmniej jeden odstający wynik - to całkiem imponująca rozpiętość skrzydeł! Rozpiętość skrzydeł wynosząca 2300 centymetrów to 23 metry - czy w Minnesocie latają pterodaktyle? Zbadajmy to.

Chociaż możesz szybko posortować dane w Excelu, aby znaleźć te odstające wyniki, kontynuuj proces wizualizacji, pracując bezpośrednio z wykresem.

Dodaj etykiety do osi x, aby pokazać, o jakie ptaki chodzi:

```
plt.title('Max Wingspan in Centimeters')
plt.ylabel('Wingspan (CM)')
plt.xlabel('Birds')
plt.xticks(rotation=45)
x = birds['Name'] 
y = birds['MaxWingspan']

plt.plot(x, y)

plt.show()
```  
![Rozpiętość z etykietami](../../../../3-Data-Visualization/09-visualization-quantities/images/max-wingspan-labels-02.png)

Nawet przy obrocie etykiet o 45 stopni jest ich zbyt wiele, aby je odczytać. Spróbujmy innej strategii: oznacz tylko te odstające wyniki i umieść etykiety na wykresie. Możesz użyć wykresu punktowego, aby zrobić więcej miejsca na etykiety:

```python
plt.title('Max Wingspan in Centimeters')
plt.ylabel('Wingspan (CM)')
plt.tick_params(axis='both',which='both',labelbottom=False,bottom=False)

for i in range(len(birds)):
    x = birds['Name'][i]
    y = birds['MaxWingspan'][i]
    plt.plot(x, y, 'bo')
    if birds['MaxWingspan'][i] > 500:
        plt.text(x, y * (1 - 0.05), birds['Name'][i], fontsize=12)
    
plt.show()
```  
Co tu się dzieje? Użyłeś `tick_params`, aby ukryć dolne etykiety, a następnie stworzyłeś pętlę nad zestawem danych o ptakach. Tworząc wykres z małymi okrągłymi niebieskimi punktami za pomocą `bo`, sprawdziłeś, czy którykolwiek ptak ma maksymalną rozpiętość skrzydeł większą niż 500 i wyświetliłeś jego etykietę obok punktu, jeśli tak. Przesunąłeś etykiety nieco na osi y (`y * (1 - 0.05)`) i użyłeś nazwy ptaka jako etykiety.

Co odkryłeś?

![Odstające wyniki](../../../../3-Data-Visualization/09-visualization-quantities/images/labeled-wingspan-02.png)

## Filtruj swoje dane

Zarówno Bielik amerykański, jak i Sokół preriowy, choć prawdopodobnie bardzo duże ptaki, wydają się być błędnie oznaczone, z dodatkowym `0` dodanym do ich maksymalnej rozpiętości skrzydeł. Mało prawdopodobne, że spotkasz Bielika z rozpiętością skrzydeł 25 metrów, ale jeśli tak, daj nam znać! Stwórzmy nową ramkę danych bez tych dwóch odstających wyników:

```python
plt.title('Max Wingspan in Centimeters')
plt.ylabel('Wingspan (CM)')
plt.xlabel('Birds')
plt.tick_params(axis='both',which='both',labelbottom=False,bottom=False)
for i in range(len(birds)):
    x = birds['Name'][i]
    y = birds['MaxWingspan'][i]
    if birds['Name'][i] not in ['Bald eagle', 'Prairie falcon']:
        plt.plot(x, y, 'bo')
plt.show()
```  

Po odfiltrowaniu odstających wyników, Twoje dane są teraz bardziej spójne i zrozumiałe.

![Wykres punktowy rozpiętości skrzydeł](../../../../3-Data-Visualization/09-visualization-quantities/images/scatterplot-wingspan-02.png)

Teraz, gdy mamy czystszy zestaw danych przynajmniej pod względem rozpiętości skrzydeł, odkryjmy więcej o tych ptakach.

Podczas gdy wykresy liniowe i punktowe mogą przedstawiać informacje o wartościach danych i ich rozkładach, chcemy pomyśleć o wartościach zawartych w tym zestawie danych. Możesz tworzyć wizualizacje, aby odpowiedzieć na następujące pytania dotyczące ilości:

> Ile kategorii ptaków istnieje i jakie są ich liczby?  
> Ile ptaków jest wymarłych, zagrożonych, rzadkich lub pospolitych?  
> Ile jest różnych rodzajów i rzędów w terminologii Linneusza?  

## Eksploracja wykresów słupkowych

Wykresy słupkowe są praktyczne, gdy chcesz pokazać grupowanie danych. Zbadajmy kategorie ptaków, które istnieją w tym zestawie danych, aby zobaczyć, która jest najliczniejsza.

W pliku notebooka stwórz podstawowy wykres słupkowy.

✅ Uwaga, możesz albo odfiltrować dwa odstające ptaki, które zidentyfikowaliśmy w poprzedniej sekcji, poprawić błąd w ich rozpiętości skrzydeł, albo pozostawić je w tych ćwiczeniach, które nie zależą od wartości rozpiętości skrzydeł.

Jeśli chcesz stworzyć wykres słupkowy, możesz wybrać dane, na których chcesz się skupić. Wykresy słupkowe można tworzyć z surowych danych:

```python
birds.plot(x='Category',
        kind='bar',
        stacked=True,
        title='Birds of Minnesota')

```  
![Pełne dane jako wykres słupkowy](../../../../3-Data-Visualization/09-visualization-quantities/images/full-data-bar-02.png)

Ten wykres słupkowy jest jednak nieczytelny, ponieważ jest zbyt wiele niegrupowanych danych. Musisz wybrać tylko dane, które chcesz wykreślić, więc spójrzmy na długość ptaków w zależności od ich kategorii.

Przefiltruj swoje dane, aby uwzględnić tylko kategorię ptaków.

✅ Zauważ, że używasz Pandas do zarządzania danymi, a następnie pozwalasz Matplotlib na tworzenie wykresów.

Ponieważ jest wiele kategorii, możesz wyświetlić ten wykres pionowo i dostosować jego wysokość, aby uwzględnić wszystkie dane:

```python
category_count = birds.value_counts(birds['Category'].values, sort=True)
plt.rcParams['figure.figsize'] = [6, 12]
category_count.plot.barh()
```  
![Kategoria i długość](../../../../3-Data-Visualization/09-visualization-quantities/images/category-counts-02.png)

Ten wykres słupkowy pokazuje dobry widok liczby ptaków w każdej kategorii. Na pierwszy rzut oka widzisz, że największa liczba ptaków w tym regionie należy do kategorii Kaczki/Gęsi/Wodne. Minnesota to 'kraina 10 000 jezior', więc to nie jest zaskakujące!

✅ Spróbuj innych obliczeń na tym zestawie danych. Czy coś Cię zaskoczyło?

## Porównywanie danych

Możesz spróbować różnych porównań grupowanych danych, tworząc nowe osie. Spróbuj porównać MaxDługość ptaka w zależności od jego kategorii:

```python
maxlength = birds['MaxLength']
plt.barh(y=birds['Category'], width=maxlength)
plt.rcParams['figure.figsize'] = [6, 12]
plt.show()
```  
![Porównywanie danych](../../../../3-Data-Visualization/09-visualization-quantities/images/category-length-02.png)

Nic tu nie zaskakuje: kolibry mają najmniejszą MaxDługość w porównaniu do pelikanów czy gęsi. Dobrze, gdy dane mają logiczny sens!

Możesz tworzyć bardziej interesujące wizualizacje wykresów słupkowych, nakładając dane. Nałóż Minimalną i Maksymalną Długość na daną kategorię ptaków:

```python
minLength = birds['MinLength']
maxLength = birds['MaxLength']
category = birds['Category']

plt.barh(category, maxLength)
plt.barh(category, minLength)

plt.show()
```  
Na tym wykresie możesz zobaczyć zakres dla każdej kategorii ptaków w odniesieniu do Minimalnej i Maksymalnej Długości. Możesz śmiało powiedzieć, że na podstawie tych danych, im większy ptak, tym większy zakres jego długości. Fascynujące!

![Nakładanie wartości](../../../../3-Data-Visualization/09-visualization-quantities/images/superimposed-02.png)

## 🚀 Wyzwanie

Ten zestaw danych o ptakach oferuje bogactwo informacji o różnych typach ptaków w określonym ekosystemie. Poszukaj w internecie innych zestawów danych związanych z ptakami. Ćwicz tworzenie wykresów i diagramów dotyczących tych ptaków, aby odkryć fakty, których wcześniej nie znałeś.

## [Quiz po wykładzie](https://ff-quizzes.netlify.app/en/ds/quiz/17)

## Przegląd i samodzielna nauka

Ta pierwsza lekcja dostarczyła Ci informacji o tym, jak korzystać z Matplotlib do wizualizacji ilości. Przeprowadź badania na temat innych sposobów pracy z zestawami danych w celu wizualizacji. [Plotly](https://github.com/plotly/plotly.py) to jedna z opcji, której nie omówimy w tych lekcjach, więc sprawdź, co może zaoferować.

## Zadanie

[Linie, Punkty i Słupki](assignment.md)

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku źródłowym powinien być uznawany za autorytatywne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.