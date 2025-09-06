<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "42119bcc97bee88254e381156d770f3c",
  "translation_date": "2025-09-05T14:37:48+00:00",
  "source_file": "3-Data-Visualization/11-visualization-proportions/README.md",
  "language_code": "pl"
}
-->
# Wizualizacja proporcji

|![ Sketchnote autorstwa [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|Wizualizacja proporcji - _Sketchnote autorstwa [@nitya](https://twitter.com/nitya)_ |

W tej lekcji użyjesz innego zestawu danych skoncentrowanego na naturze, aby zwizualizować proporcje, na przykład ile różnych rodzajów grzybów występuje w danym zestawie danych o pieczarkach. Zbadajmy te fascynujące grzyby, korzystając z zestawu danych pochodzącego z Audubon, zawierającego szczegóły dotyczące 23 gatunków grzybów blaszkowych z rodzin Agaricus i Lepiota. Będziesz eksperymentować z apetycznymi wizualizacjami, takimi jak:

- Wykresy kołowe 🥧
- Wykresy pierścieniowe 🍩
- Wykresy gofrowe 🧇

> 💡 Bardzo interesujący projekt [Charticulator](https://charticulator.com) od Microsoft Research oferuje darmowy interfejs typu "przeciągnij i upuść" do wizualizacji danych. W jednym z ich tutoriali również używają tego zestawu danych o grzybach! Możesz więc eksplorować dane i jednocześnie uczyć się biblioteki: [Tutorial Charticulator](https://charticulator.com/tutorials/tutorial4.html).

## [Quiz przed lekcją](https://ff-quizzes.netlify.app/en/ds/quiz/20)

## Poznaj swoje grzyby 🍄

Grzyby są bardzo interesujące. Zaimportujmy zestaw danych, aby je zbadać:

```python
import pandas as pd
import matplotlib.pyplot as plt
mushrooms = pd.read_csv('../../data/mushrooms.csv')
mushrooms.head()
```
Tabela jest wyświetlana z ciekawymi danymi do analizy:


| klasa     | kształt kapelusza | powierzchnia kapelusza | kolor kapelusza | siniaki | zapach   | przyczepność blaszek | odstępy między blaszkami | rozmiar blaszek | kolor blaszek | kształt trzonu | korzeń trzonu | powierzchnia trzonu nad pierścieniem | powierzchnia trzonu pod pierścieniem | kolor trzonu nad pierścieniem | kolor trzonu pod pierścieniem | typ osłony | kolor osłony | liczba pierścieni | typ pierścienia | kolor zarodników | populacja | siedlisko |
| --------- | ----------------- | --------------------- | --------------- | ------- | -------- | -------------------- | ------------------------ | --------------- | ------------- | -------------- | ------------ | ------------------------------- | ------------------------------- | ----------------------------- | ----------------------------- | ---------- | ----------- | ---------------- | --------------- | ---------------- | ---------- | -------- |
| Trujące   | Wypukły           | Gładka                | Brązowy         | Siniaki | Ostry    | Wolne                | Bliskie                  | Wąskie          | Czarny        | Powiększający  | Równy        | Gładka                          | Gładka                          | Biały                        | Biały                        | Częściowa  | Biały       | Jeden             | Wiszący         | Czarny            | Rozproszone | Miejskie |
| Jadalne   | Wypukły           | Gładka                | Żółty           | Siniaki | Migdałowy | Wolne                | Bliskie                  | Szerokie        | Czarny        | Powiększający  | Maczugowaty  | Gładka                          | Gładka                          | Biały                        | Biały                        | Częściowa  | Biały       | Jeden             | Wiszący         | Brązowy           | Liczne     | Trawy    |
| Jadalne   | Dzwonkowaty       | Gładka                | Biały           | Siniaki | Anyżowy  | Wolne                | Bliskie                  | Szerokie        | Brązowy       | Powiększający  | Maczugowaty  | Gładka                          | Gładka                          | Biały                        | Biały                        | Częściowa  | Biały       | Jeden             | Wiszący         | Brązowy           | Liczne     | Łąki     |
| Trujące   | Wypukły           | Łuskowata             | Biały           | Siniaki | Ostry    | Wolne                | Bliskie                  | Wąskie          | Brązowy       | Powiększający  | Równy        | Gładka                          | Gładka                          | Biały                        | Biały                        | Częściowa  | Biały       | Jeden             | Wiszący         | Czarny            | Rozproszone | Miejskie |

Od razu zauważasz, że wszystkie dane są tekstowe. Musisz je przekonwertować, aby móc użyć ich w wykresie. Większość danych jest reprezentowana jako obiekt:

```python
print(mushrooms.select_dtypes(["object"]).columns)
```

Wynik to:

```output
Index(['class', 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
       'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
       'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
       'stalk-surface-below-ring', 'stalk-color-above-ring',
       'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number',
       'ring-type', 'spore-print-color', 'population', 'habitat'],
      dtype='object')
```
Weź te dane i przekonwertuj kolumnę 'klasa' na kategorię:

```python
cols = mushrooms.select_dtypes(["object"]).columns
mushrooms[cols] = mushrooms[cols].astype('category')
```

```python
edibleclass=mushrooms.groupby(['class']).count()
edibleclass
```

Teraz, jeśli wyświetlisz dane o grzybach, zobaczysz, że zostały pogrupowane w kategorie według klasy trujące/jadalne:


|           | kształt kapelusza | powierzchnia kapelusza | kolor kapelusza | siniaki | zapach | przyczepność blaszek | odstępy między blaszkami | rozmiar blaszek | kolor blaszek | kształt trzonu | ... | powierzchnia trzonu pod pierścieniem | kolor trzonu nad pierścieniem | kolor trzonu pod pierścieniem | typ osłony | kolor osłony | liczba pierścieni | typ pierścienia | kolor zarodników | populacja | siedlisko |
| --------- | ----------------- | --------------------- | --------------- | ------- | ------ | -------------------- | ------------------------ | --------------- | ------------- | -------------- | --- | ------------------------------- | ----------------------------- | ----------------------------- | ---------- | ----------- | ---------------- | --------------- | ---------------- | ---------- | -------- |
| klasa     |                   |                       |                 |         |        |                      |                          |                 |               |                |     |                               |                             |                             |            |             |                  |                 |                  |            |         |
| Jadalne   | 4208              | 4208                  | 4208            | 4208    | 4208   | 4208                | 4208                     | 4208            | 4208          | 4208           | ... | 4208                         | 4208                       | 4208                       | 4208       | 4208        | 4208             | 4208            | 4208             | 4208       | 4208    |
| Trujące   | 3916              | 3916                  | 3916            | 3916    | 3916   | 3916                | 3916                     | 3916            | 3916          | 3916           | ... | 3916                         | 3916                       | 3916                       | 3916       | 3916        | 3916             | 3916            | 3916             | 3916       | 3916    |

Jeśli podążysz za kolejnością przedstawioną w tej tabeli, aby stworzyć etykiety kategorii klasy, możesz zbudować wykres kołowy:

## Koło!

```python
labels=['Edible','Poisonous']
plt.pie(edibleclass['population'],labels=labels,autopct='%.1f %%')
plt.title('Edible?')
plt.show()
```
Voila, wykres kołowy pokazujący proporcje tych danych według dwóch klas grzybów. Ważne jest, aby poprawnie ustawić kolejność etykiet, szczególnie tutaj, więc upewnij się, że weryfikujesz kolejność, w jakiej budowana jest tablica etykiet!

![wykres kołowy](../../../../3-Data-Visualization/11-visualization-proportions/images/pie1-wb.png)

## Pierścienie!

Nieco bardziej interesującym wizualnie wykresem kołowym jest wykres pierścieniowy, czyli wykres kołowy z dziurą w środku. Spójrzmy na nasze dane za pomocą tej metody.

Przyjrzyj się różnym siedliskom, w których rosną grzyby:

```python
habitat=mushrooms.groupby(['habitat']).count()
habitat
```
Tutaj grupujesz swoje dane według siedliska. Jest ich 7, więc użyj ich jako etykiet dla wykresu pierścieniowego:

```python
labels=['Grasses','Leaves','Meadows','Paths','Urban','Waste','Wood']

plt.pie(habitat['class'], labels=labels,
        autopct='%1.1f%%', pctdistance=0.85)
  
center_circle = plt.Circle((0, 0), 0.40, fc='white')
fig = plt.gcf()

fig.gca().add_artist(center_circle)
  
plt.title('Mushroom Habitats')
  
plt.show()
```

![wykres pierścieniowy](../../../../3-Data-Visualization/11-visualization-proportions/images/donut-wb.png)

Ten kod rysuje wykres i środkowe koło, a następnie dodaje to środkowe koło do wykresu. Zmień szerokość środkowego koła, zmieniając wartość `0.40` na inną.

Wykresy pierścieniowe można dostosować na różne sposoby, aby zmienić etykiety. Etykiety w szczególności można wyróżnić dla lepszej czytelności. Dowiedz się więcej w [dokumentacji](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html?highlight=donut).

Teraz, gdy wiesz, jak grupować dane i wyświetlać je jako koło lub pierścień, możesz eksplorować inne typy wykresów. Spróbuj wykresu gofrowego, który jest po prostu innym sposobem eksploracji ilości.

## Gofry!

Wykres typu 'gofrowy' to inny sposób wizualizacji ilości jako 2D tablicy kwadratów. Spróbuj zwizualizować różne ilości kolorów kapeluszy grzybów w tym zestawie danych. Aby to zrobić, musisz zainstalować pomocniczą bibliotekę [PyWaffle](https://pypi.org/project/pywaffle/) i użyć Matplotlib:

```python
pip install pywaffle
```

Wybierz segment swoich danych do grupowania:

```python
capcolor=mushrooms.groupby(['cap-color']).count()
capcolor
```

Stwórz wykres gofrowy, tworząc etykiety, a następnie grupując swoje dane:

```python
import pandas as pd
import matplotlib.pyplot as plt
from pywaffle import Waffle
  
data ={'color': ['brown', 'buff', 'cinnamon', 'green', 'pink', 'purple', 'red', 'white', 'yellow'],
    'amount': capcolor['class']
     }
  
df = pd.DataFrame(data)
  
fig = plt.figure(
    FigureClass = Waffle,
    rows = 100,
    values = df.amount,
    labels = list(df.color),
    figsize = (30,30),
    colors=["brown", "tan", "maroon", "green", "pink", "purple", "red", "whitesmoke", "yellow"],
)
```

Korzystając z wykresu gofrowego, możesz wyraźnie zobaczyć proporcje kolorów kapeluszy w tym zestawie danych o grzybach. Co ciekawe, jest wiele grzybów z zielonymi kapeluszami!

![wykres gofrowy](../../../../3-Data-Visualization/11-visualization-proportions/images/waffle.png)

✅ Pywaffle obsługuje ikony w wykresach, które wykorzystują dowolną ikonę dostępną w [Font Awesome](https://fontawesome.com/). Przeprowadź eksperymenty, aby stworzyć jeszcze bardziej interesujący wykres gofrowy, używając ikon zamiast kwadratów.

W tej lekcji nauczyłeś się trzech sposobów wizualizacji proporcji. Najpierw musisz pogrupować swoje dane w kategorie, a następnie zdecydować, który sposób ich wyświetlenia - koło, pierścień czy gofry - jest najlepszy. Wszystkie są apetyczne i dostarczają użytkownikowi natychmiastowego wglądu w zestaw danych.

## 🚀 Wyzwanie

Spróbuj odtworzyć te apetyczne wykresy w [Charticulator](https://charticulator.com).
## [Quiz po lekcji](https://ff-quizzes.netlify.app/en/ds/quiz/21)

## Przegląd i samodzielna nauka

Czasami nie jest oczywiste, kiedy użyć wykresu kołowego, pierścieniowego czy gofrowego. Oto kilka artykułów do przeczytania na ten temat:

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402

Przeprowadź badania, aby znaleźć więcej informacji na temat tej trudnej decyzji.

## Zadanie

[Spróbuj w Excelu](assignment.md)

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby zapewnić poprawność tłumaczenia, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku źródłowym powinien być uznawany za wiarygodne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.