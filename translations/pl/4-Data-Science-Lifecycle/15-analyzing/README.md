<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2baeafe1db4d58ee5b8ec85db9de728a",
  "translation_date": "2025-09-05T14:34:34+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "pl"
}
-->
# Cykl życia danych: Analiza

|![ Sketchnote autorstwa [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Cykl życia danych: Analiza - _Sketchnote autorstwa [@nitya](https://twitter.com/nitya)_ |

## Quiz przed wykładem

## [Quiz przed wykładem](https://ff-quizzes.netlify.app/en/ds/quiz/28)

Analiza w cyklu życia danych potwierdza, że dane mogą odpowiedzieć na postawione pytania lub rozwiązać konkretny problem. Ten etap może również skupiać się na potwierdzeniu, że model prawidłowo odnosi się do tych pytań i problemów. Ta lekcja koncentruje się na Eksploracyjnej Analizie Danych (Exploratory Data Analysis, EDA), czyli technikach definiowania cech i relacji w danych, które mogą być wykorzystane do przygotowania danych do modelowania.

Użyjemy przykładowego zestawu danych z [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1), aby pokazać, jak można to zastosować w Pythonie i bibliotece Pandas. Ten zestaw danych zawiera liczbę wystąpień niektórych popularnych słów w e-mailach, a źródła tych e-maili są anonimowe. Skorzystaj z [notebooka](../../../../4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb) w tym katalogu, aby śledzić proces.

## Eksploracyjna Analiza Danych

Faza pozyskiwania w cyklu życia to moment, w którym dane są gromadzone, a problemy i pytania są określane, ale skąd wiemy, że dane mogą wspierać końcowy wynik? 
Przypomnijmy, że data scientist może zadać następujące pytania podczas pozyskiwania danych:
-   Czy mam wystarczająco dużo danych, aby rozwiązać ten problem?
-   Czy dane są odpowiedniej jakości dla tego problemu?
-   Jeśli odkryję dodatkowe informacje dzięki tym danym, czy powinniśmy rozważyć zmianę lub redefinicję celów?

Eksploracyjna Analiza Danych to proces poznawania danych, który może pomóc odpowiedzieć na te pytania, a także zidentyfikować wyzwania związane z pracą z zestawem danych. Skupmy się na niektórych technikach stosowanych w tym celu.

## Profilowanie danych, statystyki opisowe i Pandas
Jak ocenić, czy mamy wystarczająco dużo danych, aby rozwiązać problem? Profilowanie danych może podsumować i zebrać ogólne informacje o naszym zestawie danych za pomocą technik statystyki opisowej. Profilowanie danych pomaga zrozumieć, co jest dostępne, a statystyki opisowe pomagają zrozumieć, ile tego jest.

W kilku poprzednich lekcjach używaliśmy Pandas do generowania statystyk opisowych za pomocą funkcji [`describe()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html). Funkcja ta dostarcza informacji takich jak liczba elementów, wartości maksymalne i minimalne, średnia, odchylenie standardowe oraz kwantyle dla danych numerycznych. Korzystanie ze statystyk opisowych, takich jak funkcja `describe()`, może pomóc ocenić, ile danych posiadamy i czy potrzebujemy więcej.

## Próbkowanie i zapytania
Eksploracja całego dużego zestawu danych może być bardzo czasochłonna i jest to zadanie, które zazwyczaj wykonuje komputer. Jednak próbkowanie jest pomocnym narzędziem w zrozumieniu danych i pozwala lepiej zrozumieć, co znajduje się w zestawie danych i co reprezentuje. Dzięki próbce można zastosować metody statystyczne i probabilistyczne, aby dojść do ogólnych wniosków na temat danych. Choć nie ma określonej reguły dotyczącej ilości danych, które należy próbować, warto pamiętać, że im więcej danych próbkujemy, tym bardziej precyzyjne wnioski możemy wyciągnąć.

Pandas oferuje funkcję [`sample()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html), w której można określić liczbę losowych próbek, które chcemy otrzymać i wykorzystać.

Ogólne zapytania dotyczące danych mogą pomóc odpowiedzieć na pytania i teorie, które mamy. W przeciwieństwie do próbkowania, zapytania pozwalają skupić się na konkretnych częściach danych, które nas interesują. Funkcja [`query()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) w bibliotece Pandas umożliwia wybór kolumn i uzyskanie prostych odpowiedzi na temat danych poprzez pobrane wiersze.

## Eksploracja za pomocą wizualizacji
Nie trzeba czekać, aż dane zostaną dokładnie oczyszczone i przeanalizowane, aby zacząć tworzyć wizualizacje. W rzeczywistości wizualna reprezentacja podczas eksploracji może pomóc zidentyfikować wzorce, relacje i problemy w danych. Ponadto wizualizacje umożliwiają komunikację z osobami, które nie są zaangażowane w zarządzanie danymi, i mogą być okazją do podzielenia się dodatkowymi pytaniami, które nie zostały uwzględnione w fazie pozyskiwania. Odwołaj się do [sekcji o wizualizacjach](../../../../../../../../../3-Data-Visualization), aby dowiedzieć się więcej o popularnych sposobach eksploracji wizualnej.

## Eksploracja w celu identyfikacji niespójności
Wszystkie tematy poruszone w tej lekcji mogą pomóc zidentyfikować brakujące lub niespójne wartości, ale Pandas oferuje funkcje do sprawdzania niektórych z nich. [isna() lub isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) mogą sprawdzić brakujące wartości. Ważnym elementem eksploracji tych wartości w danych jest zrozumienie, dlaczego znalazły się w takim stanie. Może to pomóc w podjęciu decyzji o [działaniach mających na celu ich rozwiązanie](../../../../../../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Quiz po wykładzie](https://ff-quizzes.netlify.app/en/ds/quiz/29)

## Zadanie

[Eksploracja w poszukiwaniu odpowiedzi](assignment.md)

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby zapewnić precyzję, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku źródłowym powinien być uznawany za autorytatywne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.