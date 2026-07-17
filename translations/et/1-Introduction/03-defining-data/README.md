# Andmete määratlemine

|![ Sketchnote autorilt [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Andmete määratlemine - _Sketchnote autorilt [@nitya](https://twitter.com/nitya)_ |

Andmed on faktid, info, tähelepanekud ja mõõtmised, mida kasutatakse avastuste tegemiseks ja teadlike otsuste toetamiseks. Andmepunkt on üks andmühiku indiviid andmekogumis, mis on andmepunktide kogum. Andmekogud võivad olla erinevates formaatides ja struktuurides ning tavaliselt põhinevad nende allikal ehk koht, kust andmed pärinevad. Näiteks ettevõtte igakuine tulu võib olla tabelarvutusfailis, kuid nutikella tunnipõhine südamelöögisageduse andmestik võib olla [JSON](https://stackoverflow.com/a/383699) formaadis. On tavaline, et andmeteadlased töötavad andmekogumis erinevat tüüpi andmetega.

See õppetund keskendub andmete tuvastamisele ja klassifitseerimisele nende omaduste ja allikate alusel.

## [Eelkolleegiumi viktoriin](https://ff-quizzes.netlify.app/en/ds/quiz/4)
## Kuidas andmeid kirjeldatakse

### Toorandmed
Toorandmed on andmed, mis on pärit oma allikast algses olekus ja mida pole analüüsitud ega organiseeritud. Selleks, et mõista, mis andmekogus toimub, tuleb see korraldada inimeste ja ka tehnoloogia jaoks sellisesse formaati, mida on võimalik edasi analüüsida. Andmekogu struktuur kirjeldab, kuidas see on organiseeritud, ja seda saab klassifitseerida struktureeritud, struktureerimata ja poolstruktureeritudandmeteks. Need struktuuritüübid võivad varieeruda sõltuvalt allikast, kuid sobituvad lõpuks nende kolme kategooria alla.

### Kvanitatiivsed andmed
Kvantitatiivsed andmed on arvulised vaatlused andmekogus, mida tavaliselt saab analüüsida, mõõta ja kasutada matemaatiliselt. Näiteks kvantitatiivsed andmed võivad olla: riigi rahvaarv, inimese pikkus või ettevõtte kvartalitulu. Mõne täiendava analüüsiga võiks kvantitatiivseid andmeid kasutada õhukvaliteedi indeks (AQI) hooajaliste trendide avastamiseks või tipptunni liikluse tõenäosuse hindamiseks tüüpilisel tööpäeval.

### Kvalitatiivsed andmed
Kvalitatiivsed andmed ehk kategoorilised andmed on andmed, mida ei saa objektiivselt mõõta nagu kvantitatiivsete andmete vaatlust. Tavaliselt on need erinevat laadi subjektiivsed andmed, mis kajastavad midagi kvaliteeti, näiteks toodet või protsessi. Mõnikord on kvalitatiivsed andmed arvulised, kuid neid ei kasutata tavaliselt matemaatiliselt, nagu telefoninumbrid või aegmärgid. Näiteks võivad kvalitatiivsed andmed olla: video kommentaarid, auto mark ja mudel või sinu lähimate sõprade lemmikvärv. Kvalitatiivseid andmeid saaks kasutada tarbijate eelistatud toodete tundmaõppimiseks või tööotsijate elulookirjeldustes populaarsete märksõnade tuvastamiseks.

### Struktureeritud andmed
Struktureeritud andmed on organiseeritud ridadeks ja veergudeks, kus igal real on sama veergude komplekt. Veerud esindavad konkreetset tüüpi väärtust ja neid tähistatakse nimega, mis kirjeldab, mida väärtus tähistab, samas kui read sisaldavad tegelikke väärtusi. Veergudel võib olla kindlaksmääratud reeglite või piirangute kogum, et tagada väärtuste täpne esindatus. Näiteks kujutle klienditabelit, kus igal real peab olema telefoninumber ja telefoninumbris ei tohi olla tähestikulisi märke. Võib kehtestada reeglid veeru jaoks, et see pole kunagi tühi ja sisaldab ainult numbreid.

Struktureeritud andmete eelis on see, et neid saab organiseerida selliselt, et neid saab siduda teiste struktureeritud andmetega. Kuid kuna andmed on mõeldud korraldatud kindlal viisil, võib üldise struktuuri muutmine nõuda palju vaeva. Näiteks kui lisada klienditabelisse e-posti veerg, mis ei tohi olla tühi, tuleb välja mõelda, kuidas neid väärtusi juba olemasolevatele ridadele lisada.

Näited struktureeritud andmetest: tabelarvutusfailid, relatsioonandmebaasid, telefoninumbrid, pangaväljavõtted

### Struktureerimata andmed
Struktureerimata andmed ei ole tavaliselt ridadesse ega veergudesse ja neil puudub kindel formaat või reeglistik. Kuna struktureerimata andmetel on struktuuri piiranguid vähem, on uue info lisamine lihtsam kui struktureeritud andmetel. Kui andurit, mis mõõdab baromeetrilist rõhku iga 2 minuti tagant, uuendatakse nii, et nüüd saab mõõta ja salvestada temperatuuri, ei pea struktureerimata andmete puhul olemasolevaid andmeid muutma. Kuid see võib muuta selliste andmete analüüsi või uurimise raskemaks või aeglasemaks. Näiteks teadlane, kes soovib leida eelmise kuu keskmise temperatuuri seniste andmete põhjal, avastab, et mõnes salvestatud andmes on sensori rikkumise tähistamiseks märgitud “e” tähis tavalise numbri asemel, mis tähendab, et andmed on puudulikud.

Näited struktureerimata andmetest: tekstifailid, tekstisõnumid, videofailid

### Poolstruktureeritud andmed
Poolstruktureeritud andmed omavad omadusi, mis ühendavad struktureeritud ja struktureerimata andmeid. Need ei järgi tavaliselt ridade ja veergude formaati, kuid on organiseeritud selliselt, mida peetakse struktureerituks ja võivad järgida kindlat formaati või reeglistikku. Struktuur võib allikate lõikes varieeruda, ulatudes hästi määratletud hierarhiast kuni paindlikuma vormini, mis võimaldab lihtsat uue info integreerimist. Metaandmed on näitajad, mis aitavad otsustada, kuidas andmeid korraldatakse ja salvestatakse ning neil on erinevaid nimetusi sõltuvalt andmetüübist. Levinumad metaandmete nimetused on sildid, elemendid, üksused ja atribuudid. Näiteks tüüpilisel e-kirjal on teema, sisu ja adressaadid ning see võib olla organiseeritud selle järgi, kes ja millal selle saatis.

Näited poolstruktureeritud andmetest: HTML, CSV-failid, JavaScript Object Notation (JSON)

## Andmeallikad

Andmeallikas on koht, kus andmed algselt genereeriti või kus nad asuvad, ja see varieerub sõltuvalt sellest, kuidas ja millal andmed koguti. Kasutajate (andmete toodete) genereeritud andmeid nimetatakse esmaseks andmeteks, samas kui teisene andmestik pärineb allikast, mis on kogunud andmeid üldiseks kasutamiseks. Näiteks vihmametsa teadlaste grupi poolt kogutud tähelepanekud on esmased andmed ning kui nad otsustavad seda jagada teiste teadlastega, peetakse seda sekundaarseks nendel, kes neid kasutavad.

Andmebaasid on levinud allikad ja kasutavad andmebaasi haldussüsteemi andmete majutamiseks ja hooldamiseks, kus kasutajad saavad andmeid uurida päringute ehk käskude kaudu. Failid kui allikad võivad olla audio-, pildi- ja videofailid ning tabelarvutusfailid nagu Excel. Internetiallikad on tavalised koha andmete majutamiseks, kus leidub nii andmebaase kui ka faile. Rakendusliideste programmeerimisliidesed ehk API-d võimaldavad programmeerijatel luua viise, kuidas jagada andmeid väliskasutajatega interneti kaudu, samas kui veebilehitsemine võimaldab andmeid veebilehelt eraldada. [Andmetega töötamise õppetunnid](../../../../../../../../../2-Working-With-Data) keskenduvad erinevate allikate kasutamisele.

## Kokkuvõte

Selles õppetunnis õppisime:

- Mis on andmed
- Kuidas andmeid kirjeldatakse
- Kuidas andmed klassifitseeritakse ja kategoriseeritakse
- Kust andmeid leida võib

## 🚀 Väljakutse

Kaggle on suurepärane avatud andmekogude allikas. Kasuta [andmekogude otsingutööriista](https://www.kaggle.com/datasets), et leida huvitavaid andmekogusid ja klassifitseeri 3-5 andmekogu järgmise kriteeriumi alusel:

- Kas andmed on kvantitatiivsed või kvalitatiivsed?
- Kas andmed on struktureeritud, struktureerimata või poolstruktureeritud?

## [Pärast loengut viktoriin](https://ff-quizzes.netlify.app/en/ds/quiz/5)



## Ülevaade & Iseteemaks

- See Microsoft Learn moodul, pealkirjaga [Andmeformaatide tuvastamine](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats?pivots=text), sisaldab detailset ülevaadet struktureeritud, poolstruktureeritud ja struktureerimata andmetest.

## Kodutöö

[Andmekogude klassifitseerimine](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->