# Definiranje podataka

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Definiranje podataka - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Podaci su činjenice, informacije, opažanja i mjerenja koja se koriste za otkrivanja i podršku informiranim odlukama. Podatkovna točka je jedinstvena jedinica podataka unutar skupa podataka, koji je zbirka podatkovnih točaka. Skupovi podataka mogu biti u različitim formatima i strukturama, i obično se temelje na svom izvoru ili odakle podaci dolaze. Na primjer, mjesečni prihodi tvrtke mogu biti u proračunskoj tablici, ali podatak o otkucajima srca po satu sa pametnog sata može biti u [JSON](https://stackoverflow.com/a/383699) formatu. Uobičajeno je da znanstvenici podataka rade s različitim vrstama podataka unutar skupa podataka.

Ova lekcija se fokusira na identificiranje i klasifikaciju podataka prema njihovim karakteristikama i izvorima.

## [Predavanje kviz](https://ff-quizzes.netlify.app/en/ds/quiz/4)
## Kako se podaci opisuje

### Neobrađeni podaci
Neobrađeni podaci su podaci koji su došli iz svog izvora u svom izvornom stanju i nisu analizirani niti organizirani. Kako bismo razumjeli što se događa s nekim skupom podataka, potrebno ga je organizirati u format koji mogu razumjeti ljudi kao i tehnologija koju koriste za daljnju analizu. Struktura skupa podataka opisuje kako je organizirana i može se klasificirati kao strukturirana, nestrukturirana i polustrukturirana. Ovi tipovi strukture variraju ovisno o izvoru, ali se konačno uklapaju u ove tri kategorije.

### Kvantitativni podaci
Kvantitativni podaci su numerička opažanja unutar skupa podataka i mogu se tipično analizirati, mjeriti i matematički koristiti. Neki primjeri kvantitativnih podataka su: populacija neke zemlje, visina osobe ili kvartalni prihodi tvrtke. Uz dodatnu analizu, kvantitativni podaci mogu se koristiti za otkrivanje sezonskih trendova indeksa kvalitete zraka (AQI) ili procjenu vjerojatnosti prometnog špica na uobičajeni radni dan.

### Kvalitativni podaci
Kvalitativni podaci, poznati i kao kategorizirani podaci, su podaci koji se ne mogu objektivno mjeriti poput opažanja kvantitativnih podataka. Generalno su razni formati subjektivnih podataka koji bilježe kvalitetu nečega, poput proizvoda ili procesa. Ponekad kvalitativni podaci mogu biti numerički, ali se obično ne koriste matematički, kao što su brojevi telefona ili vremenski oznake. Neki primjeri kvalitativnih podataka su: komentari na video, marka i model automobila ili najdraža boja vaših najbližih prijatelja. Kvalitativni podaci mogu se koristiti za razumijevanje koji proizvodi su najpopularniji kod potrošača ili za prepoznavanje popularnih ključnih riječi u životopisima za posao.

### Strukturirani podaci
Strukturirani podaci su podaci organizirani u retke i stupce, gdje svaki redak ima isti skup stupaca. Stupci predstavljaju vrijednost određenog tipa i bit će označeni imenom koje opisuje što vrijednost predstavlja, dok retci sadrže stvarne vrijednosti. Stupci često imaju specifičan skup pravila ili ograničenja na vrijednosti kako bi se osiguralo da vrijednosti točno predstavljaju stupac. Na primjer, zamislite proračunsku tablicu kupaca gdje svaki redak mora imati broj telefona i brojevi nikada ne smiju sadržavati slova. Mogu se primijeniti pravila na stupac broja telefona kako bi se osiguralo da nikada nije prazan i sadrži samo brojeve.

Prednost strukturiranih podataka je što se mogu organizirati na način da se mogu povezati s drugim strukturiranim podacima. Međutim, budući da su podaci dizajnirani da budu organizirani na specifičan način, promjene u cjelokupnoj strukturi mogu zahtijevati mnogo truda. Na primjer, dodavanje stupca za e-poštu u tablicu kupaca koji ne smije biti prazan znači da ćete morati osmisliti kako te vrijednosti dodati postojećim redovima kupaca u skupu podataka.

Primjeri strukturiranih podataka: proračunske tablice, relacijske baze podataka, brojevi telefona, bankovni izvodi

### Nestrukturirani podaci
Nestrukturirani podaci se obično ne mogu kategorizirati u retke ili stupce i nemaju format ili set pravila koja se slijede. Budući da nestrukturirani podaci imaju manje ograničenja svoje strukture, lakše je dodavati nove informacije u usporedbi sa strukturiranim skupom podataka. Ako senzor koji bilježi podatke o barometarskom pritisku svakih 2 minute dobije nadogradnju koja mu sada omogućuje mjerenje i bilježenje temperature, za nestrukturirane podatke nije potrebno mijenjati postojeće podatke. Međutim, to može otežati ili produžiti analizu i istraživanje takvih podataka. Na primjer, znanstvenik koji želi pronaći prosječnu temperaturu za prošli mjesec iz podataka senzora, ali otkrije da je senzor u nekim zapisima unio "e" da označi da je bio pokvaren umjesto očekivanog broja, što znači da su podaci nepotpuni.

Primjeri nestrukturiranih podataka: tekstualne datoteke, tekstualne poruke, video datoteke

### Polustrukturirani podaci
Polustrukturirani podaci imaju značajke koje ih čine kombinacijom strukturiranih i nestrukturiranih podataka. Obično ne slijede format redaka i stupaca, ali su organizirani na način koji se smatra strukturiranim i mogu slijediti fiksni format ili skup pravila. Struktura varira među izvorima, od jasno definiranih hijerarhija do fleksibilnijih formata koji omogućuju jednostavnu integraciju novih informacija. Metapodaci su indikatori koji pomažu odrediti kako su podaci organizirani i pohranjeni i imate različite nazive ovisno o vrsti podataka. Neki uobičajeni nazivi metapodataka su oznake, elementi, entiteti i atributi. Na primjer, tipična e-mail poruka ima predmet, tijelo i skup primatelja te može biti organizirana po tome tko ju je poslao ili kada.

Primjeri polustrukturiranih podataka: HTML, CSV datoteke, JavaScript Object Notation (JSON)

## Izvori podataka

Izvor podataka je početna lokacija gdje su podaci generirani ili gdje "žive" te varira ovisno o načinu i vremenu prikupljanja. Podatke koje generira korisnik (ili korisnici) nazivamo primarnim podacima, dok sekundarni podaci dolaze iz izvora koji je prikupio podatke za opću uporabu. Na primjer, skupina znanstvenika koji prikuplja opažanja u prašumi smatraju se primarnim izvorom podataka, a ako odluče podijeliti te podatke s drugim znanstvenicima, ti podaci postaju sekundarni za one koji ih koriste.

Baze podataka su čest izvor i oslanjaju se na sustav za upravljanje bazama podataka koji domaćini i održavaju podatke gdje korisnici koriste naredbe zvane upiti za istraživanje podataka. Datoteke kao izvori podataka mogu biti audio, slikovne i video datoteke kao i proračunske tablice poput Excela. Internetski izvori su česta lokacija za pohranu podataka, gdje se mogu pronaći baze podataka kao i datoteke. Sučelja za programiranje aplikacija, poznata kao API-ji, omogućuju programerima stvaranje načina za dijeljenje podataka s vanjskim korisnicima putem interneta, dok proces web scrapinga izvlači podatke s web stranice. [Lekcije u radu s podacima](../../../../../../../../../2-Working-With-Data) fokusiraju se na korištenje raznih izvora podataka.

## Zaključak

U ovoj lekciji smo naučili:

- Što su podaci
- Kako se podaci opisuju
- Kako se podaci klasificiraju i kategoriziraju
- Gdje se podaci mogu pronaći

## 🚀 Izazov

Kaggle je izvrstan izvor otvorenih skupova podataka. Koristi [alat za pretragu datasetova](https://www.kaggle.com/datasets) da pronađeš zanimljive skupove podataka i klasificiraj 3-5 skupova prema ovim kriterijima:

- Jesu li podaci kvantitativni ili kvalitativni?
- Jesu li podaci strukturirani, nestrukturirani ili polustrukturirani?

## [Kviz nakon predavanja](https://ff-quizzes.netlify.app/en/ds/quiz/5)



## Pregled i samostalno učenje

- Ovaj Microsoft Learn modul, pod nazivom [Identificiranje formata podataka](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats?pivots=text) sadrži detaljan pregled strukturiranih, polustrukturiranih i nestrukturiranih podataka.

## Zadatak

[Klasificiranje skupova podataka](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->