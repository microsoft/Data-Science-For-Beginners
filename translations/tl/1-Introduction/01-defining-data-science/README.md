<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "43212cc1ac137b7bb1dcfb37ca06b0f4",
  "translation_date": "2025-10-25T19:02:04+00:00",
  "source_file": "1-Introduction/01-defining-data-science/README.md",
  "language_code": "tl"
}
-->
# Pagpapakilala sa Data Science

| ![Sketchnote ni [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/01-Definitions.png) |
| :----------------------------------------------------------------------------------------------------: |
|              Pagpapakilala sa Data Science - _Sketchnote ni [@nitya](https://twitter.com/nitya)_       |

---

[![Video ng Pagpapakilala sa Data Science](../../../../translated_images/tl/video-def-ds.6623ee2392ef1abf6d7faf3fad10a4163642811749da75f44e35a5bb121de15c.png)](https://youtu.be/beZ7Mb_oz9I)

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/0)

## Ano ang Data?
Sa araw-araw nating pamumuhay, palagi tayong napapalibutan ng data. Ang tekstong binabasa mo ngayon ay data. Ang listahan ng mga numero ng telepono ng iyong mga kaibigan sa iyong smartphone ay data, gayundin ang kasalukuyang oras na nakikita sa iyong relo. Bilang mga tao, natural na ginagamit natin ang data sa pamamagitan ng pagbibilang ng pera o pagsusulat ng mga liham sa ating mga kaibigan.

Gayunpaman, naging mas mahalaga ang data sa paglikha ng mga computer. Ang pangunahing layunin ng mga computer ay magsagawa ng mga kalkulasyon, ngunit kailangan nila ng data upang magamit. Kaya, kailangan nating maunawaan kung paano iniimbak at pinoproseso ng mga computer ang data.

Sa pag-usbong ng Internet, mas lumaki ang papel ng mga computer bilang mga kagamitan sa paghawak ng data. Kung iisipin mo, mas ginagamit na natin ang mga computer para sa pagproseso ng data at komunikasyon, kaysa sa aktwal na mga kalkulasyon. Kapag nagsusulat tayo ng e-mail sa isang kaibigan o naghahanap ng impormasyon sa Internet - sa esensya, lumilikha, nag-iimbak, nagpapadala, at nagmamanipula tayo ng data.
> Naalala mo ba ang huling beses na ginamit mo ang computer para aktwal na mag-compute ng isang bagay?

## Ano ang Data Science?

Ayon sa [Wikipedia](https://en.wikipedia.org/wiki/Data_science), ang **Data Science** ay tinutukoy bilang *isang larangan ng agham na gumagamit ng mga siyentipikong pamamaraan upang makuha ang kaalaman at mga pananaw mula sa structured at unstructured na data, at gamitin ang kaalaman at actionable insights mula sa data sa iba't ibang larangan ng aplikasyon*.

Ang depinisyong ito ay nagtatampok ng mga sumusunod na mahahalagang aspeto ng data science:

* Ang pangunahing layunin ng data science ay **makakuha ng kaalaman** mula sa data, sa madaling salita - **maunawaan** ang data, hanapin ang mga nakatagong relasyon, at bumuo ng isang **modelo**.
* Gumagamit ang data science ng **mga siyentipikong pamamaraan**, tulad ng probability at statistics. Sa katunayan, noong unang ipinakilala ang terminong *data science*, may mga nagsabi na ang data science ay isang bagong pangalan lamang para sa statistics. Sa ngayon, malinaw na mas malawak ang saklaw ng larangan.
* Ang nakuha na kaalaman ay dapat gamitin upang makabuo ng **actionable insights**, ibig sabihin, mga praktikal na pananaw na maaaring magamit sa mga tunay na sitwasyon sa negosyo.
* Dapat tayong marunong mag-operate sa parehong **structured** at **unstructured** na data. Babalikan natin ang talakayan tungkol sa iba't ibang uri ng data sa mga susunod na bahagi ng kurso.
* Ang **application domain** ay isang mahalagang konsepto, at madalas na kailangan ng mga data scientist ang kahit kaunting kaalaman sa larangan ng problema, halimbawa: pananalapi, medisina, marketing, atbp.

> Isa pang mahalagang aspeto ng Data Science ay ang pag-aaral kung paano makukuha, maiimbak, at magagamit ang data gamit ang mga computer. Habang ang statistics ay nagbibigay sa atin ng mga pundasyong matematika, ang data science ay nag-aaplay ng mga konseptong matematika upang aktwal na makakuha ng mga pananaw mula sa data.

Isa sa mga paraan (na iniuugnay kay [Jim Gray](https://en.wikipedia.org/wiki/Jim_Gray_(computer_scientist))) upang tingnan ang data science ay ang ituring ito bilang isang hiwalay na paradigma ng agham:
* **Empirical**, kung saan umaasa tayo sa mga obserbasyon at resulta ng mga eksperimento
* **Theoretical**, kung saan lumalabas ang mga bagong konsepto mula sa umiiral na kaalaman sa agham
* **Computational**, kung saan natutuklasan natin ang mga bagong prinsipyo batay sa ilang computational experiments
* **Data-Driven**, batay sa pagtuklas ng mga relasyon at pattern sa data  

## Iba Pang Kaugnay na Larangan

Dahil ang data ay laganap, ang data science mismo ay isang malawak na larangan na sumasaklaw sa maraming iba pang disiplina.

<dl>
<dt>Databases</dt>
<dd>
Isang mahalagang konsiderasyon ay kung <b>paano iimbak</b> ang data, ibig sabihin, kung paano ito istrukturahin sa paraang mas mabilis itong maproseso. May iba't ibang uri ng databases na nag-iimbak ng structured at unstructured na data, na <a href="../../2-Working-With-Data/README.md">tatalakayin natin sa ating kurso</a>.
</dd>
<dt>Big Data</dt>
<dd>
Madalas nating kailangang mag-imbak at magproseso ng napakalaking dami ng data na may simpleng istruktura. May mga espesyal na pamamaraan at kasangkapan upang maiimbak ang data na iyon sa isang distributed na paraan sa isang computer cluster, at maproseso ito nang epektibo.
</dd>
<dt>Machine Learning</dt>
<dd>
Isang paraan upang maunawaan ang data ay ang <b>paggawa ng modelo</b> na makakapagpredikta ng nais na resulta. Ang pagbuo ng mga modelo mula sa data ay tinatawag na <b>machine learning</b>. Maaaring tingnan mo ang aming <a href="https://aka.ms/ml-beginners">Machine Learning for Beginners</a> Curriculum upang matuto pa tungkol dito.
</dd>
<dt>Artificial Intelligence</dt>
<dd>
Ang isang larangan ng machine learning na kilala bilang artificial intelligence (AI) ay umaasa rin sa data, at ito ay kinabibilangan ng paggawa ng mga modelong may mataas na antas ng komplikasyon na ginagaya ang proseso ng pag-iisip ng tao. Ang mga pamamaraan ng AI ay madalas na nagbibigay-daan sa atin upang gawing structured insights ang unstructured data (halimbawa, natural language).
</dd>
<dt>Visualization</dt>
<dd>
Ang napakaraming dami ng data ay mahirap maunawaan ng isang tao, ngunit kapag nakagawa tayo ng mga kapaki-pakinabang na visualizations gamit ang data na iyon, mas mauunawaan natin ito at makakakuha ng mga konklusyon. Kaya't mahalagang malaman ang maraming paraan ng pag-visualize ng impormasyon - isang bagay na tatalakayin natin sa <a href="../../3-Data-Visualization/README.md">Seksyon 3</a> ng ating kurso. Ang mga kaugnay na larangan ay kinabibilangan ng <b>Infographics</b>, at <b>Human-Computer Interaction</b> sa pangkalahatan.
</dd>
</dl>

## Mga Uri ng Data

Tulad ng nabanggit na, ang data ay nasa lahat ng dako. Kailangan lang natin itong makuha sa tamang paraan! Kapaki-pakinabang na pag-iba-ibahin ang **structured** at **unstructured** na data. Ang una ay karaniwang kinakatawan sa isang maayos na istruktura, madalas bilang isang table o bilang maraming table, habang ang huli ay isang koleksyon lamang ng mga file. Minsan maaari rin tayong mag-usap tungkol sa **semi-structured** na data, na may ilang uri ng istruktura na maaaring mag-iba nang malaki.

| Structured                                                                   | Semi-structured                                                                                | Unstructured                            |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------- |
| Listahan ng mga tao kasama ang kanilang mga numero ng telepono               | Mga pahina ng Wikipedia na may mga link                                                        | Teksto ng Encyclopedia Britannica       |
| Temperatura sa lahat ng silid ng isang gusali bawat minuto sa nakalipas na 20 taon | Koleksyon ng mga scientific papers sa format na JSON na may mga author, petsa ng publikasyon, at abstract | File share na may mga corporate documents |
| Data para sa edad at kasarian ng lahat ng taong pumapasok sa gusali          | Mga pahina ng Internet                                                                         | Raw video feed mula sa surveillance camera |

## Saan Makakakuha ng Data

Maraming posibleng mapagkukunan ng data, at imposibleng mailista ang lahat ng mga ito! Gayunpaman, banggitin natin ang ilan sa mga karaniwang lugar kung saan makakakuha ng data:

* **Structured**
  - **Internet of Things** (IoT), kabilang ang data mula sa iba't ibang sensors, tulad ng temperatura o pressure sensors, ay nagbibigay ng maraming kapaki-pakinabang na data. Halimbawa, kung ang isang gusali ng opisina ay may mga IoT sensors, maaari nating awtomatikong kontrolin ang heating at lighting upang mabawasan ang gastos.
  - **Mga survey** na hinihiling natin sa mga user na sagutan pagkatapos ng pagbili, o pagkatapos bumisita sa isang website.
  - **Pagsusuri ng ugali** ay maaaring makatulong sa atin na maunawaan kung gaano kalalim ang pagbisita ng isang user sa site, at ano ang karaniwang dahilan ng pag-alis sa site.
* **Unstructured**
  - **Mga teksto** ay maaaring maging mayamang mapagkukunan ng mga pananaw, tulad ng kabuuang **sentiment score**, o pagkuha ng mga keyword at semantikong kahulugan.
  - **Mga imahe** o **video**. Ang video mula sa isang surveillance camera ay maaaring gamitin upang matantya ang trapiko sa kalsada, at magbigay ng impormasyon sa mga tao tungkol sa posibleng traffic jams.
  - Mga **log ng web server** ay maaaring gamitin upang maunawaan kung aling mga pahina ng ating site ang madalas bisitahin, at kung gaano katagal.
* Semi-structured
  - Ang mga **Social Network** graphs ay maaaring maging mahusay na mapagkukunan ng data tungkol sa personalidad ng mga user at potensyal na pagiging epektibo sa pagpapalaganap ng impormasyon.
  - Kapag mayroon tayong maraming litrato mula sa isang party, maaari nating subukang kunin ang data ng **Group Dynamics** sa pamamagitan ng paggawa ng graph ng mga taong nagpipicture kasama ang isa't isa.

Sa pamamagitan ng kaalaman sa iba't ibang posibleng mapagkukunan ng data, maaari kang mag-isip tungkol sa iba't ibang mga senaryo kung saan maaaring magamit ang mga teknik ng data science upang mas maunawaan ang sitwasyon, at mapabuti ang mga proseso ng negosyo.

## Ano ang Magagawa Mo sa Data

Sa Data Science, nakatuon tayo sa mga sumusunod na hakbang ng paglalakbay ng data:

<dl>
<dt>1) Pagkuha ng Data</dt>
<dd>
Ang unang hakbang ay ang pagkolekta ng data. Habang sa maraming kaso ito ay maaaring isang simpleng proseso, tulad ng pagpasok ng data sa isang database mula sa isang web application, minsan kailangan nating gumamit ng mga espesyal na teknik. Halimbawa, ang data mula sa mga IoT sensors ay maaaring napakarami, at magandang kasanayan ang paggamit ng buffering endpoints tulad ng IoT Hub upang kolektahin ang lahat ng data bago ito iproseso.
</dd>
<dt>2) Pag-iimbak ng Data</dt>
<dd>
Ang pag-iimbak ng data ay maaaring maging hamon, lalo na kung pinag-uusapan natin ang big data. Kapag nagdedesisyon kung paano iimbak ang data, makatuwiran na isipin ang paraan kung paano mo gustong i-query ang data sa hinaharap. May ilang paraan kung paano maiimbak ang data:
<ul>
<li>Ang relational database ay nag-iimbak ng koleksyon ng mga table, at gumagamit ng espesyal na wika na tinatawag na SQL upang i-query ang mga ito. Karaniwan, ang mga table ay nakaayos sa iba't ibang grupo na tinatawag na schemas. Sa maraming kaso, kailangan nating i-convert ang data mula sa orihinal na anyo upang magkasya sa schema.</li>
<li><a href="https://en.wikipedia.org/wiki/NoSQL">Ang NoSQL</a> database, tulad ng <a href="https://azure.microsoft.com/services/cosmos-db/?WT.mc_id=academic-77958-bethanycheum">CosmosDB</a>, ay hindi nagtatakda ng mga schema sa data, at nagbibigay-daan sa pag-iimbak ng mas kumplikadong data, halimbawa, hierarchical JSON documents o graphs. Gayunpaman, ang mga NoSQL database ay walang mas maraming kakayahan sa pag-query tulad ng SQL, at hindi makakapagpatupad ng referential integrity, ibig sabihin, mga patakaran kung paano nakaayos ang data sa mga table at ang pamamahala sa mga relasyon sa pagitan ng mga table.</li>
<li><a href="https://en.wikipedia.org/wiki/Data_lake">Ang Data Lake</a> storage ay ginagamit para sa malalaking koleksyon ng data sa raw, unstructured na anyo. Ang mga data lake ay madalas na ginagamit sa big data, kung saan ang lahat ng data ay hindi magkasya sa isang makina, at kailangang iimbak at iproseso ng isang cluster ng mga server. Ang <a href="https://en.wikipedia.org/wiki/Apache_Parquet">Parquet</a> ay ang data format na madalas gamitin kasabay ng big data.</li> 
</ul>
</dd>
<dt>3) Pagproseso ng Data</dt>
<dd>
Ito ang pinaka-kapanapanabik na bahagi ng paglalakbay ng data, na kinabibilangan ng pag-convert ng data mula sa orihinal na anyo nito patungo sa anyo na maaaring magamit para sa visualization/pagsasanay ng modelo. Kapag nakikitungo sa unstructured na data tulad ng teksto o mga imahe, maaaring kailanganin nating gumamit ng ilang teknik ng AI upang makuha ang <b>mga tampok</b> mula sa data, kaya't na-convert ito sa structured na anyo.
</dd>
<dt>4) Visualization / Human Insights</dt>
<dd>
Madalas, upang maunawaan ang data, kailangan natin itong i-visualize. Sa pagkakaroon ng maraming iba't ibang teknik sa visualization sa ating toolbox, maaari nating mahanap ang tamang view upang makakuha ng pananaw. Madalas, ang isang data scientist ay kailangang "maglaro sa data", i-visualize ito nang maraming beses at hanapin ang ilang mga relasyon. Gayundin, maaari tayong gumamit ng mga teknik sa statistics upang subukan ang isang hypothesis o patunayan ang ugnayan sa pagitan ng iba't ibang piraso ng data.   
</dd>
<dt>5) Pagsasanay ng predictive model</dt>
<dd>
Dahil ang panghuling layunin ng data science ay ang makagawa ng mga desisyon batay sa data, maaaring gusto nating gamitin ang mga teknik ng <a href="http://github.com/microsoft/ml-for-beginners">Machine Learning</a> upang bumuo ng isang predictive model. Maaari natin itong gamitin upang makagawa ng mga prediksyon gamit ang mga bagong set ng data na may katulad na mga istruktura.
</dd>
</dl>

Siyempre, depende sa aktwal na data, maaaring may mga hakbang na nawawala (halimbawa, kapag mayroon na tayong data sa database, o kapag hindi natin kailangan ang pagsasanay ng modelo), o maaaring ulitin ang ilang hakbang nang maraming beses (tulad ng pagproseso ng data).

## Digitalization at Digital Transformation

Sa nakaraang dekada, maraming negosyo ang nagsimulang maunawaan ang kahalagahan ng data sa paggawa ng mga desisyon sa negosyo. Upang magamit ang mga prinsipyo ng data science sa pagpapatakbo ng negosyo, kailangang mangolekta muna ng data, ibig sabihin, isalin ang mga proseso ng negosyo sa digital na anyo. Ito ay kilala bilang **digitalization**. Ang paggamit ng mga teknik ng data science sa data na ito upang gabayan ang mga desisyon ay maaaring magdulot ng makabuluhang pagtaas sa produktibidad (o kahit na pagbabago ng negosyo), na tinatawag na **digital transformation**.

Isaalang-alang natin ang isang halimbawa. Ipagpalagay na mayroon tayong kurso sa data science (tulad ng kursong ito) na inihahatid natin online sa mga estudyante, at gusto nating gamitin ang data science upang mapabuti ito. Paano natin ito magagawa?

Maaari tayong magsimula sa pagtatanong ng "Ano ang maaaring i-digitize?" Ang pinakasimpleng paraan ay sukatin ang oras na ginugugol ng bawat estudyante upang makumpleto ang bawat module, at sukatin ang nakuha nilang kaalaman sa pamamagitan ng pagbibigay ng multiple-choice test sa dulo ng bawat module. Sa pamamagitan ng pag-average ng oras ng pagkumpleto sa lahat ng estudyante, malalaman natin kung aling mga module ang nagdudulot ng pinakamaraming hamon sa mga estudyante, at magtrabaho upang gawing mas madali ang mga ito.
> Maaaring sabihin mo na ang pamamaraang ito ay hindi perpekto, dahil ang mga module ay maaaring may iba't ibang haba. Mas makatarungan siguro kung hahatiin ang oras batay sa haba ng module (sa bilang ng mga karakter), at ikumpara ang mga halagang iyon.

Kapag sinimulan nating suriin ang mga resulta ng mga multiple-choice na pagsusulit, maaari nating subukang tukuyin kung aling mga konsepto ang mahirap maintindihan ng mga mag-aaral, at gamitin ang impormasyong iyon upang mapabuti ang nilalaman. Upang magawa ito, kailangan nating magdisenyo ng mga pagsusulit sa paraang ang bawat tanong ay tumutukoy sa isang tiyak na konsepto o bahagi ng kaalaman.

Kung nais nating gawing mas komplikado, maaari nating i-plot ang oras na ginugol sa bawat module laban sa kategorya ng edad ng mga mag-aaral. Maaaring matuklasan natin na para sa ilang kategorya ng edad, masyadong matagal ang ginugol upang matapos ang module, o kaya naman ay tumitigil ang mga mag-aaral bago ito matapos. Makakatulong ito upang magbigay ng rekomendasyon sa edad para sa module, at mabawasan ang pagkadismaya ng mga tao mula sa maling inaasahan.

## 🚀 Hamon

Sa hamong ito, susubukan nating tukuyin ang mga konseptong may kaugnayan sa larangan ng Data Science sa pamamagitan ng pagsusuri sa mga teksto. Kukuha tayo ng isang artikulo mula sa Wikipedia tungkol sa Data Science, ida-download at ipoproseso ang teksto, at gagawa ng isang word cloud na ganito:

![Word Cloud para sa Data Science](../../../../translated_images/tl/ds_wordcloud.664a7c07dca57de017c22bf0498cb40f898d48aa85b3c36a80620fea12fadd42.png)

Bisitahin ang [`notebook.ipynb`](../../../../1-Introduction/01-defining-data-science/notebook.ipynb ':ignore') upang basahin ang code. Maaari mo ring patakbuhin ang code, at makita kung paano nito isinasagawa ang lahat ng data transformations sa real time.

> Kung hindi mo alam kung paano patakbuhin ang code sa isang Jupyter Notebook, tingnan ang [artikulong ito](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/1)

## Mga Gawain

* **Gawain 1**: Baguhin ang code sa itaas upang tukuyin ang mga kaugnay na konsepto para sa mga larangan ng **Big Data** at **Machine Learning**
* **Gawain 2**: [Pag-isipan ang mga Senaryo ng Data Science](assignment.md)

## Mga Kredito

Ang araling ito ay isinulat nang may ♥️ ni [Dmitry Soshnikov](http://soshnikov.com)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na mapagkakatiwalaang pinagmulan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.