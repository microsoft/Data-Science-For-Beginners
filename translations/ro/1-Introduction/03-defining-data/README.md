<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "12339119c0165da569a93ddba05f9339",
  "translation_date": "2025-09-05T18:32:53+00:00",
  "source_file": "1-Introduction/03-defining-data/README.md",
  "language_code": "ro"
}
-->
# Definirea Datelor

|![ Sketchnote de [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Definirea Datelor - _Sketchnote de [@nitya](https://twitter.com/nitya)_ |

Datele reprezintă fapte, informații, observații și măsurători utilizate pentru a face descoperiri și pentru a susține deciziile informate. Un punct de date este o unitate individuală de date dintr-un set de date, care este o colecție de puncte de date. Seturile de date pot avea formate și structuri diferite și, de obicei, se bazează pe sursa lor sau pe locul de unde provin datele. De exemplu, câștigurile lunare ale unei companii ar putea fi într-un fișier Excel, în timp ce datele despre ritmul cardiac orar de la un smartwatch ar putea fi în format [JSON](https://stackoverflow.com/a/383699). Este obișnuit ca oamenii de știință în domeniul datelor să lucreze cu diferite tipuri de date într-un set de date.

Această lecție se concentrează pe identificarea și clasificarea datelor în funcție de caracteristicile și sursele lor.

## [Chestionar înainte de lecție](https://ff-quizzes.netlify.app/en/ds/quiz/4)

## Cum sunt descrise datele

### Date brute
Datele brute sunt date care provin din sursa lor în starea inițială și nu au fost analizate sau organizate. Pentru a înțelege ce se întâmplă cu un set de date, acesta trebuie organizat într-un format care să poată fi înțeles atât de oameni, cât și de tehnologia pe care aceștia o pot folosi pentru a-l analiza mai departe. Structura unui set de date descrie modul în care este organizat și poate fi clasificată ca fiind structurată, nestructurată sau semi-structurată. Aceste tipuri de structuri vor varia în funcție de sursă, dar în cele din urmă se vor încadra în aceste trei categorii.

### Date cantitative
Datele cantitative sunt observații numerice dintr-un set de date și, de obicei, pot fi analizate, măsurate și utilizate matematic. Câteva exemple de date cantitative sunt: populația unei țări, înălțimea unei persoane sau câștigurile trimestriale ale unei companii. Cu o analiză suplimentară, datele cantitative ar putea fi utilizate pentru a descoperi tendințe sezoniere ale Indicelui de Calitate a Aerului (AQI) sau pentru a estima probabilitatea traficului la orele de vârf într-o zi obișnuită de lucru.

### Date calitative
Datele calitative, cunoscute și sub denumirea de date categorice, sunt date care nu pot fi măsurate obiectiv, precum observațiile datelor cantitative. În general, acestea sunt diverse formate de date subiective care surprind calitatea unui produs sau proces. Uneori, datele calitative sunt numerice, dar nu ar fi utilizate în mod obișnuit matematic, cum ar fi numerele de telefon sau marcajele temporale. Câteva exemple de date calitative sunt: comentarii video, marca și modelul unei mașini sau culoarea preferată a celui mai bun prieten. Datele calitative ar putea fi utilizate pentru a înțelege care produse sunt cele mai apreciate de consumatori sau pentru a identifica cuvinte-cheie populare în CV-urile pentru aplicații de joburi.

### Date structurate
Datele structurate sunt date organizate în rânduri și coloane, unde fiecare rând va avea același set de coloane. Coloanele reprezintă o valoare de un anumit tip și vor fi identificate printr-un nume care descrie ce reprezintă valoarea, în timp ce rândurile conțin valorile propriu-zise. Coloanele vor avea adesea un set specific de reguli sau restricții asupra valorilor, pentru a se asigura că valorile reprezintă corect coloana. De exemplu, imaginați-vă un fișier Excel cu clienți, unde fiecare rând trebuie să aibă un număr de telefon, iar numerele de telefon nu conțin caractere alfabetice. Pot exista reguli aplicate coloanei de număr de telefon pentru a se asigura că aceasta nu este niciodată goală și conține doar numere.

Un avantaj al datelor structurate este că pot fi organizate astfel încât să fie relaționate cu alte date structurate. Totuși, deoarece datele sunt concepute pentru a fi organizate într-un mod specific, modificarea structurii generale poate necesita mult efort. De exemplu, adăugarea unei coloane de e-mail în fișierul Excel al clienților care nu poate fi goală înseamnă că va trebui să găsiți o modalitate de a adăuga aceste valori la rândurile existente ale clienților din setul de date.

Exemple de date structurate: fișiere Excel, baze de date relaționale, numere de telefon, extrase bancare.

### Date nestructurate
Datele nestructurate, de obicei, nu pot fi categorisite în rânduri sau coloane și nu conțin un format sau un set de reguli de urmat. Deoarece datele nestructurate au mai puține restricții asupra structurii lor, este mai ușor să adăugați informații noi în comparație cu un set de date structurat. Dacă un senzor care captează date despre presiunea barometrică la fiecare 2 minute a primit o actualizare care îi permite acum să măsoare și să înregistreze temperatura, nu este necesar să modificați datele existente dacă acestea sunt nestructurate. Totuși, acest lucru poate face ca analiza sau investigarea acestui tip de date să dureze mai mult. De exemplu, un om de știință care dorește să găsească temperatura medie a lunii precedente din datele senzorului, dar descoperă că senzorul a înregistrat un "e" în unele dintre datele sale pentru a nota că era defect, în loc de un număr obișnuit, ceea ce înseamnă că datele sunt incomplete.

Exemple de date nestructurate: fișiere text, mesaje text, fișiere video.

### Date semi-structurate
Datele semi-structurate au caracteristici care le fac o combinație între date structurate și nestructurate. De obicei, nu se conformează unui format de rânduri și coloane, dar sunt organizate într-un mod considerat structurat și pot urma un format fix sau un set de reguli. Structura va varia între surse, cum ar fi o ierarhie bine definită sau ceva mai flexibil care permite integrarea ușoară a informațiilor noi. Metadatele sunt indicatori care ajută la deciderea modului în care datele sunt organizate și stocate și vor avea diverse denumiri, în funcție de tipul de date. Câteva denumiri comune pentru metadate sunt etichete, elemente, entități și atribute. De exemplu, un mesaj tipic de e-mail va avea un subiect, un corp și un set de destinatari și poate fi organizat în funcție de cine sau când a fost trimis.

Exemple de date semi-structurate: HTML, fișiere CSV, JavaScript Object Notation (JSON).

## Surse de date

O sursă de date este locația inițială de unde au fost generate datele sau unde "trăiesc" și va varia în funcție de modul și momentul în care au fost colectate. Datele generate de utilizator(i) sunt cunoscute ca date primare, în timp ce datele secundare provin dintr-o sursă care a colectat date pentru utilizare generală. De exemplu, un grup de oameni de știință care colectează observații într-o pădure tropicală ar fi considerat primar, iar dacă decid să le împărtășească altor oameni de știință, acestea ar fi considerate secundare pentru cei care le utilizează.

Baze de date sunt o sursă comună și se bazează pe un sistem de gestionare a bazelor de date pentru a găzdui și menține datele, unde utilizatorii folosesc comenzi numite interogări pentru a explora datele. Fișierele ca surse de date pot fi fișiere audio, imagine și video, precum și fișiere Excel. Sursele de internet sunt o locație comună pentru găzduirea datelor, unde pot fi găsite atât baze de date, cât și fișiere. Interfețele de programare a aplicațiilor, cunoscute și sub denumirea de API-uri, permit programatorilor să creeze modalități de a partaja date cu utilizatori externi prin internet, în timp ce procesul de web scraping extrage date de pe o pagină web. [Lecțiile din Lucrul cu Date](../../../../../../../../../2-Working-With-Data) se concentrează pe modul de utilizare a diferitelor surse de date.

## Concluzie

În această lecție am învățat:

- Ce sunt datele
- Cum sunt descrise datele
- Cum sunt clasificate și categorisite datele
- Unde pot fi găsite datele

## 🚀 Provocare

Kaggle este o sursă excelentă de seturi de date deschise. Folosiți [instrumentul de căutare a seturilor de date](https://www.kaggle.com/datasets) pentru a găsi câteva seturi de date interesante și clasificați 3-5 seturi de date conform acestui criteriu:

- Datele sunt cantitative sau calitative?
- Datele sunt structurate, nestructurate sau semi-structurate?

## [Chestionar după lecție](https://ff-quizzes.netlify.app/en/ds/quiz/5)

## Recapitulare și Studiu Individual

- Această unitate Microsoft Learn, intitulată [Clasificarea Datelor](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/2-classify-data), oferă o descriere detaliată a datelor structurate, semi-structurate și nestructurate.

## Temă

[Clasificarea Seturilor de Date](assignment.md)

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.