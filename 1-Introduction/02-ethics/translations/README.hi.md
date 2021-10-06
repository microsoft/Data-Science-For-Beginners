# डेटा नैतिकता का परिचय

|![[(@sketchthedocs) द्वारा स्केचनोट](https://sketchthedocs.dev) ](../../../sketchnotes/02-Ethics.png)|
|:---:|
| डेटा विज्ञान नैतिकता - _[@nitya](https://twitter.com/nitya) द्वारा स्केचनोट_ |

---

हम सब इस डाटा-फाइड दुनिया में रहने वाले डाटा-नागरिक है | 

बाजार के रुझान यह दर्शाते हैं कि २०२२ तक, तीन में से एक बड़ी संस्था अपना डाटा कि खरीद और बेचना ऑनलाइन [दुकानों](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/) द्वारा करेंगी | **ऐप डेवलपर** के रूप में, हम डेटा-संचालित अंतर्दृष्टि और एल्गोरिथम-चालित स्वचालन को दैनिक उपयोगकर्ता अनुभवों में एकीकृत करना आसान और सस्ता पाएंगे। लेकिन जैसे-जैसे AI व्यापक होता जाएगा, हमें इस तरह के एल्गोरिदम के [हथियारीकरण](https://www.youtube.com/watch?v=TQHs8SA1qpk) से होने वाले संभावित नुकसान को भी समझना होगा ।

रुझान यह भी संकेत देते हैं कि हम २०२५ तक [180 zettabytes](https://www.statista.com/statistics/871513/worldwide-data-created/) डेटा का निर्माण और उपभोग करेंगे । **डेटा वैज्ञानिक** के रूप में, यह हमें व्यक्तिगत डेटा तक पहुंचने के लिये अभूतपूर्व स्तर प्रदान करता है । इसका मतलब है कि हम उपयोगकर्ताओं के व्यवहार संबंधी प्रोफाइल बना सकते हैं और निर्णय लेने को इस तरह से प्रभावित कर सकते हैं जो संभावित रूप से एक [मुक्त इच्छा का भ्रम](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) पैदा करता है जब्कि वह उपयोगकर्ताओं को हमारे द्वारा पसंद किए जाने वाले परिणामों की ओर आकर्षित करना । यह डेटा गोपनीयता और उपयोगकर्ता की सुरक्षा पर भी व्यापक प्रश्न उठाता है ।

डेटा नैतिकता अब डेटा विज्ञान और इंजीनियरिंग का  _आवश्यक रक्षक_ हैं, जिससे हमें अपने डेटा-संचालित कार्यों से संभावित नुकसान और अनपेक्षित परिणामों को नीचे रखने में मदद मिलती है । [AI के लिए गार्टनर हाइप साइकिल](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/) डिजिटल नैतिकता में उचित रुझानों की पहचान करता है AI के _democratization_ और _industrialization_ के आसपास बड़े मेगाट्रेंड के लिए प्रमुख ड्राइवर के रूप में जिम्मेदार AI की ज़िम्मेदारी और AI शासन ।


![AI के लिए गार्टनर का प्रचार चक्र - २०२०](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

इस पाठ में, हम डेटा नैतिकता के आकर्षक क्षेत्र के बारे में सीखेंगे  - मूल अवधारणाओं और चुनौतियों से लेकर केस-स्टडी और शासन जैसी एप्लाइड AI अवधारणाओं तक - जो डेटा और AI के साथ काम करने वाली समूह और संगठनों में नैतिकता संस्कृति स्थापित करने में मदद करते हैं ।

## [पाठ से पहले की प्रश्नोत्तरी](https://red-water-0103e7a0f.azurestaticapps.net/quiz/2) 🎯

## मूल परिभाषाएं

आइए बुनियादी शब्दावली को समझना शुरू करें ।

"नैतिकता" [ग्रीक शब्द "एथिकोस"](https://en.wikipedia.org/wiki/Ethics) (और इसकी जड़ "एथोस") से आया है जिसका अर्थ _चरित्र या नैतिक प्रकृति_ होता है ।

**नैतिकता** उन साझा मूल्यों और नैतिक सिद्धांतों के बारे में है जो समाज में हमारे व्यवहार को नियंत्रित करते हैं । नैतिकता कानूनों पर नहीं बल्कि "सही बनाम गलत" के व्यापक रूप से स्वीकृत मानदंड पर आधारित है । लेकिन , नैतिक विचार कॉर्पोरेट प्रशासन की पहल और अनुपालन के लिए अधिक प्रोत्साहन पैदा करने वाले सरकारी नियमों को प्रभावित कर सकते हैं ।

**डेटा नैतिकता** एक [नैतिकता की नई शाखा](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1) है जो "_डेटा, एल्गोरिदम और से संबंधित नैतिक समस्याओं का अध्ययन और मूल्यांकन करती है_" । यहां, **"डेटा"** - निर्माण, रिकॉर्डिंग, अवधि, प्रसंस्करण प्रसार, साझाकरण और उपयोग से संबंधित कार्यों पर केंद्रित है, **"एल्गोरिदम"** AI , एजेंटों, मशीन लर्निंग और रोबोटो पर केंद्रित है, और ** "अभ्यास"** जिम्मेदार नवाचार, प्रोग्रामिंग, हैकिंग और नैतिकता कोड जैसे विषयों पर केंद्रित है ।

**एप्लाइड नैतिकता** [नैतिक विचारों का व्यावहारिक अनुप्रयोग](https://en.wikipedia.org/wiki/Applied_ethics) है । यह _वास्तविक दुनिया की कार्रवाइयों, उत्पादों और प्रक्रियाओं_ के संदर्भ में नैतिक मुद्दों की सक्रिय रूप से जांच करने और सुधारात्मक उपाय करने की प्रक्रिया है ताकि ये हमारे परिभाषित नैतिक मूल्यों के साथ संरेखित रहें ।

**नैतिकता संस्कृति** यह सुनिश्चित करने के लिए [_operationalizing_ एप्लाइड नैतिकता](https://hbr.org/2019/05/how-to-design-an-ethical-organization) के बारे में है कि हमारे नैतिक सिद्धांतों और प्रथाओं को पूरे संगठन में एक सुसंगत और मापनीय तरीके से अपनाया जाए । सफल नैतिक संस्कृतियाँ संगठन-व्यापी नैतिक सिद्धांतों को परिभाषित करती हैं, अनुपालन के लिए सार्थक प्रोत्साहन प्रदान करती हैं, और संगठन के हर स्तर पर वांछित व्यवहारों को प्रोत्साहित और प्रवर्धित करके नैतिक मानदंडों को सुदृढ़ करती हैं ।


## नैतिकता की अवधारणाएं

इस खंड में, हम डेटा नैतिकता के लिए साझा मूल्यों (सिद्धांतों) और नैतिक चुनौतियों (समस्याओं) जैसी अवधारणाओं पर चर्चा करेंगे - और मामले के अध्ययन का पता लगाएंगे जो आपको वास्तविक दुनिया के संदर्भों में इन अवधारणाओं को समझने में मदद करते हैं ।

### 1. नैतिक सिद्धांत

प्रत्येक डेटा नैतिकता रणनीति _नैतिक सिद्धांतों_ को परिभाषित करके शुरू होती है - "साझा मूल्य" जो स्वीकार्य व्यवहारों का वर्णन करते हैं, और हमारे डेटा और AI परियोजनाओं में अनुपालन कार्यों का मार्गदर्शन करते हैं । लेकिन, अधिकांश बड़े संगठन इन्हें एक _नैतिक AI_ मिशन स्टेटमेंट या फ्रेमवर्क में रेखांकित करते हैं जो कॉर्पोरेट स्तर पर परिभाषित होता है और सभी टीमों में लगातार लागू होता है ।

**उदाहरण:** माइक्रोसॉफ्ट की [Responsible AI](https://www.microsoft.com/en-us/ai/responsible-ai) मिशन स्टेटमेंट कहती है : _"हम नैतिक सिद्धांतों द्वारा संचालित AI की उन्नति के लिए प्रतिबद्ध हैं जो लोगों को सबसे पहले रखते हैं |"_ - नीचे दिए गए ढांचे में 6 नैतिक सिद्धांतों की वार्ना की गयी है :

![माइक्रोसॉफ्ट की Responsible AI](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

आइए संक्षेप में इन सिद्धांतों के बारे में सीखे | _पारदर्शिता_ और _जवाबदेही_ वह मूलभूत मूल्य हैं जिन पर अन्य सिद्धांतों का निर्माण किया गया है - तो चलिए वहां शुरु करते हैं :

* [**जवाबदेही**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) उपयोगकर्ताओं को उनके डेटा और AI संचालन, और इन नैतिक सिद्धांतों के अनुपालन के लिए _जिम्मेदार_ बनाती है ।
* [**पारदर्शिता**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) सुनिश्चित करती है कि डेटा और AI क्रियाएं उपयोगकर्ताओं के लिए _समझने योग्य_ (व्याख्या योग्य) हैं, यह बताते हुए कि निर्णयों के पीछे क्या और क्यों है ।
* [**निष्पक्षता**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) - यह सुनिश्चित करने पर ध्यान केंद्रित करती है कि AI डेटा और सिस्टम में किसी भी प्रणालीगत या निहित सामाजिक-तकनीकी पूर्वाग्रहों को संबोधित करते हुए _सभी लोगों_ के साथ उचित व्यवहार करता है ।
* [**विश्वसनीयता और अहनिकारकता**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - सुनिश्चित करती है कि AI- संभावित नुकसान या अनपेक्षित परिणामों को कम करते हुए परिभाषित मूल्यों के साथ _लगातार_ काम करता है ।
* [**निजता एवं सुरक्षा**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - डेटा वंश को समझने, और उपयोगकर्ताओं को _डेटा गोपनीयता और संबंधित सुरक्षा_ प्रदान करने के बारे में है ।
* [**समग्रता**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - AI समाधानों को इरादे से डिजाइन करना एवं उन्हें _मानवीय आवश्यकताओं की एक विस्तृत श्रृंखला_ और क्षमताओं को पूरा करने के लिए अनुकूलित करने के बारे में है ।

> 🚨 अपने डेटा नैतिकता मिशन वक्तव्य के बारे में सोचें | अन्य संगठनों से नैतिक AI ढांचों का अन्वेषण करें - ये हैं कुछ उदाहरण [IBM](https://www.ibm.com/cloud/learn/ai-ethics), [Google](https://ai.google/principles) ,एवं [Facebook](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/) | इनके बीच क्या साझा मूल्य हैं? ये सिद्धांत उनके द्वारा संचालित AI उत्पाद या उद्योग से कैसे संबंधित हैं ?

### 2. नैतिकता से जुडी चुनौतियां

एक बार जब हमारे पास नैतिक सिद्धांत परिभाषित हो जाते हैं, तो अगला कदम यह देखने के लिए हमारे डेटा और एआई कार्यों का मूल्यांकन करना है कि क्या वे उन साझा मूल्यों के साथ संरेखित हैं । अपने कार्यों के बारे में दो श्रेणियों में सोचें: _डेटा संग्रह_ और _एल्गोरिदम डिज़ाइन_ | 

डेटा संग्रह के साथ, कार्रवाइयों में संभवतः पहचान योग्य जीवित व्यक्तियों के लिए **व्यक्तिगत डेटा** या व्यक्तिगत रूप से पहचान योग्य जानकारी शामिल होगी । इसमें [गैर-व्यक्तिगत डेटा के विविध आइटम] (https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en) शामिल हैं, जो _collectively_ किसी व्यक्ति की पहचान करते हैं । नैतिक चुनौतियां _डेटा गोपनीयता_, _डेटा स्वामित्व_, और उपयोगकर्ताओं के लिए _सूचित सहमति_ और _बौद्धिक संपदा अधिकार_ जैसे संबंधित विषयों से संबंधित हो सकती हैं ।

एल्गोरिथम डिज़ाइन के साथ, क्रियाओं में **डेटासेट** एकत्र करना और क्यूरेट करना शामिल होगा, फिर उनका उपयोग **डेटा मॉडल** को प्रशिक्षित और तैनात करने के लिए किया जाएगा जो वास्तविक दुनिया के संदर्भों में परिणामों की भविष्यवाणी या स्वचालित निर्णय लेते हैं । एल्गोरिथम डिज़ाइन के साथ, क्रियाओं में **डेटासेट** एकत्र करना और क्यूरेट करना शामिल होगा, फिर उनका उपयोग **डेटा मॉडल** को प्रशिक्षित और तैनात करने के लिए किया जाएगा जो वास्तविक दुनिया के संदर्भों में परिणामों की भविष्यवाणी या स्वचालित निर्णय लेते हैं ।

दोनों ही मामलों में, नैतिकता की चुनौतियाँ उन क्षेत्रों को उजागर करती हैं जहाँ हमारे कार्यों का हमारे साझा मूल्यों के साथ टकराव हो सकता है । इन चिंताओं का पता लगाने, सामना करने, कम करने या समाप्त करने के लिए - हमें अपने कार्यों से संबंधित नैतिक "हां या नहीं" प्रश्न पूछने की जरूरत है, फिर आवश्यकतानुसार सुधारात्मक कार्रवाई करें । आइए कुछ नैतिक चुनौतियों और उनके द्वारा उठाए गए नैतिक प्रश्नों पर एक नज़र डालें :


#### 2.1 डेटा स्वामित्व

डेटा संग्रह में अक्सर व्यक्तिगत डेटा शामिल होता है जो डेटा विषयों की पहचान कर सकता है । [डेटा स्वामित्व](https://permission.io/blog/data-ownership) _नियंत्रण_ के बारे में और उन [_उपयोगकर्ता अधिकारो_](https://permission.io/blog/data-ownership)के सम्भंदित है जो निर्माण , प्रसंस्करण और से संबंधित है । 

हमें जो नैतिक प्रश्न पूछने चाहिए, वे हैं : 
 * डेटा का मालिक कौन है ? (उपयोगकर्ता या संगठन)
 * डेटा विषयों के पास क्या अधिकार हैं ? (उदा: पहुंच, मिटाना, सुवाह्यता)
 * संगठनों के पास क्या अधिकार हैं ? (उदा: दुर्भावनापूर्ण उपयोगकर्ता समीक्षाओं का सुधार)

#### 2.2 सूचित सहमति

[सूचित सहमति](https://legaldictionary.net/informed-consent/) उद्देश्य, संभावित जोखिमों और विकल्पों सहित प्रासंगिक तथ्यों की _पूर्ण समझ_ के साथ कार्रवाई (जैसे डेटा संग्रह) के लिए सहमत होने वाले उपयोगकर्ताओं के कार्य को परिभाषित करता है । 

यहां देखने लायक प्रश्न हैं :
 * क्या उपयोगकर्ता (डेटा विषय) ने डेटा कैप्चर और उपयोग के लिए अनुमति दी थी ?
 * क्या उपयोगकर्ता को वह उद्देश्य समझ में आया जिसके लिए उस डेटा को कैप्चर किया गया था ?
 * क्या उपयोगकर्ता ने उनकी भागीदारी से संभावित जोखिमों को समझा ?

#### 2.3 बौद्धिक संपदा

[बौद्धिक संपदा](https://en.wikipedia.org/wiki/Intellectual_property) मानव पहल से उत्पन्न अमूर्त कृतियों को संदर्भित करता है, जिनका व्यक्तियों या व्यवसायों के लिए _आर्थिक_ महत्व हो सकता है ।

यहां देखने लायक प्रश्न हैं :
 * क्या जमा किए गए डेटा का किसी उपयोगकर्ता या व्यवसाय के लिए आर्थिक महत्व है ?
 * क्या **उपयोगकर्ता** के पास यहां बौद्धिक संपदा है ?
 * क्या **संगठन** के पास यहां बौद्धिक संपदा है ?
 * अगर ये अधिकार मौजूद हैं, तो हम उनकी रक्षा कैसे कर रहे हैं ?

#### 2.4 डाटा गोपनीयता

[डेटा गोपनीयता](https://www.northeaster.edu/graduate/blog/what-is-data-privacy/) या सूचना गोपनीयता व्यक्तिगत रूप से पहचान योग्य जानकारी के संबंध में उपयोगकर्ता की गोपनीयता के संरक्षण और उपयोगकर्ता की पहचान की सुरक्षा को संदर्भित करता है ।

यहां देखने लायक प्रश्न हैं :
 * क्या उपयोगकर्ताओं का (व्यक्तिगत) डेटा हैक और लीक से सुरक्षित है ?
 * क्या उपयोगकर्ताओं का डेटा केवल अधिकृत उपयोगकर्ताओं और संदर्भों के लिए सुलभ है ?
 * क्या डेटा साझा या प्रसारित होने पर उपयोगकर्ताओं की गोपनीयता बनी रहती है ?
 * क्या किसी उपयोगकर्ता की पहचान अज्ञात डेटासेट से की जा सकती है ?


#### 2.5 भूला दिया जाने का अधिकार

[भूला दिया जाने का अधिकार](https://en.wikipedia.org/wiki/Right_to_be_forgotten) अतिरिक्त सुविधाएं प्रदान करता है उपयोगकर्ताओं के लिए व्यक्तिगत डेटा सुरक्षा। विशेष रूप से, यह उपयोगकर्ताओं को इंटरनेट खोजों और अन्य स्थानों से व्यक्तिगत डेटा को हटाने या हटाने का अनुरोध करने का अधिकार देता है, _विशिष्ट परिस्थितियों में_ - उन्हें उनके खिलाफ पिछली कार्रवाई किए बिना ऑनलाइन एक नई शुरुआत करने की अनुमति देता है ।

यहां देखने लायक प्रश्न हैं :
 * Does the system allow data subjects to request erasure?
 * Should the withdrawal of user consent trigger automated erasure?
 * Was data collected without consent or by unlawful means?
 * Are we compliant with government regulations for data privacy?


#### 2.6 Dataset Bias

Dataset or [Collection Bias](http://researcharticles.com/index.php/bias-in-data-collection-in-research/) is about selecting a _non-representative_ subset of data for algorithm development, creating potential  unfairness in result outcomes for diverse groups. Types of bias include selection or sampling bias, volunteer bias, and instrument bias. 

Questions to explore here are:
 * Did we recruit a representative set of data subjects?
 * Did we test our collected or curated dataset for various biases?
 * Can we mitigate or remove any discovered biases?

#### 2.7 Data Quality

[Data Quality](https://lakefs.io/data-quality-testing/) looks at the validity of the curated dataset used to develop our algorithms, checking to see if features and records meet requirements for the level of accuracy and consistency needed for our AI purpose.

Questions to explore here are:
 * Did we capture valid _features_ for our use case?
 * Was data captured _consistently_ across diverse data sources?
 * Is the dataset _complete_ for diverse conditions or scenarios?
 * Is information captured _accurately_ in reflecting reality?

#### 2.8 Algorithm Fairness

[Algorithm Fairness](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f) checks to see if the algorithm design systematically discriminates against specific subgroups of data subjects leading to [potential harms](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml) in _allocation_ (where resources are denied or withheld from that group) and _quality of service_ (where AI is not as accurate for some subgroups as it is for others). 

Questions to explore here are:
 * Did we evaluate model accuracy for diverse subgroups and conditions?
 * Did we scrutinize the system for potential harms (e.g., stereotyping)?
 * Can we revise data or retrain models to mitigate identified harms?

Explore resources like [AI Fairness checklists](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA) to learn more.

#### 2.9 Misrepresentation

[Data Misrepresentation](https://www.sciencedirect.com/topics/computer-science/misrepresentation) is about asking whether we are communicating insights from honestly reported data in a deceptive manner to support a desired narrative. 

Questions to explore here are:
 * Are we reporting incomplete or inaccurate data?
 * Are we visualizing data in a manner that drives misleading conclusions?
 * Are we using selective statistical techniques to manipulate outcomes?
 * Are there alternative explanations that may offer a different conclusion?

#### 2.10 Free Choice
The [Illusion of Free Choice](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) occurs when system "choice architectures" use decision-making algorithms to nudge people towards taking a preferred outcome while seeming to give them options and control. These [dark patterns](https://www.darkpatterns.org/) can cause social and economic harm to users. Because user decisions impact behavior profiles, these actions potentially drive future choices that can amplify or extend the impact of these harms.

Questions to explore here are:
 * Did the user understand the implications of making that choice?
 * Was the user aware of (alternative) choices and the pros & cons of each?
 * Can the user reverse an automated or influenced choice later?

### 3. Case Studies

To put these ethical challenges in real-world contexts, it helps to look at case studies that highlight the potential harms and consequences to individuals and society, when such ethics violations are overlooked. 

Here are a few examples:

| Ethics Challenge | Case Study  | 
|--- |--- |
| **Informed Consent** | 1972 - [Tuskegee Syphillis Study](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - African American men who participated in the study were promised free medical care _but deceived_ by researchers who failed to inform subjects of their diagnosis or about availability of treatment. Many subjects died & partners or children were affected; the study lasted 40 years. | 
| **Data Privacy** |  2007 - The [Netflix data prize](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) provided researchers with _10M anonymized movie rankings from 50K customers_ to help improve recommendation algorithms. However, researchers were able to correlate anonymized data with personally-identifiable data in _external datasets_ (e.g., IMDb comments) - effectively "de-anonymizing" some Netflix subscribers.|
| **Collection Bias**  | 2013 - The City of Boston [developed Street Bump](https://www.boston.gov/transportation/street-bump), an app that let citizens report potholes, giving the city better roadway data to find and fix issues. However, [people in lower income groups had less access to cars and phones](https://hbr.org/2013/04/the-hidden-biases-in-big-data), making their roadway issues invisible in this app. Developers worked with academics to _equitable access and digital divides_ issues for fairness. |
| **Algorithmic Fairness**  | 2018 - The MIT [Gender Shades Study](http://gendershades.org/overview.html) evaluated the accuracy of gender classification AI products, exposing gaps in accuracy for women and persons of color. A [2019 Apple Card](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/) seemed to offer less credit to women than men. Both illustrated issues in algorithmic bias leading to socio-economic harms.|
| **Data Misrepresentation** | 2020 - The [Georgia Department of Public Health released COVID-19 charts](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening) that appeared to mislead citizens about trends in confirmed cases with non-chronological ordering on the x-axis. This illustrates misrepresentation through visualization tricks. |
| **Illusion of free choice** | 2020 - Learning app [ABCmouse paid $10M to settle an FTC complaint](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/) where parents were trapped into paying for subscriptions they couldn't cancel. This illustrates dark patterns in choice architectures, where users were nudged towards potentially harmful choices. |
| **Data Privacy & User Rights** | 2021 - Facebook [Data Breach](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users) exposed data from 530M users, resulting in a $5B settlement to the FTC. It however refused to notify users of the breach violating user rights around data transparency and access. |

Want to explore more case studies? Check out these resources:
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - ethics dilemmas across diverse industries. 
* [Data Science Ethics course](https://www.coursera.org/learn/data-science-ethics#syllabus) - landmark case studies explored.
* [Where things have gone wrong](https://deon.drivendata.org/examples/) - deon checklist with examples

> 🚨 Think about the case studies you've seen - have you experienced, or been affected by, a similar ethical challenge in your life? Can you think of at least one other case study that illustrates one of the ethical challenges we've discussed in this section?

## Applied Ethics

We've talked about ethics concepts, challenges ,and case studies in real-world contexts. But how do we get started _applying_ ethical principles and practices in our projects? And how do we _operationalize_ these practices for better governance? Let's explore some real-world solutions: 

### 1. Professional Codes

Professional Codes offer one option for organizations to "incentivize" members to support their ethical principles and mission statement. Codes are _moral guidelines_ for professional behavior, helping employees or members make decisions that align with their organization's principles. They are only as good as the voluntary compliance from members; however, many organizations offer additional rewards and penalties to motivate compliance from members.

Examples include:

 * [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/) Code of Ethics
 * [Data Science Association](http://datascienceassn.org/code-of-conduct.html) Code of Conduct (created 2013)
 * [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics) (since 1993)

> 🚨 Do you belong to a professional engineering or data science organization? Explore their site to see if they define a professional code of ethics. What does this say about their ethical principles? How are they "incentivizing" members to follow the code?

### 2. Ethics Checklists

While professional codes define required _ethical behavior_ from practitioners, they [have known limitations](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) in enforcement, particularly in large-scale projects. Instead, many data Science experts [advocate for checklists](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md), that can **connect principles to practices** in more deterministic and actionable ways. 

Checklists convert questions into "yes/no" tasks that can be operationalized, allowing them to be tracked as part of standard product release workflows. 

Examples include:
 * [Deon](https://deon.drivendata.org/) - a general-purpose data ethics checklist created from [industry recommendations](https://deon.drivendata.org/#checklist-citations) with a command-line tool for easy integration.
 * [Privacy Audit Checklist](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - provides general guidance for information handling practices from legal and social exposure perspectives.
 * [AI Fairness Checklist](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - created by AI practitioners to support the adoption and integration of fairness checks into AI development cycles.
 * [22 questions for ethics in data and AI](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - more open-ended framework, structured for initial exploration of ethical issues in design, implementation, and organizational, contexts.

### 3. Ethics Regulations

Ethics is about defining shared values and doing the right thing _voluntarily_. **Compliance** is about _following the law_ if and where defined. **Governance** broadly covers all the ways in which organizations operate to enforce ethical principles and comply with established laws.

Today, governance takes two forms within organizations. First, it's about defining **ethical AI** principles and establishing practices to operationalize adoption across all AI-related projects in the organization. Second, it's about complying with all government-mandated **data protection regulations** for regions it operates in.

Examples of data protection and privacy regulations:

 * `1974`, [US Privacy Act](https://www.justice.gov/opcl/privacy-act-1974) - regulates _federal govt._ collection, use ,and disclosure of personal information.
 * `1996`, [US Health Insurance Portability & Accountability Act (HIPAA)](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - protects personal health data.
 * `1998`, [US Children's Online Privacy Protection Act (COPPA)](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - protects data privacy of children under 13.
 * `2018`, [General Data Protection Regulation (GDPR)](https://gdpr-info.eu/) - provides user rights, data protection ,and privacy.
 * `2018`, [California Consumer Privacy Act (CCPA)](https://www.oag.ca.gov/privacy/ccpa) gives consumers more _rights_ over their (personal) data.
 * `2021`, China's [Personal Information Protection Law](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) just passed, creating one of the strongest online data privacy regulations worldwide.

> 🚨 The European Union defined GDPR (General Data Protection Regulation) remains one of the most influential data privacy regulations today. Did you know it also defines [8 user rights](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr) to protect citizens' digital privacy and personal data? Learn about what these are, and why they matter.


### 4. Ethics Culture

Note that there remains an intangible gap between _compliance_ (doing enough to meet "the letter of the law") and addressing [systemic issues](https://www.coursera.org/learn/data-science-ethics/home/week/4) (like ossification, information asymmetry ,and distributional unfairness) that can speed up the weaponization of AI. 

The latter requires [collaborative approaches to defining ethics cultures](https://towardsdatascience.com/why-ai-ethics-requires-a-culture-driven-approach-26f451afa29f) that build emotional connections and consistent shared values _across organizations_ in the industry. This calls for more [formalized data ethics cultures](https://www.codeforamerica.org/news/formalizing-an-ethical-data-culture/) in organizations - allowing _anyone_ to [pull the Andon cord](https://en.wikipedia.org/wiki/Andon_(manufacturing)) (to raise ethics concerns early in the process) and making _ethical assessments_ (e.g., in hiring) a core criteria team formation in AI projects.

---
## [Post-lecture quiz](https://red-water-0103e7a0f.azurestaticapps.net/quiz/3) 🎯
## Review & Self Study 

Courses and books help with understanding core ethics concepts and challenges, while case studies and tools help with applied ethics practices in real-world contexts. Here are a few resources to start with.

* [Machine Learning For Beginners](https://github.com/microsoft/ML-For-Beginners/blob/main/1-Introduction/3-fairness/README.md) - lesson on Fairness, from Microsoft.
* [Principles of Responsible AI](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - free learning path from Microsoft Learn.
* [Ethics and Data Science](https://resources.oreilly.com/examples/0636920203964) - O'Reilly EBook (M. Loukides, H. Mason et. al)
* [Data Science Ethics](https://www.coursera.org/learn/data-science-ethics#syllabus) - online course from the University of Michigan.
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - case studies from the University of Texas.

# Assignment 

[Write A Data Ethics Case Study](assignment.md)
