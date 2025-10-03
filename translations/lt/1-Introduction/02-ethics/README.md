<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58860ce9a4b8a564003d2752f7c72851",
  "translation_date": "2025-10-03T17:12:24+00:00",
  "source_file": "1-Introduction/02-ethics/README.md",
  "language_code": "lt"
}
-->
# Įvadas į duomenų etiką

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/02-Ethics.png)|
|:---:|
| Duomenų mokslo etika - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

---

Mes visi esame duomenų piliečiai, gyvenantys duomenų pasaulyje.

Rinkos tendencijos rodo, kad iki 2022 m. 1 iš 3 didelių organizacijų pirks ir parduos savo duomenis per internetines [rinkas ir mainų platformas](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/). Kaip **programėlių kūrėjai**, mes galėsime lengviau ir pigiau integruoti duomenimis pagrįstas įžvalgas ir algoritmais valdomą automatizaciją į kasdienes vartotojų patirtis. Tačiau, kai dirbtinis intelektas tampa visur paplitęs, turėsime suprasti galimą žalą, kurią gali sukelti tokių algoritmų [panaudojimas kaip ginklas](https://www.youtube.com/watch?v=TQHs8SA1qpk) dideliu mastu.

Tendencijos rodo, kad iki 2025 m. mes generuosime ir naudosime daugiau nei [180 zettabaitų](https://www.statista.com/statistics/871513/worldwide-data-created/) duomenų. **Duomenų mokslininkams** šis informacijos sprogimas suteikia precedento neturinčią prieigą prie asmeninių ir elgsenos duomenų. Tai suteikia galimybę kurti detalius vartotojų profilius ir subtiliai paveikti sprendimų priėmimą—dažnai taip, kad sukuriama [laisvo pasirinkimo iliuzija](https://www.datasciencecentral.com/the-pareto-set-and-the-paradox-of-choice/). Nors tai gali būti naudojama vartotojų nukreipimui link pageidaujamų rezultatų, tai taip pat kelia svarbius klausimus apie duomenų privatumą, autonomiją ir etines algoritminės įtakos ribas.

Duomenų etika dabar yra _būtinos gairės_ duomenų mokslui ir inžinerijai, padedančios sumažinti galimą žalą ir netyčines pasekmes, kylančias iš mūsų duomenimis pagrįstų veiksmų. [Gartner Hype Cycle for AI](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/) identifikuoja svarbias tendencijas skaitmeninėje etikoje, atsakingame dirbtiniame intelekte ir AI valdyme kaip pagrindinius veiksnius didesnėms megatendencijoms, susijusioms su _demokratizacija_ ir _industrializacija_ AI.

![Gartner's Hype Cycle for AI - 2020](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

Šioje pamokoje mes nagrinėsime įdomią duomenų etikos sritį—nuo pagrindinių sąvokų ir iššūkių iki atvejų analizės ir taikomų AI koncepcijų, tokių kaip valdymas, kurios padeda sukurti etikos kultūrą komandose ir organizacijose, dirbančiose su duomenimis ir AI.




## [Prieš paskaitos testas](https://ff-quizzes.netlify.app/en/ds/quiz/2) 🎯

## Pagrindinės sąvokos

Pradėkime nuo pagrindinių terminų supratimo.

Žodis „etika“ kilęs iš [graikiško žodžio „ethikos“](https://en.wikipedia.org/wiki/Ethics) (ir jo šaknies „ethos“), reiškiančio _charakterį ar moralinę prigimtį_. 

**Etika** yra apie bendras vertybes ir moralinius principus, kurie reguliuoja mūsų elgesį visuomenėje. Etika grindžiama ne įstatymais, o plačiai priimtomis normomis, kas yra „teisinga vs. neteisinga“. Tačiau etiniai svarstymai gali paveikti įmonių valdymo iniciatyvas ir vyriausybės reglamentus, kurie sukuria daugiau paskatų laikytis taisyklių.

**Duomenų etika** yra [nauja etikos šaka](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1), kuri „tiria ir vertina moralines problemas, susijusias su _duomenimis, algoritmais ir atitinkamomis praktikomis_“. Čia **„duomenys“** orientuojasi į veiksmus, susijusius su generavimu, įrašymu, kuravimu, apdorojimu, sklaida, dalijimusi ir naudojimu, **„algoritmai“** orientuojasi į AI, agentus, mašininį mokymąsi ir robotus, o **„praktikos“** orientuojasi į tokias temas kaip atsakinga inovacija, programavimas, įsilaužimas ir etikos kodeksai.

**Taikomoji etika** yra [moralinių svarstymų praktinis taikymas](https://en.wikipedia.org/wiki/Applied_ethics). Tai procesas, kai aktyviai tiriamos etinės problemos realių veiksmų, produktų ir procesų kontekste, ir imamasi korekcinių veiksmų, kad jie išliktų suderinti su apibrėžtomis etinėmis vertybėmis.

**Etikos kultūra** yra apie [_taikomosios etikos operatyvinimą_](https://hbr.org/2019/05/how-to-design-an-ethical-organization), siekiant užtikrinti, kad mūsų etiniai principai ir praktikos būtų nuosekliai ir masteliškai priimtos visoje organizacijoje. Sėkmingos etikos kultūros apibrėžia organizacijos mastu etinius principus, suteikia prasmingas paskatas laikytis taisyklių ir stiprina etikos normas, skatindamos ir amplifikuodamos pageidaujamą elgesį kiekviename organizacijos lygyje.


## Etikos sąvokos

Šiame skyriuje aptarsime tokias sąvokas kaip **bendros vertybės** (principai) ir **etikos iššūkiai** (problemos) duomenų etikoje—bei nagrinėsime **atvejų analizes**, kurios padės suprasti šias sąvokas realiame kontekste.

### 1. Etikos principai

Kiekviena duomenų etikos strategija prasideda nuo _etinių principų_ apibrėžimo—„bendrų vertybių“, kurios apibūdina priimtiną elgesį ir vadovauja veiksmams, atitinkantiems taisykles, mūsų duomenų ir AI projektuose. Juos galite apibrėžti individualiu ar komandos lygiu. Tačiau dauguma didelių organizacijų apibrėžia juos _etinio AI_ misijos pareiškime ar sistemoje, kuri yra apibrėžta korporatyviniu lygiu ir nuosekliai įgyvendinama visose komandose.

**Pavyzdys:** „Microsoft“ [atsakingo AI](https://www.microsoft.com/en-us/ai/responsible-ai) misijos pareiškimas skamba: _„Mes esame įsipareigoję AI pažangai, grindžiamai etiniais principais, kurie pirmiausia rūpinasi žmonėmis“_—identifikuojant 6 etinius principus žemiau pateiktoje sistemoje:

![Atsakingas AI „Microsoft“](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

Trumpai aptarkime šiuos principus. _Skaidrumas_ ir _atsakomybė_ yra pagrindinės vertybės, ant kurių statomi kiti principai—pradėkime nuo jų:

* [**Atsakomybė**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) daro praktikantus _atsakingus_ už jų duomenų ir AI operacijas bei atitiktį šiems etiniams principams.
* [**Skaidrumas**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) užtikrina, kad duomenų ir AI veiksmai būtų _suprantami_ vartotojams, paaiškinant, kas ir kodėl priimami sprendimai.
* [**Teisingumas**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6)—orientuojasi į tai, kad AI elgtųsi _su visais žmonėmis_ teisingai, sprendžiant bet kokius sisteminius ar implicitinius socialinius-techninius šališkumus duomenyse ir sistemose.
* [**Patikimumas ir saugumas**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6)—užtikrina, kad AI elgtųsi _nuosekliai_ su apibrėžtomis vertybėmis, sumažinant galimą žalą ar netyčines pasekmes.
* [**Privatumas ir saugumas**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6)—yra apie duomenų kilmės supratimą ir _duomenų privatumo bei susijusių apsaugų_ suteikimą vartotojams.
* [**Įtrauktis**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6)—yra apie AI sprendimų kūrimą su intencija, pritaikant juos _plačiam žmonių poreikių ir gebėjimų spektrui_.

> 🚨 Pagalvokite, kokia galėtų būti jūsų duomenų etikos misijos pareiškimas. Išnagrinėkite kitų organizacijų etinio AI sistemas—čia yra pavyzdžiai iš [IBM](https://www.ibm.com/cloud/learn/ai-ethics), [Google](https://ai.google/principles) ir [Facebook](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/). Kokias bendras vertybes jie turi? Kaip šie principai susiję su AI produktu ar pramone, kurioje jie veikia?

### 2. Etikos iššūkiai

Kai turime apibrėžtus etinius principus, kitas žingsnis yra įvertinti mūsų duomenų ir AI veiksmus, kad pamatytume, ar jie atitinka tas bendras vertybes. Pagalvokite apie savo veiksmus dviejose kategorijose: _duomenų rinkimas_ ir _algoritmų kūrimas_. 

Renkant duomenis, veiksmai greičiausiai apims **asmeninius duomenis** arba asmeniškai identifikuojamą informaciją (PII), susijusią su identifikuojamais gyvais asmenimis. Tai apima [įvairius neasmeninių duomenų elementus](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en), kurie _kolektyviai_ identifikuoja asmenį. Etikos iššūkiai gali būti susiję su _duomenų privatumu_, _duomenų nuosavybe_ ir susijusiomis temomis, tokiomis kaip _informuotas sutikimas_ ir _intelektinės nuosavybės teisės_ vartotojams.

Kuriant algoritmus, veiksmai apims **duomenų rinkinių** rinkimą ir kuravimą, o vėliau jų naudojimą **duomenų modelių** mokymui ir diegimui, kurie prognozuoja rezultatus arba automatizuoja sprendimus realiame kontekste. Etikos iššūkiai gali kilti dėl _duomenų rinkinio šališkumo_, _duomenų kokybės_ problemų, _neteisingumo_ ir _klaidingo atvaizdavimo_ algoritmuose—įskaitant kai kurias problemas, kurios yra sisteminio pobūdžio.

Abiem atvejais etikos iššūkiai pabrėžia sritis, kuriose mūsų veiksmai gali susidurti su konfliktu su mūsų bendromis vertybėmis. Norėdami aptikti, sumažinti, minimizuoti ar pašalinti šiuos rūpesčius, turime užduoti moralinius „taip/ne“ klausimus, susijusius su mūsų veiksmais, ir prireikus imtis korekcinių veiksmų. Pažvelkime į kai kuriuos etikos iššūkius ir moralinius klausimus, kuriuos jie kelia:


#### 2.1 Duomenų nuosavybė

Duomenų rinkimas dažnai apima asmeninius duomenis, kurie gali identifikuoti duomenų subjektus. [Duomenų nuosavybė](https://permission.io/blog/data-ownership) yra apie _kontrolę_ ir [_vartotojų teises_](https://permission.io/blog/data-ownership), susijusias su duomenų kūrimu, apdorojimu ir sklaida. 

Moraliniai klausimai, kuriuos turime užduoti:
 * Kas valdo duomenis? (vartotojas ar organizacija)
 * Kokias teises turi duomenų subjektai? (pvz., prieiga, ištrynimas, perkeliamumas)
 * Kokias teises turi organizacijos? (pvz., pataisyti kenksmingas vartotojų apžvalgas)

#### 2.2 Informuotas sutikimas

[Informuotas sutikimas](https://legaldictionary.net/informed-consent/) apibrėžia vartotojų sutikimą veiksmui (pvz., duomenų rinkimui) su _pilnu supratimu_ apie svarbius faktus, įskaitant tikslą, galimą riziką ir alternatyvas. 

Klausimai, kuriuos reikia nagrinėti:
 * Ar vartotojas (duomenų subjektas) davė leidimą duomenų rinkimui ir naudojimui?
 * Ar vartotojas suprato tikslą, dėl kurio tie duomenys buvo surinkti?
 * Ar vartotojas suprato galimą riziką, susijusią su jų dalyvavimu?

#### 2.3 Intelektinė nuosavybė

[Intelektinė nuosavybė](https://en.wikipedia.org/wiki/Intellectual_property) reiškia nematerialius kūrinius, atsiradusius iš žmogaus iniciatyvos, kurie gali _turėti ekonominę vertę_ asmenims ar verslui. 

Klausimai, kuriuos reikia nagrinėti:
 * Ar surinkti duomenys turėjo ekonominę vertę vartotojui ar verslui?
 * Ar **vartotojas** turi intelektinę nuosavybę čia?
 * Ar **organizacija** turi intelektinę nuosavybę čia?
 * Jei šios teisės egzistuoja, kaip mes jas saugome?

#### 2.4 Duomenų privatumas

[Duomenų privatumas](https://www.northeastern.edu/graduate/blog/what-is-data-privacy/) arba informacijos privatumas reiškia vartotojų privatumo išsaugojimą ir vartotojų tapatybės apsaugą, susijusią su asmeniškai identifikuojama informacija. 

Klausimai, kuriuos reikia nagrinėti:
 * Ar vartotojų (asmeniniai) duomenys yra apsaugoti nuo įsilaužimų ir nutekėjimų?
 * Ar vartotojų duomenys yra prieinami tik įgaliotiems vartotojams ir kontekstams?
 * Ar vartotojų anonimiškumas išsaugomas, kai duomenys yra dalijami ar skleidžiami?
 * Ar vartotojas gali būti deidentifikuotas iš anonimizuotų duomenų rinkinių?


#### 2.5 Teisė būti pamirštam

[Teisė būti pamirštam](https://en.wikipedia.org/wiki/Right_to_be_forgotten) arba [Teisė į ištrynimą](https://www.gdpreu.org/right-to-be-forgotten/) suteikia papildomą asmeninių duomenų apsaugą vartotojams. Konkrečiai, tai suteikia vartotojams teisę prašyti asmeninių duomenų ištrynimo ar pašalinimo iš interneto paieškų ir kitų vietų, _tam tikromis aplinkybėmis_—leidžiant jiems naują pradžią internete, be praeities veiksmų, kurie būtų laikomi prieš juos.

Klausimai, kuriuos reikia nagrinėti:
 * Ar sistema leidžia duomenų subjektams prašyti ištrynimo?
 * Ar vartotojo sutikimo atšaukimas turėtų automatiškai sukelti ištrynimą?
 * Ar duomenys buvo surinkti be sutikimo ar neteisėtais būdais?
 * Ar mes laikomės vyriausybės reglamentų dėl duomenų privatumo?


#### 2.6 Duomen
* Ar informacija užfiksuota _tiksliai_ atspindint realybę?

#### 2.8 Algoritmų sąžiningumas

[Algoritmų sąžiningumas](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f) tikrina, ar algoritmų dizainas sistemingai nediskriminuoja tam tikrų duomenų subjektų grupių, sukeldamas [galimą žalą](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml) _paskirstymo_ srityje (kai ištekliai atimami ar nesuteikiami tam tikrai grupei) ir _paslaugų kokybės_ srityje (kai dirbtinis intelektas nėra toks tikslus tam tikroms grupėms kaip kitoms).

Klausimai, kuriuos verta apsvarstyti:
* Ar įvertinome modelio tikslumą įvairioms grupėms ir sąlygoms?
* Ar išanalizavome sistemą dėl galimos žalos (pvz., stereotipų formavimo)?
* Ar galime peržiūrėti duomenis ar iš naujo apmokyti modelius, kad sumažintume nustatytą žalą?

Susipažinkite su tokiais šaltiniais kaip [AI sąžiningumo kontroliniai sąrašai](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA), kad sužinotumėte daugiau.

#### 2.9 Netinkamas duomenų pateikimas

[Netinkamas duomenų pateikimas](https://www.sciencedirect.com/topics/computer-science/misrepresentation) reiškia klausimą, ar mes pateikiame įžvalgas iš sąžiningai surinktų duomenų taip, kad klaidintume ir palaikytume norimą naratyvą.

Klausimai, kuriuos verta apsvarstyti:
* Ar pateikiame neišsamius ar netikslius duomenis?
* Ar vizualizuojame duomenis taip, kad sukeltume klaidingas išvadas?
* Ar naudojame selektyvius statistinius metodus rezultatams manipuliuoti?
* Ar yra alternatyvių paaiškinimų, kurie galėtų pasiūlyti kitokią išvadą?

#### 2.10 Laisvo pasirinkimo iliuzija

[Laisvo pasirinkimo iliuzija](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) atsiranda, kai sistemos „pasirinkimo architektūros“ naudoja sprendimų priėmimo algoritmus, kad paskatintų žmones priimti pageidaujamą rezultatą, tuo pačiu suteikiant jiems pasirinkimo ir kontrolės iliuziją. Tokie [tamsūs modeliai](https://www.darkpatterns.org/) gali sukelti socialinę ir ekonominę žalą vartotojams. Kadangi vartotojų sprendimai daro įtaką elgesio profiliams, šie veiksmai gali sustiprinti ar pratęsti šios žalos poveikį.

Klausimai, kuriuos verta apsvarstyti:
* Ar vartotojas suprato, kokias pasekmes turės jo pasirinkimas?
* Ar vartotojas buvo informuotas apie (alternatyvius) pasirinkimus ir jų privalumus bei trūkumus?
* Ar vartotojas gali atšaukti automatizuotą ar įtakotą pasirinkimą vėliau?

### 3. Atvejų analizės

Norint suprasti šiuos etikos iššūkius realiame pasaulyje, naudinga pažvelgti į atvejų analizes, kurios parodo galimą žalą ir pasekmes asmenims bei visuomenei, kai tokie etikos pažeidimai yra ignoruojami.

Štai keletas pavyzdžių:

| Etikos iššūkis | Atvejo analizė | 
|--- |--- |
| **Informuotas sutikimas** | 1972 m. - [Tuskegee sifilio tyrimas](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - Afrikos amerikiečiai vyrai, dalyvavę tyrime, buvo pažadėta nemokama medicininė priežiūra, _bet jie buvo apgauti_ tyrėjų, kurie neinformavo jų apie diagnozę ar gydymo galimybes. Daugelis dalyvių mirė, o jų partneriai ar vaikai buvo paveikti; tyrimas truko 40 metų. | 
| **Duomenų privatumas** | 2007 m. - [Netflix duomenų prizas](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) pateikė tyrėjams _10 mln. anonimizuotų filmų įvertinimų iš 50 tūkst. klientų_, siekiant pagerinti rekomendacijų algoritmus. Tačiau tyrėjai sugebėjo susieti anonimizuotus duomenis su asmeniškai identifikuojamais duomenimis iš _išorinių duomenų rinkinių_ (pvz., IMDb komentarų), efektyviai „deanonimizuodami“ kai kuriuos Netflix prenumeratorius.|
| **Surinkimo šališkumas** | 2013 m. - Bostono miestas [sukūrė Street Bump](https://www.boston.gov/transportation/street-bump), programėlę, leidžiančią piliečiams pranešti apie duobes, suteikiant miestui geresnius duomenis apie kelių problemas. Tačiau [žmonės iš mažesnių pajamų grupių turėjo mažiau prieigos prie automobilių ir telefonų](https://hbr.org/2013/04/the-hidden-biases-in-big-data), todėl jų kelių problemos tapo nematomos šioje programėlėje. Kūrėjai dirbo su akademikais, kad spręstų _teisingumo ir skaitmeninės atskirties_ klausimus. |
| **Algoritmų sąžiningumas** | 2018 m. - MIT [Gender Shades tyrimas](http://gendershades.org/overview.html) įvertino lyties klasifikavimo AI produktų tikslumą, atskleidžiant spragas tikslume moterims ir spalvotiems žmonėms. [2019 m. Apple kortelė](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/) atrodė, kad siūlo mažiau kredito moterims nei vyrams. Abu atvejai parodė algoritminio šališkumo problemas, sukeliančias socialinę ir ekonominę žalą.|
| **Netinkamas duomenų pateikimas** | 2020 m. - [Džordžijos sveikatos departamentas paskelbė COVID-19 diagramas](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening), kurios atrodė klaidinančios piliečius apie patvirtintų atvejų tendencijas, naudojant nechronologinę x ašies tvarką. Tai iliustruoja netinkamą pateikimą per vizualizacijos triukus. |
| **Laisvo pasirinkimo iliuzija** | 2020 m. - Mokymosi programėlė [ABCmouse sumokėjo 10 mln. dolerių, kad išspręstų FTC skundą](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/), kai tėvai buvo įstrigę mokėti už prenumeratas, kurių negalėjo atšaukti. Tai iliustruoja tamsius modelius pasirinkimo architektūrose, kur vartotojai buvo nukreipti į galimai žalingus pasirinkimus. |
| **Duomenų privatumas ir vartotojų teisės** | 2021 m. - Facebook [duomenų nutekėjimas](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users) atskleidė 530 mln. vartotojų duomenis, dėl ko buvo skirta 5 mlrd. dolerių bauda FTC. Tačiau Facebook atsisakė informuoti vartotojus apie nutekėjimą, pažeidžiant vartotojų teises į duomenų skaidrumą ir prieigą. |

Norite daugiau atvejų analizių? Peržiūrėkite šiuos šaltinius:
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - etikos dilemos įvairiose pramonės šakose.
* [Duomenų mokslo etikos kursas](https://www.coursera.org/learn/data-science-ethics#syllabus) - svarbiausi atvejų tyrimai.
* [Kur viskas suklydo](https://deon.drivendata.org/examples/) - Deon kontrolinis sąrašas su pavyzdžiais.

> 🚨 Pagalvokite apie matytus atvejų tyrimus – ar esate patyrę ar buvote paveikti panašaus etikos iššūkio savo gyvenime? Ar galite sugalvoti bent vieną kitą atvejo analizę, kuri iliustruotų vieną iš šiame skyriuje aptartų etikos iššūkių?

## Taikomoji etika

Mes aptarėme etikos sąvokas, iššūkius ir atvejų analizes realiame pasaulyje. Bet kaip pradėti _taikyti_ etikos principus ir praktiką savo projektuose? Ir kaip _operacionalizuoti_ šias praktikas geresniam valdymui? Pažvelkime į keletą realių sprendimų:

### 1. Profesiniai kodeksai

Profesiniai kodeksai siūlo vieną iš būdų organizacijoms „skatinti“ narius palaikyti jų etikos principus ir misijos pareiškimą. Kodeksai yra _moralinės gairės_ profesiniam elgesiui, padedančios darbuotojams ar nariams priimti sprendimus, atitinkančius jų organizacijos principus. Jie yra veiksmingi tiek, kiek nariai savanoriškai jų laikosi; tačiau daugelis organizacijų siūlo papildomus apdovanojimus ir bausmes, kad paskatintų narius laikytis kodekso.

Pavyzdžiai:
* [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/) Etikos kodeksas
* [Duomenų mokslo asociacija](http://datascienceassn.org/code-of-conduct.html) Elgesio kodeksas (sukurtas 2013 m.)
* [ACM Etikos ir profesinio elgesio kodeksas](https://www.acm.org/code-of-ethics) (nuo 1993 m.)

> 🚨 Ar priklausote profesinei inžinerijos ar duomenų mokslo organizacijai? Peržiūrėkite jų svetainę, kad pamatytumėte, ar jie apibrėžia profesinį etikos kodeksą. Ką tai sako apie jų etikos principus? Kaip jie „skatina“ narius laikytis kodekso?

### 2. Etikos kontroliniai sąrašai

Nors profesiniai kodeksai apibrėžia reikalaujamą _etišką elgesį_ iš praktikų, jie [turi žinomų apribojimų](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) vykdymo srityje, ypač didelio masto projektuose. Vietoj to, daugelis duomenų mokslo ekspertų [rekomenduoja kontrolinius sąrašus](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md), kurie gali **susieti principus su praktikomis** labiau deterministiniais ir veiksmais pagrįstais būdais.

Kontroliniai sąrašai paverčia klausimus „taip/ne“ užduotimis, kurias galima operacionalizuoti, leidžiant jas sekti kaip standartinių produktų išleidimo darbo eigų dalį.

Pavyzdžiai:
* [Deon](https://deon.drivendata.org/) - bendros paskirties duomenų etikos kontrolinis sąrašas, sukurtas remiantis [pramonės rekomendacijomis](https://deon.drivendata.org/#checklist-citations) su komandinės eilutės įrankiu lengvam integravimui.
* [Privatumo audito kontrolinis sąrašas](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - pateikia bendras gaires informacijos tvarkymo praktikoms iš teisinės ir socialinės perspektyvos.
* [AI sąžiningumo kontrolinis sąrašas](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - sukurtas AI praktikų, siekiant palaikyti sąžiningumo patikrinimų integraciją į AI kūrimo ciklus.
* [22 klausimai apie etiką duomenyse ir AI](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - atviresnė sistema, struktūrizuota pradiniam etikos klausimų tyrimui dizaino, įgyvendinimo ir organizaciniuose kontekstuose.

### 3. Etikos reglamentai

Etika yra apie bendrų vertybių apibrėžimą ir teisingų veiksmų atlikimą _savanoriškai_. **Atitiktis** yra apie _įstatymų laikymąsi_, jei ir kur jie yra apibrėžti. **Valdymas** apima visas organizacijų veiklos formas, skirtas etikos principų įgyvendinimui ir nustatytų įstatymų laikymuisi.

Šiandien valdymas organizacijose vyksta dviem formomis. Pirma, tai yra apie **etiško AI** principų apibrėžimą ir praktikų nustatymą, siekiant operacionalizuoti jų taikymą visiems organizacijos AI susijusiems projektams. Antra, tai yra apie visų vyriausybės nustatytų **duomenų apsaugos reglamentų** laikymąsi regionuose, kuriuose organizacija veikia.

Duomenų apsaugos ir privatumo reglamentų pavyzdžiai:
* `1974`, [JAV Privatumo aktas](https://www.justice.gov/opcl/privacy-act-1974) - reguliuoja _federalinės vyriausybės_ asmeninės informacijos rinkimą, naudojimą ir atskleidimą.
* `1996`, [JAV Sveikatos draudimo perkeliamumo ir atskaitomybės aktas (HIPAA)](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - saugo asmens sveikatos duomenis.
* `1998`, [JAV Vaikų internetinio privatumo apsaugos aktas (COPPA)](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - saugo vaikų iki 13 metų duomenų privatumą.
* `2018`, [Bendrasis duomenų apsaugos reglamentas (GDPR)](https://gdpr-info.eu/) - suteikia vartotojų teises, duomenų apsaugą ir privatumą.
* `2018`, [Kalifornijos vartotojų privatumo aktas (CCPA)](https://www.oag.ca.gov/privacy/ccpa) - suteikia vartotojams daugiau _teisių_ dėl jų (asmeninių) duomenų.
* `2021`, Kinijos [Asmeninės informacijos apsaugos įstatymas](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) - vienas stipriausių internetinių duomenų privatumo reglamentų pasaulyje.

> 🚨 Europos Sąjungos apibrėžtas GDPR (Bendrasis duomenų apsaugos reglamentas) išlieka vienu įtakingiausių duomenų privatumo reglamentų šiandien. Ar žinojote, kad jis taip pat apibrėžia [8 vartotojų teises](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr), skirtas apsaugoti piliečių skaitmeninį privatumą ir asmeninius duomenis? Sužinokite, kokios jos yra ir kodėl jos svarbios.

### 4. Etikos kultūra

Atkreipkite dėmesį, kad išlieka nematomas atotrūkis tarp _atitikties_ (pakankamo veikimo pagal „įstatymo raidę“) ir [sisteminių problemų](https://www.coursera.org/learn/data-science-ethics/home/week/4) sprendimo (pvz., informacijos asimetrijos ir paskirstymo neteisingumo), kurios gali paspartinti AI ginklavimą. 

Pastarasis reikalauja [bendradarbiavimo metodų etikos kultūrų apibrėžimui](https://towardsdatascience.com/why-ai-ethics-requires-a-culture-driven-approach-26f451afa29f), kurie kuria emocinius ryšius ir nuoseklias bendras vertybes _visose organizacijose_ pramonėje. Tai reikalauja daugiau [formalizuotų duomenų etikos kultūrų](https://www.codeforamerica.org/news/formalizing-an-ethical-data-culture/) organizacijose
* [Mašininis mokymasis pradedantiesiems](https://github.com/microsoft/ML-For-Beginners/blob/main/1-Introduction/3-fairness/README.md) - pamoka apie sąžiningumą, iš Microsoft.
* [Atsakingo dirbtinio intelekto principai](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - nemokamas mokymosi kelias iš Microsoft Learn.
* [Etika ir duomenų mokslas](https://resources.oreilly.com/examples/0636920203964) - O'Reilly elektroninė knyga (M. Loukides, H. Mason ir kt.)
* [Duomenų mokslo etika](https://www.coursera.org/learn/data-science-ethics#syllabus) - internetinis kursas iš Mičigano universiteto.
* [Etika be užuolankų](https://ethicsunwrapped.utexas.edu/case-studies) - atvejų analizės iš Teksaso universiteto.

# Užduotis

[Parašykite duomenų etikos atvejo analizę](assignment.md)

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus aiškinimus, kylančius dėl šio vertimo naudojimo.