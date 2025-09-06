<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "22acf28f518a4769ea14fa42f4734b9f",
  "translation_date": "2025-08-24T22:52:14+00:00",
  "source_file": "3-Data-Visualization/R/09-visualization-quantities/README.md",
  "language_code": "pl"
}
-->
# Wizualizacja Ilości
|![ Sketchnote autorstwa [(@sketchthedocs)](https://sketchthedocs.dev) ](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| Wizualizacja Ilości - _Sketchnote autorstwa [@nitya](https://twitter.com/nitya)_ |

W tej lekcji dowiesz się, jak korzystać z niektórych z wielu dostępnych bibliotek pakietów R, aby tworzyć interesujące wizualizacje związane z pojęciem ilości. Korzystając z oczyszczonego zestawu danych o ptakach z Minnesoty, możesz poznać wiele ciekawych faktów o lokalnej faunie.  
## [Quiz przed wykładem](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/16)

## Obserwacja rozpiętości skrzydeł za pomocą ggplot2
Doskonale nadającą się do tworzenia zarówno prostych, jak i zaawansowanych wykresów i diagramów biblioteką jest [ggplot2](https://cran.r-project.org/web/packages/ggplot2/index.html). Ogólnie rzecz biorąc, proces tworzenia wykresów za pomocą tych bibliotek obejmuje identyfikację części ramki danych, które chcesz przeanalizować, przekształcenie danych w razie potrzeby, przypisanie wartości osi x i y, wybór rodzaju wykresu oraz jego wyświetlenie.

`ggplot2` to system do deklaratywnego tworzenia grafik, oparty na The Grammar of Graphics. [Grammar of Graphics](https://en.wikipedia.org/wiki/Ggplot2) to ogólny schemat wizualizacji danych, który dzieli wykresy na semantyczne komponenty, takie jak skale i warstwy. Innymi słowy, łatwość tworzenia wykresów dla danych jednowymiarowych lub wielowymiarowych przy użyciu niewielkiej ilości kodu sprawia, że `ggplot2` jest najpopularniejszym pakietem do wizualizacji w R. Użytkownik określa, jak `ggplot2` ma mapować zmienne na estetykę, jakie prymitywy graficzne użyć, a resztą zajmuje się `ggplot2`.

> ✅ Wykres = Dane + Estetyka + Geometria  
> - Dane odnoszą się do zestawu danych  
> - Estetyka wskazuje zmienne do analizy (zmienne x i y)  
> - Geometria odnosi się do rodzaju wykresu (liniowy, słupkowy itp.)

Wybierz najlepszą geometrię (rodzaj wykresu) w zależności od danych i historii, którą chcesz opowiedzieć za pomocą wykresu.

> - Aby analizować trendy: linia, kolumna  
> - Aby porównywać wartości: słupek, kolumna, koło, wykres punktowy  
> - Aby pokazać, jak części odnoszą się do całości: koło  
> - Aby pokazać rozkład danych: wykres punktowy, słupek  
> - Aby pokazać relacje między wartościami: linia, wykres punktowy, bąbelkowy  

✅ Możesz również sprawdzić ten opisowy [cheatsheet](https://nyu-cdsc.github.io/learningr/assets/data-visualization-2.1.pdf) dla ggplot2.

## Tworzenie wykresu liniowego dla wartości rozpiętości skrzydeł ptaków

Otwórz konsolę R i zaimportuj zestaw danych.  
> Uwaga: Zestaw danych znajduje się w katalogu głównym tego repozytorium w folderze `/data`.

Zaimportujmy zestaw danych i zobaczmy jego początek (pierwsze 5 wierszy).

```r
birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")
head(birds)
```  
Początek danych zawiera mieszankę tekstu i liczb:

|      | Nazwa                        | NazwaNaukowa           | Kategoria             | Rząd         | Rodzina  | Rodzaj      | StatusOchrony       | MinDługość | MaxDługość | MinMasaCiała | MaxMasaCiała | MinRozpiętość | MaxRozpiętość |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Czarnobrzuchy gwizdacz       | Dendrocygna autumnalis | Kaczki/Gęsi/Wodnopławy| Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Płowy gwizdacz               | Dendrocygna bicolor    | Kaczki/Gęsi/Wodnopławy| Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Śnieżna gęś                  | Anser caerulescens     | Kaczki/Gęsi/Wodnopławy| Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Gęś Rossa                    | Anser rossii           | Kaczki/Gęsi/Wodnopławy| Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Gęś białoczelna              | Anser albifrons        | Kaczki/Gęsi/Wodnopławy| Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

Zacznijmy od wykreślenia niektórych danych liczbowych za pomocą podstawowego wykresu liniowego. Załóżmy, że chcesz zobaczyć maksymalną rozpiętość skrzydeł tych interesujących ptaków.

```r
install.packages("ggplot2")
library("ggplot2")
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() 
```  
Tutaj instalujesz pakiet `ggplot2`, a następnie importujesz go do przestrzeni roboczej za pomocą polecenia `library("ggplot2")`. Aby wykreślić dowolny wykres w ggplot, używana jest funkcja `ggplot()`, w której określasz zestaw danych, zmienne x i y jako atrybuty. W tym przypadku używamy funkcji `geom_line()`, ponieważ chcemy wykreślić wykres liniowy.

![MaxWingspan-lineplot](../../../../../translated_images/MaxWingspan-lineplot.b12169f99d26fdd263f291008dfd73c18a4ba8f3d32b1fda3d74af51a0a28616.pl.png)

Co zauważasz od razu? Wydaje się, że jest co najmniej jeden odstający wynik - to całkiem spora rozpiętość skrzydeł! Rozpiętość skrzydeł ponad 2000 centymetrów to ponad 20 metrów - czy w Minnesocie żyją pterodaktyle? Zbadajmy to.

Chociaż możesz szybko posortować dane w Excelu, aby znaleźć te odstające wyniki, które prawdopodobnie są literówkami, kontynuuj proces wizualizacji, pracując bezpośrednio z wykresem.

Dodaj etykiety do osi x, aby pokazać, o jakie ptaki chodzi:

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() +
  theme(axis.text.x = element_text(angle = 45, hjust=1))+
  xlab("Birds") +
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters")
```  
Określamy kąt w `theme` i ustawiamy etykiety osi x i y w `xlab()` i `ylab()` odpowiednio. `ggtitle()` nadaje nazwę wykresowi.

![MaxWingspan-lineplot-improved](../../../../../translated_images/MaxWingspan-lineplot-improved.04b73b4d5a59552a6bc7590678899718e1f065abe9eada9ebb4148939b622fd4.pl.png)

Nawet przy obrocie etykiet o 45 stopni jest ich zbyt wiele, aby je odczytać. Spróbujmy innej strategii: oznacz tylko te odstające wyniki i ustaw etykiety wewnątrz wykresu. Możesz użyć wykresu punktowego, aby zrobić więcej miejsca na etykiety:

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_point() +
  geom_text(aes(label=ifelse(MaxWingspan>500,as.character(Name),'')),hjust=0,vjust=0) + 
  theme(axis.title.x=element_blank(), axis.text.x=element_blank(), axis.ticks.x=element_blank())
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters") + 
```  
Co tu się dzieje? Użyłeś funkcji `geom_point()`, aby wykreślić punkty. Dzięki temu dodałeś etykiety dla ptaków, które miały `MaxWingspan > 500`, a także ukryłeś etykiety na osi x, aby odciążyć wykres.

Co odkrywasz?

![MaxWingspan-scatterplot](../../../../../translated_images/MaxWingspan-scatterplot.60dc9e0e19d32700283558f253841fdab5104abb62bc96f7d97f9c0ee857fa8b.pl.png)

## Filtrowanie danych

Zarówno Bielik amerykański, jak i Sokół preriowy, choć prawdopodobnie bardzo duże ptaki, wydają się być błędnie oznaczone, z dodatkowym zerem w ich maksymalnej rozpiętości skrzydeł. Mało prawdopodobne, że spotkasz Bielika z rozpiętością skrzydeł 25 metrów, ale jeśli tak, daj nam znać! Stwórzmy nową ramkę danych bez tych dwóch odstających wyników:

```r
birds_filtered <- subset(birds, MaxWingspan < 500)

ggplot(data=birds_filtered, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_point() +
  ylab("Wingspan (CM)") +
  xlab("Birds") +
  ggtitle("Max Wingspan in Centimeters") + 
  geom_text(aes(label=ifelse(MaxWingspan>500,as.character(Name),'')),hjust=0,vjust=0) +
  theme(axis.text.x=element_blank(), axis.ticks.x=element_blank())
```  
Stworzyliśmy nową ramkę danych `birds_filtered`, a następnie wykreśliliśmy wykres punktowy. Po odfiltrowaniu odstających wyników dane są teraz bardziej spójne i zrozumiałe.

![MaxWingspan-scatterplot-improved](../../../../../translated_images/MaxWingspan-scatterplot-improved.7d0af81658c65f3e75b8fedeb2335399e31108257e48db15d875ece608272051.pl.png)

Teraz, gdy mamy czystszy zestaw danych przynajmniej pod względem rozpiętości skrzydeł, odkryjmy więcej o tych ptakach.

Chociaż wykresy liniowe i punktowe mogą przedstawiać informacje o wartościach danych i ich rozkładach, chcemy pomyśleć o wartościach zawartych w tym zestawie danych. Możesz stworzyć wizualizacje, aby odpowiedzieć na następujące pytania dotyczące ilości:

> Ile kategorii ptaków istnieje i jakie są ich liczby?  
> Ile ptaków jest wymarłych, zagrożonych, rzadkich lub pospolitych?  
> Ile jest różnych rodzajów i rzędów w terminologii Linneusza?  

## Eksploracja wykresów słupkowych

Wykresy słupkowe są praktyczne, gdy chcesz pokazać grupowanie danych. Zbadajmy kategorie ptaków w tym zestawie danych, aby zobaczyć, która jest najliczniejsza.  
Stwórzmy wykres słupkowy na przefiltrowanych danych.

```r
install.packages("dplyr")
install.packages("tidyverse")

library(lubridate)
library(scales)
library(dplyr)
library(ggplot2)
library(tidyverse)

birds_filtered %>% group_by(Category) %>%
  summarise(n=n(),
  MinLength = mean(MinLength),
  MaxLength = mean(MaxLength),
  MinBodyMass = mean(MinBodyMass),
  MaxBodyMass = mean(MaxBodyMass),
  MinWingspan=mean(MinWingspan),
  MaxWingspan=mean(MaxWingspan)) %>% 
  gather("key", "value", - c(Category, n)) %>%
  ggplot(aes(x = Category, y = value, group = key, fill = key)) +
  geom_bar(stat = "identity") +
  scale_fill_manual(values = c("#D62728", "#FF7F0E", "#8C564B","#2CA02C", "#1F77B4", "#9467BD")) +                   
  xlab("Category")+ggtitle("Birds of Minnesota")

```  
W poniższym fragmencie instalujemy pakiety [dplyr](https://www.rdocumentation.org/packages/dplyr/versions/0.7.8) i [lubridate](https://www.rdocumentation.org/packages/lubridate/versions/1.8.0), aby pomóc w manipulacji i grupowaniu danych w celu wykreślenia wykresu słupkowego. Najpierw grupujesz dane według `Category` ptaków, a następnie podsumowujesz kolumny `MinLength`, `MaxLength`, `MinBodyMass`, `MaxBodyMass`, `MinWingspan`, `MaxWingspan`. Następnie wykreślasz wykres słupkowy za pomocą pakietu `ggplot2`, określając kolory dla różnych kategorii i etykiety.

![Stacked bar chart](../../../../../translated_images/stacked-bar-chart.0c92264e89da7b391a7490224d1e7059a020e8b74dcd354414aeac78871c02f1.pl.png)

Ten wykres słupkowy jest jednak nieczytelny, ponieważ jest zbyt wiele niepogrupowanych danych. Musisz wybrać tylko dane, które chcesz wykreślić, więc spójrzmy na długość ptaków w zależności od ich kategorii.

Przefiltruj swoje dane, aby uwzględnić tylko kategorię ptaków.

Ponieważ istnieje wiele kategorii, możesz wyświetlić ten wykres pionowo i dostosować jego wysokość, aby uwzględnić wszystkie dane:

```r
birds_count<-dplyr::count(birds_filtered, Category, sort = TRUE)
birds_count$Category <- factor(birds_count$Category, levels = birds_count$Category)
ggplot(birds_count,aes(Category,n))+geom_bar(stat="identity")+coord_flip()
```  
Najpierw liczysz unikalne wartości w kolumnie `Category`, a następnie sortujesz je w nowej ramce danych `birds_count`. Te posortowane dane są następnie uwzględniane na tym samym poziomie, aby były wykreślone w uporządkowany sposób. Korzystając z `ggplot2`, wykreślasz dane na wykresie słupkowym. Funkcja `coord_flip()` wykreśla poziome słupki.

![category-length](../../../../../translated_images/category-length.7e34c296690e85d64f7e4d25a56077442683eca96c4f5b4eae120a64c0755636.pl.png)

Ten wykres słupkowy pokazuje dobry widok liczby ptaków w każdej kategorii. Na pierwszy rzut oka widać, że największa liczba ptaków w tym regionie należy do kategorii Kaczki/Gęsi/Wodnopławy. Minnesota to "kraina 10 000 jezior", więc to nie jest zaskakujące!

✅ Spróbuj innych zliczeń na tym zestawie danych. Czy coś Cię zaskoczyło?

## Porównywanie danych

Możesz spróbować różnych porównań pogrupowanych danych, tworząc nowe osie. Spróbuj porównać MaxLength ptaka w zależności od jego kategorii:

```r
birds_grouped <- birds_filtered %>%
  group_by(Category) %>%
  summarise(
  MaxLength = max(MaxLength, na.rm = T),
  MinLength = max(MinLength, na.rm = T)
           ) %>%
  arrange(Category)
  
ggplot(birds_grouped,aes(Category,MaxLength))+geom_bar(stat="identity")+coord_flip()
```  
Grupujemy dane `birds_filtered` według `Category`, a następnie wykreślamy wykres słupkowy.

![comparing data](../../../../../translated_images/comparingdata.f486a450d61c7ca5416f27f3f55a6a4465d00df3be5e6d33936e9b07b95e2fdd.pl.png)

Nic zaskakującego tutaj: kolibry mają najmniejszą MaxLength w porównaniu do pelikanów czy gęsi. Dobrze, gdy dane mają sens logiczny!

Możesz tworzyć bardziej interesujące wizualizacje wykresów słupkowych, nakładając dane. Nałóżmy Minimalną i Maksymalną Długość na daną kategorię ptaków:

```r
ggplot(data=birds_grouped, aes(x=Category)) +
  geom_bar(aes(y=MaxLength), stat="identity", position ="identity",  fill='blue') +
  geom_bar(aes(y=MinLength), stat="identity", position="identity", fill='orange')+
  coord_flip()
```  
![super-imposed values](../../../../../translated_images/superimposed-values.5363f0705a1da4167625a373a1064331ea3cb7a06a297297d0734fcc9b3819a0.pl.png)

## 🚀 Wyzwanie

Ten zestaw danych o ptakach oferuje bogactwo informacji o różnych typach ptaków w danym ekosystemie. Poszukaj w internecie innych zestawów danych o ptakach. Ćwicz tworzenie wykresów i diagramów na podstawie tych danych, aby odkryć fakty, o których nie miałeś pojęcia.  
## [Quiz po wykładzie](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/17)

## Przegląd i samodzielna nauka

Ta pierwsza lekcja dostarczyła Ci informacji o tym, jak używać `ggplot2` do wizualizacji ilości. Poszukaj innych sposobów pracy z zestawami danych do wizualizacji. Poszukaj zestawów danych, które możesz wizualizować za pomocą innych pakietów, takich jak [Lattice](https://stat.ethz.ch/R-manual/R-devel/library/lattice/html/Lattice.html) i [Plotly](https://github.com/plotly/plotly.R#readme).

## Zadanie
[Linie, Punkty i Słupki](assignment.md)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby zapewnić precyzję, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.