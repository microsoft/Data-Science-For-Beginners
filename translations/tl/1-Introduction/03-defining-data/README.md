<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "12339119c0165da569a93ddba05f9339",
  "translation_date": "2025-09-06T00:30:36+00:00",
  "source_file": "1-Introduction/03-defining-data/README.md",
  "language_code": "tl"
}
-->
# Pagpapakahulugan ng Datos

|![ Sketchnote ni [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Pagpapakahulugan ng Datos - _Sketchnote ni [@nitya](https://twitter.com/nitya)_ |

Ang datos ay mga katotohanan, impormasyon, obserbasyon, at sukat na ginagamit upang makagawa ng mga tuklas at suportahan ang mga desisyong may kaalaman. Ang isang data point ay isang yunit ng datos sa loob ng isang dataset, na koleksyon ng mga data point. Ang mga dataset ay maaaring dumating sa iba't ibang format at istruktura, at karaniwang nakabatay sa pinagmulan nito, o kung saan nagmula ang datos. Halimbawa, ang buwanang kita ng isang kumpanya ay maaaring nasa spreadsheet ngunit ang datos ng oras-oras na tibok ng puso mula sa isang smartwatch ay maaaring nasa format na [JSON](https://stackoverflow.com/a/383699). Karaniwan para sa mga data scientist na magtrabaho sa iba't ibang uri ng datos sa loob ng isang dataset.

Ang araling ito ay nakatuon sa pagkilala at pag-uuri ng datos batay sa mga katangian nito at mga pinagmulan.

## [Pre-Lecture Quiz](https://ff-quizzes.netlify.app/en/ds/quiz/4)

## Paano Inilalarawan ang Datos

### Raw Data
Ang raw data ay datos na nagmula sa pinagmulan nito sa orihinal na estado at hindi pa nasusuri o naayos. Upang maunawaan kung ano ang nangyayari sa isang dataset, kailangang ayusin ito sa isang format na mauunawaan ng tao pati na rin ng teknolohiyang maaaring gamitin upang masuri ito nang higit pa. Ang istruktura ng isang dataset ay naglalarawan kung paano ito naayos at maaaring uriin bilang structured, unstructured, at semi-structured. Ang mga uri ng istruktura na ito ay mag-iiba depende sa pinagmulan ngunit sa huli ay magkasya sa tatlong kategoryang ito.

### Quantitative Data
Ang quantitative data ay mga numerikal na obserbasyon sa loob ng isang dataset at karaniwang maaaring suriin, sukatin, at gamitin sa matematika. Ilang halimbawa ng quantitative data ay: populasyon ng isang bansa, taas ng isang tao, o kita ng isang kumpanya kada quarter. Sa karagdagang pagsusuri, ang quantitative data ay maaaring gamitin upang matuklasan ang mga seasonal trend ng Air Quality Index (AQI) o tantiyahin ang posibilidad ng trapiko sa rush hour sa isang tipikal na araw ng trabaho.

### Qualitative Data
Ang qualitative data, na kilala rin bilang categorical data, ay datos na hindi maaaring sukatin nang objektibo tulad ng obserbasyon ng quantitative data. Karaniwan itong iba't ibang format ng subjektibong datos na naglalarawan sa kalidad ng isang bagay, tulad ng produkto o proseso. Minsan, ang qualitative data ay numerikal ngunit hindi karaniwang ginagamit sa matematika, tulad ng mga numero ng telepono o mga timestamp. Ilang halimbawa ng qualitative data ay: mga komento sa video, make at model ng kotse, o paboritong kulay ng pinakamalapit mong kaibigan. Ang qualitative data ay maaaring gamitin upang maunawaan kung aling mga produkto ang pinakagusto ng mga consumer o matukoy ang mga sikat na keyword sa mga resume ng aplikasyon sa trabaho.

### Structured Data
Ang structured data ay datos na naayos sa mga row at column, kung saan ang bawat row ay may parehong set ng column. Ang mga column ay kumakatawan sa isang halaga ng partikular na uri at makikilala sa isang pangalan na naglalarawan kung ano ang kinakatawan ng halaga, habang ang mga row ay naglalaman ng aktwal na mga halaga. Ang mga column ay madalas na may partikular na set ng mga panuntunan o limitasyon sa mga halaga, upang matiyak na ang mga halaga ay tumpak na kumakatawan sa column. Halimbawa, isipin ang isang spreadsheet ng mga customer kung saan ang bawat row ay dapat may numero ng telepono at ang mga numero ng telepono ay hindi kailanman naglalaman ng mga alpabetikong karakter. Maaaring may mga panuntunan na inilapat sa column ng numero ng telepono upang matiyak na hindi ito kailanman walang laman at naglalaman lamang ng mga numero.

Ang benepisyo ng structured data ay maaari itong ayusin sa paraang maaaring maiugnay sa iba pang structured data. Gayunpaman, dahil ang datos ay dinisenyo upang maayos sa isang partikular na paraan, ang paggawa ng mga pagbabago sa pangkalahatang istruktura nito ay maaaring mangailangan ng malaking pagsisikap. Halimbawa, ang pagdaragdag ng email column sa spreadsheet ng customer na hindi maaaring walang laman ay nangangahulugan na kailangan mong alamin kung paano mo idaragdag ang mga halagang ito sa mga umiiral na row ng mga customer sa dataset.

Mga halimbawa ng structured data: spreadsheets, relational databases, mga numero ng telepono, bank statements

### Unstructured Data
Ang unstructured data ay karaniwang hindi maaaring ikategorya sa mga row o column at walang format o set ng mga panuntunan na susundin. Dahil ang unstructured data ay may mas kaunting mga limitasyon sa istruktura nito, mas madali itong magdagdag ng bagong impormasyon kumpara sa isang structured dataset. Halimbawa, kung ang isang sensor na kumukuha ng datos sa barometric pressure tuwing 2 minuto ay nakatanggap ng update na ngayon ay pinapayagan itong sukatin at i-record ang temperatura, hindi nito kailangang baguhin ang umiiral na datos kung ito ay unstructured. Gayunpaman, maaaring mas matagal ang pagsusuri o pagsisiyasat sa ganitong uri ng datos. Halimbawa, ang isang siyentipiko na gustong hanapin ang average na temperatura ng nakaraang buwan mula sa datos ng sensor, ngunit natuklasan na ang sensor ay nag-record ng "e" sa ilan sa mga datos nito upang ipahiwatig na ito ay nasira sa halip na isang tipikal na numero, na nangangahulugang hindi kumpleto ang datos.

Mga halimbawa ng unstructured data: text files, text messages, video files

### Semi-structured
Ang semi-structured data ay may mga katangian na ginagawa itong kombinasyon ng structured at unstructured data. Karaniwan itong hindi sumusunod sa format ng mga row at column ngunit naayos sa paraang itinuturing na structured at maaaring sumunod sa isang nakatakdang format o set ng mga panuntunan. Ang istruktura ay mag-iiba sa pagitan ng mga pinagmulan, tulad ng isang malinaw na hierarchy hanggang sa isang mas flexible na istruktura na nagpapadali sa pagsasama ng bagong impormasyon. Ang metadata ay mga tagapagpahiwatig na tumutulong sa pagpapasya kung paano naayos at iniimbak ang datos at magkakaroon ng iba't ibang pangalan, batay sa uri ng datos. Ilang karaniwang pangalan para sa metadata ay tags, elements, entities, at attributes. Halimbawa, ang isang tipikal na email message ay magkakaroon ng subject, body, at isang set ng mga recipient at maaaring ayusin batay sa kung sino o kailan ito ipinadala.

Mga halimbawa ng semi-structured data: HTML, CSV files, JavaScript Object Notation (JSON)

## Mga Pinagmulan ng Datos

Ang pinagmulan ng datos ay ang pangunahing lokasyon kung saan nabuo ang datos, o kung saan ito "nakatira" at mag-iiba batay sa kung paano at kailan ito nakolekta. Ang datos na nabuo ng mga gumagamit nito ay kilala bilang primary data habang ang secondary data ay nagmumula sa isang pinagmulan na nangolekta ng datos para sa pangkalahatang paggamit. Halimbawa, ang isang grupo ng mga siyentipiko na nangongolekta ng obserbasyon sa isang rainforest ay ituturing na primary at kung magpasya silang ibahagi ito sa ibang mga siyentipiko, ito ay ituturing na secondary para sa mga gumagamit nito.

Ang mga database ay isang karaniwang pinagmulan at umaasa sa isang database management system upang i-host at panatilihin ang datos kung saan gumagamit ang mga user ng mga command na tinatawag na queries upang galugarin ang datos. Ang mga file bilang pinagmulan ng datos ay maaaring audio, image, at video files pati na rin ang mga spreadsheet tulad ng Excel. Ang mga internet sources ay isang karaniwang lokasyon para sa pagho-host ng datos, kung saan ang mga database pati na rin ang mga file ay matatagpuan. Ang application programming interfaces, na kilala rin bilang APIs, ay nagpapahintulot sa mga programmer na lumikha ng mga paraan upang magbahagi ng datos sa mga panlabas na user sa pamamagitan ng internet, habang ang proseso ng web scraping ay kumukuha ng datos mula sa isang web page. Ang [mga aralin sa Working with Data](../../../../../../../../../2-Working-With-Data) ay nakatuon sa kung paano gamitin ang iba't ibang pinagmulan ng datos.

## Konklusyon

Sa araling ito natutunan natin:

- Ano ang datos
- Paano inilalarawan ang datos
- Paano inuuri at ikinategorya ang datos
- Saan matatagpuan ang datos

## 🚀 Hamon

Ang Kaggle ay isang mahusay na pinagmulan ng mga open datasets. Gamitin ang [dataset search tool](https://www.kaggle.com/datasets) upang makahanap ng ilang kawili-wiling datasets at uriin ang 3-5 datasets gamit ang mga pamantayang ito:

- Ang datos ba ay quantitative o qualitative?
- Ang datos ba ay structured, unstructured, o semi-structured?

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/5)

## Review at Pag-aaral sa Sarili

- Ang Microsoft Learn unit na ito, na pinamagatang [Classify your Data](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/2-classify-data) ay may detalyadong breakdown ng structured, semi-structured, at unstructured data.

## Takdang Aralin

[Pag-uuri ng Datasets](assignment.md)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.