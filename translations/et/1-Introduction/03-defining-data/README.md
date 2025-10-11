<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "12339119c0165da569a93ddba05f9339",
  "translation_date": "2025-10-11T15:35:12+00:00",
  "source_file": "1-Introduction/03-defining-data/README.md",
  "language_code": "et"
}
-->
# Andmete määratlemine

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Andmete määratlemine - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Andmed on faktid, teave, tähelepanekud ja mõõtmised, mida kasutatakse avastuste tegemiseks ja teadlike otsuste toetamiseks. Andmepunkt on üksik andmeühik andmekogumis, mis on andmepunktide kogum. Andmekogumid võivad olla erinevates vormingutes ja struktuurides ning tavaliselt põhinevad need nende allikal ehk kust andmed pärinevad. Näiteks ettevõtte igakuine tulu võib olla arvutustabelis, kuid nutikella tunnipõhine pulsisageduse andmestik võib olla [JSON](https://stackoverflow.com/a/383699) vormingus. On tavaline, et andmeteadlased töötavad andmekogumis erinevat tüüpi andmetega.

See õppetund keskendub andmete tuvastamisele ja klassifitseerimisele nende omaduste ja allikate järgi.

## [Eelloengu viktoriin](https://ff-quizzes.netlify.app/en/ds/quiz/4)
## Kuidas andmeid kirjeldatakse

### Toorandmed
Toorandmed on andmed, mis pärinevad nende allikast algses olekus ja mida pole analüüsitud ega organiseeritud. Selleks, et mõista, mis andmekogumis toimub, tuleb andmed organiseerida vormingusse, mida inimesed ja tehnoloogia, mida nad edasiseks analüüsiks kasutavad, suudavad mõista. Andmekogumi struktuur kirjeldab, kuidas see on organiseeritud, ja seda saab klassifitseerida struktureeritud, struktureerimata ja poolstruktureeritud andmeteks. Need struktuuritüübid varieeruvad sõltuvalt allikast, kuid lõpuks sobituvad ühte neist kolmest kategooriast.

### Kvantitatiivsed andmed
Kvantitatiivsed andmed on andmekogumis olevad numbrilised tähelepanekud, mida saab tavaliselt analüüsida, mõõta ja matemaatiliselt kasutada. Mõned kvantitatiivsete andmete näited on: riigi rahvaarv, inimese pikkus või ettevõtte kvartalitulu. Täiendava analüüsi abil võiks kvantitatiivseid andmeid kasutada näiteks õhukvaliteedi indeksi (AQI) hooajaliste trendide avastamiseks või tööpäeva tipptunni liikluse tõenäosuse hindamiseks.

### Kvalitatiivsed andmed
Kvalitatiivsed andmed, tuntud ka kui kategoorilised andmed, on andmed, mida ei saa objektiivselt mõõta nagu kvantitatiivsete andmete tähelepanekuid. Need on üldiselt subjektiivsed andmed, mis kajastavad millegi kvaliteeti, näiteks toodet või protsessi. Mõnikord on kvalitatiivsed andmed numbrilised, kuid neid ei kasutata tavaliselt matemaatiliselt, nagu telefoninumbrid või ajatemplid. Mõned kvalitatiivsete andmete näited on: videokommentaarid, auto mark ja mudel või sinu lähimate sõprade lemmikvärv. Kvalitatiivseid andmeid võiks kasutada näiteks selleks, et mõista, millised tooted tarbijatele kõige rohkem meeldivad, või populaarsete märksõnade tuvastamiseks töötaotluste CV-des.

### Struktureeritud andmed
Struktureeritud andmed on andmed, mis on organiseeritud ridadesse ja veergudesse, kus igal real on sama veergude komplekt. Veerud esindavad konkreetse tüübi väärtust ja neid identifitseeritakse nimega, mis kirjeldab, mida väärtus esindab, samas kui read sisaldavad tegelikke väärtusi. Veergudel on sageli konkreetne reeglite või piirangute komplekt, et tagada, et väärtused täpselt esindavad veergu. Näiteks kujutlege klientide arvutustabelit, kus igal real peab olema telefoninumber ja telefoninumbrid ei sisalda tähestikulisi märke. Telefoninumbri veerule võib rakendada reegleid, et see ei oleks kunagi tühi ja sisaldaks ainult numbreid.

Struktureeritud andmete eeliseks on see, et neid saab organiseerida viisil, mis võimaldab neid seostada teiste struktureeritud andmetega. Kuid kuna andmed on kavandatud olema organiseeritud kindlal viisil, võib selle üldstruktuuri muutmine nõuda palju pingutust. Näiteks kui lisada klientide arvutustabelisse e-posti veerg, mis ei tohi olla tühi, tuleb välja mõelda, kuidas lisada need väärtused olemasolevatele klientide ridadele andmekogumis.

Struktureeritud andmete näited: arvutustabelid, relatsioonilised andmebaasid, telefoninumbrid, pangaväljavõtted.

### Struktureerimata andmed
Struktureerimata andmeid ei saa tavaliselt kategoriseerida ridadesse või veergudesse ning neil puudub vorming või reeglite komplekt, mida järgida. Kuna struktureerimata andmetel on vähem piiranguid nende struktuurile, on uue teabe lisamine lihtsam võrreldes struktureeritud andmekogumiga. Kui sensor, mis salvestab iga 2 minuti järel andmeid baromeetrilise rõhu kohta, saab uuenduse, mis võimaldab tal mõõta ja salvestada temperatuuri, ei nõua see olemasolevate andmete muutmist, kui need on struktureerimata. Kuid see võib muuta selliste andmete analüüsimise või uurimise ajamahukamaks. Näiteks teadlane, kes soovib leida sensori andmetest eelmise kuu keskmist temperatuuri, kuid avastab, et sensor salvestas mõnes andmes "e", et märkida, et see oli katki, mitte tüüpilist numbrit, mis tähendab, et andmed on puudulikud.

Struktureerimata andmete näited: tekstifailid, tekstisõnumid, videofailid.

### Poolstruktureeritud andmed
Poolstruktureeritud andmetel on omadused, mis muudavad need struktureeritud ja struktureerimata andmete kombinatsiooniks. Need ei vasta tavaliselt ridade ja veergude vormingule, kuid on organiseeritud viisil, mida peetakse struktureerituks ja mis võib järgida kindlat vormingut või reeglite komplekti. Struktuur varieerub allikate vahel, näiteks hästi määratletud hierarhia või midagi paindlikumat, mis võimaldab hõlpsat uue teabe integreerimist. Metaandmed on näitajad, mis aitavad otsustada, kuidas andmed on organiseeritud ja salvestatud, ning neil on erinevad nimed, sõltuvalt andmete tüübist. Mõned metaandmete levinud nimed on sildid, elemendid, üksused ja atribuudid. Näiteks tüüpilisel e-kirjal on teema, sisu ja saajate komplekt ning seda saab organiseerida selle järgi, kellele või millal see saadeti.

Poolstruktureeritud andmete näited: HTML, CSV-failid, JavaScript Object Notation (JSON).

## Andmete allikad

Andmeallikas on algne asukoht, kus andmed loodi või kus need "elavad", ja see varieerub sõltuvalt sellest, kuidas ja millal need koguti. Kasutaja(te) poolt genereeritud andmeid nimetatakse esmasteks andmeteks, samas kui teiseseid andmeid kogub allikas üldiseks kasutamiseks. Näiteks teadlaste rühm, kes kogub tähelepanekuid vihmametsas, oleks esmane allikas, ja kui nad otsustavad seda teiste teadlastega jagada, oleks see nende jaoks teisene allikas.

Andmebaasid on tavalised allikad ja tuginevad andmebaasi haldussüsteemile, et andmeid majutada ja hallata, kus kasutajad kasutavad päringuteks nimetatud käske andmete uurimiseks. Failid andmeallikatena võivad olla heli-, pildi- ja videofailid, samuti arvutustabelid nagu Excel. Interneti allikad on tavalised andmete majutamise kohad, kus võib leida nii andmebaase kui ka faile. Rakenduste programmeerimisliidesed, tuntud ka kui API-d, võimaldavad programmeerijatel luua viise andmete jagamiseks väliste kasutajatega interneti kaudu, samas kui veebikraapimine eraldab andmeid veebilehelt. [Õppetunnid andmetega töötamisest](../../../../../../../../../2-Working-With-Data) keskenduvad sellele, kuidas kasutada erinevaid andmeallikaid.

## Kokkuvõte

Selles õppetunnis õppisime:

- Mis on andmed
- Kuidas andmeid kirjeldatakse
- Kuidas andmeid klassifitseeritakse ja kategoriseeritakse
- Kus andmeid võib leida

## 🚀 Väljakutse

Kaggle on suurepärane avatud andmekogumite allikas. Kasuta [andmekogumite otsingutööriista](https://www.kaggle.com/datasets), et leida huvitavaid andmekogumeid ja klassifitseeri 3-5 andmekogumit järgmiste kriteeriumide alusel:

- Kas andmed on kvantitatiivsed või kvalitatiivsed?
- Kas andmed on struktureeritud, struktureerimata või poolstruktureeritud?

## [Järelloengu viktoriin](https://ff-quizzes.netlify.app/en/ds/quiz/5)

## Ülevaade ja iseseisev õppimine

- Microsoft Learn üksus, pealkirjaga [Classify your Data](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/2-classify-data), sisaldab üksikasjalikku jaotust struktureeritud, poolstruktureeritud ja struktureerimata andmetest.

## Ülesanne

[Andmekogumite klassifitseerimine](assignment.md)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.