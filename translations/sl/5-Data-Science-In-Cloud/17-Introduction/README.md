<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "408c55cab2880daa4e78616308bd5db7",
  "translation_date": "2025-08-30T17:47:59+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "sl"
}
-->
# Uvod v podatkovno znanost v oblaku

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Podatkovna znanost v oblaku: Uvod - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

V tej lekciji boste spoznali osnovna načela oblaka, nato pa boste videli, zakaj je lahko zanimivo uporabljati storitve v oblaku za izvajanje projektov podatkovne znanosti. Ogledali si bomo tudi nekaj primerov projektov podatkovne znanosti, ki se izvajajo v oblaku.

## [Predhodni kviz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/32)

## Kaj je oblak?

Oblak oziroma računalništvo v oblaku je dostava širokega nabora storitev računalništva, ki se plačujejo po porabi in so gostovane na infrastrukturi prek interneta. Storitve vključujejo rešitve, kot so shranjevanje, baze podatkov, omrežja, programska oprema, analitika in inteligentne storitve.

Običajno ločimo javni, zasebni in hibridni oblak, kot sledi:

* Javni oblak: javni oblak je v lasti in upravljanju tretjega ponudnika storitev v oblaku, ki svoje računalniške vire prek interneta dostavlja javnosti.
* Zasebni oblak: nanaša se na računalniške vire v oblaku, ki jih uporablja izključno eno podjetje ali organizacija, pri čemer so storitve in infrastruktura vzdrževane na zasebnem omrežju.
* Hibridni oblak: hibridni oblak je sistem, ki združuje javne in zasebne oblake. Uporabniki se odločijo za lokalni podatkovni center, hkrati pa omogočajo, da se podatki in aplikacije izvajajo na enem ali več javnih oblakih.

Večina storitev računalništva v oblaku spada v tri kategorije: infrastruktura kot storitev (IaaS), platforma kot storitev (PaaS) in programska oprema kot storitev (SaaS).

* Infrastruktura kot storitev (IaaS): uporabniki najamejo IT infrastrukturo, kot so strežniki in virtualni stroji (VM), shranjevanje, omrežja, operacijski sistemi.
* Platforma kot storitev (PaaS): uporabniki najamejo okolje za razvoj, testiranje, dostavo in upravljanje programske opreme. Uporabnikom ni treba skrbeti za nastavitev ali upravljanje osnovne infrastrukture strežnikov, shranjevanja, omrežja in baz podatkov, potrebnih za razvoj.
* Programska oprema kot storitev (SaaS): uporabniki dobijo dostop do programske opreme prek interneta, na zahtevo in običajno na podlagi naročnine. Uporabnikom ni treba skrbeti za gostovanje in upravljanje programske opreme, osnovne infrastrukture ali vzdrževanje, kot so posodobitve programske opreme in varnostni popravki.

Nekateri največji ponudniki storitev v oblaku so Amazon Web Services, Google Cloud Platform in Microsoft Azure.

## Zakaj izbrati oblak za podatkovno znanost?

Razvijalci in IT strokovnjaki se odločajo za delo z oblakom iz več razlogov, med drugim:

* Inovacije: svoje aplikacije lahko poganjate z vključevanjem inovativnih storitev, ki jih ustvarijo ponudniki oblaka, neposredno v svoje aplikacije.
* Prilagodljivost: plačate samo za storitve, ki jih potrebujete, in lahko izbirate med širokim naborom storitev. Običajno plačujete sproti in prilagajate storitve glede na svoje spreminjajoče se potrebe.
* Proračun: ni vam treba vlagati v nakup strojne in programske opreme, vzpostavitev in upravljanje lokalnih podatkovnih centrov; preprosto plačate za tisto, kar uporabljate.
* Skalabilnost: vaši viri se lahko prilagajajo potrebam vašega projekta, kar pomeni, da lahko vaše aplikacije uporabljajo več ali manj računalniške moči, shranjevanja in pasovne širine, odvisno od zunanjih dejavnikov v danem trenutku.
* Produktivnost: osredotočite se lahko na svoje poslovanje, namesto da bi izgubljali čas z nalogami, ki jih lahko upravlja nekdo drug, kot je upravljanje podatkovnih centrov.
* Zanesljivost: računalništvo v oblaku ponuja več načinov za neprekinjeno varnostno kopiranje vaših podatkov, poleg tega pa lahko vzpostavite načrte za obnovo po katastrofi, da ohranite svoje poslovanje in storitve tudi v kriznih časih.
* Varnost: izkoristite lahko politike, tehnologije in nadzore, ki krepijo varnost vašega projekta.

To so nekateri najpogostejši razlogi, zakaj se ljudje odločajo za uporabo storitev v oblaku. Zdaj, ko bolje razumemo, kaj je oblak in kakšne so njegove glavne prednosti, si poglejmo bolj specifično delo podatkovnih znanstvenikov in razvijalcev, ki delajo s podatki, ter kako jim oblak lahko pomaga pri različnih izzivih:

* Shranjevanje velikih količin podatkov: namesto da bi kupovali, upravljali in varovali velike strežnike, lahko podatke shranjujete neposredno v oblaku, z rešitvami, kot so Azure Cosmos DB, Azure SQL Database in Azure Data Lake Storage.
* Izvajanje integracije podatkov: integracija podatkov je bistveni del podatkovne znanosti, ki omogoča prehod od zbiranja podatkov do ukrepanja. S storitvami za integracijo podatkov, ki jih ponuja oblak, lahko zbirate, preoblikujete in integrirate podatke iz različnih virov v eno podatkovno skladišče, z Data Factory.
* Obdelava podatkov: obdelava velikih količin podatkov zahteva veliko računalniške moči, do katere nimajo vsi dostopa, zato se mnogi odločijo za neposredno uporabo ogromne računalniške moči oblaka za izvajanje in uvajanje svojih rešitev.
* Uporaba storitev analitike podatkov: storitve v oblaku, kot so Azure Synapse Analytics, Azure Stream Analytics in Azure Databricks, vam pomagajo pretvoriti podatke v uporabne vpoglede.
* Uporaba storitev strojnega učenja in podatkovne inteligence: namesto da začnete od začetka, lahko uporabite algoritme strojnega učenja, ki jih ponuja ponudnik oblaka, s storitvami, kot je AzureML. Uporabite lahko tudi kognitivne storitve, kot so pretvorba govora v besedilo, besedila v govor, računalniški vid in več.

## Primeri podatkovne znanosti v oblaku

Poglejmo si nekaj scenarijev, da bo to bolj konkretno.

### Analiza sentimenta na družbenih omrežjih v realnem času
Začeli bomo s scenarijem, ki ga pogosto preučujejo ljudje, ki se začenjajo ukvarjati s strojnim učenjem: analiza sentimenta na družbenih omrežjih v realnem času.

Recimo, da upravljate spletno stran z novicami in želite izkoristiti podatke v živo, da bi razumeli, kakšna vsebina bi lahko zanimala vaše bralce. Da bi izvedeli več o tem, lahko ustvarite program, ki izvaja analizo sentimenta v realnem času na podatkih iz objav na Twitterju, o temah, ki so relevantne za vaše bralce.

Ključni kazalniki, ki jih boste preučevali, so obseg tvitov o določenih temah (hashtagih) in sentiment, ki se določi z analitičnimi orodji za analizo sentimenta okoli določenih tem.

Koraki, potrebni za ustvarjanje tega projekta, so naslednji:

* Ustvarite vozlišče dogodkov za pretok vhodnih podatkov, ki bo zbiralo podatke s Twitterja.
* Konfigurirajte in zaženite aplikacijo za Twitter odjemalca, ki bo klicala Twitter Streaming API-je.
* Ustvarite Stream Analytics nalogo.
* Določite vhod in poizvedbo za nalogo.
* Ustvarite izhodno destinacijo in določite izhod za nalogo.
* Zaženite nalogo.

Celoten postopek si lahko ogledate v [dokumentaciji](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099).

### Analiza znanstvenih člankov
Poglejmo si še en primer projekta, ki ga je ustvaril [Dmitry Soshnikov](http://soshnikov.com), eden od avtorjev tega učnega načrta.

Dmitry je ustvaril orodje za analizo člankov o COVID-u. S pregledom tega projekta boste videli, kako lahko ustvarite orodje, ki iz znanstvenih člankov pridobiva znanje, pridobiva vpoglede in pomaga raziskovalcem učinkovito navigirati skozi velike zbirke člankov.

Poglejmo si različne korake, uporabljene za to:

* Pridobivanje in predobdelava informacij z [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Uporaba [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) za paralelizacijo obdelave.
* Shranjevanje in poizvedovanje informacij z [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Ustvarjanje interaktivne nadzorne plošče za raziskovanje in vizualizacijo podatkov z uporabo Power BI.

Celoten postopek si lahko ogledate na [Dmitryjevem blogu](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/).

Kot vidite, lahko storitve v oblaku na različne načine izkoristimo za izvajanje podatkovne znanosti.

## Opomba

Viri:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Kviz po predavanju

[Kviz po predavanju](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/33)

## Naloga

[Tržna raziskava](assignment.md)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za strojno prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo strokovno človeško prevajanje. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.