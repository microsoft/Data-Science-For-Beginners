<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d92f57eb110dc7f765c05cbf0f837c77",
  "translation_date": "2025-08-24T22:19:00+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "pl"
}
-->
# Cykl życia nauki o danych: Analiza

|![ Sketchnote autorstwa [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Cykl życia nauki o danych: Analiza - _Sketchnote autorstwa [@nitya](https://twitter.com/nitya)_ |

## Quiz przed wykładem

## [Quiz przed wykładem](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/28)

Analiza w cyklu życia danych potwierdza, że dane mogą odpowiedzieć na postawione pytania lub rozwiązać konkretny problem. Ten etap może również skupiać się na potwierdzeniu, że model prawidłowo odnosi się do tych pytań i problemów. Ta lekcja koncentruje się na eksploracyjnej analizie danych (Exploratory Data Analysis, EDA), czyli technikach definiowania cech i relacji w danych, które mogą być wykorzystane do przygotowania danych do modelowania.

Wykorzystamy przykładowy zbiór danych z [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1), aby pokazać, jak można to zastosować w Pythonie z użyciem biblioteki Pandas. Ten zbiór danych zawiera liczbę wystąpień niektórych popularnych słów w e-mailach, przy czym źródła tych e-maili są anonimowe. Skorzystaj z [notatnika](../../../../4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb) w tym katalogu, aby śledzić proces.

## Eksploracyjna analiza danych

Faza pozyskiwania w cyklu życia to moment, w którym dane są gromadzone, a problemy i pytania są definiowane. Ale skąd wiemy, że dane mogą wspierać końcowy wynik?  
Przypomnijmy, że naukowiec danych może zadać następujące pytania, gdy pozyskuje dane:
- Czy mam wystarczająco dużo danych, aby rozwiązać ten problem?
- Czy dane są wystarczającej jakości dla tego problemu?
- Jeśli odkryję dodatkowe informacje w tych danych, czy powinniśmy rozważyć zmianę lub redefinicję celów?

Eksploracyjna analiza danych to proces poznawania danych, który może pomóc odpowiedzieć na te pytania, a także zidentyfikować wyzwania związane z pracą z danym zbiorem danych. Skupmy się na niektórych technikach stosowanych w tym celu.

## Profilowanie danych, statystyki opisowe i Pandas
Jak ocenić, czy mamy wystarczająco dużo danych, aby rozwiązać problem? Profilowanie danych może podsumować i zebrać ogólne informacje o naszym zbiorze danych za pomocą technik statystyki opisowej. Profilowanie danych pomaga zrozumieć, co mamy do dyspozycji, a statystyki opisowe pomagają zrozumieć, ile tego mamy.

W kilku poprzednich lekcjach używaliśmy Pandas do generowania statystyk opisowych za pomocą funkcji [`describe()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html). Funkcja ta dostarcza informacji takich jak liczba elementów, wartości maksymalne i minimalne, średnia, odchylenie standardowe i kwantyle dla danych numerycznych. Korzystanie z takich statystyk opisowych jak `describe()` może pomóc ocenić, ile danych mamy i czy potrzebujemy więcej.

## Próbkowanie i zapytania
Eksplorowanie całego dużego zbioru danych może być bardzo czasochłonne i jest to zadanie, które zazwyczaj wykonuje komputer. Jednak próbki danych są pomocnym narzędziem w zrozumieniu danych i pozwalają lepiej zrozumieć, co znajduje się w zbiorze danych i co on reprezentuje. Dzięki próbce można zastosować prawdopodobieństwo i statystykę, aby dojść do ogólnych wniosków na temat danych. Chociaż nie ma określonej reguły dotyczącej tego, ile danych należy próbować, warto zauważyć, że im więcej danych próbkujemy, tym bardziej precyzyjne mogą być nasze uogólnienia.

Pandas oferuje funkcję [`sample()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html), w której można podać argument określający, ile losowych próbek chcemy otrzymać i wykorzystać.

Ogólne zapytania dotyczące danych mogą pomóc odpowiedzieć na niektóre pytania i teorie, które możemy mieć. W przeciwieństwie do próbkowania, zapytania pozwalają nam kontrolować i skupić się na konkretnych częściach danych, które nas interesują. Funkcja [`query()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) w bibliotece Pandas pozwala wybierać kolumny i uzyskiwać proste odpowiedzi na temat danych poprzez pobrane wiersze.

## Eksploracja za pomocą wizualizacji
Nie musisz czekać, aż dane zostaną dokładnie oczyszczone i przeanalizowane, aby zacząć tworzyć wizualizacje. W rzeczywistości posiadanie wizualnej reprezentacji podczas eksploracji może pomóc zidentyfikować wzorce, relacje i problemy w danych. Ponadto wizualizacje stanowią środek komunikacji z osobami, które nie są zaangażowane w zarządzanie danymi, i mogą być okazją do podzielenia się i wyjaśnienia dodatkowych pytań, które nie zostały uwzględnione na etapie pozyskiwania. Odwołaj się do [sekcji o wizualizacjach](../../../../../../../../../3-Data-Visualization), aby dowiedzieć się więcej o popularnych sposobach eksploracji wizualnej.

## Eksploracja w celu identyfikacji niespójności
Wszystkie tematy poruszone w tej lekcji mogą pomóc zidentyfikować brakujące lub niespójne wartości, ale Pandas oferuje funkcje do sprawdzania niektórych z nich. Funkcje [isna() lub isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) mogą sprawdzać brakujące wartości. Ważnym elementem eksploracji tych wartości w danych jest zbadanie, dlaczego znalazły się w takim stanie. Może to pomóc w podjęciu decyzji o [działaniach, które należy podjąć, aby je rozwiązać](../../../../../../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Quiz przed wykładem](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/27)

## Zadanie

[Eksploracja w poszukiwaniu odpowiedzi](assignment.md)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.