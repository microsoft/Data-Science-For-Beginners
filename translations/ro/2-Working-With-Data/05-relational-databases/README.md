<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "870a0086adbc313a8eea5489bdcb2522",
  "translation_date": "2025-08-26T14:31:04+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "ro"
}
-->
# Lucrul cu Date: Baze de Date Relaționale

|![ Sketchnote de [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Lucrul cu Date: Baze de Date Relaționale - _Sketchnote de [@nitya](https://twitter.com/nitya)_ |

Probabil ai folosit un tabel în trecut pentru a stoca informații. Aveai un set de rânduri și coloane, unde rândurile conțineau informațiile (sau datele), iar coloanele descriau informațiile (uneori numite metadate). O bază de date relațională se bazează pe acest principiu de bază al coloanelor și rândurilor din tabele, permițându-ți să ai informații distribuite pe mai multe tabele. Acest lucru îți permite să lucrezi cu date mai complexe, să eviți duplicarea și să ai flexibilitate în modul în care explorezi datele. Haide să explorăm conceptele unei baze de date relaționale.

## [Chestionar înainte de lecție](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/8)

## Totul începe cu tabele

O bază de date relațională are la bază tabele. La fel ca în cazul unui tabel, un tabel este o colecție de coloane și rânduri. Rândul conține datele sau informațiile cu care dorim să lucrăm, cum ar fi numele unui oraș sau cantitatea de precipitații. Coloanele descriu datele pe care le stochează.

Să începem explorarea noastră prin crearea unui tabel pentru a stoca informații despre orașe. Am putea începe cu numele și țara lor. Ai putea stoca aceste informații într-un tabel astfel:

| Oraș     | Țară          |
| -------- | ------------- |
| Tokyo    | Japonia       |
| Atlanta  | Statele Unite |
| Auckland | Noua Zeelandă |

Observă că numele coloanelor **oraș**, **țară** și **populație** descriu datele stocate, iar fiecare rând conține informații despre un oraș.

## Limitările abordării cu un singur tabel

Probabil că tabelul de mai sus îți pare destul de familiar. Să începem să adăugăm niște date suplimentare în baza noastră de date în formare - precipitațiile anuale (în milimetri). Ne vom concentra pe anii 2018, 2019 și 2020. Dacă ar fi să le adăugăm pentru Tokyo, ar putea arăta astfel:

| Oraș  | Țară    | An   | Cantitate |
| ----- | ------- | ---- | --------- |
| Tokyo | Japonia | 2020 | 1690      |
| Tokyo | Japonia | 2019 | 1874      |
| Tokyo | Japonia | 2018 | 1445      |

Ce observi la tabelul nostru? Poți observa că duplicăm numele și țara orașului de mai multe ori. Acest lucru ar putea ocupa destul de mult spațiu de stocare și este în mare parte inutil să avem mai multe copii. La urma urmei, Tokyo are doar un singur nume care ne interesează.

OK, să încercăm altceva. Să adăugăm noi coloane pentru fiecare an:

| Oraș     | Țară          | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Japonia       | 1445 | 1874 | 1690 |
| Atlanta  | Statele Unite | 1779 | 1111 | 1683 |
| Auckland | Noua Zeelandă | 1386 | 942  | 1176 |

Deși acest lucru evită duplicarea rândurilor, adaugă alte câteva provocări. Ar trebui să modificăm structura tabelului de fiecare dată când apare un nou an. În plus, pe măsură ce datele noastre cresc, având anii ca și coloane va face mai dificilă recuperarea și calcularea valorilor.

De aceea avem nevoie de mai multe tabele și relații. Prin împărțirea datelor noastre putem evita duplicarea și avem mai multă flexibilitate în modul în care lucrăm cu datele.

## Conceptele relațiilor

Să revenim la datele noastre și să determinăm cum dorim să le împărțim. Știm că vrem să stocăm numele și țara orașelor noastre, așa că acest lucru va funcționa probabil cel mai bine într-un singur tabel.

| Oraș     | Țară          |
| -------- | ------------- |
| Tokyo    | Japonia       |
| Atlanta  | Statele Unite |
| Auckland | Noua Zeelandă |

Dar înainte de a crea următorul tabel, trebuie să ne dăm seama cum să referim fiecare oraș. Avem nevoie de o formă de identificator, ID sau (în termeni tehnici de baze de date) o cheie primară. O cheie primară este o valoare utilizată pentru a identifica un rând specific într-un tabel. Deși aceasta ar putea fi bazată pe o valoare în sine (am putea folosi numele orașului, de exemplu), ar trebui să fie aproape întotdeauna un număr sau alt identificator. Nu vrem ca ID-ul să se schimbe vreodată, deoarece ar rupe relația. Vei observa că, în cele mai multe cazuri, cheia primară sau ID-ul va fi un număr generat automat.

> ✅ Cheia primară este frecvent abreviată ca PK

### orașe

| city_id | Oraș     | Țară          |
| ------- | -------- | ------------- |
| 1       | Tokyo    | Japonia       |
| 2       | Atlanta  | Statele Unite |
| 3       | Auckland | Noua Zeelandă |

> ✅ Vei observa că folosim termenii "id" și "cheie primară" interschimbabil în timpul acestei lecții. Conceptele de aici se aplică și la DataFrames, pe care le vei explora mai târziu. DataFrames nu folosesc terminologia de "cheie primară", însă vei observa că se comportă în mod similar.

Cu tabelul nostru de orașe creat, să stocăm precipitațiile. În loc să duplicăm informațiile complete despre oraș, putem folosi ID-ul. De asemenea, ar trebui să ne asigurăm că tabelul nou creat are o coloană *id*, deoarece toate tabelele ar trebui să aibă un ID sau o cheie primară.

### precipitații

| rainfall_id | city_id | An   | Cantitate |
| ----------- | ------- | ---- | --------- |
| 1           | 1       | 2018 | 1445      |
| 2           | 1       | 2019 | 1874      |
| 3           | 1       | 2020 | 1690      |
| 4           | 2       | 2018 | 1779      |
| 5           | 2       | 2019 | 1111      |
| 6           | 2       | 2020 | 1683      |
| 7           | 3       | 2018 | 1386      |
| 8           | 3       | 2019 | 942       |
| 9           | 3       | 2020 | 1176      |

Observă coloana **city_id** din tabelul nou creat **precipitații**. Această coloană conține valori care fac referire la ID-urile din tabelul **orașe**. În termeni tehnici de date relaționale, aceasta se numește **cheie străină**; este o cheie primară din alt tabel. Poți să o consideri pur și simplu ca o referință sau un indicator. **city_id** 1 face referire la Tokyo.

> [!NOTE] Cheia străină este frecvent abreviată ca FK

## Recuperarea datelor

Cu datele noastre separate în două tabele, te-ai putea întreba cum le recuperăm. Dacă folosim o bază de date relațională precum MySQL, SQL Server sau Oracle, putem folosi un limbaj numit Structured Query Language sau SQL. SQL (uneori pronunțat "sequel") este un limbaj standard utilizat pentru a recupera și modifica datele dintr-o bază de date relațională.

Pentru a recupera datele, folosești comanda `SELECT`. În esență, **selectezi** coloanele pe care vrei să le vezi **din** tabelul în care sunt conținute. Dacă ai vrea să afișezi doar numele orașelor, ai putea folosi următorul:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` este locul unde listezi coloanele, iar `FROM` este locul unde listezi tabelele.

> [NOTE] Sintaxa SQL este insensibilă la majuscule, ceea ce înseamnă că `select` și `SELECT` înseamnă același lucru. Totuși, în funcție de tipul de bază de date pe care îl folosești, coloanele și tabelele ar putea fi sensibile la majuscule. Ca rezultat, este o bună practică să tratezi întotdeauna totul în programare ca fiind sensibil la majuscule. Când scrii interogări SQL, convenția comună este să pui cuvintele cheie în litere mari.

Interogarea de mai sus va afișa toate orașele. Să ne imaginăm că vrem să afișăm doar orașele din Noua Zeelandă. Avem nevoie de o formă de filtru. Cuvântul cheie SQL pentru aceasta este `WHERE`, sau "unde ceva este adevărat".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Îmbinarea datelor

Până acum am recuperat date dintr-un singur tabel. Acum vrem să aducem datele împreună din **orașe** și **precipitații**. Acest lucru se face prin *îmbinarea* lor. Practic vei crea o legătură între cele două tabele și vei potrivi valorile dintr-o coloană din fiecare tabel.

În exemplul nostru, vom potrivi coloana **city_id** din **precipitații** cu coloana **city_id** din **orașe**. Acest lucru va potrivi valoarea precipitațiilor cu orașul său respectiv. Tipul de îmbinare pe care îl vom efectua se numește *îmbinare internă*, ceea ce înseamnă că, dacă vreun rând nu se potrivește cu nimic din celălalt tabel, nu va fi afișat. În cazul nostru, fiecare oraș are precipitații, deci totul va fi afișat.

Să recuperăm precipitațiile din 2019 pentru toate orașele noastre.

Vom face acest lucru în pași. Primul pas este să îmbinăm datele împreună indicând coloanele pentru legătură - **city_id**, așa cum am subliniat mai devreme.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Am subliniat cele două coloane pe care le dorim și faptul că vrem să îmbinăm tabelele împreună prin **city_id**. Acum putem adăuga declarația `WHERE` pentru a filtra doar anul 2019.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
WHERE rainfall.year = 2019

-- Output

-- city     | amount
-- -------- | ------
-- Tokyo    | 1874
-- Atlanta  | 1111
-- Auckland |  942
```

## Rezumat

Baze de date relaționale se concentrează pe împărțirea informațiilor între mai multe tabele, care sunt apoi reunite pentru afișare și analiză. Acest lucru oferă un grad ridicat de flexibilitate pentru a efectua calcule și pentru a manipula datele. Ai văzut conceptele de bază ale unei baze de date relaționale și cum să efectuezi o îmbinare între două tabele.

## 🚀 Provocare

Există numeroase baze de date relaționale disponibile pe internet. Poți explora datele folosind abilitățile pe care le-ai învățat mai sus.

## Chestionar după lecție

## [Chestionar după lecție](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/9)

## Recapitulare & Studiu Individual

Există mai multe resurse disponibile pe [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) pentru a-ți continua explorarea conceptelor SQL și de baze de date relaționale:

- [Descrie conceptele datelor relaționale](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Începe să interoghezi cu Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL este o versiune de SQL)
- [Conținut SQL pe Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Temă

[Titlul Temei](assignment.md)

---

**Declinarea responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.