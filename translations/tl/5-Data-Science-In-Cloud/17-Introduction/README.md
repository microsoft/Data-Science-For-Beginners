<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "408c55cab2880daa4e78616308bd5db7",
  "translation_date": "2025-08-28T02:25:11+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "tl"
}
-->
# Panimula sa Data Science sa Cloud

|![ Sketchnote ni [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Data Science Sa Cloud: Panimula - _Sketchnote ni [@nitya](https://twitter.com/nitya)_ |

Sa araling ito, matututuhan mo ang mga pangunahing prinsipyo ng Cloud, malalaman kung bakit maaaring maging kapaki-pakinabang ang paggamit ng mga serbisyo ng Cloud para sa iyong mga proyekto sa data science, at titingnan natin ang ilang halimbawa ng mga proyektong data science na isinasagawa sa Cloud.

## [Pre-Lecture Quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/32)

## Ano ang Cloud?

Ang Cloud, o Cloud Computing, ay ang pagbibigay ng malawak na hanay ng mga serbisyong pang-compute na binabayaran ayon sa paggamit at naka-host sa isang imprastraktura sa internet. Kasama sa mga serbisyong ito ang mga solusyon tulad ng storage, databases, networking, software, analytics, at mga intelligent services.

Karaniwang inihihiwalay ang Public, Private, at Hybrid clouds sa ganitong paraan:

* Public cloud: Ang public cloud ay pagmamay-ari at pinapatakbo ng isang third-party cloud service provider na naghahatid ng mga computing resources nito sa publiko sa pamamagitan ng Internet.
* Private cloud: Tumutukoy ito sa mga cloud computing resources na eksklusibong ginagamit ng isang negosyo o organisasyon, na may mga serbisyo at imprastraktura na pinapanatili sa isang pribadong network.
* Hybrid cloud: Ang hybrid cloud ay isang sistema na pinagsasama ang public at private clouds. Pinipili ng mga user ang isang on-premises datacenter, habang pinapayagan ang data at mga aplikasyon na tumakbo sa isa o higit pang public clouds.

Karamihan sa mga serbisyo ng cloud computing ay nahahati sa tatlong kategorya: Infrastructure as a Service (IaaS), Platform as a Service (PaaS), at Software as a Service (SaaS).

* Infrastructure as a Service (IaaS): Ang mga user ay umuupa ng IT infrastructure tulad ng servers at virtual machines (VMs), storage, networks, at operating systems.
* Platform as a Service (PaaS): Ang mga user ay umuupa ng isang kapaligiran para sa pagbuo, pagsubok, paghahatid, at pamamahala ng mga software application. Hindi na kailangang mag-alala ang mga user tungkol sa pag-set up o pamamahala ng underlying infrastructure ng servers, storage, network, at databases na kailangan para sa pag-develop.
* Software as a Service (SaaS): Ang mga user ay nakakakuha ng access sa mga software application sa Internet, on-demand, at karaniwang sa pamamagitan ng subscription. Hindi na kailangang mag-alala ang mga user tungkol sa pagho-host at pamamahala ng software application, ang underlying infrastructure, o ang maintenance tulad ng software upgrades at security patching.

Ilan sa mga pinakamalalaking Cloud providers ay ang Amazon Web Services, Google Cloud Platform, at Microsoft Azure.

## Bakit Pumili ng Cloud para sa Data Science?

Pinipili ng mga developer at IT professionals na magtrabaho gamit ang Cloud dahil sa maraming dahilan, kabilang ang mga sumusunod:

* Inobasyon: Maaari mong palakasin ang iyong mga aplikasyon sa pamamagitan ng pagsasama ng mga makabagong serbisyo na nilikha ng mga Cloud provider nang direkta sa iyong mga app.
* Kakayahang umangkop: Magbabayad ka lamang para sa mga serbisyong kailangan mo at maaaring pumili mula sa malawak na hanay ng mga serbisyo. Karaniwang nagbabayad ka habang ginagamit at inaangkop ang iyong mga serbisyo ayon sa iyong mga pangangailangan.
* Badyet: Hindi mo kailangang gumawa ng paunang pamumuhunan para bumili ng hardware at software, mag-set up at magpatakbo ng on-site datacenters, at magbabayad ka lamang para sa iyong ginagamit.
* Scalability: Ang iyong mga resources ay maaaring mag-scale ayon sa mga pangangailangan ng iyong proyekto, na nangangahulugang ang iyong mga app ay maaaring gumamit ng mas marami o mas kaunting computing power, storage, at bandwidth, na umaangkop sa mga panlabas na salik anumang oras.
* Produktibidad: Maaari kang mag-focus sa iyong negosyo sa halip na maglaan ng oras sa mga gawain na maaaring pamahalaan ng iba, tulad ng pamamahala ng datacenters.
* Pagiging maaasahan: Nag-aalok ang Cloud Computing ng maraming paraan upang tuloy-tuloy na i-back up ang iyong data at maaari kang mag-set up ng mga disaster recovery plan upang mapanatili ang iyong negosyo at mga serbisyo kahit sa panahon ng krisis.
* Seguridad: Maaari kang makinabang mula sa mga polisiya, teknolohiya, at kontrol na nagpapalakas sa seguridad ng iyong proyekto.

Ito ang ilan sa mga karaniwang dahilan kung bakit pinipili ng mga tao na gumamit ng mga serbisyo ng Cloud. Ngayon na mas nauunawaan na natin kung ano ang Cloud at ang mga pangunahing benepisyo nito, tingnan natin nang mas partikular ang mga trabaho ng mga Data Scientist at developer na nagtatrabaho gamit ang data, at kung paano makakatulong ang Cloud sa kanila sa ilang mga hamon na maaaring harapin nila:

* Pag-iimbak ng malalaking dami ng data: Sa halip na bumili, pamahalaan, at protektahan ang malalaking servers, maaari mong iimbak ang iyong data nang direkta sa cloud gamit ang mga solusyon tulad ng Azure Cosmos DB, Azure SQL Database, at Azure Data Lake Storage.
* Pagsasagawa ng Data Integration: Ang data integration ay isang mahalagang bahagi ng Data Science na nagbibigay-daan sa iyong mag-transition mula sa data collection patungo sa paggawa ng aksyon. Sa mga serbisyo ng data integration na inaalok sa cloud, maaari kang mangolekta, mag-transform, at mag-integrate ng data mula sa iba't ibang pinagmulan patungo sa isang data warehouse gamit ang Data Factory.
* Pagpoproseso ng data: Ang pagpoproseso ng malalaking dami ng data ay nangangailangan ng maraming computing power, at hindi lahat ay may access sa mga makinang sapat ang lakas para dito, kaya't maraming tao ang pinipiling direktang gamitin ang napakalaking computing power ng cloud upang patakbuhin at i-deploy ang kanilang mga solusyon.
* Paggamit ng mga serbisyo ng data analytics: Ang mga serbisyo ng cloud tulad ng Azure Synapse Analytics, Azure Stream Analytics, at Azure Databricks ay tumutulong sa iyo na gawing actionable insights ang iyong data.
* Paggamit ng Machine Learning at mga serbisyo ng data intelligence: Sa halip na magsimula mula sa simula, maaari mong gamitin ang mga machine learning algorithm na inaalok ng cloud provider, gamit ang mga serbisyo tulad ng AzureML. Maaari mo ring gamitin ang mga cognitive services tulad ng speech-to-text, text-to-speech, computer vision, at marami pa.

## Mga Halimbawa ng Data Science sa Cloud

Gawin nating mas kongkreto ito sa pamamagitan ng pagtingin sa ilang mga senaryo.

### Real-time na pagsusuri ng damdamin sa social media
Magsimula tayo sa isang senaryong karaniwang pinag-aaralan ng mga nagsisimula sa machine learning: pagsusuri ng damdamin sa social media nang real-time.

Halimbawa, nagpapatakbo ka ng isang news media website at nais mong gamitin ang live data upang maunawaan kung anong nilalaman ang maaaring interesado ang iyong mga mambabasa. Upang malaman ito, maaari kang bumuo ng isang program na nagsasagawa ng real-time sentiment analysis ng data mula sa mga publikasyon sa Twitter, sa mga paksang may kaugnayan sa iyong mga mambabasa.

Ang mga pangunahing tagapagpahiwatig na titingnan mo ay ang dami ng mga tweet sa mga partikular na paksa (hashtags) at damdamin, na itinatag gamit ang mga analytics tools na nagsasagawa ng sentiment analysis sa mga tinukoy na paksa.

Ang mga hakbang na kinakailangan upang likhain ang proyektong ito ay ang mga sumusunod:

* Gumawa ng event hub para sa streaming input, na mangongolekta ng data mula sa Twitter.
* I-configure at simulan ang isang Twitter client application, na tatawag sa Twitter Streaming APIs.
* Gumawa ng Stream Analytics job.
* Tukuyin ang job input at query.
* Gumawa ng output sink at tukuyin ang job output.
* Simulan ang job.

Upang makita ang buong proseso, tingnan ang [dokumentasyon](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099).

### Pagsusuri ng mga siyentipikong papel
Tingnan natin ang isa pang halimbawa ng isang proyekto na nilikha ni [Dmitry Soshnikov](http://soshnikov.com), isa sa mga may-akda ng kurikulum na ito.

Lumikha si Dmitry ng isang tool na nagsusuri ng mga papel tungkol sa COVID. Sa pamamagitan ng pagsusuri sa proyektong ito, makikita mo kung paano ka makakalikha ng isang tool na kumukuha ng kaalaman mula sa mga siyentipikong papel, nakakakuha ng mga insight, at tumutulong sa mga mananaliksik na mag-navigate sa malalaking koleksyon ng mga papel nang mas mahusay.

Narito ang iba't ibang hakbang na ginamit para dito:
* Pagkuha at pag-preprocess ng impormasyon gamit ang [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Paggamit ng [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) upang gawing parallel ang pagpoproseso.
* Pag-iimbak at pag-query ng impormasyon gamit ang [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Gumawa ng interactive dashboard para sa data exploration at visualization gamit ang Power BI.

Upang makita ang buong proseso, bisitahin ang [blog ni Dmitry](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/).

Makikita mo, maraming paraan upang magamit ang mga serbisyo ng Cloud para sa Data Science.

## Tala sa Ibaba

Mga Pinagmulan:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Post-Lecture Quiz

[Post-lecture quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/33)

## Takdang Aralin

[Market Research](assignment.md)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.