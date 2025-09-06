<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "07478c2092203a69087b9c76b1f4dd56",
  "translation_date": "2025-09-06T00:23:22+00:00",
  "source_file": "4-Data-Science-Lifecycle/14-Introduction/README.md",
  "language_code": "tl"
}
-->
# Panimula sa Lifecycle ng Data Science

|![ Sketchnote ni [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/14-DataScience-Lifecycle.png)|
|:---:|
| Panimula sa Lifecycle ng Data Science - _Sketchnote ni [@nitya](https://twitter.com/nitya)_ |

## [Pre-Lecture Quiz](https://ff-quizzes.netlify.app/en/ds/quiz/26)

Sa puntong ito, malamang napagtanto mo na ang data science ay isang proseso. Ang prosesong ito ay maaaring hatiin sa 5 yugto:

- Pagkuha
- Pagproseso
- Pagsusuri
- Komunikasyon
- Pagpapanatili

Ang araling ito ay nakatuon sa 3 bahagi ng lifecycle: pagkuha, pagproseso, at pagpapanatili.

![Diagram ng lifecycle ng data science](../../../../4-Data-Science-Lifecycle/14-Introduction/images/data-science-lifecycle.jpg)  
> Larawan mula sa [Berkeley School of Information](https://ischoolonline.berkeley.edu/data-science/what-is-data-science/)

## Pagkuha

Ang unang yugto ng lifecycle ay napakahalaga dahil nakasalalay dito ang mga susunod na yugto. Sa praktikal na aspeto, ito ay dalawang yugto na pinagsama: ang pagkuha ng data at ang pagtukoy sa layunin at mga problemang kailangang tugunan.  
Ang pagtukoy sa mga layunin ng proyekto ay nangangailangan ng mas malalim na konteksto sa problema o tanong. Una, kailangan nating tukuyin at makuha ang mga taong nangangailangan ng solusyon sa kanilang problema. Maaaring ito ay mga stakeholder sa isang negosyo o mga sponsor ng proyekto, na makakatulong sa pagtukoy kung sino o ano ang makikinabang sa proyekto, pati na rin kung ano at bakit nila ito kailangan. Ang isang malinaw na layunin ay dapat na masusukat at maikakategorya upang matukoy ang katanggap-tanggap na resulta.

Mga tanong na maaaring itanong ng isang data scientist:
- Nasubukan na ba ang problemang ito dati? Ano ang natuklasan?
- Naiintindihan ba ng lahat ang layunin at layunin ng proyekto?
- Mayroon bang kalabuan, at paano ito mababawasan?
- Ano ang mga limitasyon?
- Ano ang posibleng anyo ng resulta?
- Gaano karaming mga mapagkukunan (oras, tao, computational) ang magagamit?

Susunod ay ang pagtukoy, pagkolekta, at sa huli ay ang pag-explore sa data na kinakailangan upang maabot ang mga tinukoy na layunin. Sa hakbang na ito ng pagkuha, kailangang suriin ng mga data scientist ang dami at kalidad ng data. Nangangailangan ito ng ilang pag-explore ng data upang matiyak na ang nakuha ay makakatulong sa pag-abot sa nais na resulta.

Mga tanong na maaaring itanong ng isang data scientist tungkol sa data:
- Anong data ang mayroon na sa akin?
- Sino ang may-ari ng data na ito?
- Ano ang mga alalahanin sa privacy?
- Sapat ba ang data upang malutas ang problemang ito?
- Ang kalidad ba ng data ay katanggap-tanggap para sa problemang ito?
- Kung may natuklasang karagdagang impormasyon sa pamamagitan ng data na ito, dapat bang isaalang-alang ang pagbabago o muling pagtukoy sa mga layunin?

## Pagproseso

Ang yugto ng pagproseso sa lifecycle ay nakatuon sa pagtuklas ng mga pattern sa data pati na rin ang pagmomodelo. Ang ilang mga teknik na ginagamit sa yugto ng pagproseso ay nangangailangan ng mga estadistikal na pamamaraan upang matuklasan ang mga pattern. Karaniwan, ito ay magiging isang nakakapagod na gawain para sa isang tao na gawin sa isang malaking dataset, kaya't umaasa sa mga computer upang mapabilis ang proseso. Sa yugtong ito, nagkakaroon ng intersection ang data science at machine learning. Tulad ng natutunan mo sa unang aralin, ang machine learning ay ang proseso ng pagbuo ng mga modelo upang maunawaan ang data. Ang mga modelo ay representasyon ng relasyon sa pagitan ng mga variable sa data na tumutulong sa pagpredict ng mga resulta.

Mga karaniwang teknik na ginagamit sa yugtong ito ay sakop sa kurikulum ng ML for Beginners. Sundan ang mga link upang matuto pa tungkol sa mga ito:

- [Classification](https://github.com/microsoft/ML-For-Beginners/tree/main/4-Classification): Pag-oorganisa ng data sa mga kategorya para sa mas epektibong paggamit.
- [Clustering](https://github.com/microsoft/ML-For-Beginners/tree/main/5-Clustering): Paggrupo ng data sa mga magkakatulad na grupo.
- [Regression](https://github.com/microsoft/ML-For-Beginners/tree/main/2-Regression): Pagtukoy sa relasyon sa pagitan ng mga variable upang magpredict o magforecast ng mga halaga.

## Pagpapanatili

Sa diagram ng lifecycle, maaaring napansin mo na ang pagpapanatili ay nasa pagitan ng pagkuha at pagproseso. Ang pagpapanatili ay isang tuloy-tuloy na proseso ng pamamahala, pag-iimbak, at pag-secure ng data sa buong proseso ng proyekto at dapat isaalang-alang sa kabuuan ng proyekto.

### Pag-iimbak ng Data

Ang mga konsiderasyon kung paano at saan iniimbak ang data ay maaaring makaapekto sa gastos ng imbakan pati na rin ang performance ng bilis ng pag-access sa data. Ang mga desisyon tulad nito ay malamang na hindi lamang gagawin ng isang data scientist, ngunit maaaring kailanganin nilang gumawa ng mga pagpipilian kung paano gagamitin ang data batay sa kung paano ito iniimbak.

Narito ang ilang aspeto ng modernong sistema ng pag-iimbak ng data na maaaring makaapekto sa mga pagpipiliang ito:

**On premise vs off premise vs public o private cloud**

Ang on premise ay tumutukoy sa pagho-host at pamamahala ng data gamit ang sariling kagamitan, tulad ng pagmamay-ari ng server na may mga hard drive na nag-iimbak ng data, habang ang off premise ay umaasa sa kagamitan na hindi mo pagmamay-ari, tulad ng isang data center. Ang public cloud ay isang popular na opsyon para sa pag-iimbak ng data na hindi nangangailangan ng kaalaman kung paano o saan eksaktong iniimbak ang data, kung saan ang public ay tumutukoy sa isang unified underlying infrastructure na ginagamit ng lahat ng gumagamit ng cloud. Ang ilang mga organisasyon ay may mahigpit na mga patakaran sa seguridad na nangangailangan ng ganap na access sa kagamitan kung saan naka-host ang data at umaasa sa private cloud na nagbibigay ng sariling cloud services. Matututo ka pa tungkol sa data sa cloud sa [mga susunod na aralin](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/5-Data-Science-In-Cloud).

**Cold vs hot data**

Kapag sinasanay ang iyong mga modelo, maaaring kailanganin mo ng mas maraming training data. Kung kontento ka na sa iyong modelo, darating ang mas maraming data para magamit ang modelo sa layunin nito. Sa anumang kaso, ang gastos ng pag-iimbak at pag-access sa data ay tataas habang dumadami ito. Ang paghihiwalay ng bihirang ginagamit na data, na kilala bilang cold data, mula sa madalas na ginagamit na hot data ay maaaring maging mas murang opsyon sa pag-iimbak ng data sa pamamagitan ng hardware o software services. Kung kailangang ma-access ang cold data, maaaring mas matagal itong makuha kumpara sa hot data.

### Pamamahala ng Data

Habang nagtatrabaho ka sa data, maaaring matuklasan mo na ang ilan sa data ay kailangang linisin gamit ang ilang mga teknik na sakop sa aralin tungkol sa [data preparation](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/08-data-preparation) upang makabuo ng mga tumpak na modelo. Kapag may bagong data na dumating, kakailanganin nito ang parehong aplikasyon upang mapanatili ang pagkakapareho sa kalidad. Ang ilang mga proyekto ay maaaring gumamit ng automated na tool para sa cleansing, aggregation, at compression bago ilipat ang data sa huling lokasyon nito. Ang Azure Data Factory ay isang halimbawa ng isa sa mga tool na ito.

### Pag-secure ng Data

Isa sa mga pangunahing layunin ng pag-secure ng data ay tiyakin na ang mga nagtatrabaho dito ay may kontrol sa kung ano ang kinokolekta at sa anong konteksto ito ginagamit. Ang pagpapanatiling ligtas ng data ay nangangailangan ng limitadong access sa mga taong nangangailangan nito, pagsunod sa mga lokal na batas at regulasyon, pati na rin ang pagpapanatili ng mga pamantayang etikal, tulad ng sakop sa [ethics lesson](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/02-ethics).

Narito ang ilang bagay na maaaring gawin ng isang team na may seguridad sa isip:
- Tiyakin na ang lahat ng data ay naka-encrypt
- Magbigay ng impormasyon sa mga customer kung paano ginagamit ang kanilang data
- Alisin ang access sa data mula sa mga taong umalis na sa proyekto
- Payagan lamang ang ilang miyembro ng proyekto na baguhin ang data

## 🚀 Hamon

Maraming bersyon ng Lifecycle ng Data Science, kung saan ang bawat hakbang ay maaaring may iba't ibang pangalan at bilang ng mga yugto ngunit naglalaman ng parehong mga proseso na nabanggit sa araling ito.

Suriin ang [Team Data Science Process lifecycle](https://docs.microsoft.com/en-us/azure/architecture/data-science-process/lifecycle) at ang [Cross-industry standard process for data mining](https://www.datascience-pm.com/crisp-dm-2/). Magbanggit ng 3 pagkakatulad at pagkakaiba sa pagitan ng dalawa.

|Team Data Science Process (TDSP)|Cross-industry standard process for data mining (CRISP-DM)|
|--|--|
|![Team Data Science Lifecycle](../../../../4-Data-Science-Lifecycle/14-Introduction/images/tdsp-lifecycle2.png) | ![Data Science Process Alliance Image](../../../../4-Data-Science-Lifecycle/14-Introduction/images/CRISP-DM.png) |
| Larawan mula sa [Microsoft](https://docs.microsoft.comazure/architecture/data-science-process/lifecycle) | Larawan mula sa [Data Science Process Alliance](https://www.datascience-pm.com/crisp-dm-2/) |

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/27)

## Review at Pag-aaral sa Sarili

Ang pag-aaplay ng Lifecycle ng Data Science ay nangangailangan ng maraming tungkulin at gawain, kung saan ang ilan ay maaaring nakatuon sa partikular na bahagi ng bawat yugto. Ang Team Data Science Process ay nagbibigay ng ilang mga mapagkukunan na nagpapaliwanag sa mga uri ng tungkulin at gawain na maaaring mayroon ang isang tao sa isang proyekto.

* [Mga tungkulin at gawain sa Team Data Science Process](https://docs.microsoft.com/en-us/azure/architecture/data-science-process/roles-tasks)  
* [Pagganap ng mga gawain sa data science: exploration, modeling, at deployment](https://docs.microsoft.com/en-us/azure/architecture/data-science-process/execute-data-science-tasks)

## Takdang Aralin

[Pag-assess sa Dataset](assignment.md)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.