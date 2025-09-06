<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "07478c2092203a69087b9c76b1f4dd56",
  "translation_date": "2025-09-05T19:37:50+00:00",
  "source_file": "4-Data-Science-Lifecycle/14-Introduction/README.md",
  "language_code": "sl"
}
-->
# Uvod v življenjski cikel podatkovne znanosti

|![ Sketchnote avtorja [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/14-DataScience-Lifecycle.png)|
|:---:|
| Uvod v življenjski cikel podatkovne znanosti - _Sketchnote avtorja [@nitya](https://twitter.com/nitya)_ |

## [Predhodni kviz](https://ff-quizzes.netlify.app/en/ds/quiz/26)

Do sedaj ste verjetno že ugotovili, da je podatkovna znanost proces. Ta proces lahko razdelimo na 5 faz:

- Zajemanje
- Obdelava
- Analiza
- Komunikacija
- Vzdrževanje

Ta lekcija se osredotoča na 3 dele življenjskega cikla: zajemanje, obdelavo in vzdrževanje.

![Diagram življenjskega cikla podatkovne znanosti](../../../../4-Data-Science-Lifecycle/14-Introduction/images/data-science-lifecycle.jpg)
> Fotografija avtorja [Berkeley School of Information](https://ischoolonline.berkeley.edu/data-science/what-is-data-science/)

## Zajemanje

Prva faza življenjskega cikla je zelo pomembna, saj so naslednje faze odvisne od nje. V bistvu gre za dve fazi združeni v eno: pridobivanje podatkov in določanje namena ter problemov, ki jih je treba rešiti.  
Določanje ciljev projekta zahteva globlji vpogled v problem ali vprašanje. Najprej moramo identificirati in pridobiti tiste, ki potrebujejo rešitev za svoj problem. To so lahko deležniki v podjetju ali sponzorji projekta, ki lahko pomagajo določiti, kdo ali kaj bo imelo koristi od tega projekta, ter kaj in zakaj to potrebujejo. Dobro opredeljen cilj mora biti merljiv in kvantificiran, da lahko določimo sprejemljiv rezultat.

Vprašanja, ki jih lahko zastavi podatkovni znanstvenik:
- Ali je bil ta problem že obravnavan? Kaj je bilo odkrito?
- Ali vsi vključeni razumejo namen in cilj?
- Ali obstaja nejasnost in kako jo zmanjšati?
- Kakšne so omejitve?
- Kako bo izgledal končni rezultat?
- Koliko virov (čas, ljudje, računalniški) je na voljo?

Naslednji korak je identificiranje, zbiranje in nato raziskovanje podatkov, potrebnih za dosego teh opredeljenih ciljev. V tej fazi pridobivanja morajo podatkovni znanstveniki oceniti količino in kakovost podatkov. To zahteva nekaj raziskovanja podatkov, da se potrdi, da pridobljeni podatki podpirajo dosego želenega rezultata.

Vprašanja, ki jih lahko zastavi podatkovni znanstvenik glede podatkov:
- Kateri podatki so mi že na voljo?
- Kdo je lastnik teh podatkov?
- Kakšne so skrbi glede zasebnosti?
- Ali imam dovolj podatkov za rešitev problema?
- Ali so podatki ustrezne kakovosti za ta problem?
- Če odkrijem dodatne informacije skozi te podatke, ali bi morali razmisliti o spremembi ali ponovni opredelitvi ciljev?

## Obdelava

Faza obdelave v življenjskem ciklu se osredotoča na odkrivanje vzorcev v podatkih ter modeliranje. Nekatere tehnike, uporabljene v fazi obdelave, zahtevajo statistične metode za odkrivanje vzorcev. Običajno bi bila to zamudna naloga za človeka pri delu z velikimi nabori podatkov, zato se zanašamo na računalnike, da pospešijo proces. Ta faza je tudi točka, kjer se podatkovna znanost in strojno učenje prekrivata. Kot ste se naučili v prvi lekciji, je strojno učenje proces gradnje modelov za razumevanje podatkov. Modeli so predstavitev razmerja med spremenljivkami v podatkih, ki pomagajo napovedovati rezultate.

Pogoste tehnike, uporabljene v tej fazi, so obravnavane v učnem načrtu ML za začetnike. Sledite povezavam, da izveste več o njih:

- [Klasifikacija](https://github.com/microsoft/ML-For-Beginners/tree/main/4-Classification): Organiziranje podatkov v kategorije za bolj učinkovito uporabo.
- [Gručenje](https://github.com/microsoft/ML-For-Beginners/tree/main/5-Clustering): Združevanje podatkov v podobne skupine.
- [Regresija](https://github.com/microsoft/ML-For-Beginners/tree/main/2-Regression): Določanje razmerij med spremenljivkami za napovedovanje ali predvidevanje vrednosti.

## Vzdrževanje

Na diagramu življenjskega cikla ste morda opazili, da vzdrževanje stoji med zajemanjem in obdelavo. Vzdrževanje je stalen proces upravljanja, shranjevanja in varovanja podatkov skozi celoten proces projekta in ga je treba upoštevati skozi celoten projekt.

### Shranjevanje podatkov

Premisleki o tem, kako in kje so podatki shranjeni, lahko vplivajo na stroške shranjevanja ter na zmogljivost dostopa do podatkov. Takšne odločitve verjetno ne sprejema le podatkovni znanstvenik, vendar se lahko znajde v situaciji, ko mora sprejeti odločitve o tem, kako delati s podatki glede na način njihovega shranjevanja.

Tukaj je nekaj vidikov sodobnih sistemov za shranjevanje podatkov, ki lahko vplivajo na te odločitve:

**Na lokaciji vs. zunaj lokacije vs. javni ali zasebni oblak**

Na lokaciji pomeni gostovanje in upravljanje podatkov na lastni opremi, kot je strežnik s trdimi diski, ki shranjujejo podatke, medtem ko zunaj lokacije pomeni zanašanje na opremo, ki ni v vaši lasti, kot je podatkovni center. Javni oblak je priljubljena izbira za shranjevanje podatkov, ki ne zahteva znanja o tem, kako ali kje so podatki natančno shranjeni, pri čemer javni pomeni enotno osnovno infrastrukturo, ki jo delijo vsi uporabniki oblaka. Nekatere organizacije imajo stroge varnostne politike, ki zahtevajo popoln dostop do opreme, kjer so podatki gostovani, in se zanašajo na zasebni oblak, ki zagotavlja lastne storitve v oblaku. Več o podatkih v oblaku boste izvedeli v [kasnejših lekcijah](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/5-Data-Science-In-Cloud).

**Hladni vs. vroči podatki**

Pri treniranju modelov boste morda potrebovali več podatkov za treniranje. Če ste zadovoljni z modelom, bodo novi podatki prispeli, da bo model služil svojemu namenu. V vsakem primeru se bodo stroški shranjevanja in dostopa do podatkov povečali, ko jih boste kopičili. Ločevanje redko uporabljenih podatkov, znanih kot hladni podatki, od pogosto dostopanih vročih podatkov je lahko cenejša možnost shranjevanja podatkov prek strojne ali programske opreme. Če je treba dostopati do hladnih podatkov, lahko traja nekoliko dlje v primerjavi z vročimi podatki.

### Upravljanje podatkov

Med delom s podatki lahko ugotovite, da je treba nekatere podatke očistiti z uporabo tehnik, obravnavanih v lekciji o [pripravi podatkov](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/08-data-preparation), da zgradite natančne modele. Ko prispejo novi podatki, bo treba uporabiti enake postopke za ohranjanje doslednosti kakovosti. Nekateri projekti bodo vključevali uporabo avtomatiziranega orodja za čiščenje, združevanje in stiskanje podatkov, preden se premaknejo na končno lokacijo. Azure Data Factory je primer enega od teh orodij.

### Varovanje podatkov

Eden glavnih ciljev varovanja podatkov je zagotoviti, da tisti, ki delajo z njimi, nadzorujejo, kaj se zbira in v kakšnem kontekstu se uporablja. Ohranjanje varnosti podatkov vključuje omejevanje dostopa le na tiste, ki ga potrebujejo, spoštovanje lokalnih zakonov in predpisov ter ohranjanje etičnih standardov, kot je obravnavano v [lekciji o etiki](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/02-ethics).

Tukaj je nekaj stvari, ki jih lahko ekipa naredi z mislijo na varnost:
- Potrdi, da so vsi podatki šifrirani
- Strankam zagotovi informacije o tem, kako se njihovi podatki uporabljajo
- Odstrani dostop do podatkov tistim, ki so zapustili projekt
- Dovoli le določenim članom projekta spreminjanje podatkov

## 🚀 Izziv

Obstaja veliko različic življenjskega cikla podatkovne znanosti, kjer ima vsak korak lahko različna imena in število faz, vendar vsebuje enake procese, omenjene v tej lekciji.

Raziskujte [Team Data Science Process lifecycle](https://docs.microsoft.com/en-us/azure/architecture/data-science-process/lifecycle) in [Cross-industry standard process for data mining](https://www.datascience-pm.com/crisp-dm-2/). Poimenujte 3 podobnosti in razlike med obema.

|Team Data Science Process (TDSP)|Cross-industry standard process for data mining (CRISP-DM)|
|--|--|
|![Team Data Science Lifecycle](../../../../4-Data-Science-Lifecycle/14-Introduction/images/tdsp-lifecycle2.png) | ![Data Science Process Alliance Image](../../../../4-Data-Science-Lifecycle/14-Introduction/images/CRISP-DM.png) |
| Slika avtorja [Microsoft](https://docs.microsoft.comazure/architecture/data-science-process/lifecycle) | Slika avtorja [Data Science Process Alliance](https://www.datascience-pm.com/crisp-dm-2/) |

## [Kviz po lekciji](https://ff-quizzes.netlify.app/en/ds/quiz/27)

## Pregled in samostojno učenje

Uporaba življenjskega cikla podatkovne znanosti vključuje več vlog in nalog, pri čemer se nekateri osredotočajo na določene dele vsake faze. Team Data Science Process ponuja nekaj virov, ki pojasnjujejo vrste vlog in nalog, ki jih lahko nekdo ima v projektu.

* [Vloge in naloge v procesu podatkovne znanosti](https://docs.microsoft.com/en-us/azure/architecture/data-science-process/roles-tasks)
* [Izvajanje nalog podatkovne znanosti: raziskovanje, modeliranje in uvajanje](https://docs.microsoft.com/en-us/azure/architecture/data-science-process/execute-data-science-tasks)

## Naloga

[Ocena nabora podatkov](assignment.md)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne odgovarjamo za morebitna napačna razumevanja ali napačne interpretacije, ki bi nastale zaradi uporabe tega prevoda.