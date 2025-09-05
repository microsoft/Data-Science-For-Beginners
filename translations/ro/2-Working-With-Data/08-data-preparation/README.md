<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "90a815d332aea41a222f4c6372e7186e",
  "translation_date": "2025-09-05T05:30:22+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "ro"
}
-->
# Lucrul cu Date: Pregătirea Datelor

|![ Sketchnote de [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|Pregătirea Datelor - _Sketchnote de [@nitya](https://twitter.com/nitya)_ |

## [Chestionar Pre-Lecție](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/14)

În funcție de sursa sa, datele brute pot conține unele inconsistențe care vor crea provocări în analiză și modelare. Cu alte cuvinte, aceste date pot fi catalogate drept „murdare” și vor trebui curățate. Această lecție se concentrează pe tehnici de curățare și transformare a datelor pentru a gestiona provocările legate de datele lipsă, inexacte sau incomplete. Subiectele abordate în această lecție vor utiliza Python și biblioteca Pandas și vor fi [demonstrate în notebook](../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb) din acest director.

## Importanța curățării datelor

- **Ușurința utilizării și reutilizării**: Când datele sunt organizate și normalizate corespunzător, este mai ușor să le cauți, să le folosești și să le împărtășești cu alții.

- **Consistență**: Știința datelor necesită adesea lucrul cu mai multe seturi de date, unde seturile de date din surse diferite trebuie să fie combinate. Asigurarea că fiecare set de date individual are o standardizare comună va garanta că datele rămân utile atunci când sunt combinate într-un singur set de date.

- **Acuratețea modelului**: Datele care au fost curățate îmbunătățesc acuratețea modelelor care se bazează pe ele.

## Obiective și strategii comune de curățare

- **Explorarea unui set de date**: Explorarea datelor, care este acoperită într-o [lecție ulterioară](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing), te poate ajuta să descoperi date care trebuie curățate. Observarea vizuală a valorilor dintr-un set de date poate seta așteptări despre cum arată restul sau poate oferi o idee despre problemele care pot fi rezolvate. Explorarea poate implica interogări de bază, vizualizări și eșantionare.

- **Formatare**: În funcție de sursă, datele pot avea inconsistențe în modul în care sunt prezentate. Acest lucru poate cauza probleme în căutarea și reprezentarea valorilor, unde acestea sunt vizibile în setul de date, dar nu sunt reprezentate corect în vizualizări sau rezultate ale interogărilor. Problemele comune de formatare implică rezolvarea spațiilor albe, datelor și tipurilor de date. Rezolvarea problemelor de formatare depinde de utilizatorii datelor. De exemplu, standardele privind modul în care sunt prezentate datele și numerele pot diferi de la o țară la alta.

- **Dubluri**: Datele care au mai multe apariții pot produce rezultate inexacte și, de obicei, ar trebui eliminate. Acest lucru poate apărea frecvent atunci când se combină două sau mai multe seturi de date. Totuși, există cazuri în care dublurile din seturile de date combinate conțin informații suplimentare care ar putea fi necesare să fie păstrate.

- **Date lipsă**: Datele lipsă pot cauza inexactități, precum și rezultate slabe sau părtinitoare. Uneori, acestea pot fi rezolvate printr-o „reîncărcare” a datelor, completarea valorilor lipsă prin calcul și cod, cum ar fi Python, sau pur și simplu eliminarea valorii și a datelor corespunzătoare. Există numeroase motive pentru care datele pot lipsi, iar acțiunile luate pentru a rezolva aceste valori lipsă pot depinde de modul și motivul pentru care au dispărut.

## Explorarea informațiilor din DataFrame
> **Obiectiv de învățare:** La sfârșitul acestei subsecțiuni, ar trebui să fii confortabil în găsirea informațiilor generale despre datele stocate în DataFrames din pandas.

Odată ce ai încărcat datele în pandas, cel mai probabil vor fi într-un DataFrame (consultă [lecția anterioară](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe) pentru o prezentare detaliată). Totuși, dacă setul de date din DataFrame-ul tău are 60.000 de rânduri și 400 de coloane, cum începi să înțelegi cu ce lucrezi? Din fericire, [pandas](https://pandas.pydata.org/) oferă câteva instrumente convenabile pentru a privi rapid informațiile generale despre un DataFrame, pe lângă primele și ultimele câteva rânduri.

Pentru a explora această funcționalitate, vom importa biblioteca Python scikit-learn și vom folosi un set de date iconic: **setul de date Iris**.

```python
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
iris_df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
```
|                                        |lungime sepale (cm)|lățime sepale (cm)|lungime petale (cm)|lățime petale (cm)|
|----------------------------------------|-------------------|------------------|-------------------|------------------|
|0                                       |5.1                |3.5               |1.4                |0.2               |
|1                                       |4.9                |3.0               |1.4                |0.2               |
|2                                       |4.7                |3.2               |1.3                |0.2               |
|3                                       |4.6                |3.1               |1.5                |0.2               |
|4                                       |5.0                |3.6               |1.4                |0.2               |

- **DataFrame.info**: Pentru început, metoda `info()` este utilizată pentru a afișa un rezumat al conținutului prezent într-un `DataFrame`. Să aruncăm o privire asupra acestui set de date pentru a vedea ce avem:
```python
iris_df.info()
```
```
RangeIndex: 150 entries, 0 to 149
Data columns (total 4 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   sepal length (cm)  150 non-null    float64
 1   sepal width (cm)   150 non-null    float64
 2   petal length (cm)  150 non-null    float64
 3   petal width (cm)   150 non-null    float64
dtypes: float64(4)
memory usage: 4.8 KB
```
Din aceasta, știm că setul de date *Iris* are 150 de intrări în patru coloane, fără valori nule. Toate datele sunt stocate ca numere în virgulă mobilă pe 64 de biți.

- **DataFrame.head()**: Apoi, pentru a verifica conținutul real al `DataFrame`, folosim metoda `head()`. Să vedem cum arată primele câteva rânduri ale `iris_df`:
```python
iris_df.head()
```
```
   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
0                5.1               3.5                1.4               0.2
1                4.9               3.0                1.4               0.2
2                4.7               3.2                1.3               0.2
3                4.6               3.1                1.5               0.2
4                5.0               3.6                1.4               0.2
```
- **DataFrame.tail()**: În mod invers, pentru a verifica ultimele câteva rânduri ale `DataFrame`, folosim metoda `tail()`:
```python
iris_df.tail()
```
```
     sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
145                6.7               3.0                5.2               2.3
146                6.3               2.5                5.0               1.9
147                6.5               3.0                5.2               2.0
148                6.2               3.4                5.4               2.3
149                5.9               3.0                5.1               1.8
```
> **Concluzie:** Chiar și doar privind metadatele despre informațiile dintr-un DataFrame sau primele și ultimele câteva valori din acesta, poți obține o idee imediată despre dimensiunea, forma și conținutul datelor cu care lucrezi.

## Gestionarea Datelor Lipsă
> **Obiectiv de învățare:** La sfârșitul acestei subsecțiuni, ar trebui să știi cum să înlocuiești sau să elimini valorile nule din DataFrames.

De cele mai multe ori, seturile de date pe care vrei să le folosești (sau trebuie să le folosești) au valori lipsă. Modul în care sunt gestionate datele lipsă implică compromisuri subtile care pot afecta analiza finală și rezultatele din lumea reală.

Pandas gestionează valorile lipsă în două moduri. Primul, pe care l-ai văzut înainte în secțiunile anterioare, este `NaN`, sau Not a Number. Acesta este de fapt o valoare specială care face parte din specificația IEEE pentru numere în virgulă mobilă și este utilizată doar pentru a indica valori lipsă de tip virgulă mobilă.

Pentru valorile lipsă, altele decât cele de tip virgulă mobilă, pandas folosește obiectul Python `None`. Deși poate părea confuz să întâlnești două tipuri diferite de valori care spun, în esență, același lucru, există motive programatice solide pentru această alegere de design și, în practică, această abordare permite pandas să ofere un compromis bun pentru marea majoritate a cazurilor. Cu toate acestea, atât `None`, cât și `NaN` au restricții de care trebuie să fii conștient în ceea ce privește modul în care pot fi utilizate.

Află mai multe despre `NaN` și `None` din [notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb)!

- **Detectarea valorilor nule**: În `pandas`, metodele `isnull()` și `notnull()` sunt principalele metode pentru detectarea datelor nule. Ambele returnează măști booleene peste datele tale. Vom folosi `numpy` pentru valorile `NaN`:
```python
import numpy as np

example1 = pd.Series([0, np.nan, '', None])
example1.isnull()
```
```
0    False
1     True
2    False
3     True
dtype: bool
```
Privește cu atenție rezultatul. Te surprinde ceva? Deși `0` este un null aritmetic, este totuși un întreg perfect valid, iar pandas îl tratează ca atare. `''` este puțin mai subtil. Deși l-am folosit în Secțiunea 1 pentru a reprezenta o valoare de șir gol, este totuși un obiect de tip șir și nu o reprezentare a nullului din punctul de vedere al pandas.

Acum, să întoarcem situația și să folosim aceste metode într-un mod mai apropiat de modul în care le vei folosi în practică. Poți folosi măști booleene direct ca index pentru un ``Series`` sau ``DataFrame``, ceea ce poate fi util atunci când încerci să lucrezi cu valori izolate lipsă (sau prezente).

> **Concluzie**: Atât metodele `isnull()` cât și `notnull()` produc rezultate similare atunci când le folosești în `DataFrame`-uri: ele arată rezultatele și indexul acestor rezultate, ceea ce te va ajuta enorm în gestionarea datelor tale.

- **Eliminarea valorilor nule**: Dincolo de identificarea valorilor lipsă, pandas oferă un mijloc convenabil de a elimina valorile nule din `Series` și `DataFrame`-uri. (În special pentru seturi de date mari, este adesea mai recomandabil să elimini pur și simplu valorile lipsă [NA] din analiza ta decât să le gestionezi în alte moduri.) Pentru a vedea acest lucru în acțiune, să revenim la `example1`:
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
Observă că acest lucru ar trebui să arate ca rezultatul tău din `example3[example3.notnull()]`. Diferența aici este că, în loc să indexeze doar valorile mascate, `dropna` a eliminat acele valori lipsă din `Series` `example1`.

Deoarece `DataFrame`-urile au două dimensiuni, ele oferă mai multe opțiuni pentru eliminarea datelor.

```python
example2 = pd.DataFrame([[1,      np.nan, 7], 
                         [2,      5,      8], 
                         [np.nan, 6,      9]])
example2
```
|      | 0 | 1 | 2 |
|------|---|---|---|
|0     |1.0|NaN|7  |
|1     |2.0|5.0|8  |
|2     |NaN|6.0|9  |

(Ai observat că pandas a convertit două dintre coloane în tipuri de date float pentru a acomoda valorile `NaN`?)

Nu poți elimina o singură valoare dintr-un `DataFrame`, așa că trebuie să elimini rânduri sau coloane întregi. În funcție de ceea ce faci, s-ar putea să vrei să faci una sau alta, iar pandas îți oferă opțiuni pentru ambele. Deoarece în știința datelor, coloanele reprezintă de obicei variabile, iar rândurile reprezintă observații, este mai probabil să elimini rânduri de date; setarea implicită pentru `dropna()` este să elimine toate rândurile care conțin orice valori nule:

```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```
Dacă este necesar, poți elimina valorile NA din coloane. Folosește `axis=1` pentru a face acest lucru:
```python
example2.dropna(axis='columns')
```
```
	2
0	7
1	8
2	9
```
Observă că acest lucru poate elimina o mulțime de date pe care s-ar putea să vrei să le păstrezi, în special în seturi de date mai mici. Ce se întâmplă dacă vrei doar să elimini rânduri sau coloane care conțin mai multe sau chiar toate valorile nule? Specifici aceste setări în `dropna` cu parametrii `how` și `thresh`.

Implicit, `how='any'` (dacă vrei să verifici singur sau să vezi ce alți parametri are metoda, rulează `example4.dropna?` într-o celulă de cod). Ai putea specifica alternativ `how='all'` pentru a elimina doar rândurile sau coloanele care conțin toate valorile nule. Să extindem exemplul nostru `DataFrame` pentru a vedea acest lucru în acțiune.

```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

Parametrul `thresh` îți oferă un control mai fin: setezi numărul de valori *non-nule* pe care un rând sau o coloană trebuie să le aibă pentru a fi păstrate:
```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```
Aici, primul și ultimul rând au fost eliminate, deoarece conțin doar două valori non-nule.

- **Completarea valorilor nule**: În funcție de setul tău de date, uneori poate avea mai mult sens să completezi valorile nule cu unele valide decât să le elimini. Ai putea folosi `isnull` pentru a face acest lucru direct, dar acest lucru poate fi laborios, în special dacă ai multe valori de completat. Deoarece aceasta este o sarcină atât de comună în știința datelor, pandas oferă `fillna`, care returnează o copie a `Series` sau `DataFrame` cu valorile lipsă înlocuite cu una aleasă de tine. Să creăm un alt exemplu de `Series` pentru a vedea cum funcționează acest lucru în practică.
```python
example3 = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
example3
```
```
a    1.0
b    NaN
c    2.0
d    NaN
e    3.0
dtype: float64
```
Poți completa toate intrările nule cu o singură valoare, cum ar fi `0`:
```python
example3.fillna(0)
```
```
a    1.0
b    0.0
c    2.0
d    0.0
e    3.0
dtype: float64
```
Poți **completa înainte** valorile nule, adică să folosești ultima valoare validă pentru a completa un null:
```python
example3.fillna(method='ffill')
```
```
a    1.0
b    1.0
c    2.0
d    2.0
e    3.0
dtype: float64
```
De asemenea, poți **completa înapoi** pentru a propaga următoarea valoare validă înapoi pentru a completa un null:
```python
example3.fillna(method='bfill')
```
```
a    1.0
b    2.0
c    2.0
d    3.0
e    3.0
dtype: float64
```
După cum probabil ghicești, acest lucru funcționează la fel cu `DataFrame`-uri, dar poți specifica un `axis` de-a lungul căruia să completezi valorile nule. Luând din nou `example2` utilizat anterior:
```python
example2.fillna(method='ffill', axis=1)
```
```
	0	1	2	3
0	1.0	1.0	7.0	7.0
1	2.0	5.0	8.0	8.0
2	NaN	6.0	9.0	9.0
```
Observă că atunci când o valoare anterioară nu este disponibilă pentru completarea înainte, valoarea nulă rămâne.
> **Concluzie:** Există mai multe moduri de a gestiona valorile lipsă în seturile de date. Strategia specifică pe care o folosești (eliminarea lor, înlocuirea lor sau chiar modul în care le înlocuiești) ar trebui să fie dictată de particularitățile acelui set de date. Vei dezvolta o înțelegere mai bună a modului de a gestiona valorile lipsă pe măsură ce lucrezi și interacționezi mai mult cu seturile de date.

## Eliminarea datelor duplicate

> **Obiectiv de învățare:** La finalul acestei subsecțiuni, ar trebui să te simți confortabil să identifici și să elimini valorile duplicate din DataFrames.

Pe lângă datele lipsă, vei întâlni adesea date duplicate în seturile de date din lumea reală. Din fericire, `pandas` oferă o metodă simplă de detectare și eliminare a intrărilor duplicate.

- **Identificarea duplicatelor: `duplicated`**: Poți identifica cu ușurință valorile duplicate folosind metoda `duplicated` din pandas, care returnează o mască Boolean ce indică dacă o intrare într-un `DataFrame` este un duplicat al uneia anterioare. Să creăm un alt exemplu de `DataFrame` pentru a vedea acest lucru în acțiune.
```python
example4 = pd.DataFrame({'letters': ['A','B'] * 2 + ['B'],
                         'numbers': [1, 2, 1, 3, 3]})
example4
```
|      |litere |numere |
|------|-------|-------|
|0     |A      |1      |
|1     |B      |2      |
|2     |A      |1      |
|3     |B      |3      |
|4     |B      |3      |

```python
example4.duplicated()
```
```
0    False
1    False
2     True
3    False
4     True
dtype: bool
```
- **Eliminarea duplicatelor: `drop_duplicates`:** returnează pur și simplu o copie a datelor pentru care toate valorile `duplicated` sunt `False`:
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
Atât `duplicated`, cât și `drop_duplicates` iau în considerare implicit toate coloanele, dar poți specifica să examineze doar un subset de coloane din `DataFrame`:
```python
example4.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **Concluzie:** Eliminarea datelor duplicate este o parte esențială a aproape fiecărui proiect de știința datelor. Datele duplicate pot modifica rezultatele analizelor tale și pot oferi rezultate inexacte!


## 🚀 Provocare

Toate materialele discutate sunt disponibile ca [Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb). În plus, există exerciții prezente după fiecare secțiune, încearcă-le!

## [Quiz post-lectură](https://ff-quizzes.netlify.app/en/ds/)



## Recapitulare & Studiu Individual

Există multe moduri de a descoperi și aborda pregătirea datelor pentru analiză și modelare, iar curățarea datelor este un pas important care necesită o experiență practică. Încearcă aceste provocări de pe Kaggle pentru a explora tehnici pe care această lecție nu le-a acoperit.

- [Provocare de Curățare a Datelor: Parsarea Datelor](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [Provocare de Curățare a Datelor: Scalare și Normalizare a Datelor](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)


## Temă

[Evaluarea Datelor dintr-un Formular](assignment.md)

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.