<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a20467e046d312809d008395051fc7",
  "translation_date": "2025-09-05T14:40:51+00:00",
  "source_file": "3-Data-Visualization/10-visualization-distributions/README.md",
  "language_code": "pl"
}
-->
# Wizualizacja rozkładów

|![ Sketchnote autorstwa [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| Wizualizacja rozkładów - _Sketchnote autorstwa [@nitya](https://twitter.com/nitya)_ |

W poprzedniej lekcji dowiedziałeś się kilku interesujących faktów o zbiorze danych dotyczącym ptaków z Minnesoty. Znalazłeś błędne dane, wizualizując wartości odstające, oraz przyjrzałeś się różnicom między kategoriami ptaków na podstawie ich maksymalnej długości.

## [Quiz przed lekcją](https://ff-quizzes.netlify.app/en/ds/quiz/18)
## Eksploracja zbioru danych o ptakach

Innym sposobem na zgłębianie danych jest analiza ich rozkładu, czyli tego, jak dane są zorganizowane wzdłuż osi. Na przykład, możesz chcieć dowiedzieć się o ogólnym rozkładzie maksymalnej rozpiętości skrzydeł lub maksymalnej masy ciała ptaków z Minnesoty w tym zbiorze danych.

Odkryjmy kilka faktów dotyczących rozkładów danych w tym zbiorze. W pliku _notebook.ipynb_ znajdującym się w głównym folderze tej lekcji zaimportuj Pandas, Matplotlib oraz swoje dane:

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```

|      | Nazwa                        | NazwaNaukowa           | Kategoria             | Rząd         | Rodzina  | Rodzaj      | StatusOchrony       | MinDługość | MaxDługość | MinMasaCiała | MaxMasaCiała | MinRozpiętość | MaxRozpiętość |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Czarnobrzuchy gwizdacz       | Dendrocygna autumnalis | Kaczki/Gęsi/Wodne ptaki | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Płowy gwizdacz               | Dendrocygna bicolor    | Kaczki/Gęsi/Wodne ptaki | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Gęś śnieżna                  | Anser caerulescens     | Kaczki/Gęsi/Wodne ptaki | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Gęś Ross'a                   | Anser rossii           | Kaczki/Gęsi/Wodne ptaki | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Gęś białoczelna              | Anser albifrons        | Kaczki/Gęsi/Wodne ptaki | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

Ogólnie rzecz biorąc, możesz szybko przyjrzeć się rozkładowi danych, używając wykresu punktowego, jak zrobiliśmy to w poprzedniej lekcji:

```python
birds.plot(kind='scatter',x='MaxLength',y='Order',figsize=(12,8))

plt.title('Max Length per Order')
plt.ylabel('Order')
plt.xlabel('Max Length')

plt.show()
```
![maksymalna długość według rzędu](../../../../3-Data-Visualization/10-visualization-distributions/images/scatter-wb.png)

To daje ogólny obraz rozkładu długości ciała według rzędu ptaków, ale nie jest to optymalny sposób na przedstawienie prawdziwych rozkładów. Do tego celu zazwyczaj używa się histogramu.

## Praca z histogramami

Matplotlib oferuje bardzo dobre sposoby wizualizacji rozkładów danych za pomocą histogramów. Ten typ wykresu przypomina wykres słupkowy, gdzie rozkład można zobaczyć poprzez wzrost i spadek słupków. Aby stworzyć histogram, potrzebujesz danych liczbowych. Aby stworzyć histogram, możesz zdefiniować typ wykresu jako 'hist' dla histogramu. Ten wykres pokazuje rozkład MaxBodyMass dla całego zakresu danych liczbowych w zbiorze. Dzieląc tablicę danych na mniejsze przedziały, można zobaczyć rozkład wartości danych:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 10, figsize = (12,12))
plt.show()
```
![rozkład dla całego zbioru danych](../../../../3-Data-Visualization/10-visualization-distributions/images/dist1-wb.png)

Jak widać, większość z ponad 400 ptaków w tym zbiorze danych mieści się w zakresie poniżej 2000 dla ich maksymalnej masy ciała. Uzyskaj więcej informacji o danych, zmieniając parametr `bins` na wyższą wartość, na przykład 30:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 30, figsize = (12,12))
plt.show()
```
![rozkład dla całego zbioru danych z większym parametrem bins](../../../../3-Data-Visualization/10-visualization-distributions/images/dist2-wb.png)

Ten wykres pokazuje rozkład w nieco bardziej szczegółowy sposób. Wykres mniej przesunięty w lewo można stworzyć, wybierając tylko dane w określonym zakresie:

Przefiltruj swoje dane, aby uzyskać tylko te ptaki, których masa ciała wynosi poniżej 60, i pokaż 40 `bins`:

```python
filteredBirds = birds[(birds['MaxBodyMass'] > 1) & (birds['MaxBodyMass'] < 60)]      
filteredBirds['MaxBodyMass'].plot(kind = 'hist',bins = 40,figsize = (12,12))
plt.show()     
```
![przefiltrowany histogram](../../../../3-Data-Visualization/10-visualization-distributions/images/dist3-wb.png)

✅ Wypróbuj inne filtry i punkty danych. Aby zobaczyć pełny rozkład danych, usuń filtr `['MaxBodyMass']`, aby pokazać oznaczone rozkłady.

Histogram oferuje również ciekawe ulepszenia kolorystyczne i etykietowe, które warto wypróbować:

Stwórz histogram 2D, aby porównać relację między dwoma rozkładami. Porównajmy `MaxBodyMass` z `MaxLength`. Matplotlib oferuje wbudowany sposób pokazania zbieżności za pomocą jaśniejszych kolorów:

```python
x = filteredBirds['MaxBodyMass']
y = filteredBirds['MaxLength']

fig, ax = plt.subplots(tight_layout=True)
hist = ax.hist2d(x, y)
```
Wydaje się, że istnieje oczekiwana korelacja między tymi dwoma elementami wzdłuż przewidywanej osi, z jednym szczególnie silnym punktem zbieżności:

![wykres 2D](../../../../3-Data-Visualization/10-visualization-distributions/images/2D-wb.png)

Histogramy dobrze sprawdzają się domyślnie dla danych liczbowych. Co jeśli chcesz zobaczyć rozkłady według danych tekstowych? 
## Eksploracja zbioru danych pod kątem rozkładów według danych tekstowych 

Ten zbiór danych zawiera również dobre informacje o kategorii ptaków, ich rodzaju, gatunku, rodzinie oraz statusie ochrony. Przyjrzyjmy się bliżej informacjom o statusie ochrony. Jaki jest rozkład ptaków według ich statusu ochrony?

> ✅ W zbiorze danych używane są różne skróty do opisania statusu ochrony. Skróty te pochodzą z [IUCN Red List Categories](https://www.iucnredlist.org/), organizacji katalogującej status gatunków.
> 
> - CR: Krytycznie zagrożony
> - EN: Zagrożony
> - EX: Wymarły
> - LC: Najmniejszej troski
> - NT: Bliski zagrożenia
> - VU: Narażony

Są to wartości tekstowe, więc będziesz musiał dokonać transformacji, aby stworzyć histogram. Korzystając z dataframe filteredBirds, wyświetl jego status ochrony obok minimalnej rozpiętości skrzydeł. Co widzisz?

```python
x1 = filteredBirds.loc[filteredBirds.ConservationStatus=='EX', 'MinWingspan']
x2 = filteredBirds.loc[filteredBirds.ConservationStatus=='CR', 'MinWingspan']
x3 = filteredBirds.loc[filteredBirds.ConservationStatus=='EN', 'MinWingspan']
x4 = filteredBirds.loc[filteredBirds.ConservationStatus=='NT', 'MinWingspan']
x5 = filteredBirds.loc[filteredBirds.ConservationStatus=='VU', 'MinWingspan']
x6 = filteredBirds.loc[filteredBirds.ConservationStatus=='LC', 'MinWingspan']

kwargs = dict(alpha=0.5, bins=20)

plt.hist(x1, **kwargs, color='red', label='Extinct')
plt.hist(x2, **kwargs, color='orange', label='Critically Endangered')
plt.hist(x3, **kwargs, color='yellow', label='Endangered')
plt.hist(x4, **kwargs, color='green', label='Near Threatened')
plt.hist(x5, **kwargs, color='blue', label='Vulnerable')
plt.hist(x6, **kwargs, color='gray', label='Least Concern')

plt.gca().set(title='Conservation Status', ylabel='Min Wingspan')
plt.legend();
```

![rozpiętość skrzydeł i status ochrony](../../../../3-Data-Visualization/10-visualization-distributions/images/histogram-conservation-wb.png)

Nie wydaje się, aby istniała dobra korelacja między minimalną rozpiętością skrzydeł a statusem ochrony. Przetestuj inne elementy zbioru danych, korzystając z tej metody. Możesz również wypróbować różne filtry. Czy znajdujesz jakąś korelację?

## Wykresy gęstości

Być może zauważyłeś, że histogramy, które do tej pory oglądaliśmy, są "schodkowe" i nie płyną gładko w łuku. Aby pokazać bardziej płynny wykres gęstości, możesz spróbować wykresu gęstości.

Aby pracować z wykresami gęstości, zapoznaj się z nową biblioteką do tworzenia wykresów, [Seaborn](https://seaborn.pydata.org/generated/seaborn.kdeplot.html). 

Ładując Seaborn, spróbuj stworzyć podstawowy wykres gęstości:

```python
import seaborn as sns
import matplotlib.pyplot as plt
sns.kdeplot(filteredBirds['MinWingspan'])
plt.show()
```
![Wykres gęstości](../../../../3-Data-Visualization/10-visualization-distributions/images/density1.png)

Widzisz, że wykres odzwierciedla poprzedni dla danych o minimalnej rozpiętości skrzydeł; jest po prostu trochę bardziej płynny. Według dokumentacji Seaborn, "W porównaniu do histogramu, KDE może stworzyć wykres, który jest mniej zagracony i bardziej interpretowalny, szczególnie przy rysowaniu wielu rozkładów. Ale ma potencjał do wprowadzenia zniekształceń, jeśli podstawowy rozkład jest ograniczony lub nie jest płynny. Podobnie jak histogram, jakość reprezentacji zależy również od wyboru dobrych parametrów wygładzania." [źródło](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) Innymi słowy, wartości odstające, jak zawsze, mogą sprawić, że wykresy będą działać nieprawidłowo.

Jeśli chciałbyś ponownie przyjrzeć się tej poszarpanej linii MaxBodyMass na drugim wykresie, który stworzyłeś, możesz ją bardzo dobrze wygładzić, odtwarzając ją za pomocą tej metody:

```python
sns.kdeplot(filteredBirds['MaxBodyMass'])
plt.show()
```
![gładka linia masy ciała](../../../../3-Data-Visualization/10-visualization-distributions/images/density2.png)

Jeśli chciałbyś uzyskać linię gładką, ale nie zbyt gładką, edytuj parametr `bw_adjust`: 

```python
sns.kdeplot(filteredBirds['MaxBodyMass'], bw_adjust=.2)
plt.show()
```
![mniej gładka linia masy ciała](../../../../3-Data-Visualization/10-visualization-distributions/images/density3.png)

✅ Przeczytaj o dostępnych parametrach dla tego typu wykresu i eksperymentuj!

Ten typ wykresu oferuje pięknie wyjaśniające wizualizacje. Na przykład, za pomocą kilku linii kodu możesz pokazać gęstość maksymalnej masy ciała według rzędu ptaków:

```python
sns.kdeplot(
   data=filteredBirds, x="MaxBodyMass", hue="Order",
   fill=True, common_norm=False, palette="crest",
   alpha=.5, linewidth=0,
)
```

![masa ciała według rzędu](../../../../3-Data-Visualization/10-visualization-distributions/images/density4.png)

Możesz również mapować gęstość kilku zmiennych na jednym wykresie. Porównaj maksymalną długość i minimalną długość ptaka w odniesieniu do jego statusu ochrony:

```python
sns.kdeplot(data=filteredBirds, x="MinLength", y="MaxLength", hue="ConservationStatus")
```

![wiele gęstości, nałożone na siebie](../../../../3-Data-Visualization/10-visualization-distributions/images/multi.png)

Być może warto zbadać, czy skupisko ptaków oznaczonych jako 'Narażone' według ich długości ma jakieś znaczenie.

## 🚀 Wyzwanie

Histogramy są bardziej zaawansowanym typem wykresu niż podstawowe wykresy punktowe, słupkowe czy liniowe. Poszukaj w internecie dobrych przykładów użycia histogramów. Jak są używane, co pokazują i w jakich dziedzinach lub obszarach badań są najczęściej stosowane?

## [Quiz po lekcji](https://ff-quizzes.netlify.app/en/ds/quiz/19)

## Przegląd i samodzielna nauka

W tej lekcji używałeś Matplotlib i zacząłeś pracować z Seaborn, aby tworzyć bardziej zaawansowane wykresy. Przeprowadź badania na temat `kdeplot` w Seaborn, "ciągłej krzywej gęstości prawdopodobieństwa w jednej lub więcej wymiarach". Przeczytaj [dokumentację](https://seaborn.pydata.org/generated/seaborn.kdeplot.html), aby zrozumieć, jak działa.

## Zadanie

[Zastosuj swoje umiejętności](assignment.md)

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.