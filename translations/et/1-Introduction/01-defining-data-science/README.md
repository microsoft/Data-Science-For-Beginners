<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "43212cc1ac137b7bb1dcfb37ca06b0f4",
  "translation_date": "2025-10-25T19:16:08+00:00",
  "source_file": "1-Introduction/01-defining-data-science/README.md",
  "language_code": "et"
}
-->
# Andmeteaduse määratlemine

| ![ Sketchnote autorilt [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/01-Definitions.png) |
| :----------------------------------------------------------------------------------------------------------: |
|              Andmeteaduse määratlemine - _Sketchnote autorilt [@nitya](https://twitter.com/nitya)_           |

---

[![Andmeteaduse määratlemise video](../../../../translated_images/et/video-def-ds.6623ee2392ef1abf6d7faf3fad10a4163642811749da75f44e35a5bb121de15c.png)](https://youtu.be/beZ7Mb_oz9I)

## [Loengu-eelne viktoriin](https://ff-quizzes.netlify.app/en/ds/quiz/0)

## Mis on andmed?
Meie igapäevaelus ümbritsevad meid pidevalt andmed. Tekst, mida te praegu loete, on andmed. Teie nutitelefonis olev sõprade telefoninumbrite loetelu on andmed, samuti on andmed kellaaeg, mida teie kell näitab. Inimestena töötleme andmeid loomulikult, näiteks raha lugedes või sõpradele kirju kirjutades.

Kuid andmed muutusid palju olulisemaks arvutite loomisega. Arvutite peamine roll on teha arvutusi, kuid nad vajavad selleks andmeid. Seetõttu peame mõistma, kuidas arvutid andmeid salvestavad ja töötlevad.

Interneti tekkimisega suurenes arvutite roll andmete töötlemise seadmetena. Kui järele mõelda, siis kasutame arvuteid üha enam andmete töötlemiseks ja suhtlemiseks, mitte niivõrd arvutuste tegemiseks. Kui kirjutame sõbrale e-kirja või otsime internetist teavet, siis loome, salvestame, edastame ja töötleme sisuliselt andmeid.
> Kas mäletate, millal viimati kasutasite arvutit millegi arvutamiseks?

## Mis on andmeteadus?

[Wikipedia](https://en.wikipedia.org/wiki/Data_science) määratleb **andmeteaduse** kui *teadusvaldkonna, mis kasutab teaduslikke meetodeid, et saada teadmisi ja arusaamu struktureeritud ja struktureerimata andmetest ning rakendada saadud teadmisi ja praktilisi järeldusi erinevates rakendusvaldkondades*.

See määratlus toob esile järgmised olulised aspektid andmeteaduses:

* Andmeteaduse peamine eesmärk on **teadmiste hankimine** andmetest, teisisõnu - **mõista** andmeid, leida varjatud seoseid ja luua **mudel**.
* Andmeteadus kasutab **teaduslikke meetodeid**, nagu tõenäosusteooria ja statistika. Tegelikult, kui termin *andmeteadus* esmakordselt kasutusele võeti, väitsid mõned, et andmeteadus on lihtsalt uus moodne nimi statistikale. Tänapäeval on selge, et valdkond on palju laiem.
* Saadud teadmisi tuleks rakendada, et luua **praktilisi järeldusi**, st rakendatavaid järeldusi, mida saab kasutada reaalsetes ärisituatsioonides.
* Me peaksime olema võimelised töötlema nii **struktureeritud** kui ka **struktureerimata** andmeid. Kursuse käigus tuleme tagasi ja arutame erinevaid andmetüüpe.
* **Rakendusvaldkond** on oluline mõiste, ja andmeteadlased vajavad sageli vähemalt mingil määral teadmisi probleemivaldkonnast, näiteks: rahandus, meditsiin, turundus jne.

> Teine oluline aspekt andmeteaduses on see, et see uurib, kuidas andmeid saab koguda, salvestada ja töödelda arvutite abil. Kuigi statistika annab meile matemaatilise aluse, rakendab andmeteadus matemaatilisi kontseptsioone, et tegelikult andmetest järeldusi teha.

Üks viis (omistatud [Jim Grayle](https://en.wikipedia.org/wiki/Jim_Gray_(computer_scientist))) andmeteaduse vaatamiseks on pidada seda eraldi teadusparadigmaks:
* **Empiiriline**, kus tuginetakse peamiselt vaatluste ja katsete tulemustele
* **Teoreetiline**, kus uued kontseptsioonid tekivad olemasolevast teaduslikust teadmisest
* **Arvutuslik**, kus avastatakse uusi põhimõtteid arvutuseksperimentide põhjal
* **Andmepõhine**, mis põhineb andmetes olevate seoste ja mustrite avastamisel  

## Seotud valdkonnad

Kuna andmed on kõikjal, on ka andmeteadus lai valdkond, mis puudutab paljusid teisi distsipliine.

<dl>
<dt>Andmebaasid</dt>
<dd>
Oluline küsimus on <b>kuidas andmeid salvestada</b>, st kuidas neid struktureerida, et tagada kiirem töötlemine. On olemas erinevat tüüpi andmebaase, mis salvestavad struktureeritud ja struktureerimata andmeid, mida <a href="../../2-Working-With-Data/README.md">käsitleme oma kursusel</a>.
</dd>
<dt>Suured andmed</dt>
<dd>
Sageli peame salvestama ja töötlema väga suuri koguseid andmeid suhteliselt lihtsa struktuuriga. Selleks on olemas spetsiaalsed lähenemisviisid ja tööriistad, mis võimaldavad andmeid hajutatult salvestada arvutite klastris ja neid tõhusalt töödelda.
</dd>
<dt>Masinõpe</dt>
<dd>
Üks viis andmete mõistmiseks on <b>luua mudel</b>, mis suudab prognoosida soovitud tulemust. Mudelite arendamist andmetest nimetatakse <b>masinõppeks</b>. Võite tutvuda meie <a href="https://aka.ms/ml-beginners">Masinõppe algajatele</a> õppekavaga, et sellest rohkem teada saada.
</dd>
<dt>Tehisintellekt</dt>
<dd>
Masinõppe valdkond, mida tuntakse tehisintellektina (AI), tugineb samuti andmetele ja hõlmab keerukate mudelite loomist, mis jäljendavad inimeste mõtteprotsesse. AI meetodid võimaldavad sageli muuta struktureerimata andmed (nt loomulik keel) struktureeritud järeldusteks.
</dd>
<dt>Visualiseerimine</dt>
<dd>
Suured andmehulgad on inimesele arusaamatud, kuid kui me loome nende andmete põhjal kasulikke visualiseeringuid, saame andmetest paremini aru ja teha järeldusi. Seetõttu on oluline teada mitmeid viise teabe visualiseerimiseks - midagi, mida käsitleme <a href="../../3-Data-Visualization/README.md">kursuse 3. osas</a>. Seotud valdkondadeks on ka <b>infograafika</b> ja üldiselt <b>inimese ja arvuti interaktsioon</b>.
</dd>
</dl>

## Andmetüübid

Nagu juba mainitud, on andmed kõikjal. Me peame need lihtsalt õigesti kinni püüdma! Kasulik on eristada **struktureeritud** ja **struktureerimata** andmeid. Esimesed on tavaliselt esitatud hästi struktureeritud kujul, sageli tabelina või mitme tabelina, samas kui teised on lihtsalt failide kogum. Mõnikord räägitakse ka **poolstruktureeritud** andmetest, millel on mingisugune struktuur, mis võib oluliselt varieeruda.

| Struktureeritud                                                             | Poolstruktureeritud                                                                            | Struktureerimata                        |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------- |
| Inimeste nimekiri koos nende telefoninumbritega                             | Vikipeedia leheküljed linkidega                                                               | Encyclopedia Britannica tekst           |
| Temperatuur kõigis hoone ruumides iga minut viimase 20 aasta jooksul        | Teadusartiklite kogumik JSON-formaadis koos autorite, avaldamiskuupäeva ja kokkuvõttega       | Failijagamine ettevõtte dokumentidega   |
| Andmed hoonesse sisenevate inimeste vanuse ja soo kohta                     | Interneti leheküljed                                                                          | Toorvideo turvakaamerast                |

## Kust andmeid saada

Andmeid on võimalik saada paljudest allikatest, ja kõiki neid oleks võimatu loetleda! Siiski mainime mõningaid tüüpilisi kohti, kust andmeid saab:

* **Struktureeritud**
  - **Asjade internet** (IoT), sealhulgas andmed erinevatest sensoritest, nagu temperatuuri- või rõhuandurid, pakub palju kasulikke andmeid. Näiteks, kui kontorihoone on varustatud IoT sensoritega, saame automaatselt kontrollida kütet ja valgustust, et minimeerida kulusid.
  - **Küsitlused**, mida palume kasutajatel täita pärast ostu või veebisaidi külastamist.
  - **Käitumise analüüs** võib aidata meil mõista, kui sügavale kasutaja veebisaidil läheb ja mis on tüüpiline põhjus saidilt lahkumiseks.
* **Struktureerimata**
  - **Tekstid** võivad olla rikkalikud teadmiste allikad, näiteks üldine **meeleolu skoor** või märksõnade ja semantilise tähenduse tuvastamine.
  - **Pildid** või **videod**. Turvakaamera videoid saab kasutada liikluse hindamiseks teel ja inimeste teavitamiseks võimalikest ummikutest.
  - Veebiserveri **logid** võivad aidata mõista, milliseid meie saidi lehti külastatakse kõige sagedamini ja kui kaua.
* Poolstruktureeritud
  - **Sotsiaalvõrgustike** graafikud võivad olla suurepärased andmeallikad kasutajate isiksuste ja potentsiaalse tõhususe kohta teabe levitamisel.
  - Kui meil on peo fotode kogum, saame proovida tuvastada **grupidünaamika** andmeid, luues graafiku inimestest, kes teevad üksteisega pilte.

Teades erinevaid võimalikke andmeallikaid, saate mõelda erinevatele stsenaariumidele, kus andmeteaduse tehnikaid saab rakendada olukorra paremaks mõistmiseks ja äriprotsesside parandamiseks.

## Mida saab andmetega teha

Andmeteaduses keskendume järgmistele andmete teekonna etappidele:

<dl>
<dt>1) Andmete kogumine</dt>
<dd>
Esimene samm on andmete kogumine. Kuigi paljudel juhtudel võib see olla lihtne protsess, näiteks andmete jõudmine veebirakendusest andmebaasi, vajame mõnikord spetsiaalseid tehnikaid. Näiteks IoT sensorite andmed võivad olla ülekaalukad, ja hea tava on kasutada puhverdamise lõpp-punkte, nagu IoT Hub, et koguda kõik andmed enne edasist töötlemist.
</dd>
<dt>2) Andmete salvestamine</dt>
<dd>
Andmete salvestamine võib olla keeruline, eriti kui räägime suurtest andmetest. Otsustades, kuidas andmeid salvestada, on mõistlik ette näha, kuidas soovite tulevikus andmeid pärida. Andmeid saab salvestada mitmel viisil:
<ul>
<li>Relatsiooniline andmebaas salvestab tabelite kogumi ja kasutab spetsiaalset keelt nimega SQL nende pärimiseks. Tavaliselt on tabelid organiseeritud erinevatesse gruppidesse, mida nimetatakse skeemideks. Paljudel juhtudel peame andmed algsest vormist skeemile sobivaks teisendama.</li>
<li><a href="https://en.wikipedia.org/wiki/NoSQL">NoSQL</a> andmebaas, nagu <a href="https://azure.microsoft.com/services/cosmos-db/?WT.mc_id=academic-77958-bethanycheum">CosmosDB</a>, ei kehtesta andmetele skeeme ja võimaldab salvestada keerukamaid andmeid, näiteks hierarhilisi JSON-dokumente või graafikuid. Kuid NoSQL andmebaasidel puuduvad rikkalikud SQL-i päringuvõimalused ja nad ei saa kehtestada viitamisreegleid, st reegleid, kuidas andmed tabelites struktureeritud on ja kuidas tabelid omavahel seotud on.</li>
<li><a href="https://en.wikipedia.org/wiki/Data_lake">Andmejärve</a> salvestust kasutatakse suurte andmekogude jaoks toore, struktureerimata kujul. Andmejärvesid kasutatakse sageli suurte andmete puhul, kus kõik andmed ei mahu ühele masinale ja neid tuleb salvestada ja töödelda serverite klastris. <a href="https://en.wikipedia.org/wiki/Apache_Parquet">Parquet</a> on andmeformaat, mida sageli kasutatakse koos suurte andmetega.</li> 
</ul>
</dd>
<dt>3) Andmete töötlemine</dt>
<dd>
See on andmete teekonna kõige põnevam osa, mis hõlmab andmete teisendamist nende algsest vormist vormi, mida saab kasutada visualiseerimiseks/mudeli treenimiseks. Kui töötleme struktureerimata andmeid, nagu tekst või pildid, võime vajada mõningaid AI tehnikaid, et andmetest <b>omadusi</b> välja tuua, muutes need seega struktureeritud vormiks.
</dd>
<dt>4) Visualiseerimine / Inimeste arusaamad</dt>
<dd>
Sageli, et andmetest aru saada, peame need visualiseerima. Omades palju erinevaid visualiseerimistehnikaid oma tööriistakastis, saame leida õige vaate, et teha järeldusi. Sageli peab andmeteadlane "mängima andmetega", visualiseerides neid mitu korda ja otsides seoseid. Samuti võime kasutada statistilisi tehnikaid, et testida hüpoteese või tõestada korrelatsiooni erinevate andmeosade vahel.   
</dd>
<dt>5) Prognoosiva mudeli treenimine</dt>
<dd>
Kuna andmeteaduse lõppeesmärk on teha andmete põhjal otsuseid, võime soovida kasutada <a href="http://github.com/microsoft/ml-for-beginners">masinõppe</a> tehnikaid prognoosiva mudeli loomiseks. Seejärel saame seda kasutada prognooside tegemiseks uute sarnase struktuuriga andmekogumite põhjal.
</dd>
</dl>

Muidugi, sõltuvalt tegelikest andmetest, võivad mõned sammud puududa (nt kui andmed on juba andmebaasis või kui me ei vaja mudeli treenimist), või mõned sammud võivad olla korduvalt tehtud (näiteks andmete töötlemine).

## Digitaliseerimine ja digitaalne transformatsioon

Viimase kümnendi jooksul on paljud ettevõtted hakanud mõistma andmete tähtsust äriliste otsuste tegemisel. Et rakendada andmeteaduse põhimõtteid ettevõtte juhtimisel, tuleb kõigepealt koguda andmeid, st tõlkida äriprotsessid digitaalsesse vormi. Seda nimetatakse **digitaliseerimiseks**. Andmeteaduse tehnikate rakendamine nendele andmetele otsuste suunamiseks võib viia märkimisväärse tootlikkuse kasvuni (või isegi ärimudeli muutumiseni), mida nimetatakse **digitaalseks transformatsiooniks**.

Vaatame ühte näidet. Oletame, et meil on andmeteaduse kursus (nagu see), mida me veebis õpilastele edastame, ja me tahame kasutada andmeteadust selle parandamiseks. Kuidas me seda teha saaksime?

Me võime alustada küsimusega "Mida saab digitaliseerida?" Lihtsaim viis oleks mõõta aega, mis kulub igal õpilasel iga mooduli läbimiseks, ja mõõta saadud teadmisi, andes igale moodulile lõpus valikvastustega testi. Keskmistades kõigi õpilaste läbimise aja, saame teada, millised moodulid põhjustavad õpilastele kõige rohkem raskusi, ja töötada nende lihtsustamise kallal.
> Võib väita, et see lähenemine pole ideaalne, kuna moodulid võivad olla erineva pikkusega. Tõenäoliselt oleks õiglasem jagada aeg mooduli pikkusega (tähemärkide arvus) ja võrrelda neid väärtusi omavahel.

Kui hakkame analüüsima valikvastustega testide tulemusi, saame proovida kindlaks teha, milliste kontseptsioonide mõistmisega õpilastel raskusi on, ning kasutada seda teavet sisu parandamiseks. Selleks peame kujundama testid nii, et iga küsimus oleks seotud kindla kontseptsiooni või teadmiste osaga.

Kui soovime asja veelgi keerulisemaks teha, saame joonistada graafiku, kus on näidatud iga mooduli läbimiseks kulunud aeg vastavalt õpilaste vanusekategooriale. Võime avastada, et mõne vanusekategooria puhul võtab mooduli läbimine ebamõistlikult kaua aega või et õpilased loobuvad enne selle lõpetamist. See aitab meil anda moodulile vanuse soovitusi ja vähendada inimeste rahulolematust valede ootuste tõttu.

## 🚀 Väljakutse

Selles väljakutses püüame leida andmeteadusega seotud kontseptsioone, uurides tekste. Võtame Wikipedia artikli andmeteaduse kohta, laadime alla ja töötleme teksti ning loome sõnapilve, mis näeb välja selline:

![Sõnapilv andmeteaduse kohta](../../../../translated_images/et/ds_wordcloud.664a7c07dca57de017c22bf0498cb40f898d48aa85b3c36a80620fea12fadd42.png)

Külastage [`notebook.ipynb`](../../../../1-Introduction/01-defining-data-science/notebook.ipynb ':ignore'), et koodi läbi vaadata. Samuti saate koodi käivitada ja näha, kuidas see reaalajas kõiki andmetransformatsioone teostab.

> Kui te ei tea, kuidas Jupyter Notebookis koodi käivitada, vaadake [seda artiklit](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## [Loengu järgne viktoriin](https://ff-quizzes.netlify.app/en/ds/quiz/1)

## Ülesanded

* **Ülesanne 1**: Muutke ülaltoodud koodi, et leida seotud kontseptsioone **Big Data** ja **Machine Learning** valdkondade jaoks.
* **Ülesanne 2**: [Mõelge andmeteaduse stsenaariumidele](assignment.md)

## Autorid

Selle õppetunni on koostanud ♥️ [Dmitry Soshnikov](http://soshnikov.com)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algkeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta arusaamatuste või valesti tõlgenduste eest, mis võivad tekkida selle tõlke kasutamise tõttu.