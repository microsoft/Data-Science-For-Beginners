<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "661dad02c3ac239644d34c1eb51e76f8",
  "translation_date": "2025-09-06T21:43:03+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "hr"
}
-->
# Životni ciklus podatkovne znanosti: Analiza

|![ Sketchnote autora [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Životni ciklus podatkovne znanosti: Analiza - _Sketchnote autora [@nitya](https://twitter.com/nitya)_ |

## [Kviz prije predavanja](https://ff-quizzes.netlify.app/en/ds/quiz/28)

Analiza u životnom ciklusu podataka potvrđuje da podaci mogu odgovoriti na postavljena pitanja ili riješiti određeni problem. Ova faza također se može usredotočiti na potvrđivanje da model ispravno rješava ta pitanja i probleme. Ova lekcija fokusira se na istraživačku analizu podataka (Exploratory Data Analysis ili EDA), koja uključuje tehnike za definiranje značajki i odnosa unutar podataka te pripremu podataka za modeliranje.

Koristit ćemo primjer skupa podataka s [Kagglea](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1) kako bismo pokazali kako se to može primijeniti pomoću Pythona i biblioteke Pandas. Ovaj skup podataka sadrži brojanje nekih uobičajenih riječi pronađenih u e-mailovima, a izvori tih e-mailova su anonimni. Koristite [bilježnicu](notebook.ipynb) u ovom direktoriju kako biste pratili.

## Istraživačka analiza podataka

Faza prikupljanja u životnom ciklusu odnosi se na stjecanje podataka, kao i na probleme i pitanja koja su u fokusu, ali kako znamo da podaci mogu podržati željeni rezultat? 
Podsjetimo da podatkovni znanstvenik može postaviti sljedeća pitanja kada dobije podatke:
- Imam li dovoljno podataka za rješavanje ovog problema?
- Jesu li podaci prihvatljive kvalitete za ovaj problem?
- Ako otkrijem dodatne informacije kroz ove podatke, trebamo li razmotriti promjenu ili redefiniranje ciljeva?

Istraživačka analiza podataka proces je upoznavanja s podacima i može se koristiti za odgovaranje na ova pitanja, kao i za prepoznavanje izazova u radu s danim skupom podataka. Usredotočimo se na neke od tehnika koje se koriste za postizanje ovoga.

## Profiliranje podataka, opisna statistika i Pandas
Kako procijeniti imamo li dovoljno podataka za rješavanje problema? Profiliranje podataka može sažeti i prikupiti neke opće informacije o našem skupu podataka kroz tehnike opisne statistike. Profiliranje podataka pomaže nam razumjeti što nam je dostupno, dok opisna statistika pomaže razumjeti koliko toga imamo.

U nekoliko prethodnih lekcija koristili smo Pandas za pružanje opisne statistike pomoću funkcije [`describe()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html). Ova funkcija pruža brojanje, maksimalne i minimalne vrijednosti, srednju vrijednost, standardnu devijaciju i kvantile za numeričke podatke. Korištenje opisne statistike poput funkcije `describe()` može vam pomoći procijeniti koliko podataka imate i trebate li ih više.

## Uzorkovanje i upiti
Istraživanje svega u velikom skupu podataka može biti vrlo dugotrajno i obično je zadatak koji se prepušta računalima. Međutim, uzorkovanje je koristan alat za razumijevanje podataka i omogućuje bolje razumijevanje onoga što se nalazi u skupu podataka i što on predstavlja. Uz uzorak, možete primijeniti vjerojatnost i statistiku kako biste došli do općih zaključaka o svojim podacima. Iako ne postoji definirano pravilo o tome koliko podataka treba uzorkovati, važno je napomenuti da što više podataka uzorkujete, to precizniju generalizaciju možete napraviti.

Pandas ima funkciju [`sample()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html) u svojoj biblioteci, gdje možete proslijediti argument o tome koliko slučajnih uzoraka želite dobiti i koristiti.

Općenito postavljanje upita podacima može vam pomoći odgovoriti na neka opća pitanja i teorije koje imate. Za razliku od uzorkovanja, upiti vam omogućuju kontrolu i fokusiranje na specifične dijelove podataka o kojima imate pitanja. Funkcija [`query()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) u Pandas biblioteci omogućuje vam odabir stupaca i dobivanje jednostavnih odgovora o podacima kroz dohvaćene retke.

## Istraživanje pomoću vizualizacija
Ne morate čekati da podaci budu temeljito očišćeni i analizirani kako biste počeli stvarati vizualizacije. Zapravo, vizualni prikazi tijekom istraživanja mogu pomoći u prepoznavanju obrazaca, odnosa i problema u podacima. Nadalje, vizualizacije pružaju način komunikacije s onima koji nisu uključeni u upravljanje podacima i mogu biti prilika za dijeljenje i pojašnjenje dodatnih pitanja koja nisu obrađena u fazi prikupljanja. Pogledajte [odjeljak o vizualizacijama](../../../../../../../../../3-Data-Visualization) kako biste saznali više o nekim popularnim načinima vizualnog istraživanja.

## Istraživanje za prepoznavanje nedosljednosti
Sve teme u ovoj lekciji mogu pomoći u prepoznavanju nedostajućih ili nedosljednih vrijednosti, ali Pandas pruža funkcije za provjeru nekih od njih. Funkcije [isna() ili isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) mogu provjeriti nedostajuće vrijednosti. Jedan važan dio istraživanja ovih vrijednosti unutar vaših podataka je istražiti zašto su one uopće nastale. To vam može pomoći odlučiti koje [korake poduzeti za njihovo rješavanje](/2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Kviz nakon predavanja](https://ff-quizzes.netlify.app/en/ds/quiz/29)

## Zadatak

[Istraživanje za odgovore](assignment.md)

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane stručnjaka. Ne preuzimamo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije proizašle iz korištenja ovog prijevoda.