<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1341f6da63d434f5ba31b08ea951b02c",
  "translation_date": "2025-09-05T14:45:33+00:00",
  "source_file": "1-Introduction/02-ethics/README.md",
  "language_code": "pl"
}
-->
# Wprowadzenie do etyki danych

|![ Sketchnote autorstwa [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/02-Ethics.png)|
|:---:|
| Etyka danych - _Sketchnote autorstwa [@nitya](https://twitter.com/nitya)_ |

---

Wszyscy jesteśmy obywatelami danych żyjącymi w świecie zdominowanym przez dane.

Trendy rynkowe wskazują, że do 2022 roku 1 na 3 duże organizacje będzie kupować i sprzedawać swoje dane za pośrednictwem internetowych [rynków i giełd](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/). Jako **twórcy aplikacji**, łatwiej i taniej będzie nam integrować w codzienne doświadczenia użytkowników wnioski oparte na danych oraz automatyzację opartą na algorytmach. Jednak wraz z rozpowszechnieniem się AI, będziemy musieli zrozumieć potencjalne szkody wynikające z [militaryzacji](https://www.youtube.com/watch?v=TQHs8SA1qpk) takich algorytmów na dużą skalę.

Trendy wskazują również, że do 2025 roku stworzymy i zużyjemy ponad [180 zettabajtów](https://www.statista.com/statistics/871513/worldwide-data-created/) danych. Jako **naukowcy danych**, uzyskamy bezprecedensowy dostęp do danych osobowych. Oznacza to, że możemy budować profile behawioralne użytkowników i wpływać na podejmowanie decyzji w sposób, który tworzy [iluzję wolnego wyboru](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice), jednocześnie potencjalnie kierując użytkowników w preferowane przez nas kierunki. To również rodzi szersze pytania dotyczące prywatności danych i ochrony użytkowników.

Etyka danych staje się teraz _niezbędnym zabezpieczeniem_ dla nauki i inżynierii danych, pomagając nam minimalizować potencjalne szkody i niezamierzone konsekwencje wynikające z naszych działań opartych na danych. [Cykl Hype Gartnera dla AI](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/) identyfikuje istotne trendy w cyfrowej etyce, odpowiedzialnej AI i zarządzaniu AI jako kluczowe czynniki napędzające większe megatrendy wokół _demokratyzacji_ i _industrializacji_ AI.

![Cykl Hype Gartnera dla AI - 2020](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

W tej lekcji zgłębimy fascynujący obszar etyki danych - od podstawowych pojęć i wyzwań, przez studia przypadków, aż po zastosowane koncepcje AI, takie jak zarządzanie - które pomagają ustanowić kulturę etyki w zespołach i organizacjach pracujących z danymi i AI.

## [Quiz przed wykładem](https://ff-quizzes.netlify.app/en/ds/quiz/2) 🎯

## Podstawowe definicje

Zacznijmy od zrozumienia podstawowej terminologii.

Słowo "etyka" pochodzi od [greckiego słowa "ethikos"](https://en.wikipedia.org/wiki/Ethics) (i jego korzenia "ethos"), które oznacza _charakter lub moralną naturę_.

**Etyka** dotyczy wspólnych wartości i zasad moralnych, które regulują nasze zachowanie w społeczeństwie. Etyka opiera się nie na prawach, ale na powszechnie akceptowanych normach tego, co jest "dobre vs. złe". Jednak rozważania etyczne mogą wpływać na inicjatywy w zakresie ładu korporacyjnego i regulacje rządowe, które tworzą większe zachęty do przestrzegania zasad.

**Etyka danych** to [nowa gałąź etyki](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1), która "bada i ocenia problemy moralne związane z _danymi, algorytmami i odpowiadającymi im praktykami_". Tutaj **"dane"** koncentrują się na działaniach związanych z generowaniem, rejestrowaniem, kuracją, przetwarzaniem, rozpowszechnianiem, udostępnianiem i użytkowaniem, **"algorytmy"** skupiają się na AI, agentach, uczeniu maszynowym i robotach, a **"praktyki"** dotyczą takich tematów jak odpowiedzialna innowacja, programowanie, hacking i kodeksy etyczne.

**Etyka stosowana** to [praktyczne zastosowanie rozważań moralnych](https://en.wikipedia.org/wiki/Applied_ethics). Jest to proces aktywnego badania kwestii etycznych w kontekście _działań, produktów i procesów w rzeczywistym świecie_ oraz podejmowania działań naprawczych, aby zapewnić ich zgodność z określonymi wartościami etycznymi.

**Kultura etyki** dotyczy [_operacjonalizacji_ etyki stosowanej](https://hbr.org/2019/05/how-to-design-an-ethical-organization), aby upewnić się, że nasze zasady i praktyki etyczne są przyjmowane w sposób spójny i skalowalny w całej organizacji. Udane kultury etyki definiują zasady etyczne na poziomie organizacyjnym, zapewniają znaczące zachęty do przestrzegania zasad i wzmacniają normy etyczne, zachęcając i amplifikując pożądane zachowania na każdym poziomie organizacji.

## Koncepcje etyki

W tej sekcji omówimy koncepcje takie jak **wspólne wartości** (zasady) i **wyzwania etyczne** (problemy) w etyce danych - oraz przeanalizujemy **studia przypadków**, które pomogą zrozumieć te koncepcje w kontekstach rzeczywistego świata.

### 1. Zasady etyki

Każda strategia etyki danych zaczyna się od zdefiniowania _zasad etycznych_ - "wspólnych wartości", które opisują akceptowalne zachowania i kierują zgodnymi działaniami w naszych projektach związanych z danymi i AI. Można je definiować na poziomie indywidualnym lub zespołowym. Jednak większość dużych organizacji określa je w oświadczeniu misji lub ramach _etycznej AI_, które są definiowane na poziomie korporacyjnym i konsekwentnie egzekwowane we wszystkich zespołach.

**Przykład:** Oświadczenie misji [Odpowiedzialnej AI](https://www.microsoft.com/en-us/ai/responsible-ai) firmy Microsoft brzmi: _"Jesteśmy zaangażowani w rozwój AI kierowany przez zasady etyczne, które stawiają ludzi na pierwszym miejscu"_ - identyfikując 6 zasad etycznych w poniższych ramach:

![Odpowiedzialna AI w Microsoft](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

Przyjrzyjmy się krótko tym zasadom. _Przejrzystość_ i _odpowiedzialność_ są podstawowymi wartościami, na których opierają się inne zasady - więc zacznijmy od nich:

* [**Odpowiedzialność**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) sprawia, że praktycy są _odpowiedzialni_ za swoje operacje związane z danymi i AI oraz za zgodność z tymi zasadami etycznymi.
* [**Przejrzystość**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) zapewnia, że działania związane z danymi i AI są _zrozumiałe_ (interpretowalne) dla użytkowników, wyjaśniając co i dlaczego stoi za decyzjami.
* [**Sprawiedliwość**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) - koncentruje się na zapewnieniu, że AI traktuje _wszystkich ludzi_ sprawiedliwie, rozwiązując wszelkie systemowe lub ukryte techniczno-społeczne uprzedzenia w danych i systemach.
* [**Niezawodność i bezpieczeństwo**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - zapewnia, że AI działa _spójnie_ z określonymi wartościami, minimalizując potencjalne szkody lub niezamierzone konsekwencje.
* [**Prywatność i bezpieczeństwo**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - dotyczy zrozumienia pochodzenia danych oraz zapewnienia _prywatności danych i związanych z nimi ochron_ użytkownikom.
* [**Inkluzywność**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - dotyczy projektowania rozwiązań AI z zamiarem dostosowania ich do _szerokiego zakresu ludzkich potrzeb_ i możliwości.

> 🚨 Zastanów się, jakie mogłoby być Twoje oświadczenie misji etyki danych. Przeanalizuj ramy etycznej AI innych organizacji - oto przykłady od [IBM](https://www.ibm.com/cloud/learn/ai-ethics), [Google](https://ai.google/principles) i [Facebook](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/). Jakie wspólne wartości mają? Jak te zasady odnoszą się do produktu AI lub branży, w której działają?

### 2. Wyzwania etyczne

Gdy mamy zdefiniowane zasady etyczne, kolejnym krokiem jest ocena naszych działań związanych z danymi i AI, aby sprawdzić, czy są zgodne z tymi wspólnymi wartościami. Zastanów się nad swoimi działaniami w dwóch kategoriach: _zbieranie danych_ i _projektowanie algorytmów_.

W przypadku zbierania danych działania prawdopodobnie będą dotyczyć **danych osobowych** lub danych umożliwiających identyfikację osób (PII) dla identyfikowalnych żyjących jednostek. Obejmuje to [różnorodne elementy danych nieosobowych](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en), które _łącznie_ identyfikują jednostkę. Wyzwania etyczne mogą dotyczyć _prywatności danych_, _własności danych_ i powiązanych tematów, takich jak _świadoma zgoda_ i _prawa własności intelektualnej_ użytkowników.

W przypadku projektowania algorytmów działania będą obejmować zbieranie i kurację **zbiorów danych**, a następnie ich wykorzystanie do trenowania i wdrażania **modeli danych**, które przewidują wyniki lub automatyzują decyzje w rzeczywistych kontekstach. Wyzwania etyczne mogą wynikać z _uprzedzeń w zbiorach danych_, problemów z _jakością danych_, _niesprawiedliwości_ i _fałszywego przedstawienia_ w algorytmach - w tym niektórych problemów o charakterze systemowym.

W obu przypadkach wyzwania etyczne wskazują obszary, w których nasze działania mogą napotkać konflikt z naszymi wspólnymi wartościami. Aby wykryć, złagodzić, zminimalizować lub wyeliminować te obawy, musimy zadawać moralne pytania "tak/nie" dotyczące naszych działań, a następnie podejmować odpowiednie działania naprawcze. Przyjrzyjmy się niektórym wyzwaniom etycznym i moralnym pytaniom, które się z nimi wiążą:

#### 2.1 Własność danych

Zbieranie danych często obejmuje dane osobowe, które mogą identyfikować podmioty danych. [Własność danych](https://permission.io/blog/data-ownership) dotyczy _kontroli_ i [_praw użytkowników_](https://permission.io/blog/data-ownership) związanych z tworzeniem, przetwarzaniem i rozpowszechnianiem danych.

Moralne pytania, które należy zadać:
 * Kto jest właścicielem danych? (użytkownik czy organizacja)
 * Jakie prawa mają podmioty danych? (np. dostęp, usunięcie, przenoszenie)
 * Jakie prawa mają organizacje? (np. poprawa złośliwych recenzji użytkowników)

#### 2.2 Świadoma zgoda

[Świadoma zgoda](https://legaldictionary.net/informed-consent/) definiuje akt zgody użytkowników na działanie (np. zbieranie danych) z _pełnym zrozumieniem_ istotnych faktów, w tym celu, potencjalnych ryzyk i alternatyw.

Pytania do rozważenia:
 * Czy użytkownik (podmiot danych) wyraził zgodę na przechwytywanie i wykorzystanie danych?
 * Czy użytkownik rozumiał cel, dla którego dane zostały przechwycone?
 * Czy użytkownik rozumiał potencjalne ryzyka wynikające z jego udziału?

#### 2.3 Własność intelektualna

[Własność intelektualna](https://en.wikipedia.org/wiki/Intellectual_property) odnosi się do niematerialnych wytworów wynikających z ludzkiej inicjatywy, które mogą _mieć wartość ekonomiczną_ dla jednostek lub firm.

Pytania do rozważenia:
 * Czy zebrane dane miały wartość ekonomiczną dla użytkownika lub firmy?
 * Czy **użytkownik** ma tutaj własność intelektualną?
 * Czy **organizacja** ma tutaj własność intelektualną?
 * Jeśli te prawa istnieją, jak je chronimy?

#### 2.4 Prywatność danych

[Prywatność danych](https://www.northeastern.edu/graduate/blog/what-is-data-privacy/) lub prywatność informacji odnosi się do zachowania prywatności użytkownika i ochrony jego tożsamości w odniesieniu do danych umożliwiających identyfikację.

Pytania do rozważenia:
 * Czy dane użytkowników (osobowe) są zabezpieczone przed atakami i wyciekami?
 * Czy dane użytkowników są dostępne tylko dla autoryzowanych użytkowników i kontekstów?
 * Czy anonimowość użytkowników jest zachowana podczas udostępniania lub rozpowszechniania danych?
 * Czy użytkownik może zostać zdeidentyfikowany z anonimowych zbiorów danych?

#### 2.5 Prawo do bycia zapomnianym

[Prawo do bycia zapomnianym](https://en.wikipedia.org/wiki/Right_to_be_forgotten) lub [Prawo do usunięcia](https://www.gdpreu.org/right-to-be-forgotten/) zapewnia dodatkową ochronę danych osobowych użytkownikom. W szczególności daje użytkownikom prawo do żądania usunięcia lub wymazania danych osobowych z wyszukiwarek internetowych i innych miejsc, _w określonych okolicznościach_ - pozwalając im na nowy start online bez trzymania ich przeszłych działań przeciwko nim.

Pytania do rozważenia:
 * Czy system pozwala podmiotom danych na żądanie usunięcia?
 * Czy wycofanie zgody użytkownika powinno uruchamiać automatyczne usunięcie?
 * Czy dane zostały zebrane bez zgody lub w sposób niezgodny z prawem?
 * Czy jesteśmy zgodni z regulacjami rządowymi dotyczącymi prywatności danych?

#### 2.6 Uprzedzenia w zbiorach danych

Uprzedzenia w zbiorach danych lub [uprzedzenia w zbieraniu danych](http://researcharticles.com/index.php/bias-in-data-collection-in-research/) dotyczą wyboru _niereprezentatywnego_ podzbioru danych do rozwoju algorytmu, co może prowadzić do potencjalnej niesprawiedliwości w wynikach dla różnych grup. Rodzaje uprzedzeń obejmują uprzedzenia w wyborze lub próbkowaniu, uprzedzenia ochotników i uprzedzenia instrumentów.

Pytania do rozważenia:
 * Czy zrekrutowaliśmy reprezentatywny zestaw podmiotów danych?
 * Czy przetestowaliśmy nasz zebrany lub kuratowany zbiór danych pod kątem różnych uprzedzeń?
 * Czy możemy złagodzić lub usunąć odkryte uprzedzenia?

#### 2.7 Jakość danych

[Jakość danych](https://lakefs.io/data-quality-testing/) sprawdza ważność kuratowanego zbioru danych używanego do rozwoju naszych algorytmów, sprawdzając, czy cechy i rekordy spełniają wymagania dotyczące poziomu dokładności i spójności potrzebnego dla naszego celu AI.

Pytania do rozważenia:
 * Czy przechwyciliśmy ważne _cechy_ dla naszego przypadku użycia?
 * Czy dane były przechwy
[Algorithm Fairness](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f) sprawdza, czy projekt algorytmu systematycznie dyskryminuje określone podgrupy osób, co prowadzi do [potencjalnych szkód](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml) w _alokacji_ (gdzie zasoby są odmawiane lub wstrzymywane dla tej grupy) oraz _jakości usług_ (gdzie AI jest mniej dokładne dla niektórych podgrup niż dla innych).

Pytania, które warto tutaj rozważyć:
 * Czy oceniliśmy dokładność modelu dla różnych podgrup i warunków?
 * Czy przeanalizowaliśmy system pod kątem potencjalnych szkód (np. stereotypizacji)?
 * Czy możemy zmodyfikować dane lub ponownie wytrenować modele, aby zminimalizować zidentyfikowane szkody?

Zapoznaj się z zasobami, takimi jak [AI Fairness checklists](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA), aby dowiedzieć się więcej.

#### 2.9 Wprowadzenie w błąd

[Wprowadzenie w błąd w danych](https://www.sciencedirect.com/topics/computer-science/misrepresentation) dotyczy pytania, czy komunikujemy wnioski z uczciwie zgromadzonych danych w sposób zwodniczy, aby wspierać pożądany przekaz.

Pytania, które warto tutaj rozważyć:
 * Czy raportujemy niekompletne lub nieprecyzyjne dane?
 * Czy wizualizujemy dane w sposób prowadzący do mylących wniosków?
 * Czy stosujemy selektywne techniki statystyczne, aby manipulować wynikami?
 * Czy istnieją alternatywne wyjaśnienia, które mogą prowadzić do innych wniosków?

#### 2.10 Wolny wybór
[Iluzja wolnego wyboru](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) pojawia się, gdy "architektury wyboru" systemu wykorzystują algorytmy decyzyjne, aby nakłonić ludzi do podjęcia preferowanego działania, jednocześnie dając im pozorną kontrolę i opcje. Te [ciemne wzorce](https://www.darkpatterns.org/) mogą powodować szkody społeczne i ekonomiczne dla użytkowników. Ponieważ decyzje użytkowników wpływają na profile zachowań, te działania mogą potencjalnie napędzać przyszłe wybory, które wzmacniają lub rozszerzają skutki tych szkód.

Pytania, które warto tutaj rozważyć:
 * Czy użytkownik rozumiał konsekwencje podjęcia tej decyzji?
 * Czy użytkownik był świadomy (alternatywnych) opcji oraz ich zalet i wad?
 * Czy użytkownik może później cofnąć automatyczną lub wpłyniętą decyzję?

### 3. Studia przypadków

Aby umieścić te wyzwania etyczne w kontekście rzeczywistym, warto przyjrzeć się studiom przypadków, które podkreślają potencjalne szkody i konsekwencje dla jednostek i społeczeństwa, gdy naruszenia etyki są ignorowane.

Oto kilka przykładów:

| Wyzwanie etyczne | Studium przypadku  | 
|--- |--- |
| **Świadoma zgoda** | 1972 - [Tuskegee Syphilis Study](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - Afroamerykańscy mężczyźni, którzy uczestniczyli w badaniu, zostali obiecani darmową opieką medyczną, _ale zostali oszukani_ przez badaczy, którzy nie poinformowali ich o diagnozie ani o dostępności leczenia. Wielu uczestników zmarło, a ich partnerzy lub dzieci zostali dotknięci; badanie trwało 40 lat. | 
| **Prywatność danych** |  2007 - [Netflix data prize](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) udostępniło badaczom _10M zanonimizowanych ocen filmów od 50K klientów_, aby pomóc w ulepszaniu algorytmów rekomendacji. Jednak badacze byli w stanie powiązać zanonimizowane dane z danymi osobowymi w _zewnętrznych zbiorach danych_ (np. komentarze na IMDb), skutecznie "deanonimizując" niektórych subskrybentów Netflixa.|
| **Stronniczość w zbieraniu danych**  | 2013 - Miasto Boston [opracowało Street Bump](https://www.boston.gov/transportation/street-bump), aplikację pozwalającą obywatelom zgłaszać dziury w drogach, dostarczając miastu lepszych danych o drogach. Jednak [osoby z niższych grup dochodowych miały mniejszy dostęp do samochodów i telefonów](https://hbr.org/2013/04/the-hidden-biases-in-big-data), co sprawiło, że ich problemy drogowe były niewidoczne w tej aplikacji. Twórcy współpracowali z akademikami, aby rozwiązać problemy _równego dostępu i cyfrowych podziałów_ dla sprawiedliwości. |
| **Sprawiedliwość algorytmiczna**  | 2018 - MIT [Gender Shades Study](http://gendershades.org/overview.html) oceniło dokładność produktów AI klasyfikujących płeć, ujawniając luki w dokładności dla kobiet i osób o ciemniejszym kolorze skóry. [Apple Card z 2019 roku](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/) wydawała się oferować mniej kredytu kobietom niż mężczyznom. Oba przypadki ilustrują problemy z uprzedzeniami algorytmicznymi prowadzącymi do szkód społeczno-ekonomicznych.|
| **Wprowadzenie w błąd w danych** | 2020 - [Georgia Department of Public Health opublikowało wykresy COVID-19](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening), które wydawały się wprowadzać obywateli w błąd co do trendów w potwierdzonych przypadkach poprzez niechronologiczne uporządkowanie osi x. To ilustruje wprowadzenie w błąd za pomocą trików wizualizacyjnych. |
| **Iluzja wolnego wyboru** | 2020 - Aplikacja edukacyjna [ABCmouse zapłaciła 10M dolarów w ramach ugody z FTC](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/), gdzie rodzice byli zmuszani do płacenia za subskrypcje, których nie mogli anulować. To ilustruje ciemne wzorce w architekturach wyboru, gdzie użytkownicy byli nakłaniani do potencjalnie szkodliwych decyzji. |
| **Prywatność danych i prawa użytkowników** | 2021 - Facebook [Data Breach](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users) ujawniło dane 530M użytkowników, co skutkowało ugodą w wysokości 5B dolarów z FTC. Jednak odmówiło powiadomienia użytkowników o naruszeniu, naruszając prawa użytkowników dotyczące przejrzystości danych i dostępu. |

Chcesz poznać więcej studiów przypadków? Sprawdź te zasoby:
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - dylematy etyczne w różnych branżach. 
* [Data Science Ethics course](https://www.coursera.org/learn/data-science-ethics#syllabus) - omówione kluczowe studia przypadków.
* [Where things have gone wrong](https://deon.drivendata.org/examples/) - lista kontrolna Deon z przykładami.

> 🚨 Zastanów się nad studiami przypadków, które widziałeś - czy doświadczyłeś lub byłeś dotknięty podobnym wyzwaniem etycznym w swoim życiu? Czy możesz wymyślić co najmniej jedno inne studium przypadku, które ilustruje jedno z wyzwań etycznych omówionych w tej sekcji?

## Zastosowanie etyki

Omówiliśmy koncepcje etyczne, wyzwania i studia przypadków w kontekstach rzeczywistych. Ale jak zacząć _stosować_ zasady i praktyki etyczne w naszych projektach? I jak _operacjonalizować_ te praktyki dla lepszego zarządzania? Przyjrzyjmy się kilku rozwiązaniom w rzeczywistym świecie:

### 1. Kodeksy zawodowe

Kodeksy zawodowe oferują jedną z opcji dla organizacji, aby "zachęcić" członków do wspierania ich zasad etycznych i misji. Kodeksy są _moralnymi wytycznymi_ dla zachowań zawodowych, pomagając pracownikom lub członkom podejmować decyzje zgodne z zasadami organizacji. Są skuteczne tylko w przypadku dobrowolnego przestrzegania przez członków; jednak wiele organizacji oferuje dodatkowe nagrody i kary, aby motywować członków do przestrzegania zasad.

Przykłady obejmują:

 * [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/) Kodeks Etyki
 * [Data Science Association](http://datascienceassn.org/code-of-conduct.html) Kodeks Postępowania (utworzony w 2013 roku)
 * [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics) (od 1993 roku)

> 🚨 Czy należysz do organizacji zawodowej związanej z inżynierią lub nauką o danych? Sprawdź ich stronę, aby zobaczyć, czy definiują kodeks etyki zawodowej. Co mówi to o ich zasadach etycznych? Jak "zachęcają" członków do przestrzegania kodeksu?

### 2. Listy kontrolne etyki

Podczas gdy kodeksy zawodowe definiują wymagane _zachowania etyczne_ od praktyków, [mają znane ograniczenia](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) w egzekwowaniu, szczególnie w projektach na dużą skalę. Zamiast tego wielu ekspertów ds. nauki o danych [zaleca listy kontrolne](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md), które mogą **połączyć zasady z praktykami** w bardziej deterministyczny i wykonalny sposób.

Listy kontrolne przekształcają pytania w zadania "tak/nie", które można operacjonalizować, umożliwiając ich śledzenie jako część standardowych procesów wydania produktu.

Przykłady obejmują:
 * [Deon](https://deon.drivendata.org/) - ogólna lista kontrolna etyki danych stworzona na podstawie [rekomendacji branżowych](https://deon.drivendata.org/#checklist-citations) z narzędziem wiersza poleceń do łatwej integracji.
 * [Privacy Audit Checklist](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - zapewnia ogólne wskazówki dotyczące praktyk obsługi informacji z perspektywy prawnej i społecznej.
 * [AI Fairness Checklist](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - stworzona przez praktyków AI, aby wspierać przyjęcie i integrację kontroli sprawiedliwości w cyklach rozwoju AI.
 * [22 questions for ethics in data and AI](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - bardziej otwarta struktura, zaprojektowana do wstępnej eksploracji problemów etycznych w projektowaniu, wdrażaniu i kontekstach organizacyjnych.

### 3. Regulacje etyczne

Etyka dotyczy definiowania wspólnych wartości i dobrowolnego postępowania właściwie. **Zgodność** dotyczy _przestrzegania prawa_, jeśli jest ono określone. **Zarządzanie** obejmuje szeroko wszystkie sposoby, w jakie organizacje działają, aby egzekwować zasady etyczne i przestrzegać ustalonych przepisów.

Obecnie zarządzanie przyjmuje dwie formy w organizacjach. Po pierwsze, chodzi o definiowanie zasad **etycznego AI** i ustanawianie praktyk, które operacjonalizują ich przyjęcie we wszystkich projektach związanych z AI w organizacji. Po drugie, chodzi o przestrzeganie wszystkich rządowych regulacji dotyczących **ochrony danych** w regionach, w których działa.

Przykłady regulacji dotyczących ochrony danych i prywatności:

 * `1974`, [US Privacy Act](https://www.justice.gov/opcl/privacy-act-1974) - reguluje _federalne_ zbieranie, użycie i ujawnianie danych osobowych.
 * `1996`, [US Health Insurance Portability & Accountability Act (HIPAA)](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - chroni dane osobowe dotyczące zdrowia.
 * `1998`, [US Children's Online Privacy Protection Act (COPPA)](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - chroni prywatność danych dzieci poniżej 13 roku życia.
 * `2018`, [General Data Protection Regulation (GDPR)](https://gdpr-info.eu/) - zapewnia prawa użytkowników, ochronę danych i prywatność.
 * `2018`, [California Consumer Privacy Act (CCPA)](https://www.oag.ca.gov/privacy/ccpa) daje konsumentom więcej _praw_ dotyczących ich (osobistych) danych.
 * `2021`, [Chińska ustawa o ochronie danych osobowych](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) właśnie uchwalona, tworząc jedne z najsilniejszych regulacji dotyczących prywatności danych online na świecie.

> 🚨 Unia Europejska zdefiniowała GDPR (Ogólne Rozporządzenie o Ochronie Danych), które pozostaje jednym z najbardziej wpływowych regulacji dotyczących prywatności danych dzisiaj. Czy wiesz, że definiuje również [8 praw użytkowników](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr), aby chronić cyfrową prywatność i dane osobowe obywateli? Dowiedz się, czym są te prawa i dlaczego są ważne.

### 4. Kultura etyki

Należy zauważyć, że istnieje niematerialna luka między _zgodnością_ (robieniem wystarczająco dużo, aby spełnić "literę prawa") a rozwiązywaniem [systemowych problemów](https://www.coursera.org/learn/data-science-ethics/home/week/4) (takich jak utrwalanie, asymetria informacji i niesprawiedliwość dystrybucyjna), które mogą przyspieszyć uzbrojenie AI.

To drugie wymaga [współpracy w definiowaniu kultur etycznych](https://towardsdatascience.com/why-ai-ethics-requires-a-culture-driven-approach-26f451afa29f), które budują emocjonalne więzi i spójne wspólne wartości _w organizacjach_ w branży. To wymaga bardziej [sformalizowanych kultur etyki danych](https://www.codeforamerica.org/news/formalizing-an-ethical-data-culture/) w organizacjach - pozwalając _każdemu_ [pociągnąć za sznur Andon](https://en.wikipedia.org/wiki/Andon_(manufacturing)) (aby zgłosić obawy etyczne na wczesnym etapie procesu) i czyniąc _oceny etyczne_ (np. w zatrudnianiu) kluczowym kryterium formowania zespołów w projektach AI.

---
## [Quiz po wykładzie](https://ff-quizzes.netlify.app/en/ds/quiz/3) 🎯
## Przegląd i samodzielna nauka 

Kursy i książki pomagają w zrozumieniu podstawowych koncepcji etyki i wyzwań, podczas gdy studia przypadków i narzędzia pomagają w stosowaniu praktyk etycznych w rzeczywistych kontekstach. Oto kilka zasobów na początek:

* [Machine Learning For Beginners](https://github.com/microsoft/ML-For-Beginners/blob/main/1-Introduction/3-fairness/README.md) - lekcja o sprawiedliwości, od Microsoft.
* [Zasady odpowiedzialnej sztucznej inteligencji](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - darmowy kurs edukacyjny od Microsoft Learn.
* [Etyka i nauka o danych](https://resources.oreilly.com/examples/0636920203964) - e-book O'Reilly (M. Loukides, H. Mason i in.)
* [Etyka w nauce o danych](https://www.coursera.org/learn/data-science-ethics#syllabus) - kurs online Uniwersytetu Michigan.
* [Etyka w praktyce](https://ethicsunwrapped.utexas.edu/case-studies) - studia przypadków Uniwersytetu Teksasu.

# Zadanie

[Napisz studium przypadku dotyczące etyki danych](assignment.md)

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.