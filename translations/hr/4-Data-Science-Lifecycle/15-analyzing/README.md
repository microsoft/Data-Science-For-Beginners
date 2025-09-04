<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a167aa0bfb1c46ece1b3d21ae939cc0d",
  "translation_date": "2025-09-04T21:58:00+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "hr"
}
-->
# Životni ciklus podatkovne znanosti: Analiza

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Životni ciklus podatkovne znanosti: Analiza - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## Kviz prije predavanja

## [Kviz prije predavanja](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/28)

Analiza u životnom ciklusu podataka potvrđuje da podaci mogu odgovoriti na postavljena pitanja ili riješiti određeni problem. Ovaj korak također može biti usmjeren na potvrđivanje da model ispravno adresira ta pitanja i probleme. Ova lekcija fokusira se na eksplorativnu analizu podataka (EDA), koja uključuje tehnike za definiranje značajki i odnosa unutar podataka te se može koristiti za pripremu podataka za modeliranje.

Koristit ćemo primjer skupa podataka s [Kagglea](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1) kako bismo pokazali kako se to može primijeniti uz Python i Pandas biblioteku. Ovaj skup podataka sadrži broj nekih uobičajenih riječi pronađenih u e-mailovima, a izvori tih e-mailova su anonimni. Koristite [notebook](../../../../4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb) u ovom direktoriju za praćenje.

## Eksplorativna analiza podataka

Faza prikupljanja u životnom ciklusu je mjesto gdje se podaci dobivaju, kao i problemi i pitanja koja se postavljaju, ali kako možemo znati da podaci mogu podržati krajnji rezultat? 
Podsjetimo da podatkovni znanstvenik može postaviti sljedeća pitanja kada dobije podatke:
-   Imam li dovoljno podataka za rješavanje ovog problema?
-   Jesu li podaci prihvatljive kvalitete za ovaj problem?
-   Ako otkrijem dodatne informacije kroz ove podatke, trebamo li razmotriti promjenu ili redefiniranje ciljeva?

Eksplorativna analiza podataka je proces upoznavanja podataka i može se koristiti za odgovaranje na ova pitanja, kao i za identificiranje izazova u radu s podacima. Usredotočimo se na neke od tehnika koje se koriste za postizanje ovoga.

## Profiliranje podataka, deskriptivna statistika i Pandas
Kako procijeniti imamo li dovoljno podataka za rješavanje problema? Profiliranje podataka može sažeti i prikupiti neke opće informacije o našem skupu podataka kroz tehnike deskriptivne statistike. Profiliranje podataka pomaže nam razumjeti što nam je dostupno, a deskriptivna statistika pomaže nam razumjeti koliko toga imamo.

U nekoliko prethodnih lekcija koristili smo Pandas za pružanje deskriptivne statistike pomoću funkcije [`describe()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html). Ona pruža broj, maksimalne i minimalne vrijednosti, srednju vrijednost, standardnu devijaciju i kvantile za numeričke podatke. Korištenje deskriptivne statistike poput funkcije `describe()` može vam pomoći procijeniti koliko podataka imate i trebate li više.

## Uzorkovanje i upiti
Istraživanje svega u velikom skupu podataka može biti vrlo dugotrajno i obično se prepušta računalima. Međutim, uzorkovanje je koristan alat za razumijevanje podataka i omogućuje nam bolje razumijevanje onoga što se nalazi u skupu podataka i što predstavlja. Uz uzorak, možete primijeniti vjerojatnost i statistiku kako biste došli do općih zaključaka o svojim podacima. Iako ne postoji definirano pravilo o tome koliko podataka treba uzorkovati, važno je napomenuti da što više podataka uzorkujete, to precizniju generalizaciju možete napraviti o podacima. 

Pandas ima funkciju [`sample()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html) u svojoj biblioteci gdje možete proslijediti argument o tome koliko slučajnih uzoraka želite dobiti i koristiti.

Opći upiti podataka mogu vam pomoći odgovoriti na neka opća pitanja i teorije koje imate. Za razliku od uzorkovanja, upiti vam omogućuju kontrolu i fokusiranje na specifične dijelove podataka o kojima imate pitanja. Funkcija [`query()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) u Pandas biblioteci omogućuje vam odabir stupaca i dobivanje jednostavnih odgovora o podacima kroz dohvaćene retke.

## Istraživanje pomoću vizualizacija
Ne morate čekati da podaci budu temeljito očišćeni i analizirani kako biste počeli stvarati vizualizacije. Zapravo, vizualna reprezentacija tijekom istraživanja može pomoći u identificiranju obrazaca, odnosa i problema u podacima. Nadalje, vizualizacije pružaju način komunikacije s onima koji nisu uključeni u upravljanje podacima i mogu biti prilika za dijeljenje i pojašnjenje dodatnih pitanja koja nisu adresirana u fazi prikupljanja. Pogledajte [sekciju o vizualizacijama](../../../../../../../../../3-Data-Visualization) kako biste saznali više o nekim popularnim načinima istraživanja vizualno.

## Istraživanje za identifikaciju nedosljednosti
Sve teme u ovoj lekciji mogu pomoći u identificiranju nedostajućih ili nedosljednih vrijednosti, ali Pandas pruža funkcije za provjeru nekih od njih. [isna() ili isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) mogu provjeriti nedostajuće vrijednosti. Jedan važan dio istraživanja ovih vrijednosti unutar vaših podataka je istražiti zašto su završile na taj način. To vam može pomoći da odlučite koje [korake poduzeti za njihovo rješavanje](../../../../../../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Kviz nakon predavanja](https://ff-quizzes.netlify.app/en/ds/)

## Zadatak

[Istraživanje za odgovore](assignment.md)

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane stručnjaka. Ne preuzimamo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije proizašle iz korištenja ovog prijevoda.