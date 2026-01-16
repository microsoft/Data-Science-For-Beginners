<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "43212cc1ac137b7bb1dcfb37ca06b0f4",
  "translation_date": "2025-10-25T19:09:26+00:00",
  "source_file": "1-Introduction/01-defining-data-science/README.md",
  "language_code": "hr"
}
-->
# Definiranje podatkovne znanosti

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/01-Definitions.png) |
| :----------------------------------------------------------------------------------------------------: |
|              Definiranje podatkovne znanosti - _Sketchnote by [@nitya](https://twitter.com/nitya)_     |

---

[![Video o definiranju podatkovne znanosti](../../../../translated_images/hr/video-def-ds.6623ee2392ef1abf6d7faf3fad10a4163642811749da75f44e35a5bb121de15c.png)](https://youtu.be/beZ7Mb_oz9I)

## [Kviz prije predavanja](https://ff-quizzes.netlify.app/en/ds/quiz/0)

## Što su podaci?
U svakodnevnom životu stalno smo okruženi podacima. Tekst koji sada čitate su podaci. Popis telefonskih brojeva vaših prijatelja u pametnom telefonu su podaci, kao i trenutno vrijeme prikazano na vašem satu. Kao ljudska bića, prirodno se koristimo podacima, bilo da brojimo novac koji imamo ili pišemo pisma prijateljima.

Međutim, podaci su postali mnogo važniji s pojavom računala. Primarna uloga računala je obavljanje izračuna, ali za to im trebaju podaci. Stoga moramo razumjeti kako računala pohranjuju i obrađuju podatke.

S pojavom interneta, uloga računala kao uređaja za rukovanje podacima se povećala. Ako razmislite, sada sve više koristimo računala za obradu i komunikaciju podataka, a ne samo za stvarne izračune. Kada pišemo e-mail prijatelju ili tražimo informacije na internetu - u biti stvaramo, pohranjujemo, prenosimo i manipuliramo podacima.
> Možete li se sjetiti kada ste zadnji put koristili računalo za stvarno računanje?

## Što je podatkovna znanost?

Na [Wikipediji](https://en.wikipedia.org/wiki/Data_science), **podatkovna znanost** je definirana kao *znanstveno područje koje koristi znanstvene metode za izvlačenje znanja i uvida iz strukturiranih i nestrukturiranih podataka te primjenu znanja i praktičnih uvida iz podataka u širokom rasponu primjena*.

Ova definicija ističe sljedeće važne aspekte podatkovne znanosti:

* Glavni cilj podatkovne znanosti je **izvlačenje znanja** iz podataka, drugim riječima - **razumijevanje** podataka, pronalaženje skrivenih odnosa i izgradnja **modela**.
* Podatkovna znanost koristi **znanstvene metode**, poput vjerojatnosti i statistike. Zapravo, kada je pojam *podatkovna znanost* prvi put uveden, neki su tvrdili da je to samo novi moderni naziv za statistiku. Danas je očito da je ovo područje mnogo šire.
* Dobiveno znanje treba primijeniti kako bi se proizveli **praktični uvidi**, tj. korisni uvidi koji se mogu primijeniti u stvarnim poslovnim situacijama.
* Trebali bismo biti sposobni raditi s **strukturiranim** i **nestrukturiranim** podacima. Kasnije u tečaju ćemo se vratiti na raspravu o različitim vrstama podataka.
* **Područje primjene** je važan koncept, a podatkovni znanstvenici često trebaju barem određeni stupanj stručnosti u problematičnom području, na primjer: financije, medicina, marketing itd.

> Još jedan važan aspekt podatkovne znanosti je proučavanje načina na koji se podaci mogu prikupljati, pohranjivati i obrađivati pomoću računala. Dok nam statistika daje matematičke temelje, podatkovna znanost primjenjuje matematičke koncepte kako bi zapravo izvukla uvide iz podataka.

Jedan od načina (pripisan [Jim Grayu](https://en.wikipedia.org/wiki/Jim_Gray_(computer_scientist))) za promatranje podatkovne znanosti je razmatranje kao zasebnog znanstvenog pristupa:
* **Empirijski**, gdje se oslanjamo uglavnom na opažanja i rezultate eksperimenata
* **Teorijski**, gdje novi koncepti proizlaze iz postojećeg znanstvenog znanja
* **Računalni**, gdje otkrivamo nove principe na temelju računalnih eksperimenata
* **Vođeni podacima**, temeljen na otkrivanju odnosa i obrazaca u podacima  

## Ostala povezana područja

Budući da su podaci sveprisutni, podatkovna znanost je također široko područje koje se dotiče mnogih drugih disciplina.

<dl>
<dt>Baze podataka</dt>
<dd>
Ključna stvar je <b>kako pohraniti</b> podatke, tj. kako ih strukturirati na način koji omogućuje bržu obradu. Postoje različite vrste baza podataka koje pohranjuju strukturirane i nestrukturirane podatke, što <a href="../../2-Working-With-Data/README.md">ćemo razmotriti u našem tečaju</a>.
</dd>
<dt>Veliki podaci</dt>
<dd>
Često trebamo pohraniti i obraditi vrlo velike količine podataka s relativno jednostavnom strukturom. Postoje posebni pristupi i alati za pohranu tih podataka na distribuirani način na računalnom klasteru i njihovu učinkovitu obradu.
</dd>
<dt>Strojno učenje</dt>
<dd>
Jedan od načina za razumijevanje podataka je <b>izgradnja modela</b> koji će moći predvidjeti željeni ishod. Razvijanje modela iz podataka naziva se <b>strojno učenje</b>. Možete pogledati naš <a href="https://aka.ms/ml-beginners">Kurikulum za početnike u strojnom učenju</a> kako biste saznali više o tome.
</dd>
<dt>Umjetna inteligencija</dt>
<dd>
Područje strojnog učenja poznato kao umjetna inteligencija (AI) također se oslanja na podatke, a uključuje izgradnju složenih modela koji oponašaju ljudske procese razmišljanja. AI metode često nam omogućuju pretvaranje nestrukturiranih podataka (npr. prirodnog jezika) u strukturirane uvide. 
</dd>
<dt>Vizualizacija</dt>
<dd>
Velike količine podataka su nerazumljive za ljudsko biće, ali kada stvorimo korisne vizualizacije koristeći te podatke, možemo bolje razumjeti podatke i izvući zaključke. Stoga je važno poznavati mnoge načine vizualizacije informacija - nešto što ćemo obraditi u <a href="../../3-Data-Visualization/README.md">3. dijelu</a> našeg tečaja. Povezana područja uključuju i <b>infografiku</b> te općenito <b>interakciju čovjeka i računala</b>. 
</dd>
</dl>

## Vrste podataka

Kao što smo već spomenuli, podaci su svugdje. Samo ih trebamo uhvatiti na pravi način! Korisno je razlikovati **strukturirane** i **nestrukturirane** podatke. Prvi su obično predstavljeni u nekom dobro strukturiranom obliku, često kao tablica ili više tablica, dok su drugi samo zbirka datoteka. Ponekad možemo govoriti i o **polustrukturiranim** podacima, koji imaju neku vrstu strukture koja može značajno varirati.

| Strukturirani                                                               | Polustrukturirani                                                                            | Nestrukturirani                        |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | --------------------------------------- |
| Popis ljudi s njihovim telefonskim brojevima                                 | Wikipedijine stranice s poveznicama                                                         | Tekst Enciklopedije Britannica         |
| Temperatura u svim sobama zgrade svake minute u posljednjih 20 godina        | Zbirka znanstvenih radova u JSON formatu s autorima, datumom objave i sažetkom              | Datoteke s korporativnim dokumentima   |
| Podaci o dobi i spolu svih ljudi koji ulaze u zgradu                         | Internetske stranice                                                                         | Sirovi video zapis s nadzorne kamere   |

## Gdje pronaći podatke

Postoji mnogo mogućih izvora podataka, i nemoguće je nabrojati ih sve! Međutim, spomenimo neka tipična mjesta gdje možete pronaći podatke:

* **Strukturirani**
  - **Internet stvari** (IoT), uključujući podatke s različitih senzora, poput senzora temperature ili tlaka, pruža mnogo korisnih podataka. Na primjer, ako je poslovna zgrada opremljena IoT senzorima, možemo automatski kontrolirati grijanje i osvjetljenje kako bismo smanjili troškove. 
  - **Ankete** koje tražimo od korisnika da ispune nakon kupnje ili posjeta web stranici.
  - **Analiza ponašanja** može nam, na primjer, pomoći da razumijemo koliko duboko korisnik ulazi na stranicu i koji je tipičan razlog za napuštanje stranice.
* **Nestrukturirani**
  - **Tekstovi** mogu biti bogat izvor uvida, poput ukupnog **rezultata sentimenta** ili izdvajanja ključnih riječi i semantičkog značenja.
  - **Slike** ili **videozapisi**. Videozapis s nadzorne kamere može se koristiti za procjenu prometa na cesti i informiranje ljudi o potencijalnim gužvama.
  - **Zapisi web poslužitelja** mogu se koristiti za razumijevanje koje stranice naše web stranice se najčešće posjećuju i koliko dugo.
* Polustrukturirani
  - Grafovi **društvenih mreža** mogu biti izvrsni izvori podataka o osobnostima korisnika i potencijalnoj učinkovitosti u širenju informacija.
  - Kada imamo hrpu fotografija s zabave, možemo pokušati izvući podatke o **dinamici grupe** izgradnjom grafa ljudi koji se fotografiraju zajedno.

Poznavanjem različitih mogućih izvora podataka, možete razmisliti o različitim scenarijima u kojima se tehnike podatkovne znanosti mogu primijeniti za bolje razumijevanje situacije i poboljšanje poslovnih procesa. 

## Što možete učiniti s podacima

U podatkovnoj znanosti fokusiramo se na sljedeće korake u radu s podacima:

<dl>
<dt>1) Prikupljanje podataka</dt>
<dd>
Prvi korak je prikupljanje podataka. Iako u mnogim slučajevima to može biti jednostavan proces, poput podataka koji dolaze u bazu podataka iz web aplikacije, ponekad moramo koristiti posebne tehnike. Na primjer, podaci s IoT senzora mogu biti preplavljujući, pa je dobra praksa koristiti međutočke za prikupljanje podataka, poput IoT Hub-a, prije daljnje obrade.
</dd>
<dt>2) Pohrana podataka</dt>
<dd>
Pohranjivanje podataka može biti izazovno, posebno ako govorimo o velikim podacima. Kada odlučujemo kako pohraniti podatke, ima smisla predvidjeti način na koji ćemo ih željeti pretraživati u budućnosti. Postoji nekoliko načina na koje se podaci mogu pohraniti:
<ul>
<li>Relacijska baza podataka pohranjuje zbirku tablica i koristi poseban jezik nazvan SQL za njihovo pretraživanje. Tablice su obično organizirane u različite grupe nazvane sheme. U mnogim slučajevima moramo pretvoriti podatke iz izvornog oblika kako bi odgovarali shemi.</li>
<li><a href="https://en.wikipedia.org/wiki/NoSQL">NoSQL</a> baza podataka, poput <a href="https://azure.microsoft.com/services/cosmos-db/?WT.mc_id=academic-77958-bethanycheum">CosmosDB</a>, ne nameće sheme na podatke i omogućuje pohranu složenijih podataka, na primjer, hijerarhijskih JSON dokumenata ili grafova. Međutim, NoSQL baze podataka nemaju bogate mogućnosti pretraživanja kao SQL i ne mogu osigurati referencijalni integritet, tj. pravila o tome kako su podaci strukturirani u tablicama i upravljanje odnosima između tablica.</li>
<li><a href="https://en.wikipedia.org/wiki/Data_lake">Data Lake</a> pohrana koristi se za velike zbirke podataka u sirovom, nestrukturiranom obliku. Data lakeovi se često koriste s velikim podacima, gdje svi podaci ne mogu stati na jedan stroj i moraju se pohraniti i obraditi na klasteru poslužitelja. <a href="https://en.wikipedia.org/wiki/Apache_Parquet">Parquet</a> je format podataka koji se često koristi u kombinaciji s velikim podacima.</li> 
</ul>
</dd>
<dt>3) Obrada podataka</dt>
<dd>
Ovo je najuzbudljiviji dio rada s podacima, koji uključuje pretvaranje podataka iz izvornog oblika u oblik koji se može koristiti za vizualizaciju ili obuku modela. Kada radimo s nestrukturiranim podacima poput teksta ili slika, možda ćemo morati koristiti neke AI tehnike za izdvajanje <b>značajki</b> iz podataka, čime ih pretvaramo u strukturirani oblik.
</dd>
<dt>4) Vizualizacija / Ljudski uvidi</dt>
<dd>
Često, kako bismo razumjeli podatke, moramo ih vizualizirati. Imati mnogo različitih tehnika vizualizacije u našem alatu omogućuje nam pronalaženje pravog prikaza za dobivanje uvida. Često podatkovni znanstvenik mora "igrati se s podacima", vizualizirati ih mnogo puta i tražiti odnose. Također, možemo koristiti statističke tehnike za testiranje hipoteza ili dokazivanje korelacije između različitih dijelova podataka.   
</dd>
<dt>5) Obuka prediktivnog modela</dt>
<dd>
Budući da je krajnji cilj podatkovne znanosti donošenje odluka na temelju podataka, možda ćemo htjeti koristiti tehnike <a href="http://github.com/microsoft/ml-for-beginners">strojnog učenja</a> za izgradnju prediktivnog modela. Tada ga možemo koristiti za predviđanja koristeći nove skupove podataka slične strukture.
</dd>
</dl>

Naravno, ovisno o stvarnim podacima, neki koraci mogu nedostajati (npr. kada već imamo podatke u bazi podataka ili kada ne trebamo obuku modela), ili se neki koraci mogu ponoviti nekoliko puta (poput obrade podataka).

## Digitalizacija i digitalna transformacija

U posljednjem desetljeću, mnoge tvrtke počele su shvaćati važnost podataka pri donošenju poslovnih odluka. Kako bi primijenili principe podatkovne znanosti na vođenje poslovanja, prvo je potrebno prikupiti neke podatke, tj. prevesti poslovne procese u digitalni oblik. To je poznato kao **digitalizacija**. Primjena tehnika podatkovne znanosti na ove podatke za donošenje odluka može dovesti do značajnog povećanja produktivnosti (ili čak promjene poslovnog smjera), što se naziva **digitalna transformacija**.

Razmotrimo primjer. Pretpostavimo da imamo tečaj podatkovne znanosti (poput ovog) koji online dostavljamo studentima i želimo koristiti podatkovnu znanost za njegovo poboljšanje. Kako to možemo učiniti?

Možemo započeti pitanjem "Što se može digitalizirati?" Najjednostavniji način bio bi mjerenje vremena koje je svakom studentu potrebno za završetak svakog modula i mjerenje stečenog znanja davanjem testa s višestrukim izborom na kraju svakog modula. Prosječnim vremenom završetka među svim studentima možemo otkriti koji moduli uzrokuju najviše poteškoća studentima i raditi na njihovom pojednostavljivanju.
> Možete tvrditi da ovaj pristup nije idealan, jer moduli mogu biti različite duljine. Vjerojatno je pravednije podijeliti vrijeme s duljinom modula (u broju znakova) i usporediti te vrijednosti.

Kada počnemo analizirati rezultate testova s višestrukim izborom, možemo pokušati odrediti koje koncepte studenti imaju poteškoća razumjeti i koristiti te informacije za poboljšanje sadržaja. Da bismo to učinili, moramo osmisliti testove na način da svako pitanje odgovara određenom konceptu ili dijelu znanja.

Ako želimo ići još složenije, možemo prikazati vrijeme potrebno za svaki modul u odnosu na dobnu kategoriju studenata. Možda ćemo otkriti da za neke dobne kategorije treba neprikladno dugo vremena za dovršetak modula ili da studenti odustaju prije nego što ga završe. To nam može pomoći da damo preporuke za dobnu skupinu modula i smanjimo nezadovoljstvo ljudi zbog pogrešnih očekivanja.

## 🚀 Izazov

U ovom izazovu pokušat ćemo pronaći koncepte relevantne za područje Data Sciencea analizirajući tekstove. Uzet ćemo članak s Wikipedije o Data Scienceu, preuzeti i obraditi tekst, a zatim izraditi oblak riječi poput ovog:

![Oblak riječi za Data Science](../../../../translated_images/hr/ds_wordcloud.664a7c07dca57de017c22bf0498cb40f898d48aa85b3c36a80620fea12fadd42.png)

Posjetite [`notebook.ipynb`](../../../../1-Introduction/01-defining-data-science/notebook.ipynb ':ignore') kako biste pregledali kod. Također možete pokrenuti kod i vidjeti kako u stvarnom vremenu obavlja sve transformacije podataka.

> Ako ne znate kako pokrenuti kod u Jupyter Notebooku, pogledajte [ovaj članak](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## [Kviz nakon predavanja](https://ff-quizzes.netlify.app/en/ds/quiz/1)

## Zadaci

* **Zadatak 1**: Izmijenite gornji kod kako biste pronašli povezane koncepte za područja **Big Data** i **Machine Learning**
* **Zadatak 2**: [Razmislite o scenarijima za Data Science](assignment.md)

## Zasluge

Ovu lekciju je s ljubavlju napisao [Dmitry Soshnikov](http://soshnikov.com)

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.