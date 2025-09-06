<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f8e7cdefa096664ae86f795be571580",
  "translation_date": "2025-09-05T19:16:33+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "hr"
}
-->
# Uvod u podatkovnu znanost u oblaku

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Podatkovna znanost u oblaku: Uvod - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

U ovoj lekciji naučit ćete osnovne principe oblaka, zatim ćete vidjeti zašto bi moglo biti zanimljivo koristiti usluge oblaka za pokretanje vaših projekata podatkovne znanosti, a pogledat ćemo i neke primjere projekata podatkovne znanosti koji se izvode u oblaku.

## [Pre-Lecture Quiz](https://ff-quizzes.netlify.app/en/ds/quiz/32)

## Što je oblak?

Oblak, ili računalstvo u oblaku, predstavlja pružanje širokog spektra računalnih usluga koje se plaćaju prema korištenju, a hostirane su na infrastrukturi putem interneta. Usluge uključuju rješenja poput pohrane, baza podataka, mreža, softvera, analitike i inteligentnih usluga.

Obično razlikujemo javni, privatni i hibridni oblak na sljedeći način:

* Javni oblak: javni oblak je u vlasništvu i pod upravljanjem treće strane koja pruža usluge oblaka putem interneta javnosti.
* Privatni oblak: odnosi se na računalne resurse oblaka koji se koriste isključivo od strane jedne tvrtke ili organizacije, s uslugama i infrastrukturom održavanima na privatnoj mreži.
* Hibridni oblak: hibridni oblak je sustav koji kombinira javne i privatne oblake. Korisnici biraju podatkovni centar na lokaciji, dok omogućuju da se podaci i aplikacije pokreću na jednom ili više javnih oblaka.

Većina usluga računalstva u oblaku spada u tri kategorije: infrastruktura kao usluga (IaaS), platforma kao usluga (PaaS) i softver kao usluga (SaaS).

* Infrastruktura kao usluga (IaaS): korisnici unajmljuju IT infrastrukturu poput servera i virtualnih strojeva (VM-ova), pohrane, mreža, operativnih sustava.
* Platforma kao usluga (PaaS): korisnici unajmljuju okruženje za razvoj, testiranje, isporuku i upravljanje softverskim aplikacijama. Korisnici ne moraju brinuti o postavljanju ili upravljanju osnovnom infrastrukturom servera, pohrane, mreže i baza podataka potrebnih za razvoj.
* Softver kao usluga (SaaS): korisnici dobivaju pristup softverskim aplikacijama putem interneta, na zahtjev i obično na temelju pretplate. Korisnici ne moraju brinuti o hostingu i upravljanju softverskom aplikacijom, osnovnom infrastrukturom ili održavanjem, poput nadogradnji softvera i sigurnosnih zakrpa.

Neki od najvećih pružatelja usluga oblaka su Amazon Web Services, Google Cloud Platform i Microsoft Azure.

## Zašto odabrati oblak za podatkovnu znanost?

Razvojni programeri i IT stručnjaci biraju rad s oblakom iz mnogih razloga, uključujući sljedeće:

* Inovacija: možete osnažiti svoje aplikacije integriranjem inovativnih usluga koje pružatelji oblaka nude izravno u vaše aplikacije.
* Fleksibilnost: plaćate samo za usluge koje trebate i možete birati iz širokog spektra usluga. Obično plaćate prema korištenju i prilagođavate svoje usluge prema svojim promjenjivim potrebama.
* Proračun: ne morate ulagati u početnu kupnju hardvera i softvera, postavljanje i upravljanje podatkovnim centrima na lokaciji, već jednostavno plaćate ono što koristite.
* Skalabilnost: vaši resursi mogu se skalirati prema potrebama vašeg projekta, što znači da vaše aplikacije mogu koristiti više ili manje računalne snage, pohrane i širine pojasa, prilagođavajući se vanjskim čimbenicima u bilo kojem trenutku.
* Produktivnost: možete se usredotočiti na svoje poslovanje umjesto da trošite vrijeme na zadatke koje može obavljati netko drugi, poput upravljanja podatkovnim centrima.
* Pouzdanost: računalstvo u oblaku nudi nekoliko načina za kontinuirano sigurnosno kopiranje vaših podataka i možete postaviti planove za oporavak od katastrofa kako biste održali svoje poslovanje i usluge čak i u kriznim vremenima.
* Sigurnost: možete koristiti politike, tehnologije i kontrole koje jačaju sigurnost vašeg projekta.

Ovo su neki od najčešćih razloga zašto ljudi biraju korištenje usluga oblaka. Sada kada bolje razumijemo što je oblak i koje su njegove glavne prednosti, pogledajmo konkretnije poslove podatkovnih znanstvenika i programera koji rade s podacima te kako im oblak može pomoći u rješavanju nekoliko izazova s kojima se mogu suočiti:

* Pohrana velikih količina podataka: umjesto kupnje, upravljanja i zaštite velikih servera, možete pohraniti svoje podatke izravno u oblaku, s rješenjima poput Azure Cosmos DB, Azure SQL Database i Azure Data Lake Storage.
* Integracija podataka: integracija podataka ključni je dio podatkovne znanosti koji omogućuje prijelaz od prikupljanja podataka do poduzimanja akcija. Uz usluge integracije podataka koje se nude u oblaku, možete prikupljati, transformirati i integrirati podatke iz različitih izvora u jedinstveno skladište podataka, koristeći Data Factory.
* Obrada podataka: obrada velikih količina podataka zahtijeva puno računalne snage, a ne posjeduju svi dovoljno moćne strojeve za to, zbog čega mnogi biraju izravno korištenje ogromne računalne snage oblaka za pokretanje i implementaciju svojih rješenja.
* Korištenje usluga analitike podataka: usluge oblaka poput Azure Synapse Analytics, Azure Stream Analytics i Azure Databricks pomažu vam pretvoriti vaše podatke u korisne uvide.
* Korištenje usluga strojnog učenja i inteligencije podataka: umjesto da počinjete od nule, možete koristiti algoritme strojnog učenja koje pružatelj oblaka nudi, s uslugama poput AzureML. Također možete koristiti kognitivne usluge poput pretvorbe govora u tekst, teksta u govor, računalnog vida i više.

## Primjeri podatkovne znanosti u oblaku

Pogledajmo nekoliko scenarija kako bismo ovo učinili konkretnijim.

### Analiza sentimenta na društvenim mrežama u stvarnom vremenu

Počet ćemo sa scenarijem koji često proučavaju ljudi koji započinju s učenjem strojnog učenja: analiza sentimenta na društvenim mrežama u stvarnom vremenu.

Recimo da vodite web stranicu s vijestima i želite iskoristiti podatke uživo kako biste razumjeli koji bi sadržaj mogao zanimati vaše čitatelje. Da biste saznali više o tome, možete izraditi program koji provodi analizu sentimenta u stvarnom vremenu na podacima iz Twitter objava, o temama koje su relevantne za vaše čitatelje.

Ključni pokazatelji koje ćete pratiti su volumen tweetova o određenim temama (hashtagovima) i sentiment, koji se utvrđuje pomoću analitičkih alata za analizu sentimenta oko određenih tema.

Koraci potrebni za izradu ovog projekta su sljedeći:

* Kreirajte čvorište događaja za unos podataka, koje će prikupljati podatke s Twittera.
* Konfigurirajte i pokrenite aplikaciju klijenta za Twitter, koja će pozivati Twitter Streaming API-je.
* Kreirajte posao za Stream Analytics.
* Odredite ulaz i upit za posao.
* Kreirajte izlazni kanal i odredite izlaz za posao.
* Pokrenite posao.

Za detaljan proces, pogledajte [dokumentaciju](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099).

### Analiza znanstvenih radova

Pogledajmo još jedan primjer projekta koji je kreirao [Dmitry Soshnikov](http://soshnikov.com), jedan od autora ovog kurikuluma.

Dmitry je kreirao alat koji analizira radove o COVID-u. Pregledom ovog projekta vidjet ćete kako možete kreirati alat koji izvlači znanje iz znanstvenih radova, dobiva uvide i pomaže istraživačima da se učinkovito kreću kroz velike zbirke radova.

Pogledajmo korake korištene za ovo:

* Ekstrakcija i predobrada informacija pomoću [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Korištenje [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) za paralelizaciju obrade.
* Pohrana i upit podataka pomoću [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Kreiranje interaktivne nadzorne ploče za istraživanje i vizualizaciju podataka pomoću Power BI.

Za detaljan proces, posjetite [Dmitryjev blog](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/).

Kao što vidite, usluge oblaka možemo koristiti na mnogo načina za provođenje podatkovne znanosti.

## Napomena

Izvori:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Post-Lecture Quiz

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/33)

## Zadatak

[Market Research](assignment.md)

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.