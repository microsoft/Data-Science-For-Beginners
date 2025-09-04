<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "79ca8a5a3135e94d2d43f56ba62d5205",
  "translation_date": "2025-09-04T21:58:40+00:00",
  "source_file": "4-Data-Science-Lifecycle/14-Introduction/README.md",
  "language_code": "hr"
}
-->
# Uvod u životni ciklus podatkovne znanosti

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/14-DataScience-Lifecycle.png)|
|:---:|
| Uvod u životni ciklus podatkovne znanosti - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## [Prethodni kviz](https://red-water-0103e7a0f.azurestaticapps.net/quiz/26)

Do sada ste vjerojatno shvatili da je podatkovna znanost proces. Taj proces može se podijeliti u 5 faza:

- Prikupljanje
- Obrada
- Analiza
- Komunikacija
- Održavanje

Ova lekcija fokusira se na 3 dijela životnog ciklusa: prikupljanje, obrada i održavanje.

![Dijagram životnog ciklusa podatkovne znanosti](../../../../4-Data-Science-Lifecycle/14-Introduction/images/data-science-lifecycle.jpg)
> Fotografija od [Berkeley School of Information](https://ischoolonline.berkeley.edu/data-science/what-is-data-science/)

## Prikupljanje

Prva faza životnog ciklusa vrlo je važna jer su sljedeće faze ovisne o njoj. Praktički se radi o dvije faze spojene u jednu: prikupljanje podataka i definiranje svrhe i problema koji se trebaju riješiti.  
Definiranje ciljeva projekta zahtijeva dublji kontekst problema ili pitanja. Prvo, potrebno je identificirati i uključiti one kojima je potrebno rješenje problema. To mogu biti dionici u poslovanju ili sponzori projekta, koji mogu pomoći u identificiranju tko ili što će imati koristi od ovog projekta, kao i što i zašto im je to potrebno. Dobro definiran cilj trebao bi biti mjerljiv i kvantificiran kako bi se odredio prihvatljiv rezultat.  

Pitanja koja podatkovni znanstvenik može postaviti:
- Je li ovaj problem već bio obrađivan? Što je otkriveno?
- Je li svrha i cilj razumljiv svima uključenima?
- Postoji li nejasnoća i kako je smanjiti?
- Koja su ograničenja?
- Kako bi mogao izgledati krajnji rezultat?
- Koliko resursa (vrijeme, ljudi, računalni) je dostupno?

Sljedeći korak je identificiranje, prikupljanje, a zatim istraživanje podataka potrebnih za postizanje definiranih ciljeva. U ovoj fazi prikupljanja, podatkovni znanstvenici također moraju procijeniti količinu i kvalitetu podataka. To zahtijeva određeno istraživanje podataka kako bi se potvrdilo da će prikupljeni podaci podržati postizanje željenog rezultata.  

Pitanja koja podatkovni znanstvenik može postaviti o podacima:
- Koji podaci su mi već dostupni?
- Tko je vlasnik tih podataka?
- Koji su problemi privatnosti? 
- Imam li dovoljno podataka za rješavanje ovog problema?
- Jesu li podaci prihvatljive kvalitete za ovaj problem?
- Ako otkrijem dodatne informacije kroz ove podatke, trebamo li razmotriti promjenu ili redefiniranje ciljeva?

## Obrada

Faza obrade u životnom ciklusu fokusira se na otkrivanje obrazaca u podacima kao i na modeliranje. Neke tehnike koje se koriste u fazi obrade zahtijevaju statističke metode za otkrivanje obrazaca. Obično bi ovo bio zamoran zadatak za čovjeka s velikim skupom podataka, pa se oslanjamo na računala kako bi ubrzala proces. Ova faza također je mjesto gdje se podatkovna znanost i strojno učenje preklapaju. Kao što ste naučili u prvoj lekciji, strojno učenje je proces izgradnje modela za razumijevanje podataka. Modeli su prikaz odnosa između varijabli u podacima koji pomažu u predviđanju ishoda.

Uobičajene tehnike koje se koriste u ovoj fazi pokrivene su u kurikulumu ML za početnike. Slijedite poveznice kako biste saznali više o njima:

- [Klasifikacija](https://github.com/microsoft/ML-For-Beginners/tree/main/4-Classification): Organiziranje podataka u kategorije radi učinkovitije upotrebe.
- [Grupiranje](https://github.com/microsoft/ML-For-Beginners/tree/main/5-Clustering): Grupiranje podataka u slične skupine.
- [Regresija](https://github.com/microsoft/ML-For-Beginners/tree/main/2-Regression): Utvrđivanje odnosa između varijabli za predviđanje ili prognozu vrijednosti.

## Održavanje

Na dijagramu životnog ciklusa možda ste primijetili da održavanje stoji između prikupljanja i obrade. Održavanje je kontinuirani proces upravljanja, pohrane i osiguravanja podataka tijekom cijelog procesa projekta i treba ga uzeti u obzir tijekom cijelog trajanja projekta.  

### Pohrana podataka

Razmatranja o tome kako i gdje se podaci pohranjuju mogu utjecati na trošak njihove pohrane kao i na performanse brzine pristupa podacima. Odluke poput ovih vjerojatno neće donositi samo podatkovni znanstvenik, ali se može naći u situaciji da donosi odluke o tome kako raditi s podacima na temelju načina njihove pohrane.

Evo nekih aspekata modernih sustava za pohranu podataka koji mogu utjecati na te odluke:  

**Na lokaciji vs izvan lokacije vs javni ili privatni oblak**

Na lokaciji odnosi se na upravljanje podacima na vlastitoj opremi, poput posjedovanja servera s tvrdim diskovima koji pohranjuju podatke, dok se izvan lokacije oslanja na opremu koju ne posjedujete, poput podatkovnog centra. Javni oblak popularan je izbor za pohranu podataka koji ne zahtijeva znanje o tome kako ili gdje su točno podaci pohranjeni, gdje se javni odnosi na jedinstvenu osnovnu infrastrukturu koju dijele svi korisnici oblaka. Neke organizacije imaju stroge sigurnosne politike koje zahtijevaju da imaju potpuni pristup opremi na kojoj su podaci pohranjeni i oslanjaju se na privatni oblak koji pruža vlastite usluge oblaka. Više o podacima u oblaku naučit ćete u [kasnijim lekcijama](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/5-Data-Science-In-Cloud).

**Hladni vs vrući podaci**

Kada trenirate svoje modele, možda će vam trebati više podataka za treniranje. Ako ste zadovoljni svojim modelom, dolazit će novi podaci kako bi model služio svojoj svrsi. U svakom slučaju, trošak pohrane i pristupa podacima povećavat će se kako ih akumulirate. Razdvajanje rijetko korištenih podataka, poznatih kao hladni podaci, od često korištenih vrućih podataka može biti jeftinija opcija za pohranu podataka putem hardverskih ili softverskih usluga. Ako je potrebno pristupiti hladnim podacima, može potrajati malo duže u usporedbi s vrućim podacima.

### Upravljanje podacima

Dok radite s podacima, možete otkriti da neke od njih treba očistiti koristeći neke od tehnika pokrivenih u lekciji usmjerenoj na [pripremu podataka](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/08-data-preparation) kako biste izgradili točne modele. Kada stignu novi podaci, bit će potrebne iste primjene kako bi se održala dosljednost u kvaliteti. Neki projekti uključuju korištenje automatiziranog alata za čišćenje, agregaciju i kompresiju prije nego što se podaci premjeste na svoje konačno mjesto. Azure Data Factory je primjer jednog od tih alata.

### Osiguravanje podataka

Jedan od glavnih ciljeva osiguravanja podataka je osigurati da oni koji rade s podacima kontroliraju što se prikuplja i u kojem kontekstu se koristi. Održavanje sigurnosti podataka uključuje ograničavanje pristupa samo onima kojima je potreban, pridržavanje lokalnih zakona i propisa, kao i održavanje etičkih standarda, kao što je pokriveno u [lekciji o etici](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/02-ethics).  

Evo nekih stvari koje tim može učiniti s obzirom na sigurnost:
- Potvrditi da su svi podaci šifrirani
- Pružiti korisnicima informacije o tome kako se njihovi podaci koriste
- Ukloniti pristup podacima onima koji su napustili projekt 
- Dopustiti samo određenim članovima projekta da mijenjaju podatke

## 🚀 Izazov

Postoji mnogo verzija životnog ciklusa podatkovne znanosti, gdje svaki korak može imati različita imena i broj faza, ali će sadržavati iste procese spomenute u ovoj lekciji.

Istražite [Team Data Science Process lifecycle](https://docs.microsoft.com/en-us/azure/architecture/data-science-process/lifecycle) i [Cross-industry standard process for data mining](https://www.datascience-pm.com/crisp-dm-2/). Navedite 3 sličnosti i razlike između njih.

|Team Data Science Process (TDSP)|Cross-industry standard process for data mining (CRISP-DM)|
|--|--|
|![Team Data Science Lifecycle](../../../../4-Data-Science-Lifecycle/14-Introduction/images/tdsp-lifecycle2.png) | ![Data Science Process Alliance Image](../../../../4-Data-Science-Lifecycle/14-Introduction/images/CRISP-DM.png) |
| Slika od [Microsoft](https://docs.microsoft.comazure/architecture/data-science-process/lifecycle) | Slika od [Data Science Process Alliance](https://www.datascience-pm.com/crisp-dm-2/) |

## [Kviz nakon lekcije](https://ff-quizzes.netlify.app/en/ds/)

## Pregled i samostalno učenje

Primjena životnog ciklusa podatkovne znanosti uključuje više uloga i zadataka, gdje se neki mogu fokusirati na određene dijelove svake faze. Team Data Science Process pruža nekoliko resursa koji objašnjavaju vrste uloga i zadataka koje netko može imati u projektu.

* [Uloge i zadaci u procesu podatkovne znanosti](https://docs.microsoft.com/en-us/azure/architecture/data-science-process/roles-tasks)
* [Izvršavanje zadataka podatkovne znanosti: istraživanje, modeliranje i implementacija](https://docs.microsoft.com/en-us/azure/architecture/data-science-process/execute-data-science-tasks)

## Zadatak

[Procjena skupa podataka](assignment.md)

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prijevod [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane stručnjaka. Ne preuzimamo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije proizašle iz korištenja ovog prijevoda.