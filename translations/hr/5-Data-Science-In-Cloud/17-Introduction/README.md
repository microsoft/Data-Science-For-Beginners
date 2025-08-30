<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "408c55cab2880daa4e78616308bd5db7",
  "translation_date": "2025-08-30T17:47:02+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "hr"
}
-->
# Uvod u podatkovnu znanost u oblaku

|![ Sketchnote autora [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Podatkovna znanost u oblaku: Uvod - _Sketchnote autora [@nitya](https://twitter.com/nitya)_ |

U ovoj lekciji naučit ćete osnovna načela oblaka, zatim ćete vidjeti zašto bi moglo biti zanimljivo koristiti usluge oblaka za vođenje vaših projekata podatkovne znanosti te ćemo pogledati nekoliko primjera projekata podatkovne znanosti koji se provode u oblaku.

## [Kviz prije predavanja](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/32)

## Što je oblak?

Oblak, ili računalstvo u oblaku, odnosi se na pružanje širokog spektra računalnih usluga na zahtjev, koje se hostaju na infrastrukturi putem interneta. Usluge uključuju rješenja poput pohrane, baza podataka, mreža, softvera, analitike i inteligentnih usluga.

Obično razlikujemo javni, privatni i hibridni oblak na sljedeći način:

* Javni oblak: javni oblak je u vlasništvu i pod upravom treće strane koja pruža svoje računalne resurse putem interneta javnosti.
* Privatni oblak: odnosi se na računalne resurse u oblaku koje koristi isključivo jedna tvrtka ili organizacija, s uslugama i infrastrukturom održavanima na privatnoj mreži.
* Hibridni oblak: hibridni oblak je sustav koji kombinira javne i privatne oblake. Korisnici biraju lokalni podatkovni centar, dok omogućuju pokretanje podataka i aplikacija na jednom ili više javnih oblaka.

Većina usluga računalstva u oblaku spada u tri kategorije: infrastruktura kao usluga (IaaS), platforma kao usluga (PaaS) i softver kao usluga (SaaS).

* Infrastruktura kao usluga (IaaS): korisnici unajmljuju IT infrastrukturu poput poslužitelja i virtualnih strojeva (VM-ova), pohrane, mreža, operativnih sustava.
* Platforma kao usluga (PaaS): korisnici unajmljuju okruženje za razvoj, testiranje, isporuku i upravljanje softverskim aplikacijama. Korisnici se ne moraju brinuti o postavljanju ili upravljanju osnovnom infrastrukturom poslužitelja, pohrane, mreža i baza podataka potrebnih za razvoj.
* Softver kao usluga (SaaS): korisnici dobivaju pristup softverskim aplikacijama putem interneta, na zahtjev i obično na temelju pretplate. Korisnici se ne moraju brinuti o hostingu i upravljanju softverskom aplikacijom, osnovnom infrastrukturom ili održavanjem, poput nadogradnji softvera i sigurnosnih zakrpa.

Neki od najvećih pružatelja usluga u oblaku su Amazon Web Services, Google Cloud Platform i Microsoft Azure.

## Zašto odabrati oblak za podatkovnu znanost?

Razvojni inženjeri i IT stručnjaci biraju rad s oblakom iz mnogih razloga, uključujući sljedeće:

* Inovacija: možete unaprijediti svoje aplikacije integriranjem inovativnih usluga koje pružatelji oblaka nude izravno u vaše aplikacije.
* Fleksibilnost: plaćate samo za usluge koje trebate i možete birati iz širokog spektra usluga. Obično plaćate prema korištenju i prilagođavate usluge prema svojim potrebama.
* Proračun: ne morate ulagati u početnu kupnju hardvera i softvera, postavljanje i vođenje lokalnih podatkovnih centara, već plaćate samo ono što koristite.
* Skalabilnost: vaši resursi mogu se skalirati prema potrebama vašeg projekta, što znači da vaše aplikacije mogu koristiti više ili manje računalne snage, pohrane i propusnosti, prilagođavajući se vanjskim čimbenicima u bilo kojem trenutku.
* Produktivnost: možete se usredotočiti na svoje poslovanje umjesto da trošite vrijeme na zadatke koje može obavljati netko drugi, poput upravljanja podatkovnim centrima.
* Pouzdanost: računalstvo u oblaku nudi nekoliko načina za kontinuirano sigurnosno kopiranje vaših podataka i omogućuje postavljanje planova za oporavak od katastrofa kako bi vaše poslovanje i usluge nastavile raditi čak i u kriznim vremenima.
* Sigurnost: možete iskoristiti politike, tehnologije i kontrole koje jačaju sigurnost vašeg projekta.

Ovo su neki od najčešćih razloga zašto ljudi biraju korištenje usluga oblaka. Sada kada bolje razumijemo što je oblak i koje su njegove glavne prednosti, pogledajmo specifično poslove podatkovnih znanstvenika i razvojnih inženjera koji rade s podacima te kako im oblak može pomoći u rješavanju nekoliko izazova s kojima se mogu suočiti:

* Pohrana velikih količina podataka: umjesto kupnje, upravljanja i zaštite velikih poslužitelja, možete pohranjivati svoje podatke izravno u oblaku, koristeći rješenja poput Azure Cosmos DB, Azure SQL Database i Azure Data Lake Storage.
* Integracija podataka: integracija podataka ključni je dio podatkovne znanosti koji omogućuje prijelaz od prikupljanja podataka do poduzimanja akcija. Uz usluge integracije podataka u oblaku, možete prikupljati, transformirati i integrirati podatke iz različitih izvora u jedinstveno skladište podataka, koristeći Data Factory.
* Obrada podataka: obrada velikih količina podataka zahtijeva puno računalne snage, a ne posjeduju svi dovoljno snažne strojeve za to, zbog čega mnogi biraju izravno korištenje ogromne računalne snage oblaka za pokretanje i implementaciju svojih rješenja.
* Korištenje usluga analitike podataka: usluge oblaka poput Azure Synapse Analytics, Azure Stream Analytics i Azure Databricks pomažu vam pretvoriti podatke u korisne uvide.
* Korištenje usluga strojnog učenja i inteligencije podataka: umjesto da počinjete od nule, možete koristiti algoritme strojnog učenja koje pruža oblak, uz usluge poput AzureML. Također možete koristiti kognitivne usluge poput pretvaranja govora u tekst, teksta u govor, računalnog vida i drugih.

## Primjeri podatkovne znanosti u oblaku

Pogledajmo nekoliko scenarija kako bismo ovo učinili konkretnijim.

### Analiza sentimenta na društvenim mrežama u stvarnom vremenu

Počet ćemo sa scenarijem koji često proučavaju oni koji započinju s učenjem strojnog učenja: analiza sentimenta na društvenim mrežama u stvarnom vremenu.

Recimo da vodite web stranicu s vijestima i želite iskoristiti podatke uživo kako biste razumjeli koji bi sadržaj mogao zanimati vaše čitatelje. Da biste saznali više o tome, možete izraditi program koji provodi analizu sentimenta u stvarnom vremenu na temelju podataka s Twittera o temama koje su relevantne za vaše čitatelje.

Ključni pokazatelji koje ćete pratiti su volumen tweetova o specifičnim temama (hashtagovima) i sentiment, koji se utvrđuje pomoću alata za analitiku koji provode analizu sentimenta oko određenih tema.

Koraci potrebni za izradu ovog projekta su sljedeći:

* Kreiranje čvorišta događaja za unos podataka, koje će prikupljati podatke s Twittera
* Konfiguriranje i pokretanje aplikacije klijenta za Twitter, koja će pozivati Twitter Streaming API-je
* Kreiranje posla za Stream Analytics
* Specifikacija ulaza i upita za posao
* Kreiranje izlaznog odredišta i specifikacija izlaza posla
* Pokretanje posla

Za potpuni proces, pogledajte [dokumentaciju](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099).

### Analiza znanstvenih radova

Pogledajmo još jedan primjer projekta koji je izradio [Dmitry Soshnikov](http://soshnikov.com), jedan od autora ovog kurikuluma.

Dmitry je izradio alat koji analizira radove o COVID-u. Pregledom ovog projekta vidjet ćete kako možete izraditi alat koji izdvaja znanje iz znanstvenih radova, dobiva uvide i pomaže istraživačima da se učinkovito kreću kroz velike zbirke radova.

Pogledajmo različite korake korištene za ovo:

* Ekstrakcija i predobrada informacija pomoću [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)
* Korištenje [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) za paralelizaciju obrade
* Pohrana i upit podataka pomoću [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)
* Izrada interaktivne nadzorne ploče za istraživanje i vizualizaciju podataka pomoću Power BI-ja

Za potpuni proces, posjetite [Dmitryjev blog](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/).

Kao što vidite, usluge oblaka možemo koristiti na mnogo načina za provođenje podatkovne znanosti.

## Napomena

Izvori:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Kviz nakon predavanja

[Kviz nakon predavanja](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/33)

## Zadatak

[Istraživanje tržišta](assignment.md)

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.