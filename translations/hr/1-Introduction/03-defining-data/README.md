<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "356d12cffc3125db133a2d27b827a745",
  "translation_date": "2025-08-30T19:35:02+00:00",
  "source_file": "1-Introduction/03-defining-data/README.md",
  "language_code": "hr"
}
-->
# Definiranje Podataka

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Definiranje Podataka - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Podaci su činjenice, informacije, opažanja i mjerenja koja se koriste za otkrivanja i donošenje informiranih odluka. Točka podataka je pojedinačna jedinica podataka unutar skupa podataka, koji je zbirka točaka podataka. Skupovi podataka mogu dolaziti u različitim formatima i strukturama, a obično se temelje na svom izvoru, odnosno odakle podaci dolaze. Na primjer, mjesečni prihodi tvrtke mogu biti u proračunskoj tablici, dok podaci o otkucajima srca po satu s pametnog sata mogu biti u formatu [JSON](https://stackoverflow.com/a/383699). Uobičajeno je da znanstvenici koji se bave podacima rade s različitim vrstama podataka unutar skupa podataka.

Ova lekcija usredotočuje se na prepoznavanje i klasifikaciju podataka prema njihovim karakteristikama i izvorima.

## [Pre-Lekcijski Kviz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/4)

## Kako se Podaci Opisuju

### Sirovi Podaci
Sirovi podaci su podaci koji dolaze iz svog izvora u početnom stanju i nisu analizirani ili organizirani. Kako bi se razumjelo što se događa sa skupom podataka, potrebno ih je organizirati u format koji je razumljiv ljudima, kao i tehnologiji koju mogu koristiti za daljnju analizu. Struktura skupa podataka opisuje kako je organiziran i može se klasificirati kao strukturiran, nestrukturiran i polustrukturiran. Ove vrste struktura variraju ovisno o izvoru, ali će se na kraju uklopiti u ove tri kategorije.

### Kvantitativni Podaci
Kvantitativni podaci su numerička opažanja unutar skupa podataka i obično se mogu analizirati, mjeriti i koristiti matematički. Neki primjeri kvantitativnih podataka su: populacija zemlje, visina osobe ili kvartalni prihodi tvrtke. Uz dodatnu analizu, kvantitativni podaci mogli bi se koristiti za otkrivanje sezonskih trendova indeksa kvalitete zraka (AQI) ili procjenu vjerojatnosti prometne gužve u tipičnom radnom danu.

### Kvalitativni Podaci
Kvalitativni podaci, također poznati kao kategorijski podaci, su podaci koji se ne mogu objektivno mjeriti poput opažanja kvantitativnih podataka. Općenito su to različiti formati subjektivnih podataka koji bilježe kvalitetu nečega, poput proizvoda ili procesa. Ponekad su kvalitativni podaci numerički, ali se obično ne koriste matematički, poput telefonskih brojeva ili vremenskih oznaka. Neki primjeri kvalitativnih podataka su: komentari na videozapise, marka i model automobila ili omiljena boja vaših najbližih prijatelja. Kvalitativni podaci mogli bi se koristiti za razumijevanje koji proizvodi potrošačima najviše odgovaraju ili za identifikaciju popularnih ključnih riječi u životopisima za prijave na posao.

### Strukturirani Podaci
Strukturirani podaci su podaci organizirani u redove i stupce, gdje svaki red ima isti skup stupaca. Stupci predstavljaju vrijednost određenog tipa i identificiraju se imenom koje opisuje što vrijednost predstavlja, dok redovi sadrže stvarne vrijednosti. Stupci često imaju određeni skup pravila ili ograničenja za vrijednosti kako bi se osiguralo da vrijednosti točno predstavljaju stupac. Na primjer, zamislite proračunsku tablicu kupaca gdje svaki red mora imati telefonski broj, a telefonski brojevi nikada ne sadrže abecedne znakove. Mogu postojati pravila primijenjena na stupac telefonskog broja kako bi se osiguralo da nikada nije prazan i da sadrži samo brojeve.

Prednost strukturiranih podataka je ta što se mogu organizirati na način da se mogu povezati s drugim strukturiranim podacima. Međutim, budući da su podaci dizajnirani da budu organizirani na specifičan način, promjene u njihovoj ukupnoj strukturi mogu zahtijevati puno truda. Na primjer, dodavanje stupca za e-mail u proračunsku tablicu kupaca koji ne može biti prazan znači da ćete morati smisliti kako dodati te vrijednosti postojećim redovima kupaca u skupu podataka.

Primjeri strukturiranih podataka: proračunske tablice, relacijske baze podataka, telefonski brojevi, bankovni izvodi.

### Nestrukturirani Podaci
Nestrukturirani podaci obično se ne mogu kategorizirati u redove ili stupce i ne sadrže format ili skup pravila koja treba slijediti. Budući da nestrukturirani podaci imaju manje ograničenja u svojoj strukturi, lakše je dodati nove informacije u usporedbi sa strukturiranim skupom podataka. Ako senzor koji bilježi podatke o barometarskom tlaku svake 2 minute dobije ažuriranje koje mu omogućuje mjerenje i bilježenje temperature, to ne zahtijeva izmjenu postojećih podataka ako su nestrukturirani. Međutim, to može učiniti analizu ili istraživanje ovakvih podataka dugotrajnijim. Na primjer, znanstvenik koji želi pronaći prosječnu temperaturu prošlog mjeseca iz podataka senzora, ali otkriva da je senzor zabilježio "e" u nekim svojim podacima kako bi označio da je bio pokvaren umjesto tipičnog broja, što znači da su podaci nepotpuni.

Primjeri nestrukturiranih podataka: tekstualne datoteke, tekstualne poruke, video datoteke.

### Polustrukturirani Podaci
Polustrukturirani podaci imaju značajke koje ih čine kombinacijom strukturiranih i nestrukturiranih podataka. Obično ne odgovaraju formatu redova i stupaca, ali su organizirani na način koji se smatra strukturiranim i mogu slijediti fiksni format ili skup pravila. Struktura će varirati između izvora, od dobro definirane hijerarhije do nečega fleksibilnijeg što omogućuje jednostavnu integraciju novih informacija. Metapodaci su pokazatelji koji pomažu odlučiti kako su podaci organizirani i pohranjeni te će imati različita imena, ovisno o vrsti podataka. Neka uobičajena imena za metapodatke su oznake, elementi, entiteti i atributi. Na primjer, tipična e-mail poruka imat će predmet, tijelo i skup primatelja te se može organizirati prema tome tko ju je poslao ili kada je poslana.

Primjeri polustrukturiranih podataka: HTML, CSV datoteke, JavaScript Object Notation (JSON).

## Izvori Podataka

Izvor podataka je početna lokacija gdje su podaci generirani ili gdje "žive" i varirat će ovisno o tome kako i kada su prikupljeni. Podaci generirani od strane korisnika poznati su kao primarni podaci, dok sekundarni podaci dolaze iz izvora koji je prikupio podatke za opću upotrebu. Na primjer, skupina znanstvenika koja prikuplja opažanja u prašumi smatrala bi se primarnim izvorom, a ako odluče podijeliti podatke s drugim znanstvenicima, to bi se smatralo sekundarnim za one koji ih koriste.

Baze podataka su uobičajeni izvor i oslanjaju se na sustav za upravljanje bazama podataka za hosting i održavanje podataka, gdje korisnici koriste naredbe zvane upiti za istraživanje podataka. Datoteke kao izvori podataka mogu biti audio, slikovne i video datoteke, kao i proračunske tablice poput Excela. Internetski izvori su uobičajena lokacija za hosting podataka, gdje se baze podataka kao i datoteke mogu pronaći. Programski sučelji aplikacija, također poznata kao API-ji, omogućuju programerima stvaranje načina za dijeljenje podataka s vanjskim korisnicima putem interneta, dok proces web scraping-a izvlači podatke s web stranice. [Lekcije u radu s podacima](../../../../../../../../../2-Working-With-Data) usredotočuju se na to kako koristiti različite izvore podataka.

## Zaključak

U ovoj lekciji naučili smo:

- Što su podaci
- Kako se podaci opisuju
- Kako se podaci klasificiraju i kategoriziraju
- Gdje se podaci mogu pronaći

## 🚀 Izazov

Kaggle je izvrstan izvor otvorenih skupova podataka. Koristite [alat za pretraživanje skupova podataka](https://www.kaggle.com/datasets) kako biste pronašli nekoliko zanimljivih skupova podataka i klasificirali 3-5 skupova podataka prema ovim kriterijima:

- Jesu li podaci kvantitativni ili kvalitativni?
- Jesu li podaci strukturirani, nestrukturirani ili polustrukturirani?

## [Post-Lekcijski Kviz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/5)

## Pregled i Samostalno Učenje

- Ova jedinica na Microsoft Learn-u, pod nazivom [Klasificirajte svoje podatke](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/2-classify-data), ima detaljan pregled strukturiranih, polustrukturiranih i nestrukturiranih podataka.

## Zadatak

[Klasifikacija Skupova Podataka](assignment.md)

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.