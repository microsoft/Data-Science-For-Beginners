<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1b560955ff39a2bcf2a049fce474a951",
  "translation_date": "2025-09-05T14:33:22+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "pl"
}
-->
# Praca z danymi: Przygotowanie danych

|![ Sketchnote autorstwa [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|Przygotowanie danych - _Sketchnote autorstwa [@nitya](https://twitter.com/nitya)_ |

## [Quiz przed wykładem](https://ff-quizzes.netlify.app/en/ds/quiz/14)

W zależności od źródła, surowe dane mogą zawierać pewne niespójności, które utrudniają analizę i modelowanie. Innymi słowy, takie dane można określić jako „brudne” i wymagają one oczyszczenia. Ta lekcja koncentruje się na technikach czyszczenia i przekształcania danych, aby poradzić sobie z problemami brakujących, niedokładnych lub niekompletnych danych. Omawiane tematy wykorzystują język Python i bibliotekę Pandas, a ich zastosowanie zostanie [zademonstrowane w notatniku](../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb) w tym katalogu.

## Dlaczego czyszczenie danych jest ważne

- **Łatwość użycia i ponownego wykorzystania**: Kiedy dane są odpowiednio zorganizowane i znormalizowane, łatwiej je przeszukiwać, używać i udostępniać innym.

- **Spójność**: Praca z danymi często wymaga korzystania z więcej niż jednego zbioru danych, które pochodzą z różnych źródeł i muszą zostać połączone. Zapewnienie wspólnej standaryzacji każdego zbioru danych gwarantuje, że dane pozostaną użyteczne po ich scaleniu w jeden zbiór.

- **Dokładność modeli**: Oczyszczone dane poprawiają dokładność modeli, które na nich bazują.

## Typowe cele i strategie czyszczenia danych

- **Eksploracja zbioru danych**: Eksploracja danych, która zostanie omówiona w [późniejszej lekcji](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing), może pomóc w odkryciu danych wymagających oczyszczenia. Wizualna obserwacja wartości w zbiorze danych pozwala ustalić oczekiwania co do jego struktury lub wskazać problemy, które można rozwiązać. Eksploracja może obejmować podstawowe zapytania, wizualizacje i próbkowanie.

- **Formatowanie**: W zależności od źródła, dane mogą być niespójne w sposobie ich prezentacji. Może to powodować problemy z wyszukiwaniem i reprezentacją wartości, które są widoczne w zbiorze danych, ale nie są poprawnie przedstawiane w wizualizacjach lub wynikach zapytań. Typowe problemy z formatowaniem obejmują usuwanie białych znaków, formatowanie dat i typów danych. Rozwiązywanie tych problemów zazwyczaj należy do osób korzystających z danych. Na przykład standardy dotyczące prezentacji dat i liczb mogą różnić się w zależności od kraju.

- **Duplikaty**: Dane, które występują więcej niż raz, mogą prowadzić do niedokładnych wyników i zazwyczaj powinny zostać usunięte. Jest to częsty problem przy łączeniu dwóch lub więcej zbiorów danych. Jednak w niektórych przypadkach duplikaty mogą zawierać dodatkowe informacje i powinny zostać zachowane.

- **Brakujące dane**: Brakujące dane mogą powodować niedokładności oraz słabe lub stronnicze wyniki. Czasami można je uzupełnić poprzez „ponowne załadowanie” danych, wypełnienie brakujących wartości za pomocą obliczeń i kodu w Pythonie lub po prostu usunięcie brakujących wartości i odpowiadających im danych. Istnieje wiele powodów, dla których dane mogą być brakujące, a działania podejmowane w celu ich uzupełnienia zależą od przyczyny ich braku.

## Eksploracja informacji o DataFrame
> **Cel nauki:** Po zakończeniu tej sekcji powinieneś być w stanie znaleźć ogólne informacje o danych przechowywanych w DataFrame biblioteki pandas.

Po załadowaniu danych do pandas, najprawdopodobniej będą one znajdować się w obiekcie DataFrame (odwołaj się do poprzedniej [lekcji](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe), aby uzyskać szczegółowy przegląd). Jednak jeśli zbiór danych w Twoim DataFrame zawiera 60 000 wierszy i 400 kolumn, jak zacząć orientować się, z czym masz do czynienia? Na szczęście [pandas](https://pandas.pydata.org/) oferuje wygodne narzędzia do szybkiego przeglądania ogólnych informacji o DataFrame, a także pierwszych i ostatnich kilku wierszy.

Aby zbadać tę funkcjonalność, zaimportujemy bibliotekę Python scikit-learn i użyjemy ikonicznego zbioru danych: **Iris dataset**.

```python
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
iris_df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
```
|                                        | długość działki kielicha (cm) | szerokość działki kielicha (cm) | długość płatka (cm) | szerokość płatka (cm) |
|----------------------------------------|-------------------------------|---------------------------------|---------------------|-----------------------|
|0                                       |5.1                            |3.5                              |1.4                  |0.2                    |
|1                                       |4.9                            |3.0                              |1.4                  |0.2                    |
|2                                       |4.7                            |3.2                              |1.3                  |0.2                    |
|3                                       |4.6                            |3.1                              |1.5                  |0.2                    |
|4                                       |5.0                            |3.6                              |1.4                  |0.2                    |

- **DataFrame.info**: Na początek metoda `info()` służy do wyświetlania podsumowania zawartości obecnej w `DataFrame`. Przyjrzyjmy się temu zbiorowi danych:
```python
iris_df.info()
```
```
RangeIndex: 150 entries, 0 to 149
Data columns (total 4 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   sepal length (cm)  150 non-null    float64
 1   sepal width (cm)   150 non-null    float64
 2   petal length (cm)  150 non-null    float64
 3   petal width (cm)   150 non-null    float64
dtypes: float64(4)
memory usage: 4.8 KB
```
Z tego wynika, że zbiór danych *Iris* zawiera 150 wpisów w czterech kolumnach, bez brakujących wartości. Wszystkie dane są przechowywane jako liczby zmiennoprzecinkowe 64-bitowe.

- **DataFrame.head()**: Następnie, aby sprawdzić rzeczywistą zawartość `DataFrame`, używamy metody `head()`. Zobaczmy, jak wyglądają pierwsze wiersze naszego `iris_df`:
```python
iris_df.head()
```
```
   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
0                5.1               3.5                1.4               0.2
1                4.9               3.0                1.4               0.2
2                4.7               3.2                1.3               0.2
3                4.6               3.1                1.5               0.2
4                5.0               3.6                1.4               0.2
```
- **DataFrame.tail()**: Z kolei, aby sprawdzić ostatnie wiersze `DataFrame`, używamy metody `tail()`:
```python
iris_df.tail()
```
```
     sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
145                6.7               3.0                5.2               2.3
146                6.3               2.5                5.0               1.9
147                6.5               3.0                5.2               2.0
148                6.2               3.4                5.4               2.3
149                5.9               3.0                5.1               1.8
```
> **Wniosek:** Nawet patrząc tylko na metadane o informacjach w DataFrame lub na pierwsze i ostatnie wartości, można szybko uzyskać ogólne pojęcie o rozmiarze, kształcie i zawartości danych, z którymi pracujesz.

## Radzenie sobie z brakującymi danymi
> **Cel nauki:** Po zakończeniu tej sekcji powinieneś wiedzieć, jak zastępować lub usuwać brakujące wartości w DataFrame.

Większość zbiorów danych, z których chcesz (lub musisz) korzystać, zawiera brakujące wartości. Sposób, w jaki radzisz sobie z brakującymi danymi, wiąże się z subtelnymi kompromisami, które mogą wpłynąć na końcową analizę i wyniki w rzeczywistym świecie.

Pandas obsługuje brakujące wartości na dwa sposoby. Pierwszy z nich widziałeś już w poprzednich sekcjach: `NaN`, czyli Not a Number. Jest to specjalna wartość będąca częścią specyfikacji IEEE dla liczb zmiennoprzecinkowych i służy wyłącznie do oznaczania brakujących wartości zmiennoprzecinkowych.

Dla brakujących wartości innych niż liczby zmiennoprzecinkowe pandas używa obiektu `None` z Pythona. Choć może wydawać się to mylące, że spotykasz dwa różne rodzaje wartości oznaczających to samo, istnieją uzasadnione programistyczne powody tego wyboru projektowego. W praktyce takie podejście pozwala pandas na osiągnięcie dobrego kompromisu w większości przypadków. Niemniej jednak zarówno `None`, jak i `NaN` mają ograniczenia, o których należy pamiętać w kontekście ich użycia.

Więcej o `NaN` i `None` znajdziesz w [notatniku](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb)!

- **Wykrywanie brakujących wartości**: W `pandas` metody `isnull()` i `notnull()` są głównymi narzędziami do wykrywania brakujących danych. Obie zwracają maski logiczne dla danych. Wykorzystamy `numpy` dla wartości `NaN`:
```python
import numpy as np

example1 = pd.Series([0, np.nan, '', None])
example1.isnull()
```
```
0    False
1     True
2    False
3     True
dtype: bool
```
Przyjrzyj się uważnie wynikom. Czy coś Cię zaskoczyło? Choć `0` jest arytmetycznym zerem, nadal jest poprawną liczbą całkowitą i pandas traktuje go jako taką. `''` jest nieco bardziej subtelne. Choć używaliśmy go w sekcji 1 do reprezentowania pustego ciągu znaków, nadal jest to obiekt typu string, a nie reprezentacja wartości null według pandas.

Teraz odwróćmy sytuację i użyjmy tych metod w sposób bardziej praktyczny. Możesz używać masek logicznych bezpośrednio jako indeksu ``Series`` lub ``DataFrame``, co jest przydatne przy pracy z izolowanymi brakującymi (lub obecnymi) wartościami.

> **Wniosek:** Zarówno metody `isnull()`, jak i `notnull()` dają podobne wyniki w `DataFrame`: pokazują wyniki i indeksy tych wyników, co będzie niezwykle pomocne podczas pracy z danymi.

- **Usuwanie brakujących wartości**: Oprócz identyfikacji brakujących wartości, pandas oferuje wygodny sposób na usuwanie wartości null z `Series` i `DataFrame`. (Szczególnie w przypadku dużych zbiorów danych często bardziej wskazane jest po prostu usunięcie brakujących wartości [NA] z analizy niż radzenie sobie z nimi w inny sposób). Aby zobaczyć to w praktyce, wróćmy do `example1`:
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
Zauważ, że wynik powinien wyglądać jak Twój wynik z `example3[example3.notnull()]`. Różnica polega na tym, że zamiast indeksować na podstawie zamaskowanych wartości, `dropna` usunęło brakujące wartości z `Series` `example1`.

Ponieważ `DataFrame` ma dwie wymiary, oferuje więcej opcji usuwania danych.

```python
example2 = pd.DataFrame([[1,      np.nan, 7], 
                         [2,      5,      8], 
                         [np.nan, 6,      9]])
example2
```
|      | 0 | 1 | 2 |
|------|---|---|---|
|0     |1.0|NaN|7  |
|1     |2.0|5.0|8  |
|2     |NaN|6.0|9  |

(Zauważyłeś, że pandas przekonwertował dwie kolumny na typ float, aby uwzględnić `NaN`?)

Nie możesz usunąć pojedynczej wartości z `DataFrame`, więc musisz usunąć całe wiersze lub kolumny. W zależności od tego, co robisz, możesz chcieć zrobić jedno lub drugie, dlatego pandas daje opcje dla obu. W nauce o danych kolumny zazwyczaj reprezentują zmienne, a wiersze obserwacje, więc częściej usuwa się wiersze danych; domyślne ustawienie dla `dropna()` to usuwanie wszystkich wierszy zawierających jakiekolwiek wartości null:

```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```
Jeśli to konieczne, możesz usunąć wartości NA z kolumn. Użyj `axis=1`, aby to zrobić:
```python
example2.dropna(axis='columns')
```
```
	2
0	7
1	8
2	9
```
Zauważ, że może to usunąć wiele danych, które chciałbyś zachować, szczególnie w mniejszych zbiorach danych. Co jeśli chcesz usunąć tylko wiersze lub kolumny zawierające kilka lub wszystkie wartości null? Możesz określić te ustawienia w `dropna` za pomocą parametrów `how` i `thresh`.

Domyślnie `how='any'` (jeśli chcesz to sprawdzić lub zobaczyć, jakie inne parametry ma metoda, uruchom `example4.dropna?` w komórce kodu). Możesz alternatywnie określić `how='all'`, aby usunąć tylko wiersze lub kolumny zawierające wszystkie wartości null. Rozszerzmy nasz przykład `DataFrame`, aby zobaczyć to w praktyce.

```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

Parametr `thresh` daje Ci bardziej precyzyjną kontrolę: ustawiasz liczbę *nie-nullowych* wartości, które wiersz lub kolumna musi mieć, aby zostały zachowane:
```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```
Tutaj pierwszy i ostatni wiersz zostały usunięte, ponieważ zawierały tylko dwie wartości nie-nullowe.

- **Uzupełnianie brakujących wartości**: W zależności od Twojego zbioru danych, czasami bardziej sensowne jest uzupełnienie brakujących wartości poprawnymi niż ich usunięcie. Możesz użyć `isnull`, aby to zrobić na miejscu, ale może to być pracochłonne, szczególnie jeśli masz wiele wartości do uzupełnienia. Ponieważ jest to tak częste zadanie w nauce o danych, pandas oferuje metodę `fillna`, która zwraca kopię `Series` lub `DataFrame` z brakującymi wartościami zastąpionymi przez wybrane przez Ciebie. Stwórzmy kolejny przykład `Series`, aby zobaczyć, jak to działa w praktyce.
```python
example3 = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
example3
```
```
a    1.0
b    NaN
c    2.0
d    NaN
e    3.0
dtype: float64
```
Możesz uzupełnić wszystkie brakujące wpisy jedną wartością, na przykład `0`:
```python
example3.fillna(0)
```
```
a    1.0
b    0.0
c    2.0
d    0.0
e    3.0
dtype: float64
```
Możesz **uzupełnić w przód** brakujące wartości, czyli użyć ostatniej poprawnej wartości do uzupełnienia brakującej:
```python
example3.fillna(method='ffill')
```
```
a    1.0
b    1.0
c    2.0
d    2.0
e    3.0
dtype: float64
```
Możesz także **uzupełnić wstecz**, aby propagować następną poprawną wartość wstecz do uzupełnienia brakującej:
```python
example3.fillna(method='bfill')
```
```
a    1.0
b    2.0
c    2.0
d    3.0
e    3.0
dtype: float64
```
Jak możesz się domyślić, działa to tak samo w przypadku `DataFrame`, ale możesz także określić `axis`, wzdłuż którego uzupełniane są brakujące wartości. Biorąc ponownie wcześniej używany `example2`:
```python
example2.fillna(method='ffill', axis=1)
```
```
	0	1	2	3
0	1.0	1.0	7.0	7.0
1	2.0	5.0	8.0	8.0
2	NaN	6.0	9.0	9.0
```
Zauważ, że gdy poprzednia wartość nie jest dostępna do uzupełnienia w przód, wartość null pozostaje.
> **Wniosek:** Istnieje wiele sposobów radzenia sobie z brakującymi wartościami w zbiorach danych. Konkretna strategia, którą wybierzesz (usuwanie ich, zastępowanie lub sposób, w jaki je zastępujesz), powinna być uzależniona od specyfiki tych danych. Im więcej będziesz pracować z danymi i je analizować, tym lepiej zrozumiesz, jak radzić sobie z brakującymi wartościami.
## Usuwanie zduplikowanych danych

> **Cel nauki:** Po zakończeniu tej części powinieneś swobodnie identyfikować i usuwać zduplikowane wartości z DataFrames.

Oprócz brakujących danych, w rzeczywistych zestawach danych często napotkasz zduplikowane dane. Na szczęście `pandas` oferuje prosty sposób na wykrywanie i usuwanie zduplikowanych wpisów.

- **Identyfikowanie duplikatów: `duplicated`**: Możesz łatwo zauważyć zduplikowane wartości za pomocą metody `duplicated` w pandas, która zwraca maskę logiczną wskazującą, czy wpis w `DataFrame` jest duplikatem wcześniejszego. Stwórzmy kolejny przykład `DataFrame`, aby zobaczyć to w praktyce.
```python
example4 = pd.DataFrame({'letters': ['A','B'] * 2 + ['B'],
                         'numbers': [1, 2, 1, 3, 3]})
example4
```
|      |litery |liczby |
|------|-------|-------|
|0     |A      |1      |
|1     |B      |2      |
|2     |A      |1      |
|3     |B      |3      |
|4     |B      |3      |

```python
example4.duplicated()
```
```
0    False
1    False
2     True
3    False
4     True
dtype: bool
```
- **Usuwanie duplikatów: `drop_duplicates`:** po prostu zwraca kopię danych, w których wszystkie wartości oznaczone jako `duplicated` są `False`:
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
Zarówno `duplicated`, jak i `drop_duplicates` domyślnie uwzględniają wszystkie kolumny, ale możesz określić, że mają analizować tylko podzbiór kolumn w Twoim `DataFrame`:
```python
example4.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **Wnioski:** Usuwanie zduplikowanych danych jest kluczowym elementem niemal każdego projektu związanego z nauką o danych. Zduplikowane dane mogą zmienić wyniki Twoich analiz i prowadzić do nieprawidłowych rezultatów!


## 🚀 Wyzwanie

Wszystkie omówione materiały są dostępne jako [Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb). Dodatkowo, po każdej sekcji znajdują się ćwiczenia – spróbuj je rozwiązać!

## [Quiz po wykładzie](https://ff-quizzes.netlify.app/en/ds/quiz/15)



## Przegląd i samodzielna nauka

Istnieje wiele sposobów na odkrywanie i podejście do przygotowywania danych do analizy i modelowania, a czyszczenie danych to ważny krok, który wymaga praktycznego doświadczenia. Spróbuj tych wyzwań z Kaggle, aby zgłębić techniki, które nie zostały omówione w tej lekcji.

- [Data Cleaning Challenge: Parsing Dates](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [Data Cleaning Challenge: Scale and Normalize Data](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)


## Zadanie

[Ocena danych z formularza](assignment.md)

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby zapewnić poprawność tłumaczenia, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.