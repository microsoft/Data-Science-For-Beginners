<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6a0556b17de4c8d1a9470b02247b01d4",
  "translation_date": "2025-09-04T14:35:38+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "pl"
}
-->
# Wprowadzenie do Data Science w Chmurze

|![ Sketchnote autorstwa [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Data Science w Chmurze: Wprowadzenie - _Sketchnote autorstwa [@nitya](https://twitter.com/nitya)_ |


W tej lekcji poznasz podstawowe zasady działania chmury, dowiesz się, dlaczego korzystanie z usług chmurowych może być interesujące dla Twoich projektów z zakresu data science, a także przyjrzymy się kilku przykładom projektów data science realizowanych w chmurze. 

## [Quiz przed wykładem](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/32)

## Czym jest chmura?

Chmura, czyli Cloud Computing, to dostarczanie szerokiego zakresu usług obliczeniowych na zasadzie płatności za użycie, hostowanych na infrastrukturze dostępnej przez Internet. Usługi te obejmują takie rozwiązania jak przechowywanie danych, bazy danych, sieci, oprogramowanie, analitykę i inteligentne usługi.

Zazwyczaj wyróżniamy trzy rodzaje chmur: publiczną, prywatną i hybrydową:

* Chmura publiczna: chmura publiczna jest własnością i jest zarządzana przez zewnętrznego dostawcę usług chmurowych, który udostępnia swoje zasoby obliczeniowe publicznie przez Internet.
* Chmura prywatna: odnosi się do zasobów chmurowych używanych wyłącznie przez jedną firmę lub organizację, z usługami i infrastrukturą utrzymywanymi w prywatnej sieci.
* Chmura hybrydowa: chmura hybrydowa to system łączący chmury publiczne i prywatne. Użytkownicy korzystają z lokalnego centrum danych, jednocześnie umożliwiając uruchamianie danych i aplikacji w jednej lub kilku chmurach publicznych.

Większość usług chmurowych można podzielić na trzy kategorie: Infrastruktura jako Usługa (IaaS), Platforma jako Usługa (PaaS) i Oprogramowanie jako Usługa (SaaS).

* Infrastruktura jako Usługa (IaaS): użytkownicy wynajmują infrastrukturę IT, taką jak serwery, maszyny wirtualne (VM), pamięć masową, sieci, systemy operacyjne.
* Platforma jako Usługa (PaaS): użytkownicy wynajmują środowisko do tworzenia, testowania, dostarczania i zarządzania aplikacjami. Nie muszą martwić się o konfigurację ani zarządzanie infrastrukturą serwerów, pamięci masowej, sieci i baz danych potrzebnych do rozwoju.
* Oprogramowanie jako Usługa (SaaS): użytkownicy uzyskują dostęp do aplikacji przez Internet na żądanie, zazwyczaj na zasadzie subskrypcji. Nie muszą martwić się o hosting i zarządzanie aplikacją, infrastrukturą ani konserwacją, taką jak aktualizacje oprogramowania i poprawki bezpieczeństwa.

Najwięksi dostawcy usług chmurowych to Amazon Web Services, Google Cloud Platform i Microsoft Azure.

## Dlaczego warto wybrać chmurę dla Data Science?

Deweloperzy i specjaliści IT wybierają pracę z chmurą z wielu powodów, w tym:

* Innowacyjność: możesz wzbogacić swoje aplikacje, integrując innowacyjne usługi stworzone przez dostawców chmurowych bezpośrednio w swoich aplikacjach.
* Elastyczność: płacisz tylko za usługi, których potrzebujesz, i możesz wybierać spośród szerokiej gamy usług. Zazwyczaj płacisz w miarę użytkowania i dostosowujesz usługi do swoich zmieniających się potrzeb.
* Budżet: nie musisz inwestować w zakup sprzętu i oprogramowania, konfigurację i utrzymanie lokalnych centrów danych – płacisz tylko za to, co wykorzystujesz.
* Skalowalność: Twoje zasoby mogą być skalowane w zależności od potrzeb projektu, co oznacza, że Twoje aplikacje mogą korzystać z większej lub mniejszej mocy obliczeniowej, pamięci i przepustowości, dostosowując się do czynników zewnętrznych w dowolnym momencie.
* Produktywność: możesz skupić się na swoim biznesie, zamiast tracić czas na zadania, które mogą być zarządzane przez kogoś innego, takie jak zarządzanie centrami danych.
* Niezawodność: Cloud Computing oferuje różne sposoby ciągłego tworzenia kopii zapasowych danych i umożliwia tworzenie planów odzyskiwania danych po awarii, aby utrzymać działalność i usługi nawet w czasach kryzysu.
* Bezpieczeństwo: możesz korzystać z polityk, technologii i mechanizmów kontrolnych, które wzmacniają bezpieczeństwo Twojego projektu.

To tylko niektóre z najczęstszych powodów, dla których ludzie decydują się na korzystanie z usług chmurowych. Teraz, gdy lepiej rozumiemy, czym jest chmura i jakie są jej główne zalety, przyjrzyjmy się bardziej szczegółowo pracy naukowców zajmujących się danymi i deweloperów pracujących z danymi oraz temu, jak chmura może pomóc im w rozwiązywaniu różnych wyzwań:

* Przechowywanie dużych ilości danych: zamiast kupować, zarządzać i chronić duże serwery, możesz przechowywać swoje dane bezpośrednio w chmurze, korzystając z rozwiązań takich jak Azure Cosmos DB, Azure SQL Database i Azure Data Lake Storage.
* Integracja danych: integracja danych to kluczowy element Data Science, który pozwala przejść od zbierania danych do podejmowania działań. Dzięki usługom integracji danych oferowanym w chmurze możesz zbierać, przekształcać i integrować dane z różnych źródeł w jednym magazynie danych, korzystając z Data Factory.
* Przetwarzanie danych: przetwarzanie ogromnych ilości danych wymaga dużej mocy obliczeniowej, a nie każdy ma dostęp do wystarczająco wydajnych maszyn, dlatego wiele osób decyduje się na bezpośrednie wykorzystanie ogromnej mocy obliczeniowej chmury do uruchamiania i wdrażania swoich rozwiązań.
* Korzystanie z usług analityki danych: usługi chmurowe, takie jak Azure Synapse Analytics, Azure Stream Analytics i Azure Databricks, pomagają przekształcić dane w użyteczne informacje.
* Korzystanie z usług uczenia maszynowego i inteligencji danych: zamiast zaczynać od zera, możesz korzystać z algorytmów uczenia maszynowego oferowanych przez dostawcę chmurowego, takich jak AzureML. Możesz także korzystać z usług kognitywnych, takich jak zamiana mowy na tekst, tekst na mowę, analiza obrazu i wiele innych.

## Przykłady Data Science w Chmurze

Przyjrzyjmy się kilku scenariuszom, aby lepiej to zobrazować.

### Analiza nastrojów w mediach społecznościowych w czasie rzeczywistym
Zaczniemy od scenariusza często analizowanego przez osoby rozpoczynające naukę uczenia maszynowego: analiza nastrojów w mediach społecznościowych w czasie rzeczywistym.

Załóżmy, że prowadzisz stronę internetową z wiadomościami i chcesz wykorzystać dane na żywo, aby zrozumieć, jakie treści mogą zainteresować Twoich czytelników. Aby dowiedzieć się więcej, możesz stworzyć program, który przeprowadza analizę nastrojów w czasie rzeczywistym na podstawie danych z publikacji na Twitterze dotyczących tematów istotnych dla Twoich czytelników.

Kluczowe wskaźniki, które będziesz analizować, to liczba tweetów na określone tematy (hashtagi) oraz nastrój, który jest określany za pomocą narzędzi analitycznych przeprowadzających analizę nastrojów wokół określonych tematów.

Kroki niezbędne do stworzenia tego projektu to:

* Utworzenie centrum zdarzeń do strumieniowego przesyłania danych wejściowych, które będzie zbierać dane z Twittera.
* Skonfigurowanie i uruchomienie aplikacji klienckiej Twittera, która będzie wywoływać interfejsy API Twitter Streaming.
* Utworzenie zadania Stream Analytics.
* Określenie danych wejściowych i zapytania dla zadania.
* Utworzenie miejsca docelowego dla danych wyjściowych i określenie wyników zadania.
* Uruchomienie zadania.

Aby zobaczyć cały proces, sprawdź [dokumentację](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099).

### Analiza artykułów naukowych
Przyjrzyjmy się innemu przykładowi projektu stworzonego przez [Dmitrija Soshnikova](http://soshnikov.com), jednego z autorów tego programu nauczania.

Dmitrij stworzył narzędzie analizujące artykuły dotyczące COVID. Przeglądając ten projekt, zobaczysz, jak można stworzyć narzędzie, które wydobywa wiedzę z artykułów naukowych, uzyskuje wgląd i pomaga badaczom poruszać się po dużych zbiorach artykułów w efektywny sposób.

Oto różne kroki użyte w tym projekcie:

* Wydobywanie i wstępne przetwarzanie informacji za pomocą [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Wykorzystanie [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) do równoległego przetwarzania.
* Przechowywanie i zapytania o informacje za pomocą [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Tworzenie interaktywnego pulpitu nawigacyjnego do eksploracji i wizualizacji danych za pomocą Power BI.

Aby zobaczyć cały proces, odwiedź [blog Dmitrija](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/).

Jak widać, usługi chmurowe można wykorzystać na wiele sposobów do realizacji projektów z zakresu Data Science.

## Przypisy

Źródła:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Quiz po wykładzie

## [Quiz po wykładzie](https://ff-quizzes.netlify.app/en/ds/)

## Zadanie

[Badanie rynku](assignment.md)

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.