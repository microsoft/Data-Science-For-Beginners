<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2baeafe1db4d58ee5b8ec85db9de728a",
  "translation_date": "2025-09-06T00:22:37+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "tl"
}
-->
# Ang Lifecycle ng Data Science: Pagsusuri

|![ Sketchnote ni [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Lifecycle ng Data Science: Pagsusuri - _Sketchnote ni [@nitya](https://twitter.com/nitya)_ |

## Pre-Lecture Quiz

## [Pre-Lecture Quiz](https://ff-quizzes.netlify.app/en/ds/quiz/28)

Ang pagsusuri sa lifecycle ng data ay nagkukumpirma kung ang data ay makakasagot sa mga tanong na iminungkahi o makakalutas ng isang partikular na problema. Ang hakbang na ito ay maaari ring tumuon sa pagkumpirma kung ang isang modelo ay tamang tumutugon sa mga tanong at problemang ito. Ang araling ito ay nakatuon sa Exploratory Data Analysis o EDA, na mga teknik para sa pagtukoy ng mga katangian at relasyon sa loob ng data at maaaring gamitin upang ihanda ang data para sa pagmomodelo.

Gagamit tayo ng isang halimbawa ng dataset mula sa [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1) upang ipakita kung paano ito maiaangkop gamit ang Python at ang Pandas library. Ang dataset na ito ay naglalaman ng bilang ng ilang karaniwang salita na matatagpuan sa mga email, kung saan ang mga pinagmulan ng mga email na ito ay hindi kilala. Gamitin ang [notebook](../../../../4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb) sa direktoryong ito upang sumabay.

## Exploratory Data Analysis

Ang yugto ng pagkuha sa lifecycle ay kung saan kinokolekta ang data pati na rin ang mga problema at tanong na kailangang sagutin, ngunit paano natin malalaman kung ang data ay makakatulong sa pagsuporta sa resulta?  
Tandaan na maaaring itanong ng isang data scientist ang mga sumusunod na tanong kapag nakuha ang data:  
- May sapat ba akong data upang malutas ang problemang ito?  
- Ang kalidad ba ng data ay katanggap-tanggap para sa problemang ito?  
- Kung makakahanap ako ng karagdagang impormasyon mula sa data na ito, dapat ba nating isaalang-alang ang pagbabago o muling pagtukoy sa mga layunin?  

Ang Exploratory Data Analysis ay ang proseso ng pag-unawa sa data at maaaring gamitin upang sagutin ang mga tanong na ito, pati na rin tukuyin ang mga hamon sa pagtatrabaho sa dataset. Magtuon tayo sa ilang mga teknik na ginagamit upang makamit ito.

## Data Profiling, Descriptive Statistics, at Pandas

Paano natin masusuri kung sapat ang data upang malutas ang problemang ito? Ang data profiling ay maaaring magbigay ng buod at mangalap ng ilang pangkalahatang impormasyon tungkol sa ating dataset sa pamamagitan ng mga teknik ng descriptive statistics. Ang data profiling ay tumutulong sa atin na maunawaan kung ano ang mayroon tayo, at ang descriptive statistics ay tumutulong sa atin na maunawaan kung gaano karami ang mayroon tayo.

Sa ilang mga nakaraang aralin, ginamit natin ang Pandas upang magbigay ng ilang descriptive statistics gamit ang [`describe()` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html). Nagbibigay ito ng bilang, pinakamataas at pinakamababang halaga, mean, standard deviation, at mga quantile sa numerical na data. Ang paggamit ng descriptive statistics tulad ng `describe()` function ay makakatulong sa iyong masuri kung gaano karami ang mayroon ka at kung kailangan mo pa ng higit.

## Sampling at Querying

Ang pag-explore sa lahat ng bagay sa isang malaking dataset ay maaaring maging napakatagal at karaniwang iniiwan sa isang computer upang gawin. Gayunpaman, ang sampling ay isang kapaki-pakinabang na kasangkapan sa pag-unawa sa data at nagbibigay-daan sa atin na magkaroon ng mas mahusay na pag-unawa sa kung ano ang nasa dataset at kung ano ang kinakatawan nito. Sa pamamagitan ng sample, maaari kang mag-aplay ng probability at statistics upang makabuo ng ilang pangkalahatang konklusyon tungkol sa iyong data. Bagama’t walang tiyak na panuntunan kung gaano karaming data ang dapat mong i-sample, mahalagang tandaan na mas maraming data ang iyong i-sample, mas tiyak ang iyong magiging generalization tungkol sa data.  

Ang Pandas ay may [`sample()` function sa library nito](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html) kung saan maaari kang magpasa ng argumento kung gaano karaming random na sample ang nais mong makuha at gamitin.

Ang pangkalahatang pag-query sa data ay makakatulong sa iyong sagutin ang ilang pangkalahatang tanong at teorya na maaaring mayroon ka. Sa kaibahan sa sampling, ang mga query ay nagbibigay-daan sa iyo na magkaroon ng kontrol at tumuon sa mga partikular na bahagi ng data na mayroon kang mga tanong tungkol dito. Ang [`query()` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) sa Pandas library ay nagbibigay-daan sa iyong pumili ng mga column at makatanggap ng mga simpleng sagot tungkol sa data sa pamamagitan ng mga row na nakuha.

## Pag-explore gamit ang Visualizations

Hindi mo kailangang maghintay hanggang ang data ay lubos na nalinis at nasuri bago magsimulang lumikha ng mga visualization. Sa katunayan, ang pagkakaroon ng visual na representasyon habang nag-eexplore ay makakatulong sa pagtukoy ng mga pattern, relasyon, at problema sa data. Bukod dito, ang mga visualization ay nagbibigay ng paraan ng komunikasyon sa mga hindi kasali sa pamamahala ng data at maaaring maging isang pagkakataon upang ibahagi at linawin ang mga karagdagang tanong na hindi natugunan sa yugto ng pagkuha. Tingnan ang [seksyon sa Visualizations](../../../../../../../../../3-Data-Visualization) upang matuto nang higit pa tungkol sa ilang mga popular na paraan ng pag-explore gamit ang biswal.

## Pag-explore upang Tukuyin ang mga Inconsistency

Ang lahat ng mga paksa sa araling ito ay makakatulong sa pagtukoy ng mga nawawala o hindi tugmang halaga, ngunit ang Pandas ay nagbibigay ng mga function upang suriin ang ilan sa mga ito. Ang [isna() o isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) ay maaaring suriin ang mga nawawalang halaga. Isang mahalagang bahagi ng pag-explore para sa mga halagang ito sa loob ng iyong data ay ang pag-alam kung bakit sila naging ganoon sa simula. Makakatulong ito sa iyong magpasya kung anong [mga aksyon ang dapat gawin upang malutas ang mga ito](../../../../../../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/29)

## Gawain

[Pag-explore para sa mga sagot](assignment.md)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.