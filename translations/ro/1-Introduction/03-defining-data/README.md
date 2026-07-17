# Definirea Datelor

|![ Sketchnote de [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Definirea Datelor - _Sketchnote de [@nitya](https://twitter.com/nitya)_ |

Datele sunt fapte, informații, observații și măsurători folosite pentru a face descoperiri și pentru a susține decizii informate. Un punct de date este o unitate unică de date dintr-un set de date, care este o colecție de puncte de date. Seturile de date pot veni în diferite formate și structuri și vor fi de obicei bazate pe sursa lor, sau de unde provin datele. De exemplu, veniturile lunare ale unei companii pot fi într-un tabel de calcul, dar datele orare privind ritmul cardiac de la un smartwatch pot fi în format [JSON](https://stackoverflow.com/a/383699). Este comun ca oamenii de știință care lucrează cu date să utilizeze diferite tipuri de date în cadrul unui set de date.

Această lecție se concentrează pe identificarea și clasificarea datelor după caracteristicile și sursele lor.

## [Chestionar Pre-Lecție](https://ff-quizzes.netlify.app/en/ds/quiz/4)
## Cum Sunt Descrise Datele

### Date brute
Datele brute sunt date care provin de la sursa lor în starea lor inițială și care nu au fost analizate sau organizate. Pentru a înțelege ce se întâmplă cu un set de date, acesta trebuie organizat într-un format care poate fi înțeles atât de oameni, cât și de tehnologia pe care o pot utiliza pentru a le analiza mai departe. Structura unui set de date descrie modul în care este organizat și poate fi clasificată în structurat, nestructurat și semi-structurat. Aceste tipuri de structuri vor varia în funcție de sursă, dar în cele din urmă se încadrează în aceste trei categorii.

### Date cantitative
Datele cantitative sunt observații numerice într-un set de date și pot fi de obicei analizate, măsurate și folosite matematic. Câteva exemple de date cantitative sunt: populația unei țări, înălțimea unei persoane sau veniturile unei companii pe trimestru. Cu o analiză suplimentară, datele cantitative ar putea fi folosite pentru a descoperi tendințele sezoniere ale Indicele de Calitate a Aerului (AQI) sau pentru a estima probabilitatea traficului în orele de vârf într-o zi obișnuită de lucru.

### Date calitative
Datele calitative, cunoscute și ca date categorice, sunt date care nu pot fi măsurate obiectiv, așa cum sunt observațiile pentru datele cantitative. Ele sunt în general diferite formate de date subiective care surprind calitatea a ceva, cum ar fi un produs sau un proces. Uneori, datele calitative sunt numerice și nu sunt utilizate în mod tipic matematic, cum ar fi numerele de telefon sau timpii înregistrați. Câteva exemple de date calitative sunt: comentarii video, marca și modelul unei mașini sau culoarea preferată a prietenilor apropiați. Datele calitative pot fi folosite pentru a înțelege care produse sunt preferate de consumatori sau pentru a identifica cuvinte cheie populare în CV-urile pentru joburi.

### Date structurate
Datele structurate sunt date organizate în rânduri și coloane, unde fiecare rând are același set de coloane. Coloanele reprezintă o valoare de un anumit tip și vor fi identificate printr-un nume care descrie ce reprezintă valoarea, în timp ce rândurile conțin valorile efective. Coloanele au adesea un set specific de reguli sau restricții asupra valorilor, pentru a asigura că valorile reprezintă cu acuratețe coloana. De exemplu, imaginați-vă un tabel de clienți unde fiecare rând trebuie să aibă un număr de telefon și numerele de telefon nu conțin niciodată caractere alfabetice. Pot exista reguli aplicate coloanei numărului de telefon pentru a asigura că nu este niciodată goală și conține doar cifre.

Un beneficiu al datelor structurate este că pot fi organizate astfel încât să poată fi relaționate cu alte date structurate. Totuși, deoarece datele sunt concepute să fie organizate într-un mod specific, efectuarea de modificări asupra structurii sale generale poate necesita mult efort. De exemplu, adăugarea unei coloane cu email-urile clienților în tabelul de clienți, care să nu poată fi goală, înseamnă că va trebui să găsiți cum să adăugați aceste valori pentru rândurile existente din setul de date.

Exemple de date structurate: tabele de calcul, baze de date relaționale, numere de telefon, extrase bancare

### Date nestrucrate
Datele nestrucrate nu pot fi de obicei categorisite în rânduri sau coloane și nu conțin un format sau un set de reguli de urmat. Deoarece datele nestrucrate au mai puține restricții asupra structurii lor, este mai ușor să se adauge informații noi în comparație cu un set de date structurat. Dacă un senzor care capturează date despre presiunea barometrică la fiecare 2 minute primește o actualizare care îi permite să măsoare și să înregistreze temperatura, nu este necesar să se modifice datele existente dacă sunt nestrucrate. Totuși, acest lucru poate face ca analizarea sau investigarea acestui tip de date să dureze mai mult. De exemplu, un om de știință care vrea să găsească temperatura medie a lunii precedente din datele senzorilor, dar descoperă că senzorul a înregistrat o literă „e” în unele date pentru a nota că a fost defect, în loc de un număr tipic, ceea ce înseamnă că datele sunt incomplete.

Exemple de date nestrucrate: fișiere text, mesaje text, fișiere video

### Semi-structurate
Datele semi-structurate au caracteristici care le fac o combinație între date structurate și nestrucrate. De obicei, nu respectă formatul de rânduri și coloane, dar sunt organizate într-un mod considerat structurat și pot urma un format fix sau un set de reguli. Structura variază între surse, de la o ierarhie bine definită până la ceva mai flexibil care permite integrarea ușoară a unor informații noi. Metadatele sunt indicatori care ajută la decizia modului în care datele sunt organizate și stocate și au diverse denumiri, în funcție de tipul de date. Câteva denumiri comune pentru metadate sunt etichete, elemente, entități și atribute. De exemplu, un mesaj tipic de email va avea un subiect, corp și un set de destinatari și poate fi organizat după cine l-a trimis sau când a fost trimis.

Exemple de date semi-structurate: HTML, fișiere CSV, JavaScript Object Notation (JSON)

## Surse de date

O sursă de date este locația inițială de unde au fost generate datele, sau unde „trăiesc” și va varia în funcție de cum și când au fost colectate. Datele generate de utilizator(i) sunt cunoscute ca date primare, în timp ce datele secundare provin dintr-o sursă care a colectat date pentru uz general. De exemplu, un grup de oameni de știință care colectează observații într-o pădure tropicală ar fi considerați primari, iar dacă decid să le împărtășească altor oameni de știință, acestea ar fi considerate secundare pentru cei care le folosesc.

Bazele de date sunt o sursă comună și se bazează pe un sistem de administrare a bazelor de date pentru a găzdui și menține datele, unde utilizatorii folosesc comenzi numite interogări pentru a explora datele. Fișierele ca surse de date pot fi fișiere audio, imagine și video, precum și tabele de calcul precum Excel. Sursele de internet sunt o locație comună pentru găzduirea datelor, unde pot fi găsite atât baze de date, cât și fișiere. Interfețele de programare a aplicațiilor, cunoscute și ca API-uri, permit programatorilor să creeze modalități de a partaja date cu utilizatori externi prin internet, în timp ce procesul de web scraping extrage date de pe o pagină web. [Lecțiile din Lucrul cu datele](../../../../../../../../../2-Working-With-Data) se concentrează pe cum să se utilizeze diverse surse de date.

## Concluzie

În această lecție am învățat:

- Ce sunt datele
- Cum sunt descrise datele
- Cum sunt clasificate și categorisite datele
- Unde pot fi găsite datele

## 🚀 Provocare

Kaggle este o sursă excelentă de seturi deschise de date. Folosește [instrumentul de căutare a seturilor de date](https://www.kaggle.com/datasets) pentru a găsi câteva seturi interesante și clasifică 3-5 seturi de date conform acestui criteriu:

- Datele sunt cantitative sau calitative?
- Datele sunt structurate, nestrucrate sau semi-structurate?

## [Chestionar Post-lecție](https://ff-quizzes.netlify.app/en/ds/quiz/5)



## Recapitulare și Studiu individual

- Această unitate Microsoft Learn, intitulată [Identificarea formatelor de date](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats?pivots=text) are o descriere detaliată a datelor structurate, semi-structurate și nestrucrate.

## Temă

[Clasificarea seturilor de date](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->