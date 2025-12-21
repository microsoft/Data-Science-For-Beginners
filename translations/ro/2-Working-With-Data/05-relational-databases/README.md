<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11739c7b40e7c6b16ad29e3df4e65862",
  "translation_date": "2025-12-19T12:09:33+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "ro"
}
-->
# Lucrul cu date: baze de date relaționale

|![ Sketchnote de [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Lucrul cu date: baze de date relaționale - _Sketchnote de [@nitya](https://twitter.com/nitya)_ |

Probabil ai folosit în trecut un tabel de calcul pentru a stoca informații. Aveai un set de rânduri și coloane, unde rândurile conțineau informațiile (sau datele), iar coloanele descriau informațiile (uneori numite metadate). O bază de date relațională este construită pe acest principiu de bază al coloanelor și rândurilor în tabele, permițându-ți să ai informații răspândite în mai multe tabele. Acest lucru îți permite să lucrezi cu date mai complexe, să eviți duplicarea și să ai flexibilitate în modul în care explorezi datele. Să explorăm conceptele unei baze de date relaționale.

## [Chestionar pre-lectură](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## Totul începe cu tabele

O bază de date relațională are în centrul său tabele. La fel ca în cazul unui tabel de calcul, un tabel este o colecție de coloane și rânduri. Rândul conține datele sau informațiile cu care dorim să lucrăm, cum ar fi numele unui oraș sau cantitatea de precipitații. Coloanele descriu datele pe care le stochează.

Să începem explorarea noastră prin crearea unui tabel pentru a stoca informații despre orașe. Am putea începe cu numele și țara lor. Ai putea stoca asta într-un tabel astfel:

| Oraș     | Țară          |
| -------- | ------------- |
| Tokyo    | Japonia       |
| Atlanta  | Statele Unite |
| Auckland | Noua Zeelandă |

Observă că numele coloanelor **oraș**, **țară** și **populație** descriu datele stocate, iar fiecare rând conține informații despre un oraș.

## Limitările abordării cu un singur tabel

Probabil că tabelul de mai sus îți pare relativ familiar. Să începem să adăugăm date suplimentare în baza noastră de date în creștere - precipitațiile anuale (în milimetri). Ne vom concentra pe anii 2018, 2019 și 2020. Dacă am adăuga date pentru Tokyo, ar putea arăta cam așa:

| Oraș  | Țară   | An   | Cantitate |
| ----- | ------ | ---- | --------- |
| Tokyo | Japonia| 2020 | 1690      |
| Tokyo | Japonia| 2019 | 1874      |
| Tokyo | Japonia| 2018 | 1445      |

Ce observi la tabelul nostru? Poți observa că duplicăm numele și țara orașului iar și iar. Acest lucru ar putea ocupa destul spațiu de stocare și este în mare parte inutil să avem mai multe copii. La urma urmei, Tokyo are un singur nume care ne interesează.

OK, să încercăm altceva. Să adăugăm coloane noi pentru fiecare an:

| Oraș     | Țară          | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Japonia       | 1445 | 1874 | 1690 |
| Atlanta  | Statele Unite | 1779 | 1111 | 1683 |
| Auckland | Noua Zeelandă | 1386 | 942  | 1176 |

Deși acest lucru evită duplicarea rândurilor, adaugă câteva alte provocări. Ar trebui să modificăm structura tabelului de fiecare dată când apare un an nou. În plus, pe măsură ce datele cresc, având anii ca și coloane va face mai dificilă extragerea și calcularea valorilor.

De aceea avem nevoie de mai multe tabele și relații. Prin împărțirea datelor putem evita duplicarea și avem mai multă flexibilitate în modul în care lucrăm cu datele.

## Conceptele relațiilor

Să ne întoarcem la datele noastre și să decidem cum vrem să le împărțim. Știm că vrem să stocăm numele și țara pentru orașele noastre, deci cel mai probabil acestea vor funcționa cel mai bine într-un singur tabel.

| Oraș     | Țară          |
| -------- | ------------- |
| Tokyo    | Japonia       |
| Atlanta  | Statele Unite |
| Auckland | Noua Zeelandă |

Dar înainte să creăm următorul tabel, trebuie să găsim o modalitate de a face referire la fiecare oraș. Avem nevoie de o formă de identificator, ID sau (în termeni tehnici de baze de date) o cheie primară. O cheie primară este o valoare folosită pentru a identifica un rând specific într-un tabel. Deși aceasta ar putea fi bazată pe o valoare în sine (am putea folosi numele orașului, de exemplu), ar trebui aproape întotdeauna să fie un număr sau alt identificator. Nu vrem ca id-ul să se schimbe vreodată deoarece ar rupe relația. Vei observa că în majoritatea cazurilor cheia primară sau id-ul va fi un număr generat automat.

> ✅ Cheia primară este frecvent prescurtată ca PK

### cities

| city_id | Oraș     | Țară          |
| ------- | -------- | ------------- |
| 1       | Tokyo    | Japonia       |
| 2       | Atlanta  | Statele Unite |
| 3       | Auckland | Noua Zeelandă |

> ✅ Vei observa că folosim termenii "id" și "cheie primară" interschimbabil în această lecție. Conceptele aici se aplică și DataFrame-urilor, pe care le vei explora mai târziu. DataFrame-urile nu folosesc terminologia de "cheie primară", însă vei observa că se comportă în mod similar.

Cu tabelul nostru de orașe creat, să stocăm precipitațiile. În loc să duplicăm informațiile complete despre oraș, putem folosi id-ul. De asemenea, ar trebui să ne asigurăm că noul tabel creat are o coloană *id*, deoarece toate tabelele ar trebui să aibă un id sau o cheie primară.

### rainfall

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

Observă coloana **city_id** din noul tabel **rainfall**. Această coloană conține valori care fac referire la ID-urile din tabelul **cities**. În termeni tehnici de date relaționale, aceasta se numește **cheie externă**; este o cheie primară dintr-un alt tabel. Poți să te gândești la ea ca la o referință sau un pointer. **city_id** 1 face referire la Tokyo.

> [!NOTE] 
> Cheia externă este frecvent prescurtată ca FK

## Extragearea datelor

Cu datele noastre separate în două tabele, te-ai putea întreba cum le extragem. Dacă folosim o bază de date relațională precum MySQL, SQL Server sau Oracle, putem folosi un limbaj numit Structured Query Language sau SQL. SQL (uneori pronunțat sequel) este un limbaj standard folosit pentru a extrage și modifica date într-o bază de date relațională.

Pentru a extrage date folosești comanda `SELECT`. În esență, **selectezi** coloanele pe care vrei să le vezi **din** tabelul în care sunt conținute. Dacă ai vrea să afișezi doar numele orașelor, ai putea folosi următorul cod:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` este locul unde listezi coloanele, iar `FROM` este locul unde listezi tabelele.

> [!NOTE] 
> Sintaxa SQL nu ține cont de majuscule, ceea ce înseamnă că `select` și `SELECT` înseamnă același lucru. Totuși, în funcție de tipul bazei de date pe care o folosești, coloanele și tabelele pot fi sensibile la majuscule. Ca urmare, este o bună practică să tratezi totul în programare ca fiind sensibil la majuscule. Când scrii interogări SQL, convenția comună este să pui cuvintele cheie cu majuscule.

Interogarea de mai sus va afișa toate orașele. Să ne imaginăm că vrem să afișăm doar orașele din Noua Zeelandă. Avem nevoie de o formă de filtru. Cuvântul cheie SQL pentru asta este `WHERE`, sau "unde ceva este adevărat".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Îmbinarea datelor

Până acum am extras date dintr-un singur tabel. Acum vrem să aducem datele împreună din ambele tabele **cities** și **rainfall**. Acest lucru se face prin *îmbinare* (join). Practic vei crea o legătură între cele două tabele și vei potrivi valorile dintr-o coloană din fiecare tabel.

În exemplul nostru, vom potrivi coloana **city_id** din **rainfall** cu coloana **city_id** din **cities**. Aceasta va asocia valoarea precipitațiilor cu orașul respectiv. Tipul de îmbinare pe care îl vom face se numește *inner* join, ceea ce înseamnă că dacă vreun rând nu se potrivește cu nimic din celălalt tabel, nu va fi afișat. În cazul nostru, fiecare oraș are precipitații, deci totul va fi afișat.

Să extragem precipitațiile pentru 2019 pentru toate orașele noastre.

Vom face asta în pași. Primul pas este să îmbinăm datele indicând coloanele pentru legătură - **city_id** așa cum am evidențiat mai devreme.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Am evidențiat cele două coloane pe care le vrem și faptul că vrem să îmbinăm tabelele prin **city_id**. Acum putem adăuga declarația `WHERE` pentru a filtra doar anul 2019.

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

Bazele de date relaționale se concentrează pe împărțirea informațiilor între mai multe tabele care apoi sunt reunite pentru afișare și analiză. Acest lucru oferă un grad ridicat de flexibilitate pentru a efectua calcule și alte manipulări ale datelor. Ai văzut conceptele de bază ale unei baze de date relaționale și cum să faci o îmbinare între două tabele.

## 🚀 Provocare

Există numeroase baze de date relaționale disponibile pe internet. Poți explora datele folosind abilitățile pe care le-ai învățat mai sus.

## Chestionar post-lectură

## [Chestionar post-lectură](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Recapitulare & Studiu individual

Există mai multe resurse disponibile pe [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) pentru a-ți continua explorarea SQL și a conceptelor bazelor de date relaționale

- [Descrierea conceptelor datelor relaționale](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Începe să interoghezi cu Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL este o versiune de SQL)
- [Conținut SQL pe Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Temă

[Afisarea datelor aeroportului](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->