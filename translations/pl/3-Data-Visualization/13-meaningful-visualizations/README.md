<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0b380bb6d34102bb061eb41de23d9834",
  "translation_date": "2025-09-04T14:45:55+00:00",
  "source_file": "3-Data-Visualization/13-meaningful-visualizations/README.md",
  "language_code": "pl"
}
-->
# Tworzenie Znaczących Wizualizacji

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/13-MeaningfulViz.png)|
|:---:|
| Znaczące Wizualizacje - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

> "Jeśli wystarczająco długo torturujesz dane, wyznają wszystko" -- [Ronald Coase](https://en.wikiquote.org/wiki/Ronald_Coase)

Jedną z podstawowych umiejętności data scientistów jest zdolność do tworzenia znaczących wizualizacji danych, które pomagają odpowiadać na pytania. Przed wizualizacją danych należy upewnić się, że zostały one oczyszczone i przygotowane, jak to miało miejsce w poprzednich lekcjach. Dopiero wtedy można zacząć decydować, jak najlepiej je zaprezentować.

W tej lekcji omówisz:

1. Jak wybrać odpowiedni typ wykresu
2. Jak unikać zwodniczych wykresów
3. Jak pracować z kolorem
4. Jak stylizować wykresy dla czytelności
5. Jak tworzyć animowane lub trójwymiarowe rozwiązania wizualizacyjne
6. Jak budować kreatywne wizualizacje

## [Quiz przed lekcją](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/24)

## Wybierz odpowiedni typ wykresu

W poprzednich lekcjach eksperymentowałeś z tworzeniem różnych interesujących wizualizacji danych za pomocą Matplotlib i Seaborn. Ogólnie rzecz biorąc, możesz wybrać [odpowiedni typ wykresu](https://chartio.com/learn/charts/how-to-select-a-data-vizualization/) dla pytania, które zadajesz, korzystając z tej tabeli:

| Potrzebujesz:              | Powinieneś użyć:                |
| -------------------------- | ------------------------------- |
| Pokazać trendy danych w czasie | Liniowy                        |
| Porównać kategorie         | Słupkowy, Kołowy                |
| Porównać sumy              | Kołowy, Słupkowy warstwowy      |
| Pokazać relacje            | Punktowy, Liniowy, Facet, Podwójny liniowy |
| Pokazać rozkłady           | Punktowy, Histogram, Box        |
| Pokazać proporcje          | Kołowy, Donut, Waffle           |

> ✅ W zależności od struktury danych, może być konieczne przekształcenie ich z tekstowych na numeryczne, aby dany wykres mógł je obsłużyć.

## Unikaj zwodzenia

Nawet jeśli data scientist starannie wybierze odpowiedni wykres dla odpowiednich danych, istnieje wiele sposobów, w jakie dane mogą być przedstawione w sposób wspierający określony punkt widzenia, często kosztem podważenia samych danych. Istnieje wiele przykładów zwodniczych wykresów i infografik!

[![Jak kłamią wykresy - Alberto Cairo](../../../../translated_images/tornado.9f42168791208f970d6faefc11d1226d7ca89518013b14aa66b1c9edcd7678d2.pl.png)](https://www.youtube.com/watch?v=oX74Nge8Wkw "Jak kłamią wykresy")

> 🎥 Kliknij obrazek powyżej, aby obejrzeć konferencyjną prezentację o zwodniczych wykresach

Ten wykres odwraca oś X, aby pokazać coś przeciwnego do prawdy, bazując na dacie:

![zły wykres 1](../../../../translated_images/bad-chart-1.93130f495b748bedfb3423d91b1e754d9026e17f94ad967aecdc9ca7203373bf.pl.png)

[Ten wykres](https://media.firstcoastnews.com/assets/WTLV/images/170ae16f-4643-438f-b689-50d66ca6a8d8/170ae16f-4643-438f-b689-50d66ca6a8d8_1140x641.jpg) jest jeszcze bardziej zwodniczy, ponieważ wzrok kieruje się na prawo, aby wyciągnąć wniosek, że z czasem liczba przypadków COVID spadła w różnych hrabstwach. W rzeczywistości, jeśli przyjrzysz się datom, zauważysz, że zostały one przestawione, aby stworzyć ten zwodniczy trend spadkowy.

![zły wykres 2](../../../../translated_images/bad-chart-2.c20e36dd4e6f617c0c325878dd421a563885bbf30a394884c147438827254e0e.pl.jpg)

Ten słynny przykład używa koloru ORAZ odwróconej osi Y, aby zwodzić: zamiast wyciągać wniosek, że liczba zgonów z broni palnej wzrosła po uchwaleniu przyjaznych dla broni przepisów, wzrok zostaje oszukany, aby myśleć, że stało się odwrotnie:

![zły wykres 3](../../../../translated_images/bad-chart-3.6865d0afac4108d737558d90a61547d23a8722896397ec792264ee51a1be4be5.pl.jpg)

Ten dziwny wykres pokazuje, jak proporcje mogą być manipulowane, z zabawnym efektem:

![zły wykres 4](../../../../translated_images/bad-chart-4.68cfdf4011b454471053ee1231172747e1fbec2403b4443567f1dc678134f4f2.pl.jpg)

Porównywanie rzeczy nieporównywalnych to kolejny podejrzany trik. Istnieje [wspaniała strona internetowa](https://tylervigen.com/spurious-correlations) poświęcona 'fałszywym korelacjom', pokazująca 'fakty' korelujące takie rzeczy jak wskaźnik rozwodów w Maine i spożycie margaryny. Grupa na Reddit również zbiera [brzydkie użycia](https://www.reddit.com/r/dataisugly/top/?t=all) danych.

Ważne jest, aby zrozumieć, jak łatwo wzrok może zostać oszukany przez zwodnicze wykresy. Nawet jeśli intencje data scientist są dobre, wybór złego typu wykresu, takiego jak wykres kołowy pokazujący zbyt wiele kategorii, może być zwodniczy.

## Kolor

Na wykresie 'przemoc z użyciem broni w Florydzie' powyżej widziałeś, jak kolor może dodać dodatkową warstwę znaczenia do wykresów, szczególnie tych, które nie zostały zaprojektowane przy użyciu bibliotek takich jak Matplotlib i Seaborn, które oferują różne sprawdzone biblioteki kolorów i palety. Jeśli tworzysz wykres ręcznie, warto zapoznać się z [teorią kolorów](https://colormatters.com/color-and-design/basic-color-theory).

> ✅ Pamiętaj, projektując wykresy, że dostępność jest ważnym aspektem wizualizacji. Niektórzy użytkownicy mogą być daltonistami - czy Twój wykres jest czytelny dla osób z wadami wzroku?

Bądź ostrożny przy wyborze kolorów dla swojego wykresu, ponieważ kolor może przekazywać znaczenie, którego nie zamierzasz. 'Różowe panie' na wykresie 'wzrostu' powyżej przekazują wyraźnie 'kobiece' przypisane znaczenie, które dodaje do dziwaczności samego wykresu.

Podczas gdy [znaczenie kolorów](https://colormatters.com/color-symbolism/the-meanings-of-colors) może być różne w różnych częściach świata i zmieniać się w zależności od odcienia, ogólnie rzecz biorąc, znaczenia kolorów obejmują:

| Kolor  | Znaczenie           |
| ------ | ------------------- |
| czerwony | siła               |
| niebieski | zaufanie, lojalność |
| żółty   | szczęście, ostrożność |
| zielony | ekologia, szczęście, zazdrość |
| fioletowy | szczęście           |
| pomarańczowy | energia           |

Jeśli masz za zadanie stworzyć wykres z niestandardowymi kolorami, upewnij się, że Twoje wykresy są zarówno dostępne, jak i że kolor, który wybierasz, odpowiada znaczeniu, które chcesz przekazać.

## Stylizowanie wykresów dla czytelności

Wykresy nie są znaczące, jeśli nie są czytelne! Poświęć chwilę na rozważenie stylizacji szerokości i wysokości wykresu, aby dobrze skalował się z danymi. Jeśli jedna zmienna (np. wszystkie 50 stanów) musi być wyświetlona, pokaż je pionowo na osi Y, jeśli to możliwe, aby uniknąć wykresu przewijanego poziomo.

Oznacz swoje osie, dodaj legendę, jeśli to konieczne, i oferuj podpowiedzi dla lepszego zrozumienia danych.

Jeśli Twoje dane są tekstowe i rozbudowane na osi X, możesz ustawić tekst pod kątem dla lepszej czytelności. [Matplotlib](https://matplotlib.org/stable/tutorials/toolkits/mplot3d.html) oferuje wykresy 3D, jeśli Twoje dane na to pozwalają. Zaawansowane wizualizacje danych można tworzyć za pomocą `mpl_toolkits.mplot3d`.

![wykresy 3D](../../../../translated_images/3d.0cec12bcc60f0ce7284c63baed1411a843e24716f7d7425de878715ebad54a15.pl.png)

## Animacja i wyświetlanie wykresów 3D

Niektóre z najlepszych wizualizacji danych dzisiaj są animowane. Shirley Wu stworzyła niesamowite wizualizacje za pomocą D3, takie jak '[film flowers](http://bl.ocks.org/sxywu/raw/d612c6c653fb8b4d7ff3d422be164a5d/)', gdzie każdy kwiat jest wizualizacją filmu. Innym przykładem dla Guardian jest 'bussed out', interaktywne doświadczenie łączące wizualizacje z Greensock i D3 oraz format artykułu typu scrollytelling, aby pokazać, jak NYC radzi sobie z problemem bezdomności, wysyłając ludzi poza miasto.

![busing](../../../../translated_images/busing.7b9e3b41cd4b981c6d63922cd82004cc1cf18895155536c1d98fcc0999bdd23e.pl.png)

> "Bussed Out: Jak Ameryka przenosi swoich bezdomnych" od [Guardian](https://www.theguardian.com/us-news/ng-interactive/2017/dec/20/bussed-out-america-moves-homeless-people-country-study). Wizualizacje autorstwa Nadieh Bremer & Shirley Wu

Chociaż ta lekcja nie jest wystarczająca, aby szczegółowo nauczyć tych potężnych bibliotek wizualizacyjnych, spróbuj swoich sił w D3 w aplikacji Vue.js, używając biblioteki do wyświetlenia wizualizacji książki "Niebezpieczne związki" jako animowanej sieci społecznej.

> "Les Liaisons Dangereuses" to powieść epistolarna, czyli powieść przedstawiona jako seria listów. Napisana w 1782 roku przez Choderlos de Laclos, opowiada historię okrutnych, moralnie zbankrutowanych manewrów społecznych dwóch rywalizujących protagonistów francuskiej arystokracji z końca XVIII wieku, Wicehrabiego de Valmont i Markizy de Merteuil. Oboje spotykają swój koniec, ale nie bez wyrządzenia dużych szkód społecznych. Powieść rozwija się jako seria listów pisanych do różnych osób w ich kręgach, planując zemstę lub po prostu sprawiając kłopoty. Stwórz wizualizację tych listów, aby odkryć głównych bohaterów narracji, wizualnie.

Ukończysz aplikację internetową, która wyświetli animowany widok tej sieci społecznej. Korzysta ona z biblioteki stworzonej do [wizualizacji sieci](https://github.com/emiliorizzo/vue-d3-network) za pomocą Vue.js i D3. Gdy aplikacja działa, możesz przeciągać węzły na ekranie, aby przemieszczać dane.

![liaisons](../../../../translated_images/liaisons.7b440b28f6d07ea430244fdf1fc4c64ff48f473f143b8e921846eda1c302aeba.pl.png)

## Projekt: Stwórz wykres pokazujący sieć za pomocą D3.js

> W folderze lekcji znajduje się folder `solution`, w którym możesz znaleźć ukończony projekt jako odniesienie.

1. Postępuj zgodnie z instrukcjami w pliku README.md w folderze głównym startera. Upewnij się, że masz zainstalowane NPM i Node.js na swoim komputerze przed instalacją zależności projektu.

2. Otwórz folder `starter/src`. Znajdziesz tam folder `assets`, w którym znajduje się plik .json z wszystkimi listami z powieści, ponumerowanymi, z adnotacjami 'do' i 'od'.

3. Uzupełnij kod w `components/Nodes.vue`, aby umożliwić wizualizację. Poszukaj metody o nazwie `createLinks()` i dodaj następującą pętlę zagnieżdżoną.

Przejdź przez obiekt .json, aby uchwycić dane 'do' i 'od' dla listów i zbudować obiekt `links`, aby biblioteka wizualizacyjna mogła go wykorzystać:

```javascript
//loop through letters
      let f = 0;
      let t = 0;
      for (var i = 0; i < letters.length; i++) {
          for (var j = 0; j < characters.length; j++) {
              
            if (characters[j] == letters[i].from) {
              f = j;
            }
            if (characters[j] == letters[i].to) {
              t = j;
            }
        }
        this.links.push({ sid: f, tid: t });
      }
  ```

Uruchom swoją aplikację z terminala (npm run serve) i ciesz się wizualizacją!

## 🚀 Wyzwanie

Przejrzyj internet, aby odkryć zwodnicze wizualizacje. Jak autor oszukuje użytkownika i czy jest to zamierzone? Spróbuj poprawić wizualizacje, aby pokazać, jak powinny wyglądać.

## [Quiz po lekcji](https://ff-quizzes.netlify.app/en/ds/)

## Przegląd i samodzielna nauka

Oto kilka artykułów do przeczytania o zwodniczych wizualizacjach danych:

https://gizmodo.com/how-to-lie-with-data-visualization-1563576606

http://ixd.prattsi.org/2017/12/visual-lies-usability-in-deceptive-data-visualizations/

Zapoznaj się z tymi interesującymi wizualizacjami historycznych zasobów i artefaktów:

https://handbook.pubpub.org/

Przejrzyj ten artykuł o tym, jak animacja może poprawić Twoje wizualizacje:

https://medium.com/@EvanSinar/use-animation-to-supercharge-data-visualization-cd905a882ad4

## Zadanie

[Stwórz własną niestandardową wizualizację](assignment.md)

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.