<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3ade580a06b5f04d57cc83a768a8fb77",
  "translation_date": "2025-08-23T23:29:15+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "pl"
}
-->
# Praca z danymi: Przygotowanie danych

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|Przygotowanie danych - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## [Quiz przed wykładem](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/14)

W zależności od źródła, surowe dane mogą zawierać pewne nieścisłości, które utrudniają analizę i modelowanie. Innymi słowy, takie dane można określić jako „brudne” i wymagają oczyszczenia. Ta lekcja koncentruje się na technikach czyszczenia i transformacji danych w celu radzenia sobie z brakującymi, niedokładnymi lub niekompletnymi danymi. Omawiane tematy wykorzystują Python i bibliotekę Pandas, a przykłady są [zaprezentowane w notebooku](../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb) w tym katalogu.

## Znaczenie czyszczenia danych

- **Łatwość użycia i ponownego wykorzystania**: Gdy dane są odpowiednio zorganizowane i znormalizowane, łatwiej je wyszukiwać, używać i udostępniać innym.

- **Spójność**: Praca z danymi często wymaga korzystania z więcej niż jednego zestawu danych, gdzie dane z różnych źródeł muszą być połączone. Zapewnienie wspólnej standaryzacji każdego zestawu danych gwarantuje ich użyteczność po połączeniu w jeden zbiór.

- **Dokładność modeli**: Oczyszczone dane poprawiają dokładność modeli, które na nich bazują.

## Typowe cele i strategie czyszczenia danych

- **Eksploracja zestawu danych**: Eksploracja danych, która jest omawiana w [późniejszej lekcji](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing), pozwala odkryć dane wymagające oczyszczenia. Wizualne obserwowanie wartości w zestawie danych może pomóc w ustaleniu oczekiwań dotyczących jego struktury lub wskazać problemy, które można rozwiązać. Eksploracja może obejmować podstawowe zapytania, wizualizacje i próbkowanie.

- **Formatowanie**: W zależności od źródła, dane mogą być niespójne w sposobie ich prezentacji. Może to powodować problemy w wyszukiwaniu i reprezentacji wartości, gdzie dane są widoczne w zestawie, ale nie są odpowiednio przedstawione w wizualizacjach lub wynikach zapytań. Typowe problemy z formatowaniem obejmują usuwanie białych znaków, daty i typy danych. Rozwiązywanie tych problemów zazwyczaj należy do osób korzystających z danych. Na przykład standardy dotyczące prezentacji dat i liczb mogą różnić się w zależności od kraju.

- **Duplikaty**: Dane zawierające więcej niż jedno wystąpienie mogą prowadzić do niedokładnych wyników i zazwyczaj powinny być usunięte. Jest to częste zjawisko podczas łączenia dwóch lub więcej zestawów danych. Jednak w niektórych przypadkach duplikaty w połączonych zestawach danych mogą zawierać dodatkowe informacje, które warto zachować.

- **Brakujące dane**: Brakujące dane mogą powodować niedokładności oraz słabe lub stronnicze wyniki. Czasami można je rozwiązać poprzez „ponowne załadowanie” danych, uzupełnienie brakujących wartości za pomocą obliczeń i kodu, np. w Pythonie, lub po prostu usunięcie wartości i odpowiadających im danych. Istnieje wiele powodów, dla których dane mogą być brakujące, a działania podejmowane w celu ich rozwiązania zależą od tego, jak i dlaczego zniknęły.

## Eksploracja informacji o DataFrame
> **Cel nauki:** Po zakończeniu tej części powinieneś być w stanie znaleźć ogólne informacje o danych przechowywanych w DataFrame w Pandas.

Po załadowaniu danych do Pandas, najprawdopodobniej będą one w formie DataFrame (odwołaj się do poprzedniej [lekcji](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe) dla szczegółowego przeglądu). Jednak jeśli zestaw danych w Twoim DataFrame ma 60 000 wierszy i 400 kolumn, jak zacząć rozumieć, z czym pracujesz? Na szczęście [Pandas](https://pandas.pydata.org/) oferuje wygodne narzędzia do szybkiego przeglądania ogólnych informacji o DataFrame, a także pierwszych i ostatnich kilku wierszy.

Aby zbadać tę funkcjonalność, zaimportujemy bibliotekę Python scikit-learn i użyjemy ikonicznego zestawu danych: **Iris dataset**.

```python
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
iris_df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
```
|                                        | długość działki (cm) | szerokość działki (cm) | długość płatka (cm) | szerokość płatka (cm) |
|----------------------------------------|-----------------------|------------------------|---------------------|-----------------------|
|0                                       |5.1                   |3.5                    |1.4                 |0.2                   |
|1                                       |4.9                   |3.0                    |1.4                 |0.2                   |
|2                                       |4.7                   |3.2                    |1.3                 |0.2                   |
|3                                       |4.6                   |3.1                    |1.5                 |0.2                   |
|4                                       |5.0                   |3.6                    |1.4                 |0.2                   |

- **DataFrame.info**: Na początek metoda `info()` służy do wyświetlenia podsumowania zawartości obecnej w `DataFrame`. Spójrzmy na ten zestaw danych, aby zobaczyć, co mamy:
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
Z tego dowiadujemy się, że zestaw danych *Iris* ma 150 wpisów w czterech kolumnach bez brakujących wartości. Wszystkie dane są przechowywane jako liczby zmiennoprzecinkowe 64-bitowe.

- **DataFrame.head()**: Następnie, aby sprawdzić rzeczywistą zawartość `DataFrame`, używamy metody `head()`. Zobaczmy, jak wyglądają pierwsze kilka wierszy naszego `iris_df`:
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
- **DataFrame.tail()**: Odwrotnie, aby sprawdzić ostatnie kilka wierszy `DataFrame`, używamy metody `tail()`:
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
> **Wniosek:** Nawet patrząc tylko na metadane o informacji w DataFrame lub na pierwsze i ostatnie kilka wartości, możesz od razu uzyskać wyobrażenie o rozmiarze, kształcie i zawartości danych, z którymi pracujesz.

## Radzenie sobie z brakującymi danymi
> **Cel nauki:** Po zakończeniu tej części powinieneś wiedzieć, jak zastępować lub usuwać brakujące wartości z DataFrame.

Większość zestawów danych, które chcesz (lub musisz) używać, zawiera brakujące wartości. Sposób, w jaki radzisz sobie z brakującymi danymi, niesie ze sobą subtelne kompromisy, które mogą wpłynąć na Twoją końcową analizę i wyniki w rzeczywistym świecie.

Pandas obsługuje brakujące wartości na dwa sposoby. Pierwszy, który widziałeś wcześniej w poprzednich sekcjach: `NaN`, czyli Not a Number. Jest to specjalna wartość będąca częścią specyfikacji IEEE dla liczb zmiennoprzecinkowych i jest używana wyłącznie do wskazywania brakujących wartości zmiennoprzecinkowych.

Dla brakujących wartości innych niż liczby zmiennoprzecinkowe, Pandas używa obiektu Python `None`. Chociaż może się wydawać mylące, że napotkasz dwa różne rodzaje wartości oznaczających zasadniczo to samo, istnieją solidne programistyczne powody dla tego wyboru projektowego, a w praktyce takie podejście umożliwia Pandas dostarczenie dobrego kompromisu w zdecydowanej większości przypadków. Niemniej jednak zarówno `None`, jak i `NaN` mają ograniczenia, o których musisz pamiętać w kontekście ich użycia.

Dowiedz się więcej o `NaN` i `None` z [notebooka](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb)!

- **Wykrywanie brakujących wartości**: W `Pandas` metody `isnull()` i `notnull()` są głównymi narzędziami do wykrywania brakujących danych. Obie zwracają maski logiczne dla Twoich danych. Będziemy używać `numpy` dla wartości `NaN`:
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
Przyjrzyj się uważnie wynikom. Czy coś Cię zaskoczyło? Chociaż `0` jest arytmetycznym zerem, jest to jednak całkowicie poprawna liczba całkowita i Pandas traktuje ją jako taką. `''` jest nieco bardziej subtelne. Chociaż używaliśmy go w Sekcji 1 do reprezentowania pustej wartości tekstowej, jest to jednak obiekt tekstowy, a nie reprezentacja null w rozumieniu Pandas.

Teraz odwróćmy sytuację i użyjmy tych metod w sposób bardziej przypominający praktyczne zastosowanie. Możesz używać masek logicznych bezpośrednio jako indeksu ``Series`` lub ``DataFrame``, co może być przydatne podczas pracy z izolowanymi brakującymi (lub obecnymi) wartościami.

> **Wniosek:** Zarówno metody `isnull()` jak i `notnull()` dają podobne wyniki, gdy używasz ich w `DataFrame`: pokazują wyniki oraz indeks tych wyników, co będzie niezwykle pomocne podczas pracy z danymi.

- **Usuwanie brakujących wartości**: Oprócz identyfikacji brakujących wartości, Pandas oferuje wygodny sposób usuwania wartości null z `Series` i `DataFrame`. (Szczególnie w przypadku dużych zestawów danych, często bardziej wskazane jest po prostu usunięcie brakujących wartości [NA] z analizy niż radzenie sobie z nimi w inny sposób). Aby zobaczyć to w praktyce, wróćmy do `example1`:
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
Zauważ, że powinno to wyglądać jak Twój wynik z `example3[example3.notnull()]`. Różnica polega na tym, że zamiast indeksować na podstawie wartości zamaskowanych, `dropna` usunęło te brakujące wartości z `Series` `example1`.

Ponieważ `DataFrame` ma dwa wymiary, oferuje więcej opcji usuwania danych.

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

(Zauważyłeś, że Pandas zmieniło typ dwóch kolumn na liczby zmiennoprzecinkowe, aby uwzględnić `NaN`?)

Nie możesz usunąć pojedynczej wartości z `DataFrame`, więc musisz usunąć całe wiersze lub kolumny. W zależności od tego, co robisz, możesz chcieć zrobić jedno lub drugie, dlatego Pandas daje Ci opcje dla obu. Ponieważ w nauce o danych kolumny zazwyczaj reprezentują zmienne, a wiersze obserwacje, częściej usuwasz wiersze danych; domyślne ustawienie dla `dropna()` to usuwanie wszystkich wierszy zawierających jakiekolwiek wartości null:

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
Zauważ, że może to usunąć wiele danych, które chciałbyś zachować, szczególnie w mniejszych zestawach danych. Co jeśli chcesz usunąć tylko wiersze lub kolumny zawierające kilka lub nawet wszystkie wartości null? Możesz określić te ustawienia w `dropna` za pomocą parametrów `how` i `thresh`.

Domyślnie `how='any'` (jeśli chcesz sprawdzić samodzielnie lub zobaczyć, jakie inne parametry ma metoda, uruchom `example4.dropna?` w komórce kodu). Możesz alternatywnie określić `how='all'`, aby usunąć tylko wiersze lub kolumny zawierające wszystkie wartości null. Rozszerzmy nasz przykład `DataFrame`, aby zobaczyć to w praktyce.

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
Tutaj pierwszy i ostatni wiersz zostały usunięte, ponieważ zawierają tylko dwie wartości nie-nullowe.

- **Uzupełnianie brakujących wartości**: W zależności od Twojego zestawu danych, czasami bardziej sensowne jest uzupełnienie brakujących wartości niż ich usunięcie. Możesz użyć `isnull`, aby zrobić to na miejscu, ale może to być pracochłonne, szczególnie jeśli masz wiele wartości do uzupełnienia. Ponieważ jest to tak częste zadanie w nauce o danych, Pandas oferuje `fillna`, które zwraca kopię `Series` lub `DataFrame` z brakującymi wartościami zastąpionymi wybraną przez Ciebie wartością. Stwórzmy kolejny przykład `Series`, aby zobaczyć, jak to działa w praktyce.
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
Możesz **uzupełnić w przód** brakujące wartości, czyli użyć ostatniej poprawnej wartości do uzupełnienia null:
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
Możesz również **uzupełnić wstecz**, aby propagować następną poprawną wartość wstecz do uzupełnienia null:
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
Jak możesz się domyślić, działa to tak samo z `DataFrame`, ale możesz również określić `axis`, wzdłuż którego uzupełniasz brakujące wartości. Korzystając ponownie z wcześniej używanego `example2`:
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
> **Wniosek:** Istnieje wiele sposobów radzenia sobie z brakującymi wartościami w zbiorach danych. Konkretna strategia, którą zastosujesz (usuwanie, zastępowanie lub sposób zastępowania), powinna być uzależniona od specyfiki danych. Im więcej będziesz pracować z danymi, tym lepiej zrozumiesz, jak radzić sobie z brakującymi wartościami.

## Usuwanie zduplikowanych danych

> **Cel nauki:** Po zakończeniu tej sekcji powinieneś swobodnie identyfikować i usuwać zduplikowane wartości z DataFrame'ów.

Oprócz brakujących danych, w rzeczywistych zbiorach danych często spotkasz się z danymi zduplikowanymi. Na szczęście `pandas` oferuje prosty sposób wykrywania i usuwania zduplikowanych wpisów.

- **Identyfikowanie duplikatów: `duplicated`**: Możesz łatwo wykryć zduplikowane wartości za pomocą metody `duplicated` w pandas, która zwraca maskę logiczną wskazującą, czy wpis w `DataFrame` jest duplikatem wcześniejszego. Stwórzmy kolejny przykład `DataFrame`, aby zobaczyć to w praktyce.
```python
example4 = pd.DataFrame({'letters': ['A','B'] * 2 + ['B'],
                         'numbers': [1, 2, 1, 3, 3]})
example4
```
|      |letters|numbers|
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
- **Usuwanie duplikatów: `drop_duplicates`:** zwraca po prostu kopię danych, w której wszystkie wartości oznaczone jako `duplicated` są `False`:
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
Zarówno `duplicated`, jak i `drop_duplicates` domyślnie uwzględniają wszystkie kolumny, ale możesz określić, aby analizowały tylko podzbiór kolumn w Twoim `DataFrame`:
```python
example4.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **Wniosek:** Usuwanie zduplikowanych danych to kluczowy element niemal każdego projektu związanego z nauką o danych. Zduplikowane dane mogą zmienić wyniki Twoich analiz i prowadzić do błędnych wniosków!


## 🚀 Wyzwanie

Wszystkie omawiane materiały są dostępne w formie [Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb). Dodatkowo, po każdej sekcji znajdują się ćwiczenia – spróbuj swoich sił!

## [Quiz po wykładzie](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/15)



## Przegląd i samodzielna nauka

Istnieje wiele sposobów odkrywania i przygotowywania danych do analizy i modelowania, a ich czyszczenie to ważny krok, który wymaga praktycznego podejścia. Spróbuj tych wyzwań z Kaggle, aby poznać techniki, które nie zostały omówione w tej lekcji.

- [Wyzwanie czyszczenia danych: Parsowanie dat](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [Wyzwanie czyszczenia danych: Skalowanie i normalizacja danych](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)


## Zadanie

[Ocena danych z formularza](assignment.md)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.