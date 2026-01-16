<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "43212cc1ac137b7bb1dcfb37ca06b0f4",
  "translation_date": "2025-10-25T19:06:43+00:00",
  "source_file": "1-Introduction/01-defining-data-science/README.md",
  "language_code": "ro"
}
-->
# Definirea Științei Datelor

| ![ Schiță de [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/01-Definitions.png) |
| :----------------------------------------------------------------------------------------------------: |
|              Definirea Științei Datelor - _Schiță de [@nitya](https://twitter.com/nitya)_               |

---

[![Video despre Definirea Științei Datelor](../../../../translated_images/ro/video-def-ds.6623ee2392ef1abf6d7faf3fad10a4163642811749da75f44e35a5bb121de15c.png)](https://youtu.be/beZ7Mb_oz9I)

## [Chestionar înainte de curs](https://ff-quizzes.netlify.app/en/ds/quiz/0)

## Ce este Datele?
În viața noastră de zi cu zi, suntem înconjurați constant de date. Textul pe care îl citești acum este o dată. Lista de numere de telefon ale prietenilor tăi din smartphone-ul tău este o dată, la fel ca ora curentă afișată pe ceasul tău. Ca ființe umane, operăm în mod natural cu date, numărând banii pe care îi avem sau scriind scrisori prietenilor noștri.

Totuși, datele au devenit mult mai importante odată cu apariția calculatoarelor. Rolul principal al calculatoarelor este de a efectua calcule, dar ele au nevoie de date pentru a funcționa. Astfel, trebuie să înțelegem cum stochează și procesează calculatoarele datele.

Odată cu apariția internetului, rolul calculatoarelor ca dispozitive de gestionare a datelor a crescut. Dacă te gândești, acum folosim calculatoarele din ce în ce mai mult pentru procesarea și comunicarea datelor, mai degrabă decât pentru calcule propriu-zise. Când scriem un e-mail unui prieten sau căutăm informații pe internet - practic creăm, stocăm, transmitem și manipulăm date.
> Îți amintești ultima dată când ai folosit calculatoarele pentru a calcula efectiv ceva?

## Ce este Știința Datelor?

În [Wikipedia](https://en.wikipedia.org/wiki/Data_science), **Știința Datelor** este definită ca *un domeniu științific care utilizează metode științifice pentru a extrage cunoștințe și perspective din date structurate și nestructurate și pentru a aplica cunoștințele și perspectivele acționabile din date într-o gamă largă de domenii de aplicare*.

Această definiție subliniază următoarele aspecte importante ale științei datelor:

* Scopul principal al științei datelor este **extracția cunoștințelor** din date, cu alte cuvinte - **înțelegerea** datelor, găsirea unor relații ascunse și construirea unui **model**.
* Știința datelor utilizează **metode științifice**, cum ar fi probabilitatea și statistica. De fapt, când termenul *știința datelor* a fost introdus pentru prima dată, unii oameni au susținut că știința datelor era doar un nume nou și sofisticat pentru statistică. În prezent, este evident că domeniul este mult mai larg.
* Cunoștințele obținute ar trebui aplicate pentru a produce **perspective acționabile**, adică perspective practice pe care le poți aplica în situații reale de afaceri.
* Ar trebui să fim capabili să operăm atât pe date **structurate**, cât și pe date **nestructurate**. Vom reveni să discutăm diferite tipuri de date mai târziu în curs.
* **Domeniul de aplicare** este un concept important, iar oamenii de știință în domeniul datelor au nevoie adesea de un anumit grad de expertiză în domeniul problemei, de exemplu: finanțe, medicină, marketing etc.

> Un alt aspect important al Științei Datelor este că studiază modul în care datele pot fi colectate, stocate și operate folosind calculatoare. În timp ce statistica ne oferă fundamentele matematice, știința datelor aplică concepte matematice pentru a obține efectiv perspective din date.

Unul dintre modurile (atribuit lui [Jim Gray](https://en.wikipedia.org/wiki/Jim_Gray_(computer_scientist))) de a privi știința datelor este să o considerăm un paradigm separat al științei:
* **Empiric**, în care ne bazăm în principal pe observații și rezultatele experimentelor
* **Teoretic**, unde apar concepte noi din cunoștințele științifice existente
* **Computațional**, unde descoperim principii noi bazate pe unele experimente computaționale
* **Bazat pe date**, bazat pe descoperirea relațiilor și modelelor în date  

## Alte Domenii Conexe

Deoarece datele sunt omniprezente, știința datelor este, de asemenea, un domeniu vast, care atinge multe alte discipline.

<dl>
<dt>Baze de date</dt>
<dd>
O considerație critică este <b>cum să stocăm</b> datele, adică cum să le structurăm într-un mod care să permită procesarea mai rapidă. Există diferite tipuri de baze de date care stochează date structurate și nestructurate, pe care <a href="../../2-Working-With-Data/README.md">le vom analiza în cursul nostru</a>.
</dd>
<dt>Big Data</dt>
<dd>
Adesea trebuie să stocăm și să procesăm cantități foarte mari de date cu o structură relativ simplă. Există abordări și instrumente speciale pentru a stoca acele date într-un mod distribuit pe un cluster de calculatoare și pentru a le procesa eficient.
</dd>
<dt>Învățare Automată</dt>
<dd>
Un mod de a înțelege datele este să <b>construim un model</b> care să poată prezice un rezultat dorit. Dezvoltarea modelelor din date se numește <b>învățare automată</b>. Poți consulta <a href="https://aka.ms/ml-beginners">Curriculumul nostru de Învățare Automată pentru Începători</a> pentru a afla mai multe despre acest subiect.
</dd>
<dt>Inteligență Artificială</dt>
<dd>
Un domeniu al învățării automate cunoscut sub numele de inteligență artificială (IA) se bazează, de asemenea, pe date și implică construirea de modele de complexitate ridicată care imită procesele de gândire umană. Metodele IA ne permit adesea să transformăm datele nestructurate (de exemplu, limbajul natural) în perspective structurate.
</dd>
<dt>Vizualizare</dt>
<dd>
Cantitățile mari de date sunt greu de înțeles pentru o ființă umană, dar odată ce creăm vizualizări utile folosind acele date, putem înțelege mai bine datele și putem trage concluzii. Astfel, este important să cunoaștem multe moduri de a vizualiza informațiile - ceva ce vom acoperi în <a href="../../3-Data-Visualization/README.md">Secțiunea 3</a> a cursului nostru. Domeniile conexe includ, de asemenea, <b>Infografice</b> și <b>Interacțiunea Om-Calculator</b> în general.
</dd>
</dl>

## Tipuri de Date

Așa cum am menționat deja, datele sunt peste tot. Trebuie doar să le captăm în mod corespunzător! Este util să facem diferența între datele **structurate** și cele **nestructurate**. Primele sunt de obicei reprezentate într-o formă bine structurată, adesea sub formă de tabel sau mai multe tabele, în timp ce celelalte sunt doar o colecție de fișiere. Uneori putem vorbi și despre date **semi-structurate**, care au un fel de structură ce poate varia considerabil.

| Structurate                                                                   | Semi-structurate                                                                                | Nestructurate                            |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------- |
| Lista persoanelor cu numerele lor de telefon                                  | Pagini Wikipedia cu linkuri                                                                    | Textul Enciclopediei Britannica         |
| Temperatura din toate camerele unei clădiri la fiecare minut din ultimii 20 de ani | Colecția de lucrări științifice în format JSON cu autori, data publicării și rezumat           | Flux video brut de la o cameră de supraveghere |
| Date despre vârsta și genul tuturor persoanelor care intră în clădire         | Pagini de internet                                                                             | Documente corporative într-un folder    |

## De unde să obții Date

Există multe surse posibile de date, și ar fi imposibil să le enumerăm pe toate! Totuși, să menționăm câteva dintre locurile tipice de unde poți obține date:

* **Structurate**
  - **Internetul Lucrurilor** (IoT), inclusiv date de la diferiți senzori, cum ar fi senzori de temperatură sau presiune, oferă o mulțime de date utile. De exemplu, dacă o clădire de birouri este echipată cu senzori IoT, putem controla automat încălzirea și iluminatul pentru a minimiza costurile.
  - **Chestionare** pe care le cerem utilizatorilor să le completeze după o achiziție sau după vizitarea unui site web.
  - **Analiza comportamentului** poate, de exemplu, să ne ajute să înțelegem cât de profund explorează un utilizator un site și care este motivul tipic pentru care părăsește site-ul.
* **Nestructurate**
  - **Texte** pot fi o sursă bogată de perspective, cum ar fi un **scor de sentiment** general sau extragerea de cuvinte cheie și semnificații semantice.
  - **Imagini** sau **Video**. Un videoclip de la o cameră de supraveghere poate fi utilizat pentru a estima traficul pe drum și pentru a informa oamenii despre posibilele ambuteiaje.
  - **Jurnale de server web** pot fi utilizate pentru a înțelege care pagini ale site-ului nostru sunt cele mai des vizitate și pentru cât timp.
* Semi-structurate
  - Grafurile de **Rețele Sociale** pot fi surse excelente de date despre personalitățile utilizatorilor și potențiala eficiență în răspândirea informațiilor.
  - Când avem o mulțime de fotografii de la o petrecere, putem încerca să extragem date despre **Dinamica Grupului** construind un grafic al persoanelor care fac poze împreună.

Cunoscând diferitele surse posibile de date, poți încerca să te gândești la diferite scenarii în care tehnicile de știință a datelor pot fi aplicate pentru a înțelege mai bine situația și pentru a îmbunătăți procesele de afaceri.

## Ce poți face cu Datele

În Știința Datelor, ne concentrăm pe următorii pași ai călătoriei datelor:

<dl>
<dt>1) Achiziția Datelor</dt>
<dd>
Primul pas este colectarea datelor. Deși în multe cazuri poate fi un proces simplu, cum ar fi datele care ajung într-o bază de date dintr-o aplicație web, uneori trebuie să folosim tehnici speciale. De exemplu, datele de la senzorii IoT pot fi copleșitoare, și este o practică bună să folosim puncte de colectare tampon, cum ar fi IoT Hub, pentru a colecta toate datele înainte de procesarea ulterioară.
</dd>
<dt>2) Stocarea Datelor</dt>
<dd>
Stocarea datelor poate fi o provocare, mai ales dacă vorbim despre big data. Când decidem cum să stocăm datele, este logic să anticipăm modul în care am dori să interogăm datele în viitor. Există mai multe moduri în care datele pot fi stocate:
<ul>
<li>O bază de date relațională stochează o colecție de tabele și folosește un limbaj special numit SQL pentru a le interoga. De obicei, tabelele sunt organizate în diferite grupuri numite scheme. În multe cazuri, trebuie să convertim datele din forma originală pentru a se potrivi cu schema.</li>
<li><a href="https://en.wikipedia.org/wiki/NoSQL">O bază de date NoSQL</a>, cum ar fi <a href="https://azure.microsoft.com/services/cosmos-db/?WT.mc_id=academic-77958-bethanycheum">CosmosDB</a>, nu impune scheme asupra datelor și permite stocarea datelor mai complexe, de exemplu, documente JSON ierarhice sau grafuri. Totuși, bazele de date NoSQL nu au capacitățile bogate de interogare ale SQL și nu pot impune integritatea referențială, adică regulile privind modul în care datele sunt structurate în tabele și guvernează relațiile dintre tabele.</li>
<li><a href="https://en.wikipedia.org/wiki/Data_lake">Stocarea în Data Lake</a> este utilizată pentru colecții mari de date în formă brută, nestructurată. Data lakes sunt adesea utilizate cu big data, unde toate datele nu pot încăpea pe o singură mașină și trebuie stocate și procesate de un cluster de servere. <a href="https://en.wikipedia.org/wiki/Apache_Parquet">Parquet</a> este formatul de date care este adesea utilizat în combinație cu big data.</li> 
</ul>
</dd>
<dt>3) Procesarea Datelor</dt>
<dd>
Aceasta este partea cea mai interesantă a călătoriei datelor, care implică convertirea datelor din forma lor originală într-o formă care poate fi utilizată pentru vizualizare/antrenarea modelului. Când lucrăm cu date nestructurate, cum ar fi text sau imagini, poate fi necesar să utilizăm unele tehnici de IA pentru a extrage <b>caracteristici</b> din date, transformându-le astfel într-o formă structurată.
</dd>
<dt>4) Vizualizare / Perspective Umane</dt>
<dd>
Adesea, pentru a înțelege datele, trebuie să le vizualizăm. Având multe tehnici diferite de vizualizare în arsenalul nostru, putem găsi perspectiva potrivită pentru a obține o înțelegere. Adesea, un om de știință în domeniul datelor trebuie să "se joace cu datele", vizualizându-le de multe ori și căutând relații. De asemenea, putem utiliza tehnici statistice pentru a testa o ipoteză sau pentru a demonstra o corelație între diferite părți ale datelor.   
</dd>
<dt>5) Antrenarea unui model predictiv</dt>
<dd>
Deoarece scopul final al științei datelor este de a putea lua decizii bazate pe date, putem dori să utilizăm tehnicile de <a href="http://github.com/microsoft/ml-for-beginners">Învățare Automată</a> pentru a construi un model predictiv. Putem apoi să-l folosim pentru a face predicții utilizând seturi de date noi cu structuri similare.
</dd>
</dl>

Desigur, în funcție de datele reale, unii pași ar putea lipsi (de exemplu, atunci când avem deja datele în baza de date sau când nu avem nevoie de antrenarea modelului), sau unii pași ar putea fi repetați de mai multe ori (cum ar fi procesarea datelor).

## Digitalizare și Transformare Digitală

În ultimul deceniu, multe afaceri au început să înțeleagă importanța datelor în luarea deciziilor de afaceri. Pentru a aplica principiile științei datelor în conducerea unei afaceri, trebuie mai întâi să colectăm unele date, adică să traducem procesele de afaceri în formă digitală. Acest lucru este cunoscut sub numele de **digitalizare**. Aplicarea tehnicilor de știință a datelor la aceste date pentru a ghida deciziile poate duce la creșteri semnificative ale productivității (sau chiar la o schimbare a direcției afacerii), numită **transformare digitală**.

Să luăm un exemplu. Să presupunem că avem un curs de știința datelor (cum este acesta) pe care îl livrăm online studenților și dorim să folosim știința datelor pentru a-l îmbunătăți. Cum putem face acest lucru?

Putem începe prin a ne întreba "Ce poate fi digitalizat?" Cel mai simplu mod ar fi să măsurăm timpul necesar fiecărui student pentru a finaliza fiecare modul și să măsurăm cunoștințele obținute prin oferirea unui test cu opțiuni multiple la sfârșitul fiecărui modul. Calculând media timpului de finalizare pentru toți studenții, putem afla care module cauzează cele mai mari dificultăți pentru studenți și să lucrăm la simplificarea lor.
> Ai putea argumenta că această abordare nu este ideală, deoarece modulele pot avea lungimi diferite. Probabil ar fi mai corect să împărțim timpul la lungimea modulului (în număr de caractere) și să comparăm acele valori în schimb.

Când începem să analizăm rezultatele testelor cu răspunsuri multiple, putem încerca să determinăm care sunt conceptele pe care elevii le înțeleg cu dificultate și să folosim aceste informații pentru a îmbunătăți conținutul. Pentru a face acest lucru, trebuie să concepem teste astfel încât fiecare întrebare să corespundă unui anumit concept sau unei unități de cunoștințe.

Dacă dorim să complicăm și mai mult lucrurile, putem reprezenta grafic timpul necesar pentru fiecare modul în funcție de categoria de vârstă a elevilor. Am putea descoperi că pentru unele categorii de vârstă durează un timp nepotrivit de lung pentru a finaliza modulul sau că elevii renunță înainte de a-l termina. Acest lucru ne poate ajuta să oferim recomandări de vârstă pentru modul și să minimizăm nemulțumirea oamenilor cauzată de așteptări greșite.

## 🚀 Provocare

În această provocare, vom încerca să identificăm concepte relevante pentru domeniul Științei Datelor analizând texte. Vom lua un articol de pe Wikipedia despre Știința Datelor, vom descărca și procesa textul, iar apoi vom construi un nor de cuvinte asemănător cu acesta:

![Nor de cuvinte pentru Știința Datelor](../../../../translated_images/ro/ds_wordcloud.664a7c07dca57de017c22bf0498cb40f898d48aa85b3c36a80620fea12fadd42.png)

Vizitează [`notebook.ipynb`](../../../../1-Introduction/01-defining-data-science/notebook.ipynb ':ignore') pentru a parcurge codul. Poți, de asemenea, să rulezi codul și să vezi cum efectuează toate transformările de date în timp real.

> Dacă nu știi cum să rulezi codul într-un Jupyter Notebook, aruncă o privire la [acest articol](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## [Test de verificare post-lectură](https://ff-quizzes.netlify.app/en/ds/quiz/1)

## Temele

* **Sarcina 1**: Modifică codul de mai sus pentru a descoperi concepte legate de domeniile **Big Data** și **Machine Learning**
* **Sarcina 2**: [Gândește-te la scenarii din Știința Datelor](assignment.md)

## Credite

Această lecție a fost creată cu ♥️ de [Dmitry Soshnikov](http://soshnikov.com)

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.