<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a0516588d172f82f35f7a0d4a001e5d0",
  "translation_date": "2025-09-05T19:28:12+00:00",
  "source_file": "1-Introduction/01-defining-data-science/README.md",
  "language_code": "hr"
}
-->
## Vrste podataka

Kao što smo već spomenuli, podaci su svugdje oko nas. Samo ih trebamo pravilno zabilježiti! Korisno je razlikovati **strukturirane** i **nestrukturirane** podatke. Strukturirani podaci obično su predstavljeni u nekom dobro organiziranom obliku, često kao tablica ili niz tablica, dok su nestrukturirani podaci samo zbirka datoteka. Ponekad možemo govoriti i o **polustrukturiranim** podacima, koji imaju neku vrstu strukture koja može značajno varirati.

| Strukturirani                                                               | Polustrukturirani                                                                             | Nestrukturirani                        |
| ---------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | --------------------------------------- |
| Popis ljudi s njihovim telefonskim brojevima                                 | Wikipedijine stranice s poveznicama                                                          | Tekst Enciklopedije Britannica         |
| Temperatura u svim sobama zgrade svake minute tijekom posljednjih 20 godina | Zbirka znanstvenih radova u JSON formatu s autorima, datumom objave i sažetkom               | Datoteke s korporativnim dokumentima   |
| Podaci o dobi i spolu svih ljudi koji ulaze u zgradu                         | Internetske stranice                                                                          | Sirovi videozapis s nadzorne kamere    |

## Odakle dobiti podatke

Postoji mnogo mogućih izvora podataka, i bilo bi nemoguće nabrojati ih sve! Međutim, spomenimo neke od tipičnih mjesta gdje možete dobiti podatke:

* **Strukturirani**
  - **Internet stvari** (IoT), uključujući podatke s različitih senzora, poput senzora temperature ili tlaka, pruža mnogo korisnih podataka. Na primjer, ako je poslovna zgrada opremljena IoT senzorima, možemo automatski kontrolirati grijanje i rasvjetu kako bismo smanjili troškove.
  - **Ankete** koje tražimo od korisnika da ispune nakon kupnje ili posjeta web stranici.
  - **Analiza ponašanja** može nam, na primjer, pomoći da razumijemo koliko duboko korisnik ulazi na stranicu i koji je tipičan razlog za napuštanje stranice.
* **Nestrukturirani**
  - **Tekstovi** mogu biti bogat izvor uvida, poput ukupnog **sentiment rezultata** ili izdvajanja ključnih riječi i semantičkog značenja.
  - **Slike** ili **videozapisi**. Videozapis s nadzorne kamere može se koristiti za procjenu prometa na cesti i obavještavanje ljudi o potencijalnim gužvama.
  - **Dnevnici** web poslužitelja mogu se koristiti za razumijevanje koje stranice naše web stranice se najčešće posjećuju i koliko dugo.
* Polustrukturirani
  - **Grafovi društvenih mreža** mogu biti izvrsni izvori podataka o osobnostima korisnika i potencijalnoj učinkovitosti u širenju informacija.
  - Kada imamo niz fotografija s zabave, možemo pokušati izvući podatke o **dinamici grupe** izradom grafa ljudi koji se fotografiraju zajedno.

Poznavanjem različitih mogućih izvora podataka možete razmišljati o različitim scenarijima u kojima se tehnike znanosti o podacima mogu primijeniti za bolje razumijevanje situacije i poboljšanje poslovnih procesa.

## Što možete učiniti s podacima

U znanosti o podacima fokusiramo se na sljedeće korake u radu s podacima:

Naravno, ovisno o stvarnim podacima, neki koraci mogu nedostajati (npr. kada već imamo podatke u bazi podataka ili kada nije potrebno treniranje modela), ili se neki koraci mogu ponoviti nekoliko puta (poput obrade podataka).

## Digitalizacija i digitalna transformacija

U posljednjem desetljeću mnoge su tvrtke počele shvaćati važnost podataka pri donošenju poslovnih odluka. Kako bi se primijenili principi znanosti o podacima na vođenje poslovanja, prvo je potrebno prikupiti neke podatke, tj. prevesti poslovne procese u digitalni oblik. To se naziva **digitalizacija**. Primjena tehnika znanosti o podacima na te podatke za donošenje odluka može dovesti do značajnih povećanja produktivnosti (ili čak poslovnog zaokreta), što nazivamo **digitalnom transformacijom**.

Razmotrimo primjer. Pretpostavimo da imamo tečaj znanosti o podacima (poput ovog) koji se online dostavlja studentima, i želimo koristiti znanost o podacima za njegovo poboljšanje. Kako to možemo učiniti?

Možemo započeti pitanjem "Što se može digitalizirati?" Najjednostavniji način bio bi mjerenje vremena koje svakom studentu treba za dovršavanje svakog modula, te mjerenje stečenog znanja davanjem testa s višestrukim izborom na kraju svakog modula. Prosječnim vremenom dovršavanja među svim studentima možemo otkriti koji moduli uzrokuju najviše poteškoća studentima i raditi na njihovom pojednostavljivanju.
Možete tvrditi da ovaj pristup nije idealan, jer moduli mogu biti različitih duljina. Vjerojatno je pravednije podijeliti vrijeme s duljinom modula (u broju znakova) i usporediti te vrijednosti umjesto toga.
Kada počnemo analizirati rezultate testova s višestrukim izborom, možemo pokušati odrediti koje koncepte učenici imaju poteškoća razumjeti i koristiti te informacije za poboljšanje sadržaja. Da bismo to učinili, moramo osmisliti testove na način da svako pitanje odgovara određenom konceptu ili dijelu znanja.

Ako želimo ići još dalje, možemo prikazati vrijeme potrebno za svaki modul u odnosu na dobnu kategoriju učenika. Možda ćemo otkriti da za neke dobne kategorije treba neprikladno dugo vremena za dovršavanje modula ili da učenici odustaju prije nego što ga završe. To nam može pomoći da damo preporuke za module prema dobi i smanjimo nezadovoljstvo ljudi zbog pogrešnih očekivanja.

## 🚀 Izazov

U ovom izazovu pokušat ćemo pronaći koncepte relevantne za područje Data Science analizirajući tekstove. Uzet ćemo Wikipedia članak o Data Science, preuzeti i obraditi tekst, a zatim izraditi oblak riječi poput ovog:

![Oblak riječi za Data Science](../../../../1-Introduction/01-defining-data-science/images/ds_wordcloud.png)

Posjetite [`notebook.ipynb`](../../../../../../../../../1-Introduction/01-defining-data-science/notebook.ipynb ':ignore') kako biste pregledali kod. Također možete pokrenuti kod i vidjeti kako u stvarnom vremenu obavlja sve transformacije podataka.

> Ako ne znate kako pokrenuti kod u Jupyter Notebooku, pogledajte [ovaj članak](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## [Kviz nakon predavanja](https://ff-quizzes.netlify.app/en/ds/quiz/1)

## Zadaci

* **Zadatak 1**: Modificirajte gornji kod kako biste pronašli povezane koncepte za područja **Big Data** i **Machine Learning**
* **Zadatak 2**: [Razmislite o scenarijima za Data Science](assignment.md)

## Zasluge

Ovu lekciju je s ljubavlju napisao [Dmitry Soshnikov](http://soshnikov.com)

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.