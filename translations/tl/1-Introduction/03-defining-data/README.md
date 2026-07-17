# Pagbibigay Kahulugan sa Datos

|![ Sketchnote mula kay [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Pagbibigay Kahulugan sa Datos - _Sketchnote mula kay [@nitya](https://twitter.com/nitya)_ |

Ang datos ay mga katotohanan, impormasyon, mga obserbasyon at mga panukat na ginagamit upang makagawa ng mga tuklas at suportahan ang mga may kaalamang desisyon. Ang isang data point ay isang hiwalay na yunit ng datos sa loob ng isang dataset, na isang koleksyon ng mga data points. Ang mga dataset ay maaaring magkakaiba ang format at estruktura, at karaniwang nakabase sa pinagmulan nito, o kung saan nagmula ang datos. Halimbawa, ang buwanang kita ng isang kumpanya ay maaaring nasa spreadsheet ngunit ang datos ng heart rate bawat oras mula sa isang smartwatch ay maaaring nasa [JSON](https://stackoverflow.com/a/383699) na format. Karaniwan para sa mga data scientist na magtrabaho sa iba't ibang uri ng datos sa loob ng isang dataset. 

Ang araling ito ay nakatuon sa pagtukoy at pagsuri ng datos ayon sa mga katangian nito at pinagmulan.

## [Pre-Lecture Quiz](https://ff-quizzes.netlify.app/en/ds/quiz/4)
## Paano Inilalarawan ang Datos

### Raw Data
Ang raw data ay datos na nagmula sa pinagmulan nito sa unang estado nito at hindi pa nasuri o naayos. Upang maunawaan kung ano ang nangyayari sa isang dataset, kailangan itong ayusin sa isang format na mauunawaan ng mga tao pati na rin ng teknolohiya na maaaring gamitin upang suriin ito ng mas malalim. Ang estruktura ng isang dataset ay naglalarawan kung paano ito naayos at maaaring uriin bilang structured, unstructured, at semi-structured. Ang mga uri ng estrukturang ito ay nagbabago depende sa pinagmulan pero karaniwang mapapaloob sa tatlong kategoryang ito. 

### Quantitative Data
Ang quantitative data ay mga numerikal na obserbasyon sa loob ng isang dataset at karaniwang maaaring pag-aralan, sukatin, at gamitin sa matematika. Ilan sa mga halimbawa ng quantitative data ay: populasyon ng isang bansa, taas ng isang tao, o kita ng isang kumpanya kada quarter. Sa karagdagang pagsusuri, ang quantitative data ay maaaring gamitin upang tuklasin ang mga seasonal na trend ng Air Quality Index (AQI) o tantiyahin ang posibilidad ng trapiko tuwing rush hour sa isang tipikal na araw ng trabaho.

### Qualitative Data
Ang qualitative data, na kilala rin bilang categorical data, ay datos na hindi maaaring masukat nang obhetibo tulad ng mga obserbasyon ng quantitative data. Ito ay karaniwang iba't ibang mga porma ng subjective na datos na kumakatawan sa kalidad ng isang bagay, tulad ng produkto o proseso. Minsan, ang qualitative data ay numerikal ngunit karaniwang hindi ginagamit sa matematika, gaya ng mga numero ng telepono o timestamps. Ilan sa mga halimbawa ng qualitative data ay: mga komento sa video, brand at modelo ng sasakyan, o paboritong kulay ng iyong mga malalapit na kaibigan. Ang qualitative data ay maaaring gamitin upang maunawaan kung alin sa mga produkto ang pinakagusto ng mga konsyumer o upang matukoy ang mga popular na keyword sa mga resume ng aplikasyon sa trabaho.

### Structured Data
Ang structured data ay datos na inayos sa mga hilera at kolum, kung saan bawat hilera ay may parehong set ng mga kolum. Ang mga kolum ay kumakatawan sa halaga ng isang partikular na uri at may pangalan na naglalarawan kung ano ang kinakatawan ng halaga, habang ang mga hilera ay naglalaman ng aktwal na mga halaga. Karaniwan, ang mga kolum ay may mga patakaran o limitasyon sa mga halaga upang matiyak na tama ang mga kinakatawang values sa kolum. Halimbawa, isipin ang isang spreadsheet ng mga customer kung saan bawat hilera ay dapat may numero ng telepono at ang mga numero ng telepono ay hindi naglalaman ng mga titik. Maaaring may mga patakaran para sa kolum ng numero ng telepono upang matiyak na hindi ito walang laman at naglalaman lamang ng mga numero. 

Isang benepisyo ng structured data ay maaari itong ayusin sa paraan na maiuugnay ito sa ibang structured data. Gayunpaman, dahil ang datos ay disenyo na maayos sa isang partikular na paraan, ang paggawa ng mga pagbabago sa kabuuang estruktura nito ay maaaring mangailangan ng maraming pagsisikap. Halimbawa, ang pagdagdag ng isang email column sa spreadsheet ng customer na hindi maaaring maging walang laman ay nangangahulugang kailangan mong planuhin kung paano mo idaragdag ang mga halagang ito sa mga kasalukuyang hilera ng mga customer sa dataset. 

Mga halimbawa ng structured data: spreadsheet, relational databases, numero ng telepono, bank statements

### Unstructured Data
Ang unstructured data ay karaniwang hindi maisasailalim sa mga hilera o kolum at walang tiyak na format o set ng mga patakaran na sinusunod. Dahil ang unstructured data ay may mas kaunting mga restriksiyon sa estruktura nito, mas madali itong dagdagan ng bagong impormasyon kumpara sa structured dataset. Kung ang isang sensor na kumukuha ng datos tungkol sa barometric pressure tuwing 2 minuto ay nakatanggap ng update na pinapayagan itong sukatin at irekord ang temperatura, hindi na kailangan baguhin ang umiiral na datos kung ito ay unstructured. Gayunpaman, maaaring tumagal ng mas matagal ang pagsusuri o imbestigasyon ng ganitong uri ng datos. Halimbawa, isang siyentipiko na nais alamin ang average na temperatura ng nakaraang buwan mula sa datos ng sensor, ngunit natuklasan na may "e" na naitala sa ilang bahagi ng datos bilang palatandaan na ito ay sira, hindi isang karaniwang numero, na nangangahulugang hindi kumpleto ang datos.

Mga halimbawa ng unstructured data: mga text file, mga text message, mga video file

### Semi-structured
Ang semi-structured data ay may mga katangian na pinagsasama ang structured at unstructured data. Karaniwan, hindi ito sumusunod sa format ng mga hilera at kolum ngunit inaayos sa paraang itinuturing na structured at maaaring sumunod sa isang tiyak na format o set ng mga patakaran. Ang estruktura ay nag-iiba sa bawat pinagmulan, tulad ng isang malinaw na hierarchy hanggang sa isang mas flexible na format na nagpapadali ng integrasyon ng bagong impormasyon. Ang metadata ay mga tagapagpahiwatig na tumutulong tukuyin kung paano inaayos at iniimbak ang datos at may iba't ibang pangalan depende sa uri ng datos. Ilan sa mga karaniwang tawag sa metadata ay tags, elements, entities, at attributes. Halimbawa, ang isang tipikal na email message ay may subject, body, at set ng mga recipient at maaaring iayos ayon sa sino o kailan ito ipinadala. 

Mga halimbawa ng semi-structured data: HTML, mga CSV file, JavaScript Object Notation (JSON)

## Mga Pinagmulan ng Datos 

Ang data source ay ang unang lokasyon kung saan nagmula ang datos, o kung saan ito "nakatira" at nag-iiba depende kung paano at kailan ito nakolekta. Ang datos na ginawa ng mga gumagamit nito ay tinatawag na primary data habang ang secondary data ay nagmumula sa pinagmulan na nangolekta ng datos para sa pangkalahatang gamit. Halimbawa, isang grupo ng mga siyentipiko na nangongolekta ng mga obserbasyon sa isang rainforest ay itinuturing na primary data at kung kanilang ibabahagi ito sa ibang mga siyentipiko, magiging secondary ito para sa mga gagamit nito. 

Ang mga database ay isang karaniwang pinagmulan at umaasa sa database management system upang i-host at panatilihin ang datos kung saan gumagamit ang mga user ng mga komang tinatawag na queries upang tuklasin ang datos. Ang mga file bilang pinagmulan ng datos ay maaaring audio, imahe, at video files pati na rin mga spreadsheet tulad ng Excel. Ang mga internet source ay isang karaniwang lokasyon para mag-host ng datos, kung saan makikita ang mga database pati na rin mga file. Ang application programming interfaces, kilala rin bilang APIs, ay nagpapahintulot sa mga programmer na gumawa ng mga paraan upang ibahagi ang datos sa panlabas na mga user sa pamamagitan ng internet, habang ang proseso ng web scraping ay kumukuha ng datos mula sa isang web page. Ang [mga aralin sa Paggamit ng Data](../../../../../../../../../2-Working-With-Data) ay nakatuon sa kung paano gamitin ang iba't ibang mga pinagmulan ng datos. 

## Konklusyon

Sa araling ito natutunan natin:

- Ano ang datos
- Paano inilalarawan ang datos
- Paano ikinakategorya at iniuri ang datos
- Saan maaaring matagpuan ang datos

## 🚀 Hamon

Ang Kaggle ay isang mahusay na pinagkukunan ng bukas na mga dataset. Gamitin ang [dataset search tool](https://www.kaggle.com/datasets) upang maghanap ng mga kawili-wiling dataset at uriin ang 3-5 mga dataset gamit ang mga sumusunod na kriteriya:

- Ang datos ba ay quantitative o qualitative?
- Ang datos ba ay structured, unstructured, o semi-structured?

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/5)



## Repaso at Sariling Pag-aaral

- Ang yunit ng Microsoft Learn na ito, na may pamagat na [Identify data formats](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats?pivots=text) ay may detalyadong pagtalakay sa structured, semi-structured, at unstructured data.

## Takdang Aralin

[Pag-uuri ng mga Dataset](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->