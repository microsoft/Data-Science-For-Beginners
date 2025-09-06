<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "577a611517482c3ceaf76d3d8142cba9",
  "translation_date": "2025-09-05T14:31:40+00:00",
  "source_file": "2-Working-With-Data/07-python/README.md",
  "language_code": "pl"
}
-->
# Praca z danymi: Python i biblioteka Pandas

| ![ Sketchnote autorstwa [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/07-WorkWithPython.png) |
| :-------------------------------------------------------------------------------------------------------------: |
|                 Praca z Pythonem - _Sketchnote autorstwa [@nitya](https://twitter.com/nitya)_                   |

[![Wideo wprowadzające](../../../../2-Working-With-Data/07-python/images/video-ds-python.png)](https://youtu.be/dZjWOGbsN4Y)

Bazy danych oferują bardzo efektywne sposoby przechowywania danych i ich przeszukiwania za pomocą języków zapytań, ale najbardziej elastycznym sposobem przetwarzania danych jest napisanie własnego programu do ich manipulacji. W wielu przypadkach zapytanie do bazy danych byłoby bardziej efektywne. Jednak w sytuacjach, gdy potrzebne jest bardziej złożone przetwarzanie danych, SQL może nie być wystarczający. 
Przetwarzanie danych można zaprogramować w dowolnym języku programowania, ale istnieją języki, które są bardziej zaawansowane w pracy z danymi. Specjaliści od danych zazwyczaj preferują jeden z następujących języków:

* **[Python](https://www.python.org/)**, uniwersalny język programowania, który często jest uważany za jeden z najlepszych wyborów dla początkujących ze względu na swoją prostotę. Python posiada wiele dodatkowych bibliotek, które mogą pomóc w rozwiązywaniu praktycznych problemów, takich jak wyodrębnianie danych z archiwum ZIP czy konwersja obrazu na odcienie szarości. Oprócz analizy danych, Python jest również często używany w tworzeniu aplikacji webowych. 
* **[R](https://www.r-project.org/)** to tradycyjne narzędzie stworzone z myślą o statystycznym przetwarzaniu danych. Zawiera również dużą bazę bibliotek (CRAN), co czyni go dobrym wyborem do analizy danych. Jednak R nie jest językiem uniwersalnym i rzadko jest używany poza obszarem analizy danych.
* **[Julia](https://julialang.org/)** to kolejny język stworzony specjalnie do analizy danych. Został zaprojektowany z myślą o lepszej wydajności niż Python, co czyni go świetnym narzędziem do eksperymentów naukowych.

W tej lekcji skupimy się na używaniu Pythona do prostego przetwarzania danych. Zakładamy podstawową znajomość tego języka. Jeśli chcesz zgłębić Pythona, możesz skorzystać z jednego z poniższych zasobów:

* [Nauka Pythona w zabawny sposób z grafiką Turtle i fraktalami](https://github.com/shwars/pycourse) - szybki kurs wprowadzający do programowania w Pythonie na GitHubie
* [Pierwsze kroki z Pythonem](https://docs.microsoft.com/en-us/learn/paths/python-first-steps/?WT.mc_id=academic-77958-bethanycheum) Ścieżka nauki na [Microsoft Learn](http://learn.microsoft.com/?WT.mc_id=academic-77958-bethanycheum)

Dane mogą występować w różnych formach. W tej lekcji rozważymy trzy formy danych - **dane tabelaryczne**, **tekst** i **obrazy**.

Skupimy się na kilku przykładach przetwarzania danych, zamiast przedstawiać pełny przegląd wszystkich powiązanych bibliotek. Dzięki temu zrozumiesz główne możliwości i będziesz wiedzieć, gdzie szukać rozwiązań swoich problemów, gdy zajdzie taka potrzeba.

> **Najbardziej przydatna rada**. Gdy musisz wykonać określoną operację na danych, a nie wiesz, jak to zrobić, spróbuj poszukać jej w internecie. [Stackoverflow](https://stackoverflow.com/) często zawiera wiele przydatnych przykładów kodu w Pythonie dla typowych zadań. 

## [Quiz przed lekcją](https://ff-quizzes.netlify.app/en/ds/quiz/12)

## Dane tabelaryczne i DataFrame'y

Spotkałeś się już z danymi tabelarycznymi, gdy omawialiśmy relacyjne bazy danych. Gdy masz dużo danych, które są przechowywane w wielu powiązanych tabelach, zdecydowanie warto używać SQL do pracy z nimi. Jednak istnieje wiele przypadków, gdy mamy jedną tabelę danych i chcemy uzyskać pewne **zrozumienie** lub **wnioski** na temat tych danych, takie jak rozkład wartości, korelacje między nimi itd. W analizie danych często musimy przeprowadzić pewne transformacje danych, a następnie ich wizualizację. Oba te kroki można łatwo wykonać za pomocą Pythona.

Istnieją dwie najbardziej przydatne biblioteki w Pythonie, które mogą pomóc w pracy z danymi tabelarycznymi:
* **[Pandas](https://pandas.pydata.org/)** pozwala manipulować tak zwanymi **DataFrame'ami**, które są analogiczne do tabel relacyjnych. Możesz mieć nazwane kolumny i wykonywać różne operacje na wierszach, kolumnach i całych DataFrame'ach. 
* **[Numpy](https://numpy.org/)** to biblioteka do pracy z **tensorami**, czyli wielowymiarowymi **tablicami**. Tablica zawiera wartości tego samego typu, jest prostsza niż DataFrame, ale oferuje więcej operacji matematycznych i generuje mniejsze obciążenie.

Istnieje również kilka innych bibliotek, które warto znać:
* **[Matplotlib](https://matplotlib.org/)** to biblioteka używana do wizualizacji danych i tworzenia wykresów
* **[SciPy](https://www.scipy.org/)** to biblioteka z dodatkowymi funkcjami naukowymi. Już wcześniej spotkaliśmy się z tą biblioteką, omawiając prawdopodobieństwo i statystykę

Oto fragment kodu, który zazwyczaj używa się do importowania tych bibliotek na początku programu w Pythonie:
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import ... # you need to specify exact sub-packages that you need
``` 

Pandas opiera się na kilku podstawowych koncepcjach.

### Series 

**Series** to sekwencja wartości, podobna do listy lub tablicy numpy. Główna różnica polega na tym, że Series ma również **indeks**, który jest uwzględniany podczas operacji na Series (np. dodawania). Indeks może być tak prosty jak liczba całkowita reprezentująca numer wiersza (jest to domyślny indeks podczas tworzenia Series z listy lub tablicy), lub może mieć bardziej złożoną strukturę, taką jak przedział dat.

> **Uwaga**: W towarzyszącym notebooku [`notebook.ipynb`](../../../../2-Working-With-Data/07-python/notebook.ipynb) znajduje się wprowadzenie do kodu Pandas. Tutaj przedstawiamy tylko niektóre przykłady, ale zachęcamy do zapoznania się z pełnym notebookiem.

Rozważmy przykład: chcemy przeanalizować sprzedaż w naszym punkcie z lodami. Wygenerujmy serię liczb sprzedaży (liczba sprzedanych produktów każdego dnia) dla pewnego okresu czasu:

```python
start_date = "Jan 1, 2020"
end_date = "Mar 31, 2020"
idx = pd.date_range(start_date,end_date)
print(f"Length of index is {len(idx)}")
items_sold = pd.Series(np.random.randint(25,50,size=len(idx)),index=idx)
items_sold.plot()
```
![Wykres szeregów czasowych](../../../../2-Working-With-Data/07-python/images/timeseries-1.png)

Załóżmy teraz, że co tydzień organizujemy imprezę dla znajomych i zabieramy dodatkowe 10 opakowań lodów na imprezę. Możemy stworzyć kolejną serię, indeksowaną tygodniami, aby to pokazać:
```python
additional_items = pd.Series(10,index=pd.date_range(start_date,end_date,freq="W"))
```
Gdy dodamy dwie serie, otrzymamy całkowitą liczbę:
```python
total_items = items_sold.add(additional_items,fill_value=0)
total_items.plot()
```
![Wykres szeregów czasowych](../../../../2-Working-With-Data/07-python/images/timeseries-2.png)

> **Uwaga**: Nie używamy prostego zapisu `total_items+additional_items`. Gdybyśmy to zrobili, otrzymalibyśmy wiele wartości `NaN` (*Not a Number*) w wynikowej serii. Dzieje się tak, ponieważ brakuje wartości dla niektórych punktów indeksu w serii `additional_items`, a dodanie `NaN` do czegokolwiek skutkuje `NaN`. Dlatego musimy określić parametr `fill_value` podczas dodawania.

W przypadku szeregów czasowych możemy również **próbkować** serię z różnymi przedziałami czasowymi. Na przykład, jeśli chcemy obliczyć średnią wielkość sprzedaży miesięcznie, możemy użyć następującego kodu:
```python
monthly = total_items.resample("1M").mean()
ax = monthly.plot(kind='bar')
```
![Miesięczne średnie szeregów czasowych](../../../../2-Working-With-Data/07-python/images/timeseries-3.png)

### DataFrame

DataFrame to w zasadzie zbiór serii z tym samym indeksem. Możemy połączyć kilka serii w jeden DataFrame:
```python
a = pd.Series(range(1,10))
b = pd.Series(["I","like","to","play","games","and","will","not","change"],index=range(0,9))
df = pd.DataFrame([a,b])
```
To stworzy poziomą tabelę, taką jak ta:
|     | 0   | 1    | 2   | 3   | 4      | 5   | 6      | 7    | 8    |
| --- | --- | ---- | --- | --- | ------ | --- | ------ | ---- | ---- |
| 0   | 1   | 2    | 3   | 4   | 5      | 6   | 7      | 8    | 9    |
| 1   | I   | like | to  | use | Python | and | Pandas | very | much |

Możemy również użyć serii jako kolumn i określić nazwy kolumn za pomocą słownika:
```python
df = pd.DataFrame({ 'A' : a, 'B' : b })
```
To da nam tabelę taką jak ta:

|     | A   | B      |
| --- | --- | ------ |
| 0   | 1   | I      |
| 1   | 2   | like   |
| 2   | 3   | to     |
| 3   | 4   | use    |
| 4   | 5   | Python |
| 5   | 6   | and    |
| 6   | 7   | Pandas |
| 7   | 8   | very   |
| 8   | 9   | much   |

**Uwaga**: Możemy również uzyskać ten układ tabeli, transponując poprzednią tabelę, np. pisząc 
```python
df = pd.DataFrame([a,b]).T..rename(columns={ 0 : 'A', 1 : 'B' })
```
Tutaj `.T` oznacza operację transponowania DataFrame, czyli zamianę wierszy i kolumn, a operacja `rename` pozwala nam zmienić nazwy kolumn, aby pasowały do poprzedniego przykładu.

Oto kilka najważniejszych operacji, które możemy wykonać na DataFrame'ach:

**Wybór kolumn**. Możemy wybrać pojedyncze kolumny, pisząc `df['A']` - ta operacja zwraca serię. Możemy również wybrać podzbiór kolumn do innego DataFrame, pisząc `df[['B','A']]` - to zwraca nowy DataFrame.

**Filtrowanie** tylko określonych wierszy według kryteriów. Na przykład, aby pozostawić tylko wiersze, w których kolumna `A` jest większa niż 5, możemy napisać `df[df['A']>5]`.

> **Uwaga**: Sposób działania filtrowania jest następujący. Wyrażenie `df['A']<5` zwraca serię logiczną, która wskazuje, czy wyrażenie jest `True` czy `False` dla każdego elementu oryginalnej serii `df['A']`. Gdy seria logiczna jest używana jako indeks, zwraca podzbiór wierszy w DataFrame. Dlatego nie można używać dowolnych wyrażeń logicznych w Pythonie, na przykład pisanie `df[df['A']>5 and df['A']<7]` byłoby błędne. Zamiast tego należy użyć specjalnej operacji `&` na seriach logicznych, pisząc `df[(df['A']>5) & (df['A']<7)]` (*nawiasy są tutaj ważne*).

**Tworzenie nowych obliczalnych kolumn**. Możemy łatwo tworzyć nowe obliczalne kolumny dla naszego DataFrame, używając intuicyjnych wyrażeń, takich jak:
```python
df['DivA'] = df['A']-df['A'].mean() 
``` 
Ten przykład oblicza odchylenie A od jego wartości średniej. Co właściwie się tutaj dzieje, to obliczamy serię, a następnie przypisujemy tę serię do lewej strony, tworząc nową kolumnę. Dlatego nie możemy używać operacji, które nie są kompatybilne z seriami, na przykład poniższy kod jest błędny:
```python
# Wrong code -> df['ADescr'] = "Low" if df['A'] < 5 else "Hi"
df['LenB'] = len(df['B']) # <- Wrong result
``` 
Ostatni przykład, choć składniowo poprawny, daje błędny wynik, ponieważ przypisuje długość serii `B` do wszystkich wartości w kolumnie, a nie długość poszczególnych elementów, jak zamierzaliśmy.

Jeśli musimy obliczyć złożone wyrażenia, możemy użyć funkcji `apply`. Ostatni przykład można napisać w następujący sposób:
```python
df['LenB'] = df['B'].apply(lambda x : len(x))
# or 
df['LenB'] = df['B'].apply(len)
```

Po powyższych operacjach otrzymamy następujący DataFrame:

|     | A   | B      | DivA | LenB |
| --- | --- | ------ | ---- | ---- |
| 0   | 1   | I      | -4.0 | 1    |
| 1   | 2   | like   | -3.0 | 4    |
| 2   | 3   | to     | -2.0 | 2    |
| 3   | 4   | use    | -1.0 | 3    |
| 4   | 5   | Python | 0.0  | 6    |
| 5   | 6   | and    | 1.0  | 3    |
| 6   | 7   | Pandas | 2.0  | 6    |
| 7   | 8   | very   | 3.0  | 4    |
| 8   | 9   | much   | 4.0  | 4    |

**Wybór wierszy na podstawie numerów** można wykonać za pomocą konstrukcji `iloc`. Na przykład, aby wybrać pierwsze 5 wierszy z DataFrame:
```python
df.iloc[:5]
```

**Grupowanie** jest często używane do uzyskania wyników podobnych do *tabel przestawnych* w Excelu. Załóżmy, że chcemy obliczyć średnią wartość kolumny `A` dla każdej liczby `LenB`. Możemy wtedy pogrupować nasz DataFrame według `LenB` i wywołać `mean`:
```python
df.groupby(by='LenB').mean()
```
Jeśli potrzebujemy obliczyć średnią i liczbę elementów w grupie, możemy użyć bardziej złożonej funkcji `aggregate`:
```python
df.groupby(by='LenB') \
 .aggregate({ 'DivA' : len, 'A' : lambda x: x.mean() }) \
 .rename(columns={ 'DivA' : 'Count', 'A' : 'Mean'})
```
To daje nam następującą tabelę:

| LenB | Count | Mean     |
| ---- | ----- | -------- |
| 1    | 1     | 1.000000 |
| 2    | 1     | 3.000000 |
| 3    | 2     | 5.000000 |
| 4    | 3     | 6.333333 |
| 6    | 2     | 6.000000 |

### Pobieranie danych
Widzieliśmy, jak łatwo można tworzyć Series i DataFrames z obiektów Pythona. Jednak dane zazwyczaj występują w formie pliku tekstowego lub tabeli Excel. Na szczęście Pandas oferuje prosty sposób na załadowanie danych z dysku. Na przykład, odczytanie pliku CSV jest tak proste jak to:
```python
df = pd.read_csv('file.csv')
```
Zobaczymy więcej przykładów ładowania danych, w tym pobieranie ich z zewnętrznych stron internetowych, w sekcji "Wyzwanie".

### Drukowanie i Wizualizacja

Data Scientist często musi eksplorować dane, dlatego ważne jest, aby móc je wizualizować. Gdy DataFrame jest duży, często chcemy tylko upewnić się, że wszystko robimy poprawnie, drukując pierwsze kilka wierszy. Można to zrobić, wywołując `df.head()`. Jeśli uruchamiasz to z Jupyter Notebook, DataFrame zostanie wydrukowany w ładnej formie tabelarycznej.

Widzieliśmy również użycie funkcji `plot` do wizualizacji niektórych kolumn. Chociaż `plot` jest bardzo przydatny do wielu zadań i obsługuje różne typy wykresów za pomocą parametru `kind=`, zawsze można użyć surowej biblioteki `matplotlib`, aby stworzyć coś bardziej złożonego. Szczegółowo omówimy wizualizację danych w osobnych lekcjach kursu.

Ten przegląd obejmuje najważniejsze koncepcje Pandas, jednak biblioteka jest bardzo bogata i nie ma ograniczeń co do tego, co można z nią zrobić! Teraz zastosujmy tę wiedzę do rozwiązania konkretnego problemu.

## 🚀 Wyzwanie 1: Analiza Rozprzestrzeniania się COVID

Pierwszym problemem, na którym się skupimy, jest modelowanie rozprzestrzeniania się epidemii COVID-19. Aby to zrobić, skorzystamy z danych dotyczących liczby zakażonych osób w różnych krajach, dostarczonych przez [Center for Systems Science and Engineering](https://systems.jhu.edu/) (CSSE) na [Johns Hopkins University](https://jhu.edu/). Zestaw danych jest dostępny w [tym repozytorium GitHub](https://github.com/CSSEGISandData/COVID-19).

Ponieważ chcemy pokazać, jak radzić sobie z danymi, zachęcamy do otwarcia [`notebook-covidspread.ipynb`](../../../../2-Working-With-Data/07-python/notebook-covidspread.ipynb) i przeczytania go od początku do końca. Możesz również uruchomić komórki i wykonać wyzwania, które zostawiliśmy dla Ciebie na końcu.

![COVID Spread](../../../../2-Working-With-Data/07-python/images/covidspread.png)

> Jeśli nie wiesz, jak uruchomić kod w Jupyter Notebook, zapoznaj się z [tym artykułem](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## Praca z Niestrukturalnymi Danymi

Chociaż dane bardzo często występują w formie tabelarycznej, w niektórych przypadkach musimy radzić sobie z mniej ustrukturalnymi danymi, na przykład tekstem lub obrazami. W takim przypadku, aby zastosować techniki przetwarzania danych, które widzieliśmy wcześniej, musimy w jakiś sposób **wyodrębnić** dane ustrukturalne. Oto kilka przykładów:

* Wyodrębnianie słów kluczowych z tekstu i sprawdzanie, jak często te słowa kluczowe się pojawiają
* Używanie sieci neuronowych do wyodrębniania informacji o obiektach na zdjęciu
* Uzyskiwanie informacji o emocjach ludzi z obrazu z kamery wideo

## 🚀 Wyzwanie 2: Analiza Publikacji o COVID

W tym wyzwaniu kontynuujemy temat pandemii COVID i skupiamy się na przetwarzaniu publikacji naukowych na ten temat. Istnieje [zestaw danych CORD-19](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) zawierający ponad 7000 (w momencie pisania) publikacji na temat COVID, dostępny wraz z metadanymi i abstraktami (a dla około połowy z nich dostępny jest również pełny tekst).

Pełny przykład analizy tego zestawu danych za pomocą usługi [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health/?WT.mc_id=academic-77958-bethanycheum) opisano [w tym wpisie na blogu](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/). Omówimy uproszczoną wersję tej analizy.

> **NOTE**: Nie dostarczamy kopii zestawu danych jako części tego repozytorium. Możesz najpierw pobrać plik [`metadata.csv`](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge?select=metadata.csv) z [tego zestawu danych na Kaggle](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge). Może być wymagana rejestracja w Kaggle. Możesz również pobrać zestaw danych bez rejestracji [stąd](https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/historical_releases.html), ale będzie on zawierał wszystkie pełne teksty oprócz pliku metadanych.

Otwórz [`notebook-papers.ipynb`](../../../../2-Working-With-Data/07-python/notebook-papers.ipynb) i przeczytaj go od początku do końca. Możesz również uruchomić komórki i wykonać wyzwania, które zostawiliśmy dla Ciebie na końcu.

![Covid Medical Treatment](../../../../2-Working-With-Data/07-python/images/covidtreat.png)

## Przetwarzanie Danych Obrazowych

Ostatnio opracowano bardzo potężne modele AI, które pozwalają na rozumienie obrazów. Istnieje wiele zadań, które można rozwiązać za pomocą wstępnie wytrenowanych sieci neuronowych lub usług w chmurze. Niektóre przykłady obejmują:

* **Klasyfikacja Obrazów**, która może pomóc w kategoryzacji obrazu do jednej z predefiniowanych klas. Możesz łatwo wytrenować własne klasyfikatory obrazów, korzystając z usług takich jak [Custom Vision](https://azure.microsoft.com/services/cognitive-services/custom-vision-service/?WT.mc_id=academic-77958-bethanycheum)
* **Detekcja Obiektów**, aby wykrywać różne obiekty na obrazie. Usługi takie jak [computer vision](https://azure.microsoft.com/services/cognitive-services/computer-vision/?WT.mc_id=academic-77958-bethanycheum) mogą wykrywać wiele typowych obiektów, a Ty możesz wytrenować model [Custom Vision](https://azure.microsoft.com/services/cognitive-services/custom-vision-service/?WT.mc_id=academic-77958-bethanycheum), aby wykrywać konkretne obiekty, które Cię interesują.
* **Detekcja Twarzy**, w tym wykrywanie wieku, płci i emocji. Można to zrobić za pomocą [Face API](https://azure.microsoft.com/services/cognitive-services/face/?WT.mc_id=academic-77958-bethanycheum).

Wszystkie te usługi w chmurze można wywoływać za pomocą [Python SDKs](https://docs.microsoft.com/samples/azure-samples/cognitive-services-python-sdk-samples/cognitive-services-python-sdk-samples/?WT.mc_id=academic-77958-bethanycheum), dzięki czemu można je łatwo włączyć do swojego workflow eksploracji danych.

Oto kilka przykładów eksploracji danych z obrazów:
* W wpisie na blogu [Jak uczyć się Data Science bez kodowania](https://soshnikov.com/azure/how-to-learn-data-science-without-coding/) eksplorujemy zdjęcia z Instagrama, próbując zrozumieć, co sprawia, że ludzie dają więcej polubień zdjęciu. Najpierw wyodrębniamy jak najwięcej informacji ze zdjęć, korzystając z [computer vision](https://azure.microsoft.com/services/cognitive-services/computer-vision/?WT.mc_id=academic-77958-bethanycheum), a następnie używamy [Azure Machine Learning AutoML](https://docs.microsoft.com/azure/machine-learning/concept-automated-ml/?WT.mc_id=academic-77958-bethanycheum), aby zbudować interpretowalny model.
* W [Warsztacie Badań Twarzy](https://github.com/CloudAdvocacy/FaceStudies) używamy [Face API](https://azure.microsoft.com/services/cognitive-services/face/?WT.mc_id=academic-77958-bethanycheum), aby wyodrębnić emocje ludzi na zdjęciach z wydarzeń, próbując zrozumieć, co sprawia, że ludzie są szczęśliwi.

## Podsumowanie

Niezależnie od tego, czy masz już dane ustrukturalne, czy niestrukturalne, za pomocą Pythona możesz wykonać wszystkie kroki związane z przetwarzaniem i rozumieniem danych. Jest to prawdopodobnie najbardziej elastyczny sposób przetwarzania danych, i dlatego większość data scientistów używa Pythona jako swojego głównego narzędzia. Nauka Pythona w głębi jest prawdopodobnie dobrym pomysłem, jeśli poważnie myślisz o swojej drodze w data science!

## [Quiz po wykładzie](https://ff-quizzes.netlify.app/en/ds/quiz/13)

## Przegląd i Samodzielna Nauka

**Książki**
* [Wes McKinney. Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython](https://www.amazon.com/gp/product/1491957662)

**Zasoby Online**
* Oficjalny [10 minutowy przewodnik po Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html)
* [Dokumentacja dotycząca wizualizacji w Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html)

**Nauka Pythona**
* [Naucz się Pythona w zabawny sposób z grafiką Turtle i fraktalami](https://github.com/shwars/pycourse)
* [Zrób swoje pierwsze kroki z Pythonem](https://docs.microsoft.com/learn/paths/python-first-steps/?WT.mc_id=academic-77958-bethanycheum) Ścieżka nauki na [Microsoft Learn](http://learn.microsoft.com/?WT.mc_id=academic-77958-bethanycheum)

## Zadanie

[Wykonaj bardziej szczegółowe badanie danych dla powyższych wyzwań](assignment.md)

## Podziękowania

Ta lekcja została napisana z ♥️ przez [Dmitry Soshnikov](http://soshnikov.com)

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby zapewnić poprawność tłumaczenia, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.