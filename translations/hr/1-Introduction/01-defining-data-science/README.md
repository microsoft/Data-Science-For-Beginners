<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2583a9894af7123b2fcae3376b14c035",
  "translation_date": "2025-08-30T19:28:10+00:00",
  "source_file": "1-Introduction/01-defining-data-science/README.md",
  "language_code": "hr"
}
-->
## Vrste podataka

Kao što smo već spomenuli, podaci su svugdje oko nas. Samo ih trebamo pravilno zabilježiti! Korisno je razlikovati **strukturirane** i **nestrukturirane** podatke. Prvi su obično predstavljeni u nekom dobro strukturiranom obliku, često kao tablica ili niz tablica, dok su potonji samo zbirka datoteka. Ponekad možemo govoriti i o **polustrukturiranim** podacima, koji imaju neku vrstu strukture koja može značajno varirati.

| Strukturirani                                                              | Polustrukturirani                                                                                 | Nestrukturirani                        |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | -------------------------------------- |
| Popis ljudi s njihovim telefonskim brojevima                               | Wikipedijine stranice s poveznicama                                                               | Tekst Enciklopedije Britannica         |
| Temperatura u svim sobama zgrade svake minute tijekom posljednjih 20 godina | Zbirka znanstvenih radova u JSON formatu s autorima, datumima objave i sažecima                   | Datoteke s korporativnim dokumentima   |
| Podaci o dobi i spolu svih ljudi koji ulaze u zgradu                       | Internetske stranice                                                                               | Sirovi videozapis s nadzorne kamere    |

## Gdje pronaći podatke

Postoji mnogo mogućih izvora podataka, i bilo bi nemoguće nabrojati ih sve! Međutim, spomenimo neka od tipičnih mjesta gdje možete pronaći podatke:

* **Strukturirani**
  - **Internet stvari** (IoT), uključujući podatke s različitih senzora, poput senzora temperature ili tlaka, pruža mnogo korisnih podataka. Na primjer, ako je poslovna zgrada opremljena IoT senzorima, možemo automatski kontrolirati grijanje i rasvjetu kako bismo smanjili troškove.
  - **Ankete** koje tražimo od korisnika da ispune nakon kupnje ili posjeta web stranici.
  - **Analiza ponašanja** može nam, primjerice, pomoći razumjeti koliko duboko korisnik ulazi na stranicu i koji je tipičan razlog za napuštanje stranice.
* **Nestrukturirani**
  - **Tekstovi** mogu biti bogat izvor uvida, poput ukupnog **sentiment skora** ili izdvajanja ključnih riječi i semantičkog značenja.
  - **Slike** ili **videozapisi**. Videozapis s nadzorne kamere može se koristiti za procjenu prometa na cesti i informiranje ljudi o mogućim gužvama.
  - **Zapisi web poslužitelja** mogu se koristiti za razumijevanje koje stranice naše web stranice se najčešće posjećuju i koliko dugo.
* **Polustrukturirani**
  - **Grafovi društvenih mreža** mogu biti izvrsni izvori podataka o osobnostima korisnika i potencijalnoj učinkovitosti u širenju informacija.
  - Kada imamo niz fotografija s neke zabave, možemo pokušati izvući podatke o **dinamici grupe** izgradnjom grafa ljudi koji se fotografiraju zajedno.

Poznavanjem različitih mogućih izvora podataka, možete razmisliti o različitim scenarijima u kojima se tehnike znanosti o podacima mogu primijeniti kako biste bolje razumjeli situaciju i poboljšali poslovne procese.

## Što možete učiniti s podacima

U znanosti o podacima fokusiramo se na sljedeće korake u radu s podacima:

Naravno, ovisno o stvarnim podacima, neki koraci mogu nedostajati (npr. kada već imamo podatke u bazi podataka ili kada nije potrebno treniranje modela), ili se neki koraci mogu ponavljati nekoliko puta (poput obrade podataka).

## Digitalizacija i digitalna transformacija

U posljednjem desetljeću mnoge su tvrtke počele shvaćati važnost podataka pri donošenju poslovnih odluka. Kako bi se primijenili principi znanosti o podacima na vođenje poslovanja, prvo je potrebno prikupiti neke podatke, tj. prevesti poslovne procese u digitalni oblik. To se naziva **digitalizacija**. Primjena tehnika znanosti o podacima na te podatke za donošenje odluka može dovesti do značajnog povećanja produktivnosti (ili čak promjene poslovnog smjera), što nazivamo **digitalnom transformacijom**.

Razmotrimo primjer. Pretpostavimo da imamo tečaj znanosti o podacima (poput ovog) koji se održava online za studente, i želimo koristiti znanost o podacima kako bismo ga poboljšali. Kako to možemo učiniti?

Možemo započeti pitanjem "Što se može digitalizirati?" Najjednostavniji način bio bi mjeriti vrijeme koje je svakom studentu potrebno za završetak svakog modula i mjeriti stečeno znanje davanjem testa s višestrukim izborom na kraju svakog modula. Prosječnim vremenom završetka za sve studente možemo otkriti koji moduli uzrokuju najviše poteškoća studentima i raditi na njihovom pojednostavljivanju.
Možete tvrditi da ovaj pristup nije idealan, jer moduli mogu biti različitih duljina. Vjerojatno je pravednije podijeliti vrijeme s duljinom modula (u broju znakova) i usporediti te vrijednosti umjesto toga.
Kada počnemo analizirati rezultate testova s višestrukim izborom, možemo pokušati utvrditi koje koncepte učenici teško razumiju i koristiti te informacije za poboljšanje sadržaja. Da bismo to postigli, trebamo osmisliti testove na način da svako pitanje odgovara određenom konceptu ili dijelu znanja.

Ako želimo ići još dalje, možemo usporediti vrijeme potrebno za svaki modul s dobnim kategorijama učenika. Možda ćemo otkriti da za neke dobne kategorije treba neproporcionalno dugo da završe modul ili da učenici odustaju prije nego što ga završe. To nam može pomoći da damo preporuke za dobne skupine za modul i smanjimo nezadovoljstvo zbog pogrešnih očekivanja.

## 🚀 Izazov

U ovom izazovu pokušat ćemo pronaći koncepte relevantne za područje Data Science analizirajući tekstove. Uzet ćemo članak s Wikipedije o Data Science, preuzeti i obraditi tekst, a zatim izraditi oblak riječi poput ovog:

![Oblak riječi za Data Science](../../../../translated_images/ds_wordcloud.664a7c07dca57de017c22bf0498cb40f898d48aa85b3c36a80620fea12fadd42.hr.png)

Posjetite [`notebook.ipynb`](../../../../../../../../../1-Introduction/01-defining-data-science/notebook.ipynb ':ignore') kako biste pregledali kod. Također možete pokrenuti kod i vidjeti kako u stvarnom vremenu provodi sve transformacije podataka.

> Ako ne znate kako pokrenuti kod u Jupyter Notebooku, pogledajte [ovaj članak](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## [Kviz nakon predavanja](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/1)

## Zadaci

* **Zadatak 1**: Izmijenite gornji kod kako biste pronašli povezane koncepte za područja **Big Data** i **Machine Learning**
* **Zadatak 2**: [Razmislite o scenarijima za Data Science](assignment.md)

## Zahvale

Ovu lekciju s ljubavlju je napisao [Dmitry Soshnikov](http://soshnikov.com)

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.