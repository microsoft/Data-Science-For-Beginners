<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0f67a4139454816631526779a456b734",
  "translation_date": "2025-10-11T15:45:45+00:00",
  "source_file": "6-Data-Science-In-Wild/20-Real-World-Examples/README.md",
  "language_code": "et"
}
-->
# Andmeteadus päriselus

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-RealWorld.png) |
| :--------------------------------------------------------------------------------------------------------------: |
|               Andmeteadus päriselus - _Sketchnote by [@nitya](https://twitter.com/nitya)_                        |

Meie õppekäik on peaaegu lõppenud!

Alustasime andmeteaduse ja eetika definitsioonidest, uurisime erinevaid tööriistu ja tehnikaid andmeanalüüsiks ja visualiseerimiseks, vaatasime üle andmeteaduse elutsükli ning uurisime, kuidas pilveteenuste abil andmeteaduse töövooge skaleerida ja automatiseerida. Nüüd võite mõelda: _"Kuidas ma saan kõik need teadmised päriselu kontekstidesse rakendada?"_

Selles õppetükis uurime andmeteaduse rakendusi tööstuses ja süveneme konkreetsetesse näidetesse teadusuuringute, digitaalse humanitaarteaduse ja jätkusuutlikkuse valdkondades. Vaatame õpilasprojektide võimalusi ja lõpetame kasulike ressurssidega, mis aitavad teil oma õppekäiku jätkata!

## Loengu-eelne viktoriin

## [Loengu-eelne viktoriin](https://ff-quizzes.netlify.app/en/ds/quiz/38)

## Andmeteadus + Tööstus

Tänu tehisintellekti demokratiseerimisele on arendajatel nüüd lihtsam kujundada ja integreerida tehisintellekti juhitud otsuste tegemist ja andmepõhiseid teadmisi kasutajakogemustesse ja arendusprotsessidesse. Siin on mõned näited, kuidas andmeteadust rakendatakse päriselu tööstusvaldkondades:

 * [Google Flu Trends](https://www.wired.com/2015/10/can-learn-epic-failure-google-flu-trends/) kasutas andmeteadust, et korreleerida otsingutermineid gripitrendidega. Kuigi lähenemisel oli puudusi, tõstis see teadlikkust andmepõhiste terviseprognooside võimalustest (ja väljakutsetest).

 * [UPS marsruutide prognoosid](https://www.technologyreview.com/2018/11/21/139000/how-ups-uses-ai-to-outsmart-bad-weather/) - selgitab, kuidas UPS kasutab andmeteadust ja masinõpet, et prognoosida optimaalseid tarne marsruute, arvestades ilmastikutingimusi, liiklusmustreid, tarne tähtaegu ja muud.

 * [NYC taksoteekonna visualiseerimine](http://chriswhong.github.io/nyctaxi/) - andmed, mis koguti [avaliku teabe seaduste](https://chriswhong.com/open-data/foil_nyc_taxi/) abil, aitasid visualiseerida ühe päeva NYC taksode elust, aidates mõista, kuidas nad liiguvad läbi tiheda linna, kui palju nad teenivad ja kui kaua kestavad reisid 24-tunnise perioodi jooksul.

 * [Uber Data Science Workbench](https://eng.uber.com/dsw/) - kasutab andmeid (pealevõtmise ja mahapaneku asukohad, reisi kestus, eelistatud marsruudid jne), mis kogutakse igapäevaselt miljonitest Uberi reisidest, et luua andmeanalüüsi tööriist, mis aitab hinnakujunduses, turvalisuses, pettuste tuvastamises ja navigeerimisotsustes.

 * [Spordianalüütika](https://towardsdatascience.com/scope-of-analytics-in-sports-world-37ed09c39860) - keskendub _ennustavale analüütikale_ (meeskonna ja mängija analüüs - mõelge [Moneyball](https://datasciencedegree.wisconsin.edu/blog/moneyball-proves-importance-big-data-big-ideas/) - ja fännide haldamine) ning _andmete visualiseerimisele_ (meeskonna ja fännide armatuurlauad, mängud jne) rakendustega nagu talendiskautimine, spordikihlveod ja inventari/kohtade haldamine.

 * [Andmeteadus panganduses](https://data-flair.training/blogs/data-science-in-banking/) - toob esile andmeteaduse väärtuse finantssektoris rakendustega, mis ulatuvad riskimudelitest ja pettuste tuvastamisest kuni kliendisegmentatsiooni, reaalajas prognooside ja soovitussüsteemideni. Ennustav analüütika juhib ka kriitilisi meetmeid nagu [krediidiskoorid](https://dzone.com/articles/using-big-data-and-predictive-analytics-for-credit).

 * [Andmeteadus tervishoius](https://data-flair.training/blogs/data-science-in-healthcare/) - toob esile rakendusi nagu meditsiiniline pildistamine (nt MRI, röntgen, CT-skaneerimine), genoomika (DNA järjestamine), ravimite arendamine (riskihindamine, edu prognoosimine), ennustav analüütika (patsiendihooldus ja tarne logistika), haiguste jälgimine ja ennetamine jne.

![Andmeteaduse rakendused päriselus](../../../../translated_images/et/data-science-applications.4e5019cd8790ebac2277ff5f08af386f8727cac5d30f77727c7090677e6adb9c.png) Pildi krediit: [Data Flair: 6 Amazing Data Science Applications ](https://data-flair.training/blogs/data-science-applications/)

Joonis näitab teisi valdkondi ja näiteid andmeteaduse tehnikate rakendamiseks. Kas soovite uurida teisi rakendusi? Vaadake [Ülevaade ja iseseisev õpe](../../../../6-Data-Science-In-Wild/20-Real-World-Examples) sektsiooni allpool.

## Andmeteadus + Teadusuuringud

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Research.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              Andmeteadus ja teadusuuringud - _Sketchnote by [@nitya](https://twitter.com/nitya)_              |

Kuigi päriselu rakendused keskenduvad sageli tööstuse kasutusjuhtudele suurel skaalal, võivad _teadusuuringute_ rakendused ja projektid olla kasulikud kahest vaatenurgast:

* _innovatsioonivõimalused_ - uurida arenenud kontseptsioonide kiiret prototüüpimist ja kasutajakogemuste testimist järgmise põlvkonna rakenduste jaoks.
* _rakendamise väljakutsed_ - uurida andmeteaduse tehnoloogiate võimalikke kahjusid või soovimatuid tagajärgi päriselu kontekstides.

Õpilaste jaoks võivad need teadusprojektid pakkuda nii õppimis- kui koostöövõimalusi, mis parandavad teie arusaamist teemast ja laiendavad teie teadlikkust ja kaasatust asjakohaste inimeste või meeskondadega, kes töötavad huvipakkuvates valdkondades. Millised teadusprojektid välja näevad ja kuidas nad võivad mõju avaldada?

Vaatame ühte näidet - [MIT Gender Shades Study](http://gendershades.org/overview.html) Joy Buolamwini (MIT Media Labs) poolt koos [märkimisväärse teadusartikliga](http://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf), mille kaasautoriks oli Timnit Gebru (tol ajal Microsoft Researchis), mis keskendus:

 * **Mis:** Teadusprojekti eesmärk oli _hinnata automaatsete näoanalyüsi algoritmide ja andmekogumite kallutatust_ soo ja nahatüübi alusel.
 * **Miks:** Näoanalyüsi kasutatakse valdkondades nagu õiguskaitse, lennujaama turvalisus, värbamissüsteemid ja palju muud - kontekstides, kus ebatäpsed klassifikatsioonid (nt kallutatuse tõttu) võivad põhjustada majanduslikke ja sotsiaalseid kahjusid mõjutatud isikutele või rühmadele. Kallutatuse mõistmine (ja selle kõrvaldamine või leevendamine) on kasutamise õiglusel oluline.
 * **Kuidas:** Teadlased tunnistasid, et olemasolevad võrdlusalused kasutasid peamiselt heledanahalisi subjekte ja koostasid uue andmekogumi (1000+ pilti), mis oli _tasakaalustatum_ soo ja nahatüübi järgi. Andmekogumit kasutati kolme soolise klassifikatsiooni toote (Microsoft, IBM ja Face++) täpsuse hindamiseks.

Tulemused näitasid, et kuigi üldine klassifikatsiooni täpsus oli hea, oli märgatav erinevus veamäärades erinevate alarühmade vahel - **valesti määramine** oli kõrgem naiste või tumedama nahatüübiga isikute puhul, mis viitas kallutatusele.

**Peamised tulemused:** Tõsteti teadlikkust, et andmeteadus vajab rohkem _esinduslikke andmekogumeid_ (tasakaalustatud alarühmad) ja rohkem _kaasavaid meeskondi_ (mitmekesised taustad), et tuvastada ja kõrvaldada või leevendada selliseid kallutatusi varakult tehisintellekti lahendustes. Sellised teadusuuringud on samuti olulised paljudele organisatsioonidele, et määratleda põhimõtteid ja tavasid _vastutustundliku tehisintellekti_ jaoks, et parandada õiglust nende tehisintellekti toodetes ja protsessides.

**Kas soovite õppida Microsofti asjakohaste teadusuuringute kohta?**

* Vaadake [Microsoft Research Projects](https://www.microsoft.com/research/research-area/artificial-intelligence/?facet%5Btax%5D%5Bmsr-research-area%5D%5B%5D=13556&facet%5Btax%5D%5Bmsr-content-type%5D%5B%5D=msr-project) tehisintellekti valdkonnas.
* Uurige õpilasprojekte [Microsoft Research Data Science Summer School](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/).
* Vaadake [Fairlearn](https://fairlearn.org/) projekti ja [Vastutustundliku tehisintellekti](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) algatusi.

## Andmeteadus + Humanitaarteadused

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Humanities.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              Andmeteadus ja digitaalsed humanitaarteadused - _Sketchnote by [@nitya](https://twitter.com/nitya)_              |

Digitaalsed humanitaarteadused [on defineeritud](https://digitalhumanities.stanford.edu/about-dh-stanford) kui "praktikate ja lähenemiste kogum, mis ühendab arvutusmeetodid humanitaarteadusliku uurimisega". [Stanfordi projektid](https://digitalhumanities.stanford.edu/projects) nagu _"ajaloo taaskäivitamine"_ ja _"poeetiline mõtlemine"_ illustreerivad seost [digitaalsete humanitaarteaduste ja andmeteaduse vahel](https://digitalhumanities.stanford.edu/digital-humanities-and-data-science) - rõhutades tehnikaid nagu võrgustike analüüs, teabe visualiseerimine, ruumiline ja teksti analüüs, mis aitavad meil ajaloolisi ja kirjanduslikke andmekogumeid uuesti läbi vaadata, et tuletada uusi teadmisi ja perspektiive.

*Kas soovite uurida ja laiendada projekti selles valdkonnas?*

Vaadake ["Emily Dickinson ja meeleolu meetrum"](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671) - suurepärane näide [Jen Looperilt](https://twitter.com/jenlooper), mis küsib, kuidas saame andmeteadust kasutada, et uuesti läbi vaadata tuttavat luulet ja hinnata selle tähendust ning autori panust uutes kontekstides. Näiteks, _kas saame ennustada hooaja, millal luuletus kirjutati, analüüsides selle tooni või sentimenti_ - ja mida see räägib autori meeleolust vastaval perioodil?

Sellele küsimusele vastamiseks järgime andmeteaduse elutsükli samme:
 * [`Andmete hankimine`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#acquiring-the-dataset) - koguda asjakohane andmekogum analüüsiks. Valikud hõlmavad API kasutamist (nt [Poetry DB API](https://poetrydb.org/index.html)) või veebilehtede kraapimist (nt [Project Gutenberg](https://www.gutenberg.org/files/12242/12242-h/12242-h.htm)) tööriistadega nagu [Scrapy](https://scrapy.org/).
 * [`Andmete puhastamine`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#clean-the-data) - selgitab, kuidas teksti saab vormindada, puhastada ja lihtsustada, kasutades põhitööriistu nagu Visual Studio Code ja Microsoft Excel.
 * [`Andmete analüüs`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#working-with-the-data-in-a-notebook) - selgitab, kuidas saame nüüd andmekogumi importida "märkmetesse" analüüsiks, kasutades Python'i pakette (nagu pandas, numpy ja matplotlib), et andmeid korraldada ja visualiseerida.
 * [`Sentimendi analüüs`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#sentiment-analysis-using-cognitive-services) - selgitab, kuidas saame integreerida pilveteenuseid nagu teksti analüüs, kasutades madala koodiga tööriistu nagu [Power Automate](https://flow.microsoft.com/en-us/) automatiseeritud andmetöötluse töövoogude jaoks.

Selle töövoo abil saame uurida hooajalisi mõjusid luuletuste sentimentidele ja aidata meil kujundada oma perspektiive autorist. Proovige ise - seejärel laiendage märkmikku, et küsida muid küsimusi või visualiseerida andmeid uutel viisidel!

> Võite kasutada mõningaid tööriistu [digitaalsete humanitaarteaduste tööriistakomplektist](https://github.com/Digital-Humanities-Toolkit), et jätkata uurimist.

## Andmeteadus + Jätkusuutlikkus

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Sustainability.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              Andmeteadus ja jätkusuutlikkus - _Sketchnote by [@nitya](https://twitter.com/nitya)_              |

[2030. aasta säästva arengu tegevuskava](https://sdgs.un.org/2030agenda) - mille võtsid 2015. aastal vastu kõik ÜRO liikmed - määratleb 17 eesmärki, sealhulgas need, mis keskenduvad **planeedi kaitsmisele** degradatsiooni ja kliimamuutuste mõju eest. [Microsofti jätkusuutlikkuse](https://www.microsoft.com/en-us/sustainability) algatus toetab neid eesmärke, uurides, kuidas tehnoloogilised lahendused võivad toetada ja luua jätkusuutlikumaid tulevikke, keskendudes [neljale eesmärgile](https://dev.to/azure/a-visual-guide-to-sustainable-software-engineering-53hh) - olla süsiniknegatiivne, veepositiivne, nulljäätmetega ja bioloogiliselt mitmekesine aastaks 2030.

Nende väljakutsete lahendamine skaleeritaval ja õigeaegsel viisil nõuab pilvepõhist mõtlemist - ja suures mahus andmeid. [Planetary Computer](https://planetarycomputer.microsoft.com/) algatus pakub 4 komponenti, mis aitavad andmeteadlastel ja arendajatel selles pingutuses:

 * [Andmekataloog](https://planetarycomputer.microsoft.com/catalog) - petabaitide ulatuses Maa süsteemide andmeid (tasuta ja Azure'i hostitud).
 * [Planetary API](https://planetarycomputer.microsoft.com/docs/reference/stac/) - aitab kasutajatel otsida asjakohaseid andmeid ruumi ja aja lõikes.
 * [Hub](https://planetarycomputer.microsoft.com/docs/overview/environment/) - hallatud keskkond teadlastele massiivsete georuumiliste andmekogumite töötlemiseks.
 * [Rakendused](https://planetarycomputer.microsoft.com/applications) - näitavad kasutusjuhtumeid ja tööriistu jätkusuutlikkuse analüüside jaoks.

**Planetary Computer projekt on praegu eelvaates (seisuga september 2021)** - siin on juhised, kuidas alustada panustamist jätkusuutlikkuse lahendustesse andmeteaduse abil.

* [Taotle juurdepääsu](https://planetarycomputer.microsoft.com/account/request), et alustada uurimist ja luua ühendusi teistega.
* [Tutvu dokumentatsiooniga](https://planetarycomputer.microsoft.com/docs/overview/about), et mõista toetatud andmekogumeid ja API-sid.
* Uuri rakendusi nagu [Ecosystem Monitoring](https://analytics-lab.org/ecosystemmonitoring/), et saada inspiratsiooni rakenduste ideedeks.

Mõtle, kuidas saaksid kasutada andmete visualiseerimist, et tuua esile või võimendada olulisi teadmisi valdkondades nagu kliimamuutused ja metsade hävitamine. Või mõtle, kuidas neid teadmisi saaks kasutada uute kasutajakogemuste loomiseks, mis motiveerivad käitumuslikke muutusi jätkusuutlikuma eluviisi suunas.

## Andmeteadus + Õpilased

Oleme rääkinud reaalse maailma rakendustest tööstuses ja teadusuuringutes ning uurinud andmeteaduse rakenduste näiteid digitaalses humanitaarteaduses ja jätkusuutlikkuses. Kuidas aga arendada oma oskusi ja jagada oma teadmisi andmeteaduse algajatena?

Siin on mõned näited andmeteaduse õpilasprojektidest, mis võivad inspireerida.

 * [MSR Data Science Summer School](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/#!projects) koos GitHubi [projektidega](https://github.com/msr-ds3), mis uurivad teemasid nagu:
    - [Rassiline eelarvamus politsei jõu kasutamises](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2019-replicating-an-empirical-analysis-of-racial-differences-in-police-use-of-force/) | [Github](https://github.com/msr-ds3/stop-question-frisk)
    - [NYC metroosüsteemi töökindlus](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2018-exploring-the-reliability-of-the-nyc-subway-system/) | [Github](https://github.com/msr-ds3/nyctransit)
 * [Materiaalse kultuuri digiteerimine: Sotsiaal-majanduslike jaotuste uurimine Sirkapis](https://claremont.maps.arcgis.com/apps/Cascade/index.html?appid=bdf2aef0f45a4674ba41cd373fa23afc) - Ornella Altunyani ja tema meeskonna poolt Claremontis, kasutades [ArcGIS StoryMaps](https://storymaps.arcgis.com/).

## 🚀 Väljakutse

Otsi artikleid, mis soovitavad algajatele sobivaid andmeteaduse projekte - näiteks [need 50 teemaala](https://www.upgrad.com/blog/data-science-project-ideas-topics-beginners/) või [need 21 projektiideed](https://www.intellspot.com/data-science-project-ideas) või [need 16 projekti koos lähtekoodiga](https://data-flair.training/blogs/data-science-project-ideas/), mida saad lahti võtta ja uuesti kokku panna. Ära unusta blogida oma õppeprotsessist ja jagada oma teadmisi meie kõigiga.

## Loengu järgne viktoriin

## [Loengu järgne viktoriin](https://ff-quizzes.netlify.app/en/ds/quiz/39)

## Ülevaade ja iseseisev õpe

Soovid uurida rohkem kasutusjuhtumeid? Siin on mõned asjakohased artiklid:
 * [17 andmeteaduse rakendust ja näidet](https://builtin.com/data-science/data-science-applications-examples) - juuli 2021
 * [11 hämmastavat andmeteaduse rakendust reaalses maailmas](https://myblindbird.com/data-science-applications-real-world/) - mai 2021
 * [Andmeteadus reaalses maailmas](https://towardsdatascience.com/data-science-in-the-real-world/home) - artiklite kogumik
 * [12 reaalse maailma andmeteaduse rakendust koos näidetega](https://www.scaler.com/blog/data-science-applications/) - mai 2024
 * Andmeteadus: [Hariduses](https://data-flair.training/blogs/data-science-in-education/), [Põllumajanduses](https://data-flair.training/blogs/data-science-in-agriculture/), [Finantsvaldkonnas](https://data-flair.training/blogs/data-science-in-finance/), [Filmides](https://data-flair.training/blogs/data-science-at-movies/), [Tervishoius](https://onlinedegrees.sandiego.edu/data-science-health-care/) ja mujal.

## Ülesanne

[Uuri Planetary Computer andmekogumit](assignment.md)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.