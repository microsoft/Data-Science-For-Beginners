<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "47028abaaafa2bcb1079702d20569066",
  "translation_date": "2025-08-24T01:25:46+00:00",
  "source_file": "3-Data-Visualization/R/11-visualization-proportions/README.md",
  "language_code": "pl"
}
-->
# Wizualizacja proporcji

|![ Sketchnote autorstwa [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|Wizualizacja proporcji - _Sketchnote autorstwa [@nitya](https://twitter.com/nitya)_ |

W tej lekcji użyjesz innego zestawu danych związanych z naturą, aby zwizualizować proporcje, na przykład ile różnych rodzajów grzybów występuje w danym zestawie danych o pieczarkach. Zbadajmy te fascynujące grzyby, korzystając z zestawu danych pochodzącego z Audubon, który zawiera szczegóły dotyczące 23 gatunków grzybów blaszkowych z rodzin Agaricus i Lepiota. Będziesz eksperymentować z apetycznymi wizualizacjami, takimi jak:

- Wykresy kołowe 🥧
- Wykresy pierścieniowe 🍩
- Wykresy gofrowe 🧇

> 💡 Bardzo interesujący projekt [Charticulator](https://charticulator.com) od Microsoft Research oferuje darmowy interfejs typu "przeciągnij i upuść" do wizualizacji danych. W jednym z ich tutoriali również używają tego zestawu danych o grzybach! Możesz więc eksplorować dane i jednocześnie uczyć się biblioteki: [Tutorial Charticulator](https://charticulator.com/tutorials/tutorial4.html).

## [Quiz przed wykładem](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/20)

## Poznaj swoje grzyby 🍄

Grzyby są bardzo interesujące. Zaimportujmy zestaw danych, aby je zbadać:

```r
mushrooms = read.csv('../../data/mushrooms.csv')
head(mushrooms)
```
Tabela jest wyświetlana z ciekawymi danymi do analizy:


| klasa     | kształt kapelusza | powierzchnia kapelusza | kolor kapelusza | siniaki | zapach    | przyczepność blaszek | odstępy między blaszkami | rozmiar blaszek | kolor blaszek | kształt trzonu | korzeń trzonu | powierzchnia trzonu powyżej pierścienia | powierzchnia trzonu poniżej pierścienia | kolor trzonu powyżej pierścienia | kolor trzonu poniżej pierścienia | typ osłony | kolor osłony | liczba pierścieni | typ pierścienia | kolor zarodników | populacja | siedlisko |
| --------- | ----------------- | ---------------------- | --------------- | ------- | --------- | -------------------- | ----------------------- | --------------- | ------------- | -------------- | ------------- | ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- | ----------- | ------------ | ---------------- | --------------- | ---------------- | ---------- | -------- |
| Trujące   | Wypukły           | Gładka                | Brązowy         | Siniaki | Ostry     | Wolne                | Bliskie                 | Wąskie          | Czarny        | Powiększający  | Równy         | Gładka                        | Gładka                        | Biały                        | Biały                        | Częściowa   | Biały        | Jeden             | Wiszący         | Czarny           | Rozproszona | Miejska  |
| Jadalne   | Wypukły           | Gładka                | Żółty           | Siniaki | Migdałowy | Wolne                | Bliskie                 | Szerokie        | Czarny        | Powiększający  | Maczugowaty   | Gładka                        | Gładka                        | Biały                        | Biały                        | Częściowa   | Biały        | Jeden             | Wiszący         | Brązowy          | Liczna     | Trawy    |
| Jadalne   | Dzwonkowaty       | Gładka                | Biały           | Siniaki | Anyżowy   | Wolne                | Bliskie                 | Szerokie        | Brązowy       | Powiększający  | Maczugowaty   | Gładka                        | Gładka                        | Biały                        | Biały                        | Częściowa   | Biały        | Jeden             | Wiszący         | Brązowy          | Liczna     | Łąki     |
| Trujące   | Wypukły           | Łuskowata             | Biały           | Siniaki | Ostry     | Wolne                | Bliskie                 | Wąskie          | Brązowy       | Powiększający  | Równy         | Gładka                        | Gładka                        | Biały                        | Biały                        | Częściowa   | Biały        | Jeden             | Wiszący         | Czarny           | Rozproszona | Miejska  |
| Jadalne   | Wypukły           | Gładka                | Zielony         | Bez siniaków | Brak   | Wolne                | Zatłoczone             | Szerokie        | Czarny        | Zwężający      | Równy         | Gładka                        | Gładka                        | Biały                        | Biały                        | Częściowa   | Biały        | Jeden             | Zanikający      | Brązowy          | Obfita     | Trawy    |
| Jadalne   | Wypukły           | Łuskowata             | Żółty           | Siniaki | Migdałowy | Wolne                | Bliskie                 | Szerokie        | Brązowy       | Powiększający  | Maczugowaty   | Gładka                        | Gładka                        | Biały                        | Biały                        | Częściowa   | Biały        | Jeden             | Wiszący         | Czarny           | Liczna     | Trawy    |

Od razu zauważasz, że wszystkie dane są tekstowe. Musisz je przekonwertować, aby móc użyć ich w wykresie. Większość danych jest w rzeczywistości reprezentowana jako obiekt:

```r
names(mushrooms)
```

Wynik to:

```output
[1] "class"                    "cap.shape"               
 [3] "cap.surface"              "cap.color"               
 [5] "bruises"                  "odor"                    
 [7] "gill.attachment"          "gill.spacing"            
 [9] "gill.size"                "gill.color"              
[11] "stalk.shape"              "stalk.root"              
[13] "stalk.surface.above.ring" "stalk.surface.below.ring"
[15] "stalk.color.above.ring"   "stalk.color.below.ring"  
[17] "veil.type"                "veil.color"              
[19] "ring.number"              "ring.type"               
[21] "spore.print.color"        "population"              
[23] "habitat"            
```
Weź te dane i przekonwertuj kolumnę 'klasa' na kategorię:

```r
library(dplyr)
grouped=mushrooms %>%
  group_by(class) %>%
  summarise(count=n())
```

Teraz, jeśli wydrukujesz dane o grzybach, zobaczysz, że zostały one pogrupowane w kategorie według klasy trujące/jadalne:
```r
View(grouped)
```

| klasa | liczba |
| --------- | --------- |
| Jadalne | 4208 |
| Trujące | 3916 |

Jeśli zastosujesz kolejność przedstawioną w tej tabeli do tworzenia etykiet kategorii klasy, możesz stworzyć wykres kołowy.

## Koło!

```r
pie(grouped$count,grouped$class, main="Edible?")
```
Voila, wykres kołowy pokazujący proporcje tych danych według dwóch klas grzybów. Bardzo ważne jest, aby poprawnie ustawić kolejność etykiet, szczególnie tutaj, więc upewnij się, że weryfikujesz kolejność, w jakiej budowana jest tablica etykiet!

![wykres kołowy](../../../../../3-Data-Visualization/R/11-visualization-proportions/images/pie1-wb.png)

## Pierścienie!

Nieco bardziej interesującym wizualnie wykresem kołowym jest wykres pierścieniowy, czyli wykres kołowy z dziurą w środku. Przyjrzyjmy się naszym danym za pomocą tej metody.

Spójrz na różne siedliska, w których rosną grzyby:

```r
library(dplyr)
habitat=mushrooms %>%
  group_by(habitat) %>%
  summarise(count=n())
View(habitat)
```
Wynik to:
| siedlisko | liczba |
| --------- | --------- |
| Trawy     | 2148 |
| Liście    | 832 |
| Łąki      | 292 |
| Ścieżki   | 1144 |
| Miejskie  | 368 |
| Odpady    | 192 |
| Drewno    | 3148 |

Tutaj grupujesz swoje dane według siedliska. Jest ich 7, więc użyj ich jako etykiet dla wykresu pierścieniowego:

```r
library(ggplot2)
library(webr)
PieDonut(habitat, aes(habitat, count=count))
```

![wykres pierścieniowy](../../../../../3-Data-Visualization/R/11-visualization-proportions/images/donut-wb.png)

Ten kod używa dwóch bibliotek - ggplot2 i webr. Korzystając z funkcji PieDonut z biblioteki webr, możemy łatwo stworzyć wykres pierścieniowy!

Wykresy pierścieniowe w R można również tworzyć, używając tylko biblioteki ggplot2. Możesz dowiedzieć się więcej na ten temat [tutaj](https://www.r-graph-gallery.com/128-ring-or-donut-plot.html) i spróbować samodzielnie.

Teraz, gdy wiesz, jak grupować dane i wyświetlać je jako koło lub pierścień, możesz eksplorować inne typy wykresów. Spróbuj wykresu gofrowego, który jest po prostu innym sposobem eksplorowania ilości.

## Gofry!

Wykres typu 'gofrowy' to inny sposób wizualizacji ilości jako 2D tablicy kwadratów. Spróbuj zwizualizować różne ilości kolorów kapeluszy grzybów w tym zestawie danych. Aby to zrobić, musisz zainstalować pomocniczą bibliotekę [waffle](https://cran.r-project.org/web/packages/waffle/waffle.pdf) i użyć jej do wygenerowania wizualizacji:

```r
install.packages("waffle", repos = "https://cinc.rud.is")
```

Wybierz segment swoich danych do grupowania:

```r
library(dplyr)
cap_color=mushrooms %>%
  group_by(cap.color) %>%
  summarise(count=n())
View(cap_color)
```

Stwórz wykres gofrowy, tworząc etykiety, a następnie grupując swoje dane:

```r
library(waffle)
names(cap_color$count) = paste0(cap_color$cap.color)
waffle((cap_color$count/10), rows = 7, title = "Waffle Chart")+scale_fill_manual(values=c("brown", "#F0DC82", "#D2691E", "green", 
                                                                                     "pink", "purple", "red", "grey", 
                                                                                     "yellow","white"))
```

Korzystając z wykresu gofrowego, możesz wyraźnie zobaczyć proporcje kolorów kapeluszy w tym zestawie danych o grzybach. Co ciekawe, jest wiele grzybów z zielonymi kapeluszami!

![wykres gofrowy](../../../../../3-Data-Visualization/R/11-visualization-proportions/images/waffle.png)

W tej lekcji nauczyłeś się trzech sposobów wizualizacji proporcji. Najpierw musisz pogrupować swoje dane w kategorie, a następnie zdecydować, który sposób ich wyświetlenia - koło, pierścień czy gofr - jest najlepszy. Wszystkie są apetyczne i dają użytkownikowi natychmiastowy wgląd w zestaw danych.

## 🚀 Wyzwanie

Spróbuj odtworzyć te apetyczne wykresy w [Charticulator](https://charticulator.com).
## [Quiz po wykładzie](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/21)

## Przegląd i samodzielna nauka

Czasami nie jest oczywiste, kiedy użyć wykresu kołowego, pierścieniowego czy gofrowego. Oto kilka artykułów do przeczytania na ten temat:

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402

Poszukaj więcej informacji na temat tego trudnego wyboru.

## Zadanie

[Spróbuj w Excelu](assignment.md)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.