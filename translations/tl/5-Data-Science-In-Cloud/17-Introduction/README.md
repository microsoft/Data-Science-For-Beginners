<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f8e7cdefa096664ae86f795be571580",
  "translation_date": "2025-09-06T00:17:40+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "tl"
}
-->
# Panimula sa Data Science sa Cloud

|![ Sketchnote ni [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Data Science Sa Cloud: Panimula - _Sketchnote ni [@nitya](https://twitter.com/nitya)_ |

Sa araling ito, matututunan mo ang mga pangunahing prinsipyo ng Cloud, malalaman mo kung bakit maaaring maging kapaki-pakinabang ang paggamit ng mga serbisyo ng Cloud para sa iyong mga proyekto sa data science, at titingnan natin ang ilang halimbawa ng mga proyekto sa data science na isinasagawa sa Cloud.

## [Pre-Lecture Quiz](https://ff-quizzes.netlify.app/en/ds/quiz/32)

## Ano ang Cloud?

Ang Cloud, o Cloud Computing, ay ang pagbibigay ng malawak na hanay ng mga serbisyong pang-computing na binabayaran ayon sa paggamit, na naka-host sa isang imprastraktura sa internet. Kasama sa mga serbisyo ang mga solusyon tulad ng storage, databases, networking, software, analytics, at mga intelligent services.

Karaniwang pinag-iiba ang Public, Private, at Hybrid clouds sa ganitong paraan:

* Public cloud: Ang public cloud ay pagmamay-ari at pinapatakbo ng isang third-party cloud service provider na nagbibigay ng mga computing resources nito sa publiko sa pamamagitan ng Internet.
* Private cloud: Tumutukoy sa mga cloud computing resources na eksklusibong ginagamit ng isang negosyo o organisasyon, na may mga serbisyo at imprastraktura na pinapanatili sa isang pribadong network.
* Hybrid cloud: Ang hybrid cloud ay isang sistema na pinagsasama ang public at private clouds. Ang mga user ay pumipili ng isang on-premises datacenter, habang pinapayagan ang data at mga aplikasyon na tumakbo sa isa o higit pang public clouds.

Karamihan sa mga serbisyo ng cloud computing ay nahahati sa tatlong kategorya: Infrastructure as a Service (IaaS), Platform as a Service (PaaS), at Software as a Service (SaaS).

* Infrastructure as a Service (IaaS): Ang mga user ay nagrerenta ng IT infrastructure tulad ng servers at virtual machines (VMs), storage, networks, operating systems.
* Platform as a Service (PaaS): Ang mga user ay nagrerenta ng isang kapaligiran para sa pag-develop, pag-test, pag-deliver, at pamamahala ng mga software application. Hindi na kailangang mag-alala ang mga user tungkol sa pag-set up o pamamahala ng underlying infrastructure ng servers, storage, network, at databases na kailangan para sa development.
* Software as a Service (SaaS): Ang mga user ay nakakakuha ng access sa mga software application sa Internet, on demand, at karaniwang sa subscription basis. Hindi na kailangang mag-alala ang mga user tungkol sa pag-host at pamamahala ng software application, ang underlying infrastructure, o ang maintenance tulad ng software upgrades at security patching.

Ang ilan sa pinakamalalaking Cloud providers ay ang Amazon Web Services, Google Cloud Platform, at Microsoft Azure.

## Bakit Pumili ng Cloud para sa Data Science?

Pinipili ng mga developer at IT professionals na magtrabaho gamit ang Cloud para sa maraming dahilan, kabilang ang mga sumusunod:

* Inobasyon: Maaari mong palakasin ang iyong mga aplikasyon sa pamamagitan ng pagsasama ng mga makabagong serbisyo na nilikha ng mga Cloud provider nang direkta sa iyong mga app.
* Kakayahang umangkop: Magbabayad ka lamang para sa mga serbisyong kailangan mo at maaaring pumili mula sa malawak na hanay ng mga serbisyo. Karaniwang magbabayad ka ayon sa paggamit at iaangkop ang iyong mga serbisyo ayon sa iyong nagbabagong pangangailangan.
* Badyet: Hindi mo kailangang mag-invest nang malaki para bumili ng hardware at software, mag-set up, at magpatakbo ng on-site datacenters. Magbabayad ka lamang para sa kung ano ang ginagamit mo.
* Scalability: Ang iyong mga resources ay maaaring mag-adjust ayon sa pangangailangan ng iyong proyekto, ibig sabihin, ang iyong mga app ay maaaring gumamit ng mas marami o mas kaunting computing power, storage, at bandwidth, na umaangkop sa mga panlabas na salik anumang oras.
* Produktibidad: Maaari kang mag-focus sa iyong negosyo sa halip na maglaan ng oras sa mga gawain na maaaring pamahalaan ng iba, tulad ng pamamahala ng datacenters.
* Pagkakatiwalaan: Ang Cloud Computing ay nag-aalok ng maraming paraan upang tuloy-tuloy na mag-back up ng iyong data, at maaari kang mag-set up ng mga disaster recovery plan upang mapanatili ang iyong negosyo at mga serbisyo kahit sa panahon ng krisis.
* Seguridad: Maaari kang makinabang mula sa mga polisiya, teknolohiya, at kontrol na nagpapalakas sa seguridad ng iyong proyekto.

Ito ang ilan sa mga karaniwang dahilan kung bakit pinipili ng mga tao na gumamit ng mga serbisyo ng Cloud. Ngayon na mas nauunawaan natin kung ano ang Cloud at ang mga pangunahing benepisyo nito, tingnan natin nang mas partikular ang mga trabaho ng mga Data scientist at developer na nagtatrabaho gamit ang data, at kung paano makakatulong ang Cloud sa kanila sa ilang mga hamon na maaaring kanilang harapin:

* Pag-iimbak ng malaking dami ng data: Sa halip na bumili, pamahalaan, at protektahan ang malalaking servers, maaari mong iimbak ang iyong data nang direkta sa cloud, gamit ang mga solusyon tulad ng Azure Cosmos DB, Azure SQL Database, at Azure Data Lake Storage.
* Pagsasagawa ng Data Integration: Ang data integration ay isang mahalagang bahagi ng Data Science na nagbibigay-daan sa paglipat mula sa pagkolekta ng data patungo sa paggawa ng aksyon. Sa mga serbisyo ng data integration na inaalok sa cloud, maaari kang mangolekta, mag-transform, at mag-integrate ng data mula sa iba't ibang pinagmulan sa isang data warehouse, gamit ang Data Factory.
* Pagpoproseso ng data: Ang pagpoproseso ng napakalaking dami ng data ay nangangailangan ng maraming computing power, at hindi lahat ay may access sa mga makapangyarihang makina para dito, kaya't maraming tao ang pinipiling direktang gamitin ang malaking computing power ng cloud upang patakbuhin at i-deploy ang kanilang mga solusyon.
* Paggamit ng mga serbisyo ng data analytics: Ang mga serbisyo ng cloud tulad ng Azure Synapse Analytics, Azure Stream Analytics, at Azure Databricks ay tumutulong sa iyo na gawing actionable insights ang iyong data.
* Paggamit ng Machine Learning at mga serbisyo ng data intelligence: Sa halip na magsimula mula sa simula, maaari mong gamitin ang mga machine learning algorithm na inaalok ng cloud provider, gamit ang mga serbisyo tulad ng AzureML. Maaari mo ring gamitin ang mga cognitive services tulad ng speech-to-text, text-to-speech, computer vision, at iba pa.

## Mga Halimbawa ng Data Science sa Cloud

Gawin nating mas kongkreto ito sa pamamagitan ng pagtingin sa ilang mga senaryo.

### Real-time na pagsusuri ng damdamin sa social media
Magsimula tayo sa isang senaryo na karaniwang pinag-aaralan ng mga nagsisimula sa machine learning: pagsusuri ng damdamin sa social media nang real-time.

Halimbawa, nagpapatakbo ka ng isang news media website at nais mong gamitin ang live data upang maunawaan kung anong content ang maaaring interesado ang iyong mga mambabasa. Upang malaman ang higit pa tungkol dito, maaari kang bumuo ng isang programa na nagsasagawa ng real-time sentiment analysis ng data mula sa mga publikasyon sa Twitter, sa mga paksang may kaugnayan sa iyong mga mambabasa.

Ang mga pangunahing tagapagpahiwatig na iyong titingnan ay ang dami ng tweets sa mga partikular na paksa (hashtags) at damdamin, na itinatag gamit ang mga analytics tools na nagsasagawa ng sentiment analysis sa mga tinukoy na paksa.

Ang mga hakbang na kinakailangan upang likhain ang proyektong ito ay ang mga sumusunod:

* Gumawa ng event hub para sa streaming input, na mangongolekta ng data mula sa Twitter
* I-configure at simulan ang isang Twitter client application, na tatawag sa Twitter Streaming APIs
* Gumawa ng Stream Analytics job
* Tukuyin ang job input at query
* Gumawa ng output sink at tukuyin ang job output
* Simulan ang job

Upang makita ang buong proseso, tingnan ang [dokumentasyon](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099).

### Pagsusuri ng mga scientific papers
Tingnan natin ang isa pang halimbawa ng proyekto na ginawa ni [Dmitry Soshnikov](http://soshnikov.com), isa sa mga may-akda ng kurikulum na ito.

Gumawa si Dmitry ng tool na nagsusuri ng mga COVID papers. Sa pamamagitan ng pagsusuri sa proyektong ito, makikita mo kung paano ka makakalikha ng tool na nag-eextract ng kaalaman mula sa mga scientific papers, nakakakuha ng insights, at tumutulong sa mga mananaliksik na mag-navigate sa malalaking koleksyon ng mga papel nang mas epektibo.

Narito ang iba't ibang hakbang na ginamit para dito:

* Pagkuha at pag-preprocess ng impormasyon gamit ang [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)
* Paggamit ng [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) upang i-parallelize ang pagpoproseso
* Pag-iimbak at pag-query ng impormasyon gamit ang [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)
* Gumawa ng interactive dashboard para sa data exploration at visualization gamit ang Power BI

Upang makita ang buong proseso, bisitahin ang [blog ni Dmitry](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/).

Makikita mo, maraming paraan upang magamit ang mga serbisyo ng Cloud para sa Data Science.

## Footnote

Mga Pinagmulan:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Post-Lecture Quiz

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/33)

## Assignment

[Market Research](assignment.md)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na pinagmulan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.