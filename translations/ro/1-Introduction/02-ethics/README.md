<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3a34157cc63516eba97c89a0b2f8c3e6",
  "translation_date": "2025-09-03T21:47:57+00:00",
  "source_file": "1-Introduction/02-ethics/README.md",
  "language_code": "ro"
}
-->
# Introducere în Etica Datelor

|![ Sketchnote de [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/02-Ethics.png)|
|:---:|
| Etica în Știința Datelor - _Sketchnote de [@nitya](https://twitter.com/nitya)_ |

---

Suntem cu toții cetățeni ai datelor, trăind într-o lume dominată de acestea.

Tendințele pieței ne arată că, până în 2022, 1 din 3 organizații mari va cumpăra și vinde date prin intermediul [Piațelor și Schimburilor online](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/). Ca **Dezvoltatori de Aplicații**, vom găsi mai ușor și mai ieftin să integrăm perspective bazate pe date și automatizări bazate pe algoritmi în experiențele zilnice ale utilizatorilor. Dar, pe măsură ce AI devine omniprezent, va trebui să înțelegem și potențialele daune cauzate de [utilizarea abuzivă](https://www.youtube.com/watch?v=TQHs8SA1qpk) a acestor algoritmi la scară largă.

Tendințele indică, de asemenea, că vom crea și consuma peste [180 zettabytes](https://www.statista.com/statistics/871513/worldwide-data-created/) de date până în 2025. Ca **Oameni de Știința Datelor**, acest lucru ne oferă un acces fără precedent la datele personale. Aceasta înseamnă că putem construi profiluri comportamentale ale utilizatorilor și influența luarea deciziilor în moduri care creează o [iluzie de alegere liberă](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice), în timp ce îi îndrumăm, posibil, către rezultate pe care le preferăm. De asemenea, ridică întrebări mai ample despre confidențialitatea datelor și protecția utilizatorilor.

Etica datelor devine acum _un ghid necesar_ pentru știința și ingineria datelor, ajutându-ne să minimizăm potențialele daune și consecințele neintenționate ale acțiunilor noastre bazate pe date. [Ciclul de Hype Gartner pentru AI](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/) identifică tendințe relevante în etica digitală, AI responsabilă și guvernanța AI ca factori cheie pentru megatendințele mai mari legate de _democratizarea_ și _industrializarea_ AI.

![Ciclul de Hype Gartner pentru AI - 2020](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

În această lecție, vom explora domeniul fascinant al eticii datelor - de la concepte și provocări de bază, la studii de caz și concepte aplicate de AI, cum ar fi guvernanța - care ajută la stabilirea unei culturi etice în echipele și organizațiile care lucrează cu date și AI.

## [Chestionar înainte de lecție](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/2) 🎯

## Definiții de bază

Să începem prin a înțelege terminologia de bază.

Cuvântul "etică" provine din [cuvântul grecesc "ethikos"](https://en.wikipedia.org/wiki/Ethics) (și rădăcina sa "ethos"), care înseamnă _caracter sau natură morală_.

**Etica** se referă la valorile comune și principiile morale care guvernează comportamentul nostru în societate. Etica nu se bazează pe legi, ci pe norme larg acceptate despre ceea ce este "corect vs. greșit". Totuși, considerațiile etice pot influența inițiativele de guvernanță corporativă și reglementările guvernamentale care creează mai multe stimulente pentru conformitate.

**Etica Datelor** este o [ramură nouă a eticii](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1) care "studiază și evaluează problemele morale legate de _date, algoritmi și practici corespunzătoare_". Aici, **"datele"** se concentrează pe acțiuni legate de generare, înregistrare, curare, procesare, diseminare, partajare și utilizare, **"algoritmii"** se concentrează pe AI, agenți, învățare automată și roboți, iar **"practicile"** se concentrează pe subiecte precum inovația responsabilă, programarea, hacking-ul și codurile etice.

**Etica Aplicată** este [aplicarea practică a considerațiilor morale](https://en.wikipedia.org/wiki/Applied_ethics). Este procesul de investigare activă a problemelor etice în contextul _acțiunilor, produselor și proceselor din lumea reală_ și de luare a măsurilor corective pentru a ne asigura că acestea rămân aliniate cu valorile noastre etice definite.

**Cultura Eticii** se referă la [_operaționalizarea_ eticii aplicate](https://hbr.org/2019/05/how-to-design-an-ethical-organization) pentru a ne asigura că principiile și practicile noastre etice sunt adoptate într-un mod consistent și scalabil în întreaga organizație. Culturile etice de succes definesc principii etice la nivel organizațional, oferă stimulente semnificative pentru conformitate și întăresc normele etice prin încurajarea și amplificarea comportamentelor dorite la fiecare nivel al organizației.

## Concepte Etice

În această secțiune, vom discuta concepte precum **valori comune** (principii) și **provocări etice** (probleme) pentru etica datelor - și vom explora **studii de caz** care te ajută să înțelegi aceste concepte în contexte reale.

### 1. Principii Etice

Fiecare strategie de etică a datelor începe prin definirea _principiilor etice_ - "valorile comune" care descriu comportamentele acceptabile și ghidează acțiunile conforme în proiectele noastre de date și AI. Acestea pot fi definite la nivel individual sau de echipă. Totuși, majoritatea organizațiilor mari le conturează într-o declarație de misiune sau cadru de _AI etică_ definit la nivel corporativ și aplicat în mod consistent în toate echipele.

**Exemplu:** Declarația de misiune [AI Responsabilă](https://www.microsoft.com/en-us/ai/responsible-ai) de la Microsoft spune: _"Suntem dedicați avansării AI ghidată de principii etice care pun oamenii pe primul loc"_ - identificând 6 principii etice în cadrul de mai jos:

![AI Responsabilă la Microsoft](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

Să explorăm pe scurt aceste principii. _Transparența_ și _responsabilitatea_ sunt valori fundamentale pe care se construiesc celelalte principii - așa că să începem cu acestea:

* [**Responsabilitatea**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) face ca practicienii să fie _responsabili_ pentru operațiunile lor de date și AI și pentru conformitatea cu aceste principii etice.
* [**Transparența**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) asigură că acțiunile legate de date și AI sunt _ușor de înțeles_ (interpretabile) pentru utilizatori, explicând ce și de ce în spatele deciziilor.
* [**Corectitudinea**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) - se concentrează pe asigurarea că AI tratează _toți oamenii_ în mod echitabil, abordând orice prejudecăți socio-tehnice sistemice sau implicite în date și sisteme.
* [**Fiabilitatea și Siguranța**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - asigură că AI se comportă _consistent_ cu valorile definite, minimizând potențialele daune sau consecințe neintenționate.
* [**Confidențialitatea și Securitatea**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - se referă la înțelegerea provenienței datelor și la oferirea de _protecții legate de confidențialitatea datelor_ utilizatorilor.
* [**Incluziunea**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - se referă la proiectarea soluțiilor AI cu intenție, adaptându-le pentru a răspunde unei _game largi de nevoi și capacități umane_.

> 🚨 Gândește-te la ce ar putea fi declarația ta de misiune pentru etica datelor. Explorează cadrele de AI etică de la alte organizații - iată exemple de la [IBM](https://www.ibm.com/cloud/learn/ai-ethics), [Google](https://ai.google/principles) și [Facebook](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/). Ce valori comune au în comun? Cum se raportează aceste principii la produsul sau industria AI în care operează?

### 2. Provocări Etice

Odată ce am definit principiile etice, următorul pas este să evaluăm acțiunile noastre legate de date și AI pentru a vedea dacă acestea se aliniază cu valorile comune. Gândește-te la acțiunile tale în două categorii: _colectarea datelor_ și _proiectarea algoritmilor_.

În cazul colectării datelor, acțiunile vor implica probabil **date personale** sau informații personale identificabile (PII) pentru indivizi identificabili. Acestea includ [diverse elemente de date non-personale](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en) care, _împreună_, identifică un individ. Provocările etice pot fi legate de _confidențialitatea datelor_, _proprietatea datelor_ și subiecte conexe precum _consimțământul informat_ și _drepturile de proprietate intelectuală_ ale utilizatorilor.

În cazul proiectării algoritmilor, acțiunile vor implica colectarea și curarea **seturilor de date**, apoi utilizarea acestora pentru a antrena și implementa **modele de date** care prezic rezultate sau automatizează decizii în contexte reale. Provocările etice pot apărea din _prejudecăți în seturile de date_, probleme de _calitate a datelor_, _inechitate_ și _reprezentare greșită_ în algoritmi - inclusiv unele probleme care sunt de natură sistemică.

În ambele cazuri, provocările etice evidențiază zonele în care acțiunile noastre pot intra în conflict cu valorile comune. Pentru a detecta, atenua, minimiza sau elimina aceste preocupări, trebuie să punem întrebări morale "da/nu" legate de acțiunile noastre, apoi să luăm măsuri corective, după cum este necesar. Să analizăm câteva provocări etice și întrebările morale pe care le ridică:

#### 2.1 Proprietatea Datelor

Colectarea datelor implică adesea date personale care pot identifica subiecții datelor. [Proprietatea datelor](https://permission.io/blog/data-ownership) se referă la _controlul_ și [_drepturile utilizatorilor_](https://permission.io/blog/data-ownership) legate de crearea, procesarea și diseminarea datelor.

Întrebările morale pe care trebuie să le punem sunt:
 * Cine deține datele? (utilizator sau organizație)
 * Ce drepturi au subiecții datelor? (ex: acces, ștergere, portabilitate)
 * Ce drepturi au organizațiile? (ex: rectificarea recenziilor utilizatorilor malițioase)

#### 2.2 Consimțământul Informat

[Consimțământul informat](https://legaldictionary.net/informed-consent/) definește actul utilizatorilor de a fi de acord cu o acțiune (cum ar fi colectarea datelor) cu o _înțelegere completă_ a faptelor relevante, inclusiv scopul, riscurile potențiale și alternativele.

Întrebările de explorat aici sunt:
 * Utilizatorul (subiectul datelor) și-a dat permisiunea pentru captarea și utilizarea datelor?
 * Utilizatorul a înțeles scopul pentru care au fost capturate datele?
 * Utilizatorul a înțeles riscurile potențiale ale participării sale?

#### 2.3 Proprietatea Intelectuală

[Proprietatea intelectuală](https://en.wikipedia.org/wiki/Intellectual_property) se referă la creații intangibile rezultate din inițiativa umană, care pot _avea valoare economică_ pentru indivizi sau afaceri.

Întrebările de explorat aici sunt:
 * Datele colectate aveau valoare economică pentru un utilizator sau o afacere?
 * Utilizatorul are proprietate intelectuală aici?
 * Organizația are proprietate intelectuală aici?
 * Dacă aceste drepturi există, cum le protejăm?

#### 2.4 Confidențialitatea Datelor

[Confidențialitatea datelor](https://www.northeastern.edu/graduate/blog/what-is-data-privacy/) sau confidențialitatea informațiilor se referă la păstrarea confidențialității utilizatorilor și protecția identității utilizatorilor în raport cu informațiile personale identificabile.

Întrebările de explorat aici sunt:
 * Datele (personale) ale utilizatorilor sunt securizate împotriva atacurilor și scurgerilor?
 * Datele utilizatorilor sunt accesibile doar utilizatorilor și contextelor autorizate?
 * Anonimitatea utilizatorilor este păstrată atunci când datele sunt partajate sau diseminate?
 * Poate un utilizator fi de-identificat din seturi de date anonimizate?

#### 2.5 Dreptul de a Fi Uitat

[Dreptul de a Fi Uitat](https://en.wikipedia.org/wiki/Right_to_be_forgotten) sau [Dreptul la Ștergere](https://www.gdpreu.org/right-to-be-forgotten/) oferă protecție suplimentară datelor personale ale utilizatorilor. În mod specific, le oferă utilizatorilor dreptul de a solicita ștergerea sau eliminarea datelor personale din căutările pe Internet și alte locații, _în anumite circumstanțe_ - permițându-le un nou început online fără ca acțiunile din trecut să fie folosite împotriva lor.

Întrebările de explorat aici sunt:
 * Sistemul permite subiecților datelor să solicite ștergerea?
 * Retragerea consimțământului utilizatorului ar trebui să declanșeze ștergerea automată?
 * Datele au fost colectate fără consimțământ sau prin mijloace ilegale?
 * Suntem conformi cu reglementările guvernamentale privind confidențialitatea datelor?

#### 2.6 Prejudecăți în Seturile de Date

Prejudecățile în seturile de date sau [Prejudecățile de Colectare](http://researcharticles.com/index.php/bias-in-data-collection-in-research/) se referă la selectarea unui subset _nereprezentativ_ de date pentru dezvoltarea algoritmilor, creând potențial inechitate în rezultatele pentru grupuri diverse. Tipurile de prejudecăți includ prejudecăți de selecție sau eșantionare, prejudecăți ale voluntarilor și prejudecăți ale instrumentelor.

Întrebările de explorat aici sunt:
 * Am recrutat un set reprezentativ de subiecți ai datelor?
 * Am testat setul nostru de date colectat sau curat pentru diverse prejudecăți?
 * Putem atenua sau elimina prejudecățile descoperite?

#### 2.7 Calitatea Datelor

[Calitatea Datelor](https://lakefs.io/data-quality-testing/) analizează validitatea setului de date curat utilizat pentru dezvoltarea algoritmilor noștri, verificând dacă caracteristicile și înregistrările îndeplinesc cerințele pentru nivelul de acuratețe și consistență necesar scopului nostru AI.

Întrebările de explorat aici sunt:
 * Am capturat caracteristici valide pentru cazul nostru de utilizare?
 * Datele au fost capturate în mod consistent din surse de date diverse?
 * Setul de date este complet pentru condiții sau scenarii diverse?
 * Informațiile capturate reflectă realitatea cu acuratețe?
[Algorithm Fairness](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f) verifică dacă designul algoritmului discriminează sistematic anumite subgrupuri de persoane, conducând la [posibile prejudicii](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml) în _alocare_ (unde resursele sunt refuzate sau reținute de la acel grup) și _calitatea serviciului_ (unde AI nu este la fel de precis pentru unele subgrupuri comparativ cu altele).

Întrebări de explorat aici:
 * Am evaluat acuratețea modelului pentru subgrupuri și condiții diverse?
 * Am analizat sistemul pentru posibile prejudicii (de exemplu, stereotipuri)?
 * Putem revizui datele sau reantrena modelele pentru a reduce prejudiciile identificate?

Explorați resurse precum [AI Fairness checklists](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA) pentru a afla mai multe.

#### 2.9 Denaturarea datelor

[Denaturarea datelor](https://www.sciencedirect.com/topics/computer-science/misrepresentation) se referă la întrebarea dacă comunicăm informații din date raportate onest într-un mod înșelător pentru a susține o narațiune dorită.

Întrebări de explorat aici:
 * Raportăm date incomplete sau inexacte?
 * Vizualizăm datele într-un mod care conduce la concluzii înșelătoare?
 * Folosim tehnici statistice selective pentru a manipula rezultatele?
 * Există explicații alternative care ar putea oferi o concluzie diferită?

#### 2.10 Alegerea liberă
[Iluzia alegerii libere](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) apare atunci când "arhitecturile de alegere" ale sistemului folosesc algoritmi de luare a deciziilor pentru a influența oamenii să ia un rezultat preferat, în timp ce par să le ofere opțiuni și control. Aceste [dark patterns](https://www.darkpatterns.org/) pot provoca prejudicii sociale și economice utilizatorilor. Deoarece deciziile utilizatorilor influențează profilurile de comportament, aceste acțiuni pot conduce la alegeri viitoare care amplifică sau extind impactul acestor prejudicii.

Întrebări de explorat aici:
 * Utilizatorul a înțeles implicațiile alegerii făcute?
 * Utilizatorul era conștient de (alternativele) opțiuni și de avantajele și dezavantajele fiecăreia?
 * Utilizatorul poate inversa o alegere automată sau influențată ulterior?

### 3. Studii de caz

Pentru a pune aceste provocări etice în contexte reale, este util să analizăm studii de caz care evidențiază prejudiciile și consecințele potențiale asupra indivizilor și societății atunci când astfel de încălcări etice sunt ignorate.

Iată câteva exemple:

| Provocare etică | Studiu de caz  | 
|--- |--- |
| **Consimțământ informat** | 1972 - [Tuskegee Syphilis Study](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - Bărbații afro-americani care au participat la studiu au fost promiși îngrijire medicală gratuită _dar au fost înșelați_ de cercetători care nu le-au informat despre diagnostic sau despre disponibilitatea tratamentului. Mulți subiecți au murit, iar partenerii sau copiii au fost afectați; studiul a durat 40 de ani. | 
| **Confidențialitatea datelor** |  2007 - [Premiul Netflix pentru date](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) a oferit cercetătorilor _10M de evaluări anonimizate de filme de la 50K de clienți_ pentru a îmbunătăți algoritmii de recomandare. Totuși, cercetătorii au reușit să coreleze datele anonimizate cu date identificabile personal din _seturi de date externe_ (de exemplu, comentarii IMDb) - efectiv "de-anonimizând" unii abonați Netflix.|
| **Bias în colectare**  | 2013 - Orașul Boston [a dezvoltat Street Bump](https://www.boston.gov/transportation/street-bump), o aplicație care permite cetățenilor să raporteze gropi, oferind orașului date mai bune despre drumuri pentru a identifica și rezolva problemele. Totuși, [persoanele din grupuri cu venituri mai mici aveau acces redus la mașini și telefoane](https://hbr.org/2013/04/the-hidden-biases-in-big-data), făcând problemele lor de drum invizibile în această aplicație. Dezvoltatorii au colaborat cu academicieni pentru a aborda _accesul echitabil și diviziunile digitale_ pentru corectitudine. |
| **Corectitudinea algoritmică**  | 2018 - Studiul MIT [Gender Shades](http://gendershades.org/overview.html) a evaluat acuratețea produselor AI de clasificare a genului, expunând lacunele de acuratețe pentru femei și persoane de culoare. Un [Apple Card din 2019](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/) părea să ofere mai puțin credit femeilor decât bărbaților. Ambele au ilustrat probleme de bias algoritmic care conduc la prejudicii socio-economice.|
| **Denaturarea datelor** | 2020 - [Departamentul de Sănătate Publică din Georgia a lansat grafice COVID-19](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening) care păreau să inducă în eroare cetățenii despre tendințele cazurilor confirmate prin ordonarea non-cronologică pe axa x. Acest lucru ilustrează denaturarea prin trucuri de vizualizare. |
| **Iluzia alegerii libere** | 2020 - Aplicația de învățare [ABCmouse a plătit 10M pentru a soluționa o plângere FTC](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/) unde părinții au fost blocați în plata abonamentelor pe care nu le puteau anula. Acest lucru ilustrează dark patterns în arhitecturile de alegere, unde utilizatorii au fost influențați spre alegeri potențial dăunătoare. |
| **Confidențialitatea datelor și drepturile utilizatorilor** | 2021 - [Breșa de date Facebook](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users) a expus datele a 530M de utilizatori, rezultând într-o amendă de 5B către FTC. Totuși, compania a refuzat să notifice utilizatorii despre breșă, încălcând drepturile utilizatorilor privind transparența și accesul la date. |

Doriți să explorați mai multe studii de caz? Consultați aceste resurse:
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - dileme etice din diverse industrii. 
* [Cursul de etică în știința datelor](https://www.coursera.org/learn/data-science-ethics#syllabus) - studii de caz de referință explorate.
* [Unde lucrurile au mers prost](https://deon.drivendata.org/examples/) - checklist-ul Deon cu exemple.

> 🚨 Gândiți-vă la studiile de caz pe care le-ați văzut - ați experimentat sau ați fost afectați de o provocare etică similară în viața voastră? Puteți să vă gândiți la cel puțin un alt studiu de caz care ilustrează una dintre provocările etice discutate în această secțiune?

## Etica aplicată

Am discutat despre concepte etice, provocări și studii de caz în contexte reale. Dar cum începem să _aplicăm_ principiile și practicile etice în proiectele noastre? Și cum _operaționalizăm_ aceste practici pentru o guvernanță mai bună? Să explorăm câteva soluții reale:

### 1. Coduri profesionale

Codurile profesionale oferă o opțiune pentru organizații de a "motiva" membrii să susțină principiile etice și declarația de misiune. Codurile sunt _ghiduri morale_ pentru comportamentul profesional, ajutând angajații sau membrii să ia decizii care se aliniază cu principiile organizației lor. Ele sunt eficiente doar în măsura în care membrii le respectă voluntar; totuși, multe organizații oferă recompense și penalități suplimentare pentru a motiva respectarea codurilor.

Exemple includ:

 * [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/) Cod de Etică
 * [Data Science Association](http://datascienceassn.org/code-of-conduct.html) Cod de Conduită (creat în 2013)
 * [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics) (din 1993)

> 🚨 Faceți parte dintr-o organizație profesională de inginerie sau știința datelor? Explorați site-ul lor pentru a vedea dacă definesc un cod profesional de etică. Ce spune acesta despre principiile lor etice? Cum "motivează" membrii să urmeze codul?

### 2. Liste de verificare etică

În timp ce codurile profesionale definesc comportamentul _etic necesar_ de la practicieni, ele [au limitări cunoscute](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) în aplicare, în special în proiectele de mare amploare. În schimb, mulți experți în știința datelor [pledează pentru liste de verificare](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md), care pot **conecta principiile la practici** într-un mod mai determinist și acționabil.

Listele de verificare transformă întrebările în sarcini "da/nu" care pot fi operaționalizate, permițându-le să fie urmărite ca parte a fluxurilor de lucru standard pentru lansarea produselor.

Exemple includ:
 * [Deon](https://deon.drivendata.org/) - o listă generală de verificare pentru etica datelor creată din [recomandări din industrie](https://deon.drivendata.org/#checklist-citations) cu un instrument de linie de comandă pentru integrare ușoară.
 * [Lista de verificare pentru auditul confidențialității](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - oferă orientări generale pentru practicile de manipulare a informațiilor din perspective legale și sociale.
 * [Lista de verificare pentru corectitudinea AI](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - creată de practicieni AI pentru a sprijini adoptarea și integrarea verificărilor de corectitudine în ciclurile de dezvoltare AI.
 * [22 de întrebări pentru etica în date și AI](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - cadru mai deschis, structurat pentru explorarea inițială a problemelor etice în design, implementare și contexte organizaționale.

### 3. Reglementări etice

Etica se referă la definirea valorilor comune și la a face ceea ce este corect _voluntar_. **Conformitatea** se referă la _respectarea legii_ acolo unde este definită. **Guvernanța** acoperă în general toate modurile în care organizațiile operează pentru a aplica principiile etice și pentru a respecta legile stabilite.

Astăzi, guvernanța ia două forme în cadrul organizațiilor. În primul rând, este vorba despre definirea principiilor **AI etice** și stabilirea practicilor pentru a operaționaliza adoptarea în toate proiectele AI din organizație. În al doilea rând, este vorba despre respectarea tuturor reglementărilor guvernamentale **privind protecția datelor** pentru regiunile în care operează.

Exemple de reglementări privind protecția și confidențialitatea datelor:

 * `1974`, [US Privacy Act](https://www.justice.gov/opcl/privacy-act-1974) - reglementează colectarea, utilizarea și divulgarea informațiilor personale de către _guvernul federal_.
 * `1996`, [US Health Insurance Portability & Accountability Act (HIPAA)](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - protejează datele personale de sănătate.
 * `1998`, [US Children's Online Privacy Protection Act (COPPA)](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - protejează confidențialitatea datelor copiilor sub 13 ani.
 * `2018`, [Regulamentul General privind Protecția Datelor (GDPR)](https://gdpr-info.eu/) - oferă drepturi utilizatorilor, protecția datelor și confidențialitate.
 * `2018`, [California Consumer Privacy Act (CCPA)](https://www.oag.ca.gov/privacy/ccpa) oferă consumatorilor mai multe _drepturi_ asupra datelor lor (personale).
 * `2021`, Legea Chinei privind [Protecția Informațiilor Personale](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) tocmai a fost adoptată, creând una dintre cele mai puternice reglementări privind confidențialitatea datelor online la nivel mondial.

> 🚨 Uniunea Europeană a definit GDPR (Regulamentul General privind Protecția Datelor), care rămâne una dintre cele mai influente reglementări privind confidențialitatea datelor astăzi. Știați că definește și [8 drepturi ale utilizatorilor](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr) pentru a proteja confidențialitatea digitală și datele personale ale cetățenilor? Aflați care sunt acestea și de ce contează.

### 4. Cultura etică

Rețineți că există un decalaj intangibil între _conformitate_ (a face suficient pentru a respecta "litera legii") și abordarea [problemelor sistemice](https://www.coursera.org/learn/data-science-ethics/home/week/4) (cum ar fi osificarea, asimetria informațiilor și nedreptatea distribuțională) care pot accelera utilizarea abuzivă a AI.

Acesta din urmă necesită [abordări colaborative pentru definirea culturilor etice](https://towardsdatascience.com/why-ai-ethics-requires-a-culture-driven-approach-26f451afa29f) care construiesc conexiuni emoționale și valori comune consistente _în cadrul organizațiilor_ din industrie. Acest lucru solicită mai multe [culturi etice formalizate](https://www.codeforamerica.org/news/formalizing-an-ethical-data-culture/) în organizații - permițând _oricui_ să [tragă cordonul Andon](https://en.wikipedia.org/wiki/Andon_(manufacturing)) (pentru a ridica preocupări etice devreme în proces) și făcând _evaluările etice_ (de exemplu, în angajare) un criteriu esențial pentru formarea echipelor în proiectele AI.

---
## [Quiz post-lectură](https://ff-quizzes.netlify.app/en/ds/) 🎯
## Recapitulare și auto-studiu 

Cursurile și cărțile ajută la înțelegerea conceptelor etice de bază și a provocărilor, în timp ce studiile de caz și instrumentele ajută la practicile etice aplicate în contexte reale. Iată câteva resurse pentru a începe:

* [Machine Learning For Beginners](https://github.com/microsoft/ML-For-Beginners/blob/main/1-Introduction/3-fairness/README.md) - lecție despre corectitudine, de la Microsoft.
* [Principiile AI Responsabil](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - parcurs de învățare gratuit de la Microsoft Learn.
* [Etică și Știința Datelor](https://resources.oreilly.com/examples/0636920203964) - EBook O'Reilly (M. Loukides, H. Mason și alții)
* [Etica în Știința Datelor](https://www.coursera.org/learn/data-science-ethics#syllabus) - curs online de la Universitatea din Michigan.
* [Etica Explicată](https://ethicsunwrapped.utexas.edu/case-studies) - studii de caz de la Universitatea din Texas.

# Temă

[Scrie un Studiu de Caz despre Etica Datelor](assignment.md)

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.