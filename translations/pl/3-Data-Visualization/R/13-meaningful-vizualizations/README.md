<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4039f1c76548d144a0aee0bf28304ec",
  "translation_date": "2025-08-24T22:56:02+00:00",
  "source_file": "3-Data-Visualization/R/13-meaningful-vizualizations/README.md",
  "language_code": "pl"
}
-->
# Tworzenie Znaczących Wizualizacji

|![ Sketchnote autorstwa [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/13-MeaningfulViz.png)|
|:---:|
| Znaczące Wizualizacje - _Sketchnote autorstwa [@nitya](https://twitter.com/nitya)_ |

> "Jeśli wystarczająco długo torturujesz dane, przyznają się do wszystkiego" -- [Ronald Coase](https://en.wikiquote.org/wiki/Ronald_Coase)

Jedną z podstawowych umiejętności data scientistów jest zdolność tworzenia znaczących wizualizacji danych, które pomagają odpowiadać na postawione pytania. Zanim jednak zaczniesz wizualizować dane, musisz upewnić się, że zostały one oczyszczone i przygotowane, tak jak to robiłeś w poprzednich lekcjach. Dopiero wtedy możesz zdecydować, jak najlepiej je zaprezentować.

W tej lekcji omówimy:

1. Jak wybrać odpowiedni typ wykresu
2. Jak unikać wprowadzających w błąd wykresów
3. Jak pracować z kolorami
4. Jak stylizować wykresy, aby były czytelne
5. Jak tworzyć animowane lub trójwymiarowe wykresy
6. Jak budować kreatywne wizualizacje

## [Quiz przed lekcją](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/24)

## Wybór odpowiedniego typu wykresu

W poprzednich lekcjach eksperymentowałeś z tworzeniem różnych interesujących wizualizacji danych, używając bibliotek Matplotlib i Seaborn. Ogólnie rzecz biorąc, możesz wybrać [odpowiedni typ wykresu](https://chartio.com/learn/charts/how-to-select-a-data-vizualization/) w zależności od pytania, na które chcesz odpowiedzieć, korzystając z poniższej tabeli:

| Potrzebujesz:              | Powinieneś użyć:                |
| -------------------------- | ------------------------------- |
| Pokazać trendy w czasie    | Liniowy                         |
| Porównać kategorie         | Słupkowy, Kołowy                |
| Porównać sumy              | Kołowy, Słupkowy skumulowany    |
| Pokazać relacje            | Punktowy, Liniowy, Facet, Dual Line |
| Pokazać rozkłady           | Punktowy, Histogram, Box        |
| Pokazać proporcje          | Kołowy, Donut, Waffle           |

> ✅ W zależności od struktury danych, może być konieczne przekształcenie ich z tekstowych na numeryczne, aby dany wykres mógł je obsłużyć.

## Unikaj wprowadzania w błąd

Nawet jeśli data scientist starannie dobierze odpowiedni wykres do danych, istnieje wiele sposobów, w jakie dane mogą być przedstawione w sposób wprowadzający w błąd, często kosztem ich wiarygodności. Istnieje wiele przykładów mylących wykresów i infografik!

[![Jak kłamią wykresy autorstwa Alberto Cairo](../../../../../translated_images/pl/tornado.2880ffc7f135f82b5e5328624799010abefd1080ae4b7ecacbdc7d792f1d8849.png)](https://www.youtube.com/watch?v=oX74Nge8Wkw "How charts lie")

> 🎥 Kliknij obrazek powyżej, aby obejrzeć prezentację na temat mylących wykresów

Ten wykres odwraca oś X, aby pokazać coś odwrotnego do prawdy, bazując na dacie:

![zły wykres 1](../../../../../translated_images/pl/bad-chart-1.596bc93425a8ac301a28b8361f59a970276e7b961658ce849886aa1fed427341.png)

[Ten wykres](https://media.firstcoastnews.com/assets/WTLV/images/170ae16f-4643-438f-b689-50d66ca6a8d8/170ae16f-4643-438f-b689-50d66ca6a8d8_1140x641.jpg) jest jeszcze bardziej mylący, ponieważ wzrok kieruje się w prawo, sugerując, że liczba przypadków COVID spadła w różnych hrabstwach. W rzeczywistości, jeśli przyjrzysz się dokładnie datom, zauważysz, że zostały one przestawione, aby stworzyć fałszywy trend spadkowy.

![zły wykres 2](../../../../../translated_images/pl/bad-chart-2.62edf4d2f30f4e519f5ef50c07ce686e27b0196a364febf9a4d98eecd21f9f60.jpg)

Ten znany przykład używa koloru ORAZ odwróconej osi Y, aby wprowadzić w błąd: zamiast wniosku, że liczba zgonów z użyciem broni wzrosła po wprowadzeniu przyjaznego broni ustawodawstwa, wzrok zostaje oszukany, by myśleć, że jest odwrotnie:

![zły wykres 3](../../../../../translated_images/pl/bad-chart-3.e201e2e915a230bc2cde289110604ec9abeb89be510bd82665bebc1228258972.jpg)

Ten dziwny wykres pokazuje, jak proporcje mogą być zmanipulowane, co prowadzi do komicznego efektu:

![zły wykres 4](../../../../../translated_images/pl/bad-chart-4.8872b2b881ffa96c3e0db10eb6aed7793efae2cac382c53932794260f7bfff07.jpg)

Porównywanie rzeczy nieporównywalnych to kolejny nieuczciwy trik. Istnieje [świetna strona internetowa](https://tylervigen.com/spurious-correlations) poświęcona 'fałszywym korelacjom', pokazująca 'fakty', takie jak korelacja między wskaźnikiem rozwodów w Maine a spożyciem margaryny. Grupa na Reddicie również zbiera [brzydkie przykłady](https://www.reddit.com/r/dataisugly/top/?t=all) użycia danych.

Ważne jest, aby zrozumieć, jak łatwo wzrok może zostać oszukany przez mylące wykresy. Nawet jeśli intencje data scientista są dobre, wybór złego typu wykresu, na przykład wykresu kołowego zbyt wielu kategorii, może wprowadzać w błąd.

## Kolor

Na przykładzie wykresu o przemocy z użyciem broni na Florydzie widzieliśmy, jak kolor może dodać dodatkową warstwę znaczenia do wykresów, szczególnie tych, które nie zostały zaprojektowane przy użyciu bibliotek takich jak ggplot2 czy RColorBrewer, które oferują różne sprawdzone palety kolorów. Jeśli tworzysz wykres ręcznie, warto zapoznać się z [teorią kolorów](https://colormatters.com/color-and-design/basic-color-theory).

> ✅ Pamiętaj, projektując wykresy, że dostępność jest ważnym aspektem wizualizacji. Niektórzy użytkownicy mogą być daltonistami - czy Twój wykres jest czytelny dla osób z wadami wzroku?

Bądź ostrożny przy wyborze kolorów do wykresu, ponieważ mogą one przekazywać znaczenie, którego nie zamierzałeś. 'Różowe panie' na wykresie 'wzrostu' powyżej nadają mu wyraźnie 'kobiecy' charakter, co dodatkowo podkreśla absurdalność samego wykresu.

Chociaż [znaczenie kolorów](https://colormatters.com/color-symbolism/the-meanings-of-colors) może różnić się w zależności od regionu świata i zmieniać w zależności od odcienia, ogólnie przyjęte znaczenia kolorów obejmują:

| Kolor  | Znaczenie           |
| ------ | ------------------- |
| czerwony | siła               |
| niebieski | zaufanie, lojalność |
| żółty   | szczęście, ostrożność |
| zielony | ekologia, szczęście, zazdrość |
| fioletowy | szczęście          |
| pomarańczowy | energia          |

Jeśli masz za zadanie stworzyć wykres z niestandardowymi kolorami, upewnij się, że jest on zarówno dostępny, jak i że wybrany kolor odpowiada znaczeniu, które chcesz przekazać.

## Stylizacja wykresów dla czytelności

Wykresy nie są znaczące, jeśli nie są czytelne! Poświęć chwilę na dostosowanie szerokości i wysokości wykresu, aby dobrze skalował się z danymi. Jeśli musisz wyświetlić wiele zmiennych (np. wszystkie 50 stanów), pokaż je pionowo na osi Y, aby uniknąć przewijania w poziomie.

Oznacz osie, dodaj legendę, jeśli to konieczne, i oferuj podpowiedzi, aby ułatwić zrozumienie danych.

Jeśli Twoje dane są tekstowe i obszerne na osi X, możesz ustawić tekst pod kątem, aby poprawić czytelność. [plot3D](https://cran.r-project.org/web/packages/plot3D/index.html) oferuje wykresy 3D, jeśli Twoje dane to umożliwiają. Zaawansowane wizualizacje danych można tworzyć za jego pomocą.

![wykresy 3D](../../../../../translated_images/pl/3d.db1734c151eee87d924989306a00e23f8cddac6a0aab122852ece220e9448def.png)

## Animacja i wyświetlanie wykresów 3D

Niektóre z najlepszych wizualizacji danych są dziś animowane. Shirley Wu stworzyła niesamowite wizualizacje za pomocą D3, takie jak '[film flowers](http://bl.ocks.org/sxywu/raw/d612c6c653fb8b4d7ff3d422be164a5d/)', gdzie każdy kwiat jest wizualizacją filmu. Innym przykładem jest projekt dla Guardiana 'bussed out', interaktywne doświadczenie łączące wizualizacje z Greensock i D3 oraz artykuł w formacie 'scrollytelling', pokazujący, jak Nowy Jork radzi sobie z problemem bezdomności, wysyłając ludzi poza miasto.

![busing](../../../../../translated_images/pl/busing.8157cf1bc89a3f65052d362a78c72f964982ceb9dcacbe44480e35909c3dce62.png)

> "Bussed Out: How America Moves its Homeless" z [Guardiana](https://www.theguardian.com/us-news/ng-interactive/2017/dec/20/bussed-out-america-moves-homeless-people-country-study). Wizualizacje autorstwa Nadieh Bremer & Shirley Wu

Chociaż ta lekcja nie wystarczy, aby szczegółowo nauczyć się tych potężnych bibliotek wizualizacyjnych, spróbuj swoich sił w D3 w aplikacji Vue.js, używając biblioteki do wyświetlenia wizualizacji książki "Niebezpieczne Związki" jako animowanej sieci społecznej.

> "Niebezpieczne Związki" to powieść epistolarna, czyli powieść przedstawiona jako seria listów. Napisana w 1782 roku przez Choderlosa de Laclos, opowiada historię bezwzględnych, moralnie zbankrutowanych intryg dwóch protagonistów francuskiej arystokracji z końca XVIII wieku, Wicehrabiego de Valmont i Markizy de Merteuil. Oboje ponoszą klęskę na końcu, ale nie bez wyrządzenia znacznych szkód społecznych. Powieść rozwija się jako seria listów pisanych do różnych osób z ich otoczenia, planujących zemstę lub po prostu sprawiających kłopoty. Stwórz wizualizację tych listów, aby odkryć głównych bohaterów narracji w sposób wizualny.

Ukończysz aplikację internetową, która wyświetli animowany widok tej sieci społecznej. Wykorzystuje ona bibliotekę stworzoną do [wizualizacji sieci](https://github.com/emiliorizzo/vue-d3-network) za pomocą Vue.js i D3. Gdy aplikacja działa, możesz przeciągać węzły na ekranie, aby przemieszczać dane.

![liaisons](../../../../../translated_images/pl/liaisons.90ce7360bcf8476558f700bbbaf198ad697d5b5cb2829ba141a89c0add7c6ecd.png)

## Projekt: Stwórz wykres przedstawiający sieć za pomocą D3.js

> W folderze tej lekcji znajduje się folder `solution`, w którym znajdziesz ukończony projekt jako odniesienie.

1. Postępuj zgodnie z instrukcjami w pliku README.md w folderze głównym startera. Upewnij się, że masz zainstalowane NPM i Node.js na swoim komputerze przed instalacją zależności projektu.

2. Otwórz folder `starter/src`. Znajdziesz tam folder `assets`, w którym znajduje się plik .json z wszystkimi listami z powieści, ponumerowanymi, z adnotacjami 'to' i 'from'.

3. Uzupełnij kod w `components/Nodes.vue`, aby umożliwić wizualizację. Znajdź metodę o nazwie `createLinks()` i dodaj następującą pętlę zagnieżdżoną.

Przejdź przez obiekt .json, aby uchwycić dane 'to' i 'from' dla listów i zbudować obiekt `links`, aby biblioteka wizualizacyjna mogła go wykorzystać:

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

Uruchom aplikację z terminala (npm run serve) i ciesz się wizualizacją!

## 🚀 Wyzwanie

Przejrzyj internet w poszukiwaniu mylących wizualizacji. Jak autor wprowadza użytkownika w błąd i czy jest to celowe? Spróbuj poprawić wizualizacje, aby pokazać, jak powinny wyglądać.

## [Quiz po lekcji](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/25)

## Przegląd i samodzielna nauka

Oto kilka artykułów do przeczytania na temat mylących wizualizacji danych:

https://gizmodo.com/how-to-lie-with-data-visualization-1563576606

http://ixd.prattsi.org/2017/12/visual-lies-usability-in-deceptive-data-visualizations/

Zapoznaj się z tymi interesującymi wizualizacjami historycznych zasobów i artefaktów:

https://handbook.pubpub.org/

Przeczytaj ten artykuł o tym, jak animacja może wzbogacić Twoje wizualizacje:

https://medium.com/@EvanSinar/use-animation-to-supercharge-data-visualization-cd905a882ad4

## Zadanie

[Stwórz własną niestandardową wizualizację](assignment.md)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.