<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2baeafe1db4d58ee5b8ec85db9de728a",
  "translation_date": "2025-09-05T18:24:26+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "ro"
}
-->
# Ciclu de viață în Știința Datelor: Analiza

|![ Sketchnote de [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Ciclu de viață în Știința Datelor: Analiza - _Sketchnote de [@nitya](https://twitter.com/nitya)_ |

## Chestionar înainte de lecție

## [Chestionar înainte de lecție](https://ff-quizzes.netlify.app/en/ds/quiz/28)

Analiza în cadrul ciclului de viață al datelor confirmă că datele pot răspunde la întrebările propuse sau pot rezolva o anumită problemă. Acest pas se concentrează, de asemenea, pe confirmarea faptului că un model abordează corect aceste întrebări și probleme. Lecția aceasta este axată pe Analiza Exploratorie a Datelor (EDA), care reprezintă tehnici pentru definirea caracteristicilor și relațiilor din cadrul datelor și poate fi utilizată pentru pregătirea datelor pentru modelare.

Vom folosi un set de date exemplu de pe [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1) pentru a arăta cum poate fi aplicat acest lucru folosind Python și biblioteca Pandas. Acest set de date conține un număr de cuvinte comune găsite în e-mailuri, sursele acestor e-mailuri fiind anonime. Folosiți [notebook-ul](../../../../4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb) din acest director pentru a urmări.

## Analiza Exploratorie a Datelor

Faza de captare a ciclului de viață este cea în care datele sunt obținute, precum și problemele și întrebările de rezolvat, dar cum putem ști dacă datele pot susține rezultatul final? 
Amintiți-vă că un specialist în știința datelor poate pune următoarele întrebări atunci când obține datele:
-   Am suficiente date pentru a rezolva această problemă?
-   Datele sunt de o calitate acceptabilă pentru această problemă?
-   Dacă descopăr informații suplimentare prin aceste date, ar trebui să luăm în considerare schimbarea sau redefinirea obiectivelor?
Analiza Exploratorie a Datelor este procesul de familiarizare cu datele și poate fi utilizată pentru a răspunde la aceste întrebări, precum și pentru a identifica provocările legate de lucrul cu setul de date. Să ne concentrăm pe câteva dintre tehnicile utilizate pentru a realiza acest lucru.

## Profilarea Datelor, Statistici Descriptive și Pandas
Cum evaluăm dacă avem suficiente date pentru a rezolva această problemă? Profilarea datelor poate rezuma și aduna câteva informații generale despre setul nostru de date prin tehnici de statistici descriptive. Profilarea datelor ne ajută să înțelegem ce este disponibil pentru noi, iar statisticile descriptive ne ajută să înțelegem câte lucruri sunt disponibile pentru noi.

În câteva lecții anterioare, am folosit Pandas pentru a oferi câteva statistici descriptive cu funcția [`describe()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html). Aceasta oferă numărul, valorile maxime și minime, media, deviația standard și cuantilele pentru datele numerice. Utilizarea statisticilor descriptive, cum ar fi funcția `describe()`, vă poate ajuta să evaluați cât de multe date aveți și dacă aveți nevoie de mai multe.

## Eșantionare și Interogare
Explorarea tuturor datelor dintr-un set mare poate fi foarte consumatoare de timp și, de obicei, este o sarcină lăsată în seama unui computer. Totuși, eșantionarea este un instrument util pentru înțelegerea datelor și ne permite să avem o mai bună înțelegere a ceea ce se află în setul de date și ce reprezintă. Cu un eșantion, puteți aplica probabilități și statistici pentru a ajunge la concluzii generale despre datele dvs. Deși nu există o regulă definită despre cât de multe date ar trebui să eșantionați, este important de menționat că cu cât eșantionați mai multe date, cu atât generalizarea despre date va fi mai precisă. 
Pandas are funcția [`sample()` în biblioteca sa](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html), unde puteți trece un argument despre câte eșantioane aleatorii doriți să primiți și să utilizați.

Interogarea generală a datelor vă poate ajuta să răspundeți la câteva întrebări și teorii generale pe care le aveți. Spre deosebire de eșantionare, interogările vă permit să aveți control și să vă concentrați pe părți specifice ale datelor despre care aveți întrebări. 
Funcția [`query()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) din biblioteca Pandas vă permite să selectați coloane și să primiți răspunsuri simple despre date prin rândurile recuperate.

## Explorarea cu Vizualizări
Nu trebuie să așteptați până când datele sunt complet curățate și analizate pentru a începe să creați vizualizări. De fapt, a avea o reprezentare vizuală în timpul explorării poate ajuta la identificarea modelelor, relațiilor și problemelor din date. Mai mult, vizualizările oferă un mijloc de comunicare cu cei care nu sunt implicați în gestionarea datelor și pot fi o oportunitate de a împărtăși și clarifica întrebări suplimentare care nu au fost abordate în etapa de captare. Consultați [secțiunea despre Vizualizări](../../../../../../../../../3-Data-Visualization) pentru a afla mai multe despre câteva modalități populare de explorare vizuală.

## Explorarea pentru identificarea inconsistențelor
Toate subiectele din această lecție pot ajuta la identificarea valorilor lipsă sau inconsistente, dar Pandas oferă funcții pentru a verifica unele dintre acestea. [isna() sau isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) pot verifica valorile lipsă. Un aspect important al explorării acestor valori în cadrul datelor dvs. este să explorați de ce au ajuns în această situație. Acest lucru vă poate ajuta să decideți ce [acțiuni să luați pentru a le rezolva](../../../../../../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Chestionar după lecție](https://ff-quizzes.netlify.app/en/ds/quiz/29)

## Temă

[Explorarea pentru răspunsuri](assignment.md)

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.