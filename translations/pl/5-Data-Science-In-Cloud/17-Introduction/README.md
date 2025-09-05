<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f8e7cdefa096664ae86f795be571580",
  "translation_date": "2025-09-05T14:29:37+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "pl"
}
-->
# Wprowadzenie do Data Science w Chmurze

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Data Science w Chmurze: Wprowadzenie - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

W tej lekcji poznasz podstawowe zasady działania chmury, dowiesz się, dlaczego warto korzystać z usług chmurowych w projektach związanych z data science, a także przyjrzymy się kilku przykładom projektów data science realizowanych w chmurze.

## [Quiz przed wykładem](https://ff-quizzes.netlify.app/en/ds/quiz/32)

## Czym jest chmura?

Chmura, czyli Cloud Computing, to dostarczanie szerokiego zakresu usług obliczeniowych na zasadzie płatności za użycie, hostowanych na infrastrukturze dostępnej przez internet. Usługi te obejmują rozwiązania takie jak przechowywanie danych, bazy danych, sieci, oprogramowanie, analitykę i inteligentne usługi.

Zazwyczaj rozróżniamy chmury publiczne, prywatne i hybrydowe w następujący sposób:

* Chmura publiczna: chmura publiczna jest własnością i jest zarządzana przez zewnętrznego dostawcę usług chmurowych, który udostępnia swoje zasoby obliczeniowe przez internet dla ogółu użytkowników.
* Chmura prywatna: odnosi się do zasobów chmurowych używanych wyłącznie przez jedną firmę lub organizację, z usługami i infrastrukturą utrzymywanymi w prywatnej sieci.
* Chmura hybrydowa: chmura hybrydowa to system łączący chmury publiczne i prywatne. Użytkownicy korzystają z lokalnego centrum danych, jednocześnie umożliwiając uruchamianie danych i aplikacji na jednej lub kilku chmurach publicznych.

Większość usług chmurowych można podzielić na trzy kategorie: Infrastruktura jako Usługa (IaaS), Platforma jako Usługa (PaaS) i Oprogramowanie jako Usługa (SaaS).

* Infrastruktura jako Usługa (IaaS): użytkownicy wynajmują infrastrukturę IT, taką jak serwery, maszyny wirtualne (VM), przechowywanie danych, sieci, systemy operacyjne.
* Platforma jako Usługa (PaaS): użytkownicy wynajmują środowisko do tworzenia, testowania, dostarczania i zarządzania aplikacjami. Nie muszą martwić się o konfigurację ani zarządzanie infrastrukturą serwerów, przechowywania danych, sieci i baz danych potrzebnych do rozwoju.
* Oprogramowanie jako Usługa (SaaS): użytkownicy uzyskują dostęp do aplikacji oprogramowania przez internet, na żądanie i zazwyczaj na zasadzie subskrypcji. Nie muszą martwić się o hosting i zarządzanie aplikacją, infrastrukturą ani konserwację, taką jak aktualizacje oprogramowania czy poprawki bezpieczeństwa.

Niektórzy z największych dostawców usług chmurowych to Amazon Web Services, Google Cloud Platform i Microsoft Azure.

## Dlaczego warto wybrać chmurę dla Data Science?

Programiści i specjaliści IT wybierają pracę z chmurą z wielu powodów, w tym:

* Innowacja: możesz wzbogacić swoje aplikacje, integrując innowacyjne usługi stworzone przez dostawców chmurowych bezpośrednio w swoich aplikacjach.
* Elastyczność: płacisz tylko za usługi, których potrzebujesz, i możesz wybierać spośród szerokiego zakresu usług. Zazwyczaj płacisz na bieżąco i dostosowujesz usługi do swoich zmieniających się potrzeb.
* Budżet: nie musisz inwestować w zakup sprzętu i oprogramowania, konfigurację i prowadzenie lokalnych centrów danych – płacisz tylko za to, co wykorzystujesz.
* Skalowalność: zasoby mogą być skalowane zgodnie z potrzebami projektu, co oznacza, że aplikacje mogą korzystać z większej lub mniejszej mocy obliczeniowej, przechowywania danych i przepustowości, dostosowując się do czynników zewnętrznych w dowolnym momencie.
* Produktywność: możesz skupić się na swojej działalności, zamiast tracić czas na zadania, które mogą być zarządzane przez kogoś innego, takie jak zarządzanie centrami danych.
* Niezawodność: Cloud Computing oferuje różne sposoby ciągłego tworzenia kopii zapasowych danych i umożliwia tworzenie planów odzyskiwania danych po awarii, aby utrzymać działalność i usługi nawet w czasach kryzysu.
* Bezpieczeństwo: możesz korzystać z polityk, technologii i mechanizmów kontrolnych, które wzmacniają bezpieczeństwo Twojego projektu.

To tylko niektóre z najczęstszych powodów, dla których ludzie decydują się na korzystanie z usług chmurowych. Teraz, gdy lepiej rozumiemy, czym jest chmura i jakie są jej główne korzyści, przyjrzyjmy się bardziej szczegółowo pracy naukowców zajmujących się danymi oraz programistów pracujących z danymi, a także temu, jak chmura może pomóc im w rozwiązywaniu różnych wyzwań:

* Przechowywanie dużych ilości danych: zamiast kupować, zarządzać i chronić duże serwery, możesz przechowywać dane bezpośrednio w chmurze, korzystając z rozwiązań takich jak Azure Cosmos DB, Azure SQL Database i Azure Data Lake Storage.
* Integracja danych: integracja danych jest kluczowym elementem Data Science, który pozwala przejść od zbierania danych do podejmowania działań. Dzięki usługom integracji danych oferowanym w chmurze możesz zbierać, przekształcać i integrować dane z różnych źródeł w jednym magazynie danych, korzystając z Data Factory.
* Przetwarzanie danych: przetwarzanie ogromnych ilości danych wymaga dużej mocy obliczeniowej, a nie każdy ma dostęp do wystarczająco wydajnych maszyn. Dlatego wiele osób decyduje się na wykorzystanie ogromnej mocy obliczeniowej chmury do uruchamiania i wdrażania swoich rozwiązań.
* Korzystanie z usług analityki danych: usługi chmurowe, takie jak Azure Synapse Analytics, Azure Stream Analytics i Azure Databricks, pomagają przekształcić dane w użyteczne informacje.
* Korzystanie z usług uczenia maszynowego i inteligencji danych: zamiast zaczynać od zera, możesz korzystać z algorytmów uczenia maszynowego oferowanych przez dostawcę chmurowego, takich jak AzureML. Możesz również korzystać z usług kognitywnych, takich jak zamiana mowy na tekst, tekst na mowę, analiza obrazu i wiele innych.

## Przykłady Data Science w Chmurze

Przyjrzyjmy się kilku scenariuszom, aby zobaczyć, jak to działa w praktyce.

### Analiza nastrojów w mediach społecznościowych w czasie rzeczywistym

Zacznijmy od scenariusza często analizowanego przez osoby rozpoczynające naukę uczenia maszynowego: analiza nastrojów w mediach społecznościowych w czasie rzeczywistym.

Załóżmy, że prowadzisz stronę internetową z wiadomościami i chcesz wykorzystać dane na żywo, aby zrozumieć, jakie treści mogą zainteresować Twoich czytelników. Aby dowiedzieć się więcej, możesz stworzyć program, który przeprowadza analizę nastrojów w czasie rzeczywistym na podstawie danych z publikacji na Twitterze dotyczących tematów istotnych dla Twoich czytelników.

Kluczowe wskaźniki, na które będziesz zwracać uwagę, to liczba tweetów na określone tematy (hashtagi) oraz nastrój, który jest określany za pomocą narzędzi analitycznych przeprowadzających analizę nastrojów wokół określonych tematów.

Kroki potrzebne do stworzenia tego projektu są następujące:

* Utwórz centrum zdarzeń do strumieniowego przesyłania danych, które będzie zbierać dane z Twittera.
* Skonfiguruj i uruchom aplikację klienta Twittera, która będzie korzystać z Twitter Streaming APIs.
* Utwórz zadanie Stream Analytics.
* Określ dane wejściowe i zapytanie dla zadania.
* Utwórz miejsce docelowe dla danych wyjściowych i określ dane wyjściowe zadania.
* Uruchom zadanie.

Aby zobaczyć pełny proces, sprawdź [dokumentację](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099).

### Analiza prac naukowych

Przyjrzyjmy się innemu przykładowi projektu stworzonego przez [Dmitry Soshnikova](http://soshnikov.com), jednego z autorów tego programu nauczania.

Dmitry stworzył narzędzie do analizy prac naukowych dotyczących COVID. Przeglądając ten projekt, zobaczysz, jak można stworzyć narzędzie, które wydobywa wiedzę z prac naukowych, uzyskuje wgląd w dane i pomaga badaczom efektywnie poruszać się po dużych zbiorach prac.

Zobaczmy różne kroki użyte w tym projekcie:

* Wydobywanie i wstępne przetwarzanie informacji za pomocą [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Korzystanie z [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) do równoległego przetwarzania danych.
* Przechowywanie i zapytania do danych za pomocą [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Tworzenie interaktywnego dashboardu do eksploracji i wizualizacji danych za pomocą Power BI.

Aby zobaczyć pełny proces, odwiedź [blog Dmitry’ego](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/).

Jak widać, usługi chmurowe można wykorzystać na wiele sposobów do realizacji projektów Data Science.

## Przypisy

Źródła:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Quiz po wykładzie

## [Quiz po wykładzie](https://ff-quizzes.netlify.app/en/ds/quiz/33)

## Zadanie

[Badanie rynku](assignment.md)

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.