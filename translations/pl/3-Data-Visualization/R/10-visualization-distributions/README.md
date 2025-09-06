<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ea67c0c40808fd723594de6896c37ccf",
  "translation_date": "2025-08-24T22:44:15+00:00",
  "source_file": "3-Data-Visualization/R/10-visualization-distributions/README.md",
  "language_code": "pl"
}
-->
# Wizualizacja rozkładów

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| Wizualizacja rozkładów - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

W poprzedniej lekcji dowiedziałeś się kilku interesujących faktów o zbiorze danych dotyczącym ptaków z Minnesoty. Znalazłeś błędne dane, wizualizując wartości odstające, oraz przyjrzałeś się różnicom między kategoriami ptaków na podstawie ich maksymalnej długości.

## [Quiz przed lekcją](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/18)
## Eksploracja zbioru danych o ptakach

Innym sposobem na zgłębianie danych jest analiza ich rozkładu, czyli tego, jak dane są zorganizowane wzdłuż osi. Na przykład, możesz chcieć dowiedzieć się, jak wygląda ogólny rozkład maksymalnej rozpiętości skrzydeł lub maksymalnej masy ciała ptaków z Minnesoty w tym zbiorze danych.

Odkryjmy kilka faktów dotyczących rozkładów danych w tym zbiorze. W konsoli R zaimportuj `ggplot2` oraz bazę danych. Usuń wartości odstające z bazy danych, tak jak w poprzednim temacie.

```r
library(ggplot2)

birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")

birds_filtered <- subset(birds, MaxWingspan < 500)
head(birds_filtered)
```
|      | Nazwa                        | NazwaNaukowa           | Kategoria             | Rząd         | Rodzina  | Rodzaj      | StatusOchrony       | MinDługość | MaxDługość | MinMasaCiała | MaxMasaCiała | MinRozpiętość | MaxRozpiętość |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Czarnobrzucha kaczka gwizdająca | Dendrocygna autumnalis | Kaczki/Gęsi/Wodne ptaki | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Płowa kaczka gwizdająca       | Dendrocygna bicolor    | Kaczki/Gęsi/Wodne ptaki | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Gęś śnieżna                   | Anser caerulescens     | Kaczki/Gęsi/Wodne ptaki | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Gęś Ross'a                    | Anser rossii           | Kaczki/Gęsi/Wodne ptaki | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Gęś białoczelna większa       | Anser albifrons        | Kaczki/Gęsi/Wodne ptaki | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

Ogólnie rzecz biorąc, możesz szybko spojrzeć na sposób, w jaki dane są rozłożone, używając wykresu punktowego, tak jak zrobiliśmy to w poprzedniej lekcji:

```r
ggplot(data=birds_filtered, aes(x=Order, y=MaxLength,group=1)) +
  geom_point() +
  ggtitle("Max Length per order") + coord_flip()
```
![maksymalna długość na rząd](../../../../../translated_images/max-length-per-order.e5b283d952c78c12b091307c5d3cf67132dad6fefe80a073353b9dc5c2bd3eb8.pl.png)

To daje przegląd ogólnego rozkładu długości ciała w zależności od rzędu ptaków, ale nie jest to optymalny sposób na przedstawienie prawdziwych rozkładów. Do tego celu zazwyczaj używa się histogramu.

## Praca z histogramami

`ggplot2` oferuje bardzo dobre sposoby wizualizacji rozkładów danych za pomocą histogramów. Ten typ wykresu przypomina wykres słupkowy, gdzie rozkład można zobaczyć poprzez wzrost i spadek słupków. Aby stworzyć histogram, potrzebujesz danych numerycznych. Histogram można zbudować, definiując typ jako 'hist' dla histogramu. Ten wykres pokazuje rozkład MaxBodyMass dla całego zakresu danych numerycznych w zbiorze. Dzieląc zakres danych na mniejsze przedziały, można zobaczyć rozkład wartości danych:

```r
ggplot(data = birds_filtered, aes(x = MaxBodyMass)) + 
  geom_histogram(bins=10)+ylab('Frequency')
```
![rozkład dla całego zbioru danych](../../../../../translated_images/distribution-over-the-entire-dataset.d22afd3fa96be854e4c82213fedec9e3703cba753d07fad4606aadf58cf7e78e.pl.png)

Jak widać, większość z ponad 400 ptaków w tym zbiorze danych mieści się w zakresie poniżej 2000 dla ich maksymalnej masy ciała. Uzyskaj więcej informacji o danych, zmieniając parametr `bins` na wyższą wartość, na przykład 30:

```r
ggplot(data = birds_filtered, aes(x = MaxBodyMass)) + geom_histogram(bins=30)+ylab('Frequency')
```

![rozkład-30przedziałów](../../../../../translated_images/distribution-30bins.6a3921ea7a421bf71f06bf5231009e43d1146f1b8da8dc254e99b5779a4983e5.pl.png)

Ten wykres pokazuje rozkład w nieco bardziej szczegółowy sposób. Wykres mniej przesunięty w lewo można stworzyć, wybierając dane tylko z określonego zakresu:

Przefiltruj swoje dane, aby uzyskać tylko te ptaki, których masa ciała jest poniżej 60, i pokaż 30 `bins`:

```r
birds_filtered_1 <- subset(birds_filtered, MaxBodyMass > 1 & MaxBodyMass < 60)
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_histogram(bins=30)+ylab('Frequency')
```

![przefiltrowany histogram](../../../../../translated_images/filtered-histogram.6bf5d2bfd82533220e1bd4bc4f7d14308f43746ed66721d9ec8f460732be6674.pl.png)

✅ Wypróbuj inne filtry i punkty danych. Aby zobaczyć pełny rozkład danych, usuń filtr `['MaxBodyMass']`, aby pokazać oznaczone rozkłady.

Histogram oferuje również ciekawe ulepszenia kolorystyczne i etykietowe:

Stwórz histogram 2D, aby porównać relację między dwoma rozkładami. Porównajmy `MaxBodyMass` z `MaxLength`. `ggplot2` oferuje wbudowany sposób pokazania zbieżności za pomocą jaśniejszych kolorów:

```r
ggplot(data=birds_filtered_1, aes(x=MaxBodyMass, y=MaxLength) ) +
  geom_bin2d() +scale_fill_continuous(type = "viridis")
```
Wydaje się, że istnieje oczekiwana korelacja między tymi dwoma elementami wzdłuż przewidywanej osi, z jednym szczególnie silnym punktem zbieżności:

![wykres 2D](../../../../../translated_images/2d-plot.c504786f439bd7ebceebf2465c70ca3b124103e06c7ff7214bf24e26f7aec21e.pl.png)

Histogramy dobrze działają domyślnie dla danych numerycznych. Co jeśli chcesz zobaczyć rozkłady według danych tekstowych? 
## Eksploracja zbioru danych pod kątem rozkładów według danych tekstowych 

Ten zbiór danych zawiera również dobre informacje o kategorii ptaków, ich rodzaju, gatunku, rodzinie oraz statusie ochrony. Przyjrzyjmy się tym informacjom o ochronie. Jaki jest rozkład ptaków według ich statusu ochrony?

> ✅ W zbiorze danych używane są różne skróty do opisania statusu ochrony. Skróty te pochodzą z [IUCN Red List Categories](https://www.iucnredlist.org/), organizacji katalogującej status gatunków.
> 
> - CR: Krytycznie zagrożony
> - EN: Zagrożony
> - EX: Wymarły
> - LC: Najmniejszej troski
> - NT: Bliski zagrożenia
> - VU: Wrażliwy

Są to wartości tekstowe, więc będziesz musiał dokonać transformacji, aby stworzyć histogram. Korzystając z dataframe `filteredBirds`, wyświetl jego status ochrony obok minimalnej rozpiętości skrzydeł. Co widzisz? 

```r
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'EX'] <- 'x1' 
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'CR'] <- 'x2'
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'EN'] <- 'x3'
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'NT'] <- 'x4'
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'VU'] <- 'x5'
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'LC'] <- 'x6'

ggplot(data=birds_filtered_1, aes(x = MinWingspan, fill = ConservationStatus)) +
  geom_histogram(position = "identity", alpha = 0.4, bins = 20) +
  scale_fill_manual(name="Conservation Status",values=c("red","green","blue","pink"),labels=c("Endangered","Near Threathened","Vulnerable","Least Concern"))
```

![rozpiętość skrzydeł i status ochrony](../../../../../translated_images/wingspan-conservation-collation.4024e9aa6910866aa82f0c6cb6a6b4b925bd10079e6b0ef8f92eefa5a6792f76.pl.png)

Nie wydaje się, aby istniała dobra korelacja między minimalną rozpiętością skrzydeł a statusem ochrony. Przetestuj inne elementy zbioru danych, korzystając z tej metody. Możesz również wypróbować różne filtry. Czy znajdujesz jakąś korelację?

## Wykresy gęstości

Być może zauważyłeś, że histogramy, które do tej pory oglądaliśmy, są "schodkowe" i nie płyną gładko w łuku. Aby pokazać bardziej płynny wykres gęstości, możesz spróbować wykresu gęstości.

Przejdźmy teraz do pracy z wykresami gęstości!

```r
ggplot(data = birds_filtered_1, aes(x = MinWingspan)) + 
  geom_density()
```
![wykres gęstości](../../../../../translated_images/density-plot.675ccf865b76c690487fb7f69420a8444a3515f03bad5482886232d4330f5c85.pl.png)

Widać, że wykres odzwierciedla poprzedni dla danych o minimalnej rozpiętości skrzydeł; jest po prostu nieco bardziej płynny. Jeśli chciałbyś powrócić do tego poszarpanego wykresu MaxBodyMass z drugiego wykresu, który stworzyłeś, możesz go bardzo dobrze wygładzić, odtwarzając go za pomocą tej metody:

```r
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_density()
```
![gęstość masy ciała](../../../../../translated_images/bodymass-smooth.d31ce526d82b0a1f19a073815dea28ecfbe58145ec5337e4ef7e8cdac81120b3.pl.png)

Jeśli chciałbyś uzyskać linię płynną, ale nie zbyt płynną, edytuj parametr `adjust`: 

```r
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_density(adjust = 1/5)
```
![mniej płynna masa ciała](../../../../../translated_images/less-smooth-bodymass.10f4db8b683cc17d17b2d33f22405413142004467a1493d416608dafecfdee23.pl.png)

✅ Przeczytaj o dostępnych parametrach dla tego typu wykresu i eksperymentuj!

Ten typ wykresu oferuje piękne wizualizacje wyjaśniające. Na przykład, za pomocą kilku linii kodu możesz pokazać gęstość maksymalnej masy ciała w zależności od rzędu ptaków:

```r
ggplot(data=birds_filtered_1,aes(x = MaxBodyMass, fill = Order)) +
  geom_density(alpha=0.5)
```
![masa ciała na rząd](../../../../../translated_images/bodymass-per-order.9d2b065dd931b928c839d8cdbee63067ab1ae52218a1b90717f4bc744354f485.pl.png)

## 🚀 Wyzwanie

Histogramy są bardziej zaawansowanym typem wykresu niż podstawowe wykresy punktowe, słupkowe czy liniowe. Poszukaj w internecie dobrych przykładów użycia histogramów. Jak są używane, co pokazują i w jakich dziedzinach lub obszarach badań są najczęściej stosowane?

## [Quiz po lekcji](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/19)

## Przegląd i samodzielna nauka

W tej lekcji używałeś `ggplot2` i zacząłeś pracować nad tworzeniem bardziej zaawansowanych wykresów. Przeprowadź badania na temat `geom_density_2d()`, "ciągłej krzywej gęstości prawdopodobieństwa w jednej lub więcej wymiarach". Przeczytaj [dokumentację](https://ggplot2.tidyverse.org/reference/geom_density_2d.html), aby zrozumieć, jak to działa.

## Zadanie

[Zastosuj swoje umiejętności](assignment.md)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.