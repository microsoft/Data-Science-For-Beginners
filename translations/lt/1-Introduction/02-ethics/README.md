<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8796f41f566a0a8ebb72863a83d558ed",
  "translation_date": "2025-08-31T06:00:08+00:00",
  "source_file": "1-Introduction/02-ethics/README.md",
  "language_code": "lt"
}
-->
# Duomenų etikos įvadas

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/02-Ethics.png)|
|:---:|
| Duomenų mokslo etika - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

---

Mes visi esame duomenų piliečiai, gyvenantys duomenų pasaulyje.

Rinkos tendencijos rodo, kad iki 2022 m. 1 iš 3 didelių organizacijų pirks ir parduos savo duomenis per internetines [turgavietes ir mainų platformas](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/). Kaip **programėlių kūrėjai**, mes pastebėsime, kad duomenimis pagrįstų įžvalgų ir algoritmais pagrįstos automatizacijos integravimas į kasdienes vartotojų patirtis taps lengvesnis ir pigesnis. Tačiau, kai dirbtinis intelektas tampa visur paplitęs, turėsime suprasti ir galimą žalą, kurią gali sukelti tokių algoritmų [ginklavimas](https://www.youtube.com/watch?v=TQHs8SA1qpk) dideliu mastu.

Tendencijos taip pat rodo, kad iki 2025 m. sukursime ir suvartosime daugiau nei [180 zettabaitų](https://www.statista.com/statistics/871513/worldwide-data-created/) duomenų. Kaip **duomenų mokslininkai**, mes turėsime precedento neturintį prieigą prie asmeninių duomenų. Tai reiškia, kad galėsime kurti vartotojų elgsenos profilius ir daryti įtaką sprendimų priėmimui taip, kad sukurtume [laisvo pasirinkimo iliuziją](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice), tuo pačiu galimai nukreipdami vartotojus link mums pageidaujamų rezultatų. Tai taip pat kelia platesnius klausimus apie duomenų privatumą ir vartotojų apsaugą.

Duomenų etika dabar yra _būtinos gairės_ duomenų mokslui ir inžinerijai, padedančios sumažinti galimą žalą ir netyčines pasekmes, kylančias iš mūsų veiksmų, pagrįstų duomenimis. [Gartner Hype Cycle for AI](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/) identifikuoja skaitmeninės etikos, atsakingo DI ir DI valdymo tendencijas kaip pagrindinius veiksnius, skatinančius didesnes megatendencijas, susijusias su DI _demokratizacija_ ir _industrializacija_.

![Gartner's Hype Cycle for AI - 2020](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

Šioje pamokoje mes nagrinėsime įdomią duomenų etikos sritį – nuo pagrindinių sąvokų ir iššūkių iki atvejų analizių ir taikomų DI koncepcijų, tokių kaip valdymas, kurios padeda sukurti etikos kultūrą komandose ir organizacijose, dirbančiose su duomenimis ir DI.

## [Prieš paskaitą vykdomas testas](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/2) 🎯

## Pagrindinės sąvokos

Pradėkime nuo pagrindinių terminų supratimo.

Žodis „etika“ kilęs iš [graikiško žodžio „ethikos“](https://en.wikipedia.org/wiki/Ethics) (ir jo šaknies „ethos“), reiškiančio _charakterį arba moralinę prigimtį_.

**Etika** – tai bendros vertybės ir moraliniai principai, kurie reguliuoja mūsų elgesį visuomenėje. Etika grindžiama ne įstatymais, o plačiai priimtomis normomis, kas yra „teisinga prieš neteisinga“. Tačiau etiniai svarstymai gali turėti įtakos įmonių valdymo iniciatyvoms ir vyriausybės reglamentams, kurie sukuria daugiau paskatų laikytis taisyklių.

**Duomenų etika** yra [nauja etikos šaka](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1), kuri „tiria ir vertina moralines problemas, susijusias su _duomenimis, algoritmais ir atitinkama praktika_“. Čia **„duomenys“** apima veiksmus, susijusius su duomenų generavimu, įrašymu, tvarkymu, apdorojimu, platinimu, dalijimusi ir naudojimu, **„algoritmai“** apima DI, agentus, mašininį mokymąsi ir robotus, o **„praktika“** apima tokias temas kaip atsakingos inovacijos, programavimas, įsilaužimai ir etikos kodeksai.

**Taikomoji etika** yra [moralinių svarstymų praktinis taikymas](https://en.wikipedia.org/wiki/Applied_ethics). Tai procesas, kai aktyviai tiriamos etinės problemos realių veiksmų, produktų ir procesų kontekste, ir imamasi korekcinių veiksmų, kad jie išliktų suderinti su mūsų apibrėžtomis etinėmis vertybėmis.

**Etikos kultūra** yra apie [_taikomosios etikos įgyvendinimą_](https://hbr.org/2019/05/how-to-design-an-ethical-organization), siekiant užtikrinti, kad mūsų etikos principai ir praktika būtų nuosekliai ir masteliškai taikomi visoje organizacijoje. Sėkmingos etikos kultūros apibrėžia organizacijos mastu taikomus etikos principus, suteikia prasmingas paskatas laikytis taisyklių ir stiprina etikos normas, skatindamos ir amplifikuodamos pageidaujamą elgesį kiekviename organizacijos lygmenyje.

## Etikos sąvokos

Šioje dalyje aptarsime tokias sąvokas kaip **bendros vertybės** (principai) ir **etikos iššūkiai** (problemos) duomenų etikoje – ir nagrinėsime **atvejų analizes**, kurios padės suprasti šias sąvokas realiame kontekste.

### 1. Etikos principai

Kiekviena duomenų etikos strategija prasideda nuo _etinių principų_ apibrėžimo – „bendrų vertybių“, kurios apibūdina priimtiną elgesį ir vadovauja atitinkamiems veiksmams mūsų duomenų ir DI projektuose. Juos galima apibrėžti individualiu ar komandos lygmeniu. Tačiau dauguma didelių organizacijų šiuos principus apibrėžia _etinio DI_ misijos pareiškime arba sistemoje, kuri yra nustatyta korporaciniu lygmeniu ir nuosekliai taikoma visose komandose.

**Pavyzdys:** „Microsoft“ [atsakingo DI](https://www.microsoft.com/en-us/ai/responsible-ai) misijos pareiškimas skamba taip: _„Mes esame įsipareigoję skatinti DI, vadovaujantis etikos principais, kurie pirmiausia rūpinasi žmonėmis“_ – identifikuojant 6 etikos principus žemiau pateiktoje sistemoje:

![Atsakingas DI „Microsoft“](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

Trumpai aptarkime šiuos principus. _Skaidrumas_ ir _atsakomybė_ yra pagrindinės vertybės, ant kurių statomi kiti principai – todėl pradėkime nuo jų:

* [**Atsakomybė**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) užtikrina, kad specialistai būtų _atsakingi_ už savo duomenų ir DI veiksmus bei atitiktį šiems etikos principams.
* [**Skaidrumas**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) užtikrina, kad duomenų ir DI veiksmai būtų _suprantami_ vartotojams, paaiškinant, kas ir kodėl buvo nuspręsta.
* [**Teisingumas**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) – siekia užtikrinti, kad DI elgtųsi _teisingai su visais žmonėmis_, sprendžiant bet kokias sistemines ar implicitines šališkumo problemas duomenyse ir sistemose.
* [**Patikimumas ir saugumas**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) – užtikrina, kad DI elgtųsi _nuosekliai_ su apibrėžtomis vertybėmis, sumažinant galimą žalą ar netyčines pasekmes.
* [**Privatumas ir saugumas**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) – tai duomenų kilmės supratimas ir _duomenų privatumo bei susijusių apsaugų_ teikimas vartotojams.
* [**Įtrauktis**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) – tai DI sprendimų kūrimas su intencija, pritaikant juos, kad jie atitiktų _platų žmonių poreikių ir gebėjimų spektrą_.

> 🚨 Pagalvokite, kokia galėtų būti jūsų duomenų etikos misijos pareiškimas. Išnagrinėkite kitų organizacijų etinio DI sistemas – čia pateikiami pavyzdžiai iš [IBM](https://www.ibm.com/cloud/learn/ai-ethics), [Google](https://ai.google/principles) ir [Facebook](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/). Kokias bendras vertybes jie turi? Kaip šie principai susiję su DI produktu ar pramone, kurioje jie veikia?

### 2. Etikos iššūkiai

Kai turime apibrėžtus etikos principus, kitas žingsnis yra įvertinti mūsų duomenų ir DI veiksmus, siekiant nustatyti, ar jie atitinka šias bendras vertybes. Pagalvokite apie savo veiksmus dviejose kategorijose: _duomenų rinkimas_ ir _algoritmų kūrimas_.

Renkant duomenis, veiksmai greičiausiai apims **asmeninius duomenis** arba asmeniškai identifikuojamą informaciją (PII), susijusią su atpažįstamais gyvais asmenimis. Tai apima [įvairius neasmeninių duomenų elementus](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en), kurie _kartu_ gali identifikuoti asmenį. Etikos iššūkiai gali būti susiję su _duomenų privatumu_, _duomenų nuosavybe_ ir susijusiomis temomis, tokiomis kaip _informuotas sutikimas_ ir _intelektinės nuosavybės teisės_ vartotojams.

Kuriant algoritmus, veiksmai apims **duomenų rinkinių** rinkimą ir tvarkymą, o tada jų naudojimą **duomenų modeliams** mokyti ir diegti, siekiant prognozuoti rezultatus arba automatizuoti sprendimus realiame kontekste. Etikos iššūkiai gali kilti dėl _rinkinio šališkumo_, _duomenų kokybės_ problemų, _neteisingumo_ ir _klaidingo atvaizdavimo_ algoritmuose – įskaitant kai kurias sistemines problemas.

Abiem atvejais etikos iššūkiai pabrėžia sritis, kuriose mūsų veiksmai gali prieštarauti mūsų bendroms vertybėms. Norėdami aptikti, sumažinti, sušvelninti ar pašalinti šias problemas, turime užduoti moralinius „taip/ne“ klausimus, susijusius su mūsų veiksmais, ir prireikus imtis korekcinių veiksmų. Pažvelkime į kai kuriuos etikos iššūkius ir moralinius klausimus, kuriuos jie kelia:

#### 2.1 Duomenų nuosavybė

Duomenų rinkimas dažnai apima asmeninius duomenis, kurie gali identifikuoti duomenų subjektus. [Duomenų nuosavybė](https://permission.io/blog/data-ownership) yra apie _kontrolę_ ir [_vartotojų teises_](https://permission.io/blog/data-ownership), susijusias su duomenų kūrimu, apdorojimu ir platinimu.

Moraliniai klausimai, kuriuos turime užduoti:
 * Kas valdo duomenis? (vartotojas ar organizacija)
 * Kokias teises turi duomenų subjektai? (pvz., prieiga, ištrynimas, perkeliamumas)
 * Kokias teises turi organizacijos? (pvz., taisyti kenksmingas vartotojų apžvalgas)

#### 2.2 Informuotas sutikimas

[Informuotas sutikimas](https://legaldictionary.net/informed-consent/) apibrėžia veiksmą, kai vartotojai sutinka su veiksmu (pvz., duomenų rinkimu), turėdami _pilną supratimą_ apie svarbius faktus, įskaitant tikslą, galimą riziką ir alternatyvas.

Klausimai, kuriuos reikia nagrinėti:
 * Ar vartotojas (duomenų subjektas) davė leidimą rinkti ir naudoti duomenis?
 * Ar vartotojas suprato tikslą, dėl kurio buvo renkami duomenys?
 * Ar vartotojas suprato galimą riziką, susijusią su jų dalyvavimu?

#### 2.3 Intelektinė nuosavybė

[Intelektinė nuosavybė](https://en.wikipedia.org/wiki/Intellectual_property) reiškia nematerialius kūrinius, atsiradusius dėl žmogaus iniciatyvos, kurie gali _turėti ekonominę vertę_ asmenims ar verslui.

Klausimai, kuriuos reikia nagrinėti:
 * Ar surinkti duomenys turėjo ekonominę vertę vartotojui ar verslui?
 * Ar **vartotojas** turi intelektinę nuosavybę čia?
 * Ar **organizacija** turi intelektinę nuosavybę čia?
 * Jei šios teisės egzistuoja, kaip mes jas saugome?

#### 2.4 Duomenų privatumas

[Duomenų privatumas](https://www.northeastern.edu/graduate/blog/what-is-data-privacy/) arba informacijos privatumas reiškia vartotojų privatumo išsaugojimą ir jų tapatybės apsaugą, susijusią su asmeniškai identifikuojama informacija.

Klausimai, kuriuos reikia nagrinėti:
 * Ar vartotojų (asmeniniai) duomenys yra apsaugoti nuo įsilaužimų ir nutekėjimų?
 * Ar vartotojų duomenys yra prieinami tik įgaliotiems vartotojams ir kontekstams?
 * Ar vartotojų anonimiškumas išsaugomas, kai duomenys yra dalijami ar platinami?
 * Ar vartotojas gali būti deanonimizuotas iš anonimizuotų duomenų rinkinių?

#### 2.5 Teisė būti pamirštam

[Teisė būti pamirštam](https://en.wikipedia.org/wiki/Right_to_be_forgotten) arba [teisė į ištrynimą](https://www.gdpreu.org/right-to-be-forgotten/) suteikia papildomą asmeninių duomenų apsaugą vartotojams. Konkrečiai, ji suteikia vartotojams teisę prašyti asmeninių duomenų ištrynimo ar pašalinimo iš interneto paieškų ir kitų vietų, _tam tikromis aplinkybėmis_ – leidžiant jiems pradėti iš naujo internete, nes jų praeities veiksmai nebūtų laikomi prieš juos.

Klausimai, kuriuos reikia nagrinėti:
 * Ar sistema leidžia duomenų subjektams prašyti ištrynimo?
 * Ar vartotojo sutikimo atšaukimas turėtų automatiškai sukelti ištrynimą?
 * Ar duomenys buvo surinkti be sutikimo ar neteisėtomis priemonėmis?
 * Ar mes laikomės vyriausybės reglamentų dėl duomenų privatumo?

#### 2.6 Duomenų rinkinio šališkumas

Duomenų rinkinys arba [rinkimo š
[Algoritmų sąžiningumas](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f) tikrina, ar algoritmų kūrimas sistemingai nediskriminuoja tam tikrų duomenų subjektų grupių, sukeldamas [galimą žalą](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml) _paskirstymo_ (kai ištekliai atimami arba nesuteikiami tai grupei) ir _paslaugų kokybės_ (kai dirbtinis intelektas nėra toks tikslus kai kurioms grupėms kaip kitoms) srityse.

Klausimai, kuriuos verta apsvarstyti:
 * Ar įvertinome modelio tikslumą įvairioms grupėms ir sąlygoms?
 * Ar išanalizavome sistemą dėl galimos žalos (pvz., stereotipizavimo)?
 * Ar galime peržiūrėti duomenis arba iš naujo apmokyti modelius, kad sumažintume nustatytą žalą?

Susipažinkite su tokiais šaltiniais kaip [AI sąžiningumo kontroliniai sąrašai](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA), kad sužinotumėte daugiau.

#### 2.9 Netinkamas duomenų pateikimas

[Netinkamas duomenų pateikimas](https://www.sciencedirect.com/topics/computer-science/misrepresentation) kelia klausimą, ar mes pateikiame įžvalgas iš sąžiningai pateiktų duomenų taip, kad klaidintume ir palaikytume norimą naratyvą.

Klausimai, kuriuos verta apsvarstyti:
 * Ar pateikiame neišsamius ar netikslius duomenis?
 * Ar vizualizuojame duomenis taip, kad sukeltume klaidingas išvadas?
 * Ar naudojame selektyvius statistinius metodus rezultatams manipuliuoti?
 * Ar yra alternatyvių paaiškinimų, kurie galėtų pateikti kitokią išvadą?

#### 2.10 Laisvo pasirinkimo iliuzija

[Laisvo pasirinkimo iliuzija](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) atsiranda, kai sistemos „pasirinkimo architektūros“ naudoja sprendimų priėmimo algoritmus, kad paskatintų žmones priimti pageidaujamą rezultatą, tuo pačiu suteikdamos jiems pasirinkimo ir kontrolės iliuziją. Šie [tamsieji modeliai](https://www.darkpatterns.org/) gali sukelti socialinę ir ekonominę žalą vartotojams. Kadangi vartotojų sprendimai daro įtaką elgsenos profiliams, šie veiksmai gali sustiprinti arba pratęsti šios žalos poveikį.

Klausimai, kuriuos verta apsvarstyti:
 * Ar vartotojas suprato, kokias pasekmes turi jo pasirinkimas?
 * Ar vartotojas buvo informuotas apie (alternatyvius) pasirinkimus ir jų privalumus bei trūkumus?
 * Ar vartotojas gali vėliau atšaukti automatizuotą ar įtakotą pasirinkimą?

### 3. Atvejų analizės

Norint suprasti šiuos etikos iššūkius realiame pasaulyje, verta peržiūrėti atvejų analizes, kurios parodo galimą žalą ir pasekmes asmenims bei visuomenei, kai tokie etikos pažeidimai yra ignoruojami.

Štai keletas pavyzdžių:

| Etikos iššūkis | Atvejo analizė  | 
|--- |--- |
| **Informuotas sutikimas** | 1972 m. - [Tuskegee sifilio tyrimas](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - Afroamerikiečiai vyrai, dalyvavę tyrime, buvo pažadėti nemokama medicininė priežiūra, _bet buvo apgauti_ tyrėjų, kurie neinformavo jų apie diagnozę ar gydymo galimybes. Daugelis dalyvių mirė, o jų partneriai ar vaikai buvo paveikti; tyrimas truko 40 metų. | 
| **Duomenų privatumas** | 2007 m. - [Netflix duomenų prizas](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) pateikė tyrėjams _10 mln. anonimizuotų filmų įvertinimų iš 50 tūkst. klientų_, siekiant pagerinti rekomendacijų algoritmus. Tačiau tyrėjai sugebėjo susieti anonimizuotus duomenis su asmeniškai identifikuojamais duomenimis iš _išorinių duomenų rinkinių_ (pvz., IMDb komentarų), efektyviai „deanonimizuodami“ kai kuriuos Netflix abonentus.|
| **Duomenų rinkimo šališkumas** | 2013 m. - Bostono miestas [sukūrė Street Bump](https://www.boston.gov/transportation/street-bump), programėlę, leidžiančią piliečiams pranešti apie duobes, suteikiant miestui geresnius duomenis apie kelių būklę. Tačiau [žmonės iš mažesnių pajamų grupių turėjo mažiau prieigos prie automobilių ir telefonų](https://hbr.org/2013/04/the-hidden-biases-in-big-data), todėl jų kelių problemos tapo nematomos šioje programėlėje. Kūrėjai bendradarbiavo su akademikais, kad spręstų _teisingos prieigos ir skaitmeninės atskirties_ klausimus. |
| **Algoritmų sąžiningumas** | 2018 m. - MIT [Gender Shades tyrimas](http://gendershades.org/overview.html) įvertino AI produktų tikslumą pagal lytį, atskleisdamas tikslumo spragas moterims ir spalvotiems žmonėms. [2019 m. Apple kortelė](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/) atrodė, kad siūlo mažiau kredito moterims nei vyrams. Abu atvejai parodė algoritminio šališkumo problemas, sukeliančias socialinę ir ekonominę žalą.|
| **Netinkamas duomenų pateikimas** | 2020 m. - [Džordžijos sveikatos departamentas paskelbė COVID-19 diagramas](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening), kurios atrodė klaidinančios piliečius apie patvirtintų atvejų tendencijas, pateikdamos nechronologinę x ašies tvarką. Tai iliustruoja netinkamą pateikimą naudojant vizualizacijos triukus. |
| **Laisvo pasirinkimo iliuzija** | 2020 m. - Mokymosi programėlė [ABCmouse sumokėjo 10 mln. dolerių, kad išspręstų FTC skundą](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/), kai tėvai buvo priversti mokėti už prenumeratas, kurių negalėjo atšaukti. Tai iliustruoja tamsiuosius modelius pasirinkimo architektūrose, kur vartotojai buvo paskatinti priimti potencialiai žalingus sprendimus. |
| **Duomenų privatumas ir vartotojų teisės** | 2021 m. - Facebook [duomenų nutekėjimas](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users) atskleidė 530 mln. vartotojų duomenis, dėl ko buvo skirta 5 mlrd. dolerių bauda FTC. Tačiau Facebook atsisakė informuoti vartotojus apie nutekėjimą, pažeisdama vartotojų teises į duomenų skaidrumą ir prieigą. |

Norite sužinoti daugiau atvejų analizių? Peržiūrėkite šiuos šaltinius:
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - etikos dilemos įvairiose pramonės šakose. 
* [Duomenų mokslo etikos kursas](https://www.coursera.org/learn/data-science-ethics#syllabus) - svarbiausių atvejų analizės.
* [Kur viskas nepavyko](https://deon.drivendata.org/examples/) - Deon kontrolinis sąrašas su pavyzdžiais.

> 🚨 Pagalvokite apie matytas atvejų analizes – ar esate patyrę ar buvote paveikti panašaus etikos iššūkio savo gyvenime? Ar galite sugalvoti bent vieną kitą atvejo analizę, kuri iliustruotų vieną iš šiame skyriuje aptartų etikos iššūkių?

## Taikomoji etika

Mes aptarėme etikos sąvokas, iššūkius ir atvejų analizes realiame pasaulyje. Bet kaip pradėti _taikyti_ etikos principus ir praktikas savo projektuose? Ir kaip _įgyvendinti_ šias praktikas geresniam valdymui? Pažvelkime į keletą realių sprendimų:

### 1. Profesiniai kodeksai

Profesiniai kodeksai siūlo vieną iš būdų organizacijoms „skatinti“ narius palaikyti jų etikos principus ir misiją. Kodeksai yra _moralinės gairės_ profesiniam elgesiui, padedančios darbuotojams ar nariams priimti sprendimus, atitinkančius jų organizacijos principus. Jie yra veiksmingi tiek, kiek nariai savanoriškai jų laikosi; tačiau daugelis organizacijų siūlo papildomas paskatas ir bausmes, kad motyvuotų narius laikytis kodekso.

Pavyzdžiai:
 * [Oksfordo Miuncheno](http://www.code-of-ethics.org/code-of-conduct/) etikos kodeksas
 * [Duomenų mokslo asociacijos](http://datascienceassn.org/code-of-conduct.html) elgesio kodeksas (sukurtas 2013 m.)
 * [ACM etikos ir profesinio elgesio kodeksas](https://www.acm.org/code-of-ethics) (nuo 1993 m.)

> 🚨 Ar priklausote profesinei inžinerijos ar duomenų mokslo organizacijai? Peržiūrėkite jų svetainę, kad pamatytumėte, ar jie apibrėžia profesinį etikos kodeksą. Ką tai sako apie jų etikos principus? Kaip jie „skatina“ narius laikytis kodekso?

### 2. Etikos kontroliniai sąrašai

Nors profesiniai kodeksai apibrėžia reikalaujamą _etišką elgesį_ specialistams, jie [turi žinomų apribojimų](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) vykdymo užtikrinime, ypač didelio masto projektuose. Vietoj to, daugelis duomenų mokslo ekspertų [rekomenduoja kontrolinius sąrašus](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md), kurie gali **susieti principus su praktikomis** labiau apibrėžtais ir veiksmais pagrįstais būdais.

Kontroliniai sąrašai paverčia klausimus „taip/ne“ užduotimis, kurias galima įgyvendinti, leidžiant jas stebėti kaip standartinių produktų išleidimo darbo eigų dalį.

Pavyzdžiai:
 * [Deon](https://deon.drivendata.org/) - bendros paskirties duomenų etikos kontrolinis sąrašas, sukurtas remiantis [pramonės rekomendacijomis](https://deon.drivendata.org/#checklist-citations) su komandinės eilutės įrankiu lengvam integravimui.
 * [Privatumo audito kontrolinis sąrašas](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - pateikia bendras gaires informacijos tvarkymo praktikoms iš teisinės ir socialinės perspektyvos.
 * [AI sąžiningumo kontrolinis sąrašas](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - sukurtas AI specialistų, siekiant palaikyti sąžiningumo patikrinimų integravimą į AI kūrimo ciklus.
 * [22 klausimai apie etiką duomenyse ir AI](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - atviresnė sistema, skirta pradinei etikos klausimų analizei dizaino, įgyvendinimo ir organizaciniuose kontekstuose.

### 3. Etikos reguliavimas

Etika yra apie bendrų vertybių apibrėžimą ir teisingų veiksmų atlikimą _savanoriškai_. **Atitiktis** yra apie _įstatymų laikymąsi_, jei jie yra apibrėžti. **Valdymas** apima visas organizacijų veiklos formas, skirtas etikos principų įgyvendinimui ir nustatytų įstatymų laikymuisi.

Šiandien valdymas organizacijose vyksta dviem formomis. Pirma, tai yra apie **etiško AI** principų apibrėžimą ir praktikų įgyvendinimą, siekiant užtikrinti jų taikymą visuose organizacijos AI projektuose. Antra, tai yra apie visų vyriausybės nustatytų **duomenų apsaugos reguliavimų** laikymąsi regionuose, kuriuose organizacija veikia.

Duomenų apsaugos ir privatumo reguliavimo pavyzdžiai:

 * `1974`, [JAV Privatumo aktas](https://www.justice.gov/opcl/privacy-act-1974) - reguliuoja _federalinės vyriausybės_ asmeninės informacijos rinkimą, naudojimą ir atskleidimą.
 * `1996`, [JAV Sveikatos draudimo perkeliamumo ir atskaitomybės aktas (HIPAA)](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - saugo asmens sveikatos duomenis.
 * `1998`, [JAV Vaikų internetinio privatumo apsaugos aktas (COPPA)](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - saugo vaikų iki 13 metų duomenų privatumą.
 * `2018`, [Bendrasis duomenų apsaugos reglamentas (GDPR)](https://gdpr-info.eu/) - suteikia vartotojų teises, duomenų apsaugą ir privatumą.
 * `2018`, [Kalifornijos vartotojų privatumo aktas (CCPA)](https://www.oag.ca.gov/privacy/ccpa) suteikia vartotojams daugiau _teisių_ į jų (asmeninius) duomenis.
 * `2021`, Kinijos [Asmeninės informacijos apsaugos įstatymas](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) ką tik priimtas, sukuriantis vieną iš stipriausių internetinių duomenų privatumo reguliavimų pasaulyje.

> 🚨 Europos Sąjungos apibrėžtas GDPR (Bendrasis duomenų apsaugos reglamentas) išlieka vienu iš įtakingiausių duomenų privatumo reguliavimų šiandien. Ar žinojote, kad jis taip pat apibrėžia [8 vartotojų teises](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr), skirtas apsaugoti piliečių skaitmeninį privatumą ir asmens duomenis? Sužinokite, kokios jos yra ir kodėl jos svarbios.

### 4. Etikos kultūra

Atkreipkite dėmesį, kad vis dar egzistuoja nematomas atotrūkis tarp _atitikties_ (pakankamo veikimo pagal „įstatymo raidę“) ir [sisteminių problemų](https://www.coursera.org/learn/data-science-ethics/home/week/4) sprendimo (pvz., informacijos asimetrijos ir paskirstymo neteisingumo), kurios gali paspartinti AI ginklavimą.

Pastarasis reikalauja [bendradarbiavimo metodų etikos kultūrų kūrimui](https://towardsdatascience.com/why-ai-ethics-requires-a-culture-driven-approach-26f451afa29f), kurie užtikrina emocinius ryšius ir nuoseklias bendras vertybes _visose organizacijose_ pramonėje. Tai reikalauja daugiau [formalizuotų duomenų etikos kultūrų](https://www.codeforamerica.org/news/formalizing-an-ethical-data-culture/) organizacijose – leidžiant _bet kam_ [traukti Andon virvę](https://en.wikipedia.org/wiki/Andon_(manufacturing))
* [Atsakingo dirbtinio intelekto principai](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - nemokamas mokymosi kelias iš Microsoft Learn.  
* [Etika ir duomenų mokslas](https://resources.oreilly.com/examples/0636920203964) - O'Reilly elektroninė knyga (M. Loukides, H. Mason ir kt.)  
* [Duomenų mokslo etika](https://www.coursera.org/learn/data-science-ethics#syllabus) - internetinis kursas iš Mičigano universiteto.  
* [Etika atskleista](https://ethicsunwrapped.utexas.edu/case-studies) - atvejų analizės iš Teksaso universiteto.  

# Užduotis  

[Parašykite duomenų etikos atvejo analizę](assignment.md)  

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.